# Case 1: verifisering av rutingskostnaden (#2100), dommer #2108: GODKJENT

Kald kopi: `kost.py` kopiert til `/tmp/kald_2108/` med utdata dit, kjørt med `uv run --project arbeid/oppgave_2023`. Kjøretid ca. 3 s.

**(1) 10 %-raden på test 2026: GODKJENT, nøyaktig.** 170 rutet (11,0 %), F1 rest 0,627 (P 0,765 / R 0,531), 17 av 66 MOT hos menneske, nytt lag 0,070, System F1 (øvre) 0,735. `val.csv` og `test.csv` fra kald kjøring er byte-like med smed2s filer. Grense T = 0,9188, bredder 0 / 0,609 / 0,946 / 1,309 / 1,570 som rapportert.

**(2) Låst på val 2025: GODKJENT.** I koden avhenger T og breddene `B` bare av `v` (val_med_grupper.csv: 1909 saker, alle år 2025, ingen rad-overlapp med test). Testsakene brukes bare i `tabell()`, med T og B uendret. Stoppregelen gir 10 % på val: 0,260 og 0,168 er over 2 × 0,054 = 0,108, mens 0,042 er under. Tidspunktet «satt før test ble sett» kan ikke bevises, fordi samme kjøring skriver begge tabellene. Men på test ville regelen ha fortsatt til 15 % (0,101 er over 2 × 0,043 = 0,086), og smed2 valgte likevel 10 %. Det taler mot at test ble brukt til valget.

**(3) «System F1 (øvre)» merket som øvre grense: GODKJENT.** #2100-tallet 0,735 er ikke sitert i leveransen ennå: README og JURYSVAR (levering/) peker bare til `c1_ruting_kostnad.md`. Systemtallene som faktisk står der, er merket som øvre grense: levering/README.md l. 50, METODE.md l. 53 og 55, c1/JURYSVAR.md l. 42, c1/leveranse/BEGRENSNINGER.md pkt. 6. 1-sideren (c1/leveranse/kravrespons.md) har ikke noe system-F1.
- Liten merknad: fotnoten i BEGRENSNINGER.md l. 31 sier «system-F1 0,65» uten «øvre». Pkt. 6 i samme fil sier det rett, så dette er ikke et avvik. Speider (#2104/#1975) kan legge til «(øvre)».
- Når 0,735 eller 0,627 tas inn i leveransen, skal de stå som «øvre grense» og «F1 på resten, ikke systemets F1».

**Utenfor kravene:** pred_miks_h2.csv gir maskin-F1 0,4818, mens det offisielle tallet er 0,476 (#2090). Avviket er kjent og sagt i smed2s rapport. Det hører hjemme hos #2107 og påvirker ikke denne tabellen.
