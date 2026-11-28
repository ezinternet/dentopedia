---
title: "Prediction of lifespan and assessing risk factors of large-sample implant prostheses: a multicenter study"
authors: Kim JH, Yoon JH, Jeon HI, Kim DW, Park YB, Oh N
year: 2024
doi: 10.4047/jap.2024.16.3.151
category: [implants/survival]
source_collection: pubmed-text
full_text: true
pmid: "38957292"
pmcid: "PMC11215039"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11215039/
text_path: /Users/oracleneo/llm-wiki/papers/kim-2024-prediction-of-lifespan-and-assessing.txt
text_filename: kim-2024-prediction-of-lifespan-and-assessing.txt
---

## Why Ingested

한국 16개 기관 다기관 연구로, 임플란트 자체가 아니라 임플란트 보철물 (implant prosthesis)의 수명을 환자 면담·임상·방사선 평가로 추정한 드문 한국 자료다 (중앙 생존 16년). 보철물 생존은 임플란트 생존과 다른 지표이므로 한국 대학병원 임플란트 생존 코호트와 구분해 읽기 위해 인제스트했다. → [[implants/survival/song-2024-long-term-clinical-radiographic-outcomes]]

## Three-line Summary

Cross-sectional multicenter survey of 16 Korean institutions (May 2017 - April 2018) using the Korean Academy of Prosthodontics (KAP) criteria: 841 implant prostheses in 485 patients, with failure defined as KAP grade C or D; the unit is the prosthesis, not the implant.

Median prosthesis survival was 16 years; in the multivariate Cox model, treatment by a non-licensed practitioner (HR 5.5, 95% CI 1.216-24.630, only 6 of 841 cases), an implant prosthesis as the antagonist (HR 1.9, 95% CI 1.152-3.334) and plaque index 3 (HR 2.5, 95% CI 1.207-5.249) were significant.

Early versus late failure timing was not reported; the lifespan model (principal component analysis, biological age score) underestimated actual lifespan, with non-failed prostheses potentially lasting about 1.34 years longer than estimated, and patient nationality is not stated in the text (Korean only by setting).

## 세줄요약

한국 16개 기관에서 2017년 5월-2018년 4월 대한치과보철학회 (Korean Academy of Prosthodontics, KAP) 기준으로 평가한 다기관 횡단 설문 연구: 환자 485명, 임플란트 보철물 841개이며 KAP C·D 등급을 실패로 정의했다; 분석 단위는 임플란트가 아니라 보철물이다.

보철물 중앙 생존기간은 16년이었고, 다변량 콕스 모형에서 무면허 시술 (위험비 5.5, 95% CI 1.216-24.630, 841건 중 6건뿐), 대합치가 임플란트 보철물인 경우 (위험비 1.9, 95% CI 1.152-3.334), 플라그 지수 3 (위험비 2.5, 95% CI 1.207-5.249)가 유의했다.

조기 대 후기 실패 시점은 보고되지 않았고, 주성분 분석 기반 수명 모형 (biological age score)은 실제 수명을 과소추정했으며 실패하지 않은 보철물은 추정보다 약 1.34년 더 사용될 수 있다고 했다; 환자 국적은 본문에 명시되지 않고 한국 기관이라는 설정으로만 추정된다.

## 1. Document Information

- **Title**: Prediction of lifespan and assessing risk factors of large-sample implant prostheses: a multicenter study (PubMed title)
- **Authors**: Kim JH, Yoon JH, Jeon HI, Kim DW, Park YB, Oh N
- **Journal**: The Journal of Advanced Prosthodontics 2024;16(3):151-162 (PubMed metadata; published 2024-06-25)
- **Setting**: 16 institutions in Korea (affiliations per PubMed: Yonsei University College of Dentistry, NHIS Ilsan Hospital, Inha University, Gyeongsang National University statistics department); IRB approval Inha University Hospital (INHAUH 2017-01-012-001), written informed consent obtained. The other 13 institutions are not named in the text.
- **Nationality/ethnicity**: not stated in the text; Korean population is implied only by the Korean institutions.
- **DOI**: 10.4047/jap.2024.16.3.151
- **PMID**: 38957292 / **PMCID**: PMC11215039
- **Retrieval**: PubMed Central full text

## 2. Key Contributions

