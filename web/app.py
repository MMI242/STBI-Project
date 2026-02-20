import os
import re
import json
from flask import Flask, render_template, request
from pyserini.search.lucene import LuceneSearcher
from pathlib import Path
import sys

app = Flask(__name__)

# --- KONFIGURASI ---
# Menggunakan path absolut relatif terhadap file ini
BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = BASE_DIR / 'indexes' / 'lucene-index-pubmed'
# Using BioNLP13CG (Broad Biomedical)
MODEL_NAME = "en_ner_bionlp13cg_md"

scripts_dir = BASE_DIR / 'scripts'
sys.path.append(str(scripts_dir))
from search import build_query_string

# Load scispaCy model for NER
try:
    import spacy
    import scispacy
    try:
        # Cara 1: Load via pintasan nama string (standard spaCy)
        nlp = spacy.load(MODEL_NAME)
    except OSError:
        # Cara 2: Import sebagai modul (fallback jika linking gagal)
        # Nama package pip untuk model ini biasanya menggunakan underscore
        import en_ner_bionlp13cg_md
        nlp = en_ner_bionlp13cg_md.load()
        
    print(f"Loaded model {MODEL_NAME}")
except Exception as e:
    print(f"Warning: Failed to load model {MODEL_NAME}. Error: {e}")
    nlp = None

def extract_drugs(text):
    if not nlp:
        return []
    doc = nlp(text)
    drugs = set()
    for ent in doc.ents:
        # BioNLP13CG uses "SIMPLE_CHEMICAL" for drugs/chemicals
        # We also keep "CHEMICAL" just in case, and "DRUG"
        if ent.label_ in ["SIMPLE_CHEMICAL", "CHEMICAL", "DRUG"]:
            if len(ent.text) < 3:
                continue
                
            drugs.add(ent.text)
    return list(drugs)[:10] # Limit to 10 unique entities

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
                
                # query expandsion dan advanced parsing di build_query_string
                query_obj = build_query_string(query)
                # BM25 Search
                hits = searcher.search(query_obj, k=10)
                
                all_drugs = []
                
                for hit in hits:
                    import json
                    # ScoredDoc doesn't have .raw, need to fetch doc first
                    doc = searcher.doc(hit.docid)
                    if not doc:
                        continue
                    doc_data = json.loads(doc.raw())
                    
                    content = doc_data.get('contents', '')
                    # Judul biasanya kalimat pertama (sebelum titik pertama)
                    title_match = re.split(r'\. ', content, maxsplit=1)
                    title = title_match[0] if title_match else "No Title"
                    
                    snippet = content
                    if len(snippet) > 300:
                        snippet = snippet[:300] + "..."
                    
                    highlighted_snippet = re.sub(f"({re.escape(query)})", r'<mark>\1</mark>', snippet, flags=re.IGNORECASE)
                    
                    # Drug extraction from the full content
                    drugs_in_doc = extract_drugs(content)
                    
                    results.append({
                        'id': hit.docid,
                        'title': title,
                        'year': doc_data.get('year', 'N/A'),
                        'snippet': highlighted_snippet,
                        'drugs': drugs_in_doc
                    })
                    
                    # Collect for aggregation (using a set per doc to count DOCUMENT frequency, not term frequency)
                    # "menghitung berapa kali obat itu disebutkan di antara 10 jurnal berbeda"
                    unique_drugs_in_doc = set(drugs_in_doc)
                    all_drugs.extend(unique_drugs_in_doc)
                
                # Aggregation & Ranking
                from collections import Counter
                drug_counts = Counter(all_drugs)
                # Sort by frequency (desc), then name
                recommended_drugs = sorted(drug_counts.items(), key=lambda x: (-x[1], x[0]))
                
            except Exception as e:
                error = f"Search error: {str(e)}"
        else:
            error = f"Index tidak ditemukan di {INDEX_PATH}. Pastikan sudah menjalankan build-index.py."

    return render_template('index.html', query=query, results=results, recommended_drugs=recommended_drugs if 'recommended_drugs' in locals() else [], error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
