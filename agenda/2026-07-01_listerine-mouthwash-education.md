---
title: "치위생사 교육 — 리스테린(에센셜오일) 가글 효과 자가테스트 퀴즈"
type: agenda
date: 2026-07-01
status: in-progress
owner: 위생사 팀장
priority: P1
source_wiki:
  - wiki/overviews/antiseptic-mouthrinse-chlorhexidine-essential-oil-overview.md
  - wiki/periodontics/figuero-2019-adjunctive-antiplaque-chemical-agents-gingivitis.md
  - wiki/periodontics/james-2017-chlorhexidine-mouthrinse-adjunctive-gingival.md
  - wiki/oral-microbiology/plummer-2022-listerine-mouthwash-oropharyngeal-microbiota.md
  - wiki/oral-microbiology/min-2024-essential-oil-mouthrinses-plaque-microbiome.md
output:
  - interactives/quiz-specs/listerine-mouthwash.json
  - interactives/2026-07-01_listerine-mouthwash-quiz.html
tags: [hygienist-education, mouthwash, essential-oil, listerine, interactive, quiz]
---

# Goal

리스테린형 에센셜오일(EO) 가글의 근거 기반 효과·한계·CHX 대비 위치를 치위생사가 익히도록,
`hygienist-education` 스킬 산출 문항을 사이트 자가테스트 HTML 퀴즈로 고정. 근거 위키 한정.

# Input

- wiki/overviews/antiseptic-mouthrinse-chlorhexidine-essential-oil-overview.md — 뼈대(효능순위·착색·한계)
- wiki/periodontics/figuero-2019-...gingivitis.md — NMA 53 RCT: EO≥CHX≥triclosan>CPC
- wiki/periodontics/james-2017-...gingival.md — Cochrane: CHX 착색 SMD +1.07
- wiki/oral-microbiology/plummer-2022-listerine-...microbiota.md — 12주 EO 구인두 미생물 무변화(안전)
- wiki/oral-microbiology/min-2024-essential-oil-...microbiome.md — EO reset, 단 J&J 후원(이해상충)

# Output

- interactives/quiz-specs/listerine-mouthwash.json
- interactives/2026-07-01_listerine-mouthwash-quiz.html

# Done Criteria

- [x] 6문항(효능·한계·CHX대비·안전성·이해상충), 정답·해설·근거 cite
- [x] build-quiz.py 생성 + 색인 + operations-lint 통과
