---
title: "Synthesis-enforcement 3종 세팅 (안전 모드)"
type: agenda
date: 2026-05-26
status: in-progress
owner: 원장
priority: P1
tags: [meta, synthesis-enforcement, lint, audit, infrastructure]
source_wiki: []
output_wiki:
  - CLAUDE.md
---

# Goal

ingest가 자기 자신을 합성하도록 강제하는 3종 메커니즘 구축. ingest의 friction은 살짝 올리되 synthesis의 friction을 강하게 내리는 비대칭 설계 원칙.

성공 기준 한 줄: 내일 아침 `python3 scripts/daily-audit.py` 실행으로 ① unsynthesized source 수와 stale 30일+ 목록, ② rationale 누락된 신규 source, ③ overview 후보 카테고리가 logs/에 박혀 있어야 한다.

# Input

- 본 세션 합의된 운영 모드: **안전 모드**
  - 신규 ingest부터만 rationale 강제 (cutoff: 2026-05-27)
  - category overflow는 signal-only (자동 agenda 생성 안 함)
  - 기존 746개 source는 backfill 없음
- 기존 인프라:
  - scripts/lint.py — wiki frontmatter
  - scripts/operations-lint.py — OPS cross-link
  - scripts/orphan-check.py — PDF↔source 1:1
  - logs/ — 어제부터 활성화

# Output

- `scripts/synthesis-backlog.py` — overview 미연결 source 식별 + stale 30일+ 표시
- `scripts/ingest-rationale-lint.py` — 신규 source `## Why Ingested` 섹션 강제
- `scripts/category-overflow.py` — overview candidate 카테고리 signal-only
- `scripts/daily-audit.py` — 위 3개 + 기존 lint 3개 일괄 runner
- `CLAUDE.md` 갱신 — Step 2.5(Why Ingested) + Daily Audit 사용법
- `logs/2026-05-26_*.log` — 첫 실행 결과

# Done Criteria

- [ ] synthesis-backlog.py 작동 — overview 미연결 source 수 출력
- [ ] ingest-rationale-lint.py 작동 — cutoff 이후 source만 검사
- [ ] category-overflow.py 작동 — 비율 > 5 또는 overview=0&papers≥5 카테고리 signal
- [ ] daily-audit.py — 6개 audit (3 신규 + 3 기존) 일괄 실행, exit code 집계
- [ ] CLAUDE.md에 새 ingest 흐름 + cutoff 날짜 + 사용법 박힘
- [ ] 첫 실행 logs/ 6건 산출
- [ ] operations-lint 0 errors 유지 (본 agenda 자체도 통과)

# Notes / Decisions

- 2026-05-26: 안전 모드 선택. 자동 agenda 생성 안 함 (orphan agenda 양산 위험).
- 2026-05-26: rationale은 본문 섹션(`## Why Ingested`)으로. frontmatter 필드보다 사람이 읽기 좋고 lint도 쉬움.
- 2026-05-26: stale 임계 30일은 [claude해석] 임의값. 1개월 운영 후 조정 가능.
- 2026-05-26: overview 임계 paper:overview = 5:1도 [claude해석] 임의값. Luhmann의 비율은 거의 1:1이었지만 그건 직업 학자 케이스. 임상가 운영에서는 5:1이 현실적.
- 자동 차단(hard gate) 채택 안 함 — 임상 일정에 종속된 ingest window를 막으면 burnout/회피 위험. 거울(signal)이 강제(block)보다 지속 가능.

# References

- [[feedback_wiki-living-document]] (memory) — 본 작업의 메모리 차원 선행 선언
- [[agenda/2026-05-26_wiki-growth-visualization]] — 같은 세션, ingest:합성 비대칭 가시화의 첫 시도
- Luhmann Zettelkasten, Toyota JIT, Kanban WIP limit — 설계 선례
