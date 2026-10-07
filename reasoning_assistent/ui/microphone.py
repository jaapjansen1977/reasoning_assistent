"""Microfoon- en spraakbediening. Alleen deze thread wijzigt Tk-widgets."""
import tkinter as tk
from tkinter import ttk, messagebox
from ..audio.devices import AudioError, list_input_devices
from ..audio.settings import SpeechSettings
from ..audio.session import SpeechSession


class MicrophonePanel(ttk.LabelFrame):
    def __init__(self, parent, recorder=None, device_loader=list_input_devices, session=None):
        super().__init__(parent, text="Microfoon en lokale Nederlandse spraakherkenning")
        self.session = session if session is not None else SpeechSession(recorder=recorder)
        self.recorder = self.session.recorder
        self.device_loader = device_loader
        self.devices = ()
        self._closed = False
        self._after_id = None
        self._busy_ui = False
        self._recording_ui = False
        self._prepared_model = None
        self.selector = ttk.Combobox(self, state="readonly", width=60)
        self.selector.grid(row=0, column=0, padx=8, pady=5, sticky="ew")
        self.refresh_button = ttk.Button(self, text="Ververs microfoons", command=self.refresh)
        self.refresh_button.grid(row=0, column=1, padx=8)
        choices = ttk.Frame(self)
        choices.grid(row=1, column=0, columnspan=2, padx=8, sticky="w")
        ttk.Label(choices, text="Spraakmodel:").pack(side="left")
        self.model = ttk.Combobox(choices, values=("tiny", "base", "small"), state="readonly", width=8)
        self.model.set("base")
        self.model.pack(side="left", padx=8)
        self.model.bind("<<ComboboxSelected>>", lambda event: self._controls())
        self.load_button = ttk.Button(choices, text="Laad lokaal model", command=lambda: self.prepare(False))
        self.load_button.pack(side="left", padx=4)
        self.download_button = ttk.Button(choices, text="Download model", command=lambda: self.prepare(True))
        self.download_button.pack(side="left", padx=4)
        self.audio_only = tk.BooleanVar(value=False)
        self.test_button = ttk.Checkbutton(choices, text="Alleen audiotest", variable=self.audio_only,
                                          command=self._controls)
        self.test_button.pack(side="left", padx=8)
        self.start_button = ttk.Button(self, text="Start luisteren", command=self.start, state="disabled")
        self.start_button.grid(row=2, column=0, padx=8, pady=5, sticky="w")
        self.stop_button = ttk.Button(self, text="Stop luisteren", command=self.stop, state="disabled")
        self.stop_button.grid(row=2, column=1, padx=8)
        self.meter = ttk.Progressbar(self, maximum=60)
        self.meter.grid(row=3, column=0, columnspan=2, padx=8, pady=5, sticky="ew")
        self.status = tk.StringVar(value="Ververs microfoons. Download het model eenmaal, daarna lokaal laden.")
        self.speech_status = tk.StringVar(value="Gesprek blijft lokaal. Alleen de modeldownload gebruikt internet.")
        self.warning = tk.StringVar(value="")
        for row, variable in ((4, self.status), (5, self.speech_status), (6, self.warning)):
            ttk.Label(self, textvariable=variable, wraplength=900).grid(
                row=row, column=0, columnspan=2, padx=8, pady=2, sticky="w")
        ttk.Label(self, text="Transcript — controleer herkenningsfouten; sprekerherkenning is nog niet aanwezig.").grid(
            row=7, column=0, columnspan=2, padx=8, pady=4, sticky="w")
        frame = ttk.Frame(self)
        frame.grid(row=8, column=0, columnspan=2, padx=8, sticky="nsew")
        self.transcript = tk.Text(frame, height=7, wrap="word")
        scroll = ttk.Scrollbar(frame, command=self.transcript.yview)
        self.transcript.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.transcript.pack(fill="both", expand=True)
        self.clear_button = ttk.Button(self, text="Wis transcript", command=lambda: self.transcript.delete("1.0", "end"))
        self.clear_button.grid(row=9, column=0, padx=8, pady=5, sticky="w")
        ttk.Label(self, text="Stop verwerkt ook het laatste korte audiofragment. Sluiten verwerpt resterende audio. "
                  "Tekst en audio worden niet naar bestanden geschreven.", wraplength=900).grid(
            row=10, column=0, columnspan=2, padx=8, pady=4, sticky="w")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(8, weight=1)
        self._controls()
        self._poll()

    def _controls(self):
        busy = self._busy_ui or self.session.busy
        for widget in (self.refresh_button, self.load_button, self.download_button, self.test_button, self.clear_button):
            widget.configure(state="disabled" if busy else "normal")
        self.selector.configure(state="disabled" if busy else "readonly")
        self.model.configure(state="disabled" if busy else "readonly")
        ready = self.session.transcriber is not None and self._prepared_model == self.model.get()
        can_start = bool(self.devices) and not busy and (self.audio_only.get() or ready)
        self.start_button.configure(state="normal" if can_start else "disabled")
        self.stop_button.configure(state="normal" if self._recording_ui else "disabled")

    def refresh(self):
        try:
            self.devices = self.device_loader()
        except AudioError as exc:
            self.devices = ()
            self.status.set(str(exc))
        self.selector["values"] = [device.label for device in self.devices]
        if self.devices:
            self.selector.current(next((i for i, d in enumerate(self.devices) if d.is_default), 0))
            self.status.set("Microfoon gereed. Laad een model of kies Alleen audiotest.")
        else:
            self.selector.set("")
            if not self.status.get().startswith("Microfoon"):
                self.status.set("Geen microfoon gevonden. Controleer aansluiting en Windows-toegang.")
        self._controls()

    def prepare(self, allow_download):
        self._prepared_model = None
        self.warning.set("")
        try:
            settings = SpeechSettings(model_name=self.model.get())
            self.session.prepare(settings, allow_download=allow_download)
        except Exception as exc:
            self.speech_status.set(str(exc))
            return
        self._busy_ui = True
        self.speech_status.set("Model downloaden/laden… dit kan enkele minuten duren." if allow_download
                               else "Lokaal model laden…")
        self._controls()

    def start(self):
        index = self.selector.current()
        if not 0 <= index < len(self.devices):
            return
        try:
            self.session.start(self.devices[index], transcribe=not self.audio_only.get())
        except Exception as exc:
            self.status.set(str(exc))
            messagebox.showerror("Opname starten", str(exc))
            return
        self.warning.set("")
        self._busy_ui = self._recording_ui = True
        self.speech_status.set("Alleen audiotest." if self.audio_only.get()
                               else "Luistert. Eerste tekst na ongeveer vijf seconden audio plus verwerkingstijd.")
        self._controls()

    def stop(self):
        self.session.stop()
        self._recording_ui = False
        self.speech_status.set("Opname stopt; resterende audio wordt verwerkt…")
        self._controls()

    def _poll(self):
        if self._closed:
            return
        for event in self.session.events():
            if event.kind == "text":
                self.transcript.insert("end", event.text + "\n")
                self.transcript.see("end")
            elif event.kind == "warning":
                self.warning.set(event.text)
            elif event.kind == "ready":
                self._prepared_model = self.model.get()
                self.speech_status.set(event.text)
            elif event.kind in ("error", "timing", "stopped"):
                (self.warning if event.kind == "error" else self.speech_status).set(event.text)
            if event.kind == "stopped":
                self._recording_ui = False
                self.status.set("Microfoon gestopt.")
                self.meter["value"] = 0
        state = self.recorder.snapshot()
        if state.running:
            self.meter["value"] = state.level_db + 60
            self.status.set(f"Luistert — {state.seconds:.0f} s — {state.level_db:.0f} dBFS — "
                            f"{state.buffered_chunks} fragmenten wachten. " + state.warning)
        self._busy_ui = self.session.busy
        self._controls()
        self._after_id = self.after(100, self._poll)

    def close(self):
        self._closed = True
        if self._after_id is not None:
            self.after_cancel(self._after_id)
        self.session.close()
