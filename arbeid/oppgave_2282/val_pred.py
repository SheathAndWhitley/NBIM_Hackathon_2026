"""#2282: ærlig val 2025-prediksjon fra den frosne modellen (train.py #2044, miks h2), kjørt uendret via runpy
nøyaktig som c1_real.kjor_modell gjør. Skriver rad,p for val-radene (trent <2025) i målerens rad,p-format:
p er pv skalert monotont så rå grense t -> 0,5 (måleren sier avvik ved p >= 0,5). Rørte ingen agentfiler.
Bruk: python val_pred.py TRAIN.py DATA.csv UT.csv"""
import sys, runpy, io, contextlib, os
import numpy as np, pandas as pd
train, data, ut = sys.argv[1:4]
sys.argv = [train, data, "--variant", "miks", "--hist", "2", "--ut", os.devnull]
buf = io.StringIO()
with contextlib.redirect_stdout(buf): g = runpy.run_path(train, run_name="smed2_2044")
print("\n".join(l for l in buf.getvalue().splitlines() if l.startswith("VAL")))
pv, t, va, d = np.asarray(g["pv"], float), float(g["t"]), g["va"], g["d"]
rad = d.index[va]
p = np.where(pv < t, 0.5 * pv / t, 0.5 + 0.5 * (pv - t) / max(1 - t, 1e-9))
alle = d.index[(d.year == 2025).values]  # måleren krever alle val-rader; rader uten fasit (61) får p=0 (følg styret)
P = pd.Series(0.0, index=alle); P.loc[rad] = p
pd.DataFrame({"rad": P.index, "p": P.values}).to_csv(ut, index=False)
print(f"skrev {ut}: {len(rad)} val-rader, {(pv >= t).sum()} avvik ved rå grense {t:.5f}")
