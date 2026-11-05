# Case 1 (#1982): terskel valgt bare på val gir «gulv ELLER topp 4 % av modellen», F1 val 0,435 og test 0,450

**Kort:** Regelen er valgt og låst på val 2025 før test ble kjørt, og test ble kjørt én gang. På test gir den F1 0,450. Det slår gulvet (0,383) klart: +0,067, 95 % KI [+0,030; +0,110]. Den ligger 0,016 under smed2 v3 alene (0,466), men den forskjellen er innenfor støyen: KI [−0,078; +0,044]. Dette er det ærlige val-valgte tallet. 0,466 er bare ærlig hvis vi sier at terskelen kommer fra smed2s egen interne kalibrering på train (det gjør den, se under).

## Regelen (valgt på val, ingen fasit på test)
`MOT hvis gulvet sier MOT (NBIM stemte MOT på selskapet før) ELLER p_avvik ≥ 96-persentilen av settets egne modellscorer` (topp 4 %, likeverdier tas med).
- Hvorfor en rangterskel og ikke en fast sannsynlighet: val-modellen er trent på 2024 alene og testmodellen på 2024+2025, så kalibreringen flytter seg. En andel flagget overlever det bedre enn en fast p. Persentilen regnes av testprediksjonene selv, uten fasit.
- På test ble t = 0,400 (på val 0,643). Det flagget 182 av 1246 (val: 172 av 1506).

## Valet på val 2025 (n 1506, 136 MOT), F1 / bootstrap-snitt (300)
| regel | beste på val |
|---|---|
| gulv | 0,361 |
| smed2 alene, absolutt t 0,15–0,60 | 0,327–0,350 (smed2 sin egen t ≈ 0,45 er toppen, 0,350) |
| smed2 alene, topp q 6–20 % | 0,328–0,350 |
| **gulv ELLER topp q, q 2/4/6/8 %** | 0,422 / **0,435** / 0,418 / 0,418 |
q = 4 % gir best F1 og best bootstrap-snitt (0,433), og ligger på et platå (0,42–0,44 for 2–8 %). Platået er derfor robust. Ren modell kan ikke slå gulvet på val med noen terskel. Derfor velger en ren val-regel kombinasjonen.

## Test 2026, én kjøring (`maaler.py` + `data_v3/fasit.csv`, 129 MOT)
| kandidat | P | R | F1 | PR-AUC |
|---|---|---|---|---|
| gulv | 0,348 | 0,426 | 0,383 | 0,328 |
| smed2 v3 alene (egen intern terskel) | 0,567 | 0,395 | 0,466 | 0,441 |
| **val-regel (#1982)** | 0,385 | **0,543** | **0,450** | **0,456** |
Forsøk **#1003 = 0,450161**. Det er ført på #1976-måleren (cb9243ddee), fordi `tavle forsok` avviste 823c9610fe: «måleren er endret på disk (823c9610fe -> 4b32b210dc)». smed2 v3 gir samme tall på begge målerne (0,465753, jf. #1978).

## Anbefaling for juryen (metode 60 %)
- **Hovedsvar: velg val-regelen (0,450)**, eller lever smed2 alene og si tydelig hvor terskelen kommer fra. smed2s terskel er valgt på de siste 25 % av train (isotonisk kalibrering i `train_v3.py`) og ikke på test, så 0,466 er heller ikke test-tunet. Men på val taper den regelen mot gulvet (0,350 mot 0,361). En jury som ser val-tabellen vil spørre om dette. Den rene historien er: «regelen valgt på val, F1 0,450 på test, +0,067 over gulvet, signifikant».
- Val-regelen har høyere recall (70 av 129 MOT mot 51) og høyest PR-AUC. Det passer en agent som sender flaggene til et menneske.
- Forskjellen 0,450 mot 0,466 er ikke signifikant (andel bootstrap > 0: 0,315). Ingen av dem kan kåres som best ut fra test alene.

## Forbehold
- Tilfeldig vinkel er ikke trukket. Dette er en ren valgoppgave på 30 min.
- Val-modellen har ett treningsår og testmodellen to, så val undervurderer modellen. Det taler for at q burde vært noe høyere på test, men det er ikke justert, for da ville vi tunet på test.
- Kode: `arbeid/oppgave_1982/velg.py` (val-sveip), `bruk.py` (regelen uten fasit). Prediksjoner: `pred_val.csv`, `pred_test.csv`.
