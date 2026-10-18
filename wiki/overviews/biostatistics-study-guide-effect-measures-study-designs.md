---
title: "통계공부 — 효과측정치(OR·RR·HR)와 연구 디자인 계층 레퍼런스"
authors: Synthesis (Damian Lee)
year: 2026
date: 2026-10-18
doi: N/A
source: N/A
category: overviews
evidence_level: synthesis
pdf_path: N/A
pdf_filename: N/A
source_collection: synthesis
tags: [evidence-appraisal, biostatistics, odds-ratio, risk-ratio, hazard-ratio, study-design, rct, cohort, systematic-review, meta-analysis, nnt, grade, overview]
relations:
  - target: "[[evidence-appraisal-toolkit]]"
    type: companion
    note: "toolkit covers appraisal checklist; this page covers foundational concepts & study-type matrix"
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - **교차비 (Odds Ratio, OR)**: 사건 발생 Odds의 비 — 환자-대조군 연구(Case-Control)에서 유일하게 계산 가능. 희귀질환이면 OR≈RR이나, 흔한 결과(발생률>10%)일수록 OR이 상대위험도(Relative Risk, RR)를 **과대추정**한다.
> - **상대위험도 (Relative Risk, RR)**: 두 군의 사건 발생 **확률** 비 — 코호트·RCT의 기본 지표. 시간 개념 없음.
> - **위험비 (Hazard Ratio, HR)**: 시간 경과를 통합한 **순간 사건 발생 속도**의 비 — 생존분석(Cox 회귀, Kaplan–Meier)에서 추출. 추적 기간이 다른 군 간 공정 비교 가능. 임플란트·치주 장기 추적 연구에 자주 등장.
> - **OR vs RR vs HR 핵심 차이**: OR=역방향 조사(희귀질환 적합), RR=발생률 직접 비교(시점 고정), HR=시간 가중 생존(시점 불균등 허용). 세 지표 모두 95% CI가 1.0을 포함하면 통계적 비유의.
> - **실용 변환**: OR/HR는 절대위험차(Absolute Risk Difference, ARD)와 치료필요수(Number Needed to Treat, NNT = 1/ARD)로 환산해야 환자 상담이 직관적. "HR 2.5" → "100명 중 약 N명 더 실패"로 변환.
> - **연구 디자인 피라미드**: SR+MA > RCT > 전향 코호트 > 후향 코호트 > 환자-대조군 > 횡단 > 증례군 > 전문가 의견. OR만 계산할 수 있는 디자인은 환자-대조군뿐.
> - **RCT 유형**: Double-blind, Crossover, Cluster, Non-inferiority, Equivalence, Factorial.
> - **SR vs MA 구분**: SR은 질적 종합(숫자 합산 없음), MA는 여기에 pooling 통계 추가. SR 없는 MA는 선택 편향 위험. **I²>75%이면 pooled 효과 추정치는 거의 무의미** — subgroup 분석으로 이질성 원인을 먼저 규명해야 함.
> - **GRADE**: High→Very Low 4단계. RCT=High에서 시작하나 비뚤림·비일관성·비직접성·비정밀성·출판편향이 있으면 강등. 관찰연구=Low에서 시작하나 대효과·용량-반응 관계면 승등 가능.
> - **임상 적용 3-step**: ① 연구 디자인 확인 → 어떤 효과측정치가 타당한지 판단. ② 점추정치+95% CI 동시 읽기(CI 폭=정밀도). ③ 상대 지표(OR/RR/HR)를 절대 지표(ARD/NNT)로 변환 후 환자 설명.

## Three-line Summary

Reference guide for the foundational concepts of clinical biostatistics — effect measures (OR, RR, HR), derived metrics (ARD, NNT, SMD), statistical tests, study design hierarchy, RCT subtypes, SR/MA methodology (I², pooling, GRADE), and a head-to-head comparison matrix — intended as a compact study aid for reading and presenting clinical research, with concrete dental clinical examples throughout.

OR is calculated only from case-control designs; RR from cohort/RCT; HR from time-to-event analyses (Cox/Kaplan–Meier); all three share the same CI null at 1.0, but OR over-estimates RR when outcome prevalence exceeds ~10%.

Practical translation rule: always convert relative measures (OR/HR) to ARD or NNT before patient counseling — "HR 2.5 for smokers" is less actionable than "roughly 7 additional failures per 100 smoker-implants."

## 세줄요약

임상 바이오통계 핵심 개념 레퍼런스 — 효과측정치(OR·RR·HR), 파생 지표(ARD·NNT·SMD), 연구 디자인 계층, RCT 유형, SR+MA 방법론(I²·풀링·GRADE)을 치과 임상 예시와 함께 집약한 교육용 빠른 참조 가이드.

