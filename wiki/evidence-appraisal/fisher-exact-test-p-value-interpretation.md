---
title: "통계 렌즈 — 피셔 정확검정의 p값 해석 (Fisher's exact test: what p = 0.05 means)"
authors: synthesis (llm-wiki)
year: 2026
date: 2026-10-11
doi: null
source: synthesis
category: evidence-appraisal
evidence_level: synthesis
tags: [biostatistics, fisher-exact-test, p-value, 2x2-table, exact-test, statistical-significance, significance-threshold, critical-appraisal, case-based-stats]
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 목적: 2×2 분할표에서 피셔 정확검정 (Fisher's exact test)을 쓸 때 **p = 0.05가 정확히 무엇을 뜻하는지**, 그리고 치과 논문의 실제 2×2 표에서 어떻게 읽어야 하는지를 정리한 개념 렌즈.
> - p의 정의: 귀무가설 H₀(두 변수 무관) 참 + **주변합(marginal totals) 고정** 조건에서, 관측표와 **같거나 더 극단적인 표가 나올 조건부 확률**. 즉 Pr(관측표만큼 극단 | H₀) ≠ Pr(H₀ | 데이터) ≠ "우연일 확률".
> - "정확(exact)"의 뜻: 초기하분포 (hypergeometric distribution)로 근사 없이 계산 → 표본이 작거나 **기대빈도 < 5인 칸**이 있을 때 카이제곱 대신 사용 ([[evidence-appraisal/nam-2012-statistical-methods-medical-studies]], [[overviews/evidence-appraisal-toolkit]] 축 3).
> - p = 0.05는 자연법칙이 아니라 피셔가 제안한 **관례(20번 중 1번)**; 정확검정의 p는 **이산값(discrete)**이라 문턱 근처 값(0.049 vs 0.051)은 사실상 같은 증거 강도.
> - p > 0.05는 "효과 없음"이 아니고(absence of evidence ≠ evidence of absence), p < 0.05는 "임상적으로 중요"를 뜻하지 않는다 — 효과크기·95% 신뢰구간 (CI)과 함께 읽어야 한다 ([[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]], [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]], [[evidence-appraisal/singh-2026-is-your-research-statistically-significant]]).
> - 치과 실제예: 흡연자 임플란트 실패 3/10 vs 비흡연자 3/91의 피셔 양측 p ≈ 0.012 ([[implants/survival/de-bruyn-2025-survival-bone-remodeling-hybrid-surface]], ingester 계산) — p는 작지만 사건이 3건뿐이라 신뢰구간이 넓어 "방향성 신호"로만 읽어야 함.
> - Caveat: Fisher 정확검정의 **내부 역학(초기하·기대빈도 규칙·mid-p·Barnard)은 이 위키의 보유 논문이 다루지 않는다** — 표준 biostatistics 참조 수준의 배경지식이며, p값 *해석* 규칙만 보유 논문으로 뒷받침된다.

## Three-line Summary

Concept lens for reading a Fisher's exact test p-value in a 2×2 dental table: p is the conditional probability, **given the fixed marginal totals and no association (H₀)**, of a table at least as extreme as the observed one — not the probability the null is true, and not the probability the result is "due to chance."

"Exact" means the hypergeometric distribution is used instead of the chi-square approximation, so Fisher's test is the choice when any expected cell count is < 5; p = 0.05 is Fisher's own 1-in-20 convention, and because exact p-values are discrete and the two-sided version is conservative, a threshold-adjacent p is weak evidence.

The interpretation rules are grounded in held papers (p-value/CI: [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]], [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]], [[evidence-appraisal/singh-2026-is-your-research-statistically-significant]]; test selection: [[evidence-appraisal/nam-2012-statistical-methods-medical-studies]]), and the worked 2×2 examples come from this wiki's own pages (de Bruyn 2025 smoker failures 3/10 vs 3/91, p ≈ 0.012; Santana-Mora 2021 chewing-side = pain-side, Fisher p = 0.002).

## 세줄요약

2×2 분할표에서 피셔 정확검정의 p값을 읽는 개념 렌즈: p는 **주변합 고정 + 귀무가설(무관) 하에서** 관측표와 같거나 더 극단적인 표가 나올 **조건부 확률**이지, 귀무가설이 참일 확률도 "우연일 확률"도 아니다.

