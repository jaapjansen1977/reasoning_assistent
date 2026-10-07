# Lage rug, bekken en gerefereerde klachten: differentiaal en anamneseleidraad

Versie 0.1.0 — 2026-10-07. Status: **concept; klinische review vereist**.

Deze leesversie wordt gegenereerd uit het JSON-bestand. Pas de JSON aan en genereer dit document opnieuw.

De module is nog niet gekoppeld aan automatische adviezen. Zij ondersteunt beoordeling door een fysiotherapeut; geen autonome diagnose of triage.

## Toepassingsgebied

Volwassenen in fysiotherapeutische eerstelijnscontext; geen zelfstandige diagnose- of triageapplicatie.

Brede eerste conceptmodule; niet uitputtend.

## Buiten de huidige dekking

- Kinderen en adolescenten vereisen aanvullende pediatrische veiligheidsmodule
- Postoperatieve revalidatie, implantaatcomplicaties en specifieke oncologische behandelprotocollen
- Alle buik-, gynaecologische, urologische en heuppathologieën als afzonderlijke volledige modules
- Prescriptieve medicatie-, operatie- of beeldvormingsbeslissingen

## Open inhoudelijke punten

- Actuele volledige NHG-standaarden niet toegankelijk tijdens controle; Nederlandse medische verwijspaden nog door inhoudsdeskundige harmoniseren
- Sommige zeldzame spoedpaden zijn alleen door algemene richtlijnen ondersteund; afzonderlijke actuele bronnen toevoegen
- Isthmische spondylolisthesis en oudere stenose/parsbronnen nader actualiseren
- Geen gevalideerde waarschijnlijkheidsberekening, testcombinatie-algoritme of volledigheidsscore
- Geen automatische negatieve conclusie uit afwezige transcriptinformatie

## Regels voor AI-gebruik

- Gebruik dit bestand om conditioneel vragen voor te stellen, niet om zelfstandig diagnoses te stellen
- Niet besproken betekent onbekend, nooit ontkend
- Een vraag van de therapeut is geen patiëntantwoord; voorbeeld, hypothese en familiegeschiedenis niet als actuele patiëntbevinding extraheren
- Bewaar letterlijk transcriptbewijs, spreker, subject, datum/tijd en nieuw versus bestaand; bij negatie- of transcriptietwijfel eerst verifiëren
- Veiligheidssignalen gaan voor volledigheid: geen onderzoek of lange checklist laten wachten op plausibele spoed
- Geen aantal vinkjes, symptoomtelling of bronloze kanspercentages gebruiken als diagnose
- Onderzoeksbevindingen alleen opslaan als daadwerkelijk uitgevoerd en expliciet beschreven; nooit uit spraak afleiden dat kracht/reflexen normaal zijn
- Verworpen hypotheses met reden en datum bewaren; bij verandering heropenen
- Risicofactor, prognostische factor, teken en behandelbare factor zijn verschillende rollen
- Geen algemene psychosociale verklaring gebruiken om medische pathologie uit te sluiten
- Een expliciete ontkenning of normaal onderzoek kan een specifieke aandoening niet altijd uitsluiten
- Advies toont reden, relevante ontbrekende informatie, urgentie, onzekerheid en bron; fysiotherapeut beslist
- Onbekende regio, uitgesloten populatie of dekkingsgat expliciet aangeven en menselijke beoordeling vragen

## Vastleggen van gespreksbewijs

Toestanden: not_discussed, present, denied, unclear, not_applicable.

Verplichte velden: topic_id, state, speaker, subject, evidence_quote, observed_at, time_context, verification.

Tijdscontext: new, worsening, stable_existing, historical, unknown.

Verificatie: transcript_only, clinician_confirmed, uncertain_transcription.

### Bewijsregels

- not_applicable vereist expliciete klinische motivering
- not_discussed heeft geen evidence_quote; andere states vereisen bewijs of expliciete cliniciannotitie
- Bewaar tegenstrijdige uitspraken en markeer unclear; overschrijf niet stilzwijgend
- Geen gevoelige onderwerpen afdwingen zonder respectvolle klinische afweging
- Geen patiëntgegevens in de kennisbestanden of GitHub opslaan

## Algemene prognostische en behandelbare context voor LBP/LRS

Aspecifieke LBP/LRS waar klinisch passend; niet als universeel prognosemodel bij infectie, kanker, fractuur of viscerale ziekte.

### Prognostische context

- Eerdere episoden, hoge pijn-/beperkingslast en beenpijn
- Algemene gezondheid en kwaliteit van leven
- Stress, bewegingsangst, depressieve symptomen, passieve coping en negatieve herstelverwachtingen
- Fysiek zwaar werk, werkomgeving en tevredenheid

### Beïnvloedbare factoren

- Bewegen en functionele belastbaarheid via passende oefenopbouw
- Voorlichting, verwachtingen, zelfmanagement en gedrag met patiënt afstemmen
- Werk-/activiteitsaanpassingen en steun waar beïnvloedbaar
- Psychologische ondersteuning indien passend en met instemming

### Beperkingen

- Prognostische associaties zijn geen bewijs van individuele oorzaak
- Niet elke factor is door fysiotherapie te veranderen
- Geen vragenlijst als zelfstandige beslissing of exacte herstelvoorspelling

Bronnen: KNGF, NG59

## Mogelijke nociplastische bijdrage, los van een weefsel-DD

### Aanwijzingen

- Persisterende regionale/multifocale pijn met klinisch te beoordelen overgevoeligheid
- Niet volledig door nociceptieve of neuropathische mechanismen verklaard

### Beoordeling

- Gezamenlijk mechanismeonderzoek door clinicus; transcript alleen onvoldoende
- Overweeg slaap, vermoeidheid en belastingervaring als context zonder daarmee somatische oorzaken te verwerpen

### Beperkingen

- Psychologische stress of hoge CSI-score stelt geen nociplastische diagnose
- Kan samen voorkomen met nociceptieve of neuropathische processen

Bronnen: NOCIPLASTIC

## Vragenbank

De vragen zijn eigen formuleringen, geen gevalideerde schaal. Een vraag kan worden overgeslagen als het antwoord al expliciet en betrouwbaar bekend is. Context en klinische relevantie bepalen welke vragen nodig zijn.

### onset

Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: eigen contextvraag; geen specifieke diagnostische claim

### distribution

Waar voelt u de pijn precies en trekt deze door naar bil, lies, been, buik of flank?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: eigen contextvraag; geen specifieke diagnostische claim

### function

Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: eigen contextvraag; geen specifieke diagnostische claim

### load

Welke bewegingen, houdingen en belastingen veranderen de klachten, en wat gebeurt er daarna?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: eigen contextvraag; geen specifieke diagnostische claim

### history

Heeft u dit eerder gehad, welke diagnoses of onderzoeken zijn gedaan en wat hielp toen?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: eigen contextvraag; geen specifieke diagnostische claim

### medical

Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: eigen contextvraag; geen specifieke diagnostische claim

### course

Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: eigen contextvraag; geen specifieke diagnostische claim

### trauma

Was er een val, ongeval, botsing of andere plotselinge belasting; hoe groot was die?

Wanneer: basisonderzoek. Doel: mogelijke fractuur/trauma. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: TRAUMA, NOGG

### bone

Zijn er eerdere breuken, osteoporose, langdurig corticosteroïdgebruik of recent lengteverlies?

Wanneer: basisonderzoek. Doel: botkwetsbaarheid. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: NOGG

### cancer

Heeft u kanker gehad of nu kanker, onbedoeld gewichtsverlies of een eerdere onverklaarde fractuur?

Wanneer: basisonderzoek. Doel: medische differentiaal. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: MSCC, MYELOMA

### infection

Heeft u koorts of voelt u zich ziek; waren er recent infecties, ingrepen of verminderde afweer?

Wanneer: basisonderzoek. Doel: infectieuze context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: INFECTION

### night

Wat gebeurt er ’s nachts: komt de pijn bij draaien, wordt u wakker, en verandert zij door opstaan of bewegen?

Wanneer: basisonderzoek. Doel: onderscheiden context van nachtelijke pijn. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: SPA, MSCC

### leg

Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: LRS

### weakness

Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?

Wanneer: basisonderzoek. Doel: neurologische verandering. Prioriteit: safety.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: LRS, CES

### bladder

Is het plassen veranderd: beginnen, aandrang, gevoel van de straal, leegplassen of urineverlies?

Wanneer: basisonderzoek. Doel: nieuwe/verergerende sacrale neurologische symptomen. Prioriteit: safety.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: CES

### saddle

Is het gevoel rond geslachtsdelen, anus of binnenkant van de bovenbenen veranderd, bijvoorbeeld bij afvegen?

Wanneer: basisonderzoek. Doel: sacrale sensibiliteit. Prioriteit: safety.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: CES

### bowel

Is de ontlasting veranderd: gevoel van een volle endeldarm, passage voelen of controle verliezen?

Wanneer: basisonderzoek. Doel: sacrale functie; onderscheid met gewone obstipatie nodig. Prioriteit: safety.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: CES

### sexual

Is sinds de rug-/beenklachten het gevoel of functioneren bij seksualiteit veranderd?

Wanneer: basisonderzoek. Doel: sacrale functie. Prioriteit: safety.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: CES

### walking

Hoe ver kunt u lopen, waar ontstaat de pijn en helpt stilstaan, zitten of vooroverbuigen?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: LRS, PAD, STENOSIS

### vascular

Heeft u vaatziekte, een bekend aneurysma, diabetes, hoge bloeddruk of een rookgeschiedenis?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: AAA, PAD

