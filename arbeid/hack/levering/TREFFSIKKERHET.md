# Case 1: treffsikkerhet i klartekst (levert modell repo4 = #2044 miks h2 + 4 repotrekk, test 2026)

Spørsmålet: når agenten sier «stem MOT styret», hvor ofte har den rett, og hvor mange MOT-stemmer finner den?
Positiv klasse = NBIM stemte MOT og det var mot styret (fasit: `nbim_vote == MOT` og `against_board == 1`).
Data: arrangørens rettede `real`-data, år 2026, 1539 saker med fasit. Maskinen alene (ingen menneskelig overstyring).

## Alle 1539 saker

|                         | Fasit: MOT styret | Fasit: ikke MOT |
|-------------------------|------------------:|----------------:|
| **Agenten: MOT styret** | TP **32**         | FP **35**       |
| **Agenten: ikke MOT**   | FN **26**         | TN **1446**     |

- Accuracy: **96,0 %** (1478 av 1539). Følg styret: **96,2 %** (1481 av 1539).
- Recall MOT: **55,2 %** (32 av 58 ekte MOT-stemmer funnet).
- Presisjon MOT: **47,8 %** (32 av 67 MOT-forslag er riktige).
- Riktig på FOR (ikke-MOT-saker): **97,6 %** (1446 av 1481).
- F1 på MOT: 0,512 (måleren), 95 % KI 39,7–61,6 % (bootstrap over saker, se under). Følg styret: 0,000.

**Hvorfor accuracy lurer:** bare 58 av 1539 saker (3,8 %) er MOT mot styret, så en agent som aldri sier MOT
får 96,2 % riktig og finner null av sakene som betyr noe. Vår agent har litt lavere accuracy fordi den tør å si MOT,
og det er nettopp det som gir F1 og recall på MOT.

