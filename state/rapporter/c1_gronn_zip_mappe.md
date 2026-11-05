# Case 1 (#2522): hver grønne jury-zip lagres fast i state/levering/c1_gronn/

- Nytt: `arbeid/hack/levering/lagre_gronn.sh <zip>` kopierer til `state/levering/c1_gronn/jurypakke_c1_<HHMM>_<HEAD>.zip`
  (løpenummer om navnet finnes), sjekker SHA etter kopi, legger «sha  fil  tid» til `SHA256.txt` og peker `SISTE_GRONNE.zip` på kopien. Sletter aldri.
- `sluttsjekk.sh` steg 8 kaller den bare når steg 1-6 er grønne (rød går ut med 4 før). Feil i lagringen gir ADVARSEL i GRØNN-linja, ikke rød.
- Prøvekjøring 16:34 (MAAL /tmp/c1_sluttsjekk_smed4_2522): utgang 0, F1 MOT 0.476190,
  lagret `jurypakke_c1_1634_2f24f0c.zip`, sha256 d1b900112a0b4620ac64671aa335a14bb53509c41fb4a61415ca6f7c5911db64 = SISTE_GRONNE.zip.
- Funnet underveis: første kjøring var RØD i 3b tallsjekk: «sak 2511» i JURY_SPORSMAL.md:62 (min tekst fra #2516). Rettet til «sak #2511» (tallsjekken hopper over #-referanser). Tallsjekk 0 ikke funnet etterpå.
- Forbehold: zipen bygges fra arbeidstreet, så `<HEAD>` i navnet er HEAD ved lagring, ikke garanti for ren HEAD. frys_fasit_1600.sha256 har ukommitterte endringer fra andre og er ikke rørt; JURY_SPORSMAL-linja der må regenereres i #2519.
