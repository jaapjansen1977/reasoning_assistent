"""Vervangbare onderdelen met een vast contract."""
from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from .audio.buffer import AudioChunk
    from .audio.whisper_backend import TranscriptResult
from .domain import Consultation, Fact, Suggestion


class FactExtractor(Protocol):
    def extract(self, transcript: str) -> list[Fact]: ...


class Reasoner(Protocol):
    def suggest(self, consultation: Consultation) -> tuple[Suggestion, ...]: ...


class Transcriber(Protocol):
    def transcribe(self, audio_path: str) -> str: ...


class ChunkTranscriber(Protocol):
    def transcribe_chunk(self, chunk: "AudioChunk") -> "TranscriptResult": ...
