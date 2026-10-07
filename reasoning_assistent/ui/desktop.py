"""Lokale consultinterface. Modelvoorbereiding en klinische demo zijn gescheiden."""
import tkinter as tk
from tkinter import ttk, messagebox
from ..application import ConsultationService
from ..demo import DEMO_TRANSCRIPT
from .microphone import MicrophonePanel
from .ai_panel import AIPanel


def launch(service: ConsultationService) -> None:
    root = tk.Tk()
    root.title("Reasoning assistent — prototype")
    root.geometry("1100x950")
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)
    speech_tab = ttk.Frame(notebook)
    demo_tab = ttk.Frame(notebook)
    notebook.add(speech_tab, text="Gesprek en transcriptie")
    notebook.add(demo_tab, text="Tekstdemo klinisch redeneren")
    microphone = MicrophonePanel(speech_tab)
    microphone.pack(padx=16, pady=8, fill="both", expand=True)

    ai_tab = ttk.Frame(notebook)
    notebook.add(ai_tab, text="Online AI-proef (fictief)")
    ai_panel = AIPanel(ai_tab, lambda: microphone.transcript.get("1.0", "end-1c"))
    ai_panel.pack(padx=16, pady=12, fill="both", expand=True)

    def close():
        ai_panel.close()
        microphone.close()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", close)
    ttk.Label(demo_tab, text="Tekstdemo voor klinisch redeneren — los van het gesproken transcript",
              wraplength=950).pack(padx=16, pady=10, anchor="w")
    ttk.Label(demo_tab, text="Demo-invoer: onderwerp | status | bewijs. Vrije tekst wordt nog niet geïnterpreteerd.",
              wraplength=950).pack(padx=16, anchor="w")
    transcript = tk.Text(demo_tab, height=12, wrap="word")
    transcript.pack(padx=16, pady=8, fill="both", expand=True)
    transcript.insert("1.0", DEMO_TRANSCRIPT)
    output = tk.Text(demo_tab, height=17, wrap="word", state="disabled")

    def analyze():
        try:
            result = service.analyze(transcript.get("1.0", "end-1c"))
        except ValueError as exc:
            messagebox.showerror("Invoer controleren", str(exc))
            return
        lines = ["Demonstratievragen (geen richtlijnadviezen):"]
        for item in result.suggestions:
            lines.extend(["", item.question, item.reason,
                          f"Bron: {item.source.title} — {item.source.version}"])
        if not result.suggestions:
            lines.append("Geen ontbrekende demo-onderwerpen; dit is geen beoordeling van klinische veiligheid.")
        output.configure(state="normal")
        output.delete("1.0", "end")
        output.insert("1.0", "\n".join(lines))
        output.configure(state="disabled")

    ttk.Button(demo_tab, text="Analyseer demo-informatie", command=analyze).pack(padx=16, pady=8, anchor="w")
    output.pack(padx=16, pady=8, fill="both", expand=True)
    root.mainloop()
