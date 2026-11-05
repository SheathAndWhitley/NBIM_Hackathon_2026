# Case 1: tallkontroll 2 – BEGRENSNINGER pkt. 6 rettet, BESLUTNINGSSTOTTE kontrollert (dommer2 #2011)

**Kort fortalt:** BEGRENSNINGER.md hadde lekkende tall i pkt. 6 (#1955) og i pkt. 2 (0,51 → 0,44, eldre modell med lekkasje). Begge er rettet. Alle tallene i BESLUTNINGSSTOTTE.md stemmer med #1023/#1026/#1027 og `oppgave_1995/ruting_b.txt`. Der var ingenting å rette.

## BEGRENSNINGER.md (ligger i `arbeid/hack/c1/leveranse/`, ikke i `arbeid/hack/levering/` som oppgaven sa)
- Pkt. 6: 0,38→0,50 (test) / 0,37→0,42 (val) / 125 saker / system-F1 0,66 er byttet med **0,38→0,43 [0,35; 0,50] / 0,34→0,37 / 119 saker (ca. 120 per år) / 0,65 [0,58; 0,71]** (variant b, #1026/#1027). Kilden er nå case1_ruting_verifisert.
- Pkt. 2: tallet 0,51→0,44 kom fra den lekkende lederen (#1990). Det er tatt ut. Nå står val 0,43 (ett års historikk) mot test 0,47 (to år), med en merknad om at forskjellen blander historikk og år.
- Endringen er forklart i en kursiv linje nederst i fila.

## BESLUTNINGSSTOTTE.md – regnet om fra P/R (N = 1246, 129 MOT)
| tall i dok | regnet | kilde | ok |
|---|---|---|---|
| 10,4 MOT per 100 | 129/1246 = 10,35 | METODE pkt. 1 | ja |
| uten ruting: 17,7 flagg / 11,1 falske / 6,7 fanget / 3,7 oversett | 17,74 / 11,08 / 6,66 / 3,69 | #1023 P 0,376 R 0,643 | ja |
| 10 % sym: 9,6 rutet / 13,7 flagg / 23,3 sett / 7,9 falske / 7,3 fanget / 3,0 oversett | 9,55 / 13,72 / 23,27 / 7,87 / 7,30 / 3,05 | #1026 | ja |
| skjevt: 9,8 / 7,9 / 17,7 / 3,5 / 6,7 / 3,7 | 9,79 / 7,95 / 17,74 / 3,53 / 6,66 / 3,69 | #1027 | ja |
| fanget 62–78 % (95 % KI) | system-R [0,622; 0,777] | ruting_b.txt | ja |
| ca. 290 saker i året, 120 usikre | 290, 119 | #1026 | ja |
| 20 %: 7,6 fanget, 31 sett per 100 | 7,62 / 30,98 | ruting_b.txt sym 0.20 | ja |
| avvisning > 57 % | 1 − 0,427 = 0,573 | #1026 | ja |
| recall 0,64, P 0,38 | 0,643 / 0,376 | #1023 | ja |
| golden parachute F1 0,40 | 0,40 (variant b) | case1_undergrupper (#1992) | ja |
| 1544/1544 ordrett, 1/30 klart, 10 av 12 MOT | stemmer | case1_sitatsjekk (#1991) | ja |
| 15 av 64 snudd | referansemodellen, merket slik | BEGRENSNINGER pkt. 8 | ja |

## Grep (akseptkrav)
`grep -rnE "0,2031|0,013|125 saker|0,416|0,625|0,658|0,633|fra 0,38 til 0,50|0,51 til 0,44"` over `arbeid/hack/levering` og `arbeid/hack/c1/leveranse` (md): treff bare i rettelseslinja i METODE.md (#2005), som nevner de gamle tallene som trukket tilbake. I tillegg sier JURYSVAR.md «0,50 … er trukket tilbake». Begge står med vilje. Ingen lekkende tall brukes som gjeldende.

## Åpent
- Den ferske sitatstikkprøven (#2012, etter MOT-fiksen #2009) kan endre «1 av 30» og «10 av 12». Speideren (#1975) må oppdatere BESLUTNINGSSTOTTE etter den.