### abdomen

Zijn er ook buik- of flankklachten, plots hevige pijn, flauwvallen, zweten of ernstige misselijkheid?

Wanneer: basisonderzoek. Doel: extravertebrale spoedcontext. Prioriteit: safety.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: AAA, STONES

### urinary

Heeft u pijn bij plassen, vaker plassen, bloed in de urine of flankpijn met koorts?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: PYELONEPHRITIS, STONES

### inflammatory

Begonnen de klachten jong, verbeteren ze door bewegen, en zijn er psoriasis, darmontsteking, oogontsteking of gewrichts-/peesklachten?

Wanneer: persisterende of mogelijk inflammatoire klachten. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: SPA

### family

Komen spondyloartritis, psoriasis of vergelijkbare inflammatoire klachten in de familie voor?

Wanneer: mogelijk inflammatoir. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: SPA

### hip

Heeft u lies-/heuppijn, moeite met schoenen aantrekken of pijn bij lopen, heupbuigen of draaien?

Wanneer: mogelijke heupbron. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: OA, FAI

### lateralhip

Zit de pijn aan de buitenzijde van de heup en wat gebeurt er bij zijligging, traplopen of op één been staan?

Wanneer: laterale heuppijn. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: GLUTEAL

### training

Is de trainingsbelasting recent toegenomen; hoeveel herstel is er en zijn voeding of menstruatie veranderd?

Wanneer: sportbelasting of vermoeden stressfractuur. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: SACRUM, PARS

### pregnancy

Is zwangerschap mogelijk, bent u zwanger of recent bevallen, en zijn er ook buikpijn of bloedverlies?

Wanneer: indien klinisch relevant; vraag respectvol naar mogelijkheid, geen aanname uit gender. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: PGP, ECTOPIC

### cycle

Is er samenhang met menstruatie, bekkenpijn, seks, ontlasting of plassen; zijn de klachten cyclisch?

Wanneer: relevante bekken-/cyclische klachten. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: ENDOMETRIOSIS

### skin

Is er branderigheid, aanraakpijn of huiduitslag/blaasjes in een strook aan één kant?

Wanneer: mogelijke dermatomale huid-/zenuwpijn. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: ZOSTER

### expectations

Wat denkt u dat er aan de hand is en wat verwacht u van herstel en behandeling?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: KNGF

### fear

Welke bewegingen vermijdt u, en maakt u zich zorgen dat bewegen schade geeft?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: KNGF

### coping

Wat doet u bij pijn, wat helpt, en hoe lukt het om activiteiten te verdelen?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: KNGF

### psychosocial

Welke stress, somberheid, ondersteuning of problemen thuis of op werk beïnvloeden uw herstel?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: KNGF

### work

Wat vraagt uw werk fysiek, hoe is de steun op het werk en welke aanpassingen zijn mogelijk?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: KNGF

### sleep

Hoe slaapt u en welke factoren verstoren uw slaap?

Wanneer: basisonderzoek. Doel: ervaren herstel en functioneren; geen zelfstandige diagnose. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: eigen contextvraag; geen specifieke diagnostische claim

### goals

Wat zijn uw belangrijkste doelen, voorkeuren en praktische belemmeringen voor behandeling?

Wanneer: basisonderzoek. Doel: klinische context. Prioriteit: routine.

Bij een relevant antwoord: sinds wanneer, nieuw/veranderd, een- of tweezijdig, ernst, verloop en eerdere beoordeling vastleggen.

Bronnen: eigen contextvraag; geen specifieke diagnostische claim

## 1. Aspecifieke lagerugpijn

ID: nonspecific; categorie: syndroom; review: draft.

### Diagnostische aanwijzingen

- Rugpijn met wisselend mechanisch patroon zonder voldoende aanwijzingen voor specifieke pathologie; eventueel niet-radiculaire gerefereerde pijn

### Risicofactoren

- Eerdere episoden en belastingscontext zijn relevant maar verklaren de individuele pijnbron niet

### Vervolgvragen

- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- distribution: Waar voelt u de pijn precies en trekt deze door naar bil, lies, been, buik of flank?
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?
- load: Welke bewegingen, houdingen en belastingen veranderen de klachten, en wat gebeurt er daarna?
- history: Heeft u dit eerder gehad, welke diagnoses of onderzoeken zijn gedaan en wat hielp toen?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?
- trauma: Was er een val, ongeval, botsing of andere plotselinge belasting; hoe groot was die?
- bone: Zijn er eerdere breuken, osteoporose, langdurig corticosteroïdgebruik of recent lengteverlies?
- cancer: Heeft u kanker gehad of nu kanker, onbedoeld gewichtsverlies of een eerdere onverklaarde fractuur?
- infection: Heeft u koorts of voelt u zich ziek; waren er recent infecties, ingrepen of verminderde afweer?
- night: Wat gebeurt er ’s nachts: komt de pijn bij draaien, wordt u wakker, en verandert zij door opstaan of bewegen?
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- bladder: Is het plassen veranderd: beginnen, aandrang, gevoel van de straal, leegplassen of urineverlies?
- saddle: Is het gevoel rond geslachtsdelen, anus of binnenkant van de bovenbenen veranderd, bijvoorbeeld bij afvegen?
- bowel: Is de ontlasting veranderd: gevoel van een volle endeldarm, passage voelen of controle verliezen?
- sexual: Is sinds de rug-/beenklachten het gevoel of functioneren bij seksualiteit veranderd?
- expectations: Wat denkt u dat er aan de hand is en wat verwacht u van herstel en behandeling?
- fear: Welke bewegingen vermijdt u, en maakt u zich zorgen dat bewegen schade geeft?
- coping: Wat doet u bij pijn, wat helpt, en hoe lukt het om activiteiten te verdelen?
- psychosocial: Welke stress, somberheid, ondersteuning of problemen thuis of op werk beïnvloeden uw herstel?
- work: Wat vraagt uw werk fysiek, hoe is de steun op het werk en welke aanpassingen zijn mogelijk?
- sleep: Hoe slaapt u en welke factoren verstoren uw slaap?
- goals: Wat zijn uw belangrijkste doelen, voorkeuren en praktische belemmeringen voor behandeling?

### Lichamelijk onderzoek en beperkingen

- Functionele taken, actief bewegen en belastbaarheid observeren
- Gericht neurologisch of heup-/vaatonderzoek indien klachten daartoe aanleiding geven

### Prognostische factoren

- Algemene LBP/LRS-factoren uit profiel general_lbp uitsluitend waar passend; geen aandoeningsspecifieke kans of hersteltijd uit dit bestand.

### Therapeutisch beïnvloedbare factoren

- Zie general_lbp-profiel; passend bewegen, herstelverwachtingen, zelfmanagement en werkparticipatie

### Overleg / verwijzing

Conservatieve begeleiding als klinische beoordeling dit ondersteunt; bij afwijkend verloop of nieuwe signalen differentiaal opnieuw beoordelen.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

### Interpretatiegrenzen

- Werkdiagnose; geen diagnose uitsluitend op grond van ontbrekende transcriptinformatie
- Aspecifiek betekent niet ingebeeld
- Routinebeeldvorming levert meestal geen passend antwoord zonder gerichte indicatie

Bronnen: KNGF, NG59, REDFLAGS

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 2. Mogelijk discusgerelateerde nociceptieve pijn

ID: disc_hypothesis; categorie: pijnbronhypothese; review: draft.

### Diagnostische aanwijzingen

- Rug-/bilpijn waarbij flexie, zitten of herhaalde beweging invloed hebben; centralisatie kan klinisch relevant zijn

### Risicofactoren

- Geen gevalideerde individuele risicoscore in deze module

### Vervolgvragen

- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- distribution: Waar voelt u de pijn precies en trekt deze door naar bil, lies, been, buik of flank?
- load: Welke bewegingen, houdingen en belastingen veranderen de klachten, en wat gebeurt er daarna?
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?

### Lichamelijk onderzoek en beperkingen

- Herhaalde bewegingen alleen als veilig en functioneel relevant; respons vastleggen
- Neurologisch onderzoek bij uitstraling

### Prognostische factoren

- Algemene LBP/LRS-factoren uit profiel general_lbp uitsluitend waar passend; geen aandoeningsspecifieke kans of hersteltijd uit dit bestand.

### Therapeutisch beïnvloedbare factoren

- Na veiligheidsbeoordeling: doelen, activiteit en belastbaarheid samen afstemmen; niet elke gevonden factor is oorzakelijk of behandelbaar.

### Overleg / verwijzing

Behandel het klinische functioneren; medische herbeoordeling bij neurologische verandering of onvoldoende verklaard verloop.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

### Interpretatiegrenzen

- Dit patroon bewijst geen discogene pijn
- Een discusafwijking op MRI is niet automatisch de pijnbron
- Centralisatie is geen toestemming om rode vlaggen te negeren

Bronnen: STRUCTURE, LRS

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 3. Mogelijk facetgerelateerde pijn

ID: facet_hypothesis; categorie: pijnbronhypothese; review: draft.

### Diagnostische aanwijzingen

- Lokale of gerefereerde rugpijn, soms bij extensie/rotatie

### Risicofactoren

- Degeneratieve bevindingen kunnen bestaan zonder klachten

### Vervolgvragen

- distribution: Waar voelt u de pijn precies en trekt deze door naar bil, lies, been, buik of flank?
- load: Welke bewegingen, houdingen en belastingen veranderen de klachten, en wat gebeurt er daarna?
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?

### Lichamelijk onderzoek en beperkingen

