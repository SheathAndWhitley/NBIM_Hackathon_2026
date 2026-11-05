# Case 1 (#2715): tekststopp-zipen tørrkjørt i kald kopi kl. 18:11, GRØNN på 158 s

smed2, 05.11. Kjørte sluttsjekk-kjeden slik #2549 skal kjøre den kl. 19, med HEAD 09f6a18, men med to forskjeller: kald kopi i `/tmp/c1_tts_2715`, og zipen lagt i `/tmp`. Steg 8 (`lagre_gronn.sh`) er hoppet over, så `state/levering/c1_gronn/` og SISTE_GRONNE ikke ble rørt. Skriptet er `arbeid/oppgave_2715/sluttsjekk_torr.sh`. Det skiller seg fra originalen på to linjer: fast LAND, og steg 8 er tatt bort. Leveransen er ikke endret. Kopien, loggmappa og zipen (til sammen ca. 1 GB) er slettet etterpå. Steglogger ligger i `arbeid/oppgave_2715/*.txt`.

| | resultat |
|---|---|
| `git status --short arbeid/hack` før bygging | **tom** (hull 2 er OK nå) |
| tid fra start til grønn | **158 s** (18:10:55–18:13:33). Kaldstart 41 s (uv sync 1 s + kjøring 40 s), resten er tallvakt, pakk og ziptest |
| frysvakt | GRØNN, 21 filer like som ved frys 17:18:18 |
| tallvakt | **0 avvik** (22 filer, 173 påstander), både i kald kopi og i ziptesten |
| hovedtall | kald kopi 0.512000 = kv hack_levert 0.512000 |
| zip | 150 filer, 1,0 MB, SHA256 `017a3f26…95ae4` (tørrkjøring, ikke lagret) |
| zip-score | **ZIPTEST GRØNN 0.512000**, TP 32 FP 35 FN 26 TN 1446 STEMMER, ny prediksjonsfil = frossen (d02cf884…) |
| siste linje | SLUTTSJEKK GRØNN (frysvakt, kaldstart, tallvakt, tallsjekk, hovedtall, jury-zip, ziptest) |

## Stopp og merknader
- Ingen stopp. «ADVARSEL lagre_gronn.sh feilet» i GRØNN-linja kommer av at jeg hoppet over steg 8 med vilje. Kl. 19 skal det stå «lagret …» der.
- Info fra pakk_jury: 9 tekstfiler i zipen nevner `~`: README.md, JURY_README.md, to TREFFSIKKERHET.md, kilder/dommer_*.md, kilder/usette.py, menneske_tabell.py og c1_tallvakt.py. Kjøreveien leser dem ikke, og testen er grønn. Juryen kan se stiene, men det er for sent å rette dette før tekststopp.
- Tekstavtrykk: 57 filer er endret siden 16:03. Det er ventet etter tekstrettingene, og bare info.
- Disk: 7,3 GB ledig etter rydding. En runde bruker ca. 1 GB midlertidig.
- Til #2549 kl. 19: kjør `bash arbeid/hack/levering/sluttsjekk.sh` som planlagt. Regn med ca. 3 min fra start til grønn. Sjekk først at `git status --short arbeid/hack` er tom.
