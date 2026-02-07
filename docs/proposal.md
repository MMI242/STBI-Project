Draf Proposal: Sistem Rekomendasi Obat

## Pendahuluan

### Latar Belakang

Ketika melakukan rekomendasi obat, tenaga medis harus memberi keputusan berdasarkan bukti ilmiah terbaru. Sementara itu, volume publikasi ilmiah di dunia medis senantiasa bertambah setiap tahunnya. Platform seperti PubMed menyimpan jutaan abstrak jurnal, namun tenaga medis seringkali kesulitan menemukan informasi spesifik mengenai efektivitas suatu obat di tengah tumpukan data yang masif tersebut.

Pencarian manual memakan waktu yang lama, sementara kebutuhan terkait dengan keputusan medis seringkali bersifat mendesak. Selain itu, risiko terjadi kesalahan informasi medis juga sangatlah tinggi jika mengandalkan mesin pencari umum. Oleh karena itu, pengembangan aplikasi sistem Information Retrieval (IR) yang terfokus untuk menyaring literatur ilmiah medis sangatlah diperlukan. Sistem IR diusulkan dirancang untuk menyajikan rekomendasi dalam bentuk yang terstruktur dan mudah dipahami. Alasan mengapa aplikasi ini perlu dibuat adalah:

1. Publikasi ilmiah meningkat setiap tahun (overload informasi).
2. Rekomendasi obat harus didasarkan bukti ilmiah terbaru.
3. Perlunya efisiensi waktu bagi tenaga medis untuk menentukan keputusan.
4. Menggunakan Pyserini sebagai alat indexing dan perangkingan dalam konteks dokumen ilmiah dapat memberikan hasil yang lebih akurat dibanding pencarian umum (Google).
5. Urgensi Precision Medicine: kebutuhan untuk melakukan pencarian yang lebih spesifik berdasarkan entitas medis (gejala dan zat kimia) untuk mendukung ketepatan dosis dan jenis terapi.

### Rumusan Masalah

1. Bagaimana membangun sistem Information Retrieval yang mampu menyaring ribuan abstrak jurnal medis untuk menemukan korelasi antara penyakit dan terapi obat?
2. Bagaimana menerapkan algoritma BM25 untuk menghasilkan urutan dokumen yang memiliki relevansi tinggi terhadap gejala atau penyakit tertentu?
3. Bagaimana mengekstraksi entitas obat dari dokumen yang relevan untuk memberikan rekomendasi yang terstruktur?

### Tujuan Penelitian

