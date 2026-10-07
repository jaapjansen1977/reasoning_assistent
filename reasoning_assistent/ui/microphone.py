"""Microfoonbediening; Tk-widgets worden alleen op de UI-thread gewijzigd."""
import tkinter as tk
from tkinter import ttk, messagebox
from ..audio.devices import AudioError, list_input_devices
from ..audio.recorder import MicrophoneRecorder


class MicrophonePanel(ttk.LabelFrame):
    def __init__(self, parent, recorder=None, device_loader=list_input_devices):
        super().__init__(parent, text="Microfoon — lokale audiotest")
        self.recorder = recorder if recorder is not None else MicrophoneRecorder()
        self.device_loader = device_loader
        self.devices = ()
        self._closed = False
        self._after_id = None
        self.selector = ttk.Combobox(self, state="readonly", width=65)
        self.selector.grid(row=0, column=0, padx=8, pady=6, sticky="ew")
        self.refresh_button = ttk.Button(self, text="Ververs microfoons", command=self.refresh)
        self.refresh_button.grid(row=0, column=1, padx=8)
        self.start_button = ttk.Button(self, text="Start luisteren", command=self.start, state="disabled")
        self.start_button.grid(row=1, column=0, padx=8, sticky="w")
        self.stop_button = ttk.Button(self, text="Stop luisteren", command=self.stop, state="disabled")
        self.stop_button.grid(row=1, column=1, padx=8)
        self.meter = ttk.Progressbar(self, maximum=60)
        self.meter.grid(row=2, column=0, columnspan=2, padx=8, pady=6, sticky="ew")
        self.status = tk.StringVar(value="Niet gestart. Klik op Ververs microfoons.")
        ttk.Label(self, textvariable=self.status, wraplength=900).grid(
            row=3, column=0, columnspan=2, padx=8, pady=6, sticky="w")
        ttk.Label(self, text="Audio blijft tijdelijk in geheugen en wordt bij stoppen gewist. "
                  "Spraakherkenning is nog niet aangesloten.", wraplength=900).grid(
            row=4, column=0, columnspan=2, padx=8, pady=6, sticky="w")
        self.columnconfigure(0, weight=1)
        self._poll()

    def refresh(self):
        try:
            self.devices = self.device_loader()
        except AudioError as exc:
            self.devices = ()
            self.status.set(str(exc))
        self.selector["values"] = [device.label for device in self.devices]
        if self.devices:
            index = next((i for i, d in enumerate(self.devices) if d.is_default), 0)
            self.selector.current(index)
            self.status.set("Gereed. Start luisteren en spreek om de geluidsmeter te testen.")
        else:
            self.selector.set("")
            if not self.status.get().startswith("Microfoon"):
                self.status.set("Geen microfoon gevonden. Controleer aansluiting en Windows-toegang.")
        self.start_button.configure(state="normal" if self.devices else "disabled")

    def start(self):
        index = self.selector.current()
        if not 0 <= index < len(self.devices):
            return
        try:
            self.recorder.start(self.devices[index])
        except AudioError as exc:
            self.status.set(str(exc))
            messagebox.showerror("Microfoon", str(exc))
            return
        self.selector.configure(state="disabled")
        self.refresh_button.configure(state="disabled")
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")

    def stop(self):
        self.recorder.stop()
        self.meter["value"] = 0
        self.selector.configure(state="readonly")
        self.refresh_button.configure(state="normal")
        self.start_button.configure(state="normal" if self.devices else "disabled")
        self.stop_button.configure(state="disabled")
        self.status.set("Gestopt. Audiobuffer gewist.")

    def _poll(self):
        if self._closed:
            return
        state = self.recorder.snapshot()
        if self.recorder.running:
            if not state.running:
                warning = state.warning
                self.stop()
                self.status.set(warning)
            else:
                self.meter["value"] = state.level_db + 60
                self.status.set(f"Luistert — {state.seconds:.0f} s — niveau {state.level_db:.0f} dBFS — "
                                f"{state.buffered_chunks} fragmenten in geheugen. "
                                + (state.warning or ""))
        self._after_id = self.after(100, self._poll)

    def close(self):
        self._closed = True
        if self._after_id is not None:
            self.after_cancel(self._after_id)
        self.recorder.stop()
