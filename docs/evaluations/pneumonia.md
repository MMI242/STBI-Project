dieksekusi dengan `docker compose --profile search run --rm search python scripts/search-eval.py pneumonia`

## hasil
skor 0.8




# dengan query expansion
Berikut adalah kurasi hasil pencarian untuk query `pneumonia` dengan filter treatment/therapy:

Document ID: 38284720
Relevan: Tidak
Alasan: Artikel ini berfokus pada pengobatan Rheumatoid Arthritis (RA) dengan Methotrexate. Pneumonia hanya disebutkan sebagai manifestasi ekstra-artikular atau kondisi terkait, bukan fokus utama terapi dalam artikel ini.

Document ID: 38730686
Relevan: Ya
Alasan: Artikel ini membahas strategi pengobatan untuk Kanker Paru Non-Small-Cell (NSCLC) yang memiliki komorbiditas penyakit pernapasan, termasuk pneumonia interstisial (IP), serta membahas keamanan dan efektivitas farmakoterapi dalam konteks ini.

Document ID: 38634891
Relevan: Ya
Alasan: Artikel ini membahas tantangan dalam pengobatan *Mycoplasma pneumoniae* pneumonia pada anak, termasuk resistensi makrolida dan opsi terapi alternatif seperti tetrasiklin, fluorokuinolon, dan imunomodulator.

Document ID: 38172969
Relevan: Ya
Alasan: Studi ini membandingkan terapi antimikroba obat tunggal versus kombinasi pada pasien sakit kritis dengan pneumonia nosokomial (HAP/VAP) yang disebabkan oleh patogen Gram-negatif.

Document ID: 39643882
Relevan: Ya
Alasan: Studi kohort retrospektif ini menentukan hasil pengobatan (treatment outcome) dari community-acquired pneumonia (CAP) pada pasien anak yang dirawat di rumah sakit, serta faktor-faktor yang mempengaruhi keberhasilan atau kegagalan terapi.

Document ID: 38158959
Relevan: Ya
Alasan: Tinjauan ini membahas diagnosis dan terapi antibiotik untuk pneumonia nosokomial pada orang dewasa, menyoroti pentingnya rejimen antibiotik yang tepat waktu dan adekuat di tengah meningkatnya resistensi bakteri.

Document ID: 38179988
Relevan: Ya
Alasan: Artikel ini meninjau opsi pengobatan saat ini untuk pneumonia yang disebabkan oleh *Acinetobacter baumannii* yang resisten terhadap karbapenem (CRAB), termasuk penggunaan kombinasi sulbactam-durlobactam dan colistin.

Document ID: 39438303
Relevan: Tidak
Alasan: Fokus utama artikel ini adalah perkembangan resistensi bakteri dan praktik peresepan antibiotik secara umum di Jerman. Meskipun menyebutkan patogen penyebab pneumonia (*K. pneumoniae*), artikel ini lebih membahas resistensi antibiotik secara luas daripada terapi spesifik untuk kasus pneumonia klinis.

Document ID: 38414600
Relevan: Ya
Alasan: Artikel ini membahas perlunya memperkuat penelitian farmakoterapi untuk fibrosis paru yang diinduksi oleh COVID-19 (yang sering kali didahului oleh pneumonia), termasuk intervensi pengobatan dini dan preventif.

Document ID: 38288808
Relevan: Ya
Alasan: Studi *in silico* ini mengusulkan rejimen terapi tiga obat (acetaminophen, ursodiol, dan β-carotene) untuk mengobati ARDS yang diinduksi oleh viral pneumonia, khususnya dalam konteks COVID-19.

