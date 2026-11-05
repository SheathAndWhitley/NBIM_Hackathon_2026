# Case 1: alle tre former målt fra kald start på NBIM-måleren v3 (dommer, #1969): smed2 lgbm leder med F1 0,325, men ligger under gulvet på 0,383

Måler: `python3 -I arbeid/hack/c1/maaler.py {sti} --fasit arbeid/hack/c1/data_v3/fasit.csv`, **sha 823c9610fe** (samme som #1966). Test er 2026 (1246 forslag, 129 MOT, alle say-on-pay).

| forsøk | kandidat | P (MOT) | R (MOT) | F1 (SCORE) | PR-AUC | acc |
|---|---|---|---|---|---|---|
| #987 | **smed2 #1949 lgbm** | 0,269 | 0,411 | **0,325** | 0,262 | 0,823 |
| #988 | smed3 #1950 sitatagent v5 | 0 | 0 | 0,000 | 0,1035 | 0,897 |
| #989 | grunnlinja: følg utledet styre (FOR) | 0 | 0 | 0,000 | 0,1035 (basisrate) | 0,897 |
| (#984) | referanse: dommer-gulvet, MOT hvis NBIM stemte MOT på selskapet tidligere | 0,348 | 0,426 | 0,383 | 0,328 | 0,858 |

**Leder blant smedformene: smed2 lgbm (#987).** Ingen av formene slår gulvet på 0,383. Den beste leveransen på v3 i dag er derfor historikkregelen. smed2 kan eventuelt brukes oppå den.

## Kald start, slik den ble gjort
- Det ble laget ferske mapper med bare koden (`train.py`, `pyproject.toml`, `uv.lock`, eller smed3s `*.py` og `rl/`) og `train.csv` og `test_input.csv`. **Fasiten ble ikke kopiert.** smed2 fikk nytt `.venv` med `uv run --project .`.
  - `arbeid/kandidater/dommer_1969_smed2`: `uv run --project . python train.py --data d --ut pred.csv` (26 s). Smedens innebygde måling feiler fordi fasiten mangler, men pred.csv er allerede skrevet.
  - `arbeid/hack/varianter/dommer_1969_smed3`: `python3 -I rl_punkter.py && python3 -I agent.py d/train.csv d/test_input.csv pred.csv`.
  - Grunnlinja er laget direkte fra `styret` i test_input (alle er FOR): `arbeid/oppgave_1969/pred_folg_styret.csv`.
- Koden er identisk med kopiene fra #1966. Reproduksjonen ble sjekket med `arbeid/oppgave_1969/sml.py`. smed2: 1246 av 1246 rader er like, også p_avvik. smed3: alle anbefalingene er like.

## Avvik å merke seg (smed3)
6 rader fikk p_avvik 0,0784 ved kald start, mot 0,5 i #1966. Det kommer av at `fakta.py` leser et lokalt nett-hentet lager (`data/def14a`) som ikke følger med koden. F1 endres ikke, men PR-AUC faller fra 0,107 til 0,1035. **Før leveransen (#1952) må smed3 enten ta med `data/def14a` i pakken eller la run.sh bygge det.** Ellers gir kald start et annet svar enn smedens egen mappe.

## Dom
- smed2 #987: reprodusert og godkjent, 0,325, under gulvet. Lekkasjesjekken fra #1965 står (bare train.csv brukes, ingen forbudte kolonner).
- smed3 #988: reprodusert, 0 på test. Årsaken er kalibreringen som slår av `presedens_pay` (se #1966). Rettes i #1959.
- Grunnlinja #989: 0, som den skal være per definisjon.
