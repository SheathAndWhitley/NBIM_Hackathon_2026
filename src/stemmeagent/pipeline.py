"""End-to-end evaluation: full ballot (main result) and the US say-on-pay deep dive."""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import ballot, ballot_model as bm, baselines, dataset, features, model, xbrl
from .config import DATA_PROCESSED, N_BOOTSTRAP, RANDOM_SEED, TEST_SEASON, TRAIN_SEASON
from .evaluate import binary_metrics, bootstrap_ci, paired_bootstrap_diff, score_metrics

KEY_METRICS = ["accuracy", "precision", "recall", "f1", "pr_auc", "recall@10%", "recall@20%", "recall@30%",
               "fp_per_tp", "flagged", "tp", "fp", "fn"]


def _metrics(y, pred, score, prob=False):
    return binary_metrics(y, pred) | score_metrics(y, score, is_probability=prob)


def reliability(y, p, bins=(0, .02, .05, .1, .2, .35, .5, .75, 1.0001)) -> list[dict]:
    df = pd.DataFrame({"y": y, "p": p})
    df["bin"] = pd.cut(df["p"], bins, right=False)
    g = df.groupby("bin", observed=True).agg(n=("y", "size"), predicted=("p", "mean"), observed=("y", "mean"))
    return [{"bin": str(i), **{k: float(v) for k, v in r.items()}} for i, r in g.iterrows()]


# --------------------------------------------------------------------------- ballot

def run_ballot(n_boot: int = N_BOOTSTRAP) -> tuple[dict, pd.DataFrame, bm.BallotModel]:
    d = bm.add_model_columns(ballot.load_real())
    lab = d[d["labelled"]]
    tr, va, te = (lab[lab["split"] == s].copy() for s in ("train", "valid", "test"))
    m = bm.fit_select(tr, va)
    te["p"] = m.predict_proba(te)
    te["score"] = m.score(te, te["p"].values)
    te["flag"] = (te["score"] >= m.t_flag).astype(int)
    te["review"] = (te["score"] >= m.t_review).astype(int)
    y = te["y"].values

    systems = {
        "always_board": bm.baseline_always_board(te),
        "persistence": bm.baseline_persistence(te),
        "type_majority": bm.baseline_type_majority(te, tr),
        "model_only": ((te["p"] >= m.t_flag_model).astype(int).values, te["p"].values),
        "hybrid": (te["flag"].values, te["score"].values),
    }
    res = {name: _metrics(y, pred, score) for name, (pred, score) in systems.items()}
    te["score_type_majority"] = systems["type_majority"][1]  # training-period type rates (for figures)
    res["hybrid"]["brier"] = float(np.mean((te["p"] - y) ** 2))
    res["hybrid"]["brier_constant_base_rate"] = float(np.mean((tr["y"].mean() - y) ** 2))

    # Confidence intervals: cluster bootstrap over meetings.
    te["cluster"] = te["meeting_id"].astype(str)
    hyb = lambda f: _metrics(f["y"].values, f["flag"].values, f["score"].values)
    per = lambda f: _metrics(f["y"].values, (f["prev_same"] == 1).astype(int).values,
                             (f["prev_same"] == 1).astype(float).values)
    ci = bootstrap_ci(te, hyb, cluster_col="cluster", n_boot=n_boot, seed=RANDOM_SEED)
    diff = {k: paired_bootstrap_diff(te, hyb, per, k, cluster_col="cluster", n_boot=n_boot, seed=RANDOM_SEED)
            for k in ("pr_auc", "recall@20%", "f1")}

    review = {"share_reviewed": float(te["review"].mean()), "caught": int(y[te["review"] == 1].sum()),
              "deviations": int(y.sum()), "missed_in_autoclear": int(y[te["review"] == 0].sum()),
              "auto_cleared": int((te["review"] == 0).sum())}
    by_type = (te.groupby("proposal_type")
                 .apply(lambda g: pd.Series({"n": len(g), "deviations": int(g["y"].sum()),
                                             "flagged": int(g["flag"].sum()), "tp": int((g["y"] * g["flag"]).sum()),
                                             "caught_in_review": int((g["y"] * g["review"]).sum()),
                                             "share_reviewed": float(g["review"].mean())}), include_groups=False)
                 .sort_values("deviations", ascending=False))
    by_year = {int(yr): _metrics(g["y"].values, g["flag"].values, g["score"].values)
               for yr, g in te.groupby(te["meeting_date"].dt.year)}
    out = {
        "split": {s: {"n": int(len(f)), "deviations": int(f["y"].sum()), "rate": float(f["y"].mean())}
                  for s, f in (("train 2019-23", tr), ("valid 2024", va), ("test 2025-26", te))},
        "model_selection_valid_pr_auc": m.selection, "selected": m.name,
        "thresholds": {"t_flag_hybrid": m.t_flag, "t_review_hybrid": m.t_review, "t_flag_model_only": m.t_flag_model},
        "test": {k: {mk: res[k][mk] for mk in KEY_METRICS} for k in res},
        "test_hybrid_brier": {"model": res["hybrid"]["brier"], "constant": res["hybrid"]["brier_constant_base_rate"]},
        "test_hybrid_ci95": {k: ci[k] for k in ("precision", "recall", "f1", "pr_auc", "recall@20%") if k in ci},
        "test_hybrid_minus_persistence": diff,
        "review_queue": review,
        "by_type": by_type.reset_index().to_dict("records"),
        "by_year": {y_: {k: v[k] for k in ("precision", "recall", "f1", "pr_auc")} for y_, v in by_year.items()},
        "reliability": reliability(y, te["p"].values),
        "top_features": bm.top_text_features(m, 12).reset_index().rename(columns={"index": "feature"}).to_dict("records"),
    }
    return out, te, m


