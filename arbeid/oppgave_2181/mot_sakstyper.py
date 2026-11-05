"""#2181: MOT mot styret i test 2026 (samme definisjon som måler v3 --score mot) fordelt på forslagsstiller og sakstype,
og hvor mange av dem den frosne agenten (#2044, maskin alene) flagget. Skriver tabellen i BESLUTNINGSSTOTTE.md.
Kjør fra landsbymappen: python3 -I arbeid/oppgave_2181/mot_sakstyper.py"""
import csv, collections
F = "state/opplastet/20261105_114241_real_votes.csv"
SVAR = "arbeid/hack/levering/kjor_agent_real_maskin_alene.csv"
flagg = {r["id"] for r in csv.DictReader(open(SVAR)) if r["anbefaling"] == "1"}
rid = lambda r: f"{r['meeting_id']}|{r['item_no']}"
rr = [r for r in csv.DictReader(open(F, encoding="utf-8", newline=""))
      if r["injection_flag"] != "1" and r["year"] == "2026" and r["against_board"] != ""]
er_mot = lambda r: r["nbim_vote"] == "MOT" and r["against_board"] == "1.0"
mot = [r for r in rr if er_mot(r)]
print(f"test 2026: {len(rr)} saker, {len(mot)} MOT mot styret, agenten fant {sum(rid(r) in flagg for r in mot)}")
NAVN = {"DIRECTOR_ELECTION": "styrevalg", "AUDITOR": "revisor", "OTHER_BUSINESS": "annen sak / eventuelt",
        "OTHER_MGMT": "andre styresaker"}
def gruppe(r):
    if r["proponent"] != "Management": return f"{NAVN.get(r['proposal_type'], 'andre')} (aksjonærforslag)"
    return f"{NAVN.get(r['proposal_type'], 'øvrige')} (styret)"
c = collections.defaultdict(lambda: [0, 0, 0])
for r in rr:
    g = c[gruppe(r)]; g[0] += 1; g[1] += er_mot(r); g[2] += er_mot(r) and rid(r) in flagg
print("\n| sakstype (forslag fra) | MOT | saker | MOT-andel | agenten fant |\n|---|---|---|---|---|")
for k, (n, m, f) in sorted(c.items(), key=lambda t: -t[1][1]):
    print(f"| {k} | {m} | {n} | {100*m/n:.1f} % | {f} |".replace(".", ","))
print("\nøvrige (styret), MOT per type:", collections.Counter(r["proposal_type"] for r in mot
      if gruppe(r) == "øvrige (styret)").most_common())
print("forslagsstiller:", collections.Counter(r["proponent"] for r in mot).most_common(),
      "av saker:", collections.Counter(r["proponent"] for r in rr).most_common())
print("land (MOT):", collections.Counter(r["country"] for r in mot).most_common(5))
print("selskaper med flest MOT:", collections.Counter(r["company"] for r in mot).most_common(5))
