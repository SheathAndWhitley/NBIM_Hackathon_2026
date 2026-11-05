"""Lager ordklasse-lista som bygges inn i injeksjon_hoflig.py (#2265). Kilde: wordfreq (zipf, engelsk) og WordNet
(dominerende ordklasse etter lemma-tellinger). Beholder ord med zipf >= 4.0 som IKKE er substantiv-dominante:
r = adverb, a = adjektiv, v = verb, - = ikke i WordNet (lukket ordklasse: which, against, ...).
Utfil: arbeid/oppgave_2265/ordklasser.txt (ord<TAB>zipf*10<TAB>klasse), og blob til innbygging."""
import os, re, zlib, base64
from collections import Counter
os.environ.setdefault("NLTK_DATA", os.path.join(os.path.dirname(__file__), "nltk_data"))
from wordfreq import top_n_list, zipf_frequency
from nltk.corpus import wordnet as wn
ut = []
for w in top_n_list("en", 60000):
    if not re.fullmatch(r"[a-z]{2,}", w): continue
    z = zipf_frequency(w, "en")
    if z < 4.0: continue
    c = Counter()
    for s in wn.synsets(w):
        for l in s.lemmas(): c[s.pos().replace("s", "a")] += l.count() + 0.01
    k = c.most_common(1)[0][0] if c else "-"
    if k != "n": ut.append(f"{w}\t{round(z * 10)}\t{k}")
d = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(d, "ordklasser.txt"), "w").write("\n".join(ut) + "\n")
blob = base64.b64encode(zlib.compress("\n".join(ut).encode(), 9)).decode()
open(os.path.join(d, "ordklasser_blob.txt"), "w").write(blob)
print(len(ut), "ord, blob", len(blob), "tegn", Counter(x.split("\t")[2] for x in ut))
