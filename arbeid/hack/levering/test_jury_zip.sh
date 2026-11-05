#!/bin/sh
# Case 1: test jury-zipen som et jurymedlem (#2346, flyttet hit i #2349 for sluttsjekk.sh).
# Bruk: sh arbeid/hack/levering/test_jury_zip.sh [ZIP] [TESTMAPPE]   (standard /tmp/jurypakke_c1.zip, /tmp/jurytest_zip)
# Tom mappe, env -i med tom HOME (tom uv-buffer), og sandbox-exec som nekter lesing/skriving i landsbymappen.
# Følger README ordrett: unzip, cd c1_stemmeagent, sh KJOR.sh; deretter sjekk_treffsikkerhet.sh.
# Siste linje: ZIPTEST GRØNN, eller ZIPTEST RØD: <grunn> (utgang 1).
set -eu
LAND="$(cd "$(dirname "$0")/../../.." && pwd)"
ZIP="${1:-/tmp/jurypakke_c1.zip}"; T="${2:-/tmp/jurytest_zip}"
[ -f "$ZIP" ] || { echo "ZIPTEST RØD: finner ikke $ZIP"; exit 1; }
rm -rf "$T"; mkdir -p "$T/home"; cp "$ZIP" "$T/jurypakke_c1.zip"; cd "$T"
printf '(version 1)\n(allow default)\n(deny file-read* file-write* (subpath "%s"))\n' "$LAND" > "$T.sb"
sandbox-exec -f "$T.sb" env -i HOME="$T/home" SJEKK="$T/sjekk" PATH="$(dirname "$(command -v uv)"):/usr/bin:/bin" sh -c \
  'unzip -q jurypakke_c1.zip && cd c1_stemmeagent && sh KJOR.sh && sh arbeid/hack/levering/sjekk_treffsikkerhet.sh "$SJEKK"' \
  > "$T.logg" 2>&1 || { tail -5 "$T.logg"; echo "ZIPTEST RØD: kjøringen feilet (logg $T.logg)"; exit 1; }
grep -E "FRYSVAKT|^HOVEDTALL|TALLVAKT|STEMMER|LIK" "$T.logg" || true
for ord in "FRYSVAKT GRØNN" "TALLVAKT GRØNN" "STEMMER"; do
  grep -q "$ord" "$T.logg" || { echo "ZIPTEST RØD: mangler «$ord» i $T.logg"; exit 1; }
done
grep -q "landsby" "$T.logg" && { echo "ZIPTEST RØD: loggen nevner landsby"; exit 1; }
echo "ZIPTEST GRØNN: $(grep -E '^HOVEDTALL' "$T.logg" | tail -1)"
