---
title: "Critical Appraisal Checklists for Dental Literature"
authors: synthesis (llm-wiki)
year: 2026
date: 2026-10-17
doi: null
source: synthesis
category: overviews
evidence_level: synthesis
tags: [evidence-appraisal, critical-appraisal, checklist, rct, cohort, case-control, sr-ma, consort, strobe, prisma, amstar, grade, overview]
relations:
  - target: "overviews/study-design-primer-dental-research"
    type: companion
  - target: "overviews/evidence-appraisal-toolkit"
    type: companion
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - **핵심 목적**: 치과 임상의가 논문을 읽을 때 디자인별로 빠르게 신뢰도를 판단하는 실전 체크리스트. 7개 질문이면 충분하다는 원칙.
> - **RCT 7문**: ①무작위배정 방법이 적절한가 ②배정은닉이 있는가 ③눈가림이 적절한가 ④추적소실 < 20%+이유 무작위 ⑤ITT 분석 ⑥비교군이 표준치료인가 ⑦스폰서·이해충돌 기재.
> - **관찰연구(코호트·환자-대조군) 7문**: ①교란변수 목록 + 다변량 보정 ②노출 정의·측정 시기가 명확한가 ③선택 기준이 결과와 독립 ④추적소실 처리 ⑤불멸시간 발생 가능한 설계인가 ⑥지시편향 가능성 ⑦결과 측정 눈가림.
> - **SR+MA 7문**: ①PROSPERO·a priori PICO ②2개 이상 데이터베이스·최근 2년 내 검색 ③2인 독립 스크리닝 ④RoB 평가 도구(RoB 2/ROBINS-I) ⑤I² 확인 + 이질성 탐색 ⑥GRADE 근거등급 ⑦funnel plot·Egger 출판편향.
> - **GRADE 4등급**: High(RCT, 비뚤림 없음) → Moderate → Low → Very Low. 관찰연구는 Low에서 시작. 등급은 올라가거나 내려갈 수 있다.
> - **치과 임플란트 SR+MA 최빈 결함**: ①이질성 I² > 50%인데 pooled HR을 conclusions에 단독 제시 ②검색일이 3–5년 전 ③스폰서 편향 미기재 ④개별 연구 RoB 없이 GRADE 없음.
> - **임상 적용 임계값**: RCT·SR+MA에서 ARR < 3% 이면 NNT > 33 — 임상적으로 "통계적 유의"해도 의미 없을 수 있음; 항상 절대 효과크기로 환산해 판단.

## Three-line Summary

Seven-question critical appraisal checklists for the four main dental study designs (RCT, prospective cohort, case-control/retrospective cohort, SR+MA), designed for bedside use with a 2–3 minute time budget per paper.

Each checklist maps to the corresponding reporting guideline (CONSORT / STROBE / PRISMA + AMSTAR-2) and flags the three most common deficits found in the dental implant and endodontic literature ingested in this wiki: immortal-time bias in retrospective loading-time comparisons, I²>75% pooled estimates presented without qualification, and sponsorship bias not disclosed.

Companion to [[overviews/study-design-primer-dental-research]] (design definitions and bias taxonomy) and [[overviews/evidence-appraisal-toolkit]] (statistics).

## 세줄요약

치과 논문 4대 설계(RCT·전향코호트·후향코호트·환자-대조군·SR+MA)별 7문항 체크리스트 — CONSORT·STROBE·PRISMA·AMSTAR-2 핵심 항목을 임상 독해 2–3분 예산에 맞게 압축.

각 체크리스트는 이 wiki에서 반복 발견된 결함 3종(불멸시간편향, I²>75% 풀링값 단독 제시, 스폰서 편향 미기재)을 red flag로 명시.

GRADE 4등급 판독 기준과 임상 임계값(ARR < 3% = NNT > 33 = 통계적 유의해도 임상적으로 무의미할 수 있음)을 마지막에 정리.

---

## 체크리스트 1 — RCT

> 논문 Methods·Results를 열면 순서대로 확인. ✅ = 통과 / ⚠ = 약점 / ❌ = 결함

