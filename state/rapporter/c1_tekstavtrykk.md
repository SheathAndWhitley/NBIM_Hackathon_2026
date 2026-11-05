# Case 1: tekstavtrykk i sluttsjekk.sh (#2392)

- Steg 7 lagt inn i `arbeid/hack/levering/sluttsjekk.sh` rett før SLUTTSJEKK GRØNN:
  `echo '>>> 7 tekstavtrykk (info, ikke rødt)'; python3 -I arbeid/hack/c1/tekstavtrykk.py sjekk | tail -8 | sed 's/^/    /'`
- Kan ikke gi rødt: skriptet bruker ikke `set -e`, og pipens utgang er sed sin (0), også når sjekk gir 3 (endret).
- Test: `bash -n` OK. Sjekk alene nå: "TEKSTAVTRYKK: ikke tatt ennå (tas kl. 16.03)", pipe-utgang 0.
  Demo på kopi (lag, endre kravrespons.md, sjekk): viser "ENDRET kravrespons.md endret 15:27:26" og
  "TEKSTAVTRYKK: 1 endret siden avtrykk 15:27", pipe-utgang 0.
- Hele sluttsjekken ble ikke kjørt (tar minutter og bygger kald kopi; dommeren kjører den i #1972).
