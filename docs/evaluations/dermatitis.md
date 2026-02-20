dieksekusi dengan `docker compose --profile search run --rm search python scripts/search-eval.py dermatitis`

## hasil
skor 0.9


## Asessmen gemini 3 pro:
Berikut adalah kurasi hasil pencarian untuk query `dermatitis` (khususnya dermatitis atopik) dengan filter treatment/therapy:

Document ID: 39551506
Relevan: Ya
Alasan: Laporan kasus ini membahas strategi penghentian dini inhibitor JAK oral pada remaja dengan dermatitis atopik parah melalui rawat inap, edukasi, dan optimalisasi terapi topikal.

Document ID: 39300482
Relevan: Ya
Alasan: Laporan kasus ini menyoroti efek samping potensial (eksaserbasi dermatitis wajah) setelah pengenalan obat abrocitinib (inhibitor JAK1 oral) pada pasien dengan dermatitis atopik.

Document ID: 39045804
Relevan: Ya
Alasan: Tinjauan ini mengeksplorasi hidrogel sebagai platform terapi yang menjanjikan untuk pengiriman obat pada penyakit kulit inflamasi seperti psoriasis dan dermatitis atopik.

Document ID: 39740342
Relevan: Ya
Alasan: Artikel ini membahas kemajuan dalam sistem penghantaran obat (seperti liposom, hidrogel, jarum mikro) untuk meningkatkan stabilitas dan bioavailabilitas pengobatan dermatitis atopik.

Document ID: 39515724
Relevan: Ya
Alasan: Tinjauan komprehensif ini mengeksplorasi lanskap perawatan dermatitis atopik, mencakup metode konvensional, terapi baru, dan strategi bioteknologi yang sedang berkembang (seperti biomaterial fungsional).

Document ID: 38541978
Relevan: Ya
Alasan: Studi ini bertujuan menyajikan profil keamanan dan efektivitas berbagai metode pengobatan biologis untuk terapi pruritus (gatal) pada dermatitis atopik.

Document ID: 39340696
Relevan: Ya
Alasan: Artikel ini merangkum pembelajaran utama dari pertemuan meja bundar para ahli dermatologi Asia mengenai pendekatan manajemen optimal untuk dermatitis atopik sedang hingga berat, termasuk penggunaan terapi sistemik lanjutan.

Document ID: 38229087
Relevan: Ya
Alasan: Studi analisis jaringan integratif ini bertujuan memprioritaskan obat-obatan potensial baru untuk dermatitis atopik melalui penemuan modul penyakit inti dan skrining virtual berbasis farmakofor.

Document ID: 39201826
Relevan: Ya
Alasan: Tinjauan naratif ini memberikan gambaran umum tentang terapi biologis dan molekul kecil yang baru disetujui FDA atau sedang dalam uji klinis untuk kondisi dermatologis pediatrik, termasuk dermatitis atopik.

Document ID: 39176344
Relevan: Tidak
Alasan: Laporan kasus ini membahas dermatitis makulopapular difus sebagai efek samping dari terapi deprivasi androgen (Leuprorelin Acetate) untuk kanker prostat. Ini adalah laporan tentang adverse event obat (drug reaction), bukan tentang pengobatan untuk penyakit dermatitis itu sendiri.

