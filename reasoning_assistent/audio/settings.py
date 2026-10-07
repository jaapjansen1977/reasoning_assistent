"""Instellingen en lokaal modelpad; onafhankelijk van het venster."""
from dataclasses import dataclass
from pathlib import Path
import os


def default_model_root() -> Path:
    base = os.environ.get("LOCALAPPDATA")
    return (Path(base) if base else Path.home() / ".cache") / "ReasoningAssistent" / "models"


@dataclass(frozen=True)
class SpeechSettings:
    model_name: str = "base"
    language: str = "nl"
    cpu_threads: int = 4
    model_root: Path | None = None

    def __post_init__(self):
        if self.model_name not in ("tiny", "base", "small"):
            raise ValueError("Kies tiny, base of small (meertalig).")
        if self.cpu_threads < 1:
            raise ValueError("Aantal CPU-threads moet positief zijn.")

    @property
    def model_path(self) -> Path:
        root = self.model_root if self.model_root is not None else default_model_root()
        return root / self.model_name


@dataclass(frozen=True)
class ChunkSettings:
    """Verzamel context; knip vanaf 8 s bij een pauze, uiterlijk bij maximum."""
    min_seconds: float = 8.0
    max_seconds: float = 15.0
    pause_seconds: float = 0.8
    silence_db: float = -42.0
    max_chunks: int = 4

    def __post_init__(self):
        if not 0 < self.min_seconds <= self.max_seconds <= 30:
            raise ValueError("Kies 0 < minimum <= maximum <= 30 seconden.")
        if self.pause_seconds <= 0 or self.max_chunks < 1 or not -100 <= self.silence_db < 0:
            raise ValueError("Ongeldige pauze-/bufferinstellingen.")
