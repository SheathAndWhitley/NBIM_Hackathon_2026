"""Case 1 (#2899, ordre #282): tabell over når hver REGEL.md ble skrevet, mot første resultatfil i samme mappe.
Tidene er filenes mtime i landsbyens arbeidsmappe (git tar ikke vare på dem), lest når repoen synkes.
Bruk: python3 -I arbeid/verktoy/c1_regel_tid.py > REGEL_TIDSSTEMPLER.md   (github_synk.sh gjør det i stagen)"""
import glob, os, time
ROT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
t = lambda p: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(p)))
regler = [l.strip() for l in open(os.path.join(ROT, "arbeid/verktoy/c1_henviste_filer.txt"), encoding="utf-8")
          if l.strip().endswith("/REGEL.md")]
print("# Når bytteregelen ble skrevet: REGEL.md mot første måling\n")
print("Bytteregelen (ordre #265/#281) skal stå skrevet før kandidaten måles. Tabellen viser filtiden (mtime på")
print("utviklingsmaskinen, Europe/Oslo) for hver REGEL.md og for den eldste resultatfila (csv) i samme mappe.")
print("git lagrer ikke filtider, så tidene er lest av `arbeid/verktoy/c1_regel_tid.py` ved synk.\n")
print("| REGEL.md | skrevet | første resultatfil | laget | regel først? |\n|---|---|---|---|---|")
for r in regler:
    p = os.path.join(ROT, r)
    if not os.path.isfile(p): continue
    csv = sorted(glob.glob(os.path.join(os.path.dirname(p), "*.csv")), key=os.path.getmtime)
    if csv:
        c = csv[0]; ok = "ja" if os.path.getmtime(p) <= os.path.getmtime(c) else "**nei**"
        print(f"| `{r}` | {t(p)} | `{os.path.basename(c)}` | {t(c)} | {ok} |")
    else:
        print(f"| `{r}` | {t(p)} | (ingen ennå) | | |")
