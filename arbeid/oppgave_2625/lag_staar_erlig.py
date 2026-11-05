"""#2625: STÅR-utgaver av ERLIG_EVALUERING.md og JURY_SPORSMAL.md med ærlighetssetningene fra #2618.

STÅR-veien (#2593) ruller disse to filene tilbake fra grønn frossen-zip, som mangler forbeholdet.
Dette tar zipens utgave, limer inn STAAR-tekstene med lim_inn.py-logikken (#2618, dommerens klokkeslett #2617)
og skriver resultatet til arbeid/hack/c1/reserve_staar/. leveranse/ røres ikke.
Bruk: uv run python -I arbeid/oppgave_2625/lag_staar_erlig.py [ZIP]   (standard /tmp/jurypakke_c1_2587.zip)
"""
import pathlib, shutil, sys, tempfile, zipfile

HER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HER.parent / "oppgave_2618"))
import lim_inn  # noqa: E402

RES = HER.parents[0] / "hack" / "c1" / "reserve_staar"
zp = sys.argv[1] if len(sys.argv) > 1 else "/tmp/jurypakke_c1_2587.zip"
with zipfile.ZipFile(zp) as z, tempfile.TemporaryDirectory() as t:
    for navn in ("ERLIG_EVALUERING.md", "JURY_SPORSMAL.md"):
        (pathlib.Path(t) / navn).write_bytes(z.read(f"c1_stemmeagent/arbeid/hack/c1/leveranse/{navn}"))
    lim_inn.EE, lim_inn.JS = pathlib.Path(t) / "ERLIG_EVALUERING.md", pathlib.Path(t) / "JURY_SPORSMAL.md"
    sys.argv = ["lim_inn", "--variant", "STAAR", "--malt", "16:49–16:51"]  # klokkeslett som i BYTT-utgaven (dommer #2617)
    lim_inn.main()
    ee = lim_inn.EE.read_text()
    gml = "| 0,506 | +0,035 | +0,017 | oppfyller på papiret, avventer dom |"
    assert ee.count(gml) == 1, "tabellraden for repo4 fantes ikke nøyaktig én gang"
    ee = ee.replace(gml, "| 0,506 | +0,035 | +0,017 | besto regelen, ikke levert (pakken ikke grønn i tide) |")
    gml = "Blir en kandidat godkjent før innlevering, står det i `README.md` og her; står det ikke, er den frosne modellen levert uendret."
    assert ee.count(gml) == 1
    ee = ee.replace(gml, "Den frosne modellen er levert uendret.")
    gml = "## 7. Forsøkt etter ordre om bedre treff: tre testår, ikke valgt (05.11 kl. 16–18)"
    assert ee.count(gml) == 1
    ee = ee.replace(gml, "## 7. Forsøkt etter ordre om bedre treff: tre testår, repo4 besto regelen men ble ikke levert (05.11 kl. 16–18)")
    ee = ee.rstrip("\n") + "\n"
    (RES / "ERLIG_EVALUERING.md").write_text(ee)
    shutil.copy(lim_inn.JS, RES / "JURY_SPORSMAL.md")
print("skrevet:", RES / "ERLIG_EVALUERING.md", RES / "JURY_SPORSMAL.md")
# #2640: jury-rettelsene (STÅR-punktene) legges på til slutt, så de overlever ombygging
sys.path.insert(0, str(HER.parent / "oppgave_2640"))
import rett_staar  # noqa: E402
rett_staar.rett(RES)
