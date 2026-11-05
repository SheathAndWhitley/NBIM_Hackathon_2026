"""Vanguards amerikanske stemmeretningslinjer (feb. 2025) delt i punkter, med enkelt BM25-søk.

Hvert punkt = ett avsnitt med pilar og overskrift, så sitatet kan vise hvor i dokumentet det står.
Ren Python, ingen avhengigheter.
"""

import math
import re
from collections import Counter
from pathlib import Path

KILDE = "Vanguard-advised funds: Proxy voting policy for U.S. portfolio companies (feb. 2025)"
KILDE_URL = "https://corporate.vanguard.com (Investment Stewardship, policy documents); lokal kopi data/vg_us_2025.txt"
STI = Path(__file__).parent / "data" / "vg_us_2025.txt"
STOPP = set("the a an of to and or in for on by with is are be as that this its at from which their "
            "will may any other such not it fund funds company companies shareholder shareholders".split())


def ord_(tekst):
    return [w for w in re.findall(r"[a-z]+", tekst.lower()) if len(w) > 2 and w not in STOPP]


def les_punkter(sti=STI):
    pilar, overskrift, punkter = "Introduction", "", []
    for linje in sti.read_text(encoding="utf-8").splitlines():
        linje = re.sub(r"^[•—\\\s]+", "", linje.strip().rstrip("\\").strip())
        if not linje or linje.isdigit():
            continue
        if linje.startswith("Pillar "):
            pilar, overskrift = linje, ""
            continue
        if len(linje) < 70 and not linje.endswith("."):
            overskrift = re.sub(r"\d+$", "", linje)
            continue
        # Avsnitt som starter med «Tittel.» er egne underpunkter i policyen
        m = re.match(r"^([A-Z][^.]{3,80})\.\s", linje)
        tittel = m.group(1) if m else overskrift
        punkter.append({"nr": len(punkter) + 1, "pilar": pilar, "overskrift": overskrift,
                        "tittel": tittel, "tekst": linje})
    return punkter


class Retningslinjer:
    def __init__(self, k1=1.4, b=0.75):
        self.punkter = les_punkter()
        self.dok = [Counter(ord_(p["tittel"] + " " + p["tittel"] + " " + p["tekst"])) for p in self.punkter]
        self.len = [sum(d.values()) for d in self.dok]
        self.snitt = sum(self.len) / len(self.len)
        df = Counter(w for d in self.dok for w in d)
        n = len(self.dok)
        self.idf = {w: math.log(1 + (n - f + 0.5) / (f + 0.5)) for w, f in df.items()}
        self.k1, self.b = k1, b

    def sok(self, tekst, k=3):
        q = ord_(tekst)
        poeng = []
        for i, d in enumerate(self.dok):
            s = 0.0
            for w in q:
                if w in d:
                    tf = d[w]
                    s += self.idf[w] * tf * (self.k1 + 1) / (tf + self.k1 * (1 - self.b + self.b * self.len[i] / self.snitt))
            poeng.append((s, i))
        poeng.sort(reverse=True)
        return [dict(self.punkter[i], poeng=round(s, 2)) for s, i in poeng[:k] if s > 0]

    def sitat(self, p):
        return f"{KILDE}, {p['pilar']} > {p['overskrift'] or p['tittel']} (avsnitt {p['nr']})"
