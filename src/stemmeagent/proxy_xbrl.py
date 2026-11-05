"""Point-in-time pay data from each meeting's OWN proxy statement (DEF 14A).

Why not the XBRL frames/companyconcept API: it keeps only non-dimensional facts from a
company's latest filing. Many companies tag CEO pay per named individual
(ecd:IndividualAxis), especially in a year with a CEO change, and the API then has
nothing (Snowflake, Signet) or only the newest year (Linde, VF). The API also serves
values from proxies filed AFTER the meeting.

Here, for every issuer x meeting we take the latest DEF 14A filed in the 200 days up to
the meeting, read its XBRL instance (<doc>_htm.xml) and extract the Pay-versus-Performance
table. The numbers are exactly what shareholders saw before voting, so there is no
look-ahead, and cumulative TSR values for consecutive years share one base.

For a year with several CEOs (PEOs), `peo_sct_total` is the largest individual package
(usually the newcomer's sign-on award) and `n_peo` > 1 flags the CEO change.
"""
from __future__ import annotations

import concurrent.futures as cf
from collections import defaultdict

import pandas as pd
from lxml import etree

from . import sec

PROXY_FORM = "DEF 14A"
MAX_PROXY_AGE_DAYS = 200
EARLIEST_NEEDED = "2023-01-01"
_XBRLI = "http://www.xbrl.org/2003/instance"
_XBRLDI = "http://xbrl.org/2006/xbrldi"

PVP_CONCEPTS = {
    "PeoTotalCompAmt": "peo_sct",
    "PeoActuallyPaidCompAmt": "peo_cap",
    "NonPeoNeoAvgTotalCompAmt": "neo_avg_sct",
    "NonPeoNeoAvgCompActuallyPaidAmt": "neo_avg_cap",
    "TotalShareholderRtnAmt": "tsr",
    "PeerGroupTotalShareholderRtnAmt": "peer_tsr",
    "CoSelectedMeasureAmt": "co_selected_amt",
}


def proxy_filings(cik: int) -> list[dict]:
    """DEF 14A filings of `cik` since 2023 (follows older submission pages if needed)."""
    d = sec.get_json(f"https://data.sec.gov/submissions/CIK{cik:010d}.json")
    blocks = [d["filings"]["recent"]]
    recent_dates = d["filings"]["recent"]["filingDate"]
    if recent_dates and min(recent_dates) > EARLIEST_NEEDED:
        for extra in d["filings"].get("files", []):
            if extra.get("filingTo", "9999") >= EARLIEST_NEEDED:
                blocks.append(sec.get_json(f"https://data.sec.gov/submissions/{extra['name']}"))
    out = []
    for b in blocks:
        for form, acc, fdate, doc in zip(b["form"], b["accessionNumber"], b["filingDate"], b["primaryDocument"]):
            if form == PROXY_FORM and fdate >= EARLIEST_NEEDED:
                out.append({"accession": acc, "filing_date": fdate, "primary_doc": doc})
    return sorted(out, key=lambda r: r["filing_date"])


def choose_proxy(proxies: list[dict], meeting_date: pd.Timestamp) -> dict | None:
    lo = (meeting_date - pd.Timedelta(days=MAX_PROXY_AGE_DAYS)).strftime("%Y-%m-%d")
    hi = meeting_date.strftime("%Y-%m-%d")
    cands = [p for p in proxies if lo <= p["filing_date"] <= hi]
    return cands[-1] if cands else None


def instance_bytes(cik: int, accession: str, primary_doc: str) -> tuple[bytes | None, str | None]:
    base = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession.replace('-', '')}"
    stem = primary_doc.rsplit("/", 1)[-1].rsplit(".", 1)[0]
    url = f"{base}/{stem}_htm.xml"
    try:
        return sec.get(url), url
    except FileNotFoundError:
        pass
    try:
        idx = sec.get_json(f"{base}/index.json")
    except FileNotFoundError:
        return None, None
    names = [i["name"] for i in idx["directory"]["item"]]
    pick = [n for n in names if n.endswith("_htm.xml")] or [
        n for n in names if n.endswith(".xml") and n != "FilingSummary.xml"
        and not n.endswith(("_cal.xml", "_def.xml", "_lab.xml", "_pre.xml"))]
    if not pick:
        return None, None
    url = f"{base}/{pick[0]}"
    return sec.get(url), url