## prompt:
    Konteks:
    Ini adalah hasil searching dengan lucene search pyserini.
    Yang di cari adalah ['pneumonia'] , dengan query ['pneumonia'] AND (treatment OR pharmacotherapy OR drug OR therapy)
    index dibangun dari subdataset 1.5juta artikel PubMed dalam 5 tahun terakhir.

    Tugas kamu adalah mengkurasikan hasil pencarian ini,
    apakah sesuai atau tidak untuk masing-masing hasil pencarian.
    Berikan jawaban dalam format:
    Document ID: <docid>
    Relevan: Ya/Tidak
    Alasan: <alasan singkat>

    hasil pencariannya adalah berikut ini:
    38284720 | 10.9346
    {
    "id" : "38284720",
    "contents" : "The Journey of Methotrexate and Potential Alternative Pharmacotherapies for Rheumatoid Arthritis.. Rheumatoid Arthritis (RA) is a systemic inflammatory auto-immune disorder chiefly described by synovitis followed by extra-articular manifestations of organ association such as pneumonia in addition to the clinical symptoms that cause long-term joint damage starting from the small joints and gradually progressing to the larger ones. Early diagnosis is considered a major improvement for the most desirable outcomes. Methotrexate (MTX), an antifolate, has been the gold standard therapy in use for over forty years as an anchor drug. This drug started out as an anti-cancer drug in large doses and is now in use to treat rheumatoid arthritis at very low doses. The treatments for rheumatoid arthritis aim to curb the swelling in the body and protect the joints from further damage. Recent research has seen an increase in the use of combination therapies with Methotrexate. In this paper, we present a summary of the current drug in use and its side effects, associated with RA. The paper gives an account of alternate modes of treatment that have been explored for the treatment of rheumatoid arthritis. Initially designed to inhibit the enzyme dihydrofolate reductase and treat various types of cancer, methotrexate found application as an anti-rheumatic drug in 1984 although suggestions for the same have been made since the 1950s. Since then, a substantial amount of clinical evidence has been obtained to clearly indicate the cytotoxic activity of the drug against the cells responsible for joint inflammation associated with RA. Thus, methotrexate is a clear choice when it comes to treating RA despite the advent of other lines of treatment being explored and implemented.",
    "year" : 2024
    }
    38730686 | 10.5245
    {
    "id" : "38730686",
    "contents" : "Treatment Strategies for Non-Small-Cell Lung Cancer with Comorbid Respiratory Disease; Interstitial Pneumonia, Chronic Obstructive Pulmonary Disease, and Tuberculosis.. Non-small cell lung cancer (NSCLC) patients are often complicated by other respiratory diseases, including interstitial pneumonia (IP), chronic obstructive pulmonary disease (COPD), and pulmonary tuberculosis (TB), and the management of which can be problematic. NSCLC patients with IP sometimes develop fatal acute exacerbation induced by pharmacotherapy, and the establishment of a safe treatment strategy is desirable. For advanced NSCLC with IP, carboplatin plus nanoparticle albumin-bound paclitaxel is a relatively safe and effective first-line treatment option. Although the safety of immune checkpoint inhibitors (ICIs) for these populations remains controversial, ICIs have the potential to provide long-term survival. The severity of COPD is an important prognostic factor in NSCLC patients. Although COPD complications do not necessarily limit treatment options, it is important to select drugs with fewer side effects on the heart and blood vessels as well as the lungs. Active TB is complicated by 2-5% of NSCLC cases during their disease course. Since pharmacotherapy, especially ICIs, reportedly induces the development of TB, the possibility of developing TB should always be kept in mind during NSCLC treatment. To date, there is no coherent review article on NSCLC with these pulmonary complications. This review article summarizes the current evidence and discusses future prospects for treatment strategies for NSCLC patients complicated with IP, severe COPD, and TB.",
    "year" : 2024
    }
    38634891 | 9.7790
    {
    "id" : "38634891",
    "contents" : "Challenges in the treatment of pediatric Mycoplasma pneumoniae pneumonia.. Mycoplasma pneumoniae (MP) is an important cause of community-acquired pneumonia in children and young adolescents. Despite macrolide antibiotics effectiveness as a first-line therapy, persistence of fever and/or clinical deterioration sometimes may complicate treatment and may even lead to severe systemic disease. To date, there is no consensus on alternative treatment options, optimal dosage, and duration for treating severe, progressive, and systemic MP pneumonia after macrolide treatment failure. Macrolide-resistant MP pneumonia and refractory MP pneumonia are the two major complex conditions that are clinically encountered. Currently, the vast majority of MP isolates are resistant to macrolides in East Asia, especially China, whereas in Europe and North America, whereas in Europe and North America prevalence is substantially lower than in Asia, varying across countries. The severity of pneumonia and extrapulmonary presentations may reflect the intensity of the host's immune reaction or the dissemination of bacterial infection. Children infected with macrolide-resistant MP strains who receive macrolide treatment experience persistent fever with extended antibiotic therapy and minimal decrease in MP-DNA load. Alternative second-line agents such as tetracyclines (doxycycline or minocycline) and fluoroquinolones (ciprofloxacin or levofloxacin) may lead to clinical improvement after macrolide treatment failure in children. Refractory MP pneumonia reflects a deterioration of clinical and radiological findings due to excessive immune response against the infection. Immunomodulators such as corticosteroids and intravenous immunoglobulin (IVIG) have shown promising results in treatment of refractory MP pneumonia, particularly when combined with appropriate antimicrobials. Corticosteroid-resistant hyperinflammatory MP pneumonia represents a persistent or recrudescent fever despite corticosteroid therapy with intravenous methylprednisolone at standard dosage. This report summarizes the clinical significance of macrolide-resistant and refractory MP pneumonia and discusses the efficacy and safety of alternative drugs, with a stepwise approach to the management of MP pneumonia recommended from the viewpoint of clinical practice. • Although MP pneumonia is usually a benign self-limited infection with response macrolides as first line therapy, severe life-threatening cases may develop if additional treatment strategies are not effectively implemented. • Macrolide-resistant and refractory MP pneumonia are two conditions that may complicate the clinical course of MP pneumonia, increasing the risk for exacerbation and even death. • This report summarizes the clinical relevance of macrolide-resistant and refractory MP pneumonia and discusses the efficacy and safety of alternative drug therapies. • A practical stepwise approach to the management of MP pneumonia is developed based on a comprehensive analysis of existing evidence and expert opinion.",
    "year" : 2024
    }
    38172969 | 9.6899
    {
    "id" : "38172969",
    "contents" : "Single-drug versus combination antimicrobial therapy in critically ill patients with hospital-acquired pneumonia and ventilator-associated pneumonia due to Gram-negative pathogens: a multicenter retrospective cohort study.. In this study including 391 critically ill patients with nosocomial pneumonia due to Gram-negative pathogens, combination therapy was not associated with a reduced hazard of death at Day 28 or a greater likelihood of clinical cure at Day 14. No over-risk of AKI was observed in patients receiving combination therapy. The benefits and harms of combination antimicrobial therapy remain controversial in critically ill patients with hospital-acquired pneumonia (HAP), ventilated HAP (vHAP) or ventilator-associated pneumonia (VAP) involving Gram-negative bacteria. We included all patients in the prospective multicenter OutcomeRea database with a first HAP, vHAP or VAP due to a single Gram-negative bacterium and treated with initial adequate single-drug or combination therapy. The primary endpoint was Day-28 all-cause mortality. Secondary endpoints were clinical cure rate at Day 14 and a composite outcome of death or treatment-emergent acute kidney injury (AKI) at Day 7. The average effects of combination therapy on the study endpoints were investigated through inverse probability of treatment-weighted regression and multivariable regression models. Subgroups analyses were performed according to the resistance phenotype of the causative pathogens (multidrug-resistant or not), the pivotal (carbapenems or others) and companion (aminoglycosides/polymyxins or others) drug classes, the duration of combination therapy (< 3 or ≥ 3 days), the SOFA score value at pneumonia onset (< 7 or ≥ 7 points), and in patients with pneumonia due to non-fermenting Gram-negative bacteria, pneumonia-related bloodstream infection, or septic shock. Among the 391 included patients, 151 (38.6%) received single-drug therapy and 240 (61.4%) received combination therapy. VAP (overall, 67.3%), vHAP (16.4%) and HAP (16.4%) were equally distributed in the two groups. All-cause mortality rates at Day 28 (overall, 31.2%), clinical cure rate at Day 14 (43.7%) and the rate of death or AKI at Day 7 (41.2%) did not significantly differ between the groups. In inverse probability of treatment-weighted analyses, combination therapy was not independently associated with the likelihood of all-cause death at Day 28 (adjusted odd ratio [aOR], 1.14; 95% confidence interval [CI] 0.73-1.77; P = 0.56), clinical cure at Day 14 (aOR, 0.79; 95% CI 0.53-1.20; P = 0.27) or death or AKI at Day 7 (aOR, 1.07; 95% CI 0.71-1.63; P = 0.73). Multivariable regression models and subgroup analyses provided similar results. Initial combination therapy exerts no independent impact on Day-28 mortality, clinical cure rate at Day 14, and the hazard of death or AKI at Day 7 in critically ill patients with mono-bacterial HAP, vHAP or VAP due to Gram-negative bacteria.",
    "year" : 2024
    }
    39643882 | 9.5346
    {
    "id" : "39643882",
    "contents" : "Treatment outcome of community acquired pneumonia among pediatric patients admitted to pediatrics wards at university of Gondar comprehensive and specialized hospital, northwest Ethiopia: a Retrospective cohort study.. Pneumonia is inflammation of the lung parenchyma and is a substantial cause of childhood morbidity and mortality in developing countries. Community-acquired pneumonia (CAP) is a type of pneumonia termed when patients who develop pneumonia in the outpatient setting and have not been in any health care facilities within 90days. The objective of this study was to determine treatment outcome of community acquired pneumonia among hospitalized pediatric patients. A retrospective cohort study was conducted from April 15, 2019 to July 15, 2019 and included patients who were admitted and hospitalized in pediatrics wards from September 1, 2015 to March 30, 2019. The study included pediatric age groups between one month and fifteen years old. Study Participants were selected based on the diagnosis of Community acquired pneumonia. Systematic sampling technique was used. All the statistical data were carried out using Statistical Package for Social Sciences (SPSS 20) and descriptive statistics were presented using means with standard deviation and percentages. Binary logistic regression model was fitted to measure the association between independent and dependent variables including duration of signs and symptoms. 95% Confidence interval was used. Statistically significant at P < 0.05. A total of 385 patients with Community Acquired Pneumonia were included in this study of whom 368(95.65%) were discharged and 17(4.4%) of patients were dead. Drug therapy change (AOR 20.308(3.666-112.501), P = 0.001), Prescribing and taking of large number of drugs (above 5 drugs) (AOR 0.067, CI (0.015-0.313), P = 0.001), Loss of appetite (AOR 38.641, CI (5.454-273.769), P = 0.000), and Blood transfusion (AOR 10.514, CI (1.752-63.113), P = 0.01) have significant association with the treatment outcome of death. Poor treatment outcome (death) was accounted for 4.4% of the pediatric patients hospitalized with community acquired pneumonia in this study setting. Based on the findings of this study Community acquired pneumonia is still a cause of substantial mortality of children under 15years old while on standardized treatment strategies. Antibiotic drug therapy change, taking increased number of drugs, loss of appetite and blood transfusion are the factors that contribute to this poor treatment outcome of CAP among children under 15years old.",
    "year" : 2024
    }
    38158959 | 9.4908
    {
    "id" : "38158959",
    "contents" : "[Diagnosis and antibiotic therapy of nosocomial pneumonia in adults: from recommendations to real practice. A review].. Nosocomial pneumonia is a healthcare-associated infection with significant consequences for the patient and the healthcare system. The efficacy of treatment significantly depends on the timeliness and adequacy of the antibiotic therapy regimen. The growth of resistance of gram-negative pathogens of nosocomial pneumonia to antimicrobial agents increases the risk of prescribing inadequate empirical therapy, which worsens the results of patient treatment. Identification of risk factors for infection with multidrug-resistant microorganisms, careful local microbiological monitoring with detection of resistance mechanisms, implementation of antimicrobial therapy control strategy and use of rational combinations of antibacterial drugs are of great importance. In addition, the importance of using new drugs with activity against carbapenem-resistant strains, including ceftazidime/aviabactam, must be understood. This review outlines the current data on the etiology, features of diagnosis and antibacterial therapy of nosocomial pneumonia.",
    "year" : 2023
    }
    38179988 | 9.4886
    {
    "id" : "38179988",
    "contents" : "Current treatment options for pneumonia caused by carbapenem-resistant Acinetobacter baumannii.. The purpose of this review is to briefly summarize the challenges associated with the treatment of pneumonia caused by carbapenem-resistant Acinetobacter baumannii (CRAB), discuss its carbapenem-resistance, and review the literature supporting the current treatment paradigm and therapeutic options. In a multicenter, randomized, and controlled trial the novel β-lactam-β-lactamase inhibitor sulbactam-durlobactam was compared to colistin, both in addition to imipenem-cilastatin. The drug met the prespecified criteria for noninferiority for 28-day all-cause mortality while demonstrating higher clinical cure rates in the treatment of CRAB pneumonia. In an international, randomized, double-blind, placebo controlled trial colistin monotherapy was compared to colistin combined with meropenem. In this trial, combination therapy was not superior to monotherapy in the treatment of drug-resistant gram-negative organisms including CRAB pneumonia. CRAB pneumonia is a preeminent public health threat without an agreed upon first line treatment strategy. Historically, there have been drawbacks to available treatment modalities without a clear consensus on the first-line treatment regimen. CRAB pneumonia is a top priority for the continued development of antimicrobials, adjuvant therapies and refinement of current treatment strategies.",
    "year" : 2024
    }
    39438303 | 9.2677
    {
    "id" : "39438303",
    "contents" : "Development of bacterial resistance in Germany from 2008 to 2022 - major culprit pathogens, antibacterial drugs, and prescribing practices.. Rising bacterial resistance is a global threat, causing rising financial burdens on healthcare systems and endangering effective treatment of bacterial infections. To ensure the efficacy of antibacterial drugs, it is essential to identify the most dangerous pathogens and vulnerable antibacterial drugs. Previous research by our group suggested irrational outpatient prescribing practices in Germany, supporting a growing bacterial resistance. This study analyses developments and characteristics for the ten most prescribed antibacterial drugs in Germany from 2008 to 2022. Conclusions are based on the development of bacterial resistance levels and an analysis of correlations between pathogens. We identified cefuroxime axetil, sulfamethoxazole-trimethoprim and nitrofurantoin as the most problematic drugs. Particularly problematic pathogens include E. faecalis, E. faecium, K. pneumoniae, and P. mirabilis. Besides increasing bacterial resistance, they are characterised by a high proportion of significant positive correlations, indicating a high potential for mutually reinforcing resistance development. Alarmingly, most of the antibacterial drugs analysed showed a growing resistance to at least one of the analysed pathogens. In most cases, the best treatment option is threatened by increasing bacterial resistance. We also identified several differences between current bacterial resistance data and therapeutic guidelines. In aggregate, our findings support irrational prescribing behaviour and underscore the urgent need for improved prescribing practices to counter rising bacterial resistance in Germany. Moreover, therapeutic guidelines for bacterial infections, the \"holy grail\" of pharmacotherapy, must be updated more frequently.",
    "year" : 2024
    }
    38414600 | 9.1477
    {
    "id" : "38414600",
    "contents" : "Strengthening pharmacotherapy research for COVID-19-induced pulmonary fibrosis.. The global spread of severe acute respiratory syndrome coronavirus 2 has resulted in a significant number of individuals developing pulmonary fibrosis (PF), an irreversible lung injury. This condition can manifest within a short interval following the onset of pneumonia symptoms, sometimes even within a few days. While lung transplantation is a potentially lifesaving procedure, its limited availability, high costs, intricate surgeries, and risk of immunological rejection present significant drawbacks. The optimal timing of medication administration for coronavirus disease 2019 (COVID-19)-induced PF remains controversial. Despite this, it is crucial to explore pharmacotherapy interventions, involving early and preventative treatment as well as pharmacotherapy options for advanced-stage PF. Additionally, studies have demonstrated disparities in anti-fibrotic treatment based on race and gender factors. Genetic mutations may also impact therapeutic efficacy. Enhancing research efforts on pharmacotherapy interventions, while considering relevant pharmacological factors and optimizing the timing and dosage of medication administration, will lead to enhanced, personalized, and fair treatment for individuals impacted by COVID-19-related PF. These measures are crucial in lessening the burden of the disease on healthcare systems and improving patients' quality of life.",
    "year" : 2024
    }
    38288808 | 9.1263
    {
    "id" : "38288808",
    "contents" : "Two Birds with One Stone: Drug Regime Targets Viral Pathogenesis Phases and COVID-19 ARDS at the Same Time.. Severe COVID-19 or severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) is a kind of viral pneumonia induced by infection with the coronavirus that causes ARDS. It involves symptoms that are a combination of viral pneumonia and ARDS. Antiviral or immunosuppressive medicines are used to treat many COVID-19 patients. Several drugs are now undergoing clinical studies in order to see if they can be repurposed in the future. In this study, In silico findings of used combination of drug repurposing and high-throughput docking methods presented acetaminophen, ursodiol, and β-carotene as a three-drug therapy regimen to treat ARDS induced by viral pneumonia in addition to inducing direct antiviral effects against COVID-19 viral infection. In the current study, drug repurposing and high throughput docking methods have been employed to develop combination drug regimens as multiple-molecule drugs for the therapy of COVID-19 and ARDS based on a multiple-target therapy strategy. This approach offers a promising avenue for the treatment of COVID-19 and ARDS, and highlights the potential benefits of drug repurposing in the fight against the current pandemic.",
    "year" : 2024
    }


