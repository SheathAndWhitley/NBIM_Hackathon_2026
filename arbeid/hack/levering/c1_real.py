"""Case 1-agenten på NBIMs egne stemmer (real_votes), smed #2053. Kalles fra kjor_agent.py (standard).

Delene:
  modell  modell_repo4.py (repo4, byttet inn 05.11 17:03 etter byttedom #2570: smed2 #2044 train.py + 4 historikktrekk
          fra NBIM-repoet, prev_same_item/prev_same_person/prev_meeting_any_dev/hist_type_dev_rate), kjørt UENDRET med runpy:
          --variant miks --hist 2 (logreg tfidf+kategorier ⊕ LightGBM, rangsnitt, løpende MOT-historikk fra
          møter strengt før møtedatoen). C og rå grense velges i train.py på val 2025 (trent <2025);
          prediksjonen på inn-sakene kommer fra modellen trent på <2026. Forbudte kolonner (nbim_vote*,
          rationale_*, position_paper, funds_disagree) stoppes av assert i train.py.
  P(MOT)  (#2132) p_mot er kalibrert: isotonisk regresjon på modellens val 2025-score (trent <2025) mot fasit, brukt
          på inn-sakene. raa_score er rangsnittet fra train.py (ikke en sannsynlighet, #2109). Monoton, så MOT-flagget
          (rå score >= grense) og F1 endres ikke.
  ruting  standard (#2128/#2132): saken går til menneske når kalibrert P(MOT) ligger i båndet [0,15, 0,85) (--baand).
          Med --til-menneske PROSENT brukes den gamle regelen (case1_ruting.md, strategi A): |logit(s) - logit(grense)|
          i båndet som rutet PROSENT % av val 2025. Begge låses på val. I tillegg: datafeil, injeksjon
          (rens_tekst fra #2047) og MOT uten sitat.
  retningslinje (#2106) retningslinje_oppslag.py: id og ordrett tekst fra NBIM Global Voting Guidelines (BM25 + seksjon
          fra nabo-begrunnelsen), 86 % riktig seksjon mot NBIMs egne seksjonsnumre på MOT-sakene i 2026.
  sitat   NBIMs egen begrunnelse (rationale_text) fra en tidligere sak, samme idé som smed3 nbim_sitat.py (#2037):
          nærmeste sak med MOT og begrunnelse, alltid et tidligere år og et annet møte enn saken. Begrunnelsen
          er aldri feature, bare sitat.
Inn-saker som finnes i historikkfila (samme meeting_id|item_no) bruker sin egen rad; egen etikett brukes aldri
for egen prediksjon (train.py trener på år < 2026 og historikken tar bare møter før datoen). Nye saker legges til
uten etikett.
"""
import csv, io, os, re, runpy, sys, time, contextlib, hashlib, importlib.util
import numpy as np
import pandas as pd

HER = os.path.dirname(os.path.abspath(__file__))
ARB = os.path.abspath(os.path.join(HER, "../.."))
ROT = os.path.dirname(ARB)
REAL = os.path.join(ROT, "state/opplastet/20261105_114241_real_votes.csv")
REAL_SHA = "71ba5135e7ba9d64c943f158bb510ffab53f34203f4c2875fc43352419e525e6"  # arrangørens fil 05.11 (#2221, ordre #242)
REAL_RADER = 13757
TRAIN = os.path.join(HER, "modell_repo4.py")  # #2572 bytte: oppgave_2490/abl.py + 4 repotrekk (vant byttedommen over tre testår)
REPO = "prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate"
VERN = os.path.join(ARB, "oppgave_2047/vern.py")
MAALER = os.path.join(ARB, "hack/c1/maaler_offisiell_v2.py")
TRENG = ["meeting_id", "item_no", "company_id", "meeting_date", "proposal_text", "proposal_type", "proponent"]
FELT = ["id", "company", "meeting_date", "proposal_text", "styret", "anbefaling", "mot_styret", "p_mot", "til_menneske",
        "rutingsgrunn", "punkt", "sitat", "sitat_kilde", "sitat_likhet", "injeksjon_flagget", "raa_score",
        "retningslinje_id", "retningslinje_sitat", "retningslinje_grunnlag"]


def lg(p): p = np.clip(np.asarray(p, float), 1e-6, 1 - 1e-6); return np.log(p / (1 - p))


def rid(r): return f"{r.get('meeting_id', '')}|{r.get('item_no', '')}"


