# Case 1: stikkprøve av fem saker i agentens svar (#2823) — GRØNN

Kald kopi: `jurypakke_c1_1902_cbae393.zip` (sha256 e6dae498…7818) pakket ut i tom mappe `/tmp/c1_stikk_xipV`, `sh KJOR.sh` som README sier.
Utfall: FRYSVAKT GRØNN, HOVEDTALL 0.512000, TP 32 FP 35 FN 26, TALLVAKT GRØNN (177 påstander, 0 avvik), kjøring 29 s.
Ingen endring i frossen kode. Sjekkskript (utenfor pakka): `arbeid/oppgave_2823/stikk.py`.

Kildedokument for (a): rå nedlasting av NBIM Global Voting Guidelines fra nbim.no (`arbeid/speider/c1ret_raa/nbim_gvg.html`),
HTML-tagger fjernet, mellomrom og typografiske anførselstegn normalisert, ellers ordrett delstreng-sjekk.

| sak (id) | selskap / forslag | styret | prediksjon | p_mot | retningslinje | sitat OK | flagg OK |
|---|---|---|---|---|---|---|---|
| 2033470\|1 | Kura Sushi / Elect Director Tanaka | FOR | **MOT** (mot styret) | 1.0 | NBIM 1.1.1 | ja, ordrett | ja: p_mot utenfor [0,15;0,85), ikke rutet, ingen grunn |
| 2084542\|1 | Nomad Foods / Elect Director Franklin | FOR | **MOT** (mot styret) | 1.0 | NBIM 2.1.1 | ja, ordrett | ja: ikke rutet, ingen grunn |
| 2044124\|5 | Tokyo Tatemono / Elect Director Izumi | FOR | FOR | 0.049 | NBIM 0.0.3 | ja, ordrett | ja: ikke rutet |
| 2078993\|7 | XD Inc. / Issuance of Equity w/o pre-emptive | FOR | FOR | 0.0072 | NBIM 0.0.3 | ja, ordrett | ja: ikke rutet |
| 2039527\|13 | Vietnam Eximbank / Dismiss Members of the Board | FOR | FOR → **TIL MENNESKE** | 0.049 | NBIM 0.0.3 | ja, ordrett | ja: til_menneske=1, grunn «ukjent selskap: ingen NBIM-stemmer for selskapet før møtedatoen» |

Utvalg: tilfeldig med seed 2823 fra hver gruppe; MOT-sakene er tatt blant de 14 MOT-mot-styret som agenten tar selv
(første trekk ga en MOT der styret selv sa MOT, byttet til to ekte mot-styret-saker siden det er dem hovedtallet gjelder).

Utvidet over alle 1578 rader (ikke bare fem):
- (a) `retningslinje_sitat` ordrett i NBIM-kilden: **1578 av 1578**, 0 avvik.
- (b) `til_menneske`=1 uten `rutingsgrunn`, eller grunn uten flagg: **0**. 164 saker til menneske (10,4 %).
- MOT-sakenes ekstra `sitat` (NBIMs begrunnelse fra tidligere år) finnes i arrangørens `rationale_text`; `sitat_kilde` peker på 2020/2021, dvs. før teståret. README sier selv at dette ikke er ordrett retningslinjetekst.

(c) Arrangørrader i utdata:
- `ut/agent.csv`, `pred_maaler.csv`, `_pred_uten_ruting.csv`: 1578 rader = testsakene fra juryens egen fil; ingen fasitkolonner (`nbim_vote`, `against_board`) med.
- `ut/_data/data.csv` er arbeidskopi av juryens egen `state/opplastet/20261105_114241_real_votes.csv`: samme 13 758 rader og kolonner;
  eneste forskjell er at strengen `None` er gjort til tom (666 celler). Ingen rader utover det juryen selv leverte.

**GRØNN.** Merknad (ikke rødt): det rå NBIM-kildedokumentet er ikke med i zipen (bare `punkter.jsonl` avledet av det, og URL i README for retningslinjene i utviklingsmappa); juryen kan sjekke mot nbim.no.
