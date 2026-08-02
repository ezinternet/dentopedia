---
title: "Comparative performance of AI chatbots in dental implantology: insights and limitations"
authors: "Sultan Merve Uçar, Selin Gaş, Rafat Sasany"
year: 2026
doi: "10.1186/s12903-025-07426-9"
category: [digital-workflow]
pdf_path: /Users/oracleneo/llm-wiki/papers/ucar-2026-llm-performance-zygomatic-implantology.pdf
pdf_filename: ucar-2026-llm-performance-zygomatic-implantology.pdf
source_collection: external
---

## Why Ingested
AI 도구의 임상 의사결정 지원 가능성 평가 근거로 활용. [[digital-workflow/abbott-2024-ai-platforms-dental-caries-detection]] 등 치과 AI 연구 맥락에서 LLM 성능 한계의 실증 데이터가 필요.

## Three-line Summary
Prospective comparative evaluation (BMC Oral Health 2026; 38 standardized zygomatic implantology questions developed by 4 OMS expert surgeons; 5 calibrated independent raters; ICC 0.86–0.91 inter-rater reliability) assessing ChatGPT-4o, Claude 3.5, and Gemini 1.5 Pro using DISCERN, GQS, and a 5-point Accuracy Rubric.

No clinically meaningful performance difference among the three models (maximum score gap ≤0.5 points on 5-point scales); Gemini 1.5 Pro scored marginally higher; all models produced readable, clinically relevant content but showed persistent variability in depth and specificity of clinical guidance.

No current LLM is ready for unsupervised specialist clinical decision support; continuous expert validation, version transparency, and domain-specific benchmarking are prerequisites for integration into dental education or clinical practice.

## 세줄요약
줄1: 전향적 비교 평가 (BMC Oral Health 2026); 구강악안면외과 전문의 4인이 개발한 치근성 임플란트(Zygomatic Implant) 전문 38개 표준 질문으로 5인 평가단이 DISCERN·GQS·정확도 루브릭으로 ChatGPT-4o·Claude 3.5·Gemini 1.5 Pro 평가; 급내상관계수(Intraclass Correlation Coefficient, ICC) 0.86–0.91(우수).
줄2: 모델 간 임상적으로 유의미한 성능 차이 없음(최대 ≤0.5점/5점 척도); Gemini 1.5 Pro가 미미하게 높은 점수; 전 모델에서 임상 심층도·특이성 가변성 지속.
줄3: 현재 어떤 대형언어모델(Large Language Model, LLM)도 치과 임플란트 전문 임상 의사결정의 무감독 활용 불가; 교육·임상 통합 전 전문가 지속 검증·버전 투명성·영역별 벤치마킹 필수.

## One-line Summary
Prospective evaluation (n=38 questions, 5 raters) comparing ChatGPT-4o, Claude 3.5, and Gemini 1.5 Pro on zygomatic implantology Q&A found no clinically meaningful performance differences (≤0.5 points on 5-point scales), with Gemini scoring marginally higher.

## 한줄요약
치과의사 4인이 개발한 38개 표준 질문으로 평가한 결과, ChatGPT-4o·Claude 3.5·Gemini 1.5 Pro의 치근성 임플란트(Zygomatic Implant) 관련 응답 성능 차이는 임상적으로 유의미하지 않았다(최대 0.5점 차, 5점 척도).

## 1. Document Information
- Journal: BMC Oral Health, 2026;26:147
- Published: 2026 (submitted 2025)
- Funding: Not specified (open access CC BY-NC-ND 4.0)
- Conflicts: None declared
- Institution: Gelişim Üniversitesi & Biruni University, Istanbul, Turkey

## 2. Key Contributions
- First study evaluating LLM performance specifically on zygomatic implantology using expert-generated, standardized questions
- Employed three validated metrics (DISCERN, GQS, 5-point Accuracy Rubric) with high inter-rater reliability (ICC 0.86–0.91)
- Demonstrated that absolute performance differences between leading LLMs are clinically negligible (≤0.5 points)
- Identified consistent variability in clinical specificity and depth across all models
- Provided framework for evaluating AI tools in specialist dental domains

## 3. Methodology and Architecture
- Study design: Prospective comparative evaluation
- Question development: 38 standardized questions by 4 OMS surgeons expert in zygomatic implantology
- Models evaluated: ChatGPT-4o, Claude 3.5, Gemini 1.5 Pro
- Raters: 5 calibrated clinical raters, independent assessment
- Metrics: DISCERN (health information quality), GQS (general quality score), 5-point Accuracy Rubric
- Statistics: Kruskal-Wallis with Bonferroni post hoc; Spearman correlation; ICC(2,1) for inter-rater reliability

## 4. Key Results and Benchmarks
- Inter-rater reliability: ICC(2,1) = 0.86–0.91 (p < 0.001) — excellent
- Gemini 1.5 Pro: marginally highest mean scores for quality and accuracy
- Claude 3.5 and ChatGPT-4o: comparable performance
- Maximum score difference between models: ≤0.5 points on 5-point scales
- All models produced readable, clinically relevant content
- Persistent variability in depth and specificity of clinical guidance across all models

## 5. Limitations and Future Work
- Questions focused on zygomatic implantology only — generalizability to other dental domains unconfirmed
- Raters were Turkish clinicians; cultural/language effects on response evaluation not controlled
- Model versions are a moving target — results may not apply to updated versions
- No evaluation of hallucination rate or citation accuracy
- Expert consensus questions may not reflect real-world clinical ambiguity

## 6. Related Work
- 2023 ITI Consensus Workshop on zygomatic implants (foundational framework)
- Abbott 2024 (AI in caries detection)
- General literature on AI in dental education and clinical decision support

## 7. Glossary
- **DISCERN**: Validated instrument for assessing quality of health information for consumers
- **GQS** (General Quality Score): Rater-assigned holistic quality metric
- **ICC(2,1)**: Intraclass correlation coefficient, two-way mixed model, single measures — inter-rater reliability
- **Zygomatic implant**: Long implant anchored in zygomatic bone, bypassing maxillary sinus; used in severely atrophic maxilla