| # | 질문 | 확인 포인트 | 결함 시 의미 |
|---|---|---|---|
| 1 | **무작위배정 방법이 적절한가?** | 컴퓨터 난수·봉투·블록무작위·층화무작위 중 명시 | 미명시 → 선택편향 가능성 |
| 2 | **배정은닉 (Allocation Concealment)?** | 중앙 무작위화·불투명봉투 등 | 미비 → RoB 2 High; 효과 과대평가 20–30% |
| 3 | **눈가림 (Blinding) 수준?** | 환자·술자·평가자 중 누가 맹검인지 명시 | 술자 맹검 불가 시 → 성과 편향 경고 |
| 4 | **추적소실 < 20% + 이유 무작위?** | CONSORT flow diagram 확인; 탈락 이유가 결과와 무관한가 | 관련 탈락 → attrition bias → ITT 분석 필수 |
| 5 | **ITT 분석?** | "intention-to-treat" 명시 여부 | PP만 보고 시 → 효과 과대평가 |
| 6 | **비교군이 진짜 표준치료?** | 대조군이 위약·무처치·기존 표준인가 | "active control"인데 열등한 치료 → 효과 부풀리기 |
| 7 | **이해충돌·스폰서 기재?** | Funding + COI 선언 | 스폰서 편향: 제조사 후원 RCT에서 자사 제품 우위 패턴 반복 확인 |

**RCT 속독 30초 팁**: ① CONSORT flow 그림 → 탈락 수 ② Methods "randomization" 키워드 ③ Results 첫 표 → baseline 두 군 균형 확인 (불균형이면 무작위화 실패 또는 보고 오류)

---

## 체크리스트 2 — Prospective Cohort (전향 코호트)

| # | 질문 | 확인 포인트 | 결함 시 의미 |
|---|---|---|---|
| 1 | **노출 정의·측정 시기가 명확한가?** | 노출 측정이 결과 발생 이전 확정 | 사후 노출 분류 → 분류 편향 |
| 2 | **교란변수 목록 + 다변량 보정?** | Cox 모델·로지스틱 회귀에 교란변수 포함 | 비보정 HR을 인과로 읽으면 안 됨 |
| 3 | **선택 기준이 결과와 독립?** | 등록 시점에 이미 결과가 발생하지 않았는가 | 유병군 혼입 → 선택편향 |
| 4 | **추적소실 < 20% + 무작위?** | 추적소실 이유 + MCAR 가정 | 관련 탈락 → 생존편향 |
| 5 | **추적기간이 결과 발생에 충분한가?** | 임플란트 생존 = 최소 1년, 이상적 5년+ | 추적 짧으면 후기 실패 놓침 |
| 6 | **결과 측정이 맹검?** | X-ray 판독자가 군 배정 모르는가 | 미맹검 → detection bias |
| 7 | **STROBE 준수?** | 설계 명시·flow diagram 있는가 | 미준수 시 보고 품질 낮음 |

---

## 체크리스트 3 — Retrospective Cohort / Case-Control (후향·환자-대조군)

> 이 두 설계는 결함 유형이 거의 동일 — 통합 체크리스트

| # | 질문 | 확인 포인트 | **⚠ 치과 최빈** |
|---|---|---|---|
| 1 | **불멸시간편향?** | 군 배정 기준 기간에 결과 발생이 가능했는가 | ⚠ **즉시부하 vs 지연부하 후향 비교** — 지연 기간이 즉시군에서 무위험으로 계산됨 |
| 2 | **교란변수 보정 목록?** | Cox 또는 로지스틱에 포함된 변수 목록 | ⚠ 전신질환·흡연·골질 미포함 시 결과 신뢰 불가 |
| 3 | **지시편향 (Indication Bias)?** | 군 배정이 임상 판단에 의해 결정됐는가 | ⚠ 건강한 환자에게만 즉시부하 → "즉시부하=더 성공"으로 오독 |
| 4 | **데이터 완결성 / 누락치 처리?** | 차트 완결율; MI·MICE 사용 여부 | 결측치 무시 시 완전관측 편향 |
| 5 | **Case 정의가 명확하고 재현 가능?** | 임플란트 실패 기준 (MBL > 2mm? 제거?) 통일됐는가 | 기준 혼용 시 결과 분류 오류 |
| 6 | **Control 선정이 Case와 독립?** | Control이 Case와 같은 base population | 병원-기반 control → 입원편향 |
| 7 | **단일 기관 + 단일 술자?** | 외적 타당도 제한 명시됐는가 | 결과 일반화 금지 |

