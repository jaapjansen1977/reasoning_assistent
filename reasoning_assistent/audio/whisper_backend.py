"""Adapter op bestaande faster-whisper; geen eigen spraakmodel."""
from dataclasses import dataclass
from time import monotonic
from .buffer import AudioChunk
from .settings import SpeechSettings
from .preprocessing import to_whisper_audio


class SpeechError(RuntimeError):
    pass


@dataclass(frozen=True)
class TranscriptResult:
    text: str
    audio_seconds: float
    processing_seconds: float


class FasterWhisperTranscriber:
    def __init__(self, settings: SpeechSettings, model):
        self.settings = settings
        self.model = model

    @classmethod
    def prepare(cls, settings: SpeechSettings, allow_download=False):
        try:
            from faster_whisper import WhisperModel
            from faster_whisper.utils import download_model
        except (ImportError, OSError) as exc:
            raise SpeechError('Spraakonderdeel ontbreekt of kan niet laden. '
                              'Installeer met: python -m pip install -e ".[speech]"') from exc
        path = settings.model_path
        # Een lokale tokenizer voorkomt dat de bibliotheek terugvalt op een download.
        required = ("model.bin", "config.json", "tokenizer.json")
        complete = all((path / name).is_file() for name in required) and any(path.glob("vocabulary.*"))
        try:
            if not complete:
                if not allow_download:
                    raise SpeechError("Model nog niet lokaal beschikbaar. Klik eerst op Download model.")
                path.mkdir(parents=True, exist_ok=True)
                download_model(settings.model_name, output_dir=str(path), use_auth_token=False)
                if not all((path / name).is_file() for name in required) or not any(path.glob("vocabulary.*")):
                    raise SpeechError("Modeldownload is onvolledig. Probeer opnieuw.")
            model = WhisperModel(str(path), device="cpu", compute_type="int8",
                                 cpu_threads=settings.cpu_threads, num_workers=1,
                                 local_files_only=True)
            return cls(settings, model)
        except SpeechError:
            raise
        except Exception as exc:
            raise SpeechError(f"Model kan niet worden voorbereid ({type(exc).__name__}). "
                              "Controleer internet voor de download en beschikbare schijfruimte; "
                              "bij laadproblemen ook de Python-installatie.") from exc

    def transcribe_chunk(self, chunk: AudioChunk) -> TranscriptResult:
        started = monotonic()
        try:
            audio = to_whisper_audio(chunk)
            if not audio.size:
                return TranscriptResult("", 0.0, 0.0)
            segments, _ = self.model.transcribe(
                audio, language=self.settings.language, task="transcribe",
                beam_size=1, temperature=0.0, vad_filter=True,
                vad_parameters={"min_silence_duration_ms": 300},
                condition_on_previous_text=False)
            # De generator uitvoeren op de worker, niet op de GUI-thread.
            text = " ".join(segment.text.strip() for segment in segments if segment.text.strip())
            return TranscriptResult(text, len(audio) / 16000, monotonic() - started)
        except Exception as exc:
            raise SpeechError(f"Spraakherkenning mislukt ({type(exc).__name__}). "
                              "Controleer installatie en herstart het gesprek.") from exc
