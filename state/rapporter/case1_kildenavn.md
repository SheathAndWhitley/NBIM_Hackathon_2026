# Case 1: NBIM eller Vanguard? Hvilke data og sitater hver del bygger på (#1994, dommer2)

**Kort svar:** Hovedtallet bygger på NBIMs **egne** stemmer. Norges Bank leverer selv N-PX (CIK 1374170). Hvert sitat i pakken er derimot hentet fra **Vanguards** policy. Ingen kode i pakken leser NBIMs retningslinjer. Casen tillater dette: «Velg én forvalter dere har N-PX-data for, og bruk den forvalterens egne retningslinjer» (`arbeid/hack/oppgave.md:1331-1334`). Feilen ligger i at noen tekster sier at sitatlaget siterer NBIM.

## 1. Hva hver del bygger på
| Del | Fasit | Kjennetegn | Sitatkilde |
|---|---|---|---|
| **Hovedmåler v3** (`c1/data_v3`, `lag_v3.py`, `leveranse/kjor.sh`) | NBIMs N-PX (Norges Bank, CIK 1374170), bare US say-on-pay, 4 383 forslag, test 2026 | NBIMs egne tidligere stemmer på selskapet (`nb_*`) | ingen (gulvregelen siterer ikke) |
| **Leder smed2 lgbm v3** (`oppgave_1981/train_v3.py`, `oppgave_1993/train_v3_g.py`) | NBIM, v3 | NBIM-historikk **+ Vanguards publiserte N-PX-stemmer på samme selskap** (`sec/vanguard_unik_1109.csv`, CIK 36405, bare stemmer innsendt før møtet) + SEC lønn/TSR | ingen |
| **Arkitekt #1970** | NBIM, v3 | NBIM-historikk + Vanguards tidligere MOT-andel | ingen |
| **Sitatagent smed3 v6** (`varianter/smed3_utf_sitat`) | **Vanguards** N-PX (Vanguard Index Funds, CIK 36405), måler v2, 1 544 forslag | Vanguard-train | **Vanguard** US-policy feb 2025 (`rl/vg_us_2025.txt`, SAI på EDGAR) |
| **Sitatagent på v3** (`varianter/dommer_v3_smed3kopi`) | NBIM, v3 | NBIM-train | **Vanguard** (samme `rl/`). Gir 0 MOT på test |
| **Demo** (`levering/demo`) | Vanguards N-PX (`c1/data`) | Vanguard-train | Vanguard feb 2025 (`retningslinjer.py:12`) |
| **Motstandstest** (`levering/motstandstest.py`, `case1_motstandstest.md`) | Vanguard | | Vanguard. `leveranse/motstand_inj.py` kjører på NBIM-regelen, som ikke leser tekst |
| **Speider #1977** (`c1/kilder/nbim_begrunnelser.csv`, 999 rader) | NBIMs egne begrunnelser fra stemmedatabasen på nbim.no, med lenke til Global Voting Guidelines og posisjonsnotater | | Ikke koblet til noen agent ennå |
| `c1/retningslinjer/nbim_*.md`, `punkter.jsonl` | | | NBIM-punkter finnes, men **ingen kode leser dem** (grep: bare `speider/c1ret/lag_retningslinjer.py`) |

Det betyr i praksis at pakken har to spor. Spor A er **NBIM**: fasit, hovedtall og leder. Spor B er **Vanguard**: sitater, demo og motstandstest med tekst. Agenten som siterer, er aldri målt med gevinst mot NBIM-fasit. På v3 siterer den Vanguards policy for NBIMs stemmer, og det er en direkte kildefeil.

