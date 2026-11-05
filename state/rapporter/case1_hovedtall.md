# Case 1: det ærlige hovedtallet til leveransen kl. 13 (dommer #1993)

**Tallet juryen skal få: F1 0,47 på 2026-test (95 % [0,40, 0,54]), med grensen valgt bare på val 2025. Gulvregelen får 0,38, og modellen slår den med +0,09 [+0,03, +0,15].**

## Metode
- Modell: lederen, variant b fra `case1_lekkasjefri.md`: smed2 lgbm v3 (frosset kode), `PVP_DAGER=100`, `--drop s_float,g_sbc_vs_float,s_lonn_vs_storr`, 5 seeds.
- Grense: modellen trenes på 2024 og predikerer val 2025. Grensen er den rå scoren som gir best F1 på val (0,1842, brukt 0,1833, midt mellom naborader), som i `case1_ruting.md`. Den låses i `grense.txt` før test kjøres.
- Test: modellen trenes på 2024+2025 og predikerer 2026 med den låste grensen. Kjørt én gang. Fasit er målt med `hack/c1/maaler.py`.
- Kald start (`env -i`, tom mappe, nohup) gir nøyaktig de samme tallene. Steg 1 er bit for bit lik #1988 b.

## Tall (F1 på avvik fra styret, bootstrap 2000 trekk med selskap (cusip) som klynge)
| | Val 2025 | Test 2026 |
|---|---|---|
| **variant b, val-valgt grense** | 0,429 [0,365, 0,490]* | **0,474 [0,404, 0,538]** |
| presisjon / recall | 0,34 / 0,57 | 0,38 / 0,64 |
| variant b, 1,25 × basisrate (#1988) | 0,403 | 0,493 [0,416, 0,563] |
| gulv (NBIM stemte MOT før) | 0,361 | 0,383 [0,309, 0,458] |
| val-valgt − gulv | +0,069 [−0,023, 0,156] | **+0,090 [+0,034, +0,147]** |
| val-valgt − 1,25× | +0,026 [−0,012, 0,068] | −0,020 [−0,065, +0,027] |
| PR-AUC (avhenger ikke av grensen) | 0,334 | 0,455 |

\* Val-tallet er optimistisk, fordi grensen er tilpasset der. Det ærlige tallet er test.

Forsøk: #1022 (val) og #1023 (test), måler ee16e5945c (oppgave 1993, `hack/c1/maaler.py` mot riktig fasit).

## Om 0,509 og 1,25 × basisrate
**0,509 ble ikke valgt på val, og skal ikke gis til juryen som hovedtall.** #1985 fant ikke hvor faktoren ble valgt. `hack_c1_smed2.md` (linje 29) viser at 1,0/1,25/1,5× ble sammenlignet med test-F1 ved siden av (0,487/0,509/0,476). På val ga de 0,418/0,418/0,422, så val alene hadde ikke pekt på 1,25. Uten lekkasje (variant b) gir 1,25× 0,493 på test, og forskjellen til val-valgt grense (−0,02) er innenfor støyen.

## Følsomhet (bare informasjon, ikke brukt til valg)
Når grensen flyttes innenfor området der val-F1 er ≥ 95 % av toppen (rå 0,167–0,238), ligger test-F1 på 0,46–0,49 (`folsomhet.txt`). Valget av grense flytter tallet med ±0,02, mindre enn bootstrap-intervallet.

## Kommando for dommer #1952 kl. 13
```
rm -rf /tmp/lev13 && env -i HOME=$HOME PATH=/usr/bin:/bin nohup bash <repo>/arbeid/oppgave_1993/hovedtall.sh /tmp/lev13 > /tmp/lev13.log 2>&1; cat /tmp/lev13.log
```
Forventet: grense 0,183297, VAL SCORE 0,428571, TEST SCORE 0,474286, PRAUC 0,454970. Prediksjonsfila til leveransen er `/tmp/lev13/b_test_g.csv`.

Filer: `arbeid/oppgave_1993/` (`train_v3_g.py` = #1988-kopien + `--grense-raa`/`--raa-ut`, `velg.py`, `boot.py`, `boot.txt`, `hovedtall.sh`).
