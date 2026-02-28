## asessment Gemini 3 pro
Berikut adalah hasil evaluasi entitas obat/kimia yang diekstraksi untuk konteks "Pneumonia".

| No | Entitas | Frekuensi | Valid (Ya/Tidak) | Keterangan (Opsional) |
|---|---|---|---|---|
| 1 | methotrexate | 5 | **Ya** | Obat imunosupresan/kemoterapi. (Konteks: Pneumonia imbas obat atau pada pasien immunocompromised). |
| 2 | macrolide | 4 | **Ya** | Golongan antibiotik utama untuk pneumonia. |
| 3 | colistin | 3 | **Ya** | Antibiotik *last-resort* untuk bakteri gram negatif resisten. |
| 4 | covid-19 | 2 | **Tidak** | Nama penyakit/virus (salah deteksi entitas). |
| 5 | mtx | 1 | **Ya** | Singkatan Methotrexate. |
| 6 | antifolate | 1 | **Ya** | Kelas farmakologis (mekanisme kerja Methotrexate). |
| 7 | carboplatin | 1 | **Ya** | Obat kemoterapi. |
| 8 | paclitaxel | 1 | **Ya** | Obat kemoterapi. |
| 9 | second-line | 1 | **Tidak** | Deskripsi lini terapi, bukan nama obat. |
| 10 | tetracyclines | 1 | **Ya** | Golongan antibiotik. |
| 11 | doxycycline | 1 | **Ya** | Antibiotik untuk pneumonia atipikal. |
| 12 | minocycline | 1 | **Ya** | Antibiotik. |
| 13 | fluoroquinolones | 1 | **Ya** | Golongan antibiotik pernapasan (*respiratory fluoroquinolones*). |
| 14 | ciprofloxacin | 1 | **Ya** | Antibiotik. |
| 15 | levofloxacin | 1 | **Ya** | Antibiotik (*respiratory fluoroquinolone*). |
| 16 | corticosteroids | 1 | **Ya** | Golongan obat anti-inflamasi, tambahan terapi pada pneumonia berat. |
| 17 | ivig | 1 | **Ya** | *Intravenous Immunoglobulin* (Terapi imun). |
| 18 | corticosteroid | 1 | **Ya** | (Duplikasi entitas no 16). |
| 19 | intravenous methylprednisolone | 1 | **Ya** | Kortikosteroid spesifik. |
| 20 | macrolides | 1 | **Ya** | (Duplikasi entitas no 2). |
| 21 | non-fermenting | 1 | **Tidak** | Istilah mikrobiologi (*Non-fermenting gram-negative bacteria*). |
| 22 | [aor], | 1 | **Tidak** | *Garbage/Artifact* (*Adjusted Odds Ratio*). |
| 23 | imipenem-cilastatin | 1 | **Ya** | Antibiotik kombinasi (Carbapenem). |
| 24 | cefuroxime axetil | 1 | **Ya** | Antibiotik sefalosporin. |
| 25 | sulfamethoxazole-trimethoprim | 1 | **Ya** | Antibiotik kombinasi (Cotrimoxazole). |
| 26 | nitrofurantoin | 1 | **Ya** | Antibiotik (biasanya ISK, tapi terekstraksi sebagai obat). |
| 27 | acetaminophen | 1 | **Ya** | Analgesik/antipiretik (terapi suportif demam). |
| 28 | ursodiol | 1 | **Ya** | Obat batu empedu (Kemungkinan muncul dari komorbiditas pasien dalam paper). |

---

### Perhitungan Presisi

*   **Total Entitas Unik:** 28
*   **Total Valid:** 24
    *   (Methotrexate, Macrolide, Colistin, MTX, Antifolate, Carboplatin, Paclitaxel, Tetracyclines, Doxycycline, Minocycline, Fluoroquinolones, Ciprofloxacin, Levofloxacin, Corticosteroids, IVIG, Corticosteroid, Intravenous methylprednisolone, Macrolides, Imipenem-cilastatin, Cefuroxime axetil, Sulfamethoxazole-trimethoprim, Nitrofurantoin, Acetaminophen, Ursodiol)
