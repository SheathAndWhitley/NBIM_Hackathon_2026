"""Case 1-måler (#1947): tidssplitt på møtedato, baselines og MOT-metrikker. Bare stdlib.

Steg 1, én gang når votes.csv finnes (fra #1946):
    python3 -I arbeid/hack/c1/maaler.py split arbeid/hack/c1/data/votes.csv [--andel 0.2] [--selskap strikt|historikk]
  skriver i samme mappe som votes.csv:
    train.csv        alle kolonner, møter før grensen (lov å trene på)
    test_input.csv   holdout uten svaret (id + forslagsdata + styret) - det smedene predikerer på
    fasit.csv        id, fasit (FOR/MOT/AVSTÅ), styret, moetedato, cusip
    split_info.txt   grense, antall, hva som ble fjernet
Steg 2, mål en prediksjonsfil (id, anbefaling, konfidens):
    python3 -I arbeid/hack/c1/maaler.py PRED.csv [--fasit arbeid/hack/c1/data/fasit.csv] [--terskel 0.6]
  Siste linje: SCORE <F1 på MOT, hele holdout>. Høyere er bedre.
Baselines:
    python3 -I arbeid/hack/c1/maaler.py baseline [--fasit ...]   (skriver pred_folg_styret.csv og pred_alltid_for.csv og måler dem)

Definisjoner (låst):
- MOT = stemme AGAINST eller WITHHOLD (som baseline.py fra arrangøren). FOR = FOR. AVSTÅ = ABSTAIN.
  Andre verdier (1 YEAR, DO NOT VOTE, ...) tas ikke med i holdout; antallet står i split_info.txt.
- Enhet = forslag (cusip, moetedato, forslagstekst). Samme forslag fra flere fond slås sammen; stemmer
  fondene ulikt, gjelder flertallet, og antallet uenige rapporteres.
- Holdout = siste --andel av forslagene etter møtedato. Hele møtedagen havner på én side (ingen møte deles).
  --selskap strikt (standard): selskaper (cusip, ellers utsteder) som finnes i holdout fjernes fra train,
  så ingen selskapshistorikk krysser grensen. «historikk» beholder tidligere møter for samme selskap.
- Ruting: konfidens < --terskel betyr «til menneske». Metrikkene for de ikke-rutede er det maskinen
  står for alene. SCORE regnes på anbefalingen for alle rader, uavhengig av ruting.
- Mangler en id, duplikat-id, ukjent anbefaling eller konfidens utenfor [0,1]: UGYLDIG, exit 1.
"""
import csv, hashlib, os, sys
from collections import Counter, defaultdict

HER = os.path.dirname(os.path.abspath(__file__))
STD_FASIT = os.path.join(HER, "data", "fasit.csv")
MOT = {"against", "mot", "withhold"}
FOR = {"for"}
AVSTAA = {"abstain", "avstå", "avsta"}
STYRET_KOL = ["styret", "ledelsen", "managementRecommendation", "management_recommendation", "mgmt_rec", "styre"]
SELSKAP_KOL = ["cusip", "isin", "utsteder"]
DATO_KOL = ["moetedato", "meetingDate", "dato"]
FORSLAG_KOL = ["forslag", "voteDescription"]
STEMME_KOL = ["stemme", "howVoted", "vote"]
# Avledet av svaret (hent_votes.py): aldri med i test_input.
LEKK_KOL = {"mot_ledelsen", "delt", "n_rec"}
ANB = {"FOR": "FOR", "MOT": "MOT", "AVSTÅ": "AVSTÅ", "AVSTA": "AVSTÅ", "AGAINST": "MOT", "ABSTAIN": "AVSTÅ"}


def ugyldig(grunn):
    print(f"UGYLDIG {grunn}", file=sys.stderr); print("SCORE nan"); sys.exit(1)


def flagg(argv, navn, std=None):
    if navn in argv:
        i = argv.index(navn)
        return argv[i + 1]
    return std


def kol(felt, kandidater, paakrevd=True):
    for k in kandidater:
        if k in felt:
            return k
    if paakrevd:
        raise SystemExit(f"fant ingen av kolonnene {kandidater} i {felt}")
    return None


def klasse(v):
    v = (v or "").strip().lower()
    if v in MOT: return "MOT"
    if v in FOR: return "FOR"
    if v in AVSTAA: return "AVSTÅ"
    return None


def dato(v):
    """Normaliser til ISO. Tåler 2025-05-14, 05/14/2025 og 2025-05-14T00:00."""
    v = (v or "").strip()[:10]
    if len(v) == 10 and v[2] == "/" and v[5] == "/":
        return f"{v[6:]}-{v[:2]}-{v[3:5]}"
    return v


