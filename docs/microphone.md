# Microfoon testen op Windows

Dit beschrijft de modus **Alleen audiotest**. Voor transcriptie zie [speech.md](speech.md).

1. Download of checkout de branch `feature/local-speech`.
2. Open een terminal in de projectmap, in de Python-omgeving die je wilt gebruiken.
3. Installeer met `python -m pip install -e ".[audio]"`.
4. Start met `python main.py`.
5. Klik **Ververs microfoons** en kies je microfoon. De Windows-standaard heeft een label.
6. Vink **Alleen audiotest** aan en klik **Start luisteren**. Spreek: de meter en verstreken tijd moeten veranderen.
7. Controleer of beide gesprekspartners hoorbaar zijn via de meter; deze test zegt
   nog niets over verstaanbaarheid of transcriptiekwaliteit.
8. Klik **Stop luisteren**. De meter gaat terug naar nul en de buffer wordt gewist.
9. Start opnieuw en sluit tijdens luisteren het venster; de microfoon hoort vrij te komen.

## Als het niet werkt

- Windows 11: Instellingen → Privacy en beveiliging → Microfoon. Controleer
  microfoontoegang en **Bureaublad-apps toegang tot uw microfoon geven**.
- Op een beheerde laptop kunnen organisatie-instellingen toegang blokkeren.
- Controleer het invoerniveau ook in Windows-geluidsinstellingen.
- Bij exclusief gebruik door een andere app: sluit die app of kies een andere microfoon.
- Dezelfde fysieke microfoon kan via meerdere Windows-audio-API's verschijnen;
  kies eerst de standaard, probeer daarna een andere vermelding.
- Bij ontbrekende module: controleer of pip en de app dezelfde Python-omgeving gebruiken.
- Bij een audiowaarschuwing kan informatie ontbreken. Stop en herstart; behandel een
  later transcript nooit als compleet als de audiostream onderbroken is.

## Modules

`devices.py` vindt invoerapparaten en controleert de backend. `recorder.py` opent
mono PCM16 op de eigen samplefrequentie, ontvangt kleine blokken via een begrensde
queue en berekent RMS-niveau op een achtergrondthread. `buffer.py` bewaart maximaal
zes fragmenten van vijf seconden. `ui/microphone.py` toont bediening en leest status
elke 100 ms. Geen Tk-aanroepen vanuit de audio-thread.

Het callback-pad slaat geen bestanden op en blokkeert niet op een volle queue.
Volle queues worden gemeld. Oudere voltooide fragmenten worden normaal vervangen,
wanneer Alleen audiotest aanstaat; in de spraakmodus worden ze door de worker opgehaald. Die worker gebruikt
`recorder.pop_chunk()` en resamplen naar de frequentie van het STT-model.

## Verificatie

33 geautomatiseerde tests controleren consult- en audiogedrag met een gesimuleerde
backend. Er is in de ontwikkelomgeving geen fysieke microfoon of Windows beschikbaar.
De echte stream, desktopbediening en Windows-build moeten lokaal worden getest.

Bronnen voor de implementatie:
- https://python-sounddevice.readthedocs.io/en/latest/api/raw-streams.html
- https://python-sounddevice.readthedocs.io/en/latest/api/checking-hardware.html
- https://support.microsoft.com/nl-nl/windows/privacy/turn-on-app-permissions-for-your-microphone-in-windows
