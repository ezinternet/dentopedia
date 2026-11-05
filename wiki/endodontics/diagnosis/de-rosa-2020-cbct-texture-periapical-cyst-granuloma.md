---
title: "Differentiation of periapical granuloma from radicular cyst using cone beam computed tomography images texture analysis"
authors: "De Rosa CS, Bergamini ML, Palmieri M, Sarmento DJS, de Carvalho MO, Ricardo ALF, Hasseus B, Jonasson P, Braz-Silva PH, Ferreira Costa AL"
year: 2020
date: 2020-10-09
doi: 10.1016/j.heliyon.2020.e05194
pmid: "33088959"
pmcid: "PMC7560585"
source: de-rosa-2020-cbct-texture-periapical-cyst-granuloma.md
category: endodontics/diagnosis
evidence_level: cross-sectional
source_collection: pubmed-text
full_text: true
text_path: /Users/oracleneo/llm-wiki/papers/de-rosa-2020-cbct-texture-periapical-cyst-granuloma.txt
text_filename: de-rosa-2020-cbct-texture-periapical-cyst-granuloma.txt
tags: []
relations:
  - type: extends
    target: pitcher-2017-cbct-periapical-cyst-decision-tree
  - type: contradicts
    target: almadi-2020-cbct-grey-density-periapical-lesion
superseded_by: null
---

## Three-line Summary

Cross-sectional study (University of São Paulo + Gothenburg, Heliyon 2020): 25 biopsy-confirmed periapical lesions (14 radicular cysts, 11 granulomas) evaluated with CBCT gray level co-occurrence matrix (GLCM) texture analysis using Planmeca ProMax 3D (voxel 200 μm, FOV 6 cm) and MaZda software.

Five Haralick texture parameters significantly differentiated lesion types; best discriminator: angular second moment >0.10 → radicular cyst (AUC 81.2%, sensitivity 100%, specificity 54.5%).

Mechanism: radicular cysts produce more homogeneous CBCT texture due to semi-solid necrotic content (liquefied epithelial cells), while granulomas appear heterogeneous; texture analysis captures this internal structure difference invisible to routine visual CBCT inspection.

## 세줄요약

단면연구 (상파울루대 + 예테보리대, Heliyon 2020): 생검 확진 치근단 병소 25개(치근단낭종 14, 육아종 11), Planmeca ProMax 3D CBCT (복셀 200μm, FOV 6cm), MaZda 소프트웨어로 Haralick 회색조 공발생 행렬(GLCM) 질감 분석.

5개 파라미터(각도 2차 모멘트·제곱합·평균합·대비·상관) 유의 감별; 최고 AUC 81.2%(각도 2차 모멘트 >0.10 → 낭종, 민감도 100%, 특이도 54.5%).

치근단낭종은 상피세포 액화 괴사로 균질 질감(높은 각도 2차 모멘트), 육아종은 생리적 세포 혼합으로 비균질 질감 — 육안 판독으로 불가한 내부 구조 차이를 CBCT 질감 파라미터가 포착.

## Summary

### Background

Non-invasive differentiation of radicular cysts from periapical granulomas remains a central challenge in endodontic diagnosis. The clinical stakes are high: granulomas tend to heal with non-surgical root canal treatment (NSRCT), whereas true (enclosed-lumen) cysts are unlikely to resolve without surgery (Nair 2006). Conventional 2D radiographs cannot distinguish the two; CBCT has moderately better accuracy depending on lesion size but routine visual interpretation remains unreliable.

**Texture analysis** (mathematical extraction of spatial grey-level variation from digital images) is a computer-aided approach that can reveal structure invisible to the human eye. This study is the first to apply it to CBCT images of periapical lesions, extending prior MRI-based work.

### Study Design

- Cross-sectional, retrospective with histopathological gold standard
- Setting: University of São Paulo School of Dentistry (Brazil) + University of Gothenburg (Sweden)
- n=25 periapical lesions from 19 patients; gold standard: H&E histopathology after extraction
- Lesion types: 14 radicular cysts (56%), 11 periapical granulomas (44%)
- Exclusions: epithelized granulomas, metallic artifact cases, insufficient biopsy material

### CBCT Protocol

