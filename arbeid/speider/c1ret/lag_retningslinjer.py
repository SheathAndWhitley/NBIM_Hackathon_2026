"""Lag siterbare retningslinjer for Case 1 (#1948).

Leser rå nedlastinger i ../c1ret_raa/ og skriver nummererte markdown-filer og en felles
punkter.jsonl til arbeid/hack/c1/retningslinjer/. Hvert punkt har en id som agenten kan sitere,
f.eks. "VG26 1.2.3" (Vanguard 2026, pilar 1, avsnitt 2, ledd 3) eller "NBIM 3.1.4".
"""
import html, json, re, sys
from pathlib import Path

RAA = Path(__file__).resolve().parent.parent / "c1ret_raa"
UT = Path(sys.argv[1] if len(sys.argv) > 1 else "../../hack/c1/retningslinjer").resolve()
UT.mkdir(parents=True, exist_ok=True)
SMED3 = Path(__file__).resolve().parents[2] / "hack/varianter/smed3_utf_sitat/rl/vg_us_2025.txt"

ROM = {"I": 1, "II": 2, "III": 3, "IV": 4}


def html_tekst(s):
    s = re.sub(r"(?is)<(script|style|nav|header|footer|noscript)[^>]*>.*?</\1>", "", s)
    s = re.sub(r"(?i)<(h[1-6]|p|li|br|div|tr)[^>]*>", "\n", s)
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    return [l.strip() for l in s.splitlines() if l.strip()]


def vanguard(txt, kode, start_paa):
    """Vanguard-PDF: pilarer, avsnittsoverskrifter, ledd. Ledd splittes på kort linje med punktum."""
    L = [l.rstrip().replace("\\", "") for l in txt.split("\n")]
    i = max(k for k, l in enumerate(L) if l.strip() == start_paa)  # siste "Introduction" = selve teksten
    L = L[i:]
    # overskrifter: korte linjer uten sluttegn, ikke punktliste, ikke spørsmål-fortsettelse
    def er_overskrift(l, neste):
        s = l.strip()
        if not s or len(s) > 75 or s[0] in "•—-–(" or not s[0].isupper():
            return False
        if re.search(r"[.,;:?)”]\s*$", s) or re.fullmatch(r"[\d ]+", s):
            return False
        if s.split()[-1].lower() in {"the", "of", "and", "or", "a", "to", "in", "for", "with", "by"}:
            return False
        if neste is not None and s[-1].isdigit() and re.match(r"^\d{1,2} [A-Z]", neste.strip()):
            return True  # overskrift med fotnotetall
        return neste is not None and (neste.strip()[:1].isupper() or neste.strip()[:1] in "•")
    punkter, p, a, n, buf = [], 0, 0, 0, []
    fotnote = False
    pilnavn, avnavn = "Introduction", ""

    def flush():
        nonlocal n, buf
        t = re.sub(r"\s+", " ", " ".join(buf)).strip()
        buf = []
        if len(t) < 3:
            return
        n += 1
        punkter.append({"id": f"{kode} {p}.{a}.{n}", "pilar": pilnavn, "avsnitt": avnavn, "tekst": t})

    for k, l in enumerate(L):
        s = l.strip()
        if not s or re.fullmatch(r"\d+", s) or s.startswith("©") or re.fullmatch(r"\d{6,} \d+", s):
            continue
        if s in ("This page intentionally left blank.",):
            continue
        m = re.match(r"Pillar ([IV]+): (.*)", s)
        if m:
            flush(); p, a, n = ROM[m.group(1)], 0, 0; pilnavn, avnavn = s, ""; continue
        neste = next((x for x in L[k + 1:] if x.strip() and not re.fullmatch(r"\d+", x.strip())), None)
        if k > 0 and er_overskrift(s, neste) and not buf:
            a += 1; n = 0; avnavn = re.sub(r"\d$", "", s); continue
        if er_overskrift(s, neste) and buf and re.search(r"[.:)]\s*$", buf[-1]):
            flush(); a += 1; n = 0; avnavn = re.sub(r"\d$", "", s); continue
        if s.startswith("•") and buf:
            flush()
        if re.match(r"^\d{1,2} [A-Z] ?[a-z]", s):  # fotnote "1 C ertain"
            flush(); fotnote = True
            s = "Fotnote " + re.sub(r"^(\d+) ([A-Z]) ", r"\1: \2", s)
        buf.append(s)
        if fotnote:  # fotnotelinjer er lengre enn brødtekst (mindre skrift)
            if s.endswith(".") and (neste is None or len(neste.rstrip()) <= 102):
                flush(); fotnote = False
            continue
        if re.search(r"[.?:]\)?\s*$", s) and len(s) < 85:
            flush()
    flush()
    return punkter


