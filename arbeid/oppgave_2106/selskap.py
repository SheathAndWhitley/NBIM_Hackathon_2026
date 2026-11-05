import sys; sys.argv=[sys.argv[0]]
exec(open('arbeid/oppgave_2106/evaluer.py').read().split('if __name__')[0])
B = H[(H.against_board == 1) & H.rationale_section.fillna('').str.startswith('GVG')].sort_values('meeting_date')
for år in (2025, 2026):
    D = kjor(år, 0, 12, 0, True)
    R = H[(H.year == år) & (H.against_board == 1) & H.rationale_section.fillna('').str.startswith('GVG')].reset_index(drop=True)
    ut = {k: [] for k in ('person', 'selskap', 'kombinert')}
    for (_, r), (_, d) in zip(R.iterrows(), D.iterrows()):
        f = B[(B.year < år) & (B.company_id == r.company_id)]
        p = f[f.proposal_text == r.proposal_text]
        sp = p.rationale_section.iloc[-1].split()[1] if len(p) else None
        ss = f[f.proposal_type == r.proposal_type].rationale_section.iloc[-1].split()[1] if len(f[f.proposal_type == r.proposal_type]) else None
        ut['person'].append((sp, d.fasit)); ut['selskap'].append((ss, d.fasit))
        ut['kombinert'].append((sp or ss or d.sek, d.fasit)); ut.setdefault('person_ellers_laast', []).append((sp or d.sek, d.fasit))
    for k, v in ut.items():
        dekk = [x for x in v if x[0]]
        print(år, k, 'dekning', len(dekk), '/', len(v), 'treff der dekket', round(sum(a == b for a, b in dekk) / max(len(dekk), 1), 3), 'treff totalt', round(sum(a == b for a, b in v) / len(v), 3))
    print(år, 'låst nå', round((D.sek == D.fasit).mean(), 3))
