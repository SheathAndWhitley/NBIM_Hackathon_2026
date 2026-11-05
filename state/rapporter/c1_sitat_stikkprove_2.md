# Case 1: ny stikkprøve av 20 sitater fra den frosne agenten (#2262, dommer2): 19/20 OK, 9/10 på MOT

**Kjøring fra kald start.** `sh arbeid/hack/levering/fremmed.sh /tmp/d2_2262` kl. 14:00 (kjor_agent.py sha dedc94062cf4, c1_real.py f0acb3c5aedd, retningslinje_oppslag.py 0a45c013471b). HOVEDTALL F1 MOT 0,476190 (TP 30, FP 38, FN 28), 188 av 1 578 til menneske (11,9 %), tallvakt grønn. `agent.csv` (sha f0444a47ee0f) er byte-lik forrige kalde kjøring i `/tmp/c1_kald` kl. 13:41. Kopi: `arbeid/oppgave_2262/agent.csv`.
**Utvalget.** `arbeid/oppgave_2262/stikk.py`, seed 2262, lagdelt: 10 tilfeldige av agentens 74 MOT og 10 av 1 504 FOR (id-er i `utvalg.json`, full utskrift i `stikk_utskrift.txt`).
**Kildene.** GVG-avsnittet (`retningslinje_sitat`) er sjekket mot NBIMs rå nettside `arbeid/speider/c1ret_raa/nbim_gvg.html` og PDF 2024, med nummeret utledet fra HTML-overskriftene (ikke fra vår punkter.jsonl). NBIMs tidligere begrunnelse (`sitat`/`sitat_kilde`) er sjekket mot arrangørens `real_votes.csv`: finnes raden kilden oppgir (år, selskap, sak), og er teksten ordrett lik?

## Svar
| kontroll | MOT (10) | FOR (10) | alle (20) |
|---|---|---|---|
| GVG-sitatet står ordrett på nbim.no og i PDF 2024 | 10/10 | 10/10 | **20/20** |
| GVG-nummeret stemmer med HTML-overskriftene | 10/10 | 10/10 (0.0.3 = innledningen, vår telling) | 20/20 |
| Den tidligere begrunnelsen er ordrett lik kilderaden i real_votes, og kilden er fra et tidligere år (2020–2024) | 10/10 | (ingen, FOR siterer bare 0.0.3) | 10/10 |
| Sitatet passer saken (riktig seksjon og rimelig avsnitt) | **9/10** | 10/10 | 19/20 |
| **Hele raden OK** | **9/10** | **10/10** | **19/20** |

Sammenlignet med #2006 (10/20, MOT 0/10) og #2012 (17/20, MOT 7/10). Ingen sitater er diktet opp, og ingen kilde er fra sakens eget år.

## Feilen: Snowflake (rad 6)
`2086078|6` Snowflake, aksjonærforslaget «Require a Majority Vote for the Election of Directors». Styret sier MOT, agenten FOR (mot styret, riktig: NBIM stemte FOR). Agenten siterer **NBIM 6.2.5** (anti-takeover) via naboen Tesla 2020 «Adopt Simple Majority Vote». Riktig er **GVG 3.1**, og nettsiden har en regel som treffer presist: 3.1.8 «We will support a proposal to introduce majority requirements in director elections.» NBIMs egen 2026-begrunnelse er 3.1. Sitatet er ordrett, men hører til feil seksjon. Årsak: nabo-oppslaget matcher ordet «majority vote» til Teslas supermajority-sak. Ikke blokkerende (1 av 74 MOT i stikkprøven), men et godt ærlig eksempel til ERLIG_EVALUERING.

