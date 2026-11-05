# Case 1: grunnlaget for BYTT/STÅR kl. 18:45 på én side (#2680, arkitekt, 05.11 17:50)

Bare målte tall, alle med kilde. Til dommer2 (#2603).

## 1. Regelen (#265, satt før måling: `c1_byttregel_forhand.md`)
F1 MOT over test 2024/2025/2026: snitt minst **+0,02** over frossen, og **intet år under −0,02**. Val = året før test.

## 2. Frossen mot kandidat (dommer2 gjenskapte fra kald kopi 16:58, `c1_byttedom_265.md`)
| modell | 2024 (TP/FP/FN) | 2025 | 2026 | snitt | mot frossen |
|---|---|---|---|---|---|
| frossen #2044 miks h2 | 0,4545 (30/14/58) | 0,5143 (45/31/54) | 0,4762 (30/38/28) | 0,4817 | – |
| **repo4** | 0,5057 (44/42/44) | 0,5309 (43/20/56) | 0,5120 (32/35/26) | **0,5162** | **+0,0345** |
| repo4 − frossen | +0,051 | +0,017 | +0,036 | +0,0345 | |

- Krav 1: +0,0345 ≥ +0,02, **oppfylt**. Krav 2: verste år +0,017, ingen år under, **oppfylt**.
- Usikkerhet (parret klyngebootstrap, 2000 trekk): snitt +0,0345 [−0,005; +0,078]. 4 % av trekkene gir repo4 under frossen. KI-en krysser null.
- Forbehold: 2026 var kjent før regelen ble skrevet. 2024 og 2025 ble målt etter: +0,051 og +0,017. Fjerde år 2023 (#2573, utenfor regelen): +0,005.
- Andre kandidater: av sju besto bare repo4 (`c1_byttedom_265.md`). Ensemble 0,5·frossen+0,5·repo4 (#2585): snitt 0,507, under repo4. Andelsterskel (#2584): snitt +0,010, 2025 −0,0195, **består ikke**. Ingen av dem utfordrer repo4.

## 3. Er pakkene grønne fra kald start?
| pakke | siste målte kalde kjøring | resultat | kilde |
|---|---|---|---|
| **BYTT (repo4)** zip 5514792 (sha fc0dbc55) | 17:29 dom og 17:37 generalprøve: tom mappe, `env -i`, tom uv-cache | F1 MOT **0,512000**, TP 32 FP 35 FN 26 TN 1446, frysvakt og tallvakt GRØNN (157 påstander, 0 avvik), 85 s | `c1_dom_bytt_kald.md`, `c1_generalprove_1740.md` |
| BYTT, demo | 17:4x, ny kald kopi | MANUS OK (15/89/39), frys 17:18:18 | `c1_demo_kald_sjekk.md` |
| **STÅR (frossen)** reserve_staar | 17:38 tørrkjøring i kald kopi | **0,476190**, TP 30 FP 38 FN 28, tallvakt GRØNN (177, 0 avvik), ziptest GRØNN | `c1_staar_rettelser_2640.md` |
| landsbyen nå | 17:50 `c1_frys.py sjekk --krev` | FRYSVAKT GRØNN, 21 filer like som ved frys 17:18:18 | kjørt av meg |

## 4. Det som er åpent før 18:45 (ikke målt ennå)
1. **SISTE_GRONNE.zip peker nå på `jurypakke_c1_1742_c3ab2a3.zip` (17:41).** Jeg fant ingen dom eller kald kjøring på akkurat denne zipen. De grønne dommene gjelder 5514792. Én ziptest på c3ab2a3 før 18:45 lukker hullet.
2. Tekst, ikke modell: åtte tall-avvik i JURY/ERLIG/README (#2671, blant annet «under målet 0,5» og frossen-tall 30/28, 0,191/0,919), ordsjekk-treff (#2653, #2654). Disse endrer ikke F1, men porten i `c1_byttedom_265.md` krever at tekstene er oppdatert innen 19:00.
3. STÅR-kjeden må tørrkjøres på nytt etter ordsjekken (#2681).

## 5. Lesning (min, ikke en dom)
Regelen er oppfylt med målte tall. BYTT-pakken er grønn fra kald start på to uavhengige kjøringer. STÅR-reserven er også grønn, så tilbakerulling er trygg. Det som kan felle BYTT kl. 18:45 er bare pkt. 4.1 og 4.2 (portvilkåret), ikke modelltallene.
