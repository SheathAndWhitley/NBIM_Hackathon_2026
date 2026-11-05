# Case 1: muntlige manus v2 etter jury-rettelsene (#2641)

Nye filer (smed2 legger BYTT i `c1/leveranse/MUNTLIG.md`, smed3 legger STÅR i `c1/reserve_staar/MUNTLIG.md`):
- `state/rapporter/arkitekt_c1_muntlig_v2.md` (BYTT): 397 talte ord, ca. 2:50 ved 140 ord/min
- `state/rapporter/arkitekt_c1_muntlig_staar_v2.md` (STÅR): 422 talte ord, ca. 3:00 ved 140 ord/min (2:55 ved 145)
Bygges av `arbeid/oppgave_2641/felles.py BYTT|STAAR`. Diff mellom utgavene: tittel, tallavsnittet og rutingslinja.

Endret fra v1, etter `c1_jury_rettelser.md`:
- Internspråk ute: 0 treff på repo4, grønn, benk, tallvakt. «Repo4» heter nå «den nye modellen», «to benker» er fjernet, «KI» heter «konfidensintervallet».
- Punkt 1 sier hva MOT-F1 er (finner hvor mange av de 58, og om «mot» stemmer), og at følg styret har 96 % riktige, men 0 treff, altså F1 0, som er gulvet.
- 4f: «kontrollagent som ikke målte kandidatene». BYTT: «kjørte feilfritt fra kald start med samme tall» (etterfrys 17:18: 0,512).
- 4e/3b (STÅR): «rakk ikke å kjøre pakken … feilfritt fra kald start før fristen» og at 0,512 er fra 2026, ikke et friskt testår.
- 5c/5d: nytt forbehold. Omtrent 0,06 av F1 kommer fra NBIMs tidligere stemmer i samme sesong. Uten dem er F1 0,415, målt på den frosne (ERLIG § 2 og linje 76). I BYTT er gapet for den nye modellen ikke målt, så manuset sier «målt på den frosne».

KP: 0,512, TP 32 av 58, 164/1578 (10,4 %) = c1_etterfrys.md (forventet 0,512, fikk 0,512). 0,476, KI, 188/1578, +0,051/+0,017/+0,034 og [−0,005; +0,078] er uendret fra v1, der de er sjekket mot README og ERLIG § 7. 0,415 og 0,06 står i ERLIG:29/76 i begge utgavene. Ingen nye tall.
