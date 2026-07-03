---
title: "시멘트질 열개(Cemental Tear) chairside 결정도구 — 감별진단·치료트리·예후"
type: agenda
date: 2026-07-03
status: done
owner: 원장
priority: P2
tags: [cemental-tear, periodontics, differential-diagnosis, decision-tree, prognosis]
source_wiki:
  - wiki/periodontics/liang-2025-cemental-tear-diagnosis-treatment-consensus.md
  - wiki/cracked-tooth/patel-2025-position-statement-longitudinal-cracks-fractures.md
  - wiki/resin-bonding/corbella-2025-surgical-techniques-vertical-root-fractures-sr.md
---

# Goal

시멘트질 열개(Cemental Tear)를 수직치근파절(VRF)·근관·치주질환과 오진하지 않도록, chairside에서 (1) 감별진단, (2) 조각 위치·골내결손 기반 치료 결정, (3) 예후 예측을 즉시 참조하는 단일 3-탭 인터랙티브를 만든다. 모든 수치는 Liang 2025 합의문에서만 추출(Rule #1).

# Input

- wiki/periodontics/liang-2025-cemental-tear-diagnosis-treatment-consensus.md — 유일 근거(합의문): 감별·결정트리·예후 수치 전부
- wiki/cracked-tooth/patel-2025-position-statement-longitudinal-cracks-fractures.md — VRF/종적파절 감별 축 (맥락)
- wiki/resin-bonding/corbella-2025-surgical-techniques-vertical-root-fractures-sr.md — VRF 예후 대비 (맥락)

# Output

- interactives/2026-07-03_cemental-tear-decision-tools.html
  - Tab 1 감별진단: 치수생활력·방사선 소견·병소 분포·기왕 RCT 등 판별 인자 → cemental tear vs VRF vs 근관 vs 치주 가능성
  - Tab 2 치료 결정트리: 임상증상 유무 → 조각 위치(관상/중간/치근단 1/3) → 비수술/수술 → 골내결손(깊이·벽수·너비)별 재생술 선택
  - Tab 3 예후: 위치별 치유율(60/66.7/11.1%), 비수술 28.6% vs 수술 57.7%, 완전제거 1년 94% 잔존

frontmatter에 agenda 백링크 + source_wiki 박음.

# Done Criteria

- [x] agenda 파일 생성
- [x] 3-탭 인터랙티브 생성 (모든 수치 inline 출처 = Liang 2025)
- [x] interactives/index 재생성은 배포 스크립트가 처리 (수동 불필요)
- [x] Rule #1 준수 — 논문 밖 수치·권고 없음
