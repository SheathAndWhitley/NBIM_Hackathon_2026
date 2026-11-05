# Case 1 #2709: av-regelen med nylighet og p-vakt – ingen forbedring, frossen står

Utvidelse av #2701/#2704 på repo4 (frossen 0,5162), samme måler (oppgave_2567/maaler_aar.py, F1 MOT), variant valgt på val T-1.

| variant | 2024 | 2025 | 2026 | snitt |
|---|---|---|---|---|
| repo4 frossen | 0,5057 | 0,5309 | 0,5120 | 0,5162 |
| av (#2701) | 0,5269 | 0,5375 | 0,5246 | 0,5297 |
| avn1 (siste FOR-stemme senest i fjor) | 0,5207 | 0,5342 | 0,5203 | 0,5251 |
| avn2 (siste FOR-stemme senest for 2 år siden) | 0,5238 | 0,5342 | 0,5203 | 0,5261 |
| avp / av2 (behold flagg med p_avvik i topp 10 %) | 0,5269 | 0,5375 | 0,5246 | 0,5297 |
| valgt på val (ærlig) | 0,5269 | 0,5375 | 0,5246 | 0,5297 |

Funn: gamle FOR-stemmer forutsier fortsatt (å kreve nylighet taper i alle år). P-vakten endrer ingenting, fordi flaggene regelen fjerner aldri ligger i topp 10 % av p_avvik. Snittet er +0,0135 over frossen, under kravet på +0,02 (#265). **Frossen står.**
Kode: `cd arbeid/oppgave_2709 && uv run --project ../oppgave_2023 python nylig_repo4.py`
