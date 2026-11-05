"""The modelling table: one row per issuer x meeting with a say-on-pay (SOP) approval vote.

Unit of analysis: issuer x meeting. In 10 cases NBIM's N-PX lists two SOP rows for the
same issuer and meeting (share classes, or separate pay votes per executive); they are
collapsed and the meeting counts as AGAINST if any of its SOP rows was voted AGAINST.

Target: `against` = 1 if NBIM voted AGAINST/WITHHOLD/ABSTAIN. The board always
recommends FOR on its own SOP proposal, so this is exactly "NBIM deviates from the board".
"""
from __future__ import annotations

import pandas as pd

from .config import DATA_PROCESSED


def load_votes() -> pd.DataFrame:
    return pd.read_csv(DATA_PROCESSED / "sec_nbim_npx_sop.csv", parse_dates=["meeting_date"],
                       dtype={"cusip": str, "isin": str})


def sop_table(votes: pd.DataFrame, issuer_map: pd.DataFrame | None = None) -> pd.DataFrame:
    df = votes[(votes["proposal_type"] == "sop") & votes["voted"]].copy()
    df["cusip6"] = df["cusip"].str[:6]
    if issuer_map is not None:
        df = df.merge(issuer_map, on="cusip", how="left")
        # One identifier per company across seasons: SEC CIK when matched, else CUSIP issuer code.
        df["issuer_key"] = df["cik"].map(lambda c: f"CIK{int(c)}" if pd.notna(c) else None)
        df["issuer_key"] = df["issuer_key"].fillna("CUSIP6-" + df["cusip6"])
    else:
        df["issuer_key"] = "CUSIP6-" + df["cusip6"]

    agg = {
        "vote_id": "first", "season": "first", "issuer_name": "first", "cusip": "first",
        "isin": "first", "vote_description": "first", "how_voted": lambda s: "|".join(sorted(set(s))),
        "against": "max", "mgmt_rec_raw": lambda s: "|".join(sorted(set(s.dropna()))),
        "accession": "first", "source_url": "first",
    }
    for col in ("cik", "cik_match_method"):
        if col in df.columns:
            agg[col] = "first"
    out = (df.groupby(["issuer_key", "meeting_date"], as_index=False)
             .agg(agg)
             .sort_values(["meeting_date", "issuer_key"])
             .reset_index(drop=True))
    out["n_sop_rows"] = df.groupby(["issuer_key", "meeting_date"]).size().values
    return out
