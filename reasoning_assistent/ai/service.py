"""Validate model output and connect it to controlled questions locally."""
from dataclasses import dataclass
from .contracts import AIError, AnalysisBackend, output_schema
from .prompts import INSTRUCTIONS, knowledge_payload

MAX_TRANSCRIPT_CHARS = 16_000


@dataclass(frozen=True)
class QuestionSuggestion:
    id: str
    question: str
    reason: str
    priority: str
    sources: tuple[str, ...]


@dataclass(frozen=True)
class AIAnalysis:
    facts: tuple[dict, ...]
    suggestions: tuple[QuestionSuggestion, ...]
    uncertainties: tuple[str, ...]
    region: str
    knowledge_version: str


def _object(value, fields):
    if not isinstance(value, dict) or set(value) != set(fields):
        raise AIError('AI-antwoord heeft onverwachte velden; geen resultaat gebruikt.')


def _string(value, *, nonempty=True, maxlen=2000):
    if not isinstance(value, str) or len(value) > maxlen or (nonempty and not value.strip()):
        raise AIError('AI-antwoord bevat ongeldige tekst; geen resultaat gebruikt.')


def validate_output(data: dict, transcript: str, question_ids: set[str]) -> None:
    _object(data, ['facts', 'focus_questions', 'uncertainties'])
    for field in data:
        if not isinstance(data[field], list) or len(data[field]) > 100:
            raise AIError('AI-antwoord bevat een ongeldige lijst; geen resultaat gebruikt.')
    for fact in data['facts']:
        _object(fact, ['question_id', 'state', 'quote', 'speaker', 'subject', 'time_context'])
        for field in fact:
            _string(fact[field])
        if (fact['question_id'] not in question_ids or
            fact['state'] not in ['present', 'denied', 'unclear'] or
            fact['speaker'] not in ['patient', 'therapist', 'unknown'] or
            fact['subject'] not in ['patient', 'other', 'unknown'] or
            fact['time_context'] not in ['new', 'worsening', 'stable_existing', 'historical', 'unknown']):
            raise AIError('AI-antwoord bevat onbekende IDs of toestanden; geen resultaat gebruikt.')
        if fact['quote'] not in transcript:
            raise AIError('Een AI-citaat komt niet letterlijk in de invoer voor; controleer en probeer opnieuw.')
    seen = set()
    for focus in data['focus_questions']:
        _object(focus, ['question_id', 'reason'])
        _string(focus['question_id'])
        _string(focus['reason'])
        if focus['question_id'] not in question_ids or focus['question_id'] in seen:
            raise AIError('AI-vraagselectie bevat onbekende of dubbele IDs; geen resultaat gebruikt.')
        seen.add(focus['question_id'])
    for uncertainty in data['uncertainties']:
        _string(uncertainty)


class AIConsultationService:
    def __init__(self, backend: AnalysisBackend, module: dict):
        self.backend = backend
        self.module = module
        self.questions = {q['id']: q for q in module['questions']}
        self.sources = {s['id']: s for s in module['sources']}

    def analyze(self, transcript: str, *, fictional: bool = False) -> AIAnalysis:
        if fictional is not True:
            raise AIError('Deze online proef is uitsluitend voor fictieve gesprekken.')
        if not isinstance(transcript, str) or not transcript.strip():
            raise AIError('Voeg eerst een fictief gesprek toe.')
        if len(transcript) > MAX_TRANSCRIPT_CHARS:
            raise AIError(f'Maximaal {MAX_TRANSCRIPT_CHARS} tekens per proef; kies een korter gesprek.')
        data = self.backend.generate(INSTRUCTIONS, knowledge_payload(self.module, transcript),
                                     output_schema(list(self.questions)))
        validate_output(data, transcript, set(self.questions))
        # Model interpretation remains a proposal. Even an explicit fact does not
        # automatically suppress a compound follow-up question or a safety topic.
        suggestions = []
        for focus in data['focus_questions']:
            q = self.questions[focus['question_id']]
            refs = tuple(f"{self.sources[s]['title']} — {self.sources[s]['url']}"
                         for s in q['source_ids'])
            suggestions.append(QuestionSuggestion(q['id'], q['text'], focus['reason'],
                                                   q['priority'], refs))
        return AIAnalysis(tuple(data['facts']), tuple(suggestions), tuple(data['uncertainties']),
                          self.module['id'], self.module['version'])


def format_analysis(result: AIAnalysis) -> str:
    labels = {'present': 'expliciet genoemd', 'denied': 'expliciet ontkend', 'unclear': 'onduidelijk'}
    lines = [f'FICTIEVE PROEF — {result.region}, kennisversie {result.knowledge_version}',
             'AI-interpretatie controleren. Geen diagnose of beoordeling van klinische veiligheid.',
             '', 'Voorgestelde informatie-extractie:']
    for fact in result.facts:
        lines.extend([f"- {fact['question_id']}: {labels[fact['state']]} "
                      f"({fact['speaker']}, onderwerp {fact['subject']}, {fact['time_context']})",
                      f"  Citaat: {fact['quote']}"])
    if not result.facts:
        lines.append('Geen expliciete informatie herkend; dat betekent niet dat alle onderwerpen ontkend zijn.')
    lines.extend(['', 'Relevante vervolgvragen ter beoordeling:'])
    for suggestion in result.suggestions:
        lines.extend(['', suggestion.question, 'Waarom (AI): ' + suggestion.reason,
                      'Vraag-ID: ' + suggestion.id,
                      'Bronnen: ' + ('; '.join(suggestion.sources) or 'Eigen contextvraag uit de conceptkennisbank.')])
    if not result.suggestions:
        lines.append('Geen vervolgvragen voorgesteld. Dit betekent niet dat het gesprek volledig of veilig is.')
    lines.extend(['', 'Onzekerheden en beperkingen:'])
    lines.extend('- ' + value for value in result.uncertainties)
    lines.append('- Letterlijke citaten en geldige IDs zijn technisch gecontroleerd; de betekenis, spreker en volledigheid blijven door een mens te controleren.')
    return '\n'.join(lines)
