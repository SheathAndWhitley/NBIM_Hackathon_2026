"""Tallvakt for Case 1 (#2131): sjekker at hovedtallet i pakka stemmer med måleren.

Kjører måler v3 --score mot på den leverte svarfila, leser «MOT mot styret»-linja (TP/FP/FN, P, R, F1)
og greper levering/*.md og c1/leveranse/*.md etter påstander om det tallet:
  - «TP a FP b FN c» på linjer om MOT (ikke «streng MOT», ikke «avvik:»)
  - «F1 <tall> ... MOT» (F1 på MOT), f.eks. «F1 **0,476 på MOT mot styret**», «F1 MOT 0,476»
  - «P <tall>», «R <tall>», «presisjon <tall>», «recall <tall>» på linjer som også har en hovedtall-påstand
  - «<n> MOT mot styret» / «<n> i fasit» (antall MOT i test)
  - tabellrader «maskin alene»/«hovedtall» under en kolonnerad med presisjon | recall | F1
Et tall godtas når det er måletallet avrundet til samme antall desimaler.
Unntak: påstander med eldre/avvik/val/2025/N-PX/h1/utentype/uten sakstype/ikke hovedtall like foran
(eller etter) tallet, og linjer med «tallvakt: ignorer». Det er tall om noe annet enn hovedtallet.

  - (#2136) «<n> MOT»/«<n> MOT-stemmer» = 58, «<n> avvik fra styret/med AVSTÅ» = 66, og «X av Y (p %)» på
    linjer om menneske: Y = saker inn eller med fasit, X og p fra agentens KJORING.txt (--kjoring)
Bruk:  python3 -I arbeid/verktoy/c1_tallvakt.py [--rot LANDSBY] [--svar SVAR.csv] [--kjoring KJORING.txt] [--vis] [fil.md ...]
       --vis lister også påstandene som stemmer.
Utgang 0 = OK, 1 = avvik funnet, 2 = måleren feilet.
"""
import glob, os, re, subprocess, sys

ROT = "."
SVAR = "arbeid/hack/levering/kjor_agent_real_maskin_alene.csv"
MAALER = "arbeid/hack/c1/maaler_offisiell_v3.py"
KJORING = "arbeid/hack/levering/kjor_agent_real_test2026.txt"  # agentens logg: saker inn og til menneske
FILER = ["arbeid/hack/levering/*.md", "arbeid/hack/c1/leveranse/*.md", "arbeid/hack/c1/*.md"]  # c1/*.md fra #2665
NUM = r"(\d+[,.]\d+)"
UNNTAK = re.compile(r"eldre|avvik|\bval\b|val-|2025|N-PX|\bh1\b|utentype|uten sakstype|ikke hovedtall|"
                    r"uten løpende|historikkregel|streng MOT|ruting|rute|små|store|tidligere år", re.I)


def maal(rot, svar):
    cmd = [sys.executable, "-I", os.path.join(rot, MAALER), svar, "test", "--data", "real", "--score", "mot"]
    ut = subprocess.run(cmd, capture_output=True, text=True, timeout=50).stdout
    m = re.search(r"MOT mot styret: TP (\d+) FP (\d+) FN (\d+)\s+P ([\d.]+)\s+R ([\d.]+)\s+F1 ([\d.]+)\s+\((\d+) i fasit\)", ut)
    if not m:
        print(ut); print("FEIL: fant ikke «MOT mot styret»-linja i måleren"); sys.exit(2)
    tp, fp, fn = map(int, m.group(1, 2, 3))
    v = re.search(r"(\d+) vurderte rader, (\d+) avvik fra styret", ut)
    return ut, {"TP": tp, "FP": fp, "FN": fn, "P": float(m[4]), "R": float(m[5]), "F1": float(m[6]), "N": int(m[7]),
                "vurdert": int(v[1]) if v else None, "avvik": int(v[2]) if v else None}


def kjoring(sti, M):
    """Leser agentens KJORING.txt (#2136): saker inn og til menneske, og målerens ruting på saker med fasit."""
    t = open(sti, encoding="utf-8").read()
    m = re.search(r"inn: (\d+) saker;.*?til menneske (\d+) \(([\d.]+)%\)", t)
    r = re.findall(r"vurderte rader.*?\n(?:.*\n)*?.*?ruting[^:]*: (\d+) til menneske \(([\d.]+)%\)", t)
    if not m: print(f"FEIL: fant ikke «inn: N saker; ... til menneske R (p%)» i {sti}"); sys.exit(2)
    M["inn"], M["men_inn"], M["men_inn_pst"] = int(m[1]), int(m[2]), float(m[3])
    if r: M["men_fasit"], M["men_fasit_pst"] = int(r[-1][0]), float(r[-1][1])


