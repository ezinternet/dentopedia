---
title: "Comparison and ranking of interventions for temporomandibular disorders-myofascial pain syndrome: a Bayesian network meta-analysis based on randomized controlled trials"
authors: "Feihong Ma, Binkui Jia, Zhi Liu, Xuedong Pei, Xuehai Liu, Hongfan Li, Zhijing Song"
year: 2026
doi: "10.1186/s12903-026-08373-9"
category: [tmj]
source_collection: pubmed-text
full_text: true
pmid: "42010612"
pmcid: "PMC13270680"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13270680/
text_path: /Users/oracleneo/llm-wiki/papers/ma-2026-comparison-ranking-interventions-tmd.txt
text_filename: ma-2026-comparison-ranking-interventions-tmd.txt
---

## Why Ingested

TMD 처방(pharmacotherapy/injection) 관련 아시아 저널(아시아 저자·기관, PMC 풀텍스트) 논문 인제스트 요청에 따라 검색. 기존 [[tmj/haggman-henrikson-2017-pharmacological-orofacial-pain-sr-ma]]는 TMD 전반의 약물치료(NSAID·근이완제·클로나제팜 등 경구약)를 NMA로 다루지만, 국소 주사·물리치료 계열(리도카인 주사·PRP·보툴리눔독소·허혈성압박·레이저)의 상대적 순위는 다루지 않았다. 본 논문(Ma 2026, 간쑤중의약대학/Gansu University of Chinese Medicine, 중국)은 TMD-근막통증증후군(MPS)에 특화해 14개 RCT(674명)를 베이지안 NMA로 통합, 처방·주사성 중재의 SUCRA 순위를 제공해 [[tmj/haggman-henrikson-2017-pharmacological-orofacial-pain-sr-ma]]의 경구약물 근거를 주사·국소처치 영역으로 확장하고, [[tmj/menendez-torre-2023-dry-needling-vs-manual-therapy-tmd-nma]]의 dry needling/manual therapy NMA와도 비교축을 형성한다.

## Three-line Summary


Bayesian random-effects network meta-analysis of 14 RCTs (n=674 adults with TMD-myofascial pain syndrome), authored by a Chinese (Gansu University of Chinese Medicine) team;

lidocaine injection and ischemic compression ranked highest for short-term pain relief (SUCRA 91.7% and 88.7%) versus basic treatment, followed by platelet-rich plasma and laser therapy, but certainty of evidence for all top-ranked comparisons was low to very low (CINeMA), driven by sparse single-trial nodes, high risk of bias in 9/14 trials, and mostly indirect evidence for the top two interventions.

(incomplete)

## 세줄요약


베이지안 랜덤효과 네트워크 메타분석(14 RCT, TMD 근막통증증후군 성인 674명), 중국 간쑤중의약대학 저자팀;

리도카인 주사·허혈성압박이 기본치료 대비 단기 통증완화 SUCRA 순위 1·2위(91.7%·88.7%)였고 혈소판풍부혈장(PRP)·레이저가 뒤를 이었으나, 두 상위 중재는 간접비교 위주에 RCT 14편 중 9편이 고위험 편향으로 근거 확실성이 낮음~매우낮음(CINeMA)이다.

(incomplete)

## 1. Document Information

- Journal: BMC Oral Health, 26(1), epub 2026-04-20
- DOI: 10.1186/s12903-026-08373-9 · PMID: 42010612 · PMCID: PMC13270680
- Affiliation: Department of Rehabilitation Orthopedics I, Affiliated Hospital of Gansu University of Chinese Medicine; Clinical College of Traditional Chinese Medicine, Gansu University of Chinese Medicine, Lanzhou, Gansu Province, China (all 7 authors)
- Registration: PROSPERO CRD420251070432; reported per PRISMA-NMA
- Funding/COI: not stated in retrieved text

## 2. Key Contributions

