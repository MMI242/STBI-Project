dieksekusi dengan `docker compose --profile search run --rm search python scripts/search-eval.py type 2 diabetes mellitus`

## hasil
skor 1.0


## Asessmen gemini 3 pro:
Berikut adalah kurasi hasil pencarian untuk query `Type 2 Diabetes Mellitus` (T2DM) dengan filter treatment/therapy:

Document ID: 39323929
Relevan: Ya
Alasan: Artikel ini membahas peran terapi epigenetik sebagai tambahan (adjunct) potensial untuk farmakoterapi konvensional (seperti metformin) dalam pengobatan T2DM dan komplikasi mikrovaskularnya.

Document ID: 39592207
Relevan: Ya
Alasan: Ulasan naratif ini meneliti kemajuan terbaru dalam terapi berbasis incretin (agonis reseptor GLP-1, GIP, dan glukagon) untuk Metabolic Dysfunction-Associated Steatotic Liver Disease (MASLD), terutama pada individu dengan obesitas dan T2DM.

Document ID: 38511473
Relevan: Ya
Alasan: Artikel ini membahas pendekatan kontemporer untuk pengobatan T2DM, menekankan peran modifikasi gaya hidup dan farmakoterapi, serta faktor-faktor yang mempengaruhi kepatuhan (adherence) pengobatan.

Document ID: 39184671
Relevan: Ya
Alasan: Tinjauan sistematis ini menyelidiki efikasi farmakoterapi penurunan berat badan (seperti GLP-1RA dan SGLT2 inhibitor) pada pasien dengan obesitas dan T2DM.

Document ID: 39548626
Relevan: Ya
Alasan: Komunikasi singkat ini memperkenalkan konsep "Physio-Friendly Pharmacotherapy" (seperti GLP1RA, SGLT2i, Metformin) yang memfasilitasi remisi pada T2DM dengan memulihkan homeostasis metabolik.

Document ID: 38161340
Relevan: Ya
Alasan: Studi potong lintang ini menganalisis pola peresepan obat antidiabetes dan kardiovaskular preventif pada lansia dengan T2DM di komunitas, serta mengevaluasi kesesuaian dengan pedoman klinis.

Document ID: 38846018
Relevan: Ya
Alasan: Penelitian observasional ini menyelidiki dampak sindrom metabolik terhadap hasil farmakoterapi (kontrol glikemik, tekanan darah, lipid) pada pasien dengan T2DM.

Document ID: 38632474
Relevan: Ya
Alasan: Ulasan ini membahas kemajuan terbaru dalam farmakoterapi berbasis incretin (termasuk agen 'GLP1 plus' dan GLP1RA oral) untuk pengobatan obesitas dan T2DM.

Document ID: 39112786
Relevan: Ya (Secara Kontekstual)
Alasan: Artikel ini membahas pengobatan NAFLD (penyakit hati berlemak) yang sering terjadi bersamaan dengan T2DM. Obat-obatan diabetes seperti agonis GLP-1, PPAR, dan penghambat SGLT2 dibahas sebagai pusat pengobatan NAFLD pada pasien dengan komorbiditas metabolik.

Document ID: 38647650
Relevan: Ya
Alasan: Studi kohort ini menilai ketidakpatuhan terhadap pengobatan kardiometabolik pada pasien T2DM menggunakan metode langsung (LC-MS/MS urin) dan menganalisis hubungannya dengan hasil ginjal dan kardiovaskular.

