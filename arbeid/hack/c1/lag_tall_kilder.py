#!/usr/bin/env python3
"""Kilde for tallene i pakka som ikke står i måler v3-utskriften (#2276, dommer).
Skriver arbeid/hack/c1/tall_kilder_ut.txt (kilde B for c1_tallsjekk.py). Bare stdlib, leser prediksjonsfiler
og datafila, rører aldri modell eller prediksjoner. Kjør: python3 -I arbeid/hack/c1/lag_tall_kilder.py
Innhold: 1) menneske-tabellen (#2132/#2135) -> F1 0,779 / 0,828 / 0,294 / 0,269.
         2) klyngebootstrap-KI per selskap, seed 0, 2000 trekk, mot «følg styret» (#2103/#2134) -> KI i JURY.md.
         3) tellinger per splitt fra datafila (METODE.md) -> 9876 / 504 / 575 osv.
         4) avledet aritmetikk i TREFFSIKKERHET.md: accuracy i båndet, Clopper-Pearson 9/26, presisjon ved terskel 0,80."""
import csv, math, os, subprocess, sys, time
ROT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROT)
REAL = "state/opplastet/20261105_114241_real_votes.csv"
ut = [f"# tall_kilder_ut.txt, generert {time.strftime('%Y-%m-%d %H:%M')} av lag_tall_kilder.py (#2276)\n"]

ut.append("## 1) menneske_tabell.py på arbeid/oppgave_2132/agent.csv (kald standardkjøring)")
ut.append(subprocess.run([sys.executable, "-I", "arbeid/hack/c1/menneske_tabell.py", "arbeid/oppgave_2132/agent.csv"],
                         capture_output=True, text=True, check=True).stdout.rstrip())
ut.append("F1 0,779 = 2*37/(2*37+0+21) = %.4f; F1 0,269 = 2*9/(2*9+0+49) = %.4f" % (74 / 95, 18 / 67))

ut.append("\n## 2) diff_ki.py (#2103): parret klyngebootstrap per selskap, 2000 trekk, seed 0, rad mot null_test.csv (følg styret, F1 0)")
for navn, f in [("hovedmodell #2044 miks h2", "kontroll_h2_test"), ("regel b2", "regel_b2_test"), ("regel b", "regel_b_test"),
                ("regel a", "regel_a_test"), ("golv hist1", "hist1_test")]:
    r = subprocess.run([sys.executable, "-I", "arbeid/oppgave_2103/diff_ki.py", "arbeid/oppgave_2134/null_test.csv",
                        f"arbeid/oppgave_2134/{f}.csv", "test"], capture_output=True, text=True, check=True).stdout.strip()
    ut.append(f"{navn} ({f}.csv): {r}")

ut.append("\n## 3) tellinger per splitt fra datafila (rader med against_board satt = saker med fasit)")
F = list(csv.DictReader(open(REAL, encoding="utf-8", newline="")))
ut.append(f"datafil {REAL}: {len(F)} rader")
for navn, fn in [("train 2019-2024", lambda y: y <= 2024), ("val 2025", lambda y: y == 2025), ("test 2026", lambda y: y == 2026)]:
    R = [r for r in F if fn(int(r["year"])) and r.get("injection_flag") != "1" and r["against_board"] != ""]
    mot = sum(r["nbim_vote"] == "MOT" and r["against_board"] == "1.0" for r in R)
    avvik = sum(r["against_board"] == "1.0" for r in R)
    ut.append(f"{navn}: saker {len(R)} MOT mot styret {mot} avvik {avvik}")


def clopper_pearson(k, n, alfa=0.05):
    def cdf(p, k):  # P(X <= k)
        return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k + 1))
    def finn(f, mål, stigende):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            m = (lo + hi) / 2
            lo, hi = (m, hi) if (f(m) < mål) == stigende else (lo, m)
        return lo
    lo = 0.0 if k == 0 else finn(lambda p: 1 - cdf(p, k - 1), alfa / 2, True)   # P(X>=k) stiger med p
    hi = 1.0 if k == n else finn(lambda p: cdf(p, k), alfa / 2, False)          # P(X<=k) faller med p
    return lo, hi


