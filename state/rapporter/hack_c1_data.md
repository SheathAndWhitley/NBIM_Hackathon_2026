# Case 1 data: N-PX-stemmer i arbeid/hack/c1/data/votes.csv (smed, #1946)

**ADVARSEL TIL ALLE: `managementRecommendation` i Vanguards N-PX er IKKE styrets anbefaling.**
Det er et flagg for «stemte med ledelsen» (FOR) / «mot ledelsen» (AGAINST).
Bevis: på 1020 aksjonærforslag er stemme == feltet i 0,0 % av postene (bare AGAINST/«FOR» og FOR/«AGAINST»),
og 241 revisorvalg har «styret anbefaler AGAINST». Feltet er altså fasiten. Det heter nå `mgmt_felt_LEKKER`
og skal aldri brukes som feature eller som baseline. Bruk kolonnen `styret` (utledet: ISSUER -> FOR,
SECURITY HOLDER -> AGAINST, frekvens -> ONE YEAR).

## Tabellen
- Kilde: SEC EDGAR N-PX, `proxytable.xml` i hver innsending (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000036405&type=N-PX).
  CIK 1364742 (BlackRock) er en NOTICE uten stemmer; byttet til Vanguard Index Funds (CIK 36405).
- Kommandoer (fra `arbeid/hack/c1/`): `python3 hent_votes.py --cik 36405 --fra 2024 --ut data/votes_raa.csv`,
  `python3 lag_tabell.py data/votes_raa.csv data/votes.csv`, `python3 baseline_styret.py data/votes.csv`.
  Rå XML caches i `data/raw/`.
- Én rad per proxyTable-post (fond x forslag x stemmeforvalter). Vanguard har flere poster per forslag:
  fondets egen stemme (største post) pluss små poster fra andre forvaltere/pass-through. `hoved=1` = største post.
- Mål: `mot` (AGAINST/WITHHOLD, som startpakken) og `mot_ledelsen` (avvik fra styret, rettet).

## Versjon 4 (11:30): tre forvaltere, `data/votes_unik_alle.csv` = 582 812 unike forslag
- Ny: State Street SPDR Series Trust (CIK 1064642), 8 innsendinger med stemmer (2024-2026), 500 610 poster ->
  `data/votes_spdr_unik.csv`, 71 724 unike forslag, møter 2023-07..2026-06. **Samme lekkasje** (stemme==felt på
  1,8 % av aksjonærpostene -> med/mot-ledelsen-flagg). Alle tre forvaltere bruker feltet likt.
- År i felles tabell: 2023 34 955, 2024 185 612, 2025 176 016, 2026 186 229. Kolonnen `forvalter_cik` skiller dem.
- Startpakkens `baseline.py` (alltid FOR) på felles tabell: 582 812 forslag, MOT 9,0 %, accuracy 91,0 %, presisjon 0, recall 0.
- Baseline «følg styret» (MOT der utledet styre = AGAINST), mål MOT, test = møte >= 2025-07-01:

| forvalter | n unike | MOT | avvik fra styret | test n | test MOT | presisjon | recall | F1 |
|---|---|---|---|---|---|---|---|---|
| Vanguard Index Funds | 136 456 | 6,9 % | 6,6 % | 65 820 | 7,9 % | 88,2 % | 10,1 % | 0,181 |
| iShares Trust | 374 632 | 9,6 % | 10,7 % | 135 862 | 9,6 % | 85,9 % | 7,1 % | 0,132 |
| SPDR Series Trust | 71 724 | 10,1 % | 8,5 % | 21 696 | 8,9 % | 77,1 % | 19,1 % | 0,306 |
| alle | 582 812 | 9,0 % | 9,5 % | 223 378 | 9,0 % | 84,6 % | 9,0 % | 0,163 |

  «Alltid MOT»-gulvet på test gir F1 0,16-0,17. Baseline finner nesten bare aksjonærforslag; >90 % av MOT-stemmene
  er på selskapets egne forslag (styrevalg, lønn), der baseline har recall 0.
- Uhell 11:18-11:20: `hent_votes.py --liste` overskrev `data/votes.csv` med en tom fil. Gjenopprettet fra
  `votes_raa.csv` (513 421 rader, `votes_unik.csv` byte-identisk). Rettet: `--liste` skriver ikke lenger.
- `baseline_styret.py` virker nå også på unik-filer (uten `hoved`-kolonne).

