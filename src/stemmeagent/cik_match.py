"""Map N-PX issuers (name, CUSIP, ISIN) to SEC CIKs so XBRL pay data can be joined.

N-PX has no CIK. Candidates are the companies that report Pay-versus-Performance
XBRL (the universe that matters for features) plus SEC's company_tickers.json.

Matching cascade (method recorded per issuer):
  1. exact          - exact match on a normalized name (legal suffixes, punctuation removed)
  2. exact_nospace  - same, ignoring spaces ("V F CORP" == "VF Corporation")
  3. fuzzy          - rapidfuzz token_sort_ratio >= 97 (word order / punctuation only)
  4. openfigi       - optional (off by default): ISIN -> ticker -> CIK. It cannot recover
                      acquired companies, which are most of the unmatched issuers.
Unmatched issuers keep a CUSIP-based key; they lose XBRL features but keep the history
feature. The matched/unmatched AGAINST rates are reported to expose selection bias.
"""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

import pandas as pd
import requests
from rapidfuzz import fuzz, process

from . import sec
from .config import DATA_PROCESSED, DATA_RAW

PVP_FRAME_CONCEPTS = ["PeoTotalCompAmt", "NonPeoNeoAvgTotalCompAmt", "TotalShareholderRtnAmt"]
PVP_FRAME_YEARS = range(2020, 2026)

# Legal-form words only. Distinctive words ("bancorp", "trust") stay, or "First Bancorp"
# would collide with every "First ..." company. SEC state tags ("/DE/") are removed separately.
_SUFFIXES = (r"\b(incorporated|inc|corporation|corp|company|co|ltd|limited|plc|holdings?|group|"
             r"the|n\s?v|s\s?a|se|ag|lp|l\s?p|llc|class\s+[a-z]|common stock|ordinary shares?)\b")


def normalize(name: str) -> str:
    n = (name or "").lower().replace("&", " and ")
    n = re.sub(r"[/\\][a-z]{2,3}[/\\]?", " ", n)  # SEC state tags like "/DE/" or "\\DE"
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = re.sub(_SUFFIXES, " ", n)
    return re.sub(r"\s+", " ", n).strip()


def candidate_universe() -> pd.DataFrame:
    rows = []
    for concept in PVP_FRAME_CONCEPTS:
        for y in PVP_FRAME_YEARS:
            url = f"https://data.sec.gov/api/xbrl/frames/ecd/{concept}/USD/CY{y}.json"
            try:
                for r in sec.get_json(url)["data"]:
                    rows.append((int(r["cik"]), r["entityName"], "pvp"))
            except FileNotFoundError:
                pass
    tick = sec.get_json("https://www.sec.gov/files/company_tickers.json")
    for r in tick.values():
        rows.append((int(r["cik_str"]), r["title"], "tickers"))
    u = pd.DataFrame(rows, columns=["cik", "entity_name", "src"]).drop_duplicates(["cik", "entity_name"])
    u["norm"] = u["entity_name"].map(normalize)
    u["norm_ns"] = u["norm"].str.replace(" ", "", regex=False)
    u["has_pvp"] = u.groupby("cik")["src"].transform(lambda s: (s == "pvp").any())
    return u[u["norm"] != ""]


def _unique_lookup(u: pd.DataFrame, col: str) -> dict[str, int]:
    """norm -> cik, only where the normalized name points to exactly one CIK.

    Ties between several CIKs are broken in favour of PvP filers if exactly one is.
    """
    out = {}
    for key, grp in u.groupby(col):
        ciks = grp["cik"].unique()
        if len(ciks) == 1:
            out[key] = int(ciks[0])
        else:
            pvp = grp.loc[grp["has_pvp"], "cik"].unique()
            if len(pvp) == 1:
                out[key] = int(pvp[0])
    return out


def _openfigi(isins: list[str]) -> dict[str, str]:
    """ISIN -> ticker (US exchanges). Cached in data/raw/openfigi.json."""
    cache_file = DATA_RAW / "openfigi.json"
    cache = json.loads(cache_file.read_text()) if cache_file.exists() else {}
    todo = [i for i in isins if i and i not in cache]
    for start in range(0, len(todo), 10):
        batch = todo[start:start + 10]
        jobs = [{"idType": "ID_ISIN", "idValue": i, "exchCode": "US"} for i in batch]
        try:
            r = requests.post("https://api.openfigi.com/v3/mapping", json=jobs, timeout=30)
            if r.status_code == 429:
                time.sleep(60)
                r = requests.post("https://api.openfigi.com/v3/mapping", json=jobs, timeout=30)
            r.raise_for_status()
        except requests.RequestException as e:
            print(f"    OpenFIGI unavailable ({e}); skipping fallback")
            break
        for isin, res in zip(batch, r.json()):
            data = res.get("data") or []
            cache[isin] = data[0].get("ticker", "") if data else ""
        time.sleep(2.6)  # unauthenticated limit: 25 requests/minute
    cache_file.write_text(json.dumps(cache, indent=0, sort_keys=True))
    return cache


def match_issuers(votes: pd.DataFrame, use_openfigi: bool = False, save: bool = True) -> pd.DataFrame:
    issuers = (votes[["cusip", "isin", "issuer_name"]].drop_duplicates("cusip").reset_index(drop=True))
    u = candidate_universe()
    by_norm = _unique_lookup(u, "norm")
    by_ns = _unique_lookup(u, "norm_ns")
    pvp_names = u[u["has_pvp"]].drop_duplicates("norm")
    choices = dict(zip(pvp_names["norm"], pvp_names["cik"]))

    ciks, methods, scores = [], [], []
    for name in issuers["issuer_name"]:
        n = normalize(name)
        if n in by_norm:
            ciks.append(by_norm[n]); methods.append("exact"); scores.append(100.0)
            continue
        ns = n.replace(" ", "")
        if ns in by_ns:
            ciks.append(by_ns[ns]); methods.append("exact_nospace"); scores.append(100.0)
            continue
        best = process.extract(n, list(choices), scorer=fuzz.token_sort_ratio, limit=2)
        # >= 97: only word-order/punctuation variants ("SCHWAB CHARLES CORP"). A looser
        # threshold matched Akero Therapeutics to Keros Therapeutics (score 94).
        if best and best[0][1] >= 97 and (len(best) == 1 or best[0][1] - best[1][1] >= 3):
            ciks.append(int(choices[best[0][0]])); methods.append("fuzzy"); scores.append(best[0][1])
        else:
            ciks.append(None); methods.append(None); scores.append(None)
    issuers["cik"] = pd.array(ciks, dtype="Int64")
    issuers["cik_match_method"] = methods
    issuers["cik_match_score"] = scores

    if use_openfigi:
        missing = issuers["cik"].isna()
        tick_map = {r["ticker"].upper(): int(r["cik_str"])
                    for r in sec.get_json("https://www.sec.gov/files/company_tickers.json").values()}
        figi = _openfigi(issuers.loc[missing, "isin"].dropna().tolist())
        for i in issuers.index[missing]:
            t = figi.get(issuers.at[i, "isin"], "")
            if t and t.upper() in tick_map:
                issuers.at[i, "cik"] = tick_map[t.upper()]
                issuers.at[i, "cik_match_method"] = "openfigi"

    if save:
        issuers.to_csv(DATA_PROCESSED / "issuer_cik_map.csv", index=False)
    return issuers
