---
title: "UV-PF 파장 비교 계산기 + UV vs 플라즈마 결정 도구"
type: agenda
date: 2026-11-05
status: done
owner: 원장
priority: P1
tags: [uv-photofunctionalization, plasma, DBD, wavelength, decision-tool]
---

# Goal

UV 광기능화(UV-PF)의 파장별 광자 에너지·탄화수소 제거 효과를 시각적으로 비교하고, UV-PF vs DBD 플라즈마(메가젠 방식) 간 임상 결정 도구를 제공. 최근 인제스트 자료(Suzumura 2023 · Houshmand 2023 · Choi 2017 · Shahraki 2026 등)를 반영.

# Input

- wiki/implants/surface/plasma/shahraki-2026-cold-atmospheric-plasma-peri-implantitis-scoping-review.md
- wiki/implants/surface/choi-2017-uv-dbd-plasma-titanium-storage-biological-activity.md
- wiki/implants/surface/suzumura-2023-vuv-172nm-titanium-photofunctionalization.md
- wiki/implants/surface/houshmand-2023-uv-photofunctionalization-sla-titanium-disks.md
- wiki/implants/surface/matsuura-2024-biological-dilemma-titanium-surface-strategies.md
- wiki/implants/surface/wagstaffe-2019-rgd-tripeptide-adsorption-titania-surfaces.md
- wiki/overviews/uv-photofunctionalization-dental-implants.md
- wiki/overviews/plasma-surface-treatment-dental-implants.md

# Output

- interactives/2026-11-05_uv-wavelength-photon-energy-calculator.html
- interactives/2026-11-05_uv-vs-plasma-decision-tool.html

# Done Criteria

- [x] 파장 슬라이더/탭: 172nm · 210nm · 310nm · 365nm 각 광자 에너지(eV) + 효과 요약
- [x] 본드 에너지 임계선 시각화 (카르복실기-Ti ~3.5–4 eV)
- [x] UV vs Plasma 다축 비교표 (기전·처리시간·항균·임상근거·보관 등)
- [x] 과처리 경고 · 보관법 가이드 포함
- [x] 라이트 고정, 캐시 버전 JS 적용
- [x] frontmatter에 source_wiki + agenda 백링크 박힘

# Notes / Decisions

- 2026-11-05: Houshmand 2023의 핵심 — UVB는 접촉각만 개선, 탄소는 XPS에서 유의하게 감소하지 않음(p=0.171). 파장 선택이 임상적으로 중요함을 강조.
- 2026-11-05: Choi 2017이 UV=DBD 즉시 등가 근거이므로 결정도구에서 "동일 출발선"으로 명시.
- 2026-11-05: 임플란트 카테고리 = `implant-placement` (표면 처리 = 식립 전 단계).
