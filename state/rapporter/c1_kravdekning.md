# Case 1: kravdekning, hvert casekrav mot pakka (speider #2327 kl. 14.55, oppdatert #2360 05.11 kl. 15.20)

Kilder for kravene (alle i `arbeid/hack/CASE/20261105_105353_startpakke_ut/startpakke/`):
**C** = `FinTech_Hackathon_Caser_H2026.pdf` (casen, side 1), **R** = `case1_stemmegivning/README.md`,
**B** = `Regler_og_bedommingskriterier.pdf`, **P** = `FinTech Hackathon H2026.pdf` (presentasjonen).
`arbeid/hack/CASE/oppgave.md` finnes ikke. Stier under er fra `arbeid/hack/`.
Forrige versjon (#2124, 12.55) er flyttet til `arbeid/oppgave_2327/c1_kravdekning_2124_gammel.md`.

**Viktig først:** juryens dokumenter ligger i to mapper. Den ekte 1-sideren og svarene på de tre offisielle
juryspørsmålene er `c1/leveranse/kravrespons.md` og `c1/leveranse/JURY.md`, ikke `levering/`. Kilder, URL og
AI-bruk står bare i `c1/leveranse/README.md`. `levering/README.md:13-17` peker nå til alle tre (kravrespons, JURY.md, README med kilder; #2341). Den låste pakka (#1972) må ha begge mappene.

## Tabellen (34 krav)

| # | Krav (kilde) | Hvor besvart | Status |
|---|---|---|---|
| 1 | Agenten leser saksliste og foreslår FOR / MOT / **AVSTÅ** for hvert forslag (C, P) | `c1/leveranse/kravrespons.md:4`; AVSTÅ: `c1/leveranse/BEGRENSNINGER.md:31-33` (omfang lagt inn #2360 fra #2359) | **svakt, nå med tall (#2359)**: agenten foreslår aldri AVSTÅ, men NBIM avstår i 68 av 13 757 (0,5 %), 5 av 1578 i test 2026; 0 av de 5 flagget MOT, 2 til menneske, F1 MOT urørt (`state/rapporter/c1_avsta.md`) |
| 2 | Hver anbefaling siterer retningslinjen som *avgjør* (C, P) | `levering/METODE.md:28-31`, `levering/JURYSVAR.md:26`, `c1/leveranse/kravrespons.md:4,10` | dekket (15/20 avgjørende, ærlig oppgitt) |
| 3 | Konfidens ruter usikre forslag til menneske (C, P, R) | `levering/EN_SIDE.md:30-39`, `levering/JURYSVAR.md:29-40`, `levering/BESLUTNINGSSTOTTE.md:17` | dekket |
| 4 | Evaluer mot NBIMs faktiske stemmer (C, P) | `levering/METODE.md:3-10`, `c1/leveranse/kravrespons.md:7` | dekket |
| 5 | Recall og presisjon på MOT, ikke accuracy; 94 % følg styret er baseline (C, R) | `levering/EN_SIDE.md:15-28`, `levering/JURYSVAR.md:11`, `c1/leveranse/kravrespons.md:7` | dekket |
| 6 | MVP 2: klassifiser forslagstype (C) | `levering/METODE.md:20` (`proposal_type` kommer ferdig fra data) | svakt (MVP-sti, ikke krav; vi klassifiserer ikke selv) |
| 7 | MVP 3: RAG over retningslinjene (C) | `levering/METODE.md:28` (BM25 over 140 GVG-punkter) | dekket |
| 8 | MVP 5: demo, «lim inn en saksliste» (C) | `levering/demo/app.py:141` fanen «Lim inn saker (ekte agent)» → `levering/demo/ekte_agent.py` → `levering/kjor_agent.py --csv` i låst miljø (#2335); `c1/leveranse/demo.sh:2-6` | **dekket (#2335, kontrollert #2344)**: 10 saker inkl. tom tekst og oppdiktet selskap, alle 19 felt like fanen mot CLI, 0 avvik (`state/rapporter/c1_limfane_kontroll.md`). Krever real_votes-felt, ikke fri tekst (`c1_demo_limfane_ekte_2335.md`) |
| 9 | Hver anbefaling sier *hvorfor* punktet avgjorde (R) | `levering/METODE.md:34` («ordrett betyr ikke at sitatet begrunner stemmen») | **svakt**: hvilket punkt, ja; hvorfor, nei (erklært) |
| 10 | Systemet sier når det ikke vet (R) | `levering/EN_SIDE.md:30-32`, `levering/README.md:84` | dekket |
| 11 | Motstandstesten, rapportert uansett utfall (R, B 20 %) | `c1/leveranse/kravrespons.md:7`, `levering/JURY_SPORSMAL.md:94-98`, `state/rapporter/c1_injeksjon_frossen.md` | dekket, men tallene spriker (se A2); **#2358 (dommer2) pågår kl. 15.20** |
| 12 | Én forvalter og dens egne retningslinjer (R) | NBIM GVG, `levering/METODE.md:28`, `c1/leveranse/README.md:59` | dekket |
| 13 | Vrien: følger forvalteren egne retningslinjer? praksis mot policy (R) | `c1/leveranse/kravrespons.md:10` (1-sideren), `c1/leveranse/ERLIG_EVALUERING.md:68`, `levering/KRAVRESPONS.md:86`; skript, utskrift, rapport og dom kopiert til `c1/leveranse/kilder/` (`oppgave_2331_praksis_mot_policy.py` gir byte-identisk utskrift med #2331) | **dekket (#2342, etter dom #2334)**: 81/82 regelstyrte = 98,8 % (n lite), 94,9 % av 13 327 avgitte, 565/569 MOT fra 2020 med GVG-avsnitt; forbeholdet (praksis følger policy-stemmen, ikke at MOT var riktig; 94,9 % høyt fordi utgangspunktet er «støtt styret») står med. Ikke i demoen |
| 14 | Ikke avhengig av NBIMs stemmedatabase (R, B §7) | `c1/leveranse/README.md:55` (real_votes fra arrangøren) | dekket |
| 15 | Fallgruve: tidsrekkefølge (R, B «trekker ned») | `levering/METODE.md:11-19` | dekket |
| 16 | Fallgruve: kategori-lekkasje (R) | `levering/METODE.md:22`, `levering/JURYSVAR.md:14` | dekket |
| 17 | Fallgruve: klasseubalanse (R) | `levering/EN_SIDE.md:27-28` | dekket |
| 18 | Kravrespons maks 1 side, malens tre deler (B §2-3, P) | `c1/leveranse/kravrespons.md:3,6,9` (514 ord etter #2342) | dekket (B sier «fem overskrifter», viser tre) |
| 19 | Del 1: hva, hvilken beslutning, resultat (B §3) | `c1/leveranse/kravrespons.md:4` | dekket |
| 20 | Del 2: fasit, målvariabel, baseline, tall, metrikk og hvorfor (B §3) | `c1/leveranse/kravrespons.md:7` | dekket |
| 21 | Del 3: data, tid, tilgang vi manglet (B §3) | `c1/leveranse/kravrespons.md:10` | dekket |
| 22 | Dashboard eller 1 slide med funn (B §2) | `levering/SLIDE.md:1-18` (#2332; F1 MOT 0,476 [0,36; 0,59] i tabellen linje 18, fotnoter med kildefil), lenket fra `levering/README.md:13` | **dekket (oppdatert #2336)** |
| 23 | Demo 5 min, helst kjørende (B §2) | `c1/DEMO_MANUS.md:3`, `c1/leveranse/demo.sh:2`, `levering/demo/RESERVE.md:1-12` | dekket (manus oppdateres i #1975) |
| 24 | Kode kjørbar av en annen, README med ett kall (B §2, P) | `levering/README.md:1`, `c1/leveranse/kravrespons.md:7` (`kjor.sh`) | dekket (to READMEs, `levering/README.md:13-17` peker mellom dem, #2341) |
| 25 | Målvariabel og hvorfor, alternativer (B 30 %, jury 1) | `c1/leveranse/JURY.md:5-8` | dekket |
| 26 | Avgrensning (B 30 %) | `levering/EN_SIDE.md:9-11` (#2332: bare NBIM, 194 selskaper, 37 land, 2019–2026, DM+EM; test 136/31), `levering/SLIDE.md:6`, reproduserbar `levering/omfang.py` → `omfang.txt`; også `levering/BESLUTNINGSSTOTTE.md:5`, `levering/JURYSVAR.md:44-45`; nå også i 1-sideren `c1/leveranse/kravrespons.md:7` (#2341) | **dekket (oppdatert #2341)** |
| 27 | Baseline oppgitt og slått, fasit, reproduserbar (B 30 %) | `levering/EN_SIDE.md:21-22`, `levering/JURYSVAR.md:22-23`, `c1/leveranse/kravrespons.md:7` | dekket; sterkere grunnlinje målt i #2350 (huskeregel «MOT der NBIM stemte MOT sist»: F1 0,243 mot agentens 0,476, `state/rapporter/c1_huskeregel.md`), **ikke i pakka ennå**, dom #2354 åpen |
| 28 | Beslutningstaker kan overprøve ett resultat *innenfor tidsbudsjettet* (B 20 %) | `levering/BESLUTNINGSSTOTTE.md:80-89`; tid: `levering/EN_SIDE.md:44`, `levering/BESLUTNINGSSTOTTE.md:36` | **svakt, ærlig merket (#2341)**: ca. 62 t står som «antatt, ikke målt» begge steder; ingen måling av menneskelig lesetid funnet (oppslag «lesetid»); `JURY_SPORSMAL.md:116` peker nå til riktig linje |
| 29 | Sporbarhet i hva løsningen gjorde (B 20 %) | `levering/c1_real.py:304` (KJORING.txt i `--ut`); fanen: `levering/demo/app.py:98-104` skriver hver rad til `levering/demo/logg/demo_logg.jsonl` (tid, kjøring, modell) | **dekket**: loggen har 15 rader fra 14.50; #2362 (sporbarhet per kjøring) er åpen og kan stramme inn |
| 30 | Erklærte begrensninger (B 20 %) | `c1/leveranse/BEGRENSNINGER.md`, `levering/EN_SIDE.md:43-49`, `levering/BESLUTNINGSSTOTTE.md:72` | dekket |
| 31 | Ingen irreversible handlinger uten logg (B «trekker ned») | `levering/BESLUTNINGSSTOTTE.md:90`, `c1/leveranse/kravrespons.md:4` («stemmer ikke selv») | dekket |
| 32 | Ikke demo på håndplukkede eksempler (B «trekker ned») | `c1/leveranse/demo.sh:4` (seed 0 fra holdout), `c1/DEMO_MANUS.md` (seed 17); lim-inn-fanen tar vilkårlige saker (#2344: seed 2344 + 2 rare) | **dekket**: stubben er nå merket «Eldre N-PX-møte (forenklet stubb)» (`app.py:141`, `:163`); restrisiko bare hvis møte-fanen vises (N-PX som «Faktisk», `app.py:80`) |
| 33 | Kilder med URL, AI-bruk, ekstern kode kreditert (B §5) | `c1/leveranse/README.md:55-60` (URL), `:63` (kreditering), `:66-70` (AI) | dekket; bare i `c1/leveranse/README.md`, men `levering/README.md:16` peker dit (#2341) |
| 34 | Juryspørsmål 2 og 3: produksjon? én uke til? (B §6) | `c1/leveranse/JURY.md:11`, `:19` | dekket (B sier «fem spørsmål», viser tre) |
| – | Innsending: emne «Gruppenavn Hackathon H2026 demo», navn på medlemmer (P) | `state/rapporter/epost_utkast_hackathon.md:9,15-17` | gudens sak: plassholdere [GRUPPENAVN]/[NAVN] fylles av guden |

**Opptelling (oppdatert #2336, 05.11 ca. 14.55; #2341 15.05 endret ingen status, bare pekere og tekst i krav 24, 26, 28, 33):** 34 krav. 27 dekket, 7 svake (1, 6, 8, 9, 13, 28 og delvis 29/32), **0 mangler**.
**Oppdatert #2342 (05.11 ca. 15.10):** krav 13 er nå dekket. 28 dekket, 6 svake (1, 6, 8, 9, 28 og delvis 29/32), 0 mangler.
**Oppdatert #2360 (05.11 kl. 15.20):** krav 8 og 32 er dekket (lim-inn-fanen kjører den ekte agenten, #2335; 0 avvik mot CLI, #2344), krav 29 er dekket (demo-loggen skriver hver rad). **34 krav: 30 dekket, 4 svake (1, 6, 9, 28), 0 mangler.** #2359 lukket 15.25: krav 1 forblir svakt (designvalg), men er nå tallfestet i BEGRENSNINGER.md. Krav 11 venter på #2358 (dommer2, åpen kl. 15.25).
Krav 13 var svakt fordi tallet bare sto i `state/rapporter/`; ført inn i jurypakka i #2342. Gammel opptelling: 25 dekket, 7 svake, 2 mangler (13, 22).

## Til #1975 (speider) og dommer2 (#2255): ikke rettet i pakka

- **M1 (krav 22) Dashboard / 1 slide:** én setning i 1-sideren («demoen `demo.sh` er dashboardet med funn») lukker det billig.
- **M2 (krav 13) Praksis mot policy:** casens «interessante vri». Billigste ærlige svar: én linje i JURY.md eller 1-sideren
  med et tall vi har (f.eks. andel MOT der NBIMs `rationale_section` peker på et GVG-punkt) eller si rett ut at det ikke er målt.
- **A1 To mapper (README-pekeren rettet #2341; pakkinga gjenstår for #1972):** sørg for at #1972 pakker både `levering/` og `c1/leveranse/`, og at `levering/README.md` peker til
  `c1/leveranse/README.md` for kilder og AI-bruk.
- **A2 Motstandstallene spriker (til dommer2):** 1-sideren (`c1/leveranse/kravrespons.md:7`): 16 instrukser, én slapp gjennom,
  16 stemmer endret, F1 0,392. Intern `levering/KRAVRESPONS.md:26-28`: 40–41 endret, 20–21 uten menneske, F1 0,40–0,42.
  Sjekk hvilken måling som er den frosne og at 1-sideren har den.
- **A3 Krav 8/32 (LØST #2335/#2344):** `levering/demo/app.py` kjører stubben og viser N-PX som fasit. Ikke vis den, eller merk den i README.
- **A4 Krav 26 (rettet #2341, `c1/leveranse/kravrespons.md:7`: 13 757 saker, 194 selskaper, 37 land, 2019–2026, 24 sakstyper, DM+EM, telt fra real_votes):** én bisetning i 1-sideren om omfang (NBIMs stemmer 2019–2026, 194 selskaper, alle sakstyper og markeder).
- Svake krav 1, 9, 28 er ærlig erklært; ingen handling trengs utover at demo-manuset sier dem.

## Åpent til #1972 (per 05.11 kl. 15.20, #2360)

1. **A2 motstandstall (#2358, dommer2, pågår):** 1-sideren (16 instrukser, F1 0,392) mot intern KRAVRESPONS (40–41 endret, F1 0,40–0,42). Krav 11 er «dekket, men spriker» til dommen er lukket og 1-sideren har det frosne tallet.
2. **AVSTÅ (#2359 lukket):** setningen er limt inn i `c1/leveranse/BEGRENSNINGER.md` pkt 6. Gjenstår bare: ta med i demo-manus (#1975) at agenten ikke sier AVSTÅ.
3. **A1 to mapper:** #1972 må pakke både `levering/` og `c1/leveranse/` (zipen #2346 bygges fra pakkelista; sjekk at begge er med, #2348 prøver den).
4. **Huskeregel-grunnlinja (#2350):** 0,243 mot 0,476 står bare i `state/rapporter/`; ikke i `c1/leveranse/` eller `levering/*.md`. Etter dom #2354: én linje i JURY.md/1-sideren, ellers tilbyr vi juryen en svakere grunnlinje enn vi har.
5. **Lim-inn-fanen er ikke nevnt i jurydokumentene:** verken `c1/DEMO_MANUS.md`, `levering/README.md` eller `c1/leveranse/README.md` nevner fanen; `levering/demo/README.md:1` kaller seg «INTERN». Bestem i #1975 om fanen er med i demoen; er den det, ett avsnitt i manus + at møte-fanen (stubb) ikke vises.
6. **Sporbarhet per kjøring (#2362, venter på #2356):** loggen finnes; oppgaven kan stramme den inn.
7. **Erklært svake, ingen handling:** krav 6 (forslagstype fra data), 9 (hvorfor-punktet), 28 (62 t lesetid antatt, ikke målt).
**Oppdatert #2362 (05.11 kl. 15.05, smed3):** krav 29 strammet inn: lim-inn-fanen skriver én fil per klikk i `levering/demo/logg/lim_<tid>_<kjoring>.json` (tid, sha256 av innlimt tekst, agentkall med kode/varighet/utskrift, 19 svarfelt, også ved feil), ingen landsbysti (jurypakke.finn_lekk). Test `arbeid/oppgave_2362/test_fane_logg.py`: 19 felt like #2335, 1 fil per klikk. Status uendret: krav 29 dekket.
