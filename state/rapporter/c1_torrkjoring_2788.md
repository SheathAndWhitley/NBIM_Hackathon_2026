# Case 1 #2788: tørrkjørt sluttsjekk og ukommitterte verktøy (18:45-18:50)

**Commit:** `e1438a9`: state/c1_frys.json. Endringen var dommer2 #2738 sin godkjenning av ny hash for c1_real.py (bare feilhåndtering, smed3 #2724), og frystid satt tilbake til 17:18:18. Ferdig og testet: frysvakt GRØNN, 21 filer. Jeg måtte bruke `git add -f`, fordi state/ står i .gitignore selv om fila spores.
**github_synk.sh:** smed2 hadde alt committet den i `9beee0b` (#2762) kl. 18:45. `bash -n` ok.

**Sluttsjekk på HEAD e1438a9 (tørrkjøring, steg 8 lagring byttet ut i en kopi i /tmp, ingen ny SISTE_GRONNE): GRØNN.**
Steg 1-6 er grønne. HOVEDTALL F1 MOT 0.512000 = kv hack_levert = zipen. TP 32, FP 35, FN 26, TN 1446, og prediksjonene er sha-like med den frosne fila. Tidsbruk 113 s.
Tekstavtrykket (bare info): 70 filer endret siden avtrykket 16:03.

**Første kjøring ble RØD** av en annen grunn: disken var full, med bare 118 MB ledig. Steg 2 (kaldstart) stoppet med `cp: ... No space left on device`.
Jeg slettet 37 sluttsjekk-logger (`/tmp/c1_sluttsjekk_logg.*`) fra før kl. 17:00 som ingen prosess hadde åpne. Logger fra etter 17:00 og UVTc (som er åpen) står. Etterpå var 22 GB ledig.
Ikke rørt, men store: `/private/tmp/ren_head_2514` (27 GB, 16:29) og `/private/tmp/staar_ovelse_2631` (15 GB, 17:18). Eierne bør rydde dem. Hver sluttsjekk-kjøring legger igjen ca. 3,2 GB i /tmp, så de neste kjøringene kl. 19 og 19:30 bør rydde etter seg.

svar.csv i oppgave_1823 er ikke rørt (dommer2 dømmer den). Andre ukommitterte filer som ikke hører til Case 1-verktøyene (TILSTAND-filer, rapporter) er ikke rørt.
