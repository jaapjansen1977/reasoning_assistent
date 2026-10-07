"""Expliciete DEMO-invoer; dit is geen AI of vrije-taalinterpretatie.

Formaat per regel: onderwerp | status | bewijs | persoon | periode.
Persoon en periode zijn optioneel, standaard patient en current.
"""
from ..domain import Fact, Status


class StructuredFactExtractor:
    def extract(self, transcript: str) -> list[Fact]:
        facts = []
        for number, line in enumerate(transcript.splitlines(), 1):
            if "|" not in line:
                continue  # Vrije consulttekst blijft bewaard, maar wordt niet geïnterpreteerd.
            parts = [part.strip() for part in line.split("|")]
            if not 3 <= len(parts) <= 5 or not all(parts):
                raise ValueError(f"Regel {number}: verwacht onderwerp | status | bewijs.")
            try:
                status = Status(parts[1])
            except ValueError as exc:
                raise ValueError(f"Regel {number}: onbekende status '{parts[1]}'.") from exc
            facts.append(Fact(parts[0], status, parts[2],
                              parts[3] if len(parts) >= 4 else "patient",
                              parts[4] if len(parts) == 5 else "current"))
        return facts