ut.append("\n## 4) avledet aritmetikk i TREFFSIKKERHET.md")
ut.append("båndet konfidens >= 0,6 (TP 9 FP 0 FN 17 TN 1330 = 1356 saker): accuracy %.4f = %.2f %%, følg styret %.4f = %.1f %%"
          % (1339 / 1356, 100 * 1339 / 1356, 1330 / 1356, 100 * 1330 / 1356))
lo, hi = clopper_pearson(9, 26)
ut.append("Clopper-Pearson 95 %% recall i båndet 9/26: %.4f-%.4f = %.1f-%.1f %%" % (lo, hi, 100 * lo, 100 * hi))
lo, hi = clopper_pearson(30, 58)
ut.append("Clopper-Pearson 95 %% recall alle 30/58: %.4f-%.4f = %.1f-%.1f %%" % (lo, hi, 100 * lo, 100 * hi))
lo, hi = clopper_pearson(30, 68)
ut.append("Clopper-Pearson 95 %% presisjon alle 30/68: %.4f-%.4f = %.1f-%.1f %%" % (lo, hi, 100 * lo, 100 * hi))
ut.append("terskel 0,80 test TP/FP 41/176: presisjon 41/217 = %.4f, recall 41/58 = %.4f, F1 = %.4f" % (41 / 217, 41 / 58, 82 / (82 + 176 + 17)))

ut.append("\n## 5) terskelrader i TREFFSIKKERHET.md: P/R/F1 MOT mot styret regnet fra p_avvik i oppgave_2103/full_{val,test}.csv (#2044 miks h2)")
fas = {}
for f in F:
    if f["against_board"] == "" or f.get("injection_flag") == "1": continue
    fas[f"{f['meeting_id']}|{f['item_no']}"] = (int(f["year"]), f["mgmt_rec"] or "FOR", f["nbim_vote"] == "MOT" and f["against_board"] == "1.0")
for navn, fil, aar in [("val 2025", "arbeid/oppgave_2103/full_val.csv", 2025), ("test 2026", "arbeid/oppgave_2103/full_test.csv", 2026)]:
    S = {r["id"]: r for r in csv.DictReader(open(fil, encoding="utf-8", newline=""))}
    for t in (0.70, 0.80, 0.85, 0.90, 0.9188, 0.95, 0.97):
        tp = fp = fn = 0
        for i, (y, st, m) in fas.items():
            if y != aar or i not in S: continue
            a = ("FOR" if st == "MOT" else "MOT") if float(S[i]["p_avvik"]) >= t else st
            x = a == "MOT" and st != "MOT"
            tp += x and m; fp += x and not m; fn += (not x) and m
        P = tp / (tp + fp) if tp + fp else 0; R = tp / (tp + fn) if tp + fn else 0; F1 = 2 * P * R / (P + R) if P + R else 0
        ut.append(f"{navn} terskel {t}: P {P:.3f} R {R:.3f} F1 {F1:.3f} TP/FP {tp}/{fp}")

ut.append("\n## 6) treffsikkerhet_ki.py (#2185, frø 2185, 2000 trekk) på arbeid/oppgave_2132/agent.csv")
ut.append(subprocess.run([sys.executable, "-I", "arbeid/oppgave_2265/levering/treffsikkerhet_ki.py", "arbeid/oppgave_2132/agent.csv"],
                         capture_output=True, text=True, check=True).stdout.rstrip())

ut.append("\n## 7) øvre grenser i NESTE_VERSJON.md: F1 regnet fra oppgitte TP/FP/FN")
for navn, tp, fp, fn in [("GVG-gruppe test", 39, 38, 19), ("GVG-gruppe val", 55, 29, 44), ("revisor test", 33, 32, 25), ("revisor val", 59, 28, 40)]:
    ut.append(f"{navn}: TP {tp} FP {fp} FN {fn} -> F1 {2 * tp / (2 * tp + fp + fn):.4f}")

open("arbeid/hack/c1/tall_kilder_ut.txt", "w", encoding="utf-8").write("\n".join(ut) + "\n")
print("\n".join(ut))
