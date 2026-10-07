"""Vervangbare onderdelen met een vast contract."""
from typing import Protocol
from .domain import Consultation, Fact, Suggestion


class FactExtractor(Protocol):
    def extract(self, transcript: str) -> list[Fact]: ...


class Reasoner(Protocol):
    def suggest(self, consultation: Consultation) -> tuple[Suggestion, ...]: ...


class Transcriber(Protocol):
    def transcribe(self, audio_path: str) -> str: ...
