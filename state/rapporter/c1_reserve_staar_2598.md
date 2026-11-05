# Case 1 (#2598): STÅR-reserve av README og kravrespons klar i arbeid/hack/c1/reserve_staar/

Hva: `README.md` og `kravrespons.md` som sier frossen 0,476 igjen, med byttedommen sluttført ærlig:
«kontrollagenten dømte BYTT kl. 17:02 på vilkår om grønn pakke innen 18:45. Kandidaten besto regelen, men pakken
med repo4 ble ikke grønn i tide, så den frosne agenten står med 0,476.» Bygget av `arbeid/oppgave_2598/lag_staar.py`
fra BYTT-utgaven i `c1/leveranse/`; hver erstatning må finnes nøyaktig én gang, og skriptet stopper om BYTT-tall
står igjen utenfor dom-linjene.

Sjekk av akseptkravet:
- diff BYTT -> STÅR: README 8 blokker (hovedtall-boksen 3 linjer, dom-linja, detaljer 3 linjer, kald-start-linja,
  utskriftslinja, kodeblokken, datakilde-overskriften), kravrespons 3 linjer (hva vi bygde, verifisering, videre).
  Alle er tall eller dommesetningen; ingen andre endringer.
- diff frossen git-tekst (5442ccd README, acdd689 kravrespons) -> STÅR: bare dom-linja. Dvs. tallene er identiske
  med teksten før bytt_tall.py.
- levering/ og leveranse/ er ikke rørt.

Funn underveis (ikke rettet, utenfor oppgaven): i BYTT-utgaven av `c1/leveranse/kravrespons.md` linje 10 står
«0,512 ligger under målet vårt på 0,5». Det er feil for repo4; setningen var riktig for 0,476. Den som sluttfører BYTT
bør rette den (f.eks. «0,512 så vidt over målet vårt på 0,5»). Sjekk også `levering/`-kopien.

Bruk: se `arbeid/hack/c1/reserve_staar/LES.md`.
