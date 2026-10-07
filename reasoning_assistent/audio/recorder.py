"""Microfoonstream met begrensde queue en achtergrondverwerking.

De callback kopieert uitsluitend audio naar een queue. Geen AI, UI of bestand-I/O.
Alle PCM is native-endian signed int16 mono op de eigen samplefrequentie.
"""
from array import array
from dataclasses import dataclass
from math import sqrt, log10
from queue import Queue, Empty, Full
from threading import Event, Lock, Thread
from time import monotonic
from .buffer import ChunkBuffer
from .devices import AudioError, InputDevice, load_backend


@dataclass(frozen=True)
class RecordingStatus:
    running: bool
    level_db: float
    seconds: float
    buffered_chunks: int
    discarded_chunks: int
    dropped_blocks: int
    warning: str


class MicrophoneRecorder:
    def __init__(self, backend=None):
        self._backend = backend
        self._stream = None
        self._worker = None
        self._stop = Event()
        self._finished = Event()
        self._lock = Lock()
        self._queue = Queue(maxsize=32)
        self._buffer = None
        self._level_db = -60.0
        self._started = 0.0
        self._dropped = 0
        self._warning = ""

    @property
    def running(self):
        return self._stream is not None

    def start(self, device: InputDevice):
        if self.running:
            raise AudioError("Microfoon luistert al.")
        sd = self._backend if self._backend is not None else load_backend()
        self._stop.clear()
        self._finished.clear()
        self._queue = Queue(maxsize=32)
        self._buffer = ChunkBuffer(device.samplerate)
        self._level_db, self._dropped, self._warning = -60.0, 0, ""
        try:
            sd.check_input_settings(device=device.index, channels=1,
                                    dtype="int16", samplerate=device.samplerate)
            self._stream = sd.RawInputStream(
                device=device.index, channels=1, dtype="int16",
                samplerate=device.samplerate, blocksize=round(device.samplerate * 0.05),
                callback=self._callback, finished_callback=self._finished.set)
            self._worker = Thread(target=self._process, name="microphone-buffer", daemon=True)
            self._worker.start()
            self._started = monotonic()
            self._stream.start()
        except Exception as exc:
            self.stop()
            raise AudioError("Microfoon kan niet starten. Controleer de gekozen microfoon, "
                             "Windows-toegang en of een andere app deze exclusief gebruikt.") from exc

    def _callback(self, indata, frames, time_info, status):
        if self._stop.is_set():
            return
        if status:
            self._warning = "Audiostream meldt een onderbreking; er kan audio ontbreken."
        try:
            self._queue.put_nowait(bytes(indata))
        except Full:
            self._dropped += 1
            self._warning = "Verwerking loopt achter; audioblokken zijn verloren gegaan."

    def _process(self):
        while not self._stop.is_set():
            try:
                pcm = self._queue.get(timeout=0.1)
            except Empty:
                continue
            try:
                samples = array("h")
                samples.frombytes(pcm)
                rms = sqrt(sum(value * value for value in samples) / len(samples)) if samples else 0
                db = max(-60.0, min(0.0, 20 * log10(max(rms / 32768, 1e-3))))
                with self._lock:
                    self._level_db = db
                    self._buffer.feed(pcm)
            except Exception:
                self._warning = "Audioverwerking gestopt door een fout. Start de opname opnieuw."
                self._finished.set()
                return

    def snapshot(self):
        with self._lock:
            buffer = self._buffer
            warning = self._warning
            if self.running and self._finished.is_set():
                warning = warning or "Microfoonstream is onverwacht gestopt."
            return RecordingStatus(self.running and not self._finished.is_set(), self._level_db,
                                   monotonic() - self._started if self.running else 0.0,
                                   len(buffer.ready) if buffer else 0,
                                   buffer.evicted_chunks if buffer else 0,
                                   self._dropped, warning)

    def pop_chunk(self):
        """Toekomstige transcriptieworker haalt hier een fragment op."""
        with self._lock:
            return self._buffer.pop() if self._buffer else None

    def stop(self):
        self._stop.set()
        stream, self._stream = self._stream, None
        if stream is not None:
            try:
                stream.abort()
            except Exception:
                pass
            try:
                stream.close()
            except Exception:
                pass
        if self._worker is not None:
            self._worker.join(timeout=1.0)
            self._worker = None
        with self._lock:
            if self._buffer is not None:
                self._buffer.clear()
            self._buffer = None
            self._level_db = -60.0
        while True:
            try:
                self._queue.get_nowait()
            except Empty:
                break
