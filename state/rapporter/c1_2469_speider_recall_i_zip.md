# Case 1 (#2469): speider_2399_recall_budsjett.md ligger nå i jury-zipen

Dom #2455 fant at `NESTE_VERSJON.md:58` bygger tre tall (F1 0,517 ved k=50, 30 av 66 i topp 50, presisjon 0,60)
på `landsbyrapport:speider_2399_recall_budsjett.md`, som ikke var i zipen.

Gjort (kl. 16.04–16.12):
- `arbeid/hack/levering/pakk_jury.sh`: `state/rapporter/speider_2399_recall_budsjett.md` lagt i kopier-linja for
  bøtte b, ved siden av c1_feil_per_gruppe.md. Fila er 1,6 kB, 0 treff på ~.
- `NESTE_VERSJON.md:58`: pekeren er nå `state/rapporter/speider_2399_recall_budsjett.md:16-23` (tabellrad k=50 på
  linje 16, forbeholdet på linje 23). Første forsøk `:16,23` ble lest av tallsjekken som desimaltallet 16,23
  og ga RØD; linjeområde med bindestrek går gjennom.
- `frys_fasit_1600.sha256` regenerert: 117 filer (114 etter min fil; tre til kom fra #2475 og nbim-rapportene
  som andre la inn samtidig).

Målt:
- sluttsjekk.sh: GRØNN. Frysvakt 17 filer like (frys 16:00:01), kaldstart og tallvakt grønn, tallsjekk 0 IKKE FUNNET,
  ziptest HOVEDTALL F1 MOT 0.476190, zip 892K. Zipen fra kl. 16.07 inneholder speider-fila (1622 B).
- frys_diff --kilde: FRYS LIK, 0 avvik. frys_diff mot zipen fra 16.07: 8 avvik, alle fra andres redigeringer
  etter at zipen ble pakket (README, JURY_SPORSMAL, LESMEG, JURYSVAR, JURY_README, nbim-kildene, #2475), ikke fra denne oppgaven.

Commit: bare mine hunker i pakk_jury.sh og NESTE_VERSJON.md pluss fasiten. Resten av de uncommittede endringene i
de to filene (tiltak 4 / #2475) hører til andre og ligger urørt i arbeidstreet.
