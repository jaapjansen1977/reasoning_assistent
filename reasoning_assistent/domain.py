"""Gedeelde gegevensstructuren, onafhankelijk van UI en AI-leverancier."""
from dataclasses import dataclass, field
from enum import Enum


class Status(str, Enum):
    NOT_DISCUSSED = "niet_besproken"
    PRESENT = "aanwezig"
    DENIED = "ontkend"
    UNCLEAR = "onduidelijk"


@dataclass(frozen=True)
class Fact:
    topic: str
    status: Status
    evidence: str
    subject: str = "patient"
    period: str = "current"


@dataclass
class Consultation:
    transcript: str
    facts: dict[str, Fact] = field(default_factory=dict)


@dataclass(frozen=True)
class Source:
    title: str
    version: str
    reference: str
    clinically_reviewed: bool = False


@dataclass(frozen=True)
class Suggestion:
    id: str
    category: str
    question: str
    reason: str
    source: Source


@dataclass(frozen=True)
class Analysis:
    consultation: Consultation
    suggestions: tuple[Suggestion, ...]
