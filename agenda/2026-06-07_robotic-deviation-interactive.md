---
title: "로봇 vs 내비게이션 임플란트 deviation 비교 인터랙티브"
type: agenda
date: 2026-06-07
status: done
owner: 원장
tags: [robotic-surgery, dynamic-navigation, interactive]
source_wiki:
  - wiki/overviews/robotic-vs-navigation-implant-accuracy.md
  - wiki/digital-workflow/yu-2025-autonomous-robotic-versus-dynamic-navigation.md
  - wiki/digital-workflow/wei-2025-autonomous-robotic-surgery-dynamic-navigation.md
  - wiki/digital-workflow/chen-2025-robot-assisted-dynamic-navigation-accuracy.md
  - wiki/digital-workflow/wu-2024-autonomous-dental-implant-robotic-accuracy.md
---

# Goal
신규 ingest한 로봇 임플란트 4편의 정확도 수치(각도·플랫폼/관상·첨부 편차)를 study별 robot vs navigation 막대그래프로 시각화해, "로봇은 각도만 일관 우위"라는 overview thesis를 chairside에서 한눈에 확인할 수 있도록 단일 HTML로 제공.

# Input
- wiki/overviews/robotic-vs-navigation-implant-accuracy.md — thesis·Evidence Map
- wiki/digital-workflow/{yu-2025,wei-2025,chen-2025,wu-2024}-*.md — deviation 수치 출처

# Output
- interactives/2026-06-07_robotic-navigation-deviation-comparison.html

# Done
- [x] 4편 수치 정확 반영(angular/linear, robot vs nav, NS 표기)
- [x] metric 토글, NS·single-arm 주석
- [x] 단일 파일·CDN만(Chart.js)