교차비(Odds Ratio, OR)는 환자-대조군 연구에서만 도출 가능; 상대위험도(Relative Risk, RR)는 코호트·RCT; 위험비(Hazard Ratio, HR)는 생존분석(Cox·Kaplan–Meier). 세 지표 공통 귀무가설 경계 = 1.0; 발생률>10%에서 OR이 RR을 과대추정한다는 점이 핵심 함정.

실용 규칙: OR/HR는 반드시 절대위험차(Absolute Risk Difference, ARD) 또는 치료필요수(Number Needed to Treat, NNT)로 변환해 환자 설명에 쓸 것 — 상대 지표는 임상 결정의 체감 규모를 왜곡한다.

---

## 1. Effect Measures — Core Three

### 1.1 OR — Odds Ratio (교차비)

| Item | Detail |
|---|---|
| **Formula** | `OR = (a·d) / (b·c)` from a 2×2 table |
| **Denominator** | Odds = P(event) / P(no event) |
| **Null value** | OR = 1.0 |
| **Typical study** | Case-control, logistic regression |
| **Time dimension** | None |
| **Key trap** | Over-estimates RR when prevalence > ~10% |

**2×2 Table**

|  | 임플란트 실패(+) | 임플란트 생존(−) |
|---|---|---|
| **흡연자** | a | b |
| **비흡연자** | c | d |

- OR > 1 → exposure increases odds of disease
- OR < 1 → exposure is protective
- OR = 1 → no association

**When OR ≈ RR**: rare-disease assumption (prevalence < 5–10%). As prevalence rises, OR increasingly exceeds RR (relative over-estimation).

> **🦷 임상 예시 — OR 계산 직접 해보기**
>
> 환자-대조군 연구: 임플란트 실패 여부와 흡연 관계를 역방향으로 조사.
>
> |  | 임플란트 실패 | 임플란트 생존 |
> |---|---|---|
> | **흡연자** | 30명 (a) | 70명 (b) |
> | **비흡연자** | 10명 (c) | 90명 (d) |
>
> - 흡연자 Odds = 30/70 = 0.43
> - 비흡연자 Odds = 10/90 = 0.11
> - **OR = (30×90) / (70×10) = 2700/700 = 3.86**
> - 해석: 흡연자는 비흡연자보다 임플란트 실패 odds가 3.86배 높다.
> - 이 연구에서 발생률 = (30+10)/(200) = 20% → OR이 RR을 어느 정도 과대추정함에 주의.

---

### 1.2 RR — Relative Risk / Risk Ratio (상대위험도)

| Item | Detail |
|---|---|
| **Formula** | `RR = [a/(a+b)] / [c/(c+d)]` |
| **Denominator** | Incidence probability |
| **Null value** | RR = 1.0 |
| **Typical study** | Cohort, RCT (fixed follow-up) |
| **Time dimension** | None (fixed time point) |
| **Advantage over OR** | Direct probability ratio; no inflated magnitude at high prevalence |

- RR = 2.0 → exposed group has twice the probability of the event
- 95% CI excluding 1.0 → statistically significant

> **🦷 임상 예시 — RR 읽는 법**
>
> 5년 전향 코호트: 흡연군(n=200) vs 비흡연군(n=200)의 임플란트 실패율 비교.
>
> |  | 실패 | 생존 | 발생률 |
> |---|---|---|---|
> | **흡연군** | 20명 | 180명 | 20/200 = **10%** |
> | **비흡연군** | 5명 | 195명 | 5/200 = **2.5%** |
>
> - **RR = 10% / 2.5% = 4.0**
> - 해석: 흡연군은 비흡연군보다 5년 내 임플란트 실패 확률이 **4배** 높다.
> - OR 계산: (20×195)/(180×5) = 3900/900 = **4.33** → 발생률이 낮지 않아(10%) OR이 RR보다 크게 나옴.
> - 환자 상담: "흡연하시면 비흡연자보다 임플란트가 실패할 확률이 약 4배 높습니다" (RR 사용이 OR보다 정직함).

---

### 1.3 HR — Hazard Ratio (위험비)

| Item | Detail |
|---|---|
| **What it measures** | Instantaneous rate of event occurrence (hazard rate ratio) |
| **Null value** | HR = 1.0 |
| **Typical study** | Survival analysis: Cox proportional hazards, Kaplan–Meier |
| **Time dimension** | Yes — weighted across the full follow-up period |
| **Key advantage** | Fair comparison when follow-up times differ between groups |
| **Output** | HR from Cox regression (adjusted); log-rank p-value from KM |

- HR > 1 → event occurs faster in exposed group
- HR < 1 → protective (slower event rate)
- **HR ≈ RR** when the event is rare; diverges with common events and variable follow-up

