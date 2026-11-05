# Case 1: tallkontroll etter modellfrys (dommer2, #2255, 05.11 kl. 16.45)

**Kort fortalt:** alle tall i JURY.md, JURY_SPORSMAL.md, kravrespons.md, DEMO_MANUS.md og ERLIG_EVALUERING.md finnes i en målerlogg eller rapport med måler-sha. Hovedtallet: tallvakta GRØNN (18 filer, 169 påstander, 0 avvik, måler v3 på den frosne svarfila: F1 0,4762, TP 30 FP 38 FN 28, 58 MOT). Ingen tall er feil. **4 henvisninger peker på feil eller manglende fil** (tallet står i en annen kilde i zipen, eller bare i repoet). Lagt som oppgave til speideren.

Metode: `arbeid/oppgave_2255/sjekk.py` grepper hvert tall i kildefila teksten peker på (85 påstander), pluss manuelle grep for resten. Kilder i jury-zipen = `leveranse/kilder/`, `c1/tall_tabell.md`; «repo» = `state/rapporter/`.

## Tall -> kilde -> status
| Hvor | Tall | Kilde | Status |
|---|---|---|---|
| JURY, kravrespons, demo | F1 0,476 / P 0,441 / R 0,517 / 30 av 58 / 38 av 68 / 28 oversett / 58 MOT / 66 avvik / 188 av 1578 / 183 av 1539 (11,9 %) | tallvakt mot måler v3 sha 418a937e57 på `kjor_agent_real_maskin_alene.csv`; `c1_1975_tall_etter_frys.md` (kald kopi 16.05) | OK |
| JURY tabell | b2 0,365 [0,252; 0,492], b 0,287 [0,203; 0,378], a 0,097 [0,072; 0,124], golv 0,415 [0,301; 0,533], KI [0,359; 0,590], +0,11 [0,01; 0,22] | `kilder/c1_enkle_regler_og_hist1.md:10-14,36` | OK |
| JURY, JS1 | val 0,520 | `kilder/c1_val_kaldstart.md:23` | OK |
| JURY «ikke jaget» | 0,520231 -> 0,550898; 2024 −0,015 [−0,043; 0,017] P 0,19 | `kilder/c1_tiltak1_malt.md:19,25` | OK |
| JURY «ikke jaget» | USA->menneske 0,504 / val 0,488 | `kilder/c1_feil_stabilitet.md:23` | OK |
| JURY bommene, begr. 3–4, JS7, JS9 | 17 av 28 P≤0,09; 11 til menneske; 0 av 7 USA; 7 av 17 i USA; 0 av 17 eneste MOT; 0 av 4; 5 nye amerikanske, 7 før var FOR | `kilder/c1_bommene.md:17,23,26-29` | OK |
| JURY begr. 5 | 18 aksjonærforslag av 1578; 56 av 58; styrevalg 26, revisor 7, andre 6, eventuelt 6, øvrige 11 | `kilder/c1_mot_sakstyper.md:12-27`; 18 telt på nytt fra `real_test_input.csv` (Shareholder 18) | OK |
| JURY begr. 6, ERLIG | 11 785 / 12 179 / 394; 141 møter, 136 selskaper; 70–99 MOT per år | `kilder/tell_trening.txt:1-3`, `kilder/tell_aar.txt:4-11` | OK |
| JURY begr. 2 | KI [0,36; 0,59] klynge; [0,37; 0,59] rader; seed 0,462–0,522 snitt 0,483 | `kilder/c1_tall_likt.md:5`, `c1/tall_tabell.md:4`, `kilder/c1_seed_frossen.md:23` | OK |
| JURY begr. 7, 9, 10 | 0,282 avvik uten historikk; 0,375 og 99,4 %; sitat 15/4/1 av 20 | `kilder/c1_ablasjon_v2.md:14`, `c1_robusthet_frossen.md:12`, `c1_sitat_verifisert.md:1` | OK |
| JURY begr. 11, kravrespons, JS10, ERLIG §6 | 20–21 saker, 0,387–0,400; 16/16 fanget, verste 0,457; 0,392 før tittelvakta; 6 av 16 nye, 18–27, 0,39–0,42 | `kilder/c1_injeksjon_etter_2205.md:17`, `c1_titlecase_vakt.md:27-45`, `c1_injeksjon_hoflig.md`, `c1_motstand_etter_frys.md:20-26` (etter frys, samme tall) | OK |
| JURY begr. 12 | 26 av 38 styrevalg, 22 av 38 snudd, 5 styremedlemmer USA, 9 falske | `kilder/c1_falske_mot.md:8-9` | OK |
| JURY J1 | følg styret F1 0; aksjonærforslag=MOT 2 av 58, F1 0,066 (0,0656); 66 avvik, 5 AVSTÅ; N-PX 0,645 | `kilder/oppgave_2234_baseline_real_test.txt`, `kilder/case1_hvilken_fasit.md:3` | OK |
| JURY J1, kravrespons, demo | accuracy 96,2 % / 95,7 %; 3,8 % MOT; avvik-F1 0,482 | `kilder/TREFFSIKKERHET.md:16,22`; avvik 0,481752 i tallvakt | OK tall, **AVVIK henvisning** (se 1 og 3) |
| JURY J2, bånd-tabell | 21 treff hos menneske, 9 auto riktige; 70/120/183/220; 28/7/23, 12/23/23, 9/32/17, 9/33/16; 37/1, 5/33, 0/38 | `kilder/TREFFSIKKERHET.md:30,60`, `kilder/c1_mennesket_arbeid.md:10-16` | OK |
| JS3, JS13, demo-svar | presedens 0,515 (+0,039 [−0,051; +0,126], avrundet +0,04 [−0,05; +0,13]); hybrid 0,523 / 0,545, +0,069 [+0,007; +0,133]; PR-AUC 0,525 / 0,318 / 0,413 | `kilder/c1_nbim_repo_sammenligning.md:9-13`, `kilder/c1_nbim_repo_sammenligning_dom.md:15,25` | OK |
| JS13 (ny linje 16.40) | personnøkkel +0,049 (2026), −0,037 (2024), +0,001 (2025), KI dekker null | `kilder/c1_personnokkel_dom.md:13-17` | OK |
| JS4, ERLIG §1 | ablasjon 0,482 / 0,504 / 0,276 / 0,282; val 0,522 / 0,511 / 0,448 / 0,337 / 0,485; test 0,386 / 0,470 | `c1/tall_tabell.md:16-17`, `kilder/c1_ablasjon_v2.md` | OK |
| JS5 | 400 rader brute force, 0 avvik | `kilder/dommer_ablasjon_v2.md`, ERLIG:28 | OK |
| JS6, ERLIG §4 | beste 0,522, kravet +0,03; lt 0,472 ny 0,469 mt 0,465 alle 0,468, val alle tre 0,480 | `kilder/c1_siste_mot_forsok.md:5,11-15` (0,4715 / 0,4688 avrundet) | OK |
| JS7, JS8, demo | LOTTE p 0,0896, Mobimo 1,0, Kura 0,5833, linje 89/276/15 | `kilder/demo_saker.md:21,49,77`; `vis_manussaker.py` MANUS OK etter frys (#1975) | OK |
| JS11 | t4e 0,529, val 0,468; huskeregel 0,243, +0,23 [+0,12; +0,34]; bootstrap ±0,1 | repo: `c1_valgt_bort.md:12`, `c1_huskeregel.md:3`, `c1_bootstrap_f1.md:24` | OK tall, kilder bare i repoet (teksten sier «landsbyrapport», ikke i zipen) |
| JS12 | 0,476190 offline | `kilder/c1_offline_kaldstart.md:15` | OK |
| kravrespons | 13 757 saker, 194 selskaper, 37 land, 24 sakstyper, 2019–2026 | `levering/omfang.txt` (ikke i zipen); telt på nytt fra real_votes: 13757 / 194 / 37 / 24 | OK tall, **AVVIK henvisning** (se 2) |
| kravrespons, ERLIG §6 | 81 av 82 (98,8 %), 565 av 569 (99,3 %), 94,9 % av 13 327, 86 % | `kilder/c1_praksis_mot_policy.md`, `c1_praksis_dom.md:15`, `c1_retningslinje_sitat.md` | OK |
| kravrespons | 0,06 fra løpende historikk | 0,476 − 0,415 = 0,061, `kilder/c1_enkle_regler_og_hist1.md:14` | OK |
| ERLIG §6 | val KI (0,41–0,63); bootstrap [0,403; 0,624]; bånd 7,5 % / 7,9 %; 3 før mot 8 nå | `kilder/c1_feil_stabilitet.md:14`; repo `c1_bootstrap_f1.md:16` (ikke i zipen); `kilder/c1_menneske_terskel.md`; `kilder/c1_robusthet_reprod.md` | OK tall (se 4) |
| ERLIG §6 gammel kravrespons | 0,091 / 0,145 (gammelt internt skript), 82 av 174 | merket som ikke i pakka; 82 av 174 i repo `c1_injeksjon_frossen.md` | OK (merket) |
| DEMO_MANUS | 341 ord i «», ca. 2:20 | telt på nytt: 5 blokker, 341 ord (uten Skjerm-linjer) | OK |
| DEMO_MANUS tallkilder | «96 av 100 følger styret» | peker på `state/rapporter/c1_demo_etter_rydding.md`, som ikke inneholder tallet; står i `kilder/TREFFSIKKERHET.md:16` (1481 av 1539 = 96,2 %) | OK tall, **AVVIK henvisning** (se 1) |

## Avvik (henvisninger, ikke tall) – til speider
1. **DEMO_MANUS.md tallkilder, siste rad:** «96 av 100» peker på `state/rapporter/c1_demo_etter_rydding.md`, fila har ikke tallet. Bytt til `leveranse/kilder/TREFFSIKKERHET.md:16`.
2. **kravrespons.md «Hvordan vi verifiserte»:** 194 selskaper, 37 land, 24 sakstyper har ingen kilde i zipen (`levering/omfang.txt` er ikke med; `tell_aar.txt` har bare 13 757). Legg `omfang.txt` i kilder/ (pakk_jury.sh) eller pek på den.
3. **JURY.md Juryspørsmål 1:** «Alternativene vi målte på samme test (måler v3, `kilder/oppgave_2234_baseline_real_test.txt`)» dekker baselinene, men agentens accuracy 95,7 % og avvik-F1 0,482 står ikke der; de står i `kilder/TREFFSIKKERHET.md:16` og tallvakta. Legg til henvisningen.
4. **ERLIG_EVALUERING.md § 6:** «Bootstrap-rapportens [0,403; 0,624]» og JURY_SPORSMAL pkt. 11 («landsbyrapport: c1_neste_steg / c1_valgt_bort / c1_bootstrap_f1 / c1_huskeregel») peker på rapporter som bare finnes i repoet. Tallene stemmer. Enten kopier dem til kilder/ (jf. #2509) eller skriv «i repoet, ikke i zipen» som ellers i pakka.

Ingen av de fire endrer et tall. Modellen og de 17 frosne filene er ikke rørt.
