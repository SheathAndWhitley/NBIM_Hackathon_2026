# Case 1: kald-start-skript for dommeren (arkitekt #2060)

**Kommando (fra hvor som helst):** `bash arbeid/hack/c1/kaldstart.sh`. Det tar 40 s. Siste linje er `GRØNN|RØD F1_MOT x REF y AVVIK z`.
Exit 0 betyr grønn. Exit 3 betyr avvik over 0,005 mot tavla. Exit 2 betyr at agenten eller måleren feilet.

## Hva skriptet gjør
1. Lager en tom `mktemp -d /tmp/c1_kald.*` og kopierer bare det agenten trenger, med samme relative tre som `arbeid/`:
   `hack/levering/kjor_agent.py`, `kandidater/smed2_c1_mot` (uten .venv), `hack/varianter/smed3_utf_sitat` (uten ut/, med def14a-data), `hack/c1/*.py`, `data_v3`, `data_v3_val`. Det blir 866 MB og 437 filer. Gamle `pred_*.csv` fjernes fra kopien.
2. Kjører `uv sync --frozen` fra `uv.lock` og lager en ny .venv i kopien (lightgbm 4.7.0, sklearn 1.9.1, pandas 3.1.1).
3. Kjører agenten i kopien på holdout 2026 (1 246 saker). Den gir agent.csv med ruting og sitat, og pred_maaler.csv.
4. Måler med **landsbyens** `arbeid/hack/c1/maaler.py` (sha256 1cae2110b4), ikke med kopien, mot `data_v3/fasit.csv`. F1 på MOT regnes nøyaktig fra tp/fp/fn.
5. Referansen er beste forsøk på tavla med `kjor_agent`/`pred_maaler` (`REF=` overstyrer). Avvik > `TOL=0.005` gir rød melding.
   Tmp-mappa slettes etterpå (`BEHOLD=1` lar den stå).

## Kjøring fra tom mappe (05.11 kl. 12.04, git ef40284)
| | tall |
|---|---|
| tid totalt | 38–45 s (kopi 9 s, uv sync 23 s, agent 13 s) |
| saker / MOT / til menneske | 1 246 / 221 / 119 (9,6 %) |
| MOT P / R / F1 | 0,3756 / 0,6434 / **0,474286** (tp 83 fp 138 fn 46) |
| PR-AUC | 0,4550 |
| referanse tavla | 0,474286 (forsøk #1040 smed3, #1028 smed) |
| avvik | +0,000000 → **GRØNN** |
| rød test | `REF=0.40` → RØD, exit 3; tmp ryddet |

Full logg: `state/rapporter/arkitekt_kaldstart_logg.txt`.

## Forbehold
- Agenten kjører fortsatt på `data_v3` (vår egen SEC N-PX-henting), ikke på gudens `real_votes` og rundens `maaler.sh`. Id-formatene er ulike, så tavlas `forsok_beste` på rundens måler kan ikke brukes som referanse.
  Når #2053 setter smed2s nye modell inn i agenten, må stiene i steg 1 og eventuelt måleren i steg 4 følge med. Det er 3–4 linjer i skriptet.
- `uv sync` henter fra uv-cachen på minien, så installasjonen er kald fra lås, men ikke fra nett.
- Referansen er det *beste* agentforsøket. Blir en ny agentversjon dårligere, går skriptet rødt med vilje.
