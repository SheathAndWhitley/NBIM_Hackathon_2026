# Case 1 juryavsnitt (#2936): hvorfor bytteregelen krever +0,02 i F1 MOT

arkitekt, 05.11 kveld. Bare tall fra eksisterende rapporter (henvist i tabellen). README-utkast: arbeid/hack/levering/README_STOY_UTKAST.md (ikke i frysen).

Hovedtallet er F1 på stemmer MOT styret. Det bygger på rundt 90 MOT-saker per testår. Flytter én sak seg over grensen, endrer F1 seg med omtrent 0,005 (c1_frosnitt_v2av.md). Derfor måler vi først hvor mye tallet flytter seg uten at modellen blir bedre. Først etter det godtar vi en forbedring. Alle tall under er hentet fra rapporter som allerede finnes. Ingen nye målinger er gjort for denne siden.

| Kilde til støy | Størrelse i F1 | Kilde |
|---|---|---|
| LightGBM-frø, v2+av, per år | sd 0,008–0,012 (2024–26) | c1_natt_frospredning_v2.md, c1_frosnitt_v2av.md |
| LightGBM-frø, v2+av, snitt 2024–26 | sd 0,0047 | c1_natt_frospredning_v2.md |
| LightGBM-frø, frossen pakke, snitt 2024–26 | sd 0,0136 (2026 alene: sd 0,021) | c1_natt_frospredning_v2.md (#2886) |
| Snitt av 5 frø i stedet for 1 | ikke jevnere: sd 0,0035–0,0125 per år | c1_frosnitt_v2av.md (#2926) |
| Ett tilfeldig trekk uten informasjon lagt til (støygulv) | sd 0,009 på snittet, opptil −0,046 i ett år | c1_ablasjon_forklaring.md (#2919) |
| Mac mot Linux, samme kode og versjoner | 0,512 mot 0,520 = 0,008 (2026) | c1_plattformavvik.md |
| Grensen valgt på samme år som den måles på (pynt, ikke støy) | +0,0185 på frossen 2023 | c1_vakt2023_aerlig.md (#2927) |
| Grensen og antall flagg valgt med fasit (tak, ikke ærlig) | høyst +0,014 på snittet | c1_natt_kandidat_ny.md (#2929) |

**Derfor +0,02.** Vi legger sammen de fire uavhengige støykildene for en forskjell mellom to modeller (v2+av-frø 0,0047, frossen-frø 0,0136, trekk-gulv 0,009 og plattform 0,008) som kvadratsum. Det gir 0,019, så kravet på +0,02 ligger over summen av støyen. Kravet ligger også over det beste en grense valgt med fasit kan gi (+0,014). Det er ingen stor margin, bare omtrent én samlet sd. Derfor har regelen to vakter til. Regelen skrives i REGEL.md før hver måling. I tillegg må ingen av årene 2023–2026 falle mer enn 0,02. Natt-lederen v2+av ligger +0,043 over frossen målt snitt mot snitt over 5 frø. Det er omtrent dobbelt så mye som kravet. Selv med verste frø er den +0,036 over (c1_natt_frospredning_v2.md).

**Det støyen lærte oss om vår egen evaluering**
- 2023 var pyntet. Grensen var valgt på 2023 selv. Målt ærlig (grensen valgt på 2022) faller gevinsten til v2+av på 2023 fra +0,019 til +0,004. 2023 brukes nå bare som vakt, og bare med ærlige filer på begge sider.
- Tallvakta for pakka tåler ±0,01 mellom plattformer, ikke mer. Da fanger den fortsatt ekte endringer.
- Den frosne pakka måles nå også med 5 frø (#2933), så dommen sammenligner snitt med snitt.

**Tre lukkede spor, med tall**
1. *Grense, terskel og antall flagg* (#2929, #2703): selv med fasit gir dette bare +0,014 på snittet (0,5616 → 0,5755). Ingen ærlig grenseregel kan nå +0,02.
2. *Forklarings-trekk* (#2907, #2919): beste variant er +0,0008 over v2+av (0,5604 mot 0,5596). Alle variantene ligger inne i støybåndet til tilfeldige trekk (0,5409–0,5617).
3. *Snitt av 5 LightGBM-frø* (#2926): +0,0046 (0,5642 mot 0,5596). Det gir ikke jevnere F1 enn ett frø. Står ikke.
