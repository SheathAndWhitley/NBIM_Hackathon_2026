# Case 1: stikkprøve av 20 tall som tallsjekken bare fant i logger (#2278, dommer, 05.11 14:35)

Trekk: 20 tilfeldige (frø 2278) blant de 70 «funnet B»-tallene i JURY.md, JURYSVAR.md, EN_SIDE.md og BESLUTNINGSSTOTTE.md der kilden er en logg (treff i `tall_kilder_ut.txt` fra #2276 er utelatt, den er ikke en logg). Hvert tall er regnet på nytt av meg fra fasitfila (`20261105_114241_real_votes.csv`, test = year 2026) og den frosne svarfila, og den frosne agenten er kjørt på nytt til `/tmp/c1_dommer_2278` (`pred_maaler.csv` og maskin-alene-fila byte-like med de frosne). Egen telling: `arbeid/oppgave_2278/telling.txt`.

**Resultat: 17 OK, 1 feil (rettet), 1 upresis (rettet), 1 ikke et måletall.** Loggtreffet tallsjekken pekte på var i 7 av 20 tilfeller en tilfeldig logg (f.eks. 99,4 % i `mine_ki_B10000.txt`), men tallet var likevel riktig mot den ekte kilden.

| # | fil:linje | tall | påstand i teksten | sjekket mot | dom |
|---|---|---|---|---|---|
| 1 | JURY.md:35 | 99,4 % | nye selskaper: 99,4 % rutes | `kilder/c1_robusthet_frossen.md`: ukjent selskap 1568 av 1578 = 99,4 %, frossen modell | OK (loggtreffet var tilfeldig) |
| 2 | JURY.md:9 | 0,066 | «aksjonærforslag = MOT» F1 0,066 på test 2026 | `oppgave_2234/baseline_real_test.txt`, måler v3, real test: TP 2 FP 1 FN 56 → 0,0656 | OK |
| 3 | JURY.md:34 | 127 | 127 usikre til menneske | egen kjøring av frossen agent: usikker 127, ukjent selskap 60, instruks 1 = 188 | OK |
| 4 | JURY.md:31 | 18 | 18 aksjonærforslag av 1578 | fasitfila: 18 (16 med fasit) | OK |
| 5 | BESLUTNINGSSTOTTE.md:41 | 6 | «de 6 øvrige aksjonærforslagene fikk ingen MOT» | fasit: 16 aksjonærforslag med fasit, 2 MOT, 14 uten MOT (8 styrekandidater + 6 andre) | **upresis**, rettet til «de 14 andre (8 styrekandidater og 6 andre saker)» |
| 6 | BESLUTNINGSSTOTTE.md:45 | 729 | styrevalg (styret) 729 saker | fasit: 729, 26 MOT, agenten fant 14 | OK |
| 7 | JURY.md:35 | 6 | «BEGRENSNINGER.md pkt. 6» | henvisning, ikke måletall | ikke måletall |
| 8 | JURYSVAR.md:37 | 122 | bare båndet: 122 av 1539 (7,9 %), 27 av 58 MOT | egen kjøring: 122, 27; utenfor båndet 10 MOT-flagg, alle ekte → TP 37 FP 0 FN 21 F1 0,779; menneske sier FOR F1 0,294 | OK (også 0,779 og 0,294 på samme rad) |
| 9 | BESLUTNINGSSTOTTE.md:41 | 6 | «annen sak» 6 av 6 fikk MOT | fasit: OTHER_BUSINESS 6 av 6 MOT, agenten fant 6 | OK |
| 10 | BESLUTNINGSSTOTTE.md:47 | 130 | revisor 130 saker | fasit: 130, 7 MOT (5,4 %), fant 3 | OK |
| 11 | BESLUTNINGSSTOTTE.md:7 | 56 | 56 av 58 MOT er styrets forslag, 29 av 30 treff | fasit + frossen svarfil: 56/58, 29/30 | OK |
| 12 | BESLUTNINGSSTOTTE.md:46 | 1,9 % | øvrige (styret) 11 av 571 | fasit: 11/571 = 1,9 % (ARTICLES 3, SAY_ON_PAY 3, SHARE_ISSUANCE 2, RPT 1, EQUITY_PLAN 1, FIN_STATEMENTS 1), fant 5 | OK |
| 13 | JURY.md:9 | 0,645 | regelen så sterk ut på N-PX-data (F1 0,645), fasiten var feillest | `kilder/case1_hvilken_fasit.md`: 0,645 på N-PX 2026 med feil `against_board`; teksten sier nettopp det | OK (loggtreffet i oppgave_2283 var tilfeldig) |
| 14 | BESLUTNINGSSTOTTE.md:41 | 56 | 56 av 58 MOT er styrets forslag | fasit: Management 56, Shareholder 2 | OK |
| 15 | JURYSVAR.md:26 | 18 | 18 ulike GVG-avsnitt, alle 18 ordrett på nbim.no (#2130) | frossen agent siterer **15** ulike avsnitt (1504 × 0.0.3 + 74). #2130 talte 18 på kjøringen 12:47; `retningslinje_oppslag.py` ble endret 12:53, og 6 av de 15 var ikke med blant de 18. Alle 15 tekster finnes i `punkter.jsonl`, der #2130 sjekket alle 140 GVG-punkter ordrett | **feil**, rettet i JURYSVAR.md:26 og METODE.md:29 (18 → 15 med forklaring) |
| 16 | JURY.md:15 | 16 | Title Case-instruks bytter 16 stemmer urutet | `c1_titlecase_vakt.md`: gammel (frossen) vakt, urutet endret 16, F1 0,392 | OK |
| 17 | BESLUTNINGSSTOTTE.md:33 | 12,5 | forvalteren leser 12,5 av 100: 11,9 i sonen + 0,6 MOT-flagg utenfor (9, alle ekte) | egen kjøring: 183/1539 = 11,9 %, 9 MOT-flagg utenfor sonen, alle ekte, 9/1539 = 0,6 % → 12,5 | OK |
| 18 | BESLUTNINGSSTOTTE.md:41 | 6 | 1 av 6 «andre styresaker» | fasit: OTHER_MGMT 6 MOT av 87, fant 1 | OK |
| 19 | JURYSVAR.md:3 | 6 | «svar 6: #2130» | henvisning, ikke måletall | ikke måletall |
| 20 | BESLUTNINGSSTOTTE.md:45 | 3,6 % | styrevalg (styret) 26 av 729 | 26/729 = 3,6 % | OK |

## Bifunn utenfor de 20
- `mot_styret`-kolonnen i `agent.csv` er 1 for 3 rader der styret selv anbefalte MOT og agenten sier FOR (`2045311|16`, `2066391|14`, `2086078|6`). Det er avvik fra styret, ikke MOT. Loggens «MOT styret 74» er altså 71 MOT-flagg + 3. Måleren bruker `pred_maaler.csv` og teller riktig (TP 30 FP 38 FN 28), så hovedtallet er urørt. Tekstene som regner på «utenfor sonen» stemmer bare når disse 3 holdes utenfor, og det gjør de. Lagt som oppgave til smed2 (bare etikett i utfila, ikke prediksjon).
- Kjøringen i `arbeid/hack/levering/c1_v1/ut/agent.csv` (12:47, 10 %-logitbånd, 228 til menneske) er ikke den frosne agenten. Den bør ikke brukes som kilde for tall i pakka.

## Kontroll etter rettingene
`c1_tallvakt.py`: 16 filer, 163 påstander, 0 avvik. `c1_tallsjekk.py --feil`: IKKE FUNNET 0 (de nye tallene 15, 71, 14, 8 og 140 har kilde).