- First NMA (per the authors) to comprehensively integrate pharmacological/injection interventions (lidocaine injection, platelet-rich plasma, botulinum toxin injection) alongside physical/appliance therapies (laser, TENS, manual therapy, oral appliance, bite plate, acupuncture, biofeedback, ischemic compression) for TMD-myofascial pain syndrome specifically (a DC/TMD-defined subtype), rather than TMD broadly.
- Applies CINeMA certainty grading on top of RoB 2 and SUCRA ranking — explicitly downgrades the top-ranked interventions (lidocaine injection, ischemic compression) to "very low" certainty because they lack any direct head-to-head trial versus the reference (basic treatment) node.
- Provides a transparent node-merging/BT-composition methodology (BT = pooled sham/placebo + minimal conservative pharmacotherapy such as NSAIDs/muscle relaxants), making explicit that "muscle relaxant pharmacotherapy" (MP) as a distinct node showed no significant advantage over BT.
- Flags network sparsity explicitly: 5 of 14 intervention nodes (lidocaine injection, ischemic compression, TENS, oral-appliance+lidocaine, botulinum toxin injection) are each supported by only one trial, which the authors say precluded their planned sensitivity analyses (network would disconnect).

## 3. Methodology and Architecture

- Design: Bayesian random-effects network meta-analysis of RCTs (confidence tier `sr+ma`), PRISMA-NMA reported, PROSPERO-registered.
- Search: PubMed, Embase, Cochrane Library, Web of Science, inception–June 2025; English full-text RCTs only; no grey literature; supplementary trial-registry search found no additional eligible records.
- Population: adults ≥18y with a clinical diagnosis of TMD-MPS (mostly DC/TMD-diagnosed; some studies used investigator-defined or Simons' trigger-point criteria).
- Interventions/nodes (14 categories): basic treatment (BT, reference — pooled sham/placebo + minimal conservative pharmacotherapy [NSAIDs/muscle relaxants]), laser treatment (LT), bite plate (BP), oral appliance (OA), lidocaine injection (LI), acupuncture (AC), transcutaneous electrical stimulation (TES), biofeedback (BI), manual therapy (MT), muscle-relaxant pharmacotherapy (MP, as a standalone node distinct from BT's pooled conservative-pharmacotherapy component), ischemic compression (IC), botulinum toxin injection (BTI), platelet-rich plasma (PRP), oral appliance + lidocaine injection (OA+LI).
- Outcome: primary = short-term (0–4 week) change in pain intensity (VAS/NRS), standardized as SMD with 95% credible intervals (CrI).
- Statistics: gemtc + rjags in R 4.4.0; 4 Markov chains × 50,000 iterations (10,000 burn-in); non-informative priors; convergence via trace plots + Gelman-Rubin PSRF; node-splitting for local inconsistency; SUCRA for probabilistic ranking.
- Risk of bias: Cochrane RoB 2 (5 domains) on parallel RCTs.
- Certainty of evidence: CINeMA framework (within-study bias, reporting bias, indirectness, imprecision, heterogeneity, incoherence) — high/moderate/low/very low.
- Planned sensitivity analyses (exclude high-RoB studies; alternate BT composition) were **not performed** due to network sparsity (would disconnect the network / destabilize the model).

## 4. Key Results and Benchmarks

- 14 RCTs, n=674 (from 9,378 records screened; >70% female across studies); trials from Iran, Turkey, Italy, Brazil, Sweden, Spain, Poland, Lithuania (2010–2024).
- RoB 2: 9/14 (64.3%) high risk of bias, 5/14 (35.7%) some concerns, 0 low risk — driven mainly by blinding difficulty (Domain 2) and subjective pain-outcome measurement (Domain 4).
- NMA vs. BT (SMD, 95% CrI): lidocaine injection −2.37 (−3.67 to −0.90); ischemic compression −2.21 (−3.63 to −0.75); PRP −1.45 (−2.21 to −0.56); laser therapy −0.91 (−1.58 to −0.13) — all statistically significant. All other nodes (BP, OA, OA+LI, acupuncture, TES, manual therapy, muscle-relaxant pharmacotherapy, botulinum toxin injection, biofeedback) had CrIs crossing null.
- SUCRA ranking: lidocaine injection 91.7% > ischemic compression 88.7% > PRP 68.6% > TES 67.5% > OA+lidocaine 66.6% > botulinum toxin injection 66.5% ... BT 10.7%, biofeedback 11.2% (lowest).
- Certainty (CINeMA): laser therapy and PRP — Low (each backed by only 1 small RCT, n=41 and n=58 respectively); lidocaine injection, ischemic compression, TES, OA+lidocaine, botulinum toxin injection — Very low (no direct trial vs. BT, and/or CrI crosses null, and/or high RoB).
- No significant inconsistency detected on node-splitting (e.g., laser vs. BT p=0.808); PSRF convergence mostly <1.20 (acceptable).

## 5. Limitations and Future Work

- Small number of trials/participants overall; nearly all follow-up windows limited to 0–4 weeks, so conclusions apply to short-term analgesia only, not durability or safety.
- 5 of 14 nodes supported by a single RCT each — the two top-ranked interventions (lidocaine injection, ischemic compression) had **no direct comparison with BT at all**, so their apparent superiority rests entirely on indirect evidence chains; authors explicitly warn against using SUCRA rank directly for clinical prioritization.
- BT (reference) composition varied across trials (sham/placebo procedures vs. minimal conservative pharmacotherapy), introducing potential clinical heterogeneity that could not be resolved because planned BT-composition sensitivity analysis was blocked by network sparsity.
- Blinding was difficult to implement for injection/manual interventions, and pain outcomes were subjective — both inflate risk of bias.
- English-only, no grey literature; population skewed >70% female; key covariates (disease duration, psychosocial factors) underreported — limits generalizability.
- Authors call for head-to-head RCTs (lidocaine injection vs. ischemic compression; laser vs. PRP; both vs. standardized BT) with unified parameters, longer follow-up, and core outcome sets.

## 6. Related Work

- Positioned as filling a gap left by prior NMAs that "often cover only some interventions" for TMD-MPS — the paper explicitly aims for broader intervention coverage (14 nodes) than earlier network meta-analyses in this space.
- Cites general TMD stepped-care guideline logic (conservative-first, escalate based on individual response) consistent with the wiki's [[overviews/tmd-management-evidence-ladder]] axis 2–3 framework.
- Complementary to [[tmj/haggman-henrikson-2017-pharmacological-orofacial-pain-sr-ma]] (oral pharmacotherapy NMA for TMD/BMS broadly) — this paper's "muscle relaxant pharmacotherapy" and BT's "minimal conservative pharmacotherapy" nodes are the oral-drug side, while lidocaine injection/PRP/botulinum toxin injection are the injectable side.
- Relevant to [[tmj/zhu-2020-btx-painful-tmd-sr-ma]] and [[tmj/saini-2024-botulinum-toxin-tmd-sr-ma]] (botulinum toxin for TMD) — this NMA finds BTI's CrI crosses null vs. BT (very low certainty), a more cautious read than some standalone BTX SR+MAs.

## 7. Glossary

- **TMD-MPS**: Temporomandibular disorder–myofascial pain syndrome, a DC/TMD-defined masticatory-muscle-pain subtype involving trigger points/referred pain.
- **NMA / SUCRA**: Network meta-analysis; Surface Under the Cumulative Ranking curve — a probabilistic ranking metric, not a direct measure of superiority.
- **CINeMA**: Confidence In Network Meta-Analysis framework for grading certainty of NMA estimates (analogous to GRADE for pairwise meta-analysis).
- **BT (basic treatment)**: This paper's pooled reference node combining sham/placebo procedures and minimal conservative pharmacotherapy (NSAIDs/muscle relaxants).
- **LI / IC / PRP / BTI / TES**: Lidocaine injection; ischemic compression; platelet-rich plasma; botulinum toxin injection; transcutaneous electrical stimulation.
