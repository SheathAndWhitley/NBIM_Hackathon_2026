"""Case 1 (ordre #277, oppgave #2762): lista over ALT Case 1-arbeid som skal inn i GitHub-repoen nbim.

Brukes av github_synk.sh:  python3 -I arbeid/verktoy/c1_github_alt.py liste   -> én sti per linje (stdout)
                           python3 -I arbeid/verktoy/c1_github_alt.py utelatt -> sti<TAB>grunn per linje
Tar med: alle filer under arbeid/hack/c1 og arbeid/hack/levering, state/rapporter/c1_*.md, case1_*.md og
andre rapporter som handler om Case 1,
og skriptene/REGEL.md-filene i c1_henviste_filer.txt (#2899). Utelater rådata, fasit, arrangørens tekst og alt over 50 MB.
"""
import os
import fnmatch
import re
import sys

ROT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MAKS = 50 * 1024 * 1024
# Mapper som aldri tas med: rådata som hentes på nytt (DATA.md), virtuelle miljøer, cache
MAPPER_UT = {
    "data_off": "arrangørens casedata (hentes fra casepakken, se DATA.md)",
    "gammel_data": "nedlastet N-PX-rådata fra SEC (hentes på nytt med hent_npx.py/hent_votes.py, se DATA.md)",
    ".venv": "virtuelt miljø (lages av uv fra pyproject.toml/uv.lock)",
    "__pycache__": "Python-cache",
    "utkast_1100": "utkast holdt utenfor også før (#2666-synken)",
}
FILER_UT = {".DS_Store", ".pyc"}
# csv-kolonner som betyr fasit eller arrangørens/NBIMs rådata
KOLONNER_UT = {"fasit", "y", "stemme", "nbim_stemme", "faktisk_npx", "forslag", "proposal_text",
               "forvalter", "forvalter_cik", "nbim_stemme_side"}
SPESIELLE_UT = {"pred_miks_h2": "fasitkolonne y (#2666)"}
# Rapporter som viser rader fra arrangørens casedata (#2795, merknad i #2793)
MONSTER_UT = {"opplastet_*real_votes*": "opplastings-rapport med rader fra arrangørens real_votes.csv (#2795)",
              "opplastet_*npx_votes*": "opplastings-rapport med rader fra npx_votes.csv (#2807)",
              "opplastet_*": "opplastings-rapport, kan vise rader fra arrangørens filer (#2816, rens #2810)"}
TREFF = re.compile(r"Case 1|stemmeagent|c1_stemmeagent|NBIM", re.I)


def grunn(sti):
    deler = sti.split("/")
    for d in deler[:-1]:
        if d in MAPPER_UT:
            return MAPPER_UT[d]
    navn = deler[-1]
    if navn in FILER_UT or navn.endswith(".pyc"):
        return "systemfil/cache"
    for m, g in MONSTER_UT.items():
        if fnmatch.fnmatch(navn, m):
            return g
    for k, g in SPESIELLE_UT.items():
        if k in navn:
            return g
    full = os.path.join(ROT, sti)
    if os.path.islink(full):
        return "symlenke"
    if os.path.getsize(full) > MAKS:
        return "over 50 MB"
    if navn.endswith(".csv"):
        with open(full, encoding="utf-8", errors="replace") as fh:
            hode = {c.strip().strip('"').lower() for c in fh.readline().split(",")}
        treff = sorted(hode & KOLONNER_UT)
        if treff:
            return "csv med fasit eller arrangørens/NBIMs rådata (kolonne " + ", ".join(treff) + ")"
    return None


def kandidater():
    ut = []
    for topp in ("arbeid/hack/c1", "arbeid/hack/levering"):
        for d, mapper, filer in os.walk(os.path.join(ROT, topp)):
            rel = os.path.relpath(d, ROT)
            # ikke gå ned i store mapper vi uansett utelater; rapporter dem som én linje
            for m in list(mapper):
                if m in MAPPER_UT:
                    mapper.remove(m)
                    ut.append((f"{rel}/{m}/", MAPPER_UT[m]))
            ut.extend((f"{rel}/{f}", None) for f in filer)
    # #2899 (ordre #282): skript og REGEL.md som repo-dokumentene viser til, fra oppgave-mappene
    with open(os.path.join(ROT, "arbeid/verktoy/c1_henviste_filer.txt"), encoding="utf-8") as fh:
        for linje in fh:
            linje = linje.strip()
            if linje and not linje.startswith("#") and os.path.isfile(os.path.join(ROT, linje)):
                ut.append((linje, None))
    rap = os.path.join(ROT, "state/rapporter")
    for f in sorted(os.listdir(rap)):
        if not f.endswith(".md"):
            continue
        if f.startswith(("c1_", "case1_")):
            ut.append((f"state/rapporter/{f}", None))
            continue
        with open(os.path.join(rap, f), encoding="utf-8", errors="replace") as fh:
            if TREFF.search(fh.read()):
                ut.append((f"state/rapporter/{f}", None))
    return ut


def main():
    modus = sys.argv[1] if len(sys.argv) > 1 else "liste"
    for sti, g in kandidater():
        if g is None:
            g = grunn(sti)
        if modus == "liste" and g is None:
            print(sti)
        elif modus == "utelatt" and g is not None:
            print(f"{sti}\t{g}")


if __name__ == "__main__":
    main()
