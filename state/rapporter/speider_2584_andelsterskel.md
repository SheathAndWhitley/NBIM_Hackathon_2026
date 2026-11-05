# Speider #2584: andels-terskel på frossen modell over tre testår (Case 1) — slår ikke bytteregelen

Vinkel fra #2399 (budsjett/rangering): samme frosne p_avvik, men i stedet for rå grense fra val
flagges samme ANDEL av sakene på test som grensen flagget på val. Regel skrevet før måling:
arbeid/oppgave_2584/REGEL.md. Kode: arbeid/oppgave_2584/andel.py. Offisiell måler (--score mot), base = oppgave_2581/base_*.

| testår | frossen F1 MOT | andel F1 MOT | diff (95 % KI, parret klyngebootstrap) |
|---|---|---|---|
| 2024 | 0,4545 | 0,4768 | +0,022 [-0,044; +0,083] |
| 2025 | 0,5143 | 0,4947 | -0,020 [-0,050; +0,014] |
| 2026 | 0,4762 | 0,5042 | +0,028 [+0,008; +0,050] |
| snitt | 0,4817 | 0,4919 | +0,010 |

Dom etter regel #265 (snitt +0,02, intet år -0,02): IKKE BYTT. Snitt bare +0,010, 2025 på -0,0195 (på grensen).
Funn til ERLIG_EVALUERING/NESTE_VERSJON: rå val-grense flagger for få i 2024 (57 mot 76 ved andel) og for mange i 2026
(74 mot 67): kalibreringen glir mellom år. Terskelvalget er en kilde til ±0,02-0,03 per år. Ikke nytt hovedtall.
Ikke sendt til dommer #2570 som kandidat (kom etter fristen for kandidater og består ikke regelen uansett).
