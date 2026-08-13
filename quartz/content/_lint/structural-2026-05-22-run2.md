# Wiki Structural Lint Report
**Date**: 2026-05-22 (Run 2 — post-cleanup)
**Scope**: `wiki/` (626 pages) · `sources/` (607) · `papers/` (607) · `index.md`
**Tool**: `wiki/_lint/lint.py` v2 (보완본)

## Summary

| Check | Count | Status | Δ from Run 1 |
|---|---|---|---|
| [A] wiki 페이지가 index.md에 미등재 | 0 | ✅ | -1 |
| [B] index.md 링크인데 wiki 없음 | 0 | ✅ | 0 |
| [C] frontmatter 필수 필드 누락 | 1 | ⚠️ cosmetic | -12 |
| [D] 한줄요약 누락 | 0 | ✅ | -1 |
| [E] 깨진 wikilink | 0 | ✅ | -73 |
| [F] sources/ 파일 누락 | 0 | ✅ | -1 |
| [G] papers/ 파일 누락 | 0 | ✅ | 0 |
| [H] orphan PDF | 0 | ✅ | 0 |
| [I] orphan source | 0 | ✅ | 0 |
| [J] pdf_path·pdf_filename 불일치 | 0 | ✅ | 0 |
| [K] confidence 어휘 위반 | 0 | ✅ | -6 |
| [L] frontmatter 자체 없음 | 0 | ✅ | 0 |
| [M] .bak 잔존 | 0 | ✅ | 0 |
| [N] 중복 title 페이지 | 0 | ✅ | -2 |
| [O] 중복 DOI 페이지 | 0 | ✅ | -7 |
| [P] 불완전 DOI (cosmetic) | 0 | ✅ | -22 |

**전체 위반: 119 → 1** (cosmetic만 잔류)

## 잔류 [C] 1건 — 의도적

- `wiki/evidence-appraisal/anonymous-nd-systematic-review-critical-appraisal-worksheet.md` → `year: null`
  - 익명·날짜 미상 worksheet. 임의 추정 회피하기 위해 의도적으로 null 유지. wiki 본문에 "인용 불가, 학습용으로만 사용" 명시.

---

## Run 1 → Run 2 변경

### 1. wiki/index.md (Task #7)
- 이전: root `index.md`의 stale snapshot (564 lines, 2026-05-20)
- 처리: redirect navigation stub으로 갱신 (root `index.md`가 결정판으로 명시)
- shell 권한 제한으로 직접 삭제 불가, Write로 교체

### 2. 중복 stem 4쌍 정리 (Task #8)
삭제된 stem (drop, 12 파일):
- `vidovic-juras-2024-antibiotic-prophylaxis-dental-procedures-review` (wiki+source+pdf)
- `watson-2022-ibuprofen-codeine-third-molar-sr-ma` (wiki+source+pdf)
- `pjetursson-2026-metal-ceramic-allceramic-crowns-sr-ma` (wiki+source+pdf)
- `manresa-2018-supportive-periodontal-therapy-cochrane` (wiki+source+pdf)

Keep 결정 기준: stem 충실도 + frontmatter 완성도 + 더 긴 본문.

각 쌍에서 keep된 페이지로 wikilink 12파일 자동 fix.
index.md 4개 중복 entry 정리 (keep 페이지에 중복 정보 흡수).

PDF 611 → 607, sources 611 → 607.

### 3. Overview frontmatter 표준화 (Task #9)
- CLAUDE.md confidence 어휘에 `synthesis` 추가
- 17개 overview 페이지 frontmatter 일괄 보강 (authors / year / date / confidence)
- 기존 `confidence: claude-synthesis` 6편 → `synthesis`로 정규화

### 4. lint script 보완 (Task #10)
`wiki/_lint/lint.py` v2 작성. 변경점:
- `source:` 필드 `.md` suffix 자동 처리 ([F] false positive 제거)
- `N/A`, `unknown`, `n/a`, `NA` → `null`과 동치 처리 ([O][P] false positive 제거)
- wikilink relative path 정확한 resolution — 전체 wiki stem 인덱스 → bare stem 매칭 → cross-category 매칭
- overview는 `pdf_path/pdf_filename/source` 면제
- navigation stub (`wiki/index.md`)은 paper-field 면제
- `synthesis` confidence vocab 추가

### 5. 깨진 wikilink 처리 (Task #10)
- 63건 식별 후:
  - 31건: path 자동 교정 (e.g., `sinus-lift/lateral/padhye-2020-...` → `implants/padhye-2020-...`)
  - 25건: 의미 없는 link 자동 삭제 (`sources/...`, naked category, slash-ending)
  - 7건: 미ingest paper 참조 → `~~(미ingest) <stem>~~` strike-through로 변환 (의미 보존)

### 6. DOI 정리
- 5개 incomplete DOI (`10.4317/jced` 축약, `IEJ-16-2-71`, `PMID:...`) → `null`로 통일 (wiki + sources 동기화)

---

## 향후 ingest 후보 (Run 2에서 strike-through로 식별)
- `oral-surgery/li-2022-inferior-alveolar-nerve-position-injury-sr-ma` (2건에서 참조)
- `sinus-lift/lateral/lundgren-2004-graftless-lateral-sinus-lift`
- `implants/esposito-2014-short-vs-long-implants`
- `sinus-lift/lateral/pjetursson-2008-sinus-elevation-survival`
- `overviews/tmd-clinical-pathway-2025` (미래 overview placeholder)

## 사용법
```bash
cd /Users/oracleneo/llm-wiki
python3 wiki/_lint/lint.py           # 콘솔 출력
python3 wiki/_lint/lint.py --json    # lint-latest.json 도 생성
```
