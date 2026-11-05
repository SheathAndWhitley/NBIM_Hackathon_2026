"""The three baselines the model has to beat.

1. always_board   - vote as the board recommends (FOR on say-on-pay). The case's baseline.
2. persistence    - repeat NBIM's own previous say-on-pay vote at the same issuer
                    (strictly earlier meeting; no history -> FOR). Legitimate in
                    production: NBIM knows its own votes the moment it casts them.
3. rule_pay       - NBIM's published US rule: a stricter assessment of CEO packages worth
                    >= USD 20m (USD 25m from 2025) -> predict AGAINST above the threshold
                    in force at the meeting date.

Each returns (binary prediction, ranking score) aligned with `frame`'s index.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .config import rule_threshold


def always_board(frame: pd.DataFrame):
    zeros = pd.Series(0, index=frame.index)
    return zeros, zeros.astype(float)


def previous_vote(target: pd.DataFrame, history: pd.DataFrame, key: str = "issuer_key") -> pd.Series:
    """NBIM's most recent say-on-pay vote (1 = AGAINST) at the same issuer before each meeting.

    `history` may include `target` itself; only strictly earlier meetings are used.
    Returns NaN where there is no earlier vote.
    """
    h = history[[key, "meeting_date", "against"]].dropna(subset=[key]).sort_values("meeting_date")
    t = target[[key, "meeting_date"]].reset_index()
    t = t.sort_values("meeting_date")
    merged = pd.merge_asof(
        t, h.rename(columns={"meeting_date": "prev_meeting_date", "against": "prev_against"}),
        left_on="meeting_date", right_on="prev_meeting_date", by=key,
        allow_exact_matches=False, direction="backward",
    )
    return merged.set_index("index")["prev_against"].reindex(target.index)


def persistence(frame: pd.DataFrame, history: pd.DataFrame):
    prev = previous_vote(frame, history)
    pred = prev.fillna(0).astype(int)
    return pred, pred.astype(float)


def rule_pay(frame: pd.DataFrame, pay_col: str = "peo_sct_total"):
    pay = frame[pay_col]
    thr = frame["meeting_date"].map(rule_threshold)
    pred = (pay >= thr).astype(int)                    # missing pay -> FOR
    score = np.log10(pay.clip(lower=1)).fillna(0.0)    # rank by pay level
    return pred, score
