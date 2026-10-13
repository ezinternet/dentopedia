---
title: "Use of Artificial Intelligence in Diagnosing Vertical Root Fractures—A Systematic Review"
authors: Alshahrani Abdulmajeed Saeed, Alelyani Ahmed Ali, Jabali Ahmad, Al Malwi Ahmed Abdullah, Alroomy Riyadh, Shaiban Amal S., Almnea Raid Abdullah, Mehta Vini, Al Moaleem Mohammed M., Duong Tim, Leung Yiu Yan
year: 2026
doi: 10.3390/diagnostics16030406
category: artificial-intelligence
source_collection: pubmed-text
full_text: true
pmid: "41681724"
pmcid: "PMC12896978"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12896978/
text_path: /Users/oracleneo/llm-wiki/papers/alshahrani-2026-use-of-artificial-intelligence-in.txt
text_filename: alshahrani-2026-use-of-artificial-intelligence-in.txt
---

## Why Ingested

수직치근파절 (Vertical Root Fracture, VRF)의 AI 영상 진단을 파노라마 1차연구 한 편([[artificial-intelligence/mun-2024-deep-learning-cracked-tooth-extraction-panoramic]])으로만 보유하고 있었는데, 이 SR은 그 연구를 포함해 치근단·파노라마·CBCT 3개 영상양식에 걸친 AI 성능과 GRADE 확실성을 한 번에 비교한다. 인간 판독 쪽 CBCT의 한계를 서술한 [[cracked-tooth/patel-2022-present-status-future-directions-vertical]]와 짝을 이루는 AI 측 근거다.

## Three-line Summary

Systematic review (PRISMA 2020, PROSPERO CRD420251134312; QUADAS-2 + GRADE; 10 studies, 2013–2025; narrative synthesis because heterogeneity precluded meta-analysis) of AI-based vertical root fracture (VRF) detection on periapical, panoramic and CBCT images.

CBCT-based AI had the highest accuracy (91.4–97.8%) and specificity (90.7–100%) with moderate GRADE certainty; periapical models reached up to 95.7% accuracy but only in ex vivo settings (low certainty); panoramic models were weakest (e.g., recall 0.75 with 20 false positives; specificity 60.8%) with low certainty.

Most evidence is ex vivo or single-centre with small datasets and no external validation; AI is a promising adjunct, CBCT remains the confirmatory modality, and none of the included studies assessed clinical workflow impact.

## 세줄요약

수직치근파절 (Vertical Root Fracture, VRF)의 AI 진단을 치근단·파노라마·CBCT 영상에서 평가한 체계적 문헌고찰 10편 (PRISMA 2020, QUADAS-2, GRADE; 이질성이 커서 메타분석 불가, 서술적 종합).

CBCT 기반 AI가 정확도 91.4–97.8%, 특이도 90.7–100%로 최고 (GRADE 중간 확실성); 치근단 모델은 발치 후 (ex vivo) 조건에서 정확도 최대 95.7%, 파노라마 모델은 재현율 0.75·위양성 20건 등으로 가장 낮음 (둘 다 낮은 확실성).

근거 대부분이 발치 후·단일기관·소규모 데이터이고 외부 검증이 없어, AI는 보조 도구 수준이며 확진은 여전히 CBCT; 임상 워크플로 영향을 평가한 연구는 0편.

## 1. Document Information
- **Journal**: Diagnostics (Basel) 2026;16(3):406 (published 2026-01-27)
- **DOI**: 10.3390/diagnostics16030406
- **Institution**: Najran University, Jazan University, King Khalid University, Qassim University (Saudi Arabia); Dr. D. Y. Patil Vidyapeeth (India); additional authors (Duong, Leung) not affiliated in the PubMed record

## 2. Key Contributions
- First SR dedicated to AI detection of VRF across all three common radiographic modalities (periapical, panoramic, CBCT).
- Modality ranking: CBCT > periapical > panoramic, with a GRADE rating per modality (moderate / low / low).
- Separates ex vivo (optimistic) from in vivo (realistic) performance and flags overfitting risk from small datasets.
- Identifies the evidence gap: no study of clinical workflow integration, usability or decision-support outcomes.

