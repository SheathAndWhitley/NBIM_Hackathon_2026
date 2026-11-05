# Case 1: treffsikkerhet i klartekst (frossen modell miks h2, test 2026)

> **Eldre tall:** linjer merket «eldre frossen modell #2044» gjelder modellen som var frossen før byttet til repo4 (#2572). Målte tall er ikke endret. Dagens hovedtall står i `arbeid/hack/c1/tall_tabell.md`.

Spørsmålet: når agenten sier «stem MOT styret», hvor ofte har den rett, og hvor mange MOT-stemmer finner den?
Positiv klasse = NBIM stemte MOT og det var mot styret (fasit: `nbim_vote == MOT` og `against_board == 1`).
Data: arrangørens rettede `real`-data, år 2026, 1539 saker med fasit. Maskinen alene (ingen menneskelig overstyring).

> Språk (#2345): «konfidens < 0,6» under er målerens navn på flagget `til_menneske`. Det er de samme 183 sakene som båndet [0,15; 0,85) pluss vaktene i `JURY.md` pkt 8 (ukjent selskap/type, instruks, datafeil, MOT uten sitat).

## Alle 1539 saker

|                         | Fasit: MOT styret | Fasit: ikke MOT |
|-------------------------|------------------:|----------------:|
| **Agenten: MOT styret** | TP **30**         | FP **38**       |
| **Agenten: ikke MOT**   | FN **28**         | TN **1443**     |

- Accuracy: **95,7 %** (1473 av 1539). Følg styret: **96,2 %** (1481 av 1539).
- Recall MOT: **51,7 %** (30 av 58 ekte MOT-stemmer funnet).
- Presisjon MOT: **44,1 %** (30 av 68 MOT-forslag er riktige).
- Riktig på FOR (ikke-MOT-saker): **97,4 %** (1443 av 1481).
- F1 på MOT: 0,476 (måleren), 95 % KI 36,8–58,1 % (bootstrap over saker, se under). Følg styret: 0,000. <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->

**Hvorfor accuracy lurer:** bare 58 av 1539 saker (3,8 %) er MOT mot styret, så en agent som aldri sier MOT
får 96,2 % riktig og finner null av sakene som betyr noe. Vår agent har lavere accuracy fordi den tør å si MOT,
og det er nettopp det som gir F1 og recall på MOT.

## Saker som IKKE går til menneske (konfidens ≥ 0,6): 1356 saker

|                         | Fasit: MOT styret | Fasit: ikke MOT |
|-------------------------|------------------:|----------------:|
| **Agenten: MOT styret** | TP **9**          | FP **0**        |
| **Agenten: ikke MOT**   | FN **17**         | TN **1330**     |

- Accuracy 98,75 % (følg styret på de samme sakene: 98,1 %).
- Presisjon MOT 100 % (9 av 9), recall MOT 34,6 % (9 av 26), riktig på FOR 100 % (1330 av 1330).
- Ærlig: det som slipper gjennom uten menneske er 17 bomme MOT-er (FN), ikke falske MOT-er.

## Usikkerhet: 95 %-intervall (bootstrap, sak 2185)

Bare 58 ekte MOT-er i test, så tallene over er usikre. Bootstrap: 2000 trekk av de 1539 sakene med
tilbakelegging, fast frø 2185, 2,5- og 97,5-persentil. Clopper-Pearson (eksakt binomial) står ved siden av som kontroll.

| Del | Mål | Punkt | Bootstrap 95 % | Clopper-Pearson 95 % |
|---|---|---:|---:|---:|
| **Alle 1539 saker** | **F1 MOT (hovedtall)** | **47,6 %** | **36,8–58,1 %** | – (klyngebootstrap per selskap: 36–59 %, sak 2095) |
| Alle 1539 saker | recall MOT | 51,7 % | 39,1–65,2 % | 38,2–65,0 % |
| Alle 1539 saker | presisjon MOT | 44,1 % | 32,8–56,2 % | 32,1–56,7 % |
| Konfidens ≥ 0,6 (1356 saker) | recall MOT | 34,6 % | 15,8–55,0 % | 17,2–55,7 % |
| Konfidens ≥ 0,6 (1356 saker) | presisjon MOT | 100 % | 100–100 % (degenerert) | 66,4–100 % |

- Ærlig lesning: recall kan like gjerne være 40 % som 65 %, og presisjon 33–56 %. Forskjeller mellom modeller
  på noen få prosentpoeng i F1 er innenfor støyen.
- Presisjon 100 % i båndet ≥ 0,6 bygger på bare 9 MOT-forslag. Bootstrap kan ikke trekke en FP som ikke finnes,
  så intervallet blir 100–100. Det eksakte intervallet sier at sann presisjon kan være ned mot 66 %.
- Intervallene gjelder variasjon over saker i 2026-testen, ikke skift mellom år eller selskaper.

## Til sammenligning: de 183 sakene som går til menneske (konfidens < 0,6, 11,9 %)

| | Fasit: MOT styret | Fasit: ikke MOT |
|---|---:|---:|
| **Agenten: MOT styret** | TP 21 | FP 38 |
| **Agenten: ikke MOT**   | FN 11 | TN 113 |

Alle 38 falske MOT-er ligger her, og 21 av 30 riktige MOT-er. Tallene over er maskinens forslag før mennesket ser dem.

## Terskelen er valgt på val 2025, ikke på test (sak 2193, jf. S2 i JURY_SPORSMAL)

Agenten sier MOT når p ≥ 0,9188. Terskelen og C velges sammen i `oppgave_2044/train.py:100-108`: modellen trenes på år < 2025,
og vi tar den terskelen som gir høyest F1 på val 2025. Valget gjøres på avvik fra styret inkludert AVSTÅ, i et rutenett av kvantiler.
Test 2026 kjøres én gang med samme rå terskel (`train.py:116`). Tabellen viser MOT mot styret, maskin alene.

| terskel p ≥ | val P | val R | val F1 | test P | test R | test F1 | test TP/FP |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0,70 | 0,173 | 0,687 | 0,276 | 0,109 | 0,759 | 0,190 | 44/360 |
| 0,80 | 0,262 | 0,646 | 0,373 | 0,189 | 0,707 | 0,298 | 41/176 |
| 0,85 | 0,369 | 0,586 | 0,453 | 0,260 | 0,655 | 0,373 | 38/108 |
| 0,90 | 0,541 | 0,465 | 0,500 | 0,400 | 0,586 | 0,476 | 34/51 |
| **0,9188 (valgt)** | 0,608 | 0,455 | **0,520** | 0,441 | 0,517 | 0,476 | 30/38 |
| 0,95 | 0,660 | 0,354 | 0,461 | 0,569 | 0,500 | **0,532** | 29/22 |
| 0,97 | 0,735 | 0,253 | 0,376 | 0,742 | 0,397 | 0,517 | 23/8 |

Val 2025 har 1909 saker og 99 MOT mot styret. Test 2026 har 1539 saker og 58 MOT. Fet skrift er beste F1 i kolonnen.
- Valgt terskel har høyest val-F1 blant de sju radene. Den er ikke best på test: der vinner 0,95 med 0,532.
  Hadde vi valgt på test, ville vi tatt 0,95 og fått et for høyt tall. Vi beholder 0,9188 og melder 0,476.
- Avstanden på test mellom 0,476 og 0,532 er bare 3–4 TP og ligger innenfor bootstrap-intervallet over.
  Den viser derfor ikke at 0,95 er bedre. Den viser bare at terskelen ikke er justert etter test.
- Laget av `c1/terskel_val_test.py:14` (terskelrader) og `:17-19` (P/R/F1, samme regel som måler v3 `--score mot`).
  Kjøring: `uv run --project arbeid/oppgave_2023 python arbeid/hack/c1/terskel_val_test.py`. Valgt rad gir TP 30 FP 38, det samme som måleren.

## Slik regnes tallene på nytt (fra kald start)

```
cd <repo>/arbeid/hack/c1
python3 -I maaler_offisiell_v3.py ../levering/kjor_agent_real_pred_maaler.csv test --data real
#  -> «MOT mot styret: TP 30 FP 38 FN 28 ... (58 i fasit)», «183 til menneske» <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->
cd ../levering
python3 -I treffsikkerhet.py kjor_agent_real_pred_maaler.csv
#  -> 2x2 for alle, for konfidens >= 0.6 og < 0.6 (importerer reglene fra maaler_offisiell_v3.py)
python3 -I treffsikkerhet_ki.py kjor_agent_real_pred_maaler.csv
#  -> 95 %-intervall (bootstrap 2000 trekk, frø 2185, og Clopper-Pearson) for P og R, alle og konfidens >= 0.6
python3 -I ../c1/maaler_offisiell_v3.py baseline --data real test   # følg styret: TP 0 FN 58
```
TN = 1539 − 30 − 38 − 28 = 1443. Sjekket 05.11 av smed3 (sak 2175).
