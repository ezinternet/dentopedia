---
title: "치과 응급상황 대처 인터랙티브"
type: agenda
date: 2026-10-28
status: done
source_wiki:
  - wiki/drug/medical-emergencies/gazal-2026-risk-factors-adverse-events-tooth-extraction.md
  - wiki/drug/medical-emergencies/khattak-2026-clinical-readiness-knowledge-attitude-bls.md
  - wiki/drug/medical-emergencies/tayebi-hillali-2026-competence-semi-automated-external-defibrillator.md
  - wiki/drug/systemic-disease/jevon-2020-management-anaphylaxis-dental-practice-update.md
  - wiki/drug/systemic-disease/mistry-2023-severe-anxiety-fainting-dental-restoration.md
  - wiki/drug/systemic-disease/ross-2013-neurocardiogenic-syncope-child-dental-case-review.md
output:
  - interactives/2026-10-28_dental-emergency-management.html
---

## Goal
치과 진료실에서 발생할 수 있는 7가지 주요 응급상황(아나필락시스·심정지·저혈당·기관지경련·실신·고혈압위기·발치 출혈)의 인지→대처 프로토콜을 chairside에서 즉시 참조할 수 있는 인터랙티브 도구.

## Input
- gazal-2026: 발치 고위험 환자 이상반응 위험인자 (HbA1c <9%, INR ≤3.5, BP <180/110 임계값)
- khattak-2026: 치과의사 BLS/CPR 준비도 (AED 보유율 7.5%, 교육 aOR 4.91)
- tayebi-hillali-2026: AED 실기 역량 (143s→116s, 수정 안내 효과)
- jevon-2020: 아나필락시스 관리 (아드레날린 500μg IM, 대퇴 전외측)
- mistry-2023, ross-2013: 실신 감별·관리

## Done Criteria
- 7가지 응급유형 탭 구현
- 각 탭: 인지 증상 + 단계별 대처 + 핵심 수치
- 발치 전 안전 임계값 참조표
- BLS/AED 준비도 체크리스트
- 라이트 고정 (operations-lint 통과)
