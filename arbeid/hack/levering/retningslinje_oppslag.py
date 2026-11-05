"""Oppslag fra saken til avsnittet i NBIMs Global Voting Guidelines som avgjør (smed2 #2106).

Ren BM25 (ingen ny modell, ingen ny avhengighet) over de 140 nummererte punktene i
arbeid/hack/c1/retningslinjer/punkter.jsonl (id «NBIM prinsipp.delpunkt.ledd», speider #1948).
Poeng per punkt = BM25(spørring, punkt)
                + W_TYPE * andel av NBIMs tidligere MOT-begrunnelser for samme forslagstype som lå i punktets seksjon
                + W_NABO hvis punktet ligger i seksjonen til det tidligere sitatet (nabo-begrunnelsen)
                + W_RETNING hvis punktet er en avgjørende regel i riktig retning
                  («We will not support» for styreforslag, «We will support» for aksjonærforslag).
Spørring = forslagstype (utvidet med ord) + forslagsteksten + nabo-begrunnelsens tekst.
Alt bygger bare på tidligere år (historikken filtreres på year < sakens år); sakens egen begrunnelse
og seksjon brukes aldri. Prediksjonen påvirkes ikke: dette kjøres etter at MOT/FOR er bestemt.
"""
import json, math, os, re
from collections import Counter, defaultdict

HER = os.path.dirname(os.path.abspath(__file__))
PUNKTER = os.path.join(HER, "../c1/retningslinjer/punkter.jsonl")
KILDE = "NBIM Global Voting Guidelines (nbim.no, hentet 05.11.2026)"
W_TYPE, W_NABO, W_RETNING, MED_NABOTEKST, REGEL = 0.0, 12.0, 0.0, True, False  # valgt på val 2025 (arbeid/oppgave_2106/evaluer.py), låst før test 2026
# #2120: avsnittet innen seksjonen velges fra saken, ikke fra nabo-teksten (som ga én fast setning per seksjon).
# PRINSIPP=True: blant seksjonens prinsipp-avsnitt (ikke «We will ...»-regler, saken sier ikke hvilken regel som slo til)
# velges det som passer forslagstype+saksteksten best (BM25 med enkel stamming og synonymer), likt -> første avsnitt.
# ANTITAKEOVER=True: saker med anti-takeover-ord flyttes til 6.2 (NBIMs seksjon for anti-takeover). Valgt på val 2025.
TYPE_N, TYPE_ANDEL = int(os.environ.get("C1_TYPE_N", 10)), float(os.environ.get("C1_TYPE_ANDEL", 0.8))
PRINSIPP, ANTITAKEOVER = os.environ.get("C1_AVSNITT", "første"), True  # "av" | "prinsipp" | "sak"
SYNONYM = {"pre-emptive": "pro rata participate", "pre-emption": "pro rata participate", "preemptive": "pro rata participate",
           "supermajority": "anti-takeover", "super-majority": "anti-takeover", "poison": "anti-takeover", "takeover": "anti-takeover",
           "term": "election term", "staggered": "classify stagger", "classified": "classify stagger"}
ANTI = re.compile(r"supermajority|super-majority|poison pill|rights plan|takeover|anti-takeover", re.I)
STOPP = set("the a an of to and or in for on by with is are be as that this its at from which their will may any "
            "other such not it we our us should has have been if where when than more shareholder shareholders "
            "company companies board proposal proposals support".split())
TYPEORD = {
    "DIRECTOR_ELECTION": "director election re-election board independence independent", "AUDITOR": "auditor audit fees",
    "FIN_STATEMENTS": "financial statements annual report accounts", "DISCHARGE": "discharge liability board actions",
    "DIVIDEND": "dividend allocation income capital", "SAY_ON_PAY": "remuneration report policy pay executive ceo",
    "DIRECTOR_PAY": "remuneration directors fees", "EQUITY_PLAN": "remuneration share plan incentive vesting shares",
    "ARTICLES": "governing documents articles amend amendment", "SHARE_ISSUANCE": "share issuance issue pre-emption rights",
    "SHARE_REPURCHASE": "repurchase shares capital", "RPT": "related-party related party transaction",
    "MERGER": "merger acquisition corporate transaction", "SHP_SUSTAINABILITY": "sustainability disclosure reporting",
    "SHP_GOVERNANCE": "governance shareholder rights", "SHP_INDEP_CHAIR": "separation chairperson ceo independent chair",
    "ANTITAKEOVER": "anti-takeover takeover defence", "DUAL_CLASS": "voting rights share classes one share one vote",
    "CLASSIFY_BOARD": "classify stagger board elections", "SAY_ON_PAY_FREQ": "remuneration frequency",
}


