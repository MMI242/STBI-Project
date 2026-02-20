dieksekusi dengan `docker compose --profile search run --rm search python scripts/search-eval.py osteoarthritis`

## hasil
skor 1


## Asessmen gemini 3 pro:
Berikut adalah kurasi hasil pencarian untuk query `osteoarthritis` dengan filter treatment/therapy:

Document ID: 38938057
Relevan: Ya
Alasan: Ulasan naratif ini memberikan gambaran tentang farmakoterapi saat ini dan yang sedang berkembang (seperti penghambat NGF, saluran ion, dan antagonis CGRP) untuk mengelola nyeri terkait osteoartritis.

Document ID: 38596341
Relevan: Ya
Alasan: Studi ini menyelidiki potensi injeksi intra-artikular protein ribosom L35 (RPL35) sebagai terapi potensial baru untuk pencegahan dan pengobatan osteoartritis dengan menargetkan penuaan kondrosit.

Document ID: 39290780
Relevan: Ya
Alasan: Artikel ini membahas beban penyakit osteoartritis lutut, perawatan non-bedah yang tersedia saat ini, dan menyoroti terapi baru yang menjanjikan seperti cryoneurolysis, kortikosteroid kerja panjang, dan terapi gen.

Document ID: 38857874
Relevan: Ya
Alasan: Artikel ini membahas manajemen nyeri kronis pada gangguan reumatologi (termasuk osteoartritis), mencakup patofisiologi, farmakoterapi (NSAID, antidepresan), dan intervensi non-bedah.

Document ID: 38291203
Relevan: Ya (Secara Kontekstual)
Alasan: Studi efektivitas biaya ini mengevaluasi farmakoterapi manajemen berat badan (seperti Semaglutide). Relevansinya terletak pada analisis manfaat penurunan berat badan terhadap komplikasi terkait obesitas, termasuk pengurangan kebutuhan operasi osteoartritis lutut.

Document ID: 39503700
Relevan: Ya
Alasan: Tinjauan ini membahas peran terapi radiasi sebagai opsi pengobatan non-invasif untuk pasien osteoartritis yang refrakter terhadap terapi tradisional, terutama pada pasien lansia.

Document ID: 38590589
Relevan: Ya
Alasan: Studi prospektif ini mengevaluasi efektivitas suplemen "Cartinorm" (kombinasi glukosamin, kondroitin, kolagen, dan vitamin C) sebagai terapi pendukung dalam mengurangi nyeri dan meningkatkan kualitas hidup pasien dengan osteoartritis lutut.

Document ID: 38576449
Relevan: Ya
Alasan: Artikel ulasan ini membahas potensi eksosom yang berasal dari sel punca mesenkimal (MSC-Exos) sebagai sistem pengiriman obat yang ditargetkan untuk terapi osteoartritis.

Document ID: 38163526
Relevan: Ya
Alasan: Studi ini merancang sistem pengiriman obat intra-artikular baru (partikel nanokristal-kitosan) untuk Kartogenin, sebuah obat pemodifikasi penyakit osteoartritis (DMOAD), guna mengatasi masalah kelarutan rendah dan meningkatkan perbaikan tulang rawan.

