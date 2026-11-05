---
title: "Differentiation of periapical granuloma from radicular cyst using cone beam computed tomography images texture analysis"
authors: "De Rosa CS, Bergamini ML, Palmieri M, Sarmento DJS, de Carvalho MO, Ricardo ALF, Hasseus B, Jonasson P, Braz-Silva PH, Ferreira Costa AL"
year: 2020
doi: 10.1016/j.heliyon.2020.e05194
pmid: "33088959"
pmcid: "PMC7560585"
journal: "Heliyon 2020;6(10):e05194"
source_collection: pubmed-text
full_text: true
text_path: /Users/oracleneo/llm-wiki/papers/de-rosa-2020-cbct-texture-periapical-cyst-granuloma.txt
text_filename: de-rosa-2020-cbct-texture-periapical-cyst-granuloma.txt
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7560585/
category: endodontics/diagnosis
evidence_level: cross-sectional
tags: []
relations:
  - type: extends
    target: pitcher-2017-cbct-periapical-cyst-decision-tree
  - type: contradicts
    target: almadi-2020-cbct-grey-density-periapical-lesion
---

## Why Ingested

CBCT texture analysis (gray level co-occurrence matrix) approach to cyst/granuloma differentiation — provides a positive-result counterpoint to AlMadi 2020 (grey density AUC 0.44, fails) and a mechanistic complement to Pitcher 2017 (volume-based decision tree). Establishes that *what* you measure on CBCT matters: simple grey density fails, but spatial texture parameters succeed at AUC 81.2%. Core diagnostic question: can we non-invasively distinguish radicular cyst from granuloma to decide whether retreatment alone suffices?

→ [[endodontics/diagnosis/de-rosa-2020-cbct-texture-periapical-cyst-granuloma]]

## Three-line Summary

Cross-sectional study (University of São Paulo + Gothenburg, Heliyon 2020): 25 biopsy-confirmed periapical lesions (14 cysts, 11 granulomas) evaluated with CBCT texture analysis (Planmeca ProMax 3D, Haralick gray level co-occurrence matrix, MaZda software).

Five texture parameters (angular second moment, sum of squares, sum of average, contrast, correlation) significantly differentiated the two lesion types; best AUC 81.2% (angular second moment, sensitivity 100%, specificity 54.5%).

Mechanism: radicular cysts have more homogeneous CBCT texture (semi-solid necrotic content) versus granulomas (heterogeneous physiological cell content); texture analysis captures this internal structure difference invisible to visual inspection.

## 세줄요약

단면연구 (상파울루대 + 예테보리대, Heliyon 2020): 생검 확진 치근단 병소 25개(치근단낭종 14, 육아종 11)를 Planmeca ProMax 3D CBCT로 촬영 후 Haralick 회색조 공발생 행렬(GLCM) 기반 MaZda 소프트웨어로 질감 분석.

5개 질감 파라미터(각도 2차 모멘트, 제곱합, 평균합, 대비, 상관)가 두 병소를 유의하게 감별; 최고 AUC 81.2%(각도 2차 모멘트, 민감도 100%, 특이도 54.5%).

기전: 치근단낭종은 상피세포 액화 괴사물(반고체 균질)로 CBCT 질감이 균질하고, 육아종은 생리적 세포 내용물로 비균질 — 육안 판독에서 보이지 않는 내부 구조 차이를 질감 파라미터가 포착.

## Key Contributions

- First CBCT-based texture analysis study for periapical lesion differentiation (prior work used MRI)
- Established that **simple grey density (mean HU)** cannot differentiate (supports AlMadi 2020 negative finding), but **spatial texture parameters can**
- Five Haralick GLCM parameters predictive: angular second moment, sum of squares, sum of average, contrast, correlation
- Best discriminator: angular second moment >0.10 at S(1.0) → radicular cyst (AUC 81.2%, sensitivity 100%, specificity 54.5%)
- Tissue heterogeneity rationale: cyst = homogeneous (liquefied necrotic epithelial content); granuloma = heterogeneous (mixed inflammatory/physiological cells)

## Methodology

- Design: Cross-sectional, retrospective CBCT analysis with histopathological gold standard
- Setting: University of São Paulo School of Dentistry (Brazil) + University of Gothenburg (Sweden)
- n=25 periapical lesions from 19 patients (26 originally enrolled; 7 excluded for non-attendance, insufficient biopsy material, insufficient ROI area, or metallic artifacts)
- Lesion composition: 14 radicular cysts (56%), 11 periapical granulomas (44%)
- Lesion location: 4 anterior, 21 posterior teeth
- Patient demographics: 9F/10M, age 24–72 years (mean 46.7)
- CBCT device: Planmeca ProMax 3D (96 kVp, 12 mA, FOV 6 cm, voxel 200 μm, 12s acquisition)
- Image analysis: OnDemand 3D software (DICOM review)
- Texture software: MaZda v4.6 (after DICOM → BMP conversion)
- ROI: round, 44-pixel diameter, manually placed at lesion center on most representative sagittal slice
- Parameters: 11 Haralick GLCM texture features × 8 positions (d=1,2 × 4 directions: 0°/45°/90°/135°) = 88 variables
- Statistics: Spearman correlation, Mann-Whitney U, Benjamini-Hochberg FDR correction; ROC curve analysis; cluster analysis (dendrogram)

## Key Results

**Significant texture parameters** (Mann-Whitney, FDR-corrected):

| Parameter | Position | p-value | AUC | Cutoff | Sensitivity | Specificity |
|---|---|---|---|---|---|---|
| Angular second moment | S1.0 | 0.021 | 81.2% | >0.10 → cyst | 100% | 54.5% |
| Sum of squares | S1.0 | 0.019 | — | — | — | — |
| Sum of average | S1.0 | 0.019 | — | — | — | — |
| Contrast | Multiple positions | 0.019–0.038 | — | — | — | — |
| Correlation | Multiple positions | 0.019–0.037 | — | — | — | — |

**Cluster analysis (unsupervised):** Auto-classified into 2 groups (18 + 7 lesions); 6/25 (24%) misclassified vs histopathology.

**Mechanism of texture difference:**
- Radicular cysts: higher angular second moment → greater homogeneity → consistent with semi-solid necrotic material from liquefied epithelial cells
- Periapical granulomas: lower angular second moment → greater heterogeneity → consistent with physiological-like cell content (inflammatory infiltrate, fibroblasts, blood vessels)

## Limitations

- Small sample (n=25): insufficient power for multivariate modeling; AUC likely overoptimistic
- Single-slice 2D analysis: does not exploit CBCT's 3D information (volumetric texture may perform better)
- DICOM → BMP conversion loses resolution; reduces discriminatory potential
- Single-center; device-specific parameters (voxel size, FOV affect texture values)
- No external validation cohort
- Metallic restorations excluded: limits clinical applicability (most molar lesions have metal restorations)

## Related Papers

- [[pitcher-2017-cbct-periapical-cyst-decision-tree]] — volume >247 mm³ → 80% cyst probability; different CBCT feature (volume + root displacement vs texture)
- [[almadi-2020-cbct-grey-density-periapical-lesion]] — grey density AUC 0.44: cannot differentiate; confirms that mean HU alone fails while texture succeeds
- [[nair-2006-causes-persistent-apical-periodontitis-review]] — biological basis: true cyst (self-sustaining enclosed lumen) is the entity these imaging studies try to identify non-invasively