| Parameter | Value |
|---|---|
| Device | Planmeca ProMax 3D |
| kVp / mA | 96 / 12 |
| FOV | 6 cm |
| Voxel size | 200 μm |
| Acquisition time | 12 s |
| Window settings | WW 1650, WL 875 |
| Analysis software | OnDemand 3D (DICOM review) |

### Texture Analysis Method

1. Most representative sagittal slice selected (largest lesion dimension)
2. DICOM → BMP conversion (resolution loss acknowledged)
3. Circular ROI (44-pixel diameter) manually placed at lesion center in MaZda software
4. 11 Haralick GLCM parameters computed at 2 pixel distances × 4 directions = 88 variables
5. Statistical selection: Spearman correlation → Benjamini-Hochberg FDR correction → ROC analysis

**11 Haralick parameters evaluated:** contrast, inverse difference moment, angular second moment (ASM), correlation, sum of squares, entropy, sum of average, sum of variance, sum of entropy, difference of variance, difference of entropy

### Results

**Five significant discriminating parameters:**

| Parameter | Key position | p-value | Best AUC | Cutoff | Sens | Spec |
|---|---|---|---|---|---|---|
| **Angular second moment (ASM)** | S1.0 | 0.021 | **81.2%** | >0.10 → cyst | 100% | 54.5% |
| Sum of squares | S1.0 | 0.019 | — | — | — | — |
| Sum of average | S1.0 | 0.019 | — | — | — | — |
| Contrast | Multiple | 0.019–0.038 | — | — | — | — |
| Correlation | Multiple | 0.019–0.037 | — | — | — | — |

**Cluster analysis (unsupervised):** Auto-classification into 2 groups: 18 cysts + 7 granulomas. Misclassification rate: 6/25 (24%) vs histopathology.

**Mechanistic interpretation:**
- **Radicular cysts** → higher ASM → **more homogeneous** texture → consistent with semi-solid necrotic content (liquefied epithelial cells fill the cyst lumen)
- **Periapical granulomas** → lower ASM → **more heterogeneous** texture → consistent with mixed physiological cell content (inflammatory infiltrate, fibroblasts, vasculature)

### Limitations

- **Small n** (25 lesions): AUC estimates unreliable; underpowered for multivariate modeling
- **2D single-slice** analysis: CBCT's 3D advantage not exploited; volumetric texture could improve performance
- **DICOM → BMP resolution loss**: reduces texture discrimination potential
- **Device-specific**: voxel size and FOV affect absolute texture values; parameters non-transferable across machines without recalibration
- **No external validation**: results require confirmation in an independent cohort
- **Metal exclusion**: limits applicability to most posterior molar cases

### Clinical Takeaway

Texture analysis shows promise as an **adjunctive** non-invasive tool, but is not yet ready for clinical use:
1. High sensitivity (100%) means few cysts missed — useful as a screening tool
2. Low specificity (54.5%) means many granulomas also flagged as cysts — overdiagnoses surgical need
3. Requires specialized software and expertise (MaZda + trained evaluator)
4. Not validated beyond n=25

**Practical position in the diagnostic hierarchy:** histopathology remains gold standard; texture analysis is an exploratory adjunct that may eventually reduce unnecessary surgery — but only after validation with larger, volumetric, multi-device studies.

## Key Contributions

- First CBCT texture analysis study for periapical lesion differentiation (prior work: MRI only)
- Demonstrated that **spatial texture parameters** (ASM, sum of squares, contrast, correlation) differentiate cysts from granulomas, while **simple grey density** (mean HU) cannot (cf. AlMadi 2020: AUC 0.44)
- Identified the biological mechanism underlying texture difference: homogeneity of cyst content vs. heterogeneity of granuloma tissue
- AUC 81.2% with 100% sensitivity for cyst detection — promising upper bound for the approach pending validation

## Related Papers

- [[pitcher-2017-cbct-periapical-cyst-decision-tree]] — complementary CBCT approach: volume >247 mm³ → 80% cyst probability; different feature (3D volume + root displacement vs. 2D texture)
- [[almadi-2020-cbct-grey-density-periapical-lesion]] — contradicts: mean grey density (simple HU) AUC 0.44, cannot differentiate; confirms that texture > density as a CBCT discriminator
- [[nair-2006-causes-persistent-apical-periodontitis-review]] — biological foundation: true apical cyst (self-sustaining enclosed lumen) is the target entity; distinguishing from pocket cyst requires histology