- Beweeg- en functieonderzoek gericht op reproduceerbare klachten; geen unieke facettest

### Prognostische factoren

- Algemene LBP/LRS-factoren uit profiel general_lbp uitsluitend waar passend; geen aandoeningsspecifieke kans of hersteltijd uit dit bestand.

### Therapeutisch beïnvloedbare factoren

- Na veiligheidsbeoordeling: doelen, activiteit en belastbaarheid samen afstemmen; niet elke gevonden factor is oorzakelijk of behandelbaar.

### Overleg / verwijzing

Conservatief indien passend bij gehele beoordeling; specialistische diagnostiek alleen bij een gerichte medische vraag.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

### Interpretatiegrenzen

- Extensie-rotatiepijn, drukpijn en beeldvorming stellen geen betrouwbare zelfstandige facetdiagnose
- Geen automatische invasieve behandeling adviseren

Bronnen: STRUCTURE

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 4. Mogelijk sacro-iliacaal gerelateerde pijn

ID: si_hypothesis; categorie: pijnbronhypothese; review: draft.

### Diagnostische aanwijzingen

- Pijn rond achterste bekken/bil met belasting; overlap met heup, rug en inflammatoire klachten

### Risicofactoren

- Zwangerschap en belasting zijn context, geen bewijs voor mechanische SI-pijn

### Vervolgvragen

- distribution: Waar voelt u de pijn precies en trekt deze door naar bil, lies, been, buik of flank?
- load: Welke bewegingen, houdingen en belastingen veranderen de klachten, en wat gebeurt er daarna?
- hip: Heeft u lies-/heuppijn, moeite met schoenen aantrekken of pijn bij lopen, heupbuigen of draaien?
- inflammatory: Begonnen de klachten jong, verbeteren ze door bewegen, en zijn er psoriasis, darmontsteking, oogontsteking of gewrichts-/peesklachten?
- pregnancy: Is zwangerschap mogelijk, bent u zwanger of recent bevallen, en zijn er ook buikpijn of bloedverlies?
- trauma: Was er een val, ongeval, botsing of andere plotselinge belasting; hoe groot was die?

### Lichamelijk onderzoek en beperkingen

- Een passende pijnprovocatietestcluster kan verdenking ondersteunen; afspraken over uitvoering en klachtenherkenning nodig

### Prognostische factoren

- Algemene LBP/LRS-factoren uit profiel general_lbp uitsluitend waar passend; geen aandoeningsspecifieke kans of hersteltijd uit dit bestand.

### Therapeutisch beïnvloedbare factoren

- Na veiligheidsbeoordeling: doelen, activiteit en belastbaarheid samen afstemmen; niet elke gevonden factor is oorzakelijk of behandelbaar.

### Overleg / verwijzing

Begeleiding bij passend klinisch beeld; bij inflammatoire of fractuurverdenking medische beoordeling.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

### Interpretatiegrenzen

- Positieve cluster bevestigt SI als pijnbron onvoldoende
- Geen diagnose van scheefstand of bekkeninstabiliteit uit palpatie
- Geen gelijkstelling van mechanische SI-pijn en sacro-iliitis

Bronnen: SI, STRUCTURE

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 5. Lumbosacraal radiculair syndroom / radiculopathie

ID: lrs; categorie: neurologisch; review: draft.

### Diagnostische aanwijzingen

- Uitstralende beenpijn met mogelijk dermatomale sensibiliteitsverandering
- Bij radiculopathie ook objectiveerbare neurologische functiestoornis; pijn alleen bewijst dat niet

### Risicofactoren

- Eerdere klachten, discus-/stenosecontext; geen individuele kansberekening

### Vervolgvragen

- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- bladder: Is het plassen veranderd: beginnen, aandrang, gevoel van de straal, leegplassen of urineverlies?
- saddle: Is het gevoel rond geslachtsdelen, anus of binnenkant van de bovenbenen veranderd, bijvoorbeeld bij afvegen?
- bowel: Is de ontlasting veranderd: gevoel van een volle endeldarm, passage voelen of controle verliezen?
- sexual: Is sinds de rug-/beenklachten het gevoel of functioneren bij seksualiteit veranderd?
- walking: Hoe ver kunt u lopen, waar ontstaat de pijn en helpt stilstaan, zitten of vooroverbuigen?
- distribution: Waar voelt u de pijn precies en trekt deze door naar bil, lies, been, buik of flank?
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?

### Lichamelijk onderzoek en beperkingen

- Kracht, sensibiliteit, reflexen en functioneel lopen links/rechts vergelijken
- SLR en gekruiste SLR interpreteren samen met symptomen en neurologie

### Prognostische factoren

- Algemene LBP/LRS-factoren uit profiel general_lbp uitsluitend waar passend; geen aandoeningsspecifieke kans of hersteltijd uit dit bestand.

### Therapeutisch beïnvloedbare factoren

- Functionele opbouw, voorlichting en waar passend general_lbp; neurologisch herstel niet alleen door oefeningen bepaald

### Overleg / verwijzing

Nieuwe ernstige/progressieve parese: urgente medische beoordeling; sacrale functieverandering: CES-route. Overleg bij persisterende beperkende klachten.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Neurodynamische test alleen stelt geen diagnose
- Geen automatische MRI-aanvraag
- Beenpijn kan ook vasculair of uit heup komen

Bronnen: LRS, KNGF, CES

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 6. Lumbale spinale stenose met neurogene claudicatio

ID: stenosis; categorie: neurologisch; review: draft.

### Diagnostische aanwijzingen

- Been-/bilklachten bij staan/lopen, vaak verlichting bij zitten of flexie

### Risicofactoren

- Degeneratieve context en hogere leeftijd; anatomische stenose kan asymptomatisch zijn

### Vervolgvragen

- walking: Hoe ver kunt u lopen, waar ontstaat de pijn en helpt stilstaan, zitten of vooroverbuigen?
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- vascular: Heeft u vaatziekte, een bekend aneurysma, diabetes, hoge bloeddruk of een rookgeschiedenis?
- bladder: Is het plassen veranderd: beginnen, aandrang, gevoel van de straal, leegplassen of urineverlies?
- saddle: Is het gevoel rond geslachtsdelen, anus of binnenkant van de bovenbenen veranderd, bijvoorbeeld bij afvegen?
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?

### Lichamelijk onderzoek en beperkingen

- Looprespons, neurologie en zo nodig vaatstatus; vergelijk effecten van stilstaan en flexie

### Prognostische factoren

- Loopbeperking en neurologische status volgen; geen gevalideerd individueel prognosemodel opgenomen

### Therapeutisch beïnvloedbare factoren

- Loop-/conditieopbouw en belastingstrategie afgestemd op tolerantie; behandeling van bijkomende factoren

### Overleg / verwijzing

Huisarts/specialist bij aanzienlijke of toenemende beperking; spoed bij CES of snel progressieve uitval.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Klachten plus context nodig; scanbevinding alleen niet voldoende
- Geen afkapwaarde voor loopafstand die zelfstandig onderscheid maakt

Bronnen: STENOSIS, LRS, PAD

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 7. Degeneratieve spondylolisthesis

ID: degenerative_listhesis; categorie: structureel; review: draft.

### Diagnostische aanwijzingen

- Kan rugpijn, radiculaire klachten of neurogene claudicatio vergezellen

### Risicofactoren

- Degeneratieve context; bevinding kan toevallig zijn

### Vervolgvragen

- history: Heeft u dit eerder gehad, welke diagnoses of onderzoeken zijn gedaan en wat hielp toen?
- walking: Hoe ver kunt u lopen, waar ontstaat de pijn en helpt stilstaan, zitten of vooroverbuigen?
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?

### Lichamelijk onderzoek en beperkingen

- Functioneel en neurologisch onderzoek; medische beeldvorming bij gerichte indicatie

### Prognostische factoren

- Prognose hangt van klachten, neurologie en medische beoordeling af; radiologische verschuiving niet gelijk aan slechter herstel

### Therapeutisch beïnvloedbare factoren

- Belastbaarheid en general_lbp waar passend; conservatieve of operatieve strategie via behandelend team

### Overleg / verwijzing

Overleg bij functionele achteruitgang of neurologische klachten; CES/uitval urgent.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Geen diagnose van instabiliteit uit één houdings- of palpatiebevinding
- Oudere richtlijnsamenvatting; behandelinhoud nog nader uitwerken

Bronnen: LISTHESIS, LRS

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 8. Spondylolyse / pars stressletsel

ID: pars; categorie: structureel; review: draft.

### Diagnostische aanwijzingen

- Bij jonge sporter lokale rugpijn in relatie tot herhaalde extensie/rotatie of trainingsverandering

### Risicofactoren

- Repetitieve sportbelasting; voorgeschiedenis stressletsel

### Vervolgvragen

- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- training: Is de trainingsbelasting recent toegenomen; hoeveel herstel is er en zijn voeding of menstruatie veranderd?
- load: Welke bewegingen, houdingen en belastingen veranderen de klachten, en wat gebeurt er daarna?
- trauma: Was er een val, ongeval, botsing of andere plotselinge belasting; hoe groot was die?
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?

### Lichamelijk onderzoek en beperkingen

- Functie en belastingonderzoek; vermijd herhaald pijnlijk provoceren bij stressletselverdenking

### Prognostische factoren

- Actief stressletsel en chronisch defect onderscheiden via medische beoordeling; geen herstelduur vastgelegd

### Therapeutisch beïnvloedbare factoren

- Tijdelijk aanpassen provocerende belasting; sporthervatting afstemmen na beoordeling

