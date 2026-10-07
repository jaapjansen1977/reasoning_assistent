"""PCM16 op microfoonfrequentie naar float32 mono op 16 kHz."""
from math import gcd
from .buffer import AudioChunk


def to_whisper_audio(chunk: AudioChunk):
    import numpy as np
    from scipy.signal import resample_poly
    if chunk.channels != 1 or chunk.samplerate <= 0 or len(chunk.pcm) % 2:
        raise ValueError("Verwacht complete PCM16-monosamples met geldige samplefrequentie.")
    audio = np.frombuffer(chunk.pcm, dtype=np.int16).astype(np.float32) / 32768.0
    if audio.size and chunk.samplerate != 16000:
        divisor = gcd(chunk.samplerate, 16000)
        audio = resample_poly(audio, 16000 // divisor, chunk.samplerate // divisor)
    return np.ascontiguousarray(audio, dtype=np.float32)
