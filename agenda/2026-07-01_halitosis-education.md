---
title: "치위생사 교육 — 구취(할리토시스) 환자 자가테스트 퀴즈"
type: agenda
date: 2026-07-01
status: in-progress
owner: 위생사 팀장
priority: P1
source_wiki:
  - wiki/overviews/halitosis-etiology-measurement-management-overview.md
  - wiki/halitosis/silva-2017-estimated-prevalence-halitosis-sr.md
  - wiki/halitosis/szalai-2023-organoleptic-halitometric-assessments-do-not.md
  - wiki/halitosis/wang-2024-association-between-halitosis-and.md
  - wiki/halitosis/dou-2016-halitosis-helicobacter-pylori-meta-analysis.md
  - wiki/halitosis/huang-2022-efficacy-of-probiotics-in.md
output:
  - interactives/quiz-specs/halitosis.json
  - interactives/2026-07-01_halitosis-quiz.html
tags: [hygienist-education, halitosis, interactive, quiz]
---

# Goal

구취(할리토시스) 환자의 원인 분류·측정·관리 원칙을 치위생사가 근거와 함께 익히도록,
`hygienist-education` 스킬 산출 문항을 사이트 자가테스트 HTML 퀴즈로 고정한다. 근거 위키 한정.

# Input

- wiki/overviews/halitosis-etiology-measurement-management-overview.md — 뼈대(유병률·분기점)
- wiki/halitosis/silva-2017-estimated-prevalence-halitosis-sr.md — 유병률 31.8%
- wiki/halitosis/szalai-2023-organoleptic-halitometric-assessments-do-not.md — OLT gold standard, 할리미터 중등도 상관
- wiki/halitosis/wang-2024-association-between-halitosis-and.md — 치주염 ~4배
- wiki/halitosis/dou-2016-halitosis-helicobacter-pylori-meta-analysis.md — H. pylori 제균 RR 0.17
- wiki/halitosis/huang-2022-efficacy-of-probiotics-in.md — 프로바이오틱스 단기 효과

# Output

- interactives/quiz-specs/halitosis.json (스펙 · 진실원천)
- interactives/2026-07-01_halitosis-quiz.html (build-quiz.py 산출)

# Done Criteria

- [x] 6문항, 정답·해설·근거 cite
- [x] build-quiz.py 생성 + interactives-index 색인 + operations-lint 통과
