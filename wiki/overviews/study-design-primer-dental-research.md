---
title: "Study Design Primer for Dental Research Readers"
authors: synthesis (llm-wiki)
year: 2026
date: 2026-10-17
doi: null
source: synthesis
category: overviews
evidence_level: synthesis
tags: [evidence-appraisal, study-design, rct, cohort, case-control, cross-sectional, sr-ma, evidence-hierarchy, critical-appraisal, overview]
relations:
  - target: "overviews/evidence-appraisal-toolkit"
    type: companion
  - target: "overviews/statistical-abbreviations-cheatsheet"
    type: companion
  - target: "overviews/critical-appraisal-checklists-dental"
    type: companion
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - **핵심 목적**: 치과 논문을 처음 읽는 사람이 설계 유형을 한눈에 구분하고, 디자인별로 무슨 숫자를 믿어야 하는지 · 어떤 편향을 경계해야 하는지 파악하기 위한 입문 가이드.
> - **근거 위계**: 체계적문헌고찰+메타분석 (Systematic Review+Meta-Analysis, SR+MA) > 무작위대조시험 (Randomized Controlled Trial, RCT) > 코호트 (Cohort) > 환자-대조군 (Case-Control) > 단면연구 (Cross-Sectional) > 증례보고 (Case Report). 위계는 "인과 추론 강도"이지 "샘플 크기"가 아니다.
> - **RCT가 최강인 이유**: 무작위배정(Randomization)이 알려진·미지의 교란변수(Confounding Variable)를 동시에 분산시켜 배정군 간 차이를 처치 효과로 귀속할 수 있다. 단점은 윤리·비용·추적기간 한계.
> - **코호트 강점**: 장기 추적 가능, 여러 결과 동시 관찰, 드물지 않은 결과에서 상대위험 (Relative Risk, RR)/위험비 (Hazard Ratio, HR) 직접 계산. 약점: 교란변수 보정이 모든 신뢰도의 열쇠 — 보정하지 않은 HR을 인과 관계로 읽으면 안 된다.
> - **환자-대조군 핵심**: 드문 결과(예: 임플란트 골유착 실패 1–3%)에 적합, 교차비 (Odds Ratio, OR)만 계산 가능. OR ≈ RR인 조건: 결과 발생률 < 10%.
> - **SR+MA 읽기 순서**: abstract보다 forest plot 먼저 → 이질성 지수 I² 확인(>75%면 풀링 결과 보류) → PROSPERO 등록·a priori PICO → 개별 연구 비뚤림 위험 (Risk of Bias, RoB) → GRADE 근거 등급.
> - **인과추론 4단계 도구**: ①Bradford Hill criteria (연관성 강도·일관성·특이성·시간적 선행·생물학적 타당성) ②무작위화 ③도구변수 (Instrumental Variable, IV) ④가상사실 비교 (Counterfactual Reasoning). 관찰연구는 ①만 가능.
> - **치과 논문 최빈 편향 6가지**: ① 생존편향 (Survivorship Bias) ② 불멸시간편향 (Immortal Time Bias — 후향 즉시부하vs지연부하) ③ 지시편향 (Indication Bias — 전신질환자=다른 임플란트 프로토콜) ④ 선택편향 (Selection Bias — 단일기관 후향) ⑤ 출판편향 (Publication Bias) ⑥ 스폰서 편향 (Sponsorship Bias).

## Three-line Summary

A self-contained primer on the six major dental research study designs — SR+MA, RCT, prospective cohort, retrospective cohort, case-control, cross-sectional — covering the evidence hierarchy, per-design purpose/strengths/weaknesses, the correct effect measure for each, key internal-validity threats, and a five-item speed-read checklist.

Companion to the [[overviews/evidence-appraisal-toolkit]] (statistics axis) and [[overviews/statistical-abbreviations-cheatsheet]] (abbreviation reference): this primer answers "what kind of paper is this and what can it prove?" before those tools answer "what do the numbers mean?"

Designed as a living reference for a clinician who reads dental SRs and RCTs daily; the six bias categories highlighted are the most commonly encountered in implant and endodontic retrospective literature ingested into this wiki.

