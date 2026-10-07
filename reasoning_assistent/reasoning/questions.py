"""Demonstratie van ontbrekende/ondubbelzinnige consultinformatie."""
from ..domain import Consultation, Status, Suggestion
from ..knowledge.loader import QuestionRule


class MissingInformationReasoner:
    def __init__(self, rules: tuple[QuestionRule, ...]):
        self.rules = rules

    def suggest(self, consultation: Consultation) -> tuple[Suggestion, ...]:
        suggestions = []
        for rule in self.rules:
            fact = consultation.facts.get(rule.topic)
            status = fact.status if fact else Status.NOT_DISCUSSED
            if status not in (Status.NOT_DISCUSSED, Status.UNCLEAR):
                continue
            reason = (f"Informatie onduidelijk: {fact.evidence}" if fact and status == Status.UNCLEAR
                      else "Nog geen expliciete, actuele informatie over de patiënt vastgelegd.")
            suggestions.append(Suggestion(rule.id, "doorvragen_demo", rule.question, reason, rule.source))
        return tuple(suggestions)
