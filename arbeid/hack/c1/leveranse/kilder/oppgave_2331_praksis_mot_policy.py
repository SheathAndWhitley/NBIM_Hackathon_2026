"""Case 1 (#2331, smed2): følger NBIM egne retningslinjer? Praksis mot policy i tall.

Bare lesing og telling. Ingen modell, frossen #2044 røres ikke.
Policy-stemmen for hver sak utledes mekanisk fra NBIMs Global Voting Guidelines (GVG):
  - Regelstyrt: et «We will (not) support»-punkt som kan avgjøres fra saksteksten alene
    (forslagstekst, forslagsstiller, marked). Se REGLER under.
  - Utgangspunkt: ellers gjelder NBIM 0.0.3 «Our starting point ... is to support the board»,
    dvs. policy-stemme = styrets anbefaling.
Samsvar = NBIMs faktiske stemme == policy-stemmen (AVSTÅ teller som avvik).
Kjør: uv run python arbeid/hack/c1/leveranse/kilder/oppgave_2331_praksis_mot_policy.py [--csv state/opplastet/..real_votes.csv]
"""
import argparse, os, re
import pandas as pd

ROT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
REAL = os.path.join(ROT, "state/opplastet/20261105_114241_real_votes.csv")


def pst(t):
    m = re.search(r"(\d+(?:\.\d+)?)\s*(?:Percent|%)", t, re.I)
    return float(m.group(1)) if m else None


