---
title: "임플란트 보철 세틀링 이펙트 — 원인·대처방안 슬라이드"
type: agenda
date: 2026-07-02
status: in-progress
owner: 원장
priority: P1
tags: [implant, prosthetics, settling, preload, screw-loosening, slides]
source_wiki:
  - wiki/overviews/abutment-screw-preload-joint-stability-overview.md
  - wiki/prosthetic-materials/kim-2020-axial-displacements-removal-torque-changes.md
  - wiki/prosthetic-materials/pardal-pelaez-2017-preload-loss-abutment-screws-dynamic-fatigue.md
  - wiki/prosthetic-materials/bulaqi-2015-dynamic-nature-abutment-screw-retightening.md
  - wiki/prosthetic-materials/varvara-2020-retightening-preload-loss-abutment-screws.md
  - wiki/prosthetic-materials/saleh-saber-2017-repeated-torque-tightening-abutment-lengths.md
  - wiki/prosthetic-materials/nithyapriya-2018-factors-loss-preload-dental-implants.md
  - wiki/prosthetic-materials/sun-2026-abutment-contamination-internal-hex-preload.md
  - wiki/prosthetic-materials/marenzi-2026-torque-limiting-devices-accuracy-manufacturers.md
  - wiki/prosthetic-materials/selvi-2025-custom-stock-abutment-fatigue-sem.md
  - wiki/prosthetic-materials/ren-2024-morse-taper-abutment-subsidence-locking-force.md
output_wiki:
  - slides/2026-07-02_seminar_implant-settling-effect.md
---

# Goal

임플란트 보철 어버트먼트 나사 체결부의 **세틀링 이펙트 (Settling Effect / Embedment Relaxation)** 를 동료 임상의 대상으로 설명하는 발표 덱 제작 — 원인(기전·레버)과 대처방안(토크·재조임·리콜 프로토콜)을 근거와 함께 정리.

# Input

근거가 될 wiki 페이지. 전부 이미 위키에 존재 (Rule #1 준수 — 신규 web search 없음).

- wiki/overviews/abutment-screw-preload-joint-stability-overview.md — 18편 종합 hub, 슬라이드의 spine
- wiki/prosthetic-materials/kim-2020-axial-displacements-removal-torque-changes.md — 세틀링을 축방향 변위(µm)로 정량화, 연결부 형태 gradient
- wiki/prosthetic-materials/pardal-pelaez-2017-preload-loss-abutment-screws-dynamic-fatigue.md — 세틀링 2–10% + 피로 16.1–39% SR
- wiki/prosthetic-materials/bulaqi-2015-dynamic-nature-abutment-screw-retightening.md — 마찰→세틀링 FEA 기전
- wiki/prosthetic-materials/varvara-2020-retightening-preload-loss-abutment-screws.md — 재조임 타이밍(2분 vs 10분)
- wiki/prosthetic-materials/saleh-saber-2017-repeated-torque-tightening-abutment-lengths.md — 세틀링 plateau (2회째)
- wiki/prosthetic-materials/nithyapriya-2018-factors-loss-preload-dental-implants.md — 전하중 보존 6대 레버
- wiki/prosthetic-materials/sun-2026-abutment-contamination-internal-hex-preload.md — 오염이 전하중 형성 방해
- wiki/prosthetic-materials/marenzi-2026-torque-limiting-devices-accuracy-manufacturers.md — 토크렌치 under-deliver
- wiki/prosthetic-materials/selvi-2025-custom-stock-abutment-fatigue-sem.md — 손실 50k–1M 사이클 window → 조기 재조임
- wiki/prosthetic-materials/ren-2024-morse-taper-abutment-subsidence-locking-force.md — screwless taper-lock 침하 특수 케이스

# Output

- slides/2026-07-02_seminar_implant-settling-effect.md

각 산출물 frontmatter에 `agenda: agenda/2026-07-02_settling-effect-slides.md` 백링크 박음.

# Done Criteria

- [x] 세틀링 이펙트 정의 슬라이드
- [x] 원인 섹션 (세틀링/마찰/연결부형태/오염 + 피로와의 관계)
- [x] Kim 2020 연결부별 세틀링 µm 표
- [x] 대처방안 프로토콜 슬라이드 (청결→보정토크→지정토크→재조임→조기리콜)
- [x] 재조임 타이밍 논쟁(2분 vs 10분) 명시
- [x] taper-lock(screwless) 침하 특수 케이스
- [x] 확신도 등급·inline citation
- [x] Marp frontmatter 포함
- [x] source_wiki / agenda 백링크

# Notes / Decisions

- 2026-07-02: 세틀링 이펙트는 "screw loosening의 상류 원인 = preload loss의 두 기전 중 하나(무하중·즉시)"로 프레이밍. 동적 피로는 자매 기전으로 대비.
- 청중: 동료 임상의 → 파인만 차등에서 기초 비유 최소화, 수치·프로토콜 중심.
