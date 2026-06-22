---
title: "조기 임플란트 실패(보철 로딩 전) 인터랙티브 툴킷"
type: agenda
date: 2026-06-22
status: done
owner: 원장
tags: [early-implant-failure, implants, interactive, risk-scorer, decision-tree]
source_wiki:
  - wiki/overviews/early-implant-failure-risk-prevention-overview.md
  - wiki/implants/yari-2023-risk-factors-early-implant-failure.md
  - wiki/implants/uesugi-2024-risk-factors-early-failure-all-on-four.md
  - wiki/drug/antibiotics/momand-2024-antibiotic-prophylaxis-early-implant-failure.md
---

# Goal

조기 임플란트 실패(EIF, 보철 로딩 전) surveillance 배치(Yari·Uesugi·Momand + overview)의 위험인자·예방 근거를 chairside에서 즉시 참조할 수 있도록 4-도구 인터랙티브 툴킷으로 변환.

# Input

- wiki/overviews/early-implant-failure-risk-prevention-overview.md — 종합 thesis·evidence map·decision points
- wiki/implants/yari-2023-risk-factors-early-implant-failure.md — 다변량 위험인자 OR (스코어러 가중치 출처)
- wiki/implants/uesugi-2024-risk-factors-early-failure-all-on-four.md — all-on-four 즉시로딩 생존·OR (비교 도구 출처)
- wiki/drug/antibiotics/momand-2024-antibiotic-prophylaxis-early-implant-failure.md — 항생제 예방 RR/NNT (결정 트리 출처)
- 보조: fan-2024(흡연 OR 2.59)·naseri-2020·moy-2005(당뇨 RR 2.75·방사선 2.73)

# Output

- interactives/2026-06-22_early-implant-failure-toolkit.html — 4 도구 탭:
  1. 조기 실패 위험 스코어러 (multivariate OR 토글)
  2. 항생제 예방 결정 트리 (비복잡 vs 즉시발치와/감염)
  3. all-on-four 즉시로딩 조기 실패 비교 (상악 vs 하악 + 광기능화)
  4. 위험인자 근거 매트릭스 (논문별 OR/RR 비교)

각 산출물 frontmatter에 `agenda: agenda/2026-06-22_early-implant-failure-interactives.md` 백링크.

# Done Criteria

- [x] agenda 선행 생성 (OPERATIONS hard rule)
- [x] 4 도구 단일 HTML 툴킷, frontmatter(category: surgery) + source_wiki + agenda 백링크
- [x] 모든 수치 inline 출처(논문·OR/RR) 표기
- [x] interactives 색인 빌드 반영
- [x] 커밋·푸시
