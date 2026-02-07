import os
import re
from flask import Flask, render_template, request
from pyserini.search.lucene import LuceneSearcher
import spacy
import scispacy
from scispacy.abbreviation import AbbreviationDetector
from scispacy.linking import EntityLinker

app = Flask(__name__)

# --- KONFIGURASI ---
INDEX_PATH = 'indexes/lucene-index-pubmed'
# Using BioNLP13CG (Broad Biomedical)
MODEL_NAME = "en_ner_bionlp13cg_md"

# Load scispaCy model for NER
try:
    nlp = spacy.load(MODEL_NAME)
    print(f"Loaded model {MODEL_NAME}")
except:
    print(f"Warning: Model {MODEL_NAME} not found. please install it.")
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
            # Filter out short acronyms (e.g., "AIT", "ICS") if needed
            if len(ent.text) < 4:
                continue
                
            drugs.add(ent.text)
    return list(drugs)[:10] # Limit to 10 unique entities

def get_searcher():
    if not os.path.exists(INDEX_PATH):
        print(f"Error: Index not found at {INDEX_PATH}")
        return None
    return LuceneSearcher(INDEX_PATH)

@app.route('/')
def index():
    query = request.args.get('q', '')
    results = []
    error = None
    
    if query:
        searcher = get_searcher()
        if searcher:
            try:
                # Simple Query Expansion
                expanded_query = f"{query} AND (treatment OR pharmacotherapy OR drug OR therapy)"
                print(f"Searching for: {expanded_query}")
                
                # BM25 Search
                hits = searcher.search(expanded_query, k=10)
                
                all_drugs = []
                
                for hit in hits:
                    import json
                    # ScoredDoc doesn't have .raw, need to fetch doc first
                    doc = searcher.doc(hit.docid)
                    if not doc:
                        continue
                    doc_data = json.loads(doc.raw())
                    
                    content = doc_data.get('contents', '')
                    title = content.split('. ')[0] if '. ' in content else content
                    
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
            error = "Index not found. Please run 'python preprocessing/build-index.py' first."

    return render_template('index.html', query=query, results=results, recommended_drugs=recommended_drugs if 'recommended_drugs' in locals() else [], error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
