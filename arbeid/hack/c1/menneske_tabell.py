"""Én tabell for «send til menneske» på MOT mot styret (smed3 #2135). Bare stdlib, modellen røres ikke.
Bruk: python3 -I arbeid/hack/c1/menneske_tabell.py [AGENT.csv]   (standard: arbeid/oppgave_2132/agent.csv, kald standardkjøring #2132)
Fasit som måler v3 --score mot: test 2026, rader med against_board, MOT mot styret = nbim_vote MOT og against_board 1.
Maskin alene = agentens MOT-flagg (anbefaling MOT der styret ikke sier MOT). Maskin+menneske = rutede saker avgjort riktig (øvre grense).
"""
import csv, sys
FASIT = "state/opplastet/20261105_114241_real_votes.csv"
fil = sys.argv[1] if len(sys.argv) > 1 else "arbeid/oppgave_2132/agent.csv"
A = {r["id"]: r for r in csv.DictReader(open(fil, encoding="utf-8-sig", newline=""))}
F = [r for r in csv.DictReader(open(FASIT, encoding="utf-8", newline=""))
     if r.get("injection_flag") != "1" and r["year"] == "2026" and r["against_board"] != ""]
def prf(tp, fp, fn):
    p = tp / (tp + fp) if tp + fp else 0.0; r = tp / (tp + fn) if tp + fn else 0.0
    return p, r, (2 * p * r / (p + r) if p + r else 0.0)
def rad(navn, rut):
    m = [0, 0, 0]; s = [0, 0, 0]; g = [0, 0, 0]; n_rut = n_mot_rut = n_mot = 0
    for f in F:
        a = A[f"{f['meeting_id']}|{f['item_no']}"]
        y = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"
        x = a["anbefaling"] == "MOT" and (f["mgmt_rec"] or "FOR") != "MOT"
        r = rut(a); n_rut += r; n_mot_rut += r and y; n_mot += y
        m[0] += x and y; m[1] += x and not y; m[2] += (not x) and y
        xs = y if r else x  # øvre grense: mennesket avgjør rutede saker riktig
        s[0] += xs and y; s[1] += xs and not y; s[2] += (not xs) and y
        xg = False if r else x  # gulv: mennesket følger styret på rutede saker
        g[0] += xg and y; g[1] += xg and not y; g[2] += (not xg) and y
    f1 = lambda t: ("P %.2f / R %.2f / F1 %.3f" % prf(*t)).replace(".", ",")
    pst = f"{100*n_rut/len(F):.1f}".replace(".", ",")
    print(f"| {navn} | {n_rut} av {len(F)} ({pst} %) | {n_mot_rut} av {n_mot} | {f1(m)} (TP {m[0]} FP {m[1]} FN {m[2]}) | {f1(s)} (TP {s[0]} FP {s[1]} FN {s[2]}) | {f1(g)} |")
alle = sum(a["til_menneske"] == "1" for a in A.values())
print(f"Kilde: {fil}; inn {len(A)} saker, {alle} ({100*alle/len(A):.1f} %) til menneske; målt på {len(F)} saker med fasit (test 2026).\n")
print("| oppsett | saker til menneske | MOT mot styret blant dem | maskin alene | maskin + menneske (øvre grense, antar riktig menneskelig avgjørelse) | gulv: menneske følger styret |")
print("|---|---|---|---|---|---|")
rad("ingen til menneske", lambda a: False)
rad("bare båndet: kalibrert P(MOT) i [0,15; 0,85)", lambda a: a["til_menneske"] == "1" and "i båndet" in a["rutingsgrunn"])
rad("**standard** (bånd + ukjent selskap/type, injeksjon, datafeil, MOT uten sitat)", lambda a: a["til_menneske"] == "1")
