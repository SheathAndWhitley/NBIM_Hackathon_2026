# Dom: smed2s parede India-test (c1_india_paret.md) er GODKJENT (#2315, dommer2)

**Dom: GODKJENT.** Tallene i rapporten er reprodusert identisk, og test 2026 er ikke brukt.

## Hva jeg gjorde
- Kjørte `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2311/paret.py` på nytt. Utdata er linje for linje lik `arbeid/oppgave_2311/ut.txt` (seed 0, 10 000 trekk): 2024 Δ +0,0081, KI [0; +0,028], perm p 1,000, 1 snudd rad; 2025 Δ +0,0416, KI [+0,009; +0,082], perm p 0,063/0,066, 5 snudde rader, alle riktige.
- Målte de fire val-filene med v3-måleren (`maal_aar.py`, importerer `maaler_offisiell_v3.py` uendret, `--score mot`): 2024 PÅ 0,544444 / AV 0,536313, 2025 PÅ 0,561798 / AV 0,520231. Lik rapporten.
- Sjekket at test 2026 ikke er brukt: `paret.py` leser bare `val_*_2024/2025.csv`. `kjor.sh` kjører `train.py` med `--kun-val 1`, som avslutter før test-delen (linje 133). `maal_aar.py` nekter år 2026 med assert.
- Sjekket vinduet: `train.py` trener på år < valår og validerer på år == valår (linje 111), så 2024-tallet er ekte holdt-ut (trent på <2024). India-regelen (linje 41) er bare land + tekstmønster, ingen etiketter.

## Merknad
- F1-tallene i loggene (0,5672 / 0,5743 for 2024) er vanlig F1 på MOT fra train.py, ikke v3 sitt F1 på MOT-mot-styret. Rapporten bruker riktig v3-tallene. Ingen feil, men ikke bland dem.
- Konklusjonen i rapporten (gevinsten er ikke vist å være mer enn tilfeldighet, holdt-ut-beviset er én sak) er dekket av tallene. Dommerens avgjørelse i #2297 (regelen bygges ikke inn, frossen #2044 står) bygger på denne testen og står seg.
