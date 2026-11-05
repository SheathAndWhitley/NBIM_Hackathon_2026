#!/bin/bash
# Case 1: sluttsjekken kl. 19.30 med én kommando (arkitekt #2330, dommeren kjører den i #1972).
#   bash arbeid/hack/levering/sluttsjekk.sh [MAAL]      (MAAL = kald kopi, standard /tmp/c1_sluttsjekk)
# Kaller bare eksisterende skript, i rekkefølge, og stopper ved første røde:
#   1 frysvakt   python3 -I arbeid/verktoy/c1_frys.py sjekk --krev   (ikke frosset = rødt)
#   2 kaldstart  sh arbeid/hack/levering/fremmed.sh MAAL            (egen frysvakt og tallvakt; skriver HOVEDTALL)
#   3 tallvakt   c1_tallvakt.py i kald kopi MAAL mot kopiens egen kjøring (#2397; rød = SLUTTSJEKK RØD: TALLVAKT RØD)
#   3b tallsjekk python3 -I arbeid/verktoy/c1_tallsjekk.py --bare-ikke --feil
#   4 hovedtall  HOVEDTALL fra steg 2 = kv hack_levert (tavle.py levert: kjører 'kmd' på 'sti')
#   5 jury-zip   sh arbeid/hack/levering/pakk_jury.sh ZIP           (ZIP = $C1_JURYZIP, ellers ny mktemp-mappe per kjøring, #2443)
#   6 ziptest    sh arbeid/hack/levering/test_jury_zip.sh ZIP      (tom mappe, sandkasse; HOVEDTALL i zipen = steg 2)
#   7 avtrykk    python3 -I arbeid/hack/c1/tekstavtrykk.py sjekk    (#2384; bare info, aldri rødt; oppsummering i siste linje)
#   8 lagring    bash arbeid/hack/levering/lagre_gronn.sh ZIP       (#2522; bare når 1-6 er grønne: fast kopi i state/levering/c1_gronn/, SISTE_GRONNE.zip)
# Siste linje: SLUTTSJEKK GRØNN (lister stegene som faktisk kjørte, #2443)  eller  SLUTTSJEKK RØD: <grunn>.  Utgang 0 = grønn, 4 = rød.
# Fulle logger i en mktemp-mappe som skrives ut.
set -u
LAND="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$LAND"
MAAL="${1:-/tmp/c1_sluttsjekk}"
LOGG="$(mktemp -d /tmp/c1_sluttsjekk_logg.XXXX)"
T0=$(date +%s)
echo "sluttsjekk $(date '+%F %T'), git $(git rev-parse --short HEAD), logger i $LOGG"

rod() { echo "SLUTTSJEKK RØD: $* (logger: $LOGG, $(( $(date +%s) - T0 )) s)"; exit 4; }
kjor() {  # kjor <nr navn> <logg> <kommando...>
  local navn="$1" fil="$LOGG/$2"; shift 2
  echo ">>> $navn"
  "$@" > "$fil" 2>&1; local k=$?
  tail -4 "$fil" | sed 's/^/    /'
  return $k
}
OK=""  # stegene som faktisk kjørte grønt, i rekkefølge (#2443)
ok() { OK="${OK:+$OK, }$*"; }

kjor "1 frysvakt" 1_frys.txt python3 -I arbeid/verktoy/c1_frys.py sjekk --krev \
  || rod "frysvakt (utgang $?): $(tail -1 "$LOGG/1_frys.txt")"
ok frysvakt
kjor "2 kaldstart (fremmed.sh $MAAL)" 2_fremmed.txt sh arbeid/hack/levering/fremmed.sh "$MAAL"; K2=$?
# fremmed.sh gir utgang 1 når bare tallvakta er rød; da tar steg 3 over med egen melding (#2397)
[ $K2 -eq 0 ] || grep -q '^TALLVAKT RØD' "$LOGG/2_fremmed.txt" \
  || rod "kaldstart fremmed.sh (utgang $K2): $(tail -1 "$LOGG/2_fremmed.txt")"
ok kaldstart
# 3) tallvakta som eget steg (#2397): tallene i pakkas .md (kopiert til MAAL) mot kopiens egen kjøring
[ -x "$MAAL/.venv/bin/python" ] && [ -f "$MAAL/ut/pred_maaler.csv" ] \
  || rod "TALLVAKT RØD: kald kopi $MAAL mangler .venv eller ut/pred_maaler.csv, tallvakta kan ikke kjøres"
kjor "3 tallvakt (kald kopi $MAAL)" 3_tallvakt.txt env -i HOME="$MAAL/home" PATH="$MAAL/.venv/bin:/usr/bin:/bin" LANG=C.UTF-8 \
  "$MAAL/.venv/bin/python" -I "$MAAL/arbeid/verktoy/c1_tallvakt.py" --rot "$MAAL" \
  --svar "$MAAL/ut/pred_maaler.csv" --kjoring "$MAAL/ut/KJORING.txt"; K3=$?
if [ $K3 -ne 0 ]; then
  grep -E '^AVVIK' "$LOGG/3_tallvakt.txt" | head -5 | sed "s#$MAAL/##; s/^/    /"
  rod "TALLVAKT RØD (utgang $K3): $(grep -c '^AVVIK' "$LOGG/3_tallvakt.txt") tall i pakka avviker fra måleren, se AVVIK-linjene over ($LOGG/3_tallvakt.txt). Rett teksten i landsbymappa og kjør sluttsjekken på nytt"
