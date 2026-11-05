# Case 1 natt (#2892): hvilke saker v2 + av-regel finner som frossen bommer på

Sammenligner flaggene fra v2+av (`arbeid/c1_natt/v2av/svar/v2av_t<T>.csv`) med frossen repo4 (`arbeid/oppgave_2575/repo4_<T>_test.csv`), med målerens definisjon av MOT mot styret (anbefalt avvik der styret ikke sier MOT; fasit nbim_vote MOT og against_board 1). TP-tallene stemmer med DOM.md (49/51/31). Skript: `arbeid/oppgave_2892/sammenlign.py`, `forklar.py`, utskrift i `forklar_<T>.out`.

## Telling per testår
| år | nye TP | tapte TP | nye FP | fjernede FP | TP frossen → v2+av |
|---|---|---|---|---|---|
| 2024 | 6 | 1 | 5 | 13 | 44 → 49 |
| 2025 | 8 | 0 | 13 | 3 | 43 → 51 |
| 2026 | 0 | 1 | 4 | 13 | 32 → 31 |

Hvor endringene kommer fra (tekst = v2 uten av mot frossen, av = av-regelen etterpå):
- 2024: teksten legger til 6 TP og 11 FP, fjerner 6 FP og 1 TP. Av-regelen fjerner 13 FP og 0 TP.
- 2025: teksten legger til 10 TP og 24 FP. Av-regelen fjerner 13 FP og 2 TP.
- 2026: teksten fjerner 12 FP og 1 TP og legger til 5 FP. Av-regelen fjerner 2 FP.

**Ærlig lesning:** gevinsten er ikke at modellen finner mange nye MOT-stemmer. Over tre år gir den 14 nye TP og mister 2. Resten kommer fra færre falske flagg. I 2026 er hele gevinsten færre FP (TP går ned 32 → 31). I 2025 er det motsatt: teksten flagger mer, og av-regelen må rydde etter den.

## 5 konkrete eksempler (drivere = SHAP-bidrag fra SVD-kolonnene i LGBM-delen, refittet med samme kode)
1. **Lepu Medical og Bank of Jiangsu, 2024, nye TP (5 av 6 nye TP det året).** Kinesiske endringer av interne regelverk: «Amend Working System for Independent Directors», «Amend Related Party Transaction Management System» og «…External Guarantees». Frossen lå like under grensa (p 0,86–0,91). SVD-tekstkomponentene løfter dem: z14 (report/board of the), z16 (amend articles/of association) og z21 (reelect/articles), +0,3–0,5 hver. Teksten kjenner igjen et sakssett NBIM ofte stemmer mot, og det har ikke sakstypen fanget (typen er satt til OTHER_MGMT, RPT og til og med DIRECTOR_ELECTION).
2. **Colruyt Group, 2025, to nye TP.** «Reelect Korys Business Services I/II NV, Permanently Represented by …», altså gjenvalg av et selskap som styremedlem. Drivere: z22 (re-elect/repurchase/authorize), z10 (statutory auditor/appoint) og z46. Teksten skiller denne formuleringen fra vanlige styrevalg.
3. **Fine Organic Industries, India, 2024 og 2025: både treff og bom.** Nye TP: «Reelect Tushar Shah» (2024, z21) og «Continuation of Mukesh Shah as Chairman and Whole Time Director» (2025, z53/z22). Ny FP: «Reelect Bimal Shah» (2025). Modellen lærer «styrevalg i dette selskapet» og flagger hele familien. Det er riktig for to av tre.
4. **Fire taiwanske «Approve Amendments to Articles of Association», 2025, nye FP** (Taiwan Speciality Chemicals, Fositek, China Motor, Lumosa). Drivere: z54 (of association/report on) og z46 (+0,15–0,21). Generisk tekst og generiske komponenter, og NBIM stemte FOR. Dette er tekstsporets typiske feil: standardformuleringer som deler ord med saker NBIM stemmer mot.
5. **Koreanske «Elect X as Inside Director», 2025–26: blandet.** Ny TP: Hanwha Galleria (2025). Nye FP: Sindoh og HMM (2025), GS P&L og LS Marine (2026). z22 er hoveddriveren (+0,27–0,44). Komponenten fanger «inside director», men skiller ikke mellom selskapene.

Tapte TP (2 stk.: Western Superconducting 2024, «Amend Rules … Meetings of Board»; The Monogatari 2026, «Elect Director Kato») er grensetilfeller. p falt rett under grensa (0,933 → 0,922 og 0,948 → 0,938), ingen systematisk feil.

## SVD-komponentene som går igjen (største vekter)
- z16/z15 (k32/k64): amend articles, of association. z14: report of/board of the. z21: reelect, elect director, articles.
- z22: re-elect, repurchase, authorize (2024/25); i k48 (2026): repurchase, share repurchase program.
- z46 (k64): financing, equity plan. z53 (k64): appointment of, approve appointment. z54 (k64): of association, report on.
- SVD-kolonnene står for 41–47 % av gain i LGBM-delen. Ingen enkeltkomponent dominerer, og bidragene er spredt på 3–6 komponenter per sak.

## Forbehold
- SHAP er hentet fra en ny tilpasning av bare LGBM-delen (samme kode, frø og data). Den endelige p er et rang-snitt med LR, så p-verdiene over er fra svarfilene, ikke fra refiten.
- Komponentene har ulik betydning per år (k og treningsdata endrer seg), så z22 i 2024 er ikke z22 i 2026.
- Ingen ny modell og ingen nye tall på test. Dette er bare forklaring av eksisterende svarfiler.
