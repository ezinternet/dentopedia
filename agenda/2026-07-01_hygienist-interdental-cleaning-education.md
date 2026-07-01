---
title: "치위생사 교육 — 치간청소 도구 선택 (레슨 슬라이드 + 자가테스트 퀴즈)"
type: agenda
date: 2026-07-01
status: in-progress
owner: 위생사 팀장
priority: P1
source_wiki:
  - wiki/overviews/interdental-cleaning-devices-synthesis.md
  - wiki/interdental-cleaning/carrouel-2026-interdental-brushing-pregnancy-gingivitis-rct.md
  - wiki/interdental-cleaning/badahdah-2025-dental-water-jet-plaque-gingivitis-sr.md
  - wiki/interdental-cleaning/slekovec-2026-legionella-water-flosser-france-case-report.md
output:
  - slides/2026-07-01_hygienist_interdental-cleaning.md
  - interactives/2026-07-01_interdental-cleaning-quiz.html
tags: [hygienist-education, interdental-cleaning, slides, interactive, quiz]
---

# Goal

치간청소 도구(치실·치간칫솔·구강세정기·이쑤시개) 선택 원칙을 치위생사 신입이 근거와 함께
익히도록, `hygienist-education` 스킬 산출 레슨팩을 ① 강의 슬라이드와 ② 사이트에서 클릭으로
푸는 자가테스트 HTML 퀴즈로 고정한다. 근거는 전부 위키 한정(Four Rules).

# Input

- wiki/overviews/interdental-cleaning-devices-synthesis.md — 뼈대(결정 트리·수치)
- wiki/interdental-cleaning/carrouel-2026-...rct.md — IDB 임신치은염 BOP 56→12%, OR 3.14
- wiki/interdental-cleaning/jung-2025-flossing-performance-plaque-removal.md — 술식↑ ≠ 치태제거↑
- wiki/interdental-cleaning/badahdah-2025-...sr.md — WF 18 RCT: 출혈>치태
- wiki/interdental-cleaning/yilmaz-2025-...sustainability-rct.md — 순응도>효능
- wiki/interdental-cleaning/tyler-2023-...orthodontic-rct.md — 교정서 WF 부가 NS
- wiki/interdental-cleaning/slekovec-2026-...case-report.md — 저수조 레지오넬라 안전주의
- wiki/interdental-cleaning/el-haddad-2026-...cross-sectional.md — 나무 이쑤시개 유두손상

# Output

- slides/2026-07-01_hygienist_interdental-cleaning.md   (marp 강의 슬라이드)
- interactives/2026-07-01_interdental-cleaning-quiz.html (자가테스트 5문항 퀴즈)

각 산출물 frontmatter에 `agenda: agenda/2026-07-01_hygienist-interdental-cleaning-education.md` 백링크.

# Done Criteria

- [x] 슬라이드: 학습목표·결정트리·도구별 근거·안전주의 (inline citation)
- [x] HTML 퀴즈: 5문항, 정답·해설·근거링크, 점수 집계, self-contained
- [x] interactives-index 색인 (category: perio-maintenance)
- [x] operations-lint 통과 (agenda 백링크 체인)
