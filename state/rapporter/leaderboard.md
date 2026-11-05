# Leaderboard (fase 0: adult v2, 5-fold SKF rs=42, ROC-AUC)

Kun rader med status **verifisert** teller. Dommerens score er fasit.

| Kandidat | Smedens score | Dommerens score | Status | Dato |
|---|---|---|---|---|
| (dommer) referanse_lr | n/a | 0.90528 | referanse, ikke kandidat | 2026-10-26 |
| lr_baseline | 0.90528 | 0.90528 | **verifisert** | 2026-10-26 |
| hgb_v1 | 0.92916 | 0.92916 | **verifisert** | 2026-10-26 |
| catboost_v1 | 0.93039 | 0.93039 | **verifisert** | 2026-10-26 |
| ens_v1 | 0.93092 | 0.93092 | **verifisert** | 2026-10-26 |
| ens_v2 | 0.93101 | 0.93101 | **verifisert** | 2026-10-26 |
| ens_v3 | 0.93081 | ikke kjørt | ikke meldt (under ens_v2, smedens eget tall) | 2026-10-26 |
| ens_v4 | 0.93144 | 0.93144 | **verifisert** | 2026-10-26 |
| ens_v4b | 0.93144 | ikke kjørt | samme som ens_v4, ren fartsendring. 1125 s under load | 2026-10-26 |
| ens_v4c | 0.93144 | 0.93144 | **verifisert**, 510 s. Ny standard-train.py. Gir ikke ny score (= ens_v4) | 2026-10-26 |
| b_ebm5x | 0.93153 | ikke reprodusert (ikke nødvendig) | **underkjent** (B: 0.93153 < 0.93159, 3/5 folder) | 2026-10-26 |
| b_cb_allcat | 0.93283 | 0.93283 | **verifisert**, ny offisiell. 5/5 folder > ens_v4. Reprodusert identisk | 2026-10-26 |
| ens_v5 | 0.93358 | 0.93358 | **verifisert**, ny offisiell. 5/5 folder > b_cb_allcat. Nested vekter. Reprodusert identisk, 1420 s | 2026-10-27 |
| cb_begge | 0.93371 | 0.93371 | **underkjent** (snitt 0.93371 < 0.93373, 4/5 folder > ens_v5). Reprodusert identisk, 1987 s | 2026-10-27 |
| ens_v6 | 0.93381 | 0.93381 | **verifisert**, ny offisiell. ens_v5 + cb_begge som 4. medlem. +0.00023 (krav B ≥ +0.00015 → 0.93373), 5/5 folder > ens_v5. Reprodusert identisk, 1301 s. Re-reprodusert bit-likt etter v5.1 (#157) | 2026-10-27 |
| ens_v7 (#79) | – | – | **ikke meldt**. Smedens port stoppet den: medlem cba lr0.025/2000 alene 0.93321 mot 0.93318 (+0.00003, 3/5). Kode lest, ren. Ikke reprodusert (ingen score hevdet) | 2026-10-27 |
| cbb_hp l2=10 (#87) | 0.93366 | – | **ikke meldt**. Port 2 feilet (krav ≥ 0.93396, fikk 0.93366 = lik cb_begge). Portene ikke flyttet (snapshot). Kode ren. Ingen ens_v7 | 2026-10-27 |
| cb_kryss (#82, speider) | 0.93309 (allcat_x) / 0.93360 (begge_x) | – | **ikke kandidat**. 4 tilstandsløse kryss gir −0.00009 mot cb_allcat 0.93318 og −0.00006/−0.00007 mot cb_begge (rs=42/rs=0). Under kravet +0.0003. Kode lest, ren. Ikke reprodusert (ingen gevinst hevdet) | 2026-10-27 |

Diagnostikk #65 (ikke offisielt): ens_v4c→ens_v5 Δ på fold-seed 0/1 = +0.00194/+0.00212 (10/10 folder). Gevinst ekte; nivået på rs=42 ~0.0003 optimistisk for begge. Se dommer_fold_robusthet.md.

## S6E10-syn (fase 1-generalprøve, ikke offisiell score)
| Kandidat | Smedens score | Dommerens score | Status | Dato |
|---|---|---|---|---|
| lgbm_te (#93) | 0.96008 | 0.96008 | **verifisert** (dommer_syn.md) | 2026-10-27 |
| realmlp (#100) | 0.96113 | 0.96113 | **verifisert**, bit-identisk, perm 0.50066/0.49854. 5/5 folder > lgbm_te (dommer_realmlp.md) | 2026-10-27 |
| lgbm_full1 (#114) | 0.96052 | 0.96052 | **verifisert**, bit-identisk per fold. TE nestet, orig-vern 0.01 %. +0.00018 mot route_fn_ocb (4/5), < realmlp (dommer_full1.md) | 2026-10-27 |
| mal v3 blend (#125: realmlp+lgbm_rfo_te3+lgbm_te, rank .55/.25/.20) | 0.96140 | 0.96140 | **verifisert**, bit-identisk per fold og sub-sha. sjekk_innsending OK. Vektene var faste fra #122 (dommer_mal_v3.md) | 2026-10-27 |

## Øvelse B: M4 Hourly 48 t (OWA, lavere er bedre, Naive2 = 1.000)
| Kandidat | Smedens score | Dommerens score | Status | Dato |
|---|---|---|---|---|
| prognose_smed (#208, 2× LightGBM snitt) | 0.426 (egen holdout) | 0.411 (sMAPE 8.527, MASE 0.857) | **verifisert**, fasit-sha lik fingeravtrykk, ingen lekkasjetegn (ovelse_b_dom.md) | 2026-10-27 |

## Hackathon-øvelse: Hash Code 2020 bokskanning (høyere er bedre, toppskår 27 203 691)
| Kandidat | Smedens score | Dommerens score | Status | Dato |
|---|---|---|---|---|
| hashcode_smed (#216) | 27 211 719 | 27 211 719 (a 21, b 5 822 900, c 5 690 888, d 5 109 000, e 5 240 662, f 5 348 248) | **verifisert**, egen teller, alle gyldige, 100,03 % av toppskår, 38 min (hashcode_dom.md) | 2026-10-27 |

## Pengeøvelse D: SWE-Lancer Diamond manager (høyere er bedre, maks $264 500)
| Kandidat | Smedens score | Dommerens score | Status | Dato |
|---|---|---|---|---|
| ovelse_d_smed (#235, 27 vurderere) | 161/265, $173 375 | 161/265, $173 375 (0.655) | **verifisert**, fasit byte-lik fra CSV, ingen Upwork-boks; forbehold: mulig minnelekkasje, øvre anslag (dommer_ovelse_d.md) | 2026-10-27 |

## Programmeringsøvelse: BAPC 2026 Prelims, ferskt sett (høyere er bedre, maks 13/13; ikke offisiell score)
| Kandidat | Smedens score | Dommerens score | Status | Dato |
|---|---|---|---|---|
| bapc_smed (#238, smed + 4 hjelpere) | 13/13, plass 1/167, 8,4 min | 13/13, 880/880 tester, faktor 1.0 | **verifisert**, ingen spor av testdata, $2.27 inkl. hjelpere (dommer_etter_maling.md) | 2026-10-27 |

## Hackathon-øvelse E: AHC071 Brick Cover, 150 skjulte filer (høyere er bedre, toppnivå ca. 1 590 000)
| Kandidat | Smedens score | Dommerens score | Status | Dato |
|---|---|---|---|---|
| lag A smed (#245) | ≈1,593 mill. (data/in ×1,5) | 1 590 574 / 1 590 473 / 1 590 574 | **verifisert**, 3/3 gyldige, plass ca. 1–25, offisiell 1.0003, 44 min, $2.85 (dommer_ovelse_e.md) | 2026-10-27 |
| lag B smed2 (#246) | 1 062 851 på data/in | TLE (2,04 s kaldstart) / 1 592 208 / 1 592 241 | **underkjent**, 2/3 gyldige: TLE i kjøring 1, ca. 0,1 % bedre varm, 57 min, $4.18 | 2026-10-27 |

## Hackathon-øvelse F: AHC073 Circles of Inversion, 150 skjulte filer (høyere er bedre, vinner ca. 1 187 850, anslag)
| Kandidat | Smedens score | Dommerens score | Status | Dato |
|---|---|---|---|---|
| lag B smed (#261) | 672 438 på data/in (100 filer) | 992 874 / 995 573 / 991 397 | **verifisert**, 3/3 gyldige, snitt 993 281, plass ca. 28, offisiell 0.8362, 39 min, $2.34 (dommer_ovelse_f.md) | 2026-10-27 |
| lag A smed2 (#260) | 429 592 på data/in (100 filer) | 607 263 / 609 842 / 616 018 | **verifisert**, ikke beste: 3/3 gyldige, snitt 611 041, plass ca. 141, 50 min, $4.56. Autolukket etter 1 økt (worker-feil) | 2026-10-27 |

## Penge-øvelse H: Code4rena K2-revisjon, pott $120 000 (fasit 18 H + 42 M)
| Kandidat | Smedens funn | Dommerens dom | Status | Dato |
|---|---|---|---|---|
| smed (#274) | 3 M | treff M-38 + M-24, 1 falskt (incentives snapshot==0), presisjon 0,67, 0/18 H | **verifisert**, ca. $119,51 (0,35 % av taket $34 006), offisiell 0.0035 (dommer_ovelse_h.md) | 2026-10-28 |

## Penge-øvelse I: velg vinnerforslag i 7 Expensify-oppdrag à $250 (tilfeldig 0,139, D 0,655)
| Kandidat | Svar | Dommerens dom | Status | Dato |
|---|---|---|---|---|
| smed (#277) | 7 valg + IC 98551 | 0/7 treff, $0/$1750; nest beste traff 3/7; logg ren; IC 98551 = HR-delen av PR (anslag) | **verifisert**, offisiell 0.0 (dommer_ovelse_i.md) | 2026-10-28 |

## Penge-øvelse I2: velg vinnerforslag i 23 nye, blinde Expensify-oppdrag à $250 (tilfeldig 0,082)
| Kandidat | Svar | Dommerens dom | Status | Dato |
|---|---|---|---|---|
| smed (#281) | 23 valg (+7 brente fra I) | 7/23 treff, $1750/$5750 = 0,304; tilfeldig $473; P(≥7 ved flaks) = 0,2 %; logg ren | **verifisert**, offisiell 0.304 (dommer_ovelse_i2.md) | 2026-10-28 |

## Penge-øvelse I3: velg vinnerforslag i 20 ferske Expensify-saker, tak $3825 (tilfeldig 0,313, «siste MelvinBot» 0,824)
| Kandidat | Svar | Dommerens dom | Status | Dato |
|---|---|---|---|---|
| smed (#290) | 20 valg, alle MelvinBot | 17/20 treff, $3150/$3825 = 0,824 (fersk 10/10, eldre 7/10); P(flaks) 4e-7; lik «siste MelvinBot»; logg ren | **verifisert**, offisiell 0.824 (dommer_ovelse_i3.md) | 2026-10-28 |

## Penge-øvelse I4: 20 Expensify-saker, 13 menneskevinnere, tak $4625 (tilfeldig 0,148, «siste MelvinBot» 0,314)

| Kandidat | Metode | Score | Status | Dato |
|---|---|---|---|---|
| smed (#295) | 7 hjelpere, 5 bot / 15 menneske | 15/20 treff, $3375/$4625 = 0,730 (menneske 10/13, bot 5/7, fersk 6/6); P(flaks) 5e-10; topp-2 18/20; 0,692 uten gråsonetreff 102046; logg ren | **verifisert** (dommer_ovelse_i4.md) | 2026-10-28 |

## Dusør-øvelse H3: BattleChain Confidence Pools (CodeHawks jul 2026), tak $1621 (H2: 0,555)
| Kandidat | Funn | Score | Status | Dato |
|---|---|---|---|---|
| smed (#299) | 2 M + 1 L, 12 av 120 min (autolukket) | M-03 + L-02 truffet, $292/$1621 = 0,180; presisjon 0,67; 1 falskt (setExpiry-frontrun); M-01 i hånda, men forkastet; logg ren | **verifisert, ikke bestått på tid** (dommer_ovelse_h3.md) | 2026-10-28 |
| smed (#303, del 2) | 3 M + 1 L, 27 min arbeid av 112 (73 min venting) | rå: M-01 + M-03 + L-02 = $1034/$1621 = 0,638; M-01 forurenset fordi dommerens score-linje avslørte det; ren 0,180; presisjon 0,75; logg ren | **verifisert, ren 0,180, mer tid ga ingen uavhengige funn** (dommer_ovelse_h3b.md) | 2026-10-28 |

## Hackathon-øvelse G: AHC072 over 4 timer og flere økter, 150 skjulte systemtester (mål 0,85, strekk 0,94)
| Kandidat | Kurve (andel per økt) | Score | Status | Dato |
|---|---|---|---|---|
| smed2 (#269) | 0,686 → 0,701 → 0,729 → 0,729 (økt 4 uendret) | andel 0,729 (3 kjøringer 0,727-0,731), plass ca. 242 av 1057, 150/150 gyldige, maks 1,72 s; 68 min tomgang før frist; logg ren | **verifisert, mål ikke nådd** (dommer_ovelse_g.md) | 2026-10-28 |

## Dataøvelse J: Kaggle S6E8 mobilavhengighet, ROC AUC på 30 % holdout (bestått ≥0,9654, godt ≥0,9695)
| Kandidat | CV | Holdout-AUC | Rang av 3531 | Status | Dato |
|---|---|---|---|---|---|
| speider-baseline CatBoost | – | 0,96202 | 2649 | referanse | 2026-10-28 |
| smed2 (#304) blanding lgbm+xgb+xgb_d8+cb | 0,96756 | 0,96827 | ca. 1085 (1035-1145) | **verifisert, bestått, ikke godt** (dommer_ovelse_j.md) | 2026-10-28 |

## Dusørøvelse K: Supadata Python-SDK, to dusører ($30 gateway-feil + $40 crawl), skjulte tester
| Kandidat | Betalt | Streng | Skjulte tester | Tid | Status | Dato |
|---|---|---|---|---|---|---|
| smed2 (#309) | $70 av $70 (1,000) | $70 | 22/22 | 1 min 50 s av 90 | **verifisert** (dommer_ovelse_k.md) | 2026-10-28 |

## Hackathon-øvelse L: AHC073 Circles of Inversion, 3 timer, 150 skjulte filer (godkjent 6500, godt 6950, strekk 7700 snitt)

| Kandidat | Kurve (skjult) | Dommerens score | Status | Dato |
|---|---|---|---|---|
| smed2 (#316) v15 | v10 6980 → v15 7035 per fil | 0,902 (sum 1 055 315 / 1 169 688, 3 kjøringer 1 055 155-1 055 539), plass ca. 15 av 386, 150/150 gyldige, maks 1,61 s; 0 min valgt tomgang, ca. 40 min tapt til omstart 06:13; logg ren | **verifisert, godt nådd** (dommer_ovelse_l.md) | 2026-10-28 |

## Breddeøvelse 1: tre ekte feil i pallets/click (#347, dømt i #348)

| Kandidat | Feil A / B / C (streng) | Dommerens score | Status | Dato |
|---|---|---|---|---|
| smed (#347) | 3/3 · 0/10 · 3/5, 0 regresjoner | atferd 0,917 (A 1,0 · B 1,0 · C 0,75), streng 0,533; alle tre løst på 4 min, 7 min totalt av 120; logg ren | **verifisert** (dommer_bredde_1.md) | 2026-10-28 |

## Breddeøvelse 2: seks CTF-kryptooppgaver, ECSC 2026 (#350, dømt i #351)

| Kandidat | Flagg (sjekker) | Dommerens score | Status | Dato |
|---|---|---|---|---|
| smed2 (#350) | 5/5 automatiske JA (7/7 vekt) + ECDSA 0,5/2 for hånd | 7,5/9 = 0,833; 5 flagg på ca. 1,5 min, 5,3 min totalt av 120; ga opp ECDSA etter 2 min; LOGG.md-tidene er diktet (oppgir 40 min) | **verifisert** (dommer_bredde_2.md) | 2026-10-28 |

## Breddeøvelse 4: `--code` i sqlite-utils, issue #684 (#353, dømt i #354)

| Kandidat | Skjulte tester | Dommerens score | Status | Dato |
|---|---|---|---|---|
| smed2 (#353) | atferd 11/12, streng 7/12, 0 regresjoner | 0,917 (streng 0,583); 8,6 min av 90, 56/60 trekk; LOGG-tidene stemmer | **verifisert** (dommer_bredde_4.md) | 2026-10-28 |

## Breddeøvelse 5: booking-API for badstue (#361, dømt i #362)

| Kandidat | Skjulte prøver | Dommerens score | Status | Dato |
|---|---|---|---|---|
| smed2 (#361) | 30/30 grønne | 1,000; 5 min av 90, 1 økt (24/60 trekk), lukket tidlig med god grunn; ingen lekkasje; LOGG-tidene stemmer | **verifisert** (dommer_bredde_5.md) | 2026-10-28 |

## Breddeøvelse 6: programmeringskonkurranse «Fjordrunden» (#364, dømt i #366)

| Kandidat | Skjulte tester | Dommerens score | Status | Dato |
|---|---|---|---|---|
| smed2 (#364) | 60/60 (12/12 på A–E) | 1,000; 6,4 min av 120, 1 økt (12/60 trekk), maks 0,30 s per test; ingen lekkasje | **verifisert** (dommer_bredde_6.md) | 2026-10-28 |

## Breddeøvelse 3: strømpriser time for time, oktober 2026 (#357, dømt i #358)

| Kandidat | Ferdighet mot naiv i går (01.–27.10) | Dommerens score | Status | Dato |
|---|---|---|---|---|
| speider, blanding (referanse) | +0,068 (MAE 0,1966) | 0,500 (per definisjon) | referanse | 2026-10-28 |
| smed (#357) | +0,238 (MAE 0,1607), +0,183 mot blanding, 0 dager feil | 0,967; 51,9 min av 120, 39/60 trekk | **verifisert** (dommer_bredde_3.md) | 2026-10-28 |

## Breddeøvelse 7: kundeklage på kasseprogrammet (#368, dømt i #369)

| Kandidat | Skjulte prøver (maal.py) | Dommerens score | Status | Dato |
|---|---|---|---|---|
| urørt materiale | 0/3 feil | 0,000 | kalibrering | 2026-10-28 |
| speider, referanse | 3/3 feil | 1,000 | kalibrering | 2026-10-28 |
| smed2 (#368) | 13/13 grønne, alle tre feil, ytelse 0,75 s | 1,000; ca. 10 min av 60, 1 økt (43 trekk); ingen lekkasje; LOGG-tidene stemmer | **verifisert** (dommer_bredde_7.md) | 2026-10-28 |

## Breddeøvelse 8: rotete fakturaer til regneark (#372, dømt i #373)

| Kandidat | maal.py (A oktober, B skjult september) | Dommerens score | Status | Dato |
|---|---|---|---|---|
| smed2 (#372) | A 1,0 (69/69 rader, 12/12 felt, 0 oppdiktede celler), B 1,0 | 1,000; 7,9 min av 90, 1 økt (29/60 trekk); ingen lekkasje, ingen nett; LOGG-tidene stemmer | **verifisert** (dommer_bredde_8.md) | 2026-10-28 |

## Kaggle VQCC invsqrt (#377, dømt i #379). Faktor = 2 076 774 / (Q·(Toffoli+T/4)), lokal verifikator, 64 skudd × alle x

| Kandidat | Smedens faktor | Dommerens faktor | Status | Dato |
|---|---|---|---|---|
| referanse | 1,0 | 1,000 | kalibrering | 2026-10-28 |
| b0_a1 (offentlig, somfieao) | 3,694 | 3,694 (ε-regel treffer 10 siffer) | kalibrering | 2026-10-28 |
| smed2 beste_invsqrt.kmb (Q 122, 1732 Toffoli) | 8,614 | 8,614 (8,578 med speiderens regel); totalt 2,050 | **verifisert** (dommer_qc_invsqrt.md) | 2026-10-28 |
| smed2 beste_invsqrt_v2.kmb (#384, Q 122, 1664 Toffoli, dyadisk D104) | 8,93 | 8,932 (8,875 med speiderens regel); totalt 2,075 | **verifisert** (dommer_qc_invsqrt_v2.md, #388) | 2026-10-28 |

## Kaggle VQCC dqi (#389, dømt i #392). Score = R(ε⁺)·Q²·T, faktor = 2,444e13 / score, lokal verifikator, felt 4179, Kaggle-maske, 102 400 skudd
| Kandidat | Smedens score | Dommerens score | Status | Dato |
|---|---|---|---|---|
| smed k4179.kmb (port av Gu et al., Q 1837, T 444 030) | 13,34 (8 fasefeil) | 13,30 (9 fasefeil, frø 392392392); totalt (8,932·13,303)^(1/3) = 4,916 | **verifisert** (dommer_qc_dqi.md) | 2026-10-28 |
| smed2 k4179_v3.kmb (#393, Q 1819, T 443 862) | 13,61 (snitt 2 frø, 7 og 9 fasefeil) | 13,80 rått (3 fasefeil, frø 398398398), 13,57 med R som i #392; totalt (8,932·13,572)^(1/3) = 4,949 | **verifisert** (dommer_qc_dqi_v3.md) | 2026-10-28 |
| offentlig dqi.kmb (Ozer v8 via mrmeows, Apache-2.0, sha 569863ae…, Q 883, T 519 152) #412/#414 | 49,77 og 49,63 (smed2, 2 frø) | 50,26 rått (2 verdifeil, frø 414414414), 49,37 med R 1,2230 (mrmeows offisielle); totalt (8,932·49,37)^(1/3) = 7,611 | **verifisert**, lånt krets (dommer_qc_dqi_883.md) | 2026-10-28 |
| offentlig dfthcsos/ C59 (mrmeows v8 på Rustads R10, Apache-2.0, npz 8229861b…, Q 423, T 19 337) #417 | 8,612 (smed #410, 3 salt) | 8,612 (PASS 87 424 skudd, salt dommer417, 20 filer bit-like kilden); totalt (8,932·49,37·8,612)^(1/3) = 15,602 | **verifisert**, lånt (dommer_qc_innsending.md) | 2026-10-28 |
| dfthcsos/ kand_helio_g40 (heliosli/SomeJoint R8 B143 C60, Apache 2.0, lånt, + smedens gauge av W/H2_I; Q 430, T 16 306) #411 | 9,8605 (smed #410, 3 salt) | 9,8605 (PASS 78 080 skudd, salt dommer411, T og Q telt selv, 15 kretser bit-like heliosli); totalt (8,932·49,37·9,8605)^(1/3) = 16,322; submission.zip 6272a1fc… bygd | **verifisert**, lånt + egen gauge (dommer_qc_femoco.md) | 2026-10-28 |
| invsqrt busyaprime 07314803 (mrmeows 63q + 172-AND-oppslag, Apache 2.0, lånt; Q 63, 1334,5 Toffoli) #418/#419 | 20,2288 (smed2, 64 skudd) | 20,2288 (PASS 200 540 928 skudd, verste 0,9993 tol ved x=161, Q og Toffoli telt selv); totalt (20,2288·49,37·9,8605)^(1/3) = 21,434 | **verifisert**, lånt (dommer_qc_invsqrt_v3.md) | 2026-10-28 |
| dqi heliosli 4ee7a17b (SomeJoint fused DQI, smalnet, Apache-2.0, lånt; Q 889, T 440 564) #420/#421 | 58,92 (smed3, frø 420420420, 0 feil) | 58,9213 (PASS 102 400 skudd, 0/0/0 feil, frø 421421421, Q og Toffoli telt selv); totalt (20,2288·58,9213·9,8605)^(1/3) = 22,736 | **verifisert**, lånt (dommer_qc_dqi_889.md) | 2026-10-28 |
| dfthcsos/ kand_lk4 (smed2 #426: g40 + refit av W/H2_I med faste ord; Q 430, T 16 306) #428 | 9,8676 (smed2, 3 salt) | 9,8676 (PASS 78 080 skudd, salt dommer428, λ_eff 48,50024, error_2 19,99975 mHa, T og Q telt selv, kretser og ord bit-like g40); totalt (20,2288·58,9213·9,8676)^(1/3) = 22,741 | **verifisert**, lånt + egen refit (dommer_qc_femoco_lambda.md) | 2026-10-28 |
| dqi somejoint 897q 53d8b2ed (team-1028-stream, notatbok 29.10, Apache 2.0, lånt; Q 897, T 430 822,8, R 1,1913) #487 | 59,1836 (somejoint, standardfrø) | 59,1836 (offisiell verifikator PASS 102 400 skudd, 0/0 feil, frø 487487487; speiderens verifikator frø 417417417 også 59,1836; bygd selv, SHA lik notatboka, Q og T telt selv); totalt (20,2288·59,1836·9,8676)^(1/3) = 22,775 | **verifisert**, lånt (dommer_487_somejoint_dqi.md) | 2026-10-29 |
| dqi somejoint 897q + heliosli pole-kjede 889q 7bb65d4f (smed2-port #488, begge Apache 2.0, lånt; Q 889, T 431 137,9, R 1,1913) #493 | 60,21 (smed2, salt smed2_488d/e) | 60,2095 (offisiell verifikator PASS 102 400 skudd, 0/0 feil, salt dommer493; bygd selv, SHA lik, Q og T telt selv); totalt (20,2288·60,2095·9,8676)^(1/3) = 22,906 | **verifisert**, lånt + port (dommer_493_dqi_889_somejoint_helio.md) | 2026-10-29 |
| invsqrt busyaprime 9a8627c8 (33-qcc-v8-members: mrmeows 63q, oppslag + vindu S1 omsyntetisert, Apache 2.0, lånt; Q 63, 1329,5 Toffoli) #495/#496 | 20,2911 (smed, salt smed495) | 20,2911 (offisiell verifikator PASS 200 540 928 skudd, salt dommer496, verste 0,9993 tol ved x=161; lastet ned selv, SHA lik); totalt (20,2911·60,2095·9,8676)^(1/3) = 22,9295 | **verifisert**, lånt (dommer_496_invsqrt_busyaprime.md) | 2026-10-29 |
| invsqrt S3 42 AND 462b3f8a (busyaprime 9a8627c8 + smeds S3-omsyntese 43->42 AND, rang-18-former; Q 63, 1328,5 Toffoli) #508/#509 | 20,3036 (smed, salt smed508a/b/c) | 20,3036 (offisiell verifikator PASS 200 540 928 skudd x3, salt dommer509a/b/c, verste 0,9993 tol ved x=161 arvet; bygd selv, SHA lik); totalt (20,3036·60,3770·9,8676)^(1/3) = 22,9554 | **verifisert**, lånt + egen del (dommer_509_s3_42.md) | 2026-10-29 |
| invsqrt S4 15 AND fb56b320 (9a8627c8 + S3 42 AND + smed2s S4-omsyntese 16->15 AND, bilineær løser; Q 63, 1327,5 Toffoli) #512/#513 | 20,3161 (smed2, salt smed512a/b/c) | 20,3161 (offisiell verifikator PASS 200 540 928 skudd x3, salt dommer513a/b/c, verste 0,9993 tol ved x=161 arvet; bygd selv, SHA lik); totalt (20,3161·60,3770·9,8676)^(1/3) = 22,9601 | **verifisert**, lånt + egne deler (dommer_513_s4_15.md); venter på Kaggle 30.10 (#518) | 2026-10-29 |

## Kaggle VQCC: ekte innsendinger (offentlig tavle, høyere er bedre)
| Tid UTC | Ref | Pakke (zip sha8) | Lokal forventning | Kaggle public | Avvik | Plass | Status |
|---|---|---|---|---|---|---|---|
| 2026-10-28 18:31 | 57745852 | invsqrt #419 + dqi #421 + dfthcsos #428 (033003b7) | 22,74144 | **22,74142** | −0,0001 % | 46 av 200+ (topp 26,141) | **verifisert av Kaggle** (#437) |
| 2026-10-29 00:59 | 57753979 | invsqrt #419 + dqi #487 + dfthcsos #428 (6f7d16af) | 22,77514 | **22,77511** | −0,0001 % | 70 av 1479 (topp 10: 23,99) | **verifisert av Kaggle** (#487) |
| 2026-10-29 01:46 | 57755074 | invsqrt #419 + dqi #493 + dfthcsos #428 (38bf63be) | 22,90599 | **22,90596** | −0,0001 % | 56 av 1479 (topp 1: 26,14, topp 10: 24,02) | **verifisert av Kaggle** (#493) |
| 2026-10-29 02:27 | 57755912 | invsqrt #496 + dqi #493 + dfthcsos #428 (129f9c9a) | 22,92945 | **22,92944** | −0,0000 % | – | **verifisert av Kaggle** (#496) |
| 2026-10-29 03:07 | 57756828 | invsqrt #496 + dqi G=4 #502 + dfthcsos #428 (d7798e5e) | 22,9507 | **22,95068** | −0,0001 % | – | **verifisert av Kaggle** (#502) |
| 2026-10-29 05:06 | 57759481 | invsqrt #509 + dqi G=4 #502 + dfthcsos #428 (55e42972) | 22,9554 | **22,95539** | −0,0001 % | – | **verifisert av Kaggle** (#509) |
| 2026-10-30 01:52 | 57788927 | invsqrt 7af23dfc + dqi fold 3c2b9329 #653 + dfthcsos pk_b #589 (62648c57) | 23,0145 | **23,01450** | 0,0000 % | – | **verifisert av Kaggle** (#653) |
| invsqrt S1 3 + S4 14 AND 7af23dfc (9a8627c8 + S3 42 + S1 delvindu 5->3 #514 + S4 16->14 #516, flettet #519; Q 63, 1324,5 Toffoli) #519/#520 | 20,3537 (smed, salt smed519a) | 20,3537 (offisiell verifikator PASS 200 540 928 skudd x3, salt dommer520a/b/c, spenn 20,353699-20,353709, verste 0,9993 tol ved x=161 arvet; bygd selv, SHA lik); totalt (20,3537·60,3770·9,8676)^(1/3) = 22,9743 | **verifisert**, lånt + egne deler (dommer_520_s1s4.md); pakket, sendes av #518 30.10 | 2026-10-29 |
| kjemi 16 272 Toffoli d9a81022 (lk4-ord/W smed2 + heliosli v16 k=5,7,9,11,13 + heliosli eb9b9c2e lastere k=0,1,4,6,8,10,12; speider #539) #562 | 22,9903 (speider, salt '' og speider539b) | 22,9903 (offisiell verifikator PASS 78 080 skudd x3, salt dommer562a/b/c, kost 339 354 219,9, error_2 19,99975 mHa, faktor 9,88819) | **verifisert**, pakket zip 612d5701, erstattet av #565 | 2026-10-29 |
| kjemi 16 270 Toffoli 7b1d57a4 (som #562 + Gluzdov v38 angle_k_2; speider #564) #565 | 22,9912 (speider, salt '' og speider564b) | 22,9912 (offisiell verifikator PASS 78 080 skudd x3, salt dommer565a/b/c, kost 339 312 509,7, error_2 19,99975 mHa, faktor 9,88941) | **verifisert**, pakket zip 9d485d8e, sendes av #523 | 2026-10-29 |
| kjemi 16 266 Toffoli db3cf368 (Özer v14 på Atakans ord + Gluzdov v41 angle_k_3/k_14; speider #567) #584 | 22,9969 (speider, salt '' og speider567b) | 22,9969 (offisiell verifikator PASS 78 080 skudd x3, salt dommer584a/b/c, kost 339 062 509,3, error_2 19,99925 mHa, faktor 9,89670) | **verifisert**, pakket zip ed26e265, sendes av #523 | 2026-10-29 |
| DQI fold 3c2b9329 (209f8551 + odde steg forover foldet til ett Vandermonde-pass, −927 utført T; smed2 #648) + invsqrt 7af23dfc + kjemi pk_b #653 | 23,0145 (smed, 6 salt PASS) | 23,0145 (offisiell verifikator PASS 102 400 skudd x3, salt dommer653a/b/c, T 429 015,1, faktor 60,5075; c 1 fasefeil arvet fra 209f8551, samme skudd 91941) | **verifisert**, zip 62648c57, sendt ref 57788927 | 2026-10-30 |
| kjemi y2g (heliosli v39_ack14-vekter refit på pk_b-ordene, smed2 #661; kretser = generator_kjemi/pk_b) + DQI fold 3c2b9329 + invsqrt 7af23dfc #666 | 23,0353 (smed2, 3 salt PASS) | 23,0353 (offisiell verifikator PASS x3, salt dommer666a/b/c, kost 338 098 207,1, faktor 9,92493) | **verifisert**, zip 6e6d5adc, sendt ref 57790269, Kaggle 23,03526 | 2026-10-30 |
| invsqrt 7d91de8e (smed4 #675: CSWAP-par i aritmetikk b -> mux, -1 Toffoli) + DQI fold 3c2b9329 + kjemi y2g #686 | 23,0400 (smed4, 3 salt PASS) | 23,0400 (offisiell verifikator PASS x3, salt dommer686a/b/c, 1323,5 Toffoli, verste 0,99932 tol, faktor 20,36627) | **verifisert**, zip 49322e9b, sendt ref 57791896, Kaggle 23,04001 | 2026-10-30 |
| invsqrt 99ca73a1 (smed2 #689: lz-kjedeledd foldet inn i g-fasen, -0,5 Toffoli) + DQI fold 3c2b9329 + kjemi y2g #695 | 23,0424 (smed2, 3 salt PASS) | 23,0424 (offisiell verifikator PASS x3, salt dommer695a/b/c, 1323,0 Toffoli, verste 0,99932 tol, faktor 20,37256) | **verifisert**, zip 12b3a578 KLAR, ikke sendt (går med y44 i #700) | 2026-10-30 |
| kjemi y44 (smed2 #697: Gluzdov v44-vekter + våre ord, 2x refit) + invsqrt lz 99ca73a1 + DQI fold 3c2b9329 #700 | 23,0407 med 7d91de8e (smed2, 3 salt PASS) | 23,0430 (offisiell verifikator PASS x3, salt dommer700a/b/c, λ_eff 48,334372, kost 338 068 965,8, faktor 9,92579) | **verifisert**, zip 09142e43, sendt ref 57793871, Kaggle 23,04305 (avvik 0,0000) | 2026-10-30 |
| invsqrt p3 33546c04 (62q: yoyobar a568bc79 + våre S3/S4/S1, smed4 #707, smed2 #713) + DQI fold 3c2b9329 + kjemi y44 #714 | ca. 23,138 (smed2, lokal PASS) | 23,1378 (offisiell verifikator PASS x3, salt dommer714a/b/c, Q 62, 1327,48 Toffoli, kost 100 692,5, faktor 20,62490) | **verifisert**, zip 43b6bd41 KLAR, ikke sendt (kvote brukt, #715) | 2026-10-30 |
| A2: invsqrt p3 33546c04 + DQI fold 3c2b9329 + kjemi gr1 (smed2 #721: y44 + 7 runder nulling/refit) #727 | ca. 23,1381 (smed2, lokal PASS) | 23,1381 (offisiell kjemiverifikator PASS x3, salt dommer727a/b/c, λ_eff 48,332536, e1 19,99782/e2 19,99980 mHa, kost 338 056 123,5, faktor 9,92617) | **verifisert**, zip 5aae7b31 KLAR, ikke sendt (erstatter 43b6bd41 i #715) | 2026-10-30 |
| kjemi t1655 (smed2 #728: gr1 + haletrekk k5 j3 bit0 via 2 CX, refit+nulling) #733 | 338 054 440,7 (smed2, PASS x3) | kost 338 054 440,7, λ_eff 48,332295, faktor 9,92622 (offisiell verifikator PASS x3, salt dommer733k1/k2/k3; kretsdiff sjekket) | **verifisert** (refit ikke gjenskapt) | 2026-10-30 |
| B2: invsqrt p3 33546c04 + DQI-tvilling 31c2ea8f + kjemi t1655 #733 | ca. 23,1378 (B fra smed3 #726 med y44) | 23,1381 (23,13813 uten DQI-feilskudd; ca. 23,10 med ett) | **verifisert**, zip 7c387913 KLAR, ikke sendt (sendes i #715) | 2026-10-30 |
| C: invsqrt p4_172 a122551d (−1 AND i oppslaget, arkitekt #754/smed2 #753) + DQI-tvilling 31c2ea8f + kjemi t1655 #755 | 23,1429 (arkitekt) | 23,1429 (23,14288 uten DQI-feilskudd) | **verifisert**, zip 6710f61b KLAR i oppgave_755/ut, ikke sendt (sendes i #715) | 2026-10-30 |
| D: invsqrt p8 52265be1 (alle fem oppslagsblokker −1 AND, arkitekt #754/smed2 #753) + DQI-tvilling 31c2ea8f + kjemi t1655 #760 | 23,1619 (arkitekt) | 23,1619 (23,16192 uten DQI-feilskudd) | **verifisert**, zip f09fe684 KLAR i oppgave_760/ut, ikke sendt (går først i #715) | 2026-10-30 |
| E: invsqrt p8 52265be1 + DQI inv18-tvilling 948e2781 (smed3 #765) + kjemi v44h 60490bef (smed #768) #773 | 23,1656 (DQI) / ca. 23,1664 (kjemi) | 23,1701 (23,17008 uten DQI-feilskudd) | **verifisert**, zip 61462786 KLAR i oppgave_773/ut, ikke sendt (går i #715 foran D) | 2026-10-30 |
| F2: invsqrt p10 0b6edfcb (smed2 #770) + DQI e4ffac63 (smed3 #777) + kjemi v44h 60490bef #780 | 23,1959 (smed-anslag) | 23,19588 (F1 uten p10: 23,17198) | **verifisert**, zip dd9a293b KLAR i oppgave_780/ut (F1 5182503d i ut_f1), ikke sendt (går i #715 foran E) | 2026-10-30 |
| G: invsqrt p10 0b6edfcb + DQI 7501a672 (smed3 #782, inv17) + kjemi v44h 60490bef #789 | ca. 23,197 (smed-anslag +0,0013) | 23,19717 | **verifisert**, zip 151f89f2 KLAR i oppgave_789/ut, ikke sendt (går i #715 foran F2); arkitektens p9 (#783) er samme q50-lapp som i p10, ingen ekstra gevinst | 2026-10-30 |
| H: invsqrt p10 0b6edfcb + DQI 6505c402 (smed4 #790, inv17c = inv17b + pq17, −106 T) + kjemi v44h 60490bef #793 | ca. 23,198 (smed-anslag) | 23,19778 | **verifisert**, byte-lik fra ren kopi, 3 salt 0/0 feil, zip 60868477 KLAR i oppgave_793/ut, ikke sendt (går i #715 foran G) | 2026-10-30 |
| I: invsqrt p10 0b6edfcb + DQI 82102e6b (smed3 #794 delt F·c + smed4 #795 fase6 4 AND, −416 utført T) + kjemi v44h 60490bef #799 | ca. 23,205 (smed-anslag) | 23,20530 | **verifisert**, byte-lik fra ren kopi, 3 salt PASS (c: 1 verdifeil arvet fra H, samme input 64/64), zip 5e24b7c7 KLAR i oppgave_799/ut, ikke sendt (går i #715 foran H) | 2026-10-30 |
| J: invsqrt p10 0b6edfcb + DQI 5b5e4876 (I + smed #798 np798, neste uten z/clear_flag, −143 utført T) + kjemi v44h 60490bef #805 | ca. 23,208 (smed-anslag) | 23,20788 | **verifisert**, byte-lik fra ren kopi, salt dommer805a/b/c PASS 0 verdifeil 0 fasefeil, faktor 60,6452, zip d69aa7b0 KLAR i oppgave_805/ut, ikke sendt (går i #715 foran I) | 2026-10-30 |
| K: invsqrt p10 0b6edfcb + DQI 932ada6b (J + q801 smed2 #807 + lp808 smed4 #808, −160 utført T) + kjemi v44h 60490bef #810 | ca. 23,211 (smed4 #809) | 23,21078 | **verifisert**, byte-lik fra ren kopi, salt dommerKa/b/c PASS 0 verdifeil 0 fasefeil, faktor 60,6679 (same-salt mot J 1,000374), zip 6e7b69fd KLAR i oppgave_810/ut, ikke sendt (går i #715 foran J) | 2026-10-30 |

## Kaggle VQCC: tavla 2026-10-29 07:00 UTC (#423, speider)
Topp 1 26,141 (Breaking1800) · topp 3 25,341 · topp 6 24,744 · topp 10 24,081 · topp 20 23,604 · topp 50 22,986 · topp 100 22,849 · 1506 lag. Vi (Martinaka) 22,95539 = plass 56. 22,9743 gir ca. plass 51-52; topp 50 krever 22,986. Topp 3 har steget fra 24,89 til 25,34 siden 00:39 UTC. Nye offentlige kretser: ingen slår våre deler (se speider_423_tavle.md).
| S6E11 #1432 sub_blend_add (LGBM+additiv LR) | CV 0,94710 / offentlig 0,94753 | verifisert, sendt ref 57942865 | 2026-11-03 |
| S6E11 #1441 sub_nl3_fro3 (LGBM 3 blader mb1023, 3 frø) | CV 0,94827 / offentlig 0,94837 | verifisert, sendt ref 57945334 | 2026-11-03 |

## Øvelsesbank 17: arXiv-kategori, makro-F1 (#1450, dømt i #1456, 03.11)
| kandidat | score | status |
|---|---|---|
| smed2 stabel tfidf/bge + Haiku-naboer på usikre (state/levering/mini_1450/svar.csv, sha 6c7d17d9) | 0,912404 | verifisert, offisielt |
| smed Haiku-bunter ×2 + SVM + Opus på uenige/usikre (#1506, arbeid/smed_1506/BESTE_svar.csv) | 0,917468 | verifisert, ny offisiell; kald omkjøring #1508 i arbeid/dom1508_kald17: 0,919247 for 2,89 USD |

## Øvelsesbank 08: RAG arXiv, MRR@10 (#1503, dømt i #1504, 03.11)
| kandidat | score | status |
|---|---|---|
| smed2 z BM25+bge-l+bge-b + Sonnet-rerangering av 21 usikre (state/levering/mini08/SISTE/llmsonnet.jsonl) | 1,000000 | verifisert (kald omkjøring 1,000000) |

## Øvelsesbank 09: SQL-agent, andel riktige (#1502, dømt i #1504, 03.11)
| kandidat | score | status |
|---|---|---|
| smed agent.py med dataprofil, Haiku 5.5 (state/levering/hack/SISTE/svar_h.json) | 1,000 (31/31) | verifisert (kald omkjøring 31/31, 0,17 USD, 20 s) |

## Øvelsesbank 11: dashboard Chicago 311, andel sjekker (#1505, dømt i #1508, 03.11)
| kandidat | score | status |
|---|---|---|
| smed2 app.py uten pakker (arbeid/smed2_mini11) | 1,000000 | verifisert (kald kopi på samme mappenivå 12/12, oppstart 1,9 s); 0/12 hvis mappa flyttes dypere (relativ datasti) |

## Øvelsesbank 01: Chicago 311 lukket innen 3 d, AUC (#1511, dømt i #1515, 03.11)
| kandidat | score | status |
|---|---|---|
| speider e3 lgbm + kø/gjentak (arbeid/oppgave_1511) | 0,978828 | verifisert (kald, bit-likt); fram-features gir 0 gevinst, bare fortid 0,978877; tåler ikke flytting |
| grunnlinje mal.py --rask | 0,9720 | selvrapportert |

## Øvelsesbank 10: taxi-API, andel sjekker (#1510, dømt i #1515, 03.11)
| kandidat | score | status |
|---|---|---|
| smed2 stdlib-app (arbeid/smed2_mini10/app) | 1,000000 | verifisert (11/11, oppstart 1,4 s); 0/11 i dypere mappe uten DATA |

## Øvelsesbank 02: NYC 311 svartid, RMSE (#1509, dømt i #1519, 03.11)
| kandidat | score | status |
|---|---|---|
| smed lgbm 255 blader + arbeidsdag, 10 frø (arbeid/oppgave_1509) | 0,853400 | verifisert (kald, bit-likt); uten framtidsfeatures bedre (ett frø 0,8538 mot 0,8558); tåler ikke flytting |
| grunnlinje median etat/type/beskrivelse | 0,9730 | selvrapportert |

## Øvelsesbank 04: Chicago taxi-tips, RMSE (#1513, dømt i #1519, 03.11)
| kandidat | score | status |
|---|---|---|
| smed2 m4+c5 hurdle 50/50, kald oppskrift | 2,493273 | verifisert (kald); c5 alene 2,493126 bit-likt |
| smed2 svar_final.csv (levert) | 2,496055 | verifisert (måler på fil) |
| g0 pris × tipsandel | 3,627 | selvrapportert |

## Øvelsesbank 18: forskrift-agent, andel riktige (#1514, dømt i #1519, 03.11)
| kandidat | score | status |
|---|---|---|
| smed planer + deterministisk utfører (arbeid/oppgave_1514/agent.py) | 16/16 offentlig, **23/23 skjult** | verifisert (2 kjøringer av skjult del, like svar); tåler flytting |

## Øvelsesbank 19: LLM-uttrekk Federal Register, andel riktige felt (#1520/#1521, dømt i #1523, 03.11)
| kandidat | offentlig | skjult | status |
|---|---|---|---|
| smed regler (arbeid/oppgave_1521/losning) | 0,990566 | **0,981579** | verifisert, 0 USD |
| smed2 Haiku+regler+Sonnet (arbeid/oppgave_1520/losning) | 0,981132 | **0,971053** | verifisert, 0,00273 USD/dok |

## Øvelsesbank 20: SF brannvesen responstid, MAE (#1518, dømt i #1523, 03.11)
| kandidat | offentlig | skjult | status |
|---|---|---|---|
| speider 0,7 CatBoost + 0,3 LGBM (arbeid/oppgave_1518/svar_beste.csv) | 3,284686 | **3,349908** | verifisert, kald kjøring bit-lik |
| grunnlinje median call_type × unit_type | 4,195018 | 4,324907 | referanse |

## Kaggle Name that LLM: ekte innsendinger (offentlig tavle 40 %, balansert treffsikkerhet, #1496)
| kandidat | måler (skjev ungarsk) | Kaggle offentlig | status | dato |
|---|---|---|---|---|
| kjede #1474 (ntl-landsby-sub v1, ref 57953507) | 0,5705 | **0,342** | COMPLETE, ekte tall; måleren overvurderer med 0,23 | 2026-11-03 |
| rå trekk + argmax #1546 (ntl-landsby-sub-raa v1, ref 57959747) | 0,519 (sim «én rad per prompt» 0,526) | **0,472** | COMPLETE, ekte tall, beste NTL hittil; +0,13 over kjeden | 2026-11-03 |
| rå + ungarsk uten glob #1546 (ntl-landsby-sub-raa-ung v1, ref 57959781) | 0,612 (sim «én rad» 0,495) | **0,458** | COMPLETE, ekte tall; under raa, testen har få rader per prompt | 2026-11-04 |
| raav vekter+skift #1616 (ntl-landsby-sub-raav v1, ref 57968009) | sim nestet 0,527 | **0,487** | COMPLETE, ekte tall, beste NTL hittil; +0,015 over raa, som simulatoren sa (+0,017) | 2026-11-04 |
Tavla 03.11 21:00: topp 1 0,747, topp 20 ca. 0,694.

## Generalprøve-hack 04.11 (MAE, lavere er bedre)
| Kandidat | Holdout | Offentlig | Status | Dato |
|---|---|---|---|---|
| r4_pmed (levert, sha 137b953d) | 3,6926 | 3,3654 | verifisert fra kald start (FULL=1, bit-lik) | 2026-11-04 09:55 |
| like4+pmed | 3,6972 | 3,3735 | verifisert fra kald start (bit-lik) | 2026-11-04 09:34 |
| #528 (smed3 #485) r4 0,8 + form4 0,2 | 3,6910 | 3,3558 | verifisert fra kald start (bit-lik) | 2026-11-04 10:00 |
| #529 (smed3 #486) r4 0,8 + v7 0,2 | 3,6929 | 3,3740 | verifisert fra kald start (bit-lik) | 2026-11-04 10:00 |

## Øvelser 49-53, dom #1814 (04.11 kveld, privat, kald start, dom_ovelser_0411d.md)
| Øvelse | Kandidat | Privat | Status |
|---|---|---|---|
| 49 | speider #1800 / smed3 #1807 | 0,1752 / 0,1752 | verifisert, byte-lik; slår ikke smed2 0,1624 |
| 50 | smed #1797 v5 | 0,6737 | verifisert, byte-lik, ny beste |
| 51 | smed2 #1799 v4 | 0,9808 | verifisert, byte-lik, ny beste (innenfor støy) |
| 52 | smed2 #1794 v10 | 0,8876 | verifisert, byte-lik, ny beste; mangler SISTE.txt |
| 53 | smed #1810 v3 / smed3 #1796 v2 | 3736 / 3749 km | verifisert, byte-like; smed ny beste |

## Øvelse 56 arxiv_klynger (ARI, måler 330641a431), dom #1829, 2026-11-04
| Kandidat | Offentlig | Privat | Status |
|---|---|---|---|
| speider #1823 v5 | 0,7846 | 0,7665 | verifisert kaldt, byte-lik, vinner |
| smed3 #1827 v1 | 0,7498 | 0,7576 | verifisert kaldt, byte-lik |
| smed #1826 v4 | 0,7449 | 0,7316 | verifisert kaldt, byte-lik |

## Øvelse 57 usgs_feil (AP, måler e26cab8990), dom 2026-11-04 (dom_ovelse_57.md)
| Kandidat | Offentlig | Privat | Status |
|---|---|---|---|
| smed2 #1834 lag.sh | 0,7921 | 0,9188 | verifisert kaldt, byte-lik, vinner |
| arkitekt #1824 e6 | 0,7546 | 0,8788 | underkjent: lag.sh feiler kaldt (mangler kode for v2/v3); koden gir 0,7446 / 0,8578 |
| smed #1819 v12 | 0,8071 | 0,8637 | verifisert kaldt, byte-lik |
| smed3 #1816 | 0,7974 | 0,8571 | målt (levert fil), ikke kaldkjørt |

| reserve T+90 (#1853) | speider tilstand + q90klima10 | off 0,1743 / v1 0,1353 / v2 0,1118 / priv 0,1708 | verifisert, kald byte-lik | 2026-11-05 |
| reserve leveranse 5 (#1912) | HGB #892 k=-0,3 + sim #910, 50/50 log1p | off 0,1537 / v1 0,1089 / v2 0,1048 / 2025-snitt 0,1681 | verifisert, kald byte-lik (#937) | 2026-11-05 |

## Case 1 (hack 05.11), måler bdad4444d1, F1 MOT høyere
| Kandidat | Score | Status | Dato |
|---|---|---|---|
| Baseline følg styret (v0) | 0,357 | verifisert (dommer) | 2026-11-05 |
| Baseline alltid FOR (v0) | 0,000 | verifisert (dommer) | 2026-11-05 |

## Case 1, måler v2 52292737df (avvik fra utledet styre), 2026-11-05
| kandidat | AVVIK F1 | PR-AUC | MOT-F1 | status |
|---|---|---|---|---|
| smed3 #970 sitatagent v2 | 0,240 | 0,153 | 0,860 | verifisert |
| smed2 #966 lgbm tfidf+historikk | 0,000 | 0,018 | 0,839 | verifisert (= baseline) |
| smed3 #968 ekte styret | 0,000 | 0,014 | 0,839 | verifisert (= baseline) |
| baseline følg utledet styre | 0,000 | 0,014 | 0,839 | baseline |
| alle målinger med ledelsen-feltet (v1 «følg styret» 0,357 m.fl.) | – | – | – | underkjent: lekkasje |

## Case 1, måler v3 8b09c36e01 (`--score mot`, test 2026), dom #2366, 2026-11-05
| kandidat | F1 MOT | TP/FP/FN | status |
|---|---|---|---|
| frossen #2044 miks h2 (levert) | 0,476 | 30/38/27 | verifisert (dommer), levert |
| smed4 #2363 nyeste historikk A+B | 0,500 | 31/35/27 | verifisert byte-likt, IKKE INN: paret bootstrap skiller ikke fra base (P 0,83 / 0,88 på val 2025/2024) |

| 2026-11-05 16:3x | #2495 V2 hybrid+rangering, test 2026 | F1 MOT 0,516 | verifisert, ikke hovedtall (dom #2500) |
| 2026-11-05 16:3x | #2496 personnøkkel rullende 2024/2025 | 0,418/0,516 (uten: 0,455/0,514) | verifisert, ikke hovedtall, gevinst bare i 2026 (dom #2500) |
| 2026-11-05 17:02 | Case 1 repo4 (frossen #2044 + 4 repotrekk), F1 MOT test 2024/25/26: 0,5057/0,5309/0,5120, snitt 0,5162 (frossen 0,4817, +0,0345, KI [−0,005; +0,078]) | verifisert fra kald kopi, byte-likt | dommer2 #2570: BYTT, betinget grønn pakke innen 18:45 (c1_byttedom_265.md) |
| 2026-11-05 17:29 | Case 1 jury-zip repo4 (jurypakke_c1_1724_5514792.zip, sha fc0dbc55), test 2026 | F1 MOT 0,5120 (TP32 FP35 FN26) | verifisert fra kald start (tom mappe, egen .venv, sandbox), frys 17:18 grønn, tallvakt 0 avvik | dommer #2649: BYTT-pakka GRØNN (c1_dom_bytt_kald.md) |

## Case 1 dom 18:15 (#2713, 2026-11-05)
| kandidat | snitt 3 år | mot frossen 0,5162 | status |
|---|---|---|---|
| #2709 avn2 (smed4) | 0,5261 | +0,0099, verste år +0,0033 | underkjent for bytte (under +0,02), tall verifisert |
| #2709 av (#2701) | 0,5297 | +0,0135, verste år +0,0066 | underkjent for bytte (under +0,02), tall verifisert |
| #2710 maks-rang (arkitekt) | 0,5007 | −0,0155, 2025 −0,036 | underkjent, tall verifisert |

- 2026-11-05 19:06  [dommer #1972]  Endelig pakke jurypakke_c1_1902_cbae393.zip (ENDELIG_PAKKE.zip): kald start i sandkasse GRØNN, F1 MOT 0,512, testår snitt 0,5162, tallvakt 177/0. Verifisert. Rapport: c1_endelig_pakke_1930.md

## Case 1 natt-måling 19:46 (#2880, dommer2, 2026-11-05), mot frossen 0,5162 på 2024-26, 2023 som vakt
| kandidat | snitt 24-26 | mot frossen | verste år | status | forsøk |
|---|---|---|---|---|---|
| #2875 likhet tfidf på midt+av (smed) | 0,5261 | +0,0099 | 2025 −0,0033 | underkjent for bytte (= lederen midt+av, w=0), tall verifisert | #1252 |
| #2875 likhet MiniLM på midt+av (smed) | 0,5209 | +0,0047 | 2025 −0,0190 | underkjent for bytte, tall verifisert | #1253 |
| #2871 tekstmal første-MOT (smed2) | 0,5191 | +0,0028 | 0,0000 | underkjent for bytte, tall verifisert | #1254 |
| #2881 regimeskifte på repo4 (smed2) | 0,5212 | +0,0050 | 2024 0,0000 | underkjent for bytte, tall verifisert | #1255 |
| #2881b av + regimeskifte (smed2) | 0,5349 | +0,0187 | 2025 +0,0134 | underkjent for bytte (0,0013 under +0,02), tall verifisert; nærmeste natt-kandidat | #1256 |
| #2885 tidsvekt rangerer + arvet flaggtall + av (smed3) | 0,5401 | +0,0239 | 2025 +0,0033 | tall verifisert fra kald kopi, byte-likt (#2902); regel testinformert (diagnose med testflagg 19:49, regel 19:50); under v2+av, ikke bytt | #1265 / #1268 |
| #2887 v2 (SVD-tekst i LGBM) + av (smed) | 0,5596 | +0,0434 | 2023 +0,0188 | svarfiler verifisert fra kald kopi, byte-likt (#2895); måleren sier BYTT; v2-modellens scratch-omkjøring pågår i #2895 | #1266 |
| #2903 frø-spredning v2+av, 5 frø (smed3) | 0,5571 (frøsnitt) | +0,0409 | 2023 +0,0200 (frøsnitt); verste enkeltfrø 0,5519 | verifisert fra kald kopi, 45 csv byte-like (#2911); sd 0,0047, alle 5 frø oppfyller regelen hver for seg; byttetabell c1_byttetabell.md | #2911 |
Detaljer: c1_natt_maaling.md.
