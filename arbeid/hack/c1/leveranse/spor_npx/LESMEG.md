# Brukes bare av SPOR=npx (gammel N-PX-grunnlinje, ikke hovedtallet)

Filene her hører til den gamle veien der vi selv hentet NBIMs N-PX-stemmer fra SEC (før arrangøren leverte NBIMs egne stemmer 05.11).
Hovedveien (`bash arbeid/hack/c1/leveranse/kjor.sh` uten SPOR) bruker dem ikke.
- `motstand_inj.py`, `resultat.py`: kalles av `SPOR=npx bash arbeid/hack/c1/leveranse/kjor.sh`.
- `run.sh`, `rapport.py`, `sporlogg.py`, `utkast_1100/`: eldre utkast fra kl. 11 (make i c1/).

Agentens ekte sporbarhet er `agent.csv` og `KJORING.txt` fra hovedveien, ikke `sporlogg.py`.
