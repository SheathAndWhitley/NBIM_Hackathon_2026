# Case 1: kravrespons punkt for punkt mot casens tekst, med MOT-kravet (speider #2051, 05.11 12:10)

Kilder: kick-off-PDF s. 5–6, `case1_stemmegivning/README.md`, `Regler_og_bedommingskriterier.pdf`, nye filer i `arbeid/hack/CASE/` (11:42: `real_votes.csv`, `npx_votes.csv`), ordre #231.
Forrige versjon (jurykriterier, #1967) ligger i `arbeid/speider/hack_c1_kravrespons_1967.md`.

**Ordre #231, styrer alt under:** hovedtallet er **F1 på MOT** (avvik fra styret). «Følg styret» er gulvet (F1 = 0 per definisjon), ikke en lov løsning. Agenten må faktisk si MOT.
Beste målte i dag (real_votes test 2026, 1 539 saker, 66 MOT): maskin alene **F1 0,456** (P 0,41, R 0,52, KI 0,36–0,54), gulv 0 (`case1_mot_system.md`, #2046, selvrapportert, kontroll #2030 åpen). Val 2025-tall fra smed2 0,48 (selvrapportert).

**Største funn: leveransens kravrespons (`c1/leveranse/kravrespons.md`) og `kjor.sh` er utdaterte.** De beskriver N-PX US say-on-pay og historikkregelen (F1 0,383). Arrangøren har siden 11:42 gitt NBIMs egne stemmer globalt (`real_votes`, 2019–2026) og `npx_votes` med 141 injeksjonsrader. Hele «Hvordan vi verifiserte» og tallene må skrives om etter modellfrys kl. 16.

## Kravtabell
| # | Krav (kilde, ordrett/kort) | Hvor i leveransen | Status |
|---|---|---|---|
| 1 | Agent leser saksliste og foreslår FOR / MOT / AVSTÅ per forslag (PDF s. 6, pkt 1) | `kjor_agent.py` / `oppgave_2046/case1_mot.py` | **Delvis**: FOR/MOT finnes, AVSTÅ foreslås ikke (npx test: 297 av 634 avvik er AVSTÅ). Saksliste-inndata fra demo mangler |
| 2 | **Agenten predikerer MOT; hovedtall F1 på MOT** (#231, PDF s. 6 «recall og presisjon på MOT-stemmer») | `case1_mot_system.md` | **Delvis**: 0,456 på real test, målt én gang av smed. Ikke kontrollert av dommer (#2030), ikke i `kravrespons.md` |
| 3 | «Følg styret» oppgitt som baseline og slått (README, regler §4) | `case1_mot_system.md`, `JURY_utkast_MOT.md` | **Dekket** i rapport (0 mot 0,456); sterkere gulv «MOT før i selskapet» 0,383 bør stå ved siden |
| 4 | Ikke accuracy (README) | samme | **Dekket**, men vis ærlig at accuracy faller 0,957 → 0,947 |
| 5 | Fasit = NBIMs faktiske publiserte stemmer (PDF s. 6, pkt 3) | `real_votes.csv` (arrangør) | **Dekket i data**, **mangler i kravrespons** (der står SEC N-PX) |
| 6 | Tidssplitt, ikke tilfeldig (README fallgruve, regler «trekker ned») | train ≤2024, val 2025, test 2026 (`hack_c1_offisielle_data.md`) | **Dekket**. Test kjøres én gang |
| 7 | Kategori-/lekkasjesjekk (README) | `maaler_offisiell.py` forbudsliste, assert i `case1_mot.py` | **Delvis**: lekkasjevakt #2040 åpen; `funds_disagree`, `n_funds`, `rationale_*` må være bevist ute i levert modell |
| 8 | Klasseubalanse: system som aldri sier MOT er verdiløst (README) | forsøkstavla, MOT-vakt #2049 | **Delvis**: vakta bygges; sitatlaget (smed3) har sagt 0 MOT tidligere |
| 9 | Hver anbefaling siterer retningslinjen som avgjør (PDF pkt 2, README) | smed3 sitatlag | **Mangler for MOT**: stikkprøve 0/10 MOT OK, sitatene er Vanguard-policy (`case1_sitat_stikkprove.md`). #2009, #2037 åpne |
| 10 | …og *hvorfor* (README «og hvorfor») | `rationale_text` 627 saker som eksempler, `nbim_begrunnelser.csv` | **Mangler** i agentens utdata; rationale er forbudt som feature, lov som sitatkilde bare fra *tidligere* år |
| 11 | Konfidens som ruter usikre saker til menneske (PDF pkt 2, README) | ruting 5 %/10 %-grense i `case1_mot_system.md` | **Delvis**: finnes, men F1 0,66/0,74 med ruting er ikke sammenlignbart med maskin alene; må rapporteres som to tall |
| 12 | Motstandstest: instruks i dokumentet, rapporter uansett (README, regler §4) | `motstand_inj.py`, `npx_inj_input.csv` (141 rader) | **Mangler på levert agent**: dagens tall (0/158 snudde) gjelder historikkregelen som ikke leser tekst. #2038, #2047 åpne |
| 13 | Policy vs praksis («stemmer forvalteren slik retningslinjene sier?») (README vri) | `JURY_utkast_MOT.md` pkt 4–8, `c1_nbim_begrunnelser_1977.md` | **Delvis**: kildebelegg finnes, ingen målt sprik-tabell |
| 14 | Kravrespons maks 1 side, malens overskrifter (regler §3) | `c1/leveranse/kravrespons.md` | **Delvis**: 0 TODO, men utdaterte tall og fasit; må skrives om etter frys |
| 15 | README med ETT kall som reproduserer hovedtallet (regler §2) | `kjor.sh` | **Mangler for nytt hovedtall**: kjører N-PX/historikkregel, ikke `real_votes`-agenten. #1952 kl. 13 |
| 16 | Kilder med URL (regler §5) | README «Datakilder» | **Delvis**: SEC/NBIM-URL-er finnes; arrangørens filer og NBIM API-uttrekk må nevnes |
| 17 | AI-bruk oppgitt (regler §5) | README «AI-verktøy» | **Dekket** |
| 18 | Demo 5 min, kjørende, på holdout, ikke håndplukket (regler §2, §4) | demo-manus #1975 (16:05) | **Mangler**: må vise MOT-sak med sitat + én rutet sak, tall fra holdout |
| 19 | Sporbarhet, ingen irreversible handlinger (regler §4) | `sporlogg.py` | **Dekket** (bare anbefaler); sjekk at sporlogg følger ny agent |
| 20 | Erklærte begrensninger (regler §4) | `BEGRENSNINGER.md` | **Delvis**: skrevet for N-PX say-on-pay; må oppdateres (194 selskaper, 66 MOT i test, AVSTÅ ikke modellert, npx og real ikke overlapp) |
| 21 | Juryspm. 1–3 (målvariabel/alternativer, produksjon, én uke til) | `jury_svar.md`, `JURY_utkast_MOT.md` | **Delvis**: TBD-tall etter frys (#1975) |
| 22 | Ikke bygg noe avhengig av NBIM-databasen (README, regler §7) | arrangøren leverte `real_votes` som fil | **Dekket**: oppgi at real_votes er arrangørens uttrekk, agenten kaller ikke API |

Oppsummert (22 krav): 6 dekket, 11 delvis, 5 mangler (9, 10, 12, 15, 18). De fire første manglene henger på MOT-kravet: MOT-saker uten riktig sitat, motstandstest på en agent som ikke leser tekst, og ett-kall som ikke kjører MOT-agenten.

## Hull adressert til rolle (prioritert)
1. **smed3** (#2009, #2037): MOT-stemmer skal sitere NBIM Global Voting Guidelines (3.3.8/3.3.10 lønn, 1.1.4 uavhengighet, 1.3.3 CEO/styreleder), ikke Vanguard. Mål: stikkprøve MOT ≥ 8/10. Begrunnelse = «hvorfor» (krav 10).
2. **smed2** (#2044): én frosset MOT-modell på real_votes kl. 16, med F1 på MOT val og test, P/R, og regel-gulvet 0,383-varianten på samme data. Vurder AVSTÅ som egen klasse eller erklær den ute (krav 1).
3. **dommer** (#2030, #2040): kontroller 0,456 fra kald start; bevis at forbudte kolonner er ute (krav 2, 7).
4. **dommer2** (#2038) + **smed** (#2047): motstandstest på den *leverte* agenten med de 141 injeksjonsradene; rapporter andel MOT som snur til FOR, uansett tall (krav 12).
5. **dommer** (#1952 kl. 13): `kjor.sh` skal kjøre MOT-agenten på real_votes og skrive hovedtallet; ellers er krav 15 brutt («påstander som ikke kan reproduseres»).
6. **speider** (#1975 kl. 16:05): skriv om `kravrespons.md`, `BEGRENSNINGER.md`, `JURY.md` og demo-manus med frosne tall; fjern N-PX-say-on-pay som hovedfasit; legg real_votes-kilde i README (krav 5, 14, 16, 18, 20, 21).
7. **ordfører**: avgjør AVSTÅ (krav 1) og om ruting-F1 skal stå i hovedtabellen (anbefaling: nei, hovedtall = maskin alene; ruting som eget tall med andel til menneske).
8. **arkitekt** (#2049): MOT-vakta på forsøkstavla, så ingen kandidat med ~0 MOT kan bli valgt ved frys (krav 8).
