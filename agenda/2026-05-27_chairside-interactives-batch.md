---
title: "Chairside interactives 3종 배치 — drug ladder · implants ladder 축2·축3 도구화"
type: agenda
date: 2026-05-27
status: done
owner: 원장
priority: P1
tags: [interactive, chairside, drug, implants, batch]
output_wiki:
  - wiki/overviews/drug-clinical-decision-ladder.md
  - wiki/overviews/implants-clinical-decision-ladder.md
---

# Goal

drug 5분할 작업 + implants ladder 갱신으로 만든 thesis를 chairside에서 즉시 결정에 쓸 수 있는 인터렉티브 3종으로 도구화. 본문 페이지에 분산된 결정 트리를 한 화면 입력→권고 형태로 압축.

# Input

- wiki/overviews/drug-clinical-decision-ladder.md (허브) + 5개 sub-overview
- wiki/overviews/implants-clinical-decision-ladder.md (축 2 short implant, 축 3 drill thermal)
- wiki/overviews/osseodensification-clinical-applications.md (drill thermal selector 인접)

# Output

3개의 단일 HTML 파일 (CDN 없이 오프라인 가능, iPad chairside 가정):

- interactives/2026-05-27_drug-decision-tree.html — 약물 결정 트리 (drug 5축 통합)
- interactives/2026-05-27_short-implant-vs-augmentation.html — 위축부 implant 결정
- interactives/2026-05-27_drill-thermal-selector.html — drill thermal protocol

각 산출물 frontmatter에 `agenda: agenda/2026-05-27_chairside-interactives-batch.md` 백링크 + `source_wiki:` 의 wiki 페이지 경로 박을 것.

# Done Criteria

- [ ] 3개 HTML 모두 작성, 단일 파일·인라인 CSS/JS·외부 의존 없음
- [ ] 각 HTML frontmatter (HTML comment) 에 agenda·source_wiki 박힘
- [ ] 약물 결정 트리: 환자 case 입력 → 5축 모두에서 권고 출력
- [ ] Short implant 도구: 잔존골·부위·morbidity → short vs augment 분기
- [ ] Drill thermal: bone type·drill·irrigation → 47°C 위험 + OD 권고
- [ ] index.md 메타 섹션에 3 entry 추가
- [ ] operations-lint 통과 (15 → 18 OK 0 errors)
- [ ] daily-audit 7/8 PASS·SIGNAL

# Notes / Decisions

- 단일 HTML·인라인 — chairside iPad에서 WiFi 끊겨도 동작 보장. ISQ 칼큘레이터와 동일 패턴.
- UI 한국어. 의학 용어는 (English) 병기. drug overview 본문의 한국어 결정 트리를 그대로 fork.
- 권고 출력은 traffic-light (green/yellow/red) + 근거 paper inline citation + 원장 결정 권한 명시.
- 한약·기능식품·LA epinephrine 1:200K vs 1:80K 도구화는 본 batch에서 제외 (follow-up agenda 후보).
