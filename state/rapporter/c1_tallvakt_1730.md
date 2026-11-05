# Case 1: tallvakt på BYTT og STÅR etter siste tekstendring (#2630, smed2, 05.11 kl. 17:17)

Etter commit 3ceaac0 (#2625, ærlighetsforbeholdet inn i STÅR). Ingen filer endret: det var ingen tallfeil å rette.

| Utgave | Kjøring | Måler (v3 --score mot) | Resultat |
|---|---|---|---|
| BYTT (repo4), leveranse/ + levering/ i landsbymappa | `python3 -I arbeid/verktoy/c1_tallvakt.py` | F1 0,5120, P 0,4776, R 0,5517, TP 32 FP 35 FN 26; menneske 164/1578 (10,4 %) | 22 filer, 175 påstander, **0 avvik**, OK |
| STÅR (frossen), zip 2587 + de fire filene i reserve_staar/ kopiert inn i leveranse/ (samme rekkefølge som LES.md) i /tmp/c1_2630/c1_stemmeagent | `python3 -I arbeid/verktoy/c1_tallvakt.py --rot /tmp/c1_2630/c1_stemmeagent` | F1 0,4762, P 0,4412, R 0,5172, TP 30 FP 38 FN 28; menneske 188/1578 (11,9 %) | 17 filer, 155 påstander, **0 avvik**, OK |

I tillegg gir `lag_staar.py --sjekk` LIK for README.md og kravrespons.md, altså stemmer STÅR-reserven fortsatt med dagens BYTT-tekst.

Logger: `arbeid/oppgave_2630/bytt.txt`, `arbeid/oppgave_2630/staar.txt`.
Forbehold: STÅR-kjøringen er gjort på zipens egne svarfiler (frossen kjøring fra zip 2587), ikke på en ny kjøring av agenten. Den ekte kalde tørrkjøringen gjør smed3 (#2622).
