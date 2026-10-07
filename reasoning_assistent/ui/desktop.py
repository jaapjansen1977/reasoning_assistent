"""Lokale tekstinterface. Geen consultopslag of netwerkverkeer."""
import tkinter as tk
from tkinter import ttk, messagebox
from ..application import ConsultationService
from ..demo import DEMO_TRANSCRIPT


def launch(service: ConsultationService) -> None:
    root = tk.Tk()
    root.title("Reasoning assistent — prototype")
    root.geometry("1000x750")
    ttk.Label(root, text="DEMO — tekstprototype; AI en microfoon nog niet aangesloten",
              wraplength=950).pack(padx=16, pady=10, anchor="w")
    ttk.Label(root, text="Demo-invoer: onderwerp | status | bewijs. Vrije tekst wordt nog niet geïnterpreteerd.",
              wraplength=950).pack(padx=16, anchor="w")
    transcript = tk.Text(root, height=12, wrap="word")
    transcript.pack(padx=16, pady=8, fill="both", expand=True)
    transcript.insert("1.0", DEMO_TRANSCRIPT)
    output = tk.Text(root, height=17, wrap="word", state="disabled")

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

    ttk.Button(root, text="Analyseer demo-informatie", command=analyze).pack(padx=16, pady=8, anchor="w")
    output.pack(padx=16, pady=8, fill="both", expand=True)
    root.mainloop()