def stemmer(tekst, sann):
    x = float(tekst.replace(",", ".")); d = len(re.split(r"[,.]", tekst)[1])
    return abs(x - sann) <= 0.5 * 10 ** -d + 1e-9


def unntatt(linje, a, b, foran=45, etter=25):
    return bool(UNNTAK.search(linje[max(0, a - foran):a] + " " + linje[b:b + etter]))


def sjekk_linje(linje, M):
    """Gir (påstander, avvik): lister av (navn, tall, sann)."""
    rent = linje.replace("*", "")
    paa, avv = [], []

    def vurder(navn, tekst, sann):
        (paa if stemmer(tekst, sann) else avv).append((navn, tekst, sann))

    for m in re.finditer(r"TP (\d+),? FP (\d+),? FN (\d+)", rent):
        foran = rent[max(0, m.start() - 40):m.start()]
        if re.search(r"streng MOT|avvik:|avvik fra", foran, re.I) or "MOT" not in rent: continue
        if unntatt(rent, m.start(), m.end(), 25, 0): continue
        sett = tuple(map(int, m.groups()))
        (paa if sett == (M["TP"], M["FP"], M["FN"]) else avv).append(("TP/FP/FN", " ".join(map(str, sett)), (M["TP"], M["FP"], M["FN"])))
    for m in re.finditer(r"F1(?: MOT| på MOT[^0-9]{0,25}?| for maskinen alene er| =)? " + NUM, rent):
        etter = rent[m.end():m.end() + 45]
        om_mot = "MOT" in m.group(0) or re.match(r"\s*(\[[^\]]*\]|\([^)]*\))?[\s,]*(på|on) MOT", etter)
        if not om_mot and not re.search(r"MOT mot styret: TP", rent[:m.start()]): continue
        if re.match(r"\s*(\[[^\]]*\]|\([^)]*\))?[\s,]*på avvik", etter): continue
        if unntatt(rent, m.start(), m.end(), 70, 0): continue
        vurder("F1", m[1], M["F1"])
    for m in re.finditer(r"(?<![\w,.–-])(\d+) (?:MOT mot styret|i fasit\)|ekte MOT|(?:av dem )?MOT(?:-stemmer|-saker)? i (?:test|fasit)|MOT[;)]|MOT, P|av dem MOT)"
                         r"|(?:bare (\d+) MOT-(?:stemmer|saker)|av (\d\d+) MOT-stemmer)(?! på)", rent):
        if unntatt(rent, m.start(), m.end(), 30, 0): continue
        n = int(m[1] or m[2] or m[3]); (paa if n == M["N"] else avv).append(("antall MOT", str(n), M["N"]))
    if M.get("avvik") is not None:  # avvik fra styret i fasit (MOT + AVSTÅ), ikke det samme som MOT (#2136)
        for m in re.finditer(r"(?<![\d,.])(\d+) (?:ekte )?avvik(?: fra styret| med AVSTÅ| inkl)", rent):
            if re.search(r"eldre|N-PX|\bval\b|2025", rent[max(0, m.start() - 30):m.start()]): continue
            n = int(m[1]); (paa if n == M["avvik"] else avv).append(("antall avvik", str(n), M["avvik"]))
    if "inn" in M and re.search(r"menneske", rent, re.I):  # andel til menneske (#2136)
        for m in re.finditer(r"(?<![\d,.])(\d+) av (?:de )?(\d+)(?: saker)?(?: inn| med fasit)?(?:\s*\((\d+[,.]\d+) ?%\))?", rent):
            if re.search(r"eldre|N-PX|\bval\b|2025", rent[max(0, m.start() - 30):m.start()]): continue
            x, y = int(m[1]), int(m[2])
            sann = {M["inn"]: (M["men_inn"], M["men_inn_pst"]),
                    M.get("vurdert"): (M.get("men_fasit"), M.get("men_fasit_pst"))}.get(y)
            if not sann or sann[0] is None: continue
            (paa if x == sann[0] else avv).append(("til menneske", f"{x} av {y}", sann[0]))
            if m[3]: vurder("til menneske %", m[3], sann[1])
    if paa or avv:  # P og R bare der linja ellers handler om hovedtallet
        for m in re.finditer(r"(?<![\w.])(P|R|presisjon|recall) " + NUM + r"( ?%)?", rent):
            if unntatt(rent, m.start(), m.end(), 25, 0): continue
            navn = "P" if m[1] in ("P", "presisjon") else "R"  # «recall 51,7 %» er prosent (#2170)
            vurder(navn, m[2], M[navn] * (100 if m[3] else 1))
    return paa, avv


