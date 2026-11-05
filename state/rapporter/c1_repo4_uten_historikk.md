# Case 1 (#2645): repo4 uten samme-sesong-historikk gir F1 MOT 0,396 (ikke 0,415)

arkitekt, 05.11 ca. 17:35. Til smed2 (#2639). Frosne filer og leveransen er ikke rørt; alt ligger i `arbeid/oppgave_2645/`.

## Svaret
Uten etiketter fra samme sesong faller repo4 fra **0,512 til 0,396** på test 2026 (−0,116, 95 % KI [−0,196; −0,027], 99 % av trekkene under).
Frossen falt 0,061 (0,476 → 0,415). Hele forspranget repo4 har over frossen kommer altså fra samme-sesong-historikk.
Uten den er repo4 i praksis lik frossen uten historikk (0,396 mot 0,415, −0,019 [−0,055; +0,005], bare 4 ulike prediksjoner).
Teksten «0,512 → 0,415» er feil. Riktig er 0,512 → 0,396.

| kjøring (test 2026, 58 MOT i fasit) | egne hist-trekk | repo-trekk | val-valg | F1 MOT | TP/FP/FN | P / R |
|---|---|---|---|---|---|---|
| kontroll = pakkens repo4 (byte-lik `oppgave_2612/kjor/pakke_repo4_test.csv`) | løpende | løpende | C=3, g 0,9232 | **0,5120** | 32/35/26 | 0,478 / 0,552 |
| **repo4 uten samme sesong** | år før | år før | C=0,1, g 0,9394 | **0,3962** | **21/27/37** | 0,438 / 0,362 |
| bare egne trekk kuttet | år før | løpende | C=0,1 | 0,3962 | 21/27/37 | 0,438 / 0,362 |
| bare repotrekk kuttet | løpende | år før | C=3 | 0,5079 | 32/36/26 | 0,471 / 0,552 |
| (frossen #2044 `--hist 1`, #2134) | år før | – | C=0,3 | 0,4151 | – | 0,458 / 0,379 |

Lesning: det er de egne løpende trekkene (`--hist 2`: MOT tidligere i selskapet/teksten samme år) som bærer. De fire repotrekkene betyr lite når samme sesong kuttes (0,512 → 0,508).
Samme grenseregel som pakken: C og grense valgt på val 2025 (trent <2025), test 2026 kjørt én gang med den grensen.

## Hvordan kuttet er gjort
- `modell_uten.py` = kopi av `arbeid/hack/c1/bytte/modell_repo4.py` + flagget `--repohist`. `--repohist 1` kjører repoets `ballot.add_history` med `labelled` satt til usann for møter i år ≥ året som predikeres (val: <2025, test: <2026). Ingen andre endringer. `stemmeagent/` er kopiert uendret.
- Egne trekk: pakkens eget `--hist 1` (bare år før), samme som 0,415-målingen.
- Kontroll: `--hist 2 --repohist 2` gir byte-lik `_test.csv` som pakken (cmp), så kopien er riktig.

## Gjenskap (12 s)
```
bash arbeid/oppgave_2645/kjor.sh && cat arbeid/oppgave_2645/maal.txt
python3 -I arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2645/kontroll_h2r2_test.csv arbeid/oppgave_2645/uten_h1r1_test.csv test
```
Python: `arbeid/kandidater/smed2_c1_mot/.venv`. Måler: `arbeid/hack/c1/maaler_offisiell_v3.py --score mot`. Data: `arbeid/hack/CASE/20261105_114241_real_votes.csv`.

## Ferdig setning til ERLIG § 2 / K:10 (BYTT)
«Modellen bruker NBIMs tidligere stemmer, også fra tidligere møter samme sesong. Uten samme-sesong-stemmer (bare år før) faller F1 MOT på 2026 fra 0,512 til 0,396 (−0,12, 95 % KI −0,20 til −0,03), litt under den gamle modellen uten slike stemmer (0,415). Hele forbedringen fra den nye modellen hviler altså på at NBIM publiserer stemmene løpende, slik de gjør i dag; uten det er 0,396 nedre grense.»

## Forbehold
- Bare testår 2026 er målt uten historikk (tidsboks 30 min); 2024/2025 ikke.
- Repoets `base_rate` (prior i `hist_type_dev_rate`) er uendret, regnet på train 2019–2023; det rører ikke 2026.
