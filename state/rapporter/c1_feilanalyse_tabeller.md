# #2097 tabeller: bommer for frossen modell på test 2026 (generert av arbeid/oppgave_2097/feilanalyse.py)

TP 30 FP 38 FN 28  P 0.441 R 0.517 F1 0.47619  (1539 vurderte rader test 2026)

| sakstype | TP | FP (falsk MOT) | FN (glemt MOT) | TN |
|---|---|---|---|---|
| DIRECTOR_ELECTION | 15 | 26 | 13 | 685 |
| OTHER_MGMT | 1 | 1 | 5 | 80 |
| AUDITOR | 3 | 0 | 4 | 123 |
| ARTICLES | 1 | 1 | 2 | 51 |
| SHARE_ISSUANCE | 0 | 0 | 2 | 32 |
| EQUITY_PLAN | 0 | 0 | 1 | 21 |
| FIN_STATEMENTS | 0 | 0 | 1 | 99 |
| SAY_ON_PAY | 3 | 8 | 0 | 50 |
| DISCHARGE | 0 | 1 | 0 | 87 |
| MERGER | 0 | 1 | 0 | 1 |
| OTHER_BUSINESS | 6 | 0 | 0 | 0 |
| RPT | 1 | 0 | 0 | 28 |
| **sum** | 30 | 38 | 28 | (TN bare der det finnes feil/treff) |

| land | TP | FP (falsk MOT) | FN (glemt MOT) | TN |
|---|---|---|---|---|
| United States | 0 | 9 | 7 | 201 |
| andre land | 5 | 4 | 5 | 440 |
| India | 1 | 6 | 3 | 93 |
| Japan | 4 | 3 | 3 | 264 |
| China | 0 | 2 | 3 | 124 |
| British Virgin Islands | 1 | 1 | 2 | 11 |
| South Korea | 0 | 1 | 2 | 74 |
| Indonesia | 6 | 1 | 1 | 9 |
| Cayman Islands | 2 | 0 | 1 | 61 |
| Thailand | 2 | 0 | 1 | 23 |
| Belgium | 2 | 6 | 0 | 18 |
| Switzerland | 4 | 3 | 0 | 61 |
| Germany | 3 | 2 | 0 | 64 |
| **sum** | 30 | 38 | 28 | (TN bare der det finnes feil/treff) |

| MOT før hos selskapet | TP | FP (falsk MOT) | FN (glemt MOT) | TN |
|---|---|---|---|---|
| bare tidligere år | 28 | 37 | 20 | 852 |
| nei | 2 | 1 | 8 | 591 |
| **sum** | 30 | 38 | 28 | (TN bare der det finnes feil/treff) |

| forslagsstiller | TP | FP (falsk MOT) | FN (glemt MOT) | TN |
|---|---|---|---|---|
| styret | 29 | 38 | 27 | 1429 |
| aksjonær | 1 | 0 | 1 | 14 |
| **sum** | 30 | 38 | 28 | (TN bare der det finnes feil/treff) |

