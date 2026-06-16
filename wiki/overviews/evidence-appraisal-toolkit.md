---
title: "Evidence Appraisal Toolkit for the Clinical Dentist"
authors: synthesis (llm-wiki)
year: 2026
date: 2026-05-22
doi: null
source: synthesis
category: overviews
confidence: synthesis
tags: [evidence-appraisal, ebm, ebd, biostatistics, sr-ma-methodology, critical-appraisal, overview]
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 핵심 목적: 임상 치과의사가 체계적문헌고찰+메타분석 (Systematic Review + Meta-Analysis, SR+MA)·무작위대조시험 (Randomized Controlled Trial, RCT)·관찰연구를 비판적으로 읽기 위한 5축(SR/MA 방법론·효과측정치·검정 선택·약자 빠른참조·흔한 오류) 도구상자다.
> - 동기: wiki의 800+ 임상 paper 대부분이 SR+MA/RCT/후향 코호트이므로, 그 결론을 무비판 인용하지 않는 living-document 원칙의 운영적 backbone.
> - 축 1 핵심 룰: 이질성 I²<25%면 pooling 의미 있음, I²>75%면 pooled effect는 거의 무의미해 subgroup·메타회귀로 가야 한다.
> - 출판편향: funnel plot 비대칭 + Egger p<0.10이면 출판편향(소규모연구 효과) 의심 — SR이 PROSPERO 등록·a priori PICO·독립 reviewer 2인을 다 갖췄다고 가정 말고 Methods를 직접 확인.
> - 축 2 효과측정치 → 디자인 매핑: RCT(binary)는 상대위험 (Relative Risk, RR)·절대위험감소 (Absolute Risk Reduction, ARR)·치료필요수 (Number Needed to Treat, NNT), time-to-event는 위험비 (Hazard Ratio, HR)·Kaplan-Meier, 환자-대조군은 교차비 (Odds Ratio, OR)만 가능.
> - 환자 상담 룰: OR/HR 효과는 ARR 또는 NNT로 변환해 설명 — "실패위험 HR 2.5"가 아니라 "흡연자 100명당 약 7명 더 실패".
> - 축 3 검정 선택: 연속+2군 독립은 t-test/Mann-Whitney, paired는 paired t/Wilcoxon, ≥3군은 ANOVA/Kruskal-Wallis, binary 2×2는 chi-square/Fisher, time-to-event는 log-rank — 치과 최빈 미스는 한 환자의 양측 임플란트를 독립표본처럼 t-test로 비교(paired·mixed model 필요).
> - 축 5 흔한 오류 7가지: p>0.05를 "효과 없음"으로 해석, HR을 예후 정확도로 오해, subgroup hunting, 상관≠인과, 교란변수vs매개변수 혼동(over-adjustment), 연속변수 조기 이분화, 불멸시간편향(immortal time bias, 조기부하 vs 지연부하 후향비교).
> - 임상 체크리스트: confidence tag → I² → PRISMA/a priori protocol → 효과측정치가 맥락에 맞나 → CI를 점추정치와 함께 → subgroup이 pre-specified인가 → adjusted model에 매개변수가 들어가 있지 않은가 순.
> - 카테고리 신설 근거: 9편 모두 EBM·biostatistics 방법론 paper로 기존 23 카테고리(method/procedure 기반)에 안 맞아, 비판적 평가 자체를 method로 보고 evidence-appraisal 신설.
> - Caveat: 외부 9편 중 7편이 narrative-review/tutorial이라 individual confidence는 낮으나 다루는 원리는 Cochrane Handbook·BMJ Best Practice 표준에 합치 — 실전 사례로 Insadol 한국 임상시험 통계 타당성 비판(Choi 2015)이 "표준 처방 ≠ 근거 충분"을 시연한다.

## 한줄요약
임상 치과의사가 SR+MA·RCT·observational 연구를 비판적으로 읽기 위해 알아야 할 통계·방법론을 10편 (한국어 2편·영어 6편·익명 worksheet 1편·내부 synthesis cheatsheet 1편)에서 5축 (SR/MA 방법론·효과측정치·검정 선택·흔한 오류·약자 빠른 참조)으로 통합한 toolkit.

## 왜 이 overview인가
llm-wiki의 800+ 임상 paper 대부분이 SR+MA / RCT / retrospective cohort. 이 페이지들의 결론을 비판 없이 인용하면 안 된다는 게 우리의 wiki-living-document 원칙(memory file). 이 overview는 그 비판의 도구상자다.

9편 모두 narrative-review/educational tutorial이라 individual confidence는 낮지만, 4축으로 묶었을 때 임상 통계 reading의 standard reference 역할.

## 5축 구조

