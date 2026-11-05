"""#2640: jury-rettelsene (#2637, punktene merket STÅR/begge) inn i STÅR-reserven for
ERLIG_EVALUERING.md, JURY_SPORSMAL.md og MUNTLIG.md. README/kravrespons rettes i oppgave_2598/lag_staar.py.
Idempotent: er den nye teksten alt inne, hoppes regelen over. Finnes verken gammel eller ny nøyaktig én gang, stopper skriptet.
Bruk: python3 -I arbeid/oppgave_2640/rett_staar.py [--rot STI] [--sjekk]
lag_staar_erlig.py kaller rett() til slutt, så rettelsene overlever ombygging.
"""
import pathlib, sys

GRONN = "ikke levert, fordi pakken med repo4 ikke var reprodusert fra kald start (samme tall, uten feil) før vi måtte låse tekstene kl. 19."
REGLER = {
    "ERLIG_EVALUERING.md": [
        # 2a
        ("- Ingen variant er valgt på test [A]. Målet var F1 0,5.",
         "- Ingen modellvariant, C eller grense er valgt på test [A]; det eneste som er valgt på test, er rutingsbåndet [0,15; 0,85) for hva som går til menneske (§ 6 og `JURY_SPORSMAL.md` sp. 16). Målet var F1 0,5."),
        # 4g
        ("Benk A (samme måler på alle, ferdige svarfiler per år):",
         "Sammenligning (samme måler på alle kandidater, én ferdig svarfil per kandidat og testår):"),
        # 4d
        ("besto regelen, ikke levert (pakken ikke grønn i tide)",
         "besto regelen, ikke levert (ikke reprodusert fra kald start før fristen)"),
        # 4c
        ("Den ble likevel ikke levert, fordi pakken med repo4 ikke var grønn før tekststoppen.", "Den ble likevel " + GRONN),
        # #2654: internspråk (grønn, benk, tallvakt) og repo4 forklart første gang
        ("tre testår, repo4 besto regelen men ble ikke levert", "tre testår, repo4 (frossen + fire historikktrekk) besto regelen men ble ikke levert"),
        ("byttet til repo4 ble ikke grønt før tekststoppen", "pakken med repo4 ble ikke reprodusert fra kald start før tekststoppen"),
        ("repo4 i benk A er", "repo4 i sammenligning A er"),
        ("Benk B (", "Sammenligning B ("),
        ("(benk B sin trening)", "(sammenligning B sin trening)"),
        ("(benk A, ", "(sammenligning A, "),
        ("seks punkter, alle grønne", "seks punkter, alle besto"),
    ],
    "JURY_SPORSMAL.md": [
        # 4c
        ("Den er likevel ikke levert, fordi pakken med repo4 ikke var grønn før tekststoppen.", "Den er likevel " + GRONN),
        # #2654
        ("målere, tallvakt)", "målere, tallsjekk)"),
        ("## 20. «Repo4 besto regelen", "## 20. «Repo4 (frossen + fire historikktrekk) besto regelen"),
        ("seks punkter, alle grønne", "seks punkter, alle besto"),
    ],
    "MUNTLIG.md": [
        # 4f
        ("En kontrollagent som ikke målte selv, avgjør byttet.",
         "En kontrollagent som ikke målte kandidatene, avgjør byttet. Hovedtallet har den målt på nytt fra kald start."),
        # 4e
        ("Repo4 besto regelen, men pakken med repo4 ble ikke grønn i tide, så den frosne agenten står.",
         "Repo4 besto regelen, men vi rakk ikke å kjøre hele pakken med repo4 feilfritt fra kald start før fristen, så den frosne agenten står."),
        # 3b
        ("KI er 0,36 til 0,59. Repo4 ga 0,512.",
         "KI er 0,36 til 0,59. Repo4 ga 0,512, men det tallet er fra 2026, året repo4 ble funnet på, så det er ikke et friskt testår for den; se neste punkt."),
    ],
}

def rett(mappe, skriv=True):
    mappe = pathlib.Path(mappe)
    for navn, regler in REGLER.items():
        sti = mappe / navn
        s = s0 = sti.read_text()
        for gammel, ny in regler:
            if s.count(ny) == 1 and gammel not in s:
                continue
            if s.count(gammel) != 1:
                sys.exit(f"{navn}: fant {s.count(gammel)} treff (skal være 1) for: {gammel[:70]}")
            s = s.replace(gammel, ny)
        print(f"{navn}: {'uendret' if s == s0 else 'rettet'}")
        if skriv and s != s0:
            sti.write_text(s)

if __name__ == "__main__":
    a = sys.argv[1:]
    rot = pathlib.Path(a[a.index("--rot") + 1]) if "--rot" in a else pathlib.Path(__file__).resolve().parents[2]
    rett(rot / "arbeid/hack/c1/reserve_staar", skriv="--sjekk" not in a)
