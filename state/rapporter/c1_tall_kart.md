# Case 1: tallkart for juryfilene, med hva som må sjekkes etter frys (#2316)

Speider, 05.11 kl. 14.50. Bruk lista i #1975 (oppdater tekst) og #2255 (sjekk mot måler) etter kl. 16.
Gjennomgått: `c1/leveranse/JURY.md`, `c1/DEMO_MANUS.md`, `c1/leveranse/kravrespons.md` (1-sideren), `levering/JURYSVAR.md`
og hovedtallene i `levering/KRAVRESPONS.md` (sjekklista). Stier er fra `arbeid/hack/` med mindre annet står.
Alle filene i `c1/leveranse/kilder/` som JURY.md viser til finnes (sjekket 14.45), og det samme gjør `arbeid/oppgave_2267/maaling.txt`.

**India-kolonnen** (bryteren fra #2303: land = India + «chairman» + MD/CEO i teksten ⇒ MOT oppå modellen):
- **J** = endres hvis regelen treffer minst én rad i test 2026 (eller tallet er val 2025). Mål på nytt.
- **K** = kanskje. Ablasjon eller motstandstest av frossen #2044 *uten* bryteren. Kjør på nytt med bryteren, eller skriv «målt uten India-regelen».
- **N** = endres ikke (avhenger ikke av modellen, eller er historikk).
- Kommer bryteren **ikke** inn, er hele kolonnen N. Da holder det å sjekke at sha på `agent.csv` fortsatt er `f0444a47…`.

**Første sjekk etter frys:** treffer regelen noen test-rad? Treffer den 0 og agent.csv er byte-lik, er alle J-ene uendret, bortsett fra val 2025 (0,520 → 0,562).

## Kjernetallene (gjentas i alle filene)
Kilde for alle: `arbeid/oppgave_2267/maaling.txt` (måler v3 sha 418a937e57, `--score mot`, frossen #2044, 14.02).

| Tall | Står i (fil:linje) | India |
|---|---|---|
| F1 MOT 0,476 (0,476190) | JURY 3, 14, 25, 34, 47, 51; DEMO 14; krav 4; JURYSVAR 5, 11, 30, 36–38, 48; KRAVRESPONS 12, 54, 55, 57, 69 | J |
| TP 30 / FP 38 / FN 28 («30 av 58», «38 falske», «28 oversett») | JURY 7, 34, 59; DEMO 14, 33, 35; krav 4; JURYSVAR 6, 11, 36–38 | J |
| P 0,441 (44 %, «hvert annet flagg feil», «4 av 10 ekte») / R 0,517 | JURY 14, 34; DEMO 14; krav 4 (0,44/0,52); JURYSVAR 6, 11 | J |
| 68 MOT-flagg (= TP+FP) | JURY 34 | J |
| 58 MOT av 1539 med fasit; 3,8 % | JURY 6, 32, 34, 47; DEMO 14; krav 4, 7 (3,8 % = 58/1539, avledet); JURYSVAR 6, 32 | N (fasit) |
| Accuracy agent 95,7 % | JURY 7; JURYSVAR 11 (avledet av TP/FP/FN, `kilder/oppgave_2234_baseline_real_test.txt`) | J |
| Følg styret 96,2 % / «96 av 100» / F1 0 / 0 MOT | JURY 7, 55; DEMO 12–13, 58; krav 4, 7; JURYSVAR 11, 23 | N |
| 95 % KI [0,36; 0,59] (tabell [0,359; 0,590]) | JURY 14, 35, 51; krav 7; JURYSVAR 5, 11, 20, 48; KRAVRESPONS 13 — kilde `arbeid/oppgave_2095/ki_mot.py` (klynge, 2000 trekk, seed 0) | J |
| KI over rader [0,37; 0,59] | JURY 35 — `c1/tall_tabell.md` | J |
| Til menneske 183 av 1539 (11,9 %) | JURY 13, 41; DEMO 43–44; JURYSVAR 32, 38; KRAVRESPONS 16, 61 — `maaling.txt` «183 til menneske» | J (de snudde sakene har p 0,66–0,89 og kan havne i båndet, se #2303) |
| Til menneske 188 av 1578 = 127 usikre + 60 ukjent selskap + 1 instruks | JURY 41; krav 4; JURYSVAR 32; KRAVRESPONS 16, 61 — `state/rapporter/c1_kaldstart_2.md:7`. **JURY.md 41 oppgir ingen fil, bare «siste kaldstart»: legg inn stien** | J |
| TP maskin 9 / menneske 21; FP maskin 0 / menneske 38; FN maskin 17 / menneske 11 («alle 9 riktige», «17 ser ingen», «11 til menneske», «32 av 58 hos menneske») | JURY 13, 21, 36, 59; DEMO 33–35, 56; JURYSVAR 30, 40 | J |
| P(MOT) ≤ 0,09 for de 17 stille bommene | JURY 21, 36, 59 — `kilder/c1_bommene.md` | J |

## JURY.md (`c1/leveranse/JURY.md`), øvrige tall
| Linje | Tall | Kilde | India |
|---|---|---|---|
| 8 | 66 avvik (58 MOT, 5 AVSTÅ, 3 andre) | `kilder/oppgave_2234_baseline_real_test.txt` / maaling.txt | N |
| 8 | F1 på avvik 0,482 | maaling.txt «avvik … F1 0.4818» | J |
| 9 | «Aksjonærforslag = MOT»: 2 av 58, F1 0,066; 56 av 58 på styrets forslag | `kilder/oppgave_2234_baseline_real_test.txt`, `kilder/c1_mot_sakstyper.md` | N |
| 9 | N-PX F1 0,645 | `kilder/case1_hvilken_fasit.md` | N |
| 15 / 44 | Title Case-angrep: 16 stemmer endret, F1 0,392; 15 av 16 instrukser fanget | `kilder/c1_injeksjon_hoflig.md` | K |
| 44 | Før vakta: 20–21 saker byttet, F1 0,387–0,400 | `kilder/c1_injeksjon_etter_2205.md` | N (historikk) |
| 21, 37 | 7 av 17 stille bommer i USA; 0 av 7 USA-MOT; 0 av 17 eneste MOT i møtet; 0 av 4 nye selskaper; klynge 5 nye US-saker, 7 før 2026 FOR | `kilder/c1_bommene.md` | J (antall bommer kan endres; USA-delen trolig ikke, India er ikke USA) |
| 25, 35 | Val 2025 F1 MOT 0,520 (0,520231); 0,522 er avvik i ablasjonen | `kilder/c1_val_kaldstart.md:23` | **J: blir 0,561798 med bryteren** (`state/rapporter/c1_india_bryter.md`) |
| 26 | Tiltak 1: val 0,520231 → 0,550898 (+0,031); 2024 −0,015, KI [−0,043; 0,017], P(bedre) 0,19 | `kilder/c1_tiltak1_malt.md:18-19, 25` | N (forkastet tiltak; men grunnlinja 0,520 er uten India) |
| 27 | US-styrevalg → menneske: test 0,476 → 0,504, val 0,520 → 0,488 | `kilder/c1_feil_stabilitet.md:23` | N (forkastet regel, målt mot frossen uten India; skriv det) |
| 29 | Regelen «vinner både 2024 og 2025» | — (metode). India: 2024 0,536313 → 0,544444, 2025 0,520231 → 0,561798 (`c1_india_bryter.md`) | Bør stå som eksempel hvis bryteren kommer inn (#2314) |
| 32 | 1539 med fasit, 58 MOT; kald kjøring `/tmp/c1_kald` 05.11 12:29 | `kilder/oppgave_2216_tell.py` | **J: tidspunkt/kjøring må byttes til frys-kjøringen** |
| 38 | 18 aksjonærforslag av 1578; styrevalg 26, revisor 7, andre styresaker 6, annen sak 6, øvrige 11; 2 MOT med aksjonærkandidat | `kilder/c1_mot_sakstyper.md` | N (fasit) |
| 39 | Trening 11 785 saker 2019–2025 (12 179 − 394), 70–99 MOT per år | `kilder/tell_trening.py` | N |
| 39 | Test 141 møter i 136 selskaper | **UTEN KILDE i fila** (står bare i `state/rapporter/c1_jury_godkjent_2239.md:18`). NB: JURYSVAR 20 sier 135 selskaper i bootstrapen (trolig 1539 mot 1578 rader). Avklar | N |
| 40 | Uten løpende historikk 0,415 [0,30; 0,53] | `kilder/c1_enkle_regler_og_hist1.md` | K |
| 40 | Uten historikk 0,282 på avvik | `kilder/c1_ablasjon_v2.md` | K |
| 41 | Bånd [0,15; 0,85) | `levering/c1_real.py` / `c1_kaldstart_2.md` | N (låst på val) |
| 42 | Nye selskaper F1 0,375, 99,4 % rutes | `kilder/c1_robusthet_frossen.md` | K |
| 43 | Sitat: 15 riktig, 4 delvis, 1 feil av 20 | `kilder/c1_sitat_verifisert.md` | K (stikkprøven gjelder gamle flagg) |
| 47 | Måler v3 sha 418a937e57, 0,476190 | maaling.txt | sha N, tall J |
| 52–56 | b2 0,365 [0,252; 0,492]; b 0,287 [0,203; 0,378]; a 0,097 [0,072; 0,124]; følg styret 0; golv 0,415 [0,301; 0,533] | `kilder/c1_enkle_regler_og_hist1.md` | regler N, golv K |
| 58 | Modellen − b2: +0,11 [0,01; 0,22] | `kilder/c1_enkle_regler_og_hist1.md` (#2134) | J |
| 59 | «Rådet funnet på test (n = 5)» | `kilder/c1_bommene.md` | N |

## DEMO_MANUS.md (`c1/DEMO_MANUS.md`)
Manuset har allerede egen kildetabell (linje 51–58) og en etter-frys-oppskrift (linje 60–61). Tallene:
| Linje | Tall | Kilde | India |
|---|---|---|---|
| 4, 61 | agent.csv sha256 `f0444a47…` | `arbeid/oppgave_2260/full/agent.csv` | **J: ny sha hvis bryteren kommer inn** |
| 7 | 359 ord, ca. 2:30 ved 145 ord/min | **UTEN KILDE** (egen telling, ikke lagret) | N |
| 12–14 | 96 av 100, F1 0, F1 0,476, 30 av 58, 44 % | se kjernetallene | J (bortsett fra 96/0) |
| 18–25 | Mobimo, linje 276, `2041367|21`, p_mot 1.0, til_menneske 0, GVG 5.2 | `agent.csv` / maaling.txt | N for innholdet (Sveits), men sjekk linjenummer og rad |
| 27–35 | LOTTE, linje 89, `2048411|10`, p_mot 0.0896 (0,09), til_menneske 0; 28 / 11 / 17 / 38 | agent.csv / maaling.txt | rad N (Korea), tellingene J |
| 37–44 | Kura Sushi, linje 15, `2033470|1`, p_mot 0.5833 (0,58), bånd [0,15; 0,85), 183 av 1539, 11,9 % | agent.csv / maaling.txt | rad N (USA), 183 J |
| 47 | «Grensene valgt på 2025» | — | N |

Raden kan bare endres hvis bryteren endrer rekkefølgen i agent.csv. Det skal den ikke, men linje 15/89/276 sjekkes likevel (linje 61 i manus).

## Kravrespons, 1-sideren (`c1/leveranse/kravrespons.md`)
**Fila har ingen kildehenvisninger.** Hvert tall under er sporet av meg. Lag en usynlig kildelinje eller kommentar i #1975.
| Linje | Tall | Kilde | India |
|---|---|---|---|
| 4 | 188 av 1578 | `c1_kaldstart_2.md:7` | J |
| 4 | 30 av 58, F1 0,476, P 0,44, R 0,52, følg styret 0 | maaling.txt | J |
| 7 | 3,8 % MOT, følg styret 96,2 % | avledet 58/1539, `kilder/oppgave_2234_baseline_real_test.txt` | N |
| 7 | KI [0,36; 0,59]; b2 0,365 | ki_mot.py; `kilder/c1_enkle_regler_og_hist1.md` | KI J, b2 N |
| 7 | 16 instrukser, 15 flagget, 16 stemmer endret, F1 0,392 | `kilder/c1_injeksjon_hoflig.md` | K |
| 9 | «Omtrent 0,06 av F1» fra samme sesong; uten 0,415 | **UTEN KILDE for 0,06** (avledet 0,476 − 0,415); 0,415 fra `kilder/c1_enkle_regler_og_hist1.md` | J / K |
| 9 | 15 av 20 avgjørende | `kilder/c1_sitat_verifisert.md` | K |

## JURYSVAR.md (`levering/JURYSVAR.md`), tall utenom kjernetallene
| Linje | Tall | Kilde | India |
|---|---|---|---|
| 7 | avvik 0,4818; 66 avvik (58/5/3) | #2086, maaling.txt | 0,4818 J, 66 N |
| 14 | `position_paper` 97,5 % MOT når satt | `arbeid/oppgave_2044/train.py` | N |
| 14, 51 | Uten sakstype 0,500 [0,38; 0,61] | #2103 (`state/rapporter/c1_lekkasje_v3.md`) | K |
| 17 | Grense 0,9188 valgt på val 2025 | `arbeid/oppgave_2044/train.py` | K (regelen legges oppå flaggene; sjekk at grensen er den samme) |
| 20 | 135 selskaper, 2000 trekk | `arbeid/oppgave_2095/ki_mot.py` | N. Se avviket 135/136 mot JURY 39 |
| 20, 48 | Val 2025 0,520 [0,41; 0,63] | #2095 | **J: 0,562, nytt KI** |
| 20 | «± 0,12» | **UTEN KILDE** (avledet halv KI-bredde) | J |
| 23 | b2 0,365 [0,25; 0,49]; +0,11 [0,01; 0,22]; a 0,097; b 0,287; golv 0,415 [0,30; 0,53] | #2134, `state/rapporter/c1_enkle_regler_og_hist1.md` | b2/a/b N, +0,11 J, golv K |
| 26 | 1578 rader, 15 ulike avsnitt, 1504 FOR-standard, 74 konkrete (71 MOT-flagg + 3), 140 GVG-punkter, 18 (gammel kjøring) | #2130, #2278 | **J: 71 og 74 endres hvis det kommer nye MOT-flagg; 1504 også** |
| 26 | 54 av 63 MOT-saker (86 %) samme seksjon | #2106 | N (fasitsaker) eller K hvis nye sitater |
| 26 | 20/20 ordrett, 15/20 avgjørende, 4 delvis, 1 feil | #2115 | K |
| 27 | 8 av 20 begrunnelser etter eldre retningslinjer | #2130 | N |
| 30, 36–38 | ingen ruting 0/1539; bare bånd 122 (7,9 %), 27 av 58, F1 0,779 (TP 37 FN 21), gulv 0,294; standard 183 (11,9 %), 32 av 58, F1 0,828 (TP 41 FN 17), gulv 0,269 | `arbeid/hack/c1/menneske_tabell.py arbeid/oppgave_2132/agent.csv` | **J: kjør menneske_tabell.py på ny agent.csv** |
| 45 | Nye selskaper 0,375 (#2144), 99,4 % rutes | #2144 | K |

## `levering/KRAVRESPONS.md` (intern sjekkliste, ikke til juryen)
Hovedtallene i linje 11–17 og radene 4, 5, 7, 9, 11, 19, 31 gjentar kjernetallene (0,476, KI, 30/38/28, 188/183, 0,520, 0,4818 [0,375; 0,580]). Alle er J ved India.
Stale tall som ikke er kjernetall: linje 25 (REF 0,481752), 28 (40–41 stemmer, 0,482 → 0,40–0,42), 43 (176/171), 58 (gulv 0,386 på avvik), 60 (74/74 sitat, #2053). Det er historikk i HULL-lista, men de bør ikke kopieres til juryfilene.

## Uten kilde eller uklart (rett i #1975)
1. JURY.md 39: «141 møter i 136 selskaper». Ingen kilde i fila. JURYSVAR 20 sier 135 selskaper.
2. JURY.md 41: 127/60/1 viser til «siste kaldstart» uten sti. Kilde: `state/rapporter/c1_kaldstart_2.md:7`.
3. kravrespons.md: ingen kilder i fila. «0,06 av F1» er avledet.
4. JURYSVAR 20: «± 0,12» er avledet.
5. DEMO_MANUS 7: ordtellingen 359 / 2:30.

## Rekkefølge etter kl. 16 hvis bryteren kommer inn
1. Ny `agent.csv` → måler v3 `--score mot` → ny `maaling.txt` (TP/FP/FN, ruting, maskin/menneske). Det oppdaterer alle J-ene i kjernetabellen.
2. `ki_mot.py` (KI), `menneske_tabell.py` (JURYSVAR 7), paret bootstrap mot b2 (+0,11).
3. Val 2025: 0,520 → 0,561798 (JURY 25, 35; JURYSVAR 20, 48; KRAVRESPONS 14), og nytt KI.
4. Sitat-tellingene (71/74/1504) og `c1_bommene.md` (17/28/7 av 17).
5. K-tall: kjør på nytt eller skriv «målt på frossen #2044 uten India-regelen».