# tanpa query expansion
dieksekusi dengan `docker compose --profile search run --rm search python scripts/search-eval.py pneumonia --no-expand`


## Asessmen gemini 3 pro:
Berikut adalah kurasi hasil pencarian untuk query `pneumonia` dengan filter treatment/therapy:

Document ID: 39661638
Relevan: Tidak
Alasan: Studi ini berfokus pada akurasi diagnosis pneumonia (bakteri vs virus) di UGD anak, bukan pada pengobatan atau terapi pneumonia itu sendiri.

Document ID: 39170646
Relevan: Tidak
Alasan: Artikel ini adalah studi kohort retrospektif yang meneliti hubungan antara mortalitas dengan komorbiditas trombositopenia pada pasien pneumonia, bukan studi tentang intervensi pengobatan.

Document ID: 39499730
Relevan: Ya
Alasan: Studi ini mengidentifikasi jalur Irg1/itaconate sebagai target terapeutik potensial untuk pengobatan *Mycoplasma pneumoniae* pneumonia.

Document ID: 38717726
Relevan: Tidak
Alasan: Artikel ini menganalisis hubungan dua arah antara pneumonia dan infeksi usus serta dampaknya terhadap prognosis, bukan membahas terapi obat untuk pneumonia.

Document ID: 38368746
Relevan: Tidak
Alasan: Artikel ini mengevaluasi temuan radiografis (X-ray dada) dari *adenovirus pneumonia* pada anak-anak, berfokus pada diagnosis visual, bukan terapi.

