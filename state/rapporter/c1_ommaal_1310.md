# Case 1: ommåling av selvrapporterte forsøk (#2173, dommer2, 13:10)

Måler: `maaler_offisiell_v3.py {sti} test --data real --score mot` (tavle-sha de049083d9, fil-sha 8b09c36e01), oppgave #2139.
NB: `forsok-ommaal` fant 0 kandidater. Den fanger bare forsøk med gammel målerhash, ikke vanlige selvrapporterte. Derfor gjorde jeg ommålingen for hånd med `tavle forsok --sti`. Rundens globale måler (#2034, 9d81a418dd) er v2, og den gir avvik-F1, ikke MOT-F1.

## Målt (gammel -> ny rad, F1 MOT)
| gammel | forsøk | meldt | målt |
|---|---|---|---|
| #1119 -> #1121 | kalibrert P(MOT) + bånd [0,15;0,85) | 0,4762 | 0,4762 |
| #1118 -> #1123 | frossen #2044 --hist 1 (nedre grense) | 0,4151 | 0,4151 |
| #1117 -> #1122 | regel b2 | 0,3650 | 0,3650 |
| #1116 -> #1130 | regel b | 0,2871 | 0,2871 |
| #1115 -> #1129 | regel a | 0,0974 | 0,0974 |
| #1110 -> #1124 | GVG-sitat i agenten (UGYLDIG før) | – | 0,4762 |
| #1111 -> #1125 | isotonisk P(MOT) | 0,4818 (avvik-F1) | 0,4762 |
| #1112–1114 -> #1126–1128 | menneskebånd q0,3/0,15/0,08 | 0,418/0,468/0,455 | 0,4762 alle |
| #1093, #1104 -> #1131, #1132 | frossen #2044 miks h2 | 0,4762 | 0,4762 |
| #1107 -> #1133 | demo.sh kald kopi | 0,4818 (avvik-F1) | 0,4762 |

Avvik mellom meldt og målt kommer av ulike tall, ikke av feil: smed3s båndtall er F1 bare på ikke-rutede saker. Ruting endrer ikke prediksjonen, så måleren gir 0,4762 på full test. 0,4818 er avvik-F1 (v2).
Jeg kjørte selv måleren på agent.csv, regel_b2 og hist1. TP/FP/FN er identiske med tavla.

## Kan ikke måles (grunn skrevet i notatet)
- #1028: gammelt id-format (1578 id mangler). Erstattet av frossen #2044.
- #969, #982: ingen fil, annet datasett (Vanguard data4/dataF).
- #991: måler v1-tida, PR-AUC.  #1002: VAL 2025, ingen fil.
- #1021, #1026, #1027: rutingstall (F1 på ikke-rutede) eller tekstrapport, ingen svarfil.
- Eldre (#938, #960–963, #971, #1030, #1031) hadde allerede grunn fra automål.

## Resultat
Ingen c1-forsøk fra i dag står selvrapportert uten målt tall eller grunn (SQL-sjekk: 0 rader). Hovedtallet 0,4762 er uendret, og ingen ommåling slår det.
