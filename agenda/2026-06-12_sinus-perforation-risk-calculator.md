---
title: "Chairside 상악동 천공 위험 점수화 계산기"
type: agenda
date: 2026-06-12
status: in-progress
source_wiki:
  - wiki/overviews/odontogenic-maxillary-sinusitis-overview.md
  - wiki/sinus-lift/lateral/nemati-2023-membrane-perforation-risk-lateral-sinus.md
  - wiki/sinus-lift/lateral/ye-2025-rrh-sinus-membrane-perforation-sr-ma.md
  - wiki/sinus-lift/lateral/wang-2023-smoking-schneiderian-membrane-perforation-sinus.md
  - wiki/sinus-lift/lateral/henriques-2022-maxillary-sinus-septa-prevalence-sr-ma.md
  - wiki/sinus-lift/lateral/khiabani-2024-sinus-membrane-thickness-lsfe-mucosal.md
  - wiki/sinus-lift/lateral/gulec-2025-psaa-cbct-maxillary-sinus-anatomy.md
  - wiki/sinus-lift/lateral/lee-2023-impact-sinus-floor-elevation-techniques.md
  - wiki/sinus-lift/lateral/kozuma-2017-chronic-sinusitis-sinus-augmentation-infection.md
---

# Goal

OMS overview 예방축(§1–5)을 chairside 의사결정 도구로 압축한다. 술자가 술전 CBCT/문진에서 얻는 인자를 입력하면 막천공 위험등급과 창 디자인·예방 권고를 한 화면에 제시.

# Input (근거)

- RRH(잔존 치조골 높이) — Ye 2025 (낮을수록 천공↑, OR 4.68)
- 막두께 — Khiabani 2024 (<1mm 취약 / >5mm 금기 아님), Abullais 2024 (형태로 예측 불가)
- 상악동 격벽 — Nemati 2023 (HR 8.07), Henriques 2022 (유병률 33%/41%)
- 흡연 — Wang 2023 (OR 1.58), Nemati 2023 (HR 25)
- 점액낭종(MRC) — Nemati 2023 (HR 27.75)
- 다수치 결손 — Nemati 2023 (HR 68)
- 술전 만성 부비동염 — Kozuma 2017 (감염·실패 최강 예측, p=0.007)
- PSAA 골내형/치조정 근접 — Gulec 2025 (출혈 위험)
- 술식 선택 — Lee 2023 (측방 회전버 최고 위험 · 경치조골 리머 최저)

# Output

- interactives/2026-06-12_sinus-perforation-risk-calculator.html
- 위험등급(Low/Moderate/High) + 창디자인(단일/분할창·피에조·우회)·예방(금연·ENT 선치료·프로토콜) 권고, 각 권고에 출처 명시

# Done 기준

- [ ] 입력 → 실시간 점수·등급 산출
- [ ] 권고가 모두 위키 페이지 근거에 매핑
- [ ] frontmatter cross-link (source_wiki·agenda 백링크) 완비
- [ ] disclaimer: 의사결정 보조이지 확정 도구 아님(예측 타당도 RCT 미검증)
