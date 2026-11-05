#!/bin/sh
# Case 1 (#2593): rull BYTT (repo4) tilbake til siste grønne frossen-zip. Virker også for usporede filer (git checkout gjør ikke det).
# Bruk: sh arbeid/hack/c1/bytte/tilbake_fra_zip.sh <ROT> <GRØNN_ZIP> <frys.json fra før byttet>
#   ROT = landsbymappen (eller en kald kopi), zip = /tmp/jurypakke_c1_2587.zip, json = /tmp/bytte2572_c1_frys.json
# Gjør: 1) alle filer i zipen tilbake på sine stier (README.md->JURY_README.md, KJOR.sh->jury_kjor.sh; FROSNE_SHA256,
# rot-pyproject/uv.lock og de to sed-rettede målerne hoppes over, målerne er frosne og sjekkes av frysvakta)
# 2) sletter modell_repo4.py og stemmeagent/  3) fjerner bytte-linjene i c1_frys.py og fremmed.sh
# 4) legger tilbake state/c1_frys.json  5) ny fasit fra kilden  6) frysvakt + frys_diff mot zipen.
set -eu
ROT="${1:?rot}"; ZIP="${2:?zip}"; JSON="${3:?frys.json}"; L=arbeid/hack/levering
U="$(mktemp -d /tmp/tilbake_zip.XXXXXX)"; unzip -q "$ZIP" -d "$U"; P="$U/c1_stemmeagent"
cd "$ROT"
(cd "$P" && find . -type f -not -name .DS_Store | sed 's#^\./##') | while IFS= read -r f; do
  case "$f" in
    FROSNE_SHA256.txt|pyproject.toml|uv.lock|arbeid/hack/c1/maaler_offisiell_v*.py) continue ;;
    README.md) m=$L/JURY_README.md ;;
    KJOR.sh) m=$L/jury_kjor.sh ;;
    *) m="$f" ;;
  esac
  mkdir -p "$(dirname "$m")"; cmp -s "$P/$f" "$m" || { cp -p "$P/$f" "$m"; echo "tilbake  $m"; }
done
for f in $L/modell_repo4.py $L/stemmeagent; do [ -e "$f" ] && { rm -rf "$f"; echo "slettet  $f"; }; done
grep -v "# #2572 bytte til repo4" arbeid/verktoy/c1_frys.py > "$U/c1_frys.py" && cp "$U/c1_frys.py" arbeid/verktoy/c1_frys.py
grep -v "arbeid/hack/levering/modell_repo4.py arbeid/hack/levering/stemmeagent" $L/fremmed.sh > "$U/fremmed.sh" && cp "$U/fremmed.sh" $L/fremmed.sh
cp "$JSON" state/c1_frys.json; echo "tilbake  state/c1_frys.json ($(python3 -I -c "import json;d=json.load(open('state/c1_frys.json'));print(d['tid'],len(d['filer']),'filer')"))"
python3 -I $L/frys_fasit.py > $L/frys_fasit_1600.sha256 2>/dev/null; echo "ny fasit: $(wc -l < $L/frys_fasit_1600.sha256 | tr -d ' ') filer"
python3 -I arbeid/verktoy/c1_frys.py sjekk --krev | tail -1
echo "frys_diff zip mot ny fasit (ventet: bare EN_SIDE/KRAVRESPONS BORTE, de er interne og aldri i zipen):"
sh $L/frys_diff.sh "$ZIP" $L/frys_fasit_1600.sha256 || true
rm -rf "$U"
