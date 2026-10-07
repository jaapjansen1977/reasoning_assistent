"""Alleen hier kiezen we implementaties. Later AI of STT hier aansluiten."""
from .application import ConsultationService
from .extraction.structured import StructuredFactExtractor
from .knowledge.loader import load_demo_rules
from .reasoning.questions import MissingInformationReasoner


def build_service() -> ConsultationService:
    return ConsultationService(StructuredFactExtractor(),
                               MissingInformationReasoner(load_demo_rules()))
