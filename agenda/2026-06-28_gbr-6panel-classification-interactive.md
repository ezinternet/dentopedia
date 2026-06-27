---
title: "GBR 6패널 분류 인터랙티브 도구 배포"
type: agenda
date: 2026-06-28
status: done
owner: 원장
tags: [gbr, bone-regeneration, interactive, vertical-ridge-augmentation]
source_wiki:
  - wiki/bone-regeneration/ridge-preservation/wang-2024-simplified-gbr-biocollagen-prf-posterior-ridge.md
  - wiki/implants/vertical-ridge-augmentation/cucchi-2021-cadcam-titanium-mesh-resorbable-membrane-rct.md
  - wiki/implants/vertical-ridge-augmentation/cucchi-2021-dptfe-titanium-mesh-vertical-ridge-rct.md
  - wiki/implants/vertical-ridge-augmentation/wurtz-2026-cadcam-titanium-mesh-tenting-screw-gbr.md
output: interactives/2026-06-28_gbr-6panel-classification.html
---

# Goal

GBR 6패널 분류(Panel I–VI: 결손 위치·막 유형·침수 여부 기준) 임상 의사결정 인터랙티브 도구를 wiki interactives에 배포.

# Input

- `/Users/oracleneo/Downloads/GBR 6패널 분류 (standalone).html` — 인용 DOI 모두 검증 완료
- 인용 논문 4편 인제스트 완료:
  - Wang 2024 (DOI 10.1007/s13770-024-00654-0) — Bio-collagen + PRF simplified GBR
  - Cucchi 2021 (DOI 10.1111/clr.13841) — CAD/CAM Ti mesh ± resorbable membrane RCT
  - Cucchi 2021 (DOI 10.1111/clr.13673) — d-PTFE vs Ti mesh+collagen VRA 1y RCT
  - Wurtz 2026 (DOI 10.1111/cid.70139) — CAD/CAM Ti mesh vs tenting screws 5yr

# Output

`interactives/2026-06-28_gbr-6panel-classification.html`

# Done

- [x] 인용 DOI 4개 HTML에서 추출·검증 (Python HTMLParser)
- [x] 4편 논문 PMC 풀텍스트 인제스트 (sources/ + wiki/)
- [x] HTML 내용 수정 불필요 — 모든 DOI 정확
- [x] interactives/ 에 날짜 prefix 파일명으로 배포