def nbim_web(linjer):
    """NBIM global voting guidelines (web): prinsipp P, delpunkt S, ledd k -> NBIM P.S.k."""
    i = linjer.index("Voting principles")
    slutt = linjer.index("Related information")
    P = S = n = 0; prinsipp = "Innledning"; del_ = "Voting principles"; ut = []; sett = set()
    del_l = linjer[i + 1:slutt]
    nummer = [k for k, l in enumerate(del_l) if re.match(r"^\d+\. ", l)]
    prinsipp_k = {k for j, k in enumerate(nummer) if j + 1 < len(nummer) and del_l[nummer[j + 1]].startswith("1. ")}
    for k, l in enumerate(del_l):
        m = re.match(r"^(\d+)\. (.*)", l)
        if m:
            tall = int(m.group(1))
            if k in prinsipp_k:  # nytt prinsipp: neste nummererte linje er "1."
                P, S, n, prinsipp, del_ = tall, 0, 0, l, ""
            else:
                S, n, del_ = tall, 0, l
            continue
        if l in sett or l in ("Effective boards", "Shareholder protection", "Voting decisions") and P == 0 and False:
            continue
        if len(l) < 40 and not l.endswith("."):  # gruppeoverskrift
            if P == 0:
                del_ = l
            continue
        sett.add(l)
        n += 1
        ut.append({"id": f"NBIM {P}.{S}.{n}", "pilar": prinsipp, "avsnitt": del_, "tekst": l})
    return ut


def nbim_posisjon(slug, linjer, nr):
    try:
        i = next(k for k, l in enumerate(linjer) if l.startswith("Position paper") or l.startswith("Published"))
    except StopIteration:
        i = 0
    tittel = next((l for l in linjer if l.endswith("| Norges Bank Investment Management")), slug)
    tittel = tittel.split("|")[0].strip()
    slutt = next((k for k, l in enumerate(linjer) if l in ("Related information", "Download", "Read more")), len(linjer))
    ut, n = [], 0
    for l in linjer[i:slutt]:
        if (len(l) < 50 and not l.endswith(".")) or "| Norges Bank" in l:
            continue
        n += 1
        ut.append({"id": f"NBIM-PP{nr} {n}", "pilar": "Position paper: " + tittel, "avsnitt": slug, "tekst": l})
    return ut


KILDER = {}


def skriv(navn, tittel, url, punkter, merknad=""):
    KILDER[navn] = (tittel, url, len(punkter), merknad)
    with open(UT / f"{navn}.md", "w", encoding="utf-8") as f:
        f.write(f"# {tittel}\n\nKilde: {url}\nHentet 2026-11-05 av speider (#1948). {merknad}\n"
                f"Siter som: `{punkter[0]['id'].split()[0]} <nummer>`, f.eks. `{punkter[min(5, len(punkter)-1)]['id']}`.\n")
        sist = None
        for q in punkter:
            hode = (q["pilar"], q["avsnitt"])
            if hode != sist:
                f.write(f"\n## {q['pilar']}" + (f" / {q['avsnitt']}" if q["avsnitt"] else "") + "\n\n")
                sist = hode
            f.write(f"- **{q['id']}** {q['tekst']}\n")
    return punkter


alle = []
VPM = "https://corporate.vanguard.com/content/dam/corp/about-our-funds/pdf/vpm/vpm-proxy-voting-policy-us.pdf"
VCM = "https://corporate.vanguard.com/content/dam/corp/about-our-funds/pdf/vcm/vcm-proxy-voting-policy-us.pdf"
alle += skriv("vanguard_us_2026", "Vanguard: Proxy voting policy for U.S. portfolio companies (effektiv januar 2026)",
              VPM, vanguard((RAA / "vanguard_us.txt").read_text(), "VG26", "Introduction"),
              f"Gjelder VPM-fond (stil-/sektorindeks). VCM-versjonen ({VCM}) er ordrett lik bortsett fra hvilke enheter som har vedtatt den. "
              "Brukes for møter fra 12.01.2026.")
if SMED3.exists():
    alle += skriv("vanguard_us_2025", "Vanguard-advised funds: Proxy voting policy for U.S. portfolio companies (effektiv februar 2025)",
                  "Vanguard SAI på SEC EDGAR (Appendix, Proxy voting); tekstkopi fra smed3: arbeid/hack/varianter/smed3_utf_sitat/rl/vg_us_2025.txt",
                  vanguard(SMED3.read_text(), "VG25", "Introduction"),
                  "Brukes for møter før 12.01.2026 (Vanguard delte stewardship-teamet i to fra 2026-sesongen).")
alle += skriv("nbim_global_voting_guidelines", "NBIM: Global voting guidelines (nettversjon)",
              "https://www.nbim.no/en/responsible-investment/voting/global-voting-guidelines/",
              nbim_web((RAA / "nbim_gvg_web.txt").read_text().split("\n")),
              "PDF-utgave 2024: https://nbim.no/contentassets/01a7ee19b5d84a73a67a365e76a0fb01/global-voting-guidelines2024.pdf. "
              "Nummerering: prinsipp.delpunkt.ledd (prinsipp 1-6 som på nbim.no).")
pp = []
for nr, f in enumerate(sorted(RAA.glob("nbim_pp_*.html")), 1):
    slug = f.stem.replace("nbim_pp_", "")
    pp += nbim_posisjon(slug, html_tekst(f.read_text()), nr)
alle += skriv("nbim_posisjonsnotater", "NBIM: posisjonsnotater (position papers)",
              "https://www.nbim.no/en/responsible-investment/position-papers/ (ett notat per underside)", pp,
              "Nummerering: NBIM-PP<notat> <ledd>.")
with open(UT / "punkter.jsonl", "w", encoding="utf-8") as f:
    for q in alle:
        f.write(json.dumps(q, ensure_ascii=False) + "\n")
for k, v in KILDER.items():
    print(k, v[2], "punkter")
print("totalt", len(alle))
