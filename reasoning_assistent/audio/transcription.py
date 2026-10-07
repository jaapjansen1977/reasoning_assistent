"""Aansluitpunt voor toekomstige lokale spraakherkenning."""

class NotConfiguredTranscriber:
    def transcribe(self, audio_path: str) -> str:
        raise NotImplementedError(
            "Spraakherkenning is nog niet aangesloten. Gebruik voorlopig tekst."
        )
