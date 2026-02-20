dieksekusi dengan `docker compose --profile search run --rm search python scripts/search-eval.py Depressive Disorder`

## hasil
skor 1.0


## Asessmen gemini 3 pro:
Berikut adalah kurasi hasil pencarian untuk query `Depressive Disorder` dengan filter treatment/therapy:

Document ID: 39742882
Relevan: Ya
Alasan: Studi uji terkontrol acak (RCT) ini mengevaluasi efektivitas dan keamanan Terapi Perilaku Kognitif berbasis Realitas Virtual (VR-CBT) sebagai alternatif atau tambahan terhadap farmakoterapi standar untuk mengurangi gejala depresi dan tendensi bunuh diri.

Document ID: 39072563
Relevan: Ya
Alasan: Tinjauan ini membahas penggunaan biomarker farmakogenomik dan farmakometabolomik untuk mempersonalisasi dan mengoptimalkan efikasi serta keamanan pengobatan antidepresan, khususnya SSRI.

Document ID: 39664326
Relevan: Ya
Alasan: Meta-analisis dan tinjauan sistematis ini membandingkan efek jangka panjang (enduring effects) dari psikoterapi, antidepresan, dan kombinasi keduanya setelah penghentian pengobatan pada orang dewasa dengan depresi.

Document ID: 38687843
Relevan: Ya
Alasan: Tinjauan sistematis ini menilai efikasi menambahkan psikoterapi psikodinamik jangka pendek (STPP) ke farmakoterapi (antidepresan) pada pasien dengan gangguan depresi, baik dalam jangka pendek maupun panjang.

Document ID: 39039791
Relevan: Ya
Alasan: Artikel profil obat ini membahas kombinasi baru dextromethorphan dan bupropion (Auvelity®) sebagai opsi farmakoterapi untuk Major Depressive Disorder (MDD), mencakup mekanisme, efikasi, dan keamanan.

Document ID: 38776336
Relevan: Ya
Alasan: Dokumen ini adalah protokol untuk tinjauan sistematis dan meta-analisis yang bertujuan menilai efektivitas penambahan Terapi Perilaku Dialektis (DBT) ke farmakoterapi untuk depresi yang resistan terhadap pengobatan (TRD).

Document ID: 39067131
Relevan: Ya
Alasan: Meta-analisis ini mengevaluasi efektivitas terapi cahaya terang (Bright Light Therapy) sebagai modalitas pengobatan tambahan untuk psikoterapi dan farmakoterapi dalam mengurangi gejala Major Depressive Disorder (MDD).

Document ID: 38493750
Relevan: Ya
Alasan: Studi kohort retrospektif ini membandingkan efektivitas terapi elektrokonvulsif (ECT) dikombinasikan dengan farmakoterapi versus farmakoterapi saja pada remaja dengan MDD dan ide bunuh diri.

Document ID: 38875916
Relevan: Ya
Alasan: Studi nasional ini mengukur prevalensi penggunaan layanan dan ketepatan pengobatan (termasuk farmakoterapi yang direkomendasikan) pada mahasiswa kedokteran dan residen yang mengalami depresi di Prancis.

Document ID: 39758440
Relevan: Ya
Alasan: Studi label terbuka ini membandingkan efikasi rTMS (Repetitive Transcranial Magnetic Stimulation) yang dipandu MRI struktural dikombinasikan dengan farmakoterapi versus farmakoterapi saja pada remaja dengan MDD.

