---
title: "Supersession + confidence-decay 신호 세팅 (forward-only)"
type: agenda
date: 2026-05-31
status: done
owner: 원장
priority: P1
tags: [meta, supersession, decay, lint, audit, infrastructure, living-document]
source_wiki: []
output_wiki:
  - CLAUDE.md
---

# Goal

llm-wiki의 living-document 원칙(논문 페이지는 ingest snapshot이 아니라 후속 근거로 갱신)을 **수동 산문 갱신에서 신호 기반 audit으로 전환**. rohitg00 LLM Wiki v2의 supersession·decay 개념을 차용하되, 네 인프라의 교훈(mtime은 거짓말한다 → overview-thesis-staleness.py)을 반영해 **decay는 저장하지 않고 audit 시점에 계산**.

성공 기준 한 줄: `python3 scripts/daily-audit.py` 실행 시 logs/에 ① 깨진 superseded_by 링크, ② 필드↔배너 불일치, ③ decay 후보(고근거·5년↑·미대체)가 박혀 있어야 한다.

# 설계 원칙 (Notes/Decisions에서 승격)

- **저장하는 건 사실(superseded_by)뿐. decay는 계산 신호.** 저장된 decay 값은 그 자체가 stale해진다 — overview-thesis-staleness.py가 존재하는 이유와 동일한 함정 회피.
- **supersession은 임상 판단이지 기계 자동할당 불가.** 신규≠우위(2026 narrative-review가 2022 sr+ma를 못 이긴다). 필드는 사람/에이전트가 ingest 시 박고, audit은 깨진 링크·후보 flagging만.
- **forward-only인데도 옛 페이지를 갱신한다.** 새 논문 ingest 시 "이게 기존 페이지를 이기나?" 확인 → 이기면 *옛* 페이지에 필드를 박음. bulk backfill 불필요(Why-Ingested grandfather와 동일).
- **scope 구분(full | partial).** kim-2000(anticoagulation 절만 outdated, 나머지 방어 가능)·gaspar-2022(1차 근거는 밀렸으나 최초 human-only 합성으로 가치 유지) 같은 케이스를 full로 과대표시하지 않기 위함.

# 스키마

superseded(=구판) 페이지의 frontmatter에:

```yaml
superseded_by: <newer-stem>           # 복수면 comma-separated. wiki 내 실존 stem이어야.
superseded_scope: full                # full | partial
```

본문 최상단(frontmatter 직후, ## One-line Summary 앞)에 배너 callout:

```markdown
> [!warning] Superseded (full) → [[newer-stem]]
> 한 줄 사유. (set YYYY-MM-DD)
```

partial이면 `[!note] Partially superseded`. Obsidian·Quartz 둘 다 callout 네이티브 렌더 — 빌드 변경 없음.

# decay 임계값 (디폴트 — 원장 승인 2026-05-31)

- 대상 confidence: `sr+ma`, `sr`, `rct` (고근거만)
- 경과: `date:` 기준 ≥ 5년 (즉 2021-05-31 이전) AND
- `superseded_by` 없음
- → "still current 검증 필요" 후보로 flagging (gold standard로 유지 중일 수도, 아무도 안 본 것일 수도)

# Output

- `scripts/supersession-audit.py` — 깨진 링크 / 필드↔배너 sync / decay 후보. signal, non-blocking.
- `scripts/daily-audit.py` — AUDITS에 1행 추가 (9→10 audit).
- `CLAUDE.md` — superseded_by 스키마, ingest Step 대체 확인 절차, Daily Audit 표 행 추가.
- backfill 3페이지: lages-2018(→tisci-2026, full), padhye-2020(→inchingolo-2021, full), gaspar-2022(→lima-monteiro-2024·kalra-2025, partial).
- `logs/2026-05-31_supersession.log` — 첫 실행 결과.

# Done Criteria

- [ ] supersession-audit.py 작성·실행, 깨진 링크 0
- [ ] daily-audit.py 통합, 전체 실행 시 classic audit(lint·operations·orphan·rationale) 통과 유지
- [ ] CLAUDE.md 스키마·ingest 절차·audit 표 갱신
- [ ] backfill 3페이지 필드+배너 삽입, 필드↔배너 sync 통과
- [ ] decay 후보 수치 logs/에 기록

# Notes / Decisions

- 2026-05-31: "40개 prose-flagged" 정밀 검토 결과 진짜 intra-wiki 전체대체는 3건(2 full + 1 partial). 나머지는 외부 구판 대체(aapd-2024, wang-2025, shiboski-2016 등)·개념 진화(abraham-2014)·절단위 outdated(kim-2000, 이미 [wiki-living-document] 태그로 처리됨)라 제외. → supersession은 backfill보다 forward 트리거가 본체라는 가설 실측 확인.

# References

- [[agenda/2026-05-26_synthesis-enforcement-setup]] — 동일 비대칭 설계 철학(ingest friction↑ / 유지 friction↓)의 선행 작업
- rohitg00 LLM Wiki v2 (supersession·decay·consolidation tier 원개념): https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2
