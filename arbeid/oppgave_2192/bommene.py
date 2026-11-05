"""#2192: hva har de 28 MOT-stemmene agenten bommer på (FN, test 2026) felles? Samme definisjon som #2181 / måler v3 --score mot.
Kjør fra landsbymappen: python3 -I arbeid/oppgave_2192/bommene.py"""
import csv, collections, statistics as st
F = "state/opplastet/20261105_114241_real_votes.csv"
SVAR = "arbeid/hack/levering/kjor_agent_real_maskin_alene.csv"
sv = {r["id"]: r for r in csv.DictReader(open(SVAR))}
rid = lambda r: f"{r['meeting_id']}|{r['item_no']}"
alle = [r for r in csv.DictReader(open(F, encoding="utf-8", newline="")) if r["injection_flag"] != "1" and r["against_board"] != ""]
rr = [r for r in alle if r["year"] == "2026"]
er_mot = lambda r: r["nbim_vote"] == "MOT" and r["against_board"] == "1.0"
flagg = lambda r: sv[rid(r)]["anbefaling"] == "1"
mot = [r for r in rr if er_mot(r)]; fn = [r for r in mot if not flagg(r)]; tp = [r for r in mot if flagg(r)]
fp = [r for r in rr if flagg(r) and not er_mot(r)]
print(f"test 2026: {len(mot)} MOT, TP {len(tp)}, FN {len(fn)}, FP {len(fp)}")
p = lambda r: float(sv[rid(r)]["p_avvik"])
print("terskel: laveste p blant flagget =", min(p(r) for r in rr if flagg(r)), " høyeste blant ikke-flagget =", max(p(r) for r in rr if not flagg(r)))
pf = sorted(p(r) for r in fn)
print("p_avvik bommene: median %.3f, min %.3f, maks %.3f" % (st.median(pf), pf[0], pf[-1]))
print("p_avvik alle ikke-MOT ikke-flagget: median %.3f" % st.median(p(r) for r in rr if not er_mot(r) and not flagg(r)))
for lo, hi in [(0, .05), (.05, .1), (.1, .2), (.2, .3), (.3, 1)]:
    n = sum(lo <= x < hi for x in pf); m = sum(lo <= p(r) < hi for r in rr if not flagg(r))
    print(f"  p i [{lo},{hi}): {n} bommer av {m} ikke-flaggede saker")
# historikk: hadde selskapet MOT før 2026?
for_mot = collections.Counter(r["company_id"] for r in alle if r["year"] < "2026" and er_mot(r))
for_n = collections.Counter(r["company_id"] for r in alle if r["year"] < "2026")
def hist(r): return "ny i data" if for_n[r["company_id"]] == 0 else ("MOT før" if for_mot[r["company_id"]] else "aldri MOT før")
# samme møte: fant agenten andre MOT i møtet?
mote_tp = collections.Counter(r["meeting_id"] for r in tp); mote_mot = collections.Counter(r["meeting_id"] for r in mot)
def mote(r): return "agenten fant annen MOT i møtet" if mote_tp[r["meeting_id"]] else ("flere MOT i møtet, ingen funnet" if mote_mot[r["meeting_id"]] > 1 else "eneste MOT i møtet")
G = {"sakstype": lambda r: r["proposal_type"], "forslagsstiller": lambda r: r["proponent"], "land": lambda r: r["country"],
     "marked": lambda r: r["market"], "selskap": lambda r: r["company"], "selskapshistorikk": hist, "møtet": mote,
     "begrunnelse i data": lambda r: "har rationale_text" if r["rationale_text"].strip() else "ingen begrunnelse"}
for navn, g in G.items():
    cf = collections.Counter(map(g, fn)); ct = collections.Counter(map(g, tp)); cm = collections.Counter(map(g, mot))
    print(f"\n### {navn}\n| {navn} | bom (FN) | funnet (TP) | MOT totalt | funnet-andel |\n|---|---|---|---|---|")
    for k, n in cf.most_common(8 if navn != "selskap" else 6):
        print(f"| {k} | {n} | {ct[k]} | {cm[k]} | {100*ct[k]/cm[k]:.0f} % |")
print("\n### de 28 bommene")
for r in sorted(fn, key=p, reverse=True):
    print(f"{p(r):.3f} | {r['proposal_type']} | {r['country']} | {r['company'][:30]} | {r['proposal_text'][:70]} | {hist(r)} | {mote(r)}")
print("\n### p-bånd blant IKKE-flaggede saker: hvor mange saker et menneske må se for å fange bommene")
for lo in [.8, .7, .6, .5]:
    s = [r for r in rr if not flagg(r) and p(r) >= lo]
    print(f"p >= {lo}: {len(s)} saker, {sum(map(er_mot, s))} av bommene")
print("konfidens-verdier i svarfila (bommene):", collections.Counter(sv[rid(r)]["konfidens"] for r in fn).most_common())
us = [r for r in rr if r["country"] == "United States"]
print(f"USA test 2026: {len(us)} saker, MOT {sum(map(er_mot, us))}, flagget {sum(map(flagg, us))}")
mf = collections.Counter(r["meeting_id"] for r in rr if flagg(r))
print("bommer i møter der agenten ikke flagget noe som helst:", sum(mf[r["meeting_id"]] == 0 for r in fn))
# Standardkjøringen (#2132): hvilke av bommene sendes til menneske?
AG = {r["id"]: r for r in csv.DictReader(open("arbeid/oppgave_2132/agent.csv"))}
rut = [r for r in fn if AG[rid(r)]["til_menneske"] == "1"]; urut = [r for r in fn if AG[rid(r)]["til_menneske"] != "1"]
print(f"\n### ruting (#2132 standard): {len(rut)} av {len(fn)} bommer går til menneske, {len(urut)} ser ingen")
print("rutingsgrunn:", collections.Counter(AG[rid(r)]["rutingsgrunn"].split(";")[0][:40] for r in rut).most_common())
print("usette per sakstype:", collections.Counter(r["proposal_type"] for r in urut).most_common())
print("usette per land:", collections.Counter(r["country"] for r in urut).most_common())
print("usette P(MOT) kalibrert maks:", max(float(AG[rid(r)]["p_mot"]) for r in urut))
for r in urut: print("  usett:", r["proposal_type"], "|", r["country"], "|", r["company"][:28], "|", r["proposal_text"][:60])
import re
RX = re.compile(r"state of incorporation|reincorporat|supermajority|threshold to submit|adjourn meeting", re.I)
for aar in ["2026", "<2026"]:
    s = [r for r in alle if (r["year"] == "2026" if aar == "2026" else r["year"] < "2026") and r["country"] == "United States" and RX.search(r["proposal_text"])]
    print(f"USA aksjonærrettighets-saker (reinkorporering/supermajoritet/terskel/utsettelse) {aar}: {len(s)} saker, {sum(map(er_mot, s))} MOT"
          + (f", agenten flagget {sum(map(flagg, s))}, til menneske {sum(AG[rid(r)]['til_menneske']=='1' for r in s)}" if aar == "2026" else ""))
