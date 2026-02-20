import sys
import os
import spacy
import json
from collections import Counter

try:
    # Try importing from current directory (if running as python extraction-eval.py)
    from search import searcher, build_query_string
except ImportError:
    # Try importing from scripts (if running from root as python scripts/extraction-eval.py)
    try:
        from scripts.search import searcher, build_query_string
    except ImportError:
        print("Error: Could not import 'search.py'. Run from project root or scripts folder.")
        sys.exit(1)

# Load ScispaCy model
try:
    # print("Loading ScispaCy model...", file=sys.stderr)
    nlp = spacy.load("en_ner_bionlp13cg_md")
except OSError:
    print("Model 'en_ner_bionlp13cg_md' not found.", file=sys.stderr)
    print("Please install: pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bionlp13cg_md-0.5.4.tar.gz", file=sys.stderr)
    sys.exit(1)

def extract_chemicals(text):
    doc = nlp(text)
    # Filter only SIMPLE_CHEMICAL entities
    chemicals = [ent.text.lower() for ent in doc.ents if ent.label_ == "SIMPLE_CHEMICAL"] # Lowercase for better grouping
    return chemicals

def generate_extraction_eval_prompt(query):
    # 1. Search Documents
    # Use built query string from search.py to match exact logic
    try:
        query_obj = build_query_string(query, auto_expand=True)
    except Exception as e:
        return f"Error building query: {e}"
        
    hits = searcher.search(query_obj, k=10)
    
    all_chemicals = []
    
    # print(f"Processing {len(hits)} documents...", file=sys.stderr)

    for hit in hits:
        # Get content
        try:
             # PySerini doc object, likely returns json string
            raw_doc = searcher.doc(hit.docid).raw()
            content = json.loads(raw_doc).get('contents', '')
        except:
             # Fallback
            if hasattr(searcher.doc(hit.docid), 'contents'):
                 content = searcher.doc(hit.docid).contents()
            else:
                 content = raw_doc
        
        # 2. Extract Entities
        chems = extract_chemicals(content)
        all_chemicals.extend(chems)

    # 3. Frequency Analysis
    chem_counts = Counter(all_chemicals)
    unique_chems = sorted(chem_counts.keys())

    # 4. Generate Prompt
    prompt = f"""
Konteks:
Sistem ekstraksi informasi obat menggunakan ScispaCy (model: en_ner_bionlp13cg_md).
Dokumen sumber adalah paper medis terkait penyakit: "{query}".
Tujuan adalah mengekstraksi nama OBAT, ZAT AKTIF, atau KELAS TERAPI (Farmakologis).

Tugas Anda sebagai Evaluator:
Berikut adalah daftar entitas "SIMPLE_CHEMICAL" yang dideteksi oleh sistem.
Tentukan apakah setiap entitas adalah VALID (obat/senyawa kimia relevan untuk terapi) atau INVALID (bukan obat, misal: elemen kimia umum, salah deteksi, atau istilah umum).

Berikan output dalam format Tabel Markdown:
| No | Entitas | Frekuensi | Valid (Ya/Tidak) | Keterangan (Opsional) |
|---|---|---|---|---|
"""
    
    for i, (chem, count) in enumerate(chem_counts.most_common()):
        prompt += f"| {i+1} | {chem} | {count} | ... | ... |\n"

    prompt += f"""
\n---
Total Entitas Unik Ditemukan: {len(unique_chems)}
Total Frekuensi Entitas: {len(all_chemicals)}

Instruksi Penilaian:
- Valid: Nama obat (Aspirin), Golongan obat (Antibiotics), Zat aktif (Metformin).
- Invalid: Unsur kimia tubuh (Oxygen, Sodium), Istilah umum (Patients, Water), Salah potong kata.
"""
    return prompt

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/extraction-eval.py <disease query>")
        print("Example: python scripts/extraction-eval.py \"Diabetes Type 2\"")
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])
    print(generate_extraction_eval_prompt(query))
