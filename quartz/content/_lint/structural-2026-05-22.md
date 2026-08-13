# Wiki Structural Lint Report
**Date**: 2026-05-22
**Scope**: `wiki/` (630 pages) · `sources/` (611) · `papers/` (611) · `index.md`
**Trigger**: post-ingest of 9 PDFs into new `evidence-appraisal` category + 1 overview synthesis page

## Summary

| Check | Count | Status | Note |
|---|---|---|---|
| [A] wiki 페이지가 index.md에 미등재 | 1 | ⚠️ | wiki/index.md 자체 |
| [B] index.md 링크인데 wiki 없음 | 0 | ✅ | |
| [C] frontmatter 필수 필드 누락 | 13 | ⚠️ | 1 cosmetic (anonymous-nd year null) + 12 overview 페이지 (이전부터) |
| [D] 한줄요약 누락 | 1 | ⚠️ | wiki/index.md |
| [E] 깨진 wikilink | 73 | ⚠️ | 이전부터 누적, cross-category path 오류 |
| [F] sources/ 파일 누락 | 1 | ⚠️ | parra-gatica — lint script 결함 (실제 파일 존재) |
| [G] papers/ 파일 누락 | 0 | ✅ | |
| [H] orphan PDF | 0 | ✅ | |
| [I] orphan source | 0 | ✅ | |
| [J] pdf_path·pdf_filename 불일치 | 0 | ✅ | |
| [K] confidence 어휘 위반 | 6 | ⚠️ | 이전 overview 6편 `claude-synthesis` 사용 |
| [L] frontmatter 자체 없음 | 0 | ✅ | |
| [M] .bak 파일 잔존 | 0 | ✅ | |
| [N] 중복 title 페이지 | 2 | ⚠️ | 4쌍 중복 stem (이전부터) |
| [O] 중복 DOI 페이지 | 7 | ⚠️ | 2쌍 실제 중복 + 5건 `N/A`/`unknown` grouping |
| [P] 불완전 DOI (cosmetic) | 22 | ⚠️ | `N/A`/`unknown`/`PMID:...`/축약 DOI |

---

## 🟢 이번 ingest (9편 + 1 overview) 결과

**모든 critical check 통과** ([B][E][F][G][H][I][J][L][M][N][O] 영역에서 이번 작업 신규 위반 0건).

| Page | 한줄요약 | frontmatter | confidence | DOI | source/papers 매칭 |
|---|---|---|---|---|---|
| shin-ih-2009-... | ✅ | ✅ | narrative-review ✅ | null (학회 자료, 없음) | ✅ |
| kiriakou-2014-... | ✅ | ✅ | narrative-review ✅ | 10.1186/s40510-014-0058-5 | ✅ |
| flechner-2011-... | ✅ | ✅ | narrative-review ✅ | 10.4103/0970-1591.91446 | ✅ |
| barraclough-2011-... | ✅ | ✅ | narrative-review ✅ | 10.1097/JTO.0b013e31821b10ab | ✅ |
| anonymous-nd-... | ✅ | ⚠️ year null | narrative-review ✅ | null (worksheet) | ✅ |
| shin-wj-2015-... | ✅ | ✅ | narrative-review ✅ | 10.7599/hmr.2015.35.1.9 | ✅ |
| monaghan-2021-... | ✅ | ✅ | narrative-review ✅ | 10.3390/ijerph18115669 | ✅ |
| nam-2012-... | ✅ | ✅ | narrative-review ✅ | 10.5124/jkma.2012.55.6.573 | ✅ |
| darrigo-2024-... | ✅ | ✅ | narrative-review ✅ | 10.1093/ckj/sfae197 | ✅ |
| overviews/evidence-appraisal-toolkit | ✅ | ✅ | narrative-review ✅ | n/a (synthesis) | n/a |

**anonymous-nd `year: null` 처리**:
원본 worksheet에 저자·연도·저널·DOI 명시 없음. 임의 추정은 정직하지 않음. wiki 본문에 "인용 불가, 학습용으로만 사용" 명시. → cosmetic flag로 유지.

---

## ⚠️ 이전부터 누적된 문제 (이번 ingest와 무관, 결정 필요)

### [A][D] wiki/index.md 존재
- `wiki/index.md`가 별도로 있음. root `index.md`가 메인 카탈로그라 중복 가능성.
- 결정 필요: (1) wiki/index.md 삭제, (2) wiki/ 디렉터리 안 navigation index로 명시적 유지, (3) Obsidian 호환 wiki 홈으로 frontmatter 보강.

