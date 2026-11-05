# Case 1 kald start 2 (dommer #2127): GRØNN, F1 0,476190 på MOT fra kald kopi

**Dom: GRØNN** 12:56. `sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_kald6_2127` fra landsbymappen, ny tom mappe. rc 0, 50 s totalt
(uv sync 1 s, agent og måler 49 s).
- `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190`: TP 30 FP 38 FN 28, P 0,441, R 0,517, 58 MOT i fasit. Likt tavla (#2090) og #1952.
- Tallvakta (#2136) i kopien: `13 filer, 129 påstander om hovedtallet stemmer, 0 avviker`, TALLVAKT GRØNN.
- Til menneske: 188 av 1578 inn (11,9 %: 127 usikre i kalibrert bånd [0,15; 0,85), 60 ukjent selskap, 1 instruks), 183 av 1539 med fasit.
- `pred_maaler.csv` er byte-lik mellom første og siste kopi i dag (sha256 b113b545dd86). Prediksjonen er uendret, så lekkasjedommen fra #1952 står.

## Kjøringer
| Kopi | Tid | Utfall |
|---|---|---|
| /tmp/c1_kald2_2127 12:50 | 34 s | rc 0, men demoen viste «66 mot styret, F1 MOT 0,4818» (avvik), og siste SCORE i loggen var 0,481752 |
| /tmp/c1_kald3_2127 12:52 | 36 s | RØD: syntaksfeil i fremmed.sh. Arkitekten (#2136) skrev fila 12:53:20 mens sh leste den. Ingen feil i fila |
| /tmp/c1_kald4_2127 12:53 | 29 s | RØD, med riktig grunn: tallvakta fant 43 tall i pakka som avviker fra kjøringen |
| /tmp/c1_kald5_2127 12:55 | 48 s | RØD: 5 avvik igjen |
| /tmp/c1_kald6_2127 12:56 | 50 s | **GRØNN** |

## Rettet (pakking, ingen modellendring)
1. `c1/leveranse/demo_vis.py`: «mot styret» var `against_board == 1`, altså 66 avvik inkludert 5 AVSTÅ. Nå bruker den samme definisjon som måler v3 `--score mot`: nbim_vote MOT og against_board 1, mot anbefaling MOT med mot_styret 1. Demoen viser nå 30/38/28 og F1 0,4762. Sak 3 («NBIM fulgte styret») krever nå against_board 0.
2. `levering/fremmed.sh`: skriver til slutt `HOVEDTALL F1 MOT ...` fra v3 `--score mot` i kopien. Før var siste tallet `SCORE 0.481752` (avvik). Det var mangel 1 i #1952.
3. `c1/leveranse/demo.sh`: hodet viser HOVEDTALL-linja, med avviket som sidetall. Før viste det første SCORE-linje (0,4818).
4. Til menneske var 228 av 1578 (14,4 %) og 223 av 1539 (14,5 %), fra før det kalibrerte båndet (#2132). Nå står 188 (11,9 %) og 183 (11,9 %) i `levering/KRAVRESPONS.md` (linje 13 og 61), `levering/JURY_SPORSMAL.md:42`, `levering/EN_SIDE.md:26`, `c1/leveranse/README.md:9-10` og `c1/leveranse/BEGRENSNINGER.md:3`.
5. N-PX-tallet 129 sto uten merke i `c1/leveranse/BEGRENSNINGER.md:22` og `levering/METODE.md` (tabell og pkt. 6). Begge er merket «N-PX».
- README/BESLUTNINGSSTOTTE (P 1,00 / R 0,71 og så videre i systemkolonnene) ble rettet av andre (#2135) mens jeg jobbet.

## Til eierne, ikke rettet her
- `levering/EN_SIDE.md:23` (speider #2133) sier fortsatt «standard 10 % av val-sakene». Det stemmer ikke lenger, siden båndet nå er kalibrert P(MOT) i [0,15; 0,85). Tallvakta fanger ikke dette, fordi det ikke er et tall om hovedtallet.
- Kopilista i fremmed.sh må følge med når agenten får nye moduler (mangel 2 i #1952). Det holder i dag.
- Ingen av endringene er i git, fordi arbeid/ og state/rapporter er ignorert. Kopiene før endring ligger i /tmp/*_for_2127.*.

## Kommando
`sh arbeid/hack/c1/leveranse/demo.sh /tmp/<ny_mappe>`. Se etter `TALLVAKT GRØNN` og `HOVEDTALL ... 0.476190` i `/tmp/<ny_mappe>.log`.
Ikke rediger fremmed.sh mens noen kjører den: sh leser skriptet underveis.
