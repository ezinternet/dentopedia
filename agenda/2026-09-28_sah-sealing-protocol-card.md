---
title: "SAH 봉쇄 프로토콜 인쇄용 체어사이드 카드"
type: agenda
date: 2026-09-28
status: done
owner: 원장
priority: P2
deadline:
source_wiki:
  - wiki/overviews/screw-access-hole-sealing-protocol-overview.md
  - wiki/prosthetic-materials/abutment-screw/singla-2025-comparative-microbial-assessment-different-screw.md
  - wiki/prosthetic-materials/abutment-screw/pereira-2016-influence-sealing-screw-access-hole.md
  - wiki/prosthetic-materials/abutment-screw/packaeser-2025-effect-resin-composite-filling-thickness.md
tags: [screw-access-hole, SAH, interactive, chairside-card, prosthetic-materials]
---

# Goal

방금 종합한 스크류 접근홀(SAH) 봉쇄 프로토콜(wiki/overviews/screw-access-hole-sealing-protocol-overview.md)을 진료실에서 바로 인쇄해 참조할 수 있는 1페이지 체어사이드 카드로 만든다.

# Input

- wiki/overviews/screw-access-hole-sealing-protocol-overview.md — 3편(Singla·Pereira·Packaeser) + 기존 근거(Khurshid·Hamed) 종합, 이 카드의 1차 출처
- wiki/prosthetic-materials/abutment-screw/singla-2025-comparative-microbial-assessment-different-screw.md — 1차 충전재 비교(RCT)
- wiki/prosthetic-materials/abutment-screw/pereira-2016-influence-sealing-screw-access-hole.md — 벽 표면처리 프로토콜(in vitro)
- wiki/prosthetic-materials/abutment-screw/packaeser-2025-effect-resin-composite-filling-thickness.md — 콤포지트 두께(in vitro)

# Output

- interactives/2026-09-28_sah-sealing-protocol-card.html

# Done Criteria

- [x] 6단계 체어사이드 프로토콜 + 충전재/벽처리/두께 근거표 + 회색지대 경고 + 근거등급 요약을 1페이지(A4 인쇄 기준)로 압축
- [x] 인터랙티브 라이트 고정 규칙 준수 (다크모드 블록 없음)
- [x] frontmatter cross-link (source_wiki 4건 + agenda 백링크)
- [x] operations-lint.py 통과