## Forbehold juryen bør få
- **Eldre NBIM-ordlyd.** 3 av 10 begrunnelsessitater (NBIMs egne ord fra 2020–2023) står ikke ordrett på nbim.no *i dag*: 5.2.4 har fått tillegget «e.g. the agenda item "other business"», 1.1.2 har mistet et komma, og 1.3 om styreleder/CEO er skrevet om («we believe shareholders are best served when …»). Teksten er ekte NBIM-tekst fra arrangørens data, og agenten merker den som «NBIMs begrunnelse <år>», ikke som dagens retningslinje. Samme funn som speider #2130 (8 av 20 unike).
- **Kildefeltet avkorter saktittelen** til ca. 80 tegn (rad 2 HP og rad 10 Colruyt). Raden finnes, men et menneske som søker på tittelen må bruke prefiks.
- GVG-sitatet er seksjonens første avsnitt (prinsippet), ikke regelen som slo til. Regelen står i `retningslinje_grunnlag` («regler i seksjonen et menneske bør sjekke») og i den tidligere begrunnelsen. Kjent fra #2143.
- 8 av 10 MOT i utvalget går til menneske (kalibrert P(MOT) i båndet 0,15–0,85); bare «Other Business» (p 1,0) går rett gjennom.

## Tabell, MOT (10)
| # | sak | agent | fasit NBIM | GVG-sitat | ordrett web/PDF | begrunnelse ordrett i kilde (år) | passer | rad |
|---|---|---|---|---|---|---|---|---|
| 1 | Global Power Synergy, Other Business | MOT | MOT, 5.2 | 5.2.1 | ja/ja | ja (2020, samme selskap) | ja (5.2.4 i begrunnelsen) | OK |
| 2 | HP, Require Independent Board Chair (styret MOT) | FOR, menneske | FOR mot styret, 1.3 | 1.3.1 | ja/ja | ja (2023 TSURUHA) | ja | OK |
| 3 | Fine Organic, Elect Nadkarni | MOT, menneske | FOR | 1.2.1 | ja/ja | ja (2023, samme selskap) | ja (plausibel, men feil-MOT) | OK |
| 4 | Tokyo Tatemono, Elect Tanehashi | MOT, menneske | FOR | 1.1.1 | ja/ja | ja (2023, samme sak) | ja (plausibel, men feil-MOT) | OK |
| 5 | Consun Pharma, Elect An Meng | MOT, menneske | MOT, 1.2 | 1.2.1 | ja/ja | ja (2024, samme sak) | ja | OK |
| 6 | Snowflake, Majority Vote for Directors (styret MOT) | FOR, menneske | FOR mot styret, 3.1 | **6.2.5** | ja/ja | ja (2020 Tesla) | **nei: riktig er 3.1.8** | **FEIL** |
| 7 | PT Solusi Sinergi, Changes in the Boards | MOT, menneske | MOT, 3.1 | 3.1.1 | ja/ja | ja (2024 PT Rukun Raharja) | ja | OK |
| 8 | Keymed, Elect Changyu Wang | MOT, menneske | MOT, 1.2 | 1.2.1 | ja/ja | ja (2023, samme sak) | ja | OK |
| 9 | Praram 9 Hospital, Other Business | MOT | MOT, 5.2 | 5.2.1 | ja/ja | ja (2020, samme selskap) | ja (5.2.4 i begrunnelsen) | OK |
| 10 | Colruyt, Reelect Jef Colruyt | MOT, menneske | FOR | 1.1.1 | ja/ja | ja (2024, samme person) | ja (plausibel, men feil-MOT) | OK |

Prediksjonene i MOT-utvalget: 7 av 10 riktige mot styret, 3 feil-MOT, alle 3 sendt til menneske.

## Tabell, FOR (10)
Rad 11–20 (Lepu Medical, DocMorris ×2, Tokyo Tatemono, Arbonia, PVA TePla, Praram 9, ASMedia, TSURUHA, CCC Intelligent): alle siterer NBIM 0.0.3 «Our starting point when deciding how to vote is to support the board …», ordrett på nettsiden og i PDF, grunnlag «følger styret». Fasit FOR i 9 av 10, den siste er en ikke-stemmesak (PVA TePla «Receive Financial Statements», fasit tom). Alle OK.

Kommando: `sh arbeid/hack/levering/fremmed.sh /tmp/d2_2262 && python3 -I arbeid/oppgave_2262/stikk.py /tmp/d2_2262/ut/agent.csv`
