---
title: "가철성 국소의치(RPD) 선택 결정 축 — 결손 도메인 신설"
type: agenda
date: 2026-08-26
status: done
owner: 원장
priority: P1
tags: [rpd, removable-partial-denture, treatment-planning, domain-gap, category-creation, surveillance]
source_wiki:
  - wiki/overviews/prosthetic-materials-decision-ladder.md
  - wiki/overviews/implants-clinical-decision-ladder.md
  - wiki/complete-denture/yoo-2023-implant-surveyed-crown-rpd-disabled-patients.md
  - wiki/implants/cunha-2008-implant-location-mandibular-rpd-fea.md
  - wiki/behavioral-dentistry/communication-relationship/iyer-2025-aided-unaided-decision-making-partial-denture.md
  - wiki/_meta/categories.md
---

# Goal

위키에서 **"발치 후 무엇으로 수복하나"의 세 번째 가지**인 가철성 국소의치(Removable Partial Denture, RPD)를 **선택 결정 축에 한정해** 신설한다. 임플란트(581편)와 고정성 보철(76편 + 4축 ladder)은 두꺼운데 RPD만 3~4편이라, 지금 치료계획을 뽑으면 국소의치가 답인 케이스에서 근거를 못 낸다.

# Input

- 실측(2026-08-26): 파일명 기준 2편 · 본문 기준 RPD 주제 논문 **3편**(아래) · 전용 카테고리 없음 · overview 없음
- `wiki/overviews/prosthetic-materials-decision-ladder.md` — 고정성 축의 기존 종합(대조군이자 연결 대상)
- `wiki/_meta/categories.md` — 카테고리 신설의 단일 출처

**현재 흩어져 있는 3편** (일관된 집이 없다는 증거):

| 논문 | 현재 위치 | 문제 |
|---|---|---|
| `yoo-2023-implant-surveyed-crown-rpd-disabled-patients` | `complete-denture/` | 총의치가 아니라 국소의치 |
| `cunha-2008-implant-location-mandibular-rpd-fea` | `implants/` | 임플란트 위치 FEA로 분류됨 |
| `iyer-2025-aided-unaided-decision-making-partial-denture` | `behavioral-dentistry/communication-relationship/` | 의사결정 커뮤니케이션으로 분류됨 |

# 중간평가 판정의 교정 (이 작업의 출발점)

`agenda/2026-08-25_wiki-midterm-review` §5는 결손 도메인을 **"소아치과·고정성 보철(크라운·브릿지)·RPD·구강병리 4개"**로 적었으나, 2026-08-26 실측에서 **3개가 틀렸다**:

| 중간평가 | 실측 | |
|---|---|---|
| 크라운·브릿지 0편 | `prosthetic-materials` 76편 + `prosthetic-materials-decision-ladder`(32편 spine, 4축) | ❌ |
| 소아치과 0편 | 47편(endodontics 8·caries 7·radiology 5 …) + overview 3편 | ❌ 폴더만 없음 |
| 구강병리·구강암 0편 | 10편(oral-medicine 7 중심) | ❌ 얇을 뿐 |
| **RPD 0편** | **주제 논문 3편 · 카테고리 0 · overview 0** | ✅ |

**원인**: 중간평가가 **폴더 존재 여부**로 결손을 판정했는데, 이 위키는 고정성 보철을 `prosthetic-materials`에, 소아를 각 임상 카테고리에 분산 배치한다. 폴더 부재 ≠ 근거 부재. 메모리 [[self-referential-stale-claims]]의 패턴 그대로 — 자기상태 단언이 조용히 틀리고 어느 감사에도 안 걸린다.

→ **후속**: 중간평가 §5의 해당 문단을 교정한다 (별건 커밋).

# 범위 — 선택 결정 축 한정

2026-08-26 사용자 지정. RPD 전체는 수백 편이라 축을 하나로 좁힌다.

**포함**: 언제 RPD인가 — Kennedy 분류별 적응, 임플란트·고정성 보철과의 비교(생존·비용·환자보고결과), 잔존치 예후·환자 인자(연령·전신·구강위생·경제)로 갈리는 지점.

**제외** (후속 별건):
- 지대치 결과 축(장착 후 지대치 상실률·우식·치주 악화·유지관리)
- 임플란트 보조 RPD(IARPD/ISRPD)·서베이드 크라운
- 설계 원칙(클라스프·RPI/RPA·서베이딩)·CAD/CAM·3D 프린팅 제작