### Overleg / verwijzing

Huisarts/sportarts bij persisterende verdenking; verdere diagnostiek bepaalt beleid.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

### Interpretatiegrenzen

- Eenbenige hyperextensietest kan parsletsel niet betrouwbaar aantonen of uitsluiten
- Historische beeldvormingsaanbevelingen uit onderzoek niet overgenomen

Bronnen: PARS

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 9. Isthmische spondylolisthesis

ID: isthmic_listhesis; categorie: structureel; review: draft.

### Diagnostische aanwijzingen

- Bekend parsdefect met eventuele verschuiving; rug-/beenklachten kunnen maar hoeven niet samen te hangen

### Risicofactoren

- Parsvoorgeschiedenis en sportcontext; geen directe causaliteit uit belasting alleen

### Vervolgvragen

- history: Heeft u dit eerder gehad, welke diagnoses of onderzoeken zijn gedaan en wat hielp toen?
- training: Is de trainingsbelasting recent toegenomen; hoeveel herstel is er en zijn voeding of menstruatie veranderd?
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?

### Lichamelijk onderzoek en beperkingen

- Functie en neurologische screening; radiologische classificatie door medische beoordelaar

### Prognostische factoren

- Geen aandoeningsspecifieke prognose onderbouwd in dit concept

### Therapeutisch beïnvloedbare factoren

- Veilige belastingopbouw in samenspraak; geen correctie van wervelstand beloven

### Overleg / verwijzing

Huisarts/sportarts of wervelkolomspecialist bij verdachte klachten of neurologische tekenen.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Dekkingsgat: aparte actuele richtlijn voor volwassen isthmische spondylolisthesis toevoegen
- PARS-bron ondersteunt alleen parscontext en testbeperking, niet dit hele behandelpad

Bronnen: PARS, LRS

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 10. Osteoporotische wervelfractuur

ID: osteoporotic_fracture; categorie: fractuur; review: draft.

### Diagnostische aanwijzingen

- Nieuwe lokale rugpijn na gering trauma of zonder duidelijk trauma; mogelijke lengteafname/kyfose

### Risicofactoren

- Eerdere fragiliteitsfractuur, osteoporose, hogere leeftijd, langdurige corticosteroïden

### Vervolgvragen

- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- trauma: Was er een val, ongeval, botsing of andere plotselinge belasting; hoe groot was die?
- bone: Zijn er eerdere breuken, osteoporose, langdurig corticosteroïdgebruik of recent lengteverlies?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?

### Lichamelijk onderzoek en beperkingen

- Veilig functioneel en neurologisch onderzoek; niet pijnlijk forceren of manipuleren bij verdenking

### Prognostische factoren

- Fractuur verhoogt risico op volgende fracturen; functie, pijn, valrisico en medische botgezondheid bepalen opvolging

### Therapeutisch beïnvloedbare factoren

- Na beoordeling: passende beweging, kracht/balans en valpreventie; botmedicatie door arts

### Overleg / verwijzing

Tijdige medische beoordeling; bij acuut ernstige pijn, relevante uitval of onveilig functioneren dezelfde dag bespreken.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Afwezigheid van één rode vlag sluit fractuur niet uit
- Geen fractuurdiagnose uit drukpijn alleen

Bronnen: NOGG, REDFLAGS

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 11. Traumatische wervelfractuur / instabiel letsel

ID: traumatic_fracture; categorie: fractuur; review: draft.

### Diagnostische aanwijzingen

- Nieuwe rugpijn na relevant trauma; neurologische uitval kan bijkomen

### Risicofactoren

- Hoogenergetisch trauma; kwetsbare botten verlagen traumadrempel

### Vervolgvragen

- trauma: Was er een val, ongeval, botsing of andere plotselinge belasting; hoe groot was die?
- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?
- bladder: Is het plassen veranderd: beginnen, aandrang, gevoel van de straal, leegplassen of urineverlies?
- saddle: Is het gevoel rond geslachtsdelen, anus of binnenkant van de bovenbenen veranderd, bijvoorbeeld bij afvegen?

### Lichamelijk onderzoek en beperkingen

- Bij verdenking ernstig letsel geen routinematige provocatie; acute medische beoordeling

### Prognostische factoren

- Stabiliteit en neurologisch letsel zijn medische prognostische kwesties

### Therapeutisch beïnvloedbare factoren

- Revalidatie pas na beoordeling van stabiliteit en medische belastingsafspraken

### Overleg / verwijzing

Acute traumazorg bij ernstig mechanisme, neurologische tekenen of instabiliteitsverdenking.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Een patiënt die nog loopt kan toch relevant letsel hebben
- Geen fysiotherapeutische provocatietest om een instabiele fractuur uit te sluiten

Bronnen: TRAUMA

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 12. Sacrale insufficiëntiefractuur

ID: sacral_insufficiency; categorie: fractuur; review: draft.

### Diagnostische aanwijzingen

- Nieuwe sacrale/bil-/lage-rugpijn bij normale belasting, soms zonder duidelijk trauma

### Risicofactoren

- Osteoporose, hogere leeftijd, corticosteroïden, bekkenbestraling

### Vervolgvragen

- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- bone: Zijn er eerdere breuken, osteoporose, langdurig corticosteroïdgebruik of recent lengteverlies?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.
- trauma: Was er een val, ongeval, botsing of andere plotselinge belasting; hoe groot was die?
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?

### Lichamelijk onderzoek en beperkingen

- Gang en belastbaarheid voorzichtig beoordelen; diagnostiek door arts

### Prognostische factoren

- Botgezondheid, pijn en veilige mobiliteit bepalen beleid; gevalideerd prognosemodel ontbreekt

### Therapeutisch beïnvloedbare factoren

- Na beoordeling: aangepaste belasting, mobiliteit en fractuurpreventie via team

### Overleg / verwijzing

Medische beoordeling bij vermoeden; geen voortzetting van provocerende behandeling.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Kan op gewone radiografie gemist worden; geen advies dat normale foto alles uitsluit
- Reviewbasis beperkt en relatief oud

Bronnen: SACRUM, NOGG

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 13. Sacrale vermoeidheids-/stressfractuur

ID: sacral_fatigue; categorie: fractuur; review: draft.

### Diagnostische aanwijzingen

- Belastingsgebonden sacrale/bilpijn bij sport, soms toenemende pijn tijdens lopen

### Risicofactoren

- Plots hogere herhaalde belasting; mogelijke lage energiebeschikbaarheid/botgezondheidsproblemen nader beoordelen

### Vervolgvragen

- training: Is de trainingsbelasting recent toegenomen; hoeveel herstel is er en zijn voeding of menstruatie veranderd?
- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- load: Welke bewegingen, houdingen en belastingen veranderen de klachten, en wat gebeurt er daarna?
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?
- bone: Zijn er eerdere breuken, osteoporose, langdurig corticosteroïdgebruik of recent lengteverlies?
- pregnancy: Is zwangerschap mogelijk, bent u zwanger of recent bevallen, en zijn er ook buikpijn of bloedverlies?

### Lichamelijk onderzoek en beperkingen

- Belasting- en functieonderzoek voorzichtig; niet met herhaalde hoptesten proberen fractuur uit te sluiten

### Prognostische factoren

- Ernst, botgezondheid en belasting bepalen herstel; geen vaste weektermijn

### Therapeutisch beïnvloedbare factoren

- Belasting tijdelijk verminderen, voeding/herstel en eventuele hormonale factoren met bevoegde zorgverleners bespreken

### Overleg / verwijzing

Huisarts/sportarts bij vermoeden; beeldvormingskeuze via arts.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Fatigue en insufficiëntie niet samenvoegen: respectievelijk overbelasting en verminderde botsterkte
- Voeding/menstruatievragen zijn eigen brede sportklinische operationalisering, geen gevalideerde score

Bronnen: SACRUM

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 14. Axiale spondyloartritis

ID: axspa; categorie: inflammatoir; review: draft.

### Diagnostische aanwijzingen

- Langdurige rugpijn met begin op jongere leeftijd; mogelijk nachtelijke/bilpijn en verbetering door bewegen
- Extra-articulaire inflammatoire klachten ondersteunen context

### Risicofactoren

- Familiaire spondyloartritis, psoriasis, inflammatoire darmziekte of uveïtis in relevante context

### Vervolgvragen

- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- night: Wat gebeurt er ’s nachts: komt de pijn bij draaien, wordt u wakker, en verandert zij door opstaan of bewegen?
- inflammatory: Begonnen de klachten jong, verbeteren ze door bewegen, en zijn er psoriasis, darmontsteking, oogontsteking of gewrichts-/peesklachten?
- family: Komen spondyloartritis, psoriasis of vergelijkbare inflammatoire klachten in de familie voor?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?

### Lichamelijk onderzoek en beperkingen

- Mobiliteit en perifere gewrichten/enthesecontext; medisch onderzoek volgens verwijspad

### Prognostische factoren

- Ziekteactiviteit, functie en comorbiditeit door team beoordelen; algemene LBP-prognoses niet blind toepassen

### Therapeutisch beïnvloedbare factoren

- Bewegen en functioneren ondersteunen; ziektecontrole via reumatoloog

### Overleg / verwijzing

Bij passend patroon huisarts voor reumatologische beoordeling; acute oogpijn/roodheid met visusklachten apart urgent beoordelen.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Geen uitsluiting door normaal CRP, negatieve HLA-B27 of één ontbrekend kenmerk
- NICE-verwijscriteria zijn geen autonome diagnoseregel; exacte criteria niet geïmplementeerd

