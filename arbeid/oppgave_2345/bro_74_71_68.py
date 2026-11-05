"""#2345 H9: broen 74 / 71 / 68 MOT-flagg på test 2026 (frossen #2044, maskin alene).
Leser agentens svarfil og real_votes; teller som måler v3 (maaler_offisiell_v3.py:88-101)."""
import csv, sys
svar = sys.argv[1] if len(sys.argv) > 1 else "arbeid/hack/levering/kjor_agent_real_maskin_alene.csv"
data = sys.argv[2] if len(sys.argv) > 2 else "state/opplastet/20261105_114241_real_votes.csv"
fas = {f"{r['meeting_id']}|{r['item_no']}": r for r in csv.DictReader(open(data, encoding="utf-8-sig"))}
S = list(csv.DictReader(open(svar, encoding="utf-8-sig")))
flagg = [s for s in S if s["anbefaling"] == "1"]
print(f"svar: {len(S)} rader, avviksflagg (anbefaling=1): {len(flagg)}")
med = [s for s in flagg if s["id"] in fas and fas[s["id"]]["against_board"] != ""]
print(f"  uten fasit (against_board tom eller id ukjent): {len(flagg)-len(med)}")
print(f"  med fasit: {len(med)}")
styret_mot = [s for s in med if (fas[s['id']]['mgmt_rec'] or 'FOR') == 'MOT']
print(f"  av dem styret sa MOT (avvik = agenten sier FOR, ikke MOT-flagg i v3): {len(styret_mot)}")
mot = [s for s in med if s not in styret_mot]
print(f"  MOT-flagg i v3 (MOT mot styret): {len(mot)}")
from collections import Counter
print("  nbim_vote på MOT-flaggene:", dict(Counter(fas[s['id']]['nbim_vote'] for s in mot)))
print("  nbim_vote på avviksflagg med fasit:", dict(Counter(fas[s['id']]['nbim_vote'] for s in med)))
print("  AVSTÅ/annet-avvik blant flaggene:", [(s['id'], fas[s['id']]['nbim_vote'], fas[s['id']]['mgmt_rec']) for s in med if fas[s['id']]['against_board']=='1.0' and fas[s['id']]['nbim_vote']!='MOT'])
for s in styret_mot: f = fas[s['id']]; print("   styret MOT:", s['id'], f['company'], '| nbim', f['nbim_vote'], '| against_board', f['against_board'])
