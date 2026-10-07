from array import array
from types import SimpleNamespace
from time import monotonic, sleep
import unittest
from reasoning_assistent.audio.buffer import ChunkBuffer
from reasoning_assistent.audio.devices import InputDevice, AudioError, list_input_devices
from reasoning_assistent.audio.recorder import MicrophoneRecorder


class FakeStream:
    def __init__(self, **kwargs):
        self.callback = kwargs['callback']
        self.finished = kwargs['finished_callback']
        self.active = False
        self.closed = False

    def start(self):
        self.active = True

    def abort(self):
        self.active = False
        self.finished()

    def close(self):
        self.closed = True

    def emit(self, values, status=False):
        self.callback(array('h', values).tobytes(), len(values), None, status)


class FakeBackend:
    default = SimpleNamespace(device=(1, 0))

    def query_hostapis(self):
        return [{'name': 'Fake API'}]

    def query_devices(self):
        return [dict(name='Speaker', hostapi=0, max_input_channels=0, default_samplerate=48000),
                dict(name='Microphone', hostapi=0, max_input_channels=1, default_samplerate=100)]

    def check_input_settings(self, **kwargs):
        self.settings = kwargs

    def RawInputStream(self, **kwargs):
        self.stream = FakeStream(**kwargs)
        return self.stream


class BufferTests(unittest.TestCase):
    def test_fragments_preserve_samples_across_blocks(self):
        buffer = ChunkBuffer(10, seconds=1, max_chunks=2)
        pcm = array('h', list(range(20))).tobytes()
        buffer.feed(pcm[:6])
        buffer.feed(pcm[6:])
        self.assertEqual(buffer.pop().pcm + buffer.pop().pcm, pcm)
        self.assertIsNone(buffer.pop())

    def test_memory_is_bounded_and_discards_are_counted(self):
        buffer = ChunkBuffer(10, seconds=1, max_chunks=2)
        buffer.feed(array('h', list(range(35))).tobytes())
        self.assertEqual(len(buffer.ready), 2)
        self.assertEqual(buffer.evicted_chunks, 1)
        self.assertEqual(len(buffer.pending), 10)
        self.assertEqual(array('h', buffer.pop().pcm)[0], 10)
        buffer.clear()
        self.assertFalse(buffer.pending)
        self.assertFalse(buffer.ready)

    def test_incomplete_sample_rejected(self):
        with self.assertRaises(ValueError):
            ChunkBuffer(10).feed(b'x')


class RecorderTests(unittest.TestCase):
    def setUp(self):
        self.backend = FakeBackend()
        self.device = list_input_devices(self.backend)[0]
        self.recorder = MicrophoneRecorder(self.backend)
        self.addCleanup(self.recorder.stop)

    def wait_for(self, condition):
        deadline = monotonic() + 2
        while not condition() and monotonic() < deadline:
            sleep(.01)
        self.assertTrue(condition())

    def test_device_filter_and_default(self):
        self.assertEqual(self.device.index, 1)
        self.assertTrue(self.device.is_default)

    def test_capture_meter_chunk_and_stop_clear(self):
        self.recorder.start(self.device)
        self.backend.stream.emit([16384] * 500)
        self.wait_for(lambda: self.recorder.snapshot().buffered_chunks == 1)
        self.assertAlmostEqual(self.recorder.snapshot().level_db, -6.02, places=1)
        self.assertEqual(self.recorder.pop_chunk().samplerate, 100)
        self.recorder.stop()
        self.assertTrue(self.backend.stream.closed)
        self.assertFalse(self.recorder.running)
        self.assertIsNone(self.recorder.pop_chunk())
        self.assertEqual(self.recorder.snapshot().level_db, -60)

    def test_repeat_start_stop_and_double_start(self):
        for _ in range(2):
            self.recorder.start(self.device)
            with self.assertRaises(AudioError):
                self.recorder.start(self.device)
            self.recorder.stop()
            self.recorder.stop()

    def test_start_failure_closes_stream(self):
        def broken_start():
            raise RuntimeError('denied')
        original = self.backend.RawInputStream
        def stream(**kwargs):
            result = original(**kwargs)
            result.start = broken_start
            return result
        self.backend.RawInputStream = stream
        with self.assertRaises(AudioError):
            self.recorder.start(self.device)
        self.assertTrue(self.backend.stream.closed)
        self.assertFalse(self.recorder.running)
        self.assertIsNone(self.recorder.pop_chunk())

    def test_finished_and_overflow_visible(self):
        self.recorder.start(self.device)
        self.backend.stream.emit([0] * 10, status=True)
        self.assertIn('onderbreking', self.recorder.snapshot().warning)
        self.backend.stream.finished()
        self.assertFalse(self.recorder.snapshot().running)

    def test_full_callback_queue_never_blocks(self):
        for _ in range(40):
            self.recorder._callback(b'\0\0', 1, None, False)
        self.assertEqual(self.recorder.snapshot().dropped_blocks, 8)
        self.assertIn('verloren', self.recorder.snapshot().warning)
