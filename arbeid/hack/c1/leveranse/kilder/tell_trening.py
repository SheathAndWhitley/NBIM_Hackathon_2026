# Teller treningsradene for test-modellen: real_votes før 2026, uten injeksjonsrader og med fasit (against_board).
# Kjør: python3 -I tell_trening.py <real_votes.csv>
import sys, pandas as pd
d = pd.read_csv(sys.argv[1]); d["dato"] = pd.to_datetime(d.meeting_date)
a = d[d.dato.dt.year < 2026]
print("alle rader", len(d), "| test 2026", (d.dato.dt.year == 2026).sum(), "| før 2026", len(a))
print("injeksjonsrader før 2026", int((a.injection_flag != 0).sum()), "| uten fasit (against_board tom)", int(a.against_board.isna().sum()))
print("trening (begge krav)", int(((a.injection_flag == 0) & a.against_board.notna()).sum()))
