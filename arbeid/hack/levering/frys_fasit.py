"""Fasit for frys-dommen (#2445): sha256 for hver fil slik den ligger i jury-zipen, regnet fra kilden.

Speiler pakk_jury.sh uten å kjøre fremmed.sh: samme fillista (fremmed.sh sine kopier-linjer,
c1_frys.py FILER, c1/leveranse/, vis_manussaker.py, DEMO_MANUS.md, tall_tabell.md, KJOR.sh, README.md),
samme sed på de to målerne, og FROSNE_SHA256.txt bygd på samme vis. Zip-pakka skal ha nøyaktig disse filene.

Bruk (fra landsbymappen):  python3 -I arbeid/hack/levering/frys_fasit.py > arbeid/hack/levering/frys_fasit_1600.sha256
Utskrift: «<sha256>  c1_stemmeagent/<sti>», sortert. Endrer ingenting i pakka.
"""
import glob, hashlib, os, re, runpy, sys

KILDE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.."))
NAVN = "c1_stemmeagent"
MAALERE = ["arbeid/hack/c1/maaler_offisiell_v2.py", "arbeid/hack/c1/maaler_offisiell_v3.py"]


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def les(f):
    with open(os.path.join(KILDE, f), "rb") as fh:
        return fh.read()


def finn(mappe):
    """Som pakk_jury.sh: find -type f uten __pycache__, *.pyc, .DS_Store, ut/, spor_npx/utkast_1100/ (#2457)."""
    ut = []
    for rot, mapper, filer in os.walk(os.path.join(KILDE, mappe)):
        rel = os.path.relpath(rot, KILDE)
        if "__pycache__" in rel.split(os.sep) or "ut" in rel.split(os.sep)[len(mappe.split("/")):]:
            continue
        if rel.endswith("spor_npx/utkast_1100") or "/spor_npx/utkast_1100/" in rel + "/":  # ut av zipen (#2457)
            continue
        for f in filer:
            if f.endswith(".pyc") or f == ".DS_Store":
                continue
            ut.append(os.path.join(rel, f))
    return ut


def fillista():
    os.chdir(KILDE)
    filer = set()
    # fremmed.sh: eksplisitt liste + c1_tallvakt + levering/*.md + leveranse/*.md + pyproject/uv.lock i roten
    filer |= {
        "arbeid/hack/levering/kjor_agent.py", "arbeid/hack/levering/c1_real.py",
        "arbeid/hack/levering/injeksjon_hoflig.py", "arbeid/hack/levering/retningslinje_oppslag.py",
        "arbeid/hack/c1/retningslinjer/punkter.jsonl", "arbeid/oppgave_2044/train.py",
        "arbeid/oppgave_2047/vern.py", "arbeid/oppgave_2046/case1_mot.py",
        "arbeid/hack/c1/maaler_offisiell_v2.py", "arbeid/hack/c1/maaler_offisiell_v3.py",
        "arbeid/hack/c1/data_off/real_test_input.csv", "state/opplastet/20261105_114241_real_votes.csv",
        "arbeid/hack/levering/sjekk_treffsikkerhet.sh", "arbeid/verktoy/c1_tallvakt.py",
    }
    filer |= set(glob.glob("arbeid/hack/levering/*.md")) | set(glob.glob("arbeid/hack/c1/leveranse/*.md"))
    # pyproject.toml og uv.lock i zip-rota er kandidatens låste (pakk_jury.sh etter #2475, som fremmed.sh)
    kand = "arbeid/kandidater/smed2_c1_mot"
    rot_kopi = {"pyproject.toml": f"{kand}/pyproject.toml", "uv.lock": f"{kand}/uv.lock"}
    frosne = runpy.run_path("arbeid/verktoy/c1_frys.py", run_name="x")["FILER"]
    filer |= set(frosne)
    filer |= set(finn("arbeid/hack/c1/leveranse"))
    filer |= kopier_linjer()  # vis_manussaker.py, DEMO_MANUS.md, tall_tabell.md, #2448-filene osv.
    return sorted(filer), rot_kopi, frosne


def kopier_linjer():
    """Bokstavelige stier i pakk_jury.sh sine `kopier ...`-linjer (med \\-fortsettelser), så fasiten følger skriptet.
    Linjer med $FILER/$FROSNE/$( tas ikke herfra; de regnes ut over."""
    with open(os.path.join(KILDE, "arbeid/hack/levering/pakk_jury.sh")) as fh:
        tekst = fh.read().replace("\\\n", " ")
    ut = set()
    for linje in tekst.splitlines():
        linje = linje.split("#", 1)[0].strip()
        if not linje.startswith("kopier ") or "$" in linje:
            continue
        ut |= {s for s in linje.split()[1:] if s.startswith(("arbeid/", "state/"))}
    return ut


def innhold_i_pakka(f):
    b = les(f)
    if f in MAALERE:  # pakk_jury.sh steg 3: relative datastier
        t = b.decode("utf-8")
        t = re.sub(r'"([^"]*)"', r'os.path.join(HER, "../../../\1")', t)
        b = t.encode("utf-8")
    return b


def main():
    filer, rot_kopi, frosne = fillista()
    ut = {}
    for f in filer:
        ut[f"{NAVN}/{f}"] = sha_bytes(innhold_i_pakka(f))
    for mål, kilde in rot_kopi.items():
        ut[f"{NAVN}/{mål}"] = sha_bytes(les(kilde))
    ut[f"{NAVN}/KJOR.sh"] = sha_bytes(les("arbeid/hack/levering/jury_kjor.sh"))
    ut[f"{NAVN}/README.md"] = sha_bytes(les("arbeid/hack/levering/JURY_README.md"))
    # steg 4: FROSNE_SHA256.txt = shasum -a 256 av de frosne (ikke målerne), i FILER-rekkefølge, slik de ligger i pakka
    linjer = "".join(f"{sha_bytes(les(f))}  {f}\n" for f in frosne if "maaler_offisiell_v" not in f)
    ut[f"{NAVN}/FROSNE_SHA256.txt"] = sha_bytes(linjer.encode())
    for sti in sorted(ut):
        print(f"{ut[sti]}  {sti}")
    print(f"{len(ut)} filer", file=sys.stderr)


if __name__ == "__main__":
    main()
