# Case 1: generalprøve kl. 17:37, siste jury-zip fra kald start (#2672)

**GRØNN: zip 5514792 kjører fra tom mappe på 85 s og gir F1 MOT 0,512000, uten noe utenfor zipen.**

Zip: `state/levering/c1_gronn/jurypakke_c1_1724_5514792.zip` (= `SISTE_GRONNE.zip` kl. 17:37), sha256 `fc0dbc55…edc`, 150 filer.
Mappe: `/tmp/c1_gp_2672` (tom, utenfor landsbyen). `env -i`, tom HOME, **tom uv-cache** (`UV_CACHE_DIR` ny, 232 MB lastet ned). Logger: `/tmp/c1_gp_2672/kjor.out`, `steg4.out`.

## 1. Tid
| steg | klokke | tid |
|---|---|---|
| utpakking (`unzip`) | 17:37:17 | 0 s |
| lese README.md (inngangen), finne `sh KJOR.sh` | 17:37:17–17:37:35 | 18 s |
| `sh KJOR.sh`: uv sync 5 s (tom cache), agent + målere 61 s | 17:37:35–17:38:42 | 67 s |
| **utpakking → HOVEDTALL + TALLVAKT GRØNN** | | **85 s** |
| valgfritt steg 4, `sjekk_treffsikkerhet.sh` (egen 2x2-telling) | 17:38:55–17:39:02 | 7 s |

Agenten brukte 39 s i KJOR.sh og 6 s i steg 4 (samme svar, sha LIK). Forskjellen er last fra andre agenter (KJOR.sh fikk 18 % CPU), ikke pakka. README lover «ett til to minutter»: holder.

## 2. Tall
| krav | resultat |
|---|---|
| F1 MOT | `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.512000` (P 0,4776 R 0,5517 TP 32 FP 35 FN 26) |
| frysvakt i zipen | GRØNN, 19 filer |
| tallvakt | GRØNN, 20 filer, 157 påstander, 0 avvik |
| steg 4 uten måler | `TP 32 FP 35 FN 26 TN 1446: STEMMER`, `sha256 ny prediksjonsfil = frossen (d02cf884…4a0c): LIK` |
| landsby-stier i loggene | 0 treff på `landsby` eller `~` |

## 3. Steg som krevde kunnskap utenfor zipen
1. **Ingen.** README.md i roten sier `sh KJOR.sh` ord for ord, og KJOR.sh leser bare zipen pluss uv sin pakkebuffer.
2. Forutsetning: `uv` installert. README gir kommandoen. Det er det eneste juryen trenger fra nett (pluss pakkene, 232 MB, 5 s her).
3. Merknad til ordren: oppgaven sier «følg bare LES.md/JURY.md». Zipen har **ingen LES.md**; inngangen heter `README.md` (rot) og `arbeid/hack/c1/leveranse/JURY.md`. Juryen finner README.md med en gang, så dette er bare et navn i oppgaveteksten, ikke et hull i pakka. #1972 bør si README.md.
4. Alle filer JURY.md lenker til med `.md/.sh/.py` finnes i zipen (sjekket).

## 4. Sett, men allerede dekket av #2671 (tekst, ikke kjøring)
JURY.md:5 «under målet 0,5» (tallet er 0,512); JURY.md:24 «finner 30 av 58, overser 28» og :35 «18 MOT ser ingen» er frossen-tall (kald kjøring: 32 av 58, 26 oversett); rot-README:39–40 grenser 0,191/0,919 mot kjøringens 0,232/0,923. Tallvakta ser ikke disse. Neste zip (tekststopp #2549) dømmes i #2668 og #1972.

GRØNN
