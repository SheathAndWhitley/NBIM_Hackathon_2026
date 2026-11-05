"""Feature table for the US say-on-pay deep dive. Every feature is point-in-time.

Pay data come from the Pay-versus-Performance table of the meeting's OWN proxy
statement (see proxy_xbrl.py): exactly what shareholders saw before voting. Size
and dilution come from the us-gaap XBRL frames with the 60-day rule (xbrl.py).

Grouped by the criteria NBIM states for its US say-on-pay assessment
("absolute value, peer comparisons and dilution"), plus performance and history:

  history     prev_against, has_history   NBIM's own previous SOP vote at the issuer
  absolute    log_peo_sct, pay_above_rule, peo_cap_ratio, peo_pay_growth, peo_missing
  one-off     ceo_change (several CEOs in the year -> sign-on awards, "golden hellos")
  peers       pay_pctile (vs all proxies one fiscal year earlier), ceo_neo_ratio, log_revenue
  performance tsr_1y, rel_tsr_1y, rel_tsr_cum, loss_maker
  dilution    dilution (growth in diluted share count)

Never used: managementRecommendation (mirrors the label), anything after the meeting.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import baselines, xbrl
from .config import rule_threshold

FEATURES = [
    "prev_against", "has_history",
    "log_peo_sct", "pay_above_rule", "peo_cap_ratio", "peo_pay_growth", "peo_missing",
    "ceo_change",
    "pay_pctile", "ceo_neo_ratio", "log_revenue",
    "tsr_1y", "rel_tsr_1y", "rel_tsr_cum", "loss_maker",
    "dilution",
]

FEATURE_LABELS = {
    "prev_against": "NBIM voted AGAINST last time",
    "has_history": "NBIM has voted on this company before",
    "log_peo_sct": "CEO total pay (log10 USD)",
    "pay_above_rule": "CEO pay above NBIM's US threshold (USD 20m; 25m from 2025)",
    "peo_cap_ratio": "Compensation actually paid / reported pay",
    "peo_pay_growth": "CEO pay growth vs prior year (log)",
    "peo_missing": "CEO pay not available",
    "ceo_change": "More than one CEO in the fiscal year",
    "pay_pctile": "CEO pay percentile among US proxies (prior year)",
    "ceo_neo_ratio": "CEO pay vs other executives (log ratio)",
    "log_revenue": "Revenue (log10 USD)",
    "tsr_1y": "1-year shareholder return",
    "rel_tsr_1y": "1-year return minus peer-group return",
    "rel_tsr_cum": "Multi-year return vs peer group (log ratio)",
    "loss_maker": "Net loss in fiscal year",
    "dilution": "Growth in diluted share count",
}

PROXY_COLS = ["proxy_status", "proxy_accession", "proxy_filing_date", "proxy_url", "pvp_fy_end", "peo_sct",
              "peo_sct_prev", "peo_cap", "n_peo", "peo_names", "neo_avg_sct", "tsr", "tsr_prev", "peer_tsr",
              "peer_tsr_prev", "net_income_pvp"]


def _safe_log_ratio(a, b, lo=-3.0, hi=3.0):
    with np.errstate(divide="ignore", invalid="ignore"):
        r = np.log(a / b)
    return r.where((a > 0) & (b > 0)).clip(lo, hi)


def pay_percentile(x: pd.DataFrame, proxy_ok: pd.DataFrame) -> pd.Series:
    """Percentile of CEO pay vs all proxies whose fiscal year ended one calendar year
    earlier (fully published before this company's meeting)."""
    ref = proxy_ok.dropna(subset=["peo_sct", "pvp_fy_end"]).copy()
    ref["fy"] = pd.to_datetime(ref["pvp_fy_end"]).dt.year
    dist = {y: np.sort(g["peo_sct"].values) for y, g in ref.groupby("fy")}
    out = []
    for v, end in zip(x["peo_sct_total"], x["pvp_fy_end"]):
        ref_year = pd.Timestamp(end).year - 1 if pd.notna(end) else None
        dd = dist.get(ref_year)
        out.append(np.searchsorted(dd, v, side="right") / len(dd) if pd.notna(v) and dd is not None and len(dd) else np.nan)
    return pd.Series(out, index=x.index)


def build(sop: pd.DataFrame, proxy: pd.DataFrame, history: pd.DataFrame | None = None,
          facts: pd.DataFrame | None = None) -> pd.DataFrame:
    """Return `sop` with raw evidence columns and model features appended."""
    history = sop if history is None else history
    x = sop.copy()
    x["prev_against"] = baselines.previous_vote(x, history)
    x["has_history"] = x["prev_against"].notna().astype(int)

    pr = proxy.copy()
    pr["meeting_date"] = pd.to_datetime(pr["meeting_date"])
    pr["cik"] = pr["cik"].astype("Int64")
    x["cik"] = x["cik"].astype("Int64")
    x = x.merge(pr[["cik", "meeting_date"] + [c for c in PROXY_COLS if c in pr.columns]],
                on=["cik", "meeting_date"], how="left")
    x["pvp_fy_end"] = pd.to_datetime(x["pvp_fy_end"])

    # us-gaap size/dilution facts, point-in-time (60-day rule)
    facts = xbrl.fact_table() if facts is None else facts
    pit = xbrl.point_in_time(x, facts[facts["column"].isin(["revenue", "net_income", "diluted_shares"])])
    pit.index = x.index
    for col in ("revenue", "net_income", "diluted_shares", "diluted_shares_prev"):
        x[col] = pit[col]

    x["peo_sct_total"] = x["peo_sct"]
    x["log_peo_sct"] = np.log10(x["peo_sct_total"].clip(lower=1e4))
    thr = x["meeting_date"].map(rule_threshold)
    x["rule_threshold"] = thr
    x["pay_above_rule"] = (x["peo_sct_total"] >= thr).astype(int)
    x["peo_missing"] = x["peo_sct_total"].isna().astype(int)
    x["peo_cap_ratio"] = (x["peo_cap"] / x["peo_sct_total"]).where(x["peo_sct_total"] > 0).clip(-2, 5)
    x["peo_pay_growth"] = _safe_log_ratio(x["peo_sct_total"], x["peo_sct_prev"], -2, 2)
    x["ceo_change"] = (x["n_peo"] > 1).astype(float).where(x["n_peo"].notna())
    x["pay_pctile"] = pay_percentile(x, pr[pr["proxy_status"] == "ok"])
    x["ceo_neo_ratio"] = _safe_log_ratio(x["peo_sct_total"], x["neo_avg_sct"], -1, 4)
    x["log_revenue"] = np.log10(x["revenue"].clip(lower=1e5))
    x["tsr_1y"] = (x["tsr"] / x["tsr_prev"] - 1).where(x["tsr_prev"] > 0).clip(-0.95, 3)
    peer_1y = (x["peer_tsr"] / x["peer_tsr_prev"] - 1).where(x["peer_tsr_prev"] > 0).clip(-0.95, 3)
    x["peer_tsr_1y"] = peer_1y
    x["rel_tsr_1y"] = (x["tsr_1y"] - peer_1y).clip(-2, 2)
    x["rel_tsr_cum"] = _safe_log_ratio(x["tsr"], x["peer_tsr"], -2, 2)
    ni = x["net_income_pvp"].fillna(x["net_income"])
    x["loss_maker"] = (ni < 0).astype(float).where(ni.notna())
    x["dilution"] = (x["diluted_shares"] / x["diluted_shares_prev"] - 1).where(x["diluted_shares_prev"] > 0).clip(-0.5, 1)
    return x
