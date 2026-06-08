---
title: "골밀도화 (Osseodensification, OD) 전체 그림 — overview·interactive·slide 통합 작업"
type: agenda
date: 2026-05-25
status: done
owner: 원장
priority: P1
tags: [osseodensification, densahbur, implants, overview, interactive, slide]
source_wiki:
  - wiki/implants/fontes-pereira-2023-osseodensification-osteotomy-alternative-sr.md
  - wiki/implants/huwais-2017-novel-osseous-densification-osteotomy-primary-stability.md
  - wiki/implants/isq/althobaiti-2023-osseodensification-conventional-drilling-isq-sr.md
  - wiki/implants/isq/konuklu-2026-five-osteotomy-protocols-isq-rct.md
  - wiki/sinus-lift/transcrestal/starch-jensen-2025-transcrestal-sinus-osseodensification-meta-analysis.md
  - wiki/sinus-lift/transcrestal/el-ghobashy-osseodensification-vs-osteotome-transcrestal-sinus.md
  - wiki/sinus-lift/transcrestal/gaspar-2025-osseodensification-crestal-maxillary-sinus-elevation-narrative-review.md
  - wiki/sinus-lift/transcrestal/shalash-2023-crestal-sinus-elevation-densah-oblique.md
output_wiki:
  - wiki/overviews/osseodensification-clinical-applications.md
---

# Goal

Fontes Pereira et al. 2023 (JCM, SR, PMID 38002660)의 4-application taxonomy를 spine으로 삼아, llm-wiki에 흩어진 OD 관련 페이지를 hub-and-spoke로 묶는다. 산출물 3종 (overview·interactive·slide)으로 "한 편으로 전체 그림 확보" 요건 충족.

# Input

근거가 될 기존 wiki 페이지:

- wiki/implants/fontes-pereira-2023-osseodensification-osteotomy-alternative-sr.md — **spine SR**, 4 적용 시나리오 taxonomy
- wiki/implants/huwais-2017-novel-osseous-densification-osteotomy-primary-stability.md — OD 메커니즘 원위논문 (in vitro)
- wiki/implants/isq/althobaiti-2023-osseodensification-conventional-drilling-isq-sr.md — ISQ outcome SR
- wiki/implants/isq/konuklu-2026-five-osteotomy-protocols-isq-rct.md — 최근 RCT
- wiki/sinus-lift/transcrestal/starch-jensen-2025-transcrestal-sinus-osseodensification-meta-analysis.md — sub-antral 적용 SR+MA
- wiki/sinus-lift/transcrestal/el-ghobashy-osseodensification-vs-osteotome-transcrestal-sinus.md — sub-antral RCT
- wiki/sinus-lift/transcrestal/gaspar-2025-osseodensification-crestal-maxillary-sinus-elevation-narrative-review.md
- wiki/sinus-lift/transcrestal/shalash-2023-crestal-sinus-elevation-densah-oblique.md
- wiki/overviews/d4-bone-densah-protocol.html — 저밀도골 적용 인터랙티브 (이미 존재; 본 작업물은 cross-link)
- wiki/overviews/sinus-lift-technique-selection.md — 술식 선택 (이미 존재; cross-link)

# Output

- `wiki/overviews/osseodensification-clinical-applications.md` — overview (synthesis)
- `interactives/2026-05-25_osseodensification-navigator.html` — 시나리오 → 근거·prep parameter 네비게이터
- `slides/2026-05-25_seminar_osseodensification-whole-picture.md` — 강의·세미나용 hub-and-spoke 도식

각 산출물 frontmatter에 `agenda: agenda/2026-05-25_osseodensification-whole-picture.md` 백링크 박을 것.

# Done Criteria

- [ ] Overview에 4 적용 시나리오 walk-through + 각 시나리오 최강 근거 1편 명시 (sr+ma 우선)
- [ ] Mermaid hub-and-spoke 1장
- [ ] Outcome 매트릭스 (insertion torque, ISQ, BIC, survival) — Fontes Pereira 2023 표 기반
- [ ] 확신도 등급(sr+ma / sr / rct / in-vitro / claude해석) 모든 claim에 부착
- [ ] Interactive: 4개 시나리오 카드 + 클릭 시 적용 방법·rpm·근거·주의점
- [ ] Slide: 12장 내외, hub-and-spoke 1장 + 시나리오별 2장씩
- [ ] index.md에 overview·interactive·slide entry 추가
- [ ] wiki/implants/fontes-pereira-2023-...md에 새 overview 백링크 + `## Clinical Applications` 섹션 추가

# Notes / Decisions

- 2026-05-25: Fontes Pereira 2023을 spine으로 선택한 이유 — JCM 2023, PRISMA, PROSPERO 등록, search 2016–2023 (가장 최근까지 cover), 4 적용 시나리오를 명시적으로 분류한 유일한 SR
- 2026-05-25: 본 overview는 `d4-bone-densah-protocol.html`·`sinus-lift-technique-selection.md`와 중복 회피 — D4 protocol과 sinus 술식은 각각 그쪽에 위임, 본 페이지는 4-application 전체 entry point 역할
- 2026-05-25: [[feedback_wiki-living-document]] 원칙 적용 — Fontes Pereira 2023의 "evidence quality low–moderate" 경고를 page top에 명시하고, 이후 RCT·SR이 들어올 때 갱신 표시

# References

- [[wiki/implants/fontes-pereira-2023-osseodensification-osteotomy-alternative-sr]]
