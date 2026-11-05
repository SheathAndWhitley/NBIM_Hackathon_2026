# Case 1: pakkesjekk av levering/ og fremmed.sh (#2119, dommer2, 12:44)

Sjekket arbeid/hack/levering/ etter #2117 (speider, rydding) og #2116 (fremmed.sh-fiks, fortsatt open).

| Krav | Status |
|---|---|
| Ingen .venv (demo/.venv var 322 MB kl. 12:41) | OK, borte |
| Ingen __pycache__ (rot og demo/) | OK, borte |
| Ingen L3-L5 / L*_kald-mapper | OK, borte |
| Ingen ~-stier | OK, eneste treff er sed-linja i fremmed.sh (skal stå, den bytter stien i kopien) |
| Størrelse | OK, 3,4 MB (var 327 MB) |
| fremmed.sh kopierer arbeid/hack/levering/retningslinje_oppslag.py | **FEIL**, mangler |
| fremmed.sh kopierer arbeid/hack/c1/retningslinjer/punkter.jsonl | **FEIL**, mangler |

Konsekvens: c1_real.py linje 162 importerer retningslinje_oppslag ubetinget, og den leser
`HER/../c1/retningslinjer/punkter.jsonl`. Kald kopi krasjer med ImportError til #2116 er gjort.

Rest: #2116 (smed2) må legge til de to stiene i `kopier`-lista. Kjør så denne sjekken på nytt:
`grep -c "retningslinje_oppslag.py\|retningslinjer/punkter.jsonl" arbeid/hack/levering/fremmed.sh` (skal gi 2),
og en kald kjøring (#1952 kl. 13).

## Tillegg #2123 (dommer2, 12:58): fremmed.sh-fiksen holder fra kald kopi

| Krav | Status |
|---|---|
| fremmed.sh kopierer retningslinje_oppslag.py og retningslinjer/punkter.jsonl | OK. NB: `grep -c` gir 1 fordi begge står på samme linje; `grep -o ... \| wc -l` gir 2 |
| Kald kopi `sh arbeid/hack/levering/fremmed.sh /tmp/fremmed_2123` (env -i, uv sync --frozen) | OK, 162 MB, 35 s, ingen ImportError/Traceback |
| demo.sh (`arbeid/hack/c1/leveranse/demo.sh /tmp/c1_demo_2123`) | OK, tre saker vist, ingen feil i loggen |
| Hovedtall v3 `--score mot` på kopiens ut/agent.csv | **0,476190**, TP 30 FP 38 FN 28 (58 i fasit), identisk med README |
| Sidetall v2 avvik | 0,4818 (TP 33 FP 38 FN 33), som README |
| Forsøk på tavla | #1120, 0,47619 (maaler). Egen måler for #2123 satt: `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py {sti} test --data real --score mot` (sha de049083d9; satt av dommer2 med `--av dommer` fordi tavla bare godtar rollenavnet). Svarfil: arbeid/oppgave_2123/agent_kald.csv |

Dom: #2116 holder. Pakka kjører fra kald kopi og gir hovedtallet.
Merk: rundens globale måler er endret på disk (8733327407 -> 474eae7bc8), så forsøk uten egen oppgavemåler avvises til en dommer setter den på nytt.
