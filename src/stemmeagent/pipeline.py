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


def citation_baselines(d: pd.DataFrame, te_dev: pd.DataFrame) -> dict:
    """Simple citation rules, scored against NBIM's published section on the test deviations.

    type_majority: the section NBIM cited most often for this proposal type in training.
    previous_section: the section NBIM cited when it deviated on the same item/person before.
    previous_section_else_type: previous section where it exists, otherwise type majority.
    These are the numbers the LLM agent's citations must beat.
    """
    gvg = lambda s: s.astype(str).str.startswith("GVG")
    tr = d[(d["split"] == "train") & d["labelled"] & (d["y"] == 1) & gvg(d["rationale_section"])]
    prior = tr.groupby("proposal_type")["rationale_section"].agg(lambda s: s.value_counts().index[0])
    t = te_dev[gvg(te_dev["rationale_section"])].copy()
    truth = t["rationale_section"]
    chap = lambda s: s.astype(str).str.extract(r"GVG (\d)")[0]
    cite_type = t["proposal_type"].map(prior)
    cite_prev = t["prev_same_section"].where(t["prev_same_section"].notna())
    combo = cite_prev.where(cite_prev.notna(), cite_type)

    def score(c):
        return {"exact_section": float((c == truth).mean()), "same_chapter": float((chap(c) == chap(truth)).mean()),
                "coverage": float(c.notna().mean())}
    has_prev = cite_prev.notna()
    return {"n_test_deviations_with_section": int(len(t)), "type_majority": score(cite_type),
            "previous_section": score(cite_prev), "previous_section_else_type": score(combo),
            "previous_section_accuracy_when_present": float((cite_prev[has_prev] == truth[has_prev]).mean())
            if has_prev.any() else None}


def hit_breakdown(te: pd.DataFrame) -> dict:
    """Where the model's hits come from (cases with vs without NBIM precedent), and the cold-start case."""
    prec = (te["prev_same"] == 1).values
    y, flag, rev = te["y"].values == 1, te["flag"].values == 1, te["review"].values == 1
    missed = te[y & ~rev]
    return {
        "precedent_cases": int(prec.sum()),
        "precedent_cases_that_deviated": int((prec & y).sum()),
        "model_flags": int(flag.sum()), "model_hits": int((flag & y).sum()),
        "hits_with_precedent": int((flag & y & prec).sum()),
        "hits_without_precedent": int((flag & y & ~prec).sum()),
        "precedent_cases_flagged": int((flag & prec).sum()),
        "deviations_without_precedent": int((y & ~prec).sum()),
        "of_which_flagged_by_model": int((y & ~prec & flag).sum()),
        "of_which_caught_in_review": int((y & ~prec & rev).sum()),
        "deviations_nbim_followed_board_last_time": int((y & (te["prev_same"] == 0).values).sum()),
        "deviations_never_seen_before": int((y & te["prev_same"].isna().values).sum()),
        "missed_in_autoclear_by_type": missed["proposal_type"].value_counts().to_dict(),
        "deviations_by_country_top": te.loc[y, "country"].value_counts().head(6).to_dict(),
    }


def triage_injection(te: pd.DataFrame, m) -> dict:
    """Adversarial test for the triage model (no API key needed).

    The model cannot 'obey' an instruction, but its TF-IDF text features can be moved by
    extra words. Each injection is appended to every test proposal; we measure how much the
    probability and the route change, and whether any real deviation is pushed from the
    analyst queue to auto-clearance (the harmful direction).
    """
    from .agent_eval import INJECTIONS
    base_p, base_rev = te["p"].values, te["review"].values == 1
    y = te["y"].values == 1
    out = {}
    for name, text in INJECTIONS.items():
        x = te.copy()
        x["proposal_text"] = x["proposal_text"].astype(str) + " " + text
        x["model_text"] = [ballot.model_text(t, k) for t, k in zip(x["proposal_text"], x["person_key"])]
        p = m.predict_proba(x)
        rev = m.score(x, p) >= m.t_review
        out[name] = {"mean_abs_change_p": float(np.mean(np.abs(p - base_p))),
                     "max_abs_change_p": float(np.max(np.abs(p - base_p))),
                     "route_changed": int((rev != base_rev).sum()),
                     "deviations_moved_from_review_to_auto": int((base_rev & ~rev & y).sum()),
                     "share_reviewed_after": float(rev.mean()),
                     "deviations_caught_after": int((rev & y).sum())}
    return out


