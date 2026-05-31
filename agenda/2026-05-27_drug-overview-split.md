---
title: "drug 카테고리 overview 5개 sub-overview로 분할"
type: agenda
date: 2026-05-27
status: in-progress
owner: 원장
priority: P1
tags: [drug, synthesis, overview-split]
output_wiki:
  - wiki/overviews/drug-anticoagulant-antiplatelet-perioperative-overview.md
  - wiki/overviews/drug-mronj-antiresorptive-overview.md
  - wiki/overviews/drug-antibiotic-stewardship-overview.md
  - wiki/overviews/drug-analgesics-postop-pain-overview.md
  - wiki/overviews/drug-systemic-disease-dental-management-overview.md
  - wiki/overviews/drug-clinical-decision-ladder.md
---

# Goal

drug 카테고리(75 paper, 기존 overview 2개, papers/overview 비율 36)를 임상 결정축별 5개 sub-overview로 분할해 synthesis 커버리지를 paper 축적 속도에 맞춤. 단일 ladder가 항응고·MRONJ·항생제·진통제·전신질환의 서로 다른 임상 결정 축을 다 묶는 broad-but-shallow 구조를 해체.

# Input

- wiki/drug/*.md — 75개 paper, sub-overview 분류 대상
- wiki/overviews/anticoagulant-antiplatelet-dental-protocol.md — 기존, 항응고제 sub-overview로 rename·흡수
- wiki/overviews/drug-clinical-decision-ladder.md — 기존, 5개 sub-overview 묶는 허브로 재정의

# Output

- wiki/overviews/drug-anticoagulant-antiplatelet-perioperative-overview.md (기존 rename, 15 paper)
- wiki/overviews/drug-mronj-antiresorptive-overview.md (신규, 7 paper)
- wiki/overviews/drug-antibiotic-stewardship-overview.md (신규, 13 paper)
- wiki/overviews/drug-analgesics-postop-pain-overview.md (신규, 19 paper)
- wiki/overviews/drug-systemic-disease-dental-management-overview.md (신규, 16+2 LA paper)
- wiki/overviews/drug-clinical-decision-ladder.md (허브 재정의)

각 산출물 frontmatter에 `agenda: agenda/2026-05-27_drug-overview-split.md` 백링크 박을 것.

# Done Criteria

- [ ] 5개 sub-overview 모두 작성 (frontmatter + 한줄요약 + 임상 결정 분기 + paper wikilink)
- [ ] 75개 paper 중 임상결정축 73개가 최소 한 sub-overview에 wikilink로 등장 (한약 3개는 dental-materials cross-link)
- [ ] 기존 anticoagulant-antiplatelet-dental-protocol.md rename 완료
- [ ] drug-clinical-decision-ladder.md 허브로 재정의
- [ ] index.md에 신규 4개 entry 추가, rename된 1개 entry 갱신
- [ ] daily-audit.py 6개 audit 모두 PASS, synthesis-backlog 100% 유지
- [ ] category-overflow에서 drug 카테고리 정상 (papers/ov 비율 < 15)

# Notes / Decisions

- LA(lidocaine, vasoconstrictor) 2개는 단독 overview 어색해 systemic disease overview에 흡수 (안전성 관점).
- 한약·기능식품 3개(Magnoliae cortex 2개, hong-2019)는 임상결정축 paper 아니라 in-vitro/RCT. drug 카테고리에 그대로 두되 dental-materials나 인접 overview에 cross-link로 wikilink만 추가. 단독 sub-overview 만들지 않음.
- 분할 후 drug 카테고리 paper-to-overview 비율: 75/6 = 12.5 (이전 36.0). 갭 큰 카테고리 리스트에서 drug 빠짐.
- 후속 agenda 후보: dental-materials (51:2), bone-regeneration (44:2), prosthetic-materials (31:2), digital-workflow (28:2), periodontics (20:1).
