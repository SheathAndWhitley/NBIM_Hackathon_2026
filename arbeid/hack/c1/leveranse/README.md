# Stemmegivningsagenten (Case 1, FinTech Hackathon H2026)

> **Oppdatert grunnlinje (5.11 kveld):** Den sterkeste enkle regelen er «gjenta NBIMs forrige beslutning på samme sak eller person» (`arbeid/hack/c1/grunnlinje_gjenta_forrige.py`). Den gir F1 på MOT 0,42 / 0,51 / 0,51 for 2024–2026, snitt 0,48, mot agentens 0,51 / 0,53 / 0,51, snitt 0,52: agenten er bedre i snitt, men lik regelen i 2026. Der dette dokumentet sammenligner med regel b2 (0,365), er det en svakere regel. Lekkasjetesten: `arbeid/hack/c1/lekkasjetest.py`. <!-- tallvakt: ignorer: grunnlinje, ikke hovedtall -->

Agenten markerer sakene der NBIM sannsynligvis stemmer mot styret, i alle sakstyper og markeder i NBIMs stemmedata (194 selskaper, 37 land), med kalibrert P(MOT)
per sak og et ordrett sitat fra NBIMs Global Voting Guidelines (GVG). Saker med kalibrert P(MOT) i [0,15; 0,85), ukjent
selskap eller sakstype, datafeil eller instruksjonslignende tekst går til et menneske. Fasiten er NBIMs egne stemmer
(real_votes), og vi splitter på tid. Kravresponsen står i `kravrespons.md`.

> **Hovedtall:** F1 **0,512 på MOT mot styret**, 95 % KI [0,40; 0,62], test 2026 på NBIMs egne stemmer (real_votes, 1539 saker med fasit,
> 58 MOT mot styret). P 0,48, R 0,55 (TP 32 FP 35 FN 26). Følg styret har 96,2 % accuracy, men predikerer aldri MOT (TP 0), så F1 på MOT er 0; det er gulvet. MOT er positiv klasse fordi de 58 av 1539 sakene der NBIM stemmer mot styret, er de som krever arbeid. Grensen er valgt på val 2025 (0,530); 2026 ble brukt til å finne repo4, så 2026 er ikke et friskt testår (rutingsbåndet er valgt ut fra test og sjekket på val); repo4 (frossen modell + fire historikktrekk) ble deretter byttet inn etter regelen på tre testår (2024–2026).
> Til menneske: 164 av 1578 saker inn (10,4 %). Reproduser: `sh KJOR.sh` fra roten av repoet.
> Vi leverer repo4 (frossen modell + fire historikktrekk), ikke V2. V2 er en tidligere variant (0,516 på test), men den ble målt på test etter frysen uten en regel satt før måling, og avstanden til V1 (en eldre variant, ikke den frosne) er innenfor støyen (+0,040, KI [−0,007; +0,095]); se `JURY_SPORSMAL.md` sp. 19. <!-- tallvakt: ignorer: V2, ikke hovedtall -->
> Etter modellfrysen testet vi, etter en regel satt før måling (snitt minst +0,02 over frossen på F1 MOT over tre rullende testår 2024–2026, intet år under −0,02), kandidaten repo4 (frossen + fire historikktrekk): 0,5057/0,5309/0,5120 mot frossen 0,4545/0,5143/0,4762, snitt +0,0345, verste år +0,017, KI for snittet [−0,005; +0,078], og kontrollagenten (en egen agent som ikke målte kandidatene) dømte BYTT kl. 17:02 på vilkår om at hele pakken med repo4 kjørte feilfritt fra kald start, med samme tall, innen 18:45. Det gjorde den (se `ERLIG_EVALUERING.md` § 7). <!-- tallvakt: ignorer: byttedom, ikke hovedtall -->
> **Om de andre tallene i pakken:** V2 0,516, NBIM-hybrid 0,545 og 0,529 er målt på test etter frysen uten en regel satt på forhånd, og står bare som sidetall. Repo4 er levert fordi den besto regelen satt før måling (snitt over 2024–2026, avgjort av 2024 og 2025, som ble målt etter at regelen var skrevet), ikke fordi 0,512 er høyest. Alle kandidater målt etter byttet står i `KANDIDATER.md`; ingen nådde +0,02. <!-- tallvakt: ignorer: sidetall, ikke hovedtall -->
> **Største forbehold:** en del av F1 kommer fra NBIMs egne tidligere stemmer i samme sesong; for den eldre frosne modellen var det ca. 0,06; repo4 uten samme-sesong-historikk gir 0,396 (arkitektens måling, ikke reprodusert av kontrollagent), så hele forspranget over den eldre frosne kommer fra samme-sesong-historikk. Uten den historikken er F1 0,415 [0,30; 0,53] (målt på den frosne modellen), bare +0,05 over regel b2 (0,365). NBIM selv kjenner sine avgitte stemmer; en ekstern bruker som bare ser publiserte stemmer, får golvet (`ERLIG_EVALUERING.md` § 2, `JURY_SPORSMAL.md` sp. 18). <!-- tallvakt: ignorer: sidetall, ikke hovedtall -->

