# Case 1: slår agenten huskeregelen «stem MOT der NBIM stemte MOT sist»? (smed2 #2350)

**Til JURY:** Ja, agenten slår huskeregelen med god margin: F1 MOT 0,476 mot 0,243 på test 2026 og 0,520 mot 0,254 på val 2025. KI-en for forskjellen ligger helt over null (test +0,23 [+0,12; +0,34]).

Måler v3 `--score mot` (sha256 418a937e57), data real_votes sha256 71ba5135…, 58 MOT mot styret i test 2026, 99 i val 2025.
Ingen agentfiler eller `levering/` er rørt. Frossen #2044 = `arbeid/oppgave_2103/full_{val,test}.csv` (test gir samme tall som `levering/kjor_agent_real_maskin_alene.csv`).

## Regelen (fast før måling)
For hver sak: finn **siste tidligere møte** (møtedato strengt før sakens) med samme nøkkel og kjent NBIM-stemme.
Stem MOT hvis NBIM der stemte MOT mot styret (nbim_vote MOT og against_board 1) på minst én sak med nøkkelen. Ellers følg styret.
- **A:** nøkkel = samme selskap + samme sakstype (`proposal_type`)
- **B:** nøkkel = samme selskap, hvilken som helst sak

Historikken går over alle år, løpende, som hovedmodellen. Saker fra samme møte eller senere brukes aldri.

## Tall
| Variant | Vindu | F1 MOT | P | R | TP | FP | FN |
|---|---|---|---|---|---|---|---|
| A selskap + sakstype | val 2025 | 0,254 | 0,176 | 0,455 | 45 | 210 | 54 |
| A selskap + sakstype | test 2026 | **0,243** | 0,151 | 0,621 | 36 | 202 | 22 |
| B selskap, alle saker | val 2025 | 0,162 | 0,093 | 0,636 | 63 | 618 | 36 |
| B selskap, alle saker | test 2026 | **0,125** | 0,068 | 0,741 | 43 | 587 | 15 |
| **frossen #2044 miks h2** | val 2025 | 0,520 | 0,608 | 0,455 | 45 | 29 | 54 |
| **frossen #2044 miks h2** | test 2026 | **0,476** | 0,441 | 0,517 | 30 | 38 | 28 |

Forskjell frossen minus regel (parret klyngebootstrap per selskap, 2000 trekk, seed 0, `arbeid/oppgave_2103/diff_ki.py`):
- A: val +0,266 [+0,156; +0,369], test **+0,233 [+0,118; +0,335]**. Regelen vinner i 0 av 2000 trekk.
- B: val +0,359 [+0,240; +0,469], test **+0,351 [+0,240; +0,462]**. Regelen vinner i 0 av 2000 trekk.

## Slik leses det
- Huskeregelen finner flere av MOT-sakene (recall 0,62 og 0,74 på test), men den flagger 238 og 630 saker for å finne 36 og 43. Agenten flagger 68 for å finne 30. Gevinsten til agenten er presisjon: den lærer *hvilke* gamle MOT-er som gjentar seg.
- Til ordre #250: også agenten flagger flere enn de som er ekte (FP 38 mot TP 30 på test), men huskeregelen gjør det i mye større grad (FP 202).
- Variant B ligner regel a i #2134 (selskap, MOT «noen gang», 0,097). «Sist gang» er litt bedre (0,125), men like svak i praksis.
- Den sterkeste enkle regelen vi har målt er fortsatt b2 i `c1_enkle_regler_og_hist1.md` (samme selskap + samme tekst, 0,365). Agenten slår også den.

## Kjøring fra kald kopi (fra hvilken som helst mappe)
```
D=$(mktemp -d); cp arbeid/oppgave_2350/huskeregel.py $D/; python3 -I $D/huskeregel.py $D/ut
```
Bare stdlib, under 10 s. Den skriver `regel_{A,B}_{val,test}.csv` og printer tabellen og KI-ene. Utskrift: `arbeid/oppgave_2350/kald_ut.txt`. Samme tall fra landsbymappa og /tmp-kopi (md5 av tabellen er lik).
Tavla: forsøk #1172 (A, 0,243) og #1173 (B, 0,125). Begge er selvrapportert, fordi tavla avviste automåling («måleren endret på disk, dommeren må sette den»). Dommeren kan måle filene med v3: `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2350/regel_A_test.csv test --data real --score mot`.
