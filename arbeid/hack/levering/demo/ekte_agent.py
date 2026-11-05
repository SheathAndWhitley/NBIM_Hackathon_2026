"""Kjører den leverte agenten (arbeid/hack/levering/kjor_agent.py) på sakene som limes inn i demo-appen.

Samme modell og samme kall som `sh KJOR.sh`, men med --csv på de innlimte sakene i stedet for hele test 2026.
Agenten kjøres som egen prosess i miljøet KJOR.sh lager (.venv_kjor i repo-roten), så appen importerer ingen
frosne filer og endrer ingenting. Kjør derfor `sh KJOR.sh` i repo-roten først: den lager miljøet og legger
NBIMs stemmer på plass. DEMO_AGENT_PYTHON=<python> overstyrer miljøet. Én kjøring tar 10-30 s, fordi modellen
trenes på nytt hver gang.

Bruk uten Streamlit (samme svar som appen):
  python ekte_agent.py saker.csv      # skriver agentens rader som JSON-linjer
"""
import csv
import io
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROT = Path(__file__).resolve().parents[4]  # repo-roten
LEVERING = ROT / "arbeid/hack/levering"
REAL = ROT / "state/opplastet/20261105_114241_real_votes.csv"  # legges på plass av sh KJOR.sh
TRENG = ["meeting_id", "item_no", "company_id", "meeting_date", "proposal_text", "proposal_type", "proponent"]
FASIT = ("against_board", "nbim_vote", "nbim_vote_raw", "rationale_text", "rationale_section", "position_paper")
KJOR_FORST = "Kjør  sh KJOR.sh  i repo-roten først (lager miljøet .venv_kjor og legger dataene på plass)."
_MODELL = (LEVERING / "MODELL").read_text(encoding="utf-8").strip() if (LEVERING / "MODELL").exists() else "frossen"
AGENT = LEVERING / ("kjor_agent_v2av.py" if _MODELL == "v2av" else "kjor_agent.py")  # samme valg som KJOR.sh
MODELLNAVN = f"{'v2av' if _MODELL == 'v2av' else 'repo4'} ({AGENT.name}, samme modell som sh KJOR.sh)"


def agent_python():
    """Python med agentens låste pakker: DEMO_AGENT_PYTHON, ellers .venv_kjor fra sh KJOR.sh."""
    py = os.environ.get("DEMO_AGENT_PYTHON")
    if py:
        return py
    p = ROT / ".venv_kjor/bin/python"
    if p.exists():
        return str(p)
    raise RuntimeError("fant ikke agentens Python-miljø (.venv_kjor). " + KJOR_FORST)


def les_saker(tekst):
    """CSV-tekst i real_votes-format (overskrift + rader) -> liste av dict. Fasitfelt fjernes, ikke sendt videre."""
    rader = list(csv.DictReader(io.StringIO(tekst.strip())))
    if not rader:
        raise ValueError("fant ingen saker: lim inn en overskriftslinje og minst én rad")
    mangler = [k for k in TRENG if k not in rader[0]]
    if mangler:
        raise ValueError("overskriften mangler feltene " + ", ".join(mangler) +
                         " (real_votes-format, som arbeid/hack/c1/data_off/real_test_input.csv)")
    return [{k: v for k, v in r.items() if k not in FASIT and k is not None} for r in rader]


def uten_rot(tekst, tmp=None):
    """Bytter ut repo-stien (og den midlertidige mappa) i tekst som skal logges, så loggen ikke lekker lokale stier."""
    tekst = str(tekst).replace(str(ROT), "<rot>")
    return tekst.replace(tmp, "<tmp>") if tmp else tekst


def kjor_sporbar(saker, timeout=300):
    """Kjører agenten på sakene. Returnerer alltid en dict for loggen: kall, returkode, varighet, utskrift, rader
    (de 19 feltene i agent.csv) og feil (None når alt gikk bra). Stier er uten repo-sti."""
    if not REAL.exists():
        raise RuntimeError("mangler NBIMs stemmer (state/opplastet/). " + KJOR_FORST)
    py = agent_python()
    with tempfile.TemporaryDirectory(prefix="c1_lim_") as d:
        inn, ut = os.path.join(d, "saker.csv"), os.path.join(d, "ut")
        felt = list(dict.fromkeys(k for r in saker for k in r))
        with open(inn, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=felt)
            w.writeheader()
            w.writerows(saker)
        kall = [py, str(AGENT), "--csv", inn, "--ut", ut]
        t0 = time.monotonic()
        o = subprocess.run(kall, cwd=ROT, capture_output=True, text=True, timeout=timeout)
        fil = os.path.join(ut, "agent.csv")
        res = {"kall": [uten_rot(k, d) for k in kall], "cwd": "<rot>", "returkode": o.returncode,
               "varighet_s": round(time.monotonic() - t0, 1), "stdout": uten_rot(o.stdout.strip(), d),
               "stderr_hale": uten_rot(o.stderr.strip()[-2000:], d), "rader": [], "feil": None}
        if o.returncode != 0 or not os.path.exists(fil):
            res["feil"] = f"agenten feilet (kode {o.returncode}):\n{uten_rot((o.stdout + o.stderr)[-2000:], d)}"
        else:
            res["rader"] = list(csv.DictReader(open(fil, encoding="utf-8")))
        return res


def kjor(saker, timeout=300):
    """Returnerer (rader, stdout) eller RuntimeError. Appen bruker kjor_sporbar, som også gir loggen."""
    res = kjor_sporbar(saker, timeout)
    if res["feil"]:
        raise RuntimeError(res["feil"])
    return res["rader"], res["stdout"]


if __name__ == "__main__":
    rader, logg = kjor(les_saker(open(sys.argv[1], encoding="utf-8-sig").read()))
    print(logg, file=sys.stderr)
    for r in rader:
        print(json.dumps(r, ensure_ascii=False))
