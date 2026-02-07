1. eksekusi preparedata.py (ctrl-c manual setelah data kebanyakan +- 1juta proposal)
2. Dataset jadi: `processed/pubmed_2020_2025.jsonl`

## file yang sudah jadi
di google drive: TBD (baru upload) (2GB)

### Format json
```json
{"id": "12345678", "contents": "Article Title. Abstract text here...", "year": 2023}
```

**Fields:**

| Field | Tipe | Deskripsi |
|-------|------|-----------|
| `id` | string | PMID (PubMed ID) |
| `contents` | string | Gabungan `{title}. {abstract}` yang sudah di-clean |
| `year` | int | Tahun publikasi (>= 2020) |

**Note:**
- Hanya artikel dengan `year >= 2020` yang disimpan
- Hanya artikel dengan `contents` > 50 karakter yang disimpan
- Text sudah dinormalisasi (whitespace dirapikan)
