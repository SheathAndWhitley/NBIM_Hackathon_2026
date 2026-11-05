# Case 1: stemmeagenten, kjør fra en ren kopi

> **Hovedtall (#231, frosset modell repo4 = frossen modell + fire historikktrekk, byttet 17:03 etter byttedom #2570):** F1 **0,512 på MOT mot styret**, 95 % KI [0,40; 0,62],
> test 2026 på NBIMs egne stemmer (real_votes, 1539 saker med fasit, 58 MOT mot styret; P 0,478, R 0,552,
> TP 32 FP 35 FN 26). Målt med `c1/maaler_offisiell_v3.py --score mot` (#2087, dommer kald kopi #2090). Val 2025: 0,530 [0,42; 0,64].
> *Avvik:* 0,5294 (avvik fra styret, 66 saker: 58 MOT, 5 AVSTÅ, 3 andre, KI [0,42; 0,63], #2592) er et sidetall, ikke hovedtallet.
> Følg styret: F1 0.
>
> **Hvorfor ikke accuracy:** agenten har accuracy **96,0 %**, *lavere* enn følg styret (**96,2 %**), fordi bare 58 av 1539
> saker (3,8 %) er MOT og følg styret aldri sier MOT. 2x2 (TP 32 FP 35 FN 26 TN 1446), R 0,552, P 0,478:
> [`TREFFSIKKERHET.md`](TREFFSIKKERHET.md) (#2175).

**Juryens dokumenter ligger i to mapper (#2341).** Les disse først:
- **Kravresponsen, 1 side etter regelverkets mal:** [`c1/leveranse/kravrespons.md`](../c1/leveranse/kravrespons.md) (`arbeid/hack/c1/leveranse/kravrespons.md`).
- **Svar på juryens tre spørsmål:** [`c1/leveranse/JURY.md`](../c1/leveranse/JURY.md) (`arbeid/hack/c1/leveranse/JURY.md`).
- **Kilder med URL, kreditering av ekstern kode og AI-bruk:** [`c1/leveranse/README.md`](../c1/leveranse/README.md) (`arbeid/hack/c1/leveranse/README.md`), bare der.
- **Funn på én slide:** [`SLIDE.md`](SLIDE.md).

> **Hvor du står (#2328):** alle kommandoer under kjøres fra **roten av repoet** (mappa med `arbeid/` og `state/`,
> her kalt landsbymappen), ikke fra inne i `levering/`. Mappa `levering/` alene er ikke nok: `fremmed.sh` finner
> repo-roten tre nivåer opp og trenger modellen, dataene og målerne derfra. Har du bare `levering/`, stopper
> begge skriptene med «FEIL STED: fant ikke repo-roten …» (utgang 6) og sier hvor du skal stå (#2339).

Kravresponsen er `c1/leveranse/kravrespons.md` over. De eldre, lengre utkastene `EN_SIDE.md` og `KRAVRESPONS.md` i utviklingsmappa er ikke med i jury-zipen.

Én kommando fra landsbymappen (krever bare `uv`, ingen nett hvis uv-cachen finnes):

    sh arbeid/hack/levering/fremmed.sh /tmp/fremmed

Det skriptet gjør:
1. Kopierer bare det agenten trenger til `/tmp/fremmed` med samme relative stier. Bare arrangørens data
   (ordre #242; gammel N-PX-/skrapedata ligger i `hack/c1/arkiv/gammel_data/` og brukes ikke):
   `kjor_agent.py` og real_votes-delene (#2053, #2094): `levering/c1_real.py`, modellen `oppgave_2044/train.py`,
   vernet `oppgave_2047/vern.py` + `oppgave_2046/case1_mot.py`, `state/opplastet/..._real_votes.csv`,
   `hack/c1/data_off/real_test_input.csv` og `maaler_offisiell_v2.py`/`_v3.py` (filstien til dataene pekes til kopien).
2. Lager eget uv-prosjekt der med låste avhengigheter (`pyproject.toml` + `uv.lock` fra modellen,
   `uv sync --frozen`): Python >= 3.13, lightgbm, scikit-learn, numpy, pandas, scipy.
3. Kjører `kjor_agent.py` under `env -i` (bare HOME, PATH=.venv/bin:/usr/bin:/bin, LANG) og
   skriver tida. Ut: `/tmp/fremmed/ut/agent.csv`, `pred_maaler.csv`, `KJORING.txt`.

Forventet (test 2026 på NBIMs egne stemmer, 1578 saker inn, 1539 med fasit), standardkjøring #2132:
**HOVEDTALL F1 MOT mot styret 0,5120:** målerlinja `MOT mot styret: TP 32 FP 35 FN 26 … F1 0.5120`.
Linja `SCORE 0.529412` er IKKE hovedtallet: den er F1 på alle avvik fra styret, AVSTÅ medregnet (66 saker), og står der bare fordi rundens måler krever den.
F1 0,5294 er avvik fra styret (66 avvik: 58 MOT, 5 AVSTÅ, 3 andre), 164 av 1578 saker (10,4 %) til menneske, 161 av 1539 med fasit (10,5 %). Agenten brukte 22 s i #2132 (28 s totalt med uv sync i #2094).
Det som står sist, «TALLVAKT GRØNN», betyr at tallene i pakka stemmer med den kalde kjøringen.
Samme kjøring med måling: `bash arbeid/hack/c1/leveranse/kjor.sh` (fra landsbymappen, ca. 35 s). Se etter linja
`MOT mot styret: … F1 0.5120`; linja `SCORE 0.529412` er igjen avvik fra styret inkl. AVSTÅ, et sidetall.

Hovedtallet er F1 0,512 [0,40; 0,62] på MOT mot styret (test 2026, måler v3 `--score mot`, #2087, #2095).

Egne saker (kjøres i `/tmp/fremmed` etter `fremmed.sh`): `.venv/bin/python arbeid/hack/levering/kjor_agent.py --csv saker.csv --ut DIR`
med samme kolonner som `arbeid/hack/c1/data_off/real_test_input.csv`, eller én sak (prøvd, gir FOR med sitat NBIM 0.0.3):

    .venv/bin/python arbeid/hack/levering/kjor_agent.py --ut /tmp/en_sak --sak '{"meeting_id": "2031740", "item_no": "1", "company_id": "537900", "company": "Fraser & Neave Holdings Bhd.", "country": "Malaysia", "market": "EM", "meeting_date": "2026-01-22", "proposal_text": "Approve Final Dividend", "proposal_type": "DIVIDEND", "proponent": "Management", "mgmt_rec": "FOR"}'

Påkrevde felt: meeting_id, item_no, company_id, meeting_date, proposal_text, proposal_type, proponent (pluss helst mgmt_rec, country, market).
Mangler et felt, svarer agenten FOR og sender saken til menneske med «kan ikke vurderes: mangler felt». Svaret står i `DIR/agent.csv`.
Kjøringen skriver også testtallene for 2026 til skjermen (modellen lastes på nytt hver gang); de gjelder ikke saken din.

## Sjekk tallene selv

Én kommando, fra landsbymappen eller roten av den kalde kopien (ca. 10 s):

    sh arbeid/hack/levering/sjekk_treffsikkerhet.sh [UTMAPPE]

Skriptet kjører agenten på nytt på hele test 2026 fra rådata (ikke den lagrede prediksjonsfila), teller 2x2 for
MOT mot styret selv mot fasit i real_votes-fila (uten måleren), og skriver accuracy agent mot følg styret,
recall/presisjon/F1 på MOT, antall til menneske og sha256 mot den frosne fila `d02cf884…4a0c`.
Forventet: TP 32 FP 35 FN 26 TN 1446, accuracy 96,0 % (følg styret 96,2 %), F1 0,512 på MOT, 164 av 1578 til menneske.
Accuracy er høy for alle fordi bare 58 av 1539 saker er MOT; følg styret har høyest accuracy og finner null MOT.
Utgang 0 = stemmer, 3 = annen 2x2, 5 = annen sha.

## Send til menneske

Standard: saken går til et menneske når kalibrert P(MOT) ligger i [0,15; 0,85) (kalibreringen er lært på val 2025, aldri på sakene som vurderes), og i tillegg ved ukjent selskap eller sakstype, datafeil, instruksjonslignende tekst, ikke-latinsk eller uvanlig skrift i forslaget og MOT uten sitat. Kjente svakheter (rare saker, #2264): ikke-engelsk tekst med latinske bokstaver (norsk, fransk) rutes riktig, men med den villedende grunnen «instruksjonslignende tekst»; og står samme id to ganger, rutes bare den andre raden. Se `arbeid/hack/c1/leveranse/BEGRENSNINGER.md` pkt. 3. Båndet endres med `--baand LO,HI`; den gamle logit-regelen finnes med `--til-menneske PROSENT`.

Test 2026 på NBIMs egne stemmer, levert modell repo4 (#2044 miks h2 + 4 repotrekk), faktisk standardkjøring (#2592, kalibrert P(MOT) i båndet [0,15; 0,85) pluss ukjent selskap/type, injeksjon, datafeil og MOT uten sitat). Positiv klasse: **MOT mot styret, 58 saker av 1539** (ikke de 66 avvikene). Inn 1578 saker, 164 (10,4 %) til menneske; av de 1539 med fasit 161 (10,5 %).

| oppsett | saker til menneske | MOT mot styret blant dem | maskin alene | maskin + menneske (øvre grense, antar riktig menneskelig avgjørelse) | gulv: menneske følger styret |
|---|---|---|---|---|---|
| ingen til menneske | 0 av 1539 (0,0 %) | 0 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,48 / R 0,55 / F1 0,512 |
| bare båndet: kalibrert P(MOT) i [0,15; 0,85) | 99 av 1539 (6,4 %) | 25 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,92 / R 0,62 / F1 0,742 (TP 36 FP 3 FN 22) | P 0,79 / R 0,19 / F1 0,306 |
| **standard** (bånd + ukjent selskap/type, injeksjon, datafeil, MOT uten sitat) | 161 av 1539 (10,5 %) | 29 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,93 / R 0,69 / F1 0,792 (TP 40 FP 3 FN 18) | P 0,79 / R 0,19 / F1 0,306 |

«Maskin alene» er de samme svarene i alle rader: rutingen endrer aldri maskinens svar, bare hvem som ser saken. Kolonnen «maskin + menneske» er en **øvre grense, antar riktig menneskelig avgjørelse** på hver rutet sak. «Gulv» antar at mennesket bare følger styret. Den sanne verdien ligger mellom. 32 av 35 falske MOT-flagg havner hos mennesket (3 er MOT-flagg utenfor sonen, som forvalteren også leser); de 18 MOT ingen ser har lav P(MOT) (under 0,15) og fanges ikke av noe bånd.

Laget med: `python3 -I arbeid/hack/c1/menneske_tabell.py arbeid/oppgave_2592/agent.csv` (bare stdlib, leser fasit direkte, samme definisjon som måler v3 `--score mot`).

## Svartid og rare saker (før frys, #2257, #2259, #2264)

**Svartid per sak** (100 tilfeldige saker fra test 2026, frø 0, uten fasit, nettet sperret med `sandbox-exec`, alle 100 med utgang 0):
- Hver sak som egen prosess (kald start, med modell-lasting): median 5,28 s, p95 7,14 s, verste 12,15 s, beste 4,22 s.
- Alle 100 i én kjøring: 4,2 s totalt, 0,042 s per sak. Nesten hele enkeltsakstida er oppstart.
- Gjenskapes med (fra landsbymappen, ca. 10 min): `python3 -I arbeid/oppgave_2259/svartid.py --n 100`. Rådata: `arbeid/oppgave_2259/ut/svartid.tsv` (p95 er rang 95 av 100). Rapport: `state/rapporter/c1_svartid.md`.

**20 rare saker** (tom tekst, 6000 tegn, ukjent selskap og land, manglende styreanbefaling, norsk, fransk og kinesisk tekst, fire injeksjonsforsøk, duplikat-id, ukjent sakstype): ingen krasj, 20 av 20 enkeltkjøringer og samlefila gir utgang 0. Hver sak gir en stemme med sitat eller går til et menneske.
- Krasjfiks? Det var ingen krasj. Én feil ble rettet: kinesisk forslagstekst fikk en stille FOR uten ruting. Nå går tekst med ikke-latinsk skrift til et menneske. Fiksen endrer bare ruting og rutingsgrunn, aldri svaret eller P(MOT). Prediksjonene på test 2026 er byte for byte uendret, og regexen treffer ingen av testsakene.
- Ingen av de fire injeksjonsforsøkene styrte svaret. Alle gikk til menneske.
- Ikke rettet (se pkt. 3 i BEGRENSNINGER): villedende rutingsgrunn på norsk/fransk tekst, og ved duplikat-id rutes bare den andre raden.
- Dommeren gjenskapte funnene fra en kald kopi (`state/rapporter/c1_rare_saker_dom.md`).
- Gjenskapes med (fra landsbymappen, ca. 2 min): `python3 -I arbeid/oppgave_2257/rare_saker.py --ut /tmp/c1_rare`. Rapport: `state/rapporter/c1_rare_saker_forfrys.md`.

## Robusthet: hva agenten gjør når inndata er rare

Vi forstyrret inndataene og kjørte den frosne agenten på nytt (test 2026, 1578 saker, etter de nye vaktene fra #2152). Modellen er ikke endret. Ingen test krasjet.

| situasjon | F1 på MOT (maskin alene) | til menneske | hva agenten gjør |
|---|---|---|---|
| vanlig kjøring | 0,512 | 10,4 % | standard |
| nye selskaper (ingen historikk) | 0,375 | 99,4 % | mister selskapshistorikken, som er det sterkeste signalet. Vakta «ukjent selskap» sender nesten alt til menneske |
| tom forslagstekst | 0 (med vilje) | 100 % | vurderer ikke saken («kan ikke vurderes»), følger styret, sender alt til menneske |
| ukjent sakstype i ny sak | 0,512 | 100 % | vakta «ukjent forslagstype» slår til på alle saker. Svarene er uendret |
| styrets anbefaling mangler | 0,467 | 100 % | antar FOR, flagger flere MOT (98 mot 74). Alt går til menneske med «styrets anbefaling mangler: sjekk innkallingen» |
| land/marked mangler | 0,455 | 100 % | grunn «land/marked mangler». Færre MOT-flagg (49) |

Kort sagt: der agenten mangler grunnlag, sier den fra og sender saken til et menneske, i stedet for å gjette stille. Tallene i kolonne 2 bygger på bare 58 MOT og flytter seg mye med få saker. Les dem som retning. Hele tabellen med målerlinjer: `state/rapporter/c1_robusthet_frossen.md`.

Gjenskapes med (fra landsbymappen, ca. 15 s): `python3 -I arbeid/oppgave_2144/robusthet_frossen.py --ut /tmp/c1_robusthet.md`
og sammenlign med `state/rapporter/c1_robusthet_frossen.md` (skriv ikke over den).

Merk: gjenskapingskommandoene i denne fila (menneske_tabell, svartid, rare saker, robusthet, kjor.sh) bor i landsbymappen
og kopieres ikke av `fremmed.sh`; bare agenten, målerne og `sjekk_treffsikkerhet.sh` finnes i den kalde kopien.