## Versjon 3 (11:17): to forvaltere, felles tabell `data/votes_unik_alle.csv` (511 088 unike forslag)
- iShares Trust (BlackRock, CIK 1100663): 3 219 773 poster -> `data/votes_ishares_unik.csv`, 374 632 unike forslag
  (2023 25k, 2024 125k, 2025 116k, 2026 108k). Inkluderer utenlandske selskaper (ABSTAIN brukes). Bygd med
  `python3 lag_unik_strom.py data/votes_raa_ishares.csv data/votes_ishares_unik.csv` (strømmende, 25 s).
- **Samme lekkasje hos BlackRock.** Forklaring: skjema N-PX spør om fondet stemte for eller mot ledelsens
  anbefaling, så `managementRecommendation` er et med/mot-ledelsen-flagg hos begge. Ingen grunn til å tro
  at andre forvaltere gjør det annerledes. `lag_tabell.py` avgjør semantikken per forvalter (aksjonærposter med stemme==felt
  < 25 % gir flagg: Vanguard 0,7 %, iShares 9,2 %).
- iShares, baseline «følg styret», mål MOT: alle 374 632, MOT 9,6 %, presisjon 63,0 %, recall 9,4 %.
  Trening (< 2025-07-01) 238 770: presisjon 57,2 %, recall 10,7 %. Test (>= 2025-07-01) 135 862: presisjon 85,9 %, recall 7,1 %.
  Andel avvik fra styret 10,7 %.
- Overlapp: 52 744 forslag stemt over av begge. Samme stemme på 94,0 %. Begge MOT 1 821, bare iShares MOT 1 699,
  bare Vanguard MOT 857. Det er praksisforskjeller vi kan vise fram, men den andre forvalterens stemme er ikke kjent
  før møtet og kan ikke være en feature.

## Tall, versjon 2 (11:15): hele Vanguard Index Funds, 36 innsendinger, møter 07.2023-06.2026
- `data/votes.csv`: 513 421 poster (alle fond x forslag x stemmeforvalter), 388 598 hovedposter.
- `data/votes_unik.csv` (anbefalt modelltabell): 136 456 unike forslag (forvalter, cusip, møtedato, tekst),
  flertall over fondenes hovedposter. År: 2023 6 588, 2024 35 531, 2025 35 421, 2026 58 916.
  Fondene er uenige seg imellom på bare 0,2 % av forslagene, så policyen er felles.
- Andel MOT (AGAINST/WITHHOLD) 6,9 %, andel avvik fra styret 6,6 %. Bare 1 859 aksjonærforslag (1,4 %).
- Baseline «følg styret» på unike forslag, mål MOT:

| sett | n | andel MOT | presisjon | recall |
|---|---|---|---|---|
| alle | 136 456 | 6,9 % | 90,4 % | 17,8 % |
| trening, møte < 2025-07-01 | 70 636 | 6,0 % | 91,4 % | 27,3 % |
| test, møte >= 2025-07-01 | 65 820 | 7,9 % | 88,2 % | 10,1 % |

  På mål B (avvik fra styret, `mot_ledelsen`) har «følg styret» presisjon 0 og recall 0 per definisjon.
  Avviket øker over tid (4,8 % -> 8,6 %), så testperioden er vanskeligere enn treningen.
- Avvik per kategori (unike): styrevalg 6,7 % (98 697 forslag), say-on-pay 5,1 %, kompensasjon 18,3 %,
  selskapsstyring 12,3 %, kapitalstruktur 9,4 %, revisor 0,4 %, miljø/sosialt under 0,5 %.
  Det meste av signalet er styrevalg og lønn, ikke ESG.
- Startpakkens `baseline.py` på rå tabell (alle 515 553 poster, «alltid FOR»): MOT 6,5 %, presisjon 0, recall 0.
- Småpostene (hoved=0, pass-through/andre forvaltere) har høyere MOT (11,5 % i 2026). Bruk hoved=1 eller votes_unik.csv.

## Tall, versjon 1 (utdatert) (én innsending, Vanguard Morningstar Value Index Fund, møter 07.2025-06.2026)
21 473 poster, 9 036 hovedposter. Andel MOT 4,2 %, andel avvik fra styret 1,7 % (hovedposter).
Baseline «følg styret» (predikér MOT der styret sier AGAINST = aksjonærforslag):
- alle hovedposter: presisjon 95,8 %, recall 65,7 %, F1 0,779
- test (møtedato >= 2026-01-01): presisjon 96,0 %, recall 67,3 %, F1 0,791
- På mål B (avvik fra styret) har «følg styret» recall 0 per definisjon. Her ligger den ekte oppgaven:
  130 MOT-stemmer på selskapets egne forslag (styrevalg, lønn) som baseline aldri finner.
- Startpakkens baseline.py på rå tabell (alle poster, «alltid FOR»): MOT 8,5 %, presisjon 0, recall 0.
