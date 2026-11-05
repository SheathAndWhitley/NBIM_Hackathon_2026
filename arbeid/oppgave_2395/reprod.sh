#!/bin/sh
# Case 1, ERLIG_EVALUERING.md § 5: alle robusthetstallene fra kald kopi med én kommando (smed3 #2395).
# Bruk (fra roten av repoet): sh arbeid/oppgave_2395/reprod.sh [/tmp/c1_kald_2395] [utmappe]   (ca. 2,5 min)
# Skriver: HOVEDTALL (F1 MOT fra fremmed.sh), byte-likhet mot leverte svarfiler, 16-testers tabell,
# før/nå-sammenligning (N/16 likt), og de fem forslagene som får grunnen «instruksjonslignende tekst i forslaget».
set -eu
ROT="$(cd "$(dirname "$0")/../.." && pwd)"; cd "$ROT"
KOPI="${1:-/tmp/c1_kald_2395}"; UT="${2:-$ROT/arbeid/oppgave_2395/ut}"; mkdir -p "$UT"
echo "== 1) kald kopi + hovedtall (fremmed.sh) =="
sh arbeid/hack/levering/fremmed.sh "$KOPI" > "$UT/fremmed.log" 2>&1 || { echo "fremmed.sh feilet rc=$?"; tail -5 "$UT/fremmed.log"; exit 1; }
grep -E "^HOVEDTALL|^tid:|^TALLVAKT|^Måler v3" "$UT/fremmed.log"
echo "== 2) byte-likhet mot leverte filer =="
cmp "$KOPI/ut/_pred_uten_ruting.csv" arbeid/hack/levering/kjor_agent_real_maskin_alene.csv && echo "BYTE-LIK: _pred_uten_ruting.csv == kjor_agent_real_maskin_alene.csv"
cmp "$KOPI/ut/pred_maaler.csv" arbeid/hack/levering/kjor_agent_real_pred_maaler.csv && echo "BYTE-LIK: pred_maaler.csv == kjor_agent_real_pred_maaler.csv"
echo "== 3) 16 feiltester i kald kopi (kopiens python, env -i) =="
python3 -I arbeid/oppgave_2380/robusthet_kald.py "$KOPI" "$UT" > "$UT/robusthet.log" 2>&1
cat "$UT/tabell.md"
echo "== 4) før (#2063/#2071) mot nå =="
python3 -I arbeid/oppgave_2380/sammenlign.py arbeid/oppgave_2063/tabell.md "$UT/tabell.md" | tee "$UT/sammenlign.md"
echo "== 5) saker med grunnen «instruksjonslignende tekst i forslaget» (uten injeksjonstestene) =="
python3 -I - "$UT/resultat.json" <<'PY'
import json, sys
R = json.load(open(sys.argv[1]))
n = 0
for t in R:
    if "injeksjon" in t["test"]: continue
    for r in t["rader"]:
        if "instruksjonslignende" in r["rutingsgrunn"]:
            n += 1; print(f"  {t['test']}: «{r.get('proposal_text','')[:60]}» -> {r['rutingsgrunn'][:90]}")
print(f"ANTALL instruksjonslignende utenfor injeksjonstestene: {n}")
PY
echo "== 6) rutingsgrunn for grensesaker =="
grep -o "usikker: kalibrert P(MOT) [0-9.]* i båndet \[0.15, 0.85)" "$UT/tabell.md" | sort -u | head -3
echo "FERDIG: $UT"
