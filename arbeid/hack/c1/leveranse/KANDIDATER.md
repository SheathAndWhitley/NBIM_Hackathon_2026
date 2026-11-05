# Case 1: kandidatlogg etter byttet – alt vi prøvde, og hvorfor repo4 står

Kilderapportene i kolonnen «kilde» ligger i repoet under `state/rapporter/`, ikke i jury-zipen. «Frossen» betyr her repo4, modellen som leveres. <!-- tallvakt: ignorer: kandidatlogg, ikke hovedtall -->

## Bytteregelen, fastsatt FØR måling (ordre #265, mission.md)
En kandidat erstatter den frosne modellen bare hvis **snittet av F1 på MOT over tre rullende testår (2024, 2025, 2026) er minst +0,02 over frossen**, og **intet testår er mer enn 0,02 dårligere** enn frossen. Dommeren avgjør. Ellers står frossen.
- Frossen = repo4 (#2567): 0,5057 / 0,5309 / 0,5120, snitt **0,5162** (frys 17:18:18, frysvakt).
- Måler: den offisielle `arbeid/oppgave_2567/maaler_aar.py --score mot`. Terskel/variant velges på val-året T-1, og test T måles én gang.
- Regelen er også skrevet ned per kandidat før måling i `arbeid/oppgave_{2699,2703,2707,2708}/REGEL.md`. Når hver fil ble skrevet, mot første resultatfil i samme mappe: `arbeid/hack/c1/REGEL_TIDSSTEMPLER.md` (også natt-kandidatene fra #281).

## Tabell
Δ = kandidat minus frossen repo4. Snitt og årstall er hentet fra kilderapporten. Δ-kolonnene er regnet ut her fra de samme tallene (enkel differanse).

| id | idé | 2024 / 2025 / 2026 | snitt 3 år | Δ snitt (krav ≥ +0,02) | verste år Δ (krav ≥ -0,02) | utfall | kilde |
|---|---|---|---|---|---|---|---|
| #2699 | midt-terskel (snitt av rå grense og andel) på **gammel frossen #2044** | 0,4965 / 0,5055 / 0,4918 | 0,4979 | +0,016 mot #2044 (-0,018 mot repo4) | -0,009 (2025) mot #2044 | STÅR (målt mot gammel frossen, under +0,02) | speider_2699_midtterskel.md |
| #2700 | rang-snitt frossen #2044 + repo4, w=0,5 | 0,5025 / 0,5102 / 0,5124 | 0,5084 | -0,0078 | -0,0207 (2025) | STÅR (feiler begge krav) | arkitekt_2700_rangensemble.md |
| #2701 | repo4 + «av»: fjern MOT-flagg når NBIMs siste stemme på samme selskap+tekst var FOR (valgt på val) | 0,5269 / 0,5375 / 0,5246 | **0,5297** | +0,0135 | +0,0066 (2025) | STÅR (beste kandidat, bedre alle år, men under +0,02) | c1_2701_repo4_siste_regel.md |
| #2701 | variant «paa» | 0,5029 / 0,5181 / 0,5039 | 0,5083 | -0,0079 | -0,0128 (2025) | STÅR | c1_2701_repo4_siste_regel.md |
| #2701 | variant «av+paa» | 0,5238 / 0,5244 / 0,5161 | 0,5214 | +0,0052 | -0,0065 (2025) | STÅR | c1_2701_repo4_siste_regel.md |
| #2703 | midt-terskel + «av» på repo4 | 0,5083 / 0,5276 / 0,5424 | 0,5261 | +0,0099 | -0,0033 (2025) | STÅR | speider_2703_midt_av_repo4.md |
| #2703 | «midt» alene (rapportert, ikke kandidat) | 0,4792 / 0,5238 / 0,5333 | 0,5121 | -0,0041 | -0,0265 (2024) | STÅR (feiler begge krav) | speider_2703_midt_av_repo4.md |
| #2704 | «av» med flertall i historikk (avflert) | 0,5000 / 0,4967 / 0,4957 | 0,4975 | -0,0187 | -0,0342 (2025) | STÅR (feiler begge krav) | c1_2704_siste_regel_typefall.md |
| #2704 | «av» + fallback selskap+forslagstype (avtype) | 0,5185 / 0,5283 / 0,5357 | 0,5275 | +0,0113 | -0,0026 (2025) | STÅR | c1_2704_siste_regel_typefall.md |
| #2704 | avtype3 (fallback, ≥3 og alle FOR) | 0,5181 / 0,5375 / 0,5289 | 0,5282 | +0,0120 | +0,0066 (2025) | STÅR | c1_2704_siste_regel_typefall.md |
| #2704 | ærlig val-valg blant variantene | 0,5181 / 0,5375 / 0,5246 | 0,5267 | +0,0105 | +0,0066 (2025) | STÅR | c1_2704_siste_regel_typefall.md |
| #2705 | rang-snitt frossen+repo4, w=0,2 | 0,4673 / 0,5109 / 0,5161 | 0,4981 | -0,0181 | -0,0384 (2024) | STÅR (feiler begge krav) | arkitekt_2705_rang_w02.md |
| #2707 | «av» + fyll opp de frigjorte flaggene | 0,4972 / 0,5342 / 0,5280 | 0,5198 | +0,0036 | -0,0085 (2024) | STÅR | c1_2707_av_fyll.md |
| #2708 | «av» bare med FOR-stemme i T-1/T-2 | 0,5238 / 0,5342 / 0,5203 | 0,5261 | +0,0099 | +0,0033 (2025) | STÅR | speider_2708_av_nylig.md |
| #2709 | avn1 (siste FOR senest i fjor) | 0,5207 / 0,5342 / 0,5203 | 0,5251 | +0,0089 | +0,0033 (2025) | STÅR | c1_2709_av_nylighet.md |
| #2709 | avn2 (siste FOR senest for 2 år siden) | 0,5238 / 0,5342 / 0,5203 | 0,5261 | +0,0099 | +0,0033 (2025) | STÅR | c1_2709_av_nylighet.md |
| #2709 | avp (behold flagg i topp 10 % p_avvik), lik val-valget | 0,5269 / 0,5375 / 0,5246 | 0,5297 | +0,0135 | +0,0066 (2025) | STÅR (samme som «av», endrer ingen flagg) | c1_2709_av_nylighet.md |
| #2710 | maks-rang (ELLER) frossen+repo4 | 0,4908 / 0,4950 / 0,5161 | 0,5007 | -0,0155 | -0,0359 (2025) | STÅR (feiler begge krav) | arkitekt_2710_rang_max.md |

**Utfall samlet:** ingen av de 18 målingene når +0,02 i snitt. Beste er «av» (#2701), +0,0135, som er bedre alle tre år. **Frossen repo4 står.** Dommen 18:15 (#2713, c1_dom_1815.md): **STÅR**. Dommeren målte #2709 og #2710 på nytt med `maaler_aar.py` på smedenes svarfiler og fikk de samme tallene på alle ni filene. Etter 18:15 tas ingen nye kandidater inn.

## Lekkasjesjekk for repo4 (#2731)
Brute force-sjekken på 400 tilfeldige rader (seed 2731, alle år 2019–2026) er kjørt for de fire historikktrekkene i repo4: **15 avvik på 400 rader (11 rader)**. Alle 15 kommer av at et selskap har to møter samme dato, og NBIM-repoets `ballot.py` regner da møtet med lavest `meeting_id` som «tidligere». Med den rekkefølgen er det 0 avvik, og ingen trekk bruker senere datoer. I test 2026 er 14 av 1539 rader berørt, 1 av dem er MOT i fasit (flagget riktig; om flagget skyldes samme-dags-trekket er ikke målt). Tar man bort de 14 radene i 2026-kjøringen, går F1 fra 0,529 til 0,522 (−0,007); det er ikke hovedtallet, bare et mål på at effekten er liten. Konsekvens: påstanden «bare møter strengt før saken» stemmer ikke for repo4; riktig er «strengt tidligere møte, eller annet møte samme dag». Det svekker repo4 litt: noe av tallet kan komme fra stemmer i samme-dags-møter, som NBIM trolig kjenner når stemmen avgis, men som ikke er bevist kjent. Treårstallene (snitt 0,5162) er ikke målt på nytt uten de berørte radene, og modellen rettes ikke etter frysen. Kilde: `c1_lekkasje_repo4.md`. <!-- tallvakt: ignorer: lekkasjesjekk, ikke hovedtall -->

### Effekt av samme-dags-fiksen (#2744)
Dommeren har nå målt treårstallene med historikk bare fra strengt tidligere dato (alle møter samme dag regnes som samtidige). F1 på MOT per testår: 2024 0,5057 → 0,4973 (−0,008), 2025 0,5309 → 0,5153 (−0,016), 2026 0,5120 → 0,5636 (+0,052); snitt 0,5162 → 0,5254 (+0,009). På de berørte radene endres bare 0, 0 og 1 flagg. Endringen i F1 kommer av at valideringsåret velger en annen C og grense (2026: grense 0,9386 i stedet for 0,9232, 70 → 55 flagg), ikke av at samme-dags-historikken ga treff. Etter regelen i #265 kvalifiserer varianten ikke til bytte (snitt +0,009 < +0,02, og 2025 −0,016 er nær grensen −0,02), så levert modell står urørt. Lærdom: ±0,05 på ett år fra et nytt modellvalg er like stort som gevinsten repo4 ble valgt på. Kilde: `kilder/c1_lekkasje_effekt.md`. <!-- tallvakt: ignorer: lekkasjeeffekt, ikke hovedtall -->

## Hva juryen bør lese ut av dette
- Regelen holdt. Vi byttet ikke på en gevinst som var mindre enn kravet, selv om «av» var bedre alle tre år. Den er ført opp som neste steg, ikke som hovedtall.
- To vinkler er lukket med tall: ensemble frossen+repo4 (3 blandeformer, alle under repo4 alene) og varianter av «av»-regelen (7 varianter, alle ≤ 0,5297).
- Tavla viser 0,55814 «NYTT BESTE» for #2703. Det tallet gjelder bare 2026-fila (63/66 MOT-fasit dekket), og er ikke et snitt over tre år. Riktig tall er 0,5261 (speider_2703_midt_av_repo4.md).
- #2702 og #2706 i samme nummerserie gjelder reserveoppgaven (hack/bekker), ikke Case 1, og er utelatt.
