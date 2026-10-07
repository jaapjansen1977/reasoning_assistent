"""Provider-independent output contract for the fictional question prototype."""
from typing import Protocol


class AIError(ValueError):
    """Safe user-facing error; never includes remote payloads or credentials."""


class AnalysisBackend(Protocol):
    def generate(self, instructions: str, payload: dict, schema: dict) -> dict: ...


def output_schema(question_ids: list[str]) -> dict:
    def obj(properties):
        return {'type': 'object', 'properties': properties,
                'required': list(properties), 'additionalProperties': False}
    text = {'type': 'string'}
    topic = {'type': 'string', 'enum': question_ids}
    fact = obj({
        'question_id': topic,
        'state': {'type': 'string', 'enum': ['present', 'denied', 'unclear']},
        'quote': text,
        'speaker': {'type': 'string', 'enum': ['patient', 'therapist', 'unknown']},
        'subject': {'type': 'string', 'enum': ['patient', 'other', 'unknown']},
        'time_context': {'type': 'string', 'enum': ['new', 'worsening', 'stable_existing', 'historical', 'unknown']},
    })
    focus = obj({'question_id': topic, 'reason': text})
    return obj({'facts': {'type': 'array', 'items': fact},
                'focus_questions': {'type': 'array', 'items': focus},
                'uncertainties': {'type': 'array', 'items': text}})
