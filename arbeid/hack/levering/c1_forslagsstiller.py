"""MOT mot styret i test 2026 fordelt på forslagsstiller, og agentens treff (speider #2172/#2183).
Kjør fra arbeid/hack: python3 -I levering/c1_forslagsstiller.py   (leser bare CASE/ og levering/)"""
import csv, collections
rv = {f"{r['meeting_id']}|{r['item_no']}": r for r in csv.DictReader(open('CASE/20261105_114241_real_votes.csv'))}
mot, treff = collections.Counter(), collections.Counter()
for p in csv.DictReader(open('levering/kjor_agent_real_pred_maaler.csv')):
    r = rv[p['id']]
    if r['nbim_vote'] == 'MOT' and r['mgmt_rec'] == 'FOR':
        mot[r['proponent']] += 1
        treff[r['proponent']] += p['anbefaling'] == '1'
for k in sorted(mot):
    print(f"{k}: {mot[k]} MOT mot styret, agenten fant {treff[k]}")
print(f"sum: {sum(mot.values())} MOT mot styret, agenten fant {sum(treff.values())}")
