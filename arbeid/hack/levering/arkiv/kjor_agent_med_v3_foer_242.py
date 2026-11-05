"""Case 1, hele stemmeagenten med én kommando (smed #1998, real_votes som standard fra #2053).

STANDARD (#2053): NBIMs egne stemmer (real_votes) med smed2s MOT-modell (#2044), se c1_real.py:
  uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut /tmp/c1_ut
  måler test 2026 med maaler_offisiell_v2.py. --csv / --sak tar saker i real_votes-format.
GAMMEL (--data v3): N-PX-agenten under, uendret.

Inn: én sak (--sak JSON) eller en CSV i formatet til hack/c1/data_v3/test_input.csv (--csv).
Ut (i --ut, gjerne en tom mappe): agent.csv med stemmeforslag, P(MOT), ruting til menneske,
punkt-id og ordrett sitat, pluss pred_maaler.csv (format for hack/c1/maaler.py) og KJORING.txt.

Delene brukes uendret, de skrives ikke om:
  modell  arbeid/kandidater/smed2_c1_mot/train_v3.py, variant --lekkasjefri (dommer #1988 b,
          #1997): LightGBM 5 frø, isotonisk P(MOT), rå grense valgt på val 2025 (velg_grense).
  ruting  case1_ruting.md, strategi A: saken går til menneske når |logit(rå) - logit(grense)|
          ligger i båndet som rutet 10 % av val 2025 (--til-menneske PROSENT endrer andelen).
          Båndet låses på val og brukes uendret.
  sitat   arbeid/hack/varianter/smed3_utf_sitat/agent.py (punkt-id, sitat, grunn). Kilden er
          Vanguards «Proxy voting policy for U.S. portfolio companies» (feb 2025), ikke NBIM.

Bruk (fra landsbymappen):
  uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut /tmp/c1_ut
  ... --csv min_fil.csv --ut DIR        ... --sak '{"utsteder": "...", "cusip": "...", ...}' --ut DIR
Standard inn er holdout 2026 (hack/c1/data_v3/test_input.csv); finnes fasit.csv ved siden av, måles det.
"""
import argparse, csv, hashlib, json, os, shutil, subprocess, sys, time
import numpy as np

HER = os.path.dirname(os.path.abspath(__file__))
ARB = os.path.abspath(os.path.join(HER, "../.."))
SMED2 = os.path.join(ARB, "kandidater/smed2_c1_mot")
SMED3 = os.path.join(ARB, "hack/varianter/smed3_utf_sitat")
C1 = os.path.join(ARB, "hack/c1")
T = None  # train_v3 lastes bare for --data v3 (gammel N-PX-agent)

ANDEL = 0.10  # standard rutingsandel, låst på val (case1_ruting.md); endres med --til-menneske
FELT = ["id", "utsteder", "moetedato", "forslag", "anbefaling", "p_mot", "til_menneske", "rutingsgrunn",
        "punkt", "sitat", "sitat_grunn", "sitat_kilde", "sitatagent_anbefaling", "injeksjon_flagget", "raa_score", "uenig_med_sitatagent"]
KILDE = "Vanguard Proxy voting policy for U.S. portfolio companies (feb 2025); ikke NBIM"
# MOT-sitat (#2009): sitatagenten sier FOR i alle saker, så MOT-rader får et MOT-punkt fra Vanguards
# PIII og en grunn fra smed2s forklaring (#2007) og fjorårets stemme. Setningene er ordrette fra punkter.json.
SAY = "PIII / Advisory votes on executive compensation (Say on Pay) / "
MOT_PUNKT = {
    "kobling": (SAY + "¶3", "If there are concerns that pay and performance are not aligned, a fund may vote against a pay-related proposal."),
    "struktur": (SAY + "¶4", "Where a plan includes structural issues which the funds determine have led to, or could in the future lead to, pay-for-performance misalignment, a fund may vote against a pay-related proposal."),
    "fjor": (SAY + "¶5", "Where pay-related proposals consistently receive low support, the funds look for boards to demonstrate consideration of shareholder concerns."),
    "fallskjerm": ("PIII / Additional executive pay matters / ¶1", "A fund will typically vote for proposals to approve severance packages (or “golden parachutes”) unless they are excessive or unreasonable (i.e., cash severance payments that total more than 2.99 times salary plus targeted bonus and/or have single trigger cash or equity payments)."),
}
FORKLARING = os.path.join(SMED2, "forklaring.csv")
FJOR = "fondet (NBIM) stemte MOT styret i forrige sak i selskapet"
STANDARD_MOT = "policy åpner for MOT ved svak lønn/resultat-kobling; må vurderes av menneske"