def rolling_validation(lab: pd.DataFrame, years=(2021, 2022, 2023, 2024), C: float = 3.0) -> list[dict]:
    """Rolling-origin check on the years BEFORE the test period: for each year, train on all
    earlier years and score that year. Compares the model with the rejected precedent-first
    variant and the persistence baseline, and shows whether performance drifts over time.
    The test years 2025-26 are not used here."""
    from sklearn.metrics import average_precision_score
    from .evaluate import expected_hits_at_budget
    rows = []
    year = lab["meeting_date"].dt.year
    for vy in years:
        tr, va = lab[year < vy], lab[year == vy]
        p = bm.make_logreg(C, None).fit(tr, tr["y"].values).predict_proba(va)[:, 1]
        y = va["y"].values
        prec = (va["prev_same"] == 1).values.astype(float)
        for name, sc in (("model", p), ("precedent_first_variant", bm.precedent_first(va, p)), ("persistence", prec)):
            rows.append({"year": int(vy), "system": name, "n": int(len(va)), "deviations": int(y.sum()),
                         "pr_auc": float(average_precision_score(y, sc)),
                         "recall@20%": float(expected_hits_at_budget(y, sc, 0.2) / y.sum()),
                         "recall@40%": float(expected_hits_at_budget(y, sc, 0.4) / y.sum())})
    return rows


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
    te["score"] = m.score(te, te["p"].values)          # = p (no hand-made override)
    te["flag"] = (te["score"] >= m.t_flag).astype(int)
    te["review"] = (te["score"] >= m.t_review).astype(int)
    y = te["y"].values

    systems = {
        "always_board": bm.baseline_always_board(te),
        "persistence": bm.baseline_persistence(te),
        "type_majority": bm.baseline_type_majority(te, tr),
        "model": (te["flag"].values, te["score"].values),
    }
    res = {name: _metrics(y, pred, score) for name, (pred, score) in systems.items()}
    te["score_type_majority"] = systems["type_majority"][1]  # training-period type rates (for figures)
    res["model"]["brier"] = float(np.mean((te["p"] - y) ** 2))
    res["model"]["brier_constant_base_rate"] = float(np.mean((tr["y"].mean() - y) ** 2))
    # Rejected variant, reported for transparency only (it was NOT chosen on the test set:
    # the choice was made on the validation years, see rolling_validation).
    pf = bm.precedent_first(te, te["p"].values)
    rejected = _metrics(y, (pf >= bm.f1_threshold(va["y"].values, bm.precedent_first(va, m.predict_proba(va)))).astype(int), pf)

    # Confidence intervals: cluster bootstrap over COMPANIES. History features tie the
    # proposals of one company together, so resampling meetings would give too-narrow intervals.
    te["cluster"] = te["company_id"].astype(str)
    mod = lambda f: _metrics(f["y"].values, f["flag"].values, f["score"].values)
    per = lambda f: _metrics(f["y"].values, (f["prev_same"] == 1).astype(int).values,
                             (f["prev_same"] == 1).astype(float).values)
    ci = bootstrap_ci(te, mod, cluster_col="cluster", n_boot=n_boot, seed=RANDOM_SEED)
    diff = {k: paired_bootstrap_diff(te, mod, per, k, cluster_col="cluster", n_boot=n_boot, seed=RANDOM_SEED)
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
        "rolling_validation": rolling_validation(lab[lab["split"] != "test"]),
        "rejected_variant_precedent_first_test": {k: rejected[k] for k in KEY_METRICS},
        "thresholds": {"t_flag": m.t_flag, "t_review": m.t_review},
        "test": {k: {mk: res[k][mk] for mk in KEY_METRICS} for k in res},
        "test_model_brier": {"model": res["model"]["brier"], "constant": res["model"]["brier_constant_base_rate"]},
        "test_model_ci95": {k: ci[k] for k in ("precision", "recall", "f1", "pr_auc", "recall@20%") if k in ci},
        "test_model_minus_persistence": diff,
        "review_queue": review,
        "by_type": by_type.reset_index().to_dict("records"),
        "by_year": {y_: {k: v[k] for k in ("precision", "recall", "f1", "pr_auc")} for y_, v in by_year.items()},
        "reliability": reliability(y, te["p"].values),
        "bootstrap_cluster": "company_id",
        "hit_breakdown": hit_breakdown(te),
        "citation_baselines": citation_baselines(d, te[te["y"] == 1]),
        "triage_injection": triage_injection(te, m),
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
    cik_match = {season: {("matched" if k else "unmatched"): {"n": int(g.size), "against_rate": float(g.mean())}
                          for k, g in grp.groupby(grp.index)}
                 for season, grp in ((s_, X.loc[X["season"] == s_].set_index(X.loc[X["season"] == s_, "cik"].notna())["against"])
                                     for s_ in sorted(X["season"].unique()))}
    out = {
        "data": {"seasons": X.groupby("season")["against"].agg(["size", "sum", "mean"]).round(4).to_dict("index"),
                 "proxy_status": proxy["proxy_status"].value_counts().to_dict(),
                 "feature_coverage_test": te[features.FEATURES].notna().mean().round(3).to_dict(),
                 "cik_match": cik_match},
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
