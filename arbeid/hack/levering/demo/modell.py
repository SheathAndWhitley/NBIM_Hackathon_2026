"""Ett grensesnitt for demoen: predict(tekst, kontekst=None) -> dict.

Svaret har alltid feltene: anbefaling (FOR/MOT/AVSTÅ), konfidens (0-1), til_menneske (bool),
kilde_punkt, sitat, begrunnelse, modell, injeksjon (bool).

Ekte modell: sett DEMO_MODELL=<modul> (f.eks. "smed2_modell") der modulen har en
predict(tekst, kontekst) med samme svar. Modulen må ligge på PYTHONPATH (eller i denne mappa).
Uten DEMO_MODELL brukes stubben under: «følg styret» + regel for aksjonærforslag,
med konfidens fra treningsfrekvensene (train.csv, møter før holdout) og sitat fra BM25-søk.
"""

import importlib
import os
import re

from retningslinjer import Retningslinjer

TERSKEL_MENNESKE = 0.6  # samme som måleren (#1947)
SVAKT_TREFF = 7.0  # BM25-poeng under dette regnes som at policyen ikke nevner temaet

# Fra arbeid/hack/c1/data/train.csv (7251 rader, Vanguard, før tidssplitten):
#   ISSUER, ledelsen FOR  -> FOR 7018 av 7028           = 0,999
#   ISSUER, ledelsen AGAINST -> MOT 15, AVSTÅ 7, FOR 4  -> MOT 15/26 = 0,58
#   SECURITY HOLDER (ledelsen FOR i N-PX-feltet) -> MOT 183 av 185 = 0,99
FREKVENS = {
    ("ISSUER", "FOR"): ("FOR", 0.99),
    ("ISSUER", "AGAINST"): ("MOT", 0.58),
    ("SECURITY HOLDER", "FOR"): ("MOT", 0.99),
    ("SECURITY HOLDER", "AGAINST"): ("FOR", 0.60),
}
# Uten ledelsen-feltet (trolig lekkasje, se state/rapporter/arkitekt_c1_grunnlinje_sh.md), train.csv:
#   ISSUER -> FOR 7022 av 7056 = 0,995;  SECURITY HOLDER -> MOT 183 av 194 = 0,94
UTEN_LEDELSEN = {"ISSUER": ("FOR", 0.99), "SECURITY HOLDER": ("MOT", 0.94)}
AKSJONAER = re.compile(r"\b(shareholder|stockholder|security holder)s?\b.{0,40}\bproposal|\bproposal\b.{0,40}"
                       r"\b(shareholder|stockholder)s?\b|^\s*(shp|sh)\b", re.I)
INJEKSJON = re.compile(r"ignor(e|er)\b.{0,40}(guideline|retningslin|instruction|instruks|policy)|"
                       r"(anbefal|recommend|vote)\s+(alltid\s+)?FOR\b.{0,20}(uansett|regardless)|"
                       r"\bsystem prompt\b|\bdisregard\b", re.I)

_rl = None


def _retningslinjer():
    global _rl
    if _rl is None:
        _rl = Retningslinjer()
    return _rl


def stubb(tekst, kontekst=None):
    kontekst = kontekst or {}
    kilde = kontekst.get("kilde") or ("SECURITY HOLDER" if AKSJONAER.search(tekst) else "ISSUER")
    if kontekst.get("ledelsen"):
        ledelsen = kontekst["ledelsen"]
        anbefaling, konf = FREKVENS.get((kilde, ledelsen), ("FOR", 0.5))
    else:
        # Uten styrets anbefaling: styret anbefaler FOR egne forslag og MOT aksjonærforslag
        ledelsen = "AGAINST (antatt)" if kilde == "SECURITY HOLDER" else "FOR (antatt)"
        anbefaling, konf = UTEN_LEDELSEN[kilde]
    hist = konf
    if not kontekst.get("kilde"):
        konf = min(konf, 0.85)  # kilde gjettet fra teksten: litt mindre sikker
    injeksjon = bool(INJEKSJON.search(tekst))
    # Forslagsteksten er data, aldri instruksjon: injeksjon endrer ikke stemmen, men sender saken til menneske
    if injeksjon:
        konf = min(konf, 0.4)
    # Setninger med instruksjoner tas ut før søket, så de ikke styrer hvilket punkt som siteres
    rent = " ".join(st for st in re.split(r"(?<=[.!?])\s+", tekst) if not INJEKSJON.search(st))
    treff = _retningslinjer().sok(rent or tekst, k=1)
    if kilde == "SECURITY HOLDER" and (not treff or treff[0]["poeng"] < SVAKT_TREFF):
        # Aksjonærforslag som policyen ikke nevner direkte: det generelle punktet om E/S-forslag
        treff = [p for p in _retningslinjer().punkter if p["overskrift"] == "Environmental/social proposals"][-1:]
    if treff:
        p = treff[0]
        kilde_punkt, sitat = _retningslinjer().sitat(p), p["tekst"]
    else:
        kilde_punkt, sitat = "Introduction: case-by-case (ingen punkt traff)", ""
        konf = min(konf, 0.5)
    hvem = "aksjonærforslag" if kilde == "SECURITY HOLDER" else "styrets forslag"
    begr = (f"{hvem}, styret anbefaler {ledelsen}. Historisk stemte fondet {anbefaling} i "
            f"{round(hist * 100)} % av slike saker (train.csv).")
    if injeksjon:
        begr += " Teksten inneholder en instruksjon til agenten; den er ignorert og saken sendt til menneske."
    return {"anbefaling": anbefaling, "konfidens": round(konf, 3), "til_menneske": konf < TERSKEL_MENNESKE,
            "kilde_punkt": kilde_punkt, "sitat": sitat, "begrunnelse": begr, "modell": "stubb-v1 (følg styret+SH-regel)",
            "injeksjon": injeksjon, "kilde": kilde, "ledelsen": ledelsen}


def _last():
    navn = os.environ.get("DEMO_MODELL")
    if not navn:
        return stubb, "stubb-v1"
    try:
        return importlib.import_module(navn).predict, navn
    except Exception as e:  # demoen skal aldri stå: fall tilbake og si fra
        print(f"[demo] klarte ikke å laste {navn}: {e}; bruker stubb")
        return stubb, f"stubb-v1 ({navn} feilet)"


_predict, MODELLNAVN = _last()


def predict(tekst, kontekst=None):
    svar = dict(_predict(tekst, kontekst))
    svar.setdefault("modell", MODELLNAVN)
    svar["til_menneske"] = bool(svar.get("til_menneske", svar["konfidens"] < TERSKEL_MENNESKE))
    return svar