## 세줄요약

치과 논문 6대 설계 유형(SR+MA·RCT·전향코호트·후향코호트·환자-대조군·단면연구)을 근거 위계·목적·강약점·올바른 효과측정치·주요 편향·속독 체크리스트로 정리한 입문 가이드.

핵심 룰: 인과 추론은 무작위화 또는 충분한 교란변수 보정 없이는 불가능 — 관찰연구의 HR/OR은 "연관성"이지 "원인"이 아니다; OR은 결과 발생률 < 10%에서만 RR에 근사.

치과 최빈 편향: 불멸시간편향(후향 부하시기 비교), 지시편향(전신질환자 프로토콜 차이), 스폰서 편향(임플란트 표면·재료 RCT) 3개가 이 wiki 임플란트 문헌에서 가장 많이 발견됨.

---

## 1. 근거 위계 (Evidence Hierarchy)

```
       SR + MA (umbrella review)
           ↑ 가장 높음
       SR + MA
           ↑
       RCT (잘 설계된)
           ↑
       Prospective Cohort
           ↑
       Retrospective Cohort
           ↑
       Case-Control
           ↑
       Cross-Sectional
           ↑
       Case Series / Report
           ↓ 가장 낮음
```

> **중요**: 위계는 "인과 추론 가능성"의 순서이지 "연구 규모"나 "저널 임팩트팩터"가 아니다.
> 잘 설계된 대규모 코호트가 형편없는 소규모 RCT보다 더 유용할 수 있다.

---

## 2. 설계 유형별 핵심 정리

### 2-A. SR + MA (체계적문헌고찰 + 메타분석)

| 항목 | 내용 |
|---|---|
| **목적** | 특정 PICO 질문에 대한 기존 연구를 체계적으로 종합 |
| **효과측정치** | 원 연구의 측정치를 풀링: Weighted Mean Difference (WMD), OR, RR, HR |
| **장점** | 최대 표본 크기, 출판편향 가시화 가능 |
| **약점** | 쓰레기 in → 쓰레기 out (GIGO); 이질성 I² > 75%면 풀링 무의미; 중복 SR 범람 |
| **핵심 체크** | PROSPERO 등록? a priori PICO? 독립 reviewer 2인? AMSTAR-2/PRISMA? |
| **대표 도구** | AMSTAR-2 (SR질평가), GRADE (근거등급), funnel plot (출판편향) |

**속독 순서**: ① forest plot → I² 확인 ② GRADE 표 → 근거 등급 ③ Methods → PROSPERO·검색일 ④ 개별 연구 RoB ⑤ 임상적 이질성(연구 간 인구·프로토콜 차이)

---

### 2-B. RCT (무작위대조시험)

| 항목 | 내용 |
|---|---|
| **목적** | 처치 효과의 인과적 추정 |
| **배정 방법** | 무작위배정 (Randomization) + 배정은닉 (Allocation Concealment) |
| **효과측정치** | RR, ARR, NNT (binary); Mean Difference (연속) |
| **장점** | 인과 추론 가능, 교란변수 균형화 |
| **약점** | 윤리적 제약, 짧은 추적기간, 단일 센터, 눈가림(Blinding) 어려움 |
| **편향** | Attrition bias (탈락 비무작위), Performance bias (불균등 처치), Detection bias (비맹검평가자) |
| **핵심 체크** | CONSORT 체크리스트; ITT vs PP 분석; 눈가림 수준; 비교군이 진짜 표준치료인가? |

**속독 순서**: ① 배정 방법 (CONSORT flow) ② 배정은닉·눈가림 ③ 탈락율 < 20%? ④ ITT 분석 여부 ⑤ 효과 크기 + 95% CI

**치과 특이 함정**: 임플란트 RCT에서 환자 단위 무작위 vs 임플란트 단위 무작위를 혼용 → 클러스터링 무시(한 환자 내 임플란트 간 독립성 가정 위반)

---

### 2-C. Prospective Cohort (전향 코호트)

