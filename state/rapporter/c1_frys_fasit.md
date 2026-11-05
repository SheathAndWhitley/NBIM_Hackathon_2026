# Case 1: fasit for frys-dommen (#2445, dommer2, 05.11 kl. 15:55)

Fasit: `arbeid/hack/levering/frys_fasit_1600.sha256` (104 filer, sha256 per fil slik den ligger i jury-zipen,
stier `c1_stemmeagent/...`). Generator: `arbeid/hack/levering/frys_fasit.py`. Diff: `arbeid/hack/levering/frys_diff.sh`.

## Slik brukes den (dom #2440 kl. 16:10)
```
sh arbeid/hack/levering/frys_diff.sh /tmp/<ny jury-zip>.zip          # zip
sh arbeid/hack/levering/frys_diff.sh /tmp/<stage>/c1_stemmeagent      # utpakket mappe
sh arbeid/hack/levering/frys_diff.sh --kilde                          # kildefilene i landsbymappen nå
```
Utskrift: linjer `NY`, `ENDRET`, `BORTE` + `FRYS AVVIK: n` (utgang 1), eller `FRYS LIK: 0 avvik` (utgang 0).
Trenger fasiten lages på nytt (f.eks. etter en godkjent retting før kl. 16):
`python3 -I arbeid/hack/levering/frys_fasit.py > arbeid/hack/levering/frys_fasit_1600.sha256`

## Hvordan fasiten er regnet
frys_fasit.py speiler pakk_jury.sh uten å kjøre fremmed.sh: fillista er fremmed.sh sine kopier-linjer,
c1_frys.py FILER, hele c1/leveranse/ (uten __pycache__, .pyc, .DS_Store, ut/), vis_manussaker.py,
DEMO_MANUS.md, tall_tabell.md, KJOR.sh (= jury_kjor.sh), README.md (= JURY_README.md). De to målerne hashes
etter samme sed som pakk_jury.sh steg 3, FROSNE_SHA256.txt bygges på samme vis som steg 4. Ingenting i pakka er endret.

## Kjøringer
- `--kilde` mot nåtilstanden: FRYS LIK, 0 avvik.
- Mot /tmp/jurypakke_c1.zip (bygd 15:45, før smed2 la demo-filene inn i pakk_jury.sh): 3 avvik, alle
  ventet og fra pågående #2442: BORTE DEMO_MANUS.md og vis_manussaker.py, ENDRET leveranse/demo.sh.
- Egen testbygging med pakk_jury.sh i egne mapper (/tmp/d2_frys): se under.

## Funn: zip-rota har landsbyens pyproject.toml og uv.lock, ikke kandidatens
pakk_jury.sh sin `kopier()` kopierer fra landsbymappen etter relativ sti. Byggemappa har `pyproject.toml`
og `uv.lock` i rota (fremmed.sh legger kandidatens låste der), men `kopier pyproject.toml` tar da
**landsbyens** rotfiler (name = "landsby", torch, catboost, claude-agent-sdk, 4558 linjer lock).
Bekreftet i både /tmp/jurystage_c1 og /tmp/jurypakke_c1.zip (sha 395499ad…/66faa0a3…), mens
/tmp/jurybygg_c1 har kandidatens (96fcf3b1…/ed54fd6c…). KJOR.sh kjører `uv sync --frozen` på rotfila,
så juryen installerer landsbyens miljø. Det virker (#2416 ga 0,47619 fra zipen) og de 230 MB i README er
trolig målt med denne lockfila, men det er ikke «samme låste versjoner som modellen ble målt med» slik
pakk_jury.sh/jury_kjor.sh påstår. Fasiten speiler det pakk_jury.sh faktisk gjør i dag. Rettes dette før
kl. 16 (dommer avgjør, #2444), må fasiten lages på nytt med én-linja over. Jeg har ikke rettet noe.

## Testbygging med pakk_jury.sh (egne mapper, /tmp/d2_frys, bygd 15:50–15:52)
Første forsøk ga 8 NY-filer: noen hadde nettopp lagt 8 filer inn i pakk_jury.sh (#2448, ukommittert) etter at
fasiten ble regnet. Generatoren leser nå de bokstavelige `kopier`-linjene rett fra pakk_jury.sh, så fillista
følger skriptet. Ny fasit: **112 filer**. Diff mot den nybygde zipen: 1 avvik, ENDRET DEMO_MANUS.md, fordi fila
ble redigert i landsbymappen etter at zipen ble bygd (zip 15:51:49, DEMO_MANUS.md 15:52:21). Det er riktig oppførsel: skriptet
fanger akkurat slike endringer. `--kilde` mot nåtilstanden: FRYS LIK, 0 avvik.

**Pakka er et bevegelig mål fram til kl. 16.** Dommeren bør kjøre én-linja under kl. 16:00 presis, så fasiten
er sha256 av det som faktisk fryses, og deretter bruke frys_diff.sh på zipen fra kl. 16:10:
`python3 -I arbeid/hack/levering/frys_fasit.py > arbeid/hack/levering/frys_fasit_1600.sha256`

## Tillegg #2457 (smed3, 15:59): 3 kilder til NESTE_VERSJON inn, utkast_1100 ut
pakk_jury.sh kopierer nå `state/rapporter/c1_feil_per_gruppe.md`, `state/rapporter/arkitekt_c1_neste_versjon.md`
og `arbeid/oppgave_2274/feil_val2025.md` (bøtte b i c1_pekere_uten_sti.md), og find-kallet for c1/leveranse
har `-not -path "*/spor_npx/utkast_1100/*"` (2 filer ut). frys_fasit.py sin finn() speiler ekskluderingen.
Fasiten er laget på nytt: **113 filer** (112 + 3 − 2). frys_diff.sh mot ny zip og mot `--kilde`: FRYS LIK, 0 avvik.
Nye fingeravtrykk:
```
09885e99a9fea38b2185c4f14ba19b1477469edffc7e786692d7a2ac59639a5e  c1_stemmeagent/arbeid/oppgave_2274/feil_val2025.md
2e00fdea9a5838a13053393830f962686fe2477032be287418bc55e7d1c2471e  c1_stemmeagent/state/rapporter/arkitekt_c1_neste_versjon.md
0d0eeb0472b897c269583ee43fe43884b01e59719e95a8f59d2ccdf63c157660  c1_stemmeagent/state/rapporter/c1_feil_per_gruppe.md
```
Borte fra fasiten: `c1_stemmeagent/arbeid/hack/c1/leveranse/spor_npx/utkast_1100/README.md` og `.../kravrespons.md`.
