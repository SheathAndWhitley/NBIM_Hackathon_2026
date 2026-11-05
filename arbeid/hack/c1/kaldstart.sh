#!/usr/bin/env bash
# Case 1: hel leveranse fra kald start, ett kall (arkitekt #2060). For dommeren kl. 13 (#1952) og 19.30 (#1972).
#   bash arbeid/hack/c1/kaldstart.sh            (fra hvor som helst)
# Steg: 1 kopier leveransen (bare det agenten trenger) til en tom tmp-mappe
#       2 installer smed2-prosjektet med uv fra uv.lock (--frozen, egen .venv i tmp)
#       3 kjør agenten (kjor_agent.py) på holdout 2026 (data_off/real_test_input.csv, laget fra arrangørens real_votes) i kopien
#   Bare arrangørens data (ordre #242): state/opplastet/20261105_114241_real_votes.csv og data_off/ avledet av den.
#       4 mål F1 på MOT mot styret med måler v3 (landsbyens kopi) på real_votes test 2026 (#2099; før: N-PX-fasit)
#       5 sammenlign med beste målte forsøk på tavla; avvik > 0,005 = RØD (exit 3)
# Valg (miljø): REF=0.476190 (standard, #2090) overstyrer referansen. BEHOLD=1 lar tmp-mappa stå. TOL=0.005.
#   AGENT_ARGS="--til-menneske 15" sendes videre til kjor_agent.py.
#   Etter steg 4: TALLSJEKK-linje (#2273), bare varsel.
# Siste linje: GRØNN|RØD F1_MOT <tall> REF <tall> AVVIK <tall>.
set -euo pipefail
LAND="$(cd "$(dirname "$0")/../../.." && pwd)"     # landsbymappen
ARB="$LAND/arbeid"
TOL="${TOL:-0.005}"
T0=$(date +%s)
TMP="$(mktemp -d /tmp/c1_kald.XXXXXX)"
if [ -z "${BEHOLD:-}" ]; then trap 'rm -rf "$TMP"' EXIT; fi
K="$TMP/arbeid"                                     # kopien har samme relative tre som arbeid/
steg() { echo "[$(date '+%T') +$(( $(date +%s) - T0 ))s] $*"; }

steg "0 tmp=$TMP git=$(git -C "$LAND" rev-parse --short HEAD) (endrede filer i leveransen vises under)"
git -C "$LAND" status --short -- arbeid/hack/levering/kjor_agent.py arbeid/hack/levering/c1_real.py arbeid/oppgave_2044 arbeid/hack/c1/data_off | grep -v '^??' | head -5 || true

# frysvakt (#2142): etter frys kl. 16 stopper kald start hvis modell/prediksjoner/agent er endret
python3 -I "$ARB/verktoy/c1_frys.py" sjekk || { echo "RØD FRYSVAKT: kald start stoppet (se over)"; exit 4; }

