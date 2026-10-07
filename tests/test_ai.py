"""Offline contract and network-boundary tests; no paid API calls."""
import copy
import io
import json
import unittest
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError, URLError

from reasoning_assistent.ai.contracts import AIError
from reasoning_assistent.ai.openai_backend import OpenAIBackend, _NoRedirect
from reasoning_assistent.ai.service import AIConsultationService, MAX_TRANSCRIPT_CHARS
from reasoning_assistent.knowledge.loader import load_low_back_module

TEXT = 'Patiënt: Mijn moeder had vorig jaar rugpijn. Ik heb nu geen tintelingen.'


def output():
    return {
        'facts': [{'question_id': 'leg', 'state': 'denied', 'quote': 'Ik heb nu geen tintelingen.',
                   'speaker': 'patient', 'subject': 'patient', 'time_context': 'unknown'}],
        'focus_questions': [{'question_id': 'onset', 'reason': 'Het begin van de actuele klacht is nog onduidelijk.'}],
        'uncertainties': ['Niet alle veiligheidsvragen zijn besproken.'],
    }


class FakeBackend:
    def __init__(self, result=None):
        self.result = output() if result is None else result
        self.calls = []

    def generate(self, instructions, payload, schema):
        self.calls.append((instructions, payload, schema))
        return copy.deepcopy(self.result)


class AIServiceTests(unittest.TestCase):
    def setUp(self):
        self.module = load_low_back_module()
        self.backend = FakeBackend()
        self.service = AIConsultationService(self.backend, self.module)

    def test_gate_empty_and_oversized_input_do_not_call_backend(self):
        for text, fictional in [(TEXT, False), (' ', True), ('x' * (MAX_TRANSCRIPT_CHARS + 1), True)]:
            with self.assertRaises(AIError):
                self.service.analyze(text, fictional=fictional)
        self.assertEqual(self.backend.calls, [])

    def test_questions_and_sources_are_resolved_locally(self):
        result = self.service.analyze(TEXT, fictional=True)
        self.assertEqual(result.suggestions[0].question, self.module['questions'][0]['text'])
        self.assertEqual(self.backend.calls[0][1]['transcript_untrusted_data'], TEXT)
        self.assertEqual(result.facts[0]['quote'], 'Ik heb nu geen tintelingen.')

    def test_invented_quote_rejects_whole_result(self):
        self.backend.result['facts'][0]['quote'] = 'Ik heb normale reflexen.'
        with self.assertRaisesRegex(AIError, 'citaat'):
            self.service.analyze(TEXT, fictional=True)

    def test_unknown_question_and_extra_diagnostic_field_are_rejected(self):
        self.backend.result['focus_questions'][0]['question_id'] = 'diagnose_discushernia'
        with self.assertRaises(AIError):
            self.service.analyze(TEXT, fictional=True)
        self.backend.result = output()
        self.backend.result['diagnosis'] = 'certain'
        with self.assertRaises(AIError):
            self.service.analyze(TEXT, fictional=True)

    def test_therapist_historical_and_other_subject_quotes_remain_labeled(self):
        quote = 'Mijn moeder had vorig jaar rugpijn.'
        self.backend.result['facts'] = [
            {'question_id': 'history', 'state': 'present', 'quote': quote,
             'speaker': 'patient', 'subject': 'other', 'time_context': 'historical'},
            {'question_id': 'leg', 'state': 'unclear', 'quote': 'Ik heb nu geen tintelingen.',
             'speaker': 'unknown', 'subject': 'unknown', 'time_context': 'unknown'},
        ]
        result = self.service.analyze(TEXT, fictional=True)
        self.assertEqual(result.facts[0]['subject'], 'other')
        self.assertEqual(result.facts[0]['time_context'], 'historical')
        self.assertEqual(result.facts[1]['speaker'], 'unknown')
        # Labels are preserved proposals, not automatically converted to
        # confirmed current patient facts or used to dismiss missing questions.
        self.assertEqual(len(result.suggestions), 1)

    def test_wrong_types_and_duplicate_questions_fail_closed(self):
        for change in [lambda d: d.update(facts='not a list'),
                       lambda d: d['focus_questions'].append(copy.deepcopy(d['focus_questions'][0])),
                       lambda d: d['facts'][0].update(state=['denied'])]:
            self.backend.result = output()
            change(self.backend.result)
            with self.assertRaises(AIError):
                self.service.analyze(TEXT, fictional=True)

    def test_local_backend_can_use_same_contract(self):
        result = AIConsultationService(FakeBackend(), self.module).analyze(TEXT, fictional=True)
        self.assertEqual(result.region, 'low_back')
        self.assertEqual(result.knowledge_version, self.module['version'])


