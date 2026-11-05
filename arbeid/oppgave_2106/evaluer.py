"""Mål retningslinje-oppslaget mot NBIMs egne seksjonsnumre (rationale_section «GVG x.y») på MOT-saker.
Fasit-seksjonen brukes bare til måling. Vekter velges på val 2025, test 2026 rapporteres uendret.
  uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2106/evaluer.py
"""
import itertools, os, sys
import pandas as pd
ROT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, os.path.join(ROT, "arbeid/hack/levering"))
import c1_real, retningslinje_oppslag as RO

H = pd.read_csv(c1_real.REAL, low_memory=False)
O = RO.Oppslag(H)
bank = c1_real.sitatbank(H)


def kjor(år, wt, wn, wr, mn=True):
    RO.W_TYPE, RO.W_NABO, RO.W_RETNING, RO.MED_NABOTEKST = wt, wn, wr, mn
    R = H[(H.year == år) & (H.against_board == 1) & H.rationale_section.fillna("").str.startswith("GVG")]
    nab = c1_real.finn_sitat(bank, R)
    rad = []
    for (_, r), nb in zip(R.iterrows(), nab):
        nt, ns = (str(nb[0].rationale_text), str(nb[0].rationale_section)) if nb else ("", "")
        pid, st, sek, _ = O.finn(r.proposal_type, r.proposal_text, r.year, r.proponent == "Shareholder", nt, ns)
        fasit = r.rationale_section.split()[1]
        # fasit-avsnitt: punktet i fasit-seksjonen som ligner mest på NBIMs faktiske begrunnelse
        bm = O.bm25(r.rationale_text)
        kand = [i for i in range(len(O.P)) if O.sek[i] == fasit]
        gull = O.P[max(kand, key=bm.__getitem__)]["id"] if kand else ""
        rad.append(dict(id=c1_real.rid(r), type=r.proposal_type, tekst=r.proposal_text, fasit=fasit, sek=sek, pid=pid,
                        gull=gull, nabo=ns.replace("GVG", "").strip(), sitat=st, begr=r.rationale_text))
    return pd.DataFrame(rad)


def tall(D):
    return dict(n=len(D), seksjon=(D.sek == D.fasit).mean(), nabo_alene=(D.nabo == D.fasit).mean(),
                fasitavsnitt=(D.pid == D.gull).mean())


if __name__ == "__main__":
    print("variant (W_TYPE, W_NABO, W_RETNING) -> val 2025 seksjonstreff / fasitavsnitt")
    best = None
    for w in itertools.product([0, 2, 4, 6, 10, 20], [0, 1.5, 3, 6, 12], [0, 1.5], [True, False]):
        t = tall(kjor(2025, *w))
        if best is None or (t["seksjon"], t["fasitavsnitt"]) > (best[1]["seksjon"], best[1]["fasitavsnitt"]): best = (w, t)
        if w[1:3] == (0, 0) or w[0] == 0 and w[2] == 0: print(w, {k: round(v, 3) for k, v in t.items()})
    print("beste på val:", best)
    for w, navn in ((best[0], "låst fra val"), ((0, 0, 0, False), "bare BM25 på saksteksten"), ((10, 0, 0, False), "BM25 + typeprior")):
        for år in (2025, 2026):
            D = kjor(år, *w); print(år, navn, w, {k: round(v, 3) for k, v in tall(D).items()})
            if år == 2026 and navn.startswith("låst"): D.to_csv(os.path.join(os.path.dirname(__file__), "test2026_mot.csv"), index=False)
    import json; json.dump(dict(beste=best[0]), open(os.path.join(os.path.dirname(__file__), "beste_vekter.json"), "w"))
