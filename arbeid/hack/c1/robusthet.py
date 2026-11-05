"""Robusthetstest for Case 1-agenten (#1968). Bare stdlib, kald start < 1 min.

    python3 -I arbeid/hack/c1/robusthet.py [--data arbeid/hack/c1/data_v3 ...] [--agent "CMD {train} {test} {pred}"]
                                           [--ut state/rapporter/hack_c1_robusthet.md]

Kjører agenten på fem varianter av samme tidssplitt og måler hver med maaler.py (v2):
  basis          train/test som de er
  nye_selskaper  alle selskaper (cusip, ellers utsteder) i holdout fjernes fra train: agenten har aldri sett dem
  siste_aar      train kuttes til de siste 365 dagene før holdout: bare ett år historikk
  tom_tekst      forslagsteksten er tom i hele holdout
  tomme_felt     forslag, kategori og utsteder er tomme i holdout (kilde/styret står, ellers kan ikke måleren regne avvik)
Tall per test: AVVIK-F1 (SCORE), PR-AUC og andel rutet til menneske (konfidens < 0,6). Krasj = tall 'KRASJ'.
"""
import csv, datetime, os, re, subprocess, sys, tempfile, time

HER = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HER, "..", "..", ".."))
STD_AGENT = f"python3 -I {HER}/../varianter/smed3_utf_sitat/agent.py {{train}} {{test}} {{pred}}"


def les(sti):
    with open(sti, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def skriv(sti, felt, rader):
    with open(sti, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=felt)
        w.writeheader()
        w.writerows(rader)


def selskap(r):
    return (r.get("cusip") or "").strip() or (r.get("utsteder") or "").strip().lower()


def varianter(train, test):
    """Gir (navn, train-rader, test-rader, forklaring)."""
    yield "basis", train, test, "uendret"
    nye = {selskap(r) for r in test}
    t = [r for r in train if selskap(r) not in nye]
    yield "nye_selskaper", t, test, f"{len(train) - len(t)} av {len(train)} train-rader fjernet (selskap i holdout)"
    grense = min(r["moetedato"] for r in test)
    fra = (datetime.date.fromisoformat(grense[:10]) - datetime.timedelta(days=365)).isoformat()
    t = [r for r in train if r["moetedato"] >= fra]
    yield "siste_aar", t, test, f"train fra {fra}: {len(t)} av {len(train)} rader"
    yield "tom_tekst", train, [dict(r, forslag="") for r in test], "forslag tom i alle holdout-rader"
    yield "tomme_felt", train, [dict(r, forslag="", kategori="", utsteder="") for r in test], \
        "forslag, kategori, utsteder tomme"


def maal(pred, fasit):
    p = subprocess.run([sys.executable, "-I", os.path.join(HER, "maaler.py"), pred, "--fasit", fasit],
                       capture_output=True, text=True)
    ut = p.stdout
    if p.returncode != 0:
        return dict(feil=(ut + p.stderr).strip().splitlines()[-1:])
    g = lambda m: float(re.search(m, ut).group(1))
    return dict(f1=g(r"SCORE (\S+)"), prauc=g(r"PRAUC (\S+)"), rutet=g(r"rutet til menneske.*?= ([\d.]+)%") / 100,
                mot_f1=g(r"MOT \(sekundært\).*?F1 (\S+)"), rec=g(r"AVVIK \(hovedtall\).*?recall (\S+)"))


def kjor(data, agent, tmp):
    felt_tr, train = les(os.path.join(data, "train.csv"))
    felt_te, test = les(os.path.join(data, "test_input.csv"))
    fasit = os.path.join(data, "fasit.csv")
    res = []
    for navn, tr, te, forkl in varianter(train, test):
        d = os.path.join(tmp, os.path.basename(data.rstrip("/")) + "_" + navn)
        os.makedirs(d)
        skriv(os.path.join(d, "train.csv"), felt_tr, tr)
        skriv(os.path.join(d, "test_input.csv"), felt_te, te)
        pred = os.path.join(d, "pred.csv")
        t0 = time.time()
        p = subprocess.run(agent.format(train=f"{d}/train.csv", test=f"{d}/test_input.csv", pred=pred),
                           shell=True, capture_output=True, text=True)
        sek = time.time() - t0
        if p.returncode != 0 or not os.path.exists(pred):
            m = dict(feil=["KRASJ: " + (p.stderr.strip().splitlines() or ["?"])[-1][:160]])
        else:
            m = maal(pred, fasit)
        m.update(navn=navn, forkl=forkl, sek=sek)
        print(f"  {navn:14s} " + (f"F1 {m['f1']:.3f}  PR-AUC {m['prauc']:.3f}  rutet {m['rutet']:.1%}  ({sek:.0f} s)"
                                  if "f1" in m else " ".join(m["feil"])), flush=True)
        res.append(m)
    return res


def rapport(alle, agent):
    L = ["# Case 1: robusthetstest for agenten (#1968)", "",
         f"Agent: `{agent}`  ", "Kjør: `python3 -I arbeid/hack/c1/robusthet.py` (kald start under 1 min). "
         "Måler: maaler.py v2, hovedtall AVVIK-F1 fra utledet styre; rutet = konfidens < 0,6.", ""]
    for data, res in alle:
        b = next((r for r in res if r["navn"] == "basis" and "f1" in r), None)
        L += [f"## {os.path.relpath(data, ROT)}", "",
              "| test | AVVIK-F1 | endring | recall | PR-AUC | rutet til menneske | MOT-F1 | hva |",
              "|---|---|---|---|---|---|---|---|"]
        for r in res:
            if "f1" not in r:
                L.append(f"| {r['navn']} | KRASJ | | | | | | {' '.join(r['feil'])} |")
                continue
            d = f"{r['f1'] - b['f1']:+.3f}" if b else ""
            L.append(f"| {r['navn']} | {r['f1']:.3f} | {d} | {r['rec']:.3f} | {r['prauc']:.3f} | {r['rutet']:.1%} | "
                     f"{r['mot_f1']:.3f} | {r['forkl']} |")
        L.append("")
    return "\n".join(L)


def main(a):
    datas = [a[i + 1] for i, x in enumerate(a) if x == "--data"] or [os.path.join(HER, "data"), os.path.join(HER, "data_v3")]
    agent = a[a.index("--agent") + 1] if "--agent" in a else STD_AGENT
    ut = a[a.index("--ut") + 1] if "--ut" in a else None
    alle = []
    with tempfile.TemporaryDirectory() as tmp:
        for data in datas:
            print(os.path.relpath(data, ROT), flush=True)
            alle.append((os.path.abspath(data), kjor(os.path.abspath(data), agent, tmp)))
    tekst = rapport(alle, agent)
    if ut:
        open(ut, "w", encoding="utf-8").write(tekst + "\n")
    else:
        print(tekst)


if __name__ == "__main__":
    main(sys.argv[1:])
