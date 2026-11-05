# Dommer #1981: smed2s lgbm v3 fra kald start, test og val med bootstrap

**Kjøring:** smed2s `train_v3.py` (sha 19c3e29) og `sec_feats.py` (sha 462249d) ble frosset kl. ca. 11:25 og kopiert til `/tmp/kald1981` uten prediksjonsfiler og `.venv`. Der ble miljøet bygd på nytt med `uv sync` og koden kjørt med `env -i`. Inndata var bare `train.csv` og `test_input.csv`, uten fasit. To kjøringer ga identisk fil, så koden er deterministisk. Måler: `maaler.py`, oppgavemåler cb9243ddee (samme kommando og samme tall som 823c9610fe). Gulvet er `gulv_v3.py`. Bootstrap: 2000 trekk, parret mot gulvet, 95 %. Skript og prediksjoner ligger i `arbeid/oppgave_1981/`.

| | F1 modell [95 %] | gulv | diff mot gulv [95 %] | P(diff>0) |
|---|---|---|---|---|
| TEST 2026, dommer kald (#1001) | **0,445** [0,358; 0,529] | 0,383 | +0,062 [−0,023; +0,150] | 0,93 |
| TEST 2026, smed2 #990 (fil 11:18) | 0,466 [0,380; 0,550] | 0,383 | +0,082 [+0,004; +0,166] | 0,98 |
| VAL 2025, dommer kald (#1002) | **0,376** [0,301; 0,442] | 0,361 | +0,015 [−0,074; +0,110] | 0,62 |
| VAL 2025, smed2 #990 (fil 11:18) | 0,350 [0,270; 0,421] | 0,361 | −0,010 [−0,104; +0,088] | 0,42 |

**Dom:** Smed2s tall på 0,466 lar seg ikke reprodusere eksakt. Koden har endret seg etter at pred_v3.csv ble skrevet kl. 11:18: `train_v3.py` er fra 11:22, og SEC-data er lagt til i `sec/`. Smed2s egen kjøring kl. 11:22 ga 0,468/0,373, og min kalde kjøring av samme mappe noen minutter senere ga 0,445/0,376. Mappa er altså fortsatt i bevegelse. Til modellfrysen kl. 16 må smed2 levere en frosset kopi med sha.

På test slår modellen gulvet med +0,06 til +0,08 F1. Men det er usikkert: i dommerens egen kjøring krysser intervallet null. På val er forskjellen ±0,01–0,02, og intervallet spenner fra −0,07 til +0,11. Avstanden mellom test og val (0,07–0,09) er like stor som hele fordelen over gulvet. **Det er ikke vist at modellen slår gulvet på F1.** Det ærlige utsagnet er dette: modellen er minst like god som gulvet, sannsynligvis litt bedre, og fordelen på test er delvis flaks. Den sikre gevinsten ligger i rangeringen. PR-AUC er 0,425 på test og 0,304 på val, mot gulvets 0,383 (test) og 0,212 (val). Modellen er derfor mer nyttig til å rute usikre saker til et menneske og sortere dem (#1955) enn som ja/nei-regel.

**Lekkasjesjekk:** NBIM-historikken bruker bare train-rader med møte før dato. Vanguard-data brukes bare når innsendt < møtedato. SEC Pay-vs-Performance brukes for regnskapsår som slutter minst 20 dager før møtet, og float minst 60 dager før. Det ble ikke sjekket at tallene faktisk var publisert før møtet: XBRL-frames er lastet ned i dag og har ingen arkiveringsdato. Normalt er proxyen selve innkallingen, så risikoen er lav. Den bør likevel nevnes i JURY.md. Ingen grense er valgt på test: grensa velges på siste 25 % av train (0,294 på test-kjøringen, 0,400 på val-kjøringen).
