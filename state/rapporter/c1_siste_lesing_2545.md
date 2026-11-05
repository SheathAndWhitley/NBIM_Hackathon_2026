# Case 1: siste jurylesing av README og kravrespons (#2545)

Lest fra toppen som jury med 5 min, etter #2543/#2544. Ingen filer endret.

**Konklusjon:** Hovedtallet 0,476 (F1 på MOT, KI [0,36; 0,59]) er det første tallet juryen ser i begge filene
(README:8, kravrespons:4). Beslutningen «V1 står» kommer i hovedtallsboksen (README:11) og i kravrespons:10.
Ingen setning i de to filene sier at V2 eller hybriden er hovedtallet. Tallene 188/1578, 183/1539, 30/58, 0,415, 0,365, 0,520 stemmer med BEGRENSNINGER, ERLIG_EVALUERING og JURY_SPORSMAL sp. 19.

## Funn (maks 5, viktigst først)
1. **Motsigelse utenfor de to filene, men juryen kan lese den:** `ERLIG_EVALUERING.md:56` sier at tidligere stemmer
   er kjent «fordi NBIM publiserer stemmene løpende». Kravrespons:10 sier at dette er «antatt og ikke dokumentert», og JURY_SPORSMAL («Hull vi kjenner») kaller det en antakelse. Forslag: «det antar vi (NBIM publiserer trolig løpende, ikke dokumentert)».
2. **«Valgt på 2025, kjørt én gang» er litt for rent:** kravrespons:7 og README:9 sier at modell og grense er valgt på val. Rutingsbåndet [0,15; 0,85) ble likevel valgt fra test-tabellen (JURY_SPORSMAL:27, ERLIG_EVALUERING:56). Det endrer ikke F1, men det er det eneste testvalget, og det står ikke i noen av de to filene. Forslag: legg til en halv setning i kravrespons:7 om at båndet for ruting er valgt på test og sjekket på val.
3. **Kjøretid i tre versjoner:** README:43 sier «29 s», README:44 sier «29–52 s», og ERLIG_EVALUERING:70 sier «31–52 s». Det er lite, men en jury som teller kan se det. Forslag: bruk «29–52 s» overalt.
4. **«Rundt 0,5» (kravrespons:10) kan leses som pynt:** KI-en er [0,36; 0,59], og punktet er 0,476. Setningen sier at punktet er under målet, så den er ærlig, men «rundt 0,5» høres ut som avrunding opp mot målet. Forslag: «tallet bør leses som et sted mellom 0,36 og 0,59».
5. **Dobbel forklaring av SCORE-linja** står i README:46 og README:54. Den er riktig, men den gjentar seg og tar plass i en lesing på 5 minutter. Lav prioritet, og den kan stå hvis tekststoppen nærmer seg.

Ingen av funnene endrer et tall. Funn 1 og 2 handler om ærlighet (60 % av juryvekten), funn 3–5 er kosmetikk.
