"""Omfang (selskaper, år, markeder) i real_votes og test 2026-input, for avgrensningslinja i 1-sideren (#2332)."""
import pandas as pd
f = "state/opplastet/20261105_114241_real_votes.csv"
d = pd.read_csv(f, low_memory=False)
print("kolonner:", list(d.columns)[:25])
yr = "year" if "year" in d else None
print(f"real_votes: {len(d)} saker, {d.company_id.nunique()} selskaper, {d.meeting_id.nunique()} møter, {d.country.nunique()} land")
print("år:", d[yr].min(), "-", d[yr].max(), d[yr].value_counts().sort_index().to_dict())
print(f"sakstyper (proposal_type): {d.proposal_type.nunique()}")
print("market:", d.market.value_counts().to_dict())
print("topp land:", d.country.value_counts().head(8).to_dict())
t = pd.read_csv("arbeid/hack/c1/data_off/real_test_input.csv")
print(f"test-input: {len(t)} saker, {t.company_id.nunique()} selskaper, {t.country.nunique()} land, år {sorted(t.year.unique())}, market {t.market.value_counts().to_dict()}")
