---
title: "전문가 치면세균막관리 의사결정 도구 (Professional Biofilm Management Decision Tool)"
type: agenda
date: 2026-06-21
status: done
owner: 원장
source_wiki:
  - wiki/overviews/professional-biofilm-management-gbt-air-polishing-overview.md
output_wiki: []
tags: [guided-biofilm-therapy, air-polishing, decision-tool, interactive, periodontics, peri-implant]
---

# Goal

전문가 치면세균막관리(GBT·에어폴리싱·기계적 debridement)에서 **부위(치아/임플란트) × 임상상황**에 따라 권장 술식·분말·안전체크를 chairside에서 즉시 안내하는 인터랙티브 의사결정 도구를 만든다. 위생사·원장이 클릭 몇 번으로 근거 기반 권장안과 안전 경고를 확인하도록 한다.

# Input

- wiki/overviews/professional-biofilm-management-gbt-air-polishing-overview.md — 종합 thesis·의사결정 틀(4 시나리오 표)의 1차 입력
- wiki/periodontics/yein-2026-guided-biofilm-therapy-periodontal-efficacy-sr.md — GBT 임상우월성 없음(SR)
- wiki/periodontics/cyris-2024-guided-biofilm-therapy-versus-conventional.md — NSPT GBT=SRP 동등, 시간 단축
- wiki/periodontics/stahli-2024-clinical-evaluation-novel-protocol-supportive.md — SPC GBT=SRP 동등
- wiki/periodontics/donertas-2026-gbt-subgingival-debridement-gcf-biomarkers.md — GBT GI/PI/IL-1β 우위
- wiki/periodontics/lodigkeit-2026-periodontal-instrumentation-enamel-cementum-review.md — 에어폴리싱 최소 마모
- wiki/periodontics/dvorska-2026-mechanical-instrumentation-hard-tissue-sr.md — 기구별 경조직 손실 정량
- wiki/periodontics/ifrim-2026-edta-air-polishing-root-surface-sem.md — 에리스리톨 기구흔↓·EDTA smear layer 잔존
- wiki/periodontics/hussein-2026-subcutaneous-emphysema-subgingival-air-polishing-case.md — 치은연하 에어폴리싱 피하기종 위험(안전)
- wiki/implants/peri-implantitis/brunello-2026-nonsurgical-peri-implant-mucositis-sr.md — 점막염 PMPR 핵심·보조요법 미미
- wiki/implants/peri-implantitis/eraydin-tufek-2026-nonsurgical-peri-implantitis-multiarm-rct.md — 글리신 에어아브레이전 우월성 없음
- wiki/implants/peri-implantitis/pujarern-2024-biofilm-removal-implant-airflow-erythritol.md — 에리스리톨=탄산수소나트륨 제거력, 손상 적음

# Output

- interactives/2026-06-21_professional-biofilm-management-decision-tool.html

산출물 frontmatter(HTML 주석)에 `agenda: agenda/2026-06-21_professional-biofilm-management-decision-tool.md` 백링크 + `source_wiki:` 박음.

# Done Criteria

- [x] 부위(치아/임플란트) → 임상상황 → 권장안 클릭 플로우
- [x] 각 권장 카드에 술식·분말(에리스리톨 권장)·근거 인용 표기
- [x] 치은연하 에어폴리싱 피하기종 안전 체크리스트 포함
- [x] 단일 HTML 자가포함(외부 의존성 없음), 모바일 대응
- [x] interactive frontmatter cross-link(agenda + source_wiki)
