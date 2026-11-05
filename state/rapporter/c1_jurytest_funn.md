# Case 1: funn fra jurytesten av zipen (#2348) og hva som ble gjort (#2396, dommer2, 05.11 kl. 15.32)

Alle funn har eier. Rettingene er bare i ikke-frosne filer (ingen av dem står i `arbeid/verktoy/c1_frys.py`).
Etter rettingene: `c1_tallvakt.py` GRØNN (18 filer, 169 påstander, 0 avvik), `c1_tallsjekk.py --bare-ikke` 0 tall uten kilde.
Zipen bygges på nytt kl. 19.30 av sluttsjekken (#1972), så rettingene kommer med der.

| # | funn (fra #2348 / #2347) | status | eier | frist |
|---|---|---|---|---|
| 1 | `c1/leveranse/README.md` og `kravrespons.md` sa «ett kall: `kjor.sh`», som feiler i zipen | **rettet av smed2 (#2391)**: begge sier nå `sh KJOR.sh` i zipen, `kjor.sh`/`demo.sh` bare i repoet. Kontrollert 15.25 | smed2 | 16.00 |
| 2 | gamle dokumentlaget `levering/*.md` peker på 17 `state/rapporter/`-filer som ikke er i zipen | **rettet**: zip-rot-README (`levering/JURY_README.md`, tabellen «Hva som er hva») sier at det er et eldre lag, at `state/rapporter/…` er utviklingsrapporter som ikke er med, og at fire ligger i `kilder/`. Filene selv er beholdt fordi tallvakta leser dem | dommer2 | ferdig |
| 3 | 1,5 GB nedlasting for en sklearn-modell; README sa «ca. 1 min» | **delvis**: README sier nå 1,5 GB og «ett til noen minutter avhengig av nettet». Miljøet byttes IKKE før frysen (ny ZIPTEST ville kreve 1,5 GB disk og 5 min, og risikoen er større enn gevinsten) | dommer2 (besluttet: ikke rettes før 20.00) | ferdig |
| 4 | KJOR.sh skrev «uv sync 0 s» i én kjøring | kosmetisk, ikke rettet. Måler bare klokka rundt `uv sync`; stemmer når bufferen er varm. Ingen jurytall avhenger av den | dommer2 (besluttet: ikke rettes) | ferdig |
| 5 | sidefunn (#2346): `sjekk_treffsikkerhet.sh` sier accuracy agent 95,7 %, følg styret 96,2 % (n 1539), dashbordets kv hack_levert sier 95,39 / 95,71 | ikke i noen jurydokument (grep i `levering/*.md` og `c1/leveranse/*.md`: 0 treff). Jurytallet 96,2 % i kravrespons stemmer med 2x2 (1481/1539). Dashbordtallet må forklares eller rettes av den som satte det (b808382) | dommer | 19.30 |
| 6 | `/tmp/jurypakke_c1.zip` finnes ikke nå (15.20) | etter design: `pakk_jury.sh` sletter zipen først, og smeds sluttsjekk (#2389) stoppet i tallvakta. Bygges på nytt kl. 19.30 | dommer (#1972) | 19.30 |
| 7 | #2347 avvik 1: `levering/KRAVRESPONS.md` sa 176/171 til menneske (gamle tall) | **rettet** til 188 av 1578 / 183 av 1539 | dommer2 | ferdig |
| 8 | #2347 avvik 2 og 3: «bånd låst på val» i `KRAVRESPONS.md` krav 11 og `kjor_agent_real_test2026_LES.md` | **rettet**: kalibrering lært på val, båndet valgt på test-tabellen og sjekket på val (som ERLIG_EVALUERING, EN_SIDE, SLIDE) | dommer2 | ferdig |
| 9 | #2347 avvik 4: `kilder/c1_menneske_terskel.md` teller 66 avvik, ikke 58 MOT | **rettet**: merknad under overskriften med 58-tallene | dommer2 | ferdig |
| 10 | #2347 avvik 6: `levering/TREFFSIKKERHET.md` manglet språkmerknaden om «konfidens < 0,6» | **rettet**: samme merknad som i `kilder/`-kopien | dommer2 | ferdig |
| 11 | #2347 avvik 7: `levering/c1_v1/` (leveranse 1, 228 av 1578) uten forklaring | **rettet**: én linje i `levering/arkiv/LES_KJORING.md`. Mappa er ikke flyttet (ligger i fillista fra kald kopi) | dommer2 | ferdig |
| 12 | #2347 avvik 5: `c1/leveranse/JURY.md:41` og `README.md:11` sier «60 ukjent selskap» (riktig er 60 bare ukjent, 70 i alt, 10 også i båndet) | ikke rettet av meg: smed2 (#2391) og speider (#1975) redigerer de filene nå. Foreslått tekst står i `c1_til_menneske_tall.md` pkt 5 | speider (#1975) | 16.05 |
| 13 | disk 3,8 GB ledig; hver jurytest trenger 1,5 GB | mine kopier er slettet. Resten: #2394 | smed2 (#2394) | 16.00 |

Ikke rørt: frosne filer, `pakk_jury.sh`, `jury_kjor.sh`, `fremmed.sh`, `sluttsjekk.sh`.
