---
title: "oral-hygiene-instruction overview 합성 — 치태착색제(PDA) 효능·안전성·적용 집단"
type: agenda
date: 2026-10-12
status: review
owner: 원장
priority: P2
deadline:
source_wiki:
  - wiki/periodontics/oral-hygiene-instruction/balli-akgol-2026-plaque-disclosing-agents-biofilm-removal.md
  - wiki/periodontics/oral-hygiene-instruction/fasoulas-2019-detection-dental-plaque-disclosing-agents.md
  - wiki/periodontics/oral-hygiene-instruction/jung-2020-cytotoxicity-dental-disclosing-solution.md
  - wiki/periodontics/oral-hygiene-instruction/kamra-2024-oral-hygiene-instruction-plaque-disclosing-agents.md
  - wiki/periodontics/oral-hygiene-instruction/nagashima-2018-self-check-plaque-disclosing-solution.md
output_wiki:
  - wiki/overviews/plaque-disclosing-agents-efficacy-safety-overview.md
tags: [overview, periodontics, oral-hygiene-instruction, plaque-disclosing-agent]
---

# Goal

periodontics/oral-hygiene-instruction의 미합성 paper 5편을 종합해, 치태착색제(PDA)를 "누구에게·어떻게·어떤 안전 제한으로" 쓸지 위생사·원장이 칫솔질 교육 시 바로 조회할 overview 1개로 정리.

# Input

- balli-akgol-2026 — RCT (n=124 치대생), PDA 추가 vs 표준 교육 단독, 1차 결과 무차이 (천장효과)
- nagashima-2018 — 전후비교 (n=9 아동양육시설), 주 1회 자가검진, PCR 66.1→38.7%
- kamra-2024 — case report (n=1), 2색 PDA + Bass, 4주 PI 2.0→0.8
- fasoulas-2019 — 단면연구 (n=588 학령기 아동), 치태 검출 부위 지도 (연령·SES·BMI·DMFT 연관)
- jung-2020 — in-vitro, 에리트로신계 PDA 50× 희석에서 세포독성(apoptosis), 제거 곤란
- 맥락: wiki/overviews/oral-hygiene-instruction-overview.md (기존 종합), sooampon-2026 (염료 비교 RCT, 이미 합성됨)
- 제외: stem `oral-hygiene-instruction` — 카테고리 내비게이션 페이지(논문 아님)라 category-overflow 집계의 오탐. 실제 대상 paper는 5편.

# Output

- wiki/overviews/plaque-disclosing-agents-efficacy-safety-overview.md [작성 완료] (frontmatter에 `agenda:` 백링크, `## 한국어 핵심요약` 최상단)

# Done Criteria

이 작업이 제대로 되었다면, 위생사가 "이 환자에게 착색제를 추가할 근거가 있는가, 쓴다면 어떤 안전 제한이 필요한가"를 overview 한 페이지에서 수치(CI·p)와 출처 stem 링크로 답할 수 있다.

- [x] 5편 모두 overview에서 [[stem]]으로 참조 (category-overflow.py 재실행: 후보 카테고리 1→0 확인)
- [x] 핵심 수치 표 1장 (출처 inline), 근거 수준(rct / prospective / case-report / cross-sectional / in-vitro) 명시
- [x] 효능 근거 상충(Ballı 무차이 vs Nagashima·Kamra 개선) 병기 및 해석(집단 숙련도, 설계 한계)
- [x] 한국어 핵심요약 ~10 bullets, Three-line Summary 이중언어
- [x] 모든 수치는 해당 wiki 페이지에서 확인된 것만 (Rule #4)
- [x] 위생사용 체크리스트 1장
- [ ] qmd update/embed 및 카테고리 index 반영은 원장 확인 후 (자동 실행 안 함)

# Notes / Decisions

- 2026-10-12: 주간 브리핑 "go" 수신. 미합성 6건 중 1건은 내비 페이지 → 5편으로 확정.
- 2026-10-12: 신규 PubMed 검색 없음 (Rule #1). 보유 5편 + 해당 페이지 Related Papers에 이미 인용된 수치만 사용.

# References

- [[wiki/overviews/oral-hygiene-instruction-overview]]
- [[wiki/periodontics/oral-hygiene-instruction/sooampon-2026-dc-red-33-erythrosine-plaque-disclosure-rct]]
