---
title: "implants/soft-tissue 미합성 7편 → overview 합성"
type: agenda
date: 2026-08-04
status: done
owner: 원장
priority: P1
tags: [implants, soft-tissue, keratinized-mucosa, overview]
source_wiki:
  - wiki/implants/soft-tissue/
---

# Goal

`implants/soft-tissue` 카테고리의 미합성 7편을 종합해 각질화 점막 (Keratinized Mucosa, KM) 증대술 술식 스펙트럼 overview 페이지를 생성한다. 술식 선택 기준 + 증거 수준 비교 레퍼런스로서 진료 중 즉시 참조 가능하게.

# Input

미합성 7 stems (implants/soft-tissue):

- wiki/implants/soft-tissue/bruschi-2014-partial-thickness-flap-keratinized-gingiva-implant.md
- wiki/implants/soft-tissue/de-greef-2023-mesh-fgg-keratinized-mucosa-implant.md
- wiki/implants/soft-tissue/han-2021-apf-keratinized-gingiva-implant-ridge-augmentation.md
- wiki/implants/soft-tissue/jung-2021-flap-folding-suture-soft-tissue-implant.md
- wiki/implants/soft-tissue/kim-2015-hard-soft-tissue-esthetic-zone.md
- wiki/implants/soft-tissue/thoma-2014-soft-tissue-augmentation-implant-sr.md
- wiki/implants/soft-tissue/wang-2024-mrarf-modified-roll-envelope-apf-implant.md

# Output

- wiki/overviews/implants-soft-tissue-km-augmentation-techniques.md

해당 페이지 frontmatter에 `agenda: agenda/2026-08-04_overview-implants-soft-tissue.md` 백링크 박을 것.

# Done Criteria

- [x] 7편의 술식 분류 및 핵심 수치 통합 표 (술식 / 적응증 / 증거 수준 / KM 증가량 or 효과)
- [x] 각 술식 임상 시나리오 분기 walk-through
- [x] 확신도 등급(SR+MA / RCT / consensus / 전문가 의견) 명시
- [x] `## 한국어 핵심요약` 블록 최상단 배치 (~10 bullets)
- [x] 이중언어 세줄요약 (`## Three-line Summary` + `## 세줄요약`)
- [x] 모든 인용 stem이 overview 내 `[[wikilink]]` 또는 `sources/` 참조로 연결됨
- [x] 성공 기준: "이 overview를 열면 KM 증대 술식 선택 시 어떤 술식을 언제 쓰는지, 각 술식의 근거 수준이 한눈에 파악된다"

# Notes / Decisions

- 2026-08-04: 주간 category-overflow 스크립트 결과(2026-08-02 실행) 기반 선정. implants/soft-tissue 38편 중 31편 합성, 잔여 7편 합성.
- 이 7편은 FGG, APF, roll flap, flap folding, mesh-assisted FGG 등 술식 스펙트럼을 망라하므로 단일 overview로 통합 적합 판단.

# References

- [[agenda/_template]]
