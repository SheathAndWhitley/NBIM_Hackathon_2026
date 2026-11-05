# Case 1: ablasjon v2 av den frosne modellen miks h2 (oppgave sak 2089, smed3)

Kjørt på nytt fordi sak 1054/sak 1055 ble UGYLDIG da måleren ble endret på disk. Modellen er ikke byttet.
Kode: `<arbeidsmappe>/oppgave_2089/abl.py` (kopi av `oppgave_2044/train.py` med ablasjonsbrytere), `kjor.sh`.
Hver variant velger C og grense på val 2025 (trent <2025) og kjører test 2026 én gang med den grensen.
Måler: rundens `maaler_offisiell_v2.py --data real` (val: sha 882009b35e via sak 2073, test: sha 9d81a418dd, aktiv sak 2034).
Tall = F1 på MOT (avvik fra styret). Forsøk sak 1094–sak 1103 på tavla, alle målt.

| Variant | Val 2025 F1 (P/R) | Test 2026 F1 (P/R) | Flagget val/test (fasit 103/66) | Hva delen bidrar med (tolket på val) |
|---|---|---|---|---|
| Full (miks LR+LGBM, løpende historikk h2) | **0,522** (0,59/0,47) | 0,482 (0,46/0,50) | 81 / 71 | Referansen. |
| Uten sakstype (proposal_type ut) | 0,511 (0,58/0,46) | 0,504 (0,52/0,48) | 81 / 61 | Sakstypen er nesten overflødig (−0,011 på val): tekst og forslagsstiller bærer det samme; test gikk opp, men det er støy innenfor ±1 sak. |
| Historikk bare fra tidligere år (h1) | 0,448 (0,55/0,38) | 0,386 (0,46/0,33) | 71 / 48 | At historikken er *løpende* i sesongen gir +0,07 på val: MOT tidligere i samme sesong hos samme selskap er det sterkeste signalet. |
| Uten historikk i det hele tatt | 0,337 (0,26/0,49) | 0,282 (0,19/0,52) | 194 / 175 | Historikken er hoveddelen av modellen (−0,19 på val): uten den flagger modellen dobbelt så mange og presisjonen faller til 0,26. |
| Uten LightGBM (bare logreg) | 0,485 (0,44/0,54) | 0,470 (0,39/0,59) | 128 / 100 | LGBM i miksen gir +0,04 på val, mest via presisjon (0,44 → 0,59) og færre falske MOT. |

Ærlige forbehold:
- Val har 103 MOT, test 66. Én sak flyttet er ca. ±0,01 F1, så forskjeller under ~0,02 (sakstype) er ikke tolkbare.
- «Løpende historikk» (h2) bruker etiketter fra møter strengt før radens dato i samme sesong. Det forutsetter at NBIMs stemmer fra tidligere møter er kjent når neste sak predikeres (de publiseres løpende). Uten den antakelsen er h1-raden det ærlige tallet: test 0,386.
- Ingen variant er valgt på test; test er rapportert én gang per variant.
- Streng-MOT-tallet i måleren er 0 fordi svarfilene bruker 0/1-avvik, ikke FOR/MOT. SCORE (avvik-F1) er hovedtallet.
- Full reproduserer miks h2 nøyaktig (test 0,4818), så ablasjonen står på den frosne modellen.
