"""Felles kjennetegn per forslag-id for Case 1 (smed, #1958).

Leser BARE <split>/train.csv og <split>/test_input.csv. fasit.csv åpnes aldri.
Historikk-kolonner bruker bare train-rader med moetedato strengt før radens egen dato,
så test-rader ser hele train (alt før grensedato) og train-rader ser bare fortiden.

Bruk: python3 -I lag_kjennetegn.py ../data [../data_v3 ...]  -> <split>/kjennetegn.csv
"""
import re
import sys
from pathlib import Path

import pandas as pd

MILJO_SOSIAL = re.compile(r"ENVIRONMENT|SOCIAL|HUMAN RIGHTS|DIVERSITY", re.I)
TXT = {
    "styrevalg": re.compile(r"\belect|\bdirector nominee|re-elect", re.I),
    "revisor": re.compile(r"auditor|accounting firm|\baudit", re.I),
    "lonn": re.compile(r"compensation|say[- ]on[- ]pay|incentive|equity plan|stock plan|purchase plan|remuneration", re.I),
    "kapital": re.compile(r"authorized (common )?shares|reverse (stock )?split|issuance|issue shares|merger|acquisition|share repurchase|capital", re.I),
}


def forslagstype(kat, kilde, tekst):
    kat = str(kat or "").upper()
    tekst = str(tekst or "")
    if str(kilde).upper() == "SECURITY HOLDER":
        return "aksjonaer_miljo_sosial" if MILJO_SOSIAL.search(kat) else "aksjonaer_styring"
    if "DIRECTOR ELECTIONS" in kat:
        return "styrevalg"
    if "SAY-ON-PAY" in kat or kat.startswith("COMPENSATION"):
        return "lonn"
    if "AUDIT" in kat:
        return "revisor"
    if "CAPITAL STRUCTURE" in kat or "EXTRAORDINARY" in kat:
        return "kapital"
    for navn, rx in TXT.items():  # kategori mangler/er vag: falle tilbake på teksten
        if rx.search(tekst):
            return navn
    return "annet"


def undertype(ftype, tekst):
    t = str(tekst or "").lower()
    if ftype != "lonn":
        return ""
    if re.search(r"frequency|every (one|two|three)|one year|three years", t):
        return "frekvens"
    if re.search(r"merger|golden parachute|in connection with|transaction", t):
        return "fallskjerm"
    if re.search(r"plan", t):
        return "aksjeplan"
    return "say_on_pay"


def historikk(train, alle, nokkel, prefiks):
    tr = train[train["fasit"].isin(["FOR", "MOT", "AVSTÅ"])].copy()
    tr["_mot"] = (tr["fasit"] == "MOT").astype(int)
    tr["_avvik"] = tr["avvik"].fillna(0).astype(int)
    tr["_n"] = 1
    tr["_d"] = pd.to_datetime(tr["moetedato"]).astype("datetime64[ns]")
    g = tr.groupby(nokkel + ["_d"])[["_n", "_mot", "_avvik"]].sum().reset_index().sort_values("_d")
    c = g.groupby(nokkel)[["_n", "_mot", "_avvik"]].cumsum()
    g[["n", "mot", "avvik"]] = c.values  # t.o.m. denne datoen
    g["_hd"] = g["_d"]  # dato på siste historiske train-møte
    v = alle[["id"] + nokkel].copy()
    # strengt før: flytt radens dato ett nanosekund bakover før asof-oppslag
    v["_d"] = pd.to_datetime(alle["moetedato"]).astype("datetime64[ns]") - pd.Timedelta(1, "ns")
    m = pd.merge_asof(v.sort_values("_d"), g[nokkel + ["_d", "_hd", "n", "mot", "avvik"]].sort_values("_d"),
                      on="_d", by=nokkel, direction="backward")
    m = m.set_index("id").reindex(alle["id"])
    n = m["n"].fillna(0).astype(int)
    ut = pd.DataFrame({
        f"{prefiks}_n_tidl": n.values,
        f"{prefiks}_mot_andel_tidl": (m["mot"] / m["n"]).round(4).values,
        f"{prefiks}_avvik_andel_tidl": (m["avvik"] / m["n"]).round(4).values,
        f"{prefiks}_siste_hist_dato": m["_hd"].dt.strftime("%Y-%m-%d").values,
    })
    return ut


def lag(split: Path):
    train = pd.read_csv(split / "train.csv", low_memory=False, dtype={"cusip": str, "forvalter_cik": str})
    test = pd.read_csv(split / "test_input.csv", low_memory=False, dtype={"cusip": str, "forvalter_cik": str})
    for k in ("fasit", "avvik", "stemme", "mgmt_felt_LEKKER", "mot_ledelsen"):
        assert k not in test.columns, f"test_input har lekk-kolonne {k}"
    train["sett"], test["sett"] = "train", "test"
    alle = pd.concat([train, test], ignore_index=True)
    assert alle["id"].is_unique, "id-er er ikke unike på tvers av train/test"
    alle["selskap"] = alle["cusip"].fillna(alle["utsteder"].astype(str))
    alle["forslagstype"] = [forslagstype(k, s, t) for k, s, t in zip(alle["kategori"], alle["kilde"], alle["forslag"])]
    alle["undertype"] = [undertype(f, t) for f, t in zip(alle["forslagstype"], alle["forslag"])]
    alle["fra_aksjonaer"] = (alle["kilde"].astype(str).str.upper() == "SECURITY HOLDER").astype(int)
    alle["styret_anbefaler"] = alle["styret"].map({"FOR": "FOR", "AGAINST": "MOT"}).fillna(alle["styret"])
    tr = alle[alle["sett"] == "train"]
    deler = [alle[["id", "sett", "moetedato", "forvalter_cik", "selskap", "forslagstype", "undertype",
                   "fra_aksjonaer", "styret_anbefaler"]].reset_index(drop=True)]
    deler.append(historikk(tr, alle, ["selskap"], "sel"))
    deler.append(historikk(tr, alle, ["selskap", "forslagstype"], "seltype"))
    deler.append(historikk(tr, alle, ["forvalter_cik", "forslagstype"], "fond_type"))  # fondsprofil
    ut = pd.concat(deler, axis=1)
    ut.to_csv(split / "kjennetegn.csv", index=False)
    print(f"{split}: {len(ut)} rader ({(ut.sett=='train').sum()} train, {(ut.sett=='test').sum()} test) -> {split/'kjennetegn.csv'}")
    return ut


if __name__ == "__main__":
    for s in sys.argv[1:]:
        lag(Path(s))
