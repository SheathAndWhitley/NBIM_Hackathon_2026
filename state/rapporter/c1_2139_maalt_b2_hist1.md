# Case 1 #2139: regel b2 og «bare år før» er målt på v3-måleren, tallene stemte

- Regel b2 (samme selskap + samme tekst fikk MOT før): F1 MOT **0,364964**, forsøk #1122.
- Frossen #2044 miks `--hist 1` (bare år før): F1 MOT **0,415094**, forsøk #1123.
- Kjørt fra kald kopi (`/tmp/kald_2139`), filene er byte-identiske med #2134. Avvik 0 (krav 0,001). Regel a 0,097363 og b 0,287081 stemte også.
- Måler: de049083d9, `maaler_offisiell_v3.py {sti} test --data real --score mot`, samme som #2123/#2148.
- Detaljer står i `c1_enkle_regler_og_hist1.md`, avsnittet «Verifisert fra kald kopi».
