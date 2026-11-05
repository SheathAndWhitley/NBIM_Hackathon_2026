# Case 1 (#2498): V2 hybrid + vår rangering, KI mot frossen og mot hybriden (målt etter frys, ikke hovedtall)

Variant valgt på val 2025 i #2495: **V2** (hybrid ≥ 0,407 → MOT, hybrid < 0,091 → ikke MOT, ellers frossen #2044 p ≥ 0,919).
Test 2026, offisiell måler v3 `--score mot`, 58 MOT i fasit. KI: `oppgave_2103/diff_ki.py`, parret klyngebootstrap per selskap, 2000 trekk, seed 0.

| svar | F1 MOT | P | R | TP/FP/FN | PR-AUC (avvik) | diff mot frossen [95 % KI] | diff mot hybrid [95 % KI] |
|---|---|---|---|---|---|---|---|
| frossen #2044 (hovedtall) | 0,4762 | 0,4412 | 0,5172 | 30/38/28 | 0,5245 | – | – |
| repoets hybrid | 0,5455 | 0,5769 | 0,5172 | 30/22/28 | 0,4127 | +0,069 [+0,007; +0,133] | – |
| V2 hybrid + vår rangering | 0,5161 | 0,4848 | 0,5517 | 32/34/26 | 0,4088 | +0,040 [−0,007; +0,095], B<A 5 % | −0,029 [−0,067; +0,010], B<A 93 % |

- V2 er ikke sikkert bedre enn frossen og ikke sikkert dårligere enn hybriden. Den slår ikke hybriden alene.
- PR-AUC for V2 er lav fordi konfidensen er blandet (hybridscore der hybriden avgjør, ellers vår p); den er ingen ren rangering. Vår rene rangering (frossen) har høyest PR-AUC, 0,5245.
- Ulike prediksjoner: 22 mot frossen, 14 mot hybriden.
- Avsnitt lagt inn i `arbeid/hack/c1/leveranse/NESTE_VERSJON.md` (etter personnøkkel-avsnittet), merket «ikke hovedtall, målt etter frys». Tallvakta: 18 filer, 169 påstander, 0 avvik. Frysvakt grønn (17 filer uendret). `levering/` og frosne filer er ikke rørt.
- NESTE_VERSJON.md hadde allerede ukommittede endringer fra en annen agent (personnøkkel-avsnittet), så jeg har ikke committet fila for å ikke ta med deres arbeid. Den som eier det avsnittet committer begge.

Kommandoer:
```
uv run python arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2495/svar_V2_t2026.csv test --data real --score mot
uv run python arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2103/full_test.csv arbeid/oppgave_2495/svar_V2_t2026.csv test
uv run python arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2464/svar_vaar_hybrid_t2026.csv arbeid/oppgave_2495/svar_V2_t2026.csv test
python3 -I arbeid/verktoy/c1_tallvakt.py
```
