# ntl_start.sh har nå trinn 4 (frys) og 5 (tallmal) (#2848)

Nye valg: `--frys <navn>`, `--tall tall.json` (kan gjentas) og `--mal MAL.md.mal`.
- **Trinn 4:** `ntl_frys.py sjekk --navn <navn>`. Er en fil endret eller mangler den, eller er navnet ikke frosset: RØD, utgang 4. Uten `--frys` vises `status` med teksten "ikke klar til innsending", og trinnet er ikke rødt.
- **Trinn 5:** med `--mal` kjøres `tallmal.py sjekk` og deretter `render` med `--tall`. Et tall skrevet for hånd eller en nøkkel som mangler gir RØD, utgang 5. Med bare `--tall` skrives hvert tall ut med kilde og måler-sha. `--mal` uten `--tall` gir utgang 9.
- Valgene er frivillige, så de gamle kommandoene (#2561/#2562/#2837) virker uendret.

Kommando ved innsending: legg til `--frys <innsending> --tall <tall.json> [--mal <mal>]` på kommandoen i ntl_c_torrkjoring.md.

## Prøver (tmp-repo, `env -i` ren terminal)
- `bash -n` er grønt. Hele løpet med ekte frys og `s104` fra `ut_s104.txt:13` gir 0,5408 med fotnote og ALT GRØNT, utgang 0.
- Frys som mangler gir utgang 4. Malen med `0,54` gir utgang 5. Ukjent nøkkel gir utgang 5. Mal uten tall gir utgang 9. Bare `--tall` og ingen valg gir begge utgang 0.
- Låsene ntl_A/B/C og b_ids, b_tekst_sha1, b_utvalg og b_meta har samme sha256 før og etter (`arbeid/oppgave_2848/for.sha`). Testfilene i state/ntl_frys og state/ntl_port er ryddet bort. Ingen Case 1-filer er rørt.
