---
title: "ParaPost 포스트 선택 결정 + 식립·합착 과정 인터랙티브"
type: agenda
date: 2026-07-02
status: done
owner: 원장
priority: P2
source_wiki:
  - wiki/overviews/post-and-core-fiber-post-decision-overview.md
  - wiki/post-and-core/izadi-2020-core-materials-fracture-resistance-parapost.md
  - wiki/post-and-core/rezaei-2010-comparison-stresses-fiber-parapost-casting.md
  - wiki/post-and-core/alkahtani-2010-root-canal-sealers-timing-parapost.md
output_wiki: []
tags: [post-and-core, parapost, fiber-post, interactive, decision-tree]
---

# Goal

ETT(근관치료치) 수복에서 ①포스트 필요여부 → ②ferrule 보존 → ③포스트 재료(파이버 vs 금속/ParaPost) 결정을 chairside에서 즉시 참조하는 결정 도구를 만들고, 여기에 **ParaPost 식립·합착 단계별 과정**(인제스트 논문에 기술된 lab 프로토콜 기반)을 함께 시각화한다.

# Input

- wiki/overviews/post-and-core-fiber-post-decision-overview.md — 순차 결정 thesis(포스트→ferrule→재료, 실패양상)
- wiki/post-and-core/rezaei-2010-comparison-stresses-fiber-parapost-casting.md — 광탄성 응력 분포(ParaPost 응력 집중)
- wiki/post-and-core/izadi-2020-core-materials-fracture-resistance-parapost.md — FRC>ParaPost 파절하중 + ParaPost 식립 프로토콜(#2 peeso→#4 drill, etch, Panavia F2)
- wiki/post-and-core/goutam-2022-luxacore-photocore-coremax-fracture-parapost.md — Izadi 재현
- wiki/post-and-core/alkahtani-2010-root-canal-sealers-timing-parapost.md — resin cement 합착 타이밍·미세누출(즉시 합착·AH26 최소)
- wiki/post-and-core/wang-2019-fiber-posts-vs-metal-posts-severely-damaged.md — 심한 손상 ≤2벽 파이버 우위(RR 0.57)
- wiki/post-and-core/naumann-2017-ferrule-first-post-second-systematic-review.md — ferrule first

# Output

- interactives/2026-07-02_parapost-decision-placement.html

산출물 frontmatter에 `agenda: agenda/2026-07-02_parapost-decision-placement-interactive.md` 백링크 포함.

# Done Criteria

- [x] 결정 트리(포스트 필요→ferrule→재료) 인용 포함
- [x] ParaPost 식립·합착 단계(근거 inline) 시각화
- [x] 근거는 인제스트 논문에 한정(Rule #1); lab 프로토콜임을 명시
- [x] interactives/index 재생성 대상(배포 시 자동)