## 2. Påstander som må rettes (fil:linje → rett tekst)
1. `arbeid/hack/c1/leveranse/README.md:52-54` sier «NBIM Global voting guidelines, brukt av sitatlaget» og «NBIMs posisjonsnotater, brukt av sitatlaget». **Dette er feil.** Rett tekst: «Sitatlaget siterer *Vanguard-advised funds: Proxy voting policy for U.S. portfolio companies* (feb. 2025), <URL/SAI-lenke>. NBIMs Global voting guidelines er lastet ned og delt i punkter (`retningslinjer/`), men brukes ikke av noen modell ennå.»
2. `arbeid/hack/c1/leveranse/kravrespons.md:17` sier «sitatlaget, som knytter anbefalingen til et punkt i NBIMs retningslinjer». Rett tekst: «sitatlaget, som i dag knytter anbefalingen til et punkt i **Vanguards** policy (åpen proxy). Med NBIMs begrunnelser per stemme kunne vi byttet til NBIMs egne retningslinjer.»
3. `arbeid/hack/c1/leveranse/README.md:44-50` (Kilder) og `kravrespons.md:7` nevner ikke Vanguard. Blir lederen (smed2 lgbm v3) hovedmodell, bruker den Vanguards N-PX som kjennetegn. Da må dette inn: «Kjennetegn: Vanguard Index Funds' N-PX (CIK 36405), bare stemmer som var offentlige før møtedatoen, <URL>.» Ellers er kildelista ufullstendig.
4. `arbeid/hack/c1/leveranse/sporlogg.py:9` har en plassholder i eksempelet: `kilde_punkt="NBIM retningslinjer 4.2 Godtgjørelse", kilde_url="https://..."`. Ingen slik kobling finnes. Bytt til et ekte Vanguard-punkt, eller merk linja som eksempel.
5. `arbeid/hack/c1/leveranse/JURY.md:34` sier «Bommene er styrevalg og say-on-pay» under NBIM-forbedringer. Bommene er Vanguard-bommer (v2). Rett tekst: «Bommene **på Vanguard-måleren** er styrevalg og say-on-pay.»
6. `arbeid/hack/c1/leveranse/JURY.md:41-61` (demo-manus) viser bare Vanguard-saker: Garmin, Dell og T-Mobile. Mange av dem er styrevalg og aksjonærsaker, som ikke finnes i NBIMs N-PX. I åpningen 0:00–0:40 trengs én setning: «Demoen kjører på Vanguards stemmer og Vanguards policy, fordi det er der vi har både fasit og et sitérbart regelverk for alle sakstyper. Hovedtallet er NBIMs egne stemmer.» Linje 11 («fondet følger styret i 9 av 10») er riktig for begge.
7. `arbeid/hack/levering/demo/README.md` og `app.py:109` er riktige: de sier Vanguard. Overskriften i appen bør likevel si «Vanguard-proxy», så juryen fra NBIM ikke tror det er NBIM.
8. Tavla, delmål #45, sier «Agenten siterer NBIMs retningslinjer». Det stemmer ikke i dag. Rett tekst: «Agenten siterer forvalterens retningslinjer (Vanguard; NBIM-kobling via #1977)». Delmålet eies av ordføreren.
9. `state/rapporter/case1_sitatsjekk.md:19` sier at «fasiten er Vanguards N-PX». Det stemmer for v6 på v2. Hovedtallet bruker likevel NBIM-fasit. Rapporten er riktig, men bør ikke siteres som om den gjaldt hele pakken.

Sjekket uten funn: `JURY.md:5-6, 15, 22, 67` (skiller NBIM og Vanguard riktig), `EVALUERING.md`, `case1_lekkasjesjekk/undergrupper/ruting/val_test_gap/lekkasjefri.md` (alle gjelder NBIM v3 og sier det), `case1_demo.md` og `case1_motstandstest.md` (sier Vanguard). Tallene i `JURY.md:22` og `kravrespons.md:14` er utdatert (LightGBM 0,325 mot dagens 0,51 uten lekkasje), men det er #1975/#1993 sin jobb.

## 3. Anbefaling: én setning, samme ordlyd overalt
> «Fasiten og hovedtallet er NBIMs egne stemmer (Norges Banks N-PX, bare amerikansk say-on-pay). Sitatene og demoen bruker Vanguard som åpen proxy, fordi NBIMs N-PX ikke har styrevalg eller aksjonærforslag og NBIMs stemmedatabase ikke har åpen eksport. Vanguard har både full N-PX og en punktvis offentlig policy, slik casen åpner for. Vi har ennå ikke koblet sitatene til NBIMs egne retningslinjer. Det er neste steg (speiderens 999 NBIM-begrunnelser, #1977).»

Setningen bør stå i README (øverst), i kravresponsen under «Hva vi bygde», i JURY.md over demo-manuset og i ett lysbilde i demoen. Ingen tekst skal si at en agent siterer NBIM før en agent faktisk leser `retningslinjer/nbim_*.md` og er målt på v3. Bruk av `nbim_begrunnelser.csv` som sitatkilde må også oppgis som skrapet fra nbim.no. Casen fraråder å «bygge noe som er avhengig av» databasen (`oppgave.md:1339`), så det bør stå som et tillegg og ikke som en bærende del.
