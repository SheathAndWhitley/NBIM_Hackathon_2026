# Måler for Case 1 på NBIMs ekte stemmer (dommer2 #2020)

**T+0 kl. 11:42 var ikke en ny case.** Det var gudens rettede Case 1-data (ordre #227/#228). `hack_case_auto`
tolket filene som ny hack og la ut #2019-#2027. Ordføreren har fått #2033 om å rydde og bruke måleren.

## Måleren (v0 og v1 i ett)
- `bash arbeid/hack/maaler.sh SVAR [VINDU]` -> `arbeid/hack/c1/maaler_nbim.py`. Bare stdlib, `python3 -I`.
- Svar: `id` (= `meeting_id|item_no`), `anbefaling` (FOR/MOT/AVSTÅ eller 0/1 for avvik), valgfri `konfidens`, `p_avvik`.
- SCORE = F1 på avvik fra styret (against_board), høyere er bedre. Også presisjon, recall, PR-AUC og ruting.
- Vinduer: npx_train/val/test = split_year 2024/2025/2026 (arrangørens egen). real_*: år <=2024 / 2025 / 2026.
- injection_flag=1 (141 rader i npx) holdes utenfor SCORE og telles for seg (motstandstesten).
- Ugyldig (exit 1, `SCORE nan`): id mangler, dupl. id, ukjent anbefaling, konfidens utenfor [0,1]. Testet.
- Inndata uten fasit: `arbeid/hack/c1/data_nbim/<npx|real>_<vindu>_input.csv`, train med fasit, eksempelfiler.
- sha1: maaler.sh e43b3e44, maaler_nbim.py 8616c57d.

## Tall (målt)
| svar | npx val | npx test | real val | real test |
|---|---|---|---|---|
| følg styret | 0 | 0 | 0 | 0 |
| alltid avvik | 0,093 | | | |
| aksjonærforslag -> avvik | **0,610** | **0,645** | 0,064 | 0,195 |

## Funn som angår leveransen
1. **Én regel gir F1 0,645 på npx test.** Aksjonærforslag er avvik i 99-100 % av tilfellene i 2025-26. Alt vi
   melder på disse dataene må slå denne regelen, ikke bare «følg styret». Vårt gamle 0,47-0,51 er målt på andre data.
2. **Lekkasje:** `rationale_text` finnes på 618 av 744 avvik i real og bare 9 av 12 580 ikke-avvik. Den og
   `position_paper`, `rationale_section`, `nbim_vote*` og `against_board` er forbudt som feature. `*_input.csv` har dem ikke.
   Begrunnelsene kan brukes som sitatkilde, bare fra train-året.
3. De to filene er ulike: real er NBIMs API med 5,4 % avvik og et svakt gulv. npx er SEC-sammenstillingen.
4. Bolktabell: `arbeid/hack/BOLKER.md`. 400 av 729 avvik på val ligger i styrevalg og rutine, og gulvet treffer ingen av dem.

## Ikke gjort
v2 (uavhengig måler) står ikke. Den gir mindre enn en ruting- og gulvsjekk på de nye dataene før kl. 13.
