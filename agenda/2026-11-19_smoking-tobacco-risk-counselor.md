---
title: "흡연·담배제품 치과 위험 상담기 — 인터랙티브"
type: agenda
date: 2026-11-19
status: done
owner: 원장
priority: P1
tags: [smoking, tobacco, e-cigarette, vaping, ETS, implant, peri-implantitis, counseling, decision-tool]
source_wiki:
  - wiki/overviews/smoking-tobacco-periodontal-implant-overview.md
output:
  - interactives/2026-11-19_smoking-tobacco-risk-counselor.html
---

# Goal

흡연·담배제품(궐련·전자담배·무연담배·간접흡연) 노출을 치주·임플란트·발치 맥락에서 상담할 때, 근거 수치와 "말해도 되는/안 되는" 경계를 chairside에서 바로 꺼내 쓰기 위한 도구.

# Input

- wiki/overviews/smoking-tobacco-periodontal-implant-overview.md — 종합(흡연 23편)
- interactives/2026-11-19_smoking-tobacco-risk-counselor.html 의 `source_wiki:` 15개 페이지 — 도구 본문 수치의 출처

# Output

- interactives/2026-11-19_smoking-tobacco-risk-counselor.html

# Done Criteria

- [x] 노출 8종 × 맥락 5종 입력 → 위험 요약 + 상담 스크립트
- [x] 근거 스냅샷 표(생존·주위염·조기실패·용량-반응·금연·상악동·발치·ETS·전자담배)
- [x] 해석 주의 박스(근거 불일치·abstract-only 명시)
- [x] 라이트 고정

# Notes / Decisions

- 2026-11-19: 이 agenda는 사후 backfill이다. 도구는 `c519fd77a`로 agenda 백링크 없이 커밋되어 `operations-lint.py`가 `MISSING agenda` error를 냈다(CI `lint.yml` red). 산출물 내용은 건드리지 않고 추적 고리만 복구했다.
- 2026-11-19: 다음에 이 도구를 개정할 때 `PAGE_VERSION` 캐시 블록(OPERATIONS §7)을 함께 넣을 것 — 현재 파일에는 없다.

# References

- [[overviews/smoking-tobacco-periodontal-implant-overview]]
- [[agenda/2026-11-19_alcohol-risk-chairside-tool]]
