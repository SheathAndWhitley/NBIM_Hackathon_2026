# Dom: sluttsjekk.sh steg 3 (tallvakt) og steg 7 (tekstavtrykk), commit 1b92b3e, 4164bb5, 9bf3b25 (#2413, dommer 05.11 15:40)

**GODKJENT.** Ingen feil funnet. `bash -n` grønn. Fila er uendret siden 9bf3b25 (git status ren).

## Hva jeg testet (eget harness, linjene kopiert ordrett fra sluttsjekk.sh, falsk fremmed.sh og falsk tallvakt)
Steg 3 (linje 34–48), skal bli rød i alle feilfall:
| fall | resultat |
|---|---|
| fremmed.sh utgang 1 med TALLVAKT RØD + tallvakt utgang 1 med AVVIK | RØD «TALLVAKT RØD (utgang 1): 1 tall …», AVVIK-linja vist, utgang 4 |
| fremmed.sh grønn + tallvakt utgang 2 (krasj, ingen AVVIK) | RØD (utgang 2) |
| fremmed.sh TALLVAKT RØD men steg 3 grønn | RØD «uforklart» (linje 48) |
| fremmed.sh utgang 1 uten TALLVAKT RØD (f.eks. FRYSVAKT RØD) | RØD i steg 2 (linje 37) |
| kald kopi mangler .venv/bin/python eller ut/pred_maaler.csv | RØD (linje 40) |
| alt grønt | passerer til 3b |
Smed4s egen røde kjøring på ekte skript (`arbeid/oppgave_2397/c1_tallvakt_sluttsjekk_rod.log`, bevisst 0,512 i speilkopi) stemmer med dette.

Steg 7 (linje 74–80), skal aldri bli rød og aldri skjule en rød linje:
| fall | resultat |
|---|---|
| utgang 0 uendret / utgang 3 endret | GRØNN, oppsummeringen står i sluttlinja, utgang 0 |
| utgang 2, utgang 1, skript mangler, ingen TEKSTAVTRYKK-linje | GRØNN med «ADVARSEL …» eller «TEKSTAVTRYKK: mangler», utgang 0 |
| skriptet printer selv «SLUTTSJEKK RØD: …» | vises bare innrykket i tail -4; siste linje er fortsatt SLUTTSJEKK GRØNN |
Steg 7 kjører etter alle `rod`-kallene (rod gjør `exit 4`), så det kan ikke overstyre en rød. Ingen `set -e`, så utgang ≠ 0 fra kjor() stopper ingenting. tekstavtrykk.py `sjekk` leser bare (sha256 av leveranse/), skriver ingenting, ingen nett.

## Merknader (ikke feil, ingen endring kreves nå)
- Linje 46: krasjer tallvakta (utgang 2) står det «0 tall i pakka avviker» i den røde meldinga. Fortsatt rød, bare litt villedende tekst.
- Linje 44: tallvakta er grønn med «0 påstander» hvis ingen .md havner i kopien. fremmed.sh linje 31 kopierer dem, og steg 3b/4/6 sjekker hovedtallet uansett.
- Til #1972 (meg, 19.30): én full kjøring legger ca. 3,2 GB i `/tmp/c1_sluttsjekk_logg.*` (bygg/stage/ziptest med .venv). Slett loggmappa etterpå. Avtrykket (state/c1_tekstavtrykk.json) finnes ikke før 16.03; steg 7 sier da «ikke tatt ennå», det er riktig.
