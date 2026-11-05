# Case 1 #2704: siste-stemme-regelen utvidet (typefallback, flertall) – ingen forbedring, frossen står

Utvidelse av #2701 på repo4 (frossen 0,5162). Samme måler (oppgave_2567/maaler_aar.py, F1 MOT), variant valgt på val T-1.

| variant | 2024 | 2025 | 2026 | snitt |
|---|---|---|---|---|
| repo4 frossen | 0,5057 | 0,5309 | 0,5120 | 0,5162 |
| av (#2701) | 0,5269 | 0,5375 | 0,5246 | **0,5297** |
| avflert (flertall i historikk FOR) | 0,5000 | 0,4967 | 0,4957 | 0,4975 |
| avtype (fallback selskap+proposal_type, 2 siste FOR) | 0,5185 | 0,5283 | 0,5357 | 0,5275 |
| avtype3 (fallback, ≥3 og alle FOR) | 0,5181 | 0,5375 | 0,5289 | 0,5282 |
| valgt på val (ærlig) | 0,5181 | 0,5375 | 0,5246 | 0,5267 |

Funn: siste stemme er bedre enn flertall (NBIM endrer praksis over tid). Typefallback hjelper 2026 men taper 2024; ærlig val-valg gir 0,5267, under «av». Ingen variant når +0,02 over frossen (#265). **Frossen står.**
Kode: `uv run --project arbeid/oppgave_2023 python arbeid/oppgave_2704/typefall_repo4.py`
