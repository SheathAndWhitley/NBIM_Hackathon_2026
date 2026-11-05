#!/bin/sh
# Case 1: bygg én zip juryen kan pakke ut og kjøre alene (#2346).
# Bruk (fra landsbymappen):  sh arbeid/hack/levering/pakk_jury.sh [/tmp/jurypakke_c1.zip]
# 1) fremmed.sh i en byggemappe: frysvakt, kald kjøring, TALLVAKT GRØNN (ellers stopp). Den gir fillista.
# 2) kopierer de samme filene fra kilden (ikke fremmed.sh sine sed-rettede målere), pluss de frosne
#    filene fra c1_frys.py, c1/leveranse/ og README/KJOR.sh i roten
# 3) målerne får datastien relativ til egen fil i stedet for <repo> (regnestykket uendret)
# 4) FROSNE_SHA256.txt for alle frosne filer som er kopiert uendret; KJOR.sh sjekker dem først
# 5) zip, og grep: ingen ~ i pakka. Frosne filer endres aldri, de kopieres. Kan kjøres flere ganger.
set -eu
KILDE="$(cd "$(dirname "$0")/../../.." && pwd)"
ZIP="${1:-/tmp/jurypakke_c1.zip}"
BYGG="${C1_JURYBYGG:-/tmp/jurybygg_c1}"; NAVN=c1_stemmeagent; STAGE="${C1_JURYSTAGE:-/tmp/jurystage_c1}"; P="$STAGE/$NAVN"  # overstyres av sluttsjekk.sh
cd "$KILDE"
rm -f "$ZIP"  # en feilet bygging skal aldri etterlate en gammel zip
echo "1/5 kald kjøring med fremmed.sh i $BYGG"
sh arbeid/hack/levering/fremmed.sh "$BYGG" > "$BYGG.logg" 2>&1 || { echo "fremmed.sh feilet, se $BYGG.logg"; tail -5 "$BYGG.logg"; exit 1; }
grep -q "TALLVAKT GRØNN" "$BYGG.logg" || { echo "ikke TALLVAKT GRØNN i $BYGG.logg"; exit 1; }
grep "HOVEDTALL" "$BYGG.logg"
echo "2/5 kopierer til $P"
rm -rf "$STAGE"; mkdir -p "$P"
kopier() { for f in "$@"; do mkdir -p "$P/$(dirname "$f")"; cp -R "$f" "$P/$f"; done; }
FILER=$(cd "$BYGG" && find . -type f -not -path "./.venv/*" -not -path "./home/*" -not -path "./ut/*" -not -path "*/__pycache__/*" -not -name "*.pyc" -not -name ".DS_Store" | sed 's#^\./##' | sort \
  | grep -v -x -e arbeid/hack/levering/KRAVRESPONS.md -e arbeid/hack/levering/EN_SIDE.md)  # interne utkast, ikke for juryen (#2587)
kopier $FILER
# Rota skal ha kandidatens låste miljø (samme som fremmed.sh målte med), ikke landsbyens (#2475, funn #2445)
KAND=arbeid/kandidater/smed2_c1_mot
cp "$KAND/pyproject.toml" "$KAND/uv.lock" "$P/"
cmp -s "$KAND/uv.lock" "$BYGG/uv.lock" || { echo "uv.lock i $BYGG er ikke kandidatens"; exit 1; }
FROSNE=$(python3 -I -c "import runpy; print(' '.join(runpy.run_path('arbeid/verktoy/c1_frys.py', run_name='x')['FILER']))")
kopier $FROSNE
kopier $(find arbeid/hack/c1/leveranse -type f -not -path "*/__pycache__/*" -not -name "*.pyc" -not -name ".DS_Store" -not -path "*/ut/*" -not -path "*/spor_npx/utkast_1100/*")  # utkast_1100: gammelt utkast med TODO, ut (#2457)
kopier arbeid/hack/c1/vis_manussaker.py arbeid/hack/c1/DEMO_MANUS.md  # demo.sh i zipen (#2442), etter sh KJOR.sh
kopier arbeid/hack/c1/tall_tabell.md  # README/JURY peker på c1/tall_tabell.md (dom #2436); tallvakta leser den ikke
# Filene jurytekstene peker på for å etterprøve tall (#2448, c1_manglende_filer.md del 1). DEMO_MANUS.md står over.
# menneske_tabell.py er med som kode: standardstiene er hardkodet, kjør den med AGENT.csv/FASIT som argument.
kopier arbeid/hack/levering/kjor_agent_real_pred_maaler.csv arbeid/hack/levering/kjor_agent_real_test2026.txt \
       arbeid/hack/levering/treffsikkerhet.py arbeid/hack/levering/treffsikkerhet_ki.py \
       arbeid/hack/c1/sjekk_lekkasje.py arbeid/hack/c1/terskel_val_test.py arbeid/hack/c1/menneske_tabell.py \
       arbeid/hack/c1/data_off/real_val_input.csv
