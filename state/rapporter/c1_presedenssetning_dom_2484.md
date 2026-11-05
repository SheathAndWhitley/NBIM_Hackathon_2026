# Dom #2484: presedenssetningen i jurysvaret (#2480) stemmer med dom #2465, med én upresis ordlyd

Sjekket 2026-11-05 16:20–16:27 av dommer2: `arbeid/hack/levering/JURYSVAR.md` pkt. 5 og `arbeid/hack/c1/leveranse/JURY_SPORSMAL.md` pkt. 3 (commit 5cd3e18) mot `state/rapporter/c1_nbim_repo_sammenligning_dom.md` og repoets `ballot.py`.

## Tall, KI og splitt: GODKJENT
| påstand i jurysvaret | dommen (#2465) | OK |
|---|---|---|
| presedensregel 0,515, test 2026, vår måler | 0,514851 | ja |
| +0,04 over frossen 0,476 | +0,039 | ja (avrundet) |
| KI [−0,05; +0,13], innenfor støyen | [−0,051; +0,126] | ja |
| hybrid på vår splitt 0,545, +0,069 [+0,007; +0,133], reelt forsprang | 0,545455, +0,069 [+0,007; +0,133], B<A 1 % | ja |
| PR-AUC 0,525 mot 0,318 (presedens) og 0,413 (hybrid) | tabellen i kilderapporten, bekreftet i dommen | ja |
| «avvik teller også AVSTÅ» | presisering 1 i dommen | ja |
| modellen ikke endret etter frysen | frys_diff: bare tekstfiler | ja |

Splittene blandes ikke: begge tall er merket test 2026/vår splitt. Kildene er kopiert inn i zipen (`kilder/c1_nbim_repo_sammenligning*.md`); tallene i kopien er like originalen, bare stier er skrevet om.

Tallvakta på de tre endrede filene: 3 filer, 26 påstander, 0 avvik. `frys_diff.sh --kilde`: ett avvik, `NESTE_VERSJON.md`, som er smed2s pågående #2498 (ikke #2480).

## Ordlyd: én upresishet, må rettes (tekst, ikke tall)
Jurysvaret sier «avvik hvis samme direktør avvek sist, ellers hvis samme sakstekst avvek sist». Koden er `prev_same_person.fillna(prev_same_item)` (`ballot.py:158`): direktørens siste stemme brukes når direktøren er kjent fra før, og bare når den mangler faller regelen tilbake på sakstekst. Er direktøren kjent og avvek IKKE sist, blir svaret «ikke avvik» selv om samme sakstekst avvek sist. «Ellers» i jurysvaret kan leses som «eller», som er akkurat det dom #2465 advarte mot. Smed2s egen rapport (#2480) har riktig ordlyd («samme direktør hvis kjent, ellers samme sakstekst»); den kom ikke med inn i jurytekstene.

Foreslått erstatning begge steder: «avvik hvis siste stemme på samme direktør var et avvik; er direktøren ukjent fra før, brukes siste stemme på samme sakstekst» (avvik teller også AVSTÅ).

Ingen tallendring. Oppgave tilbake til smed2 lagt på tavla.