Document ID: 38801532
Relevan: Tidak
Alasan: Studi ini menganalisis pengaruh faktor meteorologi (suhu, kelembaban) terhadap insiden *Mycoplasma pneumoniae* pneumonia, bukan tentang pengobatan.

Document ID: 39637472
Relevan: Ya
Alasan: Artikel ini meneliti mekanisme formula obat tradisional Cina, Qingfei Yin (QFY), dalam mengobati *Streptococcus pneumoniae* pneumonia melalui promosi autophagy.

Document ID: 38229068
Relevan: Tidak
Alasan: Studi ini membahas epidemiologi molekuler, genotipe, dan resistensi makrolida pada *Mycoplasma pneumoniae* di Wuhan, fokus pada karakteristik patogen dan deteksi, bukan uji klinis pengobatan.

Document ID: 38920369
Relevan: Tidak
Alasan: Artikel ini adalah analisis farmakovigilans mengenai kasus pneumonia pada pasien yang diobati dengan clozapine (efek samping obat lain), bukan tentang pengobatan pneumonia itu sendiri.

Document ID: 39161635
Relevan: Tidak
Alasan: Studi ini menyelidiki utilitas diagnostik skor USG paru yang dimodifikasi (MLUS) untuk membedakan jenis pneumonia pada anak, fokus pada alat diagnostik.


