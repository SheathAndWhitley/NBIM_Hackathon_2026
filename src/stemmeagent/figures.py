"""Figures for the demo and the kravrespons (static PNG, light surface).

Palette: the dataviz skill's reference palette, categorical slots 1-3 only (blue,
orange, aqua). These three are documented as validated for all pairs in light and
dark mode; the validator script itself needs Node.js, which is not installed here.
Slot 3 (aqua) is below 3:1 contrast on the light surface, so every series is also
direct-labelled in text ink (relief rule), in addition to the legend.
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_curve

from .config import FIGURES
from .evaluate import expected_hits_at_budget

SURFACE = "#fcfcfb"
TEXT = "#0b0b0b"
TEXT2 = "#52514e"
GRID = "#e6e5e1"
REF = "#9a9994"
S1, S2, S3 = "#2a78d6", "#eb6834", "#1baf7a"


def _style(ax, xlabel, ylabel, title, subtitle=None):
    ax.set_facecolor(SURFACE)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=TEXT2, labelsize=9, length=0)
    ax.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.set_xlabel(xlabel, color=TEXT2, fontsize=10)
    ax.set_ylabel(ylabel, color=TEXT2, fontsize=10)
    ax.set_title(title, color=TEXT, fontsize=12, fontweight="semibold", loc="left", pad=22 if subtitle else 10)
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes, color=TEXT2, fontsize=9, va="bottom")


def _fig():
    fig, ax = plt.subplots(figsize=(7.2, 4.6), dpi=200)
    fig.patch.set_facecolor(SURFACE)
    return fig, ax


def _save(fig, name):
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(FIGURES / name, facecolor=SURFACE)
    plt.close(fig)


def _label_end(ax, x, y, text, dy=0):
    ax.annotate(text, (x, y), xytext=(6, dy), textcoords="offset points", color=TEXT, fontsize=9, va="center")


def budget_curve(y, score, grid=None):
    grid = np.linspace(0, 1, 101) if grid is None else grid
    pos = max(int(np.sum(y)), 1)
    return grid, np.array([expected_hits_at_budget(y, score, b) / pos for b in grid])


def fig_budget(te: pd.DataFrame, systems: dict, op: tuple | None, title: str, subtitle: str, name: str):
    fig, ax = _fig()
    _style(ax, "Andel forslag en analytiker leser (rangert etter risiko)", "Andel av NBIMs avvik som fanges", title, subtitle)
    ax.plot([0, 1], [0, 1], color=REF, linewidth=1.2)
    ax.annotate("Tilfeldig rekkefølge", (0.62, 0.55), color=TEXT2, fontsize=8.5, rotation=0)
    for (label, score), color in zip(systems.items(), (S1, S2, S3)):
        gx, gy = budget_curve(te["y"].values, np.asarray(score))
        ax.plot(gx, gy, color=color, linewidth=2, solid_capstyle="round", label=label)
        i = 20
        ax.plot(gx[i], gy[i], "o", color=color, markersize=8, markeredgecolor=SURFACE, markeredgewidth=2)
        _label_end(ax, gx[i], gy[i], f"{label}: {gy[i]:.0%} ved 20%", dy=0)
    if op:
        ax.axvline(op[0], color=GRID, linewidth=1, zorder=0)
        ax.plot(op[0], op[1], "o", color=S1, markersize=8, markeredgecolor=SURFACE, markeredgewidth=2, zorder=5)
        ax.annotate(f"Valgt kø: {op[0]:.0%} lest → {op[1]:.0%} fanget", (op[0], op[1]), xytext=(8, -16),
                    textcoords="offset points", color=TEXT2, fontsize=8.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.02)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    leg = ax.legend(loc="lower right", frameon=False, fontsize=9)
    for t in leg.get_texts():
        t.set_color(TEXT)
    _save(fig, name)


def fig_pr(te: pd.DataFrame, systems: dict, prevalence: float, title: str, subtitle: str, name: str):
    fig, ax = _fig()
    _style(ax, "Recall (andel av NBIMs avvik som flagges)", "Presisjon (andel flagg som er ekte avvik)", title, subtitle)
    ax.axhline(prevalence, color=REF, linewidth=1.2)
    ax.annotate(f"Alltid med styret / tilfeldig: {prevalence:.1%}", (0.62, prevalence), xytext=(0, -12),
                textcoords="offset points", color=TEXT2, fontsize=8.5)
    for (label, score), color in zip(systems.items(), (S1, S2, S3)):
        p, r, _ = precision_recall_curve(te["y"].values, np.asarray(score))
        ax.plot(r, p, color=color, linewidth=2, drawstyle="steps-post", label=label)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.02)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    leg = ax.legend(loc="upper right", frameon=False, fontsize=9)
    for t in leg.get_texts():
        t.set_color(TEXT)
    _save(fig, name)


def fig_calibration(bins: list[dict], title: str, subtitle: str, name: str):
    fig, ax = _fig()
    _style(ax, "Modellens sannsynlighet for avvik", "Faktisk andel avvik", title, subtitle)
    ax.plot([0, 1], [0, 1], color=REF, linewidth=1.2)
    b = pd.DataFrame(bins)
    ax.plot(b["predicted"], b["observed"], color=S1, linewidth=2)
    ax.plot(b["predicted"], b["observed"], "o", color=S1, markersize=8, markeredgecolor=SURFACE, markeredgewidth=2)
    for _, r in b.iterrows():
        if r["n"] >= 20 and r["predicted"] > 0.1:
            ax.annotate(f"n={int(r['n'])}", (r["predicted"], r["observed"]), xytext=(6, -10),
                        textcoords="offset points", color=TEXT2, fontsize=7.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.02)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    _save(fig, name)


def fig_policy(pv: dict, name: str):
    fig, ax = _fig()
    _style(ax, "", "NBIM stemte MOT", "Stemmer NBIM som retningslinjen sier? Ja, for CEO-lønn i USA",
           "Say-on-pay 2025-26. Terskel: NBIMs strengere vurdering av pakker over USD 20m (25m fra 2025)")
    labels = [f"CEO-lønn under terskelen", f"CEO-lønn over terskelen (n={pv['n_above_threshold']})"]
    vals = [pv["against_rate_below_threshold"], pv["against_rate_above_threshold"]]
    xs = np.arange(2)
    ax.bar(xs, vals, width=0.22, color=S1, edgecolor=SURFACE, linewidth=2)
    for x, v in zip(xs, vals):
        ax.annotate(f"{v:.0%}", (x, v), xytext=(0, 5), textcoords="offset points", ha="center",
                    color=TEXT, fontsize=11, fontweight="semibold")
    ax.set_xticks(xs, labels, color=TEXT)
    ax.set_ylim(0, max(vals) * 1.25)
    ax.set_xlim(-0.7, 1.7)
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    ax.grid(axis="x", visible=False)
    _save(fig, name)


def make_all(results: dict, te_ballot: pd.DataFrame, te_sop: pd.DataFrame) -> None:
    rb = results["ballot"]
    rq = rb["review_queue"]
    systems = {
        "Modell (presedens + tekst)": te_ballot["score"].values,
        "Samme som sist": (te_ballot["prev_same"] == 1).astype(float).values,
    }
    systems["Forslagstype-flertall"] = te_ballot["score_type_majority"].values  # training-period rates only
    n, dev = rb["split"]["test 2025-26"]["n"], rb["split"]["test 2025-26"]["deviations"]
    sub = f"Testsett 2025-26 (aldri brukt i utviklingen): {n} forslag, {dev} avvik fra styret"
    fig_budget(te_ballot, systems, (rq["share_reviewed"], rq["caught"] / rq["deviations"]),
               "Hvor mye må en analytiker lese for å fange NBIMs avvik?", sub, "ballot_review_budget.png")
    fig_pr(te_ballot, systems, dev / n, "Presisjon og recall på MOT-stemmer (hele stemmeseddelen)", sub, "ballot_pr.png")
    fig_calibration(rb["reliability"], "Kan konfidensen stoles på? Kalibrering på testsettet",
                    "Kalibrert på 2024, målt på 2025-26. Grå linje = perfekt kalibrert; n = forslag i gruppen",
                    "ballot_calibration.png")
    rs = results["say_on_pay"]
    if len(te_sop):
        tsop = te_sop.rename(columns={"against": "y"})
        sys_sop = {"Modell (lønnsdata fra proxy)": tsop["p"].values,
                   "NBIMs egen terskelregel": np.log10(tsop["peo_sct_total"].clip(lower=1)).fillna(0).values,
                   "Samme som sist": tsop["prev_against"].fillna(0).values}
        n2, d2 = len(tsop), int(tsop["y"].sum())
        fig_budget(tsop, sys_sop, None, "Say-on-pay i USA: rangering av lønnsforslag",
                   f"NBIMs egne stemmer (SEC N-PX), testsesong 2025-26: {n2} møter, {d2} MOT", "sop_review_budget.png")
        fig_policy(rs["policy_vs_practice"], "sop_policy_vs_practice.png")
