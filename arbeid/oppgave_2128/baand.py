"""#2128 smed3: send-til-menneske-bånd på kalibrert P(MOT). Frossen #2044 miks h2 urørt (p og mot_pred fra #2109).
Isotonisk kalibrering lært på val 2025, brukt på test 2026. Bånd [lo,hi) på kalibrert q => menneske."""
import json, numpy as np, pandas as pd
from sklearn.isotonic import IsotonicRegression
K = "arbeid/oppgave_2109/"
d = pd.read_csv("state/opplastet/20261105_114241_real_votes.csv", low_memory=False)
v = pd.read_csv(K + "val_pred.csv"); t = pd.read_csv(K + "test_pred.csv"); g = json.load(open(K + "kal_resultat.json"))["grense"]
iso = IsotonicRegression(out_of_bounds="clip", y_min=0, y_max=1).fit(v.p, v.y)
def f1(pr, y):
    tp = (pr & y).sum(); fp = (pr & ~y).sum(); fn = (~pr & y).sum()
    return 2 * tp / (2 * tp + fp + fn) if tp else 0.0, int(tp), int(fp), int(fn)
BAAND = [(0.3, 0.7), (0.15, 0.85), (0.08, 0.95)]
rader = []
for navn, p, y in (("val2025", v.p.values, v.y.values.astype(bool)), ("test2026", t.p.values, t.y.values.astype(bool))):
    q = iso.predict(p); pr = p >= g
    F, tp, fp, fn = f1(pr, y); print(f"{navn}: uten ruting F1 {F:.4f} (TP {tp} FP {fp} FN {fn}), n {len(y)}, MOT {y.sum()}")
    for lo, hi in BAAND:
        b = (q >= lo) & (q < hi); r = ~b
        Fr, tp, fp, fn = f1(pr[r], y[r])
        # systemtall hvis mennesket avgjør båndet riktig (øvre grense) og hvis mennesket følger styret (nedre)
        Fop, *_ = f1(np.where(b, y, pr), y); Fned, *_ = f1(np.where(b, False, pr), y)
        rad = dict(vindu=navn, baand=f"[{lo},{hi})", videresendt=int(b.sum()), andel=float(b.mean()), mot_i_baand=int(y[b].sum()),
                   mot_totalt=int(y.sum()), flagg_i_baand=int(pr[b].sum()), F1_rest=Fr, TP=tp, FP=fp, FN=fn, F1_sys_menneske_riktig=Fop, F1_sys_menneske_folger_styret=Fned)
        rader.append(rad)
        print(f"  {rad['baand']:12s} videresendt {b.sum():4d} ({b.mean():.1%}) MOT i bånd {y[b].sum():3d}/{y.sum()} flagg i bånd {pr[b].sum():3d} | F1 rest {Fr:.4f} (TP {tp} FP {fp} FN {fn}) | system: menneske riktig {Fop:.4f}, menneske følger styret {Fned:.4f}")
pd.DataFrame(rader).to_csv("baand_tabell.csv", index=False)
# svarfiler for måleren: konfidens 0.5 i båndet (=> menneske ved --terskel 0.6), ellers kalibrert sikkerhet på valgt svar
r = d.loc[t.rad]; ids = r.meeting_id.astype("Int64").astype(str) + "|" + r.item_no.astype("Int64").astype(str)
q = iso.predict(t.p); pr = (t.p >= g).values
alle = d[d.year == 2026]; ai = set(alle.meeting_id.astype("Int64").astype(str) + "|" + alle.item_no.astype("Int64").astype(str))
for lo, hi in BAAND:
    b = (q >= lo) & (q < hi); k = np.where(b, 0.5, np.maximum(np.where(pr, q, 1 - q), 0.6))
    s = pd.DataFrame({"id": ids.values, "anbefaling": pr.astype(int), "konfidens": np.round(k, 4), "p_avvik": np.round(q, 5)})
    m = sorted(ai - set(s.id)); s = pd.concat([s, pd.DataFrame({"id": m, "anbefaling": 0, "konfidens": 1.0, "p_avvik": 0.0})])
    s.to_csv(f"svar_baand_{lo}_{hi}.csv", index=False)
