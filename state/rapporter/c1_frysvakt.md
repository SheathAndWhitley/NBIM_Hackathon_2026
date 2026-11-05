# Case 1: frysvakt kl. 16 (arkitekt #2142)

**Hva:** `arbeid/verktoy/c1_frys.py` tar sha256 av den frosne modellen #2044 miks h2 og agenten, og stopper kald start hvis noe endres etter frys.

**Filer som fryses (9):** oppgave_2044/train.py, oppgave_2044/pred_miks_h2.csv, oppgave_2103/full_test.csv, hack/levering/kjor_agent.py, hack/levering/c1_real.py, hack/levering/kjor_agent_real_maskin_alene.csv, oppgave_2047/vern.py, oppgave_2046/case1_mot.py, state/opplastet/20261105_114241_real_votes.csv. Modellen trenes ved kjøring (runpy av train.py), så koden, dataene og prediksjonene *er* modellen.

**Kl. 16.00:** LaunchAgent `no.landsby.c1frys` kjører `c1_frys.py frys`, som skriver `state/c1_frys.json`. Den overskriver aldri en eksisterende frys (bare `--tving`). Står Minien i dvale, kjører launchd jobben når den våkner. Kommer frysen ikke: `python3 arbeid/verktoy/c1_frys.py frys` for hånd.

**Sjekk, koblet inn:**
- `arbeid/hack/c1/kaldstart.sh`: før steg 1. Ved avvik: «RØD FRYSVAKT», utgang 4.
- `arbeid/hack/levering/fremmed.sh`: før kopiering. Ved avvik: «FRYSVAKT RØD», utgang 4.
- `tavle.py status`: tom før frys. Etter frys vises «Frysvakt: 9 filer uendret» eller «!! FRYSVAKT: … train.py ENDRET».
- Før frys gir sjekken utgang 0 med «ikke frosset ennå». Dommeren bør kjøre `c1_frys.py sjekk --krev` kl. 19.30 (#1972), så en manglende frys også stopper.

**Test (kopi i /tmp, egen frysfil):** før frys: utgang 0, med --krev 2. Frys: 9 filer. Andre frys rørte ikke fila. Sjekk på kopien og på landsbyen: GRØNN. Etter endret train.py og slettet full_test.csv: RØD med begge filene listet, utgang 2. Når frysfila peker på en endret train.py (C1_FRYS=tmp), stopper kaldstart.sh og fremmed.sh med utgang 4 før kopiering, og tavla viser !!. Uten frys gikk kaldstart.sh GRØNN (F1_MOT 0,476190, 69 s) og fremmed.sh med TALLVAKT GRØNN, så ingenting er brutt.

**Merk:** etter kl. 16 må retting av f.eks. sitater i `kjor_agent.py` eller `c1_real.py` få ja fra dommeren og ny frys (`--tving`). Det er meningen, for prediksjonene kommer fra disse filene.
