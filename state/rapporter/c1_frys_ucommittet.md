# Case 1: ucommitterte endringer i pakka før frysen (dom #2447, 05.11 kl. 15:55)

Status kl. 15:48 var 4 ucommitterte filer. Kl. 15:48:40 committet smed2 tre av dem i `acaaff7`
(#2442). Dommen gjelder innholdet, uansett hvem som trykket commit.

| fil | hører til | ferdig? | dom |
|---|---|---|---|
| `c1/leveranse/demo.sh` | smed2 #2442 (done) | ja, committet i acaaff7. Finner pakkeroten når fremmed.sh mangler, stopper med klar melding uten KJOR.sh. Smed2 oppgir testet fra zip (KJOR.sh 0.476190, tallvakt grønn) | GRØNN |
| `levering/pakk_jury.sh` | smed2 #2442 (done) | ja, committet. Legger `c1/vis_manussaker.py` og `c1/DEMO_MANUS.md` i zipen; begge finnes og ligger i siste zip (15:49) | GRØNN, men se merknad A |
| `levering/JURY_README.md` | smed3 #2439 (85 %), ikke arkitekt #2435 | ja. Kolonnetabellen, AVSTÅ-rettingen og 0,919 rå vs 0,191 kalibrert, akkurat det #2439 ba om. Tallene stemmer med BESLUTNINGSSTOTTE.md linje 38/81; «BEGRENSNINGER.md pkt. 6» finnes og ligger i zipen. Ble sveipet med i smed2s commit (feil commit-melding, bare kosmetisk) | GRØNN |
| `c1/leveranse/demo_utskrift.txt` | smed2 (demo-kjøring 15:28 fra repoet) | én linje: dato og kopi-sti. Ingen tall endret. Ikke committet; zipen tar arbeidskopien, så fasiten (#2445) må hashe arbeidskopien, ikke HEAD | GRØNN (bør committes av smed2 før 16:00, ellers står den som avvik mot HEAD i frysdommen) |

Ingen halvferdig kode går inn i frysen. Arkitekt #2435 har ingenting ucommittet under arbeid/hack ennå.

## Merknad A (til smed2 og arkitekt, ikke RØD for frysen, men RØD for jurylesingen)
`c1/DEMO_MANUS.md` er nå med i zipen, og linje 5 sier at «fremmed.sh, vis_manussaker.py og dette
manuset er ikke med i jury-zipen, så demo.sh virker ikke derfra (#2433)». Det er nå feil. Fila har
også 6 interne #-numre og peker på `arbeid/oppgave_2260/full/agent.csv`, som ikke er i zipen.
Arkitektens #2435 dekker bare JURY, JURY_SPORSMAL og NESTE_VERSJON. Lagt som oppgave til smed2:
rett linje 5 (og helst numrene) eller ta DEMO_MANUS.md ut av pakk_jury.sh igjen. Bare tekst, ikke tall.
