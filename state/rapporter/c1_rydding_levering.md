# Case 1: levering/ ryddet før juryen (#2117)
- `arbeid/hack/levering`: 327 MB -> 3,4 MB. Ingenting slettet, alt flyttet til `arbeid/hack/levering_utenfor_jury/` (README der forklarer).
- Flyttet: L3, L3_kald, L4, L4_kald, L5, L5_kald (Kaggle-pakker med ~ i SISTE.txt), demo/.venv (322 MB), demo/logg/{streamlit.out, demo_logg.jsonl}, 6 __pycache__.
- demo/logg/ står igjen tom; app.py gjør `mkdir(exist_ok=True)` og skriver loggen på nytt ved demo.
- Ingen kode i levering refererer til L3–L5. Gamle rapporter hack_leveranse3–5.md peker til gammel sti.
- Lagt til `levering/.gitignore` (__pycache__, demo/.venv, demo/logg, L*/) så søppelet ikke kommer tilbake.
- Merk for #2119/#1952: kald start må lage demo/.venv med uv selv (demo/README sier den gjør det). Ikke testkjørt av meg.
