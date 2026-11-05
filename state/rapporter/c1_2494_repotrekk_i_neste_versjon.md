# Case 1 (#2494): repotrekk-funnet fra #2490 skrevet inn i NESTE_VERSJON.md

- Først gjenskapt uavhengig, med offisiell måler v3 `--score mot` på `arbeid/oppgave_2490/*_test.csv`:
  frossen 0,476190, + prev_same_person 0,525424, + alle fire repotrekk 0,512000. KI (diff_ki.py, 2000 trekk):
  +0,049 [+0,016; +0,090] og +0,036 [−0,008; +0,085]. Val 2025 for person: 0,536 (person.log). Alt stemmer med #2490.
- Lagt inn som et punkt sist under tiltak 4 i `arbeid/hack/c1/leveranse/NESTE_VERSJON.md`. Alle tall er merket
  «ikke hovedtall». Kilde: `landsbyrapport:c1_repotrekk_neste_versjon.md`. Ærlig: målt etter frys, testen er sett og
  regexen er laget med 2026 synlig. Derfor ikke noe bytte, bare første test i neste versjon.
- Tallvakta: 18 filer, 169 påstander, 0 avvik, OK. Fila står ikke i frysfasiten (state/c1_frys.json), og ingen frosne filer er rørt.
- Ikke committet: arkitekten (#2481) har ucommittede endringer i samme fil (tiltak 4). En commit nå ville tatt med
  arbeidet deres halvferdig. Arkitekten committer begge deler samlet.
