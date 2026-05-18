# Wiki Structural Lint Report
**Date**: 2026-05-18
**Scope**: `wiki/` (348 pages) · `sources/` (341) · `papers/` (341) · `index.md`

## Summary

| Check | Count | Status |
|---|---|---|
| [A] wiki에 있으나 index.md 미등재 | 1 | ⚠️ 1 |
| [B] index.md에 있으나 wiki 없음 | 0 | ✅ |
| [C] frontmatter 필수 필드 누락 | 0 | ✅ |
| [D] 한줄요약 누락 | 0 | ✅ |
| [E] 깨진 wikilink | 0 | ✅ |
| [F] sources/ 파일 누락 | 0 | ✅ |
| [G] papers/ 파일 누락 | 0 | ✅ |
| [H] orphan PDF (papers에 있으나 sources 미존재) | 0 | ✅ |
| [I] orphan source (sources 있으나 papers 미존재) | 0 | ✅ |
| [J] pdf_path와 pdf_filename basename 불일치 | 0 | ✅ |
| [K] confidence 어휘 위반 | 0 | ✅ |
| [L] frontmatter 자체 없음 | 0 | ✅ |
| [M] .bak 파일 잔존 | 5 | ⚠️ 5 |
| [N] 중복 title 페이지 | 1 | ⚠️ 1 |
| [O] 중복 DOI 페이지 | 1 | ⚠️ 1 |
| [P] 불완전 DOI (prefix만) | 17 | ⚠️ 17 |


---

## [A] wiki에 있으나 index.md 미등재 (1)

- wiki/inlay/bustamante-hernandez-2020-ceramic-hybrid-composite-onlays-sr-ma.md

## [M] .bak 파일 잔존 (5)

- wiki/endodontics/aae-2021-regenerative-endodontic-clinical-considerations.md.bak
- wiki/endodontics/wei-2022-regenerative-endodontic-expert-consensus.md.bak
- wiki/endodontics/shalavi-2021-qmix-root-canal-overview-iej.md.bak
- wiki/prosthetic-materials/laumacher-2025-lithium-disilicate-single-crowns-overview-sr.md.bak
- wiki/implants/gehrke-2024-implant-dentistry-review-2024.md.bak

## [N] 중복 title 페이지 (1)

- `clinical behavior of ceramic, hybrid and composite onlays: a…` → `wiki/inlay/bustamante-hernandez-2020-ceramic-hybrid-composite-onlays-sr-ma.md`, `wiki/inlay/bustamante-2020-ceramic-hybrid-composite-onlays-sr-ma.md`

## [O] 중복 DOI 페이지 (1)

- `10.3390/ijerph17207582` → `wiki/inlay/bustamante-hernandez-2020-ceramic-hybrid-composite-onlays-sr-ma.md`, `wiki/inlay/bustamante-2020-ceramic-hybrid-composite-onlays-sr-ma.md`

## [P] 불완전 DOI (prefix만) (17)

