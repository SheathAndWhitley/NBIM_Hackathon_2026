#!/bin/sh
# Case 1: kjør hele stemmeagenten fra den utpakkede jury-zipen (#2346). Legges som KJOR.sh i roten av zipen
# av pakk_jury.sh. Leser bare filer i denne mappa (pluss uv sin pakkebuffer).
# Bruk (stå i mappa der README.md og KJOR.sh ligger):  sh KJOR.sh
# 1) eget uv-miljø .venv med låste versjoner (uv.lock, uv sync --frozen)
# 2) agenten på test 2026 (kjor_agent.py) under env -i -> ut/
# 3) HOVEDTALL: F1 på MOT mot styret, måler v3 --score mot
# 4) tallvakta: tallene i pakkas .md mot denne kjøringen (utgang 1 ved avvik)
# 0) sha256 av de frosne filene mot FROSNE_SHA256.txt (laget av pakk_jury.sh mot frysen kl. 16)
set -eu
ROT="$(cd "$(dirname "$0")" && pwd)"
[ -f "$ROT/arbeid/oppgave_2044/train.py" ] || { echo "FEIL STED: KJOR.sh må ligge i roten av den utpakkede zipen."; exit 6; }
command -v uv >/dev/null 2>&1 || { echo "Mangler uv (https://docs.astral.sh/uv/): curl -LsSf https://astral.sh/uv/install.sh | sh"; exit 7; }
cd "$ROT"
shasum -a 256 -c -q FROSNE_SHA256.txt || { echo "FRYSVAKT RØD: frosne filer avviker fra FROSNE_SHA256.txt"; exit 4; }
echo "FRYSVAKT GRØNN: $(grep -c . FROSNE_SHA256.txt) frosne filer har samme sha256 som ved pakking"
mkdir -p home
T0=$(date +%s)
UV_PROJECT_ENVIRONMENT="$ROT/.venv" uv sync --frozen --no-install-project -q
T1=$(date +%s)
E() { env -i HOME="$ROT/home" PATH="$ROT/.venv/bin:/usr/bin:/bin" LANG=C.UTF-8 "$@"; }  # funksjon, ikke streng: tåler mellomrom/æøå i stien (#2426)
E "$ROT/.venv/bin/python" "$ROT/arbeid/hack/levering/kjor_agent.py" --ut "$ROT/ut" "$@"
T2=$(date +%s)
echo "tid: uv sync $((T1 - T0)) s, kjøring $((T2 - T1)) s"
printf "HOVEDTALL F1 MOT mot styret (v3 --score mot): "
E "$ROT/.venv/bin/python" -I arbeid/hack/c1/maaler_offisiell_v3.py "$ROT/ut/pred_maaler.csv" test --data real --score mot \
  | grep -E "^SCORE" | cut -d" " -f2
if E "$ROT/.venv/bin/python" -I arbeid/verktoy/c1_tallvakt.py --rot "$ROT" --svar "$ROT/ut/pred_maaler.csv" --kjoring "$ROT/ut/KJORING.txt"; then
  echo "TALLVAKT GRØNN: tallene i pakka stemmer med kald kjøring"
else
  echo "TALLVAKT RØD: tall i pakka avviker fra denne kjøringen (fil:linje over). Pakka er IKKE verifisert."; exit 1
fi
