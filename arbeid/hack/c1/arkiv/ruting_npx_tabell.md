# Arkiv: rutingtabell for den gamle N-PX-agenten (flyttet fra levering/README.md, #2135)

Gjelder ikke den leverte modellen (#2044 på real_votes). Se README «Send til menneske» for den.

**Gammel N-PX-agent, ikke standarden:** målt på N-PX holdout 2026 (1246 saker, 129 avvik), kald kjøring 05.11 (#2029).
Tabellen viser bare hvordan ruting virker. Den er ikke målt på nytt for #2044 (se `c1_ruting_kostnad.md`, #2100). «Hele systemet»
antar at mennesket avgjør de rutede sakene riktig, så det er en øvre grense:

| `--til-menneske` | Saker til menneske (test) | derav MOT | Treff hele systemet | F1 hele systemet |
|---|---|---|---|---|
| 0 | 0 (0,0 %) | 0 | 85,2 % | 0,474 (N-PX) |
| 5 | 56 (4,5 %) | 8 | 87,3 % | 0,524 |
| 10 (standard) | 119 (9,6 %) | 18 | 89,1 % | 0,572 |
| 15 | 188 (15,1 %) | 26 | 91,1 % | 0,629 |
| 20 | 270 (21,7 %) | 37 | 92,6 % | 0,674 |

«Følg styret» treffer 89,6 % med F1 0. Andelen på test kan avvike litt fra PROSENT fordi
båndet er låst på val (20 % på val ble 21,7 % på 2026). Kjøringene for 10 og 15 ligger i
`KJORING_til_menneske_10.txt` og `KJORING_til_menneske_15.txt` (N-PX-agenten, `SCORE 0.474286` der er ikke hovedtallet).
