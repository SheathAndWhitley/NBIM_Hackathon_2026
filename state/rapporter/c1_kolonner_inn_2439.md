# Case 1: kolonneforklaring og to rettinger ført inn i jurypakka (#2439, smed3, 05.11)

Bare ordlyd, ingen modell- eller prediksjonsendring. Mappa juryen får er `arbeid/hack/levering/` (pakk_jury.sh kopierer
`levering/JURY_README.md` til `README.md` i zipen og alle `levering/*.md` via fremmed.sh). `c1/leveranse/` følger også med, men
rettingene hørte hjemme i `levering/`.

## Gjort
- `levering/JURY_README.md` linje 3: «anbefaler FOR, MOT eller AVSTÅ» → «anbefaler FOR eller MOT … (aldri AVSTÅ, se BEGRENSNINGER.md pkt. 6)».
- `levering/JURY_README.md`: nytt avsnitt «Kolonnene i ut/agent.csv» (tabell med alle 19 kolonner) rett etter linja «Agentens svar ligger i ut/».
  Tabellen er den fra `c1_kolonner_forklart.md`; grensene 0,919 (rå) og 0,191 (kalibrert) er sjekket mot KJORING.txt linje 3.
- `levering/BESLUTNINGSSTOTTE.md` «Slik leser du p_mot»: merknad først i avsnittet om at 0,919 er `raa_score`, mens `p_mot` er kalibrert med flagg ved 0,191.
- Ikke rørt: demo.sh, JURY.md, JURY_SPORSMAL.md (arkitekt #2435). Merknaden for JURY_SPORSMAL spm. 8 står som gjenstående punkt for #1975 nederst i `c1_kolonner_forklart.md`.

## Verifisert
- Tallvakta på de to filene: 21 påstander stemmer, 0 avvik.
- `sluttsjekk.sh` med prøvefrys (C1_FRYS i /tmp, slettet etterpå): SLUTTSJEKK GRØNN, HOVEDTALL F1 MOT 0.476190 = zipen, 177 s.
  Zipen inneholder den nye tabellen og merknaden (grep i README.md og BESLUTNINGSSTOTTE.md i zipen).
- Første sluttsjekk-kjøring ga «syntax error line 72» etter grønt steg 6: arkitekt committet ny sluttsjekk.sh (#2443, b42f7f3)
  kl. 15:46 mens skriptet kjørte. Ikke en feil i pakka; kjøringen ble gjentatt og var grønn.

## Merk
`arbeid/` er gitignored; JURY_README.md er sporet fra før. Endringen min havnet i commit acaaff7 (#2442, 15:48, en annen agent tok fila med), så den er i HEAD. BESLUTNINGSSTOTTE.md er ikke sporet,
endringen ligger bare på disk (som resten av levering/*.md).
