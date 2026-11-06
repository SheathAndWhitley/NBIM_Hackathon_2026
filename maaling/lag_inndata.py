"""Lager agentens inndata for test 2026 fra data/real_votes.csv: alle saker fra 2026 uten fasit- og
begrunnelsesfeltene (nbim_vote, against_board, rationale_*, position_paper). id = meeting_id|item_no.
Bruk:  python3 maaling/lag_inndata.py [real_votes.csv]   ->  ut/inndata/test_2026.csv   (kjøres av KJOR.sh)
"""
import csv, os, sys

ROT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REAL = os.path.join(ROT, "data/real_votes.csv")
UT = os.path.join(ROT, "ut/inndata")
KOLONNER = ["id", "injection_flag", "meeting_id", "company_id", "company", "ticker", "country", "market", "meeting_date",
            "item_no", "proposal_number", "proposal_text", "proponent", "mgmt_rec_raw", "mgmt_rec", "year", "proposal_type"]


def main(a):
    kilde = a[0] if a else REAL
    rader = list(csv.DictReader(open(kilde, encoding="utf-8", newline="")))
    os.makedirs(UT, exist_ok=True)
    for navn, aar in (("test_2026.csv", "2026"),):
        sti = os.path.join(UT, navn)
        with open(sti, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\r\n")
            w.writerow(KOLONNER)
            n = 0
            for r in rader:
                if r["year"] != aar: continue
                w.writerow([f'{r["meeting_id"]}|{r["item_no"]}' if k == "id" else r[k] for k in KOLONNER]); n += 1
        print(f"laget {os.path.relpath(sti, ROT)}: {n} saker fra {aar}, uten fasitfelt")


if __name__ == "__main__":
    main(sys.argv[1:])
