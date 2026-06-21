---
title: "비타민 D × 임플란트 골유착 논문 감시·인제스트"
type: agenda
date: 2026-06-21
status: in-progress
owner: 원장
tags: [vitamin-d, osseointegration, implants, ingest]
source_wiki:
  - wiki/implants/moy-2005-dental-implant-failure-rates-risk.md
  - wiki/implants/fan-2024-smoking-early-implant-failure-sr-ma.md
output_wiki:
  - wiki/implants/vitamin-d/miron-2025-vitamin-d-deficiency-early-implant-failure.md
  - wiki/implants/vitamin-d/tallon-2024-vitamin-d-osseointegration-umbrella-review.md
  - wiki/implants/vitamin-d/werny-2022-vitamin-d-osseointegration-dental-implants-sr.md
  - wiki/implants/vitamin-d/buzatu-2024-vitamin-d-osseointegration-human-studies-sr.md
  - wiki/implants/vitamin-d/mohsen-2024-vitamin-d-deficiency-osseointegration-prospective.md
  - wiki/implants/vitamin-d/ayyad-2025-topical-vitamin-d-immediate-implants-rct.md
  - wiki/implants/vitamin-d/francis-2024-low-serum-vitamin-d-early-implant-failure.md
  - wiki/implants/vitamin-d/dulinska-2025-vitamin-d3-soft-tissue-bone-preservation.md
---

# Goal

비타민 D (Vitamin D, 25(OH)D) 수치·보충과 임플란트 골유착(Osseointegration)·조기 임플란트 실패(Early Dental Implant Failure, EDIF) 관계를 다룬 핵심 논문 8편을 PubMed에서 선별·인제스트하여, 위키에 부재하던 `implants/vitamin-d` 서브도메인을 신설한다.

# Input

PubMed MCP 검색 (query: vitamin D AND dental implant/osseointegration/implant failure, 231건 → 직접 관련 선별). 전문은 PMC OA 우선, 미보유 시 초록만(abstract-only).

- 앵커: wiki/implants/moy-2005-dental-implant-failure-rates-risk.md — 임플란트 실패율·위험인자 고전
- 앵커: wiki/implants/fan-2024-smoking-early-implant-failure-sr-ma.md — 조기 임플란트 실패 위험인자 SR+MA
- 앵커: wiki/implants/isq/andersson-2019-rfa-factors-5year-neoss-survival.md — ISQ/안정성 (Mohsen prospective용)

# Output

8편 = 리뷰 4 (Miron SR · Tallon umbrella · Werny SR · Buzatu SR) + 1차연구 4 (Mohsen 전향 · Ayyad RCT · Francis 무상관 · Dulinska 후향).

- sources/{stem}.md × 8
- wiki/implants/vitamin-d/{stem}.md × 8
- papers/{stem}.txt × 8 (PMC 전문 또는 초록)
- index.md 항목 8줄

# Done Criteria

- [ ] 8편 sources/ + wiki/ 작성 (bilingual 한줄요약 · Why Ingested · relations)
- [ ] index.md 8항목 추가
- [ ] lint.py + orphan-check.py 통과
- [ ] per-file commit + push + qmd embed (ingest-one.py --finish ×8)
