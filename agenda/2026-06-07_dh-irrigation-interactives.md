---
title: "DH 치료 의사결정 계산기 + 근관세정제 비교 매트릭스 (2026-06-07 ingest batch)"
type: agenda
date: 2026-06-07
status: done
owner: 원장
source_wiki:
  - wiki/overviews/dentin-hypersensitivity-overview.md
  - wiki/dentin-hypersensitivity/shan-2021-low-level-light-therapy-dentin-hypersensitivity-sr-ma.md
  - wiki/endodontics/irrigation/fortea-2024-chelating-agents-endodontic-treatment-sr.md
  - wiki/endodontics/irrigation/rao-2025-maleic-acid-root-canal-scoping-review.md
output_wiki:
  - interactives/2026-06-07_dh-treatment-decision-calculator.html
  - interactives/2026-06-07_endodontic-irrigant-comparison-matrix.html
tags: [dentin-hypersensitivity, endodontic-irrigation, interactive, chairside]
---

# Goal

2026-06-07 ingest한 DH·근관세정 28편을 chairside 의사결정 도구 2개로 변환. (1) 상아질 과민증 치료 옵션 랭킹 계산기, (2) 근관세정제·킬레이터 비교 매트릭스. 원장 본인 chairside 참조용.

# Input

DH cluster (11편):
- wiki/dentin-hypersensitivity/shan-2021-low-level-light-therapy-dentin-hypersensitivity-sr-ma.md — LLLT SMD vs placebo·타제제
- wiki/dentin-hypersensitivity/faraoni-2023-laser-therapy-dentin-hypersensitivity-sr-ma.md — 고·저출력 레이저 동등
- wiki/dentin-hypersensitivity/forouzande-2022-fluoride-gluma-laser-dentin-hypersensitivity.md — Er,Cr:YSGG > NaF varnish RCT
- wiki/dentin-hypersensitivity/naghsh-2024-three-methods-dentin-hypersensitivity-rct.md — diode laser 단기 우월·수렴
- wiki/dentin-hypersensitivity/jiang-2022-desensitizing-agents-permeability-cytotoxicity.md — GLUMA 치수액 의존·세포독성
- wiki/dentin-hypersensitivity/scheffel-2015-transdentinal-cytotoxicity-glutaraldehyde-odontoblast.md — 글루타르알데히드 세포독성
- wiki/dentin-hypersensitivity/joshi-2013-novamin-gluma-dentinal-tubule-occlusion-sem.md — tubule occlusion
- wiki/dentin-hypersensitivity/defreitas-2021-bioactive-toothpastes-dentin-hypersensitivity-sr.md — bioactive glass 치약
- wiki/dentin-hypersensitivity/martins-2022-desensitizing-toothpastes-formulations-scoping-review.md — 제형 지도
- wiki/dentin-hypersensitivity/ramli-2022-successful-dentin-hypersensitivity-treatment-strategies.md — 관리 전략
- wiki/dentin-hypersensitivity/li-2026-physical-chemical-strategies-dentin-hypersensitivity.md — 재료 기전
- wiki/overviews/dentin-hypersensitivity-overview.md — 통합 ladder

Irrigation cluster (9 + 1 bond):
- wiki/endodontics/irrigation/fortea-2024-chelating-agents-endodontic-treatment-sr.md — EDTA/HEDP 비교
- wiki/endodontics/irrigation/rao-2025-maleic-acid-root-canal-scoping-review.md — 7% maleic acid
- wiki/endodontics/irrigation/teja-2022-herbal-agents-edta-smear-layer-removal-sr.md — herbal vs EDTA
- wiki/endodontics/irrigation/elfarraj-2024-irrigants-tooth-dentin-infrared-spectroscopy-slr.md — FTIR dentin 변화
- wiki/endodontics/irrigation/agarwal-2024-irrigating-solutions-dentin-microhardness-sr-ma.md — microhardness
- wiki/endodontics/irrigation/khoury-2024-endodontic-irrigants-comprehensive-perspective-review.md — 종합·CHX substantivity
- wiki/endodontics/irrigation/nascimento-2015-gel-formulations-residues-dentinal-walls-sem-eds.md — gel 잔류
- wiki/endodontics/irrigation/cruz-2014-debris-apical-third-naocl-glyde-in-vivo.md — Glyde paste debris
- wiki/endodontics/irrigation/wong-2014-root-canal-lubricants-antibacterial-irrigants.md — 윤활제 항균
- wiki/resin-bonding/zhou-2025-collagen-crosslinkers-naocl-dentin-bond-strength-sr-ma.md — NaOCl·결합강도

# Output

- interactives/2026-06-07_dh-treatment-decision-calculator.html
- interactives/2026-06-07_endodontic-irrigant-comparison-matrix.html

# Done Criteria

- [x] DH 계산기: 자극종류·in-office/at-home·vital pulp 근접·지속성 요구 입력 → 옵션 랭킹 + 근거태그 + inline citation
- [x] 세정제 매트릭스: 7제 × 6축 비교, 필터, 셀별 출처
- [x] 단일 HTML, 인라인 CSS/JS, 오프라인, 한글 sans-serif
- [x] frontmatter agenda 백링크 + source_wiki
