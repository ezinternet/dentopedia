# Wiki Structural Lint Report
**Date**: 2026-05-16 (run 1 → run 2)
**Scope**: `wiki/` — 243 pages across all category folders  
**Checks**: orphan pages · ghost index entries · missing frontmatter · 한줄요약 · broken wikilinks · missing source/PDF files

## Result: ✅ All Clear

| Check | Count | Status |
|---|---|---|
| [A] Orphan (wiki 있으나 index 없음) | 0 | ✅ |
| [B] Ghost (index 있으나 wiki 없음) | 0 | ✅ |
| [C] Missing frontmatter fields | 0 | ✅ |
| [D] Missing 한줄요약 | 0 | ✅ |
| [E] Broken internal wikilinks | 0 | ✅ |
| [F] Source file missing | 0 | ✅ |
| [G] PDF file missing | 0 | ✅ |

## Fixes Applied — Run 2
- [B] `index.md` 4번째 라인: 포맷 예시 `[[category/stem]]` → backtick 표기로 변경 (lint 오탐 제거)
- [C] Lint 로직: overview 타입 페이지에서 `source` 필드도 exempt 추가 (overview는 `source_papers:` 다중 소스 사용)
- 신규 ingest 4편 추가 완료 (drug/): feldman-2024, miroshnychenko-2023, watson-2022, gaballah-2025

## Fixes Applied — Run 1
- [C] `overviews/eal-working-length-protocol`, `overviews/sinus-lift-isq-loading-timing` → `type: overview` 추가 (단일논문 필드 면제 처리)
- [E] Broken wikilinks 7건 수정:
  - `bone-regeneration/ayoub-2018`: `bone-regeneration/ayoub-2021` → `implants/ayoub-2021`
  - `bone-regeneration/jung-2025`: `bone-regeneration/hong-2024` → `implants/hong-2024`
  - `digital-workflow/oh-2023`: `implants/isq/versiani-2022` → `endodontics/eal/versiani-2022`
  - `digital-workflow/vankos-2026`: `digital-workflow/heimes-2025` → `immediate-implant/heimes-2025`
  - `immediate-implant/araujo-2005`, `botticelli-2004`, `chappuis-2017`: `immediate-implant/araujo-2005-dimensional` → `bone-regeneration/araujo-2005-dimensional`
- [F] `endodontics/eal/shacham-2020`: source 필드 `.pdf` → `.md`
