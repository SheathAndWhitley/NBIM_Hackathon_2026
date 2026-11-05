#!/bin/sh
# Case 1 (#2191 smed, utvidet #2322 arkitekt): lager demo-reserven på nytt og sjekker den mot frysvakta (#2142).
# Kjør fra hvor som helst (ca. 1 min): sh arbeid/hack/levering/demo/reserve/lag_reserve.sh
#   1) frysvakt FØR: state/c1_frys.json må finnes og alle frosne filer være like. Ellers utgang 4, reserven urørt.
#   2) kjører de samme demo-utskriftene som #2191 (saker 1-6, sak 7, fremmed.sh kald kopi, demo_vis 3 saker)
#      inn i en ny mappe (reserve.ny), ikke rett i reserven.
#   3) SHA.txt: sha256 av kjor_agent.py, c1_real.py, prediksjonsfilene og den kalde kopiens agent.csv,
#      og hver frosset sha sammenlignet med state/c1_frys.json linje for linje.
#   4) frysvakt ETTER + HOVEDTALL/TALLVAKT GRØNN i utskrift 3. Alt grønt: ny reserve flyttes på plass
#      (gammel til /tmp/c1_reserve_forrige_<tid>), utgang 0. Ellers utgang 4 og gammel reserve står.
# Gammel versjon uten sjekk: lag_reserve_2191.sh. C1_FRYS / C1_FRYS_ROT virker som i c1_frys.py (bare test).
set -u
KILDE="$(cd "$(dirname "$0")/../../../../.." && pwd)"
R="$KILDE/arbeid/hack/levering/demo/reserve"
N="${C1_RESERVE_UT:-$R.ny}"   # C1_RESERVE_UT: bare test, da flyttes ingenting på plass
FRYS="${C1_FRYS:-$KILDE/state/c1_frys.json}"
cd "$KILDE"
stopp() { echo "RESERVE STOPP: $1"; echo "gammel reserve urørt: $(head -1 "$R/SHA.txt" 2>/dev/null)"; exit 4; }

# 1) frysvakt før
python3 -I arbeid/verktoy/c1_frys.py sjekk --krev || stopp "frysvakta er ikke grønn før kjøring (se over)"

# 2) demo-utskriftene, samme kommandoer som #2191
rm -rf "$N"; mkdir -p "$N/csv"
bash arbeid/hack/c1/demo_saker_2026.sh /tmp/c1_res_saker > "$N/1_saker_2026.txt" 2>&1 || stopp "demo_saker_2026.sh feilet ($N/1_saker_2026.txt)"
bash arbeid/hack/c1/demo_mangler_styret.sh /tmp/c1_res_mangler > "$N/2_mangler_styret.txt" 2>&1 || stopp "demo_mangler_styret.sh feilet"
M=/tmp/c1_res_kald
sh arbeid/hack/levering/fremmed.sh "$M" > "$N/3_fremmed_kald_kopi.txt" 2>&1; rc=$?
[ $rc -eq 0 ] || stopp "fremmed.sh utgang $rc (4 = frysvakt rød i kald kopi), se $N/3_fremmed_kald_kopi.txt"
env -i HOME="$M/home" PATH="$M/.venv/bin:/usr/bin:/bin" LANG=C.UTF-8 "$M/.venv/bin/python" -I \
  arbeid/hack/c1/leveranse/demo_vis.py "$M/ut/agent.csv" "$M/state/opplastet/20261105_114241_real_votes.csv" \
  > "$N/4_demo_vis_3_saker.txt" 2>&1 || stopp "demo_vis.py feilet"
cp /tmp/c1_res_saker/demo5/agent.csv "$N/csv/demo5_agent.csv"
cp /tmp/c1_res_saker/sitat/agent.csv "$N/csv/sitat_agent.csv"
cp /tmp/c1_res_mangler/uten/agent.csv "$N/csv/mangler_styret_agent.csv"
cp "$M/ut/agent.csv" "$N/csv/test2026_agent.csv"
cp "$M/ut/KJORING.txt" "$N/csv/test2026_KJORING.txt"

# 3) SHA.txt med sammenligning mot frysen
python3 -I - "$FRYS" "$N/SHA.txt" "$N/csv/test2026_agent.csv" <<'PY' || stopp "sha avviker fra frysen (se $N/SHA.txt)"
import datetime, hashlib, json, sys
frys = json.load(open(sys.argv[1]))
def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
linjer = [f"laget {datetime.datetime.now():%Y-%m-%d %H:%M:%S}, frys {frys['tid']} ({frys.get('modell', '')})"]
feil = 0
for f in ["arbeid/hack/levering/kjor_agent.py", "arbeid/hack/levering/c1_real.py",
          "arbeid/hack/levering/kjor_agent_real_maskin_alene.csv", "arbeid/oppgave_2103/full_test.csv",
          "arbeid/oppgave_2044/pred_miks_h2.csv"]:
    h, fh = sha(f), frys["filer"].get(f)
    ok = "LIK FRYS" if h == fh else ("IKKE I FRYS" if fh is None else f"AVVIK (frosset {fh[:12]})")
    feil += h != fh
    linjer.append(f"{h}  {f}  {ok}")
linjer.append(f"{sha(sys.argv[3])}  reserve/csv/test2026_agent.csv  (kald kopi, ikke i frysen)")
linjer.append("SHA-SJEKK GRØNN: alle 5 lik frysen" if not feil else f"SHA-SJEKK RØD: {feil} avvik")
open(sys.argv[2], "w").write("\n".join(linjer) + "\n")
print("\n".join(linjer))
sys.exit(1 if feil else 0)
PY

# 4) frysvakt etter (ingen fil endret under kjøringen) og tallene i utskrift 3
python3 -I arbeid/verktoy/c1_frys.py sjekk --krev >> "$N/SHA.txt" 2>&1 || stopp "frysvakta ble rød under kjøringen"
grep -q '^HOVEDTALL' "$N/3_fremmed_kald_kopi.txt" || stopp "HOVEDTALL mangler i utskrift 3"
grep -q 'TALLVAKT GRØNN' "$N/3_fremmed_kald_kopi.txt" || stopp "TALLVAKT GRØNN mangler i utskrift 3"
grep '^HOVEDTALL' "$N/3_fremmed_kald_kopi.txt" >> "$N/SHA.txt"

# alt grønt: ny reserve på plass, skriptene blir med
[ -n "${C1_RESERVE_UT:-}" ] && { echo "TEST GRØNN: reserve i $N, ikke flyttet"; cat "$N/SHA.txt"; exit 0; }
G="/tmp/c1_reserve_forrige_$(date +%H%M%S)"; mkdir -p "$G"
for f in 1_saker_2026.txt 2_mangler_styret.txt 3_fremmed_kald_kopi.txt 4_demo_vis_3_saker.txt SHA.txt; do
  [ -f "$R/$f" ] && mv "$R/$f" "$G/"; mv "$N/$f" "$R/$f"; done
[ -d "$R/csv" ] && mv "$R/csv" "$G/csv"; mv "$N/csv" "$R/csv"; rmdir "$N"
echo "RESERVE GRØNN: skrevet i $R (forrige i $G)"; cat "$R/SHA.txt"
