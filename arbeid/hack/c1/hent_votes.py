"""Hent N-PX-stemmer (proxytable.xml) for en eller flere forvaltere til én felles tabell.

Bruk:
    python hent_votes.py --cik 36405 --fra 2024 --ut data/votes.csv
    python hent_votes.py --cik 36405 52848 --fra 2024 --ut data/votes.csv

Kun standardbiblioteket. Rå XML caches i data/raw/ (gjenbrukes ved ny kjøring).
Én rad per proxyTable-post (forslag x fond/serie). Ved delte stemmer (flere
voteRecord) velges retningen med flest aksjer, og 'delt'=1.
Kolonner: se KOLONNER. mot_ledelsen=1 når stemmen avviker fra managementRecommendation.
Kilde: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=N-PX
"""
import argparse, csv, json, os, sys, time, urllib.request
import xml.etree.ElementTree as ET

USER_AGENT = __import__("os").environ.get("SEC_USER_AGENT", "Navn kontaktadresse")  # SEC krever navn og e-post: sett SEC_USER_AGENT
HER = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HER, "data", "raw")
KOLONNER = ["forvalter_cik", "forvalter", "accession", "innsendt", "serie", "serienavn",
            "utsteder", "cusip", "isin", "moetedato", "forslag", "kategori", "kilde",
            "aksjer", "stemme", "ledelsen", "mot_ledelsen", "delt", "n_rec", "manager"]


def hent(url, forsok=10):
    for i in range(forsok):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            time.sleep(0.4)  # SEC: maks 10 kall/s, og vi deler kvoten med de andre agentene
            return data
        except Exception as e:
            print(f"  feil {e} på {url}, prøver igjen", file=sys.stderr)
            time.sleep(min(60, 5 * (i + 1)))
    raise RuntimeError(url)


def cache(navn, url):
    sti = os.path.join(RAW, navn)
    if not os.path.exists(sti):
        data = hent(url)
        with open(sti + ".tmp", "wb") as f:
            f.write(data)
        os.replace(sti + ".tmp", sti)
    return sti


