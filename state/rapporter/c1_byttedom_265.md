# Case 1 byttedom (ordre #265, oppgave #2570): **BYTT** til repo4, på vilkår om grønn pakke innen 18:45 — dommer2, 05.11 17:02

## Dommen
**BYTT.** Kandidaten repo4 (frossen #2044 miks h2 + fire historikktrekk fra NBIM-repoet: prev_same_item,
prev_same_person, prev_meeting_any_dev, hist_type_dev_rate) består byttregelen som ble fastsatt før målingen,
og jeg har gjenskapt alle tallene fra kald kopi. Byttet er betinget: pakken må være grønn (tallvakt 0 avvik,
frysvakt, frys_diff LIK, kald kopi gir 0,5120) senest 18:45 (hard port 19:00, se «Porten» under). Er den ikke det, rulles alt tilbake etter
byttplanen #2572, og frossen #2044 står med 0,476. Da gjelder STÅR-sporet nederst.

## Porten (ordre #266 hull 2, oppgave #2590, dommer2 17:05)
**PORT:** BYTT står bare hvis byttregelen holder (gjort, over) OG `bytt.sh --utfor` → `sluttsjekk.sh` → `pakk_jury.sh`+`test_jury_zip.sh` → generalprøve av demoen fra kald kopi (`fremmed.sh` + `demo.sh`, F1 MOT 0,5120, TP 32 FP 35 FN 26) er grønn innen 19:00, OG `DEMO_MANUS.md`, `JURY_SPORSMAL.md` sp. 13 og 19 og `ERLIG_EVALUERING.md` §7 er oppdatert til repo4 (sp. 13/19 og §7 må si at repo4 besto en regel satt før måling, ikke lenger «frossen står»), OG README krediterer lagkameratenes `stemmeagent/ballot.py` (hybridrepoet, R pkt. 5 «credit any copied code»; kommentaren «arrangørens repo» i `modell_repo4.py:71` rettes til «lagets hybridrepo»); mangler ett av leddene kl. 19:00, rulles det tilbake etter byttplanen, og frossen 0,476 står. Smedens mål er 18:45, så det er 15 min til tilbakerulling før porten. Grønn kl. 19:00 verifiseres av dommer (#2596), ikke av den som byttet.

## Regelen (satt før måling, se c1_byttregel_forhand.md)
Snitt F1 MOT over test 2024/2025/2026 minst +0,02 over frossen (0,4817), og intet år mer enn 0,02 under.
Val = året før test, trening = årene før val. Alt valgt på val, testår kjørt én gang.

## Gjenskapt fra kald kopi (arbeid/oppgave_2570/kald/, egen kopi av data og skript, 05.11 16:58–16:59)
Måler: `maaler_aar.py --score mot`. Data sha256 71ba5135.
| modell | 2024 F1 (TP/FP/FN) | 2025 F1 (TP/FP/FN) | 2026 F1 (TP/FP/FN) | snitt | mot frossen |
|---|---|---|---|---|---|
| frossen #2044 | 0,4545 (30/14/58) | 0,5143 (45/31/54) | 0,4762 (30/38/28) | 0,4817 | – |
| **repo4** | **0,5057 (44/42/44)** | **0,5309 (43/20/56)** | **0,5120 (32/35/26)** | **0,5162** | **+0,0345** |

Per år, repo4 minus frossen, parret klyngebootstrap på selskap (2000 trekk): 2024 +0,051 [−0,065; +0,160],
2025 +0,017 [−0,031; +0,068], 2026 +0,036 [−0,008; +0,085]. Snitt tre år +0,0345 [−0,005; +0,078];
4 % av trekkene gir repo4 under frossen, 23 % under +0,02.

Alle seks prediksjonsfiler er byte-like filene fra smed4 (#2567), #2490, dommerens #2496 og min #2575.
Krav 1: +0,0345 ≥ +0,02. Krav 2: verste år +0,017 (2025), ingen år under. **Begge krav oppfylt.**
Ingen av de seks andre kandidatene (person, V1, V1p, V2, NBIM-hybrid, snitt3 fra #2568) består; alle taper
0,04–0,05 i 2024 eller ligger under +0,02 i snitt.

## Hvorfor jeg likevel dømmer, og ærlige forbehold
1. **Regelen ble satt før de avgjørende tallene.** 2026-tallet til repo4 (0,5120) var kjent fra #2490 kl. 16:13
   da regelen ble skrevet; 2026 er altså året repo4 ble funnet på, ikke et friskt testår for den. Årene som
   avgjør er 2024 og 2025, og de ble målt etter regelen: +0,051 og +0,017, snitt +0,034. Det holder alene.
2. **Fjerde år 2023 (#2573, utenfor regelen):** repo4 +0,005 mot frossen. Fire år: +0,027, aldri under frossen.
3. **Gevinsten er ikke statistisk sikker.** KI for snittet krysser null. Det skal stå i ERLIG_EVALUERING med
   tallene over. Juryen vekter ærlig metode; et bytte etter en forhåndsregel med åpen KI er bedre metode enn
   et bytte på magefølelse, og bedre enn å la en regel vi selv satte stå ubrukt når den slår ut.
4. **Sju kandidater ble sammenlignet.** Én besto. Med 7 kandidater og krav om snitt +0,02 og ingen år under −0,02
   er tilfeldig bestått lite sannsynlig, men ikke null; det er grunnen til at regelen krever hvert år, ikke bare snittet.
5. **Lekkasje- og protokollsjekk** (#2575, seks punkter grønne): trening bare på år før val, terskel og rutingsbånd
   på val, ingen forbudte kolonner, historikk bare fra tidligere møter, repoets base_rate er én skalar fra
   2019–2023 (før alle tre testår).
6. **Risikoen ligger i pakken, ikke i modellen.** Frysen gikk kl. 16; byttet rører 24 tekster og ca. 180 tall.
   Derfor er dommen betinget av grønn pakke innen 18:45, med tilbakerulling etter byttplanen hvis ikke.

## Vilkår for at byttet står (smedens oppgave)
- Følg `state/rapporter/c1_byttplan_2572.md` steg 0–5 (`arbeid/hack/c1/bytte/bytt.sh`, tørt først, så `--utfor`).
- Grønt betyr: tallvakt 0 avvik, frysvakt og `frys_diff.sh --kilde` LIK mot ny fasit, kald kopi (`fremmed.sh`/`kald.sh`)
  gir F1 MOT 0,5120 med TP 32 FP 35 FN 26 på test 2026, `sluttsjekk.sh` grønn, ny jury-zip testet.
- Hovedtallet blir 0,512 (test 2026). Tre-års-tabellen i ERLIG_EVALUERING viser frossen og repo4 side om side,
  med KI og setningen «regelen ble fastsatt før måling; 2024 og 2025 var ukjente, 2026 var kjent».
- Ikke grønt kl. 18:45: rull tilbake (byttplanens «Tilbake»), meld på tavla, og frossen står. Ingen halvveis pakke.

## STÅR-sporet (gjelder bare hvis tilbakerulling)
Da går tallene over inn i NESTE_VERSJON og ERLIG_EVALUERING som «forsøkt og avvist av tid, ikke av regelen»:
repo4 besto regelen (snitt +0,0345, verste år +0,017), men byttet ble ikke grønt før tekststopp.

## Gjenskap
`bash arbeid/oppgave_2570/kald/kjor.sh` (ca. 20 s, seks kjøringer), deretter i samme mappe
`python3 -I maaler_aar.py <full|repo4>_<år>_test.csv y<år> --data real --score mot` og
`python3 -I diff_ki_aar.py full_<år>_test.csv repo4_<år>_test.csv <år>`;
tre-års-KI: `python3 -I arbeid/oppgave_2567/ki_snitt.py` med de seks filene.

## Endelig
**BYTT ENDELIG** (dommer2 #2603, 18:45): repo4 er levert modell; #2592 utført, #2649 kald start grønn (F1 MOT 0,5120, TP 32 FP 35 FN 26, TN 1446), #2596 sine fire tekstfeil rettet, egen kjøring 18:44 gir frysvakt GRØNN (21 filer, frys 17:18:18) og tallvakt 0 avvik (32 filer, 197 påstander), siste grønne zip er `jurypakke_c1_1827_0e3b14b.zip` (sha256 98257a6e…, SISTE_GRONNE.zip), sluttsjekk GRØNN 18:27 (#2740). Ingen tilbakerulling; STÅR-sporet gjelder ikke.
