# Diskrydding 2026-11-05 (#2400): 19 GB slettet fra HF-cachen, disken har nå 25 GB ledig

**Før:** 6,2 GB ledig av 228 GB. **Etter:** 25 GB ledig (`df -h /`). ~/.cache/huggingface gikk fra 19 GB til 218 MB.

## Hvorfor det var trygt
- Case 1 bruker ingen HF-modeller: grep etter alle 13 modellnavn og etter `SentenceTransformer|from_pretrained|huggingface|mlx_lm|HF_HOME`
  i arbeid/hack, arbeid/smed2_c1, arbeid/smed2_hack*, arbeid/oppgave_2* ga 0 treff (utenom .venv/uv.lock).
  Eneste treff på noe modellnavn var bge-small i arbeid/hack_arkiv (arkiv), og den beholdt jeg.
- Ingen symlenker fra arbeid/verktoy/modeller_lokalt eller arbeid/kandidater peker inn i cachen, og ingen blob hadde hardlenker.
- `lsof` viste ingen prosess som hadde filer i cachen åpne.
- Ingenting i arbeid/hack, frosne filer eller andres arbeidsmapper er rørt.

## Slettet (modellmappe + blob-ene den pekte på i hub/blobs/)
| Modell | MB |
|---|---|
| mlx-community/gemma-4-e4b-it-4bit | 4939 |
| BAAI/bge-reranker-base | 3203 |
| Qwen/Qwen2.5-1.5B | 2955 |
| mlx-community/Qwen2.5-3B-4bit | 1666 |
| BAAI/bge-large-en-v1.5 | 1279 |
| intfloat/e5-large-v2 | 1279 |
| Qwen/Qwen2.5-0.5B | 953 |
| allenai/specter2_base | 839 |
| answerdotai/ModernBERT-base | 572 |
| sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 471 |
| intfloat/multilingual-e5-small | 465 |
| BAAI/bge-base-en-v1.5 | 418 |
| intfloat/e5-base-v2 | 418 |
| **Sum** | **~19 450** |

**Beholdt:** BAAI/bge-small-en-v1.5 og sentence-transformers/all-MiniLM-L6-v2 (sammen ~215 MB, alle snapshot-lenker sjekket hele).

## Rulle tilbake
Alt kan lastes ned igjen, f.eks. `hf download mlx-community/gemma-4-e4b-it-4bit`. Gemma (Gemma Dev Agent, parkert)
og Qwen (mulig Name that LLM) må hentes på nytt når de sporene starter.

Merk: cachen hadde et uvanlig oppsett (store blob-er flyttet til delte hub/blobs/<xx>/ og lenket fra models--X/blobs/). Den gjenværende cachen bruker fortsatt det oppsettet.
