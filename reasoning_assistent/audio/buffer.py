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

    def clear(self):
        self.pending.clear()
        self.ready.clear()