def _rens():
    spec = importlib.util.spec_from_file_location("vern2047", VERN)
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
    return m.rens_tekst


# Robusthet (#2063): vern.py fanger engelske instrukser; dette fanger norsk, rolle-/tagg-/JSON-forsøk. Historikkens
# lengste forslag er 253 tegn, så lengre tekst er utenfor det modellen har sett og går til menneske.
EKSTRA_INJ = re.compile(r"(?i)\b(system|assistant|user)\s*:|</?\w+>|[{\[]\s*\"\w+\"\s*:|\bstem\s+(for|mot)\b|\bignorer\b|"
                        r"\banbefal(ing)?\b|\b(admin|developer)\s+mode\b|\bconfidence\s*1(\.0)?\b")
MAKS_TEKST = 1000
IKKE_LATIN = re.compile(r"[^\W\d_a-zA-ZÀ-ɏ]")  # bokstav utenfor latinsk (kinesisk, kyrillisk, arabisk ...)
STYRET = {"FOR": "FOR", "MOT": "MOT", "AGAINST": "MOT", "AVSTÅ": "AVSTÅ", "ABSTAIN": "AVSTÅ"}
GYLDIG = ("FOR", "MOT", "AVSTÅ")


def datafeil(r, sett):
    g = []
    m = [k for k in TRENG if not str(r.get(k) or "").strip()]
    if m: g.append("mangler felt: " + ",".join(m))
    d = str(r.get("meeting_date") or "")
    try: time.strptime(d, "%Y-%m-%d")
    except ValueError:
        if d: g.append(f"ugyldig møtedato «{d[:20]}»")
    tall = [k for k in ("meeting_id", "item_no", "company_id") if k not in m and not re.fullmatch(r"\d{1,12}", str(r.get(k)).strip())]
    if tall: g.append("ikke heltall: " + ",".join(f"{k}=«{str(r.get(k))[:20]}»" for k in tall))
    i = rid(r) if not m and not tall else None
    if i and i in sett: g.append(f"duplikat: {i} er sett før i samme fil")
    return g


def kjor_modell(data_fil, logg):
    """train.py uendret; returnerer globalene (p for alle rader, pv/t/va fra val 2025)."""
    gammel = sys.argv
    sys.argv = [TRAIN, data_fil, "--variant", "miks", "--hist", "2", "--repo", REPO, "--ut", os.devnull]
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf): g = runpy.run_path(TRAIN, run_name="smed2_2044")
    finally:
        sys.argv = gammel
    # #2236: train.py sin TEST 2026-linje bruker test-andelen (juks som hovedtall); merkes, verdiene er uendret
    merk = lambda x: ("IKKE HOVEDTALL (bare sjekk, grensa satt med test-fordelingen; hovedtallet er måler v3 under): " + x
                      if x.startswith("TEST 2026 (samme andel") else x)
    logg += ["--- smed2 train.py (#2044) ---"] + [merk(x) for x in buf.getvalue().splitlines() if x.strip()]
    return g


def sitatbank(H):
    from sklearn.feature_extraction.text import TfidfVectorizer
    tk = lambda d: (d.proposal_type.fillna("") + " " + d.proposal_text.fillna("")).tolist()
    B = H[(H.against_board == 1.0) & H.rationale_text.fillna("").str.strip().astype(bool)].reset_index(drop=True)
    tf = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True).fit(tk(H))
    return B, tf, tf.transform(tk(B)), tk


def finn_sitat(bank, R):
    from sklearn.metrics.pairwise import linear_kernel
    B, tf, BX, tk = bank
    S = linear_kernel(tf.transform(tk(R)), BX)
    by, bm, bt, bc = B.year.values.astype(int), B.meeting_id.astype(str).values, B.proposal_type.values, B.company_id.astype(str).values
    ut = []
    for i, (_, r) in enumerate(R.iterrows()):
        s = S[i] + 0.3 * (bt == r.proposal_type) + 0.1 * (bc == str(r.company_id))
        s[(by >= int(r.year)) | (bm == str(r.meeting_id))] = -9
        j = int(s.argmax())
        ut.append(None if s[j] <= 0 else (B.iloc[j], float(s[j])))
    return ut