Bronnen: SPA

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 15. Spondylodiscitis / vertebrale osteomyelitis

ID: vertebral_infection; categorie: infectie; review: draft.

### Diagnostische aanwijzingen

- Nieuwe of toenemende rugpijn met infectieuze context; koorts kan ontbreken

### Risicofactoren

- Bacteriëmie, recente infectie/ingreep, immuunsuppressie, relevante medische kwetsbaarheid

### Vervolgvragen

- infection: Heeft u koorts of voelt u zich ziek; waren er recent infecties, ingrepen of verminderde afweer?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.
- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- bladder: Is het plassen veranderd: beginnen, aandrang, gevoel van de straal, leegplassen of urineverlies?
- saddle: Is het gevoel rond geslachtsdelen, anus of binnenkant van de bovenbenen veranderd, bijvoorbeeld bij afvegen?

### Lichamelijk onderzoek en beperkingen

- Vitale/algemene toestand en neurologie indien bekwaam; geen vertraging voor uitgebreid bewegingsonderzoek

### Prognostische factoren

- Verwekker, uitbreiding en neurologische complicaties bepalen prognose; medisch beleid

### Therapeutisch beïnvloedbare factoren

- Infectiebehandeling door arts; fysiotherapie na medische veiligheids- en belastingsafspraken

### Overleg / verwijzing

Bij verdenking prompt medische beoordeling; ziek/septisch of neurologische tekenen: acute zorg.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Afwezigheid van koorts sluit infectie niet uit
- Oude IDSA-bron; lokale actuele infectieafspraken nodig

Bronnen: INFECTION

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 16. Spinaal epiduraal abces

ID: epidural_abscess; categorie: infectie; review: draft.

### Diagnostische aanwijzingen

- Rugpijn met mogelijke snelle neurologische verandering in infectieuze context

### Risicofactoren

- Infectie/ingreep en immuunsuppressie kunnen verdenking verhogen

### Vervolgvragen

- infection: Heeft u koorts of voelt u zich ziek; waren er recent infecties, ingrepen of verminderde afweer?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- bladder: Is het plassen veranderd: beginnen, aandrang, gevoel van de straal, leegplassen of urineverlies?
- saddle: Is het gevoel rond geslachtsdelen, anus of binnenkant van de bovenbenen veranderd, bijvoorbeeld bij afvegen?
- bowel: Is de ontlasting veranderd: gevoel van een volle endeldarm, passage voelen of controle verliezen?

### Lichamelijk onderzoek en beperkingen

- Geen provocationele behandeling bij verdenking; spoedbeoordeling neurologie via medische zorg

### Prognostische factoren

- Neurologische schade en tijdige behandeling relevant; geen prognosescore hier

### Therapeutisch beïnvloedbare factoren

- Medische infectiebehandeling/decompressie waar geïndiceerd; revalidatie daarna

### Overleg / verwijzing

Mogelijk abces met neurologische tekenen of ernstige ziekte: spoed.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Geen vereiste volledige combinatie rugpijn-koorts-uitval
- Eigen afzonderlijk spoedpad; specifieke recente abcesrichtlijn nog toevoegen

Bronnen: INFECTION, CES

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 17. Spinaal epiduraal hematoom

ID: epidural_hematoma; categorie: neurologische spoed; review: draft.

### Diagnostische aanwijzingen

- Plots hevige rug-/beenpijn met nieuwe of snel toenemende neurologische stoornis

### Risicofactoren

- Antistolling, stollingsstoornis, trauma of recente spinale ingreep als context

### Vervolgvragen

- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.
- trauma: Was er een val, ongeval, botsing of andere plotselinge belasting; hoe groot was die?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- bladder: Is het plassen veranderd: beginnen, aandrang, gevoel van de straal, leegplassen of urineverlies?
- saddle: Is het gevoel rond geslachtsdelen, anus of binnenkant van de bovenbenen veranderd, bijvoorbeeld bij afvegen?
- bowel: Is de ontlasting veranderd: gevoel van een volle endeldarm, passage voelen of controle verliezen?

### Lichamelijk onderzoek en beperkingen

- Geen uitstel door fysieke provocatietests

### Prognostische factoren

- Neurologische omvang en medische interventie bepalen uitkomst; geen individueel model

### Therapeutisch beïnvloedbare factoren

- Antistollings-/chirurgisch beleid uitsluitend arts; herstelzorg na stabilisatie

### Overleg / verwijzing

Acute medische beoordeling bij passend plots/progressief neurologisch beeld.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Zeldzaam; risicoafwezigheid sluit het niet uit
- Bronnen ondersteunen zeldzame oorzaak/CES-context; eigen specifieke pathologierichtlijn ontbreekt

Bronnen: LRS, CES

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 18. Spinale maligniteit / metastasen en mogelijke compressie

ID: spinal_malignancy; categorie: oncologisch; review: draft.

### Diagnostische aanwijzingen

- Nieuwe progressieve/onverklaarde rugpijn, vooral bij kankercontext; neurologische symptomen kunnen bijkomen

### Risicofactoren

- Actieve/doorgemaakte maligniteit; andere tekenen zoals onbedoeld gewichtsverlies in context

### Vervolgvragen

- cancer: Heeft u kanker gehad of nu kanker, onbedoeld gewichtsverlies of een eerdere onverklaarde fractuur?
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?
- night: Wat gebeurt er ’s nachts: komt de pijn bij draaien, wordt u wakker, en verandert zij door opstaan of bewegen?
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- bladder: Is het plassen veranderd: beginnen, aandrang, gevoel van de straal, leegplassen of urineverlies?
- saddle: Is het gevoel rond geslachtsdelen, anus of binnenkant van de bovenbenen veranderd, bijvoorbeeld bij afvegen?
- bowel: Is de ontlasting veranderd: gevoel van een volle endeldarm, passage voelen of controle verliezen?

### Lichamelijk onderzoek en beperkingen

- Geen belasting die verdachte instabiliteit of neurologische schade kan verergeren

### Prognostische factoren

- Tumortype, uitbreiding, stabiliteit en neurologie bepalen prognose; geen LBP-herstelmodel

### Therapeutisch beïnvloedbare factoren

- Oncologische behandeling door team; aangepaste activiteit pas met veiligheidsafspraken

### Overleg / verwijzing

Kankercontext met nieuwe verdachte pijn: snel medisch overleg; mogelijke neurologische compressie: spoed.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Ook pijn die door bewegen verandert kan bij maligniteit passen
- Nachtpijn op zichzelf is niet diagnostisch
- Britse organisatie van MSCC-zorg naar Nederlandse lokale route te vertalen

Bronnen: MSCC, REDFLAGS

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 19. Multipel myeloom / hematologische botpathologie

ID: myeloma; categorie: oncologisch; review: draft.

### Diagnostische aanwijzingen

- Persisterende bot-/rugpijn of onverklaarde fractuur; bredere medische context nodig

### Risicofactoren

- Hogere leeftijd verhoogt aandacht maar is geen vereiste

### Vervolgvragen

- cancer: Heeft u kanker gehad of nu kanker, onbedoeld gewichtsverlies of een eerdere onverklaarde fractuur?
- bone: Zijn er eerdere breuken, osteoporose, langdurig corticosteroïdgebruik of recent lengteverlies?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?

### Lichamelijk onderzoek en beperkingen

- Voorzichtige functiebeoordeling; bloed-/urineonderzoek en beeldvorming door arts

### Prognostische factoren

- Medische ziektekenmerken, nierfunctie en botcomplicaties bepalen prognose

### Therapeutisch beïnvloedbare factoren

- Medisch beleid en fractuurpreventie; activiteit afstemmen op botveiligheid

### Overleg / verwijzing

Huisarts bij onverklaarde persisterende botpijn/fractuur; spoed bij compressie/ernstig ziek zijn.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Geen diagnose uit vermoeidheid of leeftijd alleen
- NICE leeftijdscriterium voor laboratoriumonderzoek is geen uitsluitregel voor jongere patiënten

Bronnen: MYELOMA, MSCC

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 20. Cauda-equinasyndroom (CES)

ID: ces; categorie: spoedsyndroom; review: draft.

### Diagnostische aanwijzingen

- Nieuwe/verergerende verandering in blaas-, darm-, rijbroek- of seksuele functie bij rug-/beenklachten
- Ernstige/progressieve bilaterale neurologische uitval kan passen

### Risicofactoren

- Grote discusprolaps; ook tumor, infectie, bloeding of trauma; afwezig risico sluit niet uit

### Vervolgvragen

- bladder: Is het plassen veranderd: beginnen, aandrang, gevoel van de straal, leegplassen of urineverlies?
- saddle: Is het gevoel rond geslachtsdelen, anus of binnenkant van de bovenbenen veranderd, bijvoorbeeld bij afvegen?
- bowel: Is de ontlasting veranderd: gevoel van een volle endeldarm, passage voelen of controle verliezen?
- sexual: Is sinds de rug-/beenklachten het gevoel of functioneren bij seksualiteit veranderd?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?
- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?

### Lichamelijk onderzoek en beperkingen

- Negatief lichamelijk onderzoek mag relevante subjectieve symptomen niet wegstrepen
- Geen rectaal onderzoek nodig om vanuit fysiotherapie spoedverwijzing te rechtvaardigen

### Prognostische factoren

- Blijvende functiestoornissen mogelijk; geen geruststellende score berekenen

### Therapeutisch beïnvloedbare factoren

- Directe medische diagnostiek en behandeling; revalidatie na specialistisch beleid