"정확"이란 카이제곱 근사 대신 초기하분포를 쓴다는 뜻 → **기대빈도 < 5인 칸**이 있으면 피셔를 쓴다; p = 0.05는 피셔의 20분의 1 관례일 뿐이고, 정확검정 p는 이산값이라 양측검정이 보수적이어서 문턱 근처 p는 약한 증거다.

해석 규칙은 보유 논문으로 뒷받침되고(p값·CI: flechner 2011·darrigo 2024·singh 2026; 검정 선택: nam 2012), 실제 2×2 예시는 이 위키 자체 페이지에서 가져왔다(de Bruyn 2025 흡연자 실패 3/10 vs 3/91, p ≈ 0.012; Santana-Mora 2021 습관저작측=통증측, Fisher p = 0.002).

## 왜 이 페이지인가

이 위키의 치과 논문 상당수(후향 코호트·교차연구·RCT의 baseline 표·부작용 표)가 **2×2 이진 결과 × 이진 노출**을 다루고, 소표본에서는 카이제곱 대신 **피셔 정확검정**을 보고한다 [확인] — 예: [[implants/survival/cobo-vazquez-2018-effect-lack-primary-stability-survival]], [[cracked-tooth/zhang-2026-clinical-characteristics-prognostic-factors-cracked]], [[tmj/santana-mora-2021-asymmetry-chewing-chronic-tmd]]. 그런데 toolkit 축 3은 "binary 2×2 → chi-square / Fisher's exact (기대빈도 <5)" 한 줄만 주고, **그 p값을 어떻게 읽는지**는 다루지 않는다 [확인]. 이 페이지는 그 빈틈을 메우는 spoke다.

## 1. Fisher's exact test가 계산하는 것

- **설계**: 결과(이진) × 노출/군(이진)의 2×2 분할표. 행·열 **주변합을 고정**한 채, 귀무가설(두 변수 독립 = 차이 없음) 하에서 각 칸이 가질 수 있는 값을 **초기하분포(hypergeometric distribution)** 로 계산한다.
- **p값**: 관측표 **및 그보다 더 극단적인 모든 표**의 확률을 더한 값이다. 근사가 아니라 정확 계산이므로 이름이 "exact"다.
- **언제 쓰나**: 카이제곱 검정의 근사는 기대빈도가 작으면 깨진다. 관례적으로 **기대빈도 < 5인 칸이 있으면** 피셔를 쓴다 [확인] — 근거: [[evidence-appraisal/nam-2012-statistical-methods-medical-studies]], [[overviews/evidence-appraisal-toolkit]] 축 3.

> [!note] 배경지식 경계
> 위 초기하분포·주변합 고정·기대빈도 규칙은 **표준 biostatistics 교과서 수준**이며, 이 위키의 보유 논문이 본격적으로 설명하는 내용이 **아니다** [미검증]. 보유 논문이 뒷받침하는 것은 *어떻게 읽는가*(§2–§3)와 *언제 쓰는가*(축 3의 한 줄)뿐이다.

## 2. p = 0.05의 정확한 문장

$$\Pr(\text{관측표만큼 극단적인 표} \mid H_0\ \text{참, 주변합 고정}) = 0.05$$

- **H₀ 조건부** 확률이다. "$H_0$가 참일 확률 5%"가 아니다. "결과가 우연히 나올 확률"이라는 표현도 틀렸다 [확인] — [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]], [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]].
- **이산값**: 표본이 작으면 나올 수 있는 p값이 띄엄띄엄 정해져 있어 0.0500이 아니라 0.0115·0.0487·0.0712처럼 튄다.
- **문턱의 정체**: 0.05는 피셔가 제안한 관례("20번 중 1번")이지 자연법칙이 아니다 [확인] — [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]]. 그러므로 **p = 0.049 vs 0.051은 사실상 같은 증거 강도**이고, 문턱 옆 값으로 결론을 뒤집는 것은 위험하다.

## 3. p = 0.05가 **아닌** 것 다섯 가지 [확인]

