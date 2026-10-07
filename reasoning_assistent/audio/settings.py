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
