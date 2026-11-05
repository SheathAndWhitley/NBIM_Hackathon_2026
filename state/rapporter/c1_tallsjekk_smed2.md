# Case 1 (#2591): uavhengig tallsjekk av jury-teksten mot kildefilene, smed2 05.11 ca. 17.35

**Kort:** Jeg sjekket 795 tall i README, kravrespons, ERLIG_EVALUERING og JURY_SPORSMAL (`arbeid/hack/c1/leveranse/`).
Alle 795 finnes i en kilde. Men **4 avvik** må rettes, og **1 forbehold** gjelder hele pakken: byttedommen.
Selve hovedtallene stemmer: 0,476, TP 30 FP 38 FN 28, KI [0,36; 0,59], 188/1578 og den rullende tabellen.

## Slik er det sjekket
1. Maskinelt: `python3 -I arbeid/oppgave_2591/tallsjekk.py > arbeid/oppgave_2591/ut.tsv`. Skriptet henter alle tall,
   men hopper over tall i backticks, URL-er, sha-er og sak- og avsnittsnumre. Så leter det etter hvert tall i
   nivå 1-kildene, som følger pakka: `leveranse/kilder/*`, `c1/tall_tabell.md`, `tall_kilder_ut.txt`,
   `terskeltabell_ut.md` og `demo_utskrift.txt`. Finner det ikke tallet der, leter det i nivå 2: `state/rapporter/c1*`.
   Et desimaltall teller som funnet når et kildetall med flere desimaler runder av til det.
   **Resultat:** 771 OK på nivå 1, 23 OK på nivå 2 og 1 umatchet (0,081, se A1).
2. For hånd i sammenheng: å finne tallet et sted i kildene beviser lite. Derfor sjekket jeg nøkkeltallene mot riktig
   rad i kilden, og regnet aritmetikken på nytt. Detaljene står i tabellene under.

## Avvik som bør rettes før kl. 19

| tall | fil:linje | kilde | OK/AVVIK |
|---|---|---|---|
| 0,048 / 0,845 / 0,091 (historikkregel «selskapet hadde MOT før») | ERLIG_EVALUERING.md:67 | Ingen kilde i pakka. `kilder/c1_enkle_regler_og_hist1.md:11` har samme regel med **0,052 / 0,828 / 0,097**. | **AVVIK** (A1). Tabellen er sitert ordrett fra kl. 13.06, og § 6 (linje 48) varsler bare om 0,091. Men linje 72 sier: «Alle tall er målt med maaler_offisiell_v3 … og er beskrevet i kilder/c1_enkle_regler_og_hist1.md». Det stemmer ikke for disse to radene. |
| 0,081 / 0,672 / 0,145 («selskap + forslagstype») | ERLIG_EVALUERING.md:68 | Finnes ikke i noen kilde, verken i pakka eller i state/rapporter. 0,145 står bare i gamle jurylesinger (`c1_jurylesning_dommer2.md:30`, «gammelt skript `levering/c1_v1/hist_regel.py`, ingen logg»). | **AVVIK** (A1). Den eneste raden uten noen kilde. Stryk begge radene fra tabellen, eller merk dem «gammelt internt skript, ikke målt med v3», slik at linje 73 blir sann. |
| 31–52 s | ERLIG_EVALUERING.md:52 (§ 6, «Kommandoen … (31–52 s) under») | Teksten under, linje 73, sier **29–52 s**. README:43 sier også 29–52 s. Kilde: `kilder/c1_offline_kaldstart.md:35` (29 s) og `c1_kjoretid.md` (52 s). | **AVVIK** (A2). Varselet og teksten det varsler om, oppgir ulike tall. Rett 31 til 29. |
| «atten» | JURY_SPORSMAL.md:1 («de atten vanskeligste jurysporsmålene») | Fila har 19 nummererte spørsmål (sp. 1–19). README:11 viser til «sp. 19». | **AVVIK** (A3). Bytt til «nitten». |
| PR-AUC 0,525 | JURY_SPORSMAL.md:73 (sp. 17) | `demo_utskrift`/README:48 0.5245, `tall_tabell.md:10` **0.524** | **AVVIK, lite** (A4). 0,5245 runder av til 0,524 i tall-tabellen og til 0,525 her. Velg ett av dem, helst 0,524 som i tabellen. |

## Forbehold: byttedommen (gjelder nesten alle tall)
`state/rapporter/c1_byttedom_265.md` (dommer2, 17:02) sier **BYTT til repo4**, på vilkår av grønn pakke innen 18:45.
Teksten jeg har sjekket, beskriver fortsatt den frosne modellen. Det gjelder hovedtallet 0,476 i alle fire filer,
ERLIG § 7:79 («ingen kandidat er godkjent, og den frosne modellen står») og JURY_SPORSMAL sp. 19 («Den frosne agenten står»).
Å skrive inn byttet er #2580 (smed3). Blir byttet gjennomført, må tallsjekken kjøres på nytt på den nye teksten.
Kommandoen er den samme: skriptet leser filene på nytt hver gang.
Repo4-tallene i § 7 stemmer med primærloggen: 0,5057 / 0,5309 / 0,5120, snitt 0,516.

