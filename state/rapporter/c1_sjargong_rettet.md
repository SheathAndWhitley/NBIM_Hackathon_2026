# Case 1: interne #-numre og pekere ut av pakka fjernet (sak 2435)

Gjelder pkt. 7 og 8 i c1_jurylesning_status.md, bare for leveranse/JURY.md, JURY_SPORSMAL.md og NESTE_VERSJON.md.
Demo.sh og demo_utskrift.txt er ikke rørt (smed2 kjører demoen). Tall er ikke endret.

- Regler som i mekanisk.py fra sak 2281: «#NNNN» → «sak NNNN», «smed #N»/«dommer #N» → «kontrollagenten», «forsøk #N» → «forsøk N».
- `state/rapporter/X.md` → `kilder/X.md` når kopien finnes (c1_falske_mot, c1_feil_stabilitet), ellers `landsbyrapport:X.md`
  (konvensjonen i kilder/LESMEG.md). `arbeid/oppgave_N/` → `<arbeidsmappe>/oppgave_N/`.
- Nye kopier i kilder/ (pkt. 8): c1_offline_kaldstart.md og c1_beslutning_nyeste_historikk.md, med de samme omskrivningene.
- Linjer endret: JURY 1, JURY_SPORSMAL 3, NESTE_VERSJON 20. Før-kopier: arbeid/oppgave_2435/.
- NESTE_VERSJON:21: «Dom #2366» → «Kontrollagentens dom». Som «sak 2366» ble nummeret lest som et tall uten kilde, og tallsjekken ble rød.

Akseptkrav:
- `grep -nE '#[0-9]{3,}|state/rapporter|arbeid/oppgave_'` i de tre filene gir 0 treff.
- sluttsjekk.sh (med prøvefrys /tmp/c1_frys_2435.json, kl. 15.50) er GRØNN med HOVEDTALL 0.476190. Tallsjekken finner 0 tall uten kilde.
- Merk: /tmp/c1_sluttsjekk deles. To kjøringer krasjet (pandas/scipy dlopen) fordi andre agenter kjørte sluttsjekk samtidig. Det er ikke en feil i pakka.
- LESMEG.md i kilder/ nevner ikke de to nye kopiene ennå. Det må legges til hvis noen vil ha en fullstendig liste.