### 축 1 — SR/MA 방법론 (어떻게 종합되는가)
- [[evidence-appraisal/shin-ih-2009-meta-analysis-critical-interpretation]] — 한국어 강의, MA 개념·전제·heterogeneity·publication bias 입문.
- [[evidence-appraisal/shin-wj-2015-systematic-review-meta-analysis-introduction]] — 한국어 저널 paper, SR/MA full pipeline (PRISMA 2009 기준): 검색·선정·질평가·effect size·I²·고정/랜덤·funnel/Egger.
- [[evidence-appraisal/kiriakou-2014-evidence-based-dentistry-skills-interpret]] — 치과의사 대상 EBD 5단계 + RCT/SR critical appraisal.
- [[evidence-appraisal/anonymous-nd-systematic-review-critical-appraisal-worksheet]] — 4쪽 SR 체크리스트 (출처 미상, 인용 불가, 학습용).

**핵심 룰**:
- I² < 25%: pooling 의미 있음. I² > 75%: pooled effect는 거의 무의미, subgroup·meta-regression으로 가야 한다.
- funnel plot 비대칭 + Egger p<0.10 → publication bias 의심, small-study effect.
- SR이 한 편 있다고 PROSPERO 등록 / a priori PICO / 독립 reviewer 2인 / 위험편향평가가 다 있다고 가정하지 말 것. Methods 섹션을 직접 확인.

### 축 2 — 효과측정치 (숫자가 무엇을 말하는가)
- [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]] — p-value, 95% CI, NNT.
- [[evidence-appraisal/monaghan-2021-odds-ratios-relative-risk-absolute]] — OR, RR, AR, NNT.
- [[evidence-appraisal/barraclough-2011-hazard-ratios-clinicians-biostatistics-primer]] — HR, KM curve, proportional hazards.

**연구 디자인 → 적절한 측정치**:

| 디자인 | 자연스러운 측정치 | 주의 |
|---|---|---|
| RCT (binary outcome) | RR, ARR, NNT | OR도 사용되지만 baseline risk > 10%면 OR이 RR 과대평가 |
| RCT (continuous outcome) | mean difference (MD), SMD | unit이 다를 때만 SMD |
| Cohort (binary, fixed follow-up) | RR, ARR, NNT | |
| Cohort (time-to-event) | HR, KM survival, RMST | PH 가정 위반 시 HR 단독 해석 금지 |
| Case-control | OR | RR/AR 직접 추정 불가 |
| Cross-sectional (prevalence) | PR, OR | 인과 추론 약함 |

**환자 상담 룰**: OR/HR로 보고된 효과는 절대위험감소 (ARR) 또는 NNT로 변환해서 설명. "임플란트 실패 위험 HR 2.5"가 아니라 "100명 흡연자 임플란트 식립 시 비흡연자보다 약 7명 더 실패".

### 축 3 — 검정 선택 (어느 test가 옳은가)
- [[evidence-appraisal/nam-2012-statistical-methods-medical-studies]] — 한국어 검정 선택 flowchart.

**flowchart 요약**:
- 종속변수 연속 + 두 군 독립 → t-test (정규분포) / Mann-Whitney U (비모수).
- 종속변수 연속 + 두 군 paired → paired t-test / Wilcoxon signed-rank.
- 종속변수 연속 + 3군 이상 → ANOVA (one-way / repeated measures) / Kruskal-Wallis.
- 종속변수 binary + 2×2 → chi-square / Fisher's exact (기대빈도 <5).
- 종속변수 binary + paired → McNemar.
- 종속변수 time-to-event + 2군 비교 → log-rank.
- 다변수 보정 → linear (continuous) / logistic (binary) / Cox (time-to-event) regression.

치과 retrospective 자료에서 가장 흔한 미스: 같은 환자의 양측 implant를 독립 표본처럼 t-test로 비교 (paired 또는 mixed model 필요).

### 축 4 — 빠른 참조 (약자·정의 사전)
- [[overviews/statistical-abbreviations-cheatsheet]] — 2026-05-23 신설 synthesis cheatsheet: descriptive·inferential·effect size·diagnostic accuracy·meta-analysis·regression·survival·agreement·trial set 9개 카테고리 약자 + 5대 오용 패턴(OR↔RR, p<0.05=임상유의, CI 폭, SD↔SE, ITT↔PP).

**용도 분기**:
- 축 1~3·5의 paper들이 *왜 그렇게 작동하는가*를 설명한다면, cheatsheet는 paper를 읽다가 막힌 약자를 *지금 즉시* 찾기 위한 인덱스.
- ISQ 측정 reliability(Bland-Altman·ICC), 임플란트 생존(HR·KM·log-rank), EAL 진단 정확도(Sn·Sp·LR+) 같은 도메인별 빈출 약자가 카테고리화되어 있어 wiki 다른 페이지에서 wikilink로 즉시 진입 가능.
- GRADE·PRISMA 2020·RoB 2·ROBINS-I 항목 포함 — 기존 toolkit이 본격 다루지 않던 post-2015 평가 도구를 부분적으로 메움.

### 축 5 — 흔한 오류 (논문이 거짓말하는 방식)
- [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]] — 10대 biostatistics 오류, 2024년 현재 정리판.

