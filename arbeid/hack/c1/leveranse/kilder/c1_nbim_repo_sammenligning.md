# Case 1: teamets parallelle hybridløsning (ikke fra NBIM) målt på vår test 2026 (#2464, smed4)

*Rettet 05.11 (ordre #262): zipen er en løsning laget av andre i teamet, parallelt med agenten, ikke fra NBIM. «repoet» under betyr den løsningen. Tallene er uendret; «nbim» i filnavnet er historisk.*

Kode: `<arbeidsmappe>/oppgave_2464/kjor_nbim.py` (kjører repoets egen `ballot.py`/`ballot_model.py` med `python -I`, uendret, på vår offisielle real_votes; sha256 71ba51… er lik fila i repoet).
Gjenskaping: deres egne tall kom ut likt: hybrid avvik-F1 0,518 og persistence 0,491 på 2025-26 (169 avvik).
Måler: `maaler_offisiell_v3.py <svar> test --data real --score mot` (58 MOT i fasit). KI: `<arbeidsmappe>/oppgave_2103/diff_ki.py`, parret klyngebootstrap per selskap, 2000 trekk, B minus frossen #2044.

| rad | F1 MOT | P | R | flagget | avvik-F1 | PR-AUC | B−#2044, 95 % KI |
|---|---|---|---|---|---|---|---|
| vår frosne #2044 (full_test.csv) | **0,476** | 0,441 | 0,517 | 68 | 0,482 | 0,525 | – |
| deres persistence (samme sak/direktør avvek sist) | 0,515 | 0,605 | 0,448 | 43 | 0,477 | 0,318 | +0,039 [−0,051; +0,126] |
| deres modell alene (logreg C=3, deres splitt) | 0,465 | 0,561 | 0,397 | 41 | 0,469 | 0,441 | −0,012 [−0,121; +0,093] |
| deres hybrid, deres splitt (train ≤2023, valg 2024) | 0,523 | 0,547 | 0,500 | 53 | 0,520 | 0,427 | +0,046 [−0,039; +0,133] |
| deres hybrid, vår splitt (train ≤2024, valg 2025; valgte GBM) | **0,545** | 0,577 | 0,517 | 52 | 0,533 | 0,413 | **+0,069 [+0,007; +0,133]**, B<A i 1 % |

(«flagget» = MOT-flagg mot styret, TP+FP.) Svarfiler: `<arbeidsmappe>/oppgave_2464/svar_*_t2026.csv`. Tavleforsøk #1187-1189.

## Svar på ordre #254: ja, de har høyere tall, også på vår måler
Hva de gjør annerledes:
1. **Presedens først:** har NBIM avveket på samme sak (tekst uten tall) eller samme direktørnavn hos samme selskap ved et tidligere møte, flagges saken uansett modell. Denne regelen alene (0,515) slår vår frosne modell (0,476). Vi har historikk bare som features inni en modell.
2. **Færre og sikrere flagg:** terskelen settes for F1 på 2024/2025 på en isotonisk kalibrert score. Det gir 52-53 flagg med presisjon 0,55-0,58. Vi flagger 68 med presisjon 0,44. Vår rangering er faktisk best (PR-AUC 0,525 mot 0,41-0,44), så gapet ligger i presedensregelen og terskelen, ikke i modellen.
3. **Enkel tekstmodell uten navn og årstall:** TF-IDF med logreg eller GBM på strukturerte felt, valgt på PR-AUC i valideringsåret. De har ingen NPX og ingen GVG-ruting inne i scoren.

## Forbehold (ærlig)
- Bare raden med vår splitt har et KI som ligger helt over 0. De to andre gevinstene er innenfor støyen (58 positive).
- Testen deres (2025-26) inneholder 2026. Utformingen deres (presedensregelen, C-gitter, navnefjerning) kan derfor være valgt med 2026 synlig. Vår #2044 ble frosset før vi så testen. Selve tallene er likevel gjenskapt med deres uendrede kode.
- Del 3 er ikke gjort: vi har ikke kjørt vår modell på deres splitt. Måleren vår har heller ikke noe vindu for 2025-26 samlet. Deres tall på 2025-26 er avvik inkludert AVSTÅ, ikke MOT.
- Modellfrysen står. Ingenting er endret i pakka eller modellen. Om dette skal inn i ERLIG_EVALUERING/NESTE_VERSJON («presedens først og strammere terskel slår oss med +0,07»), avgjør Ordføreren. Neste versjon bør teste presedens først på vår rangering, fordi vår PR-AUC er høyest.
