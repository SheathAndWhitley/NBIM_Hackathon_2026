# Case 1: utkast til avsnitt i ERLIG_EVALUERING om sammenligning med et annet lags løsning

Ikke lagt inn i pakka (frosset 16:00). Tallene under kommer fra smed4s måling (state/rapporter/c1_nbim_repo_sammenligning.md, oppgave 2464), så plassholderne er allerede fylt. Ordføreren avgjør om avsnittet skal inn, og dommeren (oppgave 2465) dømmer tallene.

## Avsnittet (11 linjer)

**Sammenligning med et annet lags løsning.** Et annet lag har løst samme oppgave på NBIMs stemmedata. De bruker to ting. Først en presedensregel: har NBIM tidligere stemt mot styret i samme sak eller mot samme styremedlem i samme selskap, flagges saken. Deretter en logistisk regresjon på saksteksten og enkle felt, med terskel satt for best F1 i et valideringsår.
De rapporterer F1 0,518. Det tallet kan ikke settes rett ved siden av vårt 0,476. Testen deres er 2025 og 2026 samlet, vår er bare 2026. De teller avvik inkludert avståelser, vi teller bare stemmer MOT styret. Og testen deres inneholder 2026, så valgene deres kan være tatt med teståret synlig. Vår modell ble frosset før vi så testen.
Vi kjørte derfor koden deres uendret på vår test (58 stemmer mot styret i 2026). Presedensregelen alene gir F1 0,515. Hele løsningen gir 0,523 med deres treningsår og 0,545 med våre (trent til og med 2024, valgt på 2025). Vår modell gir 0,476.
Forskjellen er bare sikker for den siste varianten: +0,07, 95 % konfidensintervall +0,01 til +0,13 (bootstrap per selskap). De andre ligger innenfor støyen. Vår modell rangerer best (PR-AUC 0,525 mot 0,41–0,44), men den flagger flere saker (68 mot 52) med lavere presisjon (0,44 mot 0,58). Presedensregel først og strammere terskel er derfor det første vi ville prøvd i neste versjon.

## Sjekk
- Ingen interne oppgavenumre i avsnittet (grep under).
- Alle tall står i tabellen i c1_nbim_repo_sammenligning.md.
