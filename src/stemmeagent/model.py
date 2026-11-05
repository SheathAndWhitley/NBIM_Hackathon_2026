"""Triage model: P(NBIM votes AGAINST | point-in-time evidence).

Protocol (all choices made on the training season only):
  1. Out-of-fold (OOF) predictions on the training season with date-blocked folds
     (contiguous blocks of meeting dates, so a fold is a stretch of the calendar).
  2. Pick the model family (logistic regression vs gradient boosting) by OOF PR-AUC.
  3. Fit an isotonic calibrator on the OOF predictions -> trustworthy probabilities.
  4. Choose thresholds on the calibrated OOF predictions:
       t_flag   : maximises F1 (used for the binary MOT recommendation)
       t_review : lowest threshold that still catches >= REVIEW_RECALL of AGAINST votes
                  (everything above goes to an analyst; below is auto-cleared as FOR)
  5. Refit on the whole training season, apply to the test season once.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, precision_recall_curve
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from .config import RANDOM_SEED

N_FOLDS = 5
REVIEW_RECALL = 0.90


def make_model(kind: str):
    if kind == "logreg":
        return Pipeline([
            ("impute", SimpleImputer(strategy="median", add_indicator=True)),
            ("scale", StandardScaler()),
            ("clf", LogisticRegression(C=0.5, max_iter=2000)),
        ])
    if kind == "gbm":
        return HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, max_iter=250,
                                              l2_regularization=1.0, min_samples_leaf=30,
                                              random_state=RANDOM_SEED)
    raise ValueError(kind)


def date_blocks(dates: pd.Series, k: int = N_FOLDS) -> np.ndarray:
    """Fold id per row: k contiguous blocks of (roughly) equal size in meeting-date order."""
    order = np.argsort(dates.values, kind="stable")
    folds = np.empty(len(dates), dtype=int)
    folds[order] = np.minimum((np.arange(len(dates)) * k) // len(dates), k - 1)
    return folds


def oof_predict(kind: str, X: pd.DataFrame, y: np.ndarray, folds: np.ndarray) -> np.ndarray:
    p = np.zeros(len(y))
    for f in np.unique(folds):
        tr, va = folds != f, folds == f
        m = make_model(kind).fit(X[tr], y[tr])
        p[va] = m.predict_proba(X[va])[:, 1]
    return p


def f1_threshold(y, p) -> float:
    prec, rec, thr = precision_recall_curve(y, p)
    f1 = np.where(prec + rec > 0, 2 * prec * rec / (prec + rec + 1e-12), 0)[:-1]
    return float(thr[np.argmax(f1)])


def recall_threshold(y, p, target: float) -> float:
    pos = np.sort(p[y == 1])[::-1]
    k = int(np.ceil(target * len(pos)))
    return float(pos[k - 1]) if k >= 1 else 1.0


@dataclass
class TriageModel:
    kind: str
    features: list[str]
    model: object
    calibrator: IsotonicRegression
    t_flag: float
    t_review: float
    selection: dict

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        raw = self.model.predict_proba(X[self.features])[:, 1]
        return self.calibrator.predict(raw)

    def contributions(self, X: pd.DataFrame) -> pd.DataFrame:
        """Per-feature contribution to the log-odds (logistic regression only).

        Contribution = coefficient x standardized value; the missing-value indicators
        are folded into the feature they belong to. Sum + intercept = model log-odds.
        """
        if self.kind != "logreg":
            raise ValueError("contributions are defined for the logistic regression")
        imp, sc, clf = self.model.named_steps["impute"], self.model.named_steps["scale"], self.model.named_steps["clf"]
        Z = sc.transform(imp.transform(X[self.features]))
        names = list(self.features) + [self.features[i] for i in imp.indicator_.features_]
        contrib = Z * clf.coef_[0]
        df = pd.DataFrame(contrib, index=X.index, columns=range(len(names)))
        out = pd.DataFrame(index=X.index)
        for j, n in enumerate(names):
            out[n] = out.get(n, 0) + df[j]
        return out

    def describe(self) -> dict:
        return {"kind": self.kind, "t_flag": self.t_flag, "t_review": self.t_review, **self.selection}


def fit_triage(train: pd.DataFrame, features: list[str], target: str = "against") -> TriageModel:
    X, y = train[features], train[target].values.astype(int)
    folds = date_blocks(train["meeting_date"])
    oof = {k: oof_predict(k, X, y, folds) for k in ("logreg", "gbm")}
    ap = {k: float(average_precision_score(y, v)) for k, v in oof.items()}
    # Prefer the transparent model unless the GBM is clearly better (> 0.02 PR-AUC).
    kind = "gbm" if ap["gbm"] > ap["logreg"] + 0.02 else "logreg"
    cal = IsotonicRegression(out_of_bounds="clip", y_min=0.0, y_max=1.0).fit(oof[kind], y)
    p_cal = cal.predict(oof[kind])
    t_flag = f1_threshold(y, p_cal)
    t_review = recall_threshold(y, p_cal, REVIEW_RECALL)
    model = make_model(kind).fit(X, y)
    selection = {"oof_pr_auc": ap, "chosen": kind, "n_train": int(len(y)), "pos_train": int(y.sum()),
                 "review_share_train": float((p_cal >= t_review).mean()),
                 "oof_calibrated": p_cal.tolist()}
    return TriageModel(kind, list(features), model, cal, t_flag, t_review, selection)
