"""#2274: val 2025-prediksjoner fra den frosne #2044-modellen (train.py uendret, kjørt via runpy som i c1_real.kjor_modell).
pv = modell trent <2025 (historikk <2025) på val 2025; MOT-flagg = pv >= t (C og t valgt på val, så tallet er litt
optimistisk, men sakene er ikke i treningen). Skriver måler-format (id, anbefaling 0/1, konfidens, p_avvik) for ALLE
2025-rader, så maaler_offisiell_v3.py val --data real kan kjøres rett på fila.
Bruk: uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2274/val_pred.py UT.csv
"""
import sys, os, io, contextlib, runpy, csv
import pandas as pd, numpy as np
ARB = "arbeid"
TRAIN = os.path.join(ARB, "oppgave_2044/train.py")
DATA = "state/opplastet/20261105_114241_real_votes.csv"
ut = sys.argv[1]
sys.argv = [TRAIN, DATA, "--variant", "miks", "--hist", "2", "--ut", os.devnull]
buf = io.StringIO()
with contextlib.redirect_stdout(buf): g = runpy.run_path(TRAIN, run_name="smed3_2274")
print(buf.getvalue())
d, va, pv, t = g["d"], g["va"], np.asarray(g["pv"], float), float(g["t"])
print("val-rader med fasit:", int(va.sum()), "grense", t, "flagget MOT:", int((pv >= t).sum()))
idx = d.index[va]
P = dict(zip(idx, pv))
with open(ut, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["id", "anbefaling", "konfidens", "p_avvik"])
    for j, r in d[d.year == 2025].iterrows():
        i = f"{int(r.meeting_id)}|{int(r.item_no)}"
        p = P.get(j)
        w.writerow([i, int(p >= t) if p is not None else 0, 0.9, round(float(p), 5) if p is not None else 0.0])
print("skrev", ut)
