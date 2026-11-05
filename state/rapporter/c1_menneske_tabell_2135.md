# Case 1: én tabell for «send til menneske» i README, BESLUTNINGSSTOTTE og JURYSVAR (smed3 #2135)

Jurylesningen pkt. 5 er rettet. Modellen er ikke rørt.

- **Ny felles tabell** (test 2026, #2044, faktisk standardkjøring #2132, positiv klasse **MOT mot styret, 58 av 1539**):
  - standard (bånd [0,15; 0,85) + ukjent selskap/type, injeksjon, datafeil, MOT uten sitat): **183 av 1539 (11,9 %)** til menneske, 32 av 58 MOT blant dem.
  - Maskin alene: P 0,44 / R 0,52 / F1 0,476 (TP 30 FP 38 FN 28). Rutingen endrer ikke svarene.
  - Maskin + menneske, **øvre grense, antar riktig menneskelig avgjørelse**: P 1,00 / R 0,71 / F1 0,828. Gulv (mennesket følger styret): F1 0,269.
  - Bare båndet: 122 (7,9 %), 27 MOT, øvre grense F1 0,779.
  - Alle 38 falske flagg havner i sonen. De 9 flaggene utenfor sonen er alle ekte. 17 MOT ser ingen (P(MOT) under 0,15).
- Kommandoen står under tabellen i alle tre filer: `python3 -I arbeid/hack/c1/menneske_tabell.py arbeid/oppgave_2132/agent.csv` (ny, bare stdlib, samme definisjon som måler v3 `--score mot`).
- **README:** N-PX-rutingtabellen (9,6 %, 0,572/0,629) er flyttet til `arbeid/hack/c1/arkiv/ruting_npx_tabell.md`. Den er lenket fra README. 228/14,4 % er byttet til 188/183 (11,9 %).
- **BESLUTNINGSSTOTTE:** den gamle tabellen med tre oppsett (13,3 per 100, 65 %, talt på 66 avvik) er erstattet. I hverdagen leser forvalteren 12,5 av 100 saker, finner inntil 71 % av MOT og bruker rundt 62 t (en antagelse). Forbehold og feilavsnitt er skrevet om på 58 MOT. «Vid» og «høy presisjon» er tatt ut fordi de ble målt på en annen definisjon.
- **JURYSVAR 7:** svaret bruker nå hovedmodellen med samme tabell. N-PX-tallene står bare som en merknad med lenke til arkivet.
- **Verifisert:** tabellraden har samme md5 i alle tre filene og i skriptets utskrift. `sh arbeid/hack/levering/fremmed.sh /tmp/fremmed_2135` fra kald kopi ga samme standardrad og F1 MOT 0,4762, og tallvakta var grønn (129 påstander, 0 avvik).
- **Ikke målt:** hvor mye lesing et bredere bånd koster på MOT (58).