def parse_pvp(xml_bytes: bytes) -> pd.DataFrame:
    """One row per fiscal period in the Pay-versus-Performance table."""
    root = etree.fromstring(xml_bytes, parser=etree.XMLParser(huge_tree=True, recover=True))
    ctx = {}
    for c in root.iter(f"{{{_XBRLI}}}context"):
        p = c.find(f"{{{_XBRLI}}}period")
        if p is None:
            continue
        start = p.findtext(f"{{{_XBRLI}}}startDate")
        end = p.findtext(f"{{{_XBRLI}}}endDate") or p.findtext(f"{{{_XBRLI}}}instant")
        dims = tuple(sorted((m.get("dimension", "").split(":")[-1], (m.text or "").split(":")[-1])
                            for m in c.iter(f"{{{_XBRLDI}}}explicitMember")))
        ctx[c.get("id")] = (start, end, dims)

    vals: dict = defaultdict(dict)       # (end) -> {(col, member): value}
    names: dict = defaultdict(set)       # end -> PEO names
    starts: dict = {}
    for el in root:
        if not isinstance(el.tag, str):
            continue
        q = etree.QName(el)
        if "/ecd/" not in (q.namespace or "") and not (q.localname == "NetIncomeLoss" and "us-gaap" in (q.namespace or "")):
            continue
        c = ctx.get(el.get("contextRef"))
        if c is None or not c[1]:
            continue
        start, end, dims = c
        other_dims = [d for d in dims if d[0] != "IndividualAxis"]
        if other_dims:
            continue  # e.g. adjustment breakdowns; keep table-level facts only
        member = next((m for a, m in dims if a == "IndividualAxis"), "")
        if q.localname == "PeoName":
            names[end].add((el.text or "").strip())
            continue
        col = PVP_CONCEPTS.get(q.localname) or ("net_income_pvp" if q.localname == "NetIncomeLoss" else None)
        if col is None:
            continue
        try:
            v = float((el.text or "").replace(",", ""))
        except ValueError:
            continue
        sign = -1.0 if el.get("sign") == "-" else 1.0
        vals[end][(col, member)] = sign * v
        starts.setdefault(end, start)

    rows = []
    for end, d in vals.items():
        row = {"period_end": end, "period_start": starts.get(end)}
        peo = {m: v for (c, m), v in d.items() if c == "peo_sct"}
        if peo:
            top = max(peo, key=peo.get)
            row["peo_sct"] = peo[top]
            row["n_peo"] = len([m for m in peo if m]) or 1
            row["peo_cap"] = d.get(("peo_cap", top), d.get(("peo_cap", "")))
        for col in ("neo_avg_sct", "neo_avg_cap", "tsr", "peer_tsr", "co_selected_amt", "net_income_pvp"):
            v = d.get((col, ""))
            if v is not None:
                row[col] = v
        row["peo_names"] = "; ".join(sorted(n for n in names.get(end, ()) if n))
        rows.append(row)
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    df["period_end"] = pd.to_datetime(df["period_end"], errors="coerce")
    # Keep roughly annual periods only.
    df["period_start"] = pd.to_datetime(df["period_start"], errors="coerce")
    days = (df["period_end"] - df["period_start"]).dt.days
    df = df[(days.isna()) | ((days > 300) & (days < 430))]
    return df.sort_values("period_end").reset_index(drop=True)


def features_for_meeting(cik: int, meeting_date: pd.Timestamp) -> dict:
    out: dict = {"cik": cik, "meeting_date": meeting_date}
    try:
        proxies = proxy_filings(cik)
    except FileNotFoundError:
        out["proxy_status"] = "no_submissions"
        return out
    p = choose_proxy(proxies, meeting_date)
    if p is None:
        out["proxy_status"] = "no_def14a_in_window"
        return out
    out.update({"proxy_accession": p["accession"], "proxy_filing_date": p["filing_date"],
                "proxy_url": f"https://www.sec.gov/Archives/edgar/data/{cik}/{p['accession'].replace('-', '')}/{p['primary_doc']}"})
    xml, url = instance_bytes(cik, p["accession"], p["primary_doc"])
    if xml is None:
        out["proxy_status"] = "no_xbrl"
        return out
    out["proxy_xbrl_url"] = url
    t = parse_pvp(xml)
    if t.empty or "tsr" not in t and "peo_sct" not in t:
        out["proxy_status"] = "no_pvp_table"
        return out
    t = t[t["period_end"] <= meeting_date]
    if t.empty:
        out["proxy_status"] = "no_pvp_before_meeting"
        return out
    cur = t.iloc[-1]
    prev = t.iloc[-2] if len(t) > 1 else None
    out["proxy_status"] = "ok"
    out["pvp_fy_end"] = cur["period_end"]
    for col in ("peo_sct", "peo_cap", "n_peo", "neo_avg_sct", "neo_avg_cap", "tsr", "peer_tsr",
                "co_selected_amt", "net_income_pvp", "peo_names"):
        if col in cur and pd.notna(cur[col]):
            out[col] = cur[col]
        if prev is not None and col in prev and pd.notna(prev[col]) and col != "peo_names":
            out[f"{col}_prev"] = prev[col]
    return out


def build(sop: pd.DataFrame, workers: int = 4, progress_every: int = 200) -> pd.DataFrame:
    todo = sop.dropna(subset=["cik"])[["cik", "meeting_date"]].drop_duplicates()
    todo = [(int(c), pd.Timestamp(d)) for c, d in todo.itertuples(index=False)]
    rows = []
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(features_for_meeting, c, d): (c, d) for c, d in todo}
        for i, fut in enumerate(cf.as_completed(futs), 1):
            c, d = futs[fut]
            try:
                rows.append(fut.result())
            except Exception as e:  # keep going; record the failure
                rows.append({"cik": c, "meeting_date": d, "proxy_status": f"error: {type(e).__name__}: {e}"[:200]})
            if i % progress_every == 0:
                print(f"    proxies {i}/{len(todo)}", flush=True)
    return pd.DataFrame(rows)
