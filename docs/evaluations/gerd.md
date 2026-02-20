dieksekusi dengan `docker compose --profile search run --rm search python scripts/search-eval.py gerd`

## hasil
skor 1


## Asessmen gemini 3 pro:
Berikut adalah kurasi hasil pencarian untuk query `GERD` dengan filter treatment/therapy:

Document ID: 38767884
Relevan: Ya
Alasan: Artikel ini memberikan gambaran umum tentang manajemen GERD, termasuk faktor risiko, gejala, pendekatan diagnosis, dan opsi pengobatan mulai dari modifikasi gaya hidup, farmakoterapi (PPI, vonoprazan), hingga intervensi prosedural.

Document ID: 38348994
Relevan: Ya
Alasan: Studi prospektif ini mengevaluasi keamanan dan kemanjuran teknik endoskopi baru (Anti-Reflux Mucosectomy/ARMS dan Anti-Reflux Mucosal Ablation/ARMA) sebagai pengobatan potensial untuk pasien GERD yang refrakter terhadap PPI.

Document ID: 39106391
Relevan: Ya
Alasan: Tinjauan ini membahas strategi terapeutik inovatif untuk GERD, mencakup metode tradisional (farmakoterapi, gaya hidup) serta pendekatan baru seperti prosedur perbaikan endoskopi canggih dan pengobatan inovatif.

Document ID: 39193078
Relevan: Ya
Alasan: Artikel ini meninjau bukti saat ini mengenai penggunaan terapi tidak berkelanjutan (noncontinuous therapy) seperti *on-demand* atau *intermittent* pemberian PPI dan P-CABs (Potassium-Competitive Acid Blockers) untuk manajemen GERD.

Document ID: 38607207
Relevan: Ya
Alasan: Studi ini mengeksplorasi perbedaan karakteristik motilitas esofagus dan refluks pada pasien GERD dengan batuk kronis (CC) serta dampak terapi obat standar terhadap gejala dan parameter objektif.

Document ID: 39733305
Relevan: Ya
Alasan: Uji klinis acak ini mengevaluasi efikasi dan keamanan terapi kombinasi PPI dan agen pelindung mukosa (MPA) topikal untuk meredakan gejala dan mempercepat penyembuhan esofagitis erosif pada pasien GERD.

Document ID: 39189409
Relevan: Ya
Alasan: Tinjauan ini merangkum pengetahuan saat ini tentang keamanan jangka pendek dan jangka panjang dari Potassium-Competitive Acid Blockers (P-CABs) seperti vonoprazan dalam pengobatan GERD dibandingkan dengan PPI.

Document ID: 38367746
Relevan: Ya
Alasan: Analisis ekonomi ini menilai nilai ambang batas (threshold value) pengembangan obat baru (khususnya P-CABs) untuk GERD, dengan fokus pada penghentian gejala *heartburn* (nyeri ulu hati) sebagai kebutuhan klinis yang belum terpenuhi.

Document ID: 38803638
Relevan: Ya
Alasan: Laporan kasus ini menyoroti pentingnya intervensi dini dan pemilihan penekan asam yang tepat (beralih dari H2RA ke PPI atau P-CAB) pada kasus GERD anak yang disebabkan oleh hernia hiatus.

Document ID: 38869961
Relevan: Ya
Alasan: Meta-analisis ini mengevaluasi keamanan dan efektivitas Baclofen sebagai terapi tambahan untuk GERD refrakter (r-GERD), khususnya dalam mengurangi episode refluks non-asam.

