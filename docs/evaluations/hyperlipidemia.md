dieksekusi dengan `docker compose --profile search run --rm search python scripts/search-eval.py hyperlipidemia`

## hasil
skor 0.9


## Asessmen gemini 3 pro:
Berikut adalah kurasi hasil pencarian untuk query `Hyperlipidemia` dengan filter treatment/therapy:

Document ID: 38808220
Relevan: Ya
Alasan: Dokumen ini berisi pedoman klinis (guideline) pertama dari Iran untuk diagnosis, manajemen, dan pengobatan (termasuk farmakoterapi) hiperlipidemia pada orang dewasa.

Document ID: 38919858
Relevan: Ya
Alasan: Artikel ini merupakan tinjauan (review) tentang wawasan baru dalam pengobatan hiperlipidemia, mencakup pembaruan farmakologis dan pengobatan yang sedang berkembang (novel therapies).

Document ID: 38672720
Relevan: Ya
Alasan: Artikel ini membahas manajemen dyslipidemia pada orang dengan HIV, menekankan pada penggunaan statin, interaksi obat dengan terapi antiretroviral (HAART), dan opsi terapi tambahan.

Document ID: 39123552
Relevan: Ya
Alasan: Studi ini meneliti efek pengurangan hiperlipidemia yang diinduksi diet tinggi lemak pada tikus menggunakan anggur beras Cina (Huangjiu) sebagai strategi terapi diet potensial.

Document ID: 38278571
Relevan: Ya
Alasan: Artikel ulasan ini merangkum pengobatan standar, baru, dan yang sedang berkembang (novel pharmacotherapies) untuk hiperlipidemia dalam konteks pencegahan penyakit kardiovaskular.

Document ID: 38276246
Relevan: Ya
Alasan: Studi kohort retrospektif ini menyelidiki potensi terapeutik nitrat organik dalam mengurangi kematian setelah infark miokard akut pada pasien dengan hiperlipidemia.

Document ID: 39460970
Relevan: Ya
Alasan: Studi ini membandingkan efektivitas simvastatin tunggal dengan kombinasi simvastatin dan Beta vulgaris (bit) pada pasien hiperlipidemia.

Document ID: 38641919
Relevan: Tidak
Alasan: Artikel ini menganalisis diagnosis umum dan perawatan yang dicatat oleh mahasiswa kedokteran osteopatik pada populasi geriatri. Meskipun hiperlipidemia termasuk dalam diagnosis yang dicatat, fokus artikel adalah pada pola pencatatan diagnosis dan penggunaan Osteopathic Manipulative Treatment (OMT) secara umum, bukan studi mendalam tentang terapi hiperlipidemia itu sendiri.

Document ID: 39439657
Relevan: Ya
Alasan: Tinjauan sistematis ini mengevaluasi efikasi dan keamanan Inclisiran, obat baru dengan regimen dosis dua kali setahun, untuk pengobatan hiperkolesterolemia.

Document ID: 39715179
Relevan: Ya
Alasan: Ini adalah protokol untuk tinjauan sistematis dan meta-analisis yang bertujuan menilai efektivitas dan keamanan kombinasi ezetimibe dan statin dalam mengelola hiperlipidemia.


