# Case 1: restfunnene fra robusthetstesten er rettet (smed #2071)

Bare ruting og grunner er endret i `arbeid/hack/levering/c1_real.py`. Modellen (train.py #2044), grensen og `mot_styret` er uendret.

## Hovedtallet, før og etter
| | F1 MOT test 2026 | TP/FP/FN | til menneske |
|---|---|---|---|
| før (#2063, 12:07) | **0,4818** | 33/38/33 | 176 (11,2 %) |
| etter (#2071) | **0,4818** | 33/38/33 | 228 (14,4 %) |

Kommando: `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut /tmp/k2071`

## Fikser
1. **Ukjent selskap går til menneske** med grunnen «ukjent selskap: ingen NBIM-stemmer for selskapet før møtedatoen».
   I test 2026 gjelder det 70 saker (4,4 %). 8 av dem er MOT (11 %, mot 4 % ellers), og modellen er ustabil uten
   selskapshistorikk (P(MOT) 0,22 → 0,52 i #2063). 18 av de 70 var allerede rutet, så det kom 52 nye saker til menneske.
2. **Kjent sak med endrede felt blir ikke lenger ignorert uten beskjed.** Agenten bruker fortsatt den lagrede raden (#2053),
   men ruter saken med «felt avviker fra lagret sak (proposal_text); modellen brukte lagret rad». Slo til på 0 ekte saker i 2026.
3. **Tom inn-fil** gir nå en tydelig advarsel i tillegg til tom agent.csv.

## Robusthetstesten fra kald start (etter fiksene)
`uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2063/robusthet.py` (69 s), tabell i `arbeid/oppgave_2063/tabell.md`.
16 testtyper, 56 saker, 0 krasj, og 0 saker uten grunn. Hver sak gir MOT/FOR med grunn eller går til menneske med grunn.
To tester er nye: «kjent sak uendret» (ingen avviksruting) og «kjent sak, endret tekst/styret» (alle tre rutet med avviksgrunn).

## Bevisst ikke endret
- vern.py (#2047) flagger «The Board recommends…» og «AI agent» som instruks. Det er falske alarmer, men saken går til menneske
  uansett. Å endre vern.py kunne flytte 2026-tallet, og det er for nær modellfrys.
- Rutingsandelen er nå 14,4 %. Grensen velges i #2057 (smed2), og der bør regelen for ukjent selskap tas med.