## prompt


    Konteks:
    Ini adalah hasil searching dengan lucene search pyserini.
    Yang di cari adalah ['dermatitis'] , dengan query ['dermatitis'] AND (treatment OR pharmacotherapy OR drug OR therapy)
    index dibangun dari subdataset 1.5juta artikel PubMed dalam 5 tahun terakhir.

    Tugas kamu adalah mengkurasikan hasil pencarian ini,
    apakah sesuai atau tidak untuk masing-masing hasil pencarian.
    Berikan jawaban dalam format:
    Document ID: <docid>
    Relevan: Ya/Tidak
    Alasan: <alasan singkat>

    hasil pencariannya adalah berikut ini:
    39551506 | 10.3830
    {
    "id" : "39551506",
    "contents" : "[HOSPITALIZATION, EDUCATION, AND OPTIMIZATION OF TOPICAL THERAPY CAN LEAD TO THE EARLY DISCONTINUATION OF ORAL JAK INHIBITORS IN ADOLESCENT SEVERE ATOPIC DERMATITIS].. In cases of moderate to severe atopic dermatitis that does not respond to topical therapy, temporary systemic administration of molecular targeted drugs (biological agents or oral Janus kinase[JAK]inhibitors) may be necessary. However, topical therapy forms the basis of the treatment for atopic dermatitis, and if topical therapy is appropriately established with long-term remission achieved, the use of molecular targeted drugs can be discontinued. In these two cases of severe adolescent atopic dermatitis, successful initiation of remission was achieved through hospitalization, disease education, skincare guidance, and the combined use of appropriate topical therapy and short-term oral JAK inhibitors during the remission induction phase. Subsequently, maintenance of remission was possible with proactive topical therapy alone. As there are many cases where molecular targeted drugs cannot be discontinued, presenting cases where oral JAK inhibitors were successfully discontinued emphasizes the avoidance of indiscriminate long-term use of molecular targeted drugs. This highlights the significance of topical therapy for atopic dermatitis and the importance of avoiding the careless use of molecular targeted drugs, and supporting the transition to adulthood.",
    "year" : 2024
    }
    39300482 | 10.1298
    {
    "id" : "39300482",
    "contents" : "Severe exacerbation of facial dermatitis with swelling following introduction of abrocitinib in a patient with atopic dermatitis.. Abrocitinib, an oral small-molecule Janus kinase 1 (JAK1) inhibitor, has been widely accepted for the treatment of moderate-to-severe atopic dermatitis (AD). Currently there is a paucity of data on the adverse events (AEs) after abrocitinib treatment, especially on rare events such as exacerbation of facial dermatitis, and their causal relationship and subsequent management remains poorly elucidated. A 43-year-old female patient with moderate AD received dupilumab after failure of topical treatments. Facial dermatitis persisted and became refractory after dupilumab treatment, and the patient changed treatment to oral abrocitinib. Fifteen hours after the first dose of abrocitinib, she developed exacerbation of facial dermatitis with swelling. The patient was initially diagnosed as abrocitinib-induced hypersensitivity. However, a score of 3 of the Naranjo adverse drug reaction assessment indicates week correlation between abrocitinib therapy and exacerbation of facial dermatitis, and negative results from subsequent drug provocation test further suggests no causal relationship. The present case report highlights the necessity of careful determination of abrocitinib-induced hypersensitivity, which should not be diagnosed simply based on the time sequence between drug exposure and symptom occurrence. In addition, caution should be exercised for drug withdrawal, especially when confirmative evidence is absent. Drug provocation test can be helpful and effective treatments could be continued unless severe AEs occur.",
    "year" : 2024
    }
    39045804 | 9.6017
    {
    "id" : "39045804",
    "contents" : "Hydrogels: a promising therapeutic platform for inflammatory skin diseases treatment.. Inflammatory skin diseases, such as psoriasis and atopic dermatitis, pose significant health challenges due to their long-lasting nature, potential for serious complications, and significant health risks, which requires treatments that are both effective and exhibit minimal side effects. Hydrogels offer an innovative solution due to their biocompatibility, tunability, controlled drug delivery capabilities, enhanced treatment adherence and minimized side effects risk. This review explores the mechanisms that guide the design of hydrogel therapeutic platforms from multiple perspectives, focusing on the components of hydrogels, their adjustable physical and chemical properties, and their interactions with cells and drugs to underscore their clinical potential. We also examine various therapeutic agents for psoriasis and atopic dermatitis that can be integrated into hydrogels, including traditional drugs, novel compounds targeting oxidative stress, small molecule drugs, biologics, and emerging therapies, offering insights into their mechanisms and advantages. Additionally, we review clinical trial data to evaluate the effectiveness and safety of hydrogel-based treatments in managing psoriasis and atopic dermatitis under complex disease conditions. Lastly, we discuss the current challenges and future opportunities for hydrogel therapeutics in treating psoriasis and atopic dermatitis, such as improving skin barrier penetration and developing multifunctional hydrogels, and highlight emerging opportunities to enhance long-term safety and stability.",
    "year" : 2024
    }
    39740342 | 9.5977
    {
    "id" : "39740342",
    "contents" : "Advances in Drug Delivery Systems for Atopic Dermatitis Treatment.. Atopic dermatitis (AD) is a chronic inflammatory skin disorder characterized by pruritus and impaired skin barrier function. Advances in drug delivery systems have transformed AD treatment by enhancing drug stability, bioavailability, and targeted delivery. Drug delivery systems such as liposomes, hydrogels, and microneedles enable deeper skin penetration, prolonged drug retention, and controlled release, reducing side effects and treatment frequency. Liposomes improve drug absorption and stability, while hydrogels offer high water content and responsive drug release. Microneedles facilitate painless, localized drug delivery, enhancing patient compliance. These systems address the limitations of traditional therapies like topical corticosteroids and systemic immunosuppressants, which are associated with adverse effects and poor patient adherence. Recent innovations include Janus kinase (JAK) inhibitors and biologics targeting immune pathways, demonstrating significant efficacy in reducing inflammation and symptoms. Drug delivery systems offer a safer, more efficient alternative for delivering these advanced therapies. By improving therapeutic outcomes and patient experience, drug delivery systems represent a crucial advancement in AD management.",
    "year" : 2024
    }
    39515724 | 9.5142
    {
    "id" : "39515724",
    "contents" : "Atopic dermatitis treatment: A comprehensive review of conventional and novel bioengineered approaches.. Atopic dermatitis (AD) remains a challenging condition, with conventional treatments often leading to adverse effects and limited efficacy. This review explores the diverse landscape of AD treatments, encompassing conventional methods, novel topical and systemic therapies, and emerging bioengineered strategies. While conventional drug administration often requires high dosages or frequent administration, leading to adverse effects, targeted biologics have shown promise. Phototherapy and wet wrap therapy, while helpful, have limitations. Given these factors, the need for modern and effective therapeutic strategies for AD is pressing. Complementary or alternative therapies have garnered significant attention in recent years as a compelling treatment for AD. Among these, functionalized biomaterials and textiles with physicochemical, nanotechnology-based characteristics, or bioengineered features are some of the most common typical adjuvant therapies. The multifunctional-engineered biomaterials, as a new generation of biomedical materials, and stem cells, seem to hold tremendous promise for the treatment of dermatological diseases like AD. Biomaterials have seen great success, especially in various medical fields, due to their unique and adaptable characteristics. These materials, including collagen, PCL, and PLGA, offer unique advantages, such as biocompatibility, biodegradability, controlled drug release, and enhanced drug retention.",
    "year" : 2024
    }
    38541978 | 9.4845
    {
    "id" : "38541978",
    "contents" : "The Efficacy and Effectiveness of the Biological Treatment of Pruritus in the Course of Atopic Dermatitis.. Atopic dermatitis is a heterogenous inflammatory disease with high variety in terms of clinical symptoms and etiopathogenesis, occurring both in pediatric and adult populations. The clinical manifestation of atopic dermatitis varies depending on the age of patients, but all age groups share certain common features, such as a chronic and recurrent course of disease, pruritus, and a co-occurrence of atopic diseases in personal or family medical history. Treating pruritus is a high priority due to its incidence rate in atopic dermatitis and substantial impact on quality of life. In recent years, treatments with biological drugs have increased the range of therapeutic possibilities in atopic dermatitis. The aim of the study is to present the safety profile, efficacy, and effectiveness of various biological treatment methods for the therapy of pruritus in the course of atopic dermatitis.",
    "year" : 2024
    }
    39340696 | 9.3320
    {
    "id" : "39340696",
    "contents" : "Advanced Systemic Treatments in Patients with Moderate-to-Severe Atopic Dermatitis: Key Learnings from Physicians Practicing in Nine Asian Countries and Territories.. Rapid progress made in the management of atopic dermatitis (AD) in recent years and the differences in patient journey between Asian and non-Asian populations call for a review of current atopic dermatitis landscape in Asia. A roundtable meeting with nine regional dermatological experts was held in June 2023 to discuss the optimal management approaches for moderate-to-severe AD, focusing on the use of advanced therapies. Disease burden on patients' quality of life, treatment adherence, and financial constraints were identified as major concerns when managing patients with moderate-to-severe AD in parts of Asia. It was agreed that the Hanifin and Rajka's criteria or the UK Working Party's Diagnostic Criteria for Atopic Dermatitis can be used to guide the clinical diagnosis of AD. Meanwhile, patient-reported outcome scales including the Dermatology Life Quality Index and Atopic Dermatitis Control Tool can be used alongside depression monitoring scales to monitor treatment outcomes in patients with AD, allowing a better understanding for individualized treatment. When managing moderate-to-severe AD, phototherapy should be attempted after failure with topical treatments, followed by conventional disease-modifying antirheumatic drugs and, subsequently, biologics or Janus kinase inhibitors. Systemic corticosteroids can be used as short-term therapy for acute flares. Although these advanced treatments are known to be effective, physicians have to take into consideration safety concerns and limitations when prescribing these treatments. Treatments in AD have evolved and its management varies country by country. Unique challenges across Asian countries necessitate a different management approach in Asian patients with AD.",
    "year" : 2024
    }
    38229087 | 9.3093
    {
    "id" : "38229087",
    "contents" : "Integrative network analysis suggests prioritised drugs for atopic dermatitis.. Atopic dermatitis (AD) is a prevalent chronic inflammatory skin disease whose pathophysiology involves the interplay between genetic and environmental factors, ultimately leading to dysfunction of the epidermis. While several treatments are effective in symptom management, many existing therapies offer only temporary relief and often come with side effects. For this reason, the formulation of an effective therapeutic plan is challenging and there is a need for more effective and targeted treatments that address the root causes of the condition. Here, we hypothesise that modelling the complexity of the molecular buildup of the atopic dermatitis can be a concrete means to drive drug discovery. We preprocessed, harmonised and integrated publicly available transcriptomics datasets of lesional and non-lesional skin from AD patients. We inferred co-expression network models of both AD lesional and non-lesional skin and exploited their interactional properties by integrating them with a priori knowledge in order to extrapolate a robust AD disease module. Pharmacophore-based virtual screening was then utilised to build a tailored library of compounds potentially active for AD. In this study, we identified a core disease module for AD, pinpointing known and unknown molecular determinants underlying the skin lesions. We identified skin- and immune-cell type signatures expressed by the disease module, and characterised the impaired cellular functions underlying the complex phenotype of atopic dermatitis. Therefore, by investigating the connectivity of genes belonging to the AD module, we prioritised novel putative biomarkers of the disease. Finally, we defined a tailored compound library by characterising the therapeutic potential of drugs targeting genes within the disease module to facilitate and tailor future drug discovery efforts towards novel pharmacological strategies for AD. Overall, our study reveals a core disease module providing unprecedented information about genetic, transcriptional and pharmacological relationships that foster drug discovery in atopic dermatitis.",
    "year" : 2024
    }
    39201826 | 9.2962
    {
    "id" : "39201826",
    "contents" : "Biologics and Small Molecule Targeted Therapies for Pediatric Alopecia Areata, Psoriasis, Atopic Dermatitis, and Hidradenitis Suppurativa in the US: A Narrative Review.. The management of pediatric dermatological conditions such as alopecia areata (AA), psoriasis, atopic dermatitis (AD), and hidradenitis suppurativa (HS) has significantly evolved with the introduction of biologics and small molecule targeted therapies. The advancement in understanding the immunopathogenesis of these chronic skin conditions has led to the development and approval of novel biologics and small molecule therapies. Initially approved by the United States Food and Drug Administration (FDA) for adults, most of these therapies are now being evaluated in clinical trials for safety and efficacy in adolescents and children, expanding new treatment options for pediatric patients. The role of the FDA in drug approval is multifaceted from drug inception, ensuring that research, data, and evidence show that the proposed drug is effective and safe for the intended use. The goal of this review article is to provide an overview of the recently FDA-approved and potential biologic and oral small molecule therapies in clinical trials for AA, psoriasis, AD, and HS in pediatric patients. The search for this review included keywords in ClinicalTrials.gov, PubMed, and Google Scholar for the latest research and clinical trials relevant to these conditions and treatments without the PRISMA methodology. For pediatric AA, ritlecitinib is FDA-approved, while baricitinib and updacitinib are in phase 3 clinical trials for pediatric approval. The FDA-approved drugs for pediatric psoriasis include secukinumab, ustekinumab, ixekizumab, etanercept, and apremilast. Other phase 3 clinical trials for pediatric psoriasis include risankizumab, guselkumab, tildrakizumab, brodalumab, and deucravacitinib. For pediatric AD, the FDA-approved drugs are dupilumab, tralokinumab, abrocitinib, and upadacitinib, with many other drugs in phase 3 trials. Adalimumab is an FDA-approved biologic for pediatric HS, with various clinical trials ongoing for adults. The approved biologics and small molecule therapies had higher efficacy and improved safety profiles compared to traditional medications. With numerous ongoing trials, the success of these clinical trials could lead to their inclusion in treatment guidelines for these chronic skin conditions. Biologics and small molecule therapies offer new avenues for effective disease management, enabling personalized therapeutic interventions and improving pediatric health outcomes.",
    "year" : 2024
    }
    39176344 | 9.1100
    {
    "id" : "39176344",
    "contents" : "Diffuse Maculopapular Dermatitis Associated With Leuprorelin Acetate Androgen Deprivation Therapy.. Androgen deprivation therapy (ADT) is one of the effective treatment methods for prostate cancer, often used with radiation therapy. Among the key ADT agents is leuprolide, a synthetic gonadotropin-releasing hormone agonist, which effectively suppresses testosterone production which is a requisite for the growth and division of prostate cancer cells. However, leuprolide is associated with several well-known side effects and less common dermatological reactions. In this case, we present an 80-year-old male patient with stage IIB prostate cancer who developed diffuse maculopapular dermatitis following leuprolide acetate ADT. The patient first experienced mild dermatitis following the fifth monthly 7.5 mg leuprolide injection before it developed into a general body rash after six injections. The dermatitis manifested on the patient's arms, thighs, calves, dorsum, and back of hands but sparing the abdomen, face, and neck. The pruritic dermatitis was managed successfully with a three-week course of prednisone which led to complete resolution without long-term sequelae. This case highlights the importance of recognizing and managing dermatological side effects associated with ADT. Clinicians should maintain an index of suspicion and act promptly when these side effects manifest. Systematic reporting and further research are essential to enhance patient safety and understanding of drug-related dermatological manifestations.",
    "year" : 2024
    }
