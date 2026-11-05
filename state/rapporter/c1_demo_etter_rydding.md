# Case 1: demoen virker etter at HF-cachen ble slettet (#2406)

Kjørt 2026-11-05 15:28, etter #2400. HF-cachen er nå 218 MB: bare bge-small og MiniLM ligger igjen.

**Status: GRØNN.**

| Steg | Resultat | Tid |
|---|---|---|
| `sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_kald_2406 --ny` (ny kald kopi via fremmed.sh) | exit 0, HOVEDTALL F1 MOT 0,476190, TALLVAKT GRØNN, alle tre manussaker og tre seed-0-saker vises | 30 s totalt (agenten 20 s) | <!-- eldre: frossen #2044 (0,476), dagens hovedtall er repo4 0,512 -->
| Lim-inn-fanen, én sak (første rad i #2335 tre_saker.csv), AppTest med `HF_HUB_OFFLINE=1` | 2084790\|5: MOT, P(MOT) 1,0, ikke til menneske, 0 avvik mot #2335, 1 loggfil skrevet | 6,9 s |
| `streamlit run app.py` (headless, port 8599) | /_stcore/health svarer ok | under 20 s |

- Ingen modell lastes fra nett. Agentkoden (kjor_agent.py og c1-modulene) bruker ikke sentence_transformers eller HF i det hele tatt (sjekket med grep). Loggen fra lim-inn-kjøringen nevner verken huggingface eller download, og kjøringen gikk med HF offline.
- FRYSVAKT sier «ikke frosset ennå». Det er riktig før kl. 16, ingen feil.
- Støy: Streamlit varsler at `use_container_width` blir fjernet etter 2025-12-31. Ufarlig for demoen.
- demo.sh skrev demo_utskrift.txt på nytt med samme innhold som før (tidsstempel og kopisti er nye).

Gjenta: `sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_kald_X --ny` og
`arbeid/hack/levering/demo/.venv/bin/python arbeid/oppgave_2406/en_sak.py`
