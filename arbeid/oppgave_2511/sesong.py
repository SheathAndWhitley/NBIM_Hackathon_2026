# Dekker test 2026 en hel sesong? Antall saker per år og måned, og om injection_flag er satt.
import sys, pandas as pd
d = pd.read_csv(sys.argv[1]); d["meeting_date"] = pd.to_datetime(d["meeting_date"]); d["y"] = d.meeting_date.dt.year
print(d.groupby("y").meeting_date.agg(["min", "max", "count"]))
print(d[d.y >= 2024].groupby(["y", d.meeting_date.dt.month]).size().unstack(fill_value=0))
print(d.injection_flag.value_counts(dropna=False))
