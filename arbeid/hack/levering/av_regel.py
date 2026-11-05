"""Av-regel (#2701, natt #2887): et MOT-flagg tas av når NBIMs siste stemme på samme forslag i samme selskap
(samme company_id og samme normaliserte tekst, bare år før sakens år) var FOR. Ingen ny trening, bare etterbehandling.
Samme logikk som arbeid/oppgave_2701/siste_repo4.py (bruk med regel "av").

Som modul:  h = av_regel.Historikk(real_votes.csv);  h.siste(company_id, proposal_text, aar) -> "FOR"/"MOT"/None
Som skript: python av_regel.py <real_votes.csv> <svar.csv> <aar> <ut.csv>   (svar.csv i måler-format id,anbefaling,p_avvik)
"""
import collections, csv, re, sys

norm = lambda t: re.sub(r"[^a-z ]", "", (t or "").lower()).strip()


def _cid(x):
    x = str(x or "").strip()
    return str(int(float(x))) if re.fullmatch(r"\d+(\.0+)?", x) else x


class Historikk:
    def __init__(self, sti):
        self.R = [r for r in csv.DictReader(open(sti, encoding="utf-8")) if r["injection_flag"] != "1"]
        self.h = collections.defaultdict(list)  # nøkkel -> [(år, stemme)] sortert på møtedato
        for r in sorted((r for r in self.R if r["nbim_vote"] in ("FOR", "MOT")), key=lambda r: r["meeting_date"]):
            self.h[(_cid(r["company_id"]), norm(r["proposal_text"]))].append((int(r["year"]), r["nbim_vote"]))

    def siste(self, company_id, tekst, aar):
        v = [s for y, s in self.h.get((_cid(company_id), norm(tekst)), []) if y < int(aar)]
        return v[-1] if v else None

    def ta_av(self, mot, company_id, tekst, aar):
        return bool(mot) and self.siste(company_id, tekst, aar) == "FOR"


if __name__ == "__main__":
    data, inn, aar, ut = sys.argv[1:5]
    H = Historikk(data); F = {f"{r['meeting_id']}|{r['item_no']}": r for r in H.R}; n = 0
    with open(ut, "w") as o:
        o.write("id,anbefaling,p_avvik\n")
        for x in csv.DictReader(open(inn)):
            a = x["anbefaling"] == "1"; r = F.get(x["id"])
            if r is not None and H.ta_av(a, r["company_id"], r["proposal_text"], aar): a = False; n += 1
            o.write(f"{x['id']},{int(a)},{x['p_avvik']}\n")
    print(f"av-regel {aar}: {n} MOT-flagg tatt av")
