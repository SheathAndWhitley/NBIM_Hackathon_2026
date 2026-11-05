# Case 1: dommerkontroll av demoen og robusthetstesten etter dataryddingen (dommer2 #2233, 05.11 kl. 13.50)

**Dom: GODKJENT med to avvik som må rettes i demo-skriptet før 16.** Modellen, prediksjonene og alle tall i manuset stemmer.
De to avvikene gjelder bare hva som står på skjermen. Smed (#2227) fant de samme to, uavhengig av meg.
Robusthetstallene i pakka (BEGRENSNINGER.md:18, JURY.md:17) er de samme som #2228 målte.

## Slik kontrollerte jeg
- Egen kald kopi `/tmp/d2233_kald`, med samme filliste som `kaldstart.sh` pluss `hack/c1/demo_*.sh`. Ny .venv med `uv sync --frozen`. Bare arrangørens real_votes (sha256 71ba5135…).
- Kjørte selv, ordrett fra kopiens rot: `bash arbeid/hack/c1/demo_saker_2026.sh /tmp/d2233_demo` (44 s, inkludert første import) og `bash arbeid/hack/c1/demo_mangler_styret.sh /tmp/d2233_mangler`.
- Målte `full/_pred_uten_ruting.csv` og `full/pred_maaler.csv` med måler v3 (`--data real --score mot`). Regnet de andre tallene fra `full/agent.csv` og fasit.

## Demo-manuset (`arbeid/hack/c1/DEMO_MANUS.md`), tall for tall
| Sted | Utsagn i manuset | Min måling | Dom |
|---|---|---|---|
| Valg | 1539 saker i test 2026 med fasit | 1539 (1578 inn, 39 uten fasit) | OK |
| Valg | Seed 0–16 holder ikke, seed 17 er første | trekk.log: 0–16 «nytt trekk», 17 OK | OK |
| Valg | Sitatsak med seed 0 blant {N_AGENT_MOT} 71 agent-MOT | 71, 2089132\|3 | OK |
| 0:00 | NBIM følger styret i ca. 96 % | 1481/1539 = 96,2 % | OK |
| 0:00 | F1 MOT 0,476, følg styret F1 0 | v3: 0,476190 | OK |
| 0:00 | Treffprosent 95,7 %, følg styret 96,2 % | 1473/1539 = 95,7 %; 96,2 % | OK |
| 0:00 | 97,4 % = andelen riktige FOR | 1443/1481 ekte FOR-saker sagt FOR = 97,4 % | OK (betyr andel av ekte FOR, ikke av agentens FOR, som er 98,1 %) |
| 0:00 | 30 av 58, 44 % av flaggene ekte | TP 30, FN 28, 30/68 = 44 % | OK |
| Sak 1 | 2056685\|7 FOR, rå 0,912, 19 %, til menneske (usikker), fasit For | 0,91223, 0,1912, 1, For | OK |
| Sak 2 | 2041102\|2 FOR, 0,262, 0,8 %, nei, For | 0,2623, 0,0075, 0, For | OK |
| Sak 3 | 2039527\|11 FOR, 0,636, 5 %, ja (ukjent selskap), For | 0,63559, 0,0455, 1 ukjent selskap, For | OK |
| Sak 4 | 2084542\|6 FOR, 0,451, 1 %, nei, Against | 0,45061, 0,0138, 0, Against | OK |
| Sak 5 | 2089598\|12 FOR, 0,257, 0,8 %, ja (ukjent selskap), Against | 0,257, 0,0075, 1 ukjent selskap, Against | OK |
| Sak 1 | Grense {GRENSE} 0,919 | 0,91885 | OK |
| Sak 4/5 | NBIMs begrunnelser ordrett (Klarna, Nomad) | lik `rationale_text` i real_votes | OK |
| Sak 4/5 | Bare 2 MOT på emisjoner i 2026 | 2 (SHARE_ISSUANCE, against_board=1) | OK |
| Sak 4/5 | Recall {R_TEST} 0,52 | 0,5172 | OK |
| Sak 6 | TV TOKYO 18.06.2026, MOT, rå 0,970, 52 %, til menneske, GVG 1.1 fra NBIM 2023, fasit Against | 0,96994, 0,5217, 1, GVG 1.1, kilde «NBIMs begrunnelse 2023, TV TOKYO», Against | OK |
| Sak 6 | 799 NBIM-begrunnelser har bare 18 ulike tekster (`c1/kilder/nbim_begrunnelser.csv`) | 799 ikke-tomme, 18 ulike i den fila | OK, men se merknad 3 |
| 3:40 | {N_RUTET} 183 av 1539, 11,9 % | 183/1539; v3 «183 til menneske (11.9%)» | OK |
| Sak 7 | Utskriften fra demo_mangler_styret.sh | ord for ord lik; skjermen har i tillegg en `forslag:`-linje per blokk | OK |
| 4:30 | F1 0,476, KI 0,36–0,59, P 0,44, R 0,52, TP 30 FP 38 FN 28 av 58 | v3: 0,4762 / 0,4412 / 0,5172 / 30 38 28 / 58 | OK (KI ikke kjørt på nytt: arvet fra #2095, prediksjonene er like etter ryddingen, #2225) |
| 4:30 | «Én kommando fra kald start: demo_saker_2026.sh» (og det juryen ser) | siste linje på skjermen er `SCORE 0.4818` | **AVVIK 1** |
| 0:40 | Kolonnen «rå score» (0,912 osv.) slik den står på skjermen | skjermen viser `score 0.1912`: det er p_mot, ikke rå score | **AVVIK 2** |
| Tid | ca. 15 s / ca. 10 s | 44 s / ca. 12 s hos meg (smed: 15,7 s / 11,4 s) | OK (første kjøring er tregere) |

**AVVIK 1.** `demo_saker_2026.sh` skriver til slutt `grep ^SCORE full.log`. Det er agentens egen sjekk av «avvik fra styret» (66 i fasit, F1 0,4818), ikke måler v3 «MOT mot styret» (58, F1 0,476). En jury som ser 0,4818 på skjermen og hører 0,476, vil spørre. Rett: la skriptet skrive v3-linja (`maaler_offisiell_v3.py $UT/full/_pred_uten_ruting.csv test --data real --score mot | grep -E "MOT mot styret|SCORE"`).
**AVVIK 2.** I utskriften står `score {p_mot}`. Rett: `rå {raa_score}  sjanse for MOT {p_mot}`. Ingen av rettingene rører modellen eller prediksjonene.

## Robusthet (#2228) mot pakka
| Utsagn i pakka | #2228 (`arbeid/oppgave_2228/resultat.json`, `f1.txt`) | Dom |
|---|---|---|
| 8 varianter × 1578 saker, ingen krasj | 8 × n=1578, alle rc 0 | OK |
| «Stem FOR/MOT» flagges, alle saker går til menneske | flagget 1578, til menneske 1578 (A og B) | OK |
| «Kindly support/oppose» flagges ikke | flagget 1 (den ene som var flagget fra før) | OK |
| Vei B: 35–41 saker bytter stemme | 36, 35, 41, 40 | OK |
| 20–21 av dem går ikke til menneske | endret_ikke_rutet 20 og 21 | OK |
| F1 MOT faller fra 0,476 til 0,387–0,400 | 0,4000 / 0,3960 / 0,3871 / 0,4000; rent 0,4762 | OK |
| Rare filer (#2202/#2205): ingen krasj, fasitkolonne avvises | 12 + 10 filer, rc 0 bortsett fra 29 (rc 1 med vilje) | OK (lest fra #2228, ikke kjørt selv) |

Robusthetstallene for nye selskaper, tomme felt og manglende styreanbefaling (BEGRENSNINGER.md:14–17) kommer fra `oppgave_2144/robusthet_frossen.py`, ikke fra #2228. Dem har jeg ikke kontrollert her.

## Merknader (ikke avvik)
3. Påstanden 799/18 bygger på `c1/kilder/nbim_begrunnelser.csv`, en NBIM-kilde utenfor arrangørens data. I real_votes er tallet 627 ikke-tomme begrunnelser og 34 ulike tekster. Poenget holder i begge (få faste standardtekster). Men etter #242 (bare arrangørens data) bør manuset heller si 627/34 fra real_votes, eller si tydelig hvor tallet kommer fra. Speider bestemmer.
4. `kaldstart.sh` kopierer ikke `hack/c1/demo_*.sh`. Kl. 19.30 må dommeren kopiere dem inn selv, slik jeg og smed gjorde, eller så må fillista utvides.
5. Måler v3 har ny sha (`418a937e57`) etter #2221. Tallet er det samme. Papirene som oppgir 8b09c36e01 må oppdateres.
