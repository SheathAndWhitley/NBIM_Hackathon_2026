"""Case 1 (#2897): lager agentens inndata fra arrangørens real_votes.csv, uten fasitfelt.
data_off/real_test_input.csv = år 2026 (holdout), data_off/real_val_input.csv = år 2025. id = meeting_id|item_no.
Byte-likt med filene modellen ble frosset mot (sha256 sjekkes av c1_real.py og frysvakta). Bare standardbiblioteket.
Bruk:  python3 arbeid/hack/c1/lag_inndata.py [real_votes.csv]   (standard: state/opplastet/20261105_114241_real_votes.csv)
"""
import csv, os, sys

ROT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
REAL = os.path.join(ROT, "state/opplastet/20261105_114241_real_votes.csv")
UT = os.path.join(ROT, "arbeid/hack/c1/data_off")
KOLONNER = ["id", "injection_flag", "meeting_id", "company_id", "company", "ticker", "country", "market", "meeting_date",
            "item_no", "proposal_number", "proposal_text", "proponent", "mgmt_rec_raw", "mgmt_rec", "year", "proposal_type"]


def main(a):
    kilde = a[0] if a else REAL
    rader = list(csv.DictReader(open(kilde, encoding="utf-8", newline="")))
    os.makedirs(UT, exist_ok=True)
    for navn, aar in (("real_test_input.csv", "2026"), ("real_val_input.csv", "2025")):
        sti = os.path.join(UT, navn)
        with open(sti, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\r\n")
            w.writerow(KOLONNER)
            n = 0
            for r in rader:
                if r["year"] != aar: continue
                w.writerow([f'{r["meeting_id"]}|{r["item_no"]}' if k == "id" else r[k] for k in KOLONNER]); n += 1
        print(f"laget {os.path.relpath(sti, ROT)}: {n} saker fra år {aar}, uten fasitfelt")


if __name__ == "__main__":
    main(sys.argv[1:])
