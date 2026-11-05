"""Case 1: tabell over målte tall rett fra den offisielle måleren (#2064). Til JURY.md (#1975).

Bruk:  python3 -I lag_tall_tabell.py      (skriver tall_tabell.md ved siden av seg selv)

Hver rad: én prediksjonsfil kjøres gjennom maaler_offisiell_v3.py --score mot (real_votes), #2146. Tallene i tabellen
(P, R, F1, PR-AUC) leses fra målerens utskrift, ikke fra smedenes logger. Smedenes radformat
rad,p,mot_pred oversettes først til id,anbefaling,p_avvik med modellens EGEN beslutning (mot_pred,
grensa valgt på VAL), fordi målerens rad,p-modus bruker fast grense 0,5.
KI: parret bootstrap (2000 trekk, frø 0) over de samme radene, regnet her; punkt-F1 sjekkes lik
målerens, ellers stopper skriptet. Mangler en fil, står raden som «ikke målt».
"""
import csv, os, random, re, subprocess, sys, tempfile, hashlib, datetime

HER = os.path.dirname(os.path.abspath(__file__))
A = os.path.dirname(os.path.dirname(HER))  # .../arbeid
MAALER = os.path.join(HER, "maaler_offisiell_v3.py")
SMED3 = os.path.join(HER, "..", "varianter", "smed3_utf_sitat", "ut")
ABL = os.path.join(A, "oppgave_2045")

# (gruppe, navn, {vindu: fil})
RADER = [
    ("grunnlinje", "følg styret", {"val": f"{HER}/data_off/real_val_folg_styret.csv",
                                    "test": f"{HER}/data_off/real_test_folg_styret.csv"}),
    ("modell", "repo4 = #2044 miks h2 + 4 historikktrekk (levert agent, maskin alene, #2592)",
     {"test": f"{A}/hack/levering/kjor_agent_real_maskin_alene.csv"}),
    ("modell", "smed2 #2044 miks LR+LGBM, løpende historikk (eldre frossen, levert til 17:03)",
     {"test": f"{A}/oppgave_2044/pred_miks_h2.csv"}),
    ("modell", "smed3 #2037 tfidf+LR+selskapshistorikk med NBIM-sitat (agentens sitatvariant)",
     {"val": f"{SMED3}/real_val_svar.csv", "test": f"{SMED3}/real_test_svar.csv"}),
]
for kode, navn in [("full", "ingen (full modell = eldre frossen #2044)"), ("tekst", "uten tekst (tfidf)"),
                   ("selskap", "uten selskapshistorikk"), ("teksthist", "uten teksthistorikk"),
                   ("selskap,teksthist", "uten all historikk"), ("type", "uten forslagstype"),
                   ("stiller", "uten forslagsstiller"), ("land", "uten land"),
                   ("styre", "uten styrets anbefaling"), ("barehist", "bare historikk"),
                   ("baretekst", "bare tekst")]:
    RADER.append(("ablasjon #2045 (eldre frossen #2044)", navn, {"test": f"{ABL}/pred_{kode}.csv"}))


def les_data():
    sys.path.insert(0, HER)
    import maaler_offisiell_v3 as m
    return m, m.les("real")


def til_id(fil, R, tmp):
    """rad,p,mot_pred -> id,anbefaling,p_avvik (modellens egen beslutning). Andre format urørt."""
    rd = csv.DictReader(open(fil, encoding="utf-8-sig", newline=""))
    if "id" in (rd.fieldnames or []):
        return fil
    ut = os.path.join(tmp, hashlib.md5(fil.encode()).hexdigest() + ".csv")
    sett = set()
    with open(ut, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["id", "anbefaling", "p_avvik"])
        for r in rd:
            j = int(r["rad"]); a = r.get("mot_pred")
            a = a if a in ("0", "1") else ("1" if float(r["p"]) >= 0.5 else "0")
            i = f"{R[j]['meeting_id']}|{R[j]['item_no']}"; sett.add(i)
            w.writerow([i, a, r["p"]])
        # smedene dropper rader uten fasit (against_board tom); måleren krever id men teller dem ikke
        for r in R:
            i = f"{r['meeting_id']}|{r['item_no']}"
            if i not in sett and r["against_board"] == "":
                w.writerow([i, "0", "0"])
    return ut


def kjor_maaler(fil, vindu):
    p = subprocess.run([sys.executable, "-I", MAALER, fil, vindu, "--data", "real", "--score", "mot"],
                       capture_output=True, text=True)
    t = p.stdout
    m = re.search(r"avvik: TP (\d+) FP (\d+) FN (\d+)\s+P ([\d.]+)\s+R ([\d.]+)\s+F1 ([\d.]+)\s+PR-AUC ([\d.na]+)", t)
    mm = re.search(r"MOT mot styret: TP (\d+) FP (\d+) FN (\d+)\s+P ([\d.]+)\s+R ([\d.]+)\s+F1 ([\d.]+)", t)
    s = re.search(r"SCORE ([\d.na]+)", t)
    if p.returncode or not m or not mm or not s:
        return {"feil": (t + p.stderr).strip().splitlines()[-1] if (t + p.stderr).strip() else "ingen utskrift"}
    tp, fp, fn = map(int, mm.groups()[:3])  # MOT mot styret (#231); PR-AUC finnes bare på avvik
    return dict(tp=tp, fp=fp, fn=fn, P=float(mm[4]), R=float(mm[5]), F1=float(s[1]), auc=m[7])


