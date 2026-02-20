import sys
import subprocess
import os
from pathlib import Path

import requests

def build_index():
    # Define paths relative to project root
    # script is in preprocessing/, so we step up one level for root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    input_dir = Path(base_dir) / "preprocessing" / "dataset" / "processed"
    index_dir = Path(base_dir) / "indexes" / "lucene-index-pubmed"
    input_dir.mkdir(parents=True, exist_ok=True)
    index_dir.mkdir(parents=True, exist_ok=True)

    print(f"Base Dir: {base_dir}")
    print(f"Input Dir: {input_dir}")
    print(f"Index Dir: {index_dir}")
    
    # check apakah input_dir sudah punya file https://drive.google.com/file/d/1MPhn4gNCMapH-ddtw3jxzIZwpzLyTfex/view?usp=sharing
    # bila belum download
    file_name = "pubmed_2020_2025.jsonl"
    file_path = input_dir / file_name
    
    if file_path.exists():
        print(f"Input directory '{input_dir}' already has the dataset.")
    else:
        print(f"Input directory '{input_dir}' is empty. Downloading dataset...")
        url = "https://github.com/MMI242/STBI-Project/releases/download/dataset/pubmed_2020_2025.jsonl"
        
        # Download with stream=True to handle large files (2GB) without high memory usage
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    
        print("Dataset downloaded successfully.")
    
    # Construct Pyserini command
    # Using python -m pyserini.index.lucene
    cmd = [
        sys.executable, "-m", "pyserini.index.lucene",
        "--collection", "JsonCollection",
        # pyserini JsonCollection expects a folder containing .json or .jsonl files
        "--input", str(input_dir), 
        "--index", str(index_dir),
        "--generator", "DefaultLuceneDocumentGenerator",
        "--threads", "4",  # Increased threads since we have full dataset
        "--storePositions",  # Menyimpan posisi kata (untuk phrase query).
        "--storeDocvectors", # Menyimpan vektor dokumen (untuk query expansion/RM3).
        "--storeRaw",  # Menyimpan teks asli dokumen (boros tempat)

        # dibuat agar bisa diaktifkan/dinonaktifkan dengan argument pemanggilan
        # "--optimize", # Merges index segments for better performance and slightly smaller size
        # "--compress", # compress index
    ]
    # tambah flag untuk pyserini.
    # misal tambah optimize atau compress, panggil
    # `build-index.py --optimize --compress`
    cmd.extend([args for args in sys.argv[1:] if args.startswith("--")])
    
    print(f"Executing: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True)
        print("Indexing completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Indexing failed: {e}")

if __name__ == "__main__":
    build_index()