- Evaluates implant PROSTHESES (single crown, fixed full denture, fixed partial denture, removable implant overdenture), not implants; prosthesis survival is not implant survival.
- Standardized KAP criteria with an online multi-institution form to pool records across sites.
- Median prosthesis survival 16 years; risk factors: clinic type (non-licensed practitioner), antagonist type (implant prosthesis), plaque index 3.
- Nomogram for individual survival probability and a PCA-based biological age score (BAS) for lifespan estimation.

## 3. Methodology and Architecture

- **Design**: Cross-sectional survey with retrospective duration (usage time) and Cox/Kaplan-Meier survival analysis; patients who visited 16 institutions from May 1, 2017 to April 30, 2018.
- **Sampling**: Prostheses related to the chief complaint were excluded to reduce selection bias; prostheses whose fabrication year and month the patient could not recall were excluded. Fabrication date came from patient statement.
- **Examiners**: prosthodontists trained in workshops at the start and at each institution; patient interview plus clinical and radiological assessment.
- **Variables**: age, gender, prosthesis type, clinic type (dental hospital, local clinic, non-licensed practitioner NL, unknown), usage duration, national health insurance coverage, antagonist type, plaque index, ratio of prosthesis units to implant body.
- **Outcome**: KAP grades A (no defect), B (functions, minor adjustment) = success; C (defects preventing long-term use, temporary use only), D (harmful to tissue, immediate removal needed) = failure. Failure is a prosthesis-level grading at the examination, not implant loss.
- **Statistics**: multivariate Cox model, Kaplan-Meier, nomogram (points from HR), principal component analysis and BAS for lifespan estimation instead of multiple linear regression; R 3.4; p<.05.

## 4. Key Results and Benchmarks

| Item | Result |
|---|---|
| Sample | 841 prostheses, 485 patients |
| Median survival | 16 years (text says "with a 95% confidence interval"; no interval values given) |
| NL vs reference (clinic type) | HR 5.5 (1.216-24.630), p=.03; only 6 of 841 cases |
| Implant prosthesis antagonist vs FDP with natural teeth | HR 1.9 (1.152-3.334), p=.01 |
| Plaque index 3 | HR 2.5 (1.207-5.249), p=.01 |
| Median survival by clinic | Hos not evaluable; LC 16 y; NL 7 y; unknown 15 y |
| Median survival by antagonist | FDP 16 y; RDP 17 y; implant prosthesis 12 y |
| Median survival by plaque index | 0: 15 y; 1: 18 y; 2 and 3: 13 y |
| Nomogram points for yes/NL/3/implant | insurance coverage 100, NL 83, plaque 3 = 53, implant antagonist = 36 |
| Non-failed prostheses | potential use extended about 1.34 years beyond estimated lifespan |

- Nomogram variable order: insurance coverage, clinic type, plaque index, antagonist type, unit-to-implant ratio, age, gender. Insurance coverage was not among the multivariate significant factors reported.
- Early versus late failure: not reported. Timing is given only as survival time in years; the unit of analysis is prosthesis, with patient counts as 485.

## 5. Limitations and Future Work

- Prosthesis-level outcome (KAP C/D), not implant survival or removal; results cannot be compared with implant cumulative survival rates.
- Fabrication date from patient recall; failure onset unknown (a failure may precede the examination); success prostheses measured to the examination date, so lifespan is underestimated (authors).
- NL group only 6 of 841 cases, wide CI (1.216-24.630); authors urge cautious interpretation.
- Authors state the sample is too small to call big data; cross-sectional sampling of attending patients, chief-complaint prostheses excluded.
- Text inconsistencies: the median is described as "with a 95% confidence interval" but no interval is given; 841 prostheses versus 485 patients (clustering of multiple prostheses per patient is not explained); reference categories for clinic type are not stated explicitly.

## 6. Related Work

- [[implants/survival/song-2024-long-term-clinical-radiographic-outcomes]] — Korean single-center implant-level long-term outcomes.
- [[overviews/korean-university-hospital-implant-survival-cohorts-overview]] — Korean implant survival cohorts (implant-level).
- [[overviews/early-implant-failure-risk-prevention-overview]] — early failure context.

## 7. Glossary

- **KAP criteria (Korean Academy of Prosthodontics criteria, 대한치과보철학회 평가 기준)**: grade A-D prosthesis rating; C and D = failure.
- **Nomogram (노모그램)**: points-based chart converting Cox model factors into survival probability.
- **PCA (Principal Component Analysis, 주성분 분석)** and **BAS (Biological Age Score)**: method used to estimate prosthesis lifespan.
- **NL (non-licensed practitioner, 무면허 시술자)**: treatment by someone without a dental license.
