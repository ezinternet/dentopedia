---
title: "Leveraging large language models for patient instructions in dentistry — A systematic review and meta-analysis"
authors: Rui Zhang, Yu Pan, Yushu Liu, Yinlong Deng, Edmond Ho Nang Pow
year: 2025
date: 2025-12-10
doi: 10.1111/jopr.70068
source: zhang-2025-llm-patient-instructions-dentistry-sr-ma.md
category: [digital-workflow]
confidence: sr+ma
pdf_path: /Users/oracleneo/llm-wiki/papers/zhang-2025-llm-patient-instructions-dentistry-sr-ma.pdf
pdf_filename: zhang-2025-llm-patient-instructions-dentistry-sr-ma.pdf
source_collection: external
tags: [LLM, ChatGPT, GPT-4, Bard, Bing, patient-instructions, patient-education, prosthodontics, accuracy, QUADAS-2, sr-ma]
---

## Three-line Summary
SR + MA (J Prosthodont 2025, PRISMA, 25 studies from Nov 2022–Jun 2024, 7 databases, modified QUADAS-2 quality) evaluating LLM accuracy and clinical acceptability for answering dental patient inquiries.

Pooled LLM accuracy was 81.87% (95% CI 77.24–86.51%) and clinically acceptable responses reached 69.9% (95% CI 57.3–82.6%); ChatGPT-3.5 significantly outperformed Bing but showed no significant difference versus GPT-4.0 or Bard — the 12% accuracy-to-acceptability gap highlights that accurate facts alone do not ensure clinically safe output.

LLMs are promising for simple patient FAQs but the ~18% error rate and 30% unacceptable-response rate require front-desk or clinician oversight, especially for medication interactions and postoperative complications where verbatim LLM output is not yet safe to distribute.

## 세줄요약
SR + MA(J Prosthodont 2025, PRISMA, 25편, 2022.11–2024.6, 7 DB, modified QUADAS-2): 치과 환자 문의에 대한 LLM 정확도와 임상적 수용 가능성을 정량 평가.

LLM 정확도 풀링 81.87%(95% CI 77.24–86.51%), 임상 수용 가능 응답 69.9%(95% CI 57.3–82.6%); ChatGPT-3.5 > Bing 유의, GPT-4.0·Bard와는 차이 없음 — 정확한 사실만으로는 임상적으로 안전한 출력이 보장되지 않음을 보여주는 12%포인트 차이.

단순 FAQ에는 유망하나 ~18% 오류율·30% 수용 불가 응답으로 직원·임상가 감독 필수, 특히 약물 상호작용·술후 합병증 같은 복잡 임상 상황에서 LLM 출력을 그대로 환자에게 전달하는 것은 부적절.

## Summary
PRISMA-compliant systematic review with meta-analysis (Journal of Prosthodontics, e-pub 10 Dec 2025) of LLMs answering dental patient inquiries. 25 studies (Nov 2022 – Jun 2024) across 7 databases; quality by modified QUADAS-2.

## Key Contributions
- **First quantitative pooled accuracy**: 81.87% for LLMs in dental patient communication
- **Acceptability distinct from accuracy**: 69.9% clinically acceptable — a meaningful gap
- **Version comparison**: ChatGPT-3.5 outperforms Bing significantly; NS vs ChatGPT-4.0/Bard

## Methodology
- PRISMA guidelines
- Databases (7): PubMed, Scopus, Cochrane, others
- Window: Nov 2022 – Jun 2024
- Quality assessment: modified QUADAS-2
- Subgroup and sensitivity analyses

## Results
| Metric | Value | 95% CI |
|---|---|---|
| Pooled accuracy (all LLMs) | 81.87% | 77.24–86.51% |
| Clinically acceptable responses | 69.9% | 57.3–82.6% |
| ChatGPT-3.5 vs Bing | Significantly higher | — |
| ChatGPT-3.5 vs GPT-4.0 / Bard | NS | — |

## Clinical Implications [확인 (pooled 수치), 임상 적용 가능성은 미검증]
- For basic patient FAQs (post-extraction care, recall scheduling, brushing instruction), LLM accuracy ~82% is reasonable but the 18% error rate is non-trivial — front-desk staff oversight needed
- The 30% clinical-acceptability gap suggests verbatim LLM output is not safe to hand to patients in current form
- Complex clinical scenarios (medication interactions, postoperative complications) still need clinician intervention — counterintuitive that GPT-4.0 isn't superior; likely reflects task-specific saturation
- Korean-language LLM performance not directly assessed — extrapolation to Korean clinical setting requires local validation

## Related Papers
- [[digital-workflow/iqbal-2025-chatgpt-healthcare-umbrella-review]] — broader healthcare umbrella review on ChatGPT
- [[digital-workflow/gao-2025-ai-dentistry-narrative-review]] — multi-specialty AI overview
- [[digital-workflow/aminoshariae-2024-ai-endodontic-education-scoping]] — adjacent: AI in endodontic education
- [[digital-workflow/lee-2025-ai-dentistry-emerging-applications-narrative]] — 3-pillar framework incl. patient care