### Overleg / verwijzing

Bij reële CES-verdenking onmiddellijk medische spoedbeoordeling regelen; niet wachten op volledig klachtenbeeld of de rest van de checklist.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Geen los symptoom of test bewijst/ontkracht CES
- Bestaande incontinentie onderscheiden van nieuwe verandering
- Geen harde 14-dagengrens gebruiken om langer bestaande verdachte klachten veilig te verklaren

Bronnen: CES

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 21. Heupartrose met gerefereerde klachten

ID: hip_oa; categorie: heup; review: draft.

### Diagnostische aanwijzingen

- Activiteitsgerelateerde lies-/heuppijn, stijfheid en bewegingsbeperking; rug-/bilklachten kunnen overlappen

### Risicofactoren

- Leeftijd en eerdere heupcontext; radiologische artrose niet automatisch symptomatisch

### Vervolgvragen

- hip: Heeft u lies-/heuppijn, moeite met schoenen aantrekken of pijn bij lopen, heupbuigen of draaien?
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?
- load: Welke bewegingen, houdingen en belastingen veranderen de klachten, en wat gebeurt er daarna?
- history: Heeft u dit eerder gehad, welke diagnoses of onderzoeken zijn gedaan en wat hielp toen?
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?

### Lichamelijk onderzoek en beperkingen

- Heup-ROM en functionele taken; combineer klachtenherkenning en functie

### Prognostische factoren

- Functie en belastbaarheid volgen; geen individuele progressie uit foto alleen

### Therapeutisch beïnvloedbare factoren

- Passende oefening, voorlichting en indien relevant gewichtsmanagement zonder stigma

### Overleg / verwijzing

Huisarts bij atypische presentatie of ernstige beperking; orthopedisch overleg volgens gedeelde besluitvorming bij onvoldoende resultaat.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

### Interpretatiegrenzen

- Heup- en rugproblematiek kunnen tegelijk bestaan
- NICE klinische artrosecriteria vervangen geen differentiaal bij atypisch verloop

Bronnen: OA

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 22. FAI-syndroom / andere intra-articulaire heupklachten

ID: hip_intraarticular; categorie: heup; review: draft.

### Diagnostische aanwijzingen

- Lies-/heuppijn bij buigen/draaien of sport; soms mechanische klachten

### Risicofactoren

- Sport-/morfologiecontext, niet op zichzelf een diagnose

### Vervolgvragen

- hip: Heeft u lies-/heuppijn, moeite met schoenen aantrekken of pijn bij lopen, heupbuigen of draaien?
- training: Is de trainingsbelasting recent toegenomen; hoeveel herstel is er en zijn voeding of menstruatie veranderd?
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?
- load: Welke bewegingen, houdingen en belastingen veranderen de klachten, en wat gebeurt er daarna?
- history: Heeft u dit eerder gehad, welke diagnoses of onderzoeken zijn gedaan en wat hielp toen?

### Lichamelijk onderzoek en beperkingen

- Heupfunctie en passende provocatie zoals FADIR; geen enkelvoudige bewijswaarde

### Prognostische factoren

- Geen uniforme prognose; specifieke pathologie en doelen bepalen beleid

### Therapeutisch beïnvloedbare factoren

- Belastingaanpassing, oefening en functieopbouw; verdere diagnostiek bij gerichte vraag

### Overleg / verwijzing

Huisarts/sportarts bij persisterende verdenking en beperking.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

### Interpretatiegrenzen

- FAI-syndroom vraagt symptomen, tekenen en beeldvorming in samenhang
- Positieve FADIR of cam/pincer-morfologie alleen niet voldoende
- Labrumproblematiek nog niet als apart volledig pad uitgewerkt

Bronnen: FAI

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 23. Gluteale tendinopathie / greater trochanteric pain syndrome

ID: gluteal; categorie: heup; review: draft.

### Diagnostische aanwijzingen

- Laterale heuppijn bij belasting of zijligging; kan naar bil/bovenbeen uitstralen

### Risicofactoren

- Belastingscontext; geen universele risicoscore

### Vervolgvragen

- lateralhip: Zit de pijn aan de buitenzijde van de heup en wat gebeurt er bij zijligging, traplopen of op één been staan?
- hip: Heeft u lies-/heuppijn, moeite met schoenen aantrekken of pijn bij lopen, heupbuigen of draaien?
- load: Welke bewegingen, houdingen en belastingen veranderen de klachten, en wat gebeurt er daarna?
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?

### Lichamelijk onderzoek en beperkingen

- Gerichte laterale heupbelasting en krachtfunctie; rug-/heup-/neurologische differentiaal behouden

### Prognostische factoren

- Geen universele prognose; reactie op opbouw en functioneren volgen

### Therapeutisch beïnvloedbare factoren

- Belastingeducatie en passende oefeningen bij vastgesteld klinisch beeld

### Overleg / verwijzing

Conservatief waar passend; herbeoordeling bij afwijkende tekenen of onvoldoende verklaarde klachten.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

### Interpretatiegrenzen

- GTPS is een bredere klinische categorie dan de geselecteerde tendinopathiepopulatie uit de trial
- Geen diagnose bursitis uit locatie alleen

Bronnen: GLUTEAL

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 24. Symptomatisch / geruptureerd abdominaal aorta-aneurysma

ID: aaa; categorie: vasculair; review: draft.

### Diagnostische aanwijzingen

- Acute nieuwe rug-/buikpijn met mogelijke collaps of circulatoire tekenen

### Risicofactoren

- Bekend aneurysma, hogere leeftijd, roken en hypertensie

### Vervolgvragen

- abdomen: Zijn er ook buik- of flankklachten, plots hevige pijn, flauwvallen, zweten of ernstige misselijkheid?
- vascular: Heeft u vaatziekte, een bekend aneurysma, diabetes, hoge bloeddruk of een rookgeschiedenis?
- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.

### Lichamelijk onderzoek en beperkingen

- Bij spoedverdenking geen provocatie of wachten op palpatie/auscultatie

### Prognostische factoren

- Levensbedreigende context; uitkomst afhankelijk van medische acute zorg

### Therapeutisch beïnvloedbare factoren

- Acute vaatzorg; risicobehandeling via arts na stabilisatie

### Overleg / verwijzing

Bij passend acuut beeld: onmiddellijk spoedzorg, 112 bij instabiliteit/collaps.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Afwezigheid van voelbare pulsatie of één kenmerk sluit AAA niet uit
- Geen routine-AAA-diagnose door AI op basis van rugpijn en roken

Bronnen: AAA

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 25. Perifeer arterieel vaatlijden met vasculaire claudicatio

ID: vascular_claudication; categorie: vasculair; review: draft.

### Diagnostische aanwijzingen

- Reproduceerbare beenpijn bij lopen, verlichting door rust; flexie niet noodzakelijk voor verlichting

### Risicofactoren

- Roken, diabetes, vaatziekte en cardiovasculaire risicofactoren

### Vervolgvragen

- walking: Hoe ver kunt u lopen, waar ontstaat de pijn en helpt stilstaan, zitten of vooroverbuigen?
- vascular: Heeft u vaatziekte, een bekend aneurysma, diabetes, hoge bloeddruk of een rookgeschiedenis?
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?

### Lichamelijk onderzoek en beperkingen

- Vaatstatus en enkel-armindex indien bevoegd/bekwaam; neurologische en functionele vergelijking

### Prognostische factoren

- Vasculair risico en functionele beperkingen vragen medische follow-up

### Therapeutisch beïnvloedbare factoren

- Gestructureerde loopbegeleiding waar geïndiceerd; stoppen met roken en medische risicobehandeling

### Overleg / verwijzing

Huisarts bij verdenking; acuut koud/pijnlijk bleek been of plots ernstige uitval: spoed.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Normale palpabele pulsaties sluiten PAD niet definitief uit
- Bij diabetes kan enkel-armindex minder betrouwbaar zijn
- Neurogene en vasculaire klachten kunnen samen voorkomen

Bronnen: PAD, LRS

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 26. Nier-/uretersteen met nierkoliek

ID: renal_colic; categorie: visceraal; review: draft.

### Diagnostische aanwijzingen

- Hevige flank-/rugpijn eventueel uitstralend naar lies; misselijkheid of urineklachten kunnen passen

### Risicofactoren

- Eerdere stenen en urologische voorgeschiedenis als context

### Vervolgvragen

- abdomen: Zijn er ook buik- of flankklachten, plots hevige pijn, flauwvallen, zweten of ernstige misselijkheid?
- urinary: Heeft u pijn bij plassen, vaker plassen, bloed in de urine of flankpijn met koorts?
- history: Heeft u dit eerder gehad, welke diagnoses of onderzoeken zijn gedaan en wat hielp toen?
- infection: Heeft u koorts of voelt u zich ziek; waren er recent infecties, ingrepen of verminderde afweer?
- pregnancy: Is zwangerschap mogelijk, bent u zwanger of recent bevallen, en zijn er ook buikpijn of bloedverlies?

### Lichamelijk onderzoek en beperkingen

- Geen fysiotherapeutische test om steen vast te stellen; medische beoordeling

### Prognostische factoren

- Obstructie, infectie en nierfunctie bepalen urgentie en beleid

### Therapeutisch beïnvloedbare factoren

- Medische pijn-/steenbehandeling; geen oefening als primaire therapie

### Overleg / verwijzing

Bij verdenking acute medische beoordeling; koorts/ziek zijn of mogelijke infectie-obstructiecombinatie extra urgent.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Urine zonder zichtbaar bloed sluit steen niet uit
- Extra klinische symptomen zijn eigen operationalisering, geen gevalideerde steenregel

