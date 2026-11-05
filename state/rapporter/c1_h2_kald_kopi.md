# Case 1 H2 lukket: ett kall fra tom mappe gir hovedtallet (#2094, smed3)

**Kommando:** `bash arbeid/hack/c1/leveranse/kjor.sh` (virker fra hvor som helst, trenger bare uv, 29 s).
Den kaller `levering/fremmed.sh`, som kopierer til en tom `/tmp/c1_kald` (`KALD=` endrer stien), lager et låst
uv-miljø, kjører hele agenten under `env -i` og måler test 2026.

**Tall (fra tom mappe, 05.11):** forsøk **#1106** på rundens måler (oppgave 2034, maaler_offisiell_v2 real test):
**0,481752** F1 på avvik. v3: **MOT mot styret F1 0,4762** (TP 30 FP 38 FN 28, 58 i fasit). Det er samme tall som README-ene viser.

Hva jeg endret:
- `fremmed.sh` kopierte bare N-PX-delene. Nå kopierer det også c1_real.py, oppgave_2044/train.py,
  oppgave_2047/vern.py, oppgave_2046/case1_mot.py, real_votes.csv, data_off/real_test_input.csv og målerne v2/v3.
  Målerne har `<repo>/` hardkodet. I kopien skrives stien om til kopien med sed, så en kald kopi ikke
  leser data fra landsbymappen. Regnestykket er det samme.
- `kjor.sh`: standard er nå real-sporet (`SPOR=real`). Den gamle N-PX-grunnlinja (0,383) kjøres med `SPOR=npx`.
  N-PX-delen er ikke endret og ikke kjørt på nytt, fordi den trenger nett til sec.gov.
- `c1/leveranse/README.md` og `levering/README.md` viser nå tallene og kommandoen over.

Funn: rutingen i README var utdatert. Det sto 176 av 1578 / 171 av 1539. Målt nå er det 228 av 1578 / 223 av 1539
(14,5 %): 175 nær grensen, 52 ukjent selskap og 1 instruks. Kjøringen på plass og den kalde kopien gir byte-like
agent.csv, så avviket kommer ikke av kopieringen. Det er rettet i c1-README-en. Dommeren bør sjekke KRAVRESPONS/JURY for 171.
Merk: oppgave 2094 arvet den globale måleren (Name that LLM), så forsøket er registrert med `--oppgave 2034`.
Filer: arbeid/oppgave_2094/pred_kald_test2026.csv, agent_kald.csv.
Filer som fortsatt har 171 eller 11,1 % og bør sjekkes: c1/leveranse/BEGRENSNINGER.md, levering/KRAVRESPONS.md, levering/kjor_agent_real_test2026_LES.md.
