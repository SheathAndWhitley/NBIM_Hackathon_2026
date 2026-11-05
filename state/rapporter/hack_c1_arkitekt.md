# Case 1 leveranseskjelett (#1951, arkitekt): make -> hent, split, modell, måler, motstand, rapport

Mappe: `arbeid/hack/c1/leveranse/` (pluss `arbeid/hack/c1/Makefile`). Arbeid er gitignorert, så det er ingen commit; filene ligger på disk.

| Fil | Hva |
|---|---|
| `run.sh` (kalles av `make` i c1/) | 1 `hent_votes.py --cik` -> 1b `maaler.py split` -> 2 `modell.py` -> sjekk sporlogg -> 3 `maaler.py baseline` + `maaler.py ut/pred.csv` -> 4 `motstand.py` -> 5 `rapport.py`. Stopper med exit 2 og navnet på fila som mangler. Variabler: CIK (standard 1374170 Norges Bank), ANDEL 0.2, TERSKEL 0.6, HOPP_HENT. |
| `sporlogg.py` | `Sporlogg(...).skriv(...)` skriver én jsonl-linje per anbefaling: forslag_id, selskap, motedato, forslag, anbefaling, styret, konfidens, kilde_punkt, kilde_url, begrunnelse, til_menneske, modell, kjoring, tid. Rader uten kilde-punkt eller konfidens i [0,1] avvises. `sporlogg.py sjekk <fil>`. |
| `rapport.py` | Leser målerens tekstutskrift (eller maal.json), motstand.json og sporloggen, og skriver `ut/RESULTAT.md` med tabell, ruting, motstandstest, MOT-kilder og ett eksempel. Felt som mangler blir TODO. |
| `README.md` | ett kall, stegtabell, kontrakt mellom stegene, kilder med URL, AI-bruk, begrensninger |
| `kravrespons.md` | malens tre overskrifter (PDF-en sier «fem», men lister tre), 260 ord, tallene er TODO |
| `jury_svar.md` | utkast til de tre spørsmålene |

**KP: forventet recall 0 for følg-styret, fikk 81 %.** Jeg kjørte `rapport.py` på dommerens testdata (`c1/test/`, 78 forslag). Der fikk «følg styret» MOT presisjon 100 % / recall 81,2 %, fordi styret selv anbefaler MOT på aksjonærforslag. Den fanger 0 av 5 avvik fra styret. Så «baseline har recall 0» stemmer bare for avvik fra styret, ikke for MOT. Jeg har rettet tekstene og lagt avviks-kolonnen inn i rapporten. **Ordføreren og dommeren må bestemme hvilket tall som er hovedtallet.** Jeg anbefaler avvik fra styret: det er den beslutningen agenten avlaster, og her er baselinen 0.

**Det smedene må følge:**
- `modell.py --train data/train.csv --test data/test_input.csv --pred ut/pred.csv --spor ut/anbefalinger.jsonl`
- `pred.csv` har kolonnene `id, anbefaling, konfidens`. Alle anbefalinger skrives med `sporlogg.Sporlogg`.
- `motstand.py --test data/test_input.csv --ut ut/motstand.json` med nøklene `n, fulgte_injeksjon, endret_anbefaling, eksempel`.

**Åpne TODO:**
- Ordføreren låser forvalter: NBIM 1374170 eller Vanguard.
- Speideren skaffer eksakt URL og versjon av NBIMs retningslinjer og verifiserer URL-en til N-PX-spesifikasjonen.
- Pakkeliste/requirements og kjøretid fra kald start: dommer #1952.
