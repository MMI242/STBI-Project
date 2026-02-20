# otomatis generate prompt untuk kurasi
import sys
from search import main as search_main

def main(original_query, auto_expand=True):
    extended_query = f"{original_query} AND (treatment OR pharmacotherapy OR drug OR therapy)"
    query = f"""
Konteks:
Ini adalah hasil searching dengan lucene search pyserini.
Yang di cari adalah {original_query} , dengan query {extended_query}
index dibangun dari subdataset 1.5juta artikel PubMed dalam 5 tahun terakhir.

Tugas kamu adalah mengkurasikan hasil pencarian ini,
apakah sesuai atau tidak untuk masing-masing hasil pencarian.
Berikan jawaban dalam format:
Document ID: <docid>
Relevan: Ya/Tidak
Alasan: <alasan singkat>

hasil pencariannya adalah berikut ini:
{search_main(original_query, auto_expand=auto_expand)}
"""
    return query

if __name__ == "__main__":
    auto_expand = True
    if "--no-expand" in sys.argv:
        auto_expand = False
        sys.argv.remove("--no-expand")
    print(main(sys.argv[1:], auto_expand=auto_expand))