| 흔한 오독 | 실제 |
|---|---|
| "$H_0$가 참일 확률이 5%" | 아니다. p는 **H₀를 조건으로 한** 데이터의 확률이다 — 방향이 반대다. |
| "결과가 우연일 확률 5%" | 아니다. 우연/비우연의 확률화는 베이즈적 사후확률이며 p가 아니다. |
| "p > 0.05 → 효과 없음" | 아니다. 저검력 연구의 비유의는 *absence of evidence*, *evidence of absence*가 아니다 — [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]], [[evidence-appraisal/singh-2026-is-your-research-statistically-significant]]. |
| "p < 0.05 → 임상적으로 중요" | 아니다. 대표본에서는 임상적으로 사소한 차이도 p < 0.05가 된다 — [[evidence-appraisal/singh-2026-is-your-research-statistically-significant]], [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]]. |
| "p가 효과 크기를 말해준다" | 아니다. p는 효과크기·정밀도를 모두 버린 단일 숫자다. 2×2에서는 **교차비(Odds Ratio, OR) 또는 상대위험(Relative Risk, RR) + 95% CI**를 함께 본다 — [[evidence-appraisal/monaghan-2021-odds-ratios-relative-risk-absolute]]. |

## 4. "정확"이 "안전"을 뜻하지는 않는다

- **양측 피셔는 보수적(conservative)**: 두-sided p가 실제 유의수준보다 크게 나오는 경향이 있어 검정력이 떨어진다 — 참 효과가 있어도 p가 문턱을 넘을 수 있다 [미검증].
- **단측 vs 양측**: 같은 표에서도 단측 p가 훨씬 작다. 저자가 분석 방향을 사후에 정했다면 그 자체가 문제다 (이건 p값 해석 규칙의 일부 — [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]]의 subgroup·다중검정 항목과 같은 계열).
- **대안**: 보수성을 줄이려 **mid-p** 또는 **Barnard's test**를 쓰기도 한다. 다만 어떤 방법을 썼는지가 저자마다 다르므로, 두 논문의 p를 직접 비교할 때는 검정 방법부터 맞춰야 한다 [미검증].
- **한 줄 결론**: 검정 방법(카이제곱 vs 피셔 vs mid-p)·측(단측/양측)이 다르면 **p는 직접 비교 가능한 절대 척도가 아니다.** 이 점은 위키가 이미 강조하는 "효과크기 + CI 우선" 원칙과 같은 방향이다 [확인].

## 5. 치과 실제 2×2 예시 (이 위키 자체 페이지에서)

### 예시 A — 흡연과 초기 임플란트 실패 ([[implants/survival/de-bruyn-2025-survival-bone-remodeling-hybrid-surface]])

| | 부하 전 실패 | 성공 | 합계 |
|---|---|---|---|
| 흡연자 | 3 | 7 | **10** |
| 비흡연자 | 3 | 88 | **91** |
| 합계 | **6** | **95** | **101** |

- **주변합 고정 + 초기하분포**로 계산한 피셔 양측 p ≈ **0.012** (ingester 계산, 저자들은 이 비교를 검정하지 않음) [확인].
- **왜 피셔인가**: 기대빈도가 흡연자-실패 칸 **0.59**, 비흡연자-실패 칸 **5.41**로 < 5 → 카이제곱 근사 부적합 [확인: 직접 계산].
- **p를 어떻게 읽나**: p는 작지만 **사건이 총 3건**뿐이라 95% CI가 매우 넓다. 따라서 "흡연자 실패위험이 10배"로 인용하면 안 되고, **방향성 신호**로만 읽는다 [확인] — 같은 페이지가 "3 events의 넓은 불확실성을 감안하라"고 명시.

### 예시 B — 습관저작측 = 통증측 ([[tmj/santana-mora-2021-asymmetry-chewing-chronic-tmd]])

- 만성 편측 TMD 24명 중 **17명**에서 습관저작측이 통증측과 일치, **피셔 p = 0.002** (Kappa 0.767, risk estimate 4.5) [확인].
- 교훈: 피셔 p는 소표본 **일치도/동반성**을 보일 때도 쓰인다. 이때도 p = 0.002가 "인과"나 "진단 정확도"를 뜻하지 않는다 — 저자들 스스로 CP/LG 기록이 TMD 단독 선별검사로는 부적합하다고 못 박는다 [확인].

