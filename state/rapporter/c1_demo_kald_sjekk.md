# Case 1 (#2660): demoen fra kald kopi mot DEMO_MANUS.md, 0 avvik etter retting

**Kort:** Ny kald kjøring gir F1 MOT 0,512 (TP 32, FP 35, FN 26), og vis_manussaker sier MANUS OK. Kilden `arbeid/hack/c1/leveranse/demo_utskrift.txt` er laget på nytt, så linje 5 nå viser frys 17:18:18. Før rettingen hadde den to feil (se under). **Jury-zipen 5514792 (SISTE_GRONNE, 17:24) har fortsatt det gamle manuset.** Ny zip ved tekststoppen (#2549) må tas etter commit-en fra denne oppgaven.

## Hva jeg kjørte
1. Kald kopi av zipen: jeg pakket ut `SISTE_GRONNE.zip` (= jurypakke_c1_1724_5514792.zip) i /tmp/c1kald_CPos og kjørte `sh KJOR.sh` (71 s, TALLVAKT GRØNN, HOVEDTALL 0.512000). Deretter kjørte jeg `sh arbeid/hack/c1/leveranse/demo.sh`. Resultat: rc 0 og ORDVAKT GRØNN, men utskriften viste **AVVIK FRA MANUS** (treff og menneskesak). Grunnen er at zipen har DEMO_MANUS.md og vis_manussaker.py fra før #2659 (Mobimo linje 276 / Kura linje 15).
2. Repoet med manuset fra #2659: `sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_kald_2660 --ny` (ny kald kopi, 21 s). Resultat: **MANUS OK (15 / 89 / 39)**, FRYSVAKT GRØNN 17:18:18 og TALLVAKT GRØNN. Den nye utskriften står nå i kilden. Den gamle ligger i `arbeid/oppgave_2660/demo_utskrift_for.txt`, loggen i `arbeid/oppgave_2660/demo_ny.log`.

## Feil i kilden, nå rettet
- Linje 5 sa «frys 2026-11-05T17:10:34». Utskriften ble laget kl. 17:18, før frysen ble lagt på nytt 17:18:18 (state/c1_frys.json). Nå står det 17:18:18, likt med frysvakta.
- Utskriften inneholdt «AVVIK FRA MANUS». Manuset og vis_manussaker ble rettet i #2659, men utskriften ble ikke laget på nytt etterpå. Nå står det «MANUS OK».

## Tall og saker fra manuset, med linje i demo_utskrift.txt (den nye)
| Manus | Utskrift-linje |
|---|---|
| F1 0,512 | 4 (`0.512000`), 28 (`F1 MOT 0.5120`) |
| 32 av 58, 48 % (presisjon 0,478), 35 falske MOT, 26 oversett | 27 (58 MOT), 28 (MOT funnet 32, falsk MOT 35, MOT mistet 26, presisjon 0.478) |
| Følg styret: F1 0 | 29 |
| 161 av 1539, 10,5 % | 29 (`161 av 1539 (10.5 %)`) |
| Kura Sushi, 28.01.2026, linje 15, `2033470\|1`, MOT, p 1,0, til_menneske 0 | 8–9 |
| Kura-sitatet «A majority of shareholder-elected …» og NBIMs begrunnelse fra 2021 | 10 |
| NBIM stemte mot (Kura) | 12 |
| LOTTE, 20.03.2026, linje 89, `2048411\|10`, FOR, p 0,0887 → «0,09», til_menneske 0 | 14–15 |
| «Our starting point … support the board» | 16 |
| NBIM stemte MOT, vedtekter (LOTTE) | 17 |
| Lundbeck, 18.03.2026, linje 39, `2038357\|7`, MOT, p 0,2321 → «0,23», til_menneske 1, båndet [0.15, 0.85) | 19–20 |
| Lundbeck-sitatet «Board members should devote sufficient time …», begrunnelse fra 2021 | 21–22 |
| NBIM stemte FOR (Lundbeck) | 23 |
| Frys-tid | 5 (17:18:18 = frysvakta) |

## Tall i manuset som ikke står i demo-utskriften
Disse står med kilde i manusets tabell «Tallkilder». Jeg har sjekket dem på nytt mot den kalde kjøringen:
- FN 18 avgjort av maskinen / 8 sendt til menneske, FP 3 / 32: `telling.py /tmp/c1_kald_2660/ut/agent.csv` gir «FN maskin 18 menneske 8» og «FP maskin 3 menneske 32». Stemmer.
- Usikkerhet 0,40–0,62: `leveranse/kilder/c1_repo4_tall_2592.md:3` sier [0,400; 0,621]. Stemmer.
- «96 av 100»: `leveranse/kilder/TREFFSIKKERHET.md:16` sier at følg styret gir 96,2 %. Stemmer.

Avvik: 0 i kilden etter retting. Zipen 5514792 er fortsatt rød på manuset, men det er gammelt innhold og ingen ny feil. Det rettes når #2549 lager ny zip.
