---
title: "통계 렌즈 — 임플란트 생존 코호트의 군집·효과크기 (andersson 2019 vs roccuzzo 2022)"
type: appraisal
date: 2026-06-14
category: [evidence-appraisal]
status: done
method_lens: ["뭘 했나", "왜 골랐나", "제대로 했나", "어떻게 읽나"]
tags: [biostatistics, clustering, multilevel-logistic, odds-ratio, confidence-interval, survival, dichotomization, multiplicity, implant-survival, case-based-stats]
---

## 개요
임플란트 생존 코호트를 통계 교보재로 읽는 재사용 렌즈(4단)와, 같은 설계 결함을 "못한 예 vs 잘한 예"로 대조한 케이스 노트. andersson 2019(745 임플란트/334명, 5년)는 군집 무시·비보정 OR·연속변수 이분화의 전형이고, roccuzzo 2022(172 임플란트/84명, 20년)는 동일한 군집 문제를 다수준 로지스틱으로 보정한 대조군이다. [claude해석]

## 재사용 렌즈 — 통계 요소마다 4단
1. **뭘 했나** — 기법 식별, 표/그림에서 정확히 어느 줄.
2. **왜 골랐나** — 전제·가정, 다른 선택지는 없었나.
3. **제대로 했나** — 가정 위반, 보고 누락(검정력·CI·이질성).
4. **어떻게 읽나** — 결과 해석과 과대해석 지점.

## 통계 요소 대조표

| 요소 | andersson 2019 (못한 예) | roccuzzo 2022 (잘한 예) |
|---|---|---|
| 단위·군집 | 745 임플란트를 독립 단위로 분석 (334명 ⊂ 무시) | 다수준 로지스틱으로 **환자 단위 군집 보정** |
| 회귀 | 없음 — 단변량 카이제곱·Fisher만 | crude + **adjusted** OR (연령·결손치·FMPS·FMBS 보정) |
| 생존 | actuarial CSR, CI 없음 | 생존율 overall/군별/SPC순응별, STROBE·등록 |
| 효과크기 | 비보정 OR, 연속 ISQ 4중 이분화(60/65/70/75) | 보정 OR, 사전지정 독립변수(흡연·SPC·치주력) |
| 탈락 | 6명 탈락 사실만 기재 | 39/123 탈락 사유·군간 균형 검토(Table S1) |
| 대표 OR | <75 로딩 OR 17.9 (2.3–142.9) | 비순응 PCP OR 14.59 (1.30–164.29) |

핵심 교훈: **두 논문 모두 대표 OR의 CI가 두 자릿수를 가로지른다.** roccuzzo가 군집·교란을 제대로 보정했어도 사건이 12개뿐이라 정밀도는 못 산다 — 즉 *방법을 잘해도 events-per-variable가 부족하면 효과크기는 신뢰 못 한다*. 반대로 andersson은 방법까지 부실해 방향성 외에는 인용 불가. [claude해석]

## 4단 렌즈 적용 — andersson 2019

**① 뭘 했나** actuarial CSR(Table 6); 카이제곱·Fisher(생존 연관, Table 9); Kruskal-Wallis·Mann-Whitney(ISQ 군간, Table 7–8); 역치별 비보정 OR(Table 10).
**② 왜 골랐나** 이분 결과에 OR이 직관적, ISQ를 임상 컷오프로 단순화. 비모수는 ISQ 정규성 불확실에 대한 보수적 선택. [합의수준]
**③ 제대로 했나** 군집 무시(SE 과소→CI 과좁·p 과소) [근거강함]; 다변량 보정 0(교란 미통제); 연속변수 4중 이분화(정보손실+다중성); OR 17.9의 CI 2.3–142.9는 희소셀 분리에 가까움; CSR에 CI 없음; 통계분석자 Neoss 고용(COI). [근거강함](본문 Disclosure)
**④ 어떻게 읽나** "ISQ<70이면 실패 위험 수 배↑" 방향까지만. "17.9배" 같은 점추정·유의성은 할인. 위키 요약이 "multivariate"로 오기됐던 항목 — 2026-06-14 교정함.

## 4단 렌즈 적용 — roccuzzo 2022

**① 뭘 했나** 군별 생존율(전체 93%; PHP 94.9%/mPCP 91.8%/sPCP 93.1%, p=.29); **다수준 로지스틱**으로 crude·adjusted OR(연령·결손치·FMPS·FMBS 보정); 연속/범주 비교는 정규성(Shapiro-Wilk)으로 모수/비모수 분기.
**② 왜 골랐나** 환자내 임플란트 상관을 인지해 다수준 채택 [근거강함](Methods 2.6); 군 연령차(p<.001) 때문에 연령 보정 필요.
**③ 제대로 했나** 군집·교란 보정·탈락 균형까지 모범적. 잔여 한계: 단일기관·단일술자, 20년에 39/123 탈락(생존자 편향 가능), 사건 12개로 adjusted OR CI 매우 넓음(1.30–164.29). [claude해석]
**④ 어떻게 읽나** "치주력 자체보다 **SPC 비순응**이 손실의 결정인자"가 본 메시지(순응 PCP는 PHP와 차이 없음, p>.05). OR 14.59의 크기는 신뢰 말고 "비순응 시 위험 크게↑, 정밀도 낮음"까지. [claude해석]

## 관련 항목
- [[implants/isq/andersson-2019-rfa-factors-5year-neoss-survival]] — 못한 예 (방법 교정 완료)
- [[periodontics/roccuzzo-2022-implants-periodontitis-history-20year-prospective]] — 잘한 예 (다수준 로지스틱)
- [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]] — 군집·다중성 흔한 오류
- [[evidence-appraisal/monaghan-2021-odds-ratios-relative-risk-absolute]] — OR 해석
- [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]] — CI·p 해석
- [[evidence-appraisal/barraclough-2011-hazard-ratios-clinicians-biostatistics-primer]] — 생존·HR 기초
