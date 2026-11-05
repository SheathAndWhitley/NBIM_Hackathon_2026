# Case 1: F1 på bare MOT (uten AVSTÅ) for den frosne modellen miks h2 (smed sak 2087)

> **Eldre tall:** linjer merket «eldre frossen modell #2044» gjelder modellen som var frossen før byttet til repo4 (#2572). Målte tall er ikke endret. Dagens hovedtall står i `arbeid/hack/c1/tall_tabell.md`.

**Kort:** På bare MOT mot styret får den frosne modellen **F1 0,476 på test 2026** (P 0,441, R 0,517). Det er 0,006 under avvikstallet 0,482. På val 2025 er tallet 0,520, mot 0,522 for avvik. Forskjellen er liten fordi nesten alle avvik er MOT. Det er bare 5 AVSTÅ i test, og ingen i val som telles.

## Hvorfor måleren viste «streng MOT: TP 0 FP 0 FN 0»
`maaler_offisiell_v2.py` setter `mot = None` når svaret er 0/1 (agentens `pred_maaler.csv` / maskin-alene-fila) eller `rad,p`. Da blir streng MOT aldri telt. Ny fil `arbeid/hack/c1/maaler_offisiell_v3.py` (v2 er ikke endret på disk). Den oversetter avvik til agentens anbefaling slik `c1_real.py` gjør: avvik med styret MOT blir FOR, andre avvik blir MOT, og uten avvik følger agenten styret. Den har også en ny linje, **«MOT mot styret»**: fasit er `nbim_vote` MOT og `against_board` 1 (hovedmålet). Med `--score mot` blir dette SCORE. Standard er fortsatt avvik, så gamle tall kan sammenlignes.

## Tallene side om side (samme prediksjoner, grense 0,9188 låst på val)
| mål | val 2025 (TP/FP/FN) | P | R | F1 | test 2026 (TP/FP/FN) | P | R | F1 |
|---|---|---|---|---|---|---|---|---|
| avvik fra styret (MOT+AVSTÅ, dagens hovedtall) | 48/33/55 | 0,593 | 0,466 | 0,5217 | 33/38/33 | 0,465 | 0,500 | **0,4818** |
| **MOT mot styret (hovedmålet)** | 45/29/54 | 0,608 | 0,455 | **0,5202** | 30/38/28 | 0,441 | 0,517 | **0,4762** |
| v2/v3 «streng MOT» (all NBIM-MOT, også MOT sammen med styret) | 54/30/58 | 0,643 | 0,482 | 0,5510 | 38/41/28 | 0,481 | 0,576 | 0,5241 |

**I fasit (rader med `against_board`):**
- Val 2025: 103 avvik. Det er 99 FOR→MOT og 4 MOT→FOR. Ingen AVSTÅ telles. De 4 AVSTÅ-radene i 2025 mangler `against_board`.
- Test 2026: 66 avvik. Det er 58 FOR→MOT, 3 MOT→FOR, 3 MOT→AVSTÅ og 2 FOR→AVSTÅ, altså **5 AVSTÅ**. Alle 5 er avvik.

Modellen flagger 71 saker i test. 68 av dem blir anbefalt MOT og 3 blir FOR (der styret sier MOT).

Den tredje raden er ikke målet: den gir poeng for MOT der NBIM følger styret (8 slike i test). Den bør ikke brukes som hovedtall.

## Reproduser
```
.venv/bin/python <arbeidsmappe>/oppgave_2087/streng_mot.py
```
Kommandoen kjører `oppgave_2044/train.py` uendret med `--variant miks --hist 2` og skriver `<arbeidsmappe>/oppgave_2087/svar_val.csv` og `svar_test.csv`. Så måler den begge med v3 og `--score mot`. Testfila gir samme tall som agentens `kjor_agent_real_maskin_alene.csv`: `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/hack/levering/kjor_agent_real_maskin_alene.csv test --data real`. Ingen modell, grense eller trekk ble valgt her. Test er bare målt.

## Hva som skal stå i JURY.md
Hovedtallet skal være **F1 0,476 på MOT mot styret i test 2026 (P 0,44, R 0,52; 30 av 58 MOT funnet, 38 falske alarmer)**, siden hovedmålet sier F1 på MOT. 0,482 kan stå ved siden av som «avvik fra styret inkl. 5 AVSTÅ». Det må ikke kalles F1 på MOT. <!-- eldre: frossen #2044 (0,476), dagens hovedtall er repo4 0,512 --> <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->
