"""Akseptkrav #2362: AppTest på lim-inn-fanen med de tre demo.sh-sakene (#2335 tre_saker.csv).
Sjekker: samme 19 felt som #2335/#2344, nøyaktig én ny fil i logg/ per klikk (også ved feil), ingen landsbysti
(jurypakke.finn_lekk), og at fila har tid, sha256, agentkall og svar.
Kjør: arbeid/hack/levering/demo/.venv/bin/python arbeid/oppgave_2362/test_fane_logg.py"""
import hashlib, json, sys
from pathlib import Path
from streamlit.testing.v1 import AppTest

ROT = Path(__file__).resolve().parents[2]
DEMO = ROT / "arbeid/hack/levering/demo"
LOGG = DEMO / "logg"
sys.path.insert(0, str(ROT / "arbeid/verktoy"))
from jurypakke import finn_lekk  # noqa: E402

REF = [json.loads(l) for l in open(ROT / "arbeid/oppgave_2335/fane_svar.jsonl", encoding="utf-8")]
tekst = (ROT / "arbeid/oppgave_2335/tre_saker.csv").read_text(encoding="utf-8")
feil_alle = []


def klikk(tekst):
    foer = set(LOGG.glob("lim_*.json"))
    at = AppTest.from_file(str(DEMO / "app.py"), default_timeout=300).run()
    at.text_area[0].set_value(tekst)
    [b for b in at.button if b.label == "Anbefal"][0].click()
    at.run()
    nye = sorted(set(LOGG.glob("lim_*.json")) - foer)
    return at, nye


# 1: de tre sakene
at, nye = klikk(tekst)
rader = at.session_state["ekte"] if "ekte" in at.session_state else None
print("feil i appen:", [e.value for e in at.error])
print("nye loggfiler:", [f.name for f in nye])
if len(nye) != 1:
    feil_alle.append(f"forventet 1 ny loggfil, fikk {len(nye)}")
if rader is None or len(rader) != 3:
    feil_alle.append(f"forventet 3 rader, fikk {None if rader is None else len(rader)}")
else:
    for r, ref in zip(rader, REF):
        if list(r) != list(ref):
            feil_alle.append(f"{r.get('id')}: feltliste ulik ({len(r)} vs {len(ref)})")
        avvik = [k for k in ref if r.get(k) != ref[k]]
        print(f"{r['id']}: {len(r)} felt, {r['anbefaling']} P(MOT) {r['p_mot']}, avvik mot #2335: {avvik or 'ingen'}")
        if avvik:
            feil_alle.append(f"{r['id']}: avvik i {avvik}")
if nye:
    post = json.loads(nye[0].read_text(encoding="utf-8"))
    mangler = [k for k in ("tid", "kjoring", "tekst_sha256", "agentkall", "svar", "feil", "modell") if k not in post]
    if mangler:
        feil_alle.append(f"loggfila mangler {mangler}")
    if post.get("tekst_sha256") != hashlib.sha256(tekst.encode()).hexdigest():
        feil_alle.append("sha256 i loggen stemmer ikke med innlimt tekst")
    if post.get("svar") != rader:
        feil_alle.append("svarene i loggen er ikke de som vises i fanen")
    k = post.get("agentkall") or {}
    print("agentkall:", " ".join(k.get("kall", [])), "| kode", k.get("returkode"), "| varighet", k.get("varighet_s"), "s")
    print("stdout linjer i loggen:", len(k.get("stdout", "").splitlines()), "| sha256", post.get("tekst_sha256", "")[:16])

# 2: feilklikk (manglende felt) skal også gi én fil, med feil satt
at2, nye2 = klikk("proposal_text\nSomething")
print("feilklikk: feil i appen:", [e.value[:80] for e in at2.error], "| nye loggfiler:", [f.name for f in nye2])
if len(nye2) != 1:
    feil_alle.append(f"feilklikk: forventet 1 ny loggfil, fikk {len(nye2)}")
elif not json.loads(nye2[0].read_text(encoding="utf-8")).get("feil"):
    feil_alle.append("feilklikk: loggfila har ikke feil satt")
if "ekte" in at2.session_state and at2.session_state["ekte"]:
    feil_alle.append("feilklikk: session_state['ekte'] skulle vært tom")

# 3: ingen landsbysti i logg/
lekk = finn_lekk(LOGG, [str(ROT)])
print("landsbysti i logg/:", lekk or "ingen")
if lekk:
    feil_alle.append(f"landsbysti i loggen: {lekk}")

print("RESULTAT:", "OK" if not feil_alle else "FEIL " + "; ".join(feil_alle))
sys.exit(1 if feil_alle else 0)