def bootstrap(mm, fil, vindu, R, n=2000):
    S = mm.les_svar(fil, "real")
    par = []
    for r in R:
        if mm.vindu_av(r, "real") != vindu or r["against_board"] == "":
            continue
        a = (S[mm.rid(r)].get("anbefaling") or "").strip().upper()
        a = {"AGAINST": "MOT", "ABSTAIN": "AVSTÅ", "AVSTA": "AVSTÅ"}.get(a, a)
        styret = r["mgmt_rec"] or "FOR"
        if a in ("0", "1"):  # som v3: avvik -> MOT når styret ikke sier MOT
            mot = a == "1" and styret != "MOT"
        else:
            mot = a == "MOT" and styret != "MOT"
        par.append((mot, r["against_board"] == "1.0" and r["nbim_vote"] == "MOT"))
    def f1(pp):
        tp = sum(a and y for a, y in pp); fp = sum(a and not y for a, y in pp); fn = sum(y and not a for a, y in pp)
        return 2 * tp / (2 * tp + fp + fn) if tp else 0.0
    rng = random.Random(0); k = len(par)
    bs = sorted(f1([par[rng.randrange(k)] for _ in range(k)]) for _ in range(n))
    return f1(par), bs[int(0.025 * n)], bs[int(0.975 * n) - 1]


def main():
    mm, R = les_data()
    sha = hashlib.sha256(open(MAALER, "rb").read()).hexdigest()[:10]
    linjer = []
    with tempfile.TemporaryDirectory() as tmp:
        for gruppe, navn, filer in RADER:
            celler = []
            for vindu in ("val", "test"):
                fil = filer.get(vindu)
                if not fil or not os.path.exists(fil):
                    celler.append(("ikke målt (ingen fil)" if not fil else "ikke målt (fil mangler)", "", "", "", "", ""))
                    continue
                g = til_id(fil, R, tmp)
                r = kjor_maaler(g, vindu)
                if "feil" in r:
                    celler.append((f"UGYLDIG: {r['feil'][:60]}", "", "", "", "", "")); continue
                f, lo, hi = bootstrap(mm, g, vindu, R)
                if abs(f - r["F1"]) > 5e-6:
                    sys.exit(f"KP feilet: {navn} {vindu}: måler F1 {r['F1']}, bootstrap-punkt {f}")
                celler.append((f"{r['F1']:.3f}", f"{r['P']:.2f}", f"{r['R']:.2f}", f"[{lo:.2f}, {hi:.2f}]",
                               str(r["tp"] + r["fp"]), r["auc"][:5]))
            v, t = celler
            linjer.append(f"| {gruppe} | {navn} | {v[0]} | {t[0]} | {t[1]} | {t[2]} | {t[3]} | {t[4]} | {t[5]} |")
            print(linjer[-1])
    nv = sum(1 for r in R if mm.vindu_av(r, "real") == "test" and r["against_board"] == "1.0" and r["nbim_vote"] == "MOT")
    nav = sum(1 for r in R if mm.vindu_av(r, "real") == "test" and r["against_board"] == "1.0")
    ut = [f"# Case 1: målte tall rett fra den offisielle måleren",
          "",
          f"Generert {datetime.datetime.now():%Y-%m-%d %H:%M} med `python3 -I arbeid/hack/c1/lag_tall_tabell.py`. "
          f"Måler `maaler_offisiell_v3.py --score mot` (sha256 {sha}), data real_votes (NBIMs ekte stemmer), "
          f"VAL = 2025, TEST = 2026 ({nv} stemmer MOT mot styret; {nav} avvik inkl. AVSTÅ er ikke hovedtallet).",
          "Hovedtall: F1 på MOT mot styret (ordre #231). P, R, KI og flagget gjelder TEST; PR-AUC er på avvik (måleren har ingen MOT-sannsynlighet). "
          "KI = 95 % bootstrap (2000 trekk) over testradene (rader, ikke klynger), punkt-F1 kontrollert lik målerens. README, JURY.md og ERLIG_EVALUERING.md bruker klyngebootstrap per selskap for hovedtallet (repo4), [0,40; 0,62]; for eldre frossen #2044 er klyngebootstrap [0,36; 0,59].",
          "Grensa er valgt på VAL av hver modell; måleren får modellens egen beslutning. Ingen selvrapporterte tall.",
          "",
          "| gruppe | forsøk | VAL F1 | TEST F1 | P | R | 95 % KI | flagget | PR-AUC (avvik) |",
          "|---|---|---|---|---|---|---|---|---|", *linjer, "",
          "«ikke målt (ingen fil)»: smeden har ikke lagret VAL-prediksjoner, så VAL-tallet finnes bare i loggen "
          f"og står ikke her. Med {nv} MOT i test er ±0,05 F1 innenfor støyen; se KI."]
    open(os.path.join(HER, "tall_tabell.md"), "w", encoding="utf-8").write("\n".join(ut) + "\n")
    print("skrev", os.path.join(HER, "tall_tabell.md"))


if __name__ == "__main__":
    main()