> Språk (#2345): «konfidens < 0,6» under er målerens navn på flagget `til_menneske`. Det er de samme 161 sakene som båndet [0,15; 0,85) pluss vaktene i `JURY.md` pkt 8 (ukjent selskap/type, instruks, datafeil, MOT uten sitat).

## Saker som IKKE går til menneske (konfidens ≥ 0,6): 1378 saker

|                         | Fasit: MOT styret | Fasit: ikke MOT |
|-------------------------|------------------:|----------------:|
| **Agenten: MOT styret** | TP **11**         | FP **3**        |
| **Agenten: ikke MOT**   | FN **18**         | TN **1346**     |

- Accuracy 98,5 % (følg styret på de samme sakene: 97,9 %).
- Presisjon MOT 78,6 % (11 av 14), recall MOT 37,9 % (11 av 29), riktig på FOR 99,8 % (1346 av 1349).
- Ærlig: uten menneske slipper 18 bomme MOT-er (FN) og 3 falske MOT-er gjennom. Med den frosne modellen (#2044) var det 17 FN og 0 FP; repo4 er sikrere på flere saker og sender derfor færre til menneske (161 mot 183).

## Usikkerhet: 95 %-intervall (bootstrap, #2185)

Bare 58 ekte MOT-er i test, så tallene over er usikre. Bootstrap: 2000 trekk av de 1539 sakene med
tilbakelegging, 2,5- og 97,5-persentil (P og R: `treffsikkerhet_ki.py`, frø 2185; F1: frø 0, #2592). Clopper-Pearson (eksakt binomial) står ved siden av som kontroll.

| Del | Mål | Punkt | Bootstrap 95 % | Clopper-Pearson 95 % |
|---|---|---:|---:|---:|
| **Alle 1539 saker** | **F1 MOT (hovedtall)** | **51,2 %** | **39,7–61,6 %** | – (klyngebootstrap per selskap: 40–62 %, `oppgave_2095/ki_mot.py`) |
| Alle 1539 saker | recall MOT | 55,2 % | 42,6–67,9 % | 41,5–68,3 % |
| Alle 1539 saker | presisjon MOT | 47,8 % | 36,4–59,6 % | 35,4–60,3 % |
| Konfidens ≥ 0,6 (1378 saker) | recall MOT | 37,9 % | 20,0–57,1 % | 20,7–57,7 % |
| Konfidens ≥ 0,6 (1378 saker) | presisjon MOT | 78,6 % | 53,3–100 % | 49,2–95,3 % |

- Ærlig lesning: recall kan like gjerne være 43 % som 68 %, og presisjon 36–60 %. Forskjeller mellom modeller
  på noen få prosentpoeng i F1 er innenfor støyen.
- Presisjon i båndet ≥ 0,6 bygger på bare 14 MOT-forslag; sann presisjon kan være ned mot 49 %.
- Intervallene gjelder variasjon over saker i 2026-testen, ikke skift mellom år eller selskaper.

## Terskelen er valgt på val 2025, ikke på test (#2193, jf. S2 i JURY_SPORSMAL)

Agenten sier MOT når p ≥ 0,9232. Terskelen og C velges sammen i `c1_real.kjor_modell` (repo4: `modell_repo4.py`): modellen trenes på år < 2025,
og vi tar den terskelen som gir høyest F1 på val 2025. Valget gjøres på avvik fra styret inkludert AVSTÅ, i et rutenett av kvantiler.
Test 2026 kjøres én gang med samme rå terskel (`train.py:116`). Tabellen viser MOT mot styret, maskin alene.

| terskel p ≥ | val P | val R | val F1 | test P | test R | test F1 | test TP/FP |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0,70 | 0,179 | 0,727 | 0,287 | 0,114 | 0,741 | 0,198 | 43/334 |
| 0,80 | 0,277 | 0,646 | 0,388 | 0,186 | 0,707 | 0,295 | 41/179 |
| 0,85 | 0,376 | 0,596 | 0,461 | 0,260 | 0,655 | 0,373 | 38/108 |
| 0,90 | 0,566 | 0,475 | 0,516 | 0,427 | 0,603 | 0,500 | 35/47 |
| **0,9232 (valgt)** | 0,657 | 0,444 | **0,530** | 0,478 | 0,552 | 0,512 | 32/35 |
| 0,95 | 0,690 | 0,404 | 0,510 | 0,633 | 0,534 | **0,579** | 31/18 |
| 0,97 | 0,732 | 0,303 | 0,429 | 0,765 | 0,448 | 0,565 | 26/8 |

Val 2025 har 1909 saker og 99 MOT mot styret. Test 2026 har 1539 saker og 58 MOT. Fet skrift er beste F1 i kolonnen.
- Valgt terskel har høyest val-F1 blant de sju radene. Den er ikke best på test: der vinner 0,95 med 0,579.
  Hadde vi valgt på test, ville vi tatt 0,95 og fått et for høyt tall. Vi beholder 0,9232 og melder 0,512.
- Avstanden på test mellom 0,512 og 0,579 er 1 TP færre og 17 FP færre, med bare 58 MOT. Den viser ikke at 0,95 er bedre
  på nye år, bare at terskelen ikke er justert etter test.
- Laget av `c1/terskel_val_test.py:14` (terskelrader) og `:17-19` (P/R/F1, samme regel som måler v3 `--score mot`).
  Kjøring: `arbeid/kandidater/smed2_c1_mot/.venv/bin/python arbeid/hack/c1/terskel_val_test.py`. Valgt rad gir TP 32 FP 35, det samme som måleren.

## Til sammenligning: de 161 sakene som går til menneske (konfidens < 0,6, 10,5 %)

| | Fasit: MOT styret | Fasit: ikke MOT |
|---|---:|---:|
| **Agenten: MOT styret** | TP 21 | FP 32 |
| **Agenten: ikke MOT**   | FN 8 | TN 100 |

32 av 35 falske MOT-er ligger her, og 21 av 32 riktige MOT-er. Tallene over er maskinens forslag før mennesket ser dem.

## Slik regnes tallene på nytt (fra kald start)

```
cd <repo>/arbeid/hack/c1
python3 -I maaler_offisiell_v3.py ../levering/kjor_agent_real_pred_maaler.csv test --data real
#  -> «MOT mot styret: TP 32 FP 35 FN 26 ... (58 i fasit)», «161 til menneske»
cd ../levering
python3 -I treffsikkerhet.py kjor_agent_real_pred_maaler.csv
#  -> 2x2 for alle, for konfidens >= 0.6 og < 0.6 (importerer reglene fra maaler_offisiell_v3.py)
python3 -I treffsikkerhet_ki.py kjor_agent_real_pred_maaler.csv
#  -> 95 %-intervall (bootstrap 2000 trekk, frø 2185, og Clopper-Pearson) for P og R, alle og konfidens >= 0.6
python3 -I ../c1/maaler_offisiell_v3.py baseline --data real test   # følg styret: TP 0 FN 58
```
TN = 1539 − 32 − 35 − 26 = 1446. Regnet på nytt for repo4 05.11 av smed (#2592).
