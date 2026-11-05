# Case 1: hva betyr F1 0,476 på MOT i praksis (#2164, dommer, kontrollert)

Alle tall er regnet med ett kall, ikke kopiert:

```
.venv/bin/python arbeid/hack/levering/kjor_agent.py --ut arbeid/oppgave_2164/agent_ut   # standardkjøring, gir agent.csv med til_menneske
python3 -I arbeid/oppgave_2164/i_praksis.py   # svar_test.csv (#2087) + agent.csv + real_votes 2026
```

Kontroll: måler v3 på `arbeid/oppgave_2087/svar_test.csv` (`--score mot`) gir samme linje:
`MOT mot styret: TP 30 FP 38 FN 28  P 0.4412  R 0.5172  F1 0.4762  (58 i fasit)`, 1539 vurderte rader.
Leveransefila `kjor_agent_real_maskin_alene.csv` gir identisk linje. Agentens KJORING.txt (13:04 og min kjøring):
188 av 1578 inn til menneske (11,9 %); av de 1539 med fasit 183 (11,9 %).

## Tabellen for forvalteren (test 2026, 1539 saker med fasit, 58 ekte MOT mot styret)

| | Saker | Hva det betyr |
|---|---|---|
| Agenten flagger MOT | 68 | 4,4 av 100 saker |
| – riktige flagg | 30 | P 0,44: under halvparten av flaggene er ekte MOT |
| – falske flagg | 38 | alle 38 ligger i menneske-sonen, så et menneske ser dem |
| Ekte MOT funnet av maskinen | 30 av 58 | R 0,52 |
| Ekte MOT maskinen glemmer | 28 | |
| Menneske-sonen | 183 (11,9 %) | 32 av de 58 ekte MOT ligger her |
| Flagg utenfor sonen | 9 | alle 9 er ekte MOT |
| MOT funnet hvis mennesket avgjør sonen riktig | 41 av 58 (71 %) | øvre grense, antar riktig menneske |
| MOT ingen ser (lav P(MOT), utenfor sonen, ikke flagget) | 17 av 58 | 1,1 per 100 saker |

Av de 28 glemte ligger 11 i sonen (mennesket kan finne dem) og 17 utenfor.
Forvalteren leser 183 + 9 = 192 saker, 12,5 av 100.

## Sjekk mot pakka
- **BESLUTNINGSSTOTTE.md** har avsnittet «Hva det betyr i hverdagen» med samme tall (12,5 av 100, 183, 9, 41 av 58, 17 av 58). Stemmer. Mangler bare selve maskinlinja i klartekst (68 flagg, 30 riktige, 38 falske, 28 glemt).
- **README.md** har tabellen (TP 30 FP 38 FN 28, 183 av 1539, 32 av 58, TP 41 FN 17), men **ikke** et «i praksis»-avsnitt i klartekst.

## Forslag (smed2 limer inn i README under tabellen, og første punkt øverst i BESLUTNINGSSTOTTE-avsnittet)

> **I praksis (test 2026, 1539 saker, 58 MOT mot styret):** agenten flagger 68 saker som MOT. 30 av dem er riktige (P 0,44), 38 er falske, og alle de 38 havner i menneske-sonen. Den finner 30 av de 58 ekte MOT (R 0,52) og glemmer 28. Menneske-sonen er 183 saker (11,9 %) og rommer 32 av de 58 MOT. Avgjør forvalteren sonen riktig, blir inntil 41 av 58 funnet (71 %, øvre grense). 17 av 58 MOT ser ingen: de får lav P(MOT) og havner verken i sonen eller blant flaggene. Forvalteren leser 192 saker, 12,5 av 100.

## Tallvakta
`python3 -I arbeid/verktoy/c1_tallvakt.py --vis state/rapporter/c1_i_praksis.md`: 13 påstander om hovedtallet stemmer, 0 avviker, OK.
