# Patterns: the signals we use to predict a vote against the board

This file lists every signal ("pattern") the stemmeagent uses to predict whether
NBIM votes **against the board's recommendation**. It also says where each one is
computed, how much it matters, and how we keep it free of leakage.

There are two models, and they use different patterns:

| Model | Scope | Code | Test period |
|---|---|---|---|
| **Ballot model** (main result) | Every agenda item NBIM voted on (`ny_data/real_votes.csv`) | [ballot.py](src/stemmeagent/ballot.py), [ballot_model.py](src/stemmeagent/ballot_model.py) | 2025–26 |
| **Say-on-pay deep dive** | US say-on-pay votes from SEC N-PX | [features.py](src/stemmeagent/features.py), [model.py](src/stemmeagent/model.py) | season 2025–26 |

The LLM agent ([agent.py](src/stemmeagent/agent.py)) gets a subset of these patterns
in its case file (see section 6).

All numbers below come from `results/metrics.json`.

---

## 1. History: how NBIM voted at this company before

This is the strongest family of patterns. Votes are sticky: if NBIM opposed a
director or an item last year, it usually does so again.

| Pattern | Column | Meaning |
|---|---|---|
| **Voted down before, same item or same person** | `prev_same` → `prev_dev_yes` / `prev_dev_no` | NBIM's last vote on the same director (`prev_same_person`) or on the same recurring item (`prev_same_item`) at this company. 1 = deviated, 0 = followed the board, missing = never seen |
| Section cited last time | `prev_same_section` | The guideline section NBIM published with its earlier against vote. It goes to the agent, not to the model |
| Deviated at the last meeting | `prev_meeting_dev_yes` | Any deviation at this company's previous meeting |
| Company deviation rate | `hist_dev_rate`, `log_hist_n` | Share of earlier proposals at this company where NBIM deviated, smoothed towards the base rate (`PRIOR_STRENGTH = 5`) |
| Company × proposal-type rate | `hist_type_dev_rate`, `log_hist_type_n` | The same rate, limited to this proposal type (e.g. director elections at this company) |
| Any history at all | `has_history` | NBIM has voted at this company before |
| Previous say-on-pay vote | `prev_against` (say-on-pay model) | NBIM's previous say-on-pay vote at the same issuer |

**How items are matched across years**
- *Same item:* `item_key` lowercases the proposal text and strips digits and
  punctuation. "Approve Discharge … FY 2023" therefore matches the 2024 version.
- *Same person:* `person_key` pulls the director's name out of "Elect Director …"
  texts and sorts the name tokens, so "Tsuruha Jun" and "Jun Tsuruha" match.

**How strong it is**
- The persistence baseline, which only repeats the previous decision, reaches
  precision 0.64 and recall 0.40 on the 2025–26 ballot test set.
- When NBIM deviates again on the same item, it cites the same guideline section
  in 97% of cases.
- In the say-on-pay model, `prev_against` has the second-largest weight (+0.64).

**How it is used: the precedent rule.** The ballot model is a hybrid. If
`prev_same == 1`, the item is always flagged and ranked first
(`score = 1 + p`). All other items are ranked by the model's calibrated probability.

**Leakage guard.** History is updated only after a whole meeting has been processed,
so items in the same meeting never see each other's labels. Only strictly earlier
meetings count. The same lookup would work in production, because NBIM knows its own
past votes.

---

## 2. What the proposal is

| Pattern | Column | Notes |
|---|---|---|
| Proposal type | `proposal_type` | DIRECTOR_ELECTION, SAY_ON_PAY, EQUITY_PLAN, OTHER_BUSINESS and so on |
| Who proposed it | `proponent` | Management or Shareholder |
| Board's recommendation | `board_rec` | FOR / MOT / NONE |
| Proposal wording | `model_text` (TF-IDF, 1–2 word phrases) | Names and digits are removed first (see below) |

**Words and types that push towards MOT** (largest logistic-regression weights):
- `OTHER_BUSINESS` (+3.0). NBIM votes against blank-cheque "other business" items:
  12 of 12 in the test set.
- "board member", "member", "and member" (+2.4 to +2.7). These are slate or
  committee-member elections, typical of markets where NBIM pushes for independence.
- "**external**" (+1.7). External or non-independent directors and auditors.
- "amend", "system", "elect directors" (bundled slate), and rare proposal types
  (`infrequent_sklearn`, +2.6).

**Words that push towards FOR:** "fiscal year" (−4.4) and "year" (−3.9), which mark
routine annual items such as accounts, discharge and dividends. Also
`DIRECTOR_PAY` (−1.8) and "board for".