## prompt

    Konteks:
    Ini adalah hasil searching dengan lucene search pyserini.
    Yang di cari adalah ['Hyperlipidemia'] , dengan query ['Hyperlipidemia'] AND (treatment OR pharmacotherapy OR drug OR therapy)
    index dibangun dari subdataset 1.5juta artikel PubMed dalam 5 tahun terakhir.

    Tugas kamu adalah mengkurasikan hasil pencarian ini,
    apakah sesuai atau tidak untuk masing-masing hasil pencarian.
    Berikan jawaban dalam format:
    Document ID: <docid>
    Relevan: Ya/Tidak
    Alasan: <alasan singkat>

    hasil pencariannya adalah berikut ini:
    38808220 | 12.6563
    {
    "id" : "38808220",
    "contents" : "First Iranian guidelines for the diagnosis, management, and treatment of hyperlipidemia in adults.. This guideline is the first Iranian guideline developed for the diagnosis, management, and treatment of hyperlipidemia in adults. The members of the guideline developing group (GDG) selected 9 relevant clinical questions and provided recommendations or suggestions to answer them based on the latest scientific evidence. Recommendations include the low-density lipoprotein cholesterol (LDL-C) threshold for starting drug treatment in adults lacking comorbidities was determined to be over 190 mg/dL and the triglyceride (TG) threshold had to be >500 mg/dl. In addition to perform fasting lipid profile tests at the beginning and continuation of treatment, while it was suggested to perform cardiovascular diseases (CVDs) risk assessment using valid Iranian models. Some recommendations were also provided on lifestyle modification as the first therapeutic intervention. Statins were recommended as the first line of drug treatment to reduce LDL-C, and if its level was high despite the maximum allowed or maximum tolerated drug treatment, combined treatment with ezetimibe, proprotein convertase subtilisin/kexin type 9 inhibitors, or bile acid sequestrants was suggested. In adults with hypertriglyceridemia, pharmacotherapy with statin or fibrate was recommended. The target of drug therapy in adults with increased LDL-C without comorbidities and risk factors was considered an LDL-C level of <130 mg/dl, and in adults with increased TG without comorbidities and risk factors, TG levels of <200 mg/dl. In this guideline, specific recommendations and suggestions were provided for the subgroups of the general population, such as those with CVD, stroke, diabetes, chronic kidney disease, elderly, and women.",
    "year" : 2024
    }
    38919858 | 12.2644
    {
    "id" : "38919858",
    "contents" : "New Insights Into the Treatment of Hyperlipidemia: Pharmacological Updates and Emerging Treatments.. Cardiovascular diseases are the leading causes of global mortality and morbidity. Hyperlipidemia is a significant risk factor for atherosclerosis and subsequent cardiovascular diseases. Hyperlipidemia is characterized by imbalances in blood cholesterol levels, particularly elevated low-density lipoprotein cholesterol and triglycerides, and is influenced by genetic and environmental factors. Current management consists of lifestyle modifications and pharmacological interventions most commonly consisting of statins. This review paper explores pathophysiology, management strategies, and pharmacotherapies including commonly used well-established medications including statins, fibrates, and ezetimibe, exciting novel therapies including proprotein convertase subtilisin/kexin type 9 (PCSK9) inhibitors, and RNA interference therapies (inclisiran), lomitapide, and bempedoic acid, highlighting their mechanisms of action, clinical efficacy, and safety profiles. Additionally, emerging therapies under clinical trials including ApoC-III inhibitors, DGAT2 inhibitors, ACAT2 Inhibitors, and LPL gene therapies are examined for their potential to improve lipid homeostasis and cardiovascular outcomes. The evolving landscape of hyperlipidemia management underscores the importance of continued research into both established therapies and promising new candidates, offering hope for more effective treatment strategies in the future.",
    "year" : 2024
    }
    38672720 | 11.2638
    {
    "id" : "38672720",
    "contents" : "Pathophysiology and Clinical Management of Dyslipidemia in People Living with HIV: Sailing through Rough Seas.. Infections with human immunodeficiency virus (HIV) and acquired immune deficiency syndrome (AIDS) represent one of the greatest health burdens worldwide. The complex pathophysiological pathways that link highly active antiretroviral therapy (HAART) and HIV infection per se with dyslipidemia make the management of lipid disorders and the subsequent increase in cardiovascular risk essential for the treatment of people living with HIV (PLHIV). Amongst HAART regimens, darunavir and atazanavir, tenofovir disoproxil fumarate, nevirapine, rilpivirine, and especially integrase inhibitors have demonstrated the most favorable lipid profile, emerging as sustainable options in HAART substitution. To this day, statins remain the cornerstone pharmacotherapy for dyslipidemia in PLHIV, although important drug-drug interactions with different HAART agents should be taken into account upon treatment initiation. For those intolerant or not meeting therapeutic goals, the addition of ezetimibe, PCSK9, bempedoic acid, fibrates, or fish oils should also be considered. This review summarizes the current literature on the multifactorial etiology and intricate pathophysiology of hyperlipidemia in PLHIV, with an emphasis on the role of different HAART agents, while also providing valuable insights into potential switching strategies and therapeutic options.",
    "year" : 2024
    }
    39123552 | 10.5653
    {
    "id" : "39123552",
    "contents" : "Alleviation of High-Fat Diet-Induced Hyperlipidemia in Mice by . Hyperlipidemia is a chronic disease that is difficult to cure, and long-term pharmacotherapy may have negative consequences. Dietary therapy is a very promising strategy, and Chinese rice wine (Huangjiu) will play an important role because of its many biologically active components. In this work, the alleviating effect of",
    "year" : 2024
    }
    38278571 | 9.7600
    {
    "id" : "38278571",
    "contents" : "Novel Pharmacotherapies for Hyperlipidemia.. The link between elevated LDL-C, low HDL-C, elevated triglycerides, and an increased risk for cardiovascular disease has solidified over the past decades. Concomitantly, the number of agents to treat dyslipidemia proliferated in clinical trials, proving or refuting their clinical efficacy. Many of these agents' role in reducing cardiovascular disease morbidity and mortality is now clear. Recently, there has been an explosion in emerging therapeutics for the primary and secondary prevention of cardiovascular disease through the control of dyslipidemia. This article reviews standard, new, and emerging treatments for hyperlipidemia.",
    "year" : 2024
    }
    38276246 | 9.7586
    {
    "id" : "38276246",
    "contents" : "Investigation of the Therapeutic Potential of Organic Nitrates in Mortality Reduction Following Acute Myocardial Infarction in Hyperlipidemia Patients: A Population-Based Cohort Study.. Dyslipidemia is a known risk factor for cardiac dysfunction, and lipid-lowering therapy with statins reduces symptoms and reduces hospitalization related to left ventricular heart failure. Acute myocardial infarction (AMI) is a cause of morbidity and mortality worldwide. In this study, we aimed to determine the real-world AMI treatment drug combination used in Taiwan by using the NHI database to understand the treatment outcomes of current clinical medications prescribed for hyperlipidemia patients with AMI. Using the NHI Research Database (NHIRD), we conducted a retrospective cohort study that compared different treatments for AMI in hyperlipidemia patients in the period from 2016 to 2018. We compared the survival outcomes between those treated with and without organic nitrates in this cohort. We determined that most hyperlipidemia patients were aged 61-70 y (29.95-31.46% from 2016 to 2018), and the annual AMI risk in these patients was <1% (0.42-0.68% from 2016 to 2018). The majority of hyperlipidemia patients with AMI were women, and 25.64% were aged 61-70 y. Receiving organic nitrates was associated with lower all-cause mortality rates (HR, 95% CI, The survival benefit was significantly greater in patients treated with organic nitrates than in those treated without organic nitrates, especially when combined with diuretics. A combination of organic nitrates could be a better treatment option for hyperlipidemia patients with AMI.",
    "year" : 2024
    }
    39460970 | 9.5563
    {
    "id" : "39460970",
    "contents" : "Comparative and combination study of simvastatin alone and in combination with Beta vulgaris in hyperlipidemia patients.. Phytomedicine is gaining acceptance as well preference in health care management for various diseases. Drug combinations are mostly used clinically for hyperlipidemia, as single-agent therapy is insufficient. Statins remain the cornerstone of hyperlipidemia. The objective of the present research is to manage hyperlipidemia with the least amount of medicine effective clinically, thereby limiting its side effects. Study was carried out with 140 registered hyperlipidemia patients, divided into two groups. Group-A received simvastatin 20mg oral daily & Group B received a combination of simvastatin and beta-valgaris capsules twice a day for 90 days. Pre and post treatment values were compared within the groups and between the groups. Group B shows statistically significant decrease (p<0.05) in serum total cholesterol, low density lipoprotein (LDL), triglycerides (TG) and CRP levels. Also significant improvement (p<0.05) was noted for high density lipoprotein (HDL) levels (20.1% to 57.4%) in group B after completion of study. On the basis of our study results, we can conclude that statins remained to be the mainstay treatment for patients with elevated cholesterol levels. However, the combination has a synergistic effect and reduces oxidative stress (OS) as well.",
    "year" : 2024
    }
    38641919 | 9.5461
    {
    "id" : "38641919",
    "contents" : "Common outpatient diagnoses and associated treatments logged by osteopathic medical students within a geriatric population.. Clinical clerkships provide osteopathic medical students the opportunity to participate in the diagnosis and treatment of commonly encountered medical conditions. Appropriate management of these conditions may include pharmacotherapy and/or nonpharmacologic interventions, such as osteopathic manipulative treatment (OMT). Opportunities may exist to expand the utilization of OMT in the management of common conditions, particularly for geriatric patients, who are at increased risk for adverse outcomes from pharmacologic treatments. This study aimed to assess the most common diagnoses and corresponding treatments logged by osteopathic medical students within an ambulatory geriatric population. Patient encounters logged electronically by osteopathic medical students were retrospectively reviewed to determine the most commonly reported diagnostic codes and their treatments. Logged interventions were filtered to include patients over the age of 65 years who were seen on family medicine rotations within an ambulatory setting. The top 10 diagnoses were sorted and assessed to determine the associated treatments, including medications, procedures, and OMT. Between January 2018 and June 2020, a total of 11,185 primary diagnoses were logged pertaining to the defined patient population. The most frequently documented diagnoses were essential hypertension (n=1,420; 12.7 %), encounter for well examination (n=1,144; 10.2 %), type 2 diabetes mellitus (n=837; 7.5 %), hyperlipidemia (n=346; 3.1 %), chronic obstructive pulmonary disease (COPD; n=278; 2.5 %), osteoarthritis (OA; n=221; 2.0 %), low back pain (LBP; n=202; 1.8 %), pain in joint (n=187; 1.7 %), hypothyroidism (n=164; 1.5 %), and urinary tract infections (n=160; 1.4 %). Three of the top 10 logged diagnoses were musculoskeletal in nature (OA, LBP, and pain in joint). Pharmacotherapy was reported as the predominant treatment for musculoskeletal conditions, with OMT being logged as a treatment for 10.9 % (n=50) of those cases. The most commonly logged medication class in the management of patients with those musculoskeletal conditions was nonsteroidal anti-inflammatory drugs (NSAIDs; n=128; 27.9 %), while opioids were the second most frequently documented class of medications (n=65; 14.2 %). Musculoskeletal complaints were commonly logged by osteopathic medical students within the studied population. Opioids were documented as a treatment for musculoskeletal conditions more frequently than OMT. As such, opportunities exist to expand the utilization of OMT during clinical clerkships and to decrease the frequency of prescribed medications for pain management.",
    "year" : 2024
    }
    39439657 | 9.5146
    {
    "id" : "39439657",
    "contents" : "Inclisiran: A Systematic Review Exploring the Revolutionary Approach of Twice-Yearly Dosing Regimen in the Treatment of Hypercholesterolemia.. The global burden of hyperlipidemia is on the rise, along with an increase in associated cardiovascular complications. Since most of the patients affected by hyperlipidemia are elderly individuals with multiple comorbidities, the introduction of even a single additional drug for asymptomatic conditions such as hyperlipidemia can drastically reduce treatment compliance due to their long medication history. Hence, researchers are trying to come up with a drug with a long duration of action requiring less frequent dosing without compromising compliance and improving the outcome. This led to the discovery of inclisiran, a \"wonder drug\" that utilizes small interference RNA and requires only twice-yearly administration to maintain patients' lipid levels at optimal levels. We conducted a systematic review by following standardized guidelines on the long-term efficacy and safety of the new drug, inclisiran, in the treatment of hypercholesterolemia. We conducted an advanced search on PubMed using the MeSH strategy and then employed appropriate keywords to search other major databases, such as PubMed Central and Medline, using various inclusion and exclusion criteria, which yielded 94 articles from various databases. We narrowed down the search to 10 randomized controlled trials (ORION trials) after removing duplicates and screening for irrelevant titles for inclusion in the study. The ORION trials on inclisiran evaluated the drug's impact on various parameters, such as low-density lipoprotein-cholesterol (LDL-C), proprotein convertase subtilisin/kexin type 9 (PCSK9), high-density lipoprotein (non-HDL), apolipoprotein B (apoB), and so on, while considering the safety aspects of the drug. All the trials indicate greater efficacy of inclisiran and long-term maintenance of the results achieved when compared to a placebo and showed a long dosing interval, thereby increasing treatment compliance. Additionally, as the drug's dose increased, we observed greater reductions in the mentioned parameters without a significant increase in the incidence of adverse events. According to the review's data analysis, inclisiran, with its greater efficacy, has the potential to replace conventional pharmacological therapy in the near future, with the best results achieved when combined with lifestyle modifications. However, a long-term assessment of the drug's efficacy and safety is required before implementing it in clinical practice to identify any potential safety concerns, particularly related to the administration of higher dosage over a longer period.",
    "year" : 2024
    }
    39715179 | 9.1879
    {
    "id" : "39715179",
    "contents" : "Protocol for a systematic review and meta-analysis of the combination of ezetimibe and statins for hyperlipidemia.. Hyperlipidemia is increasingly recognized as a significant global health issue, often associated with conditions such as hypertension, diabetes, and obesity. While statins are frequently prescribed to manage lipid levels, recent studies indicate that reliance solely on statin therapy may present certain disadvantages, including prolonged treatment durations, the potential for drug resistance, and various adverse effects. Research indicates that the combination of ezetimibe and statins demonstrates a favorable therapeutic effect in the management of hyperlipidemia. However, existing studies have not consistently confirmed these benefits, and there is no current meta-analysis available. As a result, we will perform a meta-analysis to assess the effectiveness and safety of the combination of ezetimibe and statins in managing hyperlipidemia, aiming to offer evidence-based medical guidance for clinical practice. The systematic review and meta-analysis will adhere to the PRISMA guidelines for systematic reviews and meta-analyses. We will search for randomized controlled trials that investigate the efficacy and safety of the combination of ezetimibe and statins in treating hyperlipidemia, based on specific criteria. The following electronic databases will be searched by two researchers for relevant records published up to October 1, 2024: Cochrane Central Register of Controlled Trials (CENTRAL) in Cochrane Library, Embase.com, Web of Science, MEDLINE (via PubMed), Wanfang China Database, China National Knowledge Infrastructure (CNKI), Chinese Biomedical Literature Database (CBM) and Chinese Scientific Journal Database (VIP). They will also check references and relevant journals manually. Two independent reviewers will handle screening, data extraction, and quality assessment. Subgroup analysis, sensitivity analysis, and publication bias analysis will be performed to assess consistency and reliability. Review Manager 5.4 will be used for data analysis and synthesis, while the GRADE approach will be employed to evaluate the overall study's evidence quality. The findings of this systematic review will be shared with various stakeholders who are interested in the combination of ezetimibe and statins for hyperlipidemia. This will offer valuable insights for researchers undertaking future investigations and for clinical practitioners specializing in the treatment of hyperlipidemia. This study is based on a secondary analysis of the literature, so ethical review approval is not required. The final report will be published in a peer-reviewed journal. The protocol of the systematic review has been registered on Open Science Framework, with a registration DOI https://doi.org/10.17605/OSF.IO/TEVUY.",
    "year" : 2024
    }
