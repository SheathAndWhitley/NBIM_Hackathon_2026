"""Frysvakt for Case 1 (arkitekt #2142, ordre #222: modellfrys kl. 16).

  frys   skriver sha256 for de frosne filene til state/c1_frys.json (kl. 16, LaunchAgent).
         Finnes fila fra før, røres den ikke (--tving overskriver, skriv hvorfor i tavla).
  sjekk  sammenligner filene med state/c1_frys.json. Avvik eller manglende fil: tydelig
         melding og utgang 2. Ikke frosset ennå: melding og utgang 0 (--krev gir utgang 2).
  status én linje for tavla (tom hvis ikke frosset, ellers OK eller !! med filene som avviker).

  --rot DIR  sjekk/frys en kopi med samme relative stier (test, kald kopi).
  --frys F   annen frysfil (test).
  Miljø (bare test, generalprøve #2174): C1_FRYS=<frysfil>, C1_FRYS_ROT=<rot> virker også når
  kaldstart.sh/fremmed.sh kaller verktøyet uten flagg.
Kalles av arbeid/hack/c1/kaldstart.sh og arbeid/hack/levering/fremmed.sh før kopiering.
"""
import argparse, datetime, hashlib, json, os, sys

LAND = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FRYSFIL = os.environ.get("C1_FRYS") or os.path.join(LAND, "state/c1_frys.json")  # C1_FRYS: bare for test
# frossen modell #2044 miks h2 (case1_frys_valg.md, kandidater/FROSSEN.md) og agenten som kjører den
FILER = [
    "arbeid/oppgave_2044/train.py",                       # modellen, kjøres uendret med runpy
    "arbeid/oppgave_2044/pred_miks_h2.csv",               # prediksjonene fra #2044
    "arbeid/oppgave_2103/full_test.csv",                  # frosne testprediksjoner (hovedtallet 0,476)
    "arbeid/hack/levering/kjor_agent.py",                 # agentfila
    "arbeid/hack/levering/c1_real.py",
    "arbeid/hack/levering/modell_repo4.py",  # #2572 bytte til repo4
    "arbeid/hack/levering/stemmeagent/__init__.py",  # #2572 bytte til repo4
    "arbeid/hack/levering/stemmeagent/ballot.py",  # #2572 bytte til repo4
    "arbeid/hack/levering/stemmeagent/config.py",  # #2572 bytte til repo4                    # agentens modellkall (kalibrering, grense)
    "arbeid/hack/levering/injeksjon_hoflig.py",           # høflighetsvakta (#2237), importeres av c1_real.py
    "arbeid/hack/levering/kjor_agent_real_maskin_alene.csv",  # agentens maskin-alene-svar
    "arbeid/oppgave_2047/vern.py",
    "arbeid/oppgave_2046/case1_mot.py",
    "state/opplastet/20261105_114241_real_votes.csv",     # dataene modellen trenes på
    # sporet i kald kjøring (#2337, audit-hook på open/import/subprocess): agenten leser disse også
    "arbeid/hack/levering/retningslinje_oppslag.py",      # sitatene (importeres av kjor_agent/c1_real)
    "arbeid/hack/c1/retningslinjer/punkter.jsonl",        # retningslinjepunktene som siteres
    "arbeid/hack/c1/data_off/real_test_input.csv",        # standard inn: test 2026 uten fasit
    "arbeid/hack/c1/maaler_offisiell_v2.py",              # måleren agenten kaller (SCORE, ruting)
    "arbeid/hack/c1/maaler_offisiell_v3.py",              # hovedtallet F1 MOT i fremmed.sh
    "arbeid/kandidater/smed2_c1_mot/pyproject.toml",      # låste pakkeversjoner for kald kopi
    "arbeid/kandidater/smed2_c1_mot/uv.lock",
]


def sha(sti):
    h = hashlib.sha256()
    with open(sti, "rb") as f:
        for bit in iter(lambda: f.read(1 << 20), b""):
            h.update(bit)
    return h.hexdigest()


def avvik(rot, frys):
    """Liste med (fil, hva) som avviker fra frysen."""
    ut = []
    for f, h in frys["filer"].items():
        sti = os.path.join(rot, f)
        if not os.path.exists(sti):
            ut.append((f, "MANGLER"))
        elif sha(sti) != h:
            ut.append((f, f"ENDRET (frosset {h[:12]}, nå {sha(sti)[:12]})"))
    return ut


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("kommando", choices=["frys", "sjekk", "status"])
    p.add_argument("--rot", default=os.environ.get("C1_FRYS_ROT") or LAND)
    p.add_argument("--frys", default=FRYSFIL)
    p.add_argument("--tving", action="store_true")
    p.add_argument("--krev", action="store_true")
    a = p.parse_args(argv)

    if a.kommando == "frys":
        if os.path.exists(a.frys) and not a.tving:
            print(f"frys: {a.frys} finnes alt, rører den ikke (--tving for å overskrive)")
            return 0
        mangler = [f for f in FILER if not os.path.exists(os.path.join(a.rot, f))]
        if mangler:
            print("FRYS FEILET: mangler " + ", ".join(mangler))
            return 2
        d = {"tid": datetime.datetime.now().isoformat(timespec="seconds"),
             "modell": "#2044 miks h2", "rot": a.rot,
             "filer": {f: sha(os.path.join(a.rot, f)) for f in FILER}}
        os.makedirs(os.path.dirname(a.frys), exist_ok=True)
        with open(a.frys, "w") as f:
            json.dump(d, f, indent=1, ensure_ascii=False)
        print(f"FROSSET {d['tid']}: {len(FILER)} filer til {a.frys}")
        return 0

    if not os.path.exists(a.frys):
        if a.kommando == "status":
            return 0
        print(f"FRYSVAKT: ikke frosset ennå ({a.frys} finnes ikke)" + (", --krev: STOPP" if a.krev else ""))
        return 2 if a.krev else 0
    with open(a.frys) as f:
        frys = json.load(f)
    av = avvik(a.rot, frys)
    if a.kommando == "status":
        if av:
            print(f"!! FRYSVAKT: {len(av)} frosne Case 1-filer endret etter frys {frys['tid']}: "
                  + ", ".join(f"{os.path.basename(f)} {h.split()[0]}" for f, h in av))
        else:
            print(f"Frysvakt: {len(frys['filer'])} filer uendret siden frys {frys['tid']}")
        return 0
    if av:
        print("=" * 70)
        print(f"FRYSVAKT RØD: {len(av)} frosne filer avviker fra frysen {frys['tid']} ({a.frys})")
        for f, h in av:
            print(f"  {f}: {h}")
        print("STOPP: modellen/prediksjonene er endret etter modellfrys kl. 16 (ordre #222).")
        print("Rull tilbake (git diff/checkout på fila) eller få skriftlig ja fra dommeren før ny frys.")
        print("=" * 70)
        return 2
    print(f"FRYSVAKT GRØNN: {len(frys['filer'])} filer like som ved frys {frys['tid']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
