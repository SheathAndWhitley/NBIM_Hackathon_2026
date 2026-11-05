
## Step 0: What a "model" is here

A model is a formula that takes in a proposal and outputs a number between 0 and 1:

> **"How likely is it that NBIM votes against the board on this proposal?"**

Nobody writes that formula by hand. The computer **learns** it from examples where we already know the answer. That's called  *supervised learning* : you show it thousands of past cases with the correct answer, and it finds the patterns.

---

## Step 1: The examples (rows) and the answer (label)

Each row in `real_votes.csv` is one agenda item at one shareholder meeting. Our running example:

| Field            | Value                                                        |
| ---------------- | ------------------------------------------------------------ |
| Company          | Some Japanese company                                        |
| Proposal text    | "Elect John Smith as Director and Member of Audit Committee" |
| Type             | DIRECTOR_ELECTION                                            |
| Proposed by      | Management                                                   |
| Board recommends | FOR                                                          |
| NBIM voted       | MOT                                                          |

The **label** (what we want to predict) is called `y`:

* **y = 1:** NBIM voted differently from the board (MOT or AVSTÅ when the board said FOR, or the reverse).
* **y = 0:** NBIM followed the board.

Here, y = 1. About 5% of all rows have y = 1.

> **Jury version:** "Our target is: did NBIM deviate from the board's recommendation? That's the decision an analyst has to catch."

---

## Step 2: Splitting by time (so we never cheat)

A model must be tested on examples it has never seen. Otherwise it's like taking an exam you've already seen the answers to.

We split by  **date** :

| Period     | Proposals | Used for                                                    |
| ---------- | --------- | ----------------------------------------------------------- |
| 2019–2023 | 7,993     | **Training:** the model learns from these             |
| 2024       | 1,883     | **Validation:** choosing settings and thresholds      |
| 2025–2026 | 3,448     | **Test:** used once at the end to measure performance |

**Why not shuffle randomly?** The same director is re-elected every year. With a random split, the model could see John Smith in 2025 during training and then be "tested" on John Smith in 2023, i.e. it would use the future. The rules explicitly penalise this.

> **Jury version:** "We train on 2019–23, make every choice on 2024, and test once on 2025–26, exactly how it would be used in reality."

---

## Step 3: Turning a proposal into numbers ("features")

A formula can only work with numbers, so every proposal is converted into a long list of them. There are three kinds.

### 3a. The text → word counts (called "TF-IDF")

* The text is split into words and word pairs: "elect", "director", "and member", "audit committee"…
* Each gets a number: how present it is in this text, weighted up if the word is **rare** across all proposals. Words like "the" or "approve" appear everywhere and tell us little; "audit committee" is more specific.
* **We remove person names and numbers first.** The first version learned that "Davis" or "2018" meant "vote against": pure memorisation that fails on new years and can't be explained. Now the text becomes "PERSON Elect as Director and Member of Audit Committee".

### 3b. Categories → yes/no columns (called "one-hot encoding")

Proposal type, who proposed it, market (developed/emerging), country and the board's recommendation each become 0/1 columns. For example, "is_type_DIRECTOR_ELECTION = 1", "is_country_Japan = 1".

### 3c. NBIM's history at this company → numbers

These are computed  **only from earlier meetings** :

| Feature                                    | Meaning                                                                          |
| ------------------------------------------ | -------------------------------------------------------------------------------- |
| How many earlier proposals                 | How well we know this company                                                    |
| Deviation rate at the company              | How often NBIM went against this board before                                    |
| Deviation rate for this type               | E.g. for director elections specifically                                         |
| **Same item/person before**          | Did NBIM go against *this same director / this same recurring item* last time? |
| Deviated at the last meeting               | Any against-vote at the company's previous meeting                               |
| Agenda size, shareholder proposals present | Context about the meeting                                                        |

**Smoothing.** A company where NBIM voted on one item and deviated once would show a 100% deviation rate, which is misleading. So we blend it towards the overall average: (deviations + 5 × average) / (proposals + 5). Small companies stay near the average; companies with lots of history show their real rate.

**Leakage protection:**

* History is updated only *after* a whole meeting is processed, so items at the same meeting can't see each other's answers.
* NBIM's rationale text and GVG section are never used as inputs. They only exist when NBIM voted against, so they would give away the answer.

> **Jury version:** "The model sees the proposal text without names, its type and country, and NBIM's own earlier votes at that company, never anything from after the meeting."

---

## Step 4: The formula itself (logistic regression)

Every feature gets a  **weight** : a positive weight pushes towards "against", a negative one towards "follow the board". For each proposal the model:

1. Multiplies each feature by its weight and **adds them all up** to get a score.
2. Squashes the score into 0–1 with an S-shaped curve (the "logistic function"): big positive score → near 1, big negative → near 0.

Real weights from our trained model:

| Feature                            | Weight                  | What it means                                 |
| ---------------------------------- | ----------------------- | --------------------------------------------- |
| Type = "Transact other business"   | **+3.0**          | NBIM always opposes unspecified items         |
| Words "board member", "and member" | **+2.7 / +2.2**   | Committee membership → independence concerns |
| Word "amend"                       | **+2.1**          | Changes to company articles                   |
| Words "fiscal year"                | **−4.4**         | Routine annual items → follow the board      |
| Country = Malaysia / UK            | **−2.1 / −1.7** | NBIM rarely deviates there                    |
| Type = DIRECTOR_PAY                | **−1.8**         | Board fees are rarely opposed                 |

