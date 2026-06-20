---
title: "Unveiling Drug-Drug Interactions in Dental Patients: A Retrospective Real-World Study"
authors: Daiana Colibăsanu, Sebastian Mihai Ardelean, Florina-Diana Goldiș, Maria-Medana Drăgoi, Sabina-Oana Vasii, Tamara Maksimović, Șerban Colibăsanu, Codruța Șoica, Lucreția Udrescu
year: 2025
date: 2025-06-09
doi: 10.3390/dj13060255
source: colibasanu-2025-drug-drug-interactions-dental-patients-retrospective.md
category: [drug/systemic-disease]
confidence: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/colibasanu-2025-drug-drug-interactions-dental-patients-retrospective.pdf
pdf_filename: colibasanu-2025-drug-drug-interactions-dental-patients-retrospective.pdf
source_collection: external
tags: [drug-drug-interaction, polypharmacy, real-world-data, dentistry, cardiovascular, epinephrine, beta-blockers, drugbank, romania, retrospective]
---

## One-line Summary
Retrospective real-world single-center study (Romania Timișoara private dental clinic, n=105, Nov–Dec 2024): DrugBank Drug Interaction Checker evaluated 1,332 drug pairs — 542 DDIs (major 2.3%, moderate 25.0%, minor 13.4%, none 59.3%); major DDIs concentrated in the 31–60-year age group (61.3%) and cardiovascular disease patients (epinephrine + β-blocker as representative example).

## 한줄요약
후향 단일기관 실세계 연구(루마니아 Timișoara 사설 치과, n=105, 2024.11–12): DrugBank Drug Interaction Checker로 1,332 약물쌍 평가 — 542개 DDI(Drug-Drug Interaction), 주요 2.3%·중등도 25.0%·경미 13.4%·없음 59.3%; 주요 DDI는 31–60세 그룹(61.3%)과 심혈관 질환자(epinephrine + β-blocker 대표적)에 집중.

## Summary
Colibăsanu 등(2025, Victor Babeș 대학)은 루마니아 Timișoara 사설 치과의 연속 105명 환자 의무기록을 DrugBank Drug Interaction Checker(open-source, API-accessible, versioned)로 분석했다. 1,332 약물쌍 중 542개 DDI 발견: 주요(major) 2.3% / 중등도 25.0% / 경미 13.4% / 없음 59.3%. 환자의 45.7%가 기저질환을 보유했고 심혈관 질환이 19.0%로 최다. 주요 DDI는 31–60세 그룹(61.3%)과 ≥61세(38.7%)에 집중되었고 0–30세는 0건. 핵심 임상 예시는 epinephrine(국소마취 vasoconstrictor) + β-blocker로 인한 역설적 고혈압 위험. 31–60세에서 주요 DDI가 더 많은 이유는 [claude해석] 약물 recall과 정확한 보고 능력이 더 높기 때문일 가능성이 크다(저자도 elderly 그룹의 under-reporting을 caveat으로 언급).

## Key Contributions
- 루마니아 치과 실세계 DDI 정량의 첫 보고 — 약물쌍 단위 542/1,332 = 40.7% 어떤 형태의 DDI.
- DrugBank Interaction Checker라는 재현 가능한 computational workflow 시연.
- 연령·심혈관 질환별 stratification으로 위험 subgroup 식별.
- Epinephrine + β-blocker 같은 구체적 high-risk pair 명시 — chairside 위험 mitigation에 즉시 적용 가능.

## Methodology
- 후향적 단일기관, 사설 치과 105명 연속 환자 (2024.11–12).
- 변수: 인구통계, 기저질환, 치과 진단·처치, 처방약(치과 + 만성 질환).
- DDI 평가: DrugBank Drug Interaction Checker → major/moderate/minor/none 분류.
- 통계: Chi-square (major DDI × 연령군 0–30/31–60/≥61); Kruskal-Wallis (총 DDI × 연령); Mann-Whitney U (총 DDI × CVD 유무); α=0.05.
- Post-hoc power analysis; a priori sample size 계산 없음 (exploratory).

## Results
- 기저질환 보유 45.7%; CVD 19.0% (최다).
- 치과 진단: 근첨 병변 47.6%, 발치 53.3%.
- DDI 분포: 주요 2.3% / 중등도 25.0% / 경미 13.4% / 없음 59.3%.
- 주요 DDI 연령: 31–60세 61.3%; ≥61세 38.7%; 0–30세 0%.
- 대표 high-risk pair: epinephrine + β-blocker — paradoxical hypertensive crisis.
- ≥61세 underreporting 가능성 자체 caveat.

## Related Papers
- [[drug/thornhill-2019-adverse-reactions-oral-antibiotics-dentists]] — NHS England 항생제 ADR 백만 처방당 율.
- [[drug/pyo-2026-drug-interactions-prescription-safety-elderly]] — 고령 환자 DDI 40.7% prevalence 인용 (본 논문 결과와 일치하는 anchor).
- [[drug/bazsefidpay-2023-antibiotic-restrictive-use-adherence-recommendation]] — 항생제 제한 처방 adherence.
