# Case 1 #2926: snitt av 5 LGBM-frø på v2+av gir ikke jevnere treff (STÅR)

Regel skrevet før måling: arbeid/hack/varianter/smed3_utf_frosnitt/REGEL.md. Kode: samme mappe (frosnitt.py, kjor.sh).
Kandidat: v2+av uendret (miks LR+LGBM, SVD k 32/64/48, hist 2, repo-trekk, av-regel), men LGBM trent med frø 0–4
(de fem kjøringene fra #2920, tau=0) og p_avvik snittet over de fem før terskel. Terskel valgt på val-året T−1 på snittet,
samme kvantilregel som v2+av. Måler: maaler_aar.py --data real --score mot (F1 på MOT mot styret).

## Tabell (F1 MOT)
| År | v2+av (#2890) | frøsnitt 5 frø | enkeltfrø snitt (sd) | 4-frø-snitt, utelat ett: min–maks (sd) |
|---|---|---|---|---|
| 2023 (vakt) | 0,3723 | 0,3636 | 0,3582 (0,0100) | 0,3469–0,3656 (0,0084) |
| 2024 | 0,5731 | 0,5595 | 0,5591 (0,0079) | 0,5432–0,5763 (0,0125) |
| 2025 | 0,5667 | 0,5667 | 0,5530 (0,0122) | 0,5604–0,5667 (0,0035) |
| 2026 | 0,5391 | 0,5664 | 0,5593 (0,0082) | 0,5470–0,5664 (0,0076) |
| snitt 24–26 | 0,5596 | 0,5642 | 0,5571 | |

## Dom etter regelen
STÅR. Snitt +0,0046 over v2+av, kravet var +0,02. Intet år under v2+av−0,02 (2023 0,3636 ≥ 0,3523), så kandidaten er
trygg, men ikke bedre. Ikke anbefalt bytte.

## Funn om robusthet
- Frøsnittet gir ikke jevnere F1. Fire-frø-ensembler (fem utelatelser) spriker like mye som enkeltfrø: sd 0,0125 i 2024
  mot 0,0079 for enkeltfrø. Fem-frø-tallet 0,5642 er ett trekk fra en fordeling med sd rundt 0,01, ikke et fast punkt.
- Sannsynlighetene er stabile (frø-korrelasjon på test-p 0,97–0,99), men F1 er det ikke: ~90 MOT-saker per år gjør at
  én sak flyttet over terskelen gir ≈0,005 F1, og terskelen velges på et val-år med like få saker.
- Konsekvens for ærlig evaluering: forskjeller under ±0,015 per år mellom v2+av-varianter er frøstøy og bør ikke brukes
  til å velge. Det støtter #2919 (trekk-endringer gir ±0,03 per år) og bytteregelens +0,02-krav.
- v2+av i pakka bruker random_state=None; 2026-tallet 0,5391 ligger i nedre kant av frøspennet (0,5487–0,5714).
  Vil dommeren ha reproduserbart tall, bør pakka låse frøet (f.eks. 0), ikke snitte.

## Filer
- arbeid/hack/varianter/smed3_utf_frosnitt/ut/frosnitt_<T>_av.csv (svarfiler), *_maal.txt (målerutskrift), loo.txt.
