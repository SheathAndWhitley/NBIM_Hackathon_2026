# Case 1 (#2657): er muntlig manus i BYTT-pakken v2? NEI, avvik

**Dom: RØD på versjon, GRØNN på tall.** `arbeid/hack/c1/leveranse/MUNTLIG.md` (17:21, commit 5514792) er v1. Den er byte-lik fila i siste grønne jury-zip `state/levering/c1_gronn/jurypakke_c1_1724_5514792.zip` (sha fc0dbc55). v2 (`state/rapporter/arkitekt_c1_muntlig_v2.md`, 17:22) er ikke limt inn, verken i kilden eller i zipen.

## Tallene (alle stemmer med zip og README)
KP: forventet 0,512 / 32 av 58 / 164 av 1578 / 10,4 %, fikk det samme i MUNTLIG.md:13 og :22. KI 0,40–0,62, frossen 0,476, +0,051/+0,017/snitt +0,034 og KI −0,005 til +0,078 (:13, :17) stemmer med README.md:8–12 og ERLIG § 7. «1539 saker» (:13) mot «1578 saker» (:22) er riktig (1539 med fasit, 1578 inn til agenten; README.md:8 og :10), men kan forvirre muntlig.

## Avvik v1 (leveranse og zip) mot v2
1. `leveranse/MUNTLIG.md:16-17`: **største forbehold mangler**: «omtrent 0,06 av F1 kommer fra NBIMs egne tidligere stemmer i samme sesong; uten den er F1 0,415, målt på den frosne modellen» (v2:17). README.md:14 har det i hovedboksen, så muntlig og README er ikke like.
2. `leveranse/MUNTLIG.md:13`: mangler at den nye modellen er levert og kjørte feilfritt fra kald start med samme tall (v2:13). v1 har en svakere setning i :9.
3. `leveranse/MUNTLIG.md:6`: problemavsnittet nevner ikke 58 av 1539 og forklarer ikke F1 som funnet/treff (v2:6).
4. `leveranse/MUNTLIG.md:3`: overskriftslinja viser til «§ 7»; v2:3 viser til rettelsene i #2641.
5. Tider: v1 30/60/30/30/30/10 s = 190 s; v2 30/55/30/30/25/10 s = 180 s, som passer «3 minutter».

## Tiltak (for smed, før tekststopp kl. 19)
Lim v2 (linje 1–26 i rapporten, uten «v2» i tittelen om ønsket) inn i `arbeid/hack/c1/leveranse/MUNTLIG.md`. Behold VARIANT-merkene, de er like i begge. Tallvakt på fila og ny fasit-linje i `frys_fasit_1600.sha256`. Den nye grønne zipen fra #2549 (19:00) tar den med. STÅR-reserven (`reserve_staar/MUNTLIG.md`) er ikke sjekket her.
