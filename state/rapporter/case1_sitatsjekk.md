# Case 1: sitatsjekk av smed3s sitatagent v6 (#1991, dommer2)

Kilde: `arbeid/hack/varianter/smed3_utf_sitat/ut/forklaring_v6.jsonl` (1 544 holdout-saker).
Skript: `arbeid/oppgave_1991/sjekk.py` (seed 1991, utvalg i `arbeid/oppgave_1991/utvalg.json`).

## Svar på akseptkravene
| mål | resultat |
|---|---|
| Ordrette sitater, utvalg (30 saker, 12 MOT) | **30/30 = 100 %** |
| Ordrette sitater, alle 1 544 saker (maskinsjekk) | **1 544/1 544 = 100 %**, også ordrett i oppgitt punkt-id |
| Sitatet støtter stemmen klart | **1/30** (Garmin, «other matters … vote against») |
| Støtter delvis/indirekte | 18/30 (17 direktørvalg FOR, Dollar Tree written consent) |
| Støtter ikke, eller er misvisende avkortet | **11/30**, hvorav **10 av 12 MOT** |
| Oppdiktede sitater | **0** |

Ordrett-sjekken er gjort mot `rl/vg_us_2025.txt` og uavhengig mot `rl/sai.txt` (SAI fra SEC, f43193d1.htm). Begge treffer 100 % (normalisert anførselstegn og mellomrom; «…» deler sitatet i biter som sjekkes hver for seg). Det finnes bare **12 ulike sitater** i hele utdataene. 1 314 av 1 544 saker bruker samme sitat (PI uavhengighet ¶1).

## Viktigste funn: kildene er Vanguards, ikke NBIMs
Agenten siterer **Vanguards** *Proxy voting policy for U.S. portfolio companies* (feb 2025). Ingen sitater kommer fra NBIM. Dette stemmer med fasiten, som er Vanguards N-PX. Men delmål #45 på tavla sier «siterer NBIMs retningslinjer», og oppgaveteksten sier «NBIMs dokumenter». Juryteksten og demoen må si **Vanguard**. Ellers er det feilsitering på pakkenivå, selv om hvert sitat er ordrett. Speiderens #1977 (NBIMs egne MOT-begrunnelser) er en annen kilde og kan ikke brukes som belegg for v6 uten ny kobling.

## Feilsiterte eller svakt belagte (ordrette, men støtter ikke stemmen)
1. **E/S-forslag som MOT, 6 av 6 i utvalget** (Lowe's plastrapport, Chevron menneskerettigheter, Walmart AI/arbeidsstyrke, Allstate ESG/DEI-mål, Target pesticider, Digital Realty vannrisiko). Alle 22 MOT på dette punktet i hele settet bruker samme punkt. De siterer `PII / Environmental/social proposals / ¶3` avkortet med «…» rett før setningen *«the funds are more likely to support proposals seeking disclosure of such risks»*. Alle seks forslagene ber om rapport eller opplysninger. Hele avsnittet trekker altså mot FOR, og avkortingen fjerner det. Stemmen er riktig mot fasit, men belegget er misvisende.
2. **Uavhengig styreleder, MOT** (GM ×2, Zimmer Biomet) og **kumulativ stemmegivning, MOT** (Walmart). Begge siterer det generelle innledningsavsnittet `PIV / ¶1` («may generally support proposals … that safeguard shareholder rights»). Det sier ingenting om MOT. Det finnes presise punkter: `PI / Independent board leadership / ¶1` (lederstruktur er styrets skjønn) og `PIV / Board structure and director elections / ¶3` (*«vote against management or shareholder proposals to adopt cumulative voting»*). Totalt står 18 MOT i settet på `PIV / ¶1`.
3. **LyondellBasell, nederlandsk årsregnskap, FOR** på `PIV / ¶1`: et generelt avsnitt uten innhold om saken (svak, ikke feil).
4. **Dollar Tree, written consent, MOT**: sitatet støtter MOT *bare hvis* aksjonærene allerede kan kalle inn til ekstraordinært møte. Agenten sjekker ikke det. Delvis.
5. **Direktørvalg FOR (17)**: «majority … should be independent» er belegg for FOR bare i form av «ingen innvending funnet». Det er akseptabelt som standardbegrunnelse. Fortive (ikke uavhengig) og Comcast/Keurig (ulike aksjeklasser) nevner selv at policyen peker mot MOT, men stemmer FOR fordi fondet sjelden fulgte punktet på train. Det er ærlig skrevet i `grunn`.

## Forslag til smed3 (ordrett ≥ 95 %, så dette gjelder støtte, ikke ordrett)
- Uavhengig leder → `PI / Independent board leadership / ¶1`. Kumulativ stemmegivning → `PIV / Board structure and director elections / ¶3`. `PIV / ¶1` bør bare brukes når ingen spesifikk regel finnes, og da merkes som «generelt».
- E/S ¶3: ikke kutt sitatet før «more likely to support proposals seeking disclosure». Siter heller hele avsnittet, eller både første og siste setning. Skill mellom rapport-/opplysningsforslag (policy heller mot FOR, fondet stemte likevel MOT, altså «policy mot praksis») og mål-/policykrav (siste setning gir MOT). Rapportforslagene bør få lavere konfidens eller vises som praksis-avvik.
- Legg til et automatisk felt `sitat_stotter` i forklaringen (regel peker på et punkt med verbet «vote against/for» i sitatet). Da kan juryen se andelen direkte.
- Bytt «NBIM» til «Vanguard» i alt jury-/demotekst som omtaler sitatagenten.

## Utvalget (30)
MOT (12, alle MOT i fasit): Garmin (klar), GM ×2, Zimmer, Walmart kumulativ (generelt punkt, støtter ikke), Lowe's, Chevron, Walmart AI, Allstate, Target, Digital Realty (E/S avkortet, misvisende), Dollar Tree (delvis).
FOR (18, alle FOR i fasit): 17 direktørvalg (delvis), LyondellBasell (svak).
