# Task List: Sistem Rekomendasi Obat

## 1. Setup Environment
- [ ] Buat `Dockerfile` (Python + Java untuk Pyserini)
- [ ] Buat `docker-compose.yml`
- [ ] Buat `requirements.txt` (pyserini, scispacy, dll)

## 2. Dataset
- [ ] Skrip fetch PubMed (5 tahun terakhir)
- [ ] Skrip preprocessing (cleaning, format JSONL)
- [ ] Download/generate dataset

## 3. Indexing (Pyserini)
- [ ] Skrip build inverted index dari JSONL
- [ ] Verifikasi index

## 4. Information Retrieval
- [ ] Modul query expansion (tambah treatment/pharmacotherapy/drug/therapy)
- [ ] Modul search BM25 (top-K retrieval)

## 5. Ekstraksi Entitas (scispaCy)
- [ ] Modul ekstraksi nama obat
- [ ] Modul ekstraksi zat aktif/senyawa kimia
- [ ] Modul ekstraksi dosis (opsional)

## 6. Agregasi & Scoring
- [ ] Frequency scoring obat dari top-K dokumen
- [ ] Ranking rekomendasi

## 7. Evaluasi
- [ ] Siapkan 10 query penyakit (sesuai prevalensi PHC)
- [ ] Evaluasi IR: hitung P@10
- [ ] Evaluasi ekstraksi: hitung Entity Precision

## 8. UI / Output
- [ ] Tampilkan daftar rekomendasi obat
- [ ] Tampilkan cuplikan kalimat sumber + tautan jurnal

---