def mot_sitat(r, frk, sist_mot):
    """(punkt, sitat, grunn) for en MOT-rad. frk: rad fra forklaring.csv eller None."""
    gr = [frk[k] for k in ("grunn1", "grunn2", "grunn3") if frk and frk.get(k)]
    kj = [frk.get(k, "") for k in ("kjennetegn1", "kjennetegn2", "kjennetegn3")] if frk else []
    fjor = sist_mot or "nb_sist" in kj and any("stemte NBIM mot" in x for x in gr)
    tekst = (r.get("forslag") or "").lower()
    if "golden" in tekst or "parachute" in tekst or "merger" in tekst or (kj[:1] == ["t_merger"]): nøkkel = "fallskjerm"
    elif fjor: nøkkel = "fjor"
    elif kj[:1] and kj[0] in ("g_sbc", "s_cap_andel", "t_len"): nøkkel = "struktur"
    else: nøkkel = "kobling"
    punkt, sit = MOT_PUNKT[nøkkel]
    deler = ([FJOR] if fjor and not any("stemte NBIM mot" in x for x in gr) else []) + gr
    return punkt, sit, (("modellen: " if gr else "historikk: ") + " ".join(deler) if deler else STANDARD_MOT)


TRENG = ["utsteder", "cusip", "isin", "moetedato", "forslag", "kategori", "kilde", "styret"]


def datafeil(r, sett):
    """Grunner til at saken ikke kan vurderes av modellen (robusthet #2000). Tom liste = ok.
    Modellen er trent bare på styret=FOR og kilde=ISSUER; alt annet er utenfor det den kan."""
    g = []
    m = [k for k in TRENG if not str(r.get(k) or "").strip()]
    if m: g.append("mangler felt: " + ",".join(m))
    d = str(r.get("moetedato") or "")
    try:
        time.strptime(d, "%Y-%m-%d")
    except ValueError:
        if d: g.append(f"ugyldig møtedato «{d[:20]}»")
    if (r.get("styret") or "FOR") != "FOR": g.append(f"styret anbefaler «{r['styret']}», modellen kjenner bare FOR")
    if (r.get("kilde") or "ISSUER") != "ISSUER": g.append(f"kilde «{r['kilde']}», modellen kjenner bare ISSUER (styreforslag)")
    if r.get("id") in sett: g.append(f"duplikat: id {r['id']} er sett før i samme fil")
    return g


def lg(p): p = np.clip(p, 1e-6, 1 - 1e-6); return np.log(p / (1 - p))


def sha(f): return hashlib.sha256(open(f, "rb").read()).hexdigest()[:12]


class _Fanget(Exception):
    pass


def argumenter():
    """Argumentene til `train_v3.py --lekkasjefri`, hentet fra parseren i train_v3.main() selv,
    så nye flagg der får sin standardverdi. Lekkasjefri-stegene er de samme som i main()."""
    import argparse as ap
    orig = ap.ArgumentParser.parse_args
    def fang(self, *x, **k): raise _Fanget(self)
    ap.ArgumentParser.parse_args = fang
    try:
        T.main()
    except _Fanget as e:
        parser = e.args[0]
    finally:
        ap.ArgumentParser.parse_args = orig
    a = parser.parse_args(["--lekkasjefri"])
    T.PVP_DAGER = 100
    a.drop = ",".join(x for x in (a.drop, T.LEKK) if x)
    if not hasattr(a, "seed_start"): a.seed_start = 0  # eldre/nyere train_v3: frø 0..4 som før
    return a


def main():
    if "--data" in sys.argv and sys.argv[sys.argv.index("--data") + 1:][:1] == ["v3"]:
        sys.argv[sys.argv.index("--data"):sys.argv.index("--data") + 2] = []
        global T
        sys.path.insert(0, SMED2)
        import train_v3 as T  # noqa: E402
        return main_v3()
    return main_real()