def les(sti):
    with open(sti, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def skriv(sti, rader, felt):
    with open(sti, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=felt, extrasaction="ignore")
        w.writeheader(); w.writerows(rader)


def split(argv):
    sti = argv[0]
    andel = float(flagg(argv, "--andel", "0.2"))
    modus = flagg(argv, "--selskap", "strikt")
    rader = les(sti)
    felt = list(rader[0])
    kd, kf, ks = kol(felt, DATO_KOL), kol(felt, FORSLAG_KOL), kol(felt, STEMME_KOL)
    ksel, kst = kol(felt, SELSKAP_KOL), kol(felt, STYRET_KOL, paakrevd=False)
    # Slå sammen samme forslag fra flere fond.
    grupper = defaultdict(list)
    for r in rader:
        selskap = (r.get(ksel) or r.get("utsteder") or "").strip().upper()
        grupper[(selskap, dato(r[kd]), " ".join(r[kf].split()).lower())].append(r)
    forslag, uenige, andre = [], 0, Counter()
    for (selskap, d, _), rs in grupper.items():
        stemmer = Counter(klasse(r[ks]) for r in rs)
        if None in stemmer:
            for r in rs:
                if klasse(r[ks]) is None: andre[r[ks].strip().upper()] += 1
        gyldige = Counter({k: n for k, n in stemmer.items() if k})
        if len(gyldige) > 1: uenige += 1
        r = dict(rs[0]); r["_selskap"] = selskap; r["_dato"] = d
        r["fasit"] = gyldige.most_common(1)[0][0] if gyldige else ""
        r["antall_fond"] = len(rs)
        nokkel = f"{selskap}|{d}|{r[kf]}"
        r["id"] = r.get("id") or hashlib.sha1(nokkel.encode()).hexdigest()[:12]
        forslag.append(r)
    forslag.sort(key=lambda r: (r["_dato"], r["id"]))
    datoer = sorted({r["_dato"] for r in forslag})
    # Grensedato: første dato der minst (1-andel) av forslagene ligger før.
    maal, n, grense = (1 - andel) * len(forslag), 0, datoer[-1]
    per_dato = Counter(r["_dato"] for r in forslag)
    for d in datoer:
        if n >= maal:
            grense = d; break
        n += per_dato[d]
    test = [r for r in forslag if r["_dato"] >= grense and r["fasit"]]
    train = [r for r in forslag if r["_dato"] < grense]
    test_selskap = {r["_selskap"] for r in test}
    fjernet = 0
    if modus == "strikt":
        foer = len(train)
        train = [r for r in train if r["_selskap"] not in test_selskap]
        fjernet = foer - len(train)
    ut = os.path.dirname(os.path.abspath(sti))
    tfelt = ["id"] + [k for k in felt if k != "id"] + ["fasit", "antall_fond"]
    skriv(os.path.join(ut, "train.csv"), train, tfelt)
    skriv(os.path.join(ut, "test_input.csv"), test, ["id"] + [k for k in felt if k not in ("id", ks) and k not in LEKK_KOL] + ["antall_fond"])
    for r in test:
        r["styret"] = r.get(kst, "") if kst else ""
        r["moetedato"] = r["_dato"]; r["cusip"] = r["_selskap"]
    skriv(os.path.join(ut, "fasit.csv"), test, ["id", "fasit", "styret", "moetedato", "cusip"])
    tf = Counter(r["fasit"] for r in train); hf = Counter(r["fasit"] for r in test)
    info = [f"kilde {sti}: {len(rader)} rader, {len(forslag)} unike forslag, {uenige} med uenige fond",
            f"grense moetedato >= {grense} (andel {andel}), selskap-modus {modus}",
            f"train {len(train)} forslag {dict(tf)}, datoer {train[0]['_dato'] if train else '-'}..{train[-1]['_dato'] if train else '-'}",
            f"holdout {len(test)} forslag {dict(hf)}, datoer {test[0]['_dato']}..{test[-1]['_dato']}",
            f"fjernet fra train fordi selskapet er i holdout: {fjernet}",
            f"styret-kolonne: {kst or 'MANGLER (følg styret-baseline blir alltid FOR)'}",
            f"andre stemmeverdier holdt utenfor: {dict(andre.most_common(8))}",
            f"overlapp selskap train/holdout: {len({r['_selskap'] for r in train} & test_selskap)}"]
    open(os.path.join(ut, "split_info.txt"), "w").write("\n".join(info) + "\n")
    print("\n".join(info))


def prf(par):
    tp = sum(1 for p, f in par if p == "MOT" and f == "MOT")
    fp = sum(1 for p, f in par if p == "MOT" and f != "MOT")
    fn = sum(1 for p, f in par if p != "MOT" and f == "MOT")
    pr = tp / (tp + fp) if tp + fp else 0.0
    re = tp / (tp + fn) if tp + fn else 0.0
    return pr, re, (2 * pr * re / (pr + re) if pr + re else 0.0), tp, fp, fn


def maal(pred_sti, fasit_sti, terskel, stille=False):
    fasit = {r["id"]: r for r in les(fasit_sti)}
    pred = {}
    for r in les(pred_sti):
        i = (r.get("id") or "").strip()
        if i in pred: ugyldig(f"duplikat id {i}")
        a = ANB.get((r.get("anbefaling") or "").strip().upper())
        if a is None: ugyldig(f"ukjent anbefaling {r.get('anbefaling')!r} for id {i}")
        try: k = float(r.get("konfidens", ""))
        except ValueError: ugyldig(f"konfidens ikke tall for id {i}")
        if not 0 <= k <= 1: ugyldig(f"konfidens {k} utenfor [0,1] for id {i}")
        pred[i] = (a, k)
    mangler = [i for i in fasit if i not in pred]
    if mangler: ugyldig(f"{len(mangler)} id-er i holdout mangler, f.eks. {mangler[:3]}")
    ekstra = len(set(pred) - set(fasit))
    alle = [(pred[i][0], fasit[i]["fasit"]) for i in fasit]
    pr, re, f1, tp, fp, fn = prf(alle)
    ikke_rutet = [(pred[i][0], fasit[i]["fasit"]) for i in fasit if pred[i][1] >= terskel]
    rutet = len(alle) - len(ikke_rutet)
    pr2, re2, f12, *_ = prf(ikke_rutet)
    # Med menneske: antar at mennesket treffer på rutede saker (øvre grense for samspillet).
    med = [(fasit[i]["fasit"] if pred[i][1] < terskel else pred[i][0], fasit[i]["fasit"]) for i in fasit]
    pr3, re3, f13, *_ = prf(med)
    mot_rutet = sum(1 for i in fasit if pred[i][1] < terskel and fasit[i]["fasit"] == "MOT")
    n_mot = sum(1 for _, f in alle if f == "MOT")
    # Mot styret: ble det stemt annerledes enn styret anbefalte, og fanget vi det?
    st = [(pred[i][0], fasit[i]) for i in fasit if klasse(fasit[i].get("styret"))]
    avvik = [(p != (klasse(f["styret"])), f["fasit"] != klasse(f["styret"])) for p, f in st]
    atp = sum(1 for p, f in avvik if p and f); afp = sum(1 for p, f in avvik if p and not f)
    afn = sum(1 for p, f in avvik if not p and f)
    acc = sum(1 for p, f in alle if p == f) / len(alle)
    if not stille:
        print(f"holdout {len(alle)} forslag, {n_mot} MOT ({n_mot / len(alle):.1%}), ekstra id-er ignorert: {ekstra}")
        print(f"accuracy (ikke bruk alene)  {acc:.4f}")
        print(f"MOT presisjon {pr:.4f}  recall {re:.4f}  F1 {f1:.4f}  (tp {tp} fp {fp} fn {fn})")
        print(f"rutet til menneske (konfidens < {terskel}): {rutet} = {rutet / len(alle):.1%}, derav MOT {mot_rutet}")
        print(f"ikke-rutet: MOT presisjon {pr2:.4f}  recall {re2:.4f}  F1 {f12:.4f}  (n {len(ikke_rutet)})")
        print(f"maskin+menneske (menneske treffer på rutede): MOT recall {re3:.4f}  F1 {f13:.4f}")
        if st:
            apr = atp / (atp + afp) if atp + afp else 0.0; are = atp / (atp + afn) if atp + afn else 0.0
            af1 = 2 * apr * are / (apr + are) if apr + are else 0.0
            print(f"mot styret: {sum(f for _, f in avvik)} av {len(st)} avviker fra styret; "
                  f"fanget presisjon {apr:.4f} recall {are:.4f} F1 {af1:.4f}")
        print(f"SCORE {f1:.6f}")
    return f1


def baseline(argv):
    fasit_sti = flagg(argv, "--fasit", STD_FASIT)
    terskel = float(flagg(argv, "--terskel", "0.6"))
    ut = os.path.dirname(os.path.abspath(fasit_sti))
    fasit = les(fasit_sti)
    for navn, f in [("folg_styret", lambda r: klasse(r.get("styret")) or "FOR"), ("alltid_for", lambda r: "FOR")]:
        sti = os.path.join(ut, f"pred_{navn}.csv")
        skriv(sti, [{"id": r["id"], "anbefaling": f(r), "konfidens": 1.0} for r in fasit], ["id", "anbefaling", "konfidens"])
        print(f"=== baseline {navn} ({sti})")
        maal(sti, fasit_sti, terskel)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"): raise SystemExit(__doc__)
    if a[0] == "split": split(a[1:])
    elif a[0] == "baseline": baseline(a[1:])
    else: maal(a[0], flagg(a, "--fasit", STD_FASIT), float(flagg(a, "--terskel", "0.6")))
