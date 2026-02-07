import os
import gzip
import json
import re
import requests
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

# --- KONFIGURASI ---
START_INDEX = 1274  # Mulai dari file Baseline 2025 terakhir
BASE_URL_TEMPLATE = "https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/pubmed25n{:04d}.xml.gz"
OUTPUT_FILE = Path("processed/pubmed_2020_2025.jsonl")
TEMP_DIR = Path("temp")
TARGET_MIN_YEAR = 2020  # Kita ingin data dari 2020 ke atas (2019 ke bawah DIBUANG)
STOP_THRESHOLD_YEAR = 2019 # Jika max year dalam satu file < 2020, kita stop.

# Buat folder jika belum ada
os.makedirs(OUTPUT_FILE.parent, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

def clean_text(text):
    if not text: return ""
    return re.sub(r'\s+', ' ', text).strip()

def get_year_from_article(article_elem):
    """Mencoba mengekstrak tahun dari berbagai format XML PubMed"""
    try:
        journal_issue = article_elem.find("Journal/JournalIssue/PubDate")
        if journal_issue is None: return 0
        
        # Coba tag <Year>
        year_node = journal_issue.find("Year")
        if year_node is not None and year_node.text:
            return int(year_node.text)
        
        # Coba tag <MedlineDate> (contoh: "2020 Jan-Feb")
        medline_date = journal_issue.find("MedlineDate")
        if medline_date is not None and medline_date.text:
            match = re.search(r'\d{4}', medline_date.text)
            if match:
                return int(match.group(0))
    except:
        return 0
    return 0

def process_single_file(file_index):
    url = BASE_URL_TEMPLATE.format(file_index)
    filename = os.path.basename(url)
    temp_path = os.path.join(TEMP_DIR, filename)
    
    print(f"\n[{file_index}] Mendownload: {url} ...")
    
    # 1. DOWNLOAD
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(temp_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    except Exception as e:
        print(f"   [!] Gagal download: {e}")
        return None

    # 2. PARSE & EXTRACT
    print(f"   -> Memproses & Filtering (Hanya Tahun >= {TARGET_MIN_YEAR})...")
    saved_count = 0
    discarded_count = 0
    years_in_file = []
    
    # Mode append 'a' agar data tidak tertimpa saat loop file berikutnya
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f_out:
        try:
            with gzip.open(temp_path, 'rb') as f_in:
                context = ET.iterparse(f_in, events=("end",))
                for event, elem in context:
                    if elem.tag == "PubmedArticle":
                        try:
                            # Ekstrak Metadata
                            medline = elem.find("MedlineCitation")
                            article = medline.find("Article")
                            pmid = medline.find("PMID").text
                            
                            year = get_year_from_article(article)
                            
                            # Simpan statistik tahun untuk menentukan kapan harus stop
                            if year > 0:
                                years_in_file.append(year)
                            
                            # Filter: Hanya simpan jika >= 2020
                            # (LOGIKA UTAMA: Dokumen 2019 kebawah otomatis terbuang di sini)
                            if year >= TARGET_MIN_YEAR:
                                title = article.find("ArticleTitle").text or ""
                                abstract_node = article.find("Abstract")
                                abstract_text = ""
                                if abstract_node is not None:
                                    texts = [t.text for t in abstract_node.findall("AbstractText") if t.text]
                                    abstract_text = " ".join(texts)
                                
                                full_content = clean_text(f"{title}. {abstract_text}")
                                
                                if len(full_content) > 50:
                                    doc = {
                                        "id": pmid,
                                        "contents": full_content,
                                        "year": year
                                    }
                                    f_out.write(json.dumps(doc) + '\n')
                                    saved_count += 1
                            elif year > 0:
                                discarded_count += 1
                                    
                        except:
                            pass
                        elem.clear() # Bebaskan memori
        except Exception as e:
            print(f"   [!] Error parsing GZIP: {e}")

    # 3. CLEANUP
    # os.remove(temp_path)
    
    # 4. REPORT & DECISION
    if not years_in_file:
        return {"max_year": 0, "saved": 0}
        
    max_year = max(years_in_file)
    min_year = min(years_in_file)
    
    print(f"   -> Selesai file ini. Disimpan: {saved_count} dokumen.")
    print(f"   -> Dibuang (<{TARGET_MIN_YEAR}): {discarded_count} dokumen.")
    print(f"   -> Rentang Tahun di file ini: {min_year} s.d {max_year}")
    
    return {"max_year": max_year, "saved": saved_count, "discarded": discarded_count}

def main():
    # Hapus file output lama jika ada, agar bersih
    # Hapus baris di bawah ini jika ingin melanjutkan download sebelumnya (append)
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
        
    current_index = START_INDEX
    grand_total_saved = 0  # Variabel Akumulasi Total
    grand_total_discarded = 0

    print(f"Memulai Download & Ekstraksi PubMed (Target: Tahun {TARGET_MIN_YEAR}+)")
    print("Tekan Ctrl+C kapan saja untuk berhenti dan melihat total.")
    print("="*60)
    
    try:
        while current_index > 0:
            stats = process_single_file(current_index)
            
            if stats is None:
                print("   [!] Skip file ini karena error download.")
                current_index -= 1
                continue
            
            # --- Update Total Dokumen ---
            grand_total_saved += stats['saved']
            grand_total_discarded += stats['discarded']
            print(f"   [INFO] Total Akumulasi Dokumen Tersimpan: {grand_total_saved:,}")
            print(f"   [INFO] Total Akumulasi Dokumen Dibuang (<{TARGET_MIN_YEAR}): {grand_total_discarded:,}")

            # --- LOGIKA STOP ---
            if stats['max_year'] > 0 and stats['max_year'] < TARGET_MIN_YEAR:
                print("\n" + "="*50)
                print(f"STOPPING CRITERIA MET!")
                print(f"File n{current_index:04d} memiliki tahun terbaru {stats['max_year']}.")
                print(f"Ini lebih tua dari target {TARGET_MIN_YEAR}. Proses Download Selesai.")
                print("="*50)
                break
                
            current_index -= 1

    except KeyboardInterrupt:
        print("\n\n" + "!"*50)
        print("PROSES DIHENTIKAN OLEH PENGGUNA (Ctrl+C)")
        print("!"*50)
    
    # Laporan Akhir
    print(f"\nDataset Final Tersedia di: {OUTPUT_FILE}")
    print(f"TOTAL DOKUMEN VALID ({TARGET_MIN_YEAR}-2025) DISIMPAN: {grand_total_saved:,}")
    print(f"TOTAL DOKUMEN DIBUANG (<{TARGET_MIN_YEAR}): {grand_total_discarded:,}")

if __name__ == "__main__":
    main()

