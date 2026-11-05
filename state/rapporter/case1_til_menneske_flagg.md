# Case 1: forvalteren velger andelen til menneske (`--til-menneske`, smed #2029)

`kjor_agent.py --til-menneske PROSENT` (standard 10). Båndet rundt grensen låses på val 2025 så PROSENT
av val-sakene rutes; test brukes aldri til å velge. Standard gir byte-lik agent.csv med kjøringen 11:43
(fremmed.sh), SCORE 0,474286, 119 saker til menneske. `--til-menneske 0` slår av båndet.
fremmed.sh sender ekstra argumenter videre: `sh arbeid/hack/levering/fremmed.sh /tmp/f --til-menneske 15`.

| PROSENT | Til menneske (test 2026) | derav MOT | Treff hele systemet | F1 hele systemet |
|---|---|---|---|---|
| 0 | 0 | 0 | 85,2 % | 0,474 |
| 5 | 56 (4,5 %) | 8 | 87,3 % | 0,524 |
| 10 | 119 (9,6 %) | 18 | 89,1 % | 0,572 |
| 15 | 188 (15,1 %) | 26 | 91,1 % | 0,629 |
| 20 | 270 (21,7 %) | 37 | 92,6 % | 0,674 |

Hele systemet = rutede saker antas avgjort riktig av mennesket (øvre grense, samme regning som dommer
#2010). Raden for 10 % er lik dommer #2010s rad 4. Rapporten fra #2017 fantes ikke ennå da dette ble gjort,
så tallene er regnet av kjor_agent.py selv (ny linje i KJORING.txt); dommer #2017 bør bekrefte dem.
Maskinens egne svar endres ikke av flagget (F1 0,474286 i alle kjøringene).

Bevis: arbeid/hack/levering/KJORING_til_menneske_10.txt og _15.txt (kalde kjøringer 05.11),
README-tabell, robust.py (arbeid/oppgave_2000) 12/12 ok etter endringen.
Obs: alt er på gamle data_v3. Arrangørens rettede NPX-data (ordre #227/#228) er ikke med her.
fremmed.sh /tmp/fremmed2029 --til-menneske 15 (env -i, ren kopi): 188 til menneske, treff 91,1 %, F1 0,6288, 35 s — samme som over.
