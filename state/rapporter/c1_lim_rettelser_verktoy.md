# Case 1: innlimingsverktøy for jury-rettelsene (#2643)

**Bruk:** `uv run python arbeid/oppgave_2643/lim_rettelser.py <rettelser.md> --mal leveranse|reserve_staar [--torr]`. Rettelsesfila har blokker med `### FIL <sti relativ til mal-mappa>`, så `GAMMEL:` og `NY:`, hver fulgt av et kodegjerde (``` eller ~~~). Kjør alltid `--torr` først.

- Idempotent: står NY der allerede, hoppes paret over (dette virker også når NY inneholder GAMMEL).
- STOPP før noe skrives hvis GAMMEL står 0 eller 2+ ganger, hvis stien ligger utenfor mal-mappa, hvis fila er frosset (state/c1_frys.json) eller hvis formatet er feil. Det er alt eller ingenting: alle par sjekkes i minnet først.
- Hver fil skrives med tmp-fil og `os.replace`. STOPP hvis mtime eller innhold er endret siden lesingen (samme mønster som oppgave_2618/lim_inn.py).
- Testet på en kopi av reserve_staar i /tmp/t2643 med to oppdiktede par (ett med `###` og tom linje i NY, ett der NY inneholder GAMMEL): tørrkjøringen skrev ingenting, den ekte kjøringen byttet begge, og en ny kjøring hoppet over begge. STOPP slo inn ved GAMMEL 0 ganger, ved 2 ganger, ved `../`, ved en frossen fil (kjor_agent.py) og ved en fil endret underveis. Ekte filer er urørt, og frysvakta melder 21 filer uendret.
