# Case 1: de tre største uklarhetene fra jurylesningen er rettet (oppgave 2287)

Grunnlag: `state/rapporter/c1_jurylesning.md` (2281). Bare tekst og pekere er endret. Alle tall har kilde i en måler eller en telling, og ingen tall er endret. Diff: `arbeid/oppgave_2287/tekst.diff`, kopi før retting: `arbeid/oppgave_2287/for/`. Tallvakta (`c1_tallvakt.py` på den kalde kjøringen /tmp/c1_demo_2281) gir 162 påstander, 0 avvik, OK.

1. **Val 2025 som 0,520 og 0,522:** dette er to mål, ikke en avrundingsfeil. 0,520 er F1 på MOT, og 0,5217 er F1 på avvik. Begge er målt fra kald start med måler v3 (`c1_val_kaldstart.md`, 2282), og KI [0,41; 0,63] kommer fra `c1_feil_stabilitet.md`. Endret: ERLIG § 1-tekst, § 5 og verifiseringsavsnittet, JURY:28, BEGR:7 og JURY_SPORSMAL:8. JURY_SPORSMAL:8 sa før at tallet «bare står i loggen».
2. **Sitatpåstander uten kilde i pakka** (15/4/1, 18 av 18, 8 av 20, 86 %): kildene er kopiert inn i `kilder/` (`c1_sitat_verifisert.md`, `c1_sitatkilder.md`, `c1_retningslinje_sitat.md`, med #-numre gjort om til «sak NNNN»). «Ikke med i pakka» er byttet mot pekere i JURY:36, BEGR:28 og ERLIG:68.
3. **11 785 treningssaker** (13 757 − 1 578 = 12 179, så 394 rader manglet forklaring): de 394 radene før 2026 mangler fasit (`against_board` er tom), og det er 0 injeksjonsrader. Filteret er det samme som i `train.py:28`. Tellingen ligger i `kilder/tell_trening.py` + `.txt`, og ERLIG:3 og JURY:32 peker dit.

Ikke gjort: kjøretidene (29/31–52/12 s) er lagt til smed #2288 (svartid i README). README er ikke rørt. Endringene er ikke committet, fordi andre agenter skriver i de samme filene i dag. #1975 (oppdatering etter frys) bør beholde pekerne over.
