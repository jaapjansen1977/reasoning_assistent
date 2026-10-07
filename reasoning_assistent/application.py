"""Regelt de samenwerking; heeft geen kennis van vensters of AI-modellen."""
from .domain import Analysis, Consultation, Fact, Status
from .ports import FactExtractor, Reasoner


class ConsultationService:
    def __init__(self, extractor: FactExtractor, reasoner: Reasoner):
        self.extractor = extractor
        self.reasoner = reasoner

    def analyze(self, transcript: str) -> Analysis:
        consultation = Consultation(transcript)
        for fact in self.extractor.extract(transcript):
            if fact.subject != "patient" or fact.period != "current":
                continue
            previous = consultation.facts.get(fact.topic)
            if previous and previous.status != fact.status:
                fact = Fact(fact.topic, Status.UNCLEAR,
                            previous.evidence + " / " + fact.evidence)
            consultation.facts[fact.topic] = fact
        return Analysis(consultation, self.reasoner.suggest(consultation))
