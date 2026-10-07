"""Kennis laden als data; geen klinische inhoud in de interface."""
import json
from importlib.resources import files
from ..domain import Source
from dataclasses import dataclass


@dataclass(frozen=True)
class QuestionRule:
    id: str
    topic: str
    question: str
    source: Source


def load_demo_rules() -> tuple[QuestionRule, ...]:
    data = json.loads(files("reasoning_assistent.knowledge").joinpath("demo.json").read_text(encoding="utf-8"))
    source = Source(**data["source"])
    return tuple(QuestionRule(source=source, **item) for item in data["questions"])


def load_low_back_module() -> dict:
    """Load the draft as data for explicit fictional AI experiments only."""
    path = files("reasoning_assistent.knowledge").joinpath("regions", "low_back.v1.json")
    return json.loads(path.read_text(encoding="utf-8"))
