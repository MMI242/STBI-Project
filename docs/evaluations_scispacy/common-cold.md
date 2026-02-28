Berikut adalah hasil evaluasi entitas obat/kimia yang diekstraksi untuk konteks "Common Cold" (Pilek/Selesma).

| No | Entitas | Frekuensi | Valid (Ya/Tidak) | Keterangan (Opsional) |
|---|---|---|---|---|
| 1 | pseudoephedrine | 6 | **Ya** | Dekongestan oral untuk hidung tersumbat. |
| 2 | chlorphenamine | 5 | **Ya** | Antihistamin (generasi pertama) untuk gejala pilek/alergi. |
| 3 | gluconate | 4 | **Tidak** | Bagian garam anion (misal: Zinc Gluconate), bukan obatnya sendiri. |
| 4 | covid-19 | 4 | **Tidak** | Nama penyakit, bukan obat. (Salah deteksi entitas) |
| 5 | acetate | 3 | **Tidak** | Bagian garam anion (misal: Zinc Acetate). |
| 6 | xylometazoline hydrochloride | 3 | **Ya** | Dekongestan nasal (semprot hidung). |
| 7 | antihistamines | 2 | **Ya** | Golongan obat. |
| 8 | vitamins | 2 | **Ya** | Suplemen (Vitamin C, D) sering digunakan sebagai terapi suportif. |
| 9 | orotate | 2 | **Tidak** | Bagian garam kimia. |
| 10 | phenylephrine | 2 | **Ya** | Dekongestan. |
| 11 | transaminase | 2 | **Tidak** | Enzim tubuh (marker fungsi hati), bukan obat. |
| 12 | steroids | 2 | **Ya** | Golongan obat (kortikosteroid intranasal kadang digunakan). |
| 13 | otrivin | 2 | **Ya** | Merk dagang dari Xylometazoline. |
| 14 | pleconaril | 2 | **Ya** | Obat antivirus yang menargetkan rhinovirus (penyebab common cold). |
| 15 | broad-spectrum | 2 | **Tidak** | Kata sifat (spektrum luas), bukan entitas. |
| 16 | triple-drug | 2 | **Tidak** | Deskripsi kombinasi, bukan nama obat. |
| 17 | vasoconstrictors | 1 | **Ya** | Kelas farmakologis (mekanisme kerja dekongestan). |
| 18 | antihistamine | 1 | **Ya** | Golongan obat. |
| 19 | zinc | 1 | **Ya** | Mineral/Suplemen yang populer untuk memperpendek durasi pilek. |
| 20 | cinahl | 1 | **Tidak** | Database medis, bukan obat. |
| 21 | lilacs | 1 | **Tidak** | Database medis, bukan obat. |
| 22 | multivitamin | 1 | **Ya** | Suplemen terapi suportif. |
| 23 | lozenges | 1 | **Tidak** | Bentuk sediaan obat (permen hisap), bukan zat aktifnya. |
| 24 | fda | 1 | **Tidak** | Nama badan regulasi (Food and Drug Administration). |
| 25 | decongestants | 1 | **Ya** | Golongan obat utama untuk pilek. |
| 26 | minerals | 1 | **Ya** | Kategori suplemen (Zinc, Selenium). |
| 27 | tilorone | 1 | **Ya** | Obat antivirus sintetik/induser interferon. |
| 28 | nelfinavir | 1 | **Ya** | Antiretroviral (Protease inhibitor), kadang diuji untuk virus pernapasan. |
| 29 | aloe | 1 | **Ya** | Herbal (Aloe vera), sering digunakan dalam pengobatan tradisional. |
| 30 | ginger | 1 | **Ya** | Herbal (Jahe), pereda gejala pilek. |
| 31 | tannins | 1 | **Tidak** | Senyawa kimia tanaman umum (fitokimia), bukan obat spesifik dalam konteks ini. |
| 32 | alkaloids | 1 | **Tidak** | Golongan senyawa kimia tanaman umum. |
| 33 | terpenoids | 1 | **Tidak** | Golongan senyawa kimia tanaman umum. |
| 34 | flavonoids | 1 | **Tidak** | Golongan senyawa kimia tanaman umum. |
| 35 | zingiber officinale | 1 | **Ya** | Nama latin Jahe (sumber zat aktif). |
| 36 | single-agent | 1 | **Tidak** | Istilah deskriptif. |
| 37 | dual-drug | 1 | **Tidak** | Istilah deskriptif. |
| 38 | usfda | 1 | **Tidak** | Nama badan regulasi. |
| 39 | fixed-dose | 1 | **Tidak** | Istilah farmasi (dosis tetap). |
| 40 | paracetamol | 1 | **Ya** | Analgesik/Antipiretik untuk demam dan nyeri pilek. |
| 41 | chlorpheniramine | 1 | **Ya** | Sama dengan chlorphenamine (ejaan lain). |
| 42 | maleate | 1 | **Tidak** | Bagian garam (Chlorpheniramine Maleate). |

---

### Analisis Disambiguasi
1.  **Garam (Salt Forms):** *Gluconate, Acetate, Orotate, Maleate* ditandai **Invalid** karena mereka adalah anion pelengkap, bukan zat aktif utamanya (misal: Zinc Gluconate, Chlorpheniramine Maleate).
2.  **Senyawa Fitokimia Umum:** *Tannins, Alkaloids, Terpenoids, Flavonoids* ditandai **Invalid** karena merupakan kelas kimia yang terlalu luas, bukan obat spesifik.
3.  **Herbal:** *Aloe, Ginger, Zingiber officinale* ditandai **Valid** karena merupakan bahan aktif pengobatan herbal/tradisional yang umum.

### Perhitungan Presisi

*   **Total Entitas Unik:** 42
*   **Total Valid:** 22
    *   (Pseudoephedrine, Chlorphenamine, Xylometazoline HCl, Antihistamines, Vitamins, Phenylephrine, Steroids, Otrivin, Pleconaril, Vasoconstrictors, Antihistamine, Zinc, Multivitamin, Decongestants, Minerals, Tilorone, Nelfinavir, Aloe, Ginger, Zingiber officinale, Paracetamol, Chlorpheniramine)
*   **Total Invalid:** 20
    *   (Gluconate, Covid-19, Acetate, Orotate, Transaminase, Broad-spectrum, Triple-drug, Cinahl, Lilacs, Lozenges, FDA, Tannins, Alkaloids, Terpenoids, Flavonoids, Single-agent, Dual-drug, USFDA, Fixed-dose, Maleate)

$$	\text{Precision} = \frac{22}{42} \approx 0.52 \ (52\%)$$

**Kesimpulan:**
Sistem berhasil mendeteksi obat *Over-the-Counter* (OTC) utama untuk flu (Dekongestan, Antihistamin, Analgesik) dan herbal. Namun, presisi tergerus oleh deteksi potongan nama garam kimia dan istilah kimia umum tanaman.