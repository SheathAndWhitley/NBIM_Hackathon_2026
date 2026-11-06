#!/bin/sh
# Stemmeagenten (Case 1) med ett kall:  sh KJOR.sh   (fra repo-roten; krever macOS eller Linux og uv)
# 1) låst Python-miljø .venv_kjor (uv.lock)   2) inndata for test 2026 uten fasitfelt   3) agenten -> ut/agent.csv
# 4) måling: F1 på stemmer MOT styret, sammen med «følg styret» og «gjenta forrige beslutning».
# All intern utskrift havner i ut/logg.txt.
set -eu
ROT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROT"
command -v uv >/dev/null 2>&1 || { echo "Mangler uv (https://docs.astral.sh/uv/): curl -LsSf https://astral.sh/uv/install.sh | sh"; exit 7; }
[ -f data/real_votes.csv ] || { echo "Mangler data/real_votes.csv (arrangørens fil med NBIMs stemmer)."; exit 9; }
mkdir -p ut/.home
LOGG="$ROT/ut/logg.txt"
: > "$LOGG"
V="$ROT/.venv_kjor"
E() { env -i HOME="$ROT/ut/.home" PATH="$V/bin:/usr/bin:/bin" LANG=C.UTF-8 "$@"; }
steg() { printf '  %s ... ' "$1"; }
feil() { echo "FEIL"; echo; tail -20 "$LOGG"; echo; echo "Hele loggen: ut/logg.txt"; exit 1; }

echo "Stemmeagenten (Case 1): finner sakene der NBIM stemmer mot styret"
echo
steg "Python-miljø med låste pakker"
UV_PROJECT_ENVIRONMENT="$V" uv sync --frozen --no-install-project -q >> "$LOGG" 2>&1 || feil
echo "ok"
steg "Inndata test 2026 (uten fasit)"
E "$V/bin/python" -I maaling/lag_inndata.py >> "$LOGG" 2>&1 || feil
echo "ok"
steg "Agenten trener og svarer"
T0=$(date +%s)
E "$V/bin/python" agent/kjor_agent.py --ut "$ROT/ut" >> "$LOGG" 2>&1 || feil
echo "ok ($(( $(date +%s) - T0 )) s)"
echo
E "$V/bin/python" -I maaling/oppsummer.py 2>> "$LOGG" || feil
echo
echo "  Svar per sak: ut/agent.csv     Hele loggen: ut/logg.txt"
