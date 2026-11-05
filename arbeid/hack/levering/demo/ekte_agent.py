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
import re
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
# Inndatafeltene (som arbeid/hack/c1/data_off/real_test_input.csv uten id), og hele real_votes.csv. Brukes når
# raden limes inn uten overskrift: formatet kjennes igjen på antall felt.
INN_FELT = ["injection_flag", "meeting_id", "company_id", "company", "ticker", "country", "market", "meeting_date",
            "item_no", "proposal_number", "proposal_text", "proponent", "mgmt_rec_raw", "mgmt_rec", "year", "proposal_type"]
REAL_FELT = ["injection_flag", "meeting_id", "company_id", "company", "ticker", "country", "market", "meeting_date",
             "item_no", "proposal_number", "proposal_text", "proponent", "mgmt_rec_raw", "nbim_vote_raw", "mgmt_rec",
             "nbim_vote", "against_board", "rationale_text", "position_paper", "year", "proposal_type", "rationale_section"]
KJENTE = {len(INN_FELT): INN_FELT, len(INN_FELT) + 1: ["id"] + INN_FELT, len(REAL_FELT): REAL_FELT}
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


def _del_opp(tekst):
    """Innlimt tekst -> liste av rader (lister av felt). Tåler det man får ved kopiering: komma, semikolon eller
    tabulator mellom feltene (tabulator fra regneark ser ut som mellomrom), mellomrom rundt feltene (justert visning),
    og som siste utvei kolonner skilt bare med mellomrom (minst to mellom feltene; overskriften med ett)."""
    linjer = [l for l in tekst.replace("﻿", "").replace("\r\n", "\n").replace("\r", "\n").split("\n") if l.strip()]
    if not linjer:
        return []
    forste = linjer[0]
    if "\t" in forste:
        skille = "\t"
    else:
        tell = {d: forste.count(d) for d in (",", ";", "|")}
        skille = max(tell, key=tell.get) if max(tell.values()) else None
    if skille:
        rader = list(csv.reader(io.StringIO("\n".join(linjer)), delimiter=skille, skipinitialspace=True))
    else:  # bare mellomrom: overskriften har ingen mellomrom i feltnavnene, sakstekstene har bare enkle mellomrom
        rader = [forste.split()] + [re.split(r"\t|\s{2,}", l.strip()) for l in linjer[1:]]
    return [[f.strip().strip('"').strip() for f in r] for r in rader if any(f.strip() for f in r)]


def les_saker(tekst):
    """Innlimt saksliste (real_votes-format, med eller uten overskrift) -> liste av dict. Fasitfelt fjernes."""
    rader = _del_opp(tekst)
    if not rader:
        raise ValueError("fant ingen saker: lim inn minst én rad")
    if "meeting_id" in rader[0]:
        hode, data = rader[0], rader[1:]
    elif len(rader[0]) in KJENTE:  # rader uten overskrift: formatet kjennes igjen på antall felt
        hode, data = KJENTE[len(rader[0])], rader
    else:
        raise ValueError(f"fant ingen overskrift, og første rad har {len(rader[0])} felt; kjente formater uten overskrift "
                         f"har {', '.join(map(str, sorted(KJENTE)))} felt (appens eksempel, testinndata, real_votes.csv)")
    if not data:
        raise ValueError("fant bare overskriften: lim inn minst én sak under den")
    feil = [i for i, r in enumerate(data, 1) if len(r) != len(hode)]
    if feil:
        raise ValueError(f"rad {feil[0]} har {len(data[feil[0] - 1])} felt, overskriften har {len(hode)}. Sjekk skilletegnene "
                         "(komma, semikolon eller tabulator mellom feltene) og at tekst med komma står i anførselstegn")
    rader = [dict(zip(hode, r)) for r in data]
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