def datavakt(sti):
    """#2221: historikken må være arrangørens nye real_votes (fast sha256), ellers exit 3. Skriver sha og radantall."""
    try: b = open(sti, "rb").read()
    except OSError as e: print(f"FEIL DATAFIL: kan ikke lese {sti}: {e}"); sys.exit(3)
    sha = hashlib.sha256(b).hexdigest()
    n = sum(1 for _ in csv.DictReader(b.decode("utf-8").splitlines()))
    print(f"DATA real_votes {os.path.basename(sti)} sha256 {sha} rader {n}")
    if sha != REAL_SHA or n != REAL_RADER:
        print(f"FEIL DATAFIL: forventet sha256 {REAL_SHA} og {REAL_RADER} rader (arrangørens fil 05.11, ordre #242),")
        print(f"  fikk sha256 {sha} og {n} rader. Bruk den nye fila; gammel eller annen data gir tall som ikke kan sammenlignes.")
        sys.exit(3)


def main(a, andel):
    datavakt(a.historikk)
    t0 = time.time(); logg = []
    os.makedirs(a.ut, exist_ok=True); work = os.path.join(a.ut, "_data"); os.makedirs(work, exist_ok=True)
    H = pd.read_csv(a.historikk, low_memory=False)
    H["_id"] = H.meeting_id.astype("Int64").astype(str) + "|" + H.item_no.astype("Int64").astype(str)
    # 1) inn-saker
    if a.sak:
        import json
        r = json.loads(a.sak)
        if not isinstance(r, dict): sys.exit("--sak må være et JSON-objekt")
        inn = [{k: ("" if v is None else str(v)) for k, v in r.items()}]
    else:
        f = a.csv or os.path.join(ARB, "hack/c1/data_off/real_test_input.csv")
        try:
            inn = list(csv.DictReader(open(f, encoding="utf-8-sig", newline="")))
        except UnicodeDecodeError as e:  # #2724: ikke UTF-8 (f.eks. Excel/latin-1) leses som latin-1 med varsel; binært gir pen feil, ikke traceback
            print(f"advarsel: inn-fila er ikke UTF-8-tekst ({e.reason}, byte {e.start}); prøver latin-1")
            try: inn = list(csv.DictReader(open(f, encoding="latin-1", newline="")))
            except csv.Error as e2: sys.exit(f"FEIL: inn-fila «{f}» kan ikke leses som CSV ({e2}); ingen saker vurdert, ingen agent.csv skrevet")
    for k in ("against_board", "nbim_vote", "nbim_vote_raw", "rationale_text", "position_paper"):
        if inn and k in inn[0]: sys.exit(f"inn-saken har fasitfeltet «{k}»; fjern det")
    if not inn: print("advarsel: inn-fila har ingen saker (bare overskrift); skriver tom agent.csv")
    rens = _rens()
    sett, stopp, inj, lang = set(), {}, {}, {}
    # høflige/omskrevne instrukser (#2237): vokabular fra historikken minus inn-sakene selv
    sys.path.insert(0, HER); import injeksjon_hoflig as hoflig; inn_id = {rid(r) for r in inn}
    hoflig.bygg(H.proposal_text[~H._id.isin(inn_id)])
    for i, r in enumerate(inn):
        g = datafeil(r, sett)
        if g: stopp[i] = "; ".join(g); continue
        sett.add(rid(r))
        r["mgmt_rec"] = STYRET.get(str(r.get("mgmt_rec") or "").strip().upper(), r.get("mgmt_rec"))  # tom forblir tom
        ren, fl = rens(r.get("proposal_text") or "")
        if not fl and EKSTRA_INJ.search(ren): fl, ren = True, ren[:EKSTRA_INJ.search(ren).start()].strip() or ren
        if not fl and hoflig.finn(r.get("proposal_text")) is not None:  # #2237: kutt i originalen, så forslaget er ordrett
            o = r["proposal_text"]; fl, ren = True, o[:hoflig.finn(o)].strip() or ren
        if fl or r.get("injection_flag") == "1": inj[i] = ren  # modellen ser renset tekst, utfila originalen
        if len(r.get("proposal_text") or "") > MAKS_TEKST: lang[i] = len(r["proposal_text"])
    # 2) data til train.py: historikk + nye saker uten etikett (kjente saker bruker sin egen rad)
    kjent = dict(zip(H._id, H.index))
    nye = [dict(r, proposal_text=inj[i]) if i in inj else r for i, r in enumerate(inn) if i not in stopp and rid(r) not in kjent]
    if nye:
        N = pd.DataFrame(nye).reindex(columns=[c for c in H.columns if c != "_id"])
        N["injection_flag"] = 0; N["against_board"] = np.nan
        N["year"] = pd.to_datetime(N.meeting_date).dt.year
        for c in ("company_id", "item_no", "meeting_id"): N[c] = pd.to_numeric(N[c], errors="coerce")
        D = pd.concat([H.drop(columns="_id"), N], ignore_index=True)
    else:
        D = H.drop(columns="_id")
    df = os.path.join(work, "data.csv"); D.to_csv(df, index=False)
    D["_id"] = D.meeting_id.astype("Int64").astype(str) + "|" + D.item_no.astype("Int64").astype(str)
    idx = dict(zip(D._id, D.index))
    # 3) modell (val 2025 velger C og grense; inn-sakene fra modellen trent <2026)
    g = kjor_modell(df, logg)
    p, pv, t, yv, C = g["p"], g["pv"], float(g["t"]), g["yv"], g["C"]
    band = float(np.quantile(np.abs(lg(pv) - lg(t)), andel)) if andel is not None and andel > 0 else -1.0
    from sklearn.isotonic import IsotonicRegression  # kalibrering lært på val 2025 (#2109), uendret modell
    iso = IsotonicRegression(out_of_bounds="clip", y_min=0, y_max=1).fit(np.asarray(pv, float), np.asarray(yv, float))
    qlo, qhi = (float(x) for x in a.baand.split(","))
    f1v = g["f"]
    tidlig = sum(1 for i, r in enumerate(inn) if i not in stopp and int(D.year[idx[rid(r)]]) < 2026)
    # 4) sitat for MOT-sakene
    bank = sitatbank(H)
    gode = [i for i in range(len(inn)) if i not in stopp]
    R = D.loc[[idx[rid(inn[i])] for i in gode]]
    sit = dict(zip(gode, finn_sitat(bank, R))) if gode else {}
    sys.path.insert(0, HER); import retningslinje_oppslag; ro = retningslinje_oppslag.Oppslag(H)
    # 5) slå sammen
    typer = set(H.proposal_type.dropna().astype(str))
    land, marked = set(H.country.dropna().astype(str)), set(H.market.dropna().astype(str))
    # Robusthet (#2071): selskap uten NBIM-stemmer før møtedatoen (modellen mangler selskapshistorikk; P(MOT) flyttet
    # seg 0,22 -> 0,52 i #2063), og kjente saker der inn-feltene avviker fra den lagrede raden modellen brukte.
    hd = pd.to_datetime(H.meeting_date, errors="coerce"); forst = hd.groupby(H.company_id.astype("Int64").astype(str)).min()
    Hk = H.set_index("_id")
    def norm(k, v):
        v = "" if v is None or (isinstance(v, float) and np.isnan(v)) else str(v).strip()
        if k == "mgmt_rec": v = STYRET.get(v.upper(), v)
        if k in ("company_id",) and re.fullmatch(r"\d+(\.0)?", v): v = str(int(float(v)))
        return v
    rader = []
    for i, r in enumerate(inn):
        styret = STYRET.get((r.get("mgmt_rec") or "FOR").strip().upper(), (r.get("mgmt_rec") or "FOR").upper())
        if i in stopp:
            rader.append(dict(id=rid(r) if r.get("meeting_id") else f"rad{i + 1}", company=r.get("company", ""),
                              meeting_date=r.get("meeting_date", ""), proposal_text=(r.get("proposal_text") or "")[:200],
                              styret=styret, anbefaling=styret if styret in GYLDIG else "TIL MENNESKE", mot_styret=0, avvik=0, p_mot="", til_menneske=1,
                              rutingsgrunn="kan ikke vurderes: " + stopp[i], punkt="", sitat="", sitat_kilde="",
                              sitat_likhet="", injeksjon_flagget=0, raa_score="", retningslinje_id="",
                              retningslinje_sitat="", retningslinje_grunnlag=""))
            continue
        s = float(p[idx[rid(r)]]); mot = s >= t; q = float(iso.predict([s])[0])
        if andel is None:
            rut = qlo <= q < qhi
            grunn = [f"usikker: kalibrert P(MOT) {q:.2f} i båndet [{qlo:g}, {qhi:g})"] if rut else []
        else:
            avst = abs(float(lg(s)) - float(lg(t))); rut = bool(avst <= band)
            grunn = [f"nær grensen: |logit-avstand| {avst:.2f} <= bånd {band:.2f}"] if rut else []
        if i in inj: rut = True; grunn.append("instruksjonslignende tekst i forslaget")
        if str(r.get("proposal_type") or "").strip() not in typer:
            rut = True; grunn.append(f"ukjent forslagstype «{str(r.get('proposal_type'))[:30]}», finnes ikke i NBIMs historikk")
        if i in lang: rut = True; grunn.append(f"uvanlig lang tekst ({lang[i]} tegn, lengste i historikken 253)")
        # #2257: kinesisk tekst fikk stille FOR (P(MOT) 0). Ingen historikk- eller testsak har ikke-latinske bokstaver.
        if IKKE_LATIN.search(r.get("proposal_text") or ""):
            rut = True; grunn.append("ikke-latinsk skrift i forslaget: språket finnes ikke i NBIMs historikk, modellen kan ikke lese det")
        f0 = forst.get(str(int(r["company_id"])))
        if f0 is None or pd.isna(f0) or f0 >= pd.Timestamp(r["meeting_date"]):
            rut = True; grunn.append("ukjent selskap: ingen NBIM-stemmer for selskapet før møtedatoen")
        # Manglende felt (#2152, robusthet #2144): tom mgmt_rec leses som FOR, og modellen bruker land og marked.
        # Bare når også mgmt_rec_raw er tom: 39 ekte 2026-saker har tom mgmt_rec men raw «None»/«One Year»
        # (punkter uten stemmeanbefaling, f.eks. «Close Meeting»); styret har svart, data mangler ikke.
        if not str(r.get("mgmt_rec") or "").strip() and not str(r.get("mgmt_rec_raw") or "").strip():
            rut = True; grunn.append("styrets anbefaling mangler: antatt FOR, sjekk innkallingen")
        mangler = [k for k in ("country", "market") if not str(r.get(k) or "").strip()]
        if mangler: rut = True; grunn.append("land/marked mangler (" + ",".join(mangler) + "), modellen bruker disse feltene")
        # Rare verdier (#2202): ukjent land/marked, møtedato utenfor det modellen kan ha sett, og styreanbefaling som
        # ikke er FOR/MOT/AVSTÅ ble vurdert stille uten ruting. Endrer bare rutingen, aldri svaret.
        ukj = [f"{k}=«{str(r.get(k))[:20]}»" for k, kj in (("country", land), ("market", marked))
               if k not in mangler and str(r.get(k)).strip() not in kj]
        if ukj: rut = True; grunn.append("ukjent land/marked (" + ",".join(ukj) + "), finnes ikke i NBIMs historikk")
        md = pd.Timestamp(r["meeting_date"])
        if md < hd.min() or md > pd.Timestamp.now().normalize() + pd.Timedelta(days=365):
            rut = True; grunn.append(f"møtedato {r['meeting_date']} utenfor perioden modellen kjenner")
        if styret not in ("FOR", "MOT", "AVSTÅ") and str(r.get("mgmt_rec") or "").strip():
            rut = True; grunn.append(f"ukjent styreanbefaling «{str(r.get('mgmt_rec'))[:20]}», ikke FOR/MOT/AVSTÅ")
        if rid(r) in Hk.index:
            k0 = Hk.loc[rid(r)]; k0 = k0.iloc[0] if isinstance(k0, pd.DataFrame) else k0
            avvik = [k for k in ("company_id", "meeting_date", "proposal_text", "proposal_type", "proponent", "mgmt_rec")
                     if k in r and k in k0.index and norm(k, r[k]) != norm(k, k0[k])]
            if avvik: rut = True; grunn.append("felt avviker fra lagret sak (" + ",".join(avvik) + "); modellen brukte lagret rad")
        pk = st = kl = ""; lk = ""
        # retningslinjen som avgjør (#2106): NBIM GVG-punkt via BM25 + seksjonen til nabo-begrunnelsen; FOR = NBIM 0.0.3
        rl_id, rl_st, rl_gr = ro.start["id"], ro.start["tekst"], "følger styret: NBIMs utgangspunkt er å støtte styret"
        if mot:
            nb = sit[i][0] if sit[i] is not None else None
            rl_id, rl_st, _, rl_gr = ro.finn(r.get("proposal_type"), inj.get(i, r.get("proposal_text")), D.year[idx[rid(r)]],
                                             str(r.get("proponent") or "") == "Shareholder",
                                             "" if nb is None else str(nb.rationale_text),
                                             "" if nb is None else str(nb.rationale_section),
                                             "" if nb is None or not isinstance(nb.position_paper, str) else nb.position_paper)
            if sit[i] is None: rut = True; grunn.append("MOT uten sitat: fant ingen tidligere NBIM-begrunnelse")
            else:
                b, lk = sit[i]
                pk = str(b.rationale_section if isinstance(b.rationale_section, str) else "")
                st = str(b.rationale_text).strip()
                kl = f"NBIMs begrunnelse {int(b.year)}, {b.company}: «{str(b.proposal_text)[:80]}»"
                lk = round(lk, 3)
        anb = ("FOR" if styret in ("MOT", "AGAINST") else "MOT") if mot else styret
        if styret not in GYLDIG: anb = "TIL MENNESKE"  # #2205: rå styreverdi («KANSKJE») er ingen stemme; rutet over
        rader.append(dict(id=rid(r), company=r.get("company", ""), meeting_date=r["meeting_date"],
                          proposal_text=(r.get("proposal_text") or "")[:200], styret=styret, anbefaling=anb,
                          mot_styret=int(anb == "MOT" and styret not in ("MOT", "AGAINST")), avvik=int(mot), p_mot=round(q, 4), til_menneske=int(rut), rutingsgrunn="; ".join(grunn),
                          punkt=pk, sitat=st, sitat_kilde=kl, sitat_likhet=lk, injeksjon_flagget=int(i in inj), raa_score=round(s, 5),
                          retningslinje_id=rl_id, retningslinje_sitat=rl_st, retningslinje_grunnlag=rl_gr))
    with open(os.path.join(a.ut, "agent.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FELT, extrasaction="ignore"); w.writeheader(); w.writerows(rader)
    # måler-format (maaler_offisiell_v2.py, id = meeting_id|item_no, anbefaling 1 = avvik fra styret)
    for fil, med in (("pred_maaler.csv", True), ("_pred_uten_ruting.csv", False)):
        with open(os.path.join(a.ut, fil), "w", newline="") as f:
            w = csv.writer(f); w.writerow(["id", "anbefaling", "konfidens", "p_avvik"])
            for x in rader:
                k = 0.5 if (med and x["til_menneske"]) else 0.9
                w.writerow([x["id"], x["avvik"], k, x["raa_score"] if x["raa_score"] != "" else 0.0])  # rangering for PR-AUC
    n, nm, nr = len(rader), sum(x["avvik"] for x in rader), sum(x["til_menneske"] for x in rader)
    nms = sum(1 for x in rader if x["mot_styret"] and x["sitat"])
    logg = [f"kjor_agent.py (real_votes, smed2 #2044-modell) {time.strftime('%Y-%m-%d %H:%M:%S')}, {time.time() - t0:.0f} s",
            f"inn: {n} saker; avvik fra styret {nm}, av dem MOT styret {sum(x['mot_styret'] for x in rader)} (med NBIM-sitat {nms}); til menneske {nr} ({nr / max(n, 1):.1%}), "
            f"av dem {len(stopp)} som ikke kunne vurderes og {len(inj)} med injeksjon",
            f"låst på val 2025: C {C}, rå grense {t:.5f} (kalibrert {float(iso.predict([t])[0]):.3f}), val-F1 {f1v:.4f}; "
            + (f"til menneske når kalibrert P(MOT) i [{qlo:g}, {qhi:g})" if andel is None else f"{andel * 100:g} %-bånd {band:.4f} logit"),
            f"nye saker lagt til uten etikett: {len(nye)}; saker fra før 2026 (i treningen, ikke ærlig målt): {tidlig}"] + logg
    if a.vindu:
        import subprocess
        for navn, fil in (("maskin alene, ruting ignorert", "_pred_uten_ruting.csv"), ("med ruting (konfidens < 0,6 = menneske)", "pred_maaler.csv")):
            o = subprocess.run(["python3", "-I", MAALER, os.path.join(a.ut, fil), a.vindu, "--data", "real"], capture_output=True, text=True)
            logg += [f"--- måler {os.path.basename(MAALER)} {a.vindu} ({navn}) ---", (o.stdout + o.stderr).strip()]
    open(os.path.join(a.ut, "KJORING.txt"), "w").write("\n".join(logg) + "\n")
    print("\n".join(logg)); print(f"skrev {os.path.join(a.ut, 'agent.csv')}")
