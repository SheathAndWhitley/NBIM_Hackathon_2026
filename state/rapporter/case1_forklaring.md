# Case 1: «hvorfor flagget» – de tre viktigste grunnene per MOT-sak (smed2 #2007)

**Én kommando** (ca. 4 s fra kald start):
`cd arbeid/kandidater/smed2_c1_mot && uv run python forklar.py`
→ `forklaring.csv` (221 MOT-saker i test 2026) + `pred_b_test.csv`. `--alle` gir også grunner for FOR-saker.

**Modellen og grensen er ikke endret.** `forklar.py` kjører `train_v3.py --lekkasjefri` uendret i samme prosess, og fanger de 5 frø-modellene som scorer test 2026. Deretter tar den `pred_contrib=True` (SHAP i log-odds) på hver modell og bruker snittet over frøene.
- `pred_b_test.csv` er **byte-lik** med `arbeid/oppgave_1993/b_test_g.csv` (`cmp` OK), og måleren gir SCORE **0,474286**, P 0,376, R 0,643.
- Skriptet stopper med en feilmelding hvis de fangede modellene ikke gir nøyaktig de samme MOT-sakene (rå score ≥ frosset grense 0,1833).

Kolonner: `id, utsteder, moetedato, anbefaling, p_avvik, raa_score, grunn1-3` (setninger på vanlig språk), `kjennetegn1-3, bidrag1-3` (SHAP i log-odds, alle positive, altså retning MOT). Utgangspunktet før bidragene er −2,89 i log-odds (ca. 5 %).

## Tre eksempler (test 2026)
1. **Microsoft, 05.12.2025 – flagget, NBIM stemte MOT (treff).** p = 1,0.
   - Toppsjefen fikk 96,5 mill. dollar i samlet lønn siste år. (+2,54)
   - Forrige gang stemte NBIM mot lønnspakken her. (+0,66)
   - Aksjebasert lønn var 12,0 mrd. dollar siste år. (+0,38)
2. **Warner Bros. Discovery, 23.04.2026 – flagget, NBIM stemte MOT (treff).** p = 1,0.
   - Toppsjefen fikk 165,0 mill. dollar i samlet lønn siste år. (+2,60)
   - Forrige gang stemte NBIM mot lønnspakken her. (+0,51)
   - Forslaget nevner fusjon. (+0,35)
3. **Chime Financial, 02.06.2026 – flagget, men NBIM stemte FOR (falsk alarm).** p = 1,0.
   - Toppsjefen fikk 98,9 mill. dollar i samlet lønn siste år. (+3,09)
   - Aksjebasert lønn var 1,1 mrd. dollar siste år. (+0,60)
   - 100 dollar investert ble til 68 dollar over perioden (totalavkastning). (+0,25)

Eksempel 3 viser poenget for forvalteren. Grunnene er reelle mønstre, men ikke en dom. Her kan mennesket se at modellen reagerte på lønnsnivået alene.

## Hva som oftest driver flaggingen (221 saker)
Viktigste grunn: aksjebasert lønn 74, toppsjefens lønn 58, NBIMs forrige stemme 44, fusjon i forslagsteksten 27. Grunnene er altså lønnsnivå, NBIMs egen historikk og forslag knyttet til transaksjoner. Det stemmer med retningslinjene om lederlønn.

## Stabilitet (robusthet)
`uv run python stabilitet_forklaring.py` måler hver av de 5 frø-modellene for seg mot snittet. Grunn 1 er den samme i **97,6 %** av MOT-sakene, og topp tre overlapper **90,8 %**. Grunnene er altså ikke støy fra ett frø. (`stabilitet_forklaring.txt`)

## Ærlige forbehold
- SHAP forklarer **modellen**, ikke NBIM. En grunn betyr «dette trakk scoren opp», ikke «NBIM stemte mot på grunn av dette».
- 44 av 663 grunner er «toppsjefens lønn mangler i SEC-dataene». At tallet mangler, trekker i seg selv mot MOT. Det er et mønster i dataene, ikke en vurdering av lønnen. Setningen sier dette rett ut.
- Noen tall ser rare ut, for eksempel «lønnen endret seg med 2810 %» for Cloudflare. Det kommer av et svært lavt lønnstall året før i SEC-dataene (PvP). Disse tallene er rådata, ikke en feil i forklaringen.
- Bidragene er snitt i log-odds over 5 frø. Lederens prediksjon er snittet av sannsynligheter. Rangeringen av grunnene påvirkes ikke av dette i praksis, men summen av bidragene er ikke nøyaktig lik p.
- Fasit ble bare brukt til å velge hvilke eksempler som skal vises (et treff og en falsk alarm). Den ble ikke brukt i forklaringen eller modellen. Test 2026 var allerede målt én gang (#1993).
