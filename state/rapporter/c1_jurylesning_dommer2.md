# Case 1: pakka lest som jury (#2258, dommer2, 05.11 kl. 14.10)

Lest: `c1/leveranse/JURY.md`, `c1/leveranse/kravrespons.md`, `c1/DEMO_MANUS.md` (alle fra kl. 13.06–13.40), som et jurymedlem som
vekter metode og ærlig evaluering 60 %. Hver påstand om metode, evaluering, robusthet eller menneske-ruting er sjekket mot
filen den peker på. Tallene i seg selv måles på nytt i #2255 etter frys; her gjelder bare om belegget finnes og stemmer med teksten.

## Det som holder (påstand -> belegg funnet, tallet står der)
- F1 0,476 / P 0,441 / R 0,517 / TP 30 FP 38 FN 28, 58 MOT av 1539 -> `kjor_agent_real_test2026.txt`, README, `c1_kaldstart_2.md` (byte-lik svarfil, #1952).
- Accuracy 96,2 % følg styret, agent 95,7 %; aksjonærforslag=MOT finner 2 av 58, F1 0,066 -> `arbeid/oppgave_2234/baseline_real_test.txt` (0,0656), README (TN 1443).
- N-PX-regelen 0,645 bygde på feillest fasit -> `case1_hvilken_fasit.md`.
- KI [0,36; 0,59], klyngebootstrap 2000 trekk -> `c1_bootstrap_f1.md`.
- Enkle regler b 0,287, b2 0,365, golv h1 0,415, +0,11 [0,01; 0,22] -> `c1_enkle_regler_og_hist1.md` (#1116–#1118).
- Uten historikk 0,282 på avvik, ablasjon -> `c1_ablasjon_v2.md` og `ERLIG_EVALUERING.md`.
- 17 av 28 bommer med P ≤ 0,09, 7 av 17 i USA, 0 av 7 USA, 0 av 17 eneste MOT, 0 av 4 uten MOT før, 5 Delaware/Texas-saker -> `c1_bommene.md`.
- 56 av 58 MOT på styrets forslag, styrevalg 26 / revisor 7 / andre 6 / øvrige 11 -> `c1_mot_sakstyper.md`.
- Til menneske 188 av 1578, 183 av 1539, 1 instruks -> `c1_dommer_kjorer_selv.md` (#2207), `kjor_agent_real_test2026.txt`.
- 183 rutede inneholder 21 av 30 treff og alle 38 falske; 9 MOT-flagg utenfor er alle riktige -> `levering/TREFFSIKKERHET.md`.
- Nye selskaper 0,375 og 99,4 % rutet; tom tekst/felt til menneske -> `c1_robusthet_frossen.md` (#2144), `BEGRENSNINGER.md` pkt 3.
- Sitat-stikkprøve 20 MOT: 15 / 4 / 1 -> `c1_sitat_verifisert.md` (#2115). 86 % samme GVG-seksjon (54 av 63) -> `c1_retningslinje_sitat.md`.
- Historikk uten lekkasje, 400 rader mot brute force -> `dommer_ablasjon_v2.md` (#2098).
- Terskel 0,9188 valgt på val (val 0,520, test 0,476; test-optimum 0,95 ikke valgt) -> `c1_terskel_val_test_2193.md`, `TREFFSIKKERHET.md` rad 75.
- Forbudte kolonner stoppes av assert -> `c1_real.py` l. 7–8 og 147, `kjor_agent_real_test2026.txt` («FORBUDT og ikke brukt»).
- 97,4 % er andel riktige FOR -> `levering/JURY_SPORSMAL.md` S0. Demo-trekk seed 17 -> `demo_trekk_2026.py` skriver alle forsøkte seeds.

## Hull: påstander uten belegg, eller der belegget sier noe annet

| # | Hvor | Påstand | Belegg | Hva juryen ser |
|---|---|---|---|---|
| H1 | JURY.md Q2 kule 3, Q3 pkt 1, Begr. pkt 11; kravrespons «Motstandstest» | «kindly support/oppose» slipper gjennom, 20–21 saker bytter stemme urutet, F1 faller til 0,387–0,400. Å tette hullet er «dag 1–2» i neste uke. | **Motsagt av koden.** `levering/c1_real.py` l. 153–163 har vakta fra #2237 (`injeksjon_hoflig.py`, kopiert av `fremmed.sh` l. 20). `c1_injeksjon_hoflig.md` tabell: begge «kindly»-varianter flagges nå 1578/1578, 0 urutet, F1 0,476. #2241 (smed3) måler at den koster 0 treff. | Pakka beskriver en svakhet agenten ikke lenger har, og lover som neste steg noe som allerede er gjort. En jury som kjører angrepet selv, ser avviket. Enten er #2237 med i frysen (da må tekstene skrives om og pkt 11 bli «tettet, målt i `c1_injeksjon_hoflig.md`»), eller så skal vakta ut. Må avgjøres før kl. 16. |
| H2 | kravrespons tabell rad 2–3; JURY.md tabell rad «Regel a» | Historikkregel «selskapet hadde MOT før»: kravrespons sier **0,091** (P 0,048, R 0,845); JURY.md sier **0,097** [0,072; 0,124] for samme regel. «Selskap + forslagstype» 0,145 finnes bare i kravresponsen. | 0,097 er målt som forsøk #1115 (`c1_enkle_regler_og_hist1.md`). 0,091 og 0,145 står bare som «målt nå» i `hack_c1_leveranse1.md`, skript `levering/c1_v1/hist_regel.py` (gammel mappe), ingen logg eller forsøk på tavla. | To tall for samme regel i to jurydokumenter. Velg ett (0,097 har forsøk-id og KI), eller forklar forskjellen i definisjon. |
| H3 | kravrespons «Hva vi bygde» | Båndet [0,15; 0,85) er «låst på val 2025». | `c1_menneske_terskel.md` (#2128) velger båndet fra en tabell over **test 2026** (122 saker, 30 av 66 MOT) og nevner val bare som «viser samme mønster». Ingen val-tabell i pakka. | Juryen vekter ærlig evaluering. «Låst på val» er for sterkt når valgtabellen er test. Skriv ærlig: «valgt på et fast rutenett, sjekket på val 2025», eller legg ved val-tabellen som grunnlag. |
| H4 | kravrespons «Hva vi bygde» og ERLIG_EVALUERING § 2 | «NBIM publiserer stemmene løpende», og 0,06 av F1 hviler på det. | Ingen kilde. README lenker vd.nbim.no, men ingen tekst sier *når* NBIM publiserer i forhold til møtedato. Påpekt før i `c1_jurylesning.md`, fortsatt uten kilde. | Én setning med lenke til NBIMs egen side om publiseringstidspunkt. Finnes den ikke, si «antakelse» og vis golvet 0,415 like tydelig. |
| H5 | kravrespons «Hvordan vi verifiserte» | Val 2025: 0,520 (0,41–0,63). | 0,520 står i `TREFFSIKKERHET.md`; kjøreloggen sier 0,5217 og `c1_bootstrap_f1.md` sier 0,522 [0,403; 0,624]. Intervallet (0,41–0,63) finnes ikke i noen fil. | Lite, men en jury som leser bootstrap-rapporten ser 0,522 og [0,40; 0,62]. Bruk tallene fra rapporten. |
| H6 | JURY.md Begr. pkt 6 | «70–99 MOT mot styret per år», «test er 141 møter i 136 selskaper», «egen telling». | Ikke i `ERLIG_EVALUERING.md` (som pkt 6 viser til). `arbeid/oppgave_2216/tell.py` finnes, men ingen lagret utskrift. | «Egen telling» uten fil er ikke belegg. Lagre utskriften fra `tell.py` og pek på den. |
| H7 | DEMO_MANUS sak 6 | «799 NBIM-begrunnelser har bare 18 ulike tekster» (`c1/kilder/nbim_begrunnelser.csv`). | Fila har **999** rader og **19** unike begrunnelser (talt nå). Ingen rapport inneholder 799. | Tallet er feil eller gjelder et utvalg (f.eks. før test-start). Tell på nytt og skriv hvilket utvalg. |
| H8 | DEMO_MANUS 4:30 | «målt én gang med arrangørens måler». | README: «Måleren `maaler_offisiell_v3.py` er vår egen». `MAALER_LES.md` sier det samme. | Selvmotsigelse i pakka. Skriv «vår egen måler, kode i pakka». |
| H9 | DEMO_MANUS sak 6 / kravrespons | Agenten sier MOT i «71» saker (demo), 68 MOT-flagg (kravrespons: 30+38), «MOT styret 74» (`kjor_agent_real_test2026.txt`). | Alle tre tall er ekte, men fra tre ulike tellinger (1578 inn, 1539 med fasit på avvik, 1539 på MOT). Ingen fil forklarer det. | Én setning i demoen: «74 av 1578; 71 blant de 1539 med fasit, 68 regnet mot MOT-fasiten». |
| H10 | kravrespons «Motstandstest» | «På logreg-modellen #2046 (test #2047) snudde en frase 82 av 174 saker. Resultatet på den frosne modellen kommer fra #2144 og står i BEGRENSNINGER.md.» | 82/174 står bare som bisetning i `c1_injeksjon_frossen.md` l. 45 (gammel modell). Resultatet på den frosne modellen (20–21 urutet) er fra #2212, `c1_injeksjon_etter_2205.md`, ikke #2144 (det er robusthetstestene). Og se H1. | Kravresponsen nevner et gammelt tall og peker feil for det nye. Stryk #2046-tallet, pek på riktig fil, og rett etter H1. |
| H11 | kravrespons «Hvordan vi verifiserte» | «Svarfila består lekkasjevakta (`sjekk_lekkasje.py svar`)». | Kjørt én gang (`hack_c1_leveranse1.md`), men ikke i `kaldstart.sh`, `fremmed.sh`, `kjor.sh` eller `sluttkontroll.sh`. | Juryen kan ikke reprodusere det med «ett kall». Legg kallet i sluttkontroll, eller pek på rapporten. |
| H12 | JURY.md Q2 kule 1 | Peker på `levering/TREFFSIKKERHET.md`. | Stien er relativ til `c1/leveranse/` og finnes ikke der; fila er `arbeid/hack/levering/TREFFSIKKERHET.md`. Samme med `JURY_SPORSMAL.md` og `METODE.md` i demoen. TREFFSIKKERHET definerer dessuten ruting som «konfidens < 0,6», JURY.md som «P(MOT) i [0,15; 0,85)» (samme 183 saker). | Død lenke og to ulike beskrivelser av samme ruting. Bruk full sti fra landsbymappen, og ett språk for rutingen. |
| H13 | JURY.md Begr. innledning | «kald kjøring `/tmp/c1_kald` 05.11 12:29». | `/tmp` er borte for juryen. | Pek på `kjor.sh` og loggfila i pakka i stedet. |

Ikke hull, men verdt å vite: demo-trekket (`demo_trekk_2026.py`) krever «fasit MOT (avvik fra styret)», altså `against_board`, som også
teller AVSTÅ; manuset sier «NBIM stemte mot styret». For seed 17 er begge sakene ekte Against, så det endrer ingenting nå.

## Anbefalte oppgaver (speider eier tekstene; jeg retter ikke)
1. **H1 (viktigst, før frys kl. 16):** avgjør om #2237-vakta er med i frysen. Er den det: skriv om JURY.md Q2/Q3/pkt 11 og
   kravresponsens motstandsavsnitt til «tettet, målt i `c1_injeksjon_hoflig.md` og #2241», og flytt Q3 pkt 1 til noe som
   faktisk gjenstår. Er den ikke det: fjern importen fra `c1_real.py` (smed) og la tekstene stå. Én oppgave til speider + smed, 20 min.
2. **H2 + H5 + H10:** én tallrydding i kravresponsen: regel a = 0,097 (eller forklar), val = 0,522 [0,40; 0,62], stryk #2046-tallet,
   pek på `c1_injeksjon_etter_2205.md`/`c1_injeksjon_hoflig.md`. Speider, 20 min. Går inn i #2229 (én side) og #2255.
3. **H3:** omformuler «låst på val 2025» for båndet, eller lag val-tabellen (smed3 kan kjøre `menneske_tabell.py` på val, 10 min).
4. **H4:** finn NBIMs egen tekst om når stemmer publiseres, lenk den i kravrespons og ERLIG_EVALUERING. Finnes den ikke: «antakelse». Speider, 15 min.
5. **H6 + H7 + H9:** lagre `tell.py`-utskrift i pakka; tell begrunnelses-csv på nytt (999/19 nå) og rett demoen; én setning om 74/71/68. Speider, 15 min.
6. **H8 + H12 + H13:** «arrangørens måler» -> «vår egen måler»; fulle stier; ett språk for ruting. Går inn i #1975.
7. **H11:** legg `sjekk_lekkasje.py svar` i `sluttkontroll.sh` (smed, 10 min), eller pek på rapporten i kravresponsen.

Alt over gjelder belegg, ikke tallene. Tallene måles på nytt i #2255 etter frys.
