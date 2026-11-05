# Case 1 (#2037, smed3): NBIMs egne begrunnelser som sitat for hver MOT

**Hva:** ny agent `arbeid/hack/varianter/smed3_utf_sitat/nbim_sitat.py`. Den predikerer avvik fra styret
(tf-idf på forslagstekst + type/land/marked/forslagsstiller/styrets råd + selskapets avvik i tidligere år,
logistisk regresjon, grense 0,73 valgt på val). For hver MOT henter den nærmeste NBIM-begrunnelse
(`rationale_text` + `rationale_section`) fra sitatbanken: 474 avvik med begrunnelse fra train-år (≤2024),
alltid fra et **annet møte** og et **tidligere år** enn saken. Samme sakstype får +0,3 i likhet, samme
selskap +0,1 (derfor kan «likhet» passere 1). `rationale_*` er aldri feature, bare sitat.

**Tall (offisiell måler `maaler_offisiell.py --data real`):**
| vindu | avvik-F1 | PR-AUC | MOT-F1 (P / R) | rutet |
|---|---|---|---|---|
| val 2025 | 0,512 | 0,447 | 0,530 (0,55 / 0,51) | 4,0 % |
| test 2026 | **0,480** | 0,491 | **0,481** (0,41 / 0,58) | 3,3 % |
| følg styret / alltid avvik (test) | 0 / 0,082 | | 0 | |

**Sitatkvalitet:** der agenten sier MOT og NBIM faktisk avvek med egen begrunnelse, er sitert seksjon
den samme som NBIMs: val 49/53 (92 %), test 34/37 (92 %). Alle 91 MOT på test har sitat; alle fra ≤2024.

**Ærlig svakhet:** halvparten av MOT-ene er feil (P 0,41). Mange treff er «samme selskap, samme person
tidligere år» (Otsuka, Volkswagen, Dell) – sterkt signal, men det gir også FP der NBIM har snudd.
Lav likhet (<0,7) betyr svakt sitat (nr. 8 og 10 under: lønnssystem sitert som vedtektsendring);
det bør vises som «svakt sitat, se manuelt» i grensesnittet.

**Kjør:** `cd arbeid/hack/varianter/smed3_utf_sitat && ../smed2_gbm/.venv/bin/python -I nbim_sitat.py`
→ `ut/real_{val,test}_svar.csv` (til måleren) og `ut/real_{val,test}_sitat.csv` (sitat per MOT). Forsøk #1041.

## Stikkprøve: 10 tilfeldige MOT på test 2026 (seed 2037), med fasit
1. **Triple Flag Precious Metals Corp.** (Canada, 2026), `2043502|11`: «Advisory Vote on Executive Compensation Approach». Agent: MOT (p=0.765). Fasit: NBIM FOR, feil (NBIM fulgte styret); NBIMs seksjon –.
   Sitat: GVG 3.3 fra GFL Environmental Inc. 2021 («Advisory Vote on Executive Compensation Approach», likhet 1.30): _«The board is responsible for attracting the right CEO and setting appropriate remuneration. A substantial proportion of annual remuneration should be provided as shares that are locked in for five to ten years, regardles…»_

2. **Dell Technologies, Inc.** (United States, 2026), `2085617|3`: «Elect Director Egon Durban». Agent: MOT (p=0.817). Fasit: NBIM FOR, feil (NBIM fulgte styret); NBIMs seksjon –.
   Sitat: GVG 2.1 fra Dell Technologies, Inc. 2021 («Elect Director Egon Durban», likhet 1.40): _«Board members should devote sufficient time to fulfil their responsibilities effectively. The chairperson is responsible for leading all aspects of the board’s work and should devote a significant amount of time to fulfi…»_

3. **Burgan Bank KPSC** (Kuwait, 2026), `2041722|16`: «Appoint or Reappoint Auditors and Authorize Board to Fix Their Remuneration for FY 2026». Agent: MOT (p=0.863). Fasit: NBIM MOT, riktig; NBIMs seksjon GVG 5.1.
   Sitat: GVG 5.1 fra Burgan Bank KPSC 2023 («Appoint or Reappoint Auditors and Fix Their Remuneration for FY 2023», likhet 1.22): _«The external auditor should act in an independent manner. We will consider the auditor’s independence and any concerns about the accounts or audit procedures. Excessive non-audit-related fees represent a potential confli…»_