def main_real():
    """Standard (#2053): NBIMs egne stemmer (real_votes) med smed2s MOT-modell #2044, se c1_real.py."""
    import c1_real
    p = argparse.ArgumentParser(description="Case 1-agenten på real_votes (standard). --data v3 gir den gamle N-PX-agenten.")
    p.add_argument("--csv", help="saker i real_votes-format uten fasitfelt (standard: test 2026, data_off/real_test_input.csv)")
    p.add_argument("--sak", help="én sak som JSON-objekt med feltene " + ",".join(c1_real.TRENG) + " (+ mgmt_rec, country, market)")
    p.add_argument("--historikk", default=c1_real.REAL, help="NBIMs tidligere stemmer (real_votes.csv)")
    p.add_argument("--vindu", default=None, help="mål mot fasit med maaler_offisiell_v2 (test|val); standard test når --csv og --sak mangler")
    p.add_argument("--ut", required=True, help="utmappe (opprettes)")
    p.add_argument("--baand", default="0.15,0.85", metavar="LO,HI",
                   help="til menneske når kalibrert P(MOT) er i [LO, HI) (standard 0.15,0.85, valgt i #2128)")
    p.add_argument("--til-menneske", type=float, default=None, metavar="PROSENT",
                   help="gammel ruting i stedet for --baand: andel saker nær grensen (logit-bånd låst på val 2025)")
    a = p.parse_args()
    if a.til_menneske is not None and not 0 <= a.til_menneske <= 100: sys.exit("--til-menneske må være mellom 0 og 100")
    try:
        lo, hi = (float(x) for x in a.baand.split(",")); assert 0 <= lo <= hi <= 1
    except (ValueError, AssertionError): sys.exit("--baand må være LO,HI med 0 <= LO <= HI <= 1")
    if a.vindu is None and not a.csv and not a.sak: a.vindu = "test"
    c1_real.main(a, None if a.til_menneske is None else a.til_menneske / 100)


