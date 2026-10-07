from array import array
import unittest
from reasoning_assistent.audio.buffer import PauseAwareBuffer
from reasoning_assistent.audio.settings import ChunkSettings


def pcm(value, seconds, rate=100):
    return array('h', [value] * round(seconds * rate)).tobytes()


class PauseChunkTests(unittest.TestCase):
    def buffer(self, **kwargs):
        return PauseAwareBuffer(100, ChunkSettings(**kwargs))

    def test_does_not_split_after_five_seconds(self):
        buf = self.buffer()
        buf.feed(pcm(2000, 5))
        self.assertIsNone(buf.pop())
        self.assertEqual(len(buf.pending), 1000)

    def test_short_pause_keeps_sentence_together(self):
        buf = self.buffer()
        buf.feed(pcm(2000, 8) + pcm(0, .4) + pcm(2000, 2))
        self.assertIsNone(buf.pop())

    def test_full_pause_after_minimum_emits_fragment(self):
        buf = self.buffer()
        data = pcm(2000, 9) + pcm(0, .8)
        buf.feed(data)
        self.assertEqual(buf.pop().pcm, data)
        self.assertFalse(buf.pending)

    def test_early_pause_does_not_create_tiny_fragment(self):
        buf = self.buffer()
        buf.feed(pcm(2000, 2) + pcm(0, 1) + pcm(2000, 2))
        self.assertIsNone(buf.pop())

    def test_continuous_speech_cuts_at_configured_maximum(self):
        for maximum in (10, 15, 20):
            buf = self.buffer(max_seconds=maximum)
            buf.feed(pcm(2000, maximum + 1))
            self.assertEqual(len(buf.pop().pcm), maximum * 100 * 2)
            self.assertEqual(len(buf.pending), 200)

    def test_output_independent_of_callback_boundaries(self):
        data = pcm(2000, 9) + pcm(0, .8) + pcm(2000, 16)
        whole = self.buffer()
        sliced = self.buffer()
        whole.feed(data)
        for offset in range(0, len(data), 14):
            sliced.feed(data[offset:offset+14])
        self.assertEqual(list(whole.ready), list(sliced.ready))
        self.assertEqual(whole.pending, sliced.pending)
        reconstructed = b''.join(c.pcm for c in whole.ready) + bytes(whole.pending)
        self.assertEqual(reconstructed, data)

    def test_bounded_backlog_is_counted(self):
        buf = self.buffer(max_chunks=2)
        buf.feed(pcm(2000, 50))
        self.assertEqual(len(buf.ready), 2)
        self.assertEqual(buf.evicted_chunks, 1)
        self.assertEqual(len(buf.pending), 1000)

    def test_clear_resets_pause_tracking(self):
        buf = self.buffer()
        buf.feed(pcm(0, 7))
        buf.clear()
        buf.feed(pcm(2000, 8) + pcm(0, .4))
        self.assertIsNone(buf.pop())

    def test_invalid_config_rejected(self):
        with self.assertRaises(ValueError):
            ChunkSettings(min_seconds=8, max_seconds=5)
        with self.assertRaises(ValueError):
            self.buffer().feed(b'x')
