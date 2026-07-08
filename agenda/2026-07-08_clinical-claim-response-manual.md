---
title: "임상 클레임 대응 매뉴얼 (A·F·E) — 인터랙티브"
type: agenda
date: 2026-07-08
status: in-progress
owner: 원장
priority: P1
deadline:
tags: [complaint-management, claim-coach, interactive]
source_wiki:
  - wiki/overviews/complaint-management-pipeline-classification-expectation-response-education.md
  - wiki/complaint-management/alrahabi-2019-clinical-malpractice-in-endodontics.md
  - wiki/complaint-management/park-2016-analysis-of-malpractice-claims-associated.md
  - wiki/complaint-management/kwon-2017-analysis-of-the-legal-effect.md
  - wiki/complaint-management/grillo-2023-written-informed-consent-facial-cosmetic.md
  - wiki/complaint-management/friele-2006-patient-expectations-fair-complaint.md
  - wiki/behavioral-dentistry/body-dysmorphic-disorder/nabavizadeh-2023-prevalence-of-body-dysmorphic-disorder.md
---

# Goal

claim-coach 스킬로 생성한 임상 클레임(A 통증·기능 / F 심미 / E 협박·과도요구) 응대 스크립트를 체어사이드에서 바로 참조할 수 있는 인터랙티브 매뉴얼로 정리해, 위생사·실장·원장이 상황별 3톤 스크립트를 즉시 검색·복사해 쓸 수 있게 한다.

# Input

- wiki/complaint-management/*.md — 유형 분류(Reader/HCAT)·기대진단(Friele)·법적 가드 근거 21편
- wiki/overviews/complaint-management-pipeline-classification-expectation-response-education.md — 통합 파이프라인 오버뷰
- wiki/behavioral-dentistry/body-dysmorphic-disorder/nabavizadeh-2023-prevalence-of-body-dysmorphic-disorder.md — F(심미) 반복 불만족 참고
- .claude/skills/claim-coach/SKILL.md — 유형(A~H)·domain·status theory·blocklist·법적 가드 프레임 (스킬 규칙 그대로 반영)

# Output

- interactives/2026-07-08_clinical-claim-response-manual.html

각 산출물의 frontmatter에 `agenda: agenda/2026-07-08_clinical-claim-response-manual.md` 백링크 박음.

# Done Criteria

- [x] A(통증·기능) 7건, F(심미) 5건, E(협박·과도요구, 임상 트리거) 3건 — 총 15상황 커버
- [x] 상황별 3톤(공감우선/균형/전문성) 스크립트 — E는 claim-coach 규칙대로 표준 3톤 대신 신중 초안(채널별) 형식 유지
- [x] 검색(키워드) + 유형 필터 + 스크립트 복사 버튼 인터랙티브 UI
- [x] frontmatter agenda/source_wiki 백링크
- [ ] GitHub Pages 배포 확인 (push 후 Actions 확인)

# Notes / Decisions

- E 유형에 표준 3톤을 강제하지 않음 — claim-coach 스킬 자체 가드("E는 신중 초안 형식, 3톤 변주 대체")를 그대로 지킴. 사용자에게도 이 예외를 명시함.
- 사용자 요청 범위: "임상 관련 전체(A+E+F)", 형식: "상황별 3톤 변주" (E 예외 고지 후 진행).
- B(비용)/C(설명부족)/D(대기서비스)/G(리뷰)/H(서류) 유형은 이번 매뉴얼 범위 밖 — 필요 시 별도 agenda로 확장.
