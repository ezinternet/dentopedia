# Wiki Structural Lint Report
**Date**: 2026-05-18 (Run 3 — post user cleanup)
**Scope**: `wiki/` (347) · `sources/` (340) · `papers/` (340) · `index.md`

## Summary

| Check | Count | Status |
|---|---|---|
| [A] wiki에 있으나 index.md 미등재 | 0 | ✅ |
| [B] index.md에 있으나 wiki 없음 | 0 | ✅ |
| [C] frontmatter 필수 필드 누락 | 0 | ✅ |
| [D] 한줄요약 누락 | 0 | ✅ |
| [E] 깨진 wikilink | 4 | ⚠️ 4 |
| [F] sources/ 파일 누락 | 0 | ✅ |
| [G] papers/ 파일 누락 | 0 | ✅ |
| [H] orphan PDF (papers→sources 미존재) | 0 | ✅ |
| [I] orphan source (sources→papers 미존재) | 0 | ✅ |
| [J] pdf_path·pdf_filename 불일치 | 0 | ✅ |
| [K] confidence 어휘 위반 | 0 | ✅ |
| [L] frontmatter 자체 없음 | 0 | ✅ |
| [M] .bak 파일 잔존 | 0 | ✅ |
| [N] 중복 title 페이지 | 0 | ✅ |
| [O] 중복 DOI 페이지 | 0 | ✅ |
| [P] 불완전 DOI (cosmetic) | 5 | ⚠️ 5 |


---

## [E] 깨진 wikilink (4)

- `wiki/inlay/hassan-2024-lithium-disilicate-vs-nanoceramic-onlay-2year-rct.md` → [[inlay/bustamante-hernandez-2020-ceramic-hybrid-composite-onlays-sr-ma]]
- `wiki/inlay/souza-2021-lithium-disilicate-vs-resin-composite-cadcam-onlay.md` → [[inlay/bustamante-hernandez-2020-ceramic-hybrid-composite-onlays-sr-ma]]
- `wiki/inlay/bresser-2023-intracoronal-restorations-longevity-sr-ma.md` → [[inlay/bustamante-hernandez-2020-ceramic-hybrid-composite-onlays-sr-ma]]
- `wiki/dental-materials/warreth-2020-all-ceramic-restorations-review.md` → [[inlay/bustamante-hernandez-2020-ceramic-hybrid-composite-onlays-sr-ma]]

## [P] 불완전 DOI (cosmetic) (5)

- `wiki/endodontics/irrigation/shalavi-2021-qmix-root-canal-irrigation-overview.md` → `IEJ-16-2-71`
- `wiki/endodontics/irrigation/mohammadi-2019-smear-layer-irrigants-review.md` → `PMID:31204334`
- `wiki/sinus-lift/lateral/jelusic-2014-assessment-implant-stability-sinus-lift.md` → `10.15644/asc48/1/2`
- `wiki/oral-medicine/chiang-2021-lichen-planus-malignant-transformation-review.md` → `10.4317/jced`
- `wiki/oral-medicine/belenguer-guallar-2014-recurrent-aphthous-stomatitis-review.md` → `10.4317/jced`

---

## Run 2 → Run 3 변경사항 (사용자 cleanup 반영)

- [M] `.bak` 5개 → 0건 ✅
- [N] 중복 title `bustamante-…-onlays-sr-ma` → 1건 → 0건 ✅
- [O] 중복 DOI `10.3390/ijerph17207582` → 1건 → 0건 ✅
- [A] `bustamante-2020` index 재정렬 후 정합 ✅
- wiki 348 → 347, sources 341 → 340, papers 341 → 340