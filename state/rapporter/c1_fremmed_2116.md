# Case 1 #2116: fremmed.sh har retningslinje-filene, kald kopi kjører (12:52)

- `arbeid/hack/levering/fremmed.sh:21` har nå både `arbeid/hack/levering/retningslinje_oppslag.py` og
  `arbeid/hack/c1/retningslinjer/punkter.jsonl` i kopier-lista. Linja var allerede lagt inn da jeg åpnet fila.
  Jeg endret ingenting. Fila ligger i `arbeid/`, som er gitignored, så det finnes ingen commit.
- Bevis: `sh arbeid/hack/levering/fremmed.sh /tmp/fremmed_2116` kjørte uten ImportError
  (uv sync 1 s, kjøring 41 s). Begge filene ligger i kopien.
- Tall fra kopien (måler v2, test): F1 avvik 0,4818 (TP 33, FP 38, FN 33), PR-AUC 0,5245.
  Med ruting gikk 183 saker til et menneske (11,9 %).
- Retningslinjene brukes i kopien: av 74 predikerte MOT siterer alle et NBIM GVG-punkt
  (de vanligste er 1.1.2, 3.3.2, 1.2.1 og 5.2.4). FOR-sakene får NBIM 0.0.3. Det er bevisst (c1_real.py:212).
- Neste: #2123 (dommer2) kan bekrefte fra sin egen kalde kopi.
