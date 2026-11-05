# Dom #2628: GitHub-synken går av seg selv hvert 10. min

GRØNN (dommer2, 17:31): launchd no.landsby.githubsynk (StartInterval 600, exit 0, 3 kjøringer) committet 17:09:00 og 17:19:02 (600 s mellom, siste etter 17:11) og kjørte 17:29 «ingen endringer» fordi smedens manuelle synk 17:28 alt var inne; loggen viser «3/4 hemmelighetsskanning: 0 funn» hver gang; `git remote -v` er tom og ingen push finnes; `git ls-files` (147 filer) = HVITLISTE i arbeid/verktoy/github_synk.sh, uten real_votes/real_test_input/real_val_input, nøkler eller state utenom de seks hvitlista rapportene.

Merknad til #2611 (publisering): arbeid/oppgave_2044/pred_miks_h2.csv står på hvitlista og har kolonnen `y` (fasit for 1 539 rader, uten tekst). Det er avledet av arrangørens casedata; dommer i #2611 avgjør om kolonnen skal strykes før push.
