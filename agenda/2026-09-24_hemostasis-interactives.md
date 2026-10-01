---
title: "발치와 지혈 인터랙티브 — RCT 비교 매트릭스 & 지혈제 선택기"
type: agenda
date: 2026-09-24
status: done
category: drug/anticoagulants
output_wiki:
  - interactives/2026-09-24_hemostasis-rct-comparison-matrix.html
  - interactives/2026-09-24_hemostatic-agent-selector.html
---

## 목적

항혈소판·항응고제 복용 환자 발치 후 지혈제 관련 RCT(agrawal·kaddah·patil·singh-jolly) 인제스트 후
핵심 수치를 임상에서 바로 활용할 수 있도록 인터랙티브 도구 2종 제작.

## 산출물

- **RCT 비교 매트릭스**: 환자 유형별 필터링으로 적합 연구 빠르게 조회
- **지혈제 선택기**: 환자 상태 입력 → 근거 기반 지혈제 추천

## 2026-10-01 갱신 (근거 재반영)

**사유**: 2026-10-01 인제스트로 `wiki/drug/anticoagulants/`에 항응고·항혈소판 논문 11편이 추가되어 두 도구의 일부 서술이 새 근거와 어긋남 (`interactive-staleness`가 STALE 표시).

**핵심 변경**
- 선택기 DOAC 항목: "TXA 양치액이 출혈 50–60% 감소(관찰연구)" 삭제 — Ockerman 2021 RCT(n=222)의 1차 결과가 중립(RR 0.92, 0.60–1.42). "DOAC 전용 RCT 없음" 정정: Kyyak 2023(n=21)·Ockerman 2021 반영. 1순위를 "봉합 + 소켓 충전 + 압박"으로 변경(키토산·Surgicel은 외삽으로 강등).
- SAPT·DAPT·응고이상: 키토산이 지혈 시간은 최단이나 출혈 사건 순위는 최하위(Mahardawi 2023 NMA)라는 경고 추가. 항혈전제 환자에서 출혈 사건을 유의하게 줄인 유일한 제제로 TXA 행 추가(OR 0.27, 중등도 확실성; 항혈소판 단독 분석은 없어 "간접" 표시).
- DAPT: 정상 대비 출혈 위험 RR 10.3(즉시)·7.72(지연), 유지 vs 중단 비유의(RR 2.13, P=.07) — "약물 중단 불필요" 단정 문구 완화 (Alagil 2023, 초록 기준).
- 와파린: 가이드라인(유지 + 국소 지혈, INR ≤2.2, INR >3·다수 발치 협진)과 Boccatonda 2023 NMA(2일 중단이 출혈 낮음 OR 0.30, 저확신)의 긴장을 명시 — "중단 불필요" 단정 문구 완화. 거즈 + TXA 행 추가.
- 매트릭스: 카드 8장 추가(Ockerman·Kyyak·Mahardawi·Boccatonda·Valenzuela-Mencía·Alagil·Calcia·Katz), 필터 칩 2개(DOAC·종합·지침), 요약표 4행 수정, "지혈 속도 ≠ 재출혈" 경고 박스.

**한계 (도구에 그대로 표시)**: 초록만 확보한 논문 4편(Alagil·Calcia 등)의 신뢰구간·편향 평가는 확인 불가. 수치는 모두 `wiki/drug/anticoagulants/` 페이지에서 옮김.

**미반영**: 임플란트 출혈 SR(Zou 2022)·주술기 ACCP 지침(Douketis 2022)은 발치 지혈제 선택 범위를 벗어나 제외.
