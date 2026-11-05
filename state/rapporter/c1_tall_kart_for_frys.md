# Case 1: tall-kart for oppdateringen etter frysen (forarbeid til #1975)

Laget 05.11 15.55 av speider (#2456). Ingen filer er endret. Stier fra `arbeid/hack/`.
Linjenummer gjelder filene slik de sto 15.55. Arkitekt #2435 og smed4 #2450 jobber i dem, så **sjekk linjene med grep før du retter** (søk på tallet).
Filer i zipen: `c1/leveranse/JURY.md`, `c1/leveranse/JURY_SPORSMAL.md`, `c1/DEMO_MANUS.md`, `levering/JURY_README.md` (blir `README.md` i zipen). `levering/JURY_SPORSMAL.md` er **ikke** i zipen (pakk_jury.sh kopierer den ikke), så den er utelatt.

## Fremgangsmåte for #1975 (3 steg)
1. **Port:** les #2285 (kaldstart). Er HOVEDTALL `0.476190`, TALLVAKT GRØNN og `ut/agent.csv`-sha lik før frysen (`1543706f…`), er gruppe A uendret, og alle tall i gruppe D står. Da gjenstår bare B (#2266) og C (#2381).
2. Endres agent.csv eller F1: alt i A må byttes fra den nye `maaling`/KJOR-utskriften, og gruppe D må merkes «målt før frysen» eller måles på nytt (de kommer fra `kilder/*.md`, ikke fra kjøringen).
3. Kjør `sh KJOR.sh` til slutt: tallvakta må være GRØNN etter rettingen.

## A. Fra kaldstarten (#2285): KJOR.sh-utskrift / måler v3 `--score mot` / `kjor_agent_real_test2026.txt`
| Fil | Linje | Tall nå | Kilde |
|---|---|---|---|
| JURY.md | 5, 16, 35, 57, 66 | F1 0,476 | HOVEDTALL i KJOR.sh |
| JURY_README.md | 5, 22 | 0.476190 | HOVEDTALL |
| JURY_SPORSMAL.md | 6, 7, 11 (30), 23, 46, 52 | 0,476 / 0,476190 | HOVEDTALL |
| DEMO_MANUS.md | 4 (F1 0,4762), 15, 56 | 0,476; 30 av 58; 44 % | `maaling.txt` (P 0.4412) |
| JURY.md | 5, 24, 66; SPØRSMÅL 11; MANUS 15, 34, 56 | 30 av 58 funnet, 28 oversett, 38 av 68 falske, P 0,441, R 0,517 | TP/FP/FN fra måler |
| JURY_README.md | 49 | `TP 30 FP 38 FN 28 TN 1443` | sjekk_treffsikkerhet.sh |
| JURY_README.md | 25 | SCORE 0.481752 (avvik) | SCORE-linja i KJOR.sh |
| JURY.md | 29 | F1 0,482 på avvik (66 avvik: 58/5/3) | samme SCORE-linje |
| JURY.md | 28; SPØRSMÅL 10–11 | accuracy følg styret 96,2 %, agent 95,7 % | `kilder/oppgave_2234_baseline_real_test.txt` (regnes fra agent.csv) |
| DEMO_MANUS.md | 13, 60 | «96 av 100», 96,2 % | samme |
| JURY.md | 34, 46; MANUS 44–45, 57 | 183 av 1539 (11,9 %) til menneske | `maaling.txt`/telling.py, `kilder/TREFFSIKKERHET.md` |
| JURY.md | 34 | 21 av treffene til menneske, 9 auto-MOT alle riktige | `kilder/TREFFSIKKERHET.md` (treffsikkerhet.py) |
| JURY.md | 73 | 188 av 1578 = 127 usikre + 60 ukjent + 1 instruks | kjøreloggen (ruting på alle 1578) |
| JURY.md | 6, 35, 53, 68; SPØRSMÅL 31; MANUS 34–36, 58 | 17 av 28 bom P ≤ 0,09 uten menneske, 11 til menneske; 38 falske alle til menneske | `maaling.txt` «FN maskin 17 menneske 11», «FP maskin 0 menneske 38» |
| DEMO_MANUS.md | 4, 63 | agent.csv sha `f0444a47…` (gammel) og `1543706f…` (kald kopi 14.45) | sha256 av ny `ut/agent.csv`. **Linje 63 ber om f0444a47, linje 4 sier at kald kopi gir 1543706f: rett linje 63 til den sha kaldstarten gir.** |
| DEMO_MANUS.md | 19–45 | linje 276 Mobimo p 1.0; linje 89 LOTTE p 0.0896; linje 15 Kura Sushi p 0.5833 | `agent.csv` linje 15/89/276. Endres de: kjør velg.py og telling.py (manus linje 63) |
| JURY.md | 12; README 68; MANUS 7 | måler-sha `418a937e57` | `shasum` av maaler_offisiell_v3.py (frys_fasit) |
| JURY_README.md | 11 | 41–89 s, nedlasting 3–20 s, ca. 230 MB/70 MB | kaldstart-tid (#2417/#2421). Kaldstartens tid kan legges til, ikke byttes |

## B. Fra motstandstesten (#2266) på den frosne agenten
| Fil | Linje | Tall nå | Kilde |
|---|---|---|---|
| JURY.md | 76; SPØRSMÅL 43 | 16 av 16 instrukser fanget på 1 578 saker, 0 endret uten ruting | `kilder/c1_injeksjon_hoflig.md`, `c1_titlecase_vakt.md` |
| JURY.md | 76; SPØRSMÅL 43 | verste angrep F1 0,457 | samme |
| JURY.md | 36, 76; SPØRSMÅL 43 | 6 av 16 tittel-instrukser slipper, 18–27 stemmer endret, F1 0,39–0,42 | `kilder/c1_titlecase_vakt.md` |
| JURY.md | 76 | «kjørt på nytt av dommeren … 05.11 kl. 15.01» | bytt til tidspunktet for #2266 |
| JURY.md | 76 | 20–21 saker, F1 0,387–0,400 (før vakta) | `kilder/c1_injeksjon_etter_2205.md`: historisk, **ikke** bytt |
| JURY.md | 74 | uten historikk F1 0,375, 99,4 % rutes | `kilder/c1_robusthet_frossen.md` (bytt hvis #2266 kjører robusthet også) |
| JURY_SPORSMAL.md | 52 | offline: 0,476190 uendret | `kilder/c1_offline_kaldstart.md` (ikke en del av #2266; står hvis A er uendret) |

## C. Fra terskeltabellen (#2381)
| Fil | Linje | Tall nå | Kilde |
|---|---|---|---|
| JURY.md | 44–47 | bånd-tabellen: 70/120/183/220 til menneske; 28/7/23, 12/23/23, 9/32/17, 9/33/16; falske 37/1, 5/33, 0/38, 0/38 | `kilder/c1_mennesket_arbeid.md` (menneske_tabell.py) |
| JURY.md | 49 | 12 av 100, 32 av 58, 1 per 6 mot 1 per 27, 2–3 saker for 1 MOT til | regnes fra rad «Standard» |
| JURY.md | 6, 73; README 39; MANUS 3, 39, 41 | bånd [0,15; 0,85) | låst på val 2025, skal ikke endres |
| JURY_README.md | 37–38 | MOT-flagg ved p_mot ≥ 0,191; rå grense 0,919 | terskel_val_test.py / terskeltabellen |
| JURY_README.md | 58 | eksempelsaken: P(MOT) 0,52, NBIM 5.3.1 | kjør `kjor_agent.py --sak '…'` på nytt (1 s) |

## D. Fra rapporter i `kilder/` (endres ikke av frysen hvis A er uendret)
| Fil | Linje | Tall nå | Kilde |
|---|---|---|---|
| JURY.md | 5, 35, 67; SPØRSMÅL 15 | KI [0,36; 0,59] (klynge), [0,37; 0,59] (rader) | `kilder/oppgave_2095_ki_mot.py`, `c1/tall_tabell.md:10` |
| JURY.md | 16–23; SPØRSMÅL 15, 48 | b2 0,365, b 0,287, a 0,097, golv 0,415, KI-er, +0,11 [0,01; 0,22] | `kilder/c1_enkle_regler_og_hist1.md` |
| JURY.md | 23, 72; SPØRSMÅL 23 | golv 0,415 [0,30; 0,53]; uten historikk 0,282 (avvik) | samme + `kilder/c1_ablasjon_v2.md` |
| JURY_SPORSMAL.md | 18–19 | 0,482 / 0,500 / 0,276 / 0,282 / 0,504 | `c1/tall_tabell.md:13-17` |
| JURY.md | 30 | aksjonærforslag=MOT: 2 av 58, F1 0,066; N-PX 0,645 | `kilder/case1_hvilken_fasit.md` |
| JURY.md | 57, 59, 67; SPØRSMÅL 7 | val 2025 F1 0,520 (0,522 avvik) | `kilder/c1_val_kaldstart.md:23` |
| JURY.md | 58–59 | tiltak 1: 0,520231→0,550898, 2024 −0,015 [−0,043; 0,017], P 0,19; USA-regel 0,504 / 0,488 | `kilder/c1_tiltak1_malt.md`, `c1_feil_stabilitet.md` |
| JURY.md | 67 | seed 0,462–0,522, snitt 0,483 | `kilder/c1_seed_frossen.md` |
| JURY.md | 24, 53, 69; SPØRSMÅL 39 | 0 av 7 USA, 0 av 17 eneste MOT, 0 av 4 nye selskaper, klynge 5 vs 7 FOR, 7 av 17 i USA | `kilder/c1_bommene.md` |
| JURY.md | 70 | 18 aksjonærforslag av 1578; 56 av 58 styre-MOT (26/7/6/6/11) | `kilder/c1_mot_sakstyper.md` |
| JURY.md | 71 | 11 785 saker (12 179 − 394), 70–99 MOT/år, 141 møter i 136 selskaper | `kilder/tell_trening.py`, `tell_aar.txt` |
| JURY.md | 75; SPØRSMÅL 35 | sitat 15/4/1 av 20 | `kilder/c1_sitat_verifisert.md` |
| JURY.md | 77 | falske MOT: 26 av 38 styrevalg, 22 av 38 snudd, 5 USA, 9 falske i USA | `kilder/c1_falske_mot.md` |
| JURY_SPORSMAL.md | 46–48 | t4e 0,529, 0,482, 0,468 mot 0,522, huskeregel +0,23 [+0,12; +0,34] | landsbyrapporter (ikke i zipen) |

## Funn #1975 bør ta med
1. **Gamle linjepekere i JURY_SPORSMAL.md peker feil i JURY.md** (mest sannsynlig fordi JURY.md fikk «Les dette først» øverst). Svar 2 `JURY.md:7` (accuracy står på 28), svar 3 `JURY.md:44-45, :51` (KI står på 5/16/67, +0,11 på 23), svar 5 `JURY.md:49` (golvet står på 23/72), svar 10 `JURY.md:44, :15` (injeksjon står på 76), svar 11 `JURY.md:23` (det stemmer). Linjepekerne til `tall_tabell.md:4/9/10/13/16-17` stemmer. ERLIG_EVALUERING/BEGRENSNINGER/demo_saker-pekere er ikke sjekket.
2. DEMO_MANUS linje 63 og linje 4 sier forskjellige ting om hvilken sha agent.csv skal ha (se A).
3. README linje 11 har fortsatt `#2417, #2421`. Det hører til arkitektens #2435.