## prompt

    Konteks:
    Ini adalah hasil searching dengan lucene search pyserini.
    Yang di cari adalah ['gerd'] , dengan query ['gerd'] AND (treatment OR pharmacotherapy OR drug OR therapy)
    index dibangun dari subdataset 1.5juta artikel PubMed dalam 5 tahun terakhir.

    Tugas kamu adalah mengkurasikan hasil pencarian ini,
    apakah sesuai atau tidak untuk masing-masing hasil pencarian.
    Berikan jawaban dalam format:
    Document ID: <docid>
    Relevan: Ya/Tidak
    Alasan: <alasan singkat>

    hasil pencariannya adalah berikut ini:
    38767884 | 13.3517
    {
    "id" : "38767884",
    "contents" : "Gastrointestinal Conditions: Gastroesophageal Reflux Disease.. Gastroesophageal reflux disease (GERD) affects more than 20% of adults. Risk factors include older age, obesity, smoking, and sedentary lifestyle. Lower esophageal sphincter (LES) dysfunction is a primary cause. Classic symptoms include heartburn and regurgitation. With classic symptoms, proton pump inhibitors (PPIs) can be prescribed without further testing; PPIs should be taken on an empty stomach. Patients with atypical symptoms and those not benefiting from management should undergo esophagogastroduodenoscopy (EGD), and potentially pH and impedance testing to confirm GERD or identify other conditions. This is important because GERD increases risk of esophageal erosions/stricture, Barrett esophagus, and esophageal adenocarcinoma. However, a large percentage of adults taking PPIs have no clear indication for treatment, and PPIs and other antisecretory therapy should be tapered off if possible. Of note, vonoprazan, a new drug approved by the Food and Drug Administration (FDA), has shown superiority to PPIs. In addition to pharmacotherapy, lifestyle changes are indicated, including losing weight if overweight, not lying down after meals, and ceasing tobacco use. Procedural interventions, including fundoplication and magnetic sphincter augmentation, can be considered for patients wishing to discontinue drugs or with symptoms unresponsive to PPIs. Procedural interventions are effective for the first 1 to 3 years, but effectiveness decreases over time.",
    "year" : 2024
    }
    38348994 | 13.2307
    {
    "id" : "38348994",
    "contents" : "Endoscopic anti-reflux mucosectomy (ARMS) and endoscopic anti-reflux ablation (ARMA) as a potential treatment for gastroesophageal reflux - preliminary report.. &lt;b&gt;&lt;br&gt;Introduction:&lt;/b&gt; Gastroesophageal reflux (GERD) is one of the most common disorders of the alimentary tract. Apart from troublesome symptoms, untreated GERD can lead to Barrett's esophagus and, as a consequence, esophageal adenocarcinoma. As for now, the most common treatment of GERD is PPI pharmacotherapy. However, in a number of cases, this treatment is not sufficient or the patient does not tolerate PPI-group drugs. In such cases, interventional therapy is recommended. So far, laparoscopic fundoplication has been the only suggested option. Other, minimally invasive procedures such as Stretta, MUSE, TIFF, or EsophyX were not recommended due to the lack of clinical data. In 2014, Professor H.Inoue from the Digestive Diseases Center, Showa University in Japan reported on the first series of novel, endoscopic, anti-reflux procedures: anti-reflux mucosectomy (ARMS) and anti-reflux mucosal ablation (ARMA).&lt;/br&gt; &lt;b&gt;&lt;br&gt;Methods:&lt;/b&gt; We conducted our prospective, single-center study in 30 patients (14 female, 16 male) with PPI-refractory GERD. All patients underwent FSSG and GERD-HRQL evaluation and GE junction pressure study prior, 6 weeks and 6 months after the procedures. After the procedure, all patients received PPI treatment for 4 weeks.&lt;/br&gt; &lt;b&gt;&lt;br&gt;Results:&lt;/b&gt; We successfully completed the procedures in all 30 patients. The mean procedure time was 42 minutes. No complications occurred. In 86.67% (26) of our patients, we achieved total remission of GERD symptoms, FSSG scores &lt; 6 and GERD-HRQL scores &lt; 8.&lt;/br&gt; &lt;b&gt;&lt;br&gt;Conclusions:&lt;/b&gt; The results of our study show that ARMS and ARMA are simple, safe, improve GERD-related symptoms, and restore the GE junction's anti-reflux capacity.&lt;/br&gt.",
    "year" : 2023
    }
    39106391 | 12.2744
    {
    "id" : "39106391",
    "contents" : "Innovative therapeutic strategies in the treatment of gastroesophageal reflux disease (GERD): A review of progress and perspectives.. Gastroesophageal Reflux Disease (GERD) is a commonly occurring condition that can significantly impact quality of life. Often considered a lifestyle disease. Traditional treatment methods focus on pharmacotherapy, lifestyle modifications, and in extreme cases, surgical interventions. This article discusses current and novel approaches to managing gastroesophageal reflux disease. The foundation of this work was medical articles and research gathered from the PubMed database. Keywords such as \"esophageal reflux treatment\", \"new technologies in GERD treatment\", \"innovative reflux treatment methods\", were used to facilitate the literature search. In managing gastroesophageal reflux disease, the application of appropriate pharmacological therapy and lifestyle changes for the patient remains key. However, new technologies and treatment methods, such as advanced endoscopic repair procedures, innovative medications, and personalized approaches, are gaining importance. These new strategies can significantly improve patients' quality of life, reduce symptoms, and minimize the need for surgical interventions.",
    "year" : 2024
    }
    39193078 | 11.6779
    {
    "id" : "39193078",
    "contents" : "Is It Time for Noncontinuous Therapy for Gastroesophageal Reflux Disease?. Gastroesophageal reflux disease (GERD) is a chronic disorder characterized by the reflux of gastric contents into the esophagus, leading to symptoms and potential long-term complications such as Barrett esophagus and esophageal adenocarcinoma. Currently, there are various medical, endoscopic, and surgical therapeutic strategies for GERD. However, proton pump inhibitors (PPIs), which effectively suppress acid secretion but require daily administration, remain the mainstay of treatment. Noncontinuous therapy for GERD includes on-demand and different variations of intermittent administration of antireflux medication. Attributes that make an antireflux medication a good candidate for noncontinuous therapy for GERD include potent acid suppression, rapid effect, durability of antisecretory effect, and flexibility of administration. Noncontinuous therapy for GERD is appealing to patients because it is convenient, reduces cost, and alleviates concerns about complications of long-term PPI use. Patients with nonerosive esophageal reflux disease or low-grade erosive esophagitis who have episodic heartburn are probably best suited for such treatment. Although PPIs have been shown to be efficacious as on-demand or intermittent therapy for GERD, their usefulness as on-demand treatment for episodic heartburn has been limited by their slow maximal effect on intragastric acid secretion. In contrast, potassium-competitive acid blockers (P-CABs) demonstrate the pharmacokinetic and pharmacodynamic characteristics that make this class of drugs a good candidate for noncontinuous treatment of GERD. Early studies using P-CABs for noncontinuous treatment of GERD have demonstrated promising results. Future studies are needed to further establish the value of P-CABs for such a therapeutic approach. This article reviews the current evidence on the use of PPIs and P-CABs in noncontinuous therapy for GERD.",
    "year" : 2024
    }
    38607207 | 11.3091
    {
    "id" : "38607207",
    "contents" : "Difference of Esophageal Motility and Reflux Characteristics in Patients with Gastroesophageal Reflux Disease (GERD) and Chronic Cough (CC) and the Impact of Standardized Drug Therapy.. This study aimed to explore the difference between esophageal motility and reflux characteristics in patients with gastroesophageal reflux disease (GERD) and chronic cough (CC) and the effect of standardized drug therapy. Eighty-four patients diagnosed with GERD in The First People's Hospital of Hangzhou from December 2020 to December 2022 were enrolled in this study. They were divided into an observation group (Obs group, patients with GERD + CC, n = 26 cases) and a control group (control group, patients with typical GERD, n = 58 cases). Reflux symptom integral questionnaire, cough symptom integral questionnaire, high-resolution esophageal manometry (HRM), and 24-hour esophageal pH/impedance monitoring were performed. The upper esophageal sphincter pressure at resting (UESP) and distal systolic score (DCI) in the Obs group were much lower. They exhibited differences with P < .05 than those in the control group. The total numbers of proximal reflux, proximal weak acid reflux, proximal non-acid reflux, weak acid reflux, and gas-liquid mixed reflux in the Obs group were more. They showed a difference with P < .05 than those in the control group. After a standard treatment, the reflux symptom score of patients with GERD + CC was greatly lower than those of patients with typical GERD (P < .05). Ineffective esophageal motility (IEM) was dominant in patients with GERD +CC. HRM and 24-hour pH/impedance monitoring can objectively evaluate the properties of esophageal motility and reflux, respectively, which had a guiding significance for individual patient treatment.",
    "year" : 2024
    }
    39733305 | 11.1202
    {
    "id" : "39733305",
    "contents" : "The Mucosal Protection in the Treatment of Erosive Reflux Esophagitis: Mechanisms for Restoring Epithelial Permeability. A Randomized Clinical Trial.. Gastroesophageal reflux disease (GERD) is widespread in the population and is characterized by the risk of developing Barrett's esophagus and associated adenocarcinoma. Key factors in the progression of the disease are not only the frequency and duration of reflux episodes, but also the resistance of the esophageal mucosa to aggressive reflux molecules. Assessment of the state of tight junction proteins, the rate of their recovery under the influence of various treatment regimens is an urgent task for choosing optimal approaches to curing patients with GERD. The purpose of the study was to evaluate the efficacy and safety of the combination therapy with a proton pump inhibitor (PPI) and a topical mucosal protective agent (MPA) to relieve GERD symptoms and achieve a complete remission of reflux esophagitis faster. 60 patients (38 men and 22 women with an average age 41.5 years) with GERD duration of 5 years, took part in an open randomized prospective clinical study. Participants were randomized in a 1:1 ratio to be divided into the main group taking MPA and PPI and a comparison group taking a PPI only. The duration of therapy was 4 weeks. Before the treatment onset and after the end of treatment, the occurrence and severity of GERD symptoms were assessed, an endoscopic examination was performed and biopsy specimens were taken from the edge of the erosive area and the area of unchanged esophageal mucosa. The severity of histological signs of esophagitis, the expression of tight junction proteins and the proliferation marker Ki-67 were assessed. A more effective relief of GERD symptoms was documented when using combination therapy PPIs and MPAs. A more pronounced reduction in macroscopic changes was found in patients with erosive esophagitis taking PPIs and MPAs. The use of MPAs in addition to PPIs made it possible to achieve the primary and secondary endpoints more often, which suggested a high efficiency of the drug in combination with PPIs in the treatment of erosive esophagitis. An individualized approach based on the combination therapy of PPIs and MPAs can improve the effectiveness of treatment in achieving clinical, endoscopic and, more importantly, histological remission in a patient with erosive GERD.",
    "year" : 2024
    }
    39189409 | 10.6786
    {
    "id" : "39189409",
    "contents" : "Safety of potassium-competitive acid blockers in the treatment of gastroesophageal reflux disease.. Proton pump inhibitors (PPIs) are the first-line treatment for gastroesophageal reflux disease (GERD). However, due to their intrinsic limitations, there are still unmet clinical needs that have fostered the development of potassium-competitive acid blockers (P-CABs). Currently, four different drugs (vonoprazan, tegoprazan, fexuprazan, and keverprazan) are marketed in some Asian countries, whereas only vonoprazan and tegoprazan are available in Western countries (USA and Brazil or Mexico, respectively). This review summarizes the current knowledge on P-CABs acute and long-term safety in GERD treatment compared to that of PPIs. Full-text articles and abstracts were searched in PubMed. P-CABs proved to address some of the unmet clinical needs in GERD, with a favorable risk-benefit ratio compared to conventional PPIs. Preclinical and clinical findings have highlighted P-CAB safety to be superimposable, to that of PPIs, in short-term treatments, although further studies are warranted to monitor their effects in long-term therapy. From an epidemiological point of view, the paucity of rigorous data for many variables (e.g. age, ethnicity, drug interactions, comorbidities, genetic polymorphisms, interindividual susceptibility, and gut dysbiosis) deserves a worldwide framework of continuous pre/post-marketing pharmacovigilance programs to reduce potential confounding factors and accurately link acute and chronic P-CAB therapy to adverse outcomes.",
    "year" : 2025
    }
    38367746 | 10.4973
    {
    "id" : "38367746",
    "contents" : "Heartburn Relief Is the Major Unmet Need for Drug Development in Gastroesophageal Reflux Disease: Threshold Value Analysis.. Heartburn symptoms contribute to healthcare-seeking among patients with gastroesophageal reflux disease (GERD). Despite clinical guidance, management is often dictated by insurance restrictions. Several potassium-competitive acid blockers (PCABs) are under development as a new class of therapy. We performed economic analyses to align GERD drug development with the needs of gastroenterologists, insurers and patients in a value-based environment. A decision-analytic model was constructed to compare vonoprazan 20 mg daily (an example of a PCAB), common over-the-counter or prescription proton pump inhibitor regimens, and no treatment over a 1-year time horizon. Clinical responses were evaluated based on the proportions of heartburn-free days in a recent phase 3 multicenter trial. Healthcare utilization for persistent reflux symptoms was derived from national observational studies compared with healthy control subjects. Costs and quality-adjusted life years were reported. Without insurance coverage for appropriate therapy, patients spend $4443 and insurers spend $3784 on average per year for inadequately treated GERD symptoms. Our model estimates that PCABs could save at least $3000 in annual costs to patients and insurers, could generate quality-adjusted life year gains (+0.06 per year), and could be cost-saving to insurers as a covered option at a price up to $8.57 per pill, if these drugs are able to demonstrate similar effectiveness to proton pump inhibitors in future trials evaluating heartburn relief and erosive esophagitis healing to regulators. Threshold prices reflect pricing after all pharmacy benefits manager rebates and discounts. We demonstrate that aiming GERD-related drug development toward heartburn relief appears critical to align cost-effective incentives for industry and insurers with those of patients and gastroenterologists.",
    "year" : 2024
    }
    38803638 | 10.4534
    {
    "id" : "38803638",
    "contents" : "Case Report: The importance of early intervention for gastroesophageal reflex disease caused by hiatal hernia.. Gastroesophageal reflux (GER) disease (GERD) is a condition wherein GER causes troublesome symptoms that can affect daily functioning and/or clinical complications within the esophagus or other systems. To avoid this, patients with GERD often require treatment; hence, it is important to distinguish GER from GERD. Patients with GERD exhibiting alarm signs should be examined early to differentiate it from GER and treated accordingly. Herein, we present a case of GERD caused by a hiatal hernia that required surgical intervention for esophagial cicatrical stenosis despite oral treatment. We also discussed how to choose the appropriate acid suppressants for GERD. A 1-year-old boy was referred to our hospital for repeated vomiting and poor weight gain. He received histamine 2 receptor antagonists (H2RAs) that contributed slightly to the decreased frequency of vomiting and aided weight gain; however, he soon stopped gaining weight and had bloody vomit. His upper gastrointestinal series revealed hiatal hernia, a 24 h impedance pH monitoring test indicated abnormal values for acid reflux, and esophagogastroduodenoscopy (EGD) revealed esophagitis. He was subsequently diagnosed with GERD associated with hiatal hernia. A proton pump inhibitor (PPI) was intravenously administered to him, following which his medication was changed to a potassium-competitive acid blocker (P-CAB). Thereafter, his vomiting episodes significantly decreased and his weight increased. However, 6 months after starting P-CAB, his vomiting episodes suddenly increased in frequency. EGD revealed the presence esophageal stricture due to scarring from GERD. He was then treated via laparoscopic fundoplication, gastrostomy, and esophageal balloon dilation. Thereafter, his vomiting episodes stopped and food intake improved, leading to weight gain. It is essential to identify the cause of GERD early and take an appropriate treatment approach depending on the cause of GERD with alarm signs. Further, as a drug therapy for GERD as a clear acid mediated disease or in children with alarm signs, PPIs or P-CAB should be used from the beginning instead of H2RAs.",
    "year" : 2024
    }
    38869961 | 10.4393
    {
    "id" : "38869961",
    "contents" : "Efficacy of Baclofen as Add-on Therapy for Refractory Gastroesophageal Reflux Disease: A Meta-analysis.. As a GABAB receptor agonist, baclofen has demonstrated efficacy in alleviating symptoms of refractory gastroesophageal reflux disease (r-GERD). This meta-analysis aims to evaluate the safety and effectiveness of baclofen as an add-on therapy for this condition. We conducted a comprehensive search of the PubMed, Embase, and Web of Science databases for studies published up until October 2023. Subsequently, we performed a meta-analysis encompassing all eligible trials. From 719 records, 10 studies were included, most of these studies were moderate risk. The findings demonstrated that the addition of baclofen as a supplementary treatment effectively improves symptoms (GERD Q score) in r-GERD (standardized mean difference=-0.78, 95% CI: -1.06 to -0.51, I2=0%). The addition of this treatment also resulted in a decrease in the frequency of nonacidic reflux episodes (standardized mean difference=-0.93, 95% CI: -1.49 to -0.37, I2=63%) and an improvement in DeMeester scores (standardized mean difference=-0.82, 95% CI: -1.61 to -0.04, I2=81%) among patients with r-GERD when compared with the use of proton pump inhibitor (PPI) drugs alone. However, no significant disparity was observed in terms of reducing acid reflux episodes (standardized mean difference=-0.12, 95% CI: -0.49 to 0.19, I2=0%) and proximal reflux (standardized mean difference=-0.47, 95% CI: -1.08 to 0.14, I2=60%). Baclofen as an add-on treatment can effectively improve the symptoms of patients with r-GERD and reduce the incidence of nonacidic reflux and improve DeMeester score. However, long-term use of baclofen leads to an increased incidence of side effects and is not effective in reducing the occurrence of acid reflux.",
    "year" : 2024
    }