## FP, sortert på p_avvik (høyest først)
- 2049868|5 First Financial Bankshares, Inc. (United States) DIRECTOR_ELECTION, p=0.988, MOT før: bare tidligere år | Elect Director F. Scott Dueser | 
- 2066391|9 The Hartford Insurance Group, Inc. (United States) DIRECTOR_ELECTION, p=0.988, MOT før: bare tidligere år | Elect Director Christopher J. Swift | 
- 2052819|7 UMB Financial Corporation (United States) DIRECTOR_ELECTION, p=0.988, MOT før: bare tidligere år | Elect Director J. Mariner Kemper | 
- 2054683|6 First Horizon Corporation (United States) DIRECTOR_ELECTION, p=0.980, MOT før: bare tidligere år | Elect Director D. Bryan Jordan | 
- 2041102|12 Arbonia AG (Switzerland) SAY_ON_PAY, p=0.978, MOT før: bare tidligere år | Approve Remuneration Report (Non-Binding) | 
- 2105186|2 Yellow Cake Plc (Jersey) DIRECTOR_ELECTION, p=0.978, MOT før: bare tidligere år | Re-elect Anthony Tudor St John, The Lord St John of Bletso as Director | 
- 2040271|7 PVA TePla AG (Germany) SAY_ON_PAY, p=0.971, MOT før: bare tidligere år | Approve Remuneration Report | 
- 2091877|2 Meidensha Corp. (Japan) DIRECTOR_ELECTION, p=0.971, MOT før: bare tidligere år | Elect Director Miida, Takeshi | 
- 2038357|7 H. Lundbeck A/S (Denmark) DIRECTOR_ELECTION, p=0.964, MOT før: bare tidligere år | Reelect Lars Erik Holmqvist as Director | 
- 2097662|18 Colruyt Group NV (Belgium) DIRECTOR_ELECTION, p=0.964, MOT før: bare tidligere år | Reelect Korys Management NV, Permanently Represented by Lisa Colruyt, as Director | 
- 2081841|4 D'Ieteren Group (Belgium) SAY_ON_PAY, p=0.963, MOT før: bare tidligere år | Approve Changes to the Remuneration Policy | 
- 2064967|5 CCC Intelligent Solutions Holdings Inc. (United States) SAY_ON_PAY, p=0.963, MOT før: bare tidligere år | Advisory Vote to Ratify Named Executive Officers' Compensation | 
- 2086078|4 Snowflake Inc. (United States) SAY_ON_PAY, p=0.961, MOT før: bare tidligere år | Advisory Vote to Ratify Named Executive Officers' Compensation | 
- 2097662|2 Colruyt Group NV (Belgium) SAY_ON_PAY, p=0.960, MOT før: bare tidligere år | Approve Remuneration Report | 
- 2033896|37 Volkswagen AG (Germany) DIRECTOR_ELECTION, p=0.959, MOT før: bare tidligere år | Elect Susanne Wiegand to the Supervisory Board | 
- 2037517|10 Almacenes Exito SA (Colombia) DIRECTOR_ELECTION, p=0.958, MOT før: bare tidligere år | Elect Directors | 
- 2045672|5 TCC Group Holdings CO., LTD. (Taiwan) MERGER, p=0.957, MOT før: bare tidligere år | Approve Amendments to Procedures Governing the Acquisition or Disposal of Assets | 
- 2073065|12 Lepu Medical Technology (Beijing) Co., Ltd. (China) DIRECTOR_ELECTION, p=0.956, MOT før: bare tidligere år | Elect Pu Fei as Director | 
- 2085617|1 Dell Technologies, Inc. (United States) DIRECTOR_ELECTION, p=0.956, MOT før: bare tidligere år | Elect Director Michael S. Dell | 
- 2047492|1 Link & Motivation, Inc. (Japan) DIRECTOR_ELECTION, p=0.955, MOT før: bare tidligere år | Elect Director Ozasa, Yoshihisa | 
- 2097662|16 Colruyt Group NV (Belgium) DIRECTOR_ELECTION, p=0.954, MOT før: bare tidligere år | Reelect Kriya One BV, Permanently Represented by Jef Colruyt, as Director | 
- 2059197|5 Wuxi NCE Power Co., Ltd. (China) ARTICLES, p=0.953, MOT før: bare tidligere år | Amend Remuneration Management System for Directors and Senior Management Members | 
- 2059500|4 Public Storage (United States) DIRECTOR_ELECTION, p=0.947, MOT før: bare tidligere år | Elect Director Ronald L. Havner, Jr. | 
- 2110694|2 NMDC Steel Ltd. (India) DIRECTOR_ELECTION, p=0.946, MOT før: bare tidligere år | Reelect Vinay Kumar as Director | 
- 2085617|3 Dell Technologies, Inc. (United States) DIRECTOR_ELECTION, p=0.945, MOT før: bare tidligere år | Elect Director Egon Durban | 
- 2084542|7 Nomad Foods Limited (British Virgin Islands) DIRECTOR_ELECTION, p=0.944, MOT før: bare tidligere år | Elect Director Victoria Parry | 
- 2086900|7 Fine Organic Industries Limited (India) OTHER_MGMT, p=0.940, MOT før: bare tidligere år | Approve Revision in Remuneration of Mukesh Shah as Chairman and Whole-Time Director | 
- 2041367|2 Mobimo Holding AG (Switzerland) SAY_ON_PAY, p=0.937, MOT før: bare tidligere år | Approve Remuneration Report (Non-Binding) | 
- 2044124|2 Tokyo Tatemono Co., Ltd. (Japan) DIRECTOR_ELECTION, p=0.932, MOT før: bare tidligere år | Elect Director Tanehashi, Makio | 
- 2046839|4 Rain Industries Ltd. (India) DIRECTOR_ELECTION, p=0.930, MOT før: bare tidligere år | Reelect N. Sujith Kumar Reddy as Director | 
- 2081841|5 D'Ieteren Group (Belgium) DIRECTOR_ELECTION, p=0.930, MOT før: bare tidligere år | Approve Remuneration of the Vice-Chairman of the Board of Directors | 
- 2110694|3 NMDC Steel Ltd. (India) DIRECTOR_ELECTION, p=0.928, MOT før: bare tidligere år | Reelect Joydeep Dasgupta as Director | 
- 2041102|5 Arbonia AG (Switzerland) DIRECTOR_ELECTION, p=0.927, MOT før: bare tidligere år | Elect Christoph Ganz as Director, Board Chair, and Member of the Compensation Committee | 
- 2097662|3 Colruyt Group NV (Belgium) SAY_ON_PAY, p=0.925, MOT før: bare tidligere år | Approve Remuneration Policy | 
- 2085864|1 PT Barito Renewables Energy Tbk (Indonesia) DISCHARGE, p=0.923, MOT før: nei | Approve Annual Report, Financial Statements, Statutory Reports and Discharge of Directors  | 
- 2048411|13 LOTTE Chemical Corp. (South Korea) DIRECTOR_ELECTION, p=0.922, MOT før: bare tidligere år | Elect Ju Woo-hyeon as Inside Director | 
- 2086900|4 Fine Organic Industries Limited (India) DIRECTOR_ELECTION, p=0.922, MOT før: bare tidligere år | Reelect Nikhil Kamat as Director | 
- 2086900|6 Fine Organic Industries Limited (India) DIRECTOR_ELECTION, p=0.921, MOT før: bare tidligere år | Elect Shailendra Nadkarni as Director | 

