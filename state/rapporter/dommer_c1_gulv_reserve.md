# Dommer #1976: historikkgulvet lekker ikke, og er nå reserveleveranse

**Regel:** MOT på say-on-pay hvis NBIM har stemt MOT på samme selskap (cusip) i train. p_avvik = glattet MOT-andel.

## Lekkasjesjekk (`arbeid/hack/c1/reserve/lekkasjesjekk.py`, grønn på begge splitter)
| sjekk | test (data_v3) | val (data_v3_val) |
|---|---|---|
| bare NORGES BANK i train+test | ja | ja |
| siste train-møte < første test-møte | 2025-06-30 < 2025-07-01 | 2024-06-28 < 2024-07-02 |
| felles id/forslag train–test | 0 av 3137/1246 | 0 av 1631/1506 |
| fasitkolonner i test_input | 0 | 0 |
| uavhengig reimplementering med datofilter per rad: avvik fra pred | 0 av 1246 (2211 oppslag, likt med og uten filter) | 0 av 1506 |
| negativ kontroll (regel med lekket test-fasit) | 129/129 treff mot gulvets 55 → sjekken ser lekkasje | 136/136 mot 46 |

Ingen samme-dag-rader og ingen test-rader brukes. Merk: regelen bruker ikke NBIMs egne stemmer fra tidligere i testperioden (konservativt; en løpende variant kan gi mer, ikke målt her).

## Reserveleveranse
`bash arbeid/hack/c1/reserve/run.sh [DATAMAPPE] [UT.csv]` → `reserve/pred.csv`. Bare python3 stdlib.
Kald start: kopiert til /tmp/kald1976.mJqF, kjørt med `env -i PATH=/usr/bin:/bin` fra `/`: 1246 rader, byte-identisk med #984.

## Tall (måler v3, sha nå cb9243ddee, samme kommando som 823c9610fe, samme tall)
- Test: **F1 0,383** (P 0,348, R 0,426, tp 55 fp 103 fn 74), PR-AUC 0,328. Forsøk #1000.
- Val: F1 0,361.
- Rutet til menneske: bare 0,7 % (konfidens < 0,6) → gulvet ruter nesten ingenting; ruting må komme fra modellen.
