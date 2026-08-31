---
title: "삽입토크·발열·골질 임상 해석기 인터랙티브"
type: agenda
date: 2026-08-31
status: done
owner: 원장
priority: P1
tags: [implant-stability, insertion-torque, isq, osteotomy-heat, bone-quality, interactive, chairside]
source_wiki: wiki/overviews/high-insertion-torque-primary-stability-crestal-bone-overview.md
output_wiki: interactives/2026-08-31_it-stability-clinical-tool.html
---

# Goal

식립 중 손에 잡히는 삽입 토크 (Insertion Torque, IT) 값 하나를 chairside에서 **부하 결정**으로 번역하는 해석기. 이 위키의 핵심 명제 — *IT는 술자가 투여한 용량이 아니라 저항한 골을 읽은 값* — 을 계산기 형태로 구현해, 숫자를 그대로 "안정성 점수"로 읽는 오판을 막는 것이 목적.

# Input

- wiki/overviews/high-insertion-torque-primary-stability-crestal-bone-overview.md — 종합 spine (IT=측정값 명제, Rule 1–6, 구간별 부호 반전)
- wiki/implants/norton-2017-low-insertion-torque-primary-stability.md — 하한 앵커: IT ≤20 Ncm·spinner <5 Ncm도 1년 100% 생존, ISQ 67→80 회복
- wiki/implants/isq/baldi-2018-insertion-torque-isq-tapered-knife-edge.md — IT–ISQ 상관은 중간 토크에서만 유의(ρ=0.481), 실패 2건 모두 고토크군
- wiki/implants/isq/marconcini-2018-high-insertion-torque-bone-resorption-rct.md — 고토크 치조정 해악(3년 CSR 91.3 vs 98.2%)
- wiki/implants/isq/aldahlawi-2018-implant-torque-crestal-bone-remodeling.md — 하악 2.12 vs 상악 0.25 mm — 해악의 부위 한정성
- wiki/implants/coyac-2019-preclinical-model-links-osseo-densification-misfit.md — 과압축→골세포사멸 기전(천장은 존재하나 위치는 미상)
- wiki/implants/osteotomy-thermal/milone-2026-heat-dental-implant-thermal-analysis.md — 삽입 단계 발열 위험인자 (in-vitro, n=24, FLIR)
- wiki/bone-biology/palominozorrilla-2024-jawbone-quality-classification-scoping.md — Lekholm-Zarb 사용 실태와 미검증 경고
- wiki/bone-biology/shemtovyona-2021-jawbone-quality-quantitative-meta-analysis.md — CBCT 기하 파라미터 → 골질 type 정량 매핑

# Output

- interactives/2026-08-31_it-stability-clinical-tool.html — 4섹션 chairside 해석기

# Done Criteria

- [x] ISQ 기반 로딩 타이밍 판정 섹션 (최상단 배치 — 부하 결정이 최종 질문이므로)
- [x] IT 슬라이더 → 구간별 임상 해석 + ISQ 궤적 차트 (항상 표시)
- [x] 식립 중 발열 위험인자 체크 (Milone 2026)
- [x] Lekholm-Zarb Type I–IV 참조표
- [x] 출처 블록 — 위키 보유 논문 + DOI만
- [x] frontmatter에 status·category·agenda 백링크·source_wiki 박힘
- [ ] (해당 없음) 동반 퀴즈 — 교육용 아님

# Notes / Decisions

- 2026-08-31: **IT를 "높을수록 좋다"로 렌더링하지 않는다**가 설계 제약. 구간 상단(>65 Ncm)은 초록이 아니라 경고로 칠했고, 하한(<5 Ncm 스피너)도 즉시 실패로 표시하지 않는다 — Norton 2017이 spinner 전부 골유착을 보고했기 때문. 두 끝을 모두 "다시 측정하라"로 보내는 것이 보유 근거에 맞는 유일한 렌더링.
- 2026-08-31: ISQ 궤적 차트를 조건부 표시 → 항상 표시로 변경. 숨겨두면 "IT만 보면 된다"는 인상을 주어 도구의 목적과 반대로 작동.
- 2026-08-31: 슬라이더 기본값 15 → 30 Ncm. 15는 Norton 구간(예외적 하한)이라 도구를 처음 여는 사람에게 그 구간을 기본 화면으로 보여주는 셈이었다.
- 2026-08-31 (retro): agenda·frontmatter 백링크 없이 산출물이 먼저 만들어져 `operations-lint`가 FAIL. 이 파일은 사후 작성된 명세다 — OPERATIONS.md §1 hard rule(산출물 전 agenda 선행) 위반의 복구.
- 2026-08-31 (retro): 출처 자기서술 교정 — 헤더가 "논문 5편 기반"이었으나 본문 >65 Ncm 구간이 Marconcini 2018·Aldahlawi 2018·Coyac 2019를 인용하고 있어 실제 8편. 헤더·출처 블록 양쪽 갱신.
- 2026-08-31 (retro): Coyac 2019 소견을 "골수압·골세포사멸"로 적었으나 보유 페이지에 골수압(bone marrow pressure) 기술이 없음 → "미세골절·골세포사멸"로 정정 (Rule #1).
- 2026-08-31 (retro): under-milling ITV·ISQ 차트는 이 도구가 아니라 interactives/2026-08-18_under-milling-itv-isq-calculator.html의 것 — 커밋 로그만 보고 근거로 넣을 뻔한 것을 git show로 확인해 제외.
- 2026-08-31 (retro): OPERATIONS.md §7(라이트 고정) 위반 — `@media (prefers-color-scheme: dark)` + `:root[data-theme="dark"]` + 라이트/다크 토글 버튼이 들어가 있어 제거.

# References

- [[overviews/high-insertion-torque-primary-stability-crestal-bone-overview]]
- [[overviews/implants-isq-stability-ladder]]
- [[overviews/bone-quality-implant-risk-modification-overview]]
