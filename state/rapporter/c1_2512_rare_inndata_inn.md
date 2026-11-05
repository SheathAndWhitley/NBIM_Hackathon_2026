# Case 1 (#2512): de fem dømte svakhetene fra rare-inndata-testen er inn i BEGRENSNINGER og NESTE_VERSJON

- Grunnlag: `c1_rare_inndata.md` (smed4, #2499) og dommen `dom_2499_rare_inndata.md` (#2507). Dommen godkjente fem svakheter (de fire i oppgaven pluss «uleste rader får anbefaling FOR», `c1_real.py:210`). Alle fem er tatt inn.
- `leveranse/BEGRENSNINGER.md` nytt pkt. 9: tom fil gir utgang 0, ingen samlet kolonne-/skilletegnfeil, falsk injeksjonsgrunn på «AI» (`injeksjon_hoflig.py:21`), P(MOT) varierer maks 0,007 mellom batcher (grense 0,91885 mot 0,91896), uleste rader får anbefaling FOR. Med «Gjør»-linje.
- `leveranse/NESTE_VERSJON.md` nytt avsnitt: svakhet 3 og 5 som dommen ba om, pluss filsjekken fra rapporten (0 byte / manglende kolonner gir feil og utgang ≠ 0). Merket «ikke hovedtall, endrer ingen stemme».
- Kildene er kopiert til `leveranse/kilder/` (interne stier skrevet om til `<arbeidsmappe>/...`) med linje i `kilder/LESMEG.md`, så ingen peker går ut av zipen.
- Kontroll: `pakk_jury.sh` fra kald start utgang 0, HOVEDTALL F1 MOT 0.476190, TALLVAKT GRØNN (18 filer, 169 påstander, 0 avvik), «sha256 i pakka = frysfila», 131 filer. `frys_fasit_1600.sha256` regenerert (bare de 5 filene endret), `frys_diff.sh` på zipen: FRYS LIK, 0 avvik. Ingen modell eller frossen fil rørt.
