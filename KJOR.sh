#!/bin/sh
# Case 1: kjør hele stemmeagenten fra den utpakkede jury-zipen (#2346). Legges som KJOR.sh i roten av zipen
# av pakk_jury.sh. Leser bare filer i denne mappa (pluss uv sin pakkebuffer).
# Bruk (stå i mappa der README.md og KJOR.sh ligger):  sh KJOR.sh
# 1) eget uv-miljø .venv_kjor med låste versjoner (uv.lock, uv sync --frozen); rører ikke et annet .venv (#2897)
# 1b) data (#2897): ligger arrangørens real_votes.csv i ny_data/, kopieres den til state/opplastet/, og testinndata
#     (data_off/real_test_input.csv 2026, real_val_input.csv 2025) lages av arbeid/hack/c1/lag_inndata.py
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
V="$ROT/.venv_kjor"  # #2897: eget miljø, så KJOR.sh aldri overskriver et .venv brukeren har fra før
T0=$(date +%s)
UV_PROJECT_ENVIRONMENT="$V" uv sync --frozen --no-install-project -q
T1=$(date +%s)
E() { env -i HOME="$ROT/home" PATH="$V/bin:/usr/bin:/bin" LANG=C.UTF-8 "$@"; }  # funksjon, ikke streng: tåler mellomrom/æøå i stien (#2426)
# #2897: datasteget. Arrangørens real_votes.csv i ny_data/ -> fast sti; testinndata lages av den (byte-likt med frysen).
REAL="state/opplastet/20261105_114241_real_votes.csv"
NY=""
if [ -d "$ROT/ny_data" ]; then
  if [ -f "$ROT/ny_data/real_votes.csv" ]; then NY="$ROT/ny_data/real_votes.csv"
  else
    N=$(ls "$ROT"/ny_data/*.csv 2>/dev/null | wc -l | tr -d ' ')
    case "$N" in
      0) ;;
      1) NY=$(ls "$ROT"/ny_data/*.csv) ;;
      *) echo "FEIL DATA: $N csv-filer i ny_data/; legg bare arrangørens real_votes.csv der"; exit 9 ;;
    esac
  fi
fi
if [ -n "$NY" ]; then
  mkdir -p "$ROT/state/opplastet"; cp "$NY" "$ROT/$REAL"
  echo "DATA: kopierte ny_data/$(basename "$NY") til $REAL"
fi
[ -f "$ROT/$REAL" ] || { echo "MANGLER DATA: legg arrangørens real_votes.csv i ny_data/ (mkdir -p ny_data && cp <casepakka>/real_votes.csv ny_data/), og kjør sh KJOR.sh igjen. Se DATA.md."; exit 9; }
if [ -n "$NY" ] || [ ! -f "$ROT/arbeid/hack/c1/data_off/real_test_input.csv" ]; then
  E "$V/bin/python" -I "$ROT/arbeid/hack/c1/lag_inndata.py" "$ROT/$REAL"
fi
# #2896: modellvalg. Fila arbeid/hack/levering/MODELL sier frossen (standard, kjor_agent.py) eller v2av (natt-kandidaten
# #2887: v2 SVD-tekst i LGBM k=48 + av-regel, kjor_agent_v2av.py). Byttes bare etter dommerens BYTT (state/c1_BYTT).
MODELL=$(tr -d ' \n' < "$ROT/arbeid/hack/levering/MODELL" 2>/dev/null || echo frossen)
case "$MODELL" in
  frossen|"") AGENT=kjor_agent.py; MODELL=frossen ;;
  v2av) AGENT=kjor_agent_v2av.py ;;
  *) echo "FEIL MODELL: arbeid/hack/levering/MODELL sier '$MODELL' (lov: frossen, v2av)"; exit 8 ;;
esac
echo "MODELL: $MODELL ($AGENT)"
E "$V/bin/python" "$ROT/arbeid/hack/levering/$AGENT" --ut "$ROT/ut" "$@"
T2=$(date +%s)
echo "tid: uv sync $((T1 - T0)) s, kjøring $((T2 - T1)) s"
printf "HOVEDTALL F1 MOT mot styret (v3 --score mot): "
E "$V/bin/python" -I arbeid/hack/c1/maaler_offisiell_v3.py "$ROT/ut/pred_maaler.csv" test --data real --score mot \
  | grep -E "^SCORE" | cut -d" " -f2
if E "$V/bin/python" -I arbeid/verktoy/c1_tallvakt.py --rot "$ROT" --svar "$ROT/ut/pred_maaler.csv" --kjoring "$ROT/ut/KJORING.txt" --toleranse 0.01; then
  echo "TALLVAKT GRØNN: tallene i pakka stemmer med kald kjøring"
else
  echo "TALLVAKT RØD: tall i pakka avviker fra denne kjøringen (fil:linje over). Pakka er IKKE verifisert."; exit 1
fi