## prompt:


    Konteks:
    Ini adalah hasil searching dengan lucene search pyserini.
    Yang di cari adalah ['pneumonia'] , dengan query ['pneumonia'] AND (treatment OR pharmacotherapy OR drug OR therapy)
    index dibangun dari subdataset 1.5juta artikel PubMed dalam 5 tahun terakhir.

    Tugas kamu adalah mengkurasikan hasil pencarian ini,
    apakah sesuai atau tidak untuk masing-masing hasil pencarian.
    Berikan jawaban dalam format:
    Document ID: <docid>
    Relevan: Ya/Tidak
    Alasan: <alasan singkat>

    hasil pencariannya adalah berikut ini:
    39661638 | 4.8922
    {
    "id" : "39661638",
    "contents" : "Accuracy of the diagnosis of pneumonia in Canadian pediatric emergency departments: A prospective cohort study.. The diagnosis of pediatric pneumonia and determination of the likely pathogen are complicated as the clinical picture overlaps with other respiratory illnesses, interpretation of radiographs is subjective, and laboratory results are rarely diagnostic. This study was designed to describe the relative rates of bacterial and viral pneumonia in the pediatric Emergency Department (ED), determine the accuracy of pediatric ED physicians' ability to diagnose pneumonia and distinguish bacterial from viral etiology, and to determine clinical and laboratory predictors of bacterial pneumonia. Children 3 months to 16 years of age presenting to seven Canadian pediatric EDs before the COVID-19 pandemic with fever and cough who had a chest radiograph performed for possible pneumonia were enrolled and underwent standardized clinical investigations. An expert panel was convened and reached a Consensus Diagnosis of typical or atypical bacterial pneumonia, viral pneumonia or not pneumonia for each case. The expert panel assessed 247 cases with the Consensus Diagnosis being typical bacterial pneumonia (N = 44(18%)), atypical bacterial pneumonia (N = 18(7%)), viral pneumonia (N = 46(19%)) and no pneumonia (N = 139(56%)). Treating ED physician diagnoses were typical bacterial pneumonia (N = 126(51%)), atypical bacterial pneumonia (N = 3(1%)), viral pneumonia (N = 10(4%)) and no pneumonia (N = 108(44%)) with low agreement between a diagnosis of bacterial pneumonia by the ED physician and the panel's Consensus Diagnosis (Kappa 0.15 (95% CI 0.08, 0.21)). Cut off values that predicted bacterial pneumonia as the Consensus Diagnosis were ESR ≥ 47 mm/hour, CRP ≥ 42 mg/L and procalcitonin ≥0.85 ng/m. Age greater than 5 years and cough for 5 or more days also predict bacterial pneumonia. In this cohort, pediatric ED physicians over-diagnosed typical bacterial pneumonia and underdiagnosed viral and atypical bacterial pneumonia. Bacterial pneumonia is most likely in children over 5 years of age, with cough for 5 or more days and/or with elevated inflammatory markers.",
    "year" : 2024
    }
    39170646 | 4.8671
    {
    "id" : "39170646",
    "contents" : "An Investigation of Mortality Associated With Comorbid Pneumonia and Thrombocytopenia in a Rural Southwest Missouri Hospital System.. Pneumonia places a significant burden on individuals and society, contributing to a substantial number of hospital admissions, emergency department visits, deaths, and healthcare costs each year. Comorbidities can greatly increase the risk of poor outcomes when associated with pneumonia. One comorbidity that has yet to be thoroughly researched is thrombocytopenia, which is known to play an important role in activating the immune response to infections. A decrease in platelet count may limit the immune response and consequently increase mortality in patients with pneumonia. The purpose of this study was to investigate whether comorbid thrombocytopenia and pneumonia are associated with poor outcomes. This study was a retrospective cohort analysis comparing mortality rates among patients with comorbid thrombocytopenia and pneumonia, pneumonia without thrombocytopenia, and thrombocytopenia without pneumonia. Data were collected from Freeman Health System using International Classification of Diseases, Tenth Revision (ICD-10) codes from January 1, 2019, to December 31, 2021. ICD-10 codes for pneumonia and thrombocytopenia were extracted and stratified into three groups: those with both pneumonia and thrombocytopenia, those with pneumonia without thrombocytopenia, and those with thrombocytopenia without pneumonia. Mortality rates were then compared across the three groups. There were 4,414 patients admitted with pneumonia and 1,157 admissions for thrombocytopenia without pneumonia. Among the 4,414 patients admitted with pneumonia, 3,902 did not have thrombocytopenia, while 512 had thrombocytopenia. Of the patients without thrombocytopenia, 14% (3,902) expired. Among the 512 patients with thrombocytopenia, 43% expired. In the thrombocytopenia without pneumonia group, 11% (1,157) expired. These results indicate a significant increase in mortality in patients with both pneumonia and thrombocytopenia compared to those with pneumonia without thrombocytopenia (an increase in mortality of 28.93% with a 95% CI: 24.50-33.36%, P < 0.0001). While pneumonia itself increases mortality compared to the general population, patients with both pneumonia and thrombocytopenia exhibit even higher mortality rates.",
    "year" : 2024
    }
    39499730 | 4.8340
    {
    "id" : "39499730",
    "contents" : "Suppressing neutrophil itaconate production attenuates Mycoplasma pneumoniae pneumonia.. Mycoplasma pneumoniae is a common cause of community-acquired pneumonia in which neutrophils play a critical role. Immune-responsive gene 1 (IRG1), responsible for itaconate production, has emerged as an important regulator of inflammation and infection, but its role during M. pneumoniae infection remains unknown. Here, we reveal that itaconate is an endogenous pro-inflammatory metabolite during M. pneumoniae infection. Irg1 knockout (KO) mice had lower levels of bacterial burden, lactate dehydrogenase (LDH), and pro-inflammatory cytokines compared with wild-type (WT) controls after M. pneumoniae infection. Neutrophils were the major cells producing itaconate during M. pneumoniae infection in mice. Neutrophil counts were positively correlated with itaconate concentrations in bronchoalveolar lavage fluid (BALF) of patients with severe M. pneumoniae pneumonia. Adoptive transfer of Irg1 KO neutrophils, or administration of β-glucan (an inhibitor of Irg1 expression), significantly attenuated M. pneumoniae pneumonia in mice. Mechanistically, itaconate impaired neutrophil bacterial killing and suppressed neutrophil apoptosis via inhibiting mitochondrial ROS. Moreover, M. pneumoniae induced Irg1 expression by activating NF-κB and STAT1 pathways involving TLR2. Our data thus identify Irg1/itaconate pathway as a potential therapeutic target for the treatment of M. pneumoniae pneumonia.",
    "year" : 2024
    }
    38717726 | 4.8335
    {
    "id" : "38717726",
    "contents" : "Bidirectional association between pneumonia and intestinal infection: an analysis of the MIMIC-IV database.. The purpose is to analyze the prevalence of intestinal infection in patients with pneumonia in intensive care units (ICU) and the impact of intestinal infection on the prognosis of patients with pneumonia, so as to explore the bidirectional association between pneumonia and intestinal infection. The study aims to investigate the correlation between the occurrence of pneumonia and intestinal infection among patients in the ICU, utilizing the Medical Information Mart for Intensive Care IV (MIMIC-IV) database, as well as the impact of intestinal infection on the prognosis of pneumonia patients. The enrolled patients were first divided into pneumonia group and non-pneumonia group, and the primary outcome was that patients developed intestinal infection. Multivariate logistic regression was used to elucidate the association between pneumonia and the prevalence of intestinal infection, and propensity score matching (PSM) and inverse probability of treatment weighing (IPTW) were used to validate our findings. We then divided patients with pneumonia into two groups according to whether they were complicated by intestinal infection, and analyzed the effect of intestinal infection on 28-day mortality, length of ICU stay, and length of hospital stay in patients with pneumonia. This study included 50,920 patients, of which 7493 were diagnosed with pneumonia. Compared with non-pneumonia patients, the incidence of intestinal infection in pneumonia patients was significantly increased [OR 1.58 (95% CI 1.34-1.85; P < 0.001)]. Cox proportional hazards regression model showed no significant effect of co-infection on 28-day mortality in patients with pneumonia (P = 0.223). Patients in the intestinal infection group exhibited a longer length stay in ICU and hospital than those without intestinal infection (P < 0.001). In the ICU, patients with pneumonia were more likely linked to intestinal infection. In addition, the presence of concurrent intestinal infections can prolong both ICU and hospital stays for pneumonia patients.",
    "year" : 2024
    }
    38368746 | 4.8277
    {
    "id" : "38368746",
    "contents" : "Radiographic findings of adenoviral pneumonia in children.. Adenovirus pneumonia is a common cause of community-acquired pneumonia in children and can mimic bacterial pneumonia, but there are few publications on its radiographic features. This study has evaluated the chest radiography findings of community-acquired adenovirus pneumonia in children. The frequency of radiological findings mimicking bacterial pneumonia was investigated. The clinical features of patients with adenovirus pneumonia possessing radiological findings mimicking bacterial pneumonia were also evaluated. The chest radiographs of patients diagnosed with adenovirus pneumonia were retrospectively reviewed. The chest radiographs were interpreted independently by a pediatric infectious disease specialist and a pediatric radiologist. Chest radiography findings mimicking bacterial pneumonia (bacterial-like) were specified as consolidation +/- pleural effusion. Other findings on chest radiography or a completely normal chest X-ray were specified as findings that were compatible with \"typical viral pneumonia\". A total of 1407 patients were positive for adenovirus with respiratory multiplex PCR. The 219 patients who met the study criteria were included in the study. Chest radiographs were normal in 58 (26.5 %) patients. The chest radiograph findings mimicked bacterial pneumonia in 41 (18.7 %) patients. Adenovirus pneumonia occurs predominantly in children aged five years and younger, as with other viral pneumonias. The radiographic findings in adenovirus pneumonia are predominantly those seen in viral pneumonia. Increasing age and positivity for only adenovirus without other viruses on respiratory multiplex PCR were associated with the chest radiograph being more likely to be \"bacterial-like\". Adenovirus may lead to lobar/segmental consolidation at a rate that is not very rare.",
    "year" : 2024
    }
    38801532 | 4.8277
    {
    "id" : "38801532",
    "contents" : "Effect of meteorological factors on the incidence of Mycoplasma pneumoniae pneumonia in Japan: a time series analysis.. Mycoplasma pneumoniae (M. pneumoniae) is a major cause of upper and lower respiratory tract infections and respiratory tract disease in humans. While accumulated pieces of epidemiological evidence suggest an association between meteorological factors and the risk of M. pneumoniae pneumonia, comprehensive nationwide studies on this topic are lacking. We aimed to systematically assess the effect of meteorological factors such as mean temperature and relative humidity on the incidence of M. pneumoniae pneumonia in Japan over a 15-year period from 2005 to 2019. The exposure - response relationships between incidence of M. pneumoniae pneumonia, mean temperature, and relative humidity in all 47 Japanese prefectures (covering whole country) for 2005 - 2019 were quantified by using a distributed lag non-linear model for each prefecture and the estimates from all the prefectures were then pooled using a multivariate mete-regression model to derive nationwide average associations. The study encompassed a total of 162,845 M. pneumoniae pneumonia cases. Our findings indicate that seasonal variations in weekly mean temperature and relative humidity were positively associated with the incidence of M. pneumoniae pneumonia. Specifically, when considering - 1.3 °C as the reference, the relative risk (RR) peaked at 16.8 °C (with RRs of 1.50, 95% confidence interval (CI): 1.32-1.70). Similarly, when using 45.5% relative humidity as the reference, the RR reached its peak at 87.7% (with RRs of 1.49, 95% CI: 1.33-1.67). These results emphasize the necessity of implementing climate change adaptation strategies and public health interventions in regions vulnerable to M. pneumoniae pneumonia.",
    "year" : 2024
    }
    39637472 | 4.8172
    {
    "id" : "39637472",
    "contents" : "Qingfei Yin alleviates Streptococcus pneumoniae pneumonia by promoting complete autophagy to suppress necroptosis.. Bacterial pneumonia is most prevalent among all pneumonia types, with Streptococcus pneumoniae being the main pathogen. Qingfei Yin (QFY) is a traditional Chinese medicine formula used in the clinical treatment of bacterial pneumonia. Previous studies have confirmed the multi-target and -effect characteristics of QFY in treating S. pneumoniae pneumonia. The purpose of this study was to explore the mechanism underlying QFY in treating pneumonia produced by S. pneumoniae. First, an in vivo model of S. pneumoniae-induced pneumonia was established in mice and evaluated the efficacy of QFY by hematoxylin-eosin (HE) staining and measuring cytokine levels in bronchoalveolar lavage fluid. Next, single-cell transcriptomics was used to identify the targeted cell subtypes, signaling pathways, and biological processes affected by QFY. Finally, the findings were validated using a pneumolysin (PLY) -induced mouse lung epithelial cells (TC-1) model in vitro using western blot analysis, immunofluorescence (IF), acridine orange (AO) staining, and propidium iodide (PI) staining. QFY was shown to alleviate lung inflammation and reduce the TNF-α and IL-6 levels in bronchoalveolar lavage fluid in vivo. A total of 113,353 cells were classified using single-cell transcriptomics and 12 major cell types were identified. By single-cell transcriptomics, QFY was confirmed to primarily target lung epithelial cells. Differentially expressed genes were shown to be enriched in autophagy and necroptosis signaling pathways, and the key differentially expressed gene, Sequestosome 1 (p62/SQSTM1), was identified. PLY was shown to induce RIPK1-dependent necroptosis and incomplete autophagy in TC-1 cells. QFY was shown to promote complete autophagy by downregulating the expression of p62, thereby reducing phosphorylation of RIPK1 and MLKL, and alleviating necroptosis in S. pneumoniae-induced lung epithelial cell death. This study demonstrated that QFY can effectively alleviate S. pneumoniae pneumonia. The mechanism of action may be that QFY promotes complete autophagy by downregulating p62 expression, thereby alleviating necroptosis of S. pneumoniae-induced lung epithelial cells and reducing lung injury. It provides a scientific basis for clinical prevention and treatment of S. pneumoniae pneumonia.",
    "year" : 2024
    }
    38229068 | 4.8156
    {
    "id" : "38229068",
    "contents" : "Molecular epidemiology of Mycoplasma pneumoniae pneumonia in children, Wuhan, 2020-2022.. Mycoplasma pneumoniae (M. pneumoniae) is an important pathogen of community-acquired pneumonia in children. The factors contributing to the severity of illness caused by M. pneumoniae infection are still under investigation. We aimed to evaluate the sensitivity of common M. pneumoniae detection methods, as well as to analyze the clinical manifestations, genotypes, macrolide resistance, respiratory microenvironment, and their relationship with the severity of illness in children with M. pneumoniae pneumonia in Wuhan. Among 1,259 clinical samples, 461 samples were positive for M. pneumoniae via quantitative polymerase chain reaction (qPCR). Furthermore, we found that while serological testing is not highly sensitive in detecting M. pneumoniae infection, but it may serve as an indicator for predicting severe cases. We successfully identified the adhesin P1 (P1) genotypes of 127 samples based on metagenomic and Sanger sequencing, with P1-type 1 (113/127, 88.98%) being the dominant genotype. No significant difference in pathogenicity was observed among different genotypes. The macrolide resistance rate of M. pneumoniae isolates was 96% (48/50) and all mutations were A2063G in domain V of 23S rRNA gene. There was no significant difference between the upper respiratory microbiome of patients with mild and severe symptoms. During the period of this study, the main circulating M. pneumoniae was P1-type 1, with a resistance rate of 96%. Key findings include the efficacy of qPCR in detecting M. pneumoniae, the potential of IgM titers exceeding 1:160 as indicators for illness severity, and the lack of a direct correlation between disease severity and genotypic characteristics or respiratory microenvironment. This study is the first to characterize the epidemic and genomic features of M. pneumoniae in Wuhan after the COVID-19 outbreak in 2020, which provides a scientific data basis for monitoring and infection prevention and control of M. pneumoniae in the post-pandemic era.",
    "year" : 2024
    }
    38920369 | 4.8156
    {
    "id" : "38920369",
    "contents" : "Investigating in VigiBase over 6000 cases of pneumonia in clozapine-treated patients in the context of the literature: focus on high lethality and the association with aspiration pneumonia.. The literature associates clozapine with pneumonia/aspiration pneumonia. The international pharmacovigilance database (VigiBase™) uses the information component (IC) as statistical signal. VigiBase clozapine reports were analyzed for pneumonia/aspiration pneumonia from introduction to 10 May 2023. There were 6392 cases of all types of pneumonia (5572 cases of pneumonia, 775 of aspiration pneumonia, and 45 combined). The IC was 3.52 for aspiration pneumonia, introduced as a VigiBase label in 2003, and 1.91 for pneumonia. Patients were reclassified as 3628 with no signs of aspiration and 1533 with signs. Signs of aspiration were strongly associated with some co-medications: olanzapine, odds ratio (OR) = 23.8, 95% confidence interval (CI), 14.9-38.0; risperidone OR = 18.6, CI, 11.4-30.4; valproic acid, OR = 5.5, CI, 4.5-6.6; and benzodiazepines OR = 5.5, CI, 4.5-6.6. In 2415 cases with completed data, fatal outcomes made up 45% (signs of aspiration made no difference), but there was wide variability from 0% (females <45 years of age; duration ≤30 days) to 76% (males >64 years of age; duration >1 year). During the first week, pneumonia was associated with 1) very high titration doses, 2) very small doses in Parkinson's disease, and 3) Japan vs other countries. In clozapine-treated patients: 1) at least 30% of pneumonia cases may be aspiration pneumonia, 2) stopping some co-medications may decrease the risk of aspiration pneumonia, 3) average lethality in pneumonia was 45% but may be around 75% in geriatric patients with long-term treatment, and 4) safer titrations may sometimes require 5-mg tablets.",
    "year" : 2024
    }
    39161635 | 4.8136
    {
    "id" : "39161635",
    "contents" : "Distinguishing types and severity of pediatric pneumonia using modified lung ultrasound score.. This study aimed to investigate the diagnostic utility of the modified lung ultrasound score (MLUS) in distinguishing between Mycoplasma pneumonia and viral pneumonia in children and evaluate their severity. A prospective collection of 137 suspected cases of community-acquired pneumonia in children admitted to the Quanzhou Maternity and Children's Hospital in Quanzhou City, Fujian Province, from January 2023 to December 2023 constituted the study cohort. All patients underwent lung ultrasound examinations, and MLUS scores were assigned based on ultrasound findings, including pleural lines, A-lines, B-lines, and lung consolidations. Based on the pathogenic results, the patients were categorized into the Mycoplasma pneumonia (74 cases) and viral pneumonia (63 cases) groups. The severity was classified as mild (110 cases) or severe (27 cases). The diagnostic value of MLUS for Mycoplasma pneumonia and viral pneumonia in children was analyzed. (1) MLUS scores were significantly different between the Mycoplasma pneumonia (15, 10-21) and viral pneumonia (8, 5-16) groups ( MLUS, coupled with ultrasound signs of large-area lung consolidation, had reference significance for the differential diagnosis of Mycoplasma pneumonia and viral pneumonia in children and can be a preliminary assessment of the severity of viral pneumonia or mycoplasma pneumonia in children.",
    "year" : 2024
    }