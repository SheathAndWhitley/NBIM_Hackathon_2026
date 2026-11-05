# Case 1: lederen har nå flagget --lekkasjefri med grensen valgt på val (smed2 #1997)

Kommando fra kald start (ca. 5 s):
`cd arbeid/kandidater/smed2_c1_mot && uv run python train_v3.py --lekkasjefri --ut <fil>`

Flagget gir variant b fra dommer #1988: `PVP_DAGER=100` og ingen `s_float`, `g_sbc_vs_float` eller `s_lonn_vs_storr`. Grensen velges på val 2025 som standard. Først trenes modellen på `data_v3_val`, og den rå scoren på 2025 gir grensen med best F1. Grensen settes midt mellom den scoren og nabo-scoren under, med samme logikk som dommerens `velg.py`. Deretter trenes modellen på `data_v3`, og grensen brukes på test 2026. `--grense andel` gir tilbake den gamle regelen med 1,25 × basisrate.

| Kjøring | Rå grense | F1 | PR-AUC | Mot dommer #1993 |
|---|---|---|---|---|
| --lekkasjefri, test 2026 | 0,183297 | **0,4743** (P 0,376, R 0,643) | 0,4550 | byte-lik `b_test_g.csv`; forsøk #1024 = 0,474286 målt av tavla |
| --lekkasjefri --data data_v3_val, val 2025 | 0,183297 | 0,4286 (optimistisk, grensen valgt her) | 0,3340 | byte-lik `b_val_g.csv` (#1022) |
| uten flagg (frossen leder) | – | 0,5092 | – | byte-lik `oppgave_1988/full_data_v3.csv`, standardoppførselen er uendret |

Merknader:
- Val-forsøket kom ikke på tavla. Måleren for #1993 har nå bare fasit for test. Valfila er identisk med dommerens #1022.
- Ruting på konfidens 0,6 sender 14,8 % av sakene til et menneske. Presisjonen på de ikke-rutede er 0,78.
- `arbeid/` er i .gitignore, så det er ingen commit. Versjonen før endringen ligger i `arbeid/oppgave_1997/train_v3_for_1997.py`.
