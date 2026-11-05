# Case 1 #2701: speiderens «siste stemme»-regel på ny frossen repo4 – ikke bytt

Regel (#2569): fjern MOT-flagg når NBIMs siste stemme på samme selskap + samme forslagstekst (tidligere år) var FOR. Variant valgt på val-året T-1, test T målt én gang med offisiell måler (oppgave_2567/maaler_aar.py, F1 MOT).

| | 2024 | 2025 | 2026 | snitt |
|---|---|---|---|---|
| repo4 (frossen) | 0,5057 | 0,5309 | 0,5120 | 0,5162 |
| + av (valgt på val alle år) | 0,5269 | 0,5375 | 0,5246 | 0,5297 |
| + paa | 0,5029 | 0,5181 | 0,5039 | 0,5083 |
| + av+paa | 0,5238 | 0,5244 | 0,5161 | 0,5214 |

Byttregel #265: snitt +0,02 og intet år -0,02. «av» gir +0,0135 og er bedre alle år, men under +0,02. **Frossen står.** Kan nevnes for juryen som robust etterbehandling (konsistent gevinst) og som neste steg, ikke som hovedtall.
Kode: arbeid/oppgave_2701/siste_repo4.py (kjør `uv run --project arbeid/oppgave_2023 python arbeid/oppgave_2701/siste_repo4.py`).