def main_v3():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--csv", help="saker i test_input-format (standard: holdout 2026)")
    p.add_argument("--sak", help="én sak som JSON-objekt med feltene " + ",".join(TRENG))
    p.add_argument("--train", default=os.path.join(C1, "data_v3/train.csv"), help="historikk (N-PX 2024+2025)")
    p.add_argument("--val-data", default=os.path.join(C1, "data_v3_val"), help="val 2025 (grense og bånd låses her)")
    p.add_argument("--fasit", default=None, help="fasit.csv for måling (standard: ved siden av --csv om den finnes)")
    p.add_argument("--ut", required=True, help="utmappe (opprettes)")
    p.add_argument("--til-menneske", type=float, default=ANDEL * 100, metavar="PROSENT",
                   help="andel saker nær grensen som går til et menneske, i prosent (standard 10). "
                        "Båndet låses på val 2025, aldri på inn-sakene. Saker med datafeil, uten sitat "
                        "eller med injeksjon går til menneske i tillegg")
    a = p.parse_args()
    if not 0 <= a.til_menneske <= 100: sys.exit("--til-menneske må være mellom 0 og 100")
    andel = a.til_menneske / 100
    t0 = time.time()
    os.makedirs(a.ut, exist_ok=True)
    work = os.path.join(a.ut, "_data")
    os.makedirs(work, exist_ok=True)
    # 1) inn-saker -> _data/test_input.csv, historikk -> _data/train.csv
    if a.sak:
        r = json.loads(a.sak)
        if not isinstance(r, dict): sys.exit("--sak må være et JSON-objekt")
        for k in TRENG: r.setdefault(k, "")  # manglende felt sendes til menneske under, ikke krasj
        r.setdefault("id", "sak1")
        with open(os.path.join(work, "test_input.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(r)); w.writeheader(); w.writerow(r)
        fasit = a.fasit
    else:
        inn = a.csv or os.path.join(C1, "data_v3/test_input.csv")
        shutil.copy(inn, os.path.join(work, "test_input.csv"))
        fas = os.path.join(os.path.dirname(os.path.abspath(inn)), "fasit.csv")
        fasit = a.fasit or (fas if os.path.exists(fas) else None)
    shutil.copy(a.train, os.path.join(work, "train.csv"))
    alle = T.les(os.path.join(work, "test_input.csv"))
    for r in alle[:1]:
        for k in ("ledelsen", "mgmt_felt_LEKKER", "avvik", "fasit", "stemme"):
            if k in r: sys.exit(f"inn-saken har fasitfeltet «{k}»; fjern det")
    # 1b) saker modellen ikke kan vurdere tas ut og går rett til menneske med grunn (#2000)
    sett, gode, stopp = set(), [], {}
    for i, r in enumerate(alle):
        r["id"] = r.get("id") or f"rad{i + 1}"
        g = datafeil(r, sett)
        sett.add(r["id"])
        if g: stopp[i] = "; ".join(g)
        else: gode.append(r)
    if stopp:
        with open(os.path.join(work, "test_input.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(alle[0])); w.writeheader(); w.writerows(gode)
    kjente = {r["cusip"] for r in T.les(os.path.join(work, "train.csv"))}
    # 2) lås grense og rutingsbånd (--til-menneske, standard 10 %) på val 2025 (tren 2024 -> prediker 2025)
    te_v, rt_v, _ = T.modell(a.val_data, argumenter())
    fv = {r["id"]: int(r["avvik"]) for r in T.les(os.path.join(a.val_data, "fasit.csv"))}
    yv = np.array([fv[r["id"]] for r in te_v])
    g, f1v = T.velg_grense(rt_v, yv)
    band = float(np.quantile(np.abs(lg(rt_v) - lg(g)), andel)) if andel > 0 else -1.0  # 0 % = ingen bånd
    # 3) modellen på inn-sakene (tren på hele historikken)
    if gode:
        te, rt, (pt, _, _, _, iso, _, _) = T.modell(work, argumenter())
        g_kal = float(iso.predict([g])[0])
    else:
        te, rt, pt, g_kal = [], [], [], float("nan")
    # 4) sitatagenten (smed3), uendret, som egen prosess
    sp, sj = os.path.join(a.ut, "_sitat_pred.csv"), os.path.join(a.ut, "_sitat.jsonl")
    open(sj, "w").close()
    if gode: subprocess.run(["python3", "-I", os.path.join(SMED3, "agent.py"), os.path.join(work, "train.csv"),
                    os.path.join(work, "test_input.csv"), sp, "--forklaring", sj], check=True, capture_output=True)
    sit = {d["id"]: d for d in map(json.loads, open(sj, encoding="utf-8"))}
    frk = {x["id"]: x for x in csv.DictReader(open(FORKLARING, encoding="utf-8"))} if os.path.exists(FORKLARING) else {}
    sist = {}  # cusip -> avvik i siste sak i historikken (dato-sortert)
    for h in sorted(T.les(os.path.join(work, "train.csv")), key=lambda h: h["moetedato"]): sist[h["cusip"]] = h["avvik"] == "1"
    # 5) slå sammen
    rader = []
    for r, s, q in zip(te, rt, pt):
        mot = s >= g
        avst = abs(lg(s) - lg(g))
        rut = bool(avst <= band)
        d = sit.get(r["id"], {})
        if mot and d.get("sitat"):  # MOT-sitat og grunn (#2009); rader uten sitat rutes som før
            f = frk.get(r["id"]) if (frk.get(r["id"]) or {}).get("anbefaling") == "MOT" else None
            pk, st, gr = mot_sitat(r, f, sist.get(r["cusip"], False))
            d = dict(d, punkt=pk, sitat=st, grunn=gr)
        grunn = (f"nær grensen: |logit-avstand| {avst:.2f} <= bånd {band:.2f}" if rut else "")
        if d.get("injeksjon_flagget"):
            rut, grunn = True, (grunn + "; " if grunn else "") + "instruksjonslignende tekst i forslaget"
        if not d.get("sitat"):
            rut, grunn = True, (grunn + "; " if grunn else "") + "fant ikke noe sitat i retningslinjene"
        if r["cusip"] not in kjente:  # bare et varsel, ruter ikke: modellen er målt med slike saker
            d = dict(d, grunn=(d.get("grunn", "") + " | " if d.get("grunn") else "") + "obs: ingen tidligere stemmer for selskapet i historikken")
        rader.append(dict(id=r["id"], utsteder=r["utsteder"], moetedato=r["moetedato"], forslag=r["forslag"][:200],
                          anbefaling="MOT" if mot else "FOR", p_mot=round(float(q), 4), til_menneske=int(rut),
                          rutingsgrunn=grunn, punkt=d.get("punkt", ""), sitat=d.get("sitat", ""),
                          sitat_grunn=d.get("grunn", ""), sitat_kilde=KILDE if d.get("punkt") else "",
                          sitatagent_anbefaling=d.get("anbefaling", ""), injeksjon_flagget=int(bool(d.get("injeksjon_flagget"))),
                          raa_score=round(float(s), 5),
                          uenig_med_sitatagent=int(bool(d.get("anbefaling")) and d.get("anbefaling") != ("MOT" if mot else "FOR"))))
    # saker tatt ut i 1b: følger styret som standard, men alltid til menneske med grunn
    ferdig = {x["id"]: x for x in rader}  # id er unik blant gode saker (duplikater er tatt ut)
    rader = [dict(id=r["id"], utsteder=r.get("utsteder", ""), moetedato=r.get("moetedato", ""), forslag=(r.get("forslag") or "")[:200],
                  anbefaling="FOR", p_mot="", til_menneske=1, rutingsgrunn="kan ikke vurderes: " + stopp[i], punkt="", sitat="",
                  sitat_grunn="", sitat_kilde="", sitatagent_anbefaling="", injeksjon_flagget=0, raa_score="", uenig_med_sitatagent=0)
             if i in stopp else ferdig[r["id"]] for i, r in enumerate(alle)]
    with open(os.path.join(a.ut, "agent.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FELT); w.writeheader(); w.writerows(rader)
    # måler-format som ruting.py: rutet -> konfidens 0,5 (< 0,6), ellers kalibrert sikkerhet med gulv 0,6
    pm = os.path.join(a.ut, "pred_maaler.csv")
    with open(pm, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["id", "anbefaling", "konfidens", "p_avvik"])
        for x in rader:
            if x["p_mot"] == "": w.writerow([x["id"], x["anbefaling"], 0.5, 0.5]); continue
            k = 0.5 if x["til_menneske"] else max(0.6, x["p_mot"] if x["anbefaling"] == "MOT" else 1 - x["p_mot"])
            w.writerow([x["id"], x["anbefaling"], round(k, 4), x["p_mot"]])
    n, nm, nr = len(rader), sum(x["anbefaling"] == "MOT" for x in rader), sum(x["til_menneske"] for x in rader)
    logg = [f"kjor_agent.py {time.strftime('%Y-%m-%d %H:%M:%S')}, {time.time() - t0:.0f} s",
            f"inn: {n} saker; MOT {nm}; til menneske {nr} ({nr / max(n, 1):.1%}), av dem {len(stopp)} som ikke kunne vurderes",
            f"låst på val 2025: rå grense {g:.5f} (kalibrert {g_kal:.3f}), val-F1 {f1v:.4f} i utvalget; {a.til_menneske:g} %-bånd {band:.4f} logit (--til-menneske {a.til_menneske:g})",
            "kode (sha256[:12]): " + ", ".join(f"{os.path.relpath(x, ARB)} {sha(x)}" for x in
                                               (__file__, os.path.join(SMED2, "train_v3.py"), os.path.join(SMED2, "sec_feats.py"),
                                                T.VANG, os.path.join(SMED3, "agent.py"), os.path.join(SMED3, "rl/punkter.json")))]
    if fasit and gode:
        for navn, fil in (("alle saker, ruting ignorert", "_pred_uten_ruting.csv"), ("med ruting (konfidens < 0,6 = menneske)", "pred_maaler.csv")):
            if fil.startswith("_"):
                with open(os.path.join(a.ut, fil), "w", newline="") as f:
                    w = csv.writer(f); w.writerow(["id", "anbefaling", "konfidens", "p_avvik"])
                    for x in rader: w.writerow([x["id"], x["anbefaling"], 0.9, x["p_mot"]])
            o = subprocess.run(["python3", "-I", os.path.join(C1, "maaler.py"), os.path.join(a.ut, fil), "--fasit", fasit],
                               capture_output=True, text=True)
            logg += [f"--- måler ({navn}) ---", (o.stdout + o.stderr).strip()]
        # hele systemet: rutede saker antas avgjort riktig av mennesket (øvre grense, som dommer #2010/#2017)
        fs = {r["id"]: int(r["avvik"]) for r in csv.DictReader(open(fasit, encoding="utf-8"))}
        tp = fp = fn = tn = 0
        for x in rader:
            if x["id"] not in fs: continue
            y, m = fs[x["id"]], (fs[x["id"]] if x["til_menneske"] else int(x["anbefaling"] == "MOT"))
            tp += y and m; fp += m and not y; fn += y and not m; tn += not y and not m
        f1 = 2 * tp / max(2 * tp + fp + fn, 1)
        logg += [f"--- hele systemet med {a.til_menneske:g} % til menneske (mennesket antas å treffe; øvre grense) ---",
                 f"treff {(tp + tn) / max(tp + fp + fn + tn, 1):.1%}  F1 {f1:.4f}  (tp {tp} fp {fp} fn {fn} tn {tn})"]
    open(os.path.join(a.ut, "KJORING.txt"), "w").write("\n".join(logg) + "\n")
    print("\n".join(logg))
    print(f"skrev {os.path.join(a.ut, 'agent.csv')}")


if __name__ == "__main__":
    main()
