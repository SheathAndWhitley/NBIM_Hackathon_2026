"""Central configuration: paths, seasons and the fixed choices the evaluation depends on."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
RESULTS = ROOT / "results"
FIGURES = RESULTS / "figures"
LOGS = ROOT / "logs"
DOCS = ROOT / "docs"

# Norges Bank (NBIM) files Form N-PX as an institutional manager (say-on-pay votes only).
NBIM_CIK = 1374170

# N-PX reporting years run 1 July - 30 June. Label -> period end.
SEASONS = {"2023-24": "2024-06-30", "2024-25": "2025-06-30", "2025-26": "2026-06-30"}
HISTORY_SEASON = "2023-24"  # used for "previous vote" features and the stability check
TRAIN_SEASON = "2024-25"    # model selection, calibration and thresholds are chosen here only
TEST_SEASON = "2025-26"     # holdout: evaluated once, never used for any choice

RANDOM_SEED = 2026
N_BOOTSTRAP = 2000

# Point-in-time rule for XBRL facts: a fiscal period may only be used for a meeting
# if it ended at least this many days before the meeting date.
PIT_MIN_LAG_DAYS = 60

# NBIM's published US rule: a stricter assessment of the largest CEO packages.
#   Voting review H1 2024: "those worth 20 million dollars or more"
#   Voting review H1 2025: "those worth 25 million dollars or more, after making an
#                          inflationary adjustment"  (applied in 2025)
# The rule baseline uses the threshold in force at the meeting date.
RULE_PAY_THRESHOLDS = [("2000-01-01", 20_000_000), ("2025-01-01", 25_000_000)]
RULE_PAY_THRESHOLD_USD = 20_000_000  # display default


def rule_threshold(meeting_date) -> int:
    """USD threshold of NBIM's stricter US assessment in force at `meeting_date`."""
    import pandas as pd
    d = pd.Timestamp(meeting_date)
    out = RULE_PAY_THRESHOLDS[0][1]
    for start, thr in RULE_PAY_THRESHOLDS:
        if d >= pd.Timestamp(start):
            out = thr
    return out
