# Reasoning assistent

Modulair Python-prototype voor een lokale fysiotherapeutische consultassistent.
Doel: gesprekken volgen, informatie structureren, vergelijken met gecontroleerde
kennisbronnen en onderbouwde suggesties tonen.

## Wat werkt nu?

Een lokaal venster met fictieve tekst, expliciet gestructureerde feiten en
voorbeeldvragen bij ontbrekende of onduidelijke informatie. Vier toestanden:
`niet_besproken`, `aanwezig`, `ontkend`, `onduidelijk`. Ontkenning is geen ontbrekende
informatie. Uitspraken over anderen of het verleden vullen actuele patiëntfeiten
niet in. Tegenstrijdige statussen vragen om verduidelijking.

**Dit is een architectuurdemo.** Vrije gesprekstekst wordt nog niet door AI
geïnterpreteerd; microfoon, spraakherkenning, lichamelijke-testadviezen en
verwijsadviezen zijn nog niet geïmplementeerd. De kennis bevat alleen expliciet
ongereviewde demonstratievragen, geen klinische richtlijnregels.

## Starten op Windows

Gebruik Python 3.10 of nieuwer met Tkinter. Open de terminal in deze projectmap:

```powershell
python main.py
```

Zonder venster:

```powershell
python main.py --demo
python -m unittest discover -s tests -v
```

De basis gebruikt alleen de standaardbibliotheek. Optioneel installeren als pakket:

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
| `audio/` | Aansluitpunt voor lokale spraakherkenning |
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
python -m pip install -e .
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
4. Microfoon en lokale transcriptie, daarna prestatie- en foutmetingen op de laptop.
5. Klinische test-/overleg-/verwijssuggesties met bron, onzekerheid en urgentie.
6. Windows-distributie en lokale gebruikstest.

De huidige app bewaart geen consulten en doet geen netwerkverzoeken.
Gebruik fictieve gegevens voor ontwikkeltests. Opnames, patiëntgegevens en
modelbestanden horen niet in deze openbare repository.
