"""NBIM's own proxy votes from SEC Form N-PX (Norges Bank, CIK 1374170).

Since the 2024 reporting year, institutional managers that file 13F must report
their say-on-pay votes in structured XML on Form N-PX. Norges Bank files one
N-PX per year (period 1 July - 30 June), with the votes in ProxyVotingTable.xml.

Differences from the starter kit's hent_npx.py:
  * reads every N-PX filing, not just the newest;
  * takes the vote from <howVoted> (<voteRecord> is a container);
  * keeps one row per <proxyTable> (the starter emitted junk rows for container nodes);
  * classifies the proposal type from the proposal TEXT, never from the vote itself.

LEAKAGE WARNING: <managementRecommendation> in NBIM's filing mirrors NBIM's own vote
(it says AGAINST on 412 of 414 AGAINST votes, although a board always recommends FOR
on its own say-on-pay). It is kept as `mgmt_rec_raw` for the leakage demonstration only
and must never be used as a feature.
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET

import pandas as pd

from . import sec
from .config import DATA_PROCESSED, NBIM_CIK, SEASONS

FREQUENCY_VOTES = {"ONE YEAR", "TWO YEARS", "THREE YEARS"}
AGAINST_VOTES = {"AGAINST", "WITHHOLD"}  # the case's MOT definition; ABSTAIN is not a vote against

# Proposal-type detection from the ballot text (available before the vote).
_FREQ_RE = re.compile(
    r"frequen|how often|future\s+(stockholder\s+|shareholder\s+)?advisory\s+votes|every\s+(one|two|three|1|2|3)\s*[- ]?\s*years?|"
    r"one,?\s*two,?\s*or\s*three|1,?\s*2,?\s*or\s*3|annual(ly)?,?\s*biennial|"
    r"(one|1|two|2|three|3)[- ]years?\s*(,|or)",
    re.I,
)
_PARACHUTE_RE = re.compile(r"golden parachute|change[- ]in[- ]control|merger[- ]related|"
                           r"in connection with the (merger|transaction|acquisition)", re.I)


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def list_filings(cik: int = NBIM_CIK) -> list[dict]:
    """All N-PX filings for `cik` (from the cached EDGAR submissions API)."""
    data = sec.get_json(f"https://data.sec.gov/submissions/CIK{cik:010d}.json")
    blocks = [data["filings"]["recent"]]
    for extra in data["filings"].get("files", []):
        blocks.append(sec.get_json(f"https://data.sec.gov/submissions/{extra['name']}"))
    out = []
    for b in blocks:
        for form, acc, fdate, rdate in zip(b["form"], b["accessionNumber"], b["filingDate"], b["reportDate"]):
            if form in ("N-PX", "N-PX/A"):
                out.append({"form": form, "accession": acc, "filing_date": fdate, "period_end": rdate})
    out.sort(key=lambda r: (r["period_end"], r["filing_date"]))
    return out


def vote_table_url(accession: str, cik: int = NBIM_CIK) -> str:
    acc = accession.replace("-", "")
    idx = sec.get_json(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/index.json")
    names = [i["name"] for i in idx["directory"]["item"]]
    tables = [n for n in names if n.lower().endswith(".xml") and n.lower() != "primary_doc.xml"]
    if not tables:
        raise ValueError(f"No vote table XML in {accession}: {names}")
    tables.sort(key=lambda n: ("proxyvotingtable" not in n.lower(), n))
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/{tables[0]}"


def parse_vote_table(xml_bytes: bytes) -> list[dict]:
    """One dict per <proxyTable> element."""
    root = ET.fromstring(xml_bytes)
    rows = []
    for pt in root:
        if _local(pt.tag) != "proxyTable":
            continue
        rec: dict = {}
        categories: list[str] = []
        votes: list[dict] = []
        for child in pt:
            name = _local(child.tag)
            if name == "voteCategories":
                categories = [(c.text or "").strip() for c in child.iter() if _local(c.tag) == "categoryType"]
            elif name == "vote":
                for vr in child:
                    votes.append({_local(x.tag): (x.text or "").strip() for x in vr})
            elif len(child) == 0:
                rec[name] = (child.text or "").strip()
        how = sorted({v.get("howVoted", "") for v in votes if v.get("howVoted")})
        mrec = sorted({v.get("managementRecommendation", "") for v in votes if v.get("managementRecommendation")})
        rows.append({
            "issuer_name": rec.get("issuerName", ""),
            "cusip": rec.get("cusip", ""),
            "isin": rec.get("isin", ""),
            "meeting_date_raw": rec.get("meetingDate", ""),
            "vote_description": rec.get("voteDescription", ""),
            "vote_categories": "|".join(categories),
            "vote_source": rec.get("voteSource", ""),
            "n_vote_records": len(votes),
            "how_voted": "|".join(how),
            "mgmt_rec_raw": "|".join(mrec),  # LEAKS THE LABEL - never a feature
        })
    return rows


def classify_proposal(description: str) -> str:
    """Proposal type from the ballot text only: 'frequency', 'parachute' or 'sop'."""
    if _FREQ_RE.search(description or ""):
        return "frequency"
    if _PARACHUTE_RE.search(description or ""):
        return "parachute"
    return "sop"


def _season_for(period_end: str) -> str:
    for label, end in SEASONS.items():
        if end == period_end:
            return label
    y = int(period_end[:4])
    return f"{y - 1}-{str(y)[2:]}"


def build_votes(save: bool = True) -> pd.DataFrame:
    filings = list_filings()
    if any(f["form"] == "N-PX/A" for f in filings):
        print("  NOTE: N-PX/A amendments present - check whether they restate or add votes.")
    frames = []
    for f in filings:
        url = vote_table_url(f["accession"])
        rows = parse_vote_table(sec.get(url))
        df = pd.DataFrame(rows)
        df["season"] = _season_for(f["period_end"])
        df["accession"] = f["accession"]
        df["filing_date"] = f["filing_date"]
        df["source_url"] = url
        frames.append(df)
    votes = pd.concat(frames, ignore_index=True)

    votes["meeting_date"] = pd.to_datetime(votes["meeting_date_raw"], format="%m/%d/%Y")
    votes["proposal_type"] = votes["vote_description"].map(classify_proposal)
    votes["voted"] = votes["how_voted"].ne("")
    votes["split_vote"] = votes["how_voted"].str.contains("|", regex=False)
    votes["against"] = votes["how_voted"].isin(AGAINST_VOTES).astype(int)

    # Sanity check: the text-based type must agree with the vote's form (years vs FOR/AGAINST).
    freq_vote = votes["how_voted"].isin(FREQUENCY_VOTES)
    mismatch = votes["voted"] & (freq_vote != votes["proposal_type"].eq("frequency"))
    votes["type_mismatch"] = mismatch
    votes = votes.sort_values(["meeting_date", "issuer_name", "cusip"]).reset_index(drop=True)
    votes.insert(0, "vote_id", [f"{s}-{i:05d}" for i, s in enumerate(votes["season"])])

    if save:
        DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
        votes.to_csv(DATA_PROCESSED / "sec_nbim_npx_sop.csv", index=False)
    return votes


if __name__ == "__main__":
    v = build_votes()
    print(v.groupby(["season", "proposal_type"]).size())
