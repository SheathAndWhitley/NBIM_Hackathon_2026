"""#2274: samme som oppgave_2272/feil_per_gruppe.py, men med valgbart år (--aar 2025|2026), så feilmønsteret kan
sammenlignes val 2025 mot test 2026. Reglene er målerens v3 --score mot. Klyngebootstrap over meeting_id, frø 2274.
Bruk: python3 -I arbeid/oppgave_2274/feil_per_gruppe_aar.py --svar STI --aar 2025 [--md fil]
"""
import csv, sys, random, hashlib, importlib.util
sp = importlib.util.spec_from_file_location("fpg", "arbeid/oppgave_2272/feil_per_gruppe.py")
fpg = importlib.util.module_from_spec(sp); sp.loader.exec_module(fpg)

def last(svar, aar):
    b = open(fpg.DATA, "rb").read(); assert hashlib.sha256(b).hexdigest() == fpg.SHA, "feil datafil"
    S = {r["id"].strip(): r for r in csv.DictReader(open(svar, encoding="utf-8-sig", newline=""))}
    rader = []
    for f in csv.DictReader(b.decode("utf-8").splitlines()):
        if f["year"] != aar or f.get("injection_flag") == "1" or f["against_board"] == "": continue
        i = f"{f['meeting_id']}|{f['item_no']}"; s = S[i]; a = (s.get("anbefaling") or "").strip().upper()
        styret = f["mgmt_rec"] or "FOR"
        if a in ("0", "1"): avv = a == "1"; a = ("FOR" if styret == "MOT" else "MOT") if avv else styret
        mot = a == "MOT"; y = f["against_board"] == "1.0"
        x = mot and styret != "MOT"; ys = f["nbim_vote"] == "MOT" and y
        rader.append({"meeting": f["meeting_id"], "land": f["country"], "marked": f["market"], "type": f["proposal_type"],
                      "stiller": f["proponent"], "tp": x and ys, "fp": x and not ys, "fn": (not x) and ys, "y": ys})
    return rader

if __name__ == "__main__":
    a = sys.argv[1:]
    svar = a[a.index("--svar") + 1]; aar = a[a.index("--aar") + 1]
    md = a[a.index("--md") + 1] if "--md" in a else None
    rader = last(svar, aar); rng = random.Random(2274)
    P, R, F = fpg.f1_av(rader); lo, hi = fpg.boot(rader, rng)
    ut = [f"Totalt {aar}: {len(rader)} saker, {sum(r['y'] for r in rader)} MOT i fasit, TP {sum(r['tp'] for r in rader)} FP {sum(r['fp'] for r in rader)} FN {sum(r['fn'] for r in rader)}, P {P:.4f} R {R:.4f} F1 {F:.4f}, 95 % KI {lo:.2f}–{hi:.2f} (klyngebootstrap over {len({r['meeting'] for r in rader})} møter)", ""]
    for n, navn in (("type", "sakstype"), ("land", "land"), ("marked", "marked (DM/EM)"), ("stiller", "forslagsstiller")):
        ut += fpg.tabell(rader, n, rng, navn) + [""]
    print("\n".join(ut))
    if md: open(md, "w", encoding="utf-8").write("\n".join(ut))
