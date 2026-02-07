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
MODEL_NAME = "en_core_sci_sm"

# Load scispaCy model for NER
try:
    nlp = spacy.load(MODEL_NAME)
    print(f"Loaded model {MODEL_NAME}")
except:
    print(f"Warning: Model {MODEL_NAME} not found. Drug extraction will be limited.")
    nlp = None

def extract_drugs(text):
    if not nlp:
        return []
    doc = nlp(text)
    # Filter entities that are likely to be drugs/chemicals
    # In scispaCy, these are often labeled as 'CHEMICAL' or just generic entities
    # we can filter by looking for specific patterns or using a linker
    drugs = set()
    for ent in doc.ents:
        # Simple heuristic: often drugs are short or have specific suffixes
        # but here we just take the entities found by the biomedical model
        # You can refine this with more specific models like en_ner_bc5cdr_md
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
                # BM25 Search
                hits = searcher.search(query, k=10)
                
                for hit in hits:
                    # Pyserini stores the raw JSON if --storeRaw was used
                    import json
                    doc_data = json.loads(hit.raw)
                    
                    content = doc_data.get('contents', '')
                    title = content.split('. ')[0] if '. ' in content else content
                    
                    # Extract snippet (first 300 chars or around the query)
                    snippet = content
                    if len(snippet) > 300:
                        snippet = snippet[:300] + "..."
                    
                    # Highlight query in snippet (simple regex)
                    highlighted_snippet = re.sub(f"({re.escape(query)})", r'<mark>\1</mark>', snippet, flags=re.IGNORECASE)
                    
                    # Drug extraction from the full content
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
            error = "Index not found. Please run 'python preprocessing/build-index.py' first."

    return render_template('index.html', query=query, results=results, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
