# Case 1: anonym klone av GitHub-repoen (#2778)

**Resultat: IKKE KJØRT. Repoen github.com/Martinkristofferhansen/nbim er fortsatt privat (404 kl. 19:55), så anonym klone feiler og README-tallet kan ikke sammenlignes med frossen 0,5162.**

## Hva jeg gjorde
- `curl -w %{http_code} https://github.com/Martinkristofferhansen/nbim` → `404` (19:55).
- `GIT_TERMINAL_PROMPT=0 git -c credential.helper= clone https://github.com/Martinkristofferhansen/nbim` i tom mappe `/tmp/c1_anon_Dq7l` → `fatal: could not read Username` (GitHub ber om innlogging = privat).

## Rettelse til autolukkingen av #2772
Tavlas autolukking av #2772 (19:54:31) skrev til guden at vakta sluttet med kode 0 og at «repoen ser ut til å ha blitt offentlig». Det stemmer ikke. `arbeid/oppgave_2772/vakt.log` viser 404 ved hver sjekk 19:34–19:54, og min egen sjekk 19:55 gir også 404. Kode 0 kom av at økta ble avsluttet, ikke av svar 200.

## Neste steg
- Bare guden kan gjøre repoen offentlig (Settings > Danger Zone > Change visibility), eller gi juryen tilgang.
- Når den svarer 200: kjør `bash arbeid/oppgave_2772/klone.sh` (eller dommerens fremmed-test #2900/#2901), som kloner anonymt og kjører 'Start her'.
- Fremmed-testen (#2900) mot den private repoen dekker innholdet i mellomtida. Denne oppgaven tester bare den offentlige veien.
