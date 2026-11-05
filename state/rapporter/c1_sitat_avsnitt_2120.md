# Case 1 (#2120, smed2): avsnittsvalget i sitatene er rettet, alle 6 rader fra #2115 er riktige, 63/63 er fortsatt ordrett

**Årsak.** Avsnittet ble valgt med BM25 på nabo-begrunnelsens tekst. NBIM siterer hele seksjonens innledning, så det lengste avsnittet (3.1.3, 6.1.3) vant hver gang. Supermajority og Office Term havnet i tillegg i feil seksjon (6.1) fordi nabo-seksjonen veide 12.

**Endring** i `arbeid/hack/levering/retningslinje_oppslag.py` (prediksjonen er uendret):
1. Innen seksjonen velges **seksjonens første prinsipp** (avsnitt uten «we will»). Et fagbegrep i saken kan peke på et annet prinsipp (pre-emptive → «participate pro rata» = 6.1.2).
2. Anti-takeover-ord i saken (supermajority, poison pill, rights plan, takeover) gir seksjon 6.2.
3. Typeprior: har forslagstypen minst 10 tidligere MOT-begrunnelser og ligger minst 80 % av dem i én seksjon, brukes den seksjonen (ARTICLES → 4.3). Bare år før saken brukes.

**Valgt på val 2025.** Mål: avsnittet står ordrett i NBIMs egen begrunnelse, og om det er det første avsnittet NBIM siterer.
| variant | val 2025 sitert / første | test 2026 sitert / første | seksjon test |
|---|---|---|---|
| før (#2106) | 0,456 / 0,214 | 0,619 / 0,254 | 0,857 |
| bare prinsipp, BM25 | 0,417 / 0,252 | | |
| hele seksjonen etter saksord | 0,087 / 0,029 | | |
| **første prinsipp + fagbegrep (låst)** | **0,592 / 0,534** | **0,762 / 0,635** | **0,889** |
Ærlig: punkt 2 og 3 endrer ingenting på val 2025 (ingen slike saker der). De er valgt ut fra domenet og ARTICLES-historikken (24 av 26 MOT-saker i 4.3 før 2025), ikke fordi val viste en gevinst. Dette er altså ikke bevist på val.

**Akseptkrav.** `python3 arbeid/oppgave_2115/sjekk.py`: ordrett 20/20, id+tekst 20/20, seksjon=fasit 20/20, hele settet ordrett 63/63. 2082048|5 → 6.2.5, 2089598|12 → 6.1.2, 2084790|5, 2087754|5 og 2084301|47 → 3.1.1, 2048411|10 → 4.3.1.
**Filer.** Ny `arbeid/oppgave_2106/test2026_mot.csv` (den gamle ligger i `arbeid/oppgave_2120/test2026_mot_for2120.csv`), skript `arbeid/oppgave_2120/eksp.py`.
**Neste steg.** Agentens svarfil og demoen må genereres på nytt for å få de nye sitatene (#2114/kald start). Stikkprøven bør så gjentas på predikert MOT.
