---
title: "drug 미합성 5편 → 기존 sub-overview 편입 (신규 hub 생성 회피)"
type: agenda
date: 2026-06-01
status: done
owner: 원장
priority: P1
tags: [drug, overview, synthesis, mronj, diabetes, sedation, local-anesthesia]
source_wiki:
  - wiki/overviews/drug-mronj-antiresorptive-overview.md
  - wiki/overviews/drug-systemic-disease-dental-management-overview.md
  - wiki/drug/kwon-2023-mronj-position-papers-what-changed.md
  - wiki/drug/jkda-2021-60-1-004.md
  - wiki/drug/shahi-2026-implant-outcomes-diabetes-mellitus-sr.md
  - wiki/drug/karm-2023-clinical-practice-guidelines-diagnostic-procedural-sedation.md
  - wiki/drug/hwang-2023-proposal-clinical-guidelines-local-anesthesia-dentistry.md
output_wiki:
  - wiki/overviews/drug-mronj-antiresorptive-overview.md
  - wiki/overviews/drug-systemic-disease-dental-management-overview.md
---

# Goal

category-overflow가 지목한 drug 미합성 5편을, 신규 overview를 만들지 않고 이미 존재하는 2개 sub-overview(MRONJ·전신질환)에 편입해 paper:overview 비대칭을 해소. 원장·위생사가 전신질환·약물 환자 chairside 판단 시 단일 sub-overview에서 5편 근거를 함께 참조하도록 한다.

# 궤도 수정 결정 (2026-06-01)

초안은 "drug-systemic-safety 신규 overview"를 제안했으나, 점검 결과 drug 카테고리는 이미 [[drug-clinical-decision-ladder]] hub + 5개 sub-overview 체계가 완성돼 있었음. 신규 페이지 생성은 **중복 hub**를 만들 뿐. 5편은 전부 기존 sub-overview의 누락분이므로 편입이 정답.

- kwon-2023 (MRONJ 2022 변경 3가지), jkda-2021-60-1-004 (implant+BMA MRONJ) → `drug-mronj-antiresorptive-overview` (7→9편)
- shahi-2026 (DM 임플란트 SR 2026) → `drug-systemic-disease-dental-management-overview` §2 DM 축 (18→21편 누적, karm/hwang 포함)
- karm-2023 (진정 가이드), hwang-2023 (국소마취 가이드 proposal) → 동 overview §5 LA·진정 축 신설

# Input

- wiki/drug/kwon-2023-mronj-position-papers-what-changed.md — AAOMS 2022 핵심 변경 3가지 (정의에 Romosozumab 등 면역조절제 추가 / 수술 전 stage 확대 / drug holiday 권고 삭제)
- wiki/drug/jkda-2021-60-1-004.md — BMA 복용 환자 implant가 MRONJ trigger인가, decision framework (단국대 최정임 2022)
- wiki/drug/shahi-2026-implant-outcomes-diabetes-mellitus-sr.md — DM 임플란트 outcome SR (Al-Ansari 2022 후속, article-in-press)
- wiki/drug/karm-2023-clinical-practice-guidelines-diagnostic-procedural-sedation.md — 2022 한국 진정 가이드 15 PICO 해설 (consensus)
- wiki/drug/hwang-2023-proposal-clinical-guidelines-local-anesthesia-dentistry.md — 한국 치과 국소마취 표준 가이드 부재 지적 position paper

# Output

- wiki/overviews/drug-mronj-antiresorptive-overview.md — kwon-2023·jkda-2021 편입, source_papers 9편, AAOMS 2022 변경 섹션 보강
- wiki/overviews/drug-systemic-disease-dental-management-overview.md — shahi-2026 DM 축 보강, karm/hwang 진정·LA 가이드 섹션 신설

# Done Criteria

- [ ] MRONJ overview source_papers에 kwon-2023·jkda-2021 추가 + 본문 author·year 인용
- [ ] systemic-disease overview source_papers에 shahi-2026·karm-2023·hwang-2023 추가 + 본문 인용
- [ ] 확신도 태그 (sr / consensus / narrative-review / claude해석) 명시
- [ ] 모든 편입 paper가 overview 본문에서 최소 1회 author·year로 인용 (coverage-lint 통과)
- [ ] index.md 변동 없음 확인 (신규 페이지 없음 → entry 추가 불필요), 단 편입 paper의 index.md 등재 확인
- [ ] qmd update && embed
- [ ] link-integrity·operations-lint 통과

# Notes / Decisions

- 2026-06-01: 신규 overview 생성 회피, 기존 sub-overview 편입으로 전환. drug hub는 이미 포화 — 추가 hub는 thesis-staleness만 늘림.
- 2026-06-01: shahi-2026은 article-in-press라 pooled estimate 미확정. overview에는 "최신 후속 SR, 수치는 final PDF 대기"로만 반영하고 Al-Ansari 2022 OR 1.78을 주 수치로 유지.
- 2026-06-01: hwang-2023은 가이드 "부재" position paper라 수치 권고 없음 — LA 섹션에서 "한국 표준 가이드 미정립" 맥락 문장으로만 인용.

# References

- [[agenda/2026-05-27_drug-overview-split]] — 원 5축 분할 작업
- [[drug-clinical-decision-ladder]]