> **🦷 임상 예시 — HR이 RR과 다른 이유**
>
> 10년 후향 코호트: 당뇨군 vs 정상혈당군 임플란트 생존 분석.
>
> 추적 기간이 1년~10년으로 다 다름 → Kaplan–Meier 곡선 + Cox regression.
>
> - **HR(당뇨군) = 2.3 (95% CI 1.5–3.4)**
> - 해석: 당뇨군은 매 시점에서 임플란트 실패 속도가 2.3배 빠르다.
> - RR로는 계산 불가 — 환자마다 follow-up 기간이 달라 분모(인-년, person-years) 조정이 필요하기 때문.
> - **Kaplan–Meier 곡선**: x축=시간, y축=생존 확률. 두 곡선이 벌어질수록 HR > 1.
> - **Log-rank test p값**: 두 KM 곡선이 통계적으로 다른지 검정.
>
> 📊 KM 곡선 읽는 법:
> ```
> 생존율(%)
> 100 ─ ─ ─ ─────────────────── 비당뇨군
>  90          ╲
>  80           ╲ ─ ─ ─ ─ ─ ─ ─ 당뇨군
>  70                 ╲
>     0    2    4    6    8    10 (년)
> ```
> 곡선의 각 계단 = 실패 사건 발생. ✚ = censored(추적 탈락).

---

### 1.4 Head-to-Head Comparison

| | **OR** | **RR** | **HR** |
|---|---|---|---|
| Denominator | Odds | Probability | Hazard (instantaneous rate) |
| Time-sensitive | No | No | **Yes** |
| Primary design | Case-control | Cohort, RCT | Survival (Cox, KM) |
| Rare-disease approximation | OR ≈ RR | — | HR ≈ RR |
| High-prevalence trap | **OR > RR** (inflated) | Accurate | Accurate |
| 95% CI null | Excludes 1.0 | Excludes 1.0 | Excludes 1.0 |

> **🦷 세 지표 같은 데이터에서 비교 (임플란트 실패, 발생률 20%)**
>
> | 지표 | 값 | 해석 |
> |---|---|---|
> | OR | 3.86 | "흡연자 실패 odds 3.86배" |
> | RR | 3.0 | "흡연자 실패 확률 3.0배" |
> | HR | 3.2 | "흡연자 실패 속도 3.2배 빠름 (10년 추적)" |
>
> 발생률 20%에서 OR이 RR보다 크게 나오는 것을 직접 확인.
> → 논문이 OR을 보고했는데 발생률이 높다면 실제 효과는 더 작다고 보정해서 읽어야 한다.

---

## 2. Derived Metrics

| Abbreviation | Korean | Definition | Use |
|---|---|---|---|
| **ARD / RD** | 절대위험차 (Absolute Risk Difference) | Incidence_exposed − Incidence_unexposed | Magnitude of absolute benefit/harm |
| **NNT** | 치료필요수 (Number Needed to Treat) | 1 / ARD | Patients to treat for 1 additional benefit |
| **NNH** | 해필요수 (Number Needed to Harm) | 1 / ARD(harm) | Patients treated per 1 additional harm |
| **MD** | 평균차 (Mean Difference) | Mean_A − Mean_B | Continuous outcomes, same unit |
| **WMD** | 가중평균차 (Weighted Mean Difference) | Precision-weighted MD across studies | Meta-analysis of continuous outcomes |
| **SMD** | 표준화평균차 (Standardised Mean Difference) | MD / pooled SD | Meta-analysis across different scales |
| **I²** | 이질성 지수 (Heterogeneity Index) | % variance from true heterogeneity | I²<25% homogeneous; >75% pooling questionable |

> **🦷 NNT 계산 예시 — 항생제 예방투여**
>
> RCT: 발치 후 항생제 투여군(n=300) vs 위약군(n=300), 결과 = 감염 발생.
>
> | 군 | 감염 발생 | 발생률 |
> |---|---|---|
> | **항생제군** | 6명 | 2% |
> | **위약군** | 18명 | 6% |
>
> - **ARD = 6% − 2% = 4%** (위약이 4%p 더 많음)
> - **NNT = 1/0.04 = 25**
> - 해석: "25명에게 항생제를 예방 투여해야 감염 1건을 예방할 수 있다."
> - **RR = 2%/6% = 0.33** (항생제군 감염이 1/3 수준)
> - 환자 설명 비교:
>   - "항생제를 먹으면 감염 위험이 **3배** 줄어요" (RR) — 임팩트 과장 느낌
>   - "항생제를 먹으면 감염 확률이 **4% 줄어요** (6→2%)" (ARD) — 더 솔직
>   - "25명 중 1명꼴로 감염을 예방합니다" (NNT) — 가장 직관적

