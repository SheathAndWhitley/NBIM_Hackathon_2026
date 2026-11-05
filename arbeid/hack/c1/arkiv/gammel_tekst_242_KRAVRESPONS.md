# Fjernet fra levering/KRAVRESPONS.md (ordre #242, oppgave #2219)

Linje 6, 20-28, 36, 57, 73 ordrett før endring:

Speider #2083, 05.11 kl. 12.25 (erstatter arkitekt #2014 kl. 11.55, som gjaldt N-PX/0,474).
- **HULL H1: 1-sideren er feil case.** `c1/leveranse/kravrespons.md` (11.19) beskriver historikkregelen på N-PX,
  F1 0,383, «LightGBM slo ikke regelen», «sitatlaget gir 0 MOT», «0 av 158 snudd». Ingenting av det er agenten vi
  leverer. B kaller dette den viktigste leveransen. **Eier: speider (#1975) etter frys, utkast nå kan lages.**
- **~~HULL H2~~ LUKKET i #2094** (`bash arbeid/hack/c1/leveranse/kjor.sh` fra tom mappe gir 0,4762 MOT, forsøk #1106). Opprinnelig hull: ETT kall ga ikke hovedtallet fra pakken. `c1/leveranse/kjor.sh` ga da 0,383. `levering/README.md`
  og `fremmed.sh` lover 0,474286 på 1246 saker (v3). `fremmed.sh` kopierer ikke `c1_real.py`, `oppgave_2044/train.py`,
  `oppgave_2047/vern.py` eller real_votes-data. **Eier: arkitekt** (ett kall for 0,476 fra kald kopi, #2094).
- **HULL H3: kald start måler feil fasit.** `c1/kaldstart.sh` linje 46–47 måler med `c1/maaler.py` mot
  `c1/data_v3/fasit.csv`, REF hentes fra forsøk med «kjor_agent» (0,474). Real-id-ene finnes ikke i N-PX-fasiten.
  #1952 kl. 13 blir rød eller måler feil. **Eier: arkitekt/dommer** (steg 4 → `c1/maaler_offisiell_v2.py test --data real`, REF 0,481752).
- **HULL H6: KI og tall i README/BEGRENSNINGER gjelder N-PX.** `c1/leveranse/README.md` har KI 0,31–0,45 for regelen,
| 3 | Hvilken beslutning støttes (B 30 %) | `levering/BESLUTNINGSSTOTTE.md`; terskeltabell #2084 pågår | delvis: tabellen i `levering/README.md` er for v3 (1246 saker) |
| 19 | Påstander kan reproduseres fra koden (B «trekker ned») | 0,476 MOT (v3, #2087, dommer kald kopi #2090) og avvik 0,4818 målt to ganger (#2077, #2080) | løst i landsbyen; README-tallene 0,474/0,383 er påstander om en annen modell (H1, H2) |
