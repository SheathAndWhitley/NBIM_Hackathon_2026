"""Skriver resultatet av sh KJOR.sh: F1, presisjon og recall på stemmer MOT styret i test 2026 for agenten og to
grunnlinjer, alle målt med maaling/maaler.py på samme fasit. Kjøres av KJOR.sh etter agenten."""
import csv, os, re, subprocess, sys, tempfile

HER = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.dirname(HER)
MAALER = os.path.join(HER, "maaler.py")
LINJE = re.compile(r"MOT mot styret: TP (\d+) FP (\d+) FN (\d+)\s+P ([\d.]+)\s+R ([\d.]+)\s+F1 ([\d.]+)\s+\((\d+) i fasit\)")


def maal(svarfil):
    o = subprocess.run([sys.executable, "-I", MAALER, svarfil, "test", "--score", "mot"], capture_output=True, text=True)
    m, n = LINJE.search(o.stdout), re.search(r"(\d+) vurderte rader", o.stdout)
    if o.returncode or not m or not n:
        sys.exit("FEIL i målingen:\n" + o.stdout + o.stderr)
    return dict(TP=int(m[1]), FP=int(m[2]), FN=int(m[3]), P=float(m[4]), R=float(m[5]), F1=float(m[6]),
                mot=int(m[7]), n=int(n[1]))


def tall(x, d=3):
    return f"{x:.{d}f}".replace(".", ",")


def main():
    sys.path.insert(0, HER)
    import grunnlinje_gjenta_forrige as gf
    agent = list(csv.DictReader(open(os.path.join(ROT, "ut/agent.csv"), encoding="utf-8")))
    with tempfile.TemporaryDirectory(prefix="oppsummer_") as tmp:
        styret = os.path.join(tmp, "folg_styret.csv")
        with open(styret, "w", newline="") as f:
            w = csv.writer(f); w.writerow(["id", "anbefaling"]); w.writerows([r["id"], 0] for r in agent)
        regel = os.path.join(tmp, "gjenta_forrige.csv")
        gf.skriv_svar(gf.svar(), "2026", regel)
        rader = [("Følg styret", maal(styret)), ("Gjenta forrige beslutning", maal(regel)),
                 ("Agenten", maal(os.path.join(ROT, "ut/pred_maaler.csv")))]
    a = rader[-1][1]
    print(f"Test 2026: {a['n']} saker med fasit. NBIM stemte MOT styret i {a['mot']} av dem "
          f"({tall(100 * a['mot'] / a['n'], 1)} %).")
    print()
    print(f"  {'':28}{'F1 MOT':>8}{'presisjon':>12}{'recall':>10}{'funnet':>12}{'falske MOT':>13}")
    for navn, r in rader:
        p = tall(100 * r["P"], 1) + " %" if r["TP"] + r["FP"] else "–"
        print(f"  {navn:28}{tall(r['F1']):>8}{p:>12}{tall(100 * r['R'], 1) + ' %':>10}"
              f"{str(r['TP']) + ' av ' + str(r['mot']):>12}{r['FP']:>13}")
    print()
    print("  presisjon: andel av MOT-flaggene som var riktige")
    print("  recall:    andel av NBIMs MOT-stemmer som ble funnet")
    menneske = sum(r["til_menneske"] == "1" for r in agent)
    print()
    print(f"  Agenten sender {menneske} av {len(agent)} saker ({tall(100 * menneske / len(agent), 1)} %) til et menneske.")
    print("  Forventet F1 for agenten: 0,512 på macOS, 0,520 på Linux (samme kode og data).")


if __name__ == "__main__":
    main()