Testårstallene gjenskapes med én linje fra pakkas rot (`--rask` måler bare de lagrede svarfilene, uten flagg trenes repo4 på nytt per testår, ca. 10 sek):

    bash arbeid/hack/c1/leveranse/verktoy/testaar.sh

Forventet siste linje i utskriften (kald kopi 05.11, #2733; de tre linjene over den viser TP/FP/FN per år):

    F1 MOT mot styret: 2024 0.5057  2025 0.5309  2026 0.5120  snitt 0.5162

Hvorfor MOT allerede ved kalibrert P(MOT) ca. 0,19: MOT er sjelden (58 av 1539), og grensen (rå 0,919 for repo4) er valgt for F1 på val, ikke for 50 % sikkerhet. <!-- tallvakt: ignorer: grense, ikke hovedtall -->
Detaljer til hovedtallet: KI-en over er klyngebootstrap per selskap; bootstrap over rader i `c1/tall_tabell.md` gir [0,40; 0,62].
Sidetall: avvik fra styret (66 avvik: 58 MOT, 5 AVSTÅ, 3 andre) 0,529 [0,42; 0,63] (frossen 0,482). Rutingen til menneske er 101 usikre med kalibrert
P(MOT) i [0,15; 0,85), 61 ukjent selskap og 1 instruks (+1 annen vakt); av de 1539 med fasit er 161 rutet (10,5 %), målt fra kald kjøring 05.11 kl. 17.03 (#2592).
Kommandoen er `sh KJOR.sh` fra roten av repoet (se under).

## Hvilken data
Bare arrangørens filer fra 05.11 er brukt. Sjekk med `shasum -a 256` før du kjører; avviker summen, får du andre tall.

| fil | sha256 | rader (uten topptekst) | brukt til |
|---|---|---:|---|
| `state/opplastet/20261105_114241_real_votes.csv` | `71ba5135e7ba9d64c943f158bb510ffab53f34203f4c2875fc43352419e525e6` | 13 757 (2019–2026; test 2026: 1 578, 1 539 med fasit) | trening, val, test, hovedtall |
| `arbeid/hack/c1/data_off/real_test_input.csv` (avledet, uten fasit) | `1e0e22f86bbf21eafa406742d59643d3e40271dcf19e6d152e5f5070ab63de20` | 1 578 | agentens input på test 2026 |
| `state/opplastet/20261105_114240_npx_votes.csv` | `fa2cc588e5e2dbd1209102fe6bf5273c5a890457111d63d63a52ca9a403f6aa0` | 52 906 | ikke i hovedtallet (`ny_data/npx_votes.csv`) |

Egen SEC-skraping (N-PX-XML), Vanguard-, iShares- og SPDR-data er ikke med. De leses ikke av agenten eller måleren.
Riktige tall fra kald start: TP 32 FP 35 FN 26 TN 1446, F1 MOT 0,512, accuracy 96,0 % (følg styret 96,2 %).

## Ett kall reproduserer hovedresultatet

```bash
sh KJOR.sh     # fra roten av repoet
```

Trenger bare [uv](https://docs.astral.sh/uv/). `KJOR.sh` sjekker sha256 for de frosne filene (`FROSNE_SHA256.txt`), lager et eget
låst miljø (`.venv_kjor`, `uv sync --frozen`), kopierer `ny_data/real_votes.csv` til fast sti og lager testinndata, kjører hele agenten
(`arbeid/hack/levering/kjor_agent.py`) under `env -i`, måler test 2026 med `arbeid/hack/c1/maaler_offisiell_v3.py --score mot`
og kjører tallvakta (`arbeid/verktoy/c1_tallvakt.py`) mot tekstene. Kjøretiden er under ett minutt med pakkene i uv-cachen (`BEGRENSNINGER.md` pkt. 8).

**Les linja `HOVEDTALL F1 MOT mot styret`; det er hovedtallet.** Linja `SCORE 0.529412` lenger opp er IKKE hovedtallet: den er F1 på alle avvik fra styret, AVSTÅ medregnet (66 saker). Utdraget under er fra macOS; Linux gir 0,520 (TP 33 FP 36 FN 25), se README i roten. <!-- tallvakt: ignorer: plattformtall -->

```
  avvik: TP 36 FP 34 FN 30  P 0.5143  R 0.5455  F1 0.5294  PR-AUC 0.5368
  MOT mot styret: TP 32 FP 35 FN 26  P 0.4776  R 0.5517  F1 0.5120  (58 i fasit)
SCORE 0.529412
```

Agentens svar ligger i `ut/agent.csv`.

**Egne saker** (etter `sh KJOR.sh`, fra roten): `.venv_kjor/bin/python arbeid/hack/levering/kjor_agent.py --ut <tom mappe> [--csv saker.csv | --sak '<json>']`. Den gir `agent.csv` med stemme, kalibrert P(MOT), til_menneske (båndet [0,15; 0,85) pluss vaktene over), rutingsgrunn, GVG-punkt og ordrett GVG-sitat, og måler på test 2026 når fasit finnes.

## Begrensninger
Se `BEGRENSNINGER.md` (hovedmodellen på real_votes) og `ERLIG_EVALUERING.md`. Løsningen stemmer ikke. Den gir forslag, og et menneske beslutter.

## Datakilder
- **Hovedtallet (F1 0,512 på MOT mot styret):** `real_votes.csv` er NBIMs offentlig publiserte stemmer (https://vd.nbim.no/),
  utlevert som fil av arrangøren på hackathonet 05.11 (13 757 saker, 194 selskaper, 2019–2026). Fila er arrangørens,
  ikke vår nedlasting. `npx_votes.csv` fra samme pakke brukes ikke i hovedtallet.
- NBIM Global Voting Guidelines, sitert ordrett av agenten (påvirker ikke prediksjonen):
  https://www.nbim.no/en/responsible-investment/voting/global-voting-guidelines/
- NBIMs posisjonsnotater, brukt av sitatlaget: https://www.nbim.no/en/responsible-investment/position-papers/
- Måleren `maaler_offisiell_v3.py` er vår egen (fasit = `nbim_vote`/`against_board` i real_votes).
- Ingen andre data enn arrangørens filer over og NBIMs offentlige retningslinjer.
- Kreditering: se «Kilder, kreditering og AI-bruk» i README i roten.

## AI-verktøy
- **Claude Opus 5.5 (Anthropic) via Claude Code:** et lag AI-agenter skrev all kode, hentet og undersøkte dataene,
  laget måleren, fant lekkasjen i `managementRecommendation`, testet modellene og skrev denne README-en og kravresponsen.
  Hovedtallet og tallene i tabellene er målt på nytt av en egen kontrollagent («dommer») fra kald kopi; noen få tall finnes bare i kjøreloggen (se «Hull vi kjenner» i `JURY_SPORSMAL.md`).
- **Ingen språkmodell kjøres i hovedresultatet.** `kjor_agent.py` (snitt av logistisk regresjon og LightGBM, modellen (internt kalt repo4: den frosne «miks h2» pluss fire historikktrekk)) ga samme tall i to uavhengige
  kjøringer (den andre av kontrollagenten). Bootstrap-KI har fast seed (0).
