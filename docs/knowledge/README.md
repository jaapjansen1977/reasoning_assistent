# Regionale kennisbestanden

We starten met een brede **conceptmodule voor lage rug**: 30 aandoeningen, syndromen of pijnbronhypothesen, 37 herbruikbare vragen en 29 bronnen. Andere regio's staan in de index als `planned`; daarvoor is nog geen inhoud geschreven. De lage-rugmodule is niet uitputtend en vereist inhoudelijke review.

## Waar staat wat?

| Bestand | Doel |
| --- | --- |
| `reasoning_assistent/knowledge/regions/low_back.v1.json` | Bewerkbare inhoud voor latere AI-toepassing |
| `docs/knowledge/low_back.v1.md` | Volledige leesversie voor klinische review |
| `reasoning_assistent/knowledge/schemas/region.schema.json` | JSON Schema Draft 2020-12 voor dezelfde structuur bij volgende regio's |
| `reasoning_assistent/knowledge/regions/index.json` | Beschikbare en geplande regio's |
| `scripts/knowledge_tools.py` | Referentiecontrole en genereren van leesversies |

De bestanden worden meegenomen bij het installeren van het Python-pakket. De huidige demo en spraakherkenning gebruiken deze nieuwe kennis nog niet. Het aanpassen van een vlag in JSON activeert geen klinisch advies.

## Inhoud per aandoening

- Diagnostische aanwijzingen: bevindingen die een hypothese ondersteunen; geen verplichte verzameling symptomen.
- Risicofactoren: omstandigheden die de voorafkans kunnen beïnvloeden. Een risicofactor hoeft geen oorzaak te zijn.
- Vervolgvragen: verwijzingen naar een centrale vragenbank, met context en prioriteit.
- Onderzoek: wat gericht kan worden beoordeeld, waarom het relevant is en welke conclusies niet gerechtvaardigd zijn.
- Prognostische factoren: informatie over verloop; bij onvoldoende aandoeningsspecifieke onderbouwing staat die beperking vermeld.
- Therapeutisch beïnvloedbare factoren: fysiotherapeutische én medische aspecten, met vermelding van de verantwoordelijke zorgverlener.
- Overleg/verwijzing: conditionele aanleiding en urgentie, geen automatisch verwijsbesluit uit een diagnosewoord.
- Interpretatiegrenzen en bronnen: onzekerheid en de nog open inhoudelijke punten.

Algemene prognostische factoren voor LBP/LRS zijn eenmaal vastgelegd in een gedeeld profiel. Ze mogen niet automatisch op bijvoorbeeld een infectie, fractuur of maligniteit worden toegepast. Nociplastische pijn staat apart als mogelijke mechanismebijdrage, niet als orgaan-DD of verklaring op basis van stress alleen.

## Werkwijze voor latere AI-integratie

1. Haal uit het gesprek uitsluitend expliciete patiëntinformatie, met citaat, spreker, onderwerp, tijdscontext en onzekerheid. Een gestelde vraag is nog geen antwoord.
2. Laat de fysiotherapeut onzekere transcripties, negaties en kritieke veranderingen controleren. Onderscheid nieuw/verergerd van al langer bestaand.
3. Beoordeel veiligheidscontext eerst. Bij een plausibele spoedverdenking mag verder uitvragen of testen medische beoordeling niet vertragen.
4. Kies klinisch relevante hypotheses en bijbehorende vragen. De vragenbank is geen lijst die iedereen volledig moet beantwoorden.
5. Markeer per relevante vraag `not_discussed`, `present`, `denied`, `unclear` of gemotiveerd `not_applicable`. Niet genoemd betekent onbekend.
6. Toon een suggestie met reden, ontbrekende informatie, onzekerheid en bron. De fysiotherapeut besluit over aanvullende vragen, onderzoek en verwijzing.
7. Heropen beoordeling bij nieuwe informatie of veranderd beloop. Een eerdere ontkenning is geen permanente uitsluiting.

Er is bewust geen percentage 'volledig' of diagnostische score. Een gesprek kan veel vragen behandelen en toch één cruciaal signaal missen. Deze eerste versie bevat ook geen uitvoerbare beslisregels of automatische symptoommatching.

## Bewerken en controleren

Bewerk de JSON als bronbestand. Genereer daarna de leesversie vanuit de repositorymap:

```bash
python scripts/knowledge_tools.py --render
python -m unittest discover -s tests -v
```

Alleen de integriteit controleren:

```bash
python scripts/knowledge_tools.py
```

De controle gebruikt uitsluitend de Python-standaardbibliotheek. Zij controleert verplichte kernvelden, unieke IDs, verwijzingen en het uitgeschakeld blijven van conceptadvies. Het JSON Schema is daarnaast bedoeld voor editors en externe JSON Schema-validators; de standaardbibliotheekcontrole is geen volledige JSON Schema-validator. Geen van beide bewijst medische juistheid.

## Een volgende regio toevoegen

Maak bijvoorbeeld `regions/neck.v1.json` met dezelfde structuur en een eigen regio-ID. Gebruik het schema voor de velden; hergebruik nooit klakkeloos de lage-ruginhoud. Voeg expliciet toe:

- Populatie, setting, uitsluitingen, dekkingsgaten en versie.
- Gewone klinische syndromen, urgente oorzaken en relevante gerefereerde klachten.
- Een eigen vragenbank met stabiele IDs en context; niet een vaste hoeveelheid vragen per aandoening afdwingen.
- Bronnen per aandoening en beperkingen van tests, prognoses en behandeldoelen.
- `status: draft_requires_clinical_review`, `clinically_reviewed: false` en `automatic_advice_enabled: false`.

Werk vervolgens de index bij en genereer de leesversie. Bron-ID's zijn lokaal aan een regio; vraag-ID's zijn binnen die regio uniek. Gebruik bij latere koppeling samengestelde sleutels zoals `low_back:bladder` om naamconflicten te voorkomen.

## Review en versiebeheer

De lage-rugmodule is een eerste inhoudelijke synthese, niet een gevalideerd klinisch product. Met name actuele NHG-inhoud, Nederlandse verwijspaden, zeldzame spoedoorzaken en oudere specifieke bronnen moeten nog door inhoudsdeskundigen worden gecontroleerd. Voor sommige diagnoses is een betrouwbare individuele prognose niet beschikbaar in dit bestand; die is niet ingevuld met schijnzekerheid.

Leg wijzigingen vast met datum, reden en betrokken bronnen in Git. Voor klinische ingebruikname zijn inhoudelijke review, afzonderlijke integratie en toetsing met passende casuïstiek nodig. De huidige conceptschema's blijven data-only; een toekomstige gereviewde productversie krijgt een expliciet nieuw activerings- en validatieproces.

Sla geen patiënttranscripten of patiëntgegevens op in deze kennisbestanden of in GitHub.