**"Training"** means the computer tries millions of small weight adjustments until its predictions match the 2019–23 outcomes as closely as possible.

**Regularisation (the setting "C").** Without a limit, the model could give huge weights to rare words and memorise the training data. C controls how large weights may grow. We tried C = 0.3, 1 and 3.

> **Jury version:** "It's a logistic regression: every input gets a weight, and they add up to a probability. We chose it because every weight can be read and explained, which matters when a human must be able to overrule a recommendation."

---

## Step 5: Choosing the settings (on 2024 only)

We trained seven candidates on 2019–23 and scored each on 2024 by **PR-AUC** (ranking quality, explained in Step 9):

| Candidate                                            | PR-AUC on 2024           |
| ---------------------------------------------------- | ------------------------ |
| Logistic regression, C = 0.3                         | 0.44                     |
| Logistic regression, C = 1                           | 0.46                     |
| **Logistic regression, C = 3**                 | **0.50 ← chosen** |
| Same, with "balanced" class weights (three variants) | 0.42–0.45               |
| Gradient boosting (decision trees, no text)          | 0.44                     |

The winner was picked by the computer from this table. The 2025–26 test data was never involved.

---

## Step 6: Calibration (making the probabilities honest)

The raw output can be "overconfident": when it says 30%, maybe only 20% of such cases are deviations. We fix this with  **isotonic calibration** :

* On 2024, we look at what *actually* happened at each predicted level.
* We learn a correction curve that maps the raw output to the real frequency.

Afterwards, "30%" really means about 30%. We checked this on the test set (`ballot_calibration.png`): the points lie close to the diagonal.

**Why it matters:** the confidence decides what goes to a human. If confidence can't be trusted, the routing can't either.

---

## Step 7: The precedent rule (the "hybrid")

The strongest pattern in NBIM's data:  **if NBIM went against the same director or the same recurring item before, it usually does so again** , and for the same reason 97% of the time. So the final score is:

* **Precedent exists:** flag it and put it at the top of the list.
* **Otherwise:** use the model's probability.

This beat both the model alone and "same as last time" alone.

---

## Step 8: From a probability to an action (thresholds)

Two cut-off values, both chosen on 2024:

| Threshold        | Value | Rule                                                            | Purpose                                                   |
| ---------------- | ----- | --------------------------------------------------------------- | --------------------------------------------------------- |
| **Flag**   | 0.44  | Score ≥ 0.44 (or precedent) → "NBIM will likely vote against" | The yes/no prediction; chosen to give the best F1 on 2024 |
| **Review** | 0.03  | Score ≥ 0.03 → an analyst reads it                            | Chosen so that 90% of 2024's deviations would be caught   |

The review threshold is very low on purpose. Missing a deviation is worse than an analyst reading an extra proposal. On 2025–26 this sends 38% of proposals to an analyst and catches 84% of deviations.

---

## Step 9: How we measure it

Every test prediction falls into one of four boxes:

|                         | NBIM really deviated  | NBIM followed the board |
| ----------------------- | --------------------- | ----------------------- |
| **We flagged it** | ✅ True positive (78) | ❌ False alarm (54)     |
| **We didn't**     | ❌ Missed (91)        | ✅ Correct (3,225)      |

From those boxes:

* **Accuracy:** correct / all = 95.8%. Useless on its own, since "always follow the board" gets 95.1%.
* **Precision:** of our flags, how many were right? 78 / 132 =  **59%** .
* **Recall:** of real deviations, how many did we catch? 78 / 169 =  **46%** .
* **F1:** a combined score of precision and recall, from 0 to 1.  **0.52** .
* **PR-AUC:** how good the *ordering* is across all possible thresholds. Random is 0.05; we get  **0.44** .
* **Recall @ 20%:** read the 20% riskiest, and the share of deviations found is  **72%** .
* **Confidence interval (bootstrap).** We re-sampled the test meetings 2,000 times and recomputed the result each time. Our improvement over "same as last time" stays between +0.12 and +0.20 in PR-AUC, so it's not luck.

---

## Step 10: Likely technical questions, with short answers

| Question                                             | Answer                                                                                                                                                              |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Why not accuracy?*                                | "Always follow the board" scores 95% and catches nothing. We measure what matters: recall and precision on the deviations.                                          |
| *How do you avoid data leakage?*                   | Time split; history from earlier meetings only; no rationale columns; names and years removed; every choice made on 2024; test used once.                           |
| *Why logistic regression, not something advanced?* | It was best on 2024, beating gradient boosting, and every weight is explainable. The rules reward honest, explainable models over complex ones.                     |
| *Why does precision look low (59%)?*               | Deviations are rare (5%). Random flags would be right 5% of the time; ours are right 59% of the time.                                                               |
| *What does it miss?*                               | Cases that depend on facts not in the text, like board independence, attendance or overboarding. That data isn't in the dataset, and it's our "one more week" item. |
| *Would you put it in production?*                  | As a sorting tool with a human deciding: yes, tested first alongside analysts for one season. As an automatic voter: no.                                            |
| *What is the baseline?*                            | Three: always follow the board, same as last time, and the most common outcome per proposal type. We beat all three.                                                |

---

**The whole model in one breath:** "Every proposal is turned into numbers: its words, its type and country, and NBIM's own history at the company. A logistic regression adds weighted features into a calibrated probability of NBIM going against the board. Earlier deviations on the same director go straight to the top. Analysts read everything above a low threshold, which is 38% of proposals, and catch 84% of NBIM's against-votes."

If any step is still unclear, tell me which number it is and I'll explain that one with another example.
