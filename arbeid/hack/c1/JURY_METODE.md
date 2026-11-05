# Case 1: metode og ærlig evaluering (jurysvar, utkast #2056)

Hvert tall har kilde i hakeparentes. Forkortelser: [M] = `state/rapporter/c1_mot_modell_smed2.md`, [F] = `state/rapporter/case1_hvilken_fasit.md`, [T#n] = forsøk n på forsøkstavla.

**1. Fasit.** Vi måler mot NBIMs egne publiserte stemmer (real_votes fra NBIMs API), slik casen ber om. MOT betyr *mot styrets anbefaling*. Hovedtallet (#231) teller bare NBIM-stemmen MOT der styret ikke sier MOT. Sidetallet «avvik fra styret» teller også AVSTÅ. Andelen MOT er 5,6 % (744 av 13 324) [F]. NPX-fila brukes ikke som hovedtall: feltet vi tolker som styrets anbefaling ser ut til å være «for/mot ledelsen». I NPX står styret som MOT sitt eget forslag i 2 538 av 48 000 saker, mot 3 av 13 211 i NBIMs egne data [F]. «Aksjonærforslag = MOT» ser ut til å gi F1 0,645 på NPX, men faller til 0,071 når feltet tolkes riktig [F]. Det tallet bruker vi aldri som resultat.

**2. Tidssplitt.** Vi trener på data til og med 2024, velger grense og hyperparametre på 2025 og tester på 2026. Testen er kjørt én gang [M, T#1037]. Historikk-variablene (MOT-andel i samme selskap og for samme tekst) bruker bare møter *før* møtedatoen [M].

**3. Hvorfor F1 på MOT, ikke accuracy.** NBIM stemmer med styret i omtrent 94 % av sakene (case-PDF, [F]). En modell som aldri sier MOT får derfor høy accuracy, men den finner ingen av sakene som betyr noe. I test 2026 (real_votes) har «følg styret» 96,2 % riktig og bommer på alle de 58 MOT-sakene [`leveranse/kravrespons.md`, M]. F1 på MOT måler det juryen spør etter: om vi finner avvikene (recall) og om flaggene stemmer (presisjon).

**4. Grunnlinje mot modell (real_votes, test 2026: 1 539 saker, 58 MOT mot styret, 66 avvik inkl. 5 AVSTÅ [M]).** Radene uten egen merknad er målt på avvik.

| | F1 (avvik) | P | R | Kilde |
|---|---|---|---|---|
| Følg styret (gulvet, ikke en løsning) | 0 | – | 0 | [M], val 2025: 0 [T#1034] |
| Alltid MOT | 0,082 | | | [T#1035] |
| Modell, streng historikk (bare tidligere år) | 0,386 | 0,458 | 0,333 | [M, T#1038] |
| Modell, løpende historikk (valgt), avvik | 0,482 | 0,465 | 0,500 | [M, T#1037] |
| Samme modell (eldre frossen #2044), F1 på MOT mot styret | 0,476 [0,36; 0,59] | 0,441 | 0,517 | [M, #2087, #2095] |
| **Levert modell repo4 (#2044 + 4 historikktrekk), F1 på MOT mot styret (hovedtall)** | **0,512** [0,40; 0,62] | 0,478 | 0,552 | [M, #2592, `tall_tabell.md`] |

Valgt modell er et snitt av logreg (tfidf + kategorier) og LightGBM (kategorier + historikk). På val 2025 gir den F1 0,522, og PR-AUC på test er 0,52 [M]. Den finner også MOT på styrets egne forslag: 29 av 58 treff [M].

**5. Forbudte kolonner.** Disse kolonnene inneholder svaret eller NBIMs begrunnelse og brukes aldri som input: `nbim_vote`, `nbim_vote_raw`, `rationale_text`, `rationale_section`, `funds_disagree` og `position_paper` [M]. `position_paper` ble funnet som lekkasje underveis: 97,5 % av de 367 radene der feltet er satt, er MOT [M]. Treningsskriptet skriver ut hvilke kolonner det leser, og en assert stopper kjøringen ved overlapp med forbudslista [M]. Lekkasjevaktas fulle liste kommer i `FORBUDT.md` (#2055, ikke ferdig da utkastet ble skrevet).

**6. Kjente svakheter, ærlig.**
- Testen har bare 58 MOT mot styret. Usikkerheten (bootstrap 95 % per selskap) er KI [0,40; 0,62] for repo4 på MOT (eldre frossen #2044: [0,36; 0,59]; avvik [0,375; 0,580]) [M, #2592], så forskjeller under omtrent 0,1 kan være støy.
- Hovedtallet forutsetter at NBIMs tidligere stemmer i samme sesong er kjent. Det stemmer fordi NBIM publiserer løpende. Uten denne antakelsen er gulvet 0,386 [M, T#1038].
- Målet er F1 0,5. Levert repo4 ligger like over det på test (0,512 på MOT, KI [0,40; 0,62]), og val 2025 er 0,530 [M, #2592]. Eldre frossen #2044 lå under (0,476 på MOT, 0,482 på avvik; val 0,520 / 0,522).
- Det fulle agentsystemet (maskinen alene) får 0,456 [T#1036]. Tallet for den nye modellen inne i agenten er ikke målt ennå (#2053).
- Hvordan vi tolker feltet i NPX er utledet fra mønsteret i dataene, ikke fra N-PX-dokumentasjonen [F].
- Halvparten av MOT-sakene blir ikke funnet (recall 0,52 [M]). Derfor sender agenten usikre saker til et menneske (grensen velges i #2057).

*Oppdateres med tall etter modellfrys kl. 16 (#1975).*
- Hele ablasjonen (hva modellen bygger på) står i `leveranse/ERLIG_EVALUERING.md` [`c1_ablasjon_v2.md`].
