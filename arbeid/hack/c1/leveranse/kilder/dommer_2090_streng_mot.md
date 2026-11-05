# Dommer sak 2090: F1 på bare MOT for den frosne modellen – PASS

**Dom: PASS.** Tallet kan gå i juryteksten.

## Hva jeg gjorde
- Smedens sak 2087 var ikke lukket (c1_streng_mot.md fantes ikke ennå), men koden og svarfilene lå på disk. Jeg verifiserte dem direkte.
- Kald kopi i /tmp/kald2090 (bare streng_mot.py, oppgave_2044/train.py, maaler_offisiell_v3.py og real_votes.csv):
  `cd /tmp/kald2090 && <repo>/.venv/bin/python <arbeidsmappe>/oppgave_2087/streng_mot.py` (4 s).
  svar_val.csv og svar_test.csv ble byte-identiske med smedens.
- Uavhengig telling i pandas (egen kode, ikke måleren) ga nøyaktig samme TP/FP/FN på val og test.
- Fem håndplukkede test-saker, hver snudd én om gangen gjennom måler v3:

| sak | styret | NBIM | svar | forventet ved flipp | målt |
|---|---|---|---|---|---|
| 2033470\|1 Kura Sushi | FOR | MOT | 1 (TP) | TP−1, FN+1 | ✓ |
| 2038357\|7 Lundbeck | FOR | FOR | 1 (FP) | FP−1 | ✓ |
| 2048411\|10 LOTTE | FOR | MOT | 0 (FN) | TP+1, FN−1 | ✓ |
| 2039527\|16 (AVSTÅ) | FOR | AVSTÅ | 0 (TN) | FP+1 (AVSTÅ er ikke MOT) | ✓ |
| 2045311\|16 aksj.forslag | MOT | FOR | 1 (avvik = FOR) | ingen endring | ✓ |

- Dataene er konsistente: against_board=1 betyr alltid NBIM ≠ styret, og rader uten mgmt_rec har tom against_board og telles ikke.

## Tall (frossen modell miks h2, grense 0,9188 valgt på val)
| vindu | MOT mot styret (TP/FP/FN) | F1 MOT | F1 avvik |
|---|---|---|---|
| val 2025 | 45 / 29 / 54 (99 i fasit) | 0,520 | 0,522 | <!-- val 2025, ikke hovedtall; tallvakt: ignorer -->
| **test 2026** | **30 / 38 / 28 (58 i fasit)** | **0,476** (P 0,44, R 0,52) | 0,482 |

Målt forsøk sak 1105 (0,47619) på måler f4d9398b4b for sak 2090 (`maaler_offisiell_v3.py {sti} test --data real --score mot`).
(sak 1104 er samme tall, først registrert som egen rapport ved en feil.)

## Hovedtall i JURY.md
**F1 på MOT mot styret er hovedtallet: 0,476 på test 2026** (hovedmålet). Avvik-F1 0,482 er sekundærtall. <!-- eldre: frossen #2044 (0,476), dagens hovedtall er repo4 0,512 -->
JURY.md sier fortsatt «Hovedtall er F1 og PR-AUC på avvik fra styret» (linje 8) og har gamle Vanguard/v3-tall. Det må rettes i sak 1975 (speider).
Merk: 5 AVSTÅ i test er avvik, men ikke MOT. Derfor er MOT-tallet litt lavere enn avvik-tallet. Ikke kall 0,482 «MOT».
