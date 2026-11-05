# Case 1: utfallet av siste MOT-forsøk (#2248) står i pakka, forkastet (#2252)

smed2, 05.11. Avsnitt 4 i `arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md` sier hva som ble prøvd og hvordan det ble valgt, og at forsøket er forkastet. TALLVAKT er OK (154 påstander, 0 avvik).

**Valgt på val 2025** (fra #2248): kravet var F1 > 0,552. Base fikk 0,5217, lt 0,5140, ny 0,5217, mt 0,5213 og alle tre 0,4804. Ingen kom over, så forsøket ble forkastet.

**Test 2026 etter valget**, bare til kontroll. Måler v3 `--score mot`, F1 på MOT mot styret, 58 MOT i fasit:

| Variant | TP | FP | FN | P | R | F1 |
|---|---|---|---|---|---|---|
| base (= levert) | 30 | 38 | 28 | 0,441 | 0,517 | **0,4762** |
| + lt | 29 | 36 | 29 | 0,446 | 0,500 | 0,4715 |
| + ny | 30 | 40 | 28 | 0,429 | 0,517 | 0,4688 |
| + mt | 30 | 41 | 28 | 0,423 | 0,517 | 0,4651 |
| + lt+ny+mt | 29 | 37 | 29 | 0,439 | 0,500 | 0,4677 |

- Base reproduserer det leverte hovedtallet eksakt. Ingen trekk slår det på test heller, og forskjellene er under støygrensen (~0,02).
- Prediksjonene endres ikke, og ingen frosne filer er rørt. Det er derfor ikke nødvendig å varsle smed/dommer om ny prediksjon.
- Om måler-sha: oppgaven nevner v3 8b09c36e01, men fila har nå sha256[:10] **418a937e57** (endret etter #2218, tallene er de samme, se #2238).
- Måten jeg målte på, som en lærdom: `pred_<n>.csv` mangler 39 test-id-er, og måleren avviser den. Mål på `svar_pred_<n>.csv`. Den er allerede skalert slik at p ≥ 0,5 betyr over grensa fra val.

Reproduser: `cd arbeid/oppgave_2252 && uv run --project ../oppgave_2023 python train.py ../../state/opplastet/20261105_114241_real_votes.csv --variant miks --hist 2 --test 1 --ut pred_<n>.csv [--x "lt|ny|mt|lt,ny,mt"]`, deretter `python3 -I ../hack/c1/maaler_offisiell_v3.py svar_pred_<n>.csv test --data real --score mot`. Loggene: `test_*.log`, `maal_*.txt`.
