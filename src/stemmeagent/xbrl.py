"""Point-in-time XBRL facts: Pay-versus-Performance (ecd) and basic financials (us-gaap).

Source: SEC XBRL frames API, one request per concept and calendar period, e.g.
https://data.sec.gov/api/xbrl/frames/ecd/PeoTotalCompAmt/USD/CY2024.json

Point-in-time rule: for a meeting on date d, use the latest fiscal year whose period
ended on or before d - PIT_MIN_LAG_DAYS (60). That fiscal year's numbers are in the
proxy statement for that meeting; a later fiscal year can never be used.

Known caveats (declared limitations, checked in the audit):
  * The API serves each value from the company's LATEST filing that reports the period.
    Pay-versus-Performance tables repeat earlier years, so the value may come from a proxy
    filed after the meeting. Values are normally unchanged, but this is look-ahead in principle.
  * Cumulative TSR in a PvP table is measured from that table's first year, so the base
    differs between filings. Year-over-year TSR is only computed when both years come
    from the same filing (same accession number).
  * The API omits dimensional facts. Companies that tag CEO pay per named individual
    (common when the CEO changed) have no non-dimensional PeoTotalCompAmt -> missing.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import sec
from .config import PIT_MIN_LAG_DAYS

YEARS = range(2020, 2026)

# column -> (taxonomy, concept candidates in priority order, unit, kind)
CONCEPTS = {
    "peo_sct_total": ("ecd", ["PeoTotalCompAmt"], "USD", "duration"),
    "peo_cap": ("ecd", ["PeoActuallyPaidCompAmt"], "USD", "duration"),
    "neo_avg_sct": ("ecd", ["NonPeoNeoAvgTotalCompAmt"], "USD", "duration"),
    "neo_avg_cap": ("ecd", ["NonPeoNeoAvgCompActuallyPaidAmt"], "USD", "duration"),
    "tsr": ("ecd", ["TotalShareholderRtnAmt"], "USD", "duration"),
    "peer_tsr": ("ecd", ["PeerGroupTotalShareholderRtnAmt"], "USD", "duration"),
    "revenue": ("us-gaap", ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax"], "USD", "duration"),
    "net_income": ("us-gaap", ["NetIncomeLoss"], "USD", "duration"),
    "diluted_shares": ("us-gaap", ["WeightedAverageNumberOfDilutedSharesOutstanding"], "shares", "duration"),
    "assets": ("us-gaap", ["Assets"], "USD", "instant"),
}


def _frame_url(tax: str, concept: str, unit: str, kind: str, year: int) -> str:
    period = f"CY{year}" if kind == "duration" else f"CY{year}Q4I"
    return f"https://data.sec.gov/api/xbrl/frames/{tax}/{concept}/{unit}/{period}.json"


def fact_table(prefer_processed: bool = True) -> pd.DataFrame:
    """Long table: cik, column, start, end, val, accn (one row per company-period).

    Uses the committed extract data/processed/xbrl_facts_subset.csv when present
    (offline reproduction); otherwise reads the cached/live SEC frames.
    """
    from .config import DATA_PROCESSED
    extract = DATA_PROCESSED / "xbrl_facts_subset.csv"
    if prefer_processed and extract.exists():
        f = pd.read_csv(extract, parse_dates=["start", "end"])
        return f
    rows = []
    for col, (tax, concepts, unit, kind) in CONCEPTS.items():
        for priority, concept in enumerate(concepts):
            for y in YEARS:
                try:
                    data = sec.get_json(_frame_url(tax, concept, unit, kind, y))["data"]
                except FileNotFoundError:
                    continue
                for r in data:
                    rows.append((int(r["cik"]), col, priority, r.get("start"), r["end"], float(r["val"]), r["accn"]))
    f = pd.DataFrame(rows, columns=["cik", "column", "priority", "start", "end", "val", "accn"])
    f["end"] = pd.to_datetime(f["end"])
    f["start"] = pd.to_datetime(f["start"])
    # Prefer the first concept in the candidate list (e.g. Revenues before RevenueFromContract...).
    f = f.sort_values(["cik", "column", "end", "priority"]).drop_duplicates(["cik", "column", "end"])
    return f.drop(columns="priority").reset_index(drop=True)


def point_in_time(target: pd.DataFrame, facts: pd.DataFrame) -> pd.DataFrame:
    """For each row of target (cik, meeting_date): values for fiscal year t and t-1.

    Returns columns <col>, <col>_prev, <col>_accn, <col>_prev_accn, fy_end, per concept.
    """
    t = target[["cik", "meeting_date"]].copy()
    t["row"] = np.arange(len(t))
    t = t.dropna(subset=["cik"])
    t["cik"] = t["cik"].astype("int64")
    t["cutoff"] = t["meeting_date"] - pd.Timedelta(days=PIT_MIN_LAG_DAYS)
    out = pd.DataFrame({"row": np.arange(len(target))})

    # Fiscal-year anchor: the PvP year (tsr is the most widely reported PvP fact).
    for col in CONCEPTS:
        fc = facts[facts["column"] == col][["cik", "end", "val", "accn"]].sort_values("end")
        cur = pd.merge_asof(t.sort_values("cutoff"), fc.rename(columns={"end": "fy_end"}),
                            left_on="cutoff", right_on="fy_end", by="cik", direction="backward")
        # Fiscal year t must be recent: ended within ~15 months before the meeting.
        stale = (cur["meeting_date"] - cur["fy_end"]).dt.days > 455
        cur.loc[stale, ["val", "accn", "fy_end"]] = np.nan
        cur["prev_cutoff"] = cur["fy_end"] - pd.Timedelta(days=300)
        has = cur["prev_cutoff"].notna()
        prev = pd.merge_asof(cur[has].sort_values("prev_cutoff")[["row", "cik", "prev_cutoff", "fy_end"]],
                             fc.rename(columns={"end": "prev_end", "val": "prev_val", "accn": "prev_accn"}),
                             left_on="prev_cutoff", right_on="prev_end", by="cik", direction="backward")
        gap = (prev["fy_end"] - prev["prev_end"]).dt.days
        prev.loc[(gap < 300) | (gap > 430), ["prev_val", "prev_accn"]] = np.nan
        cur = cur.merge(prev[["row", "prev_val", "prev_accn"]], on="row", how="left")
        cur = cur.set_index("row")
        out[col] = cur["val"].reindex(out["row"]).values
        out[f"{col}_prev"] = cur["prev_val"].reindex(out["row"]).values
        out[f"{col}_accn"] = cur["accn"].reindex(out["row"]).values
        out[f"{col}_prev_accn"] = cur["prev_accn"].reindex(out["row"]).values
        out[f"{col}_fy_end"] = cur["fy_end"].reindex(out["row"]).values
    return out.drop(columns="row")