## FN, sortert på p_avvik (lavest først)
- 2052809|13 Texas Capital Bancshares, Inc. (United States) OTHER_MGMT, p=0.199, MOT før: bare tidligere år | Change State of Incorporation from Delaware to Texas | The right to vote on fundamental changes affecting the company is a basic right of shareholders. This includes
- 2052809|15 Texas Capital Bancshares, Inc. (United States) OTHER_MGMT, p=0.214, MOT før: bare tidligere år | Adjourn Meeting | The right to vote on fundamental changes affecting the company is a basic right of shareholders. This includes
- 2089598|11 Klarna Group Plc (United Kingdom) SHARE_ISSUANCE, p=0.241, MOT før: nei | Authorize Issue of Equity | Existing shareholders should have the right to approve share issuances in order to prevent the dilution of own
- 2089598|12 Klarna Group Plc (United Kingdom) SHARE_ISSUANCE, p=0.257, MOT før: nei | Authorize Issue of Equity without Pre-emptive Rights | Existing shareholders should have the right to approve share issuances in order to prevent the dilution of own
- 2071193|8 Ever Sunshine Services Group Limited (Cayman Islands) AUDITOR, p=0.270, MOT før: bare tidligere år | Approve Prism Hong Kong Limited as Auditors and Authorize Board to Fix Their Remuneration | The external auditor should act in an independent manner. We will consider the auditor’s independence and any 
- 2085617|11 Dell Technologies, Inc. (United States) OTHER_MGMT, p=0.406, MOT før: bare tidligere år | Change State of Incorporation from Delaware to Texas | The right to vote on fundamental changes affecting the company is a basic right of shareholders. This includes
- 2084542|9 Nomad Foods Limited (British Virgin Islands) DIRECTOR_ELECTION, p=0.410, MOT før: bare tidligere år | Elect Director Melanie Stack | Shareholders should have the right to seek changes to the board when it does not act in their best interest. W
- 2105186|5 Yellow Cake Plc (Jersey) DIRECTOR_ELECTION, p=0.442, MOT før: bare tidligere år | Re-elect Sofia Bianchi as Director | Board members should devote sufficient time to fulfil their responsibilities effectively. The chairperson is r
- 2084542|6 Nomad Foods Limited (British Virgin Islands) DIRECTOR_ELECTION, p=0.451, MOT før: bare tidligere år | Elect Director James E. Lillie | Shareholders should have the right to seek changes to the board when it does not act in their best interest. W
- 2085209|2 SPARX Group Co., Ltd. (Japan) DIRECTOR_ELECTION, p=0.484, MOT før: nei | Elect Director Abe, Shuhei | The board should guide company strategy and monitor management performance without conflicts of interest. A ma
- 2089358|1 Varroc Engineering Limited (India) FIN_STATEMENTS, p=0.589, MOT før: bare tidligere år | Accept Financial Statements and Statutory Reports | The board should use the annual report to present a fair, sensible and clear assessment of the company. The re
- 2040922|7 Star Petroleum Refining Public Company Limited (Thailand) DIRECTOR_ELECTION, p=0.602, MOT før: bare tidligere år | Elect Herbert Matthew Payne II as Director | Board decisions that are particularly vulnerable to conflicts of interest should have additional safeguards. M
- 2048572|2 Safie Inc. (Japan) DIRECTOR_ELECTION, p=0.636, MOT før: nei | Elect Director Sadoshima, Ryuhei | The board should guide company strategy and monitor management performance without conflicts of interest. A ma
- 2052809|14 Texas Capital Bancshares, Inc. (United States) OTHER_MGMT, p=0.655, MOT før: bare tidligere år | Increase Threshold to Submit Stockholder Proposals | The right to vote on fundamental changes affecting the company is a basic right of shareholders. This includes
- 2045311|15 HP Inc. (United States) EQUITY_PLAN, p=0.727, MOT før: nei | Amend Omnibus Stock Plan | The board is responsible for attracting the right CEO and setting appropriate remuneration. A substantial prop
- 2082048|5 CrowdStrike Holdings, Inc. (United States) ARTICLES, p=0.772, MOT før: bare tidligere år | Ratify Supermajority Vote Requirement to Amend Certificate of Incorporation and Bylaws | Anti-takeover measures are generally not in the interest of shareholders, and the introduction of such measure
- 2066000|7 Comfort Systems USA, Inc. (United States) DIRECTOR_ELECTION, p=0.777, MOT før: bare tidligere år | Elect Director Franklin Myers | Board members should devote sufficient time to fulfil their responsibilities effectively. The chairperson is r
- 2094542|10 Bank of Jiangsu Co., Ltd. (China) OTHER_MGMT, p=0.805, MOT før: bare tidligere år | Approve Implementing Rules for Cumulative Voting System | The right to vote on fundamental changes affecting the company is a basic right of shareholders. This includes
- 2048792|5 Fositek Corp. (Taiwan) DIRECTOR_ELECTION, p=0.806, MOT før: nei | Elect a Representative of Xinghe Investment Co., Ltd., with Shareholder No. 00000093, as N | The company should have a robust nomination and election process to ensure an effective board that is accounta
- 2084301|46 ORLEN SA (Poland) DIRECTOR_ELECTION, p=0.812, MOT før: bare tidligere år | Recall Supervisory Board Member | The company should have a robust nomination and election process to ensure an effective board that is accounta
- 2048411|10 LOTTE Chemical Corp. (South Korea) ARTICLES, p=0.855, MOT før: bare tidligere år | Amend Articles of Incorporation (Office Term) | The right to vote on fundamental changes affecting the company is a basic right of shareholders. This includes
- 2114914|3 The Monogatari Corp. (Japan) DIRECTOR_ELECTION, p=0.872, MOT før: bare tidligere år | Elect Director Kato, Hisayuki | The board should guide company strategy and monitor management performance without conflicts of interest. A ma
- 2106283|3 Indian Railway Finance Corp. Ltd. (India) DIRECTOR_ELECTION, p=0.886, MOT før: bare tidligere år | Reelect Laya Madduri as Director | Board decisions that are particularly vulnerable to conflicts of interest should have additional safeguards. M
- 2048411|12 LOTTE Chemical Corp. (South Korea) DIRECTOR_ELECTION, p=0.898, MOT før: bare tidligere år | Elect Lee Young-jun as Inside Director | The board should exercise objective judgement on corporate affairs and be able to make decisions independently
- 2070191|6 S.F. Holding Co., Ltd. (China) AUDITOR, p=0.901, MOT før: bare tidligere år | Approve PricewaterhouseCoopers Zhong Tian LLP and PricewaterhouseCoopers Respectively as t | The external auditor should act in an independent manner. We will consider the auditor’s independence and any 
- 2069803|6 S.F. Holding Co., Ltd. (China) AUDITOR, p=0.901, MOT før: bare tidligere år | Approve PricewaterhouseCoopers Zhong Tian LLP and PricewaterhouseCoopers Respectively as t | The external auditor should act in an independent manner. We will consider the auditor’s independence and any 
- 2101346|3 Voltamp Transformers Limited (India) DIRECTOR_ELECTION, p=0.901, MOT før: nei | Reelect Kanubhai S. Patel as Director | The board should exercise objective judgement on corporate affairs and be able to make decisions independently
- 2085864|3 PT Barito Renewables Energy Tbk (Indonesia) AUDITOR, p=0.907, MOT før: nei | Approve Auditors | The external auditor should act in an independent manner. We will consider the auditor’s independence and any 
