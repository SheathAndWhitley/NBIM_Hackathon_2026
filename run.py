"""One command that reproduces the main result.

    python run.py                 # everything from committed data (no network, no API key)
    python run.py --rebuild-data  # re-download SEC data first (needs SEC_USER_AGENT, ~15 min)

Writes results/metrics.json, results/predictions_test_ballot.csv,
results/predictions_test_sop.csv and the figures in results/figures/.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import warnings
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
warnings.filterwarnings("ignore")

from stemmeagent import audit, pipeline  # noqa: E402
from stemmeagent.config import RESULTS  # noqa: E402


def _row(name, m):
    return (f"  {name:15s} P={m['precision']:6.1%}  R={m['recall']:6.1%}  F1={m['f1']:.3f}  "
            f"PR-AUC={m['pr_auc']:.3f}  R@20%={m['recall@20%']:6.1%}  acc={m['accuracy']:6.1%}")


def rebuild_data() -> None:
    import pandas as pd
    from stemmeagent import cik_match, dataset, npx, proxy_xbrl, xbrl
    from stemmeagent.config import DATA_PROCESSED
    print("[0] Rebuilding SEC data (N-PX, CIK map, proxies, XBRL) ...")
    votes = npx.build_votes()
    imap = cik_match.match_issuers(votes)
    sop = dataset.sop_table(votes, imap[["cusip", "cik", "cik_match_method"]])
    proxy_xbrl.build(sop).to_csv(DATA_PROCESSED / "proxy_pvp.csv", index=False)
    f = xbrl.fact_table(prefer_processed=False)
    ciks = set(imap["cik"].dropna().astype(int))
    f[f["cik"].isin(ciks) & f["column"].isin(["revenue", "net_income", "diluted_shares"])] \
        .to_csv(DATA_PROCESSED / "xbrl_facts_subset.csv", index=False)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rebuild-data", action="store_true", help="re-download and rebuild the SEC-based tables")
    ap.add_argument("--no-figures", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    if args.rebuild_data:
        rebuild_data()

    results: dict = {}
    print("[1] Data audit")
    a = audit.run()
    results["data_audit"] = a
    print(f"  real_votes.csv: with the board {a['real_votes']['with_board_provided_label']:.1%} "
          f"(2025: {a['real_votes']['with_board_by_year'][2025]:.1%})  <- the baseline")
    print(f"  npx_votes.csv : with the board {a['npx_votes']['with_board_provided_label']:.1%} as labelled, "
          f"{a['npx_votes']['with_board_corrected']:.1%} corrected "
          f"({a['npx_votes']['mgmt_proposals_with_board_rec_MOT']} management proposals marked 'board says MOT')")
    if "sec_crosscheck" in a:
        s = a["sec_crosscheck"]
        print(f"  NBIM SEC N-PX vs real_votes: {s['real_vs_sec_agreement']:.1%} agree (n={s['real_vs_sec_matched']}); "
              f"npx_votes catches {s['of_which_npx_says_MOT']}/{s['sec_against_votes_in_npx_match']} SEC AGAINST votes")

    print("\n[2] Full ballot - NBIM's own votes (train 2019-23, choose on 2024, test 2025-26 once)")
    rb, te_ballot, mb = pipeline.run_ballot()
    results["ballot"] = rb
    t = rb["split"]["test 2025-26"]
    print(f"  test: {t['n']} proposals, {t['deviations']} deviations from the board ({t['rate']:.1%}); model: {rb['selected']}")
    for name in ("always_board", "persistence", "type_majority", "model_only", "hybrid"):
        print(_row(name, rb["test"][name]))
    rq = rb["review_queue"]
    print(f"  review queue: analysts read {rq['share_reviewed']:.0%} of proposals and catch "
          f"{rq['caught']}/{rq['deviations']}; auto-cleared misses: {rq['missed_in_autoclear']}")
    d = rb["test_hybrid_minus_persistence"]["pr_auc"]
    print(f"  hybrid - persistence, PR-AUC: {d['mean_diff']:+.3f} (95% CI {d['ci_low']:+.3f} to {d['ci_high']:+.3f})")

    print("\n[3] US say-on-pay deep dive - NBIM's SEC N-PX + pay data from each meeting's own proxy")
    rs, te_sop = pipeline.run_sop()
    results["say_on_pay"] = rs
    for name in ("always_board", "persistence", "nbim_pay_rule", "model"):
        print(_row(name, rs["test"][name]))
    pv = rs["policy_vs_practice"]
    print(f"  policy vs practice: AGAINST rate {pv['against_rate_above_threshold']:.0%} above NBIM's pay threshold "
          f"(n={pv['n_above_threshold']}) vs {pv['against_rate_below_threshold']:.1%} below")

    RESULTS.mkdir(parents=True, exist_ok=True)
    keep = ["meeting_id", "company", "country", "meeting_date", "item_no", "proposal_text", "proposal_type",
            "proponent", "board_rec", "nbim_vote", "y", "p", "score", "score_type_majority", "flag", "review", "prev_same",
            "prev_same_section", "rationale_section"]
    te_ballot[keep].to_csv(RESULTS / "predictions_test_ballot.csv", index=False)
    sop_keep = [c for c in te_sop.columns if c in (
        "issuer_name", "cik", "meeting_date", "against", "p", "flag", "review", "peo_sct_total", "rule_threshold",
        "pay_above_rule", "ceo_change", "peo_names", "tsr_1y", "rel_tsr_1y", "pay_pctile", "prev_against",
        "proxy_url", "source_url") or c.startswith("contrib_")]
    te_sop[sop_keep].to_csv(RESULTS / "predictions_test_sop.csv", index=False)

    agent_file = RESULTS / "agent_eval.json"
    if agent_file.exists():
        results["agent"] = json.loads(agent_file.read_text())
        print("\n[4] Agent (LLM) evaluation: loaded from results/agent_eval.json")
    else:
        print("\n[4] Agent (LLM) evaluation: not run yet (python -m stemmeagent.agent_eval, needs ANTHROPIC_API_KEY)")

    (RESULTS / "metrics.json").write_text(json.dumps(results, indent=2, default=lambda o: o if not hasattr(o, "item") else o.item()))
    if not args.no_figures:
        try:
            from stemmeagent import figures
            figures.make_all(results, te_ballot, te_sop)
            print(f"  figures -> {RESULTS / 'figures'}")
        except ImportError:
            pass
    print(f"\nWrote {RESULTS / 'metrics.json'}  ({time.time() - t0:.0f}s)")


if __name__ == "__main__":
    main()