**치과 paper에서 자주 보이는 오류 7가지**:
1. **p > 0.05를 "효과 없음"으로 해석** — power가 약해서 못 잡았을 가능성 무시.
2. **HR을 예후 정확도로 오해** — HR은 두 군의 비교이지, 어느 환자가 실패할지를 알려주지 않는다.
3. **Subgroup hunting** — pre-specified가 아닌 subgroup 유의성은 hypothesis-generating일 뿐.
4. **상관 ≠ 인과** — retrospective cohort에서 시간 역전·confounding 확인.
5. **Confounder vs mediator 혼동** — 흡연-임플란트 연구에서 "plaque level로 보정"하면 흡연의 진참 효과가 약하게 추정됨 (over-adjustment).
6. **변수 조기 dichotomization** — ISQ 70 cutoff처럼 연속 변수를 binary로 자르면 information 손실.
7. **Immortal time bias** — "조기 부하군 vs 지연 부하군" retrospective 비교에서 조기 부하 전에 실패한 환자가 잘못 분류됨.

## 임상 적용 — wiki 다른 페이지를 읽을 때 체크리스트

이 wiki에서 SR+MA 페이지를 열면 다음 순서로 점검:

1. **Confidence tag** (frontmatter): sr+ma > rct > prospective > retrospective > case-report. 단 sr+ma도 I²·publication bias로 무효화 가능.
2. **I²** (Methods/Results): >75%면 pooled effect 신뢰 보류.
3. **PRISMA 등록 / a priori protocol** 여부.
4. **효과측정치가 맥락과 맞나** (binary outcome RCT인데 HR 보고 → 의심).
5. **CI를 점추정치와 함께 봤나** (p-value만 보지 말 것).
6. **Subgroup 결과는 pre-specified인가**.
7. **Adjusted model에 mediator가 들어가 있지 않은가**.

## 카테고리 신설 근거
9편(외부 paper) 모두 임상 치의학 데이터가 아닌 EBM·biostatistics 방법론 paper. 기존 23개 카테고리 (implants, endodontics, periodontics 등 method/procedure 기반) 어느 곳에도 자연스럽게 들어가지 않음. **CLAUDE.md "Classify by method/procedure" 원칙**에 따라 비판적 평가 자체를 하나의 method로 보고 `evidence-appraisal` 신설. 2026-05-23 추가된 cheatsheet는 동일 카테고리 안의 내부 synthesis page (PDF 없음).

## Caveats
- 외부 paper 9편 중 7편이 narrative-review/educational tutorial. confidence 자체는 sr+ma·RCT 대비 낮음. methodology paper에는 elide할 수 있는 등급. 다만 이들이 다루는 원리 자체는 Cochrane Handbook·BMJ Best Practice 표준에 합치.
- PRISMA 2020·GRADE·AMSTAR 2·RoB 2·ROBINS-I 등 최신 (post-2015) 평가 도구는 D'Arrigo 2024와 cheatsheet에 항목으로만 등장. 본격 ingest 권장 (예: Page 2021 PRISMA 2020 statement, Sterne 2019 RoB 2, Schünemann GRADE handbook).
- cheatsheet는 표준 biostatistics reference에서 추출한 synthesis로, 자체적으로 원문 citation을 보유하지 않음. 동일 정의의 일차 출처가 필요하면 축 1~5의 paper로 역참조.

## Related (cross-category)
- 본 toolkit은 `implants/`, `bone-regeneration/`, `endodontics/`, `sinus-lift/` 등 모든 SR+MA / RCT / cohort 페이지를 읽는 데 기본 도구로 적용.
- `wiki-living-document` 원칙(memory file): 임상 페이지를 무비판적으로 옮기지 않는 원칙의 운영적 backbone.

## Additional Spokes — 실제 임상 데이터 비판적 평가 사례 (2026-05-26 추가)

본 toolkit이 실전에서 어떻게 작동하는지 보여주는 case-level appraisal:

| Spine paper | Evidence | Key finding |
|---|---|---|
| [[evidence-appraisal/choi-2015-statistical-validity-insadol-clinical-effectiveness]] | critical methodological appraisal | **Insadol(옥수수 불검화 정량추출물 = titrated unsaponifiable Zea mays L. fraction)** 한국 임상시험 5편(4편 분석가능) 통계 타당성 비판 — 한국 의료계의 표준 사용 vs 통계적 근거 부족 |

**임상 함의**: 한국 시장에서 광범위 사용되는 약물도 통계적 평가는 별개. 본 paper는 한국 임상 의사가 "그냥 처방되는" 약물 근거 검증의 실제 사례. [근거강함]

**오판 패턴**: "한국에서 표준 처방 → 근거 있음" — Choi 2015는 표준 처방과 근거 충분이 별개임을 시연. EBM 원칙 적용은 한국 의료에서도 동일. [근거강함]

## Related Papers

### 신규 추가 (2026-06)

- [[evidence-appraisal/al-abedalla-2022-unusual-findings-trials-evaluating-adjuncts]] — Methodological quality assessment (CONSORT + trial-registration audit) of 32 RCTs on SRP adjuncts published 2010–2017 by a single research group (GDCR … (sr, 2022)
- [[evidence-appraisal/singh-2026-is-your-research-statistically-significant]] — Editorial (J Conserv Dent Endod) arguing that statistical significance does not equal clinical significance … (narrative-review, 2026)