## prompt

    Konteks:
    Ini adalah hasil searching dengan lucene search pyserini.
    Yang di cari adalah ['Type', '2', 'Diabetes', 'Mellitus'] , dengan query ['Type', '2', 'Diabetes', 'Mellitus'] AND (treatment OR pharmacotherapy OR drug OR therapy)
    index dibangun dari subdataset 1.5juta artikel PubMed dalam 5 tahun terakhir.

    Tugas kamu adalah mengkurasikan hasil pencarian ini,
    apakah sesuai atau tidak untuk masing-masing hasil pencarian.
    Berikan jawaban dalam format:
    Document ID: <docid>
    Relevan: Ya/Tidak
    Alasan: <alasan singkat>

    hasil pencariannya adalah berikut ini:
    39323929 | 16.7491
    {
    "id" : "39323929",
    "contents" : "Targeting the Epigenetic Marks in Type 2 Diabetes Mellitus: Will Epigenetic Therapy Be a Valuable Adjunct to Pharmacotherapy?. Although genetic, environmental, and lifestyle factors largely contribute to type 2 diabetes mellitus (T2DM) risk, the role of epigenetics in its pathogenesis is now well established. The epigenetic mechanisms in T2DM mainly consist of DNA methylation, histone modifications and regulation by noncoding RNAs (ncRNAs). For instance, DNA methylation at CpG islands in the promoter regions of specific genes encoding insulin signaling and glucose metabolism suppresses these genes. Modulating the enzyme mediators of these epigenetic marks aims to restore standard gene expression patterns and improve glycemic control. In targeting these epigenetic marks, using epigenetic drugs such as DNA methyltransferase (DNAMT), histone deacetylase (HDAC) and histone acetyltransferase (HAT) inhibitors has led to variable success in humans and experimental murine models. Specifically, the United States' Food and Drug Administration (US FDA) has approved DNAMT inhibitors like 5-azacytidine and 5-aza-2'-deoxycytidine for use in diabetic retinopathy: a T2DM microvascular complication. These DNAMT inhibitors block the genes for methylation of mitochondrial superoxide dismutase 2 (SOD2) and matrix metallopeptidase 9 (MMP-9): the epigenetic marks in diabetic retinopathy. Traditional pharmacotherapy with metformin also have epigenetic effects in T2DM and positively alter disease outcomes when combined with epigenetic drugs like DNAMT and HDAC inhibitors, raising the prospect of using epigenetic therapy as a valuable adjunct to pharmacotherapy. However, introducing small interfering RNAs (siRNAs) in cells to silence specific target genes remains in the exploratory phase. Future research should focus on regulating gene expression in T2DM using long noncoding RNA (lncRNA) molecules, another type of ncRNA. This review discusses the epigenetics of T2DM and that of its macro- and microvascular complications, and the potential benefits of combining epigenetic therapy with pharmacotherapy for optimal results.",
    "year" : 2024
    }
    39592207 | 16.3996
    {
    "id" : "39592207",
    "contents" : "Recent advances in incretin-based therapy for MASLD: from single to dual or triple incretin receptor agonists.. Clinically effective pharmacological treatment(s) for metabolic dysfunction-associated steatotic liver disease (MASLD) and its progressive form metabolic dysfunction-associated steatohepatitis (MASH) represent a largely unmet need in medicine. Since glucagon-like peptide-1 receptor agonists (GLP-1RAs) have been licensed for the treatment of type 2 diabetes mellitus and obesity, they were one of the first drug classes to be examined in individuals with MASLD/MASH. Successful phase 2 randomised clinical trials with these agents have resulted in progression to phase 3 clinical trials (principally testing the long-term efficacy of subcutaneous semaglutide). Over the last few years, in addition to GLP-1RAs, newer agents with glucose-dependent insulinotropic peptide and/or glucagon receptor agonist functions have been tested, with increasing evidence from phase 2 randomised clinical trials of histological improvements in MASLD/MASH, as well as benefits on MASLD-related extrahepatic complications. Based on this background of evidence, single, dual or triple incretin receptor agonists are becoming an attractive and promising treatment option for MASLD or MASH, particularly in individuals with coexisting obesity or type 2 diabetes mellitus. In this narrative review, we examine the rapidly expanding body of clinical evidence supporting a role of incretin-based pharmacotherapies in delaying or reversing MASH progression. We also discuss the biology of incretins and the putative hepatoprotective mechanisms of incretin-based pharmacotherapies for managing MASLD or MASH.",
    "year" : 2024
    }
    38511473 | 15.7367
    {
    "id" : "38511473",
    "contents" : "Treatment adherence and the contemporary approach to treating type 2 diabetes mellitus.. The rising burden of type 2 diabetes mellitus (T2D) poses a significant healthcare challenge on a global scale. The economic impact is also substantial and continually increasing. In Serbia, even though the prevalence is officially around 12 percent, nearly 40 percent of the adult population is estimated to be living with undiagnosed diabetes and more than half the population is obese or overweight. This review comprehensively addresses the present approach to treating T2D, emphasizing the critical role of treatment adherence. We review the various components of T2D treatment, underlining the significance of lifestyle modifications. The pros and cons of medications used in treatment are discussed and factors influencing adherence are analysed. A healthy lifestyle remains the foundation of the treatment, and if not sufficient, early pharmacotherapy is initiated. Medications have been developed to lower blood sugar levels with cardiorenal protection, however, due to their still high cost, metformin remains the drug of first choice for most patients. Adherence to the treatment regimen is often poor. Factors associated with this are diverse and often multiple in a particular patient. Poor adherence is associated with poor glycaemic control, increased risk of disease complications, higher cardiovascular risk, increased mortality, hospitalizations, and healthcare costs. In addition to reducing the complexity of drug therapy and better informing the patient, improved education and motivation could lead to greater adherence. Enhanced communication between the patient and the physician and reduced treatment costs could also have a positive impact. The review concludes that addressing factors affecting adherence can significantly improve T2D outcomes and reduce costs. Further research is needed to identify region-specific risk factors for poor adherence.",
    "year" : 2024
    }
    39184671 | 15.4878
    {
    "id" : "39184671",
    "contents" : "The Efficacy of Pharmacotherapy in the Treatment of Obesity in Patients With Type 2 Diabetes: A Systematic Review.. Obesity is a global public health challenge that poses a significant threat to the effective control and management of type 2 diabetes mellitus (T2DM). Being overweight/obese with T2DM is associated with a wide range of comorbidities, including cardiovascular, cerebrovascular, and renal diseases. This systematic review aimed to investigate the drug therapy used globally among this type of patients in the period between 2014 and 2024. Four databases (PubMed, Web of Science, Scopus, and Cochrane) were searched using the keywords \"(Drug Therapy OR Pharmaceutical Preparations OR Pharmacotherapy) AND (Diabetes Mellitus, Type 2) AND (Obesity OR Overweight OR Weight Loss OR Weight reduction) in the title and abstract. All papers assessing the efficacy of any drug class on blood sugar and body weight (BW) were included in the systematic review. Out of 5,206 papers extracted through the database search, 25 randomized clinical trials (RCTs) were considered suitable for the systematic review. The articles included 8,208 participants who tested different drug classes, e.g., glucagon-like peptide-1 (GLP-1) and sodium-glucose co-transporter-2 (SGLT2), with or without metformin. All the reviewed drugs showed significant weight loss over 12-52 weeks. However, the magnitude of weight loss was modest, and the long-term health benefits and safety remain unclear. Interventions that combine pharmacologic therapy with lifestyle modifications may be more effective but need additional research. Continued development of new treatment options for obesity in T2DM is crucial to reduce morbidity and mortality among these patients.",
    "year" : 2024
    }
    39548626 | 15.4303
    {
    "id" : "39548626",
    "contents" : "Physio-Friendly Remission-Facilitating Pharmacotherapy (PRP) in Type 2 Diabetes.. This brief communication describes the concept of physiofriendly pharmacotherapy for type 2 diabetes mellitus. Physio-friendly therapy is defined as that which restores metabolic, including glycaemic and weight homoeostasis, to near normal levels. Drugs such as glucagon like peptide 1 receptor agonists (GLP1RA), sodium glucose cotransporter- 2 inhibitors (SGLT2i), and alfa glucosidase inhibitors, along with metformin, work in a physio-friendly manner and may facilitate remission. Thus, they can also be termed as remission-facilitating drugs.",
    "year" : 2024
    }
    38161340 | 15.1817
    {
    "id" : "38161340",
    "contents" : "Prescription patterns of antidiabetic and cardiovascular preventive medications in community-dwelling older adults with type 2 diabetes mellitus: a cross-sectional study.. To describe trends in antidiabetics drug prescription patterns in community-dwelling older adults with type 2 diabetes mellitus (T2DM) and to evaluate the use of cardiovascular preventive medications among those diagnosed with atherosclerotic cardiovascular disease (ASCVD). This cross-sectional, face-to-face interview study that comprised community-dwelling older adults (≥ 65 years) diagnosed with T2DM. The study questionnaire included the patients' demographics, clinical data, and current medication use. Patients with established ASCVD were further classified into low (i.e., not receiving evidence-based therapy or only one) and high (i.e., receiving at least two evidence-based therapies) composite score groups. Bivariate analysis followed by multivariable logistic regression analysis were performed to evaluate the demographic/clinical characteristics associated with the use of antidiabetic monotherapy/polytherapy and evidence-based pharmacotherapy. A total of 500 older adults were enrolled. The mean age of included participants was 73 ± 7 years, 310 participants (62%) were males, and 385 participants (77.0%) had established ASCVD. Antidiabetic monotherapy was reported in 251 participants (50.2%), with metformin followed by sulfonylureas being the most commonly prescribed drugs as monotherapy. The results of the multivariable analysis showed that age [odds ratio (OR) = 0.89, 95% CI: 0.85-0.94, Only one in twenty-one participant with T2DM and ASCVD collectively received three guideline-recommended therapies, indicating a deficiency of utilization of cardiovascular preventive drugs.",
    "year" : 2023
    }
    38846018 | 15.0755
    {
    "id" : "38846018",
    "contents" : "Metabolic syndrome and pharmacotherapy outcomes in patients with type 2 diabetes mellitus.. Metabolic syndrome is a group of metabolic abnormalities that increase predisposition to several diseases including ischemic heart disease and diabetes mellitus. The study aimed to investigate metabolic syndrome among patients with type-2 diabetes mellitus (DM), and its impact on pharmacotherapy outcomes. An observational cross-sectional study was performed on 910 patients with type-2 DM between June and December 2023. Fasting blood sugar, triglycerides, high-density lipoproteins (HDL), blood pressure, and abdominal obesity were measured. Metabolic syndrome was identified according to the National Cholesterol Education Program Adult Treatment Panel III criteria. Pharmacotherapy outcomes were assessed according to American Association of Clinical Endocrinologists and American Diabetes Association guidelines using the ability to achieve adequate glycemic control and normal levels of blood pressure and fasting plasma lipoproteins. In total, 87.5% of type-2 DM patients had metabolic syndrome; the prevalence increased with age and was higher among females. Metabolic syndrome showed the following distribution of risk factors: insulin resistance (100%), low HDL (95.3%), elevated blood pressure (83%), triglycerides dyslipidemia (80.1%), and abdominal obesity (62.5%). Majority of the patients had either 5 or 4 risk factors of metabolic syndrome. The most common comorbidities were dyslipidemia (97.7%) and hypertension (83%). Treatment outcomes were insufficient where adequate glycemic control was only achieved in 12% of type-2 DM patients, and proper management of comorbid dyslipidemia and hypertension was achieved in 29% and 40.9% of patients, respectively. Adequate blood pressure control was less achieved in patients with metabolic syndrome (34.4%) than those without metabolic syndrome (77.2%). Similarly, dyslipidemia was less controlled in patients with metabolic syndrome (26.9%) than in those without metabolic syndrome (47.3%). Pharmacotherapy outcomes were inadequate for most patients with type-2 diabetes mellitus. Adopting early preventive and therapeutic interventions for metabolic syndrome is advised to improve treatment outcomes of the comorbid dyslipidemia and hypertension.",
    "year" : 2024
    }
    38632474 | 14.8736
    {
    "id" : "38632474",
    "contents" : "Targeting the incretin system in obesity and type 2 diabetes mellitus.. Obesity and type 2 diabetes mellitus (T2DM) are widespread, non-communicable diseases that are responsible for considerable levels of morbidity and mortality globally, primarily in the form of cardiovascular disease (CVD). Changes to lifestyle and behaviour have insufficient long-term efficacy in most patients with these diseases; metabolic surgery, although effective, is not practically deliverable on the scale that is required. Over the past two decades, therapies based on incretin hormones, spearheaded by glucagon-like peptide 1 (GLP1) receptor agonists (GLP1RAs), have become the treatment of choice for obesity and T2DM, and clinical evidence now suggests that these agents have benefits for CVD. We review the latest advances in incretin-based pharmacotherapy. These include 'GLP1 plus' agents, which combine the known advantages of GLP1RAs with the activity of additional hormones, such as glucose-dependent insulinotropic peptide, glucagon and amylin, to achieve desired therapeutic goals. Second-generation non-peptidic oral GLP1RAs promise to extend the benefits of GLP1 therapy to those who do not want, or cannot have, subcutaneous injection therapy. We conclude with a discussion of the knowledge gaps that must be addressed before incretin-based therapies can be properly deployed for maximum benefit in the treatment of obesity and T2DM.",
    "year" : 2024
    }
    39112786 | 14.5775
    {
    "id" : "39112786",
    "contents" : "Current and experimental pharmacotherapy for the management of non-alcoholic fatty liver disease.. Non-alcoholic fatty liver disease (NAFLD) is a chronic liver disease, with its incidence increasing in parallel with the global prevalence of obesity and type 2 diabetes mellitus. Despite our steadily increasing knowledge of its pathogenesis, there is as yet no available pharmacotherapy specifically tailored for NAFLD. To define the appropriate management, it is important to clarify the context in which the disease appears. In the case of concurrent metabolic comorbidities, NAFLD patients are treated by targeting these comorbidities, such as diabetes and obesity. Thus, GLP-1 analogs, PPAR, and SGLT2 inhibitors have recently become central to the treatment of NAFLD. In parallel, randomized trials are being conducted to explore new agents targeting known pathways involved in NAFLD progression. However, there is an imperative need to intensify the effort to design new, safe drugs with biopsy-proven efficacy. Of note, the main target of the pharmacotherapy should be directed to the regression of fibrotic NASH, as this histologic stage has been correlated with increased overall as well as liver-related morbidity and mortality. Herein we discuss the drugs currently at the forefront of NAFLD treatment.",
    "year" : 2024
    }
    38647650 | 14.1458
    {
    "id" : "38647650",
    "contents" : "Non-adherence to cardiometabolic medication as assessed by LC-MS/MS in urine and its association with kidney and cardiovascular outcomes in type 2 diabetes mellitus.. Non-adherence to medication is a frequent barrier in the treatment of patients with type 2 diabetes mellitus, potentially limiting the effectiveness of evidence-based treatments. Previous studies have mostly relied on indirect adherence measures to analyse outcomes based on adherence. The aim of this study was to use LC-MS/MS in urine-a non-invasive, direct and objective measure-to assess non-adherence to cardiometabolic drugs and analyse its association with kidney and cardiovascular outcomes. This cohort study includes 1125 participants from the PROVALID study, which follows patients with type 2 diabetes mellitus at the primary care level. Baseline urine samples were tested for 79 cardiometabolic drugs and metabolites thereof via LC-MS/MS. An individual was classified as totally adherent if markers for all drugs were detected, partially non-adherent when at least one marker for one drug was detected, and totally non-adherent if no markers for any drugs were detected. Non-adherence was then analysed in the context of cardiovascular (composite of myocardial infarction, stroke and cardiovascular death) and kidney (composite of sustained 40% decline in eGFR, sustained progression of albuminuria, kidney replacement therapy and death from kidney failure) outcomes. Of the participants, 56.3% were totally adherent, 42.0% were partially non-adherent, and 1.7% were totally non-adherent to screened cardiometabolic drugs. Adherence was highest to antiplatelet and glucose-lowering agents and lowest to lipid-lowering agents. Over a median (IQR) follow-up time of 5.10 (4.12-6.12) years, worse cardiovascular outcomes were observed with non-adherence to antiplatelet drugs (HR 10.13 [95% CI 3.06, 33.56]) and worse kidney outcomes were observed with non-adherence to antihypertensive drugs (HR 1.98 [95% CI 1.37, 2.86]). This analysis shows that non-adherence to cardiometabolic drug regimens is common in type 2 diabetes mellitus and negatively affects kidney and cardiovascular outcomes.",
    "year" : 2024
    }