# Case 1 (#2487): demo-svar på «NBIM-repoet slår dere, hvorfor ikke bytte?»

Nytt pkt. 13 i `arbeid/hack/c1/leveranse/JURY_SPORSMAL.md` (overskriften er endret til «tretten»), fire setninger:
frysen kl. 16 står (å bytte etter å ha sett tall på test er å velge på test); 0,476 mot 0,515 (presedens), 0,523 (hybrid, deres splitt) og 0,545 (hybrid, vår splitt); bare 0,545 er klart bedre, +0,069 KI [+0,007; +0,133]; vår PR-AUC 0,525 er best (0,318 / 0,413), så gapet er presedensregel og terskel; neste versjon = presedens først på vår rangering, terskel valgt på val.
Alle tall er fra `c1_nbim_repo_sammenligning_dom.md` og tabellen den godkjenner. Jeg strøk en påstand om at frysen kom før repoet, fordi den ikke har noen kilde.

`arbeid/hack/c1/DEMO_MANUS.md`: kort peker til pkt. 13 under tallkildene, utenfor 2:50-manuset. Linje 63 (fra sak 1975) ga tallvakt-avvik fordi «0,476190» sto med seks desimaler. Den er nå skrevet «0,4762 (0.476190)», og tallet er uendret.

Akseptkrav: tallvakta 0 avvik på de 2 endrede filene (11 påstander) og 0 avvik på hele pakka (18 filer, 169 påstander). `frys_fasit_1600.sha256` er regenerert (117 filer, bare de 2 tekstfilene er endret). Ingen modellfil er rørt.
