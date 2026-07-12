---
title: "Harnessing AI in prosthodontics and implant dentistry: An umbrella review of systematic evidence"
authors: Alfaraj A, Limones Á, Ahmad S, Aljubairah F, Albalawi S, Albesher M, Alghamdei B, Lin WS
year: 2026
doi: 10.1111/jopr.70091
category: [artificial-intelligence]
pdf_path: /Users/oracleneo/llm-wiki/papers/alfaraj-2026-harnessing-ai-prosthodontics-implant-dentistry.pdf
pdf_filename: alfaraj-2026-harnessing-ai-prosthodontics-implant-dentistry.pdf
source_collection: external
---

## Why Ingested

기존 [[digital-workflow/revilla-leon-2021-artificial-intelligence-implant-dentistry-sr]] (17편 SR, implant type recognition/success prediction/design optimization)이 본 umbrella review에서 실제로 종합된 11편 SR 중 하나(review #4, "Revilla-León et al.")로 재등장한다. 본 논문은 그 SR을 포함한 11편의 AI SR을 AMSTAR-2로 메타-평가하여 근거 품질 지형을 그려주므로, 개별 SR 페이지의 수치를 상위 레벨에서 맥락화하는 데 사용한다. 또한 [[artificial-intelligence/garg-2026-artificial-intelligence-pediatric-dentistry-umbrella-review]]와 동일한 umbrella-review 방법론(AMSTAR-2 + CCA)을 성인 보철·임플란트 영역에 적용해, "영상 인식 과제는 고성능이나 SR 품질은 낮음/매우 낮음"이라는 패턴을 독립적으로 재확인한다.

## Three-line Summary

Umbrella review (PROSPERO CRD420251067048; 11 systematic reviews, 261 unique primary studies, PubMed/Scopus/Web of Science/Embase/Cochrane 2018–2025) synthesizing AI applications in prosthodontics and implant dentistry, appraised with AMSTAR-2 and overlap quantified via corrected covered area (CCA = 0.77% overall).

AI reached ~95.6% pooled accuracy for implant-type identification on radiographs and 96%/83% accuracy for mandibular/maxillary edentulous-site detection, but only 62.4%–80.5% accuracy for multivariable implant-prognosis prediction; caries/fracture detection in prosthodontics reached ~82%–89% accuracy and preparation-margin detection 90.6%–97.4%.

Only 4/11 reviews (36%) were AMSTAR-2 "high" quality (55% critically low, mainly for missing protocol registration and excluded-study lists), so image-recognition/segmentation tasks are the most clinically mature AI use case while multivariable outcome prediction and routine clinical adoption require further prospective validation.

## 세줄요약

엄브렐러 리뷰(PROSPERO CRD420251067048; 11편 체계적 문헌고찰(SR), 고유 1차 연구 261편, PubMed/Scopus/Web of Science/Embase/Cochrane 2018–2025)로 보철·임플란트 치의학에서의 인공지능(Artificial Intelligence, AI) 적용을 종합; AMSTAR-2 질 평가 + 중복보정면적(Corrected Covered Area, CCA) 0.77%(전체 수준).

방사선 사진 임플란트 종류 식별 풀링 정확도 ~95.6%, 하악/상악 무치악 부위 탐지 정확도 96%/83%이나, 다변량 임플란트 예후 예측은 정확도 62.4–80.5%에 그침; 보철학에서는 우식·파절 탐지 정확도 ~82–89%, 지대치 변연 탐지 90.6–97.4%.

11편 중 4편(36%)만 AMSTAR-2 "높음" 등급(55%는 critically low, 주로 사전등록 프로토콜·제외연구 목록 미비)이므로, 영상인식·분할 과제는 임상 성숙도가 가장 높은 반면 다변량 예후 예측·일상 진료 도입은 추가 전향적 검증이 필요함.

## 1. Document Information
- **Journal**: Journal of Prosthodontics 2026;35(2):127–142
- **DOI**: 10.1111/jopr.70091
- **Institution**: Department of Prosthodontics, King Faisal University College of Dentistry, Al Ahsa, Saudi Arabia; Department of Prosthodontics, Indiana University School of Dentistry, Indianapolis, USA (corresponding author Wei-Shao Lin)
- **Registration**: PROSPERO CRD420251067048; reported per PRIOR 2022 guideline

## 2. Key Contributions
- First umbrella review to jointly synthesize AI evidence across both general prosthodontics (tooth-supported prostheses) and implant dentistry, integrating 11 systematic reviews (261 unique primary studies, 281 citations, overall CCA = 0.77%).
- Introduces a 3-level "clinical readiness" scale (high/moderate/emerging) per AI task, combining best-reported performance metric with qualitative evidence-maturity judgment (Table 4).
- Quantifies AMSTAR-2 methodological quality across the 11 included SRs: 36% high, 9% low, 55% critically low — with 100% failing to report primary-study funding sources and 91% failing to list excluded studies.

## 3. Methodology and Architecture
- **Design**: Umbrella review (overview of systematic reviews), PRIOR 2022-guided, PROSPERO-registered.
- **Databases**: PubMed (MEDLINE), Scopus, Web of Science, Embase, Cochrane Library; search run April 2025, systematic reviews published 2018–2025, English only.
- **n**: 207 records → 186 after dedup → 21 full-text assessed → 11 systematic reviews included (193 studies in main analyses; 281 primary-study citations; 261 unique primary studies).
- **Quality tool**: AMSTAR-2 (two independent raters + third-reviewer arbitration).
- **Overlap**: Corrected covered area (CCA) — overall (0.77%) and task-level (reported per Table 4; N/A when only one contributing review or non-matching task categorization; tooth-shade selection task-level CCA = 1.00).
- **Synthesis**: Descriptive/narrative (statistical pooling across reviews judged inappropriate given heterogeneity); findings organized by review (Table 3) and by clinical task (Table 4).

## 4. Key Results and Benchmarks

**General prosthodontics**
- Caries/fracture detection accuracy ~82%–89%.
- Preparation-margin (finish-line) detection accuracy 90.6%–97.4%.
- AI tooth-shade matching outperformed visual shade selection in one included primary study.
- Automated CAD restoration design (14 studies) and RPD framework design/education tools (17 studies) reviewed descriptively (Revilla-León et al.).

**Implant dentistry**
- Implant-type identification on radiographs: pooled accuracy 92.56% (Alqutaibi et al.) to 95.6% (Dashti et al.), sensitivity/specificity ~95%/98%; top models (ResNet-152, Neuro-T v2.0.1) up to 99.08%/100% sensitivity; Ibraheem et al. range 67%–98.5%; Bonfanti-Gris et al. range 67%–99%.
- Edentulous-area detection: 96% accuracy mandible, 83% maxilla (Alqutaibi et al.).
- Anatomic segmentation (mandibular canal, maxillary sinus) via 3D U-Net: ~77% accuracy to ~99% precision; bone-crest segmentation up to 116× faster than manual.
- Implant failure/peri-implantitis prediction from radiographs: accuracy up to 99.8% (sensitivity 67%–95%, specificity 78%–100%); patient/biomechanical-data models only 62.4%–80.5% accuracy.
- Peri-implant radiolucency detection: ≥78.6% accuracy (Bonfanti-Gris et al.).
- AI + finite element analysis implant-design optimization: bone–implant interface stress reduced up to 36.6% (Revilla-León et al.).

**Quality (AMSTAR-2, n = 11 SRs)**: 36% high, 9% low, 55% critically low. 100% did not report included-study funding (Item 10); 91% lacked an excluded-studies list (Item 7); 36% did not report duplicate study selection (Item 5); only 36% had a pre-registered protocol (Item 2).

## 5. Limitations and Future Work
- No cross-review meta-analysis was performed (descriptive/narrative synthesis only) due to heterogeneity in AI tasks, models, and outcome metrics.
- Underlying primary studies were predominantly retrospective, single-center, and/or used idealized datasets — limiting real-world generalizability of the high accuracy figures.
- Prognostic-model outcome definitions varied widely (implant survival vs. marginal bone loss thresholds), complicating comparison.
- Majority of contributing SRs were AMSTAR-2 low/critically-low quality, chiefly from missing protocol pre-registration and incomplete bias assessment — the authors explicitly caution against treating current performance metrics as validated standard of care.
- Authors call for standardized outcome metrics (e.g., F1-score, AUC), shared benchmark datasets, and prospective/multi-center validation before routine clinical adoption.

## 6. Related Work
- revilla-leon-2021 (17 studies, implant type recognition/success prediction/design optimization) — one of the 11 primary systematic reviews synthesized here (review #4, Table 2).
- garg-2026 (pediatric dentistry AI umbrella review, AMSTAR-2 + CCA) — same umbrella-review methodology applied to a different population; independently reaches the same "image tasks mature, SR quality low" conclusion.

## 7. Glossary
- **AMSTAR-2**: A Measurement Tool to Assess Systematic Reviews, version 2 — critical-appraisal instrument for SR methodological quality (high/moderate/low/critically low).
- **CCA (corrected covered area)**: quantifies the degree of primary-study overlap across systematic reviews contributing to an umbrella review.
- **PRIOR**: Preferred Reporting Items for Overviews of Reviews (2022 guideline) for umbrella-review reporting.
- **CNN**: Convolutional neural network — deep-learning architecture dominant for image-based (radiographic) recognition/segmentation tasks in this review.
- **Clinical readiness scale**: this paper's 3-level (high/moderate/emerging) ordinal judgment combining best-reported AI performance metric with evidence-base maturity.
