# Arkitekt #2821: fem nye Case 1-regler for Name that LLM

Fil: `arbeid/handbok/laerdom_case1.md`. Ingen overlapp med #2811/#2815 eller hack_laerdom_case1.md.
1. Arrangørdata i git: lekket 18:43, rens 19:08 → `git_sperre.py` pre-commit før første commit.
2. Usporede leveransefiler (.gitignore arbeid/ state/, 17:09) → egen repo, frys nekter usporet/ignorert fil.
3. Lekkasje/robusthet etter byttet (18:19–18:20) → port før kandidat teller. Hull funnet: lekkasjesjekk.py bruker `>` på tid, så samme dag slipper gjennom. Smed bør legge til `--tid-strengt`.
4. Retting i arbeidstre, ikke i zip (17:34) → sjekk det som faktisk sendes (`kaggle kernels pull` + diff mot frys-sha).
5. Disk 118 MB ledig 18:50 → mktemp+trap, diskvakt med grense 20 GB under NTL, og intet løp hvis ledig < 2× vekter.
Tilfeldig vinkel er ikke trukket: dette var en ren lese- og skriveoppgave med tidsboks 20 min.
