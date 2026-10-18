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
> - **연구 디자인 피라미드**: SR+MA > RCT > 전향 코호트 > 후향 코호트 > 환자-대조군 > 횡단 > 증례군 > 전문가 의견. 지정 OR을 계산할 수 있는 디자인은 환자-대조군뿐.
> - **RCT 유형**: Double-blind, Crossover, Cluster, Non-inferiority, Equivalence, Factorial.
> - **SR vs MA 구분**: SR은 질적 종합(숫자 합산 없음), MA는 여기에 pooling 통계 추가. SR 없는 MA는 선택 편향 위험. **I²>75%이면 pooled 효과 추정치는 거의 무의미** — subgroup 분석으로 이질성 원인을 먼저 규명해야 함.
> - **GRADE**: High→Very Low 4단계. RCT=High에서 시작하나 비뚤림·비일관성·비직접성·비정밀성·출판편향이 있으면 강등. 관찰연구=Low에서 시작하나 대효과·용량-반응 관계면 승등 가능.
> - **임상 적용 3-step**: ① 연구 디자인 확인 → 어떤 효과측정치가 타당한지 판단. ② 점추정치+95% CI 동시 읽기(CI 폭=정밀도). ③ 상대 지표(OR/RR/HR)를 절대 지표(ARD/NNT)로 변환 후 환자 설명.

## Three-line Summary

Reference guide for the foundational concepts of clinical biostatistics — effect measures (OR, RR, HR), derived metrics (ARD, NNT, SMD), statistical tests, study design hierarchy, RCT subtypes, SR/MA methodology (I², pooling, GRADE), and a head-to-head comparison matrix — intended as a compact study aid for reading and presenting clinical research.

OR is calculated only from case-control designs; RR from cohort/RCT; HR from time-to-event analyses (Cox/Kaplan–Meier); all three share the same CI null at 1.0, but OR over-estimates RR when outcome prevalence exceeds ~10%.

Practical translation rule: always convert relative measures (OR/HR) to ARD or NNT before patient counseling — "HR 2.5 for smokers" is less actionable than "roughly 7 additional failures per 100 smoker-implants."

## 세줄요약

임상 바이오통계 핵심 개념 레퍼런스 — 효과측정치(OR·RR·HR), 파생 지표(ARD·NNT·SMD), 연구 디자인 계층, RCT 유형, SR+MA 방법론(I²·풀링·GRADE)을 한 페이지에 집약한 교육용 빠른 참조 가이드.

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

|  | Disease + | Disease − |
|---|---|---|
| **Exposed** | a | b |
| **Unexposed** | c | d |

- OR > 1 → exposure increases odds of disease
- OR < 1 → exposure is protective
- OR = 1 → no association

**When OR ≈ RR**: rare-disease assumption (prevalence < 5–10%). As prevalence rises, OR increasingly exceeds RR (relative over-estimation).

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

**Translation rule for patient counseling**:
> Convert OR/HR → ARD → NNT. Example: HR = 2.5 for smokers with implants with a 5-year failure baseline of 5% → ARD ≈ 7.5% → NNT(harm) ≈ 13. "One additional failure for every 13 smokers" is far more actionable than "HR 2.5."

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

### 5.2 I² Heterogeneity Interpretation

| I² range | Interpretation | Action |
|---|---|---|
| 0–25% | Low heterogeneity | Fixed-effects pooling reasonable |
| 25–50% | Moderate | Random-effects; explore sources |
| 50–75% | Substantial | Pooled estimate interpreted cautiously |
| > 75% | Considerable / high | Pooled estimate questionable; subgroup or meta-regression preferred |

### 5.3 Publication Bias Assessment

- **Funnel plot**: asymmetry suggests small-study effects (not always bias; also heterogeneity)
- **Egger's test**: statistical test for funnel asymmetry; p < 0.10 = suspect
- **PROSPERO registration + a priori PICO**: reduces outcome-reporting bias
- **Trim-and-fill**: imputes missing studies; visualises adjusted estimate

### 5.4 Quality Appraisal Tools

| Study type | Tool |
|---|---|
| SR+MA | AMSTAR-2 |
| RCT | Cochrane RoB 2.0 |
| Non-randomised studies | ROBINS-I |
| Diagnostic accuracy | QUADAS-2 |
| Reporting (RCT) | CONSORT |
| Reporting (SR) | PRISMA |

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

---

## 10. Cross-Reference

See [[evidence-appraisal-toolkit]] for the appraisal checklist (I², PRISMA, confidence tag workflow, study-type reading order: RCT → abstract last; SR → forest plot first).
