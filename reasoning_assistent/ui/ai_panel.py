"""Manual fictional online experiment; background worker never touches Tk."""
import os
import queue
import threading
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from typing import Callable
from ..ai.contracts import AIError
from ..ai.demo import FICTIONAL_TRANSCRIPT
from ..ai.openai_backend import DEFAULT_MODEL
from ..ai.service import format_analysis
from ..bootstrap import build_ai_service


class AIPanel(ttk.Frame):
    def __init__(self, master, get_speech_transcript: Callable[[], str]):
        super().__init__(master)
        self._get_speech_transcript = get_speech_transcript
        self._closed = False
        self._busy = False
        self._events = queue.Queue(maxsize=1)
        self._after_id = None
        self.status = tk.StringVar(value='Geen tekst verstuurd. Begin met het fictieve voorbeeld.')
        self.fictional = tk.BooleanVar(value=False)
        self.api_key = tk.StringVar(value=os.environ.get('OPENAI_API_KEY', ''))
        self.model = tk.StringVar(value=os.environ.get('REASONING_AI_MODEL', DEFAULT_MODEL))
        ttk.Label(self, text='Online AI-proef — lage rug — uitsluitend fictieve gesprekken',
                  font=('Segoe UI', 12, 'bold')).pack(anchor='w', pady=(0, 6))
        ttk.Label(self, text='Bij Analyseer verstuur je de tekst hieronder en conceptkennis naar OpenAI. '
                  'Audio wordt niet meegestuurd. API-gebruik kan kosten met zich meebrengen. '
                  'De uitkomst is een proef met vervolgvragen, geen klinisch advies.',
                  wraplength=950).pack(anchor='w')
        settings = ttk.Frame(self)
        settings.pack(fill='x', pady=8)
        ttk.Label(settings, text='API-sleutel (alleen in geheugen):').grid(row=0, column=0, sticky='w')
        ttk.Entry(settings, textvariable=self.api_key, show='*', width=50).grid(row=0, column=1, sticky='ew', padx=8)
        ttk.Label(settings, text='Model:').grid(row=1, column=0, sticky='w', pady=4)
        ttk.Entry(settings, textvariable=self.model, width=35).grid(row=1, column=1, sticky='w', padx=8)
        settings.columnconfigure(1, weight=1)
        ttk.Label(self, text='Je hebt een OpenAI API-account met beschikbaar tegoed nodig. '
                  'Deel de sleutel niet in chat, screenshots of GitHub.', wraplength=950).pack(anchor='w')
        self.transcript = ScrolledText(self, height=11, wrap='word')
        self.transcript.pack(fill='both', expand=True, pady=8)
        self.transcript.insert('1.0', FICTIONAL_TRANSCRIPT)
        actions = ttk.Frame(self)
        actions.pack(fill='x')
        self.example_button = ttk.Button(actions, text='Laad fictief voorbeeld', command=self._example)
        self.example_button.pack(side='left')
        self.copy_button = ttk.Button(actions, text='Kopieer gesproken fictief transcript', command=self._copy)
        self.copy_button.pack(side='left', padx=8)
        ttk.Checkbutton(self, text='De tekst hierboven is fictief en mag voor deze proef online worden verwerkt.',
                        variable=self.fictional).pack(anchor='w', pady=8)
        self.analyze_button = ttk.Button(self, text='Analyseer fictief gesprek online', command=self._analyze)
        self.analyze_button.pack(anchor='w')
        ttk.Label(self, textvariable=self.status, wraplength=950).pack(anchor='w', pady=6)
        self.output = ScrolledText(self, height=16, wrap='word', state='disabled')
        self.output.pack(fill='both', expand=True)
        self._after_id = self.after(100, self._poll)

    def _set_text(self, text):
        self.transcript.delete('1.0', 'end')
        self.transcript.insert('1.0', text)
        self.fictional.set(False)
        self._show('')

    def _example(self):
        self._set_text(FICTIONAL_TRANSCRIPT)
        self.status.set('Fictief voorbeeld geladen; nog niet verstuurd.')

    def _copy(self):
        self._set_text(self._get_speech_transcript())
        self.status.set('Transcript gekopieerd; controleer dat het volledig fictief is. Nog niet verstuurd.')

    def _show(self, text):
        self.output.configure(state='normal')
        self.output.delete('1.0', 'end')
        self.output.insert('1.0', text)
        self.output.configure(state='disabled')

    def _controls(self):
        state = 'disabled' if self._busy else 'normal'
        for button in [self.analyze_button, self.example_button, self.copy_button]:
            button.configure(state=state)

    def _analyze(self):
        if self._busy or self._closed:
            return
        self._show('')  # Do not leave an older successful result beside a new error.
        if not self.fictional.get():
            self.status.set('Markeer eerst dat de tekst fictief is en online verwerkt mag worden.')
            return
        try:
            service = build_ai_service(self.api_key.get(), self.model.get())
            transcript = self.transcript.get('1.0', 'end-1c')
        except AIError as exc:
            self.status.set(str(exc))
            return
        self._busy = True
        self._controls()
        self.status.set('Fictieve tekst wordt online geanalyseerd; je kunt de andere tabbladen blijven gebruiken.')

        def work():
            try:
                result = service.analyze(transcript, fictional=True)
                event = ('result', format_analysis(result), transcript)
            except AIError as exc:
                event = ('error', str(exc), transcript)
            except Exception:
                # Avoid accidental credential/transcript leakage in error text.
                event = ('error', 'Onverwachte fout; geen AI-resultaat gebruikt.', transcript)
            self._events.put_nowait(event)

        threading.Thread(target=work, daemon=True, name='fictional-ai-request').start()

    def _poll(self):
        if self._closed:
            return
        try:
            kind, text, snapshot = self._events.get_nowait()
        except queue.Empty:
            pass
        else:
            self._busy = False
            self._controls()
            if kind == 'result':
                self._show(text)
                if snapshot != self.transcript.get('1.0', 'end-1c'):
                    self.status.set('Resultaat voor de eerdere tekst. De invoer is inmiddels veranderd; analyseer opnieuw voor deze tekst.')
                else:
                    self.status.set('Proefanalyse ontvangen. Controleer citaten, interpretatie en vervolgvragen.')
            else:
                self._show('')
                self.status.set(text)
        self._after_id = self.after(100, self._poll)

    def close(self):
        self._closed = True
        self.api_key.set('')
        if self._after_id is not None:
            self.after_cancel(self._after_id)
        # An already sent request cannot be recalled. Daemon worker terminates
        # with the app; socket timeout bounds the wait if the app stays alive.
