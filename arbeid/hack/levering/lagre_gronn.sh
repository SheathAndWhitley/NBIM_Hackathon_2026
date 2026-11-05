#!/bin/bash
# Case 1 (#2522): lagrer en grønn jury-zip i en fast mappe, så det alltid finnes en «siste grønne zip».
#   bash arbeid/hack/levering/lagre_gronn.sh <zip>
# Kopierer til state/levering/c1_gronn/jurypakke_c1_<HHMM>_<HEAD>.zip, legger «sha256  fil  tid» til SHA256.txt
# og peker SISTE_GRONNE.zip på kopien. Sletter aldri noe: finnes navnet fra før, får kopien et løpenummer.
# Kalles av sluttsjekk.sh bare når alle steg er grønne. Siste linje: LAGRET <sti> <sha256>. Utgang 0 = lagret.
set -u
ZIP="${1:?bruk: lagre_gronn.sh <zip>}"
[ -f "$ZIP" ] || { echo "LAGRE_GRONN FEIL: finner ikke $ZIP"; exit 2; }
LAND="$(cd "$(dirname "$0")/../../.." && pwd)"
DIR="$LAND/state/levering/c1_gronn"
mkdir -p "$DIR" || exit 2
NAVN="jurypakke_c1_$(date +%H%M)_$(git -C "$LAND" rev-parse --short HEAD)"
MAL="$DIR/$NAVN.zip"; n=2
while [ -e "$MAL" ]; do MAL="$DIR/${NAVN}_$n.zip"; n=$((n+1)); done
cp -p "$ZIP" "$MAL" || { echo "LAGRE_GRONN FEIL: cp feilet"; exit 2; }
SHA="$(shasum -a 256 "$MAL" | awk '{print $1}')"
[ "$SHA" = "$(shasum -a 256 "$ZIP" | awk '{print $1}')" ] || { echo "LAGRE_GRONN FEIL: SHA ulik etter kopi"; exit 2; }
echo "$SHA  $(basename "$MAL")  $(date '+%F %T')" >> "$DIR/SHA256.txt"
ln -sfn "$(basename "$MAL")" "$DIR/SISTE_GRONNE.zip"
echo "LAGRET $MAL $SHA"
