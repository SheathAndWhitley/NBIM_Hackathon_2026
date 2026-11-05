# Case 1 (#2526, ordre #262): hybridløsningen kalles ikke lenger NBIMs

Zipen `state/opplastet/20261105_155545_NBIM_Hackathon_2026-main_1_.zip` er en løsning teamet laget utenom landsbyen, ikke fra NBIM. Rettet opphavet i 8 filer. Tallene er uendret.

- `c1/leveranse/JURY_SPORSMAL.md`: svar 3, 13 (overskrift og tekst), 16, 17 og 19. Svar 19 sa «fra et offentlig repo». Det var også feil og er rettet.
- `c1/leveranse/NESTE_VERSJON.md` tiltak 4: «NBIMs eget repo», «NBIM-repoet juryen lastet opp» og «repoets …» er nå «hybridløsningen».
- `levering/JURYSVAR.md` svar 3: «NBIMs egen presedensregel i det opplastede repoet» er nå «presedensregelen i teamets parallelle hybridløsning (… ikke fra NBIM)».
- `kilder/LESMEG.md`, `kilder/c1_nbim_repo_sammenligning.md`, `kilder/c1_nbim_repo_sammenligning_dom.md`: overskriftene er rettet, og det står en merknad om at «repoet» betyr teamets løsning og at «nbim_repo» i filnavnet er historisk. Filnavnene er beholdt.
- `kilder/c1_personnokkel_rullende.md`, `kilder/c1_personnokkel_dom.md`: «repoets prev_same_person» er rettet.
- Frosne filer (JURY.md o.l.) er ikke rørt. Ingen av dem hadde disse formuleringene.

Aksept: akseptgrepet gir 0 treff utenom filnavn i leveranse og levering. Tallvakt: 169 påstander, 0 avvik. `frys_fasit_1600.sha256` er regenerert (137 filer), og bare de 8 filene over fikk ny sha. `pakk_jury.sh` ga utgang 0 med egne byggemapper (/tmp/smed4_*), så #2514 ikke ble forstyrret.
Commit a29ea91. Gjenstår: «repoet» i resten av pakka betyr vår egen rotmappe og er riktig. Skriptet: `arbeid/oppgave_2526/rett.py`.

**Merk for smed (#2531) og #2519:** commit a29ea91 tok også med avsnittet «Samme kombinasjon rullet til 2024» i NESTE_VERSJON.md, som sto ulagret i fila. Teksten er urørt, bare committet tidligere. frys_fasit-sha for NESTE_VERSJON inkluderer derfor avsnittet. `kilder/c1_v2_rullende_2024.md`, som avsnittet peker på, er ikke med i min commit.
