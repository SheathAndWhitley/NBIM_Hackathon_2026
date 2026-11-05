"""Agent (LLM) evaluation: citation accuracy against NBIM's published sections and the
adversarial test (motstandstest).

    python run_agent.py              # recompute every agent metric from results/llm_cache.jsonl (no key)
    python run_agent.py --dry-run    # sample sizes, cost estimate and an example prompt
    python run_agent.py --run        # call Claude via the Message Batches API (needs ANTHROPIC_API_KEY,
                                     # e.g. in the git-ignored file .env); answers are cached
    python run_agent.py --run --live # synchronous calls instead of a batch

Afterwards, `python run.py` merges results/agent_eval.json into metrics.json and nokkeltall.md.
"""
import sys
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
warnings.filterwarnings("ignore")

from stemmeagent.agent_eval import main  # noqa: E402

if __name__ == "__main__":
    main()
