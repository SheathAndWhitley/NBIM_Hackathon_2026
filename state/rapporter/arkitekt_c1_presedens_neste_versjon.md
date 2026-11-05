# Case 1: presedensregelen skrevet inn som tiltak 4 i NESTE_VERSJON.md

- Nytt avsnitt «Tiltak 4: presedens først, vår rangering etterpå» i `arbeid/hack/c1/leveranse/NESTE_VERSJON.md`.
  Regelen er presis: samme direktør hvis kjent, ellers samme sakstekst; avvik teller også AVSTÅ.
- Tall (fra dommen, avvik 0): presedens alene 0,515, +0,039 [−0,051; +0,126]; hybrid på vår splitt 0,545,
  +0,069 [+0,007; +0,133]; PR-AUC 0,525 (vår) mot 0,318 / 0,413. Flagg 68 (P 0,441) mot 52 (P 0,577).
  Samme tall som smed2 har i JURYSVAR og JURY_SPORSMAL (der avrundet til 2 desimaler for persistence-KI).
- Kombinasjon: presedensflagg først (bare stemmer før møtedato), vår P(MOT) for resten, terskel valgt på val;
  foreldelse fra tiltak 1 gjelder også presedensflagget. Måles i den rullerende val-en fra tiltak 2.
- Hvorfor ikke bytte etter frys: målt etter at testen var sett (ville vært å velge på test), repoets egen test
  inneholder 2026, bare én rad har KI over null med 58 positive.
- Referanser peker på `kilder/c1_nbim_repo_sammenligning*.md` i pakka. Ingen interne #-numre i den nye teksten.
- Kontroller: tallvakta 18 filer, 0 avvik; frys_fasit_1600.sha256 regenerert (117 filer, bare NESTE_VERSJON endret);
  sluttsjekk GRØNN, hovedtall F1 MOT 0,476190. Ingen modellendring.
