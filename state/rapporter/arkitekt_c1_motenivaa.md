# Case 1: møtenivå blir selskapsnivå på v3. Vanguards tidligere MOT gir F1 0,400 mot gulvet 0,383, men løftet er ikke signifikant (arkitekt, #1970)

## Kontrollpunkt: møtenivå er tomt på aktiv måler
KP: forventet at avvik kommer i klynger per møte (83 % i møter med 2+ avvik hos Vanguard, #1964).
Fikk på v3 (NBIM, bare say-on-pay): 3131 av 3134 treningsmøter har ett forslag, og bare 4 av 285 avvik ligger i flerforslagsmøter.
En totrinns modell med møtet først og forslaget etterpå er derfor matematisk det samme som en forslagsmodell på v3.
Mekanismen gjelder bare v2 (Vanguard, styrevalg, 22 positive), og der er utvalget for lite til å måle den.
Klyngen hos NBIM ligger i stedet **over tid per selskap**: 1373 av 1719 selskaper har 2 møter i train.

## Det som ble bygget: totrinns på selskapsnivå
- **Trinn 1:** P(selskapet får avvik), logistisk regresjon på
  - NBIMs egne tidligere MOT (finnes, siste var MOT, log antall møter)
  - Vanguards andel MOT på alle forslag hos samme cusip
- **Trinn 2:** terskel valgt ut-av-fold (5-fold) på 2025-radene i train, ikke på test (t = 0,17).
- **Tidsriktig:** alt er strengt før møtedatoen. Vanguard-stemmer brukes bare når N-PX-en var innsendt (offentlig) før møtet.
  Uten det filteret var F1 0,418, og det er lekkasje fordi Vanguard sender N-PX i august.
- **Kode:** `python3 -I arbeid/oppgave_1970/selskapsnivaa.py arbeid/hack/c1/data_v3 arbeid/oppgave_1970/votes_snap.csv UT.csv vgany ja`
  (stdlib, 3 s). `votes_snap.csv` er et øyeblikksbilde av `arbeid/hack/c1/data/votes.csv` fra 11:25.

## Tall (v3 test 2026, maaler.py kjørt selv, tavle #991)
| variant | P | R | F1 | PR-AUC |
|---|---|---|---|---|
| dommer-gulv (NBIM MOT før) | 0,348 | 0,426 | 0,383 | 0,328 |
| logit, bare NBIM-historikk | 0,440 | 0,341 | 0,384 | 0,264 |
| regel: NBIM-MOT før ELLER Vanguard-MOT på say-on-pay før | 0,333 | 0,442 | 0,380 | 0,205 |
| **logit, NBIM + Vanguard MOT-andel alle forslag (offentlig før møtet)** | 0,422 | 0,380 | **0,400** | **0,376** |
| samme uten offentlighetsfilter (LEKKER, ikke bruk) | 0,433 | 0,403 | 0,418 | 0,373 |

- **Ablasjon:** hele løftet kommer fra Vanguards MOT-andel på alle forslag (vekt 0,33).
  Vanguards egne say-on-pay-MOT har vekt ≈0 og gjør regelen dårligere.
  «Styret er straffet før av en annen forvalter» er altså signalet, ikke lønnsstemmen.
- **Parret bootstrap mot gulvet (1000 trekk):** F1 +0,017 med 95 % KI [−0,040; +0,072], og 72 % av trekkene er over null.
  AP +0,016 med KI [−0,054; +0,088]. **Ikke signifikant.** Det svarer til ca. 3 flere riktige saker av 129.
  Målerens PR-AUC (0,376 mot 0,328) ser større ut enn det er, fordi gulvet har mange like p-verdier.
  Med min AP uten like verdier er tallene 0,385 mot 0,369.
- **Terskelfølsomhet (bare til rapporten, ikke valgt på test):** t = 0,13 gir 0,415, t = 0,15 gir 0,403, t = 0,20 gir 0,392 og t = 0,25 gir 0,362. Kurven er flat rundt valgt punkt.
- **Val-sjekk:** på data_v3_val har trening bare 2024, altså uten NBIM-historikk. Der degenererer modellen (F1 0,166), så vi har ingen uavhengig val-replikasjon.
  Ut-av-fold-F1 på 2025 er 0,394, mot gulvet 0,361 på samme år.

## Anbefaling
- **Ikke en ny leder, men en byggekloss:** gi `vg_mot_andel_for` til smed2 som kjennetegn (et lgbm-kjennetegn per cusip og dato, offentlighetsfilteret er obligatorisk).
  Den gir bedre rangering for ruting til menneske (#1955) og kostet 0 i presisjon.
- **Til juryen (ærlig evaluering):** «avvik klynger i møter» gjelder Vanguards styrevalg, ikke NBIMs say-on-pay.
  Hos NBIM er klyngen selskapet over tid, og en annen forvalters offentlige historikk legger til lite og usikkert (+0,017 F1, KI krysser 0).
  Det er et godt eksempel på en mekanisme vi målte og ikke overselger.
- **Lukket:** møtenivå-totrinns på v3 (degenerert, 1 forslag per møte) og Vanguard say-on-pay-OR-regel (0,380, under gulvet).

## Trukket vinkel (#156)
Fra økologien: «arter som forsvinner fra flere habitater». Et selskap som får MOT fra flere uavhengige forvaltere er et sterkere signal enn ett.
Testet her med én ekstra forvalter (Vanguard), og det ga +0,017.
Når iShares-hentingen (`hent_ish.log`) er ferdig, er neste tall å teste antall forvaltere med tidligere MOT (0/1/2) som kjennetegn.