Bronnen: STONES, PYELONEPHRITIS

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 27. Acute pyelonefritis

ID: pyelonephritis; categorie: visceraal/infectie; review: draft.

### Diagnostische aanwijzingen

- Flank-/rugpijn met koorts, ziek gevoel en/of urineklachten

### Risicofactoren

- Zwangerschap, diabetes, verminderde afweer of urologische afwijking maken context belangrijk

### Vervolgvragen

- infection: Heeft u koorts of voelt u zich ziek; waren er recent infecties, ingrepen of verminderde afweer?
- urinary: Heeft u pijn bij plassen, vaker plassen, bloed in de urine of flankpijn met koorts?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.
- pregnancy: Is zwangerschap mogelijk, bent u zwanger of recent bevallen, en zijn er ook buikpijn of bloedverlies?
- abdomen: Zijn er ook buik- of flankklachten, plots hevige pijn, flauwvallen, zweten of ernstige misselijkheid?

### Lichamelijk onderzoek en beperkingen

- Algemene toestand; medisch urine-/laboratoriumonderzoek

### Prognostische factoren

- Ernst, comorbiditeit en respons op medische behandeling bepalen vervolg

### Therapeutisch beïnvloedbare factoren

- Antimicrobiële behandeling door arts; herstelzorg na stabilisatie

### Overleg / verwijzing

Prompt huisarts/huisartsenpost; ernstige ziekte of sepsisverdenking via acute zorg.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Geen geruststelling als één typisch symptoom ontbreekt
- Niet behandelen als gewone mechanische rugpijn zolang infectieuze verdenking niet beoordeeld is

Bronnen: PYELONEPHRITIS

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 28. Endometriose / cyclische bekkenproblematiek

ID: endometriosis; categorie: bekken/visceraal; review: draft.

### Diagnostische aanwijzingen

- Bekkenklachten met menstruatieverband, pijn bij seks of cyclische darm-/urineklachten; rugpijn kan onderdeel zijn

### Risicofactoren

- Familiaire endometriosecontext

### Vervolgvragen

- cycle: Is er samenhang met menstruatie, bekkenpijn, seks, ontlasting of plassen; zijn de klachten cyclisch?
- pregnancy: Is zwangerschap mogelijk, bent u zwanger of recent bevallen, en zijn er ook buikpijn of bloedverlies?
- urinary: Heeft u pijn bij plassen, vaker plassen, bloed in de urine of flankpijn met koorts?
- abdomen: Zijn er ook buik- of flankklachten, plots hevige pijn, flauwvallen, zweten of ernstige misselijkheid?
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?
- course: Zijn de klachten stabiel, herstellend of toenemend, en wat is sinds de vorige beoordeling veranderd?

### Lichamelijk onderzoek en beperkingen

- Binnen eigen competentie functie beoordelen; gynaecologisch onderzoek via passende bevoegde zorgverlener

### Prognostische factoren

- Symptoomlast, doelen en medische beoordeling bepalen verloop; geen LBP-herstelmodel

### Therapeutisch beïnvloedbare factoren

- Medische/gynaecologische behandeling; aanvullende bekken-/pijnzorg waar passend

### Overleg / verwijzing

Huisarts/gynaecologie bij passend persisterend patroon. Mogelijke zwangerschap met acute buik-/bekkenpijn of bloedverlies: urgente beoordeling op andere oorzaken.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Normaal onderzoek sluit endometriose niet uit
- Geen diagnose uit menstruatieverband alleen
- Andere gynaecologische en buikoorzaken nog niet volledig uitgewerkt

Bronnen: ENDOMETRIOSIS, ECTOPIC

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 29. Zwangerschaps-/postpartumgerelateerde bekkenpijn

ID: pregnancy_pgp; categorie: bekken; review: draft.

### Diagnostische aanwijzingen

- Rug-/bekkenpijn rond zwangerschap, bij draaien, lopen, traplopen of transfers

### Risicofactoren

- Zwangerschap/postpartum en eerdere klachten als context

### Vervolgvragen

- pregnancy: Is zwangerschap mogelijk, bent u zwanger of recent bevallen, en zijn er ook buikpijn of bloedverlies?
- load: Welke bewegingen, houdingen en belastingen veranderen de klachten, en wat gebeurt er daarna?
- function: Welke activiteiten, werk, sport, zelfzorg en slaap lukken minder goed; wat wilt u weer kunnen?
- history: Heeft u dit eerder gehad, welke diagnoses of onderzoeken zijn gedaan en wat hielp toen?
- abdomen: Zijn er ook buik- of flankklachten, plots hevige pijn, flauwvallen, zweten of ernstige misselijkheid?
- weakness: Merkt u nieuwe of toenemende krachtsvermindering, struikelen of moeite met op tenen of hielen staan?
- bladder: Is het plassen veranderd: beginnen, aandrang, gevoel van de straal, leegplassen of urineverlies?

### Lichamelijk onderzoek en beperkingen

- Passend functioneel onderzoek en zo nodig bekkenfysiotherapeutische beoordeling

### Prognostische factoren

- Individueel verloop; geen garantie op vanzelf verdwijnen na bevalling

### Therapeutisch beïnvloedbare factoren

- Activiteit verdelen, passende oefening en hulpmiddelen alleen bij gerichte indicatie

### Overleg / verwijzing

Bij passend veilig beeld fysiotherapie; acute buikpijn, bloedverlies, ernstige ziekte of neurologische symptomen medisch beoordelen.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Geen automatische diagnose instabiliteit
- Niet iedere pijn tijdens zwangerschap is bekkenpijn
- Bron is patiënteninformatie; professionele Nederlandse bekkenrichtlijn nog toevoegen

Bronnen: PGP, ECTOPIC

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## 30. Herpes zoster / radiculitis

ID: zoster; categorie: huid/neurologisch; review: draft.

### Diagnostische aanwijzingen

- Eenzijdige dermatomale brandende pijn of allodynie; huidblaasjes kunnen later volgen

### Risicofactoren

- Hogere leeftijd en verminderde afweer

### Vervolgvragen

- skin: Is er branderigheid, aanraakpijn of huiduitslag/blaasjes in een strook aan één kant?
- onset: Wanneer begon de pijn, wat gebeurde er toen en hoe is het sindsdien veranderd?
- medical: Welke ziekten, operaties, medicijnen en recente wijzigingen zijn relevant? Denk ook aan corticosteroïden en bloedverdunners.
- leg: Heeft u beenpijn, tintelingen of een doof gevoel; waar precies, en aan één of beide kanten?
- infection: Heeft u koorts of voelt u zich ziek; waren er recent infecties, ingrepen of verminderde afweer?

### Lichamelijk onderzoek en beperkingen

- Huid-/sensibiliteitsbeeld gericht bekijken met toestemming; geen provocatie nodig

### Prognostische factoren

- Persisterende neuralgie mogelijk; ernst en medische context belangrijk

### Therapeutisch beïnvloedbare factoren

- Medische behandeling door arts; latere ondersteuning bij pijn/functioneren

### Overleg / verwijzing

Huisarts bij vermoeden; ernstige ziekte of kwetsbare context bepaalt extra urgentie.

Fysiotherapeut beoordeelt; medische beoordeling via huisarts/huisartsenpost, SEH of bestaande specialist afhankelijk van urgentie. Bij acute levensbedreiging 112.

Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.

### Interpretatiegrenzen

- Zonder uitslag moeilijker te herkennen; niet alle brandende pijn is zoster
- Geen automatische zenuwworteldiagnose door huidlocatie alleen

Bronnen: ZOSTER

brononderbouwde kern met eigen klinische operationalisering; niet klinisch gereviewd

## Bronnenregister

Bronnen ondersteunen de genoemde kern. Vragen, selectie, uitleg en vertaling naar een lokaal zorgpad zijn eigen operationalisering. Niet ieder onderdeel van een aandoening heeft afzonderlijk gevalideerde evidence. Oudere of beperkte bronnen en hiaten zijn expliciet gemarkeerd.

### KNGF

[Management of low back pain and lumbosacral radicular syndrome: the KNGF guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11112513/)

Bronjaar/gebruikte versie: 2024; type: richtlijnpublicatie; gecontroleerd: 2026-10-07.

Nederlandse fysiotherapie; richtlijn uit 2021, publicatie uit 2024. Algemene prognostische factoren en begeleiding bij LBP/LRS.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### NG59

