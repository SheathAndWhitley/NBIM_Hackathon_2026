# Case 1: DEMO_MANUS.md rettet for jury-zipen (#2450, dom #2447), variant (a)

- Linje 5 sier nå hvordan demoen kjøres fra zipen: `sh KJOR.sh` i roten, så `sh arbeid/hack/c1/leveranse/demo.sh` og `python3 -I arbeid/hack/c1/vis_manussaker.py ut/agent.csv`. Repo-veien (fremmed.sh /tmp/c1_kald) står som alternativ.
- Linje 4, 6, 7: pekere til `arbeid/oppgave_2260/…` og `arbeid/oppgave_2267/maaling.txt` erstattet med «i repoet (sak NNNN, ikke i zipen)». Alle #NNNN byttet til «sak NNNN». Ingen tall endret.
- Akseptkrav: `grep -nE '#[0-9]{3,}|arbeid/oppgave_'` gir 0 treff, både i repoet og i DEMO_MANUS.md inne i den nye zipen.
- sluttsjekk.sh GRØNN (160 s, HOVEDTALL F1 MOT 0.476190, ZIPTEST GRØNN), kjørt med prøvefrys `C1_FRYS=/tmp/...` fordi ekte frys først tas kl. 16 (uten den: rød på frysvakt, som ventet). Prøvefrysfila er slettet; state/c1_frys.json ikke rørt.
- Commit 1cbf77b: DEMO_MANUS.md + demo_utskrift.txt (bare datolinje). pakk_jury.sh ikke rørt (smed2 #2448 eier den; den uncommittede endringen er hans).
- git status arbeid/hack: mine filer er rene; pakk_jury.sh står fortsatt som endret, og det er smed2 sitt arbeid etter ce183ff (#2448), ikke rørt av meg.
