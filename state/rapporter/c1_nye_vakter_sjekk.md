# Case 1: dommerens sjekk av menneske-vaktene fra #2152 (dommer #2155, 05.11 kl. 13.2)

**Dom: GODKJENT.** Vaktene endrer ikke svarene på ekte data. De slår bare til på forstyrrede data, slik de skal.

## Kald kopi (egen mappe /tmp/dommer_2155, `fremmed.sh`, frysvakt før frys: grønn)
- HOVEDTALL F1 MOT **0,476190** (TP 30, FP 38, FN 28, P 0,4412, R 0,5172). 188 av 1578 til menneske, **183 av 1539** med fasit (11,9 %). TALLVAKT GRØNN (131 påstander, 0 avvik). Kjøring 49 s.
- sha256 er like i smedens før-kjøring (foer_std), smedens etter-kjøring (etter_std) og min kalde kopi:
  - agent.csv `f0444a47…17f7`
  - _pred_uten_ruting.csv `22ac6717…c788f` (= frosne `kjor_agent_real_maskin_alene.csv`)
  - pred_maaler.csv `b113b545…3653`

## Egen før-kjøring (stoler ikke på smedens foer_std)
Jeg fjernet vaktblokken (#2152) fra c1_real.py i kopien og kjørte agenten på nytt. Alle tre filene, også agent.csv med `til_menneske` og `rutingsgrunn`, er **byte-like** med kjøringen med vakter. Grunnen er at ingen 2026-sak har både `mgmt_rec` og `mgmt_rec_raw` tom (0 av 39 med tom `mgmt_rec`: 38 «None» og 1 «One Year»), og ingen har tom country eller market. Det stemmer med smedens funn. Kopien er satt tilbake etterpå.

## Robusthet (`robusthet_frossen.py`, kjørt av meg, 39 s, ut til /tmp)
Tabellen i c1_robusthet_frossen.md reproduseres eksakt:
- uten_styret: F1 0,467, **100 %** til menneske (før #2152: 15,3 %), grunn «styrets anbefaling mangler».
- tomme_valgfri: F1 0,455, **100 %** til menneske (før: 8,2 %), grunn «land/marked mangler».
- basis 0,476 / 11,9 %. Øvrige rader er uendret (nye_selskaper 0,375 / 99,4 %, tom_tekst 0 / 100 %, ukjent_type_inn 0,476 / 100 %).
F1 i de forstyrrede testene er som før #2152, fordi vaktene bare rører rutingen.

## Merknad
c1_real.py ligger ikke i git. Etter kl. 16 er det frysfila (c1_frys.json) som beskytter denne versjonen.