> **🦷 MD vs SMD — ISQ 비교**
>
> MD (같은 단위): "SLA 표면 임플란트 vs 기계가공 표면의 삽입 직후 임플란트 안정성 지수 (Implant Stability Quotient, ISQ): **MD = +8.3점** (SLA가 더 높음)"
>
> SMD (단위 다를 때): 여러 연구가 ISQ, RFA 전압값(V), 공진 주파수(Hz)를 각각 다른 단위로 보고 → SMD로 표준화 후 풀링.
> - SMD = 0.2 → 작은 효과 (Cohen's d 기준: small=0.2, medium=0.5, large=0.8)
> - SMD = 0.8 → 큰 효과

---

## 3. Study Design Hierarchy

```
         ▲  Highest evidence
         │
    ┌─────────────────────┐
    │   SR + MA           │  Systematic Review + Meta-Analysis
    ├─────────────────────┤
    │   RCT               │  Randomized Controlled Trial
    ├─────────────────────┤
    │   Prospective Cohort│
    ├─────────────────────┤
    │   Retrospective     │
    │   Cohort            │
    ├─────────────────────┤
    │   Case-Control      │
    ├─────────────────────┤
    │   Cross-Sectional   │
    ├─────────────────────┤
    │   Case Series       │
    ├─────────────────────┤
    │   Expert Opinion /  │
    │   Case Report       │
    └─────────────────────┘
         ▼  Lowest evidence
```

### 3.1 Study Type Reference

| Design | Korean | Effect measure | Causal inference | Key strength | Key limitation |
|---|---|---|---|---|---|
| **SR + MA** | 체계적문헌고찰+메타분석 | Pooled OR/RR/HR/MD | Depends on included studies | Highest precision if I²<25% | GIGO: bad input → bad pool |
| **RCT** | 무작위대조시험 | RR, ARD, NNT | Strong (randomisation controls confounding) | Causal inference | Cost, ethics, short follow-up |
| **Prospective Cohort** | 전향 코호트 | RR, HR | Moderate | Real-world data; long follow-up possible | Confounding; loss to follow-up |
| **Retrospective Cohort** | 후향 코호트 | RR, HR | Moderate-low | Fast, cheap | Data quality depends on records |
| **Case-Control** | 환자-대조군 | **OR only** | Low | Rare disease; fast | Recall bias; selection bias |
| **Cross-Sectional** | 횡단 (유병률) | Prevalence ratio | None (temporal ambiguity) | Quick; prevalence mapping | Cannot establish temporality |
| **Case Series** | 증례군 | Descriptive | None | Rare event signal; hypothesis generation | No comparison group |

> **🦷 같은 질문을 디자인별로 접근하면?**
>
> **연구 질문**: "골다공증 치료제(비스포스포네이트) 복용이 임플란트 실패 위험을 높이는가?"
>
> | 디자인 | 어떻게 하나 | 효과측정치 | 한계 |
> |---|---|---|---|
> | **Case-Control** | 임플란트 실패군 100명 vs 생존군 100명 → 과거 비스포스포네이트 복용 여부 조회 | OR | 복약 기억 오류(recall bias); 복약 기간 정보 없음 |
> | **Retrospective Cohort** | 병원 처방 DB에서 비스포스포네이트 복용군 500명 vs 비복용군 1000명 → 임플란트 실패 소급 추적 | RR, HR | 처방 여부만 알고 복약 순응도 모름 |
> | **Prospective Cohort** | 임플란트 예정 환자 중 비스포스포네이트 복용군·비복용군을 지금부터 5년 추적 | RR, HR | 5년 대기; 교란변수 통제 어려움 |
> | **RCT** | ❌ 비윤리적 — "한 군은 비스포스포네이트 먹고 임플란트 심어라"는 설계 불가 | — | 윤리 제약 |
> | **SR+MA** | 위 3가지 관찰연구들을 체계적으로 모아 HR 풀링 | Pooled HR | 각 연구 질 차이 → I² 높을 가능성 |

---

## 4. RCT Subtypes

| Subtype | Korean | Defining feature |
|---|---|---|
| **Parallel RCT** | 평행군 RCT | Standard two-arm; each participant receives one intervention |
| **Double-blind** | 이중맹검 | Participant + outcome assessor masked |
| **Triple-blind** | 삼중맹검 | + Statistician masked |
| **Crossover** | 교차 RCT | Same participant receives both treatments in sequence (washout required) |
| **Cluster RCT** | 군집 RCT | Groups (clinics, schools) randomised, not individuals |
| **Factorial** | 요인설계 RCT | 2+ interventions tested simultaneously in a 2×2 (or larger) matrix |
| **Non-inferiority** | 비열등성 RCT | Tests whether new treatment is "not worse by more than margin δ" |
| **Equivalence** | 동등성 RCT | Tests that new ≈ old within ±δ; requires two one-sided tests |
| **Adaptive** | 적응형 RCT | Interim analyses allow pre-specified modifications (sample size, arm allocation) |

> **🦷 RCT 유형별 치과 예시**
>
> **Parallel (평행군)**: 근관치료 단일방문 vs 다중방문 — 한 그룹은 단일, 다른 그룹은 2회. 가장 흔한 형태.
>
> **Double-blind**: 치주치료 후 chlorhexidine 젤 vs 위약 — 환자도 술자도 어느 것인지 모름. 젤 색·질감을 동일하게 만들어야 함.
>
> **Crossover**: 두 가지 치간세정기(치실 vs 치간칫솔) 비교 — 같은 환자가 6주씩 둘 다 사용, 2주 휴약기(washout). 환자 수 적어도 가능. 단, 세정 효과가 carry-over되면 안 됨.
>
> **Cluster RCT**: 학교 불소 프로그램 효과 — 학교 단위로 무작위 배정. 같은 학교 학생들은 "독립적이지 않으므로" 개인 단위 RCT로 배정하면 오염(contamination) 발생.
>
> **Factorial**: 항생제 AND 스테로이드 효과를 동시 검증 — 4개 군: (항생제O+스테로이드O), (항생제O+스테로이드X), (항생제X+스테로이드O), (항생제X+스테로이드X). 두 약의 상호작용도 볼 수 있음.
>
> **Non-inferiority**: 새 임플란트 표면이 기존 SLA 대비 "생존율 차이가 ±5% 이내"임을 보이는 연구. δ=5%로 설정. "기존과 같음"을 증명하는 것이 아니라 "기존보다 나쁘지 않음"을 증명.

---

## 5. Systematic Review & Meta-Analysis Methodology

### 5.1 Definitions

| Term | Distinction |
|---|---|
| **Narrative Review (NR)** | Author-selected literature; no protocol; synthesis is qualitative and non-systematic |
| **Scoping Review** | Maps evidence landscape; answers "what has been studied?" — no pooling, no GRADE |
| **Systematic Review (SR)** | Pre-registered protocol; exhaustive search; risk-of-bias assessment; qualitative synthesis |
| **Meta-Analysis (MA)** | Statistical pooling of SR data into a single effect estimate; requires sufficient homogeneity |
| **Umbrella Review** | SR of SRs; highest-tier synthesis |
| **IPD-MA** | Individual Patient Data meta-analysis; uses raw participant-level data; highest precision |
| **NMA** | Network Meta-Analysis; compares 3+ interventions including indirect comparisons |

> **🦷 리뷰 유형 구분 예시**
>
> **Narrative Review**: "임플란트 표면처리의 역사와 현황" — 저자가 자신의 지식을 바탕으로 중요 논문을 선택해 서술. 비체계적이지만 읽기 쉬움.
>
> **Scoping Review**: "지난 10년간 임플란트 ISQ에 관한 연구는 어떤 것들이 있나?" — 어떤 연구가 존재하는지 지형 파악. 효과 크기 계산 없음.
>
> **SR**: "임플란트 즉시부하 vs 지연부하의 생존율: 체계적 문헌고찰" — PICO 사전 설정, PRISMA 보고, RoB 평가. 수치 합산 없음.
>
> **SR+MA**: 위 SR에 forest plot 추가 — pooled HR = 1.05 (95% CI 0.89–1.24): "즉시부하와 지연부하 생존율 차이 없음."
>
> **NMA**: "즉시부하 vs 조기부하 vs 지연부하 vs 즉시식립+즉시부하" 4가지를 동시 비교. 직접 RCT가 없는 쌍도 간접 비교로 추정값 도출.
>
> **Umbrella Review**: 임플란트 당뇨 관련 SR+MA 12편을 모아 "어느 SR의 근거가 얼마나 신뢰할 수 있나?" 2단계 평가.

### 5.2 Forest Plot 읽는 법

```
연구명              효과 크기 (HR)              Weight
────────────────────────────────────────────────────
Kim 2020          ●──────|──────             8.2%
Lee 2021      ●───|─                        12.5%
Park 2022                  |──●──────       6.8%
Chen 2023           ●──|──                  20.1%
────────────────────────────────────────────────────
Pooled            ◆                         100%
                  |
              0.5  1.0  2.0  4.0
                   ↑ null
```

- **각 점(●)**: 개별 연구의 점 추정치
- **수평선**: 95% CI — 짧을수록 정밀 (큰 연구)
- **정사각형 크기(◆)**: 가중치(weight) — 큰 정사각형 = 해당 연구가 pooled에 더 기여
- **수직 점선**: 귀무가설(null, HR=1.0)
- **다이아몬드(◆)**: pooled 효과 추정치 + 전체 CI
- **다이아몬드가 선 오른쪽 전체에 있으면** → 유의하게 위험 증가

### 5.3 I² Heterogeneity Interpretation

| I² range | Interpretation | Action |
|---|---|---|
| 0–25% | Low heterogeneity | Fixed-effects pooling reasonable |
| 25–50% | Moderate | Random-effects; explore sources |
| 50–75% | Substantial | Pooled estimate interpreted cautiously |
| > 75% | Considerable / high | Pooled estimate questionable; subgroup or meta-regression preferred |

> **🦷 I² 예시: 왜 같은 주제인데 I²가 높을까?**
>
> 임플란트 흡연 연구 10편을 모았는데 I² = 82%.
>
> 이질성 원인 후보:
> - 추적 기간이 1년~15년으로 제각각
> - "흡연"의 정의: 하루 10개피 이상 vs 과거 흡연 포함
> - 임플란트 위치: 상악 vs 하악 vs 혼합
> - 표면처리가 SLA·기계가공·nano 모두 섞임
>
> → Subgroup 분석: "추적 5년 이상 + SLA 표면만" 6편만 모으면 I² = 28%.
> → Pooled HR = 2.1 (95% CI 1.6–2.8) — 이제 pooling이 의미있음.

### 5.4 Publication Bias Assessment

- **Funnel plot**: asymmetry suggests small-study effects (not always bias; also heterogeneity)
- **Egger's test**: statistical test for funnel asymmetry; p < 0.10 = suspect
- **PROSPERO registration + a priori PICO**: reduces outcome-reporting bias
- **Trim-and-fill**: imputes missing studies; visualises adjusted estimate

> **🦷 출판 편향(Publication Bias) 쉽게 이해하기**
>
> 깔때기 그림(Funnel Plot) 직관:
> - 큰 연구(위쪽)는 표본이 커서 효과 추정이 정확 → 대칭적으로 모임
> - 작은 연구(아래쪽)는 효과가 크게 나온 것만 출판됨 → 오른쪽에 몰림 → 깔때기 비대칭
>
> 비유: 약효 연구 100개를 해서 50개는 효과 없음이 나왔지만 서랍 속에 잠겨 있고(file-drawer problem), 효과 있다는 50개만 출판됨 → MA가 실제 효과를 과대추정.
>
> 대응책: PROSPERO에 SR 프로토콜 사전 등록 → 결과와 무관하게 출판 의무화.

### 5.5 Quality Appraisal Tools

| Study type | Tool |
|---|---|
| SR+MA | AMSTAR-2 |
| RCT | Cochrane RoB 2.0 |
| Non-randomised studies | ROBINS-I |
| Diagnostic accuracy | QUADAS-2 |
| Reporting (RCT) | CONSORT |
| Reporting (SR) | PRISMA |

> **🦷 RoB 2.0 5개 도메인 — 임플란트 RCT에 적용**
>
> | 도메인 | 질문 | 임플란트 RCT 예 |
> |---|---|---|
> | D1. 무작위화 | 배정 순서가 진짜 무작위인가? | 컴퓨터 난수 vs "홀짝 번호" |
> | D2. 배정 은닉 | 배정을 누가 알고 있었나? | 봉인 봉투 vs 연구자가 다음 배정 알 수 있음 |
> | D3. 맹검 | 결과 측정자가 배정을 몰랐나? | ISQ는 기계 측정이라 맹검 쉬움; 임상 평가는 어려움 |
> | D4. 결과 데이터 | 탈락자가 많거나 편향적이지 않나? | 20% 탈락 → 문제; ITT 분석 했나? |
> | D5. 선택적 보고 | 사전 등록한 결과를 다 보고했나? | 등록 결과: MBL; 실제 보고: ISQ만 |

---

## 6. GRADE Evidence Rating

Starting point: RCT = High; Observational study = Low.

### 6.1 Downgrade Factors (each can lower by 1–2 levels)

| Factor | Example |
|---|---|
| Risk of bias | Inadequate allocation concealment, no blinding |
| Inconsistency | I² > 50%; results direction differs across studies |
| Indirectness | Surrogate outcome (ISQ) not direct patient outcome (implant survival) |
| Imprecision | Wide 95% CI; small sample |
| Publication bias | Funnel asymmetry; industry sponsorship with positive result |

### 6.2 Upgrade Factors (observational studies only)

| Factor | Criterion |
|---|---|
| Large effect | RR or OR > 2.0 (or < 0.5) with no plausible confounding |
| Dose-response | Clear gradient between exposure level and outcome |
| Confounding direction | All unmeasured confounders would attenuate (not amplify) the effect |

### 6.3 GRADE Levels & Clinical Meaning

| Grade | Meaning | Typical source |
|---|---|---|
| **High** | Further research very unlikely to change confidence | Good SR of RCTs |
| **Moderate** | Further research likely to have impact | Downgraded RCT / upgraded cohort |
| **Low** | Further research very likely to have impact | Well-designed cohort |
| **Very Low** | Any estimate is very uncertain | Case series / expert opinion |

> **🦷 GRADE 적용 예시 — 즉시식립 vs 지연식립 생존율**
>
> 1. **연구 수집**: RCT 8편 + 코호트 5편
> 2. **RCT 시작 등급**: High
> 3. **강등 심의**:
>    - 비뚤림: 맹검 불가(수술 특성상) → −1 (Moderate)
>    - 비일관성: I² = 42% (중등도) → 유지
>    - 비직접성: 추적 기간 1~3년 (실제 임상은 5~10년 관심) → −1 (Low)
>    - 비정밀성: 일부 연구 n=30 미만 → −1 (Very Low)
> 4. **최종 등급**: Very Low → "현재 근거로는 즉시식립의 장기 생존율에 대해 확신하기 어렵다"
>
> → 임상 가이드라인에서 "전문가 경험·환자 선호도를 고려한 약한 권고(weak recommendation)" 표기.

---

## 7. Statistical Test Quick Reference

| Situation | Test |
|---|---|
| Continuous, 2 independent groups, normal | Independent t-test |
| Continuous, 2 independent groups, non-normal | Mann-Whitney U |
| Continuous, paired/before-after | Paired t-test or Wilcoxon signed-rank |
| Continuous, ≥3 groups, normal | One-way ANOVA → post-hoc (Tukey/Bonferroni) |
| Continuous, ≥3 groups, non-normal | Kruskal-Wallis → post-hoc (Dunn) |
| Categorical, 2×2 table | Chi-square (expected cell ≥ 5) or Fisher's exact (small cells) |
| Time-to-event, 2 groups | Log-rank test → HR via Cox regression |
| Multiple predictors (continuous outcome) | Multiple linear regression |
| Multiple predictors (binary outcome) | Logistic regression → OR |
| Multiple predictors (time-to-event) | Cox proportional hazards → HR |
| Repeated measures on same patient | Mixed-effects model / GEE |

**Dental-specific trap**: Two implants in the same patient are NOT independent observations. Treating them as independent in a t-test violates the independence assumption → use paired analysis or mixed-effects model (cluster by patient).

> **🦷 검정 선택 실전 — 어떤 검정을 써야 할까?**
>
> **시나리오 1**: SLA 표면 vs 기계가공 표면 임플란트의 삽입 직후 임플란트 안정성 지수 (ISQ) 비교. 두 군 독립, n=각 30, ISQ 정규분포.
> → **Independent t-test** → p값 + MD (예: "SLA군 ISQ가 평균 6.2점 높음, p=0.003")
>
> **시나리오 2**: 같은 환자 입에서 SLA와 기계가공 임플란트를 각 1개씩 식립 후 ISQ 비교 (n=25명).
> → **Paired t-test** (같은 환자의 두 임플란트는 독립 X)
>
> **시나리오 3**: 3가지 세정제(CHX / 식염수 / 위약) 처치 후 치주낭 깊이(Pocket Depth, PD) 변화. 3군, 정규분포 확인.
> → **One-way ANOVA** → post-hoc Tukey (CHX vs 식염수, CHX vs 위약, 식염수 vs 위약 쌍별 비교)
>
> **시나리오 4**: 임플란트 실패(이분형: 예/아니오)와 흡연·당뇨·연령의 관계.
> → **Logistic regression** → 각 인자의 **OR** (95% CI) 도출
>
> **시나리오 5**: 추적 기간이 제각각인 10년 코호트에서 임플란트 실패 시점 분석.
> → **Cox proportional hazards** → **HR** (95% CI) 도출 + Kaplan-Meier 곡선

---

## 8. Confidence Interval Interpretation

> A 95% CI does NOT mean "95% probability the true value is in this range."
> It means: if the study were repeated 100 times, approximately 95 of those intervals would contain the true parameter.

| CI pattern | Interpretation |
|---|---|
| 95% CI excludes 1.0 (for OR/RR/HR) | Statistically significant |
| 95% CI includes 1.0 | Not statistically significant |
| Narrow CI | High precision (large n, low variance) |
| Wide CI | Low precision (small n, high variance) |
| p < 0.05 but wide CI crossing clinically important threshold | Statistically significant but clinically uncertain |
| p > 0.05 but CI entirely below 1.0 | Under-powered; cannot rule out a true effect |

> **🦷 CI 읽기 연습**
>
> 논문 결과: "흡연군 임플란트 실패 HR = 2.1 (95% CI: 1.4–3.2), p=0.001"
>
> ✅ 올바른 해석:
> - HR 2.1: 흡연군은 비흡연군보다 실패 속도가 2.1배 빠름
> - CI 1.4–3.2: 1.0을 포함하지 않으므로 통계적 유의 (p값과 일치)
> - CI 폭이 비교적 좁음 → 정밀한 추정
>
> 비교: "ISQ 향상 MD = 3.5 (95% CI: −0.2–7.2), p=0.064"
>
> ✅ 올바른 해석:
> - p > 0.05, CI가 0을 포함 → 통계적으로 유의하지 않음
> - 그러나 CI 상한 7.2: 임상적으로 의미 있는 효과가 존재할 가능성 배제 못 함
> - **"효과 없다"는 결론 X → "검정력 부족으로 효과 불확실"이 정확**
> - 권장 행동: 표본 크기 계산 후 더 큰 연구 필요
>
> 📌 **통계적 유의 ≠ 임상적 유의**
> - "MBL 차이 MD = 0.03 mm (p=0.001)": 통계적으론 유의하나 임상적으론 무의미 (차이가 너무 작음)
> - "생존율 차이 = 8% (p=0.08)": 통계적 비유의지만 임상적으론 중요할 수 있음 → 더 큰 연구 필요

---

## 9. Common Errors in Dental Literature

| Error | Description | Correct approach |
|---|---|---|
| **p > 0.05 = "no effect"** | Absence of evidence ≠ evidence of absence | Report power; use CI to bound the effect |
| **OR instead of RR** | Reporting OR when cohort design allows RR | Use RR; if OR reported, note prevalence |
| **HR misread as prevalence ratio** | "HR = 2.5" interpreted as "2.5× more common" | HR is a rate ratio, not a risk ratio |
| **Subgroup hunting** | Testing many subgroups post-hoc | Pre-specify subgroups; apply Bonferroni |
| **Correlation ≠ causation** | Cross-sectional association stated as causal | Use temporal language; cite confounders |
| **Immortal time bias** | Retrospective loading-timing studies: delay from placement to loading creates "immortal" period counted as delay exposure | Landmark analysis or Cox with time-varying covariate |
| **Mediator over-adjustment** | Adjusting for a variable on the causal pathway | Distinguish confounder vs mediator before modelling |

> **🦷 오류별 실전 예시**
>
> **① p > 0.05 = "효과 없음" 오류**
> - 논문: "즉시식립 vs 지연식립 MBL 차이: p=0.12, 유의한 차이 없음"
> - 실제 문제: n=20 소규모 → 검정력 60%에 불과. "효과 없다"가 아니라 "찾을 힘이 없었다."
> - 올바른 표현: "현재 표본으로는 차이를 확인할 수 없었다(underpowered)."
>
> **② Subgroup Hunting (데이터 낚시)**
> - 연구: RCT에서 전체 결과 p=0.3. 사후 분석으로 20개 subgroup 테스트 → 상악 전치부만 p=0.04!
> - 문제: 20번 테스트 시 우연히 1번은 p<0.05가 나올 수 있음 (1종 오류 축적)
> - 올바른 대응: Bonferroni 보정 (p<0.05/20=0.0025 기준 사용)
>
> **③ Immortal Time Bias — 임플란트 부하 시기 연구**
> - 설계: 즉시부하군(식립 당일 부하) vs 지연부하군(3개월 후 부하)을 후향적으로 비교
> - 문제: 지연부하군은 0~3개월 동안 부하가 없었으므로 "그 기간엔 실패할 수가 없음" → 이 기간이 "불멸 시간(immortal time)"으로 지연군에 인위적 생존 이점 부여 → HR 과소추정
> - 올바른 대응: 부하 시점을 time-zero로 설정 (landmark analysis)
>
> **④ 교란변수 vs 매개변수 혼동**
> - 연구: 당뇨 → 임플란트 실패. 골밀도를 보정 변수에 포함.
> - 문제: 당뇨가 골밀도를 낮추고 → 골밀도 감소가 실패를 유발한다면, 골밀도는 **매개변수(mediator)**. 이를 보정하면 당뇨의 실제 효과를 "지워버림" (over-adjustment).
> - 올바른 대응: 인과 경로도(DAG, Directed Acyclic Graph) 먼저 그리고 교란변수 vs 매개변수 구분.

---

## 10. Quick Decision Tree — "어떤 지표를 쓸까?"

```
논문을 읽을 때
    │
    ├─ 결과가 이분형(사망/생존, 실패/성공)?
    │       │
    │       ├─ 시간 정보 있음(생존 기간) → HR (Cox, KM)
    │       │
    │       └─ 시간 정보 없음
    │               │
    │               ├─ Case-Control 디자인 → OR만 가능
    │               └─ Cohort/RCT 디자인 → RR 권장 (OR도 가능하나 과대추정 주의)
    │
    └─ 결과가 연속형(ISQ, MBL, mm)?
            │
            ├─ 단위 같음 → MD
            └─ 단위 다름 (메타분석) → SMD
```

---

## 11. Cross-Reference

See [[evidence-appraisal-toolkit]] for the appraisal checklist (I², PRISMA, confidence tag workflow, study-type reading order: RCT → abstract last; SR → forest plot first).
