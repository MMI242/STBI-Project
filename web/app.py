import os
import re
import json
from flask import Flask, render_template, request
from pyserini.search.lucene import LuceneSearcher
from pathlib import Path

app = Flask(__name__)

# --- KONFIGURASI ---
# Menggunakan path absolut relatif terhadap file ini
BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = BASE_DIR / 'indexes' / 'lucene-index-pubmed'
MODEL_NAME = "en_core_sci_sm"

# Load scispaCy model for NER
try:
    import spacy
    import scispacy
    nlp = spacy.load(MODEL_NAME)
    print(f"Loaded model {MODEL_NAME}")
except Exception as e:
    print(f"Warning: Could not load scispaCy model {MODEL_NAME}: {e}")
    print("Drug extraction will be disabled. Run: pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz")
    nlp = None

def extract_drugs(text):
    if not nlp:
        return []
    try:
        doc = nlp(text)
        # Ambil entitas yang terdeteksi oleh model scispaCy
        # Bisa difilter lebih lanjut jika menggunakan model spesifik seperti bc5cdr
        drugs = sorted(list(set([ent.text for ent in doc.ents])))
        return drugs[:10]  # Batasi 10 rekomendasi
    except Exception as e:
        print(f"Error during extraction: {e}")
        return []

def get_searcher():
    if not INDEX_PATH.exists():
        return None
    try:
        return LuceneSearcher(str(INDEX_PATH))
    except Exception as e:
        print(f"Error initializing searcher: {e}")
        return None

@app.route('/')
def index():
    query = request.args.get('q', '')
    results = []
    error = None
    
    if query:
        searcher = get_searcher()
        if searcher:
            try:
                # BM25 Search
                hits = searcher.search(query, k=10)
                
                for hit in hits:
                    # Ambil raw content (disimpan saat indexing dengan --storeRaw)
                    try:
                        doc_data = json.loads(hit.raw)
                    except:
                        # Fallback jika .raw tidak tersedia atau bukan JSON
                        doc_data = {"contents": hit.contents if hasattr(hit, 'contents') else "", "id": hit.docid, "year": "N/A"}
                    
                    content = doc_data.get('contents', '')
                    # Judul biasanya kalimat pertama (sebelum titik pertama)
                    title_match = re.split(r'\. ', content, maxsplit=1)
                    title = title_match[0] if title_match else "No Title"
                    
                    # Snippet: Ambil teks setelah judul atau awal teks
                    abstract = title_match[1] if len(title_match) > 1 else content
                    snippet = abstract[:400] + "..." if len(abstract) > 400 else abstract
                    
                    # Highlight query
                    highlighted_snippet = re.sub(f"({re.escape(query)})", r'<mark>\1</mark>', snippet, flags=re.IGNORECASE)
                    
                    # Ekstraksi rekomendasi obat
                    drugs = extract_drugs(content)
                    
                    results.append({
                        'id': hit.docid,
                        'title': title,
                        'year': doc_data.get('year', 'N/A'),
                        'snippet': highlighted_snippet,
                        'drugs': drugs
                    })
            except Exception as e:
                error = f"Search error: {str(e)}"
        else:
            error = f"Index tidak ditemukan di {INDEX_PATH}. Pastikan sudah menjalankan build-index.py."

    return render_template('index.html', query=query, results=results, error=error)

if __name__ == '__main__':
    # Pastikan templates folder ada
    os.makedirs(os.path.join(os.path.dirname(__file__), 'templates'), exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)