### 그 밖의 위키 사용례 (검정 선택 확인용)
- [[implants/survival/cobo-vazquez-2018-effect-lack-primary-stability-survival]] — 기대빈도 문제로 Fisher exact / chi-square 병용 [확인].
- [[cracked-tooth/zhang-2026-clinical-characteristics-prognostic-factors-cracked]] — 이변량 단계에서 Chi-square / Fisher's exact [확인].
- [[tmj/santana-mora-2021-asymmetry-chewing-chronic-tmd]] — Fisher exact · χ² · Kappa 병용 [확인].

## 6. 피셔 2×2를 읽는 체크리스트

1. **표를 손에 들고** 읽는다 — p만 보고 판단하지 않는다 (칸 수·주변합이 해석을 좌우).
2. **기대빈도 < 5 + 피셔**인가, 아니면 카이제곱인가. 두 논문의 p를 비교하려면 검정을 맞춘다.
3. **단측/양측**을 확인한다. 문턱 근처(0.04–0.08)는 결론을 유보한다.
4. **사건 수**를 센다. 사건이 한 자릿수면 p가 작아도 CI가 넓다 → 방향성만 취한다.
5. **OR/RR + 95% CI**를 붙여 읽는다 — [[evidence-appraisal/monaghan-2021-odds-ratios-relative-risk-absolute]] (연관이 흔하면 OR가 RR을 과대평가).
6. **문턱 이분법을 버린다** — 통계적 유의 ≠ 임상적 유의, p > 0.05 ≠ 효과 없음 [[evidence-appraisal/singh-2026-is-your-research-statistically-significant]].

## Caveats

- 이 페이지는 **내부 synthesis**다(`source: synthesis`, PDF 없음). p값 *해석* 규칙은 보유 논문으로 뒷받침되지만, **Fisher 정확검정의 내부 역학**(초기하분포 유도, 기대빈도 < 5 규칙의 정확한 출처, mid-p·Barnard 대안, 양측 정의의 두 관례)은 **이 위키의 보유 논문이 다루지 않는다** — 표준 biostatistics 참조 수준의 배경지식이며 해당 구간은 [미검증]으로 표기했다. `overviews/statistical-abbreviations-cheatsheet`와 같은 성격(자체 원문 인용 없음)이다.
- 예시 A의 피셔 p ≈ 0.012는 **저자가 보고한 값이 아니라 ingester가 계산한 값**이다(원 페이지 명시). 사건 수가 적어 수치 자체는 근사적 의미만 갖는다.
- p값을 **직접 비교 가능한 절대 척도**로 쓰지 말 것 — 검정 방법·측·다중비교 보정이 다르면 비교 불가.
- 최신 통계 개혁(효과크기·CI 우선, p값 폐기 논쟁, Bayesian 대안)은 다루지 않는다.

## Related Papers

- [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]] — p-value·95% CI·NNT를 같은 데이터의 세 렌즈로 설명. 이 페이지의 해석 규칙 1차 근거.
- [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]] — p > 0.05 오독·95% CI 오해·다중검정 등 10대 오류. 이 페이지 §3의 1차 근거.
- [[evidence-appraisal/singh-2026-is-your-research-statistically-significant]] — 통계적 유의 ≠ 임상적 유의(양방향). §3·§6 근거.
- [[evidence-appraisal/nam-2012-statistical-methods-medical-studies]] — 검정 선택 flowchart(2×2 → 카이제곱/Fisher). §1 근거.
- [[evidence-appraisal/monaghan-2021-odds-ratios-relative-risk-absolute]] — 2×2의 OR/RR/AR/NNT 네 렌즈 + OR-RR 발산 법칙.
- [[evidence-appraisal/barraclough-2011-hazard-ratios-clinicians-biostatistics-primer]] — time-to-event 짝(HR). 같은 읽기 원칙의 다른 자료형.
- [[evidence-appraisal/isq-survival-andersson-vs-roccuzzo-clustering-appraisal]] — 같은 폴더의 자매 개념 렌즈(군집·효과크기·event-per-variable). "사건 수가 적으면 방법이 좋아도 CI가 무의미해진다"를 실증.

## Related

- [[overviews/evidence-appraisal-toolkit]] — 축 3(검정 선택)의 spoke. 이 페이지는 그 한 줄을 p값 해석까지 확장한다.
- [[overviews/statistical-abbreviations-cheatsheet]] — 같은 성격의 참조형 synthesis(표준 참조 유래, 자체 인용 없음).