**Leakage guard: names and years are removed.** Without this step the TF-IDF model
learned individual names ("davis", "ichiro") and years ("fiscal 2018"). Person-level
history is handled explicitly by `prev_same_person` instead.

---

## 3. Company and meeting context

| Pattern | Column | Notes |
|---|---|---|
| Country | `country` | Mostly pushes towards FOR (Malaysia, UK, Hong Kong, Sri Lanka, Bermuda: −1.4 to −2.1). Several markets have little to oppose under NBIM's guidelines |
| Market | `market` | Developed or emerging |
| Agenda size | `log_meeting_n_items` | Number of items on the agenda |
| **Shareholder activity at the meeting** | `meeting_has_shp` | 1 if any shareholder proposal is on the agenda. This is a proxy for outside pressure on the company |

---

## 4. Pay (say-on-pay model only)

These patterns follow the criteria NBIM states for US say-on-pay ("absolute value,
peer comparisons and dilution"). They come from the Pay-versus-Performance table in
the **meeting's own proxy statement**, which shareholders saw before voting.

| Group | Pattern | Column | Weight |
|---|---|---|---|
| Absolute level | **CEO pay above NBIM's US threshold** (USD 20m; USD 25m from 2025) | `pay_above_rule` | **+0.85** (largest) |
| | CEO total pay (log) | `log_peo_sct` | +0.20 |
| | Pay growth vs prior year | `peo_pay_growth` | +0.43 |
| | Compensation actually paid / reported pay | `peo_cap_ratio` | ≈0 |
| | CEO pay missing | `peo_missing` | +0.11 |
| One-off awards | **CEO change** (more than one CEO in the year, i.e. sign-on awards) | `ceo_change` | +0.42 |
| Peers | Pay percentile among US proxies one year earlier | `pay_pctile` | +0.39 |
| | CEO pay vs other executives | `ceo_neo_ratio` | −0.10 |
| | Company size (revenue, log) | `log_revenue` | −0.35 |
| Performance | 1-year return | `tsr_1y` | −0.22 |
| | Return vs peers, 1-year and cumulative | `rel_tsr_1y`, `rel_tsr_cum` | ≈0 |
| | Net loss in the year | `loss_maker` | +0.08 |
| Dilution | Growth in diluted share count | `dilution` | −0.13 |

**Policy vs practice**
- NBIM opposed 54% of packages above the threshold and 2.9% of those below it.
- 74% of all against votes fall above the threshold.
- After a CEO change the against rate is 14.4%, against 8.6% without one.

**Leakage guard.** XBRL facts are used only if their fiscal period ended at least
60 days before the meeting (`PIT_MIN_LAG_DAYS`). Peer percentiles compare against
proxies from one fiscal year earlier, which were fully published before the meeting.

---

## 5. Patterns we deliberately do not use

| Field | Why not |
|---|---|
| `managementRecommendation` / file `mgmt_rec` on management proposals | Mirrors NBIM's vote. In `npx_votes.csv` it equals the vote on 2,538 management proposals |
| `rationale_text`, `rationale_section`, `position_paper` | Exist only for against votes, so they reveal the label |
| `nbim_vote*`, `against_board` | They are the label |
| Director names and years in the text | The model memorised them instead of learning general patterns |
| Anything dated after the meeting | Not known at decision time |
| External company data beyond SEC filings and NBIM's guidelines | Ruled out by the rules we work under |

---

## 6. What the LLM agent sees

[agent.py](src/stemmeagent/agent.py) `case_file()` gives Claude these items as
untrusted data:

- company, country, market, meeting date
- proposal text, proponent, board recommendation
- company history: "N earlier proposals, deviated on M" (`hist_n`, `hist_dev`)
- same item or director before: "NBIM voted against the board, citing GVG-…"
  (`prev_same`, `prev_same_section`)

It also gets the complete guideline edition in force at the meeting date. The triage
model's score is **not** shown to the LLM. It is used only by the router: any item
scoring at or above `t_review` goes to a human, together with deviations,
low-confidence answers, citations that fail verification and suspected injections.

---

## 7. Where the patterns fail (test set, 2025–26)

- **Director elections** hold 96 of the 169 deviations. The text carries little
  signal, so the model relies on history, and first-time nominees are hard to catch.
- **Equity plans, share issuance, financial statements and director pay:**
  0 of 8 deviations flagged. These depend on numbers (dilution, discount) that the
  ballot text does not contain.
- **First meeting at a company:** none of the history patterns exist, so only type,
  text and country remain.
