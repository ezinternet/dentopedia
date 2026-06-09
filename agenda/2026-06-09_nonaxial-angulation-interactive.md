---
title: "비축방향 식립 각도 → 경부 응력·MBL 추정 인터랙티브"
type: agenda
date: 2026-06-09
status: done
owner: 원장
priority: P2
tags: [implant, angulation, nonaxial, mbl, occlusion, interactive]
source_wiki:
  - wiki/implants/kim-2026-implant-angulation-peri-implant-bone.md
  - wiki/overviews/implant-occlusion-loading-biomechanics-overview.md
  - wiki/occlusion/di-fiore-2022-periimplant-bone-loss-overload-occlusal-analysis.md
output:
  - interactives/2026-06-09_nonaxial-angulation-mbl-calculator.html
---

# Goal

비축방향(nonaxial) 식립 각도가 임플란트 경부 응력·변연골 소실(MBL)에 미치는 영향을 chairside에서 직관적으로 보여주는 단일 HTML 위젯. 식립 각도(근원심+협설)·교합력·대합치 유형을 입력하면 응력 배수와 Kim 2026의 관측 MBL 구간을 표시.

# Input

- wiki/implants/kim-2026-implant-angulation-peri-implant-bone.md — 주 데이터(비축 0.22 vs 축 0.10 mm, 각도×대합치 상호작용 Δ0.373 mm, 15°마다 응력 +25%·30°↑ +50%)
- wiki/overviews/implant-occlusion-loading-biomechanics-overview.md — 생역학 맥락(PDL 부재, stress concentration)
- wiki/occlusion/di-fiore-2022-periimplant-bone-loss-overload-occlusal-analysis.md — 과부하-골소실 근거 한계

# Output

- interactives/2026-06-09_nonaxial-angulation-mbl-calculator.html

# Done Criteria

- [x] 근원심·협설 각도 슬라이더 → 합성(3D) 각도 산출
- [x] 교합력 입력 → 협측 분력·응력 배수 표시(논문 벡터 예시 재현)
- [x] 대합치 유형 선택 → MBL 구간 + implant-FDP 상호작용 경고
- [x] 출처 inline + 확신도 태그(retrospective, 절대값 작음 caveat)
- [x] 단일 파일·CDN 없음·한글 sans-serif
- [x] frontmatter agenda/source_wiki 백링크

# Notes / Decisions

- 응력 모델은 단순 삼각함수(F·sinθ 협측분력) + 논문이 인용한 "15°→+25%, 30°→+50%" 경험 배수의 교육용 근사. FEA 정밀모델 아님 → [claude해석]/[교육용] 명시.
- 절대 MBL이 0.1–0.22 mm로 작아 임상적 유의는 별개라는 caveat 필수.
