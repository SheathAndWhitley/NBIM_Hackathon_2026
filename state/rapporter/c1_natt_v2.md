# Case 1 natt, vinkel 2 (SVD av tf-idf inn i LGBM): STÅR, +0,019 mot kravet +0,02 (smed, #2882)

Vinkelen kom fra arkitekten (c1_natt_vinkler.md). Prototypen var `oppgave_2868/svd_rull.py`, og arkitekten har sjekket den for lekkasje. Koden ligger i `arbeid/c1_natt/v2/v2_rull.py`, som er prototypen med `--k`. Frosne filer er ikke rørt. REGEL.md ble skrevet 19:44:09, før svarfilene. Dommen kommer fra `mal_kandidat.sh`. Forsøket står på tavla som #1250.

Valget av k gikk etter REGEL: for hvert testår T ble k ∈ {32, 48, 64} valgt etter val-F1 på T-1. Det ga k=32 for 2024 (val 0,385), k=64 for 2025 (val 0,581) og k=48 for 2026 (val 0,554).

| år | frossen | v2 | diff |
|---|---|---|---|
| 2023 (vakt) | 0,3535 | 0,3592 | +0,006 |
| 2024 | 0,5057 | 0,5326 | +0,027 |
| 2025 | 0,5309 | 0,5436 | +0,013 |
| 2026 | 0,5120 | 0,5299 | +0,018 |
| snitt 24-26 | 0,5162 | **0,5354** | **+0,0192** |
| dom | | **STÅR** | krav +0,02 |

- Kandidaten slår frossen alle fire år, også vakt-året. Det er det jevneste nattresultatet så langt (v1 ga +0,007 med tre år i minus). Snittet ligger likevel 0,0008 under kravet, og regelen står.
- I skriptets egen test-F1 ligger alle ni k×år-kjøringene mellom 0,52 og 0,56. Gevinsten henger altså ikke på valget av k. (Den interne tallrekka er ikke den offisielle måleren og er ikke brukt til noe valg.)
- Jeg har ikke målt noen ny variant (fast k, flere komponenter) etter at tallet var kjent. Det ville vært å velge på test.
- Neste steg: vinkel 2 er en ren trekk-endring i LGBM-halvdelen og er ortogonal til av-regelen og regimeskiftet (smed2 #2881). En kombinasjon «v2 + beste etterbehandling» kan bli en ny kandidat, med ny REGEL.md og ny mappe. Dommeren bør bestemme om den skal måles før dommen 02:00.
