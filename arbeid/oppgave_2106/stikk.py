"""Stikkprøve 20 MOT-prediksjoner fra agent.csv (seed 2106) med NBIMs faktiske seksjon/begrunnelse ved siden av."""
import sys, pandas as pd
H=pd.read_csv('state/opplastet/20261105_114241_real_votes.csv',low_memory=False)
H['id']=H.meeting_id.astype('Int64').astype(str)+'|'+H.item_no.astype('Int64').astype(str)
A=pd.read_csv(sys.argv[1]); M=A[A.mot_styret==1].merge(H[['id','against_board','rationale_section','rationale_text','proposal_type']],on='id',how='left')
M['fas']=M.rationale_section.fillna('').str.replace('GVG ',''); M['sek']=M.retningslinje_id.str.split().str[1].str.rsplit('.',n=1).str[0]
tp=M[(M.against_board==1)&(M.fas!='')]; print('MOT',len(M),'TP',len(tp),'seksjonstreff TP',round((tp.sek==tp.fas).mean(),3))
S=M.sample(20,random_state=2106); S.to_csv(sys.argv[2],index=False)
for k,(_,r) in enumerate(S.iterrows()): print(f"{k+1}. {r.proposal_type} | {r.proposal_text[:60]} | fasit={r.against_board} {r.fas}\n   {r.retningslinje_id}: {r.retningslinje_sitat[:140]}")
