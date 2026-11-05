# Case 1: tekstavtrykket som steg 7 i sluttsjekk.sh (smed4 #2404)

- smed la inn steg 7 i commit 4164bb5 (#2392) og droppet oppgaven. Jeg forbedret det i egen commit:
  - steget kjører via `kjor()` med egen logg `7_tekstavtrykk.txt`, som de andre stegene.
  - `TEKSTAVTRYKK: ...`-oppsummeringen står nå i siste linje (`SLUTTSJEKK GRØNN: ...; TEKSTAVTRYKK: ...`), så dommeren ser endrede tekster uten å lese loggen.
  - Krasjer tekstavtrykk.py (alt utenom utgang 0/3), står det `ADVARSEL tekstavtrykk.py feilet` i stedet for at feilen forsvinner stille.
  - Steget gir fortsatt aldri rødt (arkitekt #2384: tekstene kan endres med vilje etter kl. 16, #1975).
- Test: `bash -n` grønn. Steg 7 og sluttlinja er kjørt i speilkopien /tmp/c1_avtrykk_smed4 (kopi av leveranse/ og eget avtrykk, ingen frosne filer rørt):
  - uendret: `TEKSTAVTRYKK: uendret (64 filer)`, utgang 0
  - bevisst endret (JURY.md + slettet NESTE_VERSJON.md): ENDRET/BORTE-linjer og `2 endret ... JURY.md, NESTE_VERSJON.md` i sluttlinja, utgang 0
  - ødelagt avtrykk-json: tekstavtrykk.py krasjer med utgang 1, og det vises som ADVARSEL, utgang 0
- Ikke gjort: en hel sluttsjekk. Frysvakta (`--krev`) er rød før frysen kl. 16. Den hele kjøringen er #2407.
- Merk: på den ekte maskinen er avtrykket ikke tatt ennå (tas 16.03). Før det viser steget `ikke tatt ennå`.
