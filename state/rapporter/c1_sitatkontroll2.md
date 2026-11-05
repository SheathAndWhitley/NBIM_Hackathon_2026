# Case 1 sitatkontroll 2 (#2143, dommer2): 10 av 10 sitater er ordrette og har riktig NBIM-nummer

Kilde: NBIMs egen nettside, rå nedlasting `arbeid/speider/c1ret_raa/nbim_gvg.html` (og PDF-teksten `nbim_gvg2024.txt`).
Nummeret er utledet **direkte fra HTML-en** (h3 = prinsipp, h4 = delpunkt, avsnitt i rekkefølge = ledd), ikke fra `punkter.jsonl`.
Skript: `python3 -I arbeid/oppgave_2143/sjekk.py arbeid/oppgave_2106/test2026_mot.csv <id,...>` og `python3 -I arbeid/oppgave_2143/tilfeldig.py <agent.csv> <utelatte id>`.

## Smed2s rettede sitater (#2120), fra `arbeid/oppgave_2106/test2026_mot.csv`
Rapporten listet 6 rader (oppgaven sa 5); alle 6 er sjekket.
| sak | sitert | HTML-nummer | ordrett web/PDF | i NBIMs egen begrunnelse |
|---|---|---|---|---|
| 2082048\|5 supermajority | 6.2.5 | 6.2.5 (Mergers…, ledd 5, anti-takeover) | ja/ja | ja |
| 2089598\|12 pre-emptive | 6.1.2 | 6.1.2 | ja/ja | ja (NBIMs første avsnitt er 6.1.3, så riktig, men ikke det første) |
| 2084790\|5, 2087754\|5, 2084301\|47 | 3.1.1 | 3.1.1 | ja/ja | ja |
| 2048411\|10 Office Term | 4.3.1 | 4.3.1 (4. Shareholder approval / 3. Governing documents) | ja/ja | ja |

## 5 tilfeldige fra demoen (seed 2143, blant 71 predikerte MOT med NBIM-sitat, de 6 over utelatt)
Ny kjøring av demoens agent i kald kopi `/tmp/c1_demo_2143` (fremmed.sh, 12:56).
| sak | sitert | HTML-nummer | ordrett |
|---|---|---|---|
| 2052819\|7 UMB Financial, direktørvalg | 1.3.1 | 1.3.1 | ja |
| 2081841\|3 D'Ieteren, lønnsrapport | 3.3.1 | 3.3.1 | ja |
| 2097662\|3 Colruyt, lønnspolitikk | 3.3.1 | 3.3.1 | ja |
| 2097662\|16 Colruyt, direktørvalg | 1.1.1 | 1.1.1 | ja |
| 2054683\|6 First Horizon, direktørvalg | 1.3.1 | 1.3.1 | ja |

**Resultat: 10 av 10 riktige** (11 av 11 med den sjette #2120-raden). Ingen feil i tekst eller nummer.

## Merknader (ikke sitatfeil, men viktig)
1. **`c1/leveranse/demo_utskrift.txt` (12:53) er utdatert:** den viser fortsatt gammel logikk, f.eks. 2084790|5 → «NBIM 3.1.8 We will support a proposal to introduce majority requirements…» (en aksjonærforslagsregel, feil for et styreforslag). Ny kjøring gir 3.1.1. Demoutskriften må lages på nytt (`sh arbeid/hack/c1/leveranse/demo.sh`) før frys. Jeg skrev ikke over fila.
2. Sitatene er prinsipp-avsnitt (første i seksjonen), ikke regelen som slo til. Det er ærlig i #2120, men sitatene blir generiske: 3.3.1 og 1.1.1 brukes for mange saker. «Regler i seksjonen et menneske bør sjekke» i grunnlaget dekker dette.
3. Under min kjøring endte `fremmed.sh` med `syntax error near unexpected token ')'` på linje 39 etter at agenten hadde skrevet agent.csv, så HOVEDTALL-linja manglet. Fila ble endret 12:56 mens den kjørte; `bash -n` er grønn nå. Sannsynligvis redigering midt i kjøringen, men eieren av #2127 bør kjøre den én gang til.
4. Predikerte FOR-saker får NBIM 0.0.3 («Our starting point … is to support the board»). Teksten står ordrett på nettsiden; 0.0.x er speiderens nummer for innledningen, som NBIM selv ikke nummererer.