steg "1 kopierer leveransen (uten .venv, __pycache__, ut/)"
EX=(--exclude .venv --exclude __pycache__ --exclude 'ut/' --exclude '*.log')
mkdir -p "$K/hack/levering" "$K/hack/c1" "$K/kandidater"
cp "$ARB/hack/levering/kjor_agent.py" "$K/hack/levering/"
# bare de låste avhengighetene fra smed2-prosjektet; modellen er oppgave_2044/train.py (#242: ingen gamle datamapper med)
mkdir -p "$K/kandidater/smed2_c1_mot"; cp "$ARB/kandidater/smed2_c1_mot/pyproject.toml" "$ARB/kandidater/smed2_c1_mot/uv.lock" "$K/kandidater/smed2_c1_mot/"
cp "$ARB"/hack/c1/*.py "$K/hack/c1/"
cp "$ARB"/hack/c1/demo_*.sh "$K/hack/c1/"             # demoen kan kjøres fra kopiens rot (#2235)
# real_votes-agenten (#2053, frossen #2044) trenger disse; listen er den samme som i smed3s fremmed.sh (#2094)
for f in hack/levering/c1_real.py hack/levering/injeksjon_hoflig.py hack/levering/retningslinje_oppslag.py hack/c1/retningslinjer/punkter.jsonl oppgave_2044/train.py oppgave_2047/vern.py oppgave_2046/case1_mot.py hack/c1/data_off/real_test_input.csv; do
  mkdir -p "$K/$(dirname "$f")"; cp "$ARB/$f" "$K/$f"; done
mkdir -p "$TMP/state/opplastet"; cp "$LAND/state/opplastet/20261105_114241_real_votes.csv" "$TMP/state/opplastet/"
steg "1 ferdig: $(du -sh "$TMP" | cut -f1), $(find "$K" -type f | wc -l | tr -d ' ') filer"

steg "2 uv sync --frozen fra uv.lock (ny .venv i kopien)"
P="$K/kandidater/smed2_c1_mot"
( cd "$P" && env -u VIRTUAL_ENV uv sync --frozen --quiet )
"$P/.venv/bin/python" -c "import lightgbm, sklearn, pandas; print('  lightgbm', lightgbm.__version__, 'sklearn', sklearn.__version__, 'pandas', pandas.__version__)"

steg "3 kjører agenten på holdout 2026 (real_votes, data_off/real_test_input.csv) -> $TMP/ut"
( cd "$TMP" && "$P/.venv/bin/python" "$K/hack/levering/kjor_agent.py" --ut "$TMP/ut" ${AGENT_ARGS:-} ) > "$TMP/agent.log" 2>&1 \
  || { tail -20 "$TMP/agent.log"; echo "RØD agenten feilet fra kald start"; exit 2; }
grep -E "^inn:|^låst|^treff" "$TMP/agent.log" | sed 's/^/  /'

steg "4 måler v3 (arbeid/hack/c1/maaler_offisiell_v3.py, landsbyens kopi) test 2026 --data real --score mot (#2099)"
for FIL in _pred_uten_ruting.csv pred_maaler.csv; do
  M="$(python3 -I "$ARB/hack/c1/maaler_offisiell_v3.py" "$TMP/ut/$FIL" test --data real --score mot)" \
    || { echo "$M" | tail -5; echo "RØD måleren avviste $FIL"; exit 2; }
  echo "  -- $FIL"; echo "$M" | grep -E "MOT|rutet|PRAUC|SCORE" | sed 's/^/    /'
  [ "$FIL" = _pred_uten_ruting.csv ] && F1=$(echo "$M" | sed -n 's/^SCORE *//p' | tail -1)   # hovedtallet: modellen alene
done
echo "  måler sha256[:10] $(shasum -a 256 "$ARB/hack/c1/maaler_offisiell_v3.py" | cut -c1-10)"

# tallsjekk (#2273): tall i pakkas .md uten kilde i tall-tabellen/målerutskriftene. Bare varsel, endrer ikke utgangskoden.
TS="$(python3 -I "$ARB/verktoy/c1_tallsjekk.py" --bare-ikke 2>&1)" || TS="tallsjekken feilet: $(echo "$TS" | tail -1)"
echo "  TALLSJEKK (varsel): $(echo "$TS" | tail -1)"
echo "$TS" | sed '$d' | head -20 | sed 's/^/    ikke funnet: /'

steg "5 referanse: beste målte forsøk på tavla for agenten"
REF="${REF:-0.476190}"   # dommer #2090: frossen #2044 miks h2, F1 MOT test 2026 (c1_tall_likt.md)
if [ -n "$REF" ]; then KILDE="REF fra miljøet eller #2090"
else
  read -r REF KILDE < <(cd "$LAND" && uv run --quiet python - <<'PY'
import sqlite3
c = sqlite3.connect("state/tavle.db")
r = c.execute("""SELECT score, id, av, ts FROM forsok WHERE score IS NOT NULL AND score = score
                 AND (vinkel LIKE '%kjor_agent%' OR sti LIKE '%kjor_agent%' OR sti LIKE '%pred_maaler%')
                 ORDER BY score DESC, id DESC LIMIT 1""").fetchone()
print(f"{r[0]} forsøk#{r[1]}_{r[2]}_{r[3]}" if r else "nan ingen")
PY
)
fi
echo "  REF $REF ($KILDE)"
SEK=$(( $(date +%s) - T0 ))
python3 -I - "$F1" "$REF" "$TOL" "$SEK" <<'PY'
import sys
f1, ref, tol, sek = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
av = f1 - ref
ok = abs(av) <= tol
rød, grønn, null = "\033[1;31m", "\033[1;32m", "\033[0m"
print(f"{grønn if ok else rød}{'GRØNN' if ok else 'RØD'} F1_MOT {f1:.6f} REF {ref:.6f} AVVIK {av:+.6f} (grense {tol}) tid {sek}s{null}")
sys.exit(0 if ok else 3)
PY
