# Case 1: dekker kravresponsen alle krav i casen? (#2663, repo4)

Kilder for kravene: `CASE/…startpakke_ut/startpakke/FinTech_Hackathon_Caser_H2026.pdf.pakk_ut.txt` (C), `case1_stemmegivning/README.md` (S), `Regler_og_bedommingskriterier.pdf.pakk_ut.txt` (R). Sjekket mot `arbeid/hack/c1/leveranse/kravrespons.md` (KR, 10 linjer, 349 ord) og README/JURY i samme mappe. Bare lest, ingenting endret.

**Kort sagt: 17 krav OK, 5 mangler.** To av dem er tallfeil i selve kravresponsen og bør rettes før tekststopp kl. 19.

| # | Krav (kilde) | Svar (fil:linje) | repo4-tall? | Status |
|---|---|---|---|---|
| 1 | Agent leser sakslisten og foreslår FOR/MOT/AVSTÅ (C:11) | KR:4 (markerer MOT); AVSTÅ bare i README:17 og JURY:29 | ja | **MANGLER** (se M3) |
| 2 | Sitere avgjørende retningslinje (C:13, S:51) | KR:4, KR:10 (15 av 20); README:68, JURY:80 | – | OK |
| 3 | Konfidens og ruting til menneske (C:14, S:53) | KR:4 (164 av 1 578); JURY:6, JURY:78 | ja | OK |
| 4 | Evaluer mot NBIMs faktiske stemmer (C:15) | KR:7 (13 757 saker, 2019–2026); README:64 | – | OK |
| 5 | Baseline oppgitt og slått (S:49, R:44) | KR:4 («følg styret» 0), KR:7 (96,2 %, b2 0,365) | ja | OK |
| 6 | Presisjon og recall på MOT, ikke accuracy (C:26, S:50) | KR:4 (P 0,48, R 0,55, 32 av 58) | ja, men FP 35 står ikke | OK (se M5) |
| 7 | Motstandstest: rapporter svaret (S:55) | KR:7 peker bare til JURY.md; svaret står i JURY:81, JURY_SPORSMAL:43, ERLIG:47 | – | **MANGLER** (se M4) |
| 8 | Praksis mot policy (S:39) | KR:7 peker til JURY.md; JURY:64–66 (81 av 82) | – | OK |
| 9 | Tidssplitt, ikke tilfeldig (S:61, R:55) | KR:7; JURY:4, JURY:77 | ja | OK, men se M2 |
| 10 | Kategori-lekkasje sjekket (S:63) | ikke i KR; README:77 (managementRecommendation), JURY_SPORSMAL:23 | – | OK i pakken, ikke i KR (lav prioritet) |
| 11 | Klasseubalanse (S:65) | KR:7 (96,2 % uten én MOT) | ja | OK |
| 12 | Hvilken beslutning løsningen støtter (R:23) | KR:4 («hva som bør leses først») | – | OK |
| 13 | Fasit, målvariabel, metrikk og hvorfor (R:25) | KR:7 | ja | OK |
| 14 | Hva vi ville trengt: data, tid, tilgang (R:27) | KR:10 (stemmedatabase med begrunnelser) | ja | OK, men se M1 |
| 15 | KR maks 1 side, 3–5 setninger per overskrift (R:14, R:21) | KR: 3 overskrifter med 4, 6 og 5 setninger | – | OK (malen viser 3 overskrifter, ikke 5). «Hvordan vi verifiserte» har 6 setninger, 1 over taket: M3 og M4 må flettes inn i setninger som står der fra før, ikke legges til |
| 16 | README med ett kall som reproduserer (R:16) | KR:7 `sh KJOR.sh`; README:10, README:36 | ja (README:52 TP32 FP35 FN26) | OK, men se M5 |
| 17 | Demo på 5 min, helst kjørende (R:13); MVP-steg 5 «lim inn saksliste» (C:29) | `leveranse/demo.sh`, demo_utskrift.txt (#2660 MANUS OK) | ja | OK |
| 18 | Kilder med URL i README (R:59) | README:64–69 | – | OK |
| 19 | AI-verktøy oppgitt (R:61) | README:75–79 | – | OK |
| 20 | Ekstern kode kreditert (R:65) | README:72 | – | OK |
| 21 | Ingen irreversible handlinger (R:57) | KR:4 («stemmer ikke selv»), README:61 | – | OK |
| 22 | Juryspørsmål 1–3 (R:70–72) | JURY:26, JURY:32, JURY:52 | ja | OK |

## Mangler, med forslag (prioritert)

**M1. KR:10 sier «0,512 ligger under målet vårt på 0,5». Det er feil: 0,512 er over 0,5.** Det er den første tallsetningen i siste avsnitt, og en jurymann ser feilen med en gang. Forslag: «Med 58 MOT i test er intervallet bredt: 0,512 er like over målet vårt på 0,5, men intervallet dekker godt under.» (Samme ordlyd som JURY:5.)

**M2. KR:7 har 95 %-intervall [0,36; 0,59]. Overalt ellers for repo4 står [0,40; 0,62]** (README:8, JURY:5, JURY:16, JURY_SPORSMAL:15). [0,36; 0,59] finnes ikke i noen annen leveransefil. Det er trolig det eldre frosne intervallet. Samme setning («Modell og grense er valgt på 2025 og kjørt én gang på 2026») er dessuten bare sann for den frosne modellen. Repo4 ble funnet på 2026 (JURY_SPORSMAL:87, :92). Forslag: «… med 95 %-intervall [0,40; 0,62]. Repo4 ble funnet etter å ha sett 2026, så 2026 er ikke et friskt år for den; byttet bygger på 2024 og 2025.» Plassen tas ved å korte setningen om byttedommen.

**M3. AVSTÅ er ikke nevnt i KR, selv om casen ber om FOR/MOT/AVSTÅ (C:11).** Forslag (KR:4 eller KR:7): «AVSTÅ er for sjelden (5 av 1 539 i test) til å modellere; den regnes som avvik i et sidetall (F1 0,529 på alle 66 avvik).» Tall fra README:17.

**M4. Motstandstesten står i KR bare som en peker («står i JURY.md»).** Casen sier «rapporter svaret uansett» (S:55). Forslag (KR:7): «Motstandstest: alle 16 innlagte instrukser fanges og rutes (verste angrep F1 0,457), men 6 av 16 instrukser av bare tittelord slipper gjennom (JURY_SPORSMAL:43).» Sjekk tallene mot `kilder/c1_motstand_etter_frys.md` før innsetting.

**M5 (lav). Kommandoen og FP.** `sh KJOR.sh` (KR:7) virker bare i jury-zipen. I repoet heter fila `kjor.sh` (README:19, :36), og stor/liten bokstav betyr noe på Linux. Forslag: «… med `sh KJOR.sh` i jury-zipen (i repoet `bash arbeid/hack/c1/leveranse/kjor.sh`)». Kravet om repo4-tallene: KR har 32 av 58, P 0,48 og R 0,55, men ikke «35 falske flagg». Den kan legges til i KR:4 hvis det er plass.

## Utenfor KR, sett underveis
- JURY_SPORSMAL:6 har overskriften «Målet var 0,5. Hvorfor leverer dere bare 0,512?», og JURY_SPORSMAL:81 sier «hovedtallet 0,476». Begge er rester fra den frosne versjonen. Dette hører til #2665/#2671 (smed4).
