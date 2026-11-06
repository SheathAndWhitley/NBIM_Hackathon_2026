"""Grunnlinje «gjenta NBIMs forrige beslutning», målt med maaling/maaler.py (F1 på MOT mot styret).

Regel: avvik fra styret hvis NBIM avvek forrige gang på samme sak (normalisert tekst) eller samme person (styrevalg)
i samme selskap, ellers følg styret. «Forrige gang» er historikken modellen selv bruker (agent/historikk/ballot.py,
prev_same): bare tidligere møter, også tidligere samme år, altså samme informasjon som agenten har. Ingen trening.

Bruk (fra repo-roten, etter sh KJOR.sh):  .venv_kjor/bin/python maaling/grunnlinje_gjenta_forrige.py
Skriver én linje «MOT mot styret» per testår 2024, 2025 og 2026.
"""
import os
import pathlib
import subprocess
import sys
import tempfile

import pandas as pd

ROT = pathlib.Path(__file__).resolve().parents[1]
REAL = ROT / "data/real_votes.csv"
MAALER = ROT / "maaling/maaler.py"
sys.path.insert(0, str(ROT / "agent"))
from historikk import ballot  # noqa: E402  (samme historikk som modellen)


def svar():
    """Regelens svar for alle saker: id, year og anbefaling (1 = avvik fra styret)."""
    if not REAL.exists():
        sys.exit(f"mangler {REAL.relative_to(ROT)}")
    ballot.REAL_FILE = REAL
    B = ballot.load_real()
    d = pd.read_csv(REAL, dtype=str, keep_default_na=False)
    assert len(B) == len(d) and (B.meeting_id.astype(str).values == d.meeting_id.values).all()
    d["anbefaling"] = (B.prev_same == 1).astype(int).values  # 1 = avvik fra styret
    return d


def skriv_svar(d, aar, fil):
    """Svarfil i målerens format for ett år."""
    m = d.year == aar
    pd.DataFrame({"id": d.meeting_id[m] + "|" + d.item_no[m], "anbefaling": d.anbefaling[m],
                  "p_avvik": d.anbefaling[m].astype(float)}).to_csv(fil, index=False)


def main():
    d = svar()
    with tempfile.TemporaryDirectory(prefix="gjenta_forrige_") as tmp:
        for aar in ("2024", "2025", "2026"):
            fil = os.path.join(tmp, f"gjenta_forrige_{aar}.csv")
            skriv_svar(d, aar, fil)
            o = subprocess.run([sys.executable, "-I", str(MAALER), fil, f"y{aar}", "--score", "mot"],
                               capture_output=True, text=True)
            linje = next((x.strip() for x in o.stdout.splitlines() if "MOT mot styret" in x), o.stdout + o.stderr)
            print(f"{aar}  gjenta forrige beslutning  {linje}")


if __name__ == "__main__":
    main()
