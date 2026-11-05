"""Agenten for et valgfritt testår T (2024 eller 2025) i demo-appen. 2026 kjøres med den leverte kjor_agent.py.

Samme agent som den leverte: c1_real.py med ruting, kalibrering, sitat og vern kjøres uendret. Bare modellsteget byttes
til den rullende modellen arbeid/hack/c1/leveranse/verktoy/abl_rull.py --testaar T:
- trent på år < T;
- C, terskel og kalibrering valgt på T-1, med modell trent på år < T-1.
Det er samme oppsett som treårstallene i testaar.sh, og ingen frosne filer endres. Kjøres i .venv_kjor
(se ekte_agent.py).

Bruk:  python agent_aar.py --aar 2025 --csv saker.csv --ut UTMAPPE
"""
import argparse
import contextlib
import io
import os
import runpy
import sys
from pathlib import Path

ROT = Path(__file__).resolve().parents[4]
RULL = ROT / "arbeid/hack/c1/leveranse/verktoy/abl_rull.py"
sys.path.insert(0, str(ROT / "arbeid/hack/levering"))
import c1_real  # noqa: E402  (den leverte agenten, uendret)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--aar", type=int, required=True, choices=[2024, 2025])
    p.add_argument("--csv", required=True)
    p.add_argument("--ut", required=True)
    p.add_argument("--baand", default="0.15,0.85")
    a = p.parse_args()

    def kjor_modell(data_fil, logg):
        """Som c1_real.kjor_modell, men med den rullende modellen for testår a.aar."""
        gammel = sys.argv
        sys.argv = [str(RULL), data_fil, "--variant", "miks", "--hist", "2", "--repo", c1_real.REPO,
                    "--testaar", str(a.aar), "--ut", os.devnull]
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                g = runpy.run_path(str(RULL), run_name="abl_rull")
        finally:
            sys.argv = gammel
        logg += [f"--- abl_rull.py --testaar {a.aar}: trent på år < {a.aar}, C, terskel og kalibrering valgt på {a.aar - 1} ---"]
        logg += [x for x in buf.getvalue().splitlines() if x.strip()]
        return g

    c1_real.kjor_modell = kjor_modell
    print(f"MERK: testår {a.aar}. Linjene «låst på val 2025» og «saker fra før 2026» under er standardteksten til den "
          f"leverte agenten; her er terskelen valgt på {a.aar - 1}, og modellen er trent på år før {a.aar}.")
    c1_real.main(argparse.Namespace(csv=a.csv, sak=None, historikk=c1_real.REAL, vindu=None, ut=a.ut,
                                    baand=a.baand, til_menneske=None), None)


if __name__ == "__main__":
    main()
