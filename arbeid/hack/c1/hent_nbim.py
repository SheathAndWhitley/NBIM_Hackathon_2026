"""Hent NBIMs egne stemmer (Norges Bank, CIK 1374170) fra SEC Form N-PX til CSV (dommer2, #1971).

Bruk: python3 -I hent_nbim.py [--ut data/nbim_votes.csv]
Laster ned ProxyVotingTable.xml for de tre N-PX-årene (2024, 2025, 2026) fra
https://www.sec.gov/Archives/edgar/data/1374170/<accession>/ProxyVotingTable.xml
og skriver samme CSV som arbeid/arkitekt/hack1942/parse_nbim.py (fil, issuer, cusip, isin, dato, tekst,
kategori, stemme, styret). Kolonnen 'styret' er N-PX-feltet managementRecommendation: hos NBIM er det
fasiten («med/mot ledelsen») og leses aldri av lag_v3.py. Rå XML caches i data/raw_nbim/. Bare stdlib.
"""
import argparse, csv, os, sys, time, urllib.request
import xml.etree.ElementTree as ET

USER_AGENT = __import__("os").environ.get("SEC_USER_AGENT", "Navn kontaktadresse")  # SEC krever navn og e-post: sett SEC_USER_AGENT  # SEC krever User-Agent med kontaktinfo
HER = os.path.dirname(os.path.abspath(__file__))
CIK = 1374170
ACCESSIONS = ["000137417024000042", "000137417025000082", "000137417026000072"]  # N-PX 2024, 2025, 2026
NS = "{http://www.sec.gov/edgar/document/npxproxy/informationtable}"


def hent(url, sti):
    if os.path.exists(sti): return sti
    for i in range(6):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=120) as r: data = r.read()
            with open(sti + ".tmp", "wb") as f: f.write(data)
            os.replace(sti + ".tmp", sti); time.sleep(0.3)
            return sti
        except Exception as e:
            print(f"  feil {e} på {url}, prøver igjen", file=sys.stderr); time.sleep(5 * (i + 1))
    raise RuntimeError(url)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ut", default=os.path.join(HER, "data", "nbim_votes.csv"))
    a = p.parse_args()
    raw = os.path.join(HER, "data", "raw_nbim"); os.makedirs(raw, exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(a.ut)), exist_ok=True)
    n = 0
    with open(a.ut, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["fil", "issuer", "cusip", "isin", "dato", "tekst", "kategori", "stemme", "styret"])
        for acc in ACCESSIONS:
            url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc}/ProxyVotingTable.xml"
            sti = hent(url, os.path.join(raw, f"vt_{acc}.xml"))
            for t in ET.parse(sti).getroot().iter(NS + "proxyTable"):
                g = lambda k: (t.findtext(NS + k) or "").strip()
                kat = "|".join(c.text or "" for c in t.iter(NS + "categoryType"))
                for vr in t.iter(NS + "voteRecord"):
                    w.writerow([acc, g("issuerName"), g("cusip"), g("isin"), g("meetingDate"),
                                g("voteDescription"), kat, (vr.findtext(NS + "howVoted") or "").strip(),
                                (vr.findtext(NS + "managementRecommendation") or "").strip()])
                    n += 1
            print(f"  {acc}: {url}")
    print(f"Skrev {n} stemmer til {a.ut}")


if __name__ == "__main__":
    main()
