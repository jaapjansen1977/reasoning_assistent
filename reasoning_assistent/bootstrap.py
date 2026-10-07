"""Alleen hier kiezen we implementaties. Later AI of STT hier aansluiten."""
from .application import ConsultationService
from .extraction.structured import StructuredFactExtractor
from .knowledge.loader import load_demo_rules
from .reasoning.questions import MissingInformationReasoner


def build_service() -> ConsultationService:
    return ConsultationService(StructuredFactExtractor(),
                               MissingInformationReasoner(load_demo_rules()))


def build_ai_service(api_key: str, model: str):
    """Replace this backend later with a local implementation of AnalysisBackend."""
    from .ai.openai_backend import OpenAIBackend
    from .ai.service import AIConsultationService
    from .knowledge.loader import load_low_back_module
    return AIConsultationService(OpenAIBackend(api_key, model), load_low_back_module())
