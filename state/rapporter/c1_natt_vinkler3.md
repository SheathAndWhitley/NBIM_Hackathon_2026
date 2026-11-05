# Case 1 natt: to vinkler oppå v2+av taper, og den rene kontrollen på det urørte året 2022 holder (arkitekt #2894)

Prototype: `arbeid/oppgave_2894/v3_rull.py` er en kopi av `c1_natt/v2/v2_rull.py` med to nye flagg, `--knn K` og `--bag N`. k er låst fra #2882 (32/64/48). Av-regelen velges på val T-1 akkurat som i v2av.py (`avmaal.py`), og målingen gjøres med maaler_aar.py, F1 MOT.
**KP:** jeg ventet v2 2025 SCORE 0,5213 og fikk 0,5213. Jeg ventet v2+av 0,3723/0,5731/0,5667/0,5391 og snitt 0,5596 (#2887), og fikk de samme tallene.
Sporsjekk: kNN/tekstminne og bagging/frø har ingen lukkede spor. GVG, retningslinjetrekk, grense per marked og nylighetsrate er ikke rørt.

| kandidat (alle + av valgt på val) | 2023 vakt | 2024 | 2025 | 2026 | snitt 24-26 | mot v2+av |
|---|---|---|---|---|---|---|
| frossen repo4 | 0,3535 | 0,5057 | 0,5309 | 0,5120 | 0,5162 | |
| v2+av (leder) | 0,3723 | 0,5731 | 0,5667 | 0,5391 | 0,5596 | |
| **K: kNN-tekstminne (k=10)** | 0,3587 | 0,5195 | 0,5146 | 0,5641 | 0,5327 | **−0,027**, 2024 −0,054 |
| **B: frø-bagging (5 SVD+LGBM-frø)** | 0,3723 | 0,5610 | 0,5537 | 0,5345 | 0,5497 | **−0,010**, alle år ≤ 0 |

## Vinkel K: tekstminne, de likeste tidligere sakene i alle selskaper (trukket: «databaser og indekser») → LUKK
**Hva:** for hver sak finner vi de 10 nærmeste merkede sakene etter cosinus på tf-idf, bare fra møter strengt før datoen (samme regel som hist 2). Det gir fire kolonner inn i både LR og LGBM: MOT-andel, likhetsvektet MOT-andel, største likhet til en tidligere MOT og største likhet totalt.
**Tall:** −0,027 mot lederen. Bare 2026 går opp (+0,025), mens 2024 faller 0,054. Teksten er alt i LR (tf-idf), i LGBM (SVD) og i nøkkelen for eksakt tekst. Naboene legger derfor mest til støy fra andre selskaper: det samme forslaget får ulik stemme etter selskap. Ikke bygg den.

## Vinkel B: frø-bagging → bytt ikke, men les den som en advarsel
**Hva:** snitt av 5 kjøringer med ulike frø for SVD og LGBM. Frø 0 er v2 uendret. Grense og C velges på val som før.
**Tall:** −0,010 mot lederen, og ingen år går opp. Bagging fjerner flaks fra frøet, så forventningen ligger mer i det tallet. v2+av sitt +0,043 har derfor trolig rundt 0,01 frø-flaks i seg. **Med bagging står den likevel +0,0335 over frossen** (0,5497), og verste år er 2023 +0,019. Lederen tåler altså frø-snitt etter regelen. Send dette til #2886 (frø-spredning) og 02-dommen (#2874). Forvent rundt +0,03, ikke +0,043.

## Test-sniking (#2887): ja, det trengs en ren kontroll. Den er nå kjørt på 2022 og 2021
Begge leddene ble valgt etter at testtallene for 2023-26 var kjent. Bootstrapen (#2889) måler bare utvalgsstøy og ikke seleksjon over mange forsøk. Derfor trengs et år som ingen har sett. 2022 og 2021 er aldri brukt som testår (grep: 0 treff). Regelen ble skrevet før kjøringen: `arbeid/oppgave_2894/kontroll/REGEL.md`.
| år (val T-1) | frossen | v2+av, k valgt på val | k-følsomhet (32/48/64) |
|---|---|---|---|
| **2022** (hovedår) | 0,3444 | **0,4268 (+0,083)**, k32 og k48 like på val, av ikke valgt | +0,082 / +0,080 / +0,013 |
| 2021 (tilleggsår, trent bare på 2019-20) | 0,6761 | +0,010 (k32) eller +0,000 (k48) | +0,010 / +0,000 / **−0,038** |
- **Etter regelen er kontrollen bestått, og sterkt bestått i 2022: +0,08.** Gevinsten gjentar seg på et år ingen har sett. Den kommer fra v2-delen (tekst i trærne). Av-regelen gjør nesten ingenting før 2023, fordi det finnes lite historikk.
- I 2021 er resultatet nøytralt. Valget av k er skjørt der: med lik val-score (alle tre k gir 0,6565 internt) avgjør uavgjort-regelen, og k64 gir −0,038. Det er et tynt år, men det betyr at k ikke bør velges på nytt hver natt. #2887 låste k, og det var riktig.
- Forslag til 02-dommen: før kontrollen i dommen ved siden av BYTT/STÅR, sammen med bagging-tallet. Regelen fra #265 endres ikke.

## Neste steg (anbefaling)
Andre halvdel av natta bør ikke gå til flere vinkler som stables, for begge tapte. Den bør gå til å gjøre lederen robust. (1) Tren det endelige byttet med frø-snitt, eller rapporter forventet +0,03. (2) Månedlig re-trening (#2891) er det eneste åpne løpet som stables. (3) En ren kontroll som 2022 bør kjøres for hver ny kandidat før den blir leder.

Gjenskap: `cd arbeid/oppgave_2894; ./alle.sh knn10 --knn 10; ./alle.sh bag5 --bag 5; python3 avmaal.py knn10; python3 avmaal.py bag5; python3 avmaal.py v2 ../c1_natt/v2`. Kontrollen ligger i `kontroll/` (fr_T, v2kK_T, logger).
