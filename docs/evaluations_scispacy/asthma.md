Berikut adalah hasil evaluasi entitas obat/kimia yang diekstraksi untuk konteks "Asthma" (Asma).

| No | Entitas | Frekuensi | Valid (Ya/Tidak) | Keterangan (Opsional) |
|---|---|---|---|---|
| 1 | nfa | 5 | **Tidak** | Ambigu/Singkatan tidak standar populer. Bisa merujuk pada *Niflumic Acid* (alat riset kanal klorida) atau singkatan non-obat. Bukan terapi standar asma. |
| 2 | steroids | 2 | **Ya** | Golongan obat utama untuk pereda inflamasi asma (Kortikosteroid). |
| 3 | ait | 1 | **Ya** | *Allergen Immunotherapy* (Imunoterapi alergen). Metode terapi yang valid untuk asma alergi. |
| 4 | icss | 1 | **Ya** | Kemungkinan jamak dari ICS (*Inhaled Corticosteroids*). Golongan obat utama asma. |
| 5 | labas | 1 | **Ya** | *Long-Acting Beta-Agonists*. Golongan obat bronkodilator jangka panjang. |
| 6 | lamas | 1 | **Ya** | *Long-Acting Muscarinic Antagonists*. Golongan obat bronkodilator. |
| 7 | hfa-134a | 1 | **Tidak** | Propelan (gas pendorong) dalam inhaler, bukan zat aktif terapeutik. |
| 8 | anti-ige | 1 | **Ya** | Terapi biologis (Monoclonal antibody) yang menargetkan IgE (contoh: Omalizumab). |
| 9 | anti-il5 | 1 | **Ya** | Terapi biologis yang menargetkan Interleukin-5 (contoh: Mepolizumab). |
| 10 | anti-tslp | 1 | **Ya** | Terapi biologis yang menargetkan *Thymic Stromal Lymphopoietin* (contoh: Tezepelumab). |
| 11 | leukotriene receptor antagonists | 1 | **Ya** | Golongan obat (contoh: Montelukast) untuk mencegah efek leukotrien. |
| 12 | mometasone furoate | 1 | **Ya** | Obat kortikosteroid inhalasi. |
| 13 | montelukast | 1 | **Ya** | Obat antagonis reseptor leukotrien (oral/tablet). |
| 14 | antihistamines | 1 | **Ya** | Golongan obat untuk meredakan gejala alergi yang sering menyertai asma. |
| 15 | levocetirizine | 1 | **Ya** | Obat antihistamin spesifik. |
| 16 | obe | 1 | **Tidak** | Kemungkinan singkatan dari *Obeticholic acid* (bukan obat asma) atau *Orange Berry Extract*? Terlalu ambigu/salah deteksi. |
| 17 | anti-asthma | 1 | **Tidak** | Deskriptor umum ("anti-asthma drugs"), bukan nama entitas kimia spesifik. |

---

**Ringkasan Evaluasi:**
*   **Total Valid:** 13 (Steroids, AIT, ICSS, LABAs, LAMAs, Anti-IgE, Anti-IL5, Anti-TSLP, Leukotriene Receptor Antagonists, Mometasone furoate, Montelukast, Antihistamines, Levocetirizine)
*   **Total Invalid:** 4 (NFA, HFA-134a, OBE, Anti-asthma)

**Catatan:**
*   Sistem sangat baik dalam mendeteksi **Singkatan Medis** (LABAs, LAMAs, ICS) yang merupakan istilah kunci dalam pengobatan asma.
*   Sistem juga berhasil mengenali **Terapi Biologis** modern (Anti-IgE, Anti-IL5, Anti-TSLP).
*   *False Positive* muncul pada propelan inhaler (HFA-134a) yang secara kimiawi valid tapi bukan obat.