ANNEN_KOLONNE = re.compile(r"menneske \+|gulv|øvre|alternativ", re.I)  # tall om noe annet enn maskinens hovedtall


def sjekk_rad(celler, hode, M):
    """Tabellrad uten presisjon|F1-kolonner (#2136): hver celle sjekkes for seg med kolonnens overskrift.
    Kolonner om maskin + menneske/gulv hoppes over; andel til menneske sjekkes bare i standardraden."""
    paa, avv = [], []
    for i, c in enumerate(celler):
        h = hode[i] if i < len(hode) else ""
        if i == 0 or ANNEN_KOLONNE.search(h): continue
        if "menneske" in h.lower():
            if not re.search(r"standard", celler[0], re.I): continue
            p, a = sjekk_linje(f"{c} til menneske", M)
        else:
            p, a = sjekk_linje(f"{c} på MOT mot styret" if re.search(r"F1|TP", c) else c, M)
        paa += p; avv += a
    return paa, avv


def sjekk_fil(sti, M):
    paa, avv, kol, hode = [], [], None, None
    for nr, linje in enumerate(open(sti, encoding="utf-8"), 1):
        if "tallvakt: ignorer" in linje: continue
        if linje.lstrip().startswith("|"):
            celler = [c.strip().replace("*", "") for c in linje.strip().strip("|").split("|")]
            lav = [c.lower() for c in celler]
            if all(re.fullmatch(r":?-+:?", c) for c in celler if c): continue
            if hode is None:
                hode = celler
            if any("presisjon" in c for c in lav) and any("f1" in c for c in lav):
                kol = {n: i for i, c in enumerate(lav) for n, k in (("P", "presisjon"), ("R", "recall"), ("F1", "f1")) if k in c}
                continue
            if kol and re.search(r"maskin alene|hovedtall", celler[0], re.I) and not UNNTAK.search(celler[0]):
                for n, i in kol.items():
                    t = re.match(NUM, celler[i]) if i < len(celler) else None
                    if t:
                        (paa if stemmer(t[1], M[n]) else avv).append((nr, n, t[1], M[n], linje))
                continue
            if not kol and celler is not hode:
                p, a = sjekk_rad(celler, hode, M)
                paa += [(nr, *x, linje) for x in p]; avv += [(nr, *x, linje) for x in a]
                continue
        else:
            kol, hode = None, None
        p, a = sjekk_linje(linje, M)
        paa += [(nr, *x, linje) for x in p]; avv += [(nr, *x, linje) for x in a]
    return paa, avv


def main(a):
    rot, svar, filer, vis, kj = ROT, None, [], False, None
    while a:
        x = a.pop(0)
        if x == "--rot": rot = a.pop(0)
        elif x == "--svar": svar = a.pop(0)
        elif x == "--kjoring": kj = a.pop(0)
        elif x == "--vis": vis = True
        elif x in ("-h", "--help"): print(__doc__); return 0
        else: filer.append(x)
    svar = svar or os.path.join(rot, SVAR)
    filer = filer or sorted(f for g in FILER for f in glob.glob(os.path.join(rot, g)))
    ut, M = maal(rot, svar)
    kjoring(kj or os.path.join(rot, KJORING), M)
    print(f"Måler v3 --score mot på {os.path.relpath(svar, rot)}: F1 {M['F1']:.4f}  P {M['P']:.4f}  R {M['R']:.4f}"
          f"  TP {M['TP']} FP {M['FP']} FN {M['FN']}  ({M['N']} MOT i fasit, {M['avvik']} avvik)")
    print(f"Kjøring: til menneske {M['men_inn']} av {M['inn']} inn ({M['men_inn_pst']}%)"
          + (f", {M['men_fasit']} av {M['vurdert']} med fasit ({M['men_fasit_pst']}%)" if "men_fasit" in M else ""))
    n_paa = n_avv = 0
    for f in filer:
        paa, avv = sjekk_fil(f, M)
        n_paa += len(paa); n_avv += len(avv)
        for nr, navn, tekst, sann, linje in paa * vis:
            print(f"ok    {os.path.relpath(f, rot)}:{nr}: {navn} {tekst}")
        for nr, navn, tekst, sann, linje in avv:
            print(f"AVVIK {os.path.relpath(f, rot)}:{nr}: {navn} {tekst}, måleren sier {sann}\n      {linje.strip()[:200]}")
    print(f"{len(filer)} filer, {n_paa} påstander om hovedtallet stemmer, {n_avv} avviker")
    print("OK" if n_avv == 0 else "FEIL: rett tallene over eller merk linja «eldre»/«tallvakt: ignorer»")
    return 0 if n_avv == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
