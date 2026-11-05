---
title: "Binary Decision Trees for Preoperative Periapical Cyst Screening Using Cone-beam Computed Tomography"
authors: "Pitcher B, Alaqla A, Noujeim M, Wealleans JA, Kotsakis G, Chrepa V"
year: 2017
date: 2017-03-01
doi: 10.1016/j.joen.2016.10.046
source: pitcher-2017-cbct-periapical-cyst-decision-tree.md
category: endodontics/diagnosis
evidence_level: cross-sectional
source_collection: pubmed-abstract
full_text: false
pmid: "28231977"
tags: [cbct, periapical-cyst, granuloma, decision-tree, volumetry, diagnostic-accuracy]
relations:
  - type: extends
    target: nair-2006-causes-persistent-apical-periodontitis-review
---

## Three-line Summary

Diagnostic accuracy study (n=118, pre-apicoectomy CBCT, histopathology gold standard; J Endod 2017): a CBCT-based conditional inference binary decision tree achieved 78% accuracy for pre-operative cyst vs. granuloma screening in periapical lesions.

Volume >247 mm³ predicts cyst with 80% probability; volume <247 mm³ with root displacement predicts cyst with 60% probability; interobserver agreement was excellent for volumetric/density measures but poor-to-good for subjective radiologic criteria.

Decision tree is a useful pre-operative screening aid — not a histopathology substitute — with lesion volume and root displacement as the strongest CBCT predictors; the 247 mm³ threshold requires external validation.

## 세줄요약

진단 정확도 연구 (n=118, 치근단수술 전 CBCT, 조직병리 금본위; J Endod 2017): CBCT 기반 이진 결정 트리가 78% 정확도로 술전 낭종 vs 육아종 선별을 달성.

병소 부피(Volume) >247 mm³ → 낭종 확률 80%; <247 mm³이면서 치근 변위(Root Displacement) 있음 → 60%; 부피·밀도의 판독자 간 일치도는 우수, 방사선학적 기준은 불량~양호.

임상 결정 트리는 술전 선별 보조 도구이지 조직병리 대체재가 아니며, 부피와 치근 변위가 가장 강한 예측인자; 247 mm³ 기준치의 외부 검증 연구 필요.

## Summary

Accurate pre-operative differentiation of periapical cysts from granulomas is clinically meaningful because true cysts (Nair cause #5) are unlikely to heal after non-surgical retreatment, while granulomas typically resolve. This study addressed that need by building and validating a CBCT-based binary decision tree using histopathological diagnosis as the gold standard.

**Study design**: 118 cases with pre-surgical CBCT and post-apicoectomy histopathology (definitive cyst vs. granuloma). Three examiners independently measured lesion volume, grey density, and designated radiologic criteria using volumetric software.

**Decision tree output:**

| Branch | Criterion | Cyst probability |
|---|---|---|
| Node 1 | Volume (Lesion Volume, LV) **>247 mm³** | **80%** |
| Node 2a | LV **<247 mm³** + root displacement **present** | 60% |
| Node 2b | LV **<247 mm³** + root displacement **absent** | (lower — granuloma favored) |

Overall accuracy: **78%**, with high specificity. Volume and root displacement were the two strongest predictors across all logistic regression models.

**Interobserver agreement**: Excellent for quantitative measures (volume, density); poor-to-good for subjective radiologic criteria — reinforcing that volumetric measurement is more reliable than visual interpretation for cyst screening.

## Key Contributions

- Provides the first decision-tree framework for CBCT-based pre-operative cyst probability estimation validated against histopathology.
- **247 mm³ volume threshold** as a practical single-criterion node: >247 mm³ → 80% probability of cyst.
- Demonstrates that **grey density alone** cannot reliably distinguish cysts from granulomas — consistent with AlMadi 2020 showing AUC 0.44 for grey density.
- Highlights **root displacement** as the most informative radiologic criterion when volume alone is insufficient.
- Explicitly frames the tool as pre-operative screening, not a histopathology substitute — aligning with Nair 2006's conclusion that true cysts require serial histology for definitive diagnosis.

## Methodology

- Retrospective cross-sectional design; 118 consecutive pre-apicoectomy cases.
- Gold standard: histopathology (H&E) by experienced oral pathologist — definitive cyst (epithelium-lined cavity) vs. granuloma.
- CBCT volumetric analysis with specialized segmentation software; 3 independent examiners.
- Statistical analysis: logistic regression → ROC curves → conditional inference tree (recursive partitioning, R package `party`).
- Interobserver reliability: ICC for quantitative measures; kappa for categorical criteria.

## Limitations

- All cases were already indicated for apicoectomy — over-represents larger/symptomatic lesions; may not generalize to smaller incidental lesions.
- Binary outcome (cyst vs. granuloma) excludes scar tissue, actinomycosis, cholesterol crystals, foreign-body reaction (Nair causes 2–6).
- 247 mm³ threshold is single-institution, single-dataset; external validation studies are absent at the time of publication.
- Subjective radiologic criteria showed poor interobserver reliability — limits the usefulness of the secondary (non-volume) branch.
- Pre-surgical setting only; not applicable to routine surveillance of non-surgical cases.

## Related Papers

- [[nair-2006-causes-persistent-apical-periodontitis-review]] — extends: Nair establishes why true cysts don't heal; Pitcher provides the CBCT screening tool to estimate pre-op cyst probability before deciding on surgical vs. retreatment path.
- [[almadi-2020-cbct-grey-density-periapical-lesion]] — corroborates: grey density alone (AUC 0.44) cannot distinguish cystic from solid lesions — volume, not density, is the informative CBCT parameter.
- [[de-rosa-2020-cbct-texture-periapical-cyst-granuloma]] — extends: texture analysis (angular second moment AUC 81%) provides complementary characterization beyond simple volume measurement.
