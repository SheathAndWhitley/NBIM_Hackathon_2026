"""Case 1 demo: viser tre saker fra den ekte agentens kjøring på test 2026, med NBIMs egne stemmer som fasit.
Sakene trekkes, ikke håndplukkes: alle saker i hver kategori sortert på id, numpy default_rng(0) velger én.
  1 MOT funnet: agenten går mot styret, NBIM gjorde det også, med sitat
  2 usikker: kalibrert P(MOT) i båndet [0,15, 0,85), sendt til menneske
  3 MOT bom: agenten går mot styret, men NBIM fulgte styret (rutet eller ikke; med det nye
    båndet er alle falske MOT på test 2026 sendt til menneske)
Hver sak viser retningslinjen som avgjør (retningslinje_id + ordrett NBIM GVG-avsnitt).
Bruk: python3 -I demo_vis.py AGENT_CSV REAL_VOTES_CSV
"""
import csv, sys
import numpy as np

ag = list(csv.DictReader(open(sys.argv[1])))
fas = {f"{r['meeting_id']}|{r['item_no']}": r for r in csv.DictReader(open(sys.argv[2]))
       if r["year"] == "2026" and r["against_board"] != ""}
ag = sorted((r for r in ag if r["id"] in fas), key=lambda r: r["id"])
# MOT mot styret som måler v3 --score mot (hovedmålet): NBIM stemte MOT og styret sa ikke MOT. AVSTÅ telles ikke.
mot = lambda r: fas[r["id"]]["nbim_vote"] == "MOT" and fas[r["id"]]["against_board"] == "1.0"
pmot = lambda r: r["anbefaling"] == "MOT" and r["mot_styret"] == "1"
fulgte = lambda r: fas[r["id"]]["against_board"] == "0.0"

tp = sum(pmot(r) and mot(r) for r in ag); fp = sum(pmot(r) and not mot(r) for r in ag)
fn = sum(not pmot(r) and mot(r) for r in ag); rut = sum(r["til_menneske"] == "1" for r in ag)
p = tp / max(tp + fp, 1); rc = tp / max(tp + fn, 1); f1 = 2 * p * rc / max(p + rc, 1e-9)
print(f"Agenten på test 2026 (NBIMs egne stemmer, {len(ag)} saker med fasit, {tp + fn} der NBIM stemte mot styret):")
print(f"  MOT funnet {tp}, falsk MOT {fp}, MOT mistet {fn}:  presisjon {p:.3f}  recall {rc:.3f}  F1 MOT {f1:.4f}")
print(f"  til menneske {rut} av {len(ag)} ({100 * rut / len(ag):.1f} %).  Følg styret: F1 MOT 0.")
print("  P(MOT) er kalibrert (isotonisk på val 2025); saken går til menneske når P(MOT) er i [15 %, 85 %),"
      " eller ved injeksjon, ukjent selskap/type eller datafeil.\n")

KAT = [("1 MOT funnet, med sitat", lambda r: pmot(r) and mot(r) and r["sitat"] and r["til_menneske"] == "0"),
       ("2 usikker, sendt til menneske", lambda r: r["til_menneske"] == "1" and r["rutingsgrunn"].startswith("usikker")),
       ("3 MOT bom (NBIM fulgte styret)", lambda r: pmot(r) and fulgte(r))]
for navn, krav in KAT:
    kand = [r for r in ag if krav(r)]
    if not kand: print(f"== Sak {navn}: ingen slike saker\n"); continue
    r = kand[np.random.default_rng(0).integers(len(kand))]; f = fas[r["id"]]
    print(f"== Sak {navn}  (trukket med seed 0 blant {len(kand)} slike)")
    print(f"   {r['id']}  {r['company']}  {r['meeting_date']}  ({f['country']}, {f['proposal_type']}, fremmet av {f['proponent']})")
    print(f"   forslag: {r['proposal_text'][:200]}")
    print(f"   styret anbefaler: {r['styret']}")
    print(f"   AGENT: {r['anbefaling']}  (mot styret {r['mot_styret']})  P(MOT) {float(r['p_mot']):.0%} kalibrert"
          f" (rå score {r['raa_score']})  SEND TIL MENNESKE: {'JA' if r['til_menneske'] == '1' else 'nei'}"
          + (f"  grunn: {r['rutingsgrunn']}" if r["rutingsgrunn"] else ""))
    if r.get("retningslinje_id"):
        print(f"   RETNINGSLINJE {r['retningslinje_id']}: «{r['retningslinje_sitat'][:300]}»"
              f"\n   grunnlag: {r['retningslinje_grunnlag'][:240]}")
    if r["sitat"]:
        print(f"   tidligere NBIM-begrunnelse ({r['punkt']}): «{r['sitat'][:300]}»\n   kilde: {r['sitat_kilde'][:160]}")
    print(f"   FASIT: NBIM stemte {f['nbim_vote_raw']} (mot styret {f['against_board'][:1]})"
          + (f"  NBIMs egen begrunnelse: {f['rationale_text'][:200]}" if f.get("rationale_text") else ""))
    print()