4. **DocMorris Ltd.** (Switzerland, 2026), `2042367|29`: «Transact Other Business (Voting)». Agent: MOT (p=0.991). Fasit: NBIM MOT, riktig; NBIMs seksjon GVG 5.2.
   Sitat: GVG 5.2 fra DocMorris Ltd. 2020 («Transact Other Business (Voting)», likhet 1.40): _«We will not support an agenda item if the information disclosed is insufficient to make an informed decision.»_

5. **Volkswagen AG** (Germany, 2026), `2033896|36`: «Elect Hans Dieter Poetsch to the Supervisory Board». Agent: MOT (p=0.869). Fasit: NBIM MOT, riktig; NBIMs seksjon GVG 1.1.
   Sitat: GVG 1.1 fra Volkswagen AG 2021 («Elect Hans Poetsch to the Supervisory Board», likhet 1.24): _«The board should guide company strategy and monitor management performance without conflicts of interest. A majority of shareholder-elected board members in a non-controlled company should be independent of management, d…»_

6. **Arbonia AG** (Switzerland, 2026), `2041102|6`: «Reelect Peter Barandun as Director and Member of the Compensation Committee». Agent: MOT (p=0.812). Fasit: NBIM MOT, riktig; NBIMs seksjon GVG 2.3.
   Sitat: GVG 2.3 fra Arbonia AG 2021 («Elect Peter Barandun as Director and Member of the Compensation Commit», likhet 1.28): _«Diversity contributes to the overall effectiveness of the board and is a sign of an effective nomination process. The board should ensure that it can bring a broad range of perspectives and approaches to its decision-mak…»_

7. **Otsuka Holdings Co., Ltd.** (Japan, 2026), `2045371|1`: «Elect Director Otsuka, Ichiro». Agent: MOT (p=0.819). Fasit: NBIM MOT, riktig; NBIMs seksjon GVG 1.1.
   Sitat: GVG 1.1 fra Otsuka Holdings Co., Ltd. 2023 («Elect Director Otsuka, Ichiro», likhet 1.40): _«The board should guide company strategy and monitor management performance without conflicts of interest. A majority of shareholder-elected board members in a non-controlled company should be independent of management, d…»_

8. **Zhejiang Changsheng Sliding Bearings Co., Ltd.** (China, 2026), `2076468|9`: «Amend Remuneration Management System for Directors and Senior Management Members». Agent: MOT (p=0.872). Fasit: NBIM FOR, feil (NBIM fulgte styret); NBIMs seksjon –.
   Sitat: GVG 4.3 fra S.F. Holding Co., Ltd. 2022 («Amend Management System of Raised Funds», likhet 0.63): _«The right to vote on fundamental changes affecting the company is a basic right of shareholders. This includes the right to approve changes to the company’s governing documents.»_

9. **EQB Inc.** (Canada, 2026), `2035238|12`: «Advisory Vote on Executive Compensation Approach». Agent: MOT (p=0.830). Fasit: NBIM FOR, feil (NBIM fulgte styret); NBIMs seksjon –.
   Sitat: GVG 3.3 fra GFL Environmental Inc. 2021 («Advisory Vote on Executive Compensation Approach», likhet 1.30): _«The board is responsible for attracting the right CEO and setting appropriate remuneration. A substantial proportion of annual remuneration should be provided as shares that are locked in for five to ten years, regardles…»_

10. **Jiangsu Jiejie Microelectronics Co., Ltd.** (China, 2026), `2069430|8`: «Approve to Formulate Remuneration Management System for Directors and Senior Management Me». Agent: MOT (p=0.780). Fasit: NBIM FOR, feil (NBIM fulgte styret); NBIMs seksjon –.
   Sitat: GVG 4.3 fra S.F. Holding Co., Ltd. 2022 («Amend Management System of Raised Funds», likhet 0.54): _«The right to vote on fundamental changes affecting the company is a basic right of shareholders. This includes the right to approve changes to the company’s governing documents.»_

Fasit i stikkprøven: 5 av 10 riktige, i tråd med P 0,41. Alle 5 riktige har sitat fra samme seksjon som NBIMs egen begrunnelse.
