# Case 1 (dom #2513 av #2509): kildepekere i jurytekstene

**Dom: GODKJENT**, med én retting gjort av dommeren (ett ord) og to anmerkninger.

Metode: eget skript `arbeid/oppgave_2513/sjekk.py` (ikke smedens), kjørt mot to fillister: dommer2s kalde stage-tre fra kl. 16:26 (`/tmp/jurystage_c1/c1_stemmeagent`, 128 filer) og `frys_fasit_1600.sha256` (129 filer, = zipen). Utskrifter i `arbeid/oppgave_2513/`.

## 1. Hver fil i kilder/ har peker, og ligger i zipen
- kilder/ har 54 filer. Alle 54 står i frys-fasit-lista. Stage-treet fra 16:26 manglet `dom_2497_figur.md`, fordi den ble committet 16:27 (04b76c0), ett minutt etter byggingen. Ikke et brudd; #2514 bygger på nytt fra HEAD.
- 52 av 54 har peker rett fra en av de fem tekstene (JURY, JURY_SPORSMAL, ERLIG_EVALUERING, BEGRENSNINGER, NESTE_VERSJON).
- Anmerkning A: `kilder/LESMEG.md` pekes bare fra `levering/JURYSVAR.md:3` (den ligger i zipen), ikke fra de fem.
- Anmerkning B: `kilder/tell_trening.txt` pekes bare fra `kilder/LESMEG.md:19`; JURY.md:71 peker på `tell_trening.py` (som lager den). To hopp fra jurytekstene, ikke foreldreløs.

## 2. Hver peker treffer en fil i zipen
Skriptet trakk ut 245 fil-lignende henvisninger fra de fem tekstene + kilder/LESMEG.md.
- 211 treffer en fil i zipen med eksakt sti (etter de vanlige rotene leveranse/, c1/, levering/, state/rapporter/).
- 34 treffer ikke. Alle unntatt én er lovlige: `landsbyrapport:<navn>` (LESMEG.md:7 sier at de er interne), skript merket «i repoet, ikke i zipen» / «i landsbyen» (fremmed.sh, kaldstart.sh, oppgave_2395/*, oppgave_2497/lag_figur.py), utdatafila `agent.csv`, og LESMEG.md:3 sine interne navn.
- **Brudd (rettet):** NESTE_VERSJON.md:47 pekte på `opplastet_20261105_114241_real_votes.md:7` uten `landsbyrapport:`-prefiks (linje 24 har det). Rettet til `landsbyrapport:…`. Ingen tall endret. Fasit-linja for NESTE_VERSJON.md regenerert (eneste diff, 129 filer). Tallvakt mot den kalde kjøringen fra 16:26: 18 filer, 169 påstander, 0 avvik.

## Ærlig rest
Skriptet matcher på sti og rot-gjetting, ikke på at teksten rundt pekeren stemmer med innholdet i fila. #2483 (speideren leser som juryen) dekker det.
