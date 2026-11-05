# NTL-startkommando: sperre + lekkasjeport + diskvakt i én (#2835)

`arbeid/ntl_mal/ntl_start.sh <repo> --data <mappe> --train <f> --test <f> --maal <kol> --tid <kol> [--id <kol>] [--kandidat navn] [--vekt-gb N] [--grense-gb 20]`

Rekkefølge: 1) `install_sperre.sh` og `git_sperre.py sjekk` på det som er staget nå, 2) `ntl_lekkasjeport.py kjor` (--tid-strengt, stempel i state/ntl_port/), 3) `ntl_diskvakt.py sjekk`. Første røde trinn stopper med rød melding. Exit-koden er trinnets nummer (9 = bruksfeil).

Test (tom /tmp-repo, syntetisk train/test på 40/20 rader):
- `bash -n`: grønn.
- Grønn kjøring: exit 0. 600 fingeravtrykk, port GRØNN (0 av 20 test-rader i train, all train før første testdag), disk 37,8 GB ledig mot krav 20 GB.
- Rød kjøring med `train.csv` staget: exit 1, «filnavn: train.csv» og «40 datalinjer ordrett».
- Teststempelet er slettet etterpå, og /tmp er ryddet med trap.

Ikke testet: rød på trinn 2 og 3 gjennom wrapperen. Begge er testet hver for seg i #2826/#2825. Case 1-filer er ikke rørt.
Bruk kl. 20:05: se arbeid/handbok/laerdom_case1.md, «Startkommando kl. 20:05».
