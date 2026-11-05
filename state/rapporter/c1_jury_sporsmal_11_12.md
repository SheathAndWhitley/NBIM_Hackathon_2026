# Case 1: to nye jury-spørsmål (11 og 12) etter neste-steg og offline-kjøringen (#2425, speider, 05.11)

Lagt inn i `arbeid/hack/c1/leveranse/JURY_SPORSMAL.md` (nå tolv spørsmål). Ingen nye tall; hvert tall har kildefil i svaret.

- **11. «Dere har sett 0,529 på test. Hva betyr bootstrap ±0,1 for 0,476 mot huskeregelens 0,243?»** 0,529 (t4e) er målt med eldre måler v2 (frossen agent 0,482 der), tapte på val 0,468 mot 0,522, og det ville vært valg på test. ±0,1 betyr at vi bare påstår forskjeller der KI for differansen er over null: mot huskeregelen +0,23 [+0,12; +0,34] (robust), mot b2 +0,11 [0,01; 0,22] (så vidt). Kilder: `c1_neste_steg.md`, `c1_valgt_bort.md`, `c1_bootstrap_f1.md`, `c1_huskeregel.md:3`, `leveranse/JURY.md:23`.
- **12. «Kjører agenten uten nett, og laster den ned noe?»** Ja, grønt med nett sperret (sandbox-exec, curl gir utgang 7), 0,476190 uendret, dommeren fikk bit-identiske filer; ingen torch/transformers/requests. Forbehold: `uv sync` trenger nett én gang uten uv-cache; #2417 prøver dette nå. Kilde: `c1_offline_kaldstart.md`.

**Tallvakta:** GRØNN (18 filer, 168 påstander, 0 avvik, utgang 0). Linjene med 0,529/0,482/0,243/0,23 har `tallvakt: ignorer`, slik som spørsmål 4, fordi de ikke er hovedtallet.
**Til #1975 etter frysen:** spørsmål 12 må oppdateres med utfallet av #2417 (tom uv-cache).
