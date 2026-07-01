---
title: "CAD/CAM 치과 기공 인터랙티브 2종 — 밀링/3D프린팅 적합도 비교표 + 디지털 총의치 비용효율 계산기"
type: agenda
date: 2026-07-01
status: done
owner: 원장
priority: P2
deadline:
tags: [cad-cam, digital-workflow, complete-denture, dental-materials]
source_wiki:
  - wiki/dental-materials/omar-2026-marginal-gap-additive-subtractive-nanoceramic.md
  - wiki/dental-materials/ali-2023-cadcam-restoration-failure-reasons-sr-ma.md
  - wiki/dental-materials/saravi-2021-cadcam-all-ceramic-fdp-clinical-sr-ma.md
  - wiki/dental-materials/zirconia/aswal-2023-cadcam-zirconia-lithium-disilicate-crowns-sr-ma.md
  - wiki/dental-materials/zirconia/kwon-2024-strength-limiting-defects-zirconia-cad-cam.md
  - wiki/inlay/souza-2021-lithium-disilicate-vs-resin-composite-cadcam-onlay.md
  - wiki/inlay/basheer-2026-cadcam-3dprinted-inlays-onlays-veneers-scoping.md
  - wiki/digital-workflow/fouda-2025-accuracy-digital-workflow-implant-fullarch.md
  - wiki/complete-denture/muehlemann-2025-cost-efficiency-digital-conventional-denture.md
  - wiki/complete-denture/jafarpour-2024-cadcam-versus-traditional-complete-dentures.md
  - wiki/complete-denture/srinivasan-2021-cad-cam-removable-complete-dentures.md
  - wiki/complete-denture/thu-2024-digital-complete-denture-clinical-laboratory.md
  - wiki/complete-denture/khorasani-2024-3d-printed-vs-milled-complete.md
  - wiki/complete-denture/feng-2025-expert-consensus-digital-complete-denture.md
---

# Goal

CAD/CAM 치과 기공(dental laboratory) 관련 신규 인제스트 4편(fouda-2025, omar-2026, muehlemann-2025, feng-2025) + 기존 CAD/CAM 재료 페이지들을 종합해, chairside에서 즉시 참조할 수 있는 (1) 밀링 vs 3D프린팅 vs 프레스 적합도 비교 매트릭스, (2) 디지털 vs 전통 총의치 워크플로우 비용효율 계산기 두 가지 인터랙티브 도구로 정리.

# Input

- wiki/dental-materials/omar-2026-marginal-gap-additive-subtractive-nanoceramic.md — 밀링 34–38µm vs 3D프린팅 60–64µm 마진갭 (하이브리드 나노세라믹 임플란트 크라운)
- wiki/dental-materials/ali-2023-cadcam-restoration-failure-reasons-sr-ma.md — CAD/CAM 수복물 파절 55%/탈락 20%, 두께 <1.5mm 위험 증가
- wiki/dental-materials/saravi-2021-cadcam-all-ceramic-fdp-clinical-sr-ma.md — 5년 생존 >90%, 지르코니아 베니어링 치핑 최다 합병증
- wiki/dental-materials/zirconia/aswal-2023-cadcam-zirconia-lithium-disilicate-crowns-sr-ma.md — 심미 합병증 OR 16.88 (지르코니아 vs LiDi)
- wiki/dental-materials/zirconia/kwon-2024-strength-limiting-defects-zirconia-cad-cam.md — 밀링 유발 표면결함(gouge/scratch/chip) vs 폴리싱 후 강도-신뢰도 트레이드오프
- wiki/inlay/souza-2021-lithium-disilicate-vs-resin-composite-cadcam-onlay.md — e.max CAD vs Lava Ultimate 1년 마진갭 유의차 없음
- wiki/inlay/basheer-2026-cadcam-3dprinted-inlays-onlays-veneers-scoping.md — 인레이/온레이/베니어별 밀링 vs 3D프린팅 적합도 스코핑 리뷰
- wiki/digital-workflow/fouda-2025-accuracy-digital-workflow-implant-fullarch.md — 완전 디지털 전악 프레임워크 SST 통과 0/10, 스캐닝 오차 주원인
- wiki/complete-denture/muehlemann-2025-cost-efficiency-digital-conventional-denture.md — 디지털 vs 전통 총의치 비용효율 SR+MA, 전체 NS, 시술자 숙련도 유의
- wiki/complete-denture/jafarpour-2024-cadcam-versus-traditional-complete-dentures.md — 상반 SR+MA(CAD/CAM 유의하게 저렴) — evidence-conflict 표시 필요
- wiki/complete-denture/srinivasan-2021-cad-cam-removable-complete-dentures.md — 73편, 밀링>3D프린팅 강도/인성/표면조도, CAD-CAM 유지력·비용 우위
- wiki/complete-denture/thu-2024-digital-complete-denture-clinical-laboratory.md — 39편, IOS 유지력 60%↓, 내원 2–6회, 합병증(유지상실 37.5%·재제작 31.3%)
- wiki/complete-denture/khorasani-2024-3d-printed-vs-milled-complete.md — 4편 소규모 SR+MA, 유지력·만족도 NS (근거 희박)

# Output

- interactives/2026-07-01_cadcam-fit-comparison-matrix.html
- interactives/2026-07-01_digital-denture-cost-calculator.html

각 산출물 frontmatter에 `agenda: agenda/2026-07-01_cadcam-lab-workflow-interactives.md` 백링크.

# Done Criteria

- [x] 비교 매트릭스: 수복물 유형(크라운/인레이·온레이/베니어/전악프레임워크) × 가공법(밀링/3D프린팅/프레스) 별 마진갭·합병증 수치 표, 출처 inline citation
- [x] 비용효율 계산기: 사용자 입력(전통 워크플로우 기공비·임상비·내원횟수) → Muehlemann 2025 pooled MD±CI 적용 디지털 워크플로우 예상 범위, 시술자 숙련도 토글
- [x] 계산기에 jafarpour-2024 상반 결과 evidence-conflict 배너 포함
- [x] 확신도 등급 명시 (in-vitro/sr+ma 등), Class B 임상 도구 — 자동 재작성 금지 주석
- [x] source_wiki frontmatter 백링크 완비 (agenda + 두 interactives 모두)

# Notes / Decisions

- 2026-07-01: 사용자가 CAD/CAM 치과 기공 논문 인제스트 후 인터랙티브 2종 제작을 요청. 위 Input 목록은 grep+Read로 직접 수치 추출(서브에이전트 위임 실패 후 직접 수행).

# References

- 없음 (신규 작업)
