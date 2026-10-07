from array import array
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace, ModuleType
from unittest.mock import patch
from threading import Event
from time import monotonic, sleep
import unittest
import importlib.util

HAS_AUDIO_LIBS = all(importlib.util.find_spec(name) for name in ("numpy", "scipy"))

from reasoning_assistent.audio.buffer import AudioChunk
from reasoning_assistent.audio.preprocessing import to_whisper_audio
from reasoning_assistent.audio.settings import SpeechSettings, ChunkSettings
from reasoning_assistent.audio.whisper_backend import FasterWhisperTranscriber, SpeechError, TranscriptResult
from reasoning_assistent.audio.session import SpeechSession
from reasoning_assistent.audio.recorder import MicrophoneRecorder
from test_audio import FakeBackend
from reasoning_assistent.audio.devices import list_input_devices


@unittest.skipUnless(HAS_AUDIO_LIBS, "Installeer de speech-extra voor resamplingtests")
class PreprocessingTests(unittest.TestCase):
    def test_amplitude_and_dtype(self):
        data = to_whisper_audio(AudioChunk(array('h', [-32768, 0, 16384]).tobytes(), 16000))
        self.assertEqual(data.dtype.name, 'float32')
        self.assertEqual(list(data), [-1.0, 0.0, 0.5])

    def test_resample_48k_and_44100(self):
        for rate in (48000, 44100):
            data = to_whisper_audio(AudioChunk(array('h', [1000] * rate).tobytes(), rate))
            self.assertEqual(len(data), 16000)

    def test_invalid_and_empty(self):
        with self.assertRaises(ValueError):
            to_whisper_audio(AudioChunk(b'\0', 16000))
        with self.assertRaises(ValueError):
            to_whisper_audio(AudioChunk(b'', 0))
        self.assertEqual(len(to_whisper_audio(AudioChunk(b'', 16000))), 0)


class BackendTests(unittest.TestCase):
    @unittest.skipUnless(HAS_AUDIO_LIBS, "Installeer de speech-extra voor transcriptie-adaptertests")
    def test_generator_is_consumed_and_dutch_vad_is_enabled(self):
        class Model:
            def transcribe(self, audio, **kwargs):
                self.kwargs = kwargs
                return (SimpleNamespace(text=t) for t in [' Hallo ', '', 'wereld.']), None
        model = Model()
        engine = FasterWhisperTranscriber(SpeechSettings(), model)
        result = engine.transcribe_chunk(AudioChunk(array('h', [1000] * 16000).tobytes(), 16000))
        self.assertEqual(result.text, 'Hallo wereld.')
        self.assertEqual(result.audio_seconds, 1)
        self.assertEqual(model.kwargs['language'], 'nl')
        self.assertTrue(model.kwargs['vad_filter'])
        self.assertFalse(model.kwargs['condition_on_previous_text'])

    def fake_modules(self, download, factory):
        module = ModuleType('faster_whisper')
        module.WhisperModel = factory
        utils = ModuleType('faster_whisper.utils')
        utils.download_model = download
        return {'faster_whisper': module, 'faster_whisper.utils': utils}

    def write_model(self, path):
        path.mkdir(parents=True, exist_ok=True)
        for name in ('model.bin', 'config.json', 'tokenizer.json', 'vocabulary.txt'):
            (path / name).write_text('test')

    def test_offline_load_uses_local_path_and_never_downloads(self):
        with TemporaryDirectory() as directory:
            settings = SpeechSettings(model_root=Path(directory))
            self.write_model(settings.model_path)
            calls = []
            def factory(*args, **kwargs):
                calls.append((args, kwargs))
                return object()
            def download(*args, **kwargs):
                self.fail('Offline loading must never download')
            with patch.dict('sys.modules', self.fake_modules(download, factory)):
                FasterWhisperTranscriber.prepare(settings)
            self.assertEqual(calls[0][0][0], str(settings.model_path))
            self.assertTrue(calls[0][1]['local_files_only'])
            self.assertEqual(calls[0][1]['device'], 'cpu')
            self.assertEqual(calls[0][1]['compute_type'], 'int8')

    def test_missing_tokenizer_blocks_offline_load(self):
        with TemporaryDirectory() as directory:
            settings = SpeechSettings(model_root=Path(directory))
            self.write_model(settings.model_path)
            (settings.model_path / 'tokenizer.json').unlink()
            def unexpected(*args, **kwargs):
                self.fail('No implicit model load/download')
            with patch.dict('sys.modules', self.fake_modules(unexpected, unexpected)):
                with self.assertRaises(SpeechError):
                    FasterWhisperTranscriber.prepare(settings)

    def test_explicit_download_then_local_load(self):
        with TemporaryDirectory() as directory:
            settings = SpeechSettings(model_name='tiny', model_root=Path(directory))
            calls = []
            def download(name, **kwargs):
                calls.append((name, kwargs))
                self.write_model(Path(kwargs['output_dir']))
            with patch.dict('sys.modules', self.fake_modules(download, lambda *a, **k: object())):
                FasterWhisperTranscriber.prepare(settings, allow_download=True)
            self.assertEqual(calls[0][0], 'tiny')
            self.assertFalse(calls[0][1]['use_auth_token'])


