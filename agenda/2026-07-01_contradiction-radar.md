---
title: "논쟁 레이더 — 위키 내부 상충 근거 자동 수집 인터랙티브"
type: agenda
date: 2026-07-01
status: in-progress
owner: 원장
priority: P1
tags: [interactive, relations, meta, class-a]
---

# Goal

위키의 `relations: type: contradicts`(정면충돌) · `type: refines`(조건부 반박) typed edge를 전부 긁어, **위키 안에서 근거가 서로 싸우고 있는 지점**만 임상 도메인별로 모은 self-contained 인터랙티브를 자동 생성한다. 임상가가 알고 싶은 건 정답이 아니라 "어디가 아직 회색지대인가" — 그 회색지대 지도를 만든다. Class A(숫자=repo 상태)이므로 배포 때 재생성.

# Input

- 전체 `wiki/**/*.md` frontmatter의 `relations:` 블록 (contradicts/refines edge) — 단일 진실원천
- 각 페이지 frontmatter(title/authors/year/confidence/category) + `## One-line Summary` / `## 한줄요약` — 논쟁 양측의 thesis
- 참고: `scripts/build-overviews-map.py`, `scripts/relations-audit.py` — auto-gen 인터랙티브·relations 파싱 컨벤션

# Output

- `scripts/build-contradiction-radar.py` — 빌드 스크립트 (AUTO-GENERATED 생성기)
- `interactives/contradiction-radar.html` — 산출물 (덮어쓰기, 손편집 금지)
- (후속) `deploy-pages.yml`에 빌드 스텝 추가 + `build-interactives-index.py` 인덱싱

# Done Criteria

- [x] contradicts/refines edge 전수 수집 + 양측 thesis 살붙이기
- [x] 무순서 쌍 dedup(상호 엣지 mutual 표기), 강한 타입 우선(contradicts > refines)
- [x] 임상 도메인별 그룹 + 검색 + 정면충돌/조건부 필터
- [x] 각 논문 → 배포 사이트 페이지 링크
- [ ] deploy 워크플로 배선 (후속)
