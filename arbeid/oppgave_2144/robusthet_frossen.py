"""Robusthetstest for den frosne Case 1-agenten (#2144, smed2). Gjenbruker idéen fra hack/c1/robusthet.py (#1968).

    python3 -I arbeid/oppgave_2144/robusthet_frossen.py [--bare navn,navn] [--ut state/rapporter/c1_robusthet_frossen.md]

Agent: arbeid/hack/levering/kjor_agent.py (standard real_votes, frossen #2044 miks h2, ruting bånd [0,15, 0,85)), urørt.
Viktig: agenten slår opp inn-saker som finnes i historikkfila og bruker den lagrede raden. Forstyrrelsen legges
derfor BÅDE i inn-fila og i 2026-radene i en kopi av historikkfila (--historikk), ellers ville modellen ikke se den.
Fasit- og forbudte felt i kopien er urørt (train.py leser dem ikke for 2026; måleren bruker sin egen originalfil).
Måler: hack/c1/maaler_offisiell_v3.py <pred> test --data real --score mot, på _pred_uten_ruting.csv (maskin alene).
"""
import csv, os, re, subprocess, sys, tempfile, time

HER = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HER, "../.."))
REAL = os.path.join(ROT, "state/opplastet/20261105_114241_real_votes.csv")
AGENT = os.path.join(ROT, "arbeid/hack/levering/kjor_agent.py")
PY = os.path.join(ROT, "arbeid/kandidater/smed2_c1_mot/.venv/bin/python")
MAALER = os.path.join(ROT, "arbeid/hack/c1/maaler_offisiell_v3.py")
INNFELT = ["id", "injection_flag", "meeting_id", "company_id", "company", "ticker", "country", "market", "meeting_date",
           "item_no", "proposal_number", "proposal_text", "proponent", "mgmt_rec_raw", "mgmt_rec", "year", "proposal_type"]


def nye_sel(r): return dict(r, company_id=str(9_000_000 + int(float(r["company_id"]))), company="NY " + r["company"], ticker="")


VARIANTER = [  # (navn, endring av en 2026-rad, forklaring)
    ("basis", lambda r: r, "uendret"),
    ("nye_selskaper", nye_sel, "company_id/navn byttet til ukjente: ingen selskapshistorikk før 2026"),
    ("tom_tekst", lambda r: dict(r, proposal_text=""), "proposal_text tom i alle 2026-saker"),
    ("tomme_felt", lambda r: dict(r, company="", ticker="", country="", market="", proposal_number="", proponent=""),
     "company, ticker, country, market, proposal_number, proponent tomme"),
    ("ukjent_type", lambda r: dict(r, proposal_type="NY_SAKSTYPE"),
     "proposal_type = NY_SAKSTYPE i inn OG historikk-kopi (typen havner da i historikken, så vakta ser den ikke)"),
    ("ukjent_type_inn", lambda r: dict(r, proposal_type="NY_SAKSTYPE"),
     "INN:proposal_type = NY_SAKSTYPE bare i inn-fila (som en ny sak); modellen bruker lagret rad"),
    ("tomme_valgfri", lambda r: dict(r, company="", ticker="", country="", market="", proposal_number=""),
     "company, ticker, country, market, proposal_number tomme (felt agenten ikke krever)"),
    ("uten_styret", lambda r: dict(r, mgmt_rec="", mgmt_rec_raw=""), "mgmt_rec og mgmt_rec_raw tomme (manglende styreanbefaling)"),
]


def maal(pred):
    p = subprocess.run(["python3", "-I", MAALER, pred, "test", "--data", "real", "--score", "mot"], capture_output=True, text=True)
    ut = p.stdout + p.stderr
    m = re.search(r"SCORE (\S+)", ut)
    return (float(m.group(1)) if m and m.group(1) != "nan" else None), ut


