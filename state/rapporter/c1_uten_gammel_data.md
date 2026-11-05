# Case 1: gammel data påvirker ikke den frosne modellen (#2044 miks h2) (smed #2225, ordre #242)

**Svar: ja, det er bevist.** I en kald kopi uten noen gamle datamapper blir prediksjonene byte-like (sha256), og F1 MOT på test 2026 er 0,476190 som før. Ingen rader endret seg.

## Oppsett (05.11 kl. 13.29)
- `BEHOLD=1 bash arbeid/hack/c1/kaldstart.sh` -> `/tmp/c1_kald.XMN7aG` (git 58f2bd1). arbeid/hack er ikke rørt.
- Kopien har 35 filer, 3,5 MB. Eneste data er arrangørens `state/opplastet/20261105_114241_real_votes.csv` og `hack/c1/data_off/real_test_input.csv` (avledet av den), pluss `retningslinjer/punkter.jsonl` (NBIMs retningslinjer, ikke stemmedata).
- Ingen Vanguard-, iShares-, SPDR-, SEC/N-PX-mapper eller npx_votes finnes i kopien. Modellen trenes på nytt i kopien (train.py kjøres med runpy), og .venv bygges fra uv.lock.

## Resultat
| Fil | Kald kopi uten gammel data | Frossen i landsbyen | Lik? |
|---|---|---|---|
| `_pred_uten_ruting.csv` (maskin alene) | 22ac6717e1287c5a… | `hack/levering/kjor_agent_real_maskin_alene.csv` 22ac6717e1287c5a… | ja |
| `pred_maaler.csv` (med ruting) | b113b545dd86b263… | `hack/levering/kjor_agent_real_pred_maaler.csv` b113b545dd86b263… | ja |
| `train.py --variant miks --hist 2` direkte | 40afcc3e2fec85b2… | `oppgave_2044/pred_miks_h2.csv` 40afcc3e2fec85b2… | ja |

Måler v3 (sha 8b09c36e01), test 2026, MOT mot styret: TP 30, FP 38, FN 28, P 0,4412, R 0,5172, **F1 0,476190**. Kaldstart sier GRØNN, avvik +0,000000, tid 43 s. Agenten: 1578 saker, 74 MOT, 188 (11,9 %) går til et menneske.

## Hvilke filer agenten åpner (audit-hook)
Jeg kjørte agenten en gang til med `sys.addaudithook` på alle `open`-kall (`arbeid/oppgave_2225/c1_kald_audit.py`, logg i `arbeid/oppgave_2225/aapnet.txt`). Utenom Python-biblioteker og egne ut-filer åpnet den bare disse:
`real_test_input.csv`, `punkter.jsonl`, `kjor_agent.py`, `oppgave_2044/train.py` og `real_votes.csv`. Alle ligger i tmp-kopien. Det var 0 åpninger under ~ og 0 treff på vanguard/ishares/spdr/sec_/npx. Den andre kjøringen ga samme sha (22ac6717…).

## Forbehold
- Kopien har med seg hjelpeskript i `hack/c1/*.py` (hent_npx.py o.l.), men agenten åpner dem aldri (se auditen). #2223/#2218 kan fjerne dem fra kaldstart-lista for ryddighetens skyld.
- Auditen dekker bare Python-`open`. LightGBM leser ingen filer selv.
