# Case 1: pakken kjører fra en ren kopi under env -i (#2016)

Kommando: `sh arbeid/hack/levering/fremmed.sh /tmp/fremmed` (README: arbeid/hack/levering/README.md).

- Kopien er 159 MB, bare filene agenten leser (liste i README). Eget uv-prosjekt med
  modellens `uv.lock`, `uv sync --frozen`. Kjøring under `env -i`, PATH bare .venv/bin:/usr/bin:/bin.
- Akseptkrav oppfylt: F1 0,474286 (tp 83 fp 138 fn 46), 119 saker (9,6 %) til menneske, derav 18 avvik.
- `pred_maaler.csv` fra kopien er byte-identisk med `levering/kjor_agent_pred_maaler.csv`.
- Tid målt (date): 42 s totalt, uv sync 0 s med varm cache. Med tom uv-cache tok sync 9,6 s
  (234 MB .venv). KJORING.txt sier 12 s fordi den teller fra etter import av lightgbm og
  før måleren; resten er oppstart i ny venv.
- Ærlig forbehold: samme maskin, så uv-styrt Python 3.13 fantes alt; en helt ny maskin må laste
  den ned (én gang, uv gjør det selv). Ingen stier utenfor kopien brukes: alt går via
  relative stier fra kjor_agent.py.
