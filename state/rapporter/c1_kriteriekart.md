# Case 1: juryens kriterier koblet til bevis i JURY.md (speider #2390, 05.11 15.30)

Kriteriene er fra `arbeid/hack/CASE/20261105_105353_startpakke_ut/startpakke/Regler_og_bedommingskriterier.pdf.pakk_ut.txt` linje 31–57 (§4) og 65–70 (§6), og casekravene fra `FinTech_Hackathon_Caser_H2026.pdf.pakk_ut.txt` linje 10–15.
Linjenummer gjelder `arbeid/hack/c1/leveranse/JURY.md` slik fila sto 15.25 (77 linjer, før #1975). Kildestier er fra `leveranse/`. Alle 28 kildefiler som JURY.md viser til finnes på disk. Jeg har sjekket at de finnes og at de står i pakkelista (`arbeid/oppgave_2333/pakkeliste.txt`), men har ikke målt tallene på nytt. Den kontrollen er #2255.
Status: **OK** = besvart med kilde i pakka. **SVAKT** = besvart, men beviset er tynt eller ligger et annet sted. **MANGLER** = ikke besvart i JURY.md.

## Metode og ærlig evaluering (60 %)

| # | Kriterium (regler/case) | Hvor i JURY.md | Bevis (måler/rapport) | Status |
|---|---|---|---|---|
| 1 | Problemforståelse 30 %: valg av målvariabel og hvorfor | 4, 26–30 | `maaler_offisiell_v3.py` (MOT-definisjon), `kilder/oppgave_2234_baseline_real_test.txt`, `kilder/case1_hvilken_fasit.md` | OK |
| 2 | Avgrensning | 29 (AVSTÅ), 70 (pkt. 5, aksjonærforslag), 71 (pkt. 6, lite data) | `kilder/c1_mot_sakstyper.md`, `kilder/tell_aar.txt`, `kilder/tell_trening.py` | SVAKT: avgrensningen er spredt over begrensningene. Hva datasettet dekker (194 selskaper, 37 land, 2019–2026) står i `kravrespons.md:7`, ikke i JURY.md |
| 3 | Forstår hvilken beslutning løsningen støtter | 6, 32–38 (sortering for analytiker, ikke automatisk stemme) | `kilder/TREFFSIKKERHET.md`, `kilder/c1_mennesket_arbeid.md` | OK |
| 4 | Jury-spm. 1: målvariabel og alternativer | 26–30 | `kilder/oppgave_2234_baseline_real_test.txt`, `kilder/case1_hvilken_fasit.md` | OK |
| 5 | Evaluering 30 %: baseline oppgitt og slått | 11–23 (tabell, +0,11 [0,01; 0,22] over b2) | `kilder/c1_enkle_regler_og_hist1.md`, måler v3 sha 418a937e57 | OK |
| 6 | Riktig metrikk (recall/presisjon på MOT, ikke accuracy; case s. 1) | 5, 28, 66 (P 0,441, R 0,517) | `levering/kjor_agent_real_test2026.txt`, `kilder/oppgave_2234_baseline_real_test.txt` | OK |
| 7 | Fasit brukt (NBIMs faktiske stemmer) | 9, 30 | `kilder/case1_hvilken_fasit.md`, README:55 (https://vd.nbim.no/) | OK |
| 8 | Resultatet kan reproduseres (ett kall) | 9 (nevner `kjor.sh` og `/tmp/c1_kald`) | `README.md:29` `bash arbeid/hack/c1/leveranse/kjor.sh`, kaldstart `state/rapporter/c1_pakkeliste.md:9` | SVAKT: JURY.md sier ikke selve kommandoen og hvor lang tid den tar. Den står bare i README |
| 9 | Trekker ned: lekkasje / tilfeldig splitt | 4, 9, 72 (pkt. 7) | `ERLIG_EVALUERING.md:28` og `:54` (brute force på 400 rader, assert på forbudte kolonner), `kilder/dommer_ablasjon_v2.md` | SVAKT: JURY.md nevner tidssplitten, men ikke lekkasjesjekken (400 rader, 0 avvik) eller forbudslista. Juryen må til ERLIG_EVALUERING |
| 10 | Trekker ned: ytelse som ikke kan reproduseres | 9, 12 | måler v3 + kald kjøring; tallvakt i `c1_pakkeliste.md:9` | OK |
| 11 | Ærlig usikkerhet (KI, seed, under målet) | 5, 67 (pkt. 2) | `kilder/oppgave_2095_ki_mot.py`, `kilder/c1_seed_frossen.md`, `c1/tall_tabell.md` | OK |
| 12 | Test ikke brukt til å velge | 56–61 | `kilder/c1_tiltak1_malt.md:18-25`, `kilder/c1_feil_stabilitet.md:23` | SVAKT: båndet [0,15; 0,85) ble valgt fra en tabell på test 2026 (`JURY_SPORSMAL.md:27`), men JURY.md:40 sier «låst på val 2025». **De to filene sier ulike ting.** Den ene må rettes |
| 13 | Feilanalyse: hvor den bommer | 24, 68–69, 77 | `kilder/c1_bommene.md`, `kilder/c1_falske_mot.md` | OK |

## Beslutningsstøtte og robusthet (40 %)

| # | Kriterium | Hvor i JURY.md | Bevis | Status |
|---|---|---|---|---|
| 14 | Forklarbarhet 20 %: kan forstå og overprøve et enkeltresultat innenfor tidsbudsjettet | 6 («kilde:»-linja), 75 (pkt. 10, sitat), 77 (pkt. 12) | `kilder/c1_sitat_verifisert.md`, `kilder/demo_saker.md` | **MANGLER: tid.** Ingen målt tid for å overprøve ett flagg. `BEGRENSNINGER.md:38` har bare maskinens tid (4,3 s per sak). Case 1 oppgir ikke noe tidsbudsjett per sak. Case 2 oppgir 30 sekunder per flagg, og juryen bruker trolig samme mål |
| 15 | Sitat av avgjørende retningslinje (case) | 75 (pkt. 10: 15/4/1 av 20) | `kilder/c1_sitat_verifisert.md`, `kilder/c1_retningslinje_sitat.md` | OK |
| 16 | Konfidens som ruter usikre saker til menneske (case) | 6, 34, 40–49 (båndtabell), 73 (pkt. 8) | `kilder/c1_mennesket_arbeid.md`, `kilder/TREFFSIKKERHET.md` | OK |
| 17 | FOR / MOT / AVSTÅ per forslag (case) | 29, 74 (AVSTÅ aldri foreslått) | `BEGRENSNINGER.md` pkt. 6 | OK, erklært som begrensning |
| 18 | Jury-spm. 2: i produksjon? | 32–38 | `kilder/TREFFSIKKERHET.md` | OK |
| 19 | Jury-spm. 3: én uke til | 51–54 | `kilder/c1_injeksjon_hoflig.md`, `kilder/c1_titlecase_vakt.md`, `kilder/c1_bommene.md` | OK |
| 20 | Robusthet 20 %: motstandstesten gjennomført | 36, 52, 76 (pkt. 11) | `kilder/c1_injeksjon_etter_2205.md`, `kilder/c1_injeksjon_hoflig.md`, `kilder/c1_titlecase_vakt.md`; kjøres i `kjor.sh:39` (`motstand_inj.py`) | OK. Utfallet er ærlig rapportert: 6 av 16 nye instrukser slipper gjennom |
| 21 | Robusthet: rare felt / nye selskaper | 74 (pkt. 9) | `kilder/c1_robusthet_frossen.md` | OK. #2380 og #2386 kan endre tallene |
| 22 | Sporbarhet i hva løsningen gjorde | 9 (agentlogg `levering/kjor_agent_real_test2026.txt`), 6 («kilde:») | `kjor.sh:26-41` (`kjoring.log`), lim-inn-fanen logger hvert klikk (commit d51d58e, #2362) | **MANGLER:** JURY.md forklarer ikke sporbarheten. Det står ikke hvor loggen per kjøring og per sak ligger eller hva den inneholder |
| 23 | Erklærte begrensninger | 63–77 (12 punkter) | `BEGRENSNINGER.md` + kildene per punkt | OK |
| 24 | Trekker ned: irreversible handlinger uten logg/bekreftelse | 33 («Nei, som automatisk stemme»), 6 | – | SVAKT: det står ingen steder rett ut at agenten bare skriver en anbefalingsfil og aldri sender en stemme |
| 25 | Trekker ned: demo på håndplukkede eksempler uten holdout | – | `kilder/demo_saker.md:5` (første sak av hver type, test 2026), `DEMO_MANUS.md:6` | SVAKT: valgregelen står i pakka, men ikke i JURY.md |

## Brutte eller svake kilder
- **JURY.md:77 viser til `state/rapporter/c1_beslutning_nyeste_historikk.md`.** Fila står ikke i pakkelista, så juryen får den ikke. Den bør kopieres til `leveranse/kilder/`, eller henvisningen bør fjernes.
- JURY.md:9 og 12 viser til `levering/kjor_agent_real_test2026.txt` og `c1/tall_tabell.md`. Begge står i pakkelista (linje 12 og 40), så her er det i orden.

## Forslag til #1975 (tekst etter frysen, i prioritert rekkefølge)
1. Rett motsigelsen om båndet (rad 12): enten JURY.md:40 eller JURY_SPORSMAL.md:27.
2. Legg til én setning om sporbarhet (rad 22) og om irreversible handlinger (rad 24), f.eks.: «Agenten skriver bare en anbefalingsfil og en logg per kjøring (`kjoring.log`) og per klikk i lim-inn-fanen. Den sender aldri en stemme.»
3. Legg til én setning om lekkasjesjekken (rad 9) og valgregelen for demosakene (rad 25), med kilde.
4. Overprøvingstid (rad 14): ta tida på én analytiker som overprøver 5 flagg fra demoen og oppgi medianen. Har vi ikke tid, skriv i JURY.md at tida ikke er målt.
5. Kopier c1_beslutning_nyeste_historikk.md inn i `kilder/`, eller fjern henvisningen.