def kjor(navn, f, forkl, tmp):
    with open(REAL, encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh); felt = rd.fieldnames; H = list(rd)
    bare_inn = forkl.startswith("INN:")
    H0 = H
    H = [f(dict(r)) if r["year"] == "2026" else r for r in H]
    if bare_inn: H, Hinn = H0, H
    else: Hinn = H
    d = os.path.join(tmp, navn); os.makedirs(d)
    hist, inn, ut = os.path.join(d, "real.csv"), os.path.join(d, "inn.csv"), os.path.join(d, "ut")
    with open(hist, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=felt); w.writeheader(); w.writerows(H)
    with open(inn, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=INNFELT, extrasaction="ignore"); w.writeheader()
        for r in Hinn:
            if r["year"] == "2026" and r["injection_flag"] != "1":
                w.writerow(dict(r, id=f"{r['meeting_id']}|{r['item_no']}"))
    t0 = time.time()
    p = subprocess.run([PY, AGENT, "--csv", inn, "--historikk", hist, "--ut", ut], capture_output=True, text=True, cwd=ROT)
    sek = time.time() - t0
    a = os.path.join(ut, "agent.csv")
    if p.returncode != 0 or not os.path.exists(a):
        return dict(navn=navn, forkl=forkl, sek=sek, feil="KRASJ: " + ((p.stderr.strip().splitlines() or ["?"])[-1])[:200])
    rader = list(csv.DictReader(open(a, encoding="utf-8")))
    n = len(rader); nm = sum(int(x["mot_styret"]) for x in rader); nr = sum(int(x["til_menneske"]) for x in rader)
    grunner = {}
    for x in rader:
        for g in filter(None, (s.split(":")[0].split("«")[0].strip() for s in x["rutingsgrunn"].split(";"))):
            grunner[g] = grunner.get(g, 0) + 1
    f1, mtxt = maal(os.path.join(ut, "_pred_uten_ruting.csv"))
    ln = [l for l in mtxt.splitlines() if "MOT mot styret" in l]
    return dict(navn=navn, forkl=forkl, sek=sek, n=n, nm=nm, rutet=nr / max(n, 1), f1=f1, motlinje=ln[0].strip() if ln else "",
                grunner=sorted(grunner.items(), key=lambda kv: -kv[1])[:3], maaler=mtxt if f1 is None else "")


def rapport(res):
    b = next((r for r in res if r["navn"] == "basis" and r.get("f1") is not None), None)
    L = ["# Case 1: robusthetstest på den frosne agenten (#2044 miks h2, real_votes test 2026) (smed2 #2144)", "",
         "Kommando (fra landsbymappen, ca. 1 min per test): `python3 -I arbeid/oppgave_2144/robusthet_frossen.py "
         "--ut state/rapporter/c1_robusthet_frossen.md`", "",
         "Agent: `arbeid/kandidater/smed2_c1_mot/.venv/bin/python arbeid/hack/levering/kjor_agent.py --csv INN --historikk KOPI --ut DIR` "
         "(standard ruting: kalibrert P(MOT) i [0,15, 0,85) + datafeil/ukjent type/ukjent selskap). Modellen er ikke endret.  ",
         "Måler: `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py DIR/_pred_uten_ruting.csv test --data real --score mot` "
         "(F1 på MOT mot styret, maskin alene).  ",
         "Forstyrrelsen legges i inn-fila OG i 2026-radene i en kopi av real_votes, fordi agenten bruker den lagrede raden for "
         "kjente saker. Fasit er urørt (måleren leser originalfila).", "",
         "| test | F1 MOT | endring | saker | MOT-flagg | sendt til menneske | viktigste rutingsgrunner | hva |", "|---|---|---|---|---|---|---|---|"]
    for r in res:
        if "feil" in r:
            L.append(f"| {r['navn']} | KRASJ | | | | | | {r['feil']} |"); continue
        f = "nan" if r["f1"] is None else f"{r['f1']:.3f}"
        d = f"{r['f1'] - b['f1']:+.3f}" if b and r["f1"] is not None else ""
        g = ", ".join(f"{k} {v}" for k, v in r["grunner"])
        L.append(f"| {r['navn']} | {f} | {d} | {r['n']} | {r['nm']} | {r['rutet']:.1%} | {g} | {r['forkl'].removeprefix('INN:')} |")
    L += ["", "Målerlinje «MOT mot styret» per test:", ""] + [f"- {r['navn']}: `{r.get('motlinje', '')}`" for r in res if "feil" not in r]
    return "\n".join(L)


def main(a):
    bare = a[a.index("--bare") + 1].split(",") if "--bare" in a else None
    ut = a[a.index("--ut") + 1] if "--ut" in a else None
    res = []
    with tempfile.TemporaryDirectory() as tmp:
        for navn, f, forkl in VARIANTER:
            if bare and navn not in bare: continue
            r = kjor(navn, f, forkl, tmp); res.append(r)
            print(f"  {navn:14s}", r.get("feil") or f"F1 MOT {r['f1']}  MOT-flagg {r['nm']}  rutet {r['rutet']:.1%}  ({r['sek']:.0f} s)",
                  r.get("maaler", "")[-300:], flush=True)
    tekst = rapport(res)
    if ut: open(os.path.join(ROT, ut) if not os.path.isabs(ut) else ut, "w", encoding="utf-8").write(tekst + "\n")
    print(tekst)


if __name__ == "__main__":
    main(sys.argv[1:])