1. Mengimplementasikan framework Pyserini dengan algoritma BM25 untuk melakukan indexing dan retrieval dokumen medis dari dataset PubMed secara efisien.
2. Mengembangkan modul ekstraksi obat dari dokumen hasil pencarian teratas (top-$K$ retrieval) menggunakan scispaCy (https://github.com/allenai/scispacy).
3. Mengevaluasi performa sistem dalam menyajikan dokumen dengan metrik Precision@$K$, dan akurasi ekstraksi entitas obat menggunakan metrik Entity Precision.
4. Menghasilkan prototipe sistem rekomendasi obat dengan Evidence-Based Medicine yang menyajikan kutipan referensi ilmiah sebagai alat bantu bagi tenaga medis.

### Batasan Masalah

1. Hanya mengambil informasi dari abstrak jurnal.
2. Rekomendasi obat diberikan berdasarkan frekuensi dan relevansi literatur, bukan diagnosis.
3. Dataset yang digunakan adalah subset PubMed (batasi 5 tahun terakhir).

## Tinjauan Pustaka

Akhir-akhir ini, pertumbuhan publikasi jurnal medis meningkat pesat. Darici (2025) menemukan bahwa volume publikasi jurnal medis berbahasa Inggris meningkat 30,38% di 10 tahun terakhir. Pada penelitian lainnya, Gomez dkk. (2022) menyatakan bahwa pertumbuhan publikasi medis peer-reviewed dalam dekade terakhir (dari 2013) adalah sebesar 9,42% per tahun. Pertumbuhan yang terus meningkat ini menyediakan potensi yang besar bagi tenaga medis untuk mendapatkan informasi medis dari penelitian scientific yang telah dipublikasikan. Akan tetapi, pertumbuhan volume informasi yang terus meningkat ini justru memunculkan tantangan baru yang dikenal dengan information overload. Arnold dkk. (2023) menegaskan bahwa digitalisasi dan penggunaan teknologi informasi yang tidak terkelola dapat memperparah kondisi information overload, sehingga diperlukan intervensi struktural melalui desain teknologi yang tepat untuk mengatasinya. Dalam bidang medis, ketiadaan alat penyaring yang efektif membuat tenaga kesehatan kesulitan memilah bukti ilmiah yang relevan di tengah tumpukan data yang besar.

Untuk menjawab tantangan tersebut, perlu dikembangkan sistem temu balik informasi (Information Retrieval) dengan algoritma pembobotan yang mampu membedakan relevansi dokumen secara akurat, bukan sekadar mencari dokumen yang mengulang kata kunci paling banyak sebagaimana yang dilakukan pada algoritma TF-IDF. TF-IDF klasik memiliki kelemahan utama yaitu asumsi linearitas frekuensi kata. Dalam TF-IDF, sebuah dokumen yang memiliki kata “aspirin” sebanyak 50 kali akan mendapatkan skor yang jauh lebih tinggi daripada dokumen yang menyebutkan kata tersebut sebanyak 5 kali, seolah relevansinya sepuluh kali lipat. Padahal dalam konteks rekomendasi obat, setelah abstrak menyebutkan nama obat beberapa kali, penyebutan tambahan tidak lagi memberikan informasi baru yang signifikan. BM25 mengatasi masalah ini melalui fitur term frequency saturation yang dikendalikan oleh parameter $k_1$. Kurva skor saturasi ini memastikan bahwa dampak dari pengulangan kata akan melandai (plateau) setelah titik tertentu. Hal ini mencegah sistem bias terhadap artikel yang bersifat repetitif, dan memprioritaskan dokumen yang mengandung cakupan istilah kueri yang lebih lengkap (Zhang, 2021).

Selain tantangan volume data, hambatan lainnya adalah kesulitan pengguna dalam mengusulkan kata kunci atau membuat query yang tepat. Seringkali istilah yang digunakan pengguna berbeda dengan terminologi spesifik yang tertulis dalam literatur ilmiah. Oleh karena itu, teknik Query Expansion juga perlu diterapkan. Dalam studi kasus pada korpus medis MEDLINE, penerapan Query Expansion terbukti secara signifikan meningkatkan efisiensi penemuan dokumen relevan dengan cara menjembatani kesenjangan istilah antara kueri awam dan teks scientific (Rivas et al., 2014).

BM25 memberikan solusi untuk menemukan dokumen yang relevan sebagai langkah awal. Hasil pencarian ini masih membebani tenaga medis untuk membaca untuk mendapatkan informasi obat terkait terapi medis yang dilakukan. Untuk mengubah sekumpulan dokumen menjadi daftar rekomendasi yang praktis dan terstruktur, diperlukan teknologi Natural Language Processing (NLP). NLP dapat digunakan untuk mengenali entitas kimia. Tugas ekstraksi entitas ini dapat dilakukan dengan library scispaCy. scispaCy merupakan alat berbasis spaCy yang dioptimalkan untuk teks biomedis, juga telah diterapkan dalam dunia medis, seperti obat-obatan dan penyakit yang berguna untuk membangun sistem rekomendasi berbasis teks (Neumann et al., 2019). scispaCy dengan kemampuan memproses natural language medis dapat diintegrasikan dengan baik untuk menyaring dan mengkategorikan informasi medis yang relevan dalam sistem rekomendasi obat (Jolly et al., 2024).

Berdasarkan pembahasan masalah dan tinjauan teknologi di atas, penelitian ini hendak mengintegrasikan kedua pendekatan tersebut ke dalam sebuah aplikasi Sistem Rekomendasi Obat. Dengan menggabungkan pendekatan algoritma BM25 untuk IR dan kemampuan ekstraksi entitas dengan scispaCy, sistem ini dirancang untuk membantu tenaga medis menangani permasalahan information overload. Sistem yang diusulkan memberikan keluaran nama-nama obat maupun zat aktif serta tautan ke jurnal ilmiah yang relevan. Sistem ini bukanlah pengganti dokter, namun sebagai alat bantu bagi dokter dan tenaga medis untuk memberikan terapi obat dan mempelajarinya.

## Metode Penelitian

### Dataset

Penelitian ini menggunakan subset dataset abstrak jurnal medis dari PubMed dengan batasan publikasi 5 tahun terakhir.

Dataset melalui proses pembersihan untuk menghapus karakter non-text, stopwords, dan menstandarisasi format teks agar hasil indexing lebih optimal.

### Pengembangan Sistem

Sistem yang dikembangkan menerima input gejala penyakit atau nama penyakit, dan memberikan keluaran rekomendasi obat serta tautan/kutipan jurnal terkait. Sistem memiliki alur penggunaan dan tahapan proses yang divisualisasikan pada diagram berikut.

#### Tahap 1: IR

**Pembuatan Indeks**

Menggunakan framework Pyserini untuk membangun inverted index dari kumpulan data abstrak. Hal ini memungkinkan pencarian kata kunci dengan cepat pada dokumen berskala besar.

**Ekspansi Query dan IR**

1. Input dari pengguna berupa gejala penyakit.
2. Query secara otomatis diperkaya dengan penambahan terminologi medis seperti treatment / pharmacotherapy.
3. Contoh query: $\text{\{query\_user\}} \;\text{AND}\; (\text{treatment OR pharmacotherapy OR drug OR therapy})$.

**IR**

1. Ranking hasil pencarian dengan BM25.
2. Diambil top-$K$ (10) dokumen teratas.

#### Tahap 2: Ekstraksi

**Ekstraksi Entitas Obat**

Teks abstrak dari 10 dokumen teratas dipindai menggunakan tool NLP scispaCy. Sistem mengekstraksi informasi yang relevan berupa:

1. Nama obat generic/non-generic.
2. Bahan aktif (senyawa kimia).
3. Dosis.

**Agregasi**

1. Frequency scoring: menghitung bobot masing-masing obat berdasarkan frekuensi kemunculan pada 10 dokumen teratas. Obat yang direkomendasikan di banyak jurnal mendapat peringkat lebih tinggi.
2. Visualisasi hasil dengan menunjukkan daftar rekomendasi obat dan cuplikan kalimat sumber dari jurnal beserta tautannya.

### Evaluasi Sistem

#### Evaluasi Information Retrieval

Evaluasi bagian pertama (IR) dilakukan untuk mengukur kemampuan sistem Pyserini+BM25 dalam menyajikan dokumen yang memuat informasi terapi obat. Metrik yang digunakan adalah Precision@10 (P@10). Prosedur yang dilakukan adalah sebagai berikut:

1. Sistem diuji dengan 10 query penyakit.
2. Untuk masing-masing query, diambil top-10 hasil pencarian.
3. Top-10 untuk masing-masing query kemudian dinilai secara manual (peneliti sebagai assessor), diberi skor 1 bila relevan dan 0 bila tidak relevan.

Rumus:

$$
	ext{P@10} = \frac{\text{jumlah dokumen relevan di top-10}}{10}
$$

Metrik keseluruhan = mean(P@10).

Penentuan 10 kueri penyakit didasarkan pada prevalensi penyakit di layanan kesehatan primer (PHC) menurut studi epidemiologi terbaru (Albalawi et al., 2024) untuk memastikan evaluasi sistem memiliki relevansi klinis yang tinggi. Berdasarkan data prevalensi tersebut, kueri dibagi menjadi:

1. Penyakit pernapasan (22,5%): Common Cold, Asthma, Pneumonia.
2. Penyakit kardiovaskular (18,3%): Hypertension, Hyperlipidemia.
3. Gangguan endokrin (15,8%): Type 2 Diabetes Mellitus.
4. Kondisi muskuloskeletal (15,2% pada wanita): Osteoarthritis.
5. Kondisi dermatologis (pasien muda): Dermatitis.
6. Kesehatan mental (7,6% pada wanita): Depressive Disorder.
7. Beban penyakit umum PHC: GERD.

#### Evaluasi Tahap 2 (Ekstraksi)

Evaluasi bagian kedua (ekstraksi) dilakukan dengan menggunakan Entity Precision untuk mengukur akurasi scispaCy dalam membedakan entitas obat dengan selain obat. Tahapan evaluasi adalah sebagai berikut:

1. Dapatkan daftar kata yang dianggap obat dari dokumen yang relevan dari sistem.
2. Dilakukan validasi manual, diberi label Valid bila merupakan nama obat atau zat aktif, dan Invalid bila berupa kata selain entitas obat.

Rumus metrik:

$$
	ext{Precision} = \frac{\text{jumlah entitas obat valid}}{\text{total entitas yang diekstraksi}}
$$

## Daftar Pustaka
Darıcı, S. (2025). Artificial Intelligence and Medicine 2014-2024: Bibliometric Analysis and Global Impacts . Journal of Intelligent Decision Making and Information Science, 2, 250–271. https://doi.org/10.59543/jidmis.v2i.13525, (mirror1) (archive.org)

De Andrade Gomes, J., Braga, L. A. M., Cabral, B. P., Lopes, R. M., & Mota, F. B. (2024). Problem-Based Learning in Medical Education: A Global Research Landscape of the Last Ten Years (2013-2022). Medical science educator, 34(3), 551–560. https://doi.org/10.1007/s40670-024-02003-1

Arnold, M., Goldschmitt, M., & Rigotti, T. (2023). Dealing with information overload: a comprehensive review. Frontiers in psychology, 14, 1122200. https://doi.org/10.3389/fpsyg.2023.1122200

Rivas, A. R., Iglesias, E. L., & Borrajo, L. (2014). Study of query expansion techniques and their application in the biomedical information retrieval. TheScientificWorldJournal, 2014, 132158. https://doi.org/10.1155/2014/132158

Neumann M, et al. ScispaCy: Fast and Robust Models for Biomedical Natural Language Processing. ACL. 2019.
https://doi.org/10.48550/arXiv.1902.07669 

Jolly A, et al. Exploring Biomedical Named Entity Recognition via SciSpaCy and BioBERT. 2024.
https://doi.org/10.2174/0118741207289680240510045617

Zhang, Z. (2021). An improved BM25 algorithm for clinical decision support in precision medicine based on co-word analysis and cuckoo search. BMC Medical Informatics and Decision Making, 21, 81. https://doi.org/10.1186/s12911-021-01454-5

Albalawi, N. M. ., Alatawi, A. A. . F. ., GHURM S, A. D., hzazi , F. ahmed, & Alatawi, F. A. . . (2024). Patterns of Common Diseases in Primary Health Care Settings: A Cross-Sectional Study. Journal of Ecohumanism, 3(8), 14449 –. https://doi.org/10.62754/joe.v3i8.6760
