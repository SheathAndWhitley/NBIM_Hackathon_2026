# Dom #2455: stikkprøve av speiderens sortering av 202 pekere (#2449)

**GRØNN med én retting.** Feilrate i stikkprøven på bøtte-spørsmålet («burde vært b»): 1 av 30 (3 %).
Bøtte a: 0 av 20. Bøtte c: 1 av 10. De 3 filene i bøtte b ligger i zipen og har ingen `~`.

Grunnlag: ny zip bygd med `pakk_jury.sh` kl. 15:58 i `/tmp/d2455.cPRb` (113 filer), trekk med seed 2455
(`/tmp/d2455_sample_a.txt`, `_c.txt`). Hver peker lest i kontekst i zipen og slått opp etter filnavn i zipen.

## Funnet som må rettes (c → b)
`NESTE_VERSJON.md:58` viser til `landsbyrapport:speider_2399_recall_budsjett.md` for tallene
«F1 0,517 ved k=50, 30 av 66 MOT i topp 50, presisjon 0,60, 0,03 recall ved tilfeldig utvalg».
Ingen av de tre k=50-tallene finnes andre steder i zipen (`c1_menneske_terskel.md:15` har «30 av 66» for
standardbåndet, ikke for k=50). Dette er nøyaktig samme type peker som speideren satte i bøtte b for
`c1_feil_per_gruppe.md`: et tall i jurytekst som bygger på en intern rapport. Fila finnes,
er 1,6 kB, har ingen `~` og tallene står på linje 16 og 23.
Retting: legg `state/rapporter/speider_2399_recall_budsjett.md` i kopier-linja for bøtte b (#2457), og gi
pekeren på linje 58 full sti. Alternativ: stryk de tre tallene fra setningen.

## Småfeil i beskrivelsene (bøtta er riktig, teksten upresis)
- `c1_robusthet_reprod.md:19` `fem_nye.py`: speideren skriver «finnes ikke i repo: stryk pekeren». Fila finnes
  (`arbeid/oppgave_2395/fem_nye.py`, laget 15:24, før rapporten 15:52). Bøtte c står: tallet «fem» er ikke i JURY.md.
- `c1_falske_mot.md:3` `real_votes.csv`: speideren sier «under data_*/». Den ligger som
  `state/opplastet/20261105_114241_real_votes.csv`. Fila er i zipen, så a er riktig.
- `c1_sitatkilder.md:5` `agent.csv`: linja har full sti `arbeid/oppgave_2106/agent.csv`, som ikke er i zipen.
  Det er en intern peker (c), ikke «utfil som lages ved kjøring». Ingen tall i JURY.md hviler på den.

## Resten av stikkprøven
- Bøtte a, 17 av 20 rent riktige: `train.py` (4, i zip under oppgave_2044), `real_val_input.csv` (i zip under
  data_off), utfiler fra kjøring (`agent.csv`, `ut/tabell.md`, `full.log`, `pred_maaler_kald.csv`, `kjor_tomt.log`,
  `_pred_uten_ruting.csv`, `K/rv.csv`, `resultat.json`), plassholdere (`saker.csv`) og `npx_votes.csv` (ikke brukt).
  `resultat.json` i `c1_injeksjon_hoflig.md:30` hører til den interne driveren `inj.py`, men vakta selv
  (`arbeid/hack/levering/injeksjon_hoflig.py`) og motstandstesten (`spor_npx/motstand_inj.py`) er i zipen,
  og tallene JURY.md bruker (pkt. 11) kommer fra `kilder/c1_injeksjon_etter_2205.md`.
- Bøtte c, 9 av 10 riktige: 6 rader fra `spor_npx/utkast_1100/` er borte, mappa er ute av den nye zipen (0 treff).
  `hist_regel.py` (`ERLIG_EVALUERING.md:48`) er alt rettet (#2454). `c1_neste_steg.md:63` handler om rekkefølge,
  ikke tall. `fem_nye.py` se over.

## Bøtte b
`c1_feil_per_gruppe.md`, `arkitekt_c1_neste_versjon.md`, `feil_val2025.md`: alle tre i den nye zipen
(state/rapporter/ og arbeid/oppgave_2274/), 0 treff på `~` både i zipen og i kildene.