# NESTE_VERSJON.md bygger tall på disse (#2449 bøtte b, #2457)
kopier state/rapporter/c1_feil_per_gruppe.md state/rapporter/arkitekt_c1_neste_versjon.md \
       state/rapporter/speider_2399_recall_budsjett.md \
       arbeid/oppgave_2274/feil_val2025.md
# Stier jurytekstene peker på som manglet i zipen (#2509, state/rapporter/c1_kilder_pekere.md)
kopier arbeid/hack/c1/JURY_METODE.md arbeid/hack/c1/SVAKHETER.md arbeid/hack/c1/DEMO_MANUS_5min_tilfeldige.md \
       arbeid/hack/levering/c1_forslagsstiller.py arbeid/hack/levering/c1_forslagsstiller.txt \
       state/rapporter/c1_injeksjon_frossen.md state/rapporter/c1_motstandstall_dom.md state/rapporter/c1_demo_etter_rydding.md
cp arbeid/hack/levering/jury_kjor.sh "$P/KJOR.sh"
cp arbeid/hack/levering/JURY_README.md "$P/README.md"
echo "3/5 relative datastier i målerne"
for m in arbeid/hack/c1/maaler_offisiell_v2.py arbeid/hack/c1/maaler_offisiell_v3.py; do
  sed -i '' 's#"\([^"]*\)"#os.path.join(HER, "../../../\1")#g' "$P/$m"
done
echo "4/5 FROSNE_SHA256.txt"
(cd "$P" && for f in $FROSNE; do case "$f" in *maaler_offisiell_v*) ;; *) shasum -a 256 "$f";; esac; done) > "$P/FROSNE_SHA256.txt"
FRYSFIL="${C1_FRYS:-state/c1_frys.json}"  # C1_FRYS: bare for test, som i c1_frys.py
if [ -f "$FRYSFIL" ]; then  # etter kl. 16: pakkas sha256 skal være frysens
  python3 -I - "$P/FROSNE_SHA256.txt" "$FRYSFIL" <<'PY'
import json, sys
frys = json.load(open(sys.argv[2]))["filer"]
for l in open(sys.argv[1]):
    s, f = l.split(None, 1); f = f.strip()
    if frys.get(f) != s: sys.exit(f"AVVIK mot frysen: {f}")
print("  sha256 i pakka = frysfila")
PY
else echo "  (ikke frosset ennå: sha256 er dagens filer)"; fi
echo "5/5 zip og stisjekk"
if grep -rIl "~" "$P" > "$STAGE.stier"; then
  echo "  merk: $(wc -l < "$STAGE.stier" | tr -d ' ') tekstfiler nevner ~ (se $STAGE.stier); kjørestien leser dem ikke"
fi
rm -f "$ZIP"; (cd "$STAGE" && zip -qr "$ZIP" "$NAVN")
echo "ferdig: $ZIP ($(du -h "$ZIP" | cut -f1), $(cd "$P" && find . -type f | wc -l | tr -d ' ') filer)"
