"""Achtergrondcontroller voor modelvoorbereiding en live transcriptie.

UI leest events; alle modelaanroepen staan op één worker. Stop verwerkt de staart,
sluiten annuleert en verwerpt latere resultaten. Native inferentie kan niet direct
worden onderbroken; een nieuw gesprek start pas wanneer de worker klaar is.
"""
from dataclasses import dataclass
from queue import Queue, Empty
from threading import Event, Thread
from .recorder import MicrophoneRecorder
from .whisper_backend import FasterWhisperTranscriber


@dataclass(frozen=True)
class SpeechEvent:
    kind: str
    text: str = ""


class SpeechSession:
    def __init__(self, recorder=None, prepare=FasterWhisperTranscriber.prepare):
        self.recorder = recorder if recorder is not None else MicrophoneRecorder()
        self._prepare = prepare
        self.transcriber = None
        self._events = Queue()
        self._worker = None
        self._stop = Event()
        self._cancel = Event()
        self._closed = False

    @property
    def busy(self):
        return self._worker is not None and self._worker.is_alive()

    def events(self):
        while True:
            try:
                yield self._events.get_nowait()
            except Empty:
                return

    def _emit(self, kind, text=""):
        if not self._closed:
            self._events.put(SpeechEvent(kind, text))

    def prepare(self, settings, allow_download=False):
        if self.busy or self._closed:
            raise RuntimeError("Wacht tot de huidige taak klaar is.")
        self.transcriber = None
        def work():
            try:
                engine = self._prepare(settings, allow_download=allow_download)
                if not self._closed:
                    self.transcriber = engine
                    self._emit("ready", f"Model {settings.model_name} gereed — Nederlands, lokaal op CPU.")
            except Exception as exc:
                self._emit("error", str(exc))
        self._worker = Thread(target=work, name="speech-model", daemon=True)
        self._worker.start()

    def start(self, device, transcribe=True):
        if self.busy or self._closed:
            raise RuntimeError("Wacht tot de huidige taak klaar is.")
        if transcribe and self.transcriber is None:
            raise RuntimeError("Laad eerst een spraakmodel of kies Alleen audiotest.")
        self._stop.clear()
        self._cancel.clear()
        self.recorder.start(device)
        self._worker = Thread(target=self._run, args=(transcribe,), name="speech-transcript", daemon=True)
        self._worker.start()

    def _decode(self, chunk):
        if self._cancel.is_set():
            return
        result = self.transcriber.transcribe_chunk(chunk)
        if self._cancel.is_set():
            return
        if result.text:
            self._emit("text", result.text)
        ratio = result.processing_seconds / result.audio_seconds if result.audio_seconds else 0
        self._emit("timing", f"Laatste fragment: {result.audio_seconds:.1f} s audio in "
                   f"{result.processing_seconds:.1f} s verwerkt (factor {ratio:.2f}).")
        if ratio > 1:
            self._emit("warning", "Spraakherkenning loopt achter op het gesprek. "
                       "Probeer tiny of kortere tests; audio kan verloren gaan bij een volle buffer.")

    def _run(self, transcribe):
        lost = 0
        last_warning = ""
        try:
            while not self._stop.is_set() and not self._cancel.is_set():
                state = self.recorder.snapshot()
                if state.warning and state.warning != last_warning:
                    self._emit("warning", state.warning + " Transcript kan onvolledig zijn.")
                    last_warning = state.warning
                total_lost = state.discarded_chunks + state.dropped_blocks
                if total_lost > lost:
                    self._emit("warning", "Er is audio verloren gegaan. Het transcript is onvolledig.")
                    lost = total_lost
                if not state.running:
                    self._emit("warning", state.warning or "Microfoon is onverwacht gestopt.")
                    break
                chunk = self.recorder.pop_chunk() if transcribe else None
                if chunk is not None:
                    self._decode(chunk)
                else:
                    self._stop.wait(0.05)
            final_state = self.recorder.snapshot()
            if transcribe and final_state.discarded_chunks + final_state.dropped_blocks > lost:
                self._emit("warning", "Er is audio verloren gegaan. Het transcript is onvolledig.")
            if self._cancel.is_set() or not transcribe:
                self.recorder.stop()
            else:
                for chunk in self.recorder.finish():
                    if self._cancel.is_set():
                        break
                    self._decode(chunk)
        except Exception as exc:
            self._emit("error", str(exc))
        finally:
            self.recorder.stop()
            self._emit("stopped", "Gestopt. Audio uit de opnamebuffer verwijderd; tekst blijft zichtbaar.")

    def stop(self):
        self._stop.set()

    def close(self):
        self._closed = True
        self._cancel.set()
        self._stop.set()
        # Opname meteen stoppen; inferentie-resultaten daarna worden genegeerd.
        self.recorder.stop()
        for _ in self.events():
            pass
