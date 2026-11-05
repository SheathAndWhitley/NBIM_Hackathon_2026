# Case 1 (#2696): demoen fra kald kopi etter manusrettelsene i #2693, MANUS OK, 0 avvik

**Kort:** `sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_kald_2696 --ny` (ny kald kopi, 39 s, rc 0) gir F1 MOT 0,512 (TP 32, FP 35, FN 26), **MANUS OK (15 / 89 / 39)**, FRYSVAKT GRØNN 21 filer, frys 2026-11-05T17:18:18 i linje 5, TALLVAKT GRØNN og ORDVAKT GRØNN. Ny `arbeid/hack/c1/leveranse/demo_utskrift.txt` er committet. Mot utskriften fra #2660 er bare linje 2 endret (tidsstempel 17:55 og kopisti /tmp/c1_kald_2696). Ingen frosne filer er rørt. **Zipen:** den nye utskriften kommer med i jury-zipen når tekststopp-zipen lages (#2549, kl. 19). Jeg har ikke laget noen zip selv. Den gamle utskriften ligger i `arbeid/oppgave_2696/demo_utskrift_for.txt`, loggen i `arbeid/oppgave_2696/demo_ny.log`.

## Manus-tall -> linje i demo_utskrift.txt
| Manus (DEMO_MANUS.md / MUNTLIG.md) | Utskrift-linje |
|---|---|
| F1 0,512 | 4 (`0.512000`), 28 (`F1 MOT 0.5120`) |
| 32 av 58, presisjon 0,478, 35 falske MOT, 26 oversett | 27 (58 MOT), 28 |
| Følg styret: F1 0 | 29 |
| 161 av 1539 med fasit, 10,5 % | 29 (`161 av 1539 (10.5 %)`) |
| Kura Sushi, linje 15, `2033470\|1`, MOT, p 1,0, til_menneske 0, sitat GVG 1.1, NBIM mot | 8–12 |
| LOTTE, linje 89, `2048411\|10`, FOR, p 0,0887, «support the board», NBIM MOT | 14–17 |
| Lundbeck, linje 39, `2038357\|7`, MOT, p 0,2321, til_menneske 1, båndet [0.15, 0.85), sitat GVG 2.1, NBIM FOR | 19–23 |
| MANUS OK | 25 |
| Frys-tid 17:18:18 | 5 (= frysvakta) |

## Tall fra #2693 som ikke står i demo-utskriften
- MUNTLIG.md:22 «164 av 1578 innkomne saker … 10,4 %». Jeg talte i den kalde kopien `/tmp/c1_kald_2696/ut/agent.csv`: 1578 rader, 164 med til_menneske=1 (164/1578 = 10,4 %). Stemmer. Linje 29 i demoen viser bare tallet for sakene med fasit (161 av 1539), og det samsvarer med andre setning i MUNTLIG.md:22.

Avvik: 0.