def regel(r):
    """(policy-stemme, GVG-id) for regelstyrte saker, ellers (None, None)."""
    t, typ, mk = str(r.proposal_text), r.proposal_type, r.market
    shp = r.proponent == "Shareholder"
    if re.search(r"\bother business\b", t, re.I):
        return "MOT", "NBIM 5.2.4"                      # «e.g. the agenda item 'other business'»
    if re.search(r"poison pill|takeover defen[cs]e plan|shareholder rights plan", t, re.I) and not re.search(r"remove|eliminat|abolish|redeem", t, re.I):
        return "MOT", "NBIM 6.2.7"                      # innføring/fornyelse av anti-takeover
    if re.search(r"remove provisions on takeover defen|eliminate .*supermajority|reduce supermajority|adopt simple majority", t, re.I):
        return "FOR", "NBIM 6.2.8"                      # avskaffe anti-takeover
    if re.search(r"\bdeclassify\b", t, re.I):
        return "FOR", "NBIM 3.1.5"
    if re.search(r"\bclassify\b|stagger", t, re.I):
        return "MOT", "NBIM 3.1.4"
    if re.search(r"separate (the )?chair|independent board chair", t, re.I):
        return "FOR", "NBIM 1.3.5"
    if re.search(r"majority vote for the election of directors|majority voting", t, re.I):
        return "FOR", "NBIM 3.1.8"
    if re.search(r"proxy access", t, re.I) and shp:
        return "FOR", "NBIM 3.1.11"
    if typ == "SHARE_ISSUANCE" and re.search(r"without pre-?emptive", t, re.I) and "with or without" not in t.lower():
        p = pst(t)
        if p is not None:
            grense = 20 if mk == "DM" else 30
            return ("MOT" if p > grense else "FOR"), ("NBIM 6.1.5" if mk == "DM" else "NBIM 6.1.6")
    return None, None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--csv", default=REAL); ap.add_argument("--topp", type=int, default=12)
    a = ap.parse_args()
    d0 = pd.read_csv(a.csv, low_memory=False)
    d = d0[d0.nbim_vote.notna()].copy()  # 334 saker uten avgitt stemme (Do Not Vote, frekvens-valg o.l.) er ingen policy-beslutning
    rr = d.apply(regel, axis=1, result_type="expand"); d["regel_stemme"], d["regel_id"] = rr[0], rr[1]
    d["policy"] = d.regel_stemme.fillna(d.mgmt_rec)
    udef = d[d.policy.isna()]  # ingen regel og ingen styreanbefaling (f.eks. brasilianske stemmesedel-spørsmål)
    d = d[d.policy.notna()].copy()
    d["samsvar"] = d.nbim_vote == d.policy
    d["regelstyrt"] = d.regel_stemme.notna()
    d["har_gvg"] = d.rationale_section.astype(str).str.startswith("GVG")
    print(f"saker i fila {len(d0)}; uten avgitt stemme {d0.nbim_vote.isna().sum()}; uten regel og uten styreanbefaling {len(udef)}; målt {len(d)}")
    print(f"saker {len(d)}, år {d.year.min()}-{d.year.max()}, kilde {os.path.relpath(a.csv, ROT)}")
    print(f"TOTALT samsvar med policy-stemmen: {d.samsvar.mean():.1%} ({d.samsvar.sum()}/{len(d)})")
    rs = d[d.regelstyrt]
    print(f"regelstyrte saker: {len(rs)}, samsvar {rs.samsvar.mean():.1%} ({rs.samsvar.sum()}/{len(rs)})")
    ut = d[~d.regelstyrt]
    avv = ut[~ut.samsvar]
    print(f"utgangspunkt-saker (støtt styret, NBIM 0.0.3): {len(ut)}, samsvar {ut.samsvar.mean():.1%}; "
          f"avvik {len(avv)}, av dem MOT {int((avv.nbim_vote=='MOT').sum())} / AVSTÅ {int((avv.nbim_vote=='AVSTÅ').sum())} / FOR {int((avv.nbim_vote=='FOR').sum())}; "
          f"MOT-avvik med eget GVG-avsnitt i begrunnelsen: {avv[avv.nbim_vote=='MOT'].har_gvg.mean():.1%}")
    print("\n| forslagstype | saker | samsvar med policy | regelstyrte (samsvar) | avvik MOT | avvik AVSTÅ | avvik FOR | MOT-avvik med GVG-begrunnelse |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|")
    for typ, g in sorted(d.groupby("proposal_type"), key=lambda x: -len(x[1]))[:a.topp]:
        av = g[~g.samsvar]; rg = g[g.regelstyrt]; mot = av[av.nbim_vote == "MOT"]
        rtxt = f"{len(rg)} ({rg.samsvar.mean():.0%})" if len(rg) else "0"
        gtxt = f"{mot.har_gvg.mean():.0%} ({int(mot.har_gvg.sum())}/{len(mot)})" if len(mot) else "-"
        print(f"| {typ} | {len(g)} | {g.samsvar.mean():.1%} | {rtxt} | {len(mot)} | {int((av.nbim_vote=='AVSTÅ').sum())} | {int((av.nbim_vote=='FOR').sum())} | {gtxt} |")
    print("\nPer regel:")
    for rid, g in rs.groupby("regel_id"):
        print(f"  {rid}: {len(g)} saker, samsvar {g.samsvar.mean():.0%}, policy {dict(g.regel_stemme.value_counts())}, NBIM {dict(g.nbim_vote.value_counts())}")
    print("\nRegelstyrte avvik (praksis != tydelig regel):")
    kol = ["year", "company", "country", "market", "proposal_text", "proponent", "mgmt_rec", "nbim_vote", "regel_id", "rationale_section"]
    print(rs[~rs.samsvar][kol].to_string(max_colwidth=70))
    print("\nUtgangspunkt-avvik der NBIM stemte AVSTÅ (GVG har ingen avstå-regel), per selskap:", dict(avv[avv.nbim_vote == "AVSTÅ"].company.value_counts().head(6)))
    print("Utgangspunkt-avvik MOT uten GVG-begrunnelse, per selskap/år:")
    print(avv[(avv.nbim_vote == "MOT") & ~avv.har_gvg].groupby(["company", "year", "proposal_type"]).size().sort_values(ascending=False).head(10).to_string())
    print("\nMOT-avvik uten GVG-begrunnelse per type:", dict(avv[(avv.nbim_vote == "MOT") & ~avv.har_gvg].proposal_type.value_counts().head(8)))


if __name__ == "__main__":
    main()