| 항목 | 내용 |
|---|---|
| **목적** | 노출 → 결과 추적; 장기 생존율, 여러 결과 동시 관찰 |
| **효과측정치** | RR, HR, Kaplan-Meier 생존분석 |
| **장점** | 시간적 선행 확립, 노출 전 데이터 수집, 여러 결과 동시 가능 |
| **약점** | 비용·시간, 추적소실 (Loss to Follow-up) |
| **편향** | Selection bias (등록 기준), Attrition bias (탈락 비무작위), Confounding |
| **핵심 체크** | STROBE 체크리스트; 교란변수 측정·보정 방법; 추적소실율 < 20% |

---

### 2-D. Retrospective Cohort (후향 코호트)

| 항목 | 내용 |
|---|---|
| **목적** | 이미 축적된 기록에서 노출↔결과 관계 탐색 |
| **효과측정치** | RR (고정기간), HR (생존분석), OR (로지스틱 회귀) |
| **장점** | 빠르고 저렴, 희귀 노출 연구 가능 |
| **약점** | 데이터 품질 의존, 기록 누락, 교란변수 보정 한계 |
| **고유 편향** | **불멸시간편향 (Immortal Time Bias)**: 노출군 정의 기간 동안 결과가 발생 불가능 → 노출군 생존율 과대평가. 치과에서 가장 흔한 사례: 즉시부하 vs 지연부하 후향 비교 |
| **핵심 체크** | 교란변수 목록 + Cox 비례위험 모델에 포함 여부; 불멸시간 처리; 생존편향 가능성 |

---

### 2-E. Case-Control (환자-대조군)

| 항목 | 내용 |
|---|---|
| **목적** | **드문 결과** 연구에 최적 (예: 임플란트 실패 1–3%, 악골 괴사 등) |
| **설계 방향** | 결과(Case) → 소급하여 노출 확인 |
| **효과측정치** | **OR만** 계산 가능 (RR/AR 직접 추정 불가) |
| **OR ≈ RR 조건** | 결과 발생률 < 10% (치과 임플란트 실패에서 대체로 성립) |
| **장점** | 드문 결과에 효율적, 빠름 |
| **약점** | 회상편향 (Recall Bias), 선택편향, 인과 방향 불명확 |
| **핵심 체크** | Case/Control 선정 기준; 매칭 변수; 회상편향 최소화 전략 |

---

### 2-F. Cross-Sectional (단면연구)

| 항목 | 내용 |
|---|---|
| **목적** | 특정 시점의 노출-결과 공존 관계; 유병률 조사 |
| **효과측정치** | Prevalence Ratio (PR), OR |
| **장점** | 빠름, 저렴, 유병률 기술 |
| **약점** | 인과 방향 불명확 (닭-달걀), 시간적 선행 확립 불가 |
| **용도** | 유병률 조사, 연구 가설 생성 |

---

## 3. 편향 빠른참조 (치과 최빈 6가지)

| 편향 | 발생 상황 | 대표 사례 (이 wiki) |
|---|---|---|
| **생존편향** (Survivorship Bias) | 초기 탈락자·실패자가 분석에서 제외됨 | 단일기관 10년 생존율 → 전원·사망·포기 환자 미포함 |
| **불멸시간편향** (Immortal Time Bias) | 노출군 정의 기간 동안 결과 발생 불가 | 즉시부하 코호트: 부하 결정 시점 이전 실패를 지연부하군에 배정 |
| **지시편향** (Indication Bias) | 노출과 결과가 제3 요인(임상 판단)에 의해 함께 결정 | 당뇨 환자 → 더 보수적 프로토콜 → 더 나은 결과 → "당뇨=좋음"으로 오독 |
| **선택편향** (Selection Bias) | 연구 참여 여부가 결과와 연관 | 단일 전문의 클리닉 후향 차트 — 의뢰 편향 |
| **출판편향** (Publication Bias) | 양성 결과만 출판 | funnel plot 비대칭; 소규모 RCT에서 큰 효과 |
| **스폰서 편향** (Sponsorship Bias) | 제조사 후원 → 자사 제품 유리한 결과 | 임플란트 표면처리 RCT에서 후원사 제품 우위 패턴 |

