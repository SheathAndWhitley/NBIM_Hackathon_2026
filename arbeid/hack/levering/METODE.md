# Metode: slik er stemmeagenten bygget og målt (Case 1)

> **Hovedtall (#231, frosset modell repo4 = #2044 miks h2 + 4 repotrekk, byttet 17:03 etter byttedom #2570):** F1 **0,512 på MOT mot styret**, 95 % KI [0,40; 0,62],
> test 2026 på NBIMs egne stemmer (real_votes, 1539 saker med fasit, 58 MOT mot styret; P 0,478, R 0,552,
> TP 32 FP 35 FN 26). Målt med `c1/maaler_offisiell_v3.py --score mot` (#2087, dommer kald kopi #2090). Val 2025: 0,530 [0,42; 0,64].
> *Avvik:* 0,5294 (avvik fra styret inkl. 5 AVSTÅ, 66 saker, KI [0,42; 0,63], #2592) er et sidetall, ikke hovedtallet.
> Følg styret: F1 0.

## 0. Hovedmodellen på real_votes (den som leveres)
- **Data:** arrangørens `real_votes` (`state/opplastet/20261105_114241_real_votes.csv`), NBIMs egne stemmer 2019–2026, alle saktyper, utviklede (8577 rader) og fremvoksende markeder (4747). **Fasit (#231):** MOT mot styret = `nbim_vote` MOT og `against_board` 1 (måler v3 `--score mot`). Modellen trenes på `against_board` (avvik, inkl. AVSTÅ).
- **Splitt etter møteår, aldri tilfeldig** (tellinger fra datafila, #2137):

  | split | år | saker | MOT mot styret | avvik |
  |---|---|---|---|---|
  | train | 2019–2024 | 9876 | 504 | 575 |
  | val | 2025 | 1909 | 99 | 103 |
  | test | 2026 | 1539 | 58 | 66 |

  Val-modellen er trent på 2019–2024. Test-modellen er trent på 2019–2025 (11 785 saker) og kjørt én gang.
- **Trekk:** TF-IDF på forslagsteksten; kategorier `proposal_type`, `proponent`, `mgmt_rec`, `mgmt_rec_raw`, `country`, `market`; MOT-historikk per selskap, per selskap+tekst og per tekst, løpende (`--hist 2`: bare møter strengt før møtedatoen, også tidligere i samme sesong; forutsetter at NBIM publiserer stemmene løpende). Logistisk regresjon (balanserte vekter) og LightGBM (400 trær), snitt av rangene («miks»). Forbudt og stoppet med assert: `nbim_vote`, `nbim_vote_raw`, `rationale_text`, `rationale_section`, `funds_disagree`, `position_paper` (`oppgave_2044/train.py:3-4,24`).
- **Grensen 0,9232:** C ∈ {0,1; 0,3; 1; 3} × 80 grenser mellom 80- og 99,5-persentilen av val-scorene. Høyest val-F1 ga C = 3 og rå grense 0,9232 for repo4 (val-F1 0,525 på avvik, `kjor_agent_real_test2026.txt`; frossen hadde 0,9232). Grensen ble låst før test 2026 ble kjørt én gang (`oppgave_2044/train.py:101-116`).
- **Lekkasjesjekk (#2103):** uten sakstypen endres F1 MOT med −0,011 [−0,040; +0,011] på val og +0,024 [−0,012; +0,062] på test (parret bootstrap), altså ingen lekkasje via kategorien (`c1_lekkasje_v3.md`). Den store avhengigheten er den løpende historikken: med bare år før (`--hist 1`) går F1 0,512 → 0,415 [0,30; 0,53] på MOT mot styret (#2134, `c1_enkle_regler_og_hist1.md`; 0,386 i #1038 var på avvik).
- **Usikkerhet (#2095):** klyngebootstrap med selskap som klynge (135 selskaper i test, 2000 trekk): test 0,512 [0,40; 0,62], val 0,530 [0,42; 0,64] (`oppgave_2095/ki_mot.py`). Følg styret gir F1 0.

## 7. Sitater og kilder (den leverte agenten)
*Nummeret er beholdt fordi andre filer viser til det. Sitatene påvirker ingen prediksjon: svarfila er byte-lik med og uten sitat-oppslaget (#2106).*
Agenten gir to slags sitat per sak i `agent.csv`:
- **A. Retningslinja (`retningslinje_id`, `retningslinje_sitat`, `retningslinje_grunnlag`):** et ordrett avsnitt fra NBIMs *Global Voting Guidelines* (https://www.nbim.no/en/responsible-investment/voting/global-voting-guidelines/). Det velges med BM25 over 140 GVG-punkter pluss seksjonen til nabo-begrunnelsen (B), med vekter låst på val 2025 (`retningslinje_oppslag.py`, #2106). På test 2026 er det 1578 rader og 18 ulike avsnitt. 1504 rader er FOR-standarden NBIM 0.0.3 («Our starting point when deciding how to vote is to support the board»), og 74 er et konkret punkt (#2130).
  - *Ordrett:* 15 av 15 avsnitt den frosne agenten siterer står ordrett på nbim.no (hentet 05.11) og i PDF-en fra 2024: #2130 kontrollerte alle 140 GVG-punkter i den lokale kopien, dommeren talte 15 ulike på den frosne agenten (#2278; en kjøring kl. 12:47 ga 18). Siste ledd i id-en (f.eks. `.2` i 1.1.2) er vår telling og står ikke på nbim.no.
  - *Riktig seksjon:* på MOT-sakene der NBIM selv oppga seksjon, treffer agenten samme seksjon i 54 av 63 (86 %) på test og 68 % på val (#2106). Nesten hele treffet kommer fra nabo-begrunnelsen.
  - *Stikkprøve (#2115, 20 av 63 MOT-saker, seed 2115):* 20/20 ordrett, **15/20 er regelen som avgjør**, 4 delvis (riktig seksjon, svakere avsnitt) og 1 feil (6.1.3 på en vedtektssak). Rettingen av de fem pågår i #2120. Forbehold: utvalget er faktiske MOT-saker, ikke agentens predikerte MOT.
- **B. Tidligere NBIM-begrunnelse (`punkt`, `sitat`):** `rationale_text` fra en lignende sak (TF-IDF-nabo), med 20 unike tekster på test. 12 stemmer med dagens GVG-tekst, og 8 er skrevet etter en eldre versjon av retningslinjene (#2130). De er ekte NBIM-tekst, men står ikke ordrett på nbim.no i dag.
- **Hvorfor `rationale_*` er sitat og ikke trekk:** modellen leser aldri `rationale_*` (assert i `oppgave_2044/train.py`). Sitatet hentes *etter* at MOT/FOR er bestemt, og bare fra andre møter i tidligere år (`c1_real.py:114` utelukker samme år, senere år og samme møte). Sakens egen begrunnelse brukes aldri. Begrunnelsen viser hva NBIM skrev i en lignende sak før. Den er ikke NBIMs begrunnelse for denne saken.
- Ordrett betyr ikke at sitatet begrunner stemmen. Det sier hvor mennesket skal lese.
