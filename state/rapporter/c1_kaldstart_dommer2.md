# Case 1: kald start av endelig zip i tom mappe (dommer2, 05.11 19:40, #2860)

**Dom: GRØNN** for begge zipene. Alle README-kommandoer kjørte med utgang 0 i en ny tom mappe under /tmp, uten noe fra landsbymappen (0 treff på `<repo>` i loggene). Ikke noe i pakken eller repoen er endret.

## Avvik meldt til dommer (#2828/#2831), 19:38
Utkastet i `arbeid/oppgave_2828/UTKAST.md` og pekeren `ENDELIG_PAKKE.zip` viser 1902-zipen, mens `c1_repo4_synk.md` sier endelig zip er 1918-zipen (`SISTE_GRONNE.zip`). Forskjellen er to tekstfiler (`leveranse/README.md`, `kravrespons.md`): 1918 har 0,396-rettelsen (repo4 uten samme-sesong-historikk) og er byte-lik GitHub; 1902 sier «golvet ikke målt». Kode, modell og data er like. Sluttkvitteringen bør bruke 1918-sha. Jeg kaldstartet derfor begge.

## Tall
| zip | sha256 | KJOR.sh | testaar.sh | F1 MOT 2026 | 2024 / 2025 / 2026, snitt |
|---|---|---|---|---|---|
| jurypakke_c1_1902_cbae393.zip (ENDELIG_PAKKE, #2828-utkast) | e6dae4988dbd2056ba4d6ee399d116394e66e9e59493121c09e1ac40f8ea7818 | utgang 0, FRYSVAKT GRØNN, TALLVAKT GRØNN | utgang 0 | 0.512000 | 0.5057 / 0.5309 / 0.5120, snitt 0.5162 |
| jurypakke_c1_1918_9f41d82.zip (SISTE_GRONNE, lik GitHub) | 84aefb46fbb5eca17d2d590c2fe571357b03b7f114a1c1b7f57c68cd93462f73 | utgang 0, FRYSVAKT GRØNN, TALLVAKT GRØNN | utgang 0 | 0.512000 | 0.5057 / 0.5309 / 0.5120, snitt 0.5162 |

Forventet snitt 0,5162: truffet nøyaktig. Detaljer 2026: P 0,4776, R 0,5517, TP 32 / FP 35 / FN 26 (58 MOT i fasit). Til menneske 164 av 1578. Tallvakta: 26 filer, 177 påstander om hovedtallet, 0 avvik.

## Forbehold
- uv sin pakkebuffer var varm (`uv sync 0 s`), så nedlastingen fra tom buffer er ikke testet her (den er testet tidligere, se README-en i pakken). Pakkens eget `.venv` ble bygd på nytt fra `uv.lock`.
- `uv` og `python3` kom fra PATH, som README krever.
- Tid: KJOR.sh 40 s, testaar.sh 14 s.

## Kommandoer
    D=/tmp/c1_kald_dommer2_1932; mkdir -p $D && cd $D && cp state/levering/c1_gronn/jurypakke_c1_1902_cbae393.zip pakke.zip && unzip -q pakke.zip && cd c1_stemmeagent
    sh KJOR.sh; bash arbeid/hack/c1/leveranse/verktoy/testaar.sh
    (samme for jurypakke_c1_1918_9f41d82.zip i $D/z1918)
Logger: `/tmp/c1_kald_dommer2_1932/{kjor,testaar}.log` og `/tmp/c1_kald_dommer2_1932/z1918/{kjor_1918,testaar_1918}.log`.
