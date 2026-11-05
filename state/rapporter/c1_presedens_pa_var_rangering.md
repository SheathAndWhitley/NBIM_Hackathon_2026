# Case 1 (#2485): «presedens først» oppå vår frosne #2044-rangering. Slår ikke 0,545

Bare for neste versjon. Frossen pakke og `levering/` er ikke rørt.

## Hva er gjort
- Presedensflagget er hentet rett fra NBIM-repoets `ballot.load_real()`: `prev_same = prev_same_person.fillna(prev_same_item)`. Avvik teller også AVSTÅ (som i dom #2465). Det gir 375 saker med flagg 1 i hele datasettet, 43 i test 2026.
- Score = 1 + p_avvik hvis prev_same==1, ellers p_avvik. p_avvik er fra den frosne #2044 (`oppgave_2103/full_val.csv` og `full_test.csv`). Dette er samme form som repoets hybrid, bare med vår rangering i stedet for deres modell.
- Terskelen er valgt på val 2025 (F1 MOT) og så brukt uendret på test: **t = 0,9215**. Val F1 0,537 (TP 47, FP 29, FN 52). Ren presedens (t ≥ 1) ga 0,506 på val og ble derfor ikke valgt.

## Tallene, test 2026 (offisiell måler v3, 58 MOT i fasit)

| svar | F1 MOT | P | R | flagget MOT | PR-AUC (avvik) |
|---|---|---|---|---|---|
| frossen #2044 | 0,476190 | | | | |
| **#2044 + presedens først (t=0,9215 fra val)** | **0,484848** | 0,4324 | 0,5517 | 74 (TP 32, FP 42) | 0,447 |
| ren presedens (t ≥ 1, ikke valgt på val), til sammenligning | 0,5149 | | | | |
| NBIM-repoets hybrid, vår splitt (dom #2465) | 0,545455 | | | | |

KI mot #2044 (`diff_ki.py`, klyngebootstrap per selskap, 2000 trekk): **+0,0087, 95 % KI [−0,024; +0,048]**, B<A i 34 % av trekkene, 8 ulike prediksjoner. Altså støy.

Merknad: svarfila setter p_avvik = min(score, 1), så alle presedenssaker får konfidens 1 og ruting blir 0 til menneske. Rutingen er ikke målt her; bare F1.

## Hva det betyr
- Presedens først oppå vår rangering gir +0,009, innenfor støyen. Det slår **ikke** 0,545 fra repoets hybrid.
- Grunnen: den val-valgte terskelen ligger nesten på vår frosne (≈0,919). Regelen legger da bare til noen få presedenssaker. Vår rangering ser allerede ut til å fange det meste av presedensen.
- Ren presedens ville gitt 0,515 på test, men val 2025 valgte bort den. Å bytte til den etter å ha sett test ville være å velge på test.
- Repoets forsprang ser altså ikke ut til å komme av presedensregelen alene. Det kommer av deres modell eller trekk sammen med regelen. Det er neste spor for neste versjon. Det er ikke en terskel vi kan skru på.

## Kommandoer (fra landsbymappen)
```
cd arbeid/oppgave_2485 && uv run python -I hent_presedens.py && uv run python -I kombiner.py && cd ../..
uv run python arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2485/svar_presedens_t2026.csv test --data real --score mot
uv run python arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2103/full_test.csv arbeid/oppgave_2485/svar_presedens_t2026.csv test
```
Svarfil: `arbeid/oppgave_2485/svar_presedens_t2026.csv`. Kode: `hent_presedens.py`, `kombiner.py` (samme mappe, eget miljø kopiert fra #2464).