fi
grep -q '^TALLVAKT RØD' "$LOGG/2_fremmed.txt" && rod "TALLVAKT RØD i fremmed.sh, men grønn i steg 3: uforklart, se $LOGG/2_fremmed.txt"
ok tallvakt
kjor "3b tallsjekk" 3_tallsjekk.txt python3 -I arbeid/verktoy/c1_tallsjekk.py --bare-ikke --feil \
  || rod "tallsjekk (utgang $?): $(grep -c . "$LOGG/3_tallsjekk.txt") linjer, tall i pakka uten kilde"
ok tallsjekk

echo ">>> 4 hovedtall mot kv hack_levert"
KALD="$(grep -E '^HOVEDTALL' "$LOGG/2_fremmed.txt" | tail -1 | awk '{print $NF}')"
LEV="$(uv run python tavle.py levert 2>/dev/null | tail -1)"
STI="$(printf '%s' "$LEV" | python3 -I -c 'import json,sys; print(json.load(sys.stdin)["sti"])' 2>/dev/null)"
KMD="$(printf '%s' "$LEV" | python3 -I -c 'import json,sys; print(json.load(sys.stdin)["kmd"])' 2>/dev/null)"
[ -n "$STI" ] && [ -n "$KMD" ] || rod "kv hack_levert mangler eller er uleselig: $LEV"
eval "${KMD//\{sti\}/\"$STI\"}" > "$LOGG/4_levert.txt" 2>&1
TAVLE="$(grep -E '^SCORE' "$LOGG/4_levert.txt" | tail -1 | awk '{print $2}')"
echo "    kald kopi: ${KALD:-mangler}   kv hack_levert: ${TAVLE:-mangler}"
[ -n "$KALD" ] || rod "fant ingen HOVEDTALL-linje i fremmed.sh"
[ -n "$TAVLE" ] || rod "måleren i kv hack_levert ga ingen SCORE ($LOGG/4_levert.txt)"
[ "$KALD" = "$TAVLE" ] || rod "HOVEDTALL $KALD fra kald kopi != $TAVLE i kv hack_levert"
ok hovedtall

# egen zip per kjøring (#2443): skriver aldri over en felles /tmp-fil som andre kan bruke samtidig
ZIP="${C1_JURYZIP:-$(mktemp -d /tmp/c1_jurypakke.XXXX)/jurypakke_c1.zip}"
echo "    jury-zip denne kjøringen: $ZIP"
C1_JURYBYGG="$LOGG/bygg" C1_JURYSTAGE="$LOGG/stage" \
kjor "5 jury-zip (pakk_jury.sh -> $ZIP)" 5_pakk.txt sh arbeid/hack/levering/pakk_jury.sh "$ZIP" \
  || rod "pakk_jury.sh (utgang $?): $(tail -1 "$LOGG/5_pakk.txt"); ingen zip"
ok jury-zip
kjor "6 ziptest (tom mappe, sandkasse uten landsbymappen)" 6_ziptest.txt sh arbeid/hack/levering/test_jury_zip.sh "$ZIP" "$LOGG/ziptest" \
  || rod "ziptest (utgang $?): $(tail -1 "$LOGG/6_ziptest.txt")"
ZIPTALL="$(grep -E '^ZIPTEST GRØNN' "$LOGG/6_ziptest.txt" | awk '{print $NF}')"
[ "$ZIPTALL" = "$KALD" ] || rod "HOVEDTALL i zipen ${ZIPTALL:-mangler} != $KALD fra kald kopi"
ok ziptest

# 7) tekstavtrykk av leveranse/ fra 16.03 (#2384, #2392): bare info, aldri rødt (tekster kan endres med vilje, #1975)
#    utgang 0 = uendret/ikke tatt, 3 = endret (info), 2 = skriptfeil (vises som ADVARSEL, fortsatt ikke rødt) (#2404)
kjor "7 tekstavtrykk (info, ikke rødt)" 7_tekstavtrykk.txt python3 -I arbeid/hack/c1/tekstavtrykk.py sjekk; K7=$?
AVTRYKK="$(grep -E '^TEKSTAVTRYKK' "$LOGG/7_tekstavtrykk.txt" | tail -1)"
case $K7 in 0|3) ;; *) AVTRYKK="ADVARSEL tekstavtrykk.py feilet (utgang $K7), se $LOGG/7_tekstavtrykk.txt"; echo "    $AVTRYKK";; esac

# 8) fast kopi av den grønne zipen (#2522): alle steg over er grønne her (rød har allerede gått ut med 4).
#    Bare info: feil i lagringen gjør ikke sjekken rød, men står i GRØNN-linja.
kjor "8 lagre grønn zip (state/levering/c1_gronn)" 8_lagre.txt bash arbeid/hack/levering/lagre_gronn.sh "$ZIP"; K8=$?
if [ $K8 -eq 0 ]; then LAGRET="lagret $(tail -1 "$LOGG/8_lagre.txt" | awk '{print $2}')"
else LAGRET="ADVARSEL lagre_gronn.sh feilet (utgang $K8), se $LOGG/8_lagre.txt"; fi

echo "SLUTTSJEKK GRØNN: $OK ok; HOVEDTALL F1 MOT $KALD = kv hack_levert = zipen ($ZIP, $(du -h "$ZIP" | cut -f1)); $LAGRET; ${AVTRYKK:-TEKSTAVTRYKK: mangler} ($(( $(date +%s) - T0 )) s)"
exit 0