---

## 4. 효과측정치 ↔ 설계 매핑

| 측정치 | 정의 | 쓰이는 설계 | 주의 |
|---|---|---|---|
| **RR** (Relative Risk, 상대위험) | P(결과\|노출) / P(결과\|비노출) | RCT, 코호트 | 기저위험 무시; ARR 항상 같이 |
| **OR** (Odds Ratio, 교차비) | (Case 노출 odds) / (Control 노출 odds) | 환자-대조군, 로지스틱 회귀 | 결과 > 10%면 RR 과대평가 |
| **HR** (Hazard Ratio, 위험비) | 순간 위험률 비 | 생존분석 (코호트, RCT time-to-event) | 비례위험(PH) 가정 위반 시 단독 해석 금지 |
| **ARR** (Absolute Risk Reduction, 절대위험감소) | P(결과\|대조) − P(결과\|처치) | RCT | 환자 상담에 필수 |
| **NNT** (Number Needed to Treat, 치료필요수) | 1 / ARR | RCT | 클수록 효과 약함; 95% CI 함께 제시 |
| **MD** (Mean Difference) | 두 군 평균차 | RCT (연속) | 단위 동일할 때 |
| **SMD** (Standardized MD) | MD / pooled SD | SR+MA (단위 다를 때) | 해석 위해 원래 단위로 역변환 |

---

## 5. 설계별 PICO 질문 패턴

| 질문 유형 | 최적 설계 |
|---|---|
| "처치 A가 B보다 효과적인가?" (인과) | RCT → SR+MA |
| "위험요인 X는 결과 Y를 얼마나 증가시키는가?" (장기) | Prospective Cohort |
| "드문 결과 Y의 위험요인은?" | Case-Control |
| "현재 유병률은?" | Cross-Sectional |
| "10년 생존율은?" | Retrospective Cohort 또는 Prospective Cohort |
| "여러 RCT를 합치면?" | SR + MA |

---

## 6. CONSORT / STROBE / PRISMA 한눈에

### RCT → CONSORT (25개 항목 중 핵심 5개)
1. 무작위배정 방법 (sequence generation)
2. 배정은닉 (allocation concealment mechanism)
3. 눈가림 (blinding — 누가, 어떻게)
4. 참여자 흐름도 (CONSORT flow diagram — 탈락 이유)
5. 분석 집단 (ITT? PP? 무엇이 기본?)

### 관찰연구 → STROBE (22개 항목 중 핵심 5개)
1. 연구 설계 명시 (코호트? 환자-대조군? 단면?)
2. 참여자 선정 기준 + 제외 기준
3. 노출 측정 방법 (어떻게 정의하고 측정했는가)
4. 교란변수 목록 + 보정 방법
5. 민감도 분석 또는 결측치 처리

### SR + MA → PRISMA (27개 항목 중 핵심 5개)
1. PROSPERO 등록 번호
2. 검색 전략 (데이터베이스 + 날짜 + 필터)
3. 포함/제외 기준 (2인 독립 스크리닝)
4. 개별 연구 비뚤림 위험 (RoB 2 / ROBINS-I)
5. GRADE 근거 등급 + 비대칭 funnel plot

---

## 7. 관련 페이지

- [[overviews/evidence-appraisal-toolkit]] — 5축 통계 도구상자 (I², OR/RR/HR 수식, 흔한 오류 7가지, 검정 선택)
- [[overviews/statistical-abbreviations-cheatsheet]] — 통계 약자 9맥락 빠른참조
- [[overviews/critical-appraisal-checklists-dental]] — 설계별 체크리스트 실전 워크시트
- [[evidence-appraisal/barraclough-2011-hazard-ratios-clinicians-biostatistics-primer]] — HR·KM 상세
- [[evidence-appraisal/monaghan-2021-odds-ratios-relative-risk-absolute]] — OR·RR·ARR·NNT 상세
- [[evidence-appraisal/habibzadeh-2024-reinterpretation-results-randomized-clinical-trials]] — p값 재해석
- [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]] — 흔한 통계 오류
