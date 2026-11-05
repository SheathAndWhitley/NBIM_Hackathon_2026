"""Figur for juryen (sak 2497): rullende F1 MOT per testår, frossen vs + personnøkkel.
Tallene leses direkte fra tabellen i state/rapporter/c1_personnokkel_rullende.md (ingen tall skrevet for hånd)."""
import re, sys, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
RAPPORT = os.path.join(ROT, "state/rapporter/c1_personnokkel_rullende.md")
UT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "c1_personnokkel_rullende.png")

tall = lambda s: float(s.replace("−", "-").replace(",", "."))
rader = {}
for l in open(RAPPORT, encoding="utf-8"):
    m = re.match(r"\| (\d{4}) \(val \d{4}\) \| (uten|\+ person)[^|]*\| ([\d,]+) \|[^|]*\|[^|]*\| *(.*?) *\|", l)
    if not m:
        continue
    aar, var, f1, ki = int(m[1]), m[2], tall(m[3]), m[4]
    rader.setdefault(aar, {})[var] = f1
    k = re.search(r"\*\*([−+\-\d,]+)\*\* \[([−+\-\d,]+); ([−+\-\d,]+)\]", ki)
    if k:
        rader[aar]["ki"] = (tall(k[1]), tall(k[2]), tall(k[3]))
aar = sorted(rader)
assert aar == [2024, 2025, 2026] and all(len(rader[a]) == 3 for a in aar), rader
uten = [rader[a]["uten"] for a in aar]
med = [rader[a]["+ person"] for a in aar]

fig, ax = plt.subplots(figsize=(7.5, 4.6), dpi=150)
ax.axhline(0, color="#888", lw=1.2, ls="--")
ax.text(2023.75, 0.012, "grunnlinje «følg styret» = 0 (predikerer aldri MOT)", color="#666", fontsize=8)
ax.plot(aar, uten, "o-", color="#2a6fb0", lw=2, label="frossen modell (uten personnøkkel)")
ax.plot(aar, med, "s-", color="#d9822b", lw=2, label="+ personnøkkel (repoets prev_same_person)")
for a, u, p in zip(aar, uten, med):
    d, lo, hi = rader[a]["ki"]
    x = a + 0.07
    ax.plot([x, x], [u + lo, u + hi], color="#d9822b", lw=1.2, alpha=0.7)
    ax.plot([x - 0.02, x + 0.02], [u + lo] * 2, color="#d9822b", lw=1.2, alpha=0.7)
    ax.plot([x - 0.02, x + 0.02], [u + hi] * 2, color="#d9822b", lw=1.2, alpha=0.7)
    ou, op = (8, -14) if u < p else (8, -14)
    ax.annotate(f"{u:.4f}".replace(".", ","), (a, u), textcoords="offset points", xytext=(-40, 6 if u >= p else -12), fontsize=8, color="#2a6fb0")
    ax.annotate(f"{p:.4f}".replace(".", ","), (a, p), textcoords="offset points", xytext=(-40, 6 if p > u else -12), fontsize=8, color="#d9822b")
    s = lambda v: f"{v:+.3f}".replace(".", ",").replace("-", "−")
    ax.text(a, 0.655, f"person − uten {s(d)}\n95 % KI [{s(lo)}; {s(hi)}]", fontsize=7.5, color="#7a4a10", ha="center", va="top")
    0 and ax.text(x + 0.04, u + hi, f"diff {s(d)}\n[{s(lo)}; {s(hi)}]", fontsize=7.5, color="#7a4a10", va="top")
ax.set_xticks(aar, [f"{a}\n(val {a-1})" for a in aar])
ax.set_xlim(2023.7, 2026.5)
ax.set_ylim(-0.03, 0.68)
ax.set_xlabel("Testår (C og terskel valgt på året før)")
ax.set_ylabel("F1 på MOT-stemmer")
ax.set_title("Personnøkkelen hjelper bare i 2026: rullende F1 MOT (ikke hovedtall)", fontsize=10.5)
ax.legend(loc="lower right", bbox_to_anchor=(1, 0.08), fontsize=8, frameon=False)
fig.text(0.01, 0.01, "Strek = 95 % KI for (person − uten), lagt på «uten»-punktet. Parret klyngebootstrap per selskap, 2000 trekk.\n"
         "Kilde: state/rapporter/c1_personnokkel_rullende.md (sak 2496). Hovedtallet er frossen 2026 = 0,4762.", fontsize=7, color="#555")
fig.subplots_adjust(bottom=0.24)
fig.savefig(UT)
print("skrev", UT)
for a, u, p in zip(aar, uten, med):
    print(a, "uten", u, "person", p, "ki", rader[a]["ki"])
