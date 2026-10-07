# Lokale Nederlandse spraakherkenning

## Starten

Download de branch `feature/local-speech`. Open een terminal in de uitgepakte map:

```powershell
python -m pip install -e ".[speech]"
python main.py
```

Gebruik bij voorkeur een eigen Python-omgeving om andere projecten niet te beïnvloeden.
De speech-extra installeert sounddevice, faster-whisper, NumPy, SciPy en bijbehorende
afhankelijkheden. GPU-software is niet nodig voor deze CPU-instelling.

1. Open **Gesprek en transcriptie** en klik **Ververs microfoons**.
2. Kies de eerder geteste microfoon.
3. Laat het model op **base** staan. Klik de eerste keer op **Download model**.
   Hiervoor is internet nodig; er wordt geen gesprek gestart of geüpload.
4. Wacht tot **Model base gereed** verschijnt. De voorbereiding kan enkele minuten duren.
5. Zorg dat **Alleen audiotest** niet aangevinkt is en klik **Start luisteren**.
6. Spreek twintig tot dertig seconden in het Nederlands. Tekst verschijnt per
   vijf seconden audio, plus de verwerkingstijd. Dit is geen woord-voor-woord-streaming.
7. Klik **Stop luisteren** en wacht tot resterende audio verwerkt is.
8. Voor een nieuw consult: klik **Wis transcript** voordat je weer start.

De tekst is bewerkbaar, wordt niet opgeslagen en blijft na Stop zichtbaar.
Zonder wissen wordt een volgende opname toegevoegd aan dezelfde tekst.
Sluiten verwerpt resterende audio en late resultaten. Een al actieve native
modelberekening kan niet onmiddellijk worden onderbroken.

## Offline gebruik

Modelbestanden staan op Windows in `%LOCALAPPDATA%/ReasoningAssistent/models/base`
(of de gekozen modelnaam). Ze staan buiten de repository en blijven na een nieuwe
ZIP-download beschikbaar. Op andere systemen is het pad onder de eigen `.cache`.

Na de eerste modeldownload kun je de app opnieuw starten zonder internet. Klik
**Laad lokaal model**. Dat pad staat geen modeldownload toe; alle benodigde
modelbestanden, inclusief tokenizer, moeten vooraf lokaal aanwezig zijn.

Alleen de expliciete modeldownload gebruikt netwerktoegang. Microfoonaudio wordt
lokaal resampled en door het lokale CPU-model verwerkt; niets wordt naar een
spraak-API gestuurd. De app schrijft geen audio of transcript naar bestanden.

## Modellen en snelheid

`tiny`, `base` en `small` zijn meertalige Whisper-modellen. We starten met `base`;
vergelijk op dezelfde voorbeeldzinnen of `tiny` voldoende herkenning biedt en of
`small` op jouw laptop voldoende snel is. Voor elk model is een aparte download nodig.

De status toont verwerkingstijd ten opzichte van fragmentduur. Een factor boven
1 betekent dat dat fragment langer kostte dan de audio duurde. De buffer bewaart
maximaal ongeveer 30 seconden voltooide fragmenten; bij aanhoudende vertraging
kunnen oude fragmenten wegvallen. De app meldt dit en beschouwt het transcript
als onvolledig. Probeer dan een kleiner model en herhaal de test.

## Beperkingen en praktijktest

De herkenner onderscheidt therapeut en patiënt nog niet. Vijfsecondenfragmenten
worden afzonderlijk verwerkt; woorden op grenzen kunnen ontbreken of fout zijn.
VAD slaat stilte over, maar voorkomt niet alle verzonnen of verkeerd herkende tekst.
Let bij de proef vooral op ontkenningen, getallen en fysiotherapeutische termen.
De klinische tekstdemo staat in een ander tabblad en analyseert deze transcriptie
nog niet automatisch. Koppeling naar betrouwbare klinische extractie volgt later.

Test met fictieve zinnen, bijvoorbeeld:
- Ik heb sinds drie weken last van mijn onderrug.
- Ik heb geen tintelingen in mijn linkerbeen.
- De pijn is zes op tien als ik lang zit.
- Ik wil weer kunnen tuinieren.

Vergelijk letterlijk, probeer ook een stilte en een korte opname onder vijf seconden.
Controleer dat Stop de laatste woorden verwerkt en dat opnieuw starten werkt.
Controleer daarna offline laden na een herstart.

## Hergebruik en onderhoud

`whisper_backend.py` is onze kleine adapter op de bestaande bibliotheek
[SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper).
`preprocessing.py` verzorgt PCM16 → float32, 16 kHz met SciPy-resampling.
`settings.py` beheert modelkeuze en paden. `session.py` regelt threads, gebeurtenissen,
stoppen en achterstand. De GUI kent de details van het spraakmodel niet.

Een andere backend implementeert `ChunkTranscriber.transcribe_chunk(AudioChunk)` en
levert `TranscriptResult`. Via `SpeechSession(prepare=...)` kan die worden vervangen.
`whisper.cpp` en uitgebreidere streamingprojecten zijn mogelijke vervolgstappen;
deze versie installeert ze niet.

## Verificatie en distributie

De tests controleren dat geen model automatisch wordt gedownload, dat de CPU-instelling
gebruikt wordt en dat audio/staat bij Stop/Close correct worden verwerkt. Resampling
wordt getest met echte NumPy/SciPy; inferentie en download worden gesimuleerd.
Een echte modeldownload, Nederlandse herkenning, fysieke microfoon en Windows-executable
moeten lokaal worden getest. Het PyInstaller-script neemt backendassets mee, maar
het model staat apart in de gebruikersmap en wordt niet in de executable gebundeld.

Bronnen:
- https://github.com/SYSTRAN/faster-whisper
- https://github.com/SYSTRAN/faster-whisper/blob/master/faster_whisper/utils.py
- https://github.com/ggml-org/whisper.cpp
- https://github.com/ufal/whisper_streaming
