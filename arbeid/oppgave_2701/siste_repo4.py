"""#2701: speiderens #2569-regel (siste stemme samme selskap+tekst) på repo4 (frossen 0,5162). Variant valgt på val T-1, test T én gang med offisiell måler."""
import csv, re, collections, subprocess, os
D = "state/opplastet/20261105_114241_real_votes.csv"
B = "arbeid/oppgave_2575"; M = "arbeid/oppgave_2567/maaler_aar.py"
U = os.path.dirname(os.path.abspath(__file__))
R = [r for r in csv.DictReader(open(D, encoding="utf-8")) if r["injection_flag"] != "1"]
F = {f"{r['meeting_id']}|{r['item_no']}": r for r in R}
norm = lambda t: re.sub(r"[^a-z ]", "", t.lower()).strip()
def les(f): return list(csv.DictReader(open(f)))
def hist(aar):
    h = collections.defaultdict(list)
    for r in sorted((r for r in R if int(r["year"]) < aar and r["nbim_vote"] in ("FOR", "MOT")), key=lambda r: r["meeting_date"]):
        h[(r["company_id"], norm(r["proposal_text"]))].append(r["nbim_vote"])
    return h
def bruk(rows, aar, regel, f):
    h = hist(aar)
    with open(f, "w") as o:
        o.write("id,anbefaling,p_avvik\n")
        for x in rows:
            a = x["anbefaling"] == "1"; r = F.get(x["id"])
            if r is not None:
                v = h.get((r["company_id"], norm(r["proposal_text"])), []); styret = r["mgmt_rec"] or "FOR"
                if "av" in regel and a and v and v[-1] == "FOR": a = False
                if "paa" in regel and not a and v and v[-1] == "MOT" and styret != "MOT": a = True
            o.write(f"{x['id']},{int(a)},{x['p_avvik']}\n")
def mål(f, v):
    o = subprocess.run(["python3", "-I", M, f, v, "--data", "real", "--score", "mot"], capture_output=True, text=True).stdout
    return float([l for l in o.splitlines() if l.startswith("SCORE")][-1].split()[1])
res = {k: [] for k in ("", "av", "paa", "av+paa", "valgt")}
for T in (2024, 2025, 2026):
    V, S = les(f"{B}/repo4_{T}_val.csv"), les(f"{B}/repo4_{T}_test.csv"); vb = {}
    for regel in ("", "av", "paa", "av+paa"):
        fv = f"{U}/v_{T}_{regel or 'ingen'}.csv"; bruk(V, T-1, regel, fv); vb[regel] = mål(fv, f"y{T-1}")
        ft = f"{U}/r4siste_{regel or 'ingen'}_{T}_test.csv"; bruk(S, T, regel, ft); res[regel].append(mål(ft, f"y{T}"))
    valgt = max(vb, key=lambda k: (vb[k], k == ""))
    res["valgt"].append(res[valgt][-1])
    print(T, "val", {k: round(v, 4) for k, v in vb.items()}, "valgt", valgt or "ingen", "test", {k: round(v[-1], 4) for k, v in res.items()}, flush=True)
for k, v in res.items(): print(f"{k or 'repo4':7s} snitt {sum(v)/3:.4f}", [round(x, 4) for x in v])
