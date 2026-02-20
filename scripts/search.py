from sys import argv
from pyserini.search.lucene import LuceneSearcher
from jnius import autoclass

searcher = LuceneSearcher('indexes/lucene-index-pubmed')

def build_query_string(query):
    """
    Fungsi ini membersihkan query input dan membangun string query untuk Lucene.
    Query yang dibangun akan menggabungkan query asli dengan filter untuk mencari artikel yang relevan
    Menggunakan jqueryparser dan jenglishanalyzer agar query tidak diproses sebagai Bags of Words, melainkan sebagai frase yang utuh.
    """
    if isinstance(query, list):
        query = " ".join(query)
    
    query_bersih = query.replace("[", "").replace("]", "").replace("'", "").replace('"', "").replace(",", "")
    query_bersih = " ".join(query_bersih.split())

    lucene_query_str = f'("{query_bersih}") AND (treatment OR pharmacotherapy OR drug OR therapy)'
    print(f"Melakukan pencarian dengan string query: {lucene_query_str}")
    
    # Panggil class Java dari Lucene secara langsung
    JString = autoclass('java.lang.String')
    JQueryParser = autoclass('org.apache.lucene.queryparser.classic.QueryParser')
    JEnglishAnalyzer = autoclass('org.apache.lucene.analysis.en.EnglishAnalyzer')
    
    # Gunakan Java EnglishAnalyzer
    analyzer = JEnglishAnalyzer()
    parser = JQueryParser(JString("contents"), analyzer)
    
    try:
        query_obj = parser.parse(JString(lucene_query_str))
        print(f"Query berhasil diparse menjadi objek Lucene: {query_obj.toString()}")
    except Exception as e:
        raise ValueError(f"Error saat mem-parsing query: {e}")
    return query_obj


def main(query):
    hits = searcher.search(build_query_string(query), k=10)

    hasil = ""
    for hit in hits:
        hasil += f"{hit.docid} | {hit.score:.4f}\n"
        doc = searcher.doc(hit.docid)
        hasil += doc.raw() + "\n"  
    return hasil

if __name__ == "__main__":
    if len(argv) > 1:
        query = " ".join(argv[1:])
    else:
        query = input("Masukkan query penyakit: ")
        
    print(main(query))