# Case 1: sjekk av tabellen «send til menneske» fra kald kopi (#2153, dommer)

**Dom: GRØNN. Ingen avvik.**

## Kjøring
- `BEHOLD=1 bash arbeid/hack/c1/kaldstart.sh` (git e74453d, 13:01): tom tmp-mappe `/tmp/c1_kald.k58u9e`, uv sync --frozen, agenten fra kopien. GRØNN F1_MOT 0.476190 REF 0.476190, 40 s. Måler v3 sha256[:10] 8b09c36e01.
- `python3 -I arbeid/hack/c1/menneske_tabell.py /tmp/c1_kald.k58u9e/ut/agent.csv`: tabellen er tegn for tegn lik standardkjøringen (`arbeid/oppgave_2132/agent.csv`).

## Akseptkrav
| krav | kald kopi | uavrundet | ok |
|---|---|---|---|
| saker til menneske | 183 av 1539 (11,9 %) | 11,89 % | ja |
| MOT i sonen | 32 av 58 | | ja |
| maskin alene F1 | 0,476 (TP 30 FP 38 FN 28) | 60/126 = 0,4762 | ja |
| øvre grense F1 | 0,828 (TP 41 FP 0 FN 17) | 82/99 = 0,8283 | ja |
| gulv F1 | 0,269 (TP 9 FP 0 FN 49) | 18/67 = 0,2687 | ja |

Alle innen 0,001. Inn 1578 saker, 188 (11,9 %) til menneske, likt med agentloggen.

## Dokumentene (grep i arbeid/hack/levering/)
README.md:47, BESLUTNINGSSTOTTE.md:24 og JURYSVAR.md:39 har den samme standardraden ordrett (183 av 1539, 32 av 58, 0,476 / 0,828 / 0,269). Tekst i JURYSVAR.md:31 (11,9 %, 32 av 58, alle 38 falske flagg i sonen, 0,828) og BESLUTNINGSSTOTTE.md:31 (12,5 av 100 = (183+9)/1539; 9 flagg utenfor sonen, alle ekte MOT = gulvets TP 9 FP 0) stemmer med tallene.

## Merknad (ikke avvik)
agent.csv fra kald kopi og #2132 skiller seg i 50 rader, men bare i sitatkolonnene (retningslinje_id/sitat/grunnlag; trolig sitatendringen #2106 etter #2132). Anbefaling, P(MOT), til_menneske og rutingsgrunn er like i alle 1578 rader. Liten ting: BESLUTNINGSSTOTTE.md:34 sier «rundt 62» timer; regnestykket gir 62,5.