# --------------------------------------------------------------------------- say-on-pay

def run_sop(n_boot: int = N_BOOTSTRAP) -> tuple[dict, pd.DataFrame]:
    votes = dataset.load_votes()
    imap = pd.read_csv(DATA_PROCESSED / "issuer_cik_map.csv", dtype={"cusip": str})
    sop = dataset.sop_table(votes, imap[["cusip", "cik", "cik_match_method"]])
    proxy = pd.read_csv(DATA_PROCESSED / "proxy_pvp.csv")
    X = features.build(sop, proxy, facts=xbrl.fact_table())
    tr, te = X[X["season"] == TRAIN_SEASON].copy(), X[X["season"] == TEST_SEASON].copy()
    tm = model.fit_triage(tr, features.FEATURES)
    te["p"] = tm.predict_proba(te)
    te["flag"] = (te["p"] >= tm.t_flag).astype(int)
    te["review"] = (te["p"] >= tm.t_review).astype(int)
    y = te["against"].values
    systems = {"always_board": baselines.always_board(te), "persistence": baselines.persistence(te, X),
               "nbim_pay_rule": baselines.rule_pay(te), "model": (te["flag"].values, te["p"].values)}
    res = {k: _metrics(y, np.asarray(p), np.asarray(s)) for k, (p, s) in systems.items()}
    res["model"]["brier"] = float(np.mean((te["p"] - y) ** 2))
    mfn = lambda f: _metrics(f["against"].values, f["flag"].values, f["p"].values)
    rfn = lambda f: _metrics(f["against"].values, *map(np.asarray, baselines.rule_pay(f)))
    ci = bootstrap_ci(te, mfn, cluster_col="issuer_key", n_boot=n_boot, seed=RANDOM_SEED)
    diff = {k: paired_bootstrap_diff(te, mfn, rfn, k, cluster_col="issuer_key", n_boot=n_boot, seed=RANDOM_SEED)
            for k in ("pr_auc", "recall@20%", "f1")}
    contrib = tm.contributions(te) if tm.kind == "logreg" else None
    coef = None
    if tm.kind == "logreg":
        clf, imp = tm.model.named_steps["clf"], tm.model.named_steps["impute"]
        names = list(tm.features) + [f"{tm.features[i]} (missing)" for i in imp.indicator_.features_]
        coef = dict(sorted(zip(names, clf.coef_[0].round(3)), key=lambda kv: -abs(kv[1])))
    above = te[te["peo_missing"] == 0]
    out = {
        "data": {"seasons": X.groupby("season")["against"].agg(["size", "sum", "mean"]).round(4).to_dict("index"),
                 "proxy_status": proxy["proxy_status"].value_counts().to_dict(),
                 "feature_coverage_test": te[features.FEATURES].notna().mean().round(3).to_dict()},
        "selected": tm.describe() | {"oof_calibrated": None},
        "test": {k: {mk: res[k][mk] for mk in KEY_METRICS} for k in res},
        "test_model_brier": res["model"]["brier"],
        "test_model_ci95": {k: ci[k] for k in ("precision", "recall", "f1", "pr_auc", "recall@20%") if k in ci},
        "test_model_minus_nbim_rule": diff,
        "policy_vs_practice": {
            "against_rate_above_threshold": float(above.loc[above["pay_above_rule"] == 1, "against"].mean()),
            "n_above_threshold": int((above["pay_above_rule"] == 1).sum()),
            "against_rate_below_threshold": float(above.loc[above["pay_above_rule"] == 0, "against"].mean()),
            "share_of_against_votes_above_threshold": float(above.loc[above["against"] == 1, "pay_above_rule"].mean()),
            "against_rate_ceo_change": float(te.loc[te["ceo_change"] == 1, "against"].mean()),
            "against_rate_no_ceo_change": float(te.loc[te["ceo_change"] == 0, "against"].mean()),
        },
        "coefficients": coef,
        "review_queue": {"share_reviewed": float(te["review"].mean()), "caught": int(y[te["review"] == 1].sum()),
                         "against": int(y.sum())},
    }
    if contrib is not None:
        te = te.join(contrib.add_prefix("contrib_"))
    return out, te
