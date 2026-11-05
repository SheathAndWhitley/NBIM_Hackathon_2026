"""Triage model for the full ballot: P(NBIM deviates from the board | proposal, history).

Protocol (walk-forward, no random splits):
  * fit on 2019-2023 (train)
  * choose hyperparameters and model family on 2024 (valid) by PR-AUC
  * fit an isotonic calibrator and the thresholds on the 2024 predictions
  * evaluate once on 2025-2026 (test)

Baselines: always with the board (the case baseline), persistence (repeat NBIM's
previous decision on the same item/person at the same company) and proposal-type
majority (deviate where NBIM deviated on most proposals of this type in training).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

from .config import RANDOM_SEED
from .model import f1_threshold, recall_threshold

CAT = ["proposal_type", "proponent", "market", "country", "board_rec"]
NUM = ["log_hist_n", "hist_dev_rate", "log_hist_type_n", "hist_type_dev_rate", "prev_dev_yes", "prev_dev_no",
       "prev_meeting_dev_yes", "has_history", "log_meeting_n_items", "meeting_has_shp"]
TEXT = "model_text"  # proposal text without names and digits (see ballot.model_text)
REVIEW_RECALL = 0.90


def add_model_columns(d: pd.DataFrame) -> pd.DataFrame:
    d = d.copy()
    d["log_hist_n"] = np.log1p(d["hist_n"])
    d["log_hist_type_n"] = np.log1p(d["hist_type_n"])
    d["prev_dev_yes"] = (d["prev_same"] == 1).astype(int)
    d["prev_dev_no"] = (d["prev_same"] == 0).astype(int)
    d["prev_meeting_dev_yes"] = (d["prev_meeting_any_dev"] == 1).astype(int)
    d["log_meeting_n_items"] = np.log1p(d["meeting_n_items"])
    return d


def make_logreg(C: float, class_weight):
    pre = ColumnTransformer([
        ("txt", TfidfVectorizer(ngram_range=(1, 2), min_df=3, max_features=30000, sublinear_tf=True), TEXT),
        ("cat", OneHotEncoder(handle_unknown="ignore", min_frequency=20), CAT),
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("sc", StandardScaler())]), NUM),
    ])
    return Pipeline([("pre", pre), ("clf", LogisticRegression(C=C, class_weight=class_weight, max_iter=4000))])


def make_gbm():
    pre = ColumnTransformer([
        ("cat", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1, encoded_missing_value=-1), CAT),
        ("num", "passthrough", NUM),
    ])
    clf = HistGradientBoostingClassifier(max_depth=4, learning_rate=0.05, max_iter=300, l2_regularization=1.0,
                                         min_samples_leaf=40, categorical_features=list(range(len(CAT))),
                                         random_state=RANDOM_SEED)
    return Pipeline([("pre", pre), ("clf", clf)])


@dataclass
class BallotModel:
    """Precedent-first hybrid.

    Rule 1 (precedent): NBIM deviated on the same item/person at the same company at an
    earlier meeting -> flag. (NBIM then cites the same guideline section in 97% of cases.)
    Rule 2 (model): otherwise the calibrated probability ranks the proposal.
    score = 1 + p for precedent cases (always ranked first), else p.
    """
    name: str
    pipeline: Pipeline
    calibrator: IsotonicRegression
    t_flag: float       # on the hybrid score, chosen for F1 on the validation year
    t_review: float     # on the hybrid score, catches REVIEW_RECALL on the validation year
    t_flag_model: float
    selection: list[dict]

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        return self.calibrator.predict(self.pipeline.predict_proba(X)[:, 1])

    def raw_proba(self, X: pd.DataFrame) -> np.ndarray:
        return self.pipeline.predict_proba(X)[:, 1]

    def score(self, X: pd.DataFrame, p: np.ndarray | None = None) -> np.ndarray:
        p = self.predict_proba(X) if p is None else p
        return np.where((X["prev_same"] == 1).values, 1.0 + p, p)


def fit_select(train: pd.DataFrame, valid: pd.DataFrame) -> BallotModel:
    ytr, yva = train["y"].values, valid["y"].values
    candidates = [(f"logreg(C={C},cw={cw})", lambda C=C, cw=cw: make_logreg(C, cw))
                  for C in (0.3, 1.0, 3.0) for cw in (None, "balanced")]
    candidates.append(("gbm(structured only)", make_gbm))
    results, best = [], None
    for name, factory in candidates:
        pipe = factory().fit(train, ytr)
        p = pipe.predict_proba(valid)[:, 1]
        ap = float(average_precision_score(yva, p))
        results.append({"model": name, "valid_pr_auc": ap})
        if best is None or ap > best[2]:
            best = (name, pipe, ap, p)
    name, pipe, _, p_valid = best
    cal = IsotonicRegression(out_of_bounds="clip", y_min=0.0, y_max=1.0).fit(p_valid, yva)
    pc = cal.predict(p_valid)
    hv = np.where((valid["prev_same"] == 1).values, 1.0 + pc, pc)
    return BallotModel(name, pipe, cal, f1_threshold(yva, hv), recall_threshold(yva, hv, REVIEW_RECALL),
                       f1_threshold(yva, pc), results)


# --- baselines ----------------------------------------------------------------

def baseline_always_board(frame: pd.DataFrame):
    z = np.zeros(len(frame))
    return z.astype(int), z


def baseline_persistence(frame: pd.DataFrame):
    pred = (frame["prev_same"] == 1).astype(int).values
    return pred, pred.astype(float)


def baseline_type_majority(frame: pd.DataFrame, train: pd.DataFrame):
    rates = train.groupby("proposal_type")["y"].mean()
    score = frame["proposal_type"].map(rates).fillna(train["y"].mean()).values
    return (score > 0.5).astype(int), score


def top_text_features(model: BallotModel, k: int = 15) -> pd.DataFrame:
    """Largest positive/negative logistic-regression weights (global explanation)."""
    if not model.name.startswith("logreg"):
        return pd.DataFrame()
    pre, clf = model.pipeline.named_steps["pre"], model.pipeline.named_steps["clf"]
    names = pre.get_feature_names_out()
    w = pd.Series(clf.coef_[0], index=names).sort_values()
    return pd.concat([w.tail(k)[::-1].rename("weight").to_frame().assign(direction="towards MOT"),
                      w.head(k).rename("weight").to_frame().assign(direction="towards FOR")])