def npx_filer(cik, fra_aar):
    sti = cache(f"sub{int(cik)}.json", f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json")
    d = json.load(open(sti))
    lister = [d["filings"]["recent"]]
    for ekstra in d["filings"].get("files", []):
        if ekstra["filingTo"][:4] >= str(fra_aar):
            lister.append(json.load(open(cache(ekstra["name"], f"https://data.sec.gov/submissions/{ekstra['name']}"))))
    ut, sett = [], set()
    for r in lister:
        for form, acc, dato in zip(r["form"], r["accessionNumber"], r["filingDate"]):
            if form.startswith("N-PX") and int(dato[:4]) >= fra_aar and acc not in sett:
                sett.add(acc); ut.append((acc, dato, form))
    return d["name"], ut


def lokal(tag):
    return tag.rsplit("}", 1)[-1]


def serienavn(sti):
    """series-id -> navn fra primary_doc.xml (navnet står i en kommentar etter seriesId)."""
    import re
    tekst = open(sti, encoding="utf-8", errors="replace").read()
    return dict(re.findall(r"<seriesId>(S\d+)</seriesId>\s*<!--[^>]*?Series Name; Data: (.*?)-->", tekst))


def iso(d):
    m, dd, y = d.split("/")
    return f"{y}-{m}-{dd}"


def parse_tabell(sti, felles, snavn, w):
    n = 0
    for ev, el in ET.iterparse(sti, events=("end",)):
        if lokal(el.tag) != "proxyTable":
            continue
        rad = dict(felles)
        kat, recs = [], []
        for x in el:
            t = lokal(x.tag)
            tekst = (x.text or "").strip()
            if t == "issuerName": rad["utsteder"] = tekst
            elif t == "cusip": rad["cusip"] = tekst
            elif t == "isin": rad["isin"] = tekst
            elif t == "meetingDate": rad["moetedato"] = iso(tekst)
            elif t == "voteDescription": rad["forslag"] = " ".join(tekst.split())
            elif t == "voteSource": rad["kilde"] = tekst
            elif t == "sharesVoted": rad["aksjer"] = tekst
            elif t == "voteSeries": rad["serie"] = tekst
            elif t == "voteManager":
                rad["manager"] = "|".join((c.text or "").strip() for c in x.iter() if lokal(c.tag) == "otherManager")
            elif t == "voteCategories":
                kat = [(c.text or "").strip() for c in x.iter() if lokal(c.tag) == "categoryType"]
            elif t == "vote":
                for vr in x:
                    b = {lokal(y.tag): (y.text or "").strip() for y in vr}
                    recs.append((b.get("howVoted", ""), float(b.get("sharesVoted") or 0),
                                 b.get("managementRecommendation", "")))
        rad["kategori"] = "|".join(kat)
        rad["serienavn"] = snavn.get(rad.get("serie", ""), "")
        rad["n_rec"] = len(recs)
        if recs:
            hv, _, lr = max(recs, key=lambda r: r[1])
            rad["stemme"], rad["ledelsen"] = hv, lr
            rad["delt"] = int(len({r[0] for r in recs}) > 1)
            rad["mot_ledelsen"] = int(bool(lr) and lr not in ("NONE", "N/A") and hv != lr)
        else:
            rad["stemme"] = rad["ledelsen"] = ""
            rad["delt"] = rad["mot_ledelsen"] = 0
        w.writerow(rad)
        n += 1
        el.clear()
    return n


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--cik", nargs="+", required=True)
    p.add_argument("--fra", type=int, default=2024, help="første innsendingsår (XML fra 2024)")
    p.add_argument("--ut", default=os.path.join(HER, "data", "votes.csv"))
    p.add_argument("--liste", action="store_true", help="bare list innsendingene")
    p.add_argument("--maks", type=int, default=0, help="maks innsendinger per CIK (0 = alle)")
    a = p.parse_args()
    os.makedirs(RAW, exist_ok=True)
    if a.liste:  # bare list, skriv aldri (overskrev votes.csv 05.11)
        for cik in a.cik:
            navn, filer = npx_filer(cik, a.fra)
            print(f"{navn} (CIK {cik}): {len(filer)} N-PX-innsendinger fra {a.fra}")
            for x in filer: print("  ", *x)
        return
    tot = 0
    with open(a.ut + ".tmp", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=KOLONNER, extrasaction="ignore")
        w.writeheader()
        for cik in a.cik:
            navn, filer = npx_filer(cik, a.fra)
            if a.maks:
                filer = filer[: a.maks]
            print(f"{navn} (CIK {cik}): {len(filer)} N-PX-innsendinger fra {a.fra}")
            if a.liste:
                for x in filer: print("  ", *x)
                continue
            for acc, dato, form in filer:
                acc0 = acc.replace("-", "")
                base = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc0}"
                try:
                    idx = json.load(open(cache(f"{acc0}_index.json", f"{base}/index.json")))
                except RuntimeError:
                    print(f"  {acc}: hoppet over (SEC svarte ikke), kjør på nytt senere"); continue
                navnliste = [i["name"] for i in idx["directory"]["item"]]
                tab = [x for x in navnliste if x.lower().endswith(".xml") and x != "primary_doc.xml"]
                if not tab:
                    print(f"  {acc} {dato}: ingen stemmetabell (notice?)")
                    continue
                snavn = {}
                if "primary_doc.xml" in navnliste:
                    snavn = serienavn(cache(f"{acc0}_primary.xml", f"{base}/primary_doc.xml"))
                felles = {"forvalter_cik": int(cik), "forvalter": navn, "accession": acc,
                          "innsendt": dato}
                n = 0
                for t in tab:
                    try:
                        sti = cache(f"{acc0}_{t}", f"{base}/{t}")
                    except RuntimeError:
                        print(f"  {acc}: {t} hoppet over (SEC svarte ikke)"); continue
                    try:
                        n += parse_tabell(sti, felles, snavn, w)
                    except ET.ParseError as e:
                        print(f"  parsefeil {t}: {e}")
                tot += n
                print(f"  {acc} {dato} {form}: {n} poster (totalt {tot})", flush=True)
    os.replace(a.ut + ".tmp", a.ut)
    print(f"Skrev {tot} rader til {a.ut}")


if __name__ == "__main__":
    main()
