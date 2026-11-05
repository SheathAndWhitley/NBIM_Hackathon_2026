# Viser de tre sakene i DEMO_MANUS.md (treff, bom, til menneske) fra en agent.csv, slik juryen skal se dem (#2329/#2340).
# Sakene regnes ut hver gang, ikke slås opp: den FØRSTE i fila av hver type (samme regel som arbeid/oppgave_2260/velg.py).
# Avviker de fra id-ene manuset ble skrevet for, sier skjermen det tydelig (etter frys skal manuset da byttes, ikke sakene).
# Bruk: python3 -I arbeid/hack/c1/vis_manussaker.py AGENT_CSV [REAL_VOTES_CSV]
import csv, sys
REAL = sys.argv[2] if len(sys.argv) > 2 else "state/opplastet/20261105_114241_real_votes.csv"
MANUS = {"treff_maskin": ("2033470|1", 15), "bom_maskin": ("2048411|10", 89), "til_menneske": ("2038357|7", 39)}  # repo4, sak 2659
NAVN = {"treff_maskin": "Treff (agent MOT, NBIM MOT, maskinen alene)", "bom_maskin": "Bom (maskinen alene, feil mot fasit)",
        "til_menneske": "Til menneske (første sak agenten sendte videre)"}
fas = {f"{r['meeting_id']}|{r['item_no']}": r for r in csv.DictReader(open(REAL, encoding="utf-8"))}
first = {}
for i, r in enumerate(csv.DictReader(open(sys.argv[1], encoding="utf-8")), start=2):
    f = fas.get(r["id"])
    if f is None or f["against_board"] == "":
        continue
    pm = r["anbefaling"] == "MOT" and r["styret"] != "MOT"       # agent: MOT mot styret
    ym = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"  # fasit: MOT mot styret (#231)
    rut = r["til_menneske"] == "1"
    for k, ok in (("treff_maskin", pm and ym and not rut), ("bom_maskin", pm != ym and not rut), ("til_menneske", rut)):
        if ok and k not in first:
            first[k] = (i, r, f)
avvik = []
for k in ("treff_maskin", "bom_maskin", "til_menneske"):
    if k not in first:
        print(f"== {NAVN[k]}: ingen slik sak i fila\n"); avvik.append(k); continue
    i, r, f = first[k]
    print(f"== {NAVN[k]}: {r['company']}  {r['meeting_date']}  «{r['proposal_text']}»  (agent.csv linje {i}, {r['id']})")
    print(f"   styret: {r['styret']}   AGENT: {r['anbefaling']}   p_mot {r['p_mot']}   til_menneske {r['til_menneske']}  {r['rutingsgrunn']}")
    if r["punkt"]:
        print(f"   punkt {r['punkt']}: \"{r['sitat']}\"   [{r['sitat_kilde']}]")
    print(f"   retningslinje {r['retningslinje_id']}: \"{r['retningslinje_sitat']}\"")
    print(f"   fasit: NBIM stemte {f['nbim_vote_raw']} (mot styret {f['against_board'][:1]})"
          + (f"  NBIMs begrunnelse: {f['rationale_text'][:160]}" if f.get("rationale_text") else ""))
    print()
    if (r["id"], i) != MANUS[k]:
        avvik.append(f"{k}: fila har {r['id']} linje {i}, manuset sier {MANUS[k][0]} linje {MANUS[k][1]}")
if avvik:
    print("AVVIK FRA MANUS (bytt tekst i DEMO_MANUS.md, ikke sakene):"); [print("  " + a) for a in avvik]
else:
    print("MANUS OK: samme tre saker som DEMO_MANUS.md (linje 15 / 89 / 39)")
