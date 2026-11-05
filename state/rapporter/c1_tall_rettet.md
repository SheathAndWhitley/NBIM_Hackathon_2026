# Case 1: gamle tall rettet i README, METODE, JURYSVAR og 1-sideren (speider #2104)

Hovedtallet står nå likt i alle fire filene: **F1 0,476 [0,36; 0,59] på MOT mot styret**, test 2026, real_votes,
frosset #2044 miks h2, måler v3 `--score mot` (#2087, #2090, KI #2095). 0,4818 er merket som *avvik* (sidetall, inkl. AVSTÅ).

## Endringer
| fil | hva |
|---|---|
| `levering/README.md` | Boks med hovedtallet øverst. «Standard er 10 (F1 0,474286, 119 saker)» er byttet med 228 av 1578 (14,4 %, #2094). «Maskinens egne svar (F1 0,474)» er nå 0,476 på MOT. Rutingtabellen er merket som gammel N-PX-agent, rad 0 «0,474 (N-PX)». KJORING_*.txt er merket som N-PX. 0,4818 er merket som avvik |
| `levering/METODE.md` | Boks med hovedtallet og en «Les dette først» som beskriver #2044 (LR+LightGBM, historikk bare fra år før, assert på forbudte kolonner, grense 0,9188 fra val) og sier at pkt. 1–8 gjelder N-PX. Pkt. 2 og 5 har nye titler. «Hovedtall: F1 0,474» heter nå «N-PX-modellens tall (ikke lenger hovedtall)». Tabellradene er merket N-PX. Målerlinja peker på v3 `--score mot` og ki_mot.py |
| `levering/JURYSVAR.md` | Boks med hovedtallet. Svar 1 (treff 95,7 % mot 96,2 %, regnet fra TP 30 FP 38 FN 28 av 1539), 3 (grensen låst på val), 4 (0,476 [0,36; 0,59], 58 MOT, val 0,520) og 5 (følg styret 0; historikkregel er **ikke målt** på real_votes) er skrevet om. Svar 2, 7 og 9 er merket N-PX |
| `c1/leveranse/kravrespons.md` (1-sideren, H1) | Skrevet om: #2044-modellen, tabell følg styret mot 0,476 [0,36; 0,59], avvik 0,4818 merket som sidetall, ruting med bånd fra val (ikke «konfidens < 0,6»), ett kall `bash leveranse/kjor.sh`. Fjernet: 0,383-regelen som modell, «LightGBM slo ikke regelen», «0 av 158 snudd», «sitatlaget gir 0 MOT» |

## Aksepttest
`grep -nE "0,474|0,383|0[.,]4818" levering/{README,METODE,JURYSVAR}.md c1/leveranse/kravrespons.md | grep -viE "N-PX|ikke hovedtall|avvik|gulvregel"`
gir 3 linjer, og alle er merket i konteksten (METODE l.14 «ikke hovedtallet» på neste linje, JURYSVAR svar 2 har N-PX i tittelen, README l.32 «0,474 er ikke hovedtallet»). Ingen 0,474/0,383 står som hovedtall.

## Ikke gjort / åpent
- Treffprosent 95,7/96,2 % er regnet fra TP/FP/FN, ikke målt i en egen kjøring.
- Historikkregelen er ikke målt på real_votes med v3 `--score mot`. Dette er et hull i «slår vi en enkel regel?» (juryen vil spørre). Forslag til smed: ett kall med regelen gjennom v3 `--score mot`.
- Ruting: README og 1-sideren bruker 228/1578 (#2094, kald kopi), c1_tall_likt.md har 176/1578 (#2095). Tallene er fra ulike kjøringer og bør avklares ved frys.
- Rå logger (`KJORING_til_menneske_*.txt`, `kjor_agent_holdout2026.txt`) er ikke endret. De er N-PX og bør ut av pakken (#1975/dommer).
- Etter frys kl. 16: bytt 0,476 overalt med `grep -rn "0,476\|0,36; 0,59" arbeid/hack/levering arbeid/hack/c1`.
