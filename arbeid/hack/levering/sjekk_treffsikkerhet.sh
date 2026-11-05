#!/bin/sh
# Case 1: sjekk treffsikkerheten selv, med én kommando (#2206, ordre #241).
# Bruk (fra landsbymappen eller roten av en kald kopi fra fremmed.sh):
#   sh arbeid/hack/levering/sjekk_treffsikkerhet.sh [UTMAPPE]     (standard /tmp/c1_sjekk_<tid>)
# 1) kjører kjor_agent.py på hele test 2026 fra rådata (real_votes), ikke den lagrede prediksjonsfila
# 2) teller 2x2 for MOT mot styret selv, direkte mot fasit (nbim_vote, against_board) i real_votes-fila;
#    bruker verken måleren eller pakkas tellekode
# 3) skriver accuracy agent vs følg styret, recall/presisjon/F1 på MOT, antall til menneske,
#    og sha256 av den nye fila mot den frosne d02cf884…4a0c
set -eu
ROT="$(cd "$(dirname "$0")/../../.." && pwd)"
UT="${1:-/tmp/c1_sjekk_$(date +%H%M%S)}"
FROSSEN=d02cf88475bfee934c204827ce2f01bd6cffe3fb61e407a3d86da660efcd4a0c
FASIT="$ROT/state/opplastet/20261105_114241_real_votes.csv"
# rotsjekk (#2339): gi en klar feil hvis skriptet ikke står i et repo eller en kald kopi fra fremmed.sh
[ -f "$ROT/arbeid/oppgave_2044/train.py" ] && [ -f "$FASIT" ] || {
  echo "FEIL STED: fant ikke modellen og dataene under $ROT."
  echo "Kjør fra roten av repoet eller av en kald kopi laget med fremmed.sh: sh arbeid/hack/levering/sjekk_treffsikkerhet.sh"
  echo "Mappa levering/ alene er ikke nok, se README.md («Hvor du står»)."; exit 6; }
cd "$ROT"
rm -rf "$UT"
T0=$(date +%s)
# python med modellens låste pakker: kald kopi har egen .venv i roten, landsbymappen bruker smed2_c1_mot
if [ -x "$ROT/.venv/bin/python" ] && "$ROT/.venv/bin/python" -c "import lightgbm" 2>/dev/null; then
  PY="$ROT/.venv/bin/python"
else
  PY="uv run -q --project $ROT/arbeid/kandidater/smed2_c1_mot python"
fi
echo "kjører agenten på test 2026 fra rådata -> $UT"
$PY arbeid/hack/levering/kjor_agent.py --ut "$UT" > "$UT.logg" 2>&1 || { echo "AGENTEN FEILET, se $UT.logg"; tail -20 "$UT.logg"; exit 2; }
T1=$(date +%s)
RC=0
python3 -I - "$UT/agent.csv" "$FASIT" <<'PY' || RC=$?
import csv, sys
agent = {r["id"]: r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"))}
t = dict(TP=0, FP=0, FN=0, TN=0); n_fasit = mangler = ikke_svar = 0; menneske = dict(TP=0, FP=0, FN=0, TN=0)
for f in csv.DictReader(open(sys.argv[2], encoding="utf-8")):
    if f.get("injection_flag") == "1" or f["year"] != "2026": continue
    if f["against_board"] == "": mangler += 1; continue
    i = f"{f['meeting_id']}|{f['item_no']}"
    if i not in agent: ikke_svar += 1; continue
    a = agent[i]; n_fasit += 1
    # MOT mot styret = stemme MOT der styret ikke sier MOT (samme definisjon som fasit). 3 saker der styret
    # sier MOT og både agent og NBIM stemte FOR, er avvik i FOR-retning og telles ikke som MOT (blir TN)
    sier_mot = a["anbefaling"] == "MOT" and f["mgmt_rec"] != "MOT"      # agenten stemmer MOT styret
    var_mot = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"   # NBIM stemte faktisk MOT styret
    k = ("T" if sier_mot == var_mot else "F") + ("P" if sier_mot else "N")
    t[k] += 1
    if a["til_menneske"] == "1": menneske[k] += 1
n = sum(t.values()); TP, FP, FN, TN = t["TP"], t["FP"], t["FN"], t["TN"]
P = TP / max(TP + FP, 1); R = TP / max(TP + FN, 1); F1 = 2 * P * R / max(P + R, 1e-12)
tm_alle = sum(1 for a in agent.values() if a["til_menneske"] == "1")
print(f"\nTEST 2026: {len(agent)} saker inn, {n} med fasit ({mangler} uten fasit utelatt, {ikke_svar} uten svar)")
print(f"2x2 MOT mot styret:  TP {TP}  FP {FP}  FN {FN}  TN {TN}")
print(f"  accuracy agent        {(TP+TN)/n:.4f}  ({(TP+TN)/n*100:.1f} %)")
print(f"  accuracy følg styret  {(TN+FP)/n:.4f}  ({(TN+FP)/n*100:.1f} %)  <- finner 0 av {TP+FN} MOT, F1 0")
print(f"  MOT: recall {R:.4f}  presisjon {P:.4f}  F1 {F1:.4f}   <- hovedtallet er F1 på MOT")
print(f"  til menneske: {tm_alle} av {len(agent)} saker inn ({tm_alle/len(agent)*100:.1f} %), "
      f"{sum(menneske.values())} av {n} med fasit (der: TP {menneske['TP']} FP {menneske['FP']} FN {menneske['FN']} TN {menneske['TN']})")
fasit = (TP, FP, FN, TN) == (32, 35, 26, 1446)
print("  forventet TP 32 FP 35 FN 26 TN 1446:", "STEMMER" if fasit else "AVVIK (se over)")
sys.exit(0 if fasit else 3)
PY

SHA=$(shasum -a 256 "$UT/pred_maaler.csv" | cut -d" " -f1)
if [ "$SHA" = "$FROSSEN" ]; then echo "  sha256 ny prediksjonsfil = frossen fil (d02cf884…4a0c): LIK"
else echo "  sha256 ny prediksjonsfil $SHA != frossen d02cf884…4a0c: ULIK"; RC=5; fi
echo "tid: agent $((T1 - T0)) s, totalt $(( $(date +%s) - T0 )) s. Agentens logg: $UT.logg"
exit $RC
