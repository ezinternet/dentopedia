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

## One-line Summary
SR+MA (J Prosthodont 2025, 25 studies): pooled LLM accuracy for dental patient questions 81.87% (95% CI 77.24–86.51%), clinically acceptable responses 69.9% (95% CI 57.3–82.6%); ChatGPT-3.5 significantly outperformed Bing, no significant difference vs GPT-4.0/Bard — promising for simple instructions, limited for complex clinical scenarios.

## 한줄요약
sr+ma (J Prosthodont 2025 Early View, 25편): 치과 환자 질문 응답에서 LLM 정확도 풀링 81.87% (95% CI 77.24–86.51%), 임상적 수용 가능 응답 69.9% (95% CI 57.3–82.6%); ChatGPT-3.5 > Bing 유의, GPT-4.0/Bard와는 차이 없음 — 단순 안내에는 유망, 복잡 임상에는 한계.

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

## Clinical Implications [근거강함 for pooled numbers; claude해석 for clinic applicability]
- For basic patient FAQs (post-extraction care, recall scheduling, brushing instruction), LLM accuracy ~82% is reasonable but the 18% error rate is non-trivial — front-desk staff oversight needed
- The 30% clinical-acceptability gap suggests verbatim LLM output is not safe to hand to patients in current form
- Complex clinical scenarios (medication interactions, postoperative complications) still need clinician intervention — counterintuitive that GPT-4.0 isn't superior; likely reflects task-specific saturation
- Korean-language LLM performance not directly assessed — extrapolation to Korean clinical setting requires local validation

## Related Papers
- [[digital-workflow/iqbal-2025-chatgpt-healthcare-umbrella-review]] — broader healthcare umbrella review on ChatGPT
- [[digital-workflow/gao-2025-ai-dentistry-narrative-review]] — multi-specialty AI overview
- [[digital-workflow/aminoshariae-2024-ai-endodontic-education-scoping]] — adjacent: AI in endodontic education
- [[digital-workflow/lee-2025-ai-dentistry-emerging-applications-narrative]] — 3-pillar framework incl. patient care
