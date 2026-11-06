"""Agenten for et valgfritt testår T (2024 eller 2025) i demo-appen. 2026 kjøres med den leverte kjor_agent.py.

Samme agent som den leverte: agent/kjerne.py med ruting, kalibrering, sitat og vern kjøres uendret. Bare modellsteget
byttes til den rullende modellen agent/modell_rullende.py --testaar T:
- trent på år < T;
- C, terskel og kalibrering valgt på T-1, med modell trent på år < T-1.
Det er samme oppsett som treårstallene i maaling/testaar.sh, og ingen agentfiler endres. Kjøres i .venv_kjor
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

ROT = Path(__file__).resolve().parents[1]
RULL = ROT / "agent/modell_rullende.py"
sys.path.insert(0, str(ROT / "agent"))
import kjerne  # noqa: E402  (den leverte agenten, uendret)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--aar", type=int, required=True, choices=[2024, 2025])
    p.add_argument("--csv", required=True)
    p.add_argument("--ut", required=True)
    p.add_argument("--baand", default="0.15,0.85")
    a = p.parse_args()

    def kjor_modell(data_fil, logg):
        """Som kjerne.kjor_modell, men med den rullende modellen for testår a.aar."""
        gammel = sys.argv
        sys.argv = [str(RULL), data_fil, "--variant", "miks", "--hist", "2", "--repo", kjerne.REPO,
                    "--testaar", str(a.aar), "--ut", os.devnull]
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                g = runpy.run_path(str(RULL), run_name="modell_rullende")
        finally:
            sys.argv = gammel
        logg += [f"--- modell_rullende.py --testaar {a.aar}: trent på år < {a.aar}, C, terskel og kalibrering valgt på {a.aar - 1} ---"]
        logg += [x for x in buf.getvalue().splitlines() if x.strip()]
        return g

    kjerne.kjor_modell = kjor_modell
    print(f"MERK: testår {a.aar}. Linjene «låst på val 2025» og «saker fra før 2026» under er standardteksten til den "
          f"leverte agenten; her er terskelen valgt på {a.aar - 1}, og modellen er trent på år før {a.aar}.")
    kjerne.main(argparse.Namespace(csv=a.csv, sak=None, historikk=kjerne.REAL, vindu=None, ut=a.ut,
                                    baand=a.baand, til_menneske=None), None)


if __name__ == "__main__":
    main()
