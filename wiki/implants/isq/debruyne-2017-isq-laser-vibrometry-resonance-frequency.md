---
title: "ISQ calculation evaluation of in vitro laser scanning vibrometry-captured resonance frequency"
authors: Stijn Debruyne, Nicolas Grognard, Gino Verleye, Korneel Van Massenhove, Dimitrios Mavreas, Bart Vande Vannet
year: 2017
date: 2017-09-28
doi: 10.1186/s40729-017-0105-3
source: debruyne-2017-isq-laser-vibrometry-resonance-frequency.md
category: [implants/isq]
confidence: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/debruyne-2017-isq-laser-vibrometry-resonance-frequency.pdf
pdf_filename: debruyne-2017-isq-laser-vibrometry-resonance-frequency.pdf
source_collection: external
tags: []
---

## One-line Summary

In-vitro bench study (20 resin-imbedded test implants across Straumann tissue-level, Ankylos, 3i Certain) that captured implant–Smartpeg resonance frequency by laser Doppler vibrometry and recomputed ISQ via the proprietary Osstell algorithm: indirect (LDV-derived) and direct (Osstell IDx) ISQ correlated at r = 0.99 with a clinically negligible mean difference, validating the Osstell ISQ-calculation algorithm.

## 한줄요약

시험관내(in-vitro) 벤치 연구 — 레진에 매립한 시험 임플란트 20개(스트라우만 조직수준·앵킬로스·3i Certain)에서 임플란트-Smartpeg 공명주파수(Resonance Frequency, RF)를 레이저 도플러 진동측정법(Laser Doppler Vibrometry, LDV)으로 독립 포착해 비공개 Osstell 알고리즘으로 ISQ를 역산한 결과, 기기 직접측정 ISQ와 r=0.99로 일치하고 평균차도 임상적으로 무시할 수준이어서 Osstell ISQ 산출 알고리즘의 타당성을 입증.

## Summary

임플란트 안정성 지수(Implant Stability Quotient, ISQ)는 공명주파수분석(Resonance Frequency Analysis, RFA)으로 측정한 RF를 Osstell의 비공개 4차 다항식 계수(a–e)에 넣어 산출한다. 이 변환 알고리즘 자체의 정확성은 그동안 독립적으로 검증된 적이 없었다.

본 연구는 임플란트를 폴리우레탄 레진에 매립해 주변골·골-임플란트 강성(stiffness) 두 요소를 일정하게 고정한 뒤, Osstell IDx로 Smartpeg를 전자기 자극하고 그 진동을 비접촉 LDV로 독립 포착했다. 고속푸리에변환(Fast Fourier Transformation, FFT) 자기스펙트럼(autospectrum)에서 최대 RF를 추출하여 동일한 Osstell 알고리즘으로 ISQ를 역산(indirect)한 뒤, 같은 위치에서 기기가 직접 표시한 ISQ(direct)와 비교했다.

결과적으로 두 ISQ는 Pearson r = 0.990 (p < 0.001)로 거의 완전 일치했고, 평균차는 통계적으로 0과 다르지 않았다(paired t p = 0.058; Wilcoxon p = 0.062; 초록 기준 평균차 ~0.09 ISQ). 이는 (1) Osstell의 ISQ 산출 알고리즘이 옳다는 점, (2) 이 벤치 플랫폼이 향후 임플란트-Smartpeg 복합체 강성 연구에 쓸 수 있다는 점을 보여준다. 임상적으로는 구형 유선 Osstell 기기의 ISQ가 (적어도 스트라우만 조직수준 SLA 임플란트에서) 편향·과소평가됨을 재확인하므로, 기기 세대가 다른 연구 간 ISQ 비교·메타분석에는 보정이 필요하다.

## Key Contributions

