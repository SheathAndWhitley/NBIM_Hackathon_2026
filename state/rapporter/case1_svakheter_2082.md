# Case 1: «Kjente svakheter og hva vi forkastet» er skrevet til juryen (speider, #2082)

Fil: `arbeid/hack/c1/SVAKHETER.md` (norsk + engelsk). Fem punkter, alle med kilde (rapport eller forsøks-id).

Nytt i forhold til kildene:
- **Test-logg talt fra forsøkstabellen:** test 2026 (real_votes) er kjørt for 14 ulike varianter mellom 11:47 og 12:16
  (logreg-trapp 5, #2044-familien 5, smed 1, smed3 3). Hovedmodellens prediksjoner er i tillegg reprodusert byte-likt
  3 ganger (#1046, #1064, #1066). Beste test-tall (t4e 0,529) velges ikke, fordi val rangerer den sist.
- **Grensa til #2044 (sett i ettertid på test, ikke brukt til valg):** F1 er 0,47–0,54 for 35–100 flagg (valgt 71, 0,482).
  Men p er presset sammen: grense 0,92 → 0,83 gir 176 flagg og F1 0,35. Kalibrering som driver fra år til år er en reell risiko.
  Skript: `arbeid/oppgave_2082/grense.py`.

Til #1975 etter frys: bytt hovedtallet i toppen og i avsnitt 4 hvis dommeren (#2080) fryser en annen modell enn #2044,
og legg til test-kjøringer som kommer etter 12:16.
