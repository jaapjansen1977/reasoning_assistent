import unittest
from reasoning_assistent.bootstrap import build_service
from reasoning_assistent.domain import Status
from reasoning_assistent.audio.transcription import NotConfiguredTranscriber


class ConsultationTests(unittest.TestCase):
    def setUp(self):
        self.service = build_service()

    def ids(self, text):
        return {s.id for s in self.service.analyze(text).suggestions}

    def test_empty_consult_has_three_demo_questions(self):
        self.assertEqual(len(self.ids('')), 3)

    def test_denied_is_not_missing(self):
        self.assertNotIn('question_beperkingen', self.ids(
            'beperkingen | ontkend | Ik ervaar geen beperkingen.'))

    def test_unclear_keeps_evidence(self):
        result = self.service.analyze('beloop | onduidelijk | Ik weet het niet.')
        suggestion = next(s for s in result.suggestions if s.id == 'question_beloop')
        self.assertIn('Ik weet het niet.', suggestion.reason)

    def test_other_subject_does_not_fill_patient_fact(self):
        self.assertIn('question_beperkingen', self.ids(
            'beperkingen | aanwezig | Mijn moeder kan niet lopen. | moeder | current'))

    def test_past_does_not_fill_current_fact(self):
        self.assertIn('question_beperkingen', self.ids(
            'beperkingen | aanwezig | Vroeger kon ik niet lopen. | patient | past'))

    def test_conflict_is_unclear(self):
        result = self.service.analyze(
            'beperkingen | aanwezig | Ik kan niet lopen.\n'
            'beperkingen | ontkend | Geen beperkingen.')
        self.assertEqual(result.consultation.facts['beperkingen'].status, Status.UNCLEAR)
        self.assertIn('question_beperkingen', {s.id for s in result.suggestions})

    def test_new_consult_does_not_inherit_previous_facts(self):
        self.service.analyze('hulpvraag | aanwezig | Ik wil tuinieren.')
        self.assertEqual(len(self.ids('')), 3)

    def test_unstructured_text_is_not_guessed(self):
        result = self.service.analyze('Mijn vader heeft rugpijn, ik niet.')
        self.assertEqual(result.consultation.facts, {})
        self.assertEqual(result.consultation.transcript, 'Mijn vader heeft rugpijn, ik niet.')

    def test_bad_status_is_reported(self):
        with self.assertRaises(ValueError):
            self.service.analyze('beloop | onbekend | iets')

    def test_no_demo_is_presented_as_reviewed_advice(self):
        for item in self.service.analyze('').suggestions:
            self.assertFalse(item.source.clinically_reviewed)
            self.assertEqual(item.category, 'doorvragen_demo')

    def test_audio_fails_explicitly_until_configured(self):
        with self.assertRaises(NotImplementedError):
            NotConfiguredTranscriber().transcribe('example.wav')


if __name__ == '__main__':
    unittest.main()