## Sjekket i sammenheng: OK
| tall | fil:linje | kilde | OK/AVVIK |
|---|---|---|---|
| F1 0,476, P 0,44/0,441, R 0,52/0,517, TP 30 FP 38 FN 28, 58 MOT, 1539 | README:8-9,28,49; kravrespons:4; ERLIG:6,71 | `demo_utskrift.txt`, `kilder/c1_siste_mot_forsok.md:11`, `oppgave_2567/benk.txt` (frossen 2026) | OK |
| TN 1443, accuracy 95,7 %, følg styret 96,2 % | README:28; kravrespons:7; ERLIG:62 | Regnet på nytt: 30+38+28+1443=1539; 1473/1539=95,71 %; 1481/1539=96,23 % | OK |
| KI [0,36; 0,59] klynge, [0,37; 0,59] rader | README:8,13; kravrespons:7; JURY_SP:15 | `kilder/c1_enkle_regler_og_hist1.md:10` [0,359; 0,590]; `tall_tabell.md:10` [0.37, 0.59] | OK |
| 188 av 1578 (11,9 %), 127 usikre + 60 ukjent + 1 instruks, 183 av 1539 | README:10,14-15; kravrespons:4 | Talt på nytt fra `/tmp/c1_kald/ut/agent.csv`: 188 rutet; 60 «ukjent selskap», 1 instruks, 127 usikre. `kilder/c1_offline_kaldstart.md:35`, `TREFFSIKKERHET.md:7` (183) | OK. Merk at `c1_robusthet_frossen.md:11` skriver «ukjent selskap 70». Den teller trolig flere grunner per sak; README stemmer med agent.csv. |
| 66 avvik (58/5/3), 0,482 [0,375; 0,580] | README:14; ERLIG:7,71 | `kilder/c1_bootstrap_f1.md:13`, `c1_tall_likt.md:7` | OK |
| val 0,520, 0,522 på avvik | README:9; ERLIG:34,44; JURY_SP:7 | `kilder/c1_val_kaldstart.md`, `c1_siste_mot_forsok.md:5` (0,5217) | OK |
| V2 0,516, +0,040 [−0,007; +0,095] | README:11; ERLIG:32; JURY_SP:81-82 | `kilder/c1_v2_rullende_2024.md:24`; `benk.txt` V2 2026 0.5161, B-A +0.0399 [−0.007; +0.095] | OK |
| 13 757 saker, 194 selskaper, 37 land, 1 578, 52 906 | README:3,23,25,62; kravrespons:7 | `kilder/omfang.txt:2-3`; 52 906 bare i `state/rapporter/c1_datasjekk_242.md:82` (nivå 2) | OK (52 906 har ikke kilde i pakka, men sha-en står i README) |
| b2 0,365, +0,11 [0,01; 0,22], h1 0,415 [0,30; 0,53], «0,06 av F1» | kravrespons:7,10; ERLIG:28,69-70; JURY_SP:15,23,74,78 | `kilder/c1_enkle_regler_og_hist1.md:13-14`; 0,476−0,415=0,061 | OK |
| 15 av 20 sitat | kravrespons:10; JURY_SP:35 | `kilder/c1_sitat_verifisert.md:1,13` (15/20, 4 delvis, 1 feil) | OK |
| 29–52 s, 41–89 s, 4,8 s | README:43,55 | `kilder/c1_offline_kaldstart.md:35`, `BEGRENSNINGER.md:38`, `levering/JURY_README.md:13`, `kilder/c1_kjoretid.md:11` | OK |
| ERLIG § 1-ablasjonen (15 tall og flagg) og avledede tall (−0,19, +0,07, +0,04, 0,44→0,59, −0,011) | ERLIG:13-24 | `kilder/c1_ablasjon_v2.md:11-15`; differansene regnet på nytt | OK |
| § 4: lt 0,472, ny 0,469, mt 0,465, alle 0,468, base 0,522, krav 0,552 | ERLIG:37-38 | `kilder/c1_siste_mot_forsok.md:5,12-15` | OK |
| § 7 benk A og B (alle celler for 2025 og 2026, snitt, «mot frossen») | ERLIG:84-100 | Primærlogger `arbeid/oppgave_2567/benk.txt` og `oppgave_2568/snitt.log`; `state/rapporter/c1_erlig_eval_tre_aar_2571.md` | OK. Kilden finnes bare utenfor pakka (nivå 2). Teksten sier dette selv («`kilder/`-kopi hvis dommen tar den inn»). |
| Rullende 0,4545/0,5143/0,4762, snitt 0,482; 58 mot 70–99 | JURY_SP:61 | `benk.txt` (frossen); `kilder/tell_aar.txt:3-10` (min 70 i 2020, maks 99 i 2025) | OK |
| 11 av 28 til menneske, 17 urutet ≤ 0,09; USA 0 av 7; 5 nye saker | JURY_SP:31,39 | `kilder/c1_bommene.md:17,26,28` | OK |
| Angrep: F1 0,457, 6 av 16 slipper, 18–27 stemmer, F1 0,39–0,42 | JURY_SP:43; ERLIG:41 | `kilder/c1_titlecase_vakt.md:44-55`: 5 slipper i tabellen, og «Board Knows Best» med 18 gjør 6. F1 0,392–0,422. | OK |
| Grensetabell 0,373–0,532 | JURY_SP:65 | `kilder/TREFFSIKKERHET.md:75,78` | OK |
| Hybrid +0,069 [+0,007; +0,133], 0,545, modell alene 0,538 | JURY_SP:74,81 | `benk.txt` NBIMhybrid 2026; `kilder/c1_nbim_repo_sammenligning_dom.md:22` | OK |

## Ikke sjekket
- Tall inne i lange setninger i ERLIG § 6 og i JURY_SPORSMAL sp. 11–13 er bare sjekket maskinelt (nivå 1 eller 2). Jeg har ikke lest dem i sammenheng.
- Jeg har ikke trent eller kjørt noen modell. Bare agent.csv fra den siste kalde kjøringen (14:50) er lest.

Filer: `arbeid/oppgave_2591/tallsjekk.py`, `arbeid/oppgave_2591/ut.tsv` (795 rader: tall, fil:linje, kilde, status).
