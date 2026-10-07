"""Responses API adapter using Python stdlib; no SDK/install required."""
import json
import socket
from urllib import error, request
from .contracts import AIError

DEFAULT_MODEL = 'gpt-4.1-mini'
ENDPOINT = 'https://api.openai.com/v1/responses'
MAX_RESPONSE_BYTES = 2_000_000


class _NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Never forward bearer credentials to a redirect destination.
        return None


class OpenAIBackend:
    def __init__(self, api_key: str, model: str = DEFAULT_MODEL, *, timeout: float = 45):
        self._key = api_key.strip()
        self.model = model.strip()
        self.timeout = timeout
        if not self._key or '\n' in self._key or '\r' in self._key:
            raise AIError('Vul een geldige API-sleutel in; deel deze niet in GitHub of chat.')
        if not self.model or len(self.model) > 120 or any(c.isspace() for c in self.model):
            raise AIError('Vul een geldige modelnaam in.')

    def generate(self, instructions: str, payload: dict, schema: dict) -> dict:
        body = {
            'model': self.model, 'instructions': instructions,
            'input': json.dumps(payload, ensure_ascii=False),
            'text': {'format': {'type': 'json_schema', 'name': 'fictional_consult',
                                'strict': True, 'schema': schema}},
            'store': False, 'max_output_tokens': 3000,
        }
        req = request.Request(ENDPOINT, data=json.dumps(body).encode('utf-8'),
                              headers={'Authorization': 'Bearer ' + self._key,
                                       'Content-Type': 'application/json'}, method='POST')
        try:
            opener = request.build_opener(_NoRedirect())
            with opener.open(req, timeout=self.timeout) as response:
                raw = response.read(MAX_RESPONSE_BYTES + 1)
        except error.HTTPError as exc:
            messages = {
                400: 'API-aanvraag geweigerd. Controleer modelondersteuning voor Responses/Structured Outputs.',
                401: 'API-sleutel niet geaccepteerd. Controleer de sleutel.',
                403: 'Geen toegang: controleer account-, model- en netwerktoestemming.',
                404: 'Model of endpoint niet beschikbaar voor dit account.',
                429: 'Limiet of API-tegoed bereikt. Controleer API-billing en probeer later opnieuw.',
            }
            code = exc.code
            exc.close()
            raise AIError(messages.get(code, f'AI-dienst gaf HTTP {code}; probeer later opnieuw.')) from None
        except (TimeoutError, socket.timeout):
            raise AIError('AI-aanvraag duurde te lang. Er is niet automatisch opnieuw verstuurd.') from None
        except (error.URLError, OSError):
            raise AIError('Geen verbinding met AI. Controleer internet, werkproxy en certificaten; schakel beveiliging niet uit.') from None
        if len(raw) > MAX_RESPONSE_BYTES:
            raise AIError('AI-antwoord is te groot; niet gebruikt.')
        try:
            envelope = json.loads(raw)
            if not isinstance(envelope, dict) or envelope.get('status') != 'completed':
                raise AIError('AI-antwoord is onvolledig of mislukt; geen resultaat gebruikt.')
            texts = []
            for item in envelope.get('output', []):
                if item.get('type') == 'message' and item.get('role') == 'assistant':
                    for content in item.get('content', []):
                        if content.get('type') == 'refusal':
                            raise AIError('AI heeft de aanvraag geweigerd; geen resultaat gebruikt.')
                        if content.get('type') == 'output_text':
                            texts.append(content['text'])
            parsed = json.loads(''.join(texts))
            if not isinstance(parsed, dict):
                raise AIError('AI gaf geen geldig analyseobject terug.')
            return parsed
        except (ValueError, TypeError, KeyError, AttributeError) as exc:
            if isinstance(exc, AIError):
                raise
            raise AIError('AI gaf een ongeldig antwoord; geen resultaat gebruikt.') from None
