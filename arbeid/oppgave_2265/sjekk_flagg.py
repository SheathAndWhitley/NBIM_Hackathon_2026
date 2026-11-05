"""Flaggsjekk for vakta i en gitt mappe: falske flagg på ren test 2026 / val 2025, og fangst per angrepsfrase."""
import sys, csv, importlib, pandas as pd
mappe = sys.argv[1]; sys.path.insert(0, mappe); sys.path.insert(0, "arbeid/oppgave_2237"); sys.path.insert(0, "arbeid/oppgave_2265")
import injeksjon_hoflig as hoflig, fraser as F, blinde as B
print("modul:", hoflig.__file__)
H = pd.read_csv("state/opplastet/20261105_114241_real_votes.csv", low_memory=False)
H["_id"] = H.meeting_id.astype(str) + "|" + H.item_no.astype(str)
inn = list(csv.DictReader(open("arbeid/hack/c1/data_off/real_test_input.csv", encoding="utf-8-sig")))
ids = {r["id"] for r in inn}; T = [r["proposal_text"] for r in inn]
hoflig.bygg(H.proposal_text[H.year < 2025]); val = list(H[H.year == 2025].proposal_text.fillna(""))
fv = [t for t in val if hoflig.finn(t) is not None]
hoflig.bygg(H.proposal_text[~H._id.isin(ids)])
ft = [t for t in T if hoflig.finn(t) is not None]
print(f"falske flagg: test 2026 {len(ft)}/{len(T)}, val 2025 {len(fv)}/{len(val)}")
for t in ft + fv: print("   ", t[:110])
for navn, sett in [("BYGD", F.BYGD), ("NYE", F.NYE), ("BLINDE1", B.BLINDE), ("BLINDE2", B.BLINDE2)]:
    for k, f in sett.items():
        n = sum(hoflig.finn(t + f) is not None for t in T)
        eks = T[0] + f; p = hoflig.finn(eks)
        print(f"{navn:8s} {k:18s} {n:5d}/{len(T)}  kutt: «{eks[p:] if p is not None else '-'}»")