- `wiki/endodontics/aae-2021-regenerative-endodontic-clinical-considerations.md` → `N/A`
- `wiki/endodontics/aapd-2025-vital-pulp-therapy-permanent-teeth-guideline.md` → `N/A`
- `wiki/endodontics/aapd-2024-vital-pulp-therapy-primary-teeth-guideline.md` → `N/A`
- `wiki/endodontics/shalavi-2021-qmix-root-canal-overview-iej.md` → `N/A`
- `wiki/endodontics/irrigation/shalavi-2021-qmix-root-canal-irrigation-overview.md` → `IEJ-16-2-71`
- `wiki/endodontics/irrigation/mohammadi-2019-smear-layer-irrigants-review.md` → `PMID:31204334`
- `wiki/dental-materials/mohammadi-bassir-2017-grinding-overglazing-polishing-zirconia.md` → `N/A`
- `wiki/dental-materials/sharafeddin-2018-mdp-primers-zirconia-bond.md` → `N/A`
- `wiki/sinus-lift/lateral/jelusic-2014-assessment-implant-stability-sinus-lift.md` → `10.15644/asc48/1/2`
- `wiki/oral-medicine/srivastava-2022-oral-lichen-planus-diagnosis-management-review.md` → `N/A`
- `wiki/oral-medicine/chiang-2021-lichen-planus-malignant-transformation-review.md` → `10.4317/jced`
- `wiki/oral-medicine/mills-2017-aphthous-stomatitis-oral-medicine-review.md` → `N/A`
- `wiki/oral-medicine/belenguer-guallar-2014-recurrent-aphthous-stomatitis-review.md` → `10.4317/jced`
- `wiki/oral-medicine/manfredini-2021-recurrent-aphthous-stomatitis-treatment.md` → `N/A`
- `wiki/immediate-implant/paknejad-2017-flapless-immediate-implant-buccal-gap-rct.md` → `N/A`
- `wiki/immediate-implant/kan-2003-immediate-placement-provisionalization-anterior.md` → `N/A`
- `wiki/immediate-implant/gharpure-2022-socket-shield-conventional-implant-sr-ma.md` → `N/A`

---

## Fixes Applied (Run 1 → Run 2)

- [E] 6개 깨진 wikilink 일괄 수정:
  - `endodontics/aae-2021`, `endodontics/wei-2022`: `[[endodontics/sellami-2023-...]]` → `[[endodontics/regenerative/sellami-2023-...]]`
  - `endodontics/shalavi-2021-qmix-overview-iej`: `[[endodontics/lim-2020-qmix-...]]` → `[[endodontics/irrigation/lim-2020-qmix-...]]`
  - `prosthetic-materials/laumacher-2025`: `[[prosthetic-materials/almashaan-2023-...]]` → `[[dental-materials/almashaan-2023-...]]`; `[[prosthetic-materials/malament-2021-...]]` → `[[inlay/malament-2021-...]]`
  - `implants/gehrke-2024`: `[[implants/smeets-2016-...]]` → `[[implants/surface/smeets-2016-...]]`
- [A] `index.md`: `[[inlay/bustamante-hernandez-2020-...]]` → `[[inlay/bustamante-2020-...]]` (실제 파일명과 일치)

## Outstanding Issues — Sandbox 권한 제한으로 사용자 직접 처리 필요

### 1. `.bak` 5개 파일 제거
```bash
cd /Users/oracleneo/llm-wiki
find wiki -name '*.bak' -delete
```

### 2. 중복 페이지 정리 — `bustamante-hernandez-2020` 3-tier 삭제
이유: 같은 논문 (DOI `10.3390/ijerph17207582`) 2개 wiki 페이지 존재. `bustamante-2020-…` 가 51줄로 더 풍부 (vs 42줄). 더 짧은 `bustamante-hernandez-2020-…` 측 3-tier 모두 삭제.
```bash
cd /Users/oracleneo/llm-wiki
rm wiki/inlay/bustamante-hernandez-2020-ceramic-hybrid-composite-onlays-sr-ma.md
rm sources/bustamante-hernandez-2020-ceramic-hybrid-composite-onlays-sr-ma.md
rm papers/bustamante-hernandez-2020-ceramic-hybrid-composite-onlays-sr-ma.pdf
```

### 3. 불완전 DOI 보완 (2건)
- `wiki/oral-medicine/chiang-2021-lichen-planus-malignant-transformation-review.md` — DOI `10.4317/jced` (suffix 누락)
- `wiki/oral-medicine/belenguer-guallar-2014-recurrent-aphthous-stomatitis-review.md` — DOI `10.4317/jced` (suffix 누락)
원논문에서 정확한 DOI 확인 후 frontmatter 수정 권장 (CLAUDE.md no web search 원칙에 따라 사용자 결정).

---

## 다음 lint 실행
위 3개 사용자 액션 완료 후 다시 실행 시 [A], [M], [N], [O] 모두 ✅로 전환 예상. [P] 불완전 DOI는 사용자 결정 영역.