- **Osstell ISQ 알고리즘의 독립 검증.** RF를 완전히 독립적인 방법(LDV)으로 포착한 뒤 동일 알고리즘에 넣어 기기 출력과 비교 — RF→ISQ 변환 단계의 타당도(validity)를 처음으로 확인.
- **재현 가능한 RFA 벤치 플랫폼 구축.** 레진 매립 + Osstell 자극 + 비접촉 LDV 검출 + FFT 처리 조합으로, 임상에서 골 강성에 가려지는 임플란트-Smartpeg 복합체 강성을 분리 연구할 수 있는 도구 제시.
- **기기 세대 간 ISQ 편향 재확인.** 구형 유선 Osstell이 Mentor/IDx 대비 ISQ를 과소평가(임상 ~9 ISQ, 사체 ~10 ISQ 차이)함을 뒷받침 — 체계적 문헌고찰에서 ISQ pooling 시 보정 필요.

## Methodology

- **임플란트 3종:** 스트라우만 SLA 조직수준(RN 3.3×12, RN 3.3×4.1, WN 4.8×8), 앵킬로스 Cell Plus(4.5×8, 4.5×9.5), 3i Full Osseotite Tapered Certain(4.0×13).
- **매립:** Duromod B 이성분 폴리우레탄 레진, 바 형태 실리콘 몰드(16×2.5×3 cm), 바당 임플란트 5개. 완전 매립 = 완전 골유착 시뮬레이션.
- **Smartpeg:** 시스템별 Smartpeg를 8 Ncm로 조임(스트라우만 #04, 앵킬로스 #16, 3i #15).
- **간접(LDV):** Polytec PDV 100 레이저 진동계(λ=640 nm)를 Smartpeg 육각면에 조준 → Brüel & Kjær ADC → Pulse Labshop. 측정창 31.25 ms, FFT 0–12.58 kHz, 400 구간(32 Hz 해상도), 세션당 1000회 평균, 5회 반복 평균을 알고리즘 입력값으로 사용.
- **직접:** 동일 프로브 위치에서 Osstell IDx 표시 ISQ 판독.
- **측정 수:** 구성별 간접 25회 + 직접 5회.
- **통계(SPSS 22.0):** Shapiro-Wilk(정규성), paired t-test + Wilcoxon(일치), Pearson r(상관), α=0.05.

## Results

- **상관:** Pearson r = 0.990, p < 0.001 (초록: 검사 시스템 r = 0.99) — 매우 높은 선형관계.
- **일치:** 간접 ISQ가 평균 ~0.535 단위 높았으나 0과 유의차 없음(paired t = 2.018, df = 19, p = 0.058; Wilcoxon Z = 1.867, p = 0.062). 초록 보고 평균차 ~0.09 ISQ — 임상적으로 무시 가능.
- **분포:** 간접·직접 ISQ 모두 비정규(Shapiro-Wilk p = 0.05 / 0.02), 음의 왜도.
- **대표값(Table 2, 평균 간접 ISQ / 직접 ISQ):** 앵킬로스 4.5×9.5 ≈ 85–89 / 85–90; 스트라우만 3.3×12 ≈ 64.5–65.6 / 64–65; 스트라우만 4.1×10 ≈ 79.6–80.0 / 80; 스트라우만 4.8×8 ≈ 77.2–80.7 / 75–79. RF는 ~5.0 kHz(저-ISQ)–~8.6 kHz(고-ISQ) 범위.
- **결론:** Osstell ISQ 알고리즘은 정확하며 벤치법은 향후 임플란트-Smartpeg 강성 연구에 타당. 임상적으로는 구형 Osstell ISQ가 편향·과소평가됨을 입증하여 기기 간 ISQ 비교에 보정 필요.

## Related Papers

- [[implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability]] — extends: RFA의 수학적 모델링을 실험적으로 보강 (RF→ISQ 변환 알고리즘 정확성을 벤치에서 확증).
- [[implants/isq/herrero-climent-2013-osstell-isq-reliability-icc]] — reinforces: Osstell ISQ 신뢰도(reliability) 논의에 측정 변환 단계의 타당도(validity) 근거 추가.