## 3. Methodology and Architecture
- **Design**: Systematic review, PRISMA 2020; protocol registered PROSPERO CRD420251134312; QUADAS-2 risk of bias; GRADE for certainty; Nested Knowledge platform for screening/extraction (two independent reviewers, third for disagreements).
- **Databases**: PubMed, Embase, Web of Science, Scopus (Methods); the Abstract instead lists PubMed, Scopus, Web of Science and the Cochrane Library, and says "up to January 2025" whereas Methods say published through July 2025.
- **n**: 404 records → 146 duplicates removed → 258 screened → 245 excluded (191 irrelevant, 51 reviews, 3 editorials) → 13 full texts → 3 excluded → 10 included. Included datasets 120–418 images/teeth (e.g., 200 extracted premolars; 552 manually cropped CBCT ROIs).
- **Outcomes**: accuracy, sensitivity, specificity, precision/recall, F1, AUC; observer agreement (kappa, ICC); comparison with human observers.
- **Reference standards**: stereomicroscope/micro-CT for ex vivo studies; consensus diagnosis for retrospective/in vivo series.
- No meta-analysis (heterogeneous AI model types CNN/PNN/DNN, modalities, preprocessing, metrics).

## 4. Key Results and Benchmarks

Risk of bias: Fukuda 2020 and Chang 2024 high risk overall; Kositbowornchai 2013 and Kapralos 2020 low risk.

| Study | Modality / setting | AI model | Key result |
|---|---|---|---|
| Fukuda 2020 | Panoramic, 300 images, clinical | CNN (DetectNet) | recall 0.75, precision 0.93, F-measure 0.83; VRF detection rate 20%, 20 false positives |
| Hu 2022 | CBCT | Pretrained CNNs | manual ROI: accuracy 97.8% (AUC 0.99; sens 97.0%, spec 98.5%); automatic ROI: 91.4% (AUC 0.96) |
| Abdelazim 2024 | Periapical, ex vivo | Ensemble of 5 pretrained CNNs | DenseNet121/169: sens 89.4%/87.2%, spec 93.6%, AUC 0.98 |
| Ozsari 2025 | Periapical, clinical | DenseNet–Inception fusion + enhancement | accuracy/precision/recall/F1/AUC all ~0.80; kappa 0.60 |
| Yang 2023 | CBCT slices, in vivo (14 patients) | Fine-tuned ResNet-50 | sens 94.5%, spec 73.2%, AUC 0.929; higher sensitivity than two oral radiologists, lower specificity |
| Mun 2024 | Panoramic | ResNet-50 (best of 3) | sens 90.43%, spec 60.77%, accuracy 75.84%, AUC 0.825 |
| Kositbowornchai 2013 | Periapical, ex vivo | PNN | sens 97.2–98.0%, spec 60.0–90.5%, accuracy 88.3–95.7% |
| Johari 2017 | Periapical vs CBCT, ex vivo | PNN vs MLP | periapical: sens 97.78%, accuracy 70.0%; CBCT: accuracy 96.6%, spec 100% |
| Chang 2024 | Clinical/procedural variables (not images), retrospective | DNN vs SVM | accuracy 80.7%, recall 93.7%, F1 86.7% (DNN > SVM) |
| Kapralos 2020 | Periapical, root-filled teeth | Digital subtraction radiography vs conventional | AUC 0.73 for DSR (higher than conventional) |

GRADE certainty: CBCT-based AI moderate; periapical low; panoramic low. Downgrades for risk of bias (ex vivo, retrospective), inconsistency, indirectness.

## 5. Limitations and Future Work
- Heterogeneous designs, datasets, image parameters and metric reporting; no pooling possible.
- Many ex vivo/single-centre studies; few with external or prospective validation; small datasets raise overfitting risk (e.g., 14 patients in Yang 2023).
- Reference standards differ (micro-CT vs consensus vs surgical verification).
- Included set is not purely AI image interpretation: Chang 2024 used non-imaging variables and Kapralos 2020 compared digital subtraction radiography.
- Future work: multicentre prospective validation, standardised protocols, explainable AI (class activation maps), hybrid image + clinical-data models, cost-effectiveness analysis.

## 6. Related Work
- Mun 2024 (included as study 24): panoramic CNN, sens 90–94%, spec 53–61%.
- Patel 2022: human CBCT cannot reliably show the fracture line itself, only the bone-loss pattern.
- Eraslan 2026: language-model benchmarking in cracked tooth syndrome (text scenarios, not imaging).
- Albano 2024, Demir 2024: other QUADAS-2 AI imaging SRs with the same "promising but heterogeneous, no pooling" pattern.

## 7. Glossary
- **VRF (Vertical Root Fracture)**: longitudinal fracture extending from the root canal to the external root surface.
- **QUADAS-2**: risk-of-bias/applicability tool for diagnostic accuracy studies.
- **GRADE**: framework rating certainty of evidence (high/moderate/low/very low).
- **PNN (Probabilistic Neural Network)**: older neural-network classifier used in two ex vivo studies.
- **ROI (Region of Interest)**: cropped image region fed to the model; manual cropping outperformed automatic selection in Hu 2022.
- **Ex vivo**: extracted teeth imaged outside the patient; typically overestimates real-world performance.
