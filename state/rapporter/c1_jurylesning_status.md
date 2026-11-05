# Case 1: er funnene fra jurylesningene #2129 og #2281 rettet i dagens leveranse/? (#2428, arkitekt, 05.11 15.50)

Bare lest, ingenting endret. Jeg sjekket `arbeid/hack/c1/leveranse/` slik den sto kl. 15.40–15.50.
Kildene: #2129 (de fem punktene i oppgaveresultatet; rapportfila ble overskrevet av #2281) og `c1_jurylesning.md` (#2281).
Linjenumrene viser til dagens filer.

## Status
| # | punkt (kilde) | status | bevis (fil:linje) |
|---|---|---|---|
| 1 | METODE beskriver N-PX og ikke den leverte modellen (#2129 pkt 1) | rettet | Det finnes ingen METODE i leveranse/. ERLIG_EVALUERING:3 beskriver «miks h2», og README:23 sier at N-PX og Vanguard ikke er med |
| 2 | `--hist 2` bruker samme sesong, mens pakka sa «bare år før» (#2129 pkt 2) | rettet | BEGRENSNINGER:10, JURY:72, JURY_SPORSMAL:22–23 |
| 3 | Løpende publisering er antatt uten kilde (#2129 pkt 2, #2281 b) | rettet (sagt rett ut) | kravrespons:10 («antatt og ikke dokumentert»), BEGRENSNINGER:10–11 |
| 4 | Ingen ærlig grunnlinje på real, bare «følg styret» = 0 (#2129 pkt 3) | rettet | JURY:5, JURY:17 (b2 0,365), JURY:21 (golv 0,415), ERLIG:66–67 |
| 5 | Sitatkilden er Vanguard eller NBIM (#2129 pkt 4) | rettet | README:3–4, 61. Vanguard står bare i README:23 som «ikke med» |
| 6 | Tre ulike rutingtall, og N-PX-tabell i README (#2129 pkt 5) | rettet | Samme regel i README:4–5, README:52 og ERLIG:56. README:43–46 viser utskriften fra real |
| 7 | #-numre og intern sjargong (#2281 a) | **ikke rettet (kommet tilbake)** | Det er 69 treff i 18 filer, mot 0 etter #2281: JURY:77 (forsøk #2363, #2366), JURY_SPORSMAL:53–54 («smed #2412, dommer #2414»), demo.sh:2,5, demo_utskrift.txt:1 («smed2 #2044-modell»), NESTE_VERSJON:3,4,19,21,45 («smed3 #2323, forsøk #1171»), kilder/c1_robusthet_kald_2380.md (13), kilder/c1_robusthet_reprod.md (10) |
| 8 | Pekere til filer utenfor pakka (#2281 a) | **ikke rettet (nye)** | JURY_SPORSMAL:54 (`state/rapporter/c1_offline_kaldstart.md`, `arbeid/oppgave_2412/…`), JURY:77 (`state/rapporter/c1_beslutning_nyeste_historikk.md`), NESTE_VERSJON:21,47,55 |
| 9 | TALLVAKT RØD fra NESTE_VERSJON:51 TP/FP/FN 59 28 40 (#2281 «Viktig») | rettet | `grep "59 28 40" NESTE_VERSJON.md` gir 0 treff. Tavla melder grønn kaldstart |
| 10 | Val 2025 står som 0,520 og som 0,522 (#2281 b) | rettet | ERLIG_EVALUERING:50 skiller dem (MOT mot avvik). Kilden er kilder/c1_val_kaldstart.md:23–25 (0,5202 MOT, 0,5217 avvik) |
| 11 | 0,520 finnes bare i loggen (#2281 c) | rettet | kilder/c1_val_kaldstart.md:23 (målt på nytt fra kald start, måler v3), JURY_SPORSMAL:8 |
| 12 | KI for val [0,41; 0,63] | rettet | kilder/c1_tall_likt.md:6, BEGRENSNINGER:7 |
| 13 | 11 785 treningssaker forklares ikke (394 rader) (#2281 c) | rettet | ERLIG_EVALUERING:3, JURY:71 (394 uten fasit, kilder/tell_trening.py) |
| 14 | Sitatpåstander uten kilde i pakka (15/4/1, 18 av 18, 86 %) (#2281 c) | rettet | BEGRENSNINGER:28 og JURY:75 viser til kilder/c1_sitatkilder.md og kilder/c1_sitat_verifisert.md. kilder/c1_retningslinje_sitat.md ligger i pakka |
| 15 | Kjøretid fra kald start: 29 s, 52 s eller 31–52 s (#2281 b) | **ikke rettet** | README:39 sier «29 s», BEGRENSNINGER:38 sier «52 s fra kald start». Ingen setning forklarer forskjellen |
| 16 | «ca. 12 s» for hele agenten har ingen kilde (#2281 b) | **ikke rettet** | README:52. Det finnes ikke noe 12 s i kilder/c1_kjoretid.md, som gir 4,8 s for agenten alene (BEGRENSNINGER:38) |
| 17 | «±0,05 innenfor støyen» er ikke beregnet (#2281 c) | **ikke rettet** | JURY_SPORSMAL:7. KI-et ±0,12 (BEGRENSNINGER:7) sier egentlig mer |
| 18 | `<!-- tallvakt: ignorer -->` synes i rå markdown (#2281 a) | ikke rettet (med vilje) | JURY:30, 36, 59. Merkelappene trengs for at tallvakta skal holde seg grønn |
| 19 | Ordliste for sak, smed/dommer, miks h2, golv | rettet | kilder/LESMEG.md. «golv» er stavet likt overalt (JURY:21, ERLIG:29), og «gulv» gir 0 treff |
| 20 | Sti i kommando `arbeid/kandidater/smed2_c1_mot` (#2281 a) | ikke rettet (må stå) | README:52. Det er en ekte sti |

## Ikke rettet, rangert etter juryvekt
Metode og ærlig evaluering teller 60 %, så de punktene står først.
1. **Pkt. 17, ±0,05 (metode/ærlighet):** Bytt «±0,05 innenfor støyen» i JURY_SPORSMAL:7 med «95 % KI er [0,36; 0,59], så 0,5 ligger inne i intervallet» (kilde: BEGRENSNINGER:7).
2. **Pkt. 8, pekere ut av pakka (etterprøvbarhet):** Kopier `c1_offline_kaldstart.md` og `c1_beslutning_nyeste_historikk.md` inn i kilder/, og bytt stiene i JURY_SPORSMAL:54, JURY:77 og NESTE_VERSJON:21 til `kilder/<fil>`.
3. **Pkt. 16, 12 s uten kilde (ærlig tall):** Bytt «ca. 12 s» i README:52 med «4,8 s for agenten alene (kilder/c1_kjoretid.md)», eller fjern tallet.
4. **Pkt. 15, 29 s mot 52 s (robusthet):** Legg til denne setningen etter README:39: «Kjøretiden fra kald start er 29–52 s, avhengig av om uv-cachen er varm (BEGRENSNINGER:38).»
5. **Pkt. 7, #-numre er tilbake (lesbarhet):** Kjør `arbeid/oppgave_2281/mekanisk.py` på nytt («#NNNN» → «sak NNNN», «smed #N»/«dommer #N» → «kontrollagenten»), i hvert fall på JURY.md, JURY_SPORSMAL.md, NESTE_VERSJON.md, demo.sh og demo_utskrift.txt. Etterpå må sluttsjekk.sh kjøres, slik at tallvakta fortsatt er grønn.

Ingen av punktene rører modell, tall eller prediksjoner. Alle er ordlydsendringer som #1975 kan ta etter frysen.
