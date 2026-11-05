"""Grunnlinje «gjenta NBIMs forrige beslutning», målt med den offisielle måleren (F1 på MOT mot styret).

Regel: avvik fra styret hvis NBIM avvek forrige gang på samme sak (normalisert tekst) eller samme person (styrevalg)
i samme selskap, ellers følg styret. «Forrige gang» er historikken modellen selv bruker (arbeid/hack/levering/
stemmeagent/ballot.py, prev_same): bare tidligere møter, også tidligere i samme sesong, altså samme informasjon som
agenten har. Ingen trening, ingen terskel.

Bruk (fra repo-roten, etter sh KJOR.sh, som legger dataene på plass):
  .venv_kjor/bin/python arbeid/hack/c1/grunnlinje_gjenta_forrige.py
Skriver svarfiler i en midlertidig mappe og én linje «MOT mot styret» per testår 2024, 2025 og 2026.
"""
import os
import pathlib
import subprocess
import sys
import tempfile

import pandas as pd

ROT = pathlib.Path(__file__).resolve().parents[3]
REAL = ROT / "state/opplastet/20261105_114241_real_votes.csv"
MAALER = ROT / "arbeid/hack/c1/leveranse/verktoy/maaler_aar.py"
sys.path.insert(0, str(ROT / "arbeid/hack/levering"))
from stemmeagent import ballot  # noqa: E402  (samme historikk som modellen)


def main():
    if not REAL.exists():
        sys.exit(f"mangler {REAL.relative_to(ROT)}: kjør sh KJOR.sh først")
    ballot.REAL_FILE = REAL
    B = ballot.load_real()
    d = pd.read_csv(REAL, dtype=str, keep_default_na=False)
    assert len(B) == len(d) and (B.meeting_id.astype(str).values == d.meeting_id.values).all()
    d["anbefaling"] = (B.prev_same == 1).astype(int).values  # 1 = avvik fra styret
    with tempfile.TemporaryDirectory(prefix="gjenta_forrige_") as tmp:
        for aar in ("2024", "2025", "2026"):
            m = d.year == aar
            svar = os.path.join(tmp, f"gjenta_forrige_{aar}.csv")
            pd.DataFrame({"id": d.meeting_id[m] + "|" + d.item_no[m], "anbefaling": d.anbefaling[m],
                          "p_avvik": d.anbefaling[m].astype(float)}).to_csv(svar, index=False)
            o = subprocess.run([sys.executable, "-I", str(MAALER), svar, f"y{aar}", "--data", "real", "--score", "mot"],
                               capture_output=True, text=True, env={**os.environ, "C1_DATA": str(REAL)})
            linje = next((x.strip() for x in o.stdout.splitlines() if "MOT mot styret" in x), o.stdout + o.stderr)
            print(f"{aar}  gjenta forrige beslutning  {linje}")


if __name__ == "__main__":
    main()
