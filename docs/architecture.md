# Architectuur en uitbreidingscontracten

`main` start; `bootstrap` verbindt; `ConsultationService` coördineert. De UI roept
alleen de service aan. Extractie en analyse importeren geen UI-code.

## Gespreksinformatie

Een extractor levert `Fact`-objecten met onderwerp, status, bewijs, persoon en
periode. De demo leest expliciete regels. Een toekomstige lokale AI-extractor
implementeert hetzelfde `extract(transcript)`-contract en wordt in `bootstrap`
gekozen. Bewijs moet terug te vinden zijn in de invoer; AI-uitvoer wordt gevalideerd.
Spreker en persoon zijn verschillende begrippen: een therapeut kan informatie over
de patiënt noemen. Onbekende personen of tijdsreferenties mogen niet stilzwijgend
als actuele patiëntinformatie worden behandeld.

De service verwerkt steeds het volledige consult opnieuw. Ze leegt haar toestand
per analyse. De huidige conservatieve conflictregel maakt tegengestelde statussen
onduidelijk; een latere expliciete correctie vereist een uitgebreider tijdmodel.

## Kennis en adviezen

`knowledge/demo.json` bevat uitsluitend demonstratievragen, met bron en versie.
Voor echte regels komen klachtmodules met doelgroep, toepasbaarheid, voorwaarden,
bronpassage, versie, reviewstatus en uitzonderingen. Een lichamelijke test moet
passen bij een expliciete onderzoeksvraag. Een verwijssuggestie vereist daarnaast
brononderbouwde aanleiding, passende bestemming en urgentie. Een taalmodel mag
ontbrekende broninhoud niet invullen. De huidige demonstratiereasoner geeft geen
klinische test- of verwijsadviezen.

## Audio en snelheid

`Transcriber.transcribe(audio_path)` is het eerste aansluitpunt; de implementatie
is nog niet aanwezig. Live audio gebruikt nu een aparte recorder, chunkbuffer en achtergrondworker.
Sprekerherkenning en transcriptie zijn nog niet aangesloten. Zware verwerking mag het venster niet blokkeren.
Eerst meten we transcriptkwaliteit en verwerkingstijd op de CPU-laptop.

## Configuratie en distributie

Kennis wordt via `importlib.resources` geladen, onafhankelijk van de werkmap.
De desktop heeft geen netwerk- of bestandsopslagfunctie. Latere modellen blijven lokaal;
modelpaden, versies en instellingen komen in aparte configuratie. PyInstaller
neemt de pakketdata mee. Geen modeldownloads tijdens een consult.

## Verificatie

Tests bewaken ontkenning, onzekerheid, andere personen, verleden, tegenstrijdige
informatie, lege invoer en onafhankelijkheid van opeenvolgende consulten. De
fictieve demo toetst programmagedrag en bewijst geen klinische betrouwbaarheid.
