"""Begrensde PCM16-monobuffer voor toekomstige transcriptie."""
from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class AudioChunk:
    pcm: bytes
    samplerate: int
    channels: int = 1


class ChunkBuffer:
    def __init__(self, samplerate: int, seconds: float = 5.0, max_chunks: int = 6):
        if samplerate <= 0 or seconds <= 0 or max_chunks <= 0:
            raise ValueError("Bufferinstellingen moeten positief zijn.")
        self.samplerate = samplerate
        self.chunk_bytes = round(samplerate * seconds) * 2
        if self.chunk_bytes <= 0:
            raise ValueError("Fragment moet ten minste één sample bevatten.")
        self.pending = bytearray()
        self.ready = deque(maxlen=max_chunks)
        self.evicted_chunks = 0

    def feed(self, pcm: bytes):
        if len(pcm) % 2:
            raise ValueError("PCM16 moet complete samples bevatten.")
        self.pending.extend(pcm)
        while len(self.pending) >= self.chunk_bytes:
            chunk = AudioChunk(bytes(self.pending[:self.chunk_bytes]), self.samplerate)
            del self.pending[:self.chunk_bytes]
            if len(self.ready) == self.ready.maxlen:
                self.evicted_chunks += 1
            self.ready.append(chunk)

    def pop(self):
        return self.ready.popleft() if self.ready else None

    def flush(self):
        if self.pending:
            if len(self.ready) == self.ready.maxlen:
                self.evicted_chunks += 1
            self.ready.append(AudioChunk(bytes(self.pending), self.samplerate))
            self.pending.clear()

    def clear(self):
        self.pending.clear()
        self.ready.clear()


class PauseAwareBuffer:
    """PCM16 segmenteren op korte energievensters; geen extra AI-afhankelijkheid.

    Dit detecteert rustige audio, geen semantisch zinseinde. De maximale duur
    beschermt geheugen en vertraging. Alle samples blijven in volgorde behouden.
    """
    def __init__(self, samplerate, settings):
        if samplerate <= 0:
            raise ValueError("Samplefrequentie moet positief zijn.")
        self.samplerate = samplerate
        self.settings = settings
        self.pending = bytearray()
        self.ready = deque(maxlen=settings.max_chunks)
        self.evicted_chunks = 0
        self._cursor = 0
        self._quiet_samples = 0
        self._window_samples = max(1, round(samplerate * 0.1))
        self._min_samples = max(1, round(samplerate * settings.min_seconds))
        self._max_samples = max(1, round(samplerate * settings.max_seconds))
        self._pause_samples = max(1, round(samplerate * settings.pause_seconds))
        self._threshold = 32768 * 10 ** (settings.silence_db / 20)

    def feed(self, pcm):
        from array import array
        from math import sqrt
        if len(pcm) % 2:
            raise ValueError("PCM16 moet complete samples bevatten.")
        self.pending.extend(pcm)
        while True:
            # Ook bij een niet-rond maximum exact op de maximale sample knippen.
            remaining = self._max_samples - self._cursor // 2
            count = min(self._window_samples, remaining)
            end = self._cursor + count * 2
            if len(self.pending) < end:
                break
            samples = array("h")
            samples.frombytes(self.pending[self._cursor:end])
            rms = sqrt(sum(value * value for value in samples) / count)
            self._quiet_samples = self._quiet_samples + count if rms <= self._threshold else 0
            self._cursor = end
            duration = self._cursor // 2
            if duration >= self._max_samples or (duration >= self._min_samples and
                                                 self._quiet_samples >= self._pause_samples):
                self._emit(self._cursor)

    def _emit(self, size):
        if len(self.ready) == self.ready.maxlen:
            self.evicted_chunks += 1
        self.ready.append(AudioChunk(bytes(self.pending[:size]), self.samplerate))
        del self.pending[:size]
        self._cursor = self._quiet_samples = 0

    def pop(self):
        return self.ready.popleft() if self.ready else None

    def clear(self):
        self.pending.clear()
        self.ready.clear()
        self._cursor = self._quiet_samples = 0