*   **Total Invalid:** 4
    *   (Covid-19, Second-line, Non-fermenting, [aor],)

$$ \text{Precision} = \frac{24}{28} \approx 0.857 \ (85.7\%) $$

**Kesimpulan:**
Ekstraksi pada topik Pneumonia memiliki presisi yang **sangat tinggi (85,7%)**. ScispaCy berhasil mengidentifikasi berbagai kelas antibiotik yang sangat relevan (Makrolida, Fluorokuinoloa, Tetrasiklin) serta obat kemoterapi yang sering dikaitkan dengan risiko pneumonia pada pasien kanker. Kesalahan deteksi sangat minimal.

## prompt


Konteks:
Sistem ekstraksi informasi obat menggunakan ScispaCy (model: en_ner_bionlp13cg_md).
Dokumen sumber adalah paper medis terkait penyakit: "pneumonia".
Tujuan adalah mengekstraksi nama OBAT, ZAT AKTIF, atau KELAS TERAPI (Farmakologis).

Tugas Anda sebagai Evaluator:
Berikut adalah daftar entitas "SIMPLE_CHEMICAL" yang dideteksi oleh sistem.
Tentukan apakah setiap entitas adalah VALID (obat/senyawa kimia relevan untuk terapi) atau INVALID (bukan obat, misal: elemen kimia umum, salah deteksi, atau istilah umum).

Berikan output dalam format Tabel Markdown:
| No | Entitas | Frekuensi | Valid (Ya/Tidak) | Keterangan (Opsional) |
|---|---|---|---|---|
| 1 | methotrexate | 5 | ... | ... |
| 2 | macrolide | 4 | ... | ... |
| 3 | colistin | 3 | ... | ... |
| 4 | covid-19 | 2 | ... | ... |
| 5 | mtx | 1 | ... | ... |
| 6 | antifolate | 1 | ... | ... |
| 7 | carboplatin | 1 | ... | ... |
| 8 | paclitaxel | 1 | ... | ... |
| 9 | second-line | 1 | ... | ... |
| 10 | tetracyclines | 1 | ... | ... |
| 11 | doxycycline | 1 | ... | ... |
| 12 | minocycline | 1 | ... | ... |
| 13 | fluoroquinolones | 1 | ... | ... |
| 14 | ciprofloxacin | 1 | ... | ... |
| 15 | levofloxacin | 1 | ... | ... |
| 16 | corticosteroids | 1 | ... | ... |
| 17 | ivig | 1 | ... | ... |
| 18 | corticosteroid | 1 | ... | ... |
| 19 | intravenous methylprednisolone | 1 | ... | ... |
| 20 | macrolides | 1 | ... | ... |
| 21 | non-fermenting | 1 | ... | ... |
| 22 | [aor], | 1 | ... | ... |
| 23 | imipenem-cilastatin | 1 | ... | ... |
| 24 | cefuroxime axetil | 1 | ... | ... |
| 25 | sulfamethoxazole-trimethoprim | 1 | ... | ... |
| 26 | nitrofurantoin | 1 | ... | ... |
| 27 | acetaminophen | 1 | ... | ... |
| 28 | ursodiol | 1 | ... | ... |


---
Total Entitas Unik Ditemukan: 28
Total Frekuensi Entitas: 38
Presisi:

Rumus metrik:
$$\text{Precision} = \frac{\text{Banyak entitas obat valid}}{\text{Total entitas yang diekstraksi}}$$


Instruksi Penilaian:
- Valid: Nama obat (Aspirin), Golongan obat (Antibiotics), Zat aktif (Metformin).
- Invalid: Unsur kimia tubuh (Oxygen, Sodium), Istilah umum (Patients, Water), Salah potong kata.

