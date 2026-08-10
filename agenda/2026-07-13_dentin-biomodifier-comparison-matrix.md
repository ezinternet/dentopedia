---
title: "Dentin Biomodifier 20종 비교 매트릭스 (El Alaoui 2026 umbrella review 기반)"
type: agenda
date: 2026-07-13
status: done
owner: 원장
priority: P2
deadline:
tags: [resin-bonding, dentin-biomodification, interactive]
source_wiki:
  - wiki/resin-bonding/el-alaoui-2026-dentin-biomodification-resin-composite-umbrella.md
  - wiki/overviews/resin-dentin-bond-durability-degradation-overview.md
---

# Goal

레진-상아질 결합 내구성을 위한 dentin biomodifier 20종(천연/물리/화학)의 시기별(즉시·중기·장기) 효과를 chairside에서 즉시 비교 조회할 수 있도록 필터형 비교 매트릭스로 정리.

# Input

- wiki/resin-bonding/el-alaoui-2026-dentin-biomodification-resin-composite-umbrella.md — umbrella review 원 데이터 (9 SR, 7 MA, 51 experimental setups, 20 agents)
- sources/el-alaoui-2026-dentin-biomodification-resin-composite-umbrella.md — 세부 수치(SMD/MD/95%CI/I²) 추출 소스
- wiki/overviews/resin-dentin-bond-durability-degradation-overview.md — 임상 맥락(§4 MMP억제, §7 umbrella taxonomy)

# Output

- interactives/2026-07-13_dentin-biomodifier-comparison-matrix.html

# Done Criteria

- [x] 20종 biomodifier 전부 표에 반영 (천연 7·물리 7·화학 6)
- [x] 시기별(short/medium/long-term) 효과 방향 뱃지 (positive/negative/no-effect/controversial/no-data) — 색상 + 기호 이중 인코딩(색맹 고려)
- [x] 카테고리(천연/물리/화학) + "오늘 chairside 적용 가능" 필터 칩, 검색창
- [x] NTAP 두 SR 간 CCA 57.9%(very high overlap) 주의사항 명시 — 논문 원문의 핵심 caveat 누락 방지
- [x] frontmatter에 source_wiki 백링크 박음
- [x] agenda 파일 자체 생성 (Hard rule)

# Notes / Decisions

- 2026-07-13: 논문이 일부 agent(전기전류·오존·glycolic acid·warm air blow)에 대해 pooled effect를 보고하지 않음 — "no data reported"로 명시적으로 구분(효과 없음과 혼동 방지).
- 2026-07-13: NTAP는 물리적 agent 중 최고 효과크기(SMD 최대 3.28)이나 두 NTAP SR 간 CCA=57.9%(very high)로 과대평가 가능성 있음 — 이 caveat을 표 상단 callout으로 강조(수치만 보고 오해할 위험이 커서).
- 색상은 효과방향(positive=녹색/negative=적색/controversial=amber/no-effect=회색/no-data=연회색)과 기호(▲▼◆●—)를 이중 인코딩해 색각이상 사용자도 구분 가능하도록 설계.

# References

- [[wiki/resin-bonding/el-alaoui-2026-dentin-biomodification-resin-composite-umbrella]]
- [[wiki/overviews/resin-dentin-bond-durability-degradation-overview]]
