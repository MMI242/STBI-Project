## asessment gemini3pro
Berikut adalah hasil evaluasi entitas obat/kimia yang diekstraksi untuk konteks "Hyperlipidemia" (Hiperlipidemia/Kolesterol Tinggi).

| No | Entitas | Frekuensi | Valid (Ya/Tidak) | Keterangan (Opsional) |
|---|---|---|---|---|
| 1 | statins | 13 | **Ya** | Golongan obat utama penurun kolesterol (HMG-CoA reductase inhibitors). |
| 2 | ezetimibe | 8 | **Ya** | Obat penghambat penyerapan kolesterol. |
| 3 | omt | 4 | **Tidak** | Singkatan *"Optimal Medical Therapy"*, bukan zat kimia. |
| 4 | triglycerides | 3 | **Tidak** | Target terapi (lemak darah), bukan obat. |
| 5 | simvastatin | 3 | **Ya** | Obat golongan statin. |
| 6 | fibrates | 2 | **Ya** | Golongan obat penurun trigliserida. |
| 7 | lipid | 2 | **Tidak** | Kategori senyawa biokimia umum. |
| 8 | cholesterol | 2 | **Tidak** | Target terapi, senyawa tubuh. |
| 9 | ldl-c | 1 | **Tidak** | Biomarker (kolesterol jahat), bukan obat. |
| 10 | triglyceride | 1 | **Tidak** | Target terapi. |
| 11 | bile acid sequestrants | 1 | **Ya** | Golongan obat (Resin pengikat asam empedu). |
| 12 | fibrate | 1 | **Ya** | Golongan obat (singular). |
| 13 | lomitapide | 1 | **Ya** | Obat untuk Hiperkolesterolemia Familial (MTP inhibitor). |
| 14 | apoc-iii | 1 | **Tidak** | Protein target terapi, bukan obatnya (kecuali jika disebut "ApoC-III inhibitor"). |
| 15 | acat2 | 1 | **Tidak** | Enzim target, bukan obat. |
| 16 | haart | 1 | **Tidak** | Singkatan regimen terapi (*Highly Active Antiretroviral Therapy*), bukan nama kimia tunggal. |
| 17 | darunavir | 1 | **Ya** | Obat HIV (penyebab dislipidemia sekunder). |
| 18 | atazanavir | 1 | **Ya** | Obat HIV. |
| 19 | disoproxil fumarate | 1 | **Ya** | Bagian dari garam obat (Tenofovir Disoproxil Fumarate), muncul dalam konteks efek samping metabolik. |
| 20 | nevirapine | 1 | **Ya** | Obat HIV. |
| 21 | rilpivirine | 1 | **Ya** | Obat HIV. |
| 22 | lipid-lowering | 1 | **Tidak** | Kata sifat (*adjective*), bukan entitas. |
| 23 | single-agent | 1 | **Tidak** | Deskripsi terapi. |
| 24 | ldl | 1 | **Tidak** | Lipoprotein (target). |
| 25 | hdl | 1 | **Tidak** | Lipoprotein. |
| 26 | nonsteroidal anti-inflammatory | 1 | **Ya** | Golongan obat (Mungkin referensi silang komorbiditas). |
| 27 | opioids | 1 | **Ya** | Golongan obat. |
| 28 | non-hdl | 1 | **Tidak** | Parameter lab. |

---

### Perhitungan Presisi

*   **Total Entitas Unik:** 28
*   **Total Valid:** 14
    *   (Statins, Ezetimibe, Simvastatin, Fibrates, Bile acid sequestrants, Fibrate, Lomitapide, Darunavir, Atazanavir, Disoproxil fumarate, Nevirapine, Rilpivirine, Nonsteroidal anti-inflammatory, Opioids)
*   **Total Invalid:** 14
    *   (OMT, Triglycerides, Lipid, Cholesterol, LDL-C, Triglyceride, ApoC-III, ACAT2, HAART, Lipid-lowering, Single-agent, LDL, HDL, Non-HDL)

$$ \text{Precision} = \frac{14}{28} = 0.5 \ (50\%) $$

**Kesimpulan:**
Presisi model pada topik ini cukup rendah **(50%)**. ScispaCy kesulitan membedakan antara **Obat** (Statin, fibrate) dengan **Target Biologis/Lemak** (Cholesterol, LDL, Triglyceride) karena keduanya memiliki label `SIMPLE_CHEMICAL`. Selain itu, banyak obat HIV (Antiretroviral) terdeteksi karena paper tentang hiperlipidemia sering membahas efek samping metabolik dari terapi HIV.


## prompt


Konteks:
Sistem ekstraksi informasi obat menggunakan ScispaCy (model: en_ner_bionlp13cg_md).
Dokumen sumber adalah paper medis terkait penyakit: "hyperlipidemia".
Tujuan adalah mengekstraksi nama OBAT, ZAT AKTIF, atau KELAS TERAPI (Farmakologis).

Tugas Anda sebagai Evaluator:
Berikut adalah daftar entitas "SIMPLE_CHEMICAL" yang dideteksi oleh sistem.
Tentukan apakah setiap entitas adalah VALID (obat/senyawa kimia relevan untuk terapi) atau INVALID (bukan obat, misal: elemen kimia umum, salah deteksi, atau istilah umum).

Berikan output dalam format Tabel Markdown:
| No | Entitas | Frekuensi | Valid (Ya/Tidak) | Keterangan (Opsional) |
|---|---|---|---|---|
| 1 | statins | 13 | ... | ... |
| 2 | ezetimibe | 8 | ... | ... |
| 3 | omt | 4 | ... | ... |
| 4 | triglycerides | 3 | ... | ... |
| 5 | simvastatin | 3 | ... | ... |
| 6 | fibrates | 2 | ... | ... |
| 7 | lipid | 2 | ... | ... |
| 8 | cholesterol | 2 | ... | ... |
| 9 | ldl-c | 1 | ... | ... |
| 10 | triglyceride | 1 | ... | ... |
| 11 | bile acid sequestrants | 1 | ... | ... |
| 12 | fibrate | 1 | ... | ... |
| 13 | lomitapide | 1 | ... | ... |
| 14 | apoc-iii | 1 | ... | ... |
| 15 | acat2 | 1 | ... | ... |
| 16 | haart | 1 | ... | ... |
| 17 | darunavir | 1 | ... | ... |
| 18 | atazanavir | 1 | ... | ... |
| 19 | disoproxil fumarate | 1 | ... | ... |
| 20 | nevirapine | 1 | ... | ... |
| 21 | rilpivirine | 1 | ... | ... |
| 22 | lipid-lowering | 1 | ... | ... |
| 23 | single-agent | 1 | ... | ... |
| 24 | ldl | 1 | ... | ... |
| 25 | hdl | 1 | ... | ... |
| 26 | nonsteroidal anti-inflammatory | 1 | ... | ... |
| 27 | opioids | 1 | ... | ... |
| 28 | non-hdl | 1 | ... | ... |


---
Total Entitas Unik Ditemukan: 28
Total Frekuensi Entitas: 57
Presisi:

Rumus metrik:
$$\text{Precision} = \frac{\text{Banyak entitas obat valid}}{\text{Total entitas yang diekstraksi}}$$


Instruksi Penilaian:
- Valid: Nama obat (Aspirin), Golongan obat (Antibiotics), Zat aktif (Metformin).
- Invalid: Unsur kimia tubuh (Oxygen, Sodium), Istilah umum (Patients, Water), Salah potong kata.

