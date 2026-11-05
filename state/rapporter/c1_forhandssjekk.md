# Case 1: forhåndssjekk av leveransepakken før kald start kl. 13 (dommer #2113)

Statisk gjennomgang av `arbeid/hack/levering` 12:37–12:50. Pipelinen er ikke kjørt, det gjøres i #1952.

## Feil funnet
1. **BLOKKER: kald start kommer til å krasje.** `c1_real.py:162` importerer `retningslinje_oppslag` (ny 12:36, #2106),
   og den leser `arbeid/hack/c1/retningslinjer/punkter.jsonl`. Ingen av dem står i kopier-lista i `fremmed.sh`.
   `kjor.sh` og `demo.sh` går begge via fremmed.sh. Kopien får derfor ImportError (eller FileNotFoundError).
   -> **#2116 smed2**: legg begge filene inn i kopier-lista før 13:00.
2. **Søppel og fremmede filer i pakken (327 MB):** `demo/.venv` (322 MB), 6 `__pycache__`-mapper,
   `demo/logg/streamlit.out` og `demo_logg.jsonl`, og mappene L3/L3_kald/L4/L4_kald/L5/L5_kald, som er Kaggle-pakker
   (`score: 0.158924 off`), ikke Case 1. SISTE.txt i dem har `~`-stier. -> **#2117 speider**: flytt ut.
3. Liten feil: `kjor_agent.py:49` leser `kandidater/smed2_c1_mot/forklaring.csv`, men fremmed.sh kopierer den ikke.
   Den brukes bare på den gamle N-PX-stien (`--data v3`), og koden hopper stille over den når fila mangler. Det
   rører ikke hovedtallet. Den står med i #2116 som valgfri.

## Sjekket og i orden
- (1) README-kommandoene: `fremmed.sh`, `c1/leveranse/kjor.sh`, `demo.sh` og `kjor_agent.py` finnes.
  Alle 21 stiene i kopier-lista finnes (største: `def14a` 102 MB, `sec` 52 MB).
- (2) Låst miljø: `kandidater/smed2_c1_mot/pyproject.toml` og `uv.lock` (156 KB) kopieres, og `uv sync --frozen` brukes. Demoen har egen `demo/uv.lock`.
- (3) Forbudte kolonner: `oppgave_2044/train.py` har FORBUDT-settet med assert. `c1_real.py:123` avviser inn-saker med fasitfelt.
  `rationale_*` brukes bare til sitat og retningslinjeprior fra historikken, og bare fra **strengt tidligere år**
  (`finn_sitat`: `by >= year` blokkeres; `retningslinje_oppslag.py:81`: `y < year`). `real_test_input.csv` har ingen nbim/rationale-kolonner.
  Det gir ingen lekkasje til prediksjonen.
- (4) Absolutte stier: den kopierte koden har ingen `~`. Unntaket er målerne v2/v3, der fremmed.sh skriver stien om med sed.
  `smed3_utf_sitat/forklar.py` og `nbim_sitat.py` har hardkodede stier, men de kopieres ikke og brukes ikke.

Rutingtall-avviket (228/1578 mot 176/171) er ført i #2111 og er ikke tatt med her.
