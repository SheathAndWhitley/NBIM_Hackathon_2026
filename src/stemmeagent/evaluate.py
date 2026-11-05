"""Metrics for the AGAINST (MOT) class, with cluster-bootstrap confidence intervals.

Why these metrics: ~10% of say-on-pay votes are AGAINST, so accuracy rewards a
system that never says MOT (~90%). What matters for the decision (which proposals
an analyst must look at) is how many AGAINST votes are caught (recall), how many
flags are wasted (precision / false positives per hit), how well the ranking works
under a fixed review budget, and whether the stated confidence can be trusted
(Brier score, calibration), because confidence decides the routing.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, brier_score_loss, roc_auc_score

BUDGETS = (0.10, 0.20, 0.30)


def binary_metrics(y, yhat) -> dict:
    y = np.asarray(y).astype(int)
    yhat = np.asarray(yhat).astype(int)
    tp = int(((yhat == 1) & (y == 1)).sum())
    fp = int(((yhat == 1) & (y == 0)).sum())
    fn = int(((yhat == 0) & (y == 1)).sum())
    tn = int(((yhat == 0) & (y == 0)).sum())
    n = len(y)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "n": n, "positives": int(y.sum()), "prevalence": y.mean() if n else 0.0,
        "flagged": tp + fp, "tp": tp, "fp": fp, "fn": fn, "tn": tn,
        "accuracy": (tp + tn) / n if n else 0.0,
        "precision": precision, "recall": recall, "f1": f1,
        "fp_per_tp": fp / tp if tp else float("inf"),
    }


def expected_hits_at_budget(y, score, budget: float) -> float:
    """Expected number of positives among the top `budget` share of proposals.

    Ties in `score` are broken at random (in expectation), so binary or constant
    baselines are not flattered or punished by an arbitrary sort order.
    """
    y = np.asarray(y).astype(int)
    s = np.asarray(score, dtype=float)
    k = int(round(budget * len(y)))
    if k <= 0:
        return 0.0
    df = pd.DataFrame({"y": y, "s": s}).groupby("s", sort=True)["y"].agg(["size", "sum"])
    df = df.iloc[::-1]  # highest score first
    taken, hits = 0, 0.0
    for size, pos in zip(df["size"], df["sum"]):
        if taken + size <= k:
            taken += size
            hits += pos
        else:
            hits += pos * (k - taken) / size
            break
    return hits


def score_metrics(y, score, *, is_probability: bool = False) -> dict:
    y = np.asarray(y).astype(int)
    s = np.asarray(score, dtype=float)
    out = {"pr_auc": float(average_precision_score(y, s)) if y.any() else float("nan")}
    out["roc_auc"] = float(roc_auc_score(y, s)) if 0 < y.sum() < len(y) and len(np.unique(s)) > 1 else 0.5
    pos = y.sum()
    for b in BUDGETS:
        hits = expected_hits_at_budget(y, s, b)
        k = int(round(b * len(y)))
        out[f"recall@{int(b * 100)}%"] = hits / pos if pos else float("nan")
        out[f"precision@{int(b * 100)}%"] = hits / k if k else float("nan")
        out[f"missed_in_autoclear@{int(b * 100)}%"] = pos - hits
    if is_probability:
        out["brier"] = float(brier_score_loss(y, np.clip(s, 0, 1)))
    return out


def bootstrap_ci(frame: pd.DataFrame, metric_fn, *, cluster_col: str = "issuer_key",
                 n_boot: int = 2000, seed: int = 2026, alpha: float = 0.05) -> dict:
    """Cluster bootstrap: resample issuers (not rows), recompute `metric_fn(frame)`.

    `metric_fn` returns a dict of scalars; the result maps each key to (low, high).
    """
    rng = np.random.default_rng(seed)
    groups = frame.groupby(cluster_col).indices
    keys = np.array(list(groups.keys()), dtype=object)
    idx_lists = [groups[k] for k in keys]
    samples: dict[str, list[float]] = {}
    for _ in range(n_boot):
        pick = rng.integers(0, len(keys), len(keys))
        idx = np.concatenate([idx_lists[i] for i in pick])
        res = metric_fn(frame.iloc[idx])
        for k, v in res.items():
            if isinstance(v, (int, float, np.floating)) and np.isfinite(v):
                samples.setdefault(k, []).append(float(v))
    lo, hi = 100 * alpha / 2, 100 * (1 - alpha / 2)
    return {k: (float(np.percentile(v, lo)), float(np.percentile(v, hi))) for k, v in samples.items()}


def paired_bootstrap_diff(frame: pd.DataFrame, fn_a, fn_b, metric: str, *, cluster_col: str = "issuer_key",
                          n_boot: int = 2000, seed: int = 2026) -> dict:
    """Bootstrap the difference metric(A) - metric(B) on the same resampled issuers."""
    rng = np.random.default_rng(seed)
    groups = frame.groupby(cluster_col).indices
    keys = list(groups.keys())
    idx_lists = [groups[k] for k in keys]
    diffs = []
    for _ in range(n_boot):
        pick = rng.integers(0, len(keys), len(keys))
        sub = frame.iloc[np.concatenate([idx_lists[i] for i in pick])]
        a, b = fn_a(sub)[metric], fn_b(sub)[metric]
        if np.isfinite(a) and np.isfinite(b):
            diffs.append(a - b)
    d = np.array(diffs)
    return {"mean_diff": float(d.mean()), "ci_low": float(np.percentile(d, 2.5)),
            "ci_high": float(np.percentile(d, 97.5)), "p_le_0": float((d <= 0).mean())}
