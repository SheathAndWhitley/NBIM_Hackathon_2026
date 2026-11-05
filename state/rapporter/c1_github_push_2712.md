# Case 1 (#2712): den lokale repoen er pushet til GitHub-repoen nbim

- Remote: origin = git@github.com:Martinkristofferhansen/nbim.git (egen deploy-nøkkel ~/.config/landsby_nbim/nbim_deploy via core.sshCommand, #274).
- Første push lyktes 18:29:26 (954c045, ny gren main). Det var etter at guden la inn den nye nøkkelen og historikken var squashet (#2730).
- Gjeldende: GitHub main = **948fadde2b503b855985b2ef7058c1a66f738cde** (ls-remote 18:41). Det er lik lokal HEAD, 0 commits foran.
  948fadd er rettingen av BEGRENSNINGER pkt 1 fra #2779, pushet som vanlig fast-forward 13c3b4a..948fadd.
- Hemmelighetsskanning (arbeid/verktoy/c1_hemmelig_skann.sh) på repoen før pushen: 0 funn (rc 0). Ingen fasitfil og ingen pred_miks_h2 i historikken.
  kilder/case1_hvilken_fasit.md er en rapport om hvilken fasit som brukes, ikke selve fasitdataene.
- Ingen --force, ingen annen repo.
- Merk: https://github.com/Martinkristofferhansen/nbim gir 404 anonymt fordi repoen er privat. Guden må gjøre den offentlig før kl. 20; #2772 holder vakt på det.
- Logg: arbeid/oppgave_2712/push.log
