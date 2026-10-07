# Reasoning assistent

Modulair Python-prototype voor een lokale fysiotherapeutische consultassistent.
Doel: gesprekken volgen, informatie structureren, vergelijken met gecontroleerde
kennisbronnen en onderbouwde suggesties tonen.

## Wat werkt nu?

Een lokaal venster met microfoonkeuze, start-/stopknoppen, geluidsmeter en lokale
Nederlandse transcriptie via faster-whisper. Modellen: tiny, base en small.
Zie [spraakherkenning starten](docs/speech.md).
Spraakfragmenten verzamelen minstens acht seconden context en worden daarna
bij voorkeur op een pauze geknipt. Maximum instelbaar: 10, 15 of 20 seconden.
Daarnaast werkt de tekstdemo met fictieve tekst, expliciet gestructureerde feiten en
voorbeeldvragen bij ontbrekende of onduidelijke informatie. Vier toestanden:
`niet_besproken`, `aanwezig`, `ontkend`, `onduidelijk`. Ontkenning is geen ontbrekende
informatie. Uitspraken over anderen of het verleden vullen actuele patiëntfeiten
niet in. Tegenstrijdige statussen vragen om verduidelijking.

**Dit is een architectuurdemo.** Vrije gesprekstekst wordt nog niet door AI
geïnterpreteerd; lichamelijke-testadviezen en
verwijsadviezen zijn nog niet geïmplementeerd. De actieve demo gebruikt alleen expliciet
ongereviewde demonstratievragen, geen klinische richtlijnregels.

Daarnaast is er een [conceptkennisbank voor de lage rug](docs/knowledge/README.md),
met differentiaal, vervolgvragen en bronnen. Deze is nog niet verbonden aan de
adviesfunctie en vereist inhoudelijke review.

## Starten op Windows

Gebruik Python 3.10 of nieuwer met Tkinter. Open de terminal in deze projectmap.
Installeer de optionele spraak- en microfoonafhankelijkheden en start de app:

```powershell
python -m pip install -e ".[speech]"
python main.py
```

Zonder venster:

```powershell
python main.py --demo
python -m unittest discover -s tests -v
```

De tekstdemo gebruikt alleen de standaardbibliotheek en werkt ook zonder de audio- of speech-extra.
Voor alleen microfoontesten volstaat `python -m pip install -e ".[audio]"`.
Optioneel installeren als pakket zonder microfoonondersteuning:

```powershell
python -m pip install -e .
python -m reasoning_assistent
```

## Onderdelen afzonderlijk verbeteren

| Bestand / map | Verantwoordelijkheid |
| --- | --- |
| `main.py` | Start de applicatie |
| `reasoning_assistent/main.py` | Kies venster of tekstdemo |
| `bootstrap.py` | Kies en verbind implementaties |
| `application.py` | Laat de onderdelen samenwerken |
| `domain.py` | Gedeelde feiten, statussen, bronnen en suggesties |
| `ports.py` | Contracten voor vervangbare onderdelen |
| `audio/` | Microfoons, stream, geheugenbuffer en aansluitpunt voor spraakherkenning |
| `extraction/` | Gespreksinformatie structureren |
| `knowledge/` | Losse kennisbestanden en brongegevens |
| `reasoning/` | Informatie vergelijken en suggesties maken |
| `ui/` | Venster en presentatie |
| `tests/` | Gedrag controleren onafhankelijk van de interface |

Paden in de tabel zijn binnen `reasoning_assistent/`, behalve waar anders aangegeven.
Zie [architectuur](docs/architecture.md) voor uitbreiding.

## Later een Windows-app bouwen

Installeer PyInstaller in de ontwikkelomgeving op Windows:

```powershell
python -m pip install -e ".[speech]"
python -m pip install pyinstaller
powershell -ExecutionPolicy Bypass -File scripts/build_windows.ps1
```

Uitvoer: `dist/ReasoningAssistent/ReasoningAssistent.exe`. Deel de hele map,
want de executable gebruikt meegeleverde bestanden. Python hoeft op de
ontvangende computer niet apart geïnstalleerd te zijn. De build is voorbereid,
maar moet nog op Windows worden gebouwd en getest. Modelbestanden voor
latere STT/AI-versies worden apart beheerd.

## Ontwikkelvolgorde

1. Architectuur en fictieve testconsulten (deze versie).
2. Eén klachtmodule met controleerbare bronnen en beoordeelde regels.
3. Lokale AI-extractie met bewijsfragmenten; vergelijk tegen handmatig gelabelde consulten.
4. Microfoon en lokale transcriptie (aanwezig); prestatie- en foutmetingen op de laptop volgen.
5. Klinische test-/overleg-/verwijssuggesties met bron, onzekerheid en urgentie.
6. Windows-distributie en lokale gebruikstest.

De huidige app schrijft geen consulten of audio naar bestanden. Alleen de expliciete
modeldownload gebruikt internet; gesprekken worden volledig lokaal verwerkt.
In spraakmodus blijven maximaal vier volledige audiofragmenten plus een
onvolledig fragment in geheugen (standaard maximaal circa 75 seconden); oudere fragmenten worden vervangen.
Bij Stop wordt resterende audio getranscribeerd en de opnamebuffer geleegd;
bij sluiten wordt resterende audio verworpen. Tekst blijft na Stop zichtbaar. Bij achterstand kan de buffer fragmenten verliezen; dit wordt gemeld. Dit is geen volledige
consultopname en geen garantie van forensisch wissen uit RAM.
Zie [microfoon testen](docs/microphone.md) voor de praktijktest.
Gebruik fictieve gegevens voor ontwikkeltests. Opnames, patiëntgegevens en
modelbestanden horen niet in deze openbare repository.
