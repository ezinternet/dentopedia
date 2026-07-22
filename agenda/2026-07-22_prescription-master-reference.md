---
title: "쓸 것인가, 말 것인가 — 치과 처방 결정 레퍼런스 인터랙티브"
type: agenda
date: 2026-07-22
status: done
owner: 원장
priority: P1
tags: [drug, antibiotics, analgesics, prescription, chairside, interactive]
---

# Goal

발치·임플란트·근관치료·치주·치성감염 등 개원 치과에서 매일 나오는 처방 결정을, 위키가 이미 보유한 근거(drug overview 5종 + 인접 페이지)만으로 **한 화면에서 끝내는** chairside 레퍼런스 인터랙티브를 만든다. 페니실린 알레르기 대체, 특수환자(신·간·임신·소아·고령 DDI·항응고·MRONJ·IE), "처방하면 안 되는 상황" 목록까지 포함해 이 파일 하나로 커버.

# Input

근거가 될 wiki 페이지. 모든 용량·수치는 아래에서만 인용한다 (Rule #1).

- wiki/overviews/drug-clinical-decision-ladder.md — 5축 허브·한국 임상 조정(Clindamycin→Cephalexin/Azithromycin, 임신 Felypressin 회피)
- wiki/overviews/drug-antibiotic-odontogenic-pain-overview.md — 통증≠감염 원칙, ADA 2019 CPG 결정표, 지연처방, 치관주위염, 소아 4 D's, 임플란트 NNT=143
- wiki/overviews/drug-antibiotic-stewardship-overview.md — IE 4개 고위험군, 단순발치 무효(Lodi), 임플란트 단일 2g(Torof), 상악동(Díaz), 약물 안전성(Thornhill), 치주 국소전달(Aimetti·Milinkovic)
- wiki/overviews/drug-analgesics-postop-pain-overview.md — Ibu400+APAP1000 NNT≈1.5, alternate>concurrent, opioid 회피, preemptive 시술별 차이, endo 시간대 의존, NSAID 안전성 4축, 피린계 SJS/TEN
- wiki/overviews/drug-anticoagulant-antiplatelet-perioperative-overview.md — TXA 4.8% 양치 프로토콜, INR ≤3.5 비중단
- wiki/overviews/drug-systemic-disease-dental-management-overview.md — DM/HbA1c 임계, 1:200,000 epinephrine, 임신 vasoconstrictor, 고령 DDI 40.7%
- wiki/drug/mronj/vidovic-juras-2024-antibiotic-prophylaxis-dental-procedures.md — AP 적응증·Amoxicillin 2g / Clindamycin 600mg
- wiki/drug/antibiotics/wilson-2021-ie-prophylaxis-aha-scientific-statement.md — IE 용량표(성인 2g / 소아 50mg/kg)
- wiki/drug/antibiotics/diaz-2025-antibiotics-sinus-lift-infection-umbrella.md — 상악동거상술 프로토콜·페니실린 알레르기 대안 용량
- wiki/periodontics/alharbi-2019-management-acute-periodontal-abscess-mimicking.md — 급성 치주농양 실제 처방 프로토콜
- wiki/periodontics/herrera-2014-acute-periodontal-lesions.md — 급성 치주병변·NPD 메트로니다졸
- wiki/oral-surgery/schmidt-2021-pericoronitis-management-antibiotic-prescribing-recommendations.md — 치관주위염 처치 표
- wiki/oral-surgery/camps-font-2024-antibiotic-prophylaxis-dry-socket-nma.md — dry socket NNT=25 / SSI NNT=18
- interactives/2026-06-19_allergy-drug-reference.html — 기존 알레르기 대체 참조(상품명·용법 표기 관례 승계)

# Output

- interactives/2026-07-22_prescription-master-reference.html

# Done Criteria

- [x] 처치별 처방 카드 (발치·임플란트·근관·치주·치성감염) — 항생제/진통제/보조 3단 구조
- [x] 페니실린 알레르기 대체 경로 단독 탭 (교차반응 severity 분기 포함)
- [x] 특수환자 탭 (신·간·임신수유·소아·고령 DDI·항응고·MRONJ·IE·당뇨)
- [x] "처방하지 말 것" 네거티브 리스트 — 근거 인용 포함
- [x] 모든 수치에 출처 배지 (저자-연도) + 근거 등급
- [x] 검색 필터 + 처방문 복사 버튼 (chairside 실사용)
- [x] frontmatter `agenda:` 백링크

# Notes

이 도구는 OPERATIONS.md §6 기준 **Class B (임상 결정 도구)** — 수치가 특정 논문에서 추출된 임상 임계값이므로 deploy 스크립트가 재생성하지 않는다. `source_wiki:` 페이지가 갱신되면 `scripts/interactive-staleness.py`가 STALE 신호를 내고, 재작성은 사람/LLM in-the-loop.

기존 `2026-05-27_drug-decision-tree.html`(결정 트리)·`2026-06-19_allergy-drug-reference.html`(특정 환자 알레르기 프로파일)과는 **역할이 다르다** — 이 파일은 처치별 처방 전체를 한 화면에 모으는 종합 레퍼런스. 두 기존 도구는 유지.