[NICE NG59: Low back pain and sciatica](https://www.nice.org.uk/guidance/ng59/chapter/recommendations)

Bronjaar/gebruikte versie: 2020; type: richtlijn; gecontroleerd: 2026-10-07.

Context, behandeling en terughoudendheid met routinebeeldvorming.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### LRS

[NVN: Anamnese en lichamelijk onderzoek bij LRS](https://richtlijnendatabase.nl/richtlijn/lumbosacraal_radiculair_syndroom_lrs/anamnese_en_lichamelijk_onderzoek_bij_lrs.html)

Bronjaar/gebruikte versie: 2020; type: richtlijn; gecontroleerd: 2026-10-07.

Radiculaire klachten en neurologisch onderzoek.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### CES

[GIRFT National Suspected Cauda Equina Syndrome Pathway](https://gettingitrightfirsttime.co.uk/wp-content/uploads/2025/03/National-Suspected-Cauda-Equina-Pathway-February-2025.pdf)

Bronjaar/gebruikte versie: 2025; type: zorgpad; gecontroleerd: 2026-10-07.

Symptomen, beperkingen van uitsluiting en spoedbeoordeling. Britse route niet letterlijk als Nederlandse route overgenomen.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### SPA

[NICE NG65: Spondyloarthritis](https://www.nice.org.uk/guidance/ng65/chapter/Recommendations)

Bronjaar/gebruikte versie: 2017; type: richtlijn; gecontroleerd: 2026-10-07.

Herkenning en verwijzing bij verdenking axiale spondyloartritis.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### MSCC

[NICE NG234: Spinal metastases and metastatic spinal cord compression](https://www.nice.org.uk/guidance/ng234/chapter/recommendations)

Bronjaar/gebruikte versie: 2023; type: richtlijn; gecontroleerd: 2026-10-07.

Oncologische verdenking en neurologische spoedsignalen.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### INFECTION

[IDSA Native Vertebral Osteomyelitis](https://www.idsociety.org/practice-guideline/vertebral-osteomyelitis/)

Bronjaar/gebruikte versie: 2015; type: richtlijn; gecontroleerd: 2026-10-07.

Vertebrale infectie; richtlijn relatief oud, herbeoordeling nodig bij actualisatie.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### NOGG

[NOGG fracture risk and symptomatic vertebral fractures](https://www.nogg.org.uk/full-guideline/section-8-management-symptomatic-osteoporotic-vertebral-fractures)

Bronjaar/gebruikte versie: 2024; type: richtlijn; gecontroleerd: 2026-10-07.

Wervelfractuur, herstel en secundaire fractuurpreventie. Risicohoofdstuk: https://www.nogg.org.uk/full-guideline/section-3-fracture-risk-assessment-and-case-finding

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### TRAUMA

[NICE NG41: Spinal injury](https://www.nice.org.uk/guidance/ng41/chapter/Recommendations)

Bronjaar/gebruikte versie: 2016; type: richtlijn; gecontroleerd: 2026-10-07.

Traumatische wervelkolomletsels; spoedzorgcontext.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### STENOSIS

[NASS guideline summary: Degenerative lumbar spinal stenosis](https://pubmed.ncbi.nlm.nih.gov/23830297/)

Bronjaar/gebruikte versie: 2013; type: richtlijnsamenvatting; gecontroleerd: 2026-10-07.

Stenose; oudere bron. Aanvullend LRS voor klinische differentiatie.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### LISTHESIS

[NASS guideline summary: Degenerative lumbar spondylolisthesis](https://pubmed.ncbi.nlm.nih.gov/26681351/)

Bronjaar/gebruikte versie: 2016; type: richtlijnsamenvatting; gecontroleerd: 2026-10-07.

Degeneratieve spondylolisthesis; bron actualiseren voordat behandelregels worden geactiveerd.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### PARS

[Use of the one-legged hyperextension test and MRI in active spondylolysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC2465027/)

Bronjaar/gebruikte versie: 2006; type: diagnostisch onderzoek; gecontroleerd: 2026-10-07.

Beperking van eenbenige extensietest. Geen overname van historische beeldvormingsstrategie.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### SACRUM

[Risk factors associated with sacral stress fractures: a systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC4461718/)

Bronjaar/gebruikte versie: 2015; type: systematische review; gecontroleerd: 2026-10-07.

Onderscheid vermoeidheids- en insufficiëntiefracturen van het sacrum.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### STRUCTURE

[Low back pain of disc, sacroiliac joint, or facet joint origin: a diagnostic accuracy systematic review](https://pubmed.ncbi.nlm.nih.gov/37096189/)

Bronjaar/gebruikte versie: 2023; type: systematische review; gecontroleerd: 2026-10-07.

Anatomische pijnbronhypothesen en beperkingen van diagnostiek.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### SI

[Diagnostic accuracy of clusters of pain provocation tests for SI joint pain](https://pubmed.ncbi.nlm.nih.gov/34210160/)

Bronjaar/gebruikte versie: 2021; type: systematische review; gecontroleerd: 2026-10-07.

Positieve SI-testcluster bewijst de pijnbron niet.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### REDFLAGS

[Red flags to screen for malignancy and fracture in patients with low back pain](https://www.bmj.com/content/347/bmj.f7095)

Bronjaar/gebruikte versie: 2013; type: systematische review; gecontroleerd: 2026-10-07.

Beperkte waarde van veel afzonderlijke rode vlaggen; context en combinaties belangrijk.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### NOCIPLASTIC

[Chronic nociplastic pain affecting the musculoskeletal system: clinical criteria and grading system](https://pubmed.ncbi.nlm.nih.gov/33974577/)

Bronjaar/gebruikte versie: 2021; type: consensuscriteria; gecontroleerd: 2026-10-07.

Pijnmechanisme, geen orgaan- of weefseldiagnose en geen automatische conclusie uit psychologische factoren.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### OA

[NICE NG226: Osteoarthritis](https://www.nice.org.uk/guidance/ng226/chapter/Recommendations)

Bronjaar/gebruikte versie: 2022; type: richtlijn; gecontroleerd: 2026-10-07.

Klinische herkenning en conservatieve begeleiding bij artrose.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### FAI

[Warwick Agreement on femoroacetabular impingement syndrome](https://bjsm.bmj.com/content/50/19/1169)

Bronjaar/gebruikte versie: 2016; type: consensus; gecontroleerd: 2026-10-07.

FAI-syndroom vereist samenhang tussen klachten, klinische tekenen en beeldvorming.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### GLUTEAL

[Education plus exercise versus injection versus wait and see for gluteal tendinopathy](https://www.bmj.com/content/361/bmj.k1662)

Bronjaar/gebruikte versie: 2018; type: gerandomiseerd onderzoek; gecontroleerd: 2026-10-07.

Behandeling van geselecteerde gluteale tendinopathie; geen diagnostische richtlijn voor alle laterale heuppijn.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### AAA

[NICE NG156: Abdominal aortic aneurysm](https://www.nice.org.uk/guidance/ng156/chapter/Recommendations)

Bronjaar/gebruikte versie: 2020; type: richtlijn; gecontroleerd: 2026-10-07.

Herkenning van mogelijk symptomatisch/geruptureerd aneurysma.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### PAD

[NICE CG147: Peripheral arterial disease](https://www.nice.org.uk/guidance/cg147/chapter/recommendations)

Bronjaar/gebruikte versie: 2020; type: richtlijn; gecontroleerd: 2026-10-07.

Vasculaire claudicatio, onderzoek en begeleiding.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### STONES

[NICE NG118: Renal and ureteric stones](https://www.nice.org.uk/guidance/ng118/chapter/recommendations)

Bronjaar/gebruikte versie: 2019; type: richtlijn; gecontroleerd: 2026-10-07.

Medische beoordeling en beeldvorming bij nierkoliek; geen diagnose door fysiotherapeutische provocatie.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### PYELONEPHRITIS

[NICE NG111: Pyelonephritis](https://www.nice.org.uk/guidance/ng111/chapter/recommendations)

Bronjaar/gebruikte versie: 2018; type: richtlijn; gecontroleerd: 2026-10-07.

Medische behandeling, risicogroepen en escalatie.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### ENDOMETRIOSIS

[NICE NG73: Endometriosis](https://www.nice.org.uk/guidance/ng73/chapter/Recommendations)

Bronjaar/gebruikte versie: 2024; type: richtlijn; gecontroleerd: 2026-10-07.

Cyclische bekkenklachten en verwijzing. Publicatie oorspronkelijk 2017, inhoud geactualiseerd.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### MYELOMA

[NICE NG12: Suspected cancer, myeloma recommendations](https://www.nice.org.uk/guidance/ng12/chapter/recommendations-organised-by-site-of-cancer)

Bronjaar/gebruikte versie: 2015; type: richtlijn; gecontroleerd: 2026-10-07.

Persisterende bot-/rugpijn en onverklaarde fractuur; controleer actuele pagina vóór klinische implementatie.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### PGP

[RCOG: Pelvic girdle pain and pregnancy](https://www.rcog.org.uk/media/edcf20pq/pi_pgp_2025-pc.pdf)

Bronjaar/gebruikte versie: 2025; type: patiënteninformatie beroepsvereniging; gecontroleerd: 2026-10-07.

Zwangerschapsgerelateerde bekkenpijn; lager detailniveau dan een professionele richtlijn.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### ZOSTER

[CDC: Clinical features of shingles](https://www.cdc.gov/shingles/hcp/clinical-signs/index.html)

Bronjaar/gebruikte versie: 2024; type: publieke gezondheidsinformatie; gecontroleerd: 2026-10-07.

Dermatomale pijn en huidafwijkingen.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

### ECTOPIC

[NICE NG126: Ectopic pregnancy and miscarriage](https://www.nice.org.uk/guidance/ng126/chapter/recommendations)

Bronjaar/gebruikte versie: 2023; type: richtlijn; gecontroleerd: 2026-10-07.

Veiligheidscontext bij mogelijke zwangerschap met acute buik-/bekkenklachten.

inhoud via publicatie of zoekindex gecontroleerd; geen garantie op toekomstige URL-beschikbaarheid

## Benodigde inhoudelijke review

- Fysiotherapeut met expertise lage rug: inhoud, terminologie en klinische haalbaarheid
- Medisch inhoudsdeskundige: spoedcriteria en Nederlandse verwijspaden
- Broncontrole en datum-/versiebeheer per aandoening
- Controle op ongewenste bias, overdiagnostiek en belasting voor patiënt
- Pas na review afzonderlijk implementeren en klinisch valideren

Technische tests valideren bestandsintegriteit, niet medische juistheid.