### [C][K] overview 페이지 frontmatter 미완 (12개)
대상: `third-molar-ian-risk-protocol.md`, `sinus-lift-technique-selection.md`, `endodontic-access-cavity-decision-tree.md`, `implant-surface-comparison.md`, `isq-loading-threshold.md`, `immediate-implant-conditions.md`, `sinus-lift-isq-loading-timing.md`, `irrigation-activation-comparison.md`, `anticoagulant-antiplatelet-dental-protocol.md`, `mb2-detection-strategy.md`, `eal-working-length-protocol.md`, +1.
누락: `authors`, `year`, `confidence`.
[K] 6편은 `confidence: claude-synthesis` 사용 — CLAUDE.md vocabulary 위반.

**제안**: overview 페이지용 표준 frontmatter 통일.
- `authors: synthesis (llm-wiki)`
- `year: <작성연도>` + `date: YYYY-MM-DD`
- `confidence: narrative-review` (synthesis는 narrative-review에 매핑하거나 CLAUDE.md에 새 어휘 `synthesis` 추가)

이번에 작성한 `evidence-appraisal-toolkit.md`는 이 패턴을 따랐음 (참고용).

### [E] 깨진 wikilink (73건)
대부분 cross-category 참조에서 path 오류. 예:
- `digital-workflow/jamil-2020-...` → `sinus-lift/lateral/padhye-2020-...` 링크는 실제 파일 존재. **lint script 버그 가능성**: relative path resolution 점검 필요.
- `oral-surgery/al-maawi-2021-...` → `bone-regeneration/` (slash로 끝남, 페이지 미지정) — 실제 오류.
- `digital-workflow/schiavon-2025-...` → `sources/schiavon-2025-...` — sources 디렉터리 직접 참조, wikilink 스타일 위반.

**제안**: 73건을 자동 분류 (false-positive vs 실제 오류) 후 batch fix.

### [F] sources/ 파일 누락 (1) — lint script 버그
- `wiki/resin/parra-gatica-2023-flowable-bulk-fill-composites-sr.md`의 `source:` 필드가 `.md` suffix 없음.
- 실제 source 파일은 존재 (`sources/parra-gatica-2023-flowable-bulk-fill-composites-sr.md`).
- lint script 보완: `source` 필드에 `.md` suffix 자동 append 후 검사.

### [N][O] 중복 stem (4쌍)
| 쌍 | 결정 필요 |
|---|---|
| `vidovic-juras-2024-antibiotic-prophylaxis-dental-procedures.md` vs `-review.md` | 동일 paper |
| `watson-2022-acetaminophen-codeine-ibuprofen-...` vs `watson-2022-ibuprofen-codeine-...` | 동일 paper |
| `pjetursson-2026-metal-ceramic-allceramic-crowns-sr-ma.md` vs `metal-ceramic-all-ceramic-crowns-survival-sr-ma.md` | 동일 paper |
| `manresa-2018-supportive-periodontal-therapy-cochrane.md` vs `-cochrane-sr.md` | 동일 paper |

**제안**: 각 쌍 중 한쪽 유지·다른 쪽 제거 + index.md 갱신. PDF/source orphan check 함께.

[O] 'N/A'/'unknown'으로 grouping된 5건은 실제 중복 아님 (DOI 모르는 페이지들이 우연히 같은 placeholder 사용). DOI를 `null`로 통일하면 [O]에서 사라짐.

### [P] 불완전 DOI (22건, cosmetic)
- `N/A` / `unknown` / `PMID:...` / `IEJ-16-2-71` 형식. wiki 정합성에 직접 영향 없음.
- **제안**: `N/A` `unknown`은 `null`로 통일 (DOI 없음 명시), PMID는 별도 frontmatter 필드 `pmid:` 도입.

---

## 다음 액션 (우선순위)

1. **wiki/index.md 처리 방향 결정** (사용자) — 삭제 vs 유지.
2. **중복 stem 4쌍 정리** (사용자 결정 후 자동 처리 가능) — orphan PDF/source check 동반.
3. **overview frontmatter 표준화** — `synthesis` confidence 어휘를 CLAUDE.md에 추가하거나 `narrative-review`로 통일.
4. **[E] 깨진 wikilink 73건** — lint script 보완 + 실제 오류 batch fix.
5. **lint script 자체 보완** — `source:` 필드 `.md` suffix 자동 처리, `N/A`/`unknown` placeholder를 `null`과 동등 취급.

---

## Run history
- 2026-05-18-run4 → 2026-05-22 (this run)
- 신규 카테고리: `evidence-appraisal/` (+9 pages)
- 신규 overview: `evidence-appraisal-toolkit` (+1)
- wiki 페이지 총수: 619 → 630 (+11 net; -1은 lint script 카운팅 차이일 수 있음, 확인 필요)
- 카테고리 표 (CLAUDE.md) 1행 추가
