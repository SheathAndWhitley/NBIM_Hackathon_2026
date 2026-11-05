"""Lekkasjevakt for Case 1 (dommer2 #2055). Bare stdlib. Se FORBUDT.md.

Bruk:  python3 -I sjekk_lekkasje.py kode <fil.py eller mappe> ...      statisk: forbudte kolonner brukt i koden
       python3 -I sjekk_lekkasje.py svar SVAR.csv --data real|npx [--vindu val|test]
           (1) svarfila har forbudte kolonner -> AVVIST
           (2) lekkasjesignatur (bare real): treffrate på MOT med begrunnelse vs uten, og
               avvik predikert på de 9 FOR-radene som har begrunnelse. Stor forskjell -> MISTANKE.
Utgang 0 = ren, 1 = AVVIST (forbudt kolonne i svarfila), 2 = MISTANKE (dommeren ser på koden/svaret).
"""
import csv, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import maaler_offisiell_v2 as M

FORBUDT = ["nbim_vote_raw", "nbim_vote", "against_board", "rationale_text", "rationale_section",
           "position_paper", "funds_disagree", "n_funds", "injection_flag"]
# Lov å nevne: fasit i trening (y = against_board på TRAIN), sitat fra TIDLIGERE år. Linjer med
# kommentaren '# lov: <grunn>' slippes (dommeren leser grunnen).
RX = re.compile(r"\b(" + "|".join(FORBUDT) + r")\b")

def kode(stier):
    filer = []
    for s in stier:
        if os.path.isdir(s):
            for rot, _, fs in os.walk(s):
                filer += [os.path.join(rot, f) for f in fs if f.endswith(".py")]
        else: filer.append(s)
    treff = 0; rå = 0
    for f in filer:
        if os.path.basename(f) in ("sjekk_lekkasje.py",) or "maaler" in os.path.basename(f): continue
        for i, l in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
            if "opplastet/" in l and "votes.csv" in l:
                rå += 1; print(f"RÅDATA  {f}:{i}: leser rå fil med fasit, bruk data_off/*_input.csv: {l.strip()[:120]}")
            m = RX.findall(l)
            ren = l.split("#")[0]
            if m and "# lov:" not in l and RX.search(ren) and not re.match(r"\s*(FORBUDT|LEKK)\w*\s*=", ren):
                treff += 1; print(f"FORBUDT {f}:{i}: {sorted(set(m))}: {l.strip()[:120]}")
    print(f"KODE: {len(filer)} filer, {treff} linjer med forbudte kolonner, {rå} lesinger av rådata")
    print("Hver linje må være fasit på TRAIN eller sitat fra tidligere år, merket '# lov: ...'. Dommeren leser hver.")
    return 2 if treff or rå else 0

def _avv(s, f):
    a = (s.get("anbefaling") or "").strip().upper(); a = {"AGAINST": "MOT", "ABSTAIN": "AVSTÅ"}.get(a, a)
    return (a == "1") if a in ("0", "1") else (a != (f["mgmt_rec"] or "FOR"))

def svar(sti, data, vindu):
    hode = next(csv.reader(open(sti, encoding="utf-8")))
    bad = [k for k in hode if k.strip().lower() in FORBUDT]
    if bad: print(f"AVVIST: svarfila har forbudte kolonner {bad}"); return 1
    S = M.les_svar(sti, data) if hasattr(M, "les_svar") else None
    if S is None: print("OK kolonner. (Signaturtesten trenger les_svar i måleren.)"); return 0
    fas = {M.rid(r): r for r in M.les(data) if M.vindu_av(r, data) == vindu}
    if data != "real": print("OK kolonner. Signaturtest bare på real (npx har ingen begrunnelser)."); return 0
    g = {"mot_med": [0, 0], "mot_uten": [0, 0], "for_med": [0, 0]}
    for i, f in fas.items():
        if i not in S or f["against_board"] == "": continue
        s = S[i]; a = (s.get("anbefaling") or "").strip().upper()
        a = {"AGAINST": "MOT", "ABSTAIN": "AVSTÅ"}.get(a, a)
        avv = _avv(s, f)
        med = f["rationale_text"].strip() != ""; y = f["against_board"] == "1.0"
        k = ("mot_med" if med else "mot_uten") if y else ("for_med" if med else None)
        if k: g[k][0] += avv; g[k][1] += 1
    r = {k: (v[0] / v[1] if v[1] else float("nan"), v[1]) for k, v in g.items()}
    for k, (x, n) in r.items(): print(f"  {k:9s} avvik predikert {x:.2f} (n={n})")
    # Fra 2023 har nesten alle MOT begrunnelse: «begrunnelse finnes» alene gir F1 ~0,96. Et svar som
    # nesten er det samme settet som begrunnelsesradene, er laget med fasit.
    pa = {i for i, f in fas.items() if i in S and f["against_board"] != "" and _avv(S[i], f)}
    rb = {i for i, f in fas.items() if f["against_board"] != "" and f["rationale_text"].strip()}
    jac = len(pa & rb) / len(pa | rb) if pa | rb else 0.0
    print(f"  overlapp (Jaccard) mellom predikerte avvik og rader med begrunnelse: {jac:.2f}  (ærlig modell ~0,3)")
    mist = jac >= 0.75  # for_med har bare 2-4 rader per år: vises, men avgjør ikke
    print("MISTANKE: svaret følger NBIMs etterpå-begrunnelser, ikke saken" if mist else "OK: ingen lekkasjesignatur")
    return 2 if mist else 0

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(0)
    if a[0] == "kode": sys.exit(kode(a[1:]))
    if a[0] == "svar":
        data = a[a.index("--data") + 1] if "--data" in a else "real"
        vindu = a[a.index("--vindu") + 1] if "--vindu" in a else "val"
        sys.exit(svar(a[1], data, vindu))
    print(__doc__); sys.exit(1)
