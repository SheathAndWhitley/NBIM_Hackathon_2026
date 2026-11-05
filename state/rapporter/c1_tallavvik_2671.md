# Case 1 (#2671): tall-avvik fra tallsjekk #2624 rettet i JURY.md, ERLIG og rot-README

Skript: `arbeid/oppgave_2671/rett.py` (23 erstatninger, hver sjekket unik, backup `arbeid/oppgave_2671/backup_*`).
Overlapp: #2661/#2669 hadde alt rettet JURY.md:5 («like over»), KI i pkt. 2 og modellnavn i JURY:4/9/16. #2653 hadde rettet ERLIG:53.

| Pkt #2624 | Rettet til |
|---|---|
| 1 «under målet» | var alt rettet (#2661, #2653) |
| 2 rot-README = `levering/JURY_README.md:39-40` | p_mot-grense 0,232, rå 0,923 (KJORING.txt). Samme tall rettet i `levering/BESLUTNINGSSTOTTE.md:81,83`; `levering/JURY_SPORSMAL.md:86` merker 0,83/176 flagg som eldre frossen |
| 3 JURY:29 avvik-F1 | 0,529 [0,42; 0,63] for repo4, 0,482 merket eldre frossen. Også ERLIG:7 |
| 3 JURY:78 ruting | 101 usikre, 61 ukjent, 1 instruks (+1 annen vakt), kilde repo4-kjøring 17.03 |
| 3 JURY:82 falske | «Repo4 har 35 falske MOT»; 26/22 av 38 merket som analyse på eldre frossen |
| 4 KI [0,36; 0,59] | var alt rettet (#2669) |
| 5 JURY:24 30/28 | repo4 32/26 og 18 usette først; 30/28/17 merket eldre frossen |
| 6 modellnavn | ERLIG:3 og tabellraden ERLIG:71 sier repo4 |

Fant i tillegg og rettet i JURY.md: :6 «17 av 28 ≤ 0,09» → 18 av 26 ≤ 0,11; :34 «alle 9 auto-flagg riktige» → 11 av 14 (repo4, som tabellrad 47 og BESLUTNINGSSTOTTE); tabellen :46-47 markerer nå repo4-raden som standard og frossen-raden som eldre; :50 10,5 av 100 og 29 MOT i bunken; :61 og :82 «den frosne agenten står» → repo4 byttet inn 17:02; :63 «test brukes aldri til å velge» → «avgjør aldri alene et bytte» (sann mot :4).

Sjekker etterpå: tallvakt 195 påstander 0 avvik OK; frysvakt GRØNN (21 filer); sjekk_rod.sh punkt 2-4 GRØNN, punkt 5 RØD på `SVAKHETER.md:77`, som er en falsk positiv: linja er engelsk og sier «older 0.476», sjekken leter bare etter «eldre». Til dommer2 (#2668).
Ikke rettet: `c1/leveranse/kilder/*` og `NESTE_VERSJON.md:91`/`DEMO_MANUS_5min:40` (0,919 er frossen-tall i kilde/manus, #2685 og #2693 eier dem).
