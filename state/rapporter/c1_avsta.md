# Case 1: stemmer NBIM AVSTÅ, og hva betyr det for agenten (#2359)

Skript: `arbeid/oppgave_2359/tell_avsta.py`, utskrift `tell_avsta.txt`. Data: `arbeid/hack/CASE/20261105_114241_real_votes.csv`; agent: frossen #2044 (`levering/kjor_agent_real_maskin_alene.csv`, all konfidens 0,9; ruting fra `kjor_agent_real_pred_maaler.csv`, konfidens < 0,6 = menneske, 188 saker). Ingen endring i agent eller pakke.

## (1) AVSTÅ i real_votes (nbim_vote_raw = «Abstain» → nbim_vote = AVSTÅ)

| år | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 (test) | sum |
|---|---|---|---|---|---|---|---|---|---|
| AVSTÅ | 1 | 20 | 9 | 25 | 2 | 2 | 4 | **5** | **68** |
| alle saker | 1504 | 1539 | 1564 | 1828 | 1832 | 1942 | 1970 | 1578 | 13757 |

- Ja, NBIM avstår, men sjelden: 68 av 13 757 (0,49 %), 5 av 1578 i test 2026 (0,32 %). MOT (Against + Withhold) er 757, altså 11 ganger så vanlig.
- 47 av 68 er styrevalg (DIRECTOR_ELECTION). Styret anbefalte FOR i 36, MOT i 3, ingen anbefaling i 28.
- «Ikke stemt» i rådata: 283 tomme, 13 «Do Not Vote», 38 «One Year/Three Years» (say-on-pay-frekvens). Disse er uten fasit og ikke AVSTÅ. I test 2026: 35 tomme + 1 «One Year».

## (2) AVSTÅ-sakene i test 2026 mot agenten

| id | selskap | type | styret | agent | til menneske |
|---|---|---|---|---|---|
| 2039527\|16 | Vietnam Eximbank | styrevalg | FOR | FOR | ja (konf 0,5) |
| 2039527\|17 | Vietnam Eximbank | styrevalg | FOR | FOR | ja (konf 0,5) |
| 2042367\|19–21 | DocMorris (3 saker) | styrevalg | MOT | FOR (avvik nei) | nei |

- 2 av de 5 AVSTÅ-sakene er blant de 188 til menneske; 0 av 5 flagges MOT av agenten.
- Hovedtallet (streng MOT, F1 0,476) teller ikke AVSTÅ som positiv, så de 5 påvirker det ikke. I sidetallet (avvik fra styret, 0,482) er de 5 bom (FN).

## (3) Setning til BEGRENSNINGER.md (speider limer inn)

> NBIM avstår sjelden: 68 av 13 757 stemmer i real_votes 2019–2026 (0,5 %; 47 er styrevalg) og 5 av 1578 i test 2026, så agenten foreslår bare FOR eller MOT; av de 5 AVSTÅ-sakene i test 2026 flagger agenten ingen som MOT og sender 2 til menneske, og de påvirker ikke hovedtallet (F1 på MOT) fordi AVSTÅ ikke telles som MOT.

## Vurdering
Krav 1 er dekket ærlig med tall: AVSTÅ er under 1 % av stemmene, for få til en egen klasse (5 i test, 4 i val 2025). En AVSTÅ-klasse ville gitt et tall uten statistisk mening. Anbefaling: ingen endring i agenten; bruk setningen over. Etter fristen kan en regel «styrevalg der styret ikke anbefaler» vurderes, men 28 saker over 8 år er for tynt.
