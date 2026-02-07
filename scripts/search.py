from sys import argv
from pyserini.search.lucene import LuceneSearcher


searcher = LuceneSearcher('indexes/lucene-index-pubmed')

# Ambil query dari argumen atau input interaktif
if len(argv) > 1:
    query = " ".join(argv[1:])
else:
    query = input("Masukkan query penyakit: ")

hits = searcher.search(f"{query} AND (treatment OR pharmacotherapy OR drug OR therapy)", k=10)

for hit in hits:
    print(f"{hit.docid} | {hit.score:.4f}")
    doc = searcher.doc(hit.docid)
    print(doc.raw())  # JSON lengkap