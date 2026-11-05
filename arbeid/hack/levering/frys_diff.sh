#!/bin/sh
# Frys-dommen (#2445): sammenlign en jury-zip eller en mappe mot fasiten og list NY / ENDRET / BORTE.
# Bruk (fra landsbymappen):
#   sh arbeid/hack/levering/frys_diff.sh /tmp/jurypakke_c1.zip            [FASIT]
#   sh arbeid/hack/levering/frys_diff.sh /tmp/jurystage_c1/c1_stemmeagent [FASIT]   (utpakket zip eller stage)
#   sh arbeid/hack/levering/frys_diff.sh --kilde                          [FASIT]   (kilden nå, via frys_fasit.py)
# FASIT er arbeid/hack/levering/frys_fasit_1600.sha256 om ikke annet er gitt. Utgang 0 = 0 avvik, 1 = avvik.
set -eu
HER="$(cd "$(dirname "$0")" && pwd)"; KILDE="$(cd "$HER/../../.." && pwd)"
MAAL="${1:?zip, mappe eller --kilde}"; FASIT="${2:-$HER/frys_fasit_1600.sha256}"
[ -f "$FASIT" ] || { echo "fant ikke fasit $FASIT"; exit 2; }
TMP="$(mktemp -d /tmp/frys_diff.XXXXXX)"; trap 'rm -rf "$TMP"' EXIT
if [ "$MAAL" = "--kilde" ]; then
  (cd "$KILDE" && python3 -I arbeid/hack/levering/frys_fasit.py 2>/dev/null) | sort -k2 > "$TMP/na"
else
  if [ -f "$MAAL" ]; then ROT="$TMP/ut"; mkdir -p "$ROT"; unzip -q "$MAAL" -d "$ROT"
  elif [ -d "$MAAL" ]; then ROT="$MAAL"
  else echo "finnes ikke: $MAAL"; exit 2; fi
  # stier i fasiten starter med c1_stemmeagent/; en mappe som selv er pakkeroten får prefikset lagt på
  if [ -d "$ROT/c1_stemmeagent" ]; then PRE=""; else PRE="c1_stemmeagent/"; fi
  (cd "$ROT" && find . -type f -not -name ".DS_Store" | sed 's#^\./##' | sort | while IFS= read -r f; do
      printf '%s  %s%s\n' "$(shasum -a 256 "$f" | cut -d' ' -f1)" "$PRE" "$f"; done) | sort -k2 > "$TMP/na"
fi
sort -k2 "$FASIT" > "$TMP/fasit"
awk '{print $2}' "$TMP/fasit" > "$TMP/f_stier"; awk '{print $2}' "$TMP/na" > "$TMP/n_stier"
comm -13 "$TMP/f_stier" "$TMP/n_stier" | sed 's/^/NY      /' > "$TMP/avvik"
comm -23 "$TMP/f_stier" "$TMP/n_stier" | sed 's/^/BORTE   /' >> "$TMP/avvik"
join -1 2 -2 2 "$TMP/fasit" "$TMP/na" | awk '$2 != $3 {print "ENDRET  " $1}' >> "$TMP/avvik"
N=$(wc -l < "$TMP/avvik" | tr -d ' ')
echo "fasit: $FASIT ($(wc -l < "$TMP/fasit" | tr -d ' ') filer)   sammenlignet: $MAAL ($(wc -l < "$TMP/na" | tr -d ' ') filer)"
if [ "$N" = 0 ]; then echo "FRYS LIK: 0 avvik"; exit 0; fi
sort "$TMP/avvik"; echo "FRYS AVVIK: $N"; exit 1
