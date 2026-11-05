# Diskrydding 05.11 (oppgave #2196): fra 4,2 GB til ca. 15 GB ledig

Fjernet (alt kan hentes igjen):
| Hva | Størrelse | Hente igjen |
|---|---|---|
| HF-cache: google/siglip2-so400m-patch16-512 | 4,6 GB | lastes ned automatisk ved første `from_pretrained`, eller `hf download google/siglip2-so400m-patch16-512` |
| HF-cache: facebook/dinov2-large | 1,2 GB | `hf download facebook/dinov2-large` |
| HF-cache: openai/clip-vit-large-patch14 | 1,7 GB | `hf download openai/clip-vit-large-patch14` |
| HF-cache: timm/vit_large_patch14_clip_224.openai | 1,7 GB | `hf download timm/vit_large_patch14_clip_224.openai` |
| HF-cache: imageomics/bioclip-2 | 1,7 GB | `hf download imageomics/bioclip-2` |
| Homebrew-cache (`brew cleanup -s`) | ~1 GB | lastes ned igjen ved neste brew install |

Hvorfor disse: bildemodeller brukt bare i øvelse 53 og bildeoppgaver (#1599, #1810, #1841), alle ferdige 04.11.
Case 1 er tekst og bruker ingen HF-modell (grep i arbeid/hack: ingen treff).

Ikke rørt: arbeid/hack/, dagens arbeid/oppgave_*, gemma-4 (Gemma Dev Agent er parkert, men kommer tilbake),
Qwen/bge/e5, uv-cachen (16 GB, men venv-ene deler blokker med den), nowiki_dump_smed3 (eier ukjent).

NB for neste rydder: HF-hub-en har egen dedup: store filer ligger i `~/.cache/huggingface/hub/blobs/<xx>/<hash>`
med en `.refs`-fil som sier hvilke modeller som bruker dem. Slett modellmappa OG blobber der alle refs peker på slettede modeller.
Neste kandidater ved behov: arbeid/nowiki_dump_smed3 (2,3 GB rå dump, spør smed3), mlx Qwen2.5-3B (1,75 GB).
