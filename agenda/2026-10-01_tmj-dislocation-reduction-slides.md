---
title: "악관절 탈구 복원·재발방지 세미나 슬라이드"
type: agenda
date: 2026-10-01
status: in-progress
owner: 원장
priority: P1
tags: [tmj, tmj-dislocation, acute-reduction, recurrence-prevention, seminar, slides]
source_wiki:
  - wiki/overviews/tmj-dislocation-reduction-recurrence-overview.md
---

# Goal

2026-10-01에 인제스트한 악관절 탈구 10편 종합 overview를 **동료 임상의 대상 25–30분 세미나**로 변환한다. 목적은 술기 시연이 아니라 **판단 교정** — 이 주제에서 문헌·지침·합의가 서로 어긋나는 지점 세 곳(손목축법, ABI 패키지, 덱스트로스)을 근거 등급과 함께 보여주고, 첫 탈구 환자에게 "복원 성공"이 아니라 "재발 계획"을 건네도록 만드는 것.

# Input

- `wiki/overviews/tmj-dislocation-reduction-recurrence-overview.md` — spine. 10편 종합, 5축 + 12단계 결정 사다리 + 공백 9항
- 멤버 페이지 10편 (전부 `wiki/tmj/`):
  - `prechel-2018-the-treatment-of-temporomandibular-joint.md` — 독일 S3 진료지침, 24,650→136편, GoR/LoE 등급
  - `neff-2021-the-estmjs-european-society-of.md` — ESTMJS 국제합의, 수정 델파이, 24개 권고
  - `abrahamsson-2020-treatment-of-temporomandibular-joint-luxation.md` — RCT한정 SR 8편 338명, 근거 천장
  - `tarhio-2023-causes-and-treatment-of-temporomandibular.md` — 후향 n=260, 재발 위험비
  - `lin-2026-rapid-reduction-of-temporomandibular-joint.md` — PGR n=83, 150±52초
  - `stolbizer-2020-anterior-dislocation-of-the-temporomandibular.md` — PGR n=42
  - `okoje-2017-managing-temporomandibular-joint-dislocation-in.md` — 후향 n=11, 지연 내원
  - `hoppe-2025-management-of-recurrent-temporomandibular-joint.md` — 소아 SR 9편
  - `hoppe-2026-peri-and-intraarticular-injections-with.md` — 주사 매핑리뷰, 분리가능성 게이트
  - `tummings-2023-an-inexpensive-biomechanical-model-to.md` — $67 교육 모델

# Output

- `slides/2026-10-01_seminar_tmj-dislocation-reduction.md` — 16 slide, 25–30분, 동료 임상의

양방향 백링크: 슬라이드 frontmatter에 `agenda: agenda/2026-10-01_tmj-dislocation-reduction-slides.md`, 이 파일의 `# Output`에 슬라이드 경로.

# Done Criteria

- [x] 술기별 1차 성공률 표 1장 (분모·출처 inline)
- [x] 재발 위험비 표 1장 (유의/비유의 구분 명시 — 고령·여성이 무의미하다는 것이 핵심)
- [x] 문헌-지침 불일치 3개를 각각 독립 슬라이드로 (손목축법 / ABI 패키지 / 덱스트로스)
- [x] 확신도 등급 전 슬라이드 부착 (`[근거강함]` / `[근거중간]` / `[근거약함]` / `[합의수준]`)
- [x] 체어사이드 압축 사다리 1장
- [x] 공백·비주장 1장 (과잉 일반화 방지)
- [x] Marp frontmatter 블록 (marp/theme/paginate/size/lang) — VS Code 미리보기·export용
- [x] frontmatter에 source_wiki / agenda 백링크
- [ ] 발표 후 피드백 반영 → status: done

# Notes / Decisions

- 2026-10-01: **audience = `seminar`(동료 임상의)로 확정.** `hygienist`·`staff` 버킷은 부적합 — 이 내용의 핵심이 GoR 등급·RCT vs 합의 긴장·수술 역치라서 근거등급 리터러시가 전제된다. 팀 교육용이 따로 필요하면 응급 대응 체크리스트만 추린 별도 deck으로 분리할 것(현재 범위 아님).
- 2026-10-01: **동반 퀴즈 생성하지 않음** — 모든 슬라이드가 교육 평가용은 아니라는 기존 결정. 필요 시 명시 요청으로 `/clinical-quiz-gate` 별도 실행.
- 2026-10-01: 근거 태그에 `[근거약함]`·`[합의수준]` 2종 추가 사용. 기존 deck 어휘는 강함/중간/보통 3종이었으나 이 주제는 수술 RCT 0편·독일 지침 BTX가 근거수준 V에 권고등급 A라 약함 티어 없이는 등급이 거짓이 된다.
- 2026-10-01: 슬라이드에서 **숫자 합산·재계산 금지** 원칙 유지 — overview가 멤버 페이지에서 그대로 옮긴 수치만 쓰고, 내부 불일치(Refai 2011 p=0.039 vs NS)는 슬라이드에 올리지 않고 overview에만 남김(강연에서 다룰 층위가 아님).

# References

- [[overviews/tmj-dislocation-reduction-recurrence-overview]]
- OPERATIONS.md §1 Hard rule (slides는 agenda 선행 필수) · §2 파일명 · §3 frontmatter cross-link
