# Case 1: én-sideren og beslutningsstøtten lest som jury (#2190)

Speider, 05.11 ca. 13:35. Modell og prediksjoner er ikke rørt. `python3 -I arbeid/verktoy/c1_tallvakt.py`: OK (14 filer, 139 påstander, 0 avvik).

**Sjekket og i orden:** hovedtallet er F1 på MOT 0,476 [0,36; 0,59], med «følg styret» F1 0 og accuracy 96,2 % mot agentens 95,7 % rett ved siden av.

**Endret i `arbeid/hack/levering/EN_SIDE.md`:**
- #2183-funnet manglet. Nå står det: 56 av 58 MOT er stemmer mot styrets egne forslag, og 29 av 30 treff er der. «Aksjonærforslag = MOT» kan finne høyst 2 av 58 (`c1_forslagsstiller.txt`).
- Avsnitt 4 (til menneske) var en tekstblokk med henvisning til den gamle `--til-menneske`-regelen. Nå er det en tabell med fire rader: 183 av 1539 (11,9 %), 32 av 58 MOT blant dem, 41 av 58 / F1 0,828 som øvre grense mot 0,269 som gulv, og 17 av 58 som ingen ser. Kilden er `kjor_agent_real_test2026.txt`. Lesetiden (62 t) er merket som antatt.
- «17 av 58 ser ingen» sto tre ganger, nå står det én gang. Begrensning 1 og 3 og accuracy-avsnittet er kortet.

**Endret i `BESLUTNINGSSTOTTE.md`:**
- #2183-funnet er lagt inn som eget avsnitt øverst.
- «Ny stikkprøve av sitatene kommer i #2012» var et løfte som ikke er holdt. Det er byttet ut med det målte: 15 av 20 (#2115).
- Fjernet setningen om den gamle N-PX-versjonen. Den forvirrer juryen.

**Flyttet:** `KJORING_til_menneske_10.txt` og `_15.txt` til `levering/arkiv/`, med `LES_KJORING.md` som forklarer hvorfor. Filene var fra den gamle prosentregelen på 1246 saker (F1 0,474 på avvik, 15,1 % til menneske), og ingen md-fil eller ingen skript i pakka viser til dem. Kan flyttes tilbake.

**Gjenstår (ikke mitt):** én-sideren har nå 659 ord, mot 590 før. Den er fortsatt over én side ved utskrift. Tabellen over treffsikkerhet kan kuttes hvis det trengs plass, fordi TP/FP/FN står i hovedtabellen. Etter frysen kl. 16 må tallene sjekkes på nytt (#1975).

Merk: `arbeid/` er gitignorert, så endringene ligger bare på disk og er ikke committet.
