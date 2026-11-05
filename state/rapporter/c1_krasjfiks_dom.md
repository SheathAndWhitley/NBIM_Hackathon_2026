# Case 1: dom over smed3s krasjfiks (#2724), dommer2 #2739

**GODKJENT.** Kald kopi (`fremmed.sh /tmp/kald2739`, 18:30): F1 MOT 0,512, tallvakt 0 avvik, agent.csv sha256 24ee6b18… byte-lik smed3s før/etter-tall; alle 14 inn-filer i `arbeid/oppgave_2724/inn/` (13 pluss 01b) kjørt fra kopien under `env -i`, exit 0 og 0 tracebacks, 12_binaer gir varsel og to rader til menneske, 13_latin1 gir varsel og «Blåøyd Fjørfe ASA» riktig i utfila.

Grunnlag:
- Diff e0730dc: bare `try/except UnicodeDecodeError` rundt lesingen av inn-fila i `c1_real.py` (linje 149), latin-1-fallback med varsel, pen `sys.exit` ved `csv.Error`. Ingen modell-, terskel- eller rutingkode berørt.
- Frys: ny hash d9c239a2… for c1_real.py ligger i `state/c1_frys.json` under `godkjent` (dom #2738), frystid står på modellfrysen 17:18:18. Smed3s egen `frys --tving` 18:19:39 uten dommer-ja er ført som prosessbrudd i c1_frysvakt_1818.md, ingen videre følge.

Reproduksjon: `sh arbeid/hack/levering/fremmed.sh /tmp/kald && for f in arbeid/oppgave_2724/inn/*.csv; do /tmp/kald/.venv/bin/python /tmp/kald/arbeid/hack/levering/kjor_agent.py --csv $f --ut /tmp/ut_$(basename $f .csv); done`. Logger og utfiler: `/tmp/rob2739/`.