def ord_(t): return [w for w in re.findall(r"[a-z]+", str(t).lower()) if len(w) > 2 and w not in STOPP]


def stam(t):
    t = str(t).lower()
    for k, v in SYNONYM.items(): t = re.sub(rf"\b{re.escape(k)}\b", f"{k} {v}", t)
    return [re.sub(r"(ies|es|s)$", "", w) if len(w) > 4 else w for w in ord_(t)]


def seksjon(pid): return ".".join(pid.split()[1].split(".")[:2])  # «NBIM 3.2.4» -> «3.2»


class Oppslag:
    def __init__(self, H, k1=1.2, b=0.75):
        """H: historikken (real_votes) som DataFrame. Bare GVG-punktene i prinsipp 1-6 er kandidater."""
        P = [json.loads(l) for l in open(PUNKTER, encoding="utf-8")]
        self.P = [p for p in P if p["id"].startswith("NBIM ") and not p["id"].startswith("NBIM 0.")]
        self.dok = [ord_(p["avsnitt"] + " " + p["tekst"]) for p in self.P]
        self.tf = [Counter(d) for d in self.dok]
        self.dl = [len(d) for d in self.dok]; self.avg = sum(self.dl) / len(self.dl)
        df = Counter(w for d in self.dok for w in set(d)); n = len(self.dok)
        self.idf = {w: math.log(1 + (n - c + 0.5) / (c + 0.5)) for w, c in df.items()}
        self.k1, self.b = k1, b
        self.sek = [seksjon(p["id"]) for p in self.P]
        self.retning = [p["tekst"].startswith("We will not support") for p in self.P]
        self.for_retning = [p["tekst"].startswith("We will support") for p in self.P]
        # forslagstype -> år -> Counter(seksjon) fra NBIMs MOT-begrunnelser (brukes kumulativt, bare år før saken)
        self.prior = defaultdict(lambda: defaultdict(Counter))
        M = H[(H.against_board == 1.0) & H.rationale_section.fillna("").str.startswith("GVG")]
        for t, y, s in zip(M.proposal_type.astype(str), M.year.astype(int), M.rationale_section):
            self.prior[t][y][s.split()[1]] += 1
        self.pp = {}  # «Position paper: Board independence» -> «NBIM-PP2»
        for p in P:
            if p["id"].startswith("NBIM-PP"): self.pp.setdefault(p["pilar"].strip().lower().rstrip("s"), p["id"].split()[0])
        self.forste = next(i for i, p in enumerate(P) if p["id"] == "NBIM 0.0.3")
        self.start = P[self.forste]

    def bm25(self, q):
        q = Counter(ord_(q)); ut = []
        for tf, dl in zip(self.tf, self.dl):
            s = 0.0
            for w, qn in q.items():
                f = tf.get(w)
                if f: s += self.idf[w] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * dl / self.avg))
            ut.append(s)
        return ut

    def finn(self, proposal_type, proposal_text, year, aksjonaer=False, nabo_tekst="", nabo_seksjon="", nabo_pp=""):
        """(id, sitat, seksjon, grunnlag) for punktet som avgjør en MOT-sak. year: sakens år."""
        t = str(proposal_type or "")
        c = Counter()
        for y, cc in self.prior.get(t, {}).items():
            if y < int(year): c.update(cc)
        tot = sum(c.values())
        nabo = str(nabo_seksjon or "").replace("GVG", "").strip()
        q = " ".join([TYPEORD.get(t, t.replace("_", " ").lower()), str(proposal_text or ""), str(nabo_tekst or "") if MED_NABOTEKST else ""])
        s = self.bm25(q)
        for i in range(len(s)):
            if tot: s[i] += W_TYPE * c[self.sek[i]] / tot
            if nabo and self.sek[i] == nabo: s[i] += W_NABO
            if (self.for_retning if aksjonaer else self.retning)[i]: s[i] += W_RETNING
        if ANTITAKEOVER and ANTI.search(str(proposal_text or "")):
            for i in range(len(s)):
                if self.sek[i] == "6.2": s[i] += 1000
        # TYPESEKSJON: har forslagstypen ≥ TYPE_N tidligere MOT-begrunnelser og ≥ TYPE_ANDEL i én seksjon, brukes den seksjonen
        topp1 = c.most_common(1)
        if TYPE_ANDEL < 1 and topp1 and tot >= TYPE_N and topp1[0][1] / tot >= TYPE_ANDEL and not (ANTITAKEOVER and ANTI.search(str(proposal_text or ""))):
            for i in range(len(s)):
                if self.sek[i] == topp1[0][0]: s[i] += 1000
        j = max(range(len(s)), key=s.__getitem__)
        if PRINSIPP != "av":
            kand = [i for i in range(len(s)) if self.sek[i] == self.sek[j]
                    and (PRINSIPP == "sak" or (PRINSIPP.startswith("prinsipp") or PRINSIPP == "første") and not re.search(r"\bwe will\b", self.P[i]["tekst"], re.I))]
            if kand:
                q = Counter(stam(" ".join([TYPEORD.get(t, t.replace("_", " ").lower()), str(proposal_text or "")])))
                def sc(i):
                    d = Counter(stam(self.P[i]["tekst"]))
                    return sum(min(q[w], 1) * min(d[w], 1) for w in q)
                if PRINSIPP == "første":  # seksjonens første prinsipp, unntatt når et fagbegrep i saken peker på et annet
                    tx = str(proposal_text or "").lower()
                    q = Counter(w for k, v in SYNONYM.items() if re.search(rf"\b{re.escape(k)}\b", tx) for w in stam(v))
                j = max(kand, key=lambda i: (sc(i), -i) if PRINSIPP == "første" else (sc(i), -i) if PRINSIPP == "prinsipp" else (sc(i), s[i]) if PRINSIPP == "prinsipp_s" else (s[i],) if PRINSIPP == "prinsipp_gammel" else (sc(i), s[i]))
        # REGEL=True velger «We will not support»-regelen i seksjonen fra saksteksten. Av (stikkprøve #2106): saken sier ikke
        # hvilken regel som slo til (oppmøte, honorarer, lav støtte), så det blir gjetning. Reglene listes i grunnlaget i stedet.
        rett = self.for_retning if aksjonaer else self.retning
        regler = [self.P[i]["id"].split()[1] for i in range(len(s)) if self.sek[i] == self.sek[j] and rett[i]]
        if REGEL:  # i valgt seksjon: velg regelen i riktig retning som passer saksteksten best (BM25 uten nabo-tekst)
            rett = self.for_retning if aksjonaer else self.retning
            kand = [i for i in range(len(s)) if self.sek[i] == self.sek[j] and rett[i]]
            if kand:
                q2 = self.bm25(" ".join([TYPEORD.get(t, t.replace("_", " ").lower()), str(proposal_text or "")]))
                if PRINSIPP == "første":  # seksjonens første prinsipp, unntatt når et fagbegrep i saken peker på et annet
                    tx = str(proposal_text or "").lower()
                    q = Counter(w for k, v in SYNONYM.items() if re.search(rf"\b{re.escape(k)}\b", tx) for w in stam(v))
                j = max(kand, key=lambda i: (sc(i), -i) if PRINSIPP == "første" else (q2[i], s[i]))
        topp = c.most_common(1)
        gr = (f"BM25 {s[j]:.1f}; type {t}: {c[self.sek[j]]}/{tot} tidligere MOT-begrunnelser i {self.sek[j]}"
              + (f"; nabo-begrunnelsen i {nabo}" if nabo else "")
              + (f"; regler i seksjonen et menneske bør sjekke: {', '.join(regler)}" if regler else ""))
        # posisjonsnotat fra nabo-begrunnelsen (#2106): stemmer med sakens eget i 56 % (val 2025) / 79 % (test 2026)
        pps = [x.strip() for x in str(nabo_pp or "").split(";") if x.strip()]
        pps = list(dict.fromkeys(f"{x.split(':', 1)[-1].strip()} ({self.pp[x.lower().rstrip('s')]})" if x.lower().rstrip("s") in self.pp else x for x in pps))
        if pps: gr += "; posisjonsnotat (fra nabo-begrunnelsen): " + ", ".join(pps)
        return self.P[j]["id"], self.P[j]["tekst"], self.sek[j], gr