Document ID: 38293880
Relevan: Ya
Alasan: Tinjauan bibliografi ini mengidentifikasi strategi teknologi formulasi obat baru (menggunakan nano dan mikroteknologi) untuk pengobatan osteoartritis dan rheumatoid arthritis, yang bertujuan meningkatkan efektivitas terapi dan pelepasan obat terkontrol.
## prompt

    Konteks:
    Ini adalah hasil searching dengan lucene search pyserini.
    Yang di cari adalah ['osteoarthritis'] , dengan query ['osteoarthritis'] AND (treatment OR pharmacotherapy OR drug OR therapy)
    index dibangun dari subdataset 1.5juta artikel PubMed dalam 5 tahun terakhir.

    Tugas kamu adalah mengkurasikan hasil pencarian ini,
    apakah sesuai atau tidak untuk masing-masing hasil pencarian.
    Berikan jawaban dalam format:
    Document ID: <docid>
    Relevan: Ya/Tidak
    Alasan: <alasan singkat>

    hasil pencariannya adalah berikut ini:
    38938057 | 12.3226
    {
    "id" : "38938057",
    "contents" : "Pharmacotherapy for osteoarthritis-related pain: current and emerging therapies.. Osteoarthritis (OA) related pain has affected millions of people worldwide. However, the current pharmacological options for managing OA-related pain have not achieved a satisfactory effect. This narrative review provides an overview of the current and emerging drugs for OA-related pain. It covers the drugs' mechanism of action, safety, efficacy, and limitations. The National Library of Medicine (PubMed) database was primarily searched from 2000 to 2024. Current treatment options are limited and suboptimal for OA pain management. Topical nonsteroidal anti-inflammatory drugs (NSAIDs) are the recognized and first-line treatment in the management of OA-related pain, and other drugs are inconsistent recommendations by guidelines. Emerging treatment options are promising for OA-related pain, including nerve growth factor (NGF) inhibitors, ion channel inhibitors, and calcitonin gene-related peptide (CGRP) antagonists. Besides, drugs repurposing from antidepressants and antiepileptic analgesics are shedding light on the management of OA-related pain. The management of OA-related pain is challenging as pain is heterogeneous and subjective. A more comprehensive strategy combined with non-pharmacological therapy needs to be considered, and tailored management options to individualized patients.",
    "year" : 2024
    }
    38596341 | 10.7449
    {
    "id" : "38596341",
    "contents" : "RPL35 downregulated by mechanical overloading promotes chondrocyte senescence and osteoarthritis development via Hedgehog-Gli1 signaling.. To investigate the potential role of Ribosomal protein L35 (RPL35) in regulating chondrocyte catabolic metabolism and to examine whether osteoarthritis (OA) progression can be delayed by overexpressing RPL35 in a mouse compression loading model. RNA sequencing analysis was performed on chondrocytes treated with or without 20 % elongation strain loading for 24 h. Experimental OA in mice was induced by destabilization of the medial meniscus and compression loading. Mice were randomly assigned to a sham group, an intra-articular adenovirus-mediated overexpression of the negative group, and an intra-articular adenovirus-mediated overexpression of the RPL35 operated group. The Osteoarthritis Research Society International score was used to evaluate cartilage degeneration. Immunostaining and western blot analyses were conducted to detect relative protein levels. Primary mouse chondrocytes were treated with 20 % elongation strain loading for 24 h to investigate the role of RPL35 in modulating chondrocyte catabolic metabolism and regulating cellular senescence in chondrocytes. The protein expression of RPL35 in mouse chondrocytes was significantly reduced when excessive mechanical loading was applied, while elevated protein levels of RPL35 protected articular chondrocytes from degeneration. In addition, the RPL35 knockdown alone induced chondrocyte senescence, decreased the expression of anabolic markers, and increased the expression of catabolic markers These findings demonstrated a functional pathway important for OA development and identified intra-articular injection of RPL35 as a potential therapy for OA prevention and treatment. It is necessary to develop new targeted drugs for OA due to the limitations of conventional pharmacotherapy. Our study explores and demonstrates the protective effect of RPL35 against excessive mechanical stress in OA models in vivo and in vitro in animals. These findings might provide novel insights into OA pathogenesis and show its translational potential for OA therapy.",
    "year" : 2024
    }
    39290780 | 10.0734
    {
    "id" : "39290780",
    "contents" : "Knee osteoarthritis: disease burden, available treatments, and emerging options.. Osteoarthritis (OA) is a prevalent condition that affects nearly 528 million people worldwide, including 23% of the global population aged ⩾40, and is characterized by progressive damage to articular cartilage, which often leads to substantial pain, stiffness, and reduced mobility for affected patients. Pain related to OA is a barrier to maintaining physical activity and a leading cause of disability, accounting for 2.4% of all years lived with disability globally, reducing the ability to work in 66% of US patients with OA and increasing absenteeism in 21% of US patients with OA. The joint most commonly involved in OA is the knee, which is affected in about 60%-85% of all OA cases. The aging population and longer life expectancy, coupled with earlier and younger diagnoses, translate into a growing cohort of symptomatic patients in need of alternatives to surgery. Despite the large number of patients with knee OA (OAK) worldwide, the high degree of variability in patient presentation can lead to challenges in diagnosis and treatment. Multiple society guidelines recommend therapies for OAK, but departures from guidelines by healthcare professionals in clinical settings reflect a discordance between evidence-based treatment algorithms and routine clinical practice. Furthermore, disease-modifying pharmacotherapies are limited, and treatment for OAK often focuses solely on symptom relief, rather than underlying causes. In this narrative review, we summarize the patient journey, analyze current disease burden and nonsurgical therapy recommendations for OAK, and highlight emerging and promising therapies-such as cryoneurolysis, long-acting corticosteroids, and gene therapies-for this debilitating condition.",
    "year" : 2024
    }
    38857874 | 10.0536
    {
    "id" : "38857874",
    "contents" : "Chronic pain for rheumatological disorders: Pathophysiology, therapeutics and evidence.. Pain is the leading reason people seek orthopedic and rheumatological care. By definition, most pain can be classified as nociceptive, or pain resulting from non-neural tissue injury or potential injury, with between 15% and 50% of individuals suffering from concomitant neuropathic pain or the newest category of pain, nociplastic pain, defined as \"pain arising from altered nociception despite no clear evidence of actual or threatened tissue damage, or of a disease or lesion affecting the somatosensory system.\" Pain classification is important because it affects treatment decisions at all levels of care. Although several instruments can assist with classifying treatment, physician designation is the reference standard. The appropriate treatment of pain should ideally involve multidisciplinary care including physical therapy, psychotherapy and integrative therapies when appropriate, and pharmacotherapy with non-steroidal anti-inflammatory drugs for acute, mechanical pain, membrane stabilizers for neuropathic and nociplastic pain, and serotonin-norepinephrine reuptake inhibitors and tricyclic antidepressants for all types of pain. For nonsurgical interventions, there is evidence to support a small effect for epidural steroid injections for an intermediate-term duration, and conflicting evidence for radiofrequency ablation to provide at least 6months of benefit for facet joint pain, knee osteoarthritis, and sacroiliac joint pain. Since pain and disability represent the top reason for elective surgery, it should be reserved for patients who fail conservative interventions. Risk factors for procedural failure are the same as risk factors for conservative treatment failure and include greater disease burden, psychopathology, opioid use, central sensitization and multiple comorbid pain conditions, poorly controlled preoperative and postoperative pain, and secondary gain.",
    "year" : 2024
    }
    38291203 | 9.7491
    {
    "id" : "38291203",
    "contents" : "Cost-effectiveness of weight-management pharmacotherapies in Canada: a societal perspective.. This study aimed to assess the cost-effectiveness of weight-management pharmacotherapies approved by Canada Health, i.e., orlistat, naltrexone 32 mg/bupropion 360 mg (NB-32), liraglutide 3.0 mg and semaglutide 2.4 mg as compared to the current standard of care (SoC). Analyses were conducted using a cohort with a mean starting age 50 years, body mass index (BMI) 37.5 kg/m From a societal perspective, at a willingness-to-pay (WTP) threshold of CAD 50 000 per QALY, semaglutide 2.4 mg was the most cost-effective treatment, at an incremental cost-utility ratio (ICUR) of CAD 31 243 and CAD 29 014 per QALY gained versus the next best alternative, i.e., orlistat, and SoC, respectively. Semaglutide 2.4 mg extendedly dominated other pharmacotherapies such as NB-32 or liraglutide 3.0 mg and remained cost-effective both under a public and private payer perspective. Results were robust to sensitivity analyses varying post-treatment catch-up rates, longer treatment durations and using real-world cohort characteristics. Semaglutide 2.4 mg was the preferred intervention, with a likelihood of 70% at a WTP threshold of CAD 50 000 per QALY gained. However, when the modeled benefits of weight-loss on cancer, mortality, cardiovascular disease (CVD) or osteoarthritis surgeries were removed simultaneously, orlistat emerged as the best value for money compared with SoC, with an ICUR of CAD 35 723 per QALY gained. Semaglutide 2.4 mg was the most cost-effective treatment alternative compared with D&E or orlistat alone, and extendedly dominated other pharmacotherapies such as NB-32 or liraglutide 3.0 mg. Results were sensitive to the inclusion of the combined benefits of mortality, cancer, CVD, and knee osteoarthritis.",
    "year" : 2024
    }
    39503700 | 9.4923
    {
    "id" : "39503700",
    "contents" : "Radiation Therapy for the Treatment of Osteoarthritis.. Osteoarthritis is a common cause of pain and disability in the United States. Many patients experience pain that is refractory or unable to be treated by traditional treatments such as exercise, physical therapy, nonsteroidal anti-inflammatory drugs, and/or cyclooxygenase-2 inhibitors. For patients with medically refractory disease, intra-articular corticosteroid therapy, hyaluronic acid, or surgery can be considered. However, for many older patients with significant impairment in quality of life related to osteoarthritis, radiation therapy is a noninvasive treatment option that has a long history of global use. In this topic discussion, we review the clinical evidence supporting treatment of osteoarthritis, as well as considerations for how to select which patient and joint to treat. We discuss technical considerations for treatment including dose and immobilization, assessment of treatment response, and the role of retreatment.",
    "year" : 2025
    }
    38590589 | 9.3966
    {
    "id" : "38590589",
    "contents" : "Evaluation of the Cartinorm Use in the Therapy of Patients with Knee Osteoarthritis.. Knee osteoarthritis is the most common rheumatic disease characterized by pain, structural changes and impairment of quality of life. This disease has a multifactorial etiopathogenesis, and the main role is attributed to mechanical factors. There is a primary and secondary form of osteoarthritis. Osteoarthritis diagnosis is carried out on the basis of history, clinical picture and radiological examinations. Osteoarthritis is a major cause of absenteeism for middle-aged people. In the treatment of osteoarthritis, the triad is important: education, rehabilitation and supportive therapy with chondroprotective drugs. As part of the study, 60 patients with clinical and radiographic signs of knee osteoarthritis were given Cartinorm (1500mg glucosamine sulfate, 800mg chondroitin sulfate, 5000mg forti gel, 250mg vitamin C). After 3 months of treatment, there was an improvement in movement, a reduction in pain and an improvement in activities of daily living as measured by the Oswestry score. Objective: The aim of this study was to evaluate the reduction of pain, improvement of the clinical picture and improvement of the quality of life, after three months of supportive therapy with chondroprotective drugs (Cartinorm -1500mg glucosamine sulfate, 800mg chondroitin sulfate, 5000mg forti gel, 250 mg vitamin C). In a study that is prospective, analytical and descriptive, 60 subjects of both sexes with clinical and radiological signs of knee osteoarthritis were included. The study was conducted in six cities (Sarajevo, Tuzla, Banja Luka, Mostar, Zenica and Bijeljina) and lasted three months. During the study for pain relief, patients could only use Paracetamol and all patients took Cartinorm 1x a day. Pain Scale and Ostwestry index tests were performed for each patient to assess the quality of life at the beginning of the study, at the end of the first, second and third month. Results and. Total number of 60 subjects with clinical and radiological signs of knee osteoarthritis were included in the study. The analysis of the gender structure showed the dominance of the female gender (43 respondents), compared to the male population (17 respondents). The largest number of respondents had bilateral knee osteoarthritis. Assessment of pain through the VAS pain scale on the first day and at the end of the 3-month study showed a statistically significant reduction in pain. Analysis of the quality of life at the beginning of the study showed that 22 subjects performed activities with many difficulties, and at the end of the study only 5 subjects performed activities with many difficulties, which shows an improvement in the quality of life after 3 months of taking Cartinorm. Conclusion: Proper education of subjects with knee osteoarthritis and application of chondroprotective drugs (Cartinorm) for a period of 3 months showed an improvement in terms of pain reduction measured through the VAS scale, improvement of knee mobility and improvement of quality of life measured through Oswestry Scor.",
    "year" : 2024
    }
    38576449 | 9.2665
    {
    "id" : "38576449",
    "contents" : "Exosomes derived from MSC as drug system in osteoarthritis therapy.. Osteoarthritis (OA) is the most common degenerative disease of the joint with irreversible cartilage damage as the main pathological feature. With the development of regenerative medicine, mesenchymal stem cells (MSCs) have been found to have strong therapeutic potential. However, intraarticular MSCs injection therapy is limited by economic costs and ethics. Exosomes derived from MSC (MSC-Exos), as the important intercellular communication mode of MSCs, contain nucleic acid, proteins, lipids, microRNAs, and other biologically active substances. With excellent editability and specificity, MSC-Exos function as a targeted delivery system for OA treatment, modulating immunity, inhibiting apoptosis, and promoting regeneration. This article reviews the mechanism of action of MSC-Exos in the treatment of osteoarthritis, the current research status of the preparation of MSC-Exos and its application of drug delivery in OA therapy.",
    "year" : 2024
    }
    38163526 | 9.2176
    {
    "id" : "38163526",
    "contents" : "Nanocrystal-chitosan particles for intra-articular delivery of disease-modifying osteoarthritis drugs.. Osteoarthritis is the most common chronic joint disease and a major health care concern due to the lack of efficient treatments. This is mainly related to the local and degenerative nature of this disease. Kartogenin was recently reported as a disease-modifying osteoarthritis drug that promotes cartilage repair, but its therapeutic effect is impeded by its very low solubility. Therefore, we designed a unique nanocrystal-chitosan particle intra-articular delivery system for osteoarthritis treatment that merges the following formulation techniques: nanosize reduction of a drug by wet milling and spray drying. The intermediate formulation (kartogenin nanocrystals) increased the solubility and dissolution rates of kartogenin. The final drug delivery system consisted of an easily resuspendable and ready-to-use microsphere powder for intra-articular injection. Positively charged chitosan microspheres with a median size of approximately 10 µm acted as a mothership drug delivery system for kartogenin nanocrystals in a simulated intra-articular injection. The microspheres showed suitable stability and a controlled release profile in synovial fluid and were nontoxic in human synoviocytes. The cartilage retention skills of the microspheres were also explored ex vivo using cartilage. This drug delivery system shows promise for advancement to preclinical stages in osteoarthritis therapy and scale-up production.",
    "year" : 2024
    }
    38293880 | 9.1906
    {
    "id" : "38293880",
    "contents" : "[New technological strategies for drug administration in the treatment of joint pathologies].. Despite the availability of drugs and pharmaceutical forms for the treatment of rheumatoid arthritis and osteoarthritis symptoms, their adverse effects and lack of response to therapy reinforces the need to search for new technological formulation strategies capable of delaying the progress of the disease, with better therapeutic results and prolonged control of arthropathy. The aim of this bibliographic review was to identify new reported therapeutic approaches for these diseases. The treatment of rheumatoid arthritis and osteoarthritis is an unresolved challenge, due to the complexity of these diseases. Thus, the new therapies aim to suppress inflammatory mediators and to reduce the degradation of the extracellular matrix. In addition, the use of nano and microtechnology takes advantage of the properties of polymers, lipids, peptides, and nucleic acids to develop controlled drug release systems, aiming to obtain highly effective precision therapies, whose usefulness should be evaluated in future clinical trials.",
    "year" : 2023
    }