# Dom: injeksjonsvakt-ablasjonen (#2241) er GODKJENT (dommer, #2263, 05.11 14:10)

Smed3 meldte F1 MOT 0,4818 med og uten den nye injeksjonsvakta (#2237) og 0 falske alarmer på ren test 2026.
Jeg har målt begge filene selv. Tallene stemmer. Ført som målte forsøk #1142 (med vakt) og #1143 (uten vakt).

## Egne tall (rundens måler `bash arbeid/hack/maaler.sh <fil> real_test`, måler-sha 9efaab198a; v3 `maaler_offisiell_v3.py <fil> test --data real --score mot`)

| fil | sha256 | rundens måler F1 MOT | v3 F1 MOT |
|---|---|---|---|
| arbeid/oppgave_2241/agent_med_vakt.csv  | f0444a47ee0f921d51c07d4b799c656ba213b6772d1ea19b1f35ce49b3ef17f7 | 0,481752 | 0,476190 |
| arbeid/oppgave_2241/agent_uten_vakt.csv | f0444a47ee0f921d51c07d4b799c656ba213b6772d1ea19b1f35ce49b3ef17f7 | 0,481752 | 0,476190 |
| pred_med_vakt.csv / pred_uten_vakt.csv  | b113b545dd86b263bba78ea9ddb16f0580363d34e6718be66c1218025a783653 (begge) | 0,481752 | – |

Forskjellen 0,4818 mot 0,4762 er bare måleren (rundens måler mot v3), ikke modellen. Pakkas hovedtall 0,476 er v3-tallet og står.

## Sjekket
- **Identiske rad for rad:** `cmp` gir ingen forskjell, samme sha256 på begge agent.csv og begge pred.csv. 1578 rader, 1578 unike id-er, 74 MOT, 188 til menneske i begge.
- **Frossen modell:** pred_med_vakt.csv er rad for rad lik leveransens egen testkjøring (arbeid/hack/levering/kjor_agent_real_pred_maaler.csv, 0 ulike av 1578). Ablasjonen kjørte altså den leverte agenten, ikke en variant.
- **«Uten» slo vakta av på ekte:** kjor_uten_hoflig.py bytter ut `injeksjon_hoflig.finn` med en som aldri flagger, og c1_real.py kaller `hoflig.finn` via modulattributt (linje 163), så byttet virker.
- **0 falske alarmer fra ny vakt:** nøyaktig én rad har injeksjon_flagget=1 i begge filene: Bank of Jiangsu 2094542|10 «Approve Implementing Rules for Cumulative Voting System» (FOR/FOR, p_mot 0,0455, til menneske). Siden raden er flagget også når den nye vakta er av, kommer flagget fra det gamle vernet (vern.py), ikke den nye. Stemmer med rapporten.

## Avvik
Ingen. Smed3s tall (TP 33, FP 38, FN 33, F1 0,4818) er reprodusert. Fangsttallene i rapportens del 2 (23 671 av 25 248) er ikke kjørt på nytt av meg; de er utenfor akseptkravet og påvirker ikke stemmene.

## Konklusjon
GODKJENT. Vakta koster ingenting på vanlige saker, og modellen i pakka er urørt. Ingen endring før frysen.
