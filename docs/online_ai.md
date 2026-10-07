# Online AI proberen met fictieve gesprekken

De online proef herkent voorgestelde patiëntinformatie en selecteert relevante vervolgvragen uit de conceptmodule voor de lage rug. Zij gebruikt OpenAI via HTTPS. Er hoeven geen extra Python-pakketten of AI-programma's te worden geïnstalleerd. De microfoon en lokale spraakherkenning blijven werken zoals eerder.

## Eerste proef op Windows

1. Merge de pull request voor de online AI-koppeling in GitHub.
2. Download de nieuwe projectversie en open de terminal in die map. Bij een eerder gedownloade ZIP worden bestaande lokale bestanden niet automatisch bijgewerkt.
3. Gebruik je bestaande Python-omgeving waarin de app al werkte. Als je een nieuwe projectmap gebruikt en de oude versie editable was geïnstalleerd, koppel de omgeving opnieuw aan de nieuwe map:

```powershell
conda activate reasoning_assistent
python -m pip install -e .
python main.py
```

Deze nieuwe koppeling vraagt geen aanvullende afhankelijkheden. Voor spraak moeten de eerder geïnstalleerde speech-afhankelijkheden aanwezig blijven; `-e .` installeert die niet opnieuw.

4. Maak of gebruik een OpenAI API-project via [het platform](https://platform.openai.com/). Zorg voor beschikbaar API-tegoed/billing en maak een API-sleutel. Een sleutel geeft alleen toegang tot de modellen die voor jouw project beschikbaar zijn. Houd het gebruik klein en controleer het verbruik in het platform.
5. Open het tabblad **Online AI-proef (fictief)**.
6. Vul je sleutel in het gemaskeerde veld in. Hij wordt niet door de app opgeslagen. Laat voor de eerste proef model `gpt-4.1-mini` staan; modeltoegang kan per account verschillen.
7. Gebruik het reeds ingevulde fictieve voorbeeld. Markeer dat deze tekst fictief is en online verwerkt mag worden.
8. Klik op **Analyseer fictief gesprek online**.

De eerste echte API-aanvraag moet op jouw laptop worden getest. In de ontwikkeling zijn alleen offline tests met nagebootste antwoorden uitgevoerd, zonder echte sleutel of kosten. Ook de Windows-interface en .exe-build zijn in deze wijziging niet op Windows getest.

Een API-sleutel hoef je nooit aan de ontwikkelaar te geven. Deel hem niet in chat, screenshots of GitHub.

## Verwachte uitkomst

Je ziet voorgestelde informatie met letterlijke citaten, relevante vragen met een korte AI-reden en bijbehorende bronnen waar beschikbaar, plus onzekerheden. De exacte selectie kan per aanvraag verschillen. Er geldt een maximum van 16.000 tekens per proef; langere tekst wordt niet stilzwijgend afgekapt.

Het voorbeeld bevat onder andere een beginmoment, activiteitshinder, eerdere klachten en een negatieve uitspraak over tintelingen. Dat is geen ontkenning van iedere mogelijke neurologische klacht. Controleer vooral of de AI:

- Een therapeutvraag niet als patiëntantwoord gebruikt.
- Actuele klachten onderscheidt van eerdere episodes of klachten van anderen.
- Samengestelde onderwerpen niet als volledig beantwoord behandelt na één deelantwoord.
- Niet genoemde informatie openlaat.

De app verwerpt het hele antwoord bij onder andere een onbekende vraag-ID, extra uitvoervelden, een onvolledig API-antwoord of een citaat dat niet letterlijk in de invoer voorkomt. Dat bewijst niet dat een wel geaccepteerd antwoord inhoudelijk klopt. Er is geen automatische bevestiging van de spreker, de betekenis of medische volledigheid. Deze proef geeft geen diagnose-, behandel-, test- of verwijssuggesties.

## Een gesproken fictief gesprek proberen

1. Spreek een volledig verzonnen consult in op het bestaande transcriptietabblad.
2. Stop bij voorkeur de opname zodat de laatste fragmenten verwerkt zijn.
3. Open de AI-proef en klik op **Kopieer gesproken fictief transcript**.
4. Controleer de tekst. Voeg waar je dat betrouwbaar weet sprekerlabels toe, bijvoorbeeld `Fysiotherapeut:` en `Patiënt:`.
5. Markeer de fictieve status en klik op Analyseer.

Er is nog geen sprekerherkenning in de spraakpipeline. De AI mag bij een onduidelijke spreker geen zekerheid suggereren. Kopiëren en spreken versturen niets naar de online AI: alleen de analyseknop doet dat. Tijdens een aanvraag blijven de andere tabbladen bruikbaar. Het resultaat hoort bij de tekst zoals die op het moment van klikken was; een latere tekstwijziging vraagt een nieuwe analyse.

## Wat wordt verstuurd en opgeslagen?

De aanvraag bevat de ingevoerde fictieve tekst en een selectie uit de kennisbank: vragen, context, hypothesen en interpretatiegrenzen. Audio, modelbestanden en andere lokale bestanden worden niet meegestuurd. Er worden geen aanvullende web-, tool- of bestandsaanroepen door het model aangevraagd.

De app schrijft sleutel, transcript en AI-resultaat niet naar bestanden. De sleutel blijft tijdens gebruik in procesgeheugen; dit is geen garantie van forensisch wissen. Ook de werkcomputer kan eigen organisatiebeleid of monitoring hebben.

De aanvraag gebruikt `store: false`. Dit is **geen garantie dat de aanbieder niets bewaart**: er kunnen bijvoorbeeld monitoringlogs worden bewaard volgens de accountinstellingen en het beleid van de aanbieder. Daarom blijft deze versie uitsluitend een fictieve proef.

Een aanvraag die al is verstuurd kan niet worden teruggehaald door het venster te sluiten. Er wordt niet automatisch opnieuw geprobeerd bij een fout. Als je zelf opnieuw klikt, kan dat een nieuwe betaalde aanvraag zijn, ook wanneer het vorige antwoord door een timeout niet zichtbaar werd.

## Als het niet werkt

| Melding | Volgende stap |
| --- | --- |
| API-sleutel niet geaccepteerd | Controleer of de sleutel bij een geldig API-project hoort en opnieuw correct is ingevuld |
| Model niet beschikbaar / aanvraag geweigerd | Controleer projecttoegang en kies zo nodig een model dat Responses en Structured Outputs ondersteunt |
| Limiet of API-tegoed bereikt | Controleer API-billing, beschikbaar tegoed en gebruikslimieten |
| Geen verbinding | Het werknetwerk, de proxy of certificaatconfiguratie kan toegang blokkeren; vraag IT om een toegestane verbinding naar `api.openai.com` |
| Aanvraag duurt te lang | Er is een netwerktimeout van 45 seconden; probeer met kortere fictieve tekst en houd rekening met mogelijke kosten van de eerdere aanvraag |
| Citaat of structuur ongeldig | Er wordt geen resultaat gebruikt; controleer de invoer en probeer eventueel opnieuw |

Schakel certificaatcontrole of andere beveiliging van je werklaptop niet uit. Een API-koppeling die geen installatie vraagt, kan nog steeds onder werkbeleid vallen.

## Later lokaal draaien

De applicatie hangt niet rechtstreeks aan OpenAI. Er zijn afzonderlijke onderdelen:

| Onderdeel | Verantwoordelijkheid |
| --- | --- |
| `ai/contracts.py` | Vast backendcontract en uitvoerschema |
| `ai/prompts.py` | Instructies en selectie van kennis/context |
| `ai/openai_backend.py` | Alleen de huidige HTTPS-koppeling |
| `ai/service.py` | Grenzen, uitvoercontrole en verbinden aan vaste vragen/bronnen |
| `ui/ai_panel.py` | Handmatige bediening en achtergrondaanvraag |
| `bootstrap.py` | Samenstellen van de gekozen implementatie |

Een lokaal model krijgt later een backend met dezelfde `generate(instructions, payload, schema)`-interface. Het uitvoercontract en de kennisbank kunnen dan hetzelfde blijven. De prompt, contextlengte en kwaliteit moeten opnieuw worden getest voor het gekozen lokale model; gelijkwaardige prestaties zijn niet gegarandeerd. De huidige fictief-beperking blijft actief totdat een afzonderlijke klinische integratie is beoordeeld.

Voor de lokale keuze moeten we eerst RAM, beschikbare CPU-capaciteit naast Whisper en toegestane software op jouw werklaptop vaststellen. Daarvoor installeren we nu niets.

## Officiële documentatie

Geraadpleegd op 7 oktober 2026:

- [OpenAI API-overzicht en authenticatie](https://developers.openai.com/api/reference/overview)
- [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [GPT-4.1 mini: Responses en Structured Outputs](https://developers.openai.com/api/docs/models/gpt-4.1-mini)
- [Gegevensverwerking en retentie](https://developers.openai.com/api/docs/guides/your-data)
