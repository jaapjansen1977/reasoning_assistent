"""Microfoondetectie; optionele afhankelijkheid pas laden bij gebruik."""
from dataclasses import dataclass


class AudioError(RuntimeError):
    pass


def load_backend():
    try:
        import sounddevice
        return sounddevice
    except (ImportError, OSError) as exc:
        raise AudioError("Microfoononderdeel ontbreekt of kan niet laden. "
                         "Installeer met: python -m pip install -e .[audio]") from exc


@dataclass(frozen=True)
class InputDevice:
    index: int
    name: str
    hostapi: str
    samplerate: int
    is_default: bool = False

    @property
    def label(self):
        return f"{self.name} ({self.hostapi}, #{self.index})" + (" — standaard" if self.is_default else "")


def list_input_devices(backend=None):
    sd = backend if backend is not None else load_backend()
    try:
        apis = sd.query_hostapis()
        default = sd.default.device[0]
        return tuple(InputDevice(i, item["name"], apis[item["hostapi"]]["name"],
                                 round(item["default_samplerate"]), i == default)
                     for i, item in enumerate(sd.query_devices())
                     if item["max_input_channels"] > 0)
    except Exception as exc:
        raise AudioError("Microfoons niet gevonden. Controleer Windows-microfoontoegang en aansluiting.") from exc
