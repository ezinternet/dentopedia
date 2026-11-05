---
title: "Binary Decision Trees for Preoperative Periapical Cyst Screening Using Cone-beam Computed Tomography"
authors: Pitcher B, Alaqla A, Noujeim M, Wealleans JA, Kotsakis G, Chrepa V
year: 2017
doi: 10.1016/j.joen.2016.10.046
journal: Journal of Endodontics 43(3):383-388
pmid: "28231977"
category: [endodontics/diagnosis]
source_collection: pubmed-abstract
full_text: false
---

abstract-only — full text not retrieved

## Why Ingested

CBCT에서 치근단 낭종 확률을 사전에 추정하는 임상 결정 트리를 제공하는 핵심 논문. Nair 2006의 "true cyst는 비외과적 치료에 반응하지 않는다"는 명제를 실제 술전 screening으로 연결한다 (→ [[endodontics/diagnosis/pitcher-2017-cbct-periapical-cyst-decision-tree]]). 병소 부피(volume >247 mm³) 단일 기준이 낭종 확률 80%를 예측한다는 수치 anchor를 제공한다.

## Three-line Summary

Diagnostic accuracy study (n=118, pre-apicoectomy CBCT scans, histopathology gold standard; J Endod 2017): a conditional-inference binary decision tree using CBCT volumetric analysis ± radiologic criteria achieved 78% accuracy for pre-operative cyst vs. granuloma screening.

Volume >247 mm³ → 80% cyst probability; volume <247 mm³ + root displacement present → 60% cyst probability; interobserver agreement was excellent for volume/density but poor-to-good for radiologic criteria.

Decision tree is a useful pre-operative screening aid but cannot replace histopathological diagnosis; volume and root displacement are the strongest CBCT predictors; confirmatory studies are needed.

## 세줄요약

진단 정확도 연구 (n=118, 치근단수술 전 CBCT, 조직병리 금본위; J Endod 2017): CBCT 체적 분석 ± 방사선 기준을 사용한 조건부 추론 이진 결정 트리가 78% 정확도로 술전 낭종 vs 육아종 선별을 달성.

병소 부피 >247 mm³ → 낭종 확률 80%; <247 mm³이면서 치근 변위(root displacement) 있음 → 낭종 확률 60%; 부피·밀도의 판독자 간 일치도는 우수, 방사선학적 기준은 불량~양호 수준.

결정 트리는 유용한 술전 선별 도구이나 조직병리를 대체할 수 없다; 부피와 치근 변위가 가장 강한 CBCT 예측인자; 확증 연구 필요.

## 1. Document Information

- **Title**: Binary Decision Trees for Preoperative Periapical Cyst Screening Using Cone-beam Computed Tomography
- **Authors**: Brandon Pitcher, Ali Alaqla, Marcel Noujeim, James A. Wealleans, Georgios Kotsakis, Vanessa Chrepa
- **Affiliation**: Department of Endodontics, University of Texas Health Science Center at San Antonio; Wilford Hall Dept of Endodontics, Joint Base San Antonio-Lackland
- **Journal**: Journal of Endodontics 2017;43(3):383–388
- **DOI**: 10.1016/j.joen.2016.10.046
- **PMID**: 28231977
- **Study design**: Diagnostic accuracy / cross-sectional retrospective

## 2. Key Contributions

- First binary decision tree classifier for pre-operative CBCT cyst screening with histopathological validation.
- Establishes a clinically actionable volume threshold: **>247 mm³ → 80% cyst probability**.
- Secondary branch: volume **<247 mm³ + root displacement** → 60% cyst probability.
- Overall decision tree accuracy: **78%**, with high specificity.
- Identifies **volume and root displacement** as the two strongest CBCT predictors; grey density added limited incremental value.
- Interobserver agreement: excellent for volume (quantitative) and density, poor-to-good for subjective radiologic criteria — highlights why objective volumetric measures outperform visual assessment.

## 3. Methodology

- **Sample**: 118 pre-surgical CBCT scans from patients who underwent apicoectomy with accompanying histopathological diagnosis (cyst or granuloma).
- **Gold standard**: histopathology of apicoectomy specimens — definitive cyst vs. granuloma classification.
- **Examiners**: 3 independent examiners; interobserver reliability assessed.
- **Measurements**: lesion volume (mm³), grey density, and designated radiologic criteria (root displacement, cortical expansion, etc.) using specialized volumetric software.
- **Analysis**: logistic regression → ROC curves → conditional inference binary decision tree (recursive partitioning algorithm).

## 4. Key Results

| Decision node | Finding | Cyst probability |
|---|---|---|
| Volume >247 mm³ | — | **80%** |
| Volume <247 mm³ + root displacement present | — | **60%** |
| Volume <247 mm³ + no root displacement | — | (lower; granuloma more likely) |

- Overall decision tree accuracy: **78%**
- Strongest predictors: **volume** and **root displacement**
- Interobserver agreement: excellent for volume/density; poor-to-good for radiologic criteria

## 5. Limitations

- Retrospective; all cases already indicated for apicoectomy — selection bias toward larger/symptomatic lesions.
- Sample limited to cyst vs. granuloma; does not address scar tissue, actinomycosis, or other Nair causes.
- 247 mm³ threshold requires external validation.
- Radiologic criteria had poor interobserver reliability — limits generalizability of the subjective branch.
- Not validated in non-surgical management settings.
