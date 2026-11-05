# Case 1 (#2495): repoets hybrid som første filter + vår frosne rangering for resten. Slår ikke 0,545

Bare for neste versjon. Frysen står, ingenting i `leveranse/` eller `levering/` er rørt.

## Oppsett
- Repoets hybrid er kjørt på vår splitt (train ≤2024, valg 2025, valgte GBM, t_flag 0,4074) med uendret kode (`arbeid/oppgave_2495/hent_hybrid.py`). Det gir hybridscore h for 2025 og 2026.
- Vår p_avvik er den frosne #2044 (`oppgave_2103/full_val.csv`, `full_test.csv`).
- Regelen: h ≥ a gir MOT-flagg (hybriden er sikker på ja). h < b gir ikke flagg (hybriden er sikker på nei). Ellers flagger vi når vår p ≥ t. a, b, t og w er valgt på F1 MOT på val 2025 og brukt uendret på test 2026. Test 2026 er ikke brukt til valg.
- Forbehold: hybridens egen t_flag er også valgt på 2025. Val-tallene for kombinasjonene er derfor litt optimistiske. Test er likevel ren.

## Tall, test 2026 (offisiell måler v3, 58 MOT)
KI: `diff_ki.py`, parret klyngebootstrap per selskap, 2000 trekk.

| svar | valgt på val | val F1 | test F1 MOT | TP/FP/FN | mot #2044 (0,476) | mot hybrid (0,545) |
|---|---|---|---|---|---|---|
| frossen #2044 | – | 0,520 | 0,4762 | 30/38/28 | – | – |
| repoets hybrid alene | (deres t) | 0,525* | **0,5455** | – | +0,069 [+0,007; +0,133] | – |
| V1: hybridflagg ELLER vår p ≥ 0,923 | t | 0,537 | 0,4812 | 32/43/26 | +0,005 [−0,035; +0,051] | −0,064 [−0,107; −0,022] |
| V1p: presedens ELLER vår p ≥ 0,923 | t | 0,537 | 0,4923 | 32/40/26 | +0,016 [−0,019; +0,058] | −0,053 [−0,101; −0,006] |
| **V2: hybrid sikker ja (h ≥ 0,407) / sikker nei (h < 0,091), vår p ≥ 0,919 i midten** | a, b, t | **0,548** | **0,5161** | 32/34/26 | +0,040 [−0,007; +0,095], B<A 5 % | −0,029 [−0,067; +0,010], B<A 93 % |
| V3: blandet score w·h + (1−w)·p | w, t (valgte w=0, lik V1p) | 0,537 | 0,4923 | | | |

\* hybridens egen terskel er valgt på 2025, så val-tallet er i utvalget.
Tavleforsøk #1196 (V2), #1197 (V1), #1198 (V1p).

## Hva det betyr
- Den beste kombinasjonen (V2) gir 0,516 på test. Det er +0,04 over vår frosne, men KI-et krysser 0. Mot hybriden er den −0,03, og B<A i 93 % av trekkene. **Ingen av variantene slår 0,545.**
- Val 2025 velger hver gang en terskel på vår score nær den frosne (0,92). Da legger vår rangering til mange flagg med lav presisjon: 66–75 flagg mot hybridens 52. Hybridens styrke er at den flagger få og sikre saker. Vår høye PR-AUC gir ikke F1 ved den terskelen val 2025 velger.
- V2 vinner over V1 fordi «sikker nei» fra hybriden fjerner falske flagg fra vår modell (FP 43 → 34). Det er den delen av hybriden som hjelper, ikke «sikker ja».
- Ærlig svar til ordre #259: på denne splitten og med terskel valgt på val har vi ikke en modell som slår repoet på F1 MOT. Beste ærlige kandidat for neste versjon er V2 (0,516). Den er ikke signifikant bedre enn frossen og ikke signifikant dårligere enn hybriden.

## Kommandoer (fra landsbymappen)
```
cd arbeid/oppgave_2495 && uv run python -I hent_hybrid.py && uv run python kombiner.py && uv run python blanding.py && cd ../..
uv run python arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2495/svar_V2_t2026.csv test --data real --score mot
uv run python arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2103/full_test.csv arbeid/oppgave_2495/svar_V2_t2026.csv test
uv run python arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2464/svar_vaar_hybrid_t2026.csv arbeid/oppgave_2495/svar_V2_t2026.csv test
```
Merknad: svarfilene har konfidens = hybridscore der hybriden avgjør og ellers vår p. Måleren ruter 0 saker til menneske for disse filene. Rutingen er ikke vurdert her.