class OpenAIAdapterTests(unittest.TestCase):
    def envelope(self, data=None, **extra):
        return {'status': 'completed', 'output': [
            {'type': 'reasoning', 'summary': []},
            {'type': 'message', 'role': 'assistant', 'content': [
                {'type': 'output_text', 'text': json.dumps(output() if data is None else data)}]}], **extra}

    def opener(self, envelope):
        response = MagicMock()
        response.read.return_value = json.dumps(envelope).encode()
        opener = MagicMock()
        opener.open.return_value.__enter__.return_value = response
        return opener

    def test_request_is_text_only_store_false_no_retries_and_nested_output_is_parsed(self):
        opener = self.opener(self.envelope())
        with patch('reasoning_assistent.ai.openai_backend.request.build_opener', return_value=opener):
            result = OpenAIBackend('fake-key-for-tests').generate('instructions', {'transcript_untrusted_data': TEXT}, {'type': 'object'})
        req = opener.open.call_args.args[0]
        body = json.loads(req.data)
        self.assertEqual(req.full_url, 'https://api.openai.com/v1/responses')
        self.assertEqual(req.method, 'POST')
        self.assertIs(body['store'], False)
        self.assertEqual(json.loads(body['input']), {'transcript_untrusted_data': TEXT})
        self.assertNotIn('tools', body)
        self.assertEqual(opener.open.call_count, 1)
        self.assertEqual(result, output())

    def test_refusal_incomplete_and_malformed_response_are_not_results(self):
        cases = [self.envelope(status='incomplete'),
                 {'status': 'completed', 'output': [{'type': 'message', 'role': 'assistant', 'content': [{'type': 'refusal', 'refusal': 'no'}]}]},
                 {'status': 'completed', 'output': []},
                 {'status': 'completed', 'output': [None]}]
        for envelope in cases:
            with self.subTest(envelope=envelope):
                with patch('reasoning_assistent.ai.openai_backend.request.build_opener', return_value=self.opener(envelope)):
                    with self.assertRaises(AIError):
                        OpenAIBackend('fake-key').generate('', {}, {})

    def test_http_and_network_errors_hide_provider_content_and_key(self):
        for exception in [HTTPError('https://api.openai.com', 401, 'fake-key secret transcript', {}, io.BytesIO(b'sensitive')),
                          URLError('fake-key secret transcript'), TimeoutError('fake-key')]:
            opener = MagicMock()
            opener.open.side_effect = exception
            with patch('reasoning_assistent.ai.openai_backend.request.build_opener', return_value=opener):
                with self.assertRaises(AIError) as raised:
                    OpenAIBackend('fake-key').generate('', {}, {})
            self.assertNotIn('fake-key', str(raised.exception))
            self.assertNotIn('secret transcript', str(raised.exception))
            self.assertEqual(opener.open.call_count, 1)

    def test_redirect_cannot_forward_bearer_credentials(self):
        self.assertIsNone(_NoRedirect().redirect_request(None, None, 302, '', {}, 'https://other.example'))

    def test_invalid_key_rejected_before_network(self):
        with patch('reasoning_assistent.ai.openai_backend.request.build_opener') as network:
            for key in ['', 'key\nInjected: header']:
                with self.assertRaises(AIError):
                    OpenAIBackend(key)
            network.assert_not_called()


if __name__ == '__main__':
    unittest.main()
