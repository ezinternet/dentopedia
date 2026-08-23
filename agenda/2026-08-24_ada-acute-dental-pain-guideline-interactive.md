---
title: "ADA 급성 치통 약리관리 가이드라인 인터랙티브 체어사이드 도구"
type: agenda
date: 2026-08-24
status: done
owner: 원장
priority: P1
tags: [guideline, acute-dental-pain, analgesics, interactive]
source_wiki:
  - wiki/drug/analgesics/carrasco-labra-2024-pharmacologic-management-acute-dental-pain-guideline.md
  - wiki/drug/analgesics/ada-2024-chairside-guide-adult-extraction.md
  - wiki/drug/analgesics/ada-2024-chairside-guide-adult-pulpitis.md
---

# Goal

ADA 2024 급성 치통 약리관리 임상진료지침 패키지(본문 + Chairside Guide 2종)의 전체 권고안·주의사항·용량 한계를 발치 후 통증과 치통 잠정관리 두 시나리오에서 빠짐없이 참조할 수 있는 인터랙티브 결정 도구로 종합해 원장·스탭이 chairside에서 쓰게 한다.

# Input

- wiki/drug/analgesics/carrasco-labra-2024-pharmacologic-management-acute-dental-pain-guideline.md — 지침 본문 (JADA 2024;155(2):102-117): Box 1·2 권고 전문, GPS, 일반 비고, 근거 방법론
- wiki/drug/analgesics/ada-2024-chairside-guide-adult-extraction.md — 발치 후 통증 체어사이드 경로 (단순/외과 발치, ADD/REPLACE 사다리, 금기 분기)
- wiki/drug/analgesics/ada-2024-chairside-guide-adult-pulpitis.md — 치통 잠정관리 체어사이드 경로 (확정치료 게이트, 국소마취·벤조카인 보조)
- wiki/drug/analgesics/miroshnychenko-2023-dental-extraction-pain-network-meta.md — 발치 통증 NMA (82 RCT/n=9,095) — 권고의 핵심 직접근거
- wiki/drug/analgesics/miroshnychenko-2023-injectable-topical-anesthetics-acute-pain-sr.md — 국소마취·도포마취 SR 2편 — LA·벤조카인 권고 근거
- papers/carrasco-labra-2024-pharmacologic-management-acute-dental-pain-guideline.pdf 등 papers/ 원본 3종 — verbatim 대조원

# Output

- interactives/2026-08-24_ada-acute-dental-pain-chairside-guide.html — 단일 파일 인터랙티브 (시나리오 A/B 의사결정 흐름 + 용량 참조 + 이행 체크리스트 + GRADE 해설). frontmatter에 `agenda:` 백링크·`source_wiki:` 명시

각 산출물의 frontmatter에 `agenda: agenda/2026-08-24_ada-acute-dental-pain-guideline-interactive.md` 백링크 박을 것.

# Done Criteria

- [x] Box 1 권고 전체 (1, 1.1–1.5, 2, 2.1–2.2, 3) — 강도·확실성 라벨 포함
- [x] Box 2 권고 전체 (1, 2, 2.1–2.4, 3, 4) + 벤조카인 근거 수치 (10%×2 RCT, 20%×3 RCT, 20% vs 10% 무차별)
- [x] Good Practice Statements 양 시나리오 공통 전 항목
- [x] 최대 일일 용량(ibuprofen 2,400 / naproxen sodium 1,100 / acetaminophen 4,000 mg)·연령 구간·오피오이드 금기·동의·보관/폐기·PDMP 안전가드 전부
- [x] FDA 안전성 소통 3건 (naloxone 2020, tramadol 소아금기 2018, codeine/tramadol 12–18경고·수유경고)
- [x] GRADE 강도·확실성 해설 표
- [x] 확신도 등급 명시 (consensus 지침 + 각 권고의 GRADE certainty inline)
- [x] 모든 산출물 frontmatter에 source_wiki / agenda 백링크
- [x] operations-lint 통과

# Notes / Decisions

- 2026-08-24: 지침 본문 내부 불일치 확인 — Box 2 각주는 "2–3일 내 확정치료 불가 시 연락", 본문 Remarks 문단은 "1–2일". 체어사이드 지 2종과 Box 2 각주가 일치하는 **2–3일**을 기본값으로 채택하고 본문 변형은 도구 내 각주로 남김
- 2026-08-24: 코르티코스테로이드 SR (패널 4대 SR 중 1편)은 미보유 — 도구 근거 패널에 gap으로 명시 (권고 1.5 반대 권고의 직접근거 페이지 없음)
- 2026-08-24: tampi-2019(항생제 축)는 개입이 달라 타입화 엣지 없이 prose 링크로만 연결 (INGEST.md 관계 어휘 5종 원칙)

# References

- [[agenda/]] — 해당 없음 (신규 작업)
- 원본: ADA.org/painmanagement (지침 전문·환자 커뮤니케이션 자료)
