# Case 1 (#1978): gulvregel + modell gir 0,43–0,45, men ingen kombinasjon slår smed2 v3 alene (0,466)

**Kort:** Begge kombinasjonene slår gulvet (0,383), men taper mot smed2 lgbm v3 alene, fordi v3 allerede har NBIMs historikk som kjennetegn. Anbefaling: smed2 v3 er hovedmodellen. «Gulv ELLER modell» er en **høy-recall-modus** for menneskesjekk: den fanger 71 av 129 MOT-stemmer mot 51, og gir høyere PR-AUC.

## Metode (ingen tuning på test)
- Mekanismene ble tunet bare på val 2025 (`data_v3_val`, gulv bygd fra train 2024). Mekanismen og terskelen ble valgt før test ble kjørt.
- Fem mekanismer på val, F1 (gulv 0,361, smed2 v3 0,350):
  eller 0,418 · og 0,229 · gulv der det har historikk, ellers modell (`tomt`) 0,434 · vektet blanding 0,435 · gulv_veto 0,434.
- `tomt` er flat over terskelen (0,41–0,43 for t mellom 0,3 og 0,8). Valgt: t = 0,5, rund verdi midt på platået.

## Test 2026 (måler maaler.py + data_v3/fasit, 129 avvik)
| kandidat | P | R | F1 | PR-AUC | rutet <0,6 |
|---|---|---|---|---|---|
| gulv (dommer #984) | 0,348 | 0,426 | 0,383 | 0,328 | |
| smed2 v3 alene (#990) | **0,567** | 0,395 | **0,466** | 0,441 | 58 |
| **tomt t=0,5** (valgt på val) | 0,374 | 0,504 | 0,429 | 0,414 | 123 |
| eller (ingen parametre) | 0,384 | **0,550** | 0,452 | **0,456** | 125 |

## Hvorfor kombinasjonen ikke vinner på F1
- smed2 v3 bruker allerede NBIM-historikken som kjennetegn. Gulvet legger derfor bare til falske MOT (fp 39 → 109–114) på selskaper der NBIM har snudd og stemmer FOR igjen.
- Rangeringen på val stemte ikke på test. På val var modellen svak (0,350, trent på bare 2024). På test er den sterk (trent på 2024+2025). Val med ett treningsår undervurderer modellen. Dette bør stå i evalueringskapittelet (#1979).

## Anbefaling
- **Ikke bygg kombinasjonen som hovedsvar.** Lever smed2 v3 (F1 0,466).
- Bruk gulvet som forklaring og reserve. «NBIM stemte MOT her i fjor» er et sitérbart argument for agenten (#45), og regelen er reserve hvis modellen feiler (#1976).
- Høy-recall-modus (eller): når et menneske uansett skal sjekke de flaggede sakene, fanger den 20 flere MOT-stemmer for 75 ekstra flagg. Kan vises i demoen som en terskelbryter.

## Avvik og forbehold
- Måleren på disk har endret sha siden 823c9610fe (nå cb9243ddee). smed2 v3 gir likevel samme tall (0,465753), så tallene er sammenlignbare. `tavle forsok` avviste føringen fordi #1978 mangler egen måler. Dommeren må sette den (`tavle maaler --oppgave 1978`) og føre tallene, så de er selvmålte til da.
- Kode: `arbeid/oppgave_1978/kombiner.py`. Prediksjoner: `pred_tomt_test.csv`, `pred_eller_test.csv`.
- Tilfeldig vinkel er ikke trukket. Tidsboksen og oppgaven var en ren måling.
