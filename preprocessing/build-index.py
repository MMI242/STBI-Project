import sys
import subprocess
import os

def build_index():
    # Define paths relative to project root
    # script is in preprocessing/, so we step up one level for root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    input_dir = os.path.join(base_dir, "preprocessing", "dataset", "processed")
    index_dir = os.path.join(base_dir, "indexes", "lucene-index-pubmed")
    
    print(f"Base Dir: {base_dir}")
    print(f"Input Dir: {input_dir}")
    print(f"Index Dir: {index_dir}")
    
    # Check input
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return

    # Construct Pyserini command
    # Using python -m pyserini.index.lucene
    cmd = [
        sys.executable, "-m", "pyserini.index.lucene",
        "--collection", "JsonCollection",
        "--input", input_dir,
        "--index", index_dir,
        "--generator", "DefaultLuceneDocumentGenerator",
        "--threads", "4",  # Increased threads since we have full dataset
        "--storePositions", "--storeDocvectors", "--storeRaw",
        "--compress", # compress index
        "--optimize", #
    ]
    
    print(f"Executing: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True)
        print("Indexing completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Indexing failed: {e}")

if __name__ == "__main__":
    build_index()