**불멸시간편향 판별 2초 룰**: Methods에서 "군 배정 시점"과 "추적 시작 시점"이 다르면 의심. 즉시부하군의 추적 시작 = 수술일; 지연부하군의 추적 시작 = 부하 결정일이면 정의상 불멸시간 없음. 불멸시간이 있다면 두 군의 총 추적기간이 같더라도 위험에 노출된 기간이 다름.

---

## 체크리스트 4 — SR + MA

| # | 질문 | 확인 포인트 | 결함 시 의미 |
|---|---|---|---|
| 1 | **PROSPERO 등록 + a priori PICO?** | 등록번호 확인; Methods가 Results와 다르면 PROSPERO 원문 확인 | 미등록 = 선택적 보고 위험 |
| 2 | **검색: ≥2 DB + 최근 2년 내?** | MEDLINE + EMBASE 최소; 검색일자 확인 | 오래된 검색 = 신규 고품질 RCT 누락 |
| 3 | **2인 독립 스크리닝?** | inter-rater κ 또는 이견 해결 방법 명시 | 1인 선정 = 포함 편향 |
| 4 | **개별 연구 RoB 평가?** | RoB 2 (RCT), ROBINS-I (관찰연구) 사용 | 미평가 = GRADE 도출 불가 |
| 5 | **I² 확인 + 이질성 탐색?** | I² > 75% 시 pooled effect에 ⚠ 표시; subgroup·meta-regression | ⚠ **I²>75%인데 pooled HR만 결론에 제시 — 치과 SR 최빈 결함** |
| 6 | **GRADE 근거등급?** | High/Moderate/Low/Very Low; "근거 불충분" 결론 정직한가 | 없으면 임상 의사결정 적용 불가 |
| 7 | **출판편향 검사?** | funnel plot + Egger·Begg 검정; 연구수 < 10이면 funnel 신뢰 불가 | 비대칭 funnel → 소규모 연구 과대 효과 |

**SR+MA 속독 순서**: ① forest plot → pooled effect + I² ② GRADE 표 ③ 검색일자 ④ 개별 연구 sample size 분포 (1개 대형 연구가 pool을 지배하는지) ⑤ 결론이 GRADE와 일치하는가

---

## GRADE 근거등급 판독

| 등급 | 정의 | 시작점 | 내려가는 조건 | 올라가는 조건 |
|---|---|---|---|---|
| **High** | 참값에 가깝다 | RCT | 비뚤림·불일치·비직접성·불정밀·출판편향 중 심각한 것 | — |
| **Moderate** | 중간 신뢰 | — | 위 요인 중 1개 심각 | 관찰연구에서 강한 효과(RR>2) |
| **Low** | 참값과 상당히 다를 수 있음 | 관찰연구 | 위 요인 중 2개 | 용량-반응 관계 |
| **Very Low** | 매우 불확실 | 증례보고·전문가 의견 | 위 요인 중 3개+ | — |

> 치과 임플란트 SR 대부분 = Moderate–Low. "Moderate"를 "강한 근거"로 읽으면 안 된다.

---

## 임상 적용 임계값

| 상황 | 판단 기준 |
|---|---|
| RR 또는 HR만 보고 | ARR과 NNT로 변환 필수 (공식: ARR = 기저위험 × (1 − RR)) |
| ARR < 3% | NNT > 33 → 통계적 유의해도 임상적 이득 미미할 수 있음 |
| I² > 75% | 풀링된 점추정치(pooled estimate) 임상 적용 보류; 방향(direction)만 참고 |
| GRADE Very Low | 임상 의사결정 근거로 사용 금지; 추가 연구 대기 |
| 단일 RCT (n < 100) | 복제(replication) 없이 프로토콜 변경 금지 |
| 스폰서 = 제조사 + 단일 RCT | 독립 연구 복제 대기 후 임상 적용 |

---

## 관련 페이지

- [[overviews/study-design-primer-dental-research]] — 설계 유형 정의·근거 위계·편향 분류
- [[overviews/evidence-appraisal-toolkit]] — 5축 통계 도구상자
- [[overviews/statistical-abbreviations-cheatsheet]] — 통계 약자 빠른참조
- [[evidence-appraisal/al-abedalla-2022-unusual-findings-trials-evaluating-adjuncts]] — 임플란트 RCT 이상 발견 실증
- [[evidence-appraisal/choi-2015-statistical-validity-insadol-clinical-effectiveness]] — 한국 임상시험 통계 타당성 비판 사례
- [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]] — 흔한 통계 오류