class SessionTests(unittest.TestCase):
    def setUp(self):
        self.backend = FakeBackend()
        self.device = list_input_devices(self.backend)[0]
        self.recorder = MicrophoneRecorder(self.backend)
        class Engine:
            def __init__(self):
                self.chunks = []
            def transcribe_chunk(self, chunk):
                self.chunks.append(chunk)
                return TranscriptResult('Nederlandse tekst', len(chunk.pcm) / (2 * chunk.samplerate), .01)
        self.engine = Engine()
        self.session = SpeechSession(self.recorder, prepare=lambda *a, **k: self.engine)
        self.addCleanup(self.session.close)

    def wait_for(self, condition):
        deadline = monotonic() + 3
        while not condition() and monotonic() < deadline:
            sleep(.01)
        self.assertTrue(condition())

    def prepare(self):
        self.session.prepare(SpeechSettings())
        self.wait_for(lambda: not self.session.busy)
        self.assertIs(self.session.transcriber, self.engine)
        list(self.session.events())

    def test_start_requires_ready_model(self):
        with self.assertRaises(RuntimeError):
            self.session.start(self.device, chunk_settings=ChunkSettings(min_seconds=1, max_seconds=5))
        self.assertFalse(self.recorder.running)

    def test_live_text_and_stop_preserves_short_tail(self):
        self.prepare()
        self.session.start(self.device, chunk_settings=ChunkSettings(min_seconds=1, max_seconds=5))
        self.backend.stream.emit([1000] * 500)
        self.wait_for(lambda: len(self.engine.chunks) == 1)
        self.backend.stream.emit([1000] * 30)
        self.session.stop()
        self.wait_for(lambda: not self.session.busy)
        self.assertEqual([len(c.pcm) for c in self.engine.chunks], [1000, 60])
        kinds = [e.kind for e in self.session.events()]
        self.assertEqual(kinds.count('text'), 2)
        self.assertIn('stopped', kinds)
        self.assertFalse(self.recorder.running)
        self.assertIsNone(self.recorder.pop_chunk())

    def test_audio_only_works_without_model(self):
        self.session.start(self.device, transcribe=False)
        self.backend.stream.emit([0] * 200)
        self.session.stop()
        self.wait_for(lambda: not self.session.busy)
        self.assertFalse(self.engine.chunks)

    def test_close_suppresses_inflight_text_and_closes_microphone(self):
        self.prepare()
        entered, release = Event(), Event()
        original = self.engine.transcribe_chunk
        def slow(chunk):
            entered.set()
            release.wait(2)
            return original(chunk)
        self.engine.transcribe_chunk = slow
        self.session.start(self.device, chunk_settings=ChunkSettings(min_seconds=1, max_seconds=5))
        self.backend.stream.emit([1000] * 500)
        self.assertTrue(entered.wait(2))
        self.session.close()
        self.assertTrue(self.backend.stream.closed)
        release.set()
        self.wait_for(lambda: not self.session.busy)
        self.assertEqual(list(self.session.events()), [])

    def test_failure_stops_capture_and_is_reported(self):
        self.prepare()
        def broken(chunk):
            raise SpeechError('Model failure')
        self.engine.transcribe_chunk = broken
        self.session.start(self.device, chunk_settings=ChunkSettings(min_seconds=1, max_seconds=5))
        self.backend.stream.emit([1000] * 500)
        self.wait_for(lambda: not self.session.busy)
        events = list(self.session.events())
        self.assertIn('error', [e.kind for e in events])
        self.assertFalse(self.recorder.running)

    def test_prepare_failure_reported(self):
        def broken(*args, **kwargs):
            raise SpeechError('Missing dependencies')
        session = SpeechSession(self.recorder, prepare=broken)
        session.prepare(SpeechSettings())
        self.wait_for(lambda: not session.busy)
        self.assertEqual(next(session.events()).kind, 'error')
        self.assertIsNone(session.transcriber)
        session.close()