## prompt


    Konteks:
    Ini adalah hasil searching dengan lucene search pyserini.
    Yang di cari adalah ['Depressive', 'Disorder'] , dengan query ['Depressive', 'Disorder'] AND (treatment OR pharmacotherapy OR drug OR therapy)
    index dibangun dari subdataset 1.5juta artikel PubMed dalam 5 tahun terakhir.

    Tugas kamu adalah mengkurasikan hasil pencarian ini,
    apakah sesuai atau tidak untuk masing-masing hasil pencarian.
    Berikan jawaban dalam format:
    Document ID: <docid>
    Relevan: Ya/Tidak
    Alasan: <alasan singkat>

    hasil pencariannya adalah berikut ini:
    39742882 | 13.3568
    {
    "id" : "39742882",
    "contents" : "Virtual Reality-Based Cognitive Behavior Therapy for Major Depressive Disorder: An Alternative to Pharmacotherapy for Reducing Suicidality.. Cognitive behavioral therapy (CBT) has long been recognized as an effective treatment for depression and suicidality. Virtual reality (VR) technology is widely used for cognitive training for conditions such as anxiety disorder and post-traumatic stress disorder, but little research has considered VR-based CBT for depressive symptoms and suicidality. We tested the effectiveness and safety of a VR-based CBT program for depressive disorders. We recruited 57 participants from May 2022 through February 2023 using online advertisements. This multi-center, assessor-blinded, randomized, controlled exploratory trial used two groups: VR treatment group and treat as usual (TAU) group. VR treatment group received a VR mental health training/education program. TAU group received standard pharmacotherapy. Assessments were conducted at baseline, immediately after the 6-week treatment period, and 4 weeks after the end of the treatment period in each group. Depression scores decreased significantly over time in both VR treatment and TAU groups, with no differences between the two groups. The suicidality score decreased significantly only in VR group. No group differences were found in the remission or response rate for depression, perceived stress, or clinical severity. No adverse events or motion sickness occurred during the VR treatment program. VR CBT treatment for major depressive disorder has the potential to be equivalent to the gold-standard pharmacotherapy in reducing depressive symptoms, suicidality, and related clinical symptoms, with no difference in improvement found in this study. Thus, VR-based CBT might be an effective alternative to pharmacotherapy for depressive disorders.",
    "year" : 2025
    }
    39072563 | 13.0457
    {
    "id" : "39072563",
    "contents" : "[Pharmacogenomic and pharmacometabolomic biomarkers of the efficacy and safety of antidepressants: focus on selective serotonin reuptake inhibitors].. The efficacy and safety of psychopharmacotherapy with antidepressants is of great medical importance. The search for clinical and biological predictors for choosing the optimal psychopharmacotherapy with antidepressants is actively underway all over the world. Research is mainly devoted to searching for associations of polymorphic gene variants with the efficacy and safety of therapy. However, information about a patient's genetic polymorphism is often insufficient to predict the efficacy and safety of a drug. Modern research on the personalization of pharmacotherapy should include, in addition to genetic, phenotypic biomarkers. This is important because genotyping, for example, cannot accurately predict the actual metabolic activity of an isoenzyme. To personalize therapy, a combination of methods is required to obtain the most complete profile of the efficacy and safety of the drug. Successful treatment of depression remains a challenge, and inter-individual differences in response to antidepressants are common. About half of patients with depressive disorders do not respond to the first attempt at antidepressant therapy. Serious side-effects of antidepressant pharmacotherapy and discontinuation of treatment due to their intolerance are associated with ineffective therapy. This review presents the results of the latest studies of «omics» biomarkers of the efficacy and safety of antidepressants.",
    "year" : 2024
    }
    39664326 | 12.7971
    {
    "id" : "39664326",
    "contents" : "Enduring effects of psychotherapy, antidepressants and their combination for depression: a systematic review and meta-analysis.. Although depressive disorders are frequently associated with relapses, the sustained efficacy of therapies after their termination has been insufficiently investigated. The aim of this study was to evaluate the current evidence of enduring effects of psychotherapy, antidepressants and their combination after the end of treatment. PubMed and PsychINFO were systematically screened according to PRISMA guidelines (except for preregistration). Only randomized controlled trials (RCTs) between 1980 and 2022 comparing the efficacy of psychotherapy, antidepressants and their combination in adult depression at follow-up at least 12 months after termination of therapy, which could be acute phase, maintenance or relapse prevention therapy, were included. Risk of bias was assessed by using the Cochrane risk of bias tool. In total 19 RCTs with a total of 1154 participants were included. Psychotherapy was significantly superior to pharmacotherapy regarding relapse rates and Beck Depression Inventory scores at follow-up after acute treatment in two of nine RCTs. Combined treatment performed significantly better than pharmacotherapy, but not psychotherapy, regarding relapse and remission in five out of nine RCTs at least 12 months after treatment termination. Pairwise meta-analyses indicated a superiority of combined treatment compared to pharmacotherapy alone regarding relapse, recurrence, and rehospitalization rates (RR=0.60, 95%-CI: 0.37-0.97, p=.041) and for psychotherapy compared to pharmacotherapy alone regarding relapse and recurrence rates (RR=0.58, 95%-CI: 0.38-0.89, p=.023), however comparative treatment effects between psychotherapy and combined treatment were insignificant. Current findings suggest a superiority of psychotherapy and combined treatment over pharmacotherapy alone in major depressive disorder depression. Major limitations were a low number of studies reporting follow-up data after termination of study periods and a heterogeneity in definitions of treatment outcomes. Practice guidelines and participatory decision-making processes for the choice of treatment should consider the current knowledge on long-term effects of antidepressant therapy methods more than has been the case to date.",
    "year" : 2024
    }
    38687843 | 12.4425
    {
    "id" : "38687843",
    "contents" : "Efficacy and suitability of adding short-term psychodynamic psychotherapy (STPP) to pharmacotherapy in patients with depressive disorders: a systematic review.. Recent guidelines on depressive disorders suggest a combination of antidepressants and psychotherapy in case of moderate to severe symptomatology. While cognitive behavioral therapy and interpersonal therapy are the most investigated interventions, psychodynamic psychotherapies have been less explored. The aim of this paper is to systematically review literature data on the efficacy of shortterm psychodynamic psychotherapy (STPP) in combination with antidepressants in the treatment of depressive disorders, focusing both on short and on long-term results and on potential moderators that could influence its effectiveness. The systematic review was conducted using the PRISMA guidelines. Databases searched were PubMed, Ovid, Scopus, and Cochrane Library, from inception to August 2023. Adding STPP to medications in the first six months of treatment didn't influence remission rates, but improved acceptability, work adjustment, interpersonal relationships, social role functioning, hospitalization rates and cost-effectiveness. After 12 months, a significant difference in remission rates arised, favouring combined therapy. In a long-term perspective, adding STPP to pharmacotherapy reduced the recurrence rate by almost 50%. STPP has proven to be more effective in longer depressive episodes, in more severe depressions and in patients with a childhood abuse history. Instead, STPP had no impact on major depressive disorder with comorbid Obsessive-Compulsive Disorder (OCD). Combining STPP with antidepressants appeared to be helpful both in a short-term and in a long-term perspective. Still, there are few rigorous studies with large samples and further research is needed to identify which subgroups of patients may benefit more from STPP.",
    "year" : 2024
    }
    39039791 | 11.9620
    {
    "id" : "39039791",
    "contents" : "Profiling the combination of bupropion and dextromethorphan as a treatment option for major depressive disorder.. Major Depressive Disorder (MDD) is a common mental health disorder marked by sadness, hopelessness, and anhedonia. Various therapies exist, but their effectiveness is limited. Dextromethorphan hydrobromide combined with bupropion hydrochloride (Auvelity®) is a recently approved alternative for treating this condition in adults. This review summarizes the neurobiology of major depression and delves into the pharmacology, efficacy, safety, and tolerability of dextromethorphan plus bupropion in adult patients. It is based on observational studies, clinical trials, and other secondary studies obtained through systematic literature searches. The combination of bupropion and dextromethorphan as a new pharmacotherapy for mental health is an interesting addition to the treatment options that can be used for MDD. The combination can be used in a range of scenarios, including as a first line therapy, as a second option when a patient has failed to achieve remission with a serotonin targeting agent, and for treatment resistant depression. Further research for other indications, including addiction disorders, may provide exciting results. Although a new combination, clinicians will be very familiar with both agents, increasing their acceptability. This pharmacotherapy also may bring increased impetus for discovering other combinations that may have beneficial synergistic effects.",
    "year" : 2024
    }
    38776336 | 11.7564
    {
    "id" : "38776336",
    "contents" : "Dialectical Behavior Therapy as an intervention for Treatment Resistant Depression in adults: A protocol for systematic review and meta-analysis.. Major Depressive Disorder is a long-term, recurring, and very common illness that is associated with a significant decline in functional ability. The gold-standard method of treating depression is pharmacotherapy, which involves the use of antidepressant medications either alone or in various combinations. However, approximately 30% of Major Depressive Disorder patients suffer from Treatment Resistant Depression, a more severe condition that has a profound impact on patients' lives. Our study aims to conduct the first comprehensive review and meta-analysis to assess the effectiveness and safety of adding Dialectical Behavior Therapy to antidepressant medications compared to groups using pharmacotherapy alone as an intervention for adults with Treatment Resistant Depression. We will search for publications in the following databases: Cochrane Central Register of Controlled Trials, MEDLINE, Embase, Lilacs, Web of Science, and PsycINFO. We will manually review the reference lists of the included studies to identify potentially relevant studies. There will be no restrictions on the language or publication date. Quality assessment of the included studies will be performed independently according to the Cochrane Risk of Bias instrument. To assess the certainty of the findings' body of evidence, we will use the Grading of Recommendations Assessment, Development and Evaluation (GRADE) methodology. This study aims to determine the effectiveness and safety of Dialectical Behavior Therapy as an intervention for Treatment Resistant Depression in adults. Ethical approval was not required as individual patient data was not obtained. Our intention is to publish the systematic review in a medical journal that offers open access upon completion of the process. PROSPERO registration number CRD42023406301. Registered on March 24, 2023.",
    "year" : 2024
    }
    39067131 | 11.6978
    {
    "id" : "39067131",
    "contents" : "The effect of bright light therapy on major depressive disorder: A systematic review and meta-analysis of randomised controlled trials.. The increasing prevalence of major depressive disorder (MDD) has led to increased demand for psychotherapy and pharmacotherapy, yet concerns were raised regarding the cost and accessibility to these therapies. Bright light therapy (BLT) has shown promise in mitigating depressive symptoms of non-seasonal affective disorders. This meta-analysis gathered evidence from randomised controlled trials (RCTs) to assess the effectiveness of BLT on patients with non-seasonal MDD. Five databases were systematically searched. The primary outcome of the meta-analysis was the endpoint depression score from the BLT and control treatment groups, with the remission and response rates as the secondary outcomes. Results are presented in standardised mean difference (SMD) and log odd ratio. Subgroup analyses compared the effects of trial length and the length of daily exposure. Results on 15 RCTs between 1996 and 2024 with 883 patients showed positive effects of BLT on alleviating depressive symptoms (SMD = 0.48, 95 % CI [0.22, 0.74], p <.001). Trials that lasted two weeks or less or those with 60 minutes or more of daily exposure were associated with higher therapeutic effectiveness. BLT was also associated with a higher response rate at the end of the trial. This meta-analysis offers positive evidence that favours BLT in alleviating depressive symptoms in MDD, suggesting that it could be a convenient and easily accessible treatment modality to augment psychotherapy and pharmacotherapy.",
    "year" : 2024
    }
    38493750 | 11.6065
    {
    "id" : "38493750",
    "contents" : "The efficacy of electroconvulsive therapy in adolescent major depressive disorder with suicidal ideation: A propensity score-matched, retrospective cohort study.. More evidence is needed to validate the use of ECT in adolescent depression. This study aims to compare the effectiveness of electroconvulsive therapy (ECT) to conventional medication therapy for adolescents with major depression with suicidal ideation. In this retrospective cohort study, we reviewed inpatient records from the First Affiliated Hospital of Chongqing Medical University spanning December 2016 to June 2021. We focused on adolescents diagnosed with severe depression presenting with suicidal tendencies. To equalize baseline differences between patients, we used the one-to-one propensity score matching to match patients who received ECT treatment with those who did not. Multivariate regression analysis was utilized to adjust for potential confounders, and subgroup analyses and sensitivity analyses were conducted to verify the robustness of our findings. Of the 626 patients in this study, 474 underwent ECT treatment while 152 received medication treatment, all aged between 10 and 18 years. Once matched, each group contained 143 patients. The ECT group demonstrated a significantly higher response rate and greater reductions in both Hamilton Depression Rating Scale and Hamilton Anxiety Scale scores (all P < 0.001). Additionally, the ECT group was more effective in reducing suicidal ideation, with fewer individuals retaining such ideation at discharge. In the multivariable regression analysis, both ECT treatment and shorter disease duration were independently linked to enhanced antidepressant efficacy. Subgroup analyses and sensitivity analyses verified the robustness of the main study effect. For adolescents with major depressive disorder and suicidal ideation, combining ECT with pharmacotherapy is more effective than pharmacotherapy alone before medications reach full effect.",
    "year" : 2024
    }
    38875916 | 11.3230
    {
    "id" : "38875916",
    "contents" : "Use of service and treatment adequacy in medical students and residents suffering from depression in France: A nationwide study.. Depression was already a public health issue before the Covid-19 pandemic. Use of service and treatment adequacy in medical students was poorly known. A 2021 French national study found the prevalence of 12-month major depressive disorder (MDD) was 25 % in medical school students and residents (MSSR). The main objective of our study was to measure the prevalence of service use and adequate treatment (therapy and/or recommended pharmacotherapy) and their associated factors. A national online survey was conducted in 2021. The Composite International Diagnostic Interview Short-Form questionnaire was used to assess MDD; 12-months service use and pharmacotherapy were assessed. Univariate and multivariate logistic regressions were performed between students' demographic characteristics, use of services, and treatment adequacy. Among included MSSR who experienced MDD in the last 12 months, only 32 % received adequate treatment, including 20 % with recommended pharmacotherapy. Being more advanced in medical studies and being treated both by a general practitioner and a psychiatrist were associated with receiving recommended pharmacotherapy. To our knowledge, our study is the largest to assess use of service and treatment adequacy in MSSR. Given the low percentage of depressed students receiving recommended treatment, it seems important to develop new interventions to better detect and treat MDD in MSSR.",
    "year" : 2024
    }
    39758440 | 11.3105
    {
    "id" : "39758440",
    "contents" : "Effectiveness of individualized rTMS under sMRI guidance in reducing depressive symptoms and suicidal ideation in adolescents with depressive disorders: an open-label study.. Major Depressive Disorder (MDD) is occurring at a progressively younger age, and suicide is now the second leading cause of death among adolescents with MDD. Studies have shown that structural magnetic resonance imaging (sMRI) can improve the positioning accuracy and anti-depressant effects of repetitive transcranial magnetic stimulation (rTMS), thereby reducing suicidal ideation. To compare the efficacy of sMRI-guided rTMS combined with pharmacotherapy, surface 5-cm rTMS positioning combined with pharmacotherapy, and pharmacotherapy alone on reducing depressive symptoms and suicidal ideation (SI) in MDD adolescents. This was an open-label study of adjustable-dose pharmacotherapy combined with rTMS for the treatment of depressive symptoms and suicidal ideation in MDD adolescents. The three study groups were as follows: sMRI navigation for individualized rTMS coordinates targeting the dorsolateral prefrontal cortex (DLPFC) and in combination with pharmacotherapy for 10 rTMS sessions over two weeks; surface 5-cm positioning for DLPFC in combination with pharmacotherapy for 10 rTMS sessions over two weeks; pharmacotherapy. All patients received only one type of SSRIs anti-depressant. A total of 123 Chinese adolescents aged 13-18 with MDD were enrolled, and psychological parameters were evaluated in the first and second weeks of treatment. Following treatment, the clinical symptoms improved in all three groups. The sMRI navigation group exhibited significantly more improvement in depressive symptoms and suicidal ideation, without severe adverse reactions. Ten sessions of rTMS treatment are feasible and effective in improving depressive symptoms and reducing SI in MDD adolescents. The combination of sMRI navigation rTMS and pharmacotherapy was found to yield the best outcomes. https://www.medicalresearch.org.cn/index, identifier MR-33-24-030536.",
    "year" : 2024
    }

