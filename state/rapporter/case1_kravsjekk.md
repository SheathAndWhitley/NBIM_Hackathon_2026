# Case 1: kravsjekk punkt for punkt mot casens tekst (speider #2059, 05.11 kl. 12.20)

Kilder for kravene: kick-off-PDF s. 6, 9–12 (K), `FinTech_Hackathon_Caser_H2026.pdf` (C), `case1_stemmegivning/README.md` (R), `Regler_og_bedommingskriterier.pdf` (B), ordre #231.
Sjekket mot: `state/rapporter/hack_c1_kravrespons.md` (#2051), `arbeid/hack/c1/JURY_METODE.md` (#2056), `arbeid/hack/c1/leveranse/`, `arbeid/hack/levering/` og `c1/kaldstart.sh` slik de står kl. 12.15.
Erstatter ikke #2051 eller arkitektens `levering/KRAVRESPONS.md` (#2014), men samler dem og legger til det som er nytt siden.

## Status 12:30 (speider #2069, runde 2: hullene mot filene kl. 12.25)

Hovedendring siden 12.20: `levering/kjor_agent.py` kjører nå **real_votes som standard** (#2053, via `levering/c1_real.py`), med smed2s #2044-modell og NBIM-sitat. Målt test 2026 én gang: F1 MOT 0,4818 (P 0,465, R 0,500, 66 MOT), 11,2 % til menneske (`levering/kjor_agent_real_test2026.txt`). Resten av pakken er ikke fulgt etter.

| # | Status | Bevis (fil, kl.) | Eier |
|---|---|---|---|
| H1 to fasiter | **delvis løst**: agenten = real_votes. Men `c1/kaldstart.sh` steg 4 måler fortsatt med `c1/maaler.py` mot `data_v3/fasit.csv` (N-PX), og REF hentes fra forsøk med «kjor_agent» (0,474). Agentens id-er (`2031740\|1`) finnes ikke i N-PX-fasiten → kald start kl. 13 blir RØD eller måler feil | `kaldstart.sh` linje 46–47, `c1_real.py` linje 179 | **arkitekt** (#2060): steg 4 → `maaler_offisiell_v2.py` mot real, REF 0,481752 |
| H2 ETT kall | **åpent**: `c1/leveranse/kjor.sh` (0,383) og `run.sh` (manglende moduler) uendret siden 11.18 | `c1/leveranse/kjor.sh`, `run.sh` | **arkitekt** |
| H3 1-sider/README | **åpent**: `c1/leveranse/kravrespons.md` 11.19, `README.md` 11.36, fortsatt N-PX/0,383 | samme filer | **speider** (#1975, 16.05) |
| H4 sitat | **løst i agenten**: real-stien siterer NBIMs egen `rationale_text` fra tidligere år/annet møte (74/74 MOT har sitat). Gammel N-PX-sti har fortsatt Vanguard (`kjor_agent.py` linje 19, 39). Sitatkvalitet ikke stikkprøvd på real | `c1_real.py` linje 12, 79, 167; `kjor_agent_real_test2026.txt` | **dommer2** (#2012) stikkprøve |
| H5 motstandstest | **åpent**: `levering/motstand_ut/` 11.03, før real-agenten | `levering/motstand_ut/` | **dommer2** etter frys 16.00 |
| H6 «hvorfor» | **åpent**: `c1_real.FELT` har `sitat`, men ingen `grunn`/topp-3-grunner (N-PX-stien hadde `sitat_grunn`) | `c1_real.py` linje 31–32 | **smed** |
| H7 demo | **åpent**: `levering/demo/modell.py` er fortsatt stubben, `DEMO_MODELL` ikke koblet; `c1/DEMO_MANUS.md` (12.03) bruker N-PX VAL 2025 og 0,474 | `demo/modell.py` linje 6–8, `DEMO_MANUS.md` linje 3, 73 | **smed** kobler; **speider** manus (#1975, #2070) |
| H8 AVSTÅ | **åpent** (avgrensning): ingen AVSTÅ i `c1_real.py`; ikke skrevet i BEGRENSNINGER | `c1_real.py`, `c1/leveranse/BEGRENSNINGER.md` 11.41 | **ordfører** bekrefter; **speider** skriver |
| H9 robusthet | **pågår**: #2063 50 %, 14 testtyper, 1 krasj (ikke-numerisk item_no) | tavla #2063, `case1_robusthet_kontroll.md` | **smed** (#2063/#2071) |
| H10 e-post | **løst** som utkast (12.07); dommer verifiserer, guden fyller navn og sender | `state/rapporter/epost_utkast_hackathon.md` | **dommer** |
| H11 BEGRENSNINGER/JURY | **åpent**: `jury_svar.md` har 9 TODO; BEGRENSNINGER og JURY.md gjelder N-PX | `c1/leveranse/jury_svar.md`, `JURY.md` 11.17 | **speider** (#1975) |
| H12 KI hovedtall | **åpent**: README har KI 0,31–0,45 for regelen på N-PX; ingen KI for 0,482 real i leveransen (`JURY_METODE.md` har KI, men for hvilket tall må sjekkes) | `c1/leveranse/README.md` linje 71 | **arkitekt** (#2064) |
| H13 filnavn | **åpent**: README peker på `KRAVRESPONS.md`, fila heter `kravrespons.md` | `c1/leveranse/README.md` linje 5 | **arkitekt** ved pakking |

**Telling:** 1 løst (H10), 1 løst i agenten (H4), 1 delvis (H1), 1 pågår (H9), 9 åpne. Kravtabellen under er ikke telt på nytt; krav 3, 4 og 8 går fra «mangler/delvis» mot dekket når H1 er lukket i kaldstart.

### Topp 3 som kan felle oss hos juryen
1. **H1/H2: hovedtallet kan ikke reproduseres med ett kall.** Agenten sier 0,482 (real), kaldstart måler mot N-PX og `kjor.sh` gir 0,383. B §2 krever ETT kall; dette er 60 %-delen (metode og etterprøvbarhet). Rett før 13.00 (#1952), ellers er første kalde start bortkastet.
2. **H7: demoen viser stubben («følg styret» + regel), ikke agenten.** C pkt 5 og B §4: juryen ser en agent som ikke er den vi måler. Manuset forteller om N-PX-tall.
3. **H3/H11: tekstene juryen leser (1-sider, README, BEGRENSNINGER, jury_svar) beskriver en annen oppgave** (N-PX say-on-pay, Vanguard, 0,383). Uærlig-inntrykk selv om tallene er ekte. Låst bak modellfrys 16.00, men må ha ferdig mal før.
(Neste etter disse: H5 motstandstest på levert agent og H6 «hvorfor»-kolonne.)

## HULL (øverst, prioritert; hvem tetter)

| # | Hull | Bevis | Hvem |
|---|---|---|---|
| H1 | **To fasiter med nesten like tall.** `JURY_METODE.md` sier hovedfasit er `real_votes` (NBIM globalt, test 2026: 1 539 saker, 66 MOT, F1 0,482). Agenten (`levering/kjor_agent.py`), `kaldstart.sh` (måler på `data_v3`), `DEMO_MANUS.md` og hele `c1/leveranse/` bruker N-PX say-on-pay (1 246 saker, 129 MOT, F1 0,474). 0,482 og 0,474 er to ulike oppgaver, ikke samme tall. Juryen vil se dette som uetterprøvbart («trekker ned», B §4). | `JURY_METODE.md` §4, `kjor_agent_holdout2026.txt`, `kaldstart.sh` linje 3–4 | **ordfører** velger én hovedfasit nå (anbefaling: real_votes, fordi casen sier «NBIMs faktiske stemmer» og den dekker alle sakstyper). Deretter **smed** (#2053) og **arkitekt** (#2060) peker agent og kaldstart dit |
| H2 | **ETT kall gir feil hovedtall.** `c1/leveranse/README.md` og `kjor.sh` gir `SCORE 0.383275` (historikkregel). `run.sh` peker på `modell.py` og `motstand.py`, som ikke finnes (krasjer). | `kjor.sh`, `run.sh` linje 30, 41 | **arkitekt** (#2060): `kjor.sh` = `kaldstart.sh`, slett eller merk `run.sh` som gammel |
| H3 | **1-sideren og README er utdatert.** `kravrespons.md` beskriver N-PX say-on-pay, historikkregel 0,383, «LightGBM 0,325 slo ikke regelen», «sitatlaget gir 0 MOT», ruting «konfidens < 0,6». Ingenting av det gjelder levert agent. | `c1/leveranse/kravrespons.md`, `README.md` | **speider** (#1975, 16.05) |
| H4 | **Sitat fra feil forvalter.** Agenten siterer Vanguards policy (`kjor_agent.py` linje 14, 35). R: «bruk den forvalterens egne retningslinjer». NBIM-teksten ligger i `c1/retningslinjer/`. Stikkprøve MOT 0/10 OK (#2051). #2061 la inn NBIM-sitat i forklaringen, men ikke målt eller koblet til agentens `sitat`-kolonne. | `kjor_agent.py`, `BEGRENSNINGER.md` pkt 7 | **smed3** (#2009/#2037) bytter kilden; **dommer2** (#2012) stikkprøver ≥ 8/10 |
| H5 | **Motstandstest ikke kjørt på levert agent.** Eneste tall: referansemodell TF-IDF+LR, 15/64 snudde (STRYK), og historikkregel 0/158 (leser ikke tekst). | `case1_motstandstest.md`, `kravrespons.md` | **dommer2** kjører `levering/motstandstest.py --modell` mot frosset agent etter kl. 16, rapporterer uansett |
| H6 | **«Hvorfor» mangler i agentens utdata.** `forklar.py` (#2007) gir topp-3 grunner, men bare for smed2s modell i egen mappe, ikke som kolonne i `agent.csv`. | `case1_forklaring.md` | **smed** (#2053): ta `grunn1-3` inn i `agent.csv` |
| H7 | **Demoen bruker stubben.** `levering/demo/modell.py` = følg styret + «aksjonærforslag → MOT», Vanguard-fasit. C pkt 5: «lim inn en saksliste». | `levering/KRAVRESPONS.md` H5 | **smed** kobler `kjor_agent` inn via `DEMO_MODELL`; **speider** manus (#1975) |
| H8 | **AVSTÅ foreslås aldri.** Agenten gir bare FOR/MOT, måleren teller AVSTÅ som avvik. Må stå som avgrensning. | `kjor_agent.py` linje 205 | **ordfører** bekrefter; **speider** skriver i BEGRENSNINGER |
| H9 | **Robusthet: ukjent forslagstype rutes 0 %.** | `BEGRENSNINGER.md` pkt 8 | **smed** (#2063) |
| H10 | **Ingen e-postutkast for innsending.** Ingen `epost_utkast_hackathon.md` i `state/rapporter/`. Innsending: e-post til arrangøren, emne «Gruppenavn Hackathon H2026 demo», navn på alle medlemmer (K s. 10). Gruppenavn og navn må guden fylle inn. | `ls state/rapporter/epost_utkast_*` | utkast laget: `epost_utkast_hackathon.md` (speider); **dommer** verifiserer, guden fyller navn og sender |
| H11 | **`BEGRENSNINGER.md` og `JURY.md` gjelder N-PX/Vanguard.** `jury_svar.md` har 10+ TODO. | `grep TODO jury_svar.md` | **speider** (#1975) etter H1 |
| H12 | **KI for hovedtallet ikke i leveransen.** KI står for regelen (0,31–0,45), ikke for agentens tall. | `c1/leveranse/README.md` | **arkitekt** (#2064, tabell rett fra måleren) |
| H13 | **Filnavn.** README sier `KRAVRESPONS.md`, fila heter `kravrespons.md`. Virker på Mac, brekker på Linux/zip. | `ls c1/leveranse` | **arkitekt** når pakken bygges |

## Kravtabell

| # | Krav (kilde) | Hvor dekket (fil) | Status |
|---|---|---|---|
| 1 | Agent leser saksliste og foreslår per forslag (C, K s. 6 pkt 1) | `levering/kjor_agent.py --csv/--sak` | delvis: bare say-on-pay målt i agenten (H1) |
| 2 | FOR / MOT / AVSTÅ (C) | `agent.csv` kolonne `anbefaling` | delvis: ingen AVSTÅ (H8) |
| 3 | Agenten predikerer MOT, hovedtall F1 på MOT (#231, C «recall og presisjon på MOT») | `kjor_agent_holdout2026.txt` (221 MOT, F1 0,474 N-PX); `JURY_METODE.md` (0,482 real) | delvis: sier MOT, men to fasiter (H1) |
| 4 | Siterer retningslinjen som avgjør (C, R) | `kjor_agent.py` `punkt`, `sitat` | mangler: Vanguard, ikke NBIM (H4) |
| 5 | …og hvorfor (R) | `kandidater/smed2_c1_mot/forklar.py` | delvis: finnes, ikke i agentens utdata (H6) |
| 6 | Konfidens ruter usikre saker til menneske (C, R) | `kjor_agent.py --til-menneske`, `levering/README.md` tabell 0–20 % | dekket (N-PX). Grense velges i #2057 |
| 7 | Systemet sier når det ikke vet (R) | `rutingsgrunn` «kan ikke vurderes» | delvis (H9) |
| 8 | Evaluer mot NBIMs faktiske, publiserte stemmer (C pkt 3) | `real_votes.csv` (arrangør), `c1/hent_nbim.py` (N-PX) | delvis: begge er NBIM, men leveransen sier N-PX og metoden sier real (H1) |
| 9 | Baseline «følg styret» oppgitt og slått (R, B §4) | `JURY_METODE.md` §4, `maaler.py baseline` | dekket: 0 mot 0,47–0,48. Sterkere gulv (historikkregel) bør stå ved siden |
| 10 | Presisjon og recall på MOT, ikke accuracy (C, R) | `JURY_METODE.md` §3–4, `kjor_agent_holdout2026.txt` | dekket |
| 11 | Tidssplitt, ikke tilfeldig (R, B) | `JURY_METODE.md` §2, `lag_v3.py` assert | dekket. Merk: «løpende historikk» i samme sesong må forklares (§6) |
| 12 | Kategori-/kolonnelekkasje sjekket (R) | `c1/FORBUDT.md` (#2055), assert i trening, `maaler.py` nekter `managementRecommendation` | dekket, `position_paper` funnet og fjernet |
| 13 | Klasseubalanse (R) | grense valgt på val-F1, PR-AUC, MOT-vakt (#2049) | dekket |
| 14 | Motstandstest i dokumentet, rapporter uansett (R, B §4) | `levering/motstandstest.py`, `case1_motstandstest.md` | mangler på levert agent (H5) |
| 15 | Policy vs praksis-vrien (R) | `JURY_utkast_MOT.md`, `c1_nbim_begrunnelser_1977.md` | delvis: ingen målt sprik-tabell. Valgfritt, lav prioritet |
| 16 | Kravrespons maks 1 side, tre deler (B §3, K s. 9) | `c1/leveranse/kravrespons.md` (395 ord) | delvis: form OK, innhold utdatert (H3). B sier «fem overskrifter», men lister tre: følg de tre |
| 17 | Kode en annen kan kjøre + README (B §2, K s. 10) | `levering/fremmed.sh`, `c1/kaldstart.sh` (#2060) | delvis: kald start kl. 13 (#1952) ikke kjørt ennå |
| 18 | ETT kall reproduserer hovedresultatet (B §2) | `kjor.sh` (0,383), `kaldstart.sh` (0,474) | mangler for valgt hovedtall (H2) |
| 19 | Usikkerhet på tallet (B «etterprøvbarhet») | `JURY_METODE.md` §6 (KI 0,37–0,58) | delvis: ikke i README/1-sider (H12) |
| 20 | Kilder med URL i README (B §5) | `c1/leveranse/README.md` «Datakilder» | delvis: mangler arrangørens `real_votes`/`npx_votes`, Vanguard-policy-URL |
| 21 | AI-bruk oppgitt (B §5) | README «AI-verktøy» | dekket. «Ingen språkmodell i hovedresultatet» må sjekkes mot frosset agent |
| 22 | Kopiert/ekstern kode kreditert (B §5) | README «Datakilder» | delvis: nevn LightGBM, scikit-learn, Streamlit |
| 23 | Bare åpne kilder, ikke bygg på NBIM-databasen (B §5, §7, R) | SEC N-PX, nbim.no, arrangørens filer | dekket: real_votes er arrangørens fil, agenten kaller ingen API |
| 24 | Demo 5 min, kjørende, på holdout, ikke håndplukket (B §2, §4) | `c1/DEMO_MANUS.md` (utkast), `levering/demo/` | delvis: stubb (H7), tall i {KLAMMER} |
| 25 | Beslutningsstøtte: forstå og overprøve én sak (B §4, 20 %) | `levering/BESLUTNINGSSTOTTE.md`, `forklar.py` | delvis: avhenger av H4 og H6 |
| 26 | Sporbarhet, ingen irreversible handlinger (B §4) | `c1/leveranse/sporlogg.py`, sha-er i `kjor_agent_holdout2026.txt` | dekket. Agenten anbefaler bare |
| 27 | Erklærte begrensninger (B §4) | `c1/leveranse/BEGRENSNINGER.md` | delvis: skrevet for N-PX/Vanguard (H11) |
| 28 | Juryens spørsmål 1–3 (B §6) | `c1/leveranse/jury_svar.md`, `JURY_METODE.md` | delvis: TODO-tall (H11). B sier «fem», lister tre: forbered også «hva er lekkasjen?» og «hvordan valgte dere grensen?» |
| 29 | Innsending: e-post med gruppenavn og medlemmer, frist fre 06.11 kl. 12 (K s. 10) | `state/rapporter/epost_utkast_hackathon.md` | delvis: utkast laget, dommer verifiserer, guden sender |

**Oppsummert (29 krav):** 10 dekket, 16 delvis, 3 mangler (4 sitat, 14 motstandstest, 18 ett kall).
H1 er roten: så lenge agent, kaldstart og demo måler på N-PX mens metoden sier real_votes, kan ingen av tekstene (H3, H11, H12) skrives ferdig.

## Neste for speider
1. Ferdig: `state/rapporter/epost_utkast_hackathon.md` (H10), uten tall.
2. #1975 kl. 16.05: skrive om 1-sider, README, BEGRENSNINGER, JURY og demo-manus når H1 er avgjort.
