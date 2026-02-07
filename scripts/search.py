from sys import argv
from pyserini.search.lucene import LuceneSearcher


searcher = LuceneSearcher('indexes/lucene-index-pubmed')

def main(query):
    hits = searcher.search(f"{query} AND (treatment OR pharmacotherapy OR drug OR therapy)", k=10)

    hasil = ""
    for hit in hits:
        hasil += f"{hit.docid} | {hit.score:.4f}\n"
        doc = searcher.doc(hit.docid)
        hasil += doc.raw() + "\n"  # JSON lengkap
    return hasil

if __name__ == "__main__":
    # Ambil query dari argumen atau input interaktif
    if len(argv) > 1:
        query = " ".join(argv[1:])
    else:
        query = input("Masukkan query penyakit: ")
    print(main(query))