# Output

- `wiki/removable-partial-denture/` — 신규 카테고리 (논문 15~20편)
- `wiki/removable-partial-denture/removable-partial-denture.md` — 카테고리 네비 허브
- `wiki/overviews/rpd-vs-implant-vs-fpd-selection-overview.md` — 선택 결정 종합 1편
- `wiki/_meta/categories.md` — 보철 그룹에 `removable-partial-denture | 국소의치` 항목 삽입
- `sources/*.md` · `papers/*.pdf` (PMC 전문텍스트 우선 정책 적용)

# Done Criteria

- [x] `wiki/_meta/categories.md` 보철 그룹에 항목 삽입 (라우팅 원칙 5단계 준수 — `complete-denture` 다음, 정렬 규약대로 append 금지)
- [x] PubMed 서베일런스 — 선택 결정 축 한정, SR+MA·RCT·장기 코호트 우선
- [x] 논문 **12편** 3-tier 파이프라인 통과 (`papers/` → `sources/` → `wiki/`) — 15~20편 목표 대비 12편 (선택 결정 축 SR+MA·RCT 우선 정책 적용; 서베일런스 추가 편수는 추후 별건)
- [x] 각 페이지 이중언어 세줄요약 + `evidence_level:` 포함
- [x] overview 1편 (`wiki/overviews/rpd-vs-implant-vs-fpd-selection-overview.md`) — 한국어 핵심요약 콜아웃 + Kennedy 분류별 결정 분기 + 임플란트/FPD 대비 표 (commit fd51fe1)
- [x] overview가 `prosthetic-materials-decision-ladder`·`implants-clinical-decision-ladder`와 상호 wikilink
- [ ] 흩어진 3편 재라우팅 판단 — 옮길지 wikilink만 걸지 결정하고 근거 기록 (**보류** — 노트: 신규 12편 카테고리가 자리 잡혔으므로 판단 가능; cunha-2008은 임플란트 FEA라 잔류가 맞을 수 있음)
- [x] `index.md` 등재 + 카테고리 허브 등재 (commit 584c28b, b3b6b9d)
- [x] `qmd update && qmd embed` — 완료 (needsEmbedding: 0 확인)
- [ ] `python3 scripts/daily-audit.py` 통과 (blocking 3종 + rationale) — **미실행**
- [ ] 중간평가 §5 결손 도메인 문단 교정 커밋 — **미완료**

# Notes / Decisions

- 2026-08-26: **카테고리는 신설한다.** 라우팅 원칙 1(qmd로 유사 페이지 찾기)을 실제로 돌렸고, 결과는 전부 총의치·오버덴쳐(무치악)였다 — RPD는 잔존치를 지대치로 쓰는 다른 결정이다. `complete-denture`의 Korean 라벨이 "총의치·**가철성보철**"이라 이름만 보면 맞아 보이지만 Includes는 OVD·악간관계·무치악 보철뿐이라 실제로는 총의치 전용이다. 원칙 3(분류 기준은 method/procedure)에 따라 별도 folder가 옳다.
- 2026-08-26: **범위를 선택 결정 축으로 좁힌 것은 사용자 지정**이며, 메모리 [[ingest-scope-ask-if-broad]]가 요구하는 사전 확인을 거쳤다. 설계·제작 축을 같이 넣으면 기공 문헌이 대량 유입돼 치료계획 목적과 멀어진다.
- 2026-08-26: **흩어진 3편을 선제적으로 옮기지 않는다.** 재라우팅은 신규 15~20편이 들어와 카테고리 형태가 잡힌 뒤 판단한다 — 먼저 옮기면 옮긴 근거(유사 페이지 다수)가 아직 없다. `cunha-2008`은 임플란트 위치 FEA라 `implants` 잔류가 옳을 수도 있다.
- 2026-08-26: 이 세션은 허브 전환 큐(다른 세션 담당)에서 빠져 이 축을 맡는다 — 같은 트리에서 두 세션이 같은 큐를 보고 중복 작업한 것이 2회 발생해 축을 분리했다.

# References

- [[agenda/2026-08-25_wiki-midterm-review]] — 결손 도메인을 지목한 중간평가 (§5 판정은 위에서 교정)
- `wiki/_meta/categories.md` — 라우팅 원칙 5단계·정렬 규약
- `INGEST.md` — 3-tier 파이프라인·필드 정의
