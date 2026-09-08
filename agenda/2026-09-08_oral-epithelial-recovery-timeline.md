---
title: "구강점막 자가회복 타임라인 계산기"
type: agenda
date: 2026-09-08
status: done
owner: 원장
priority: P2
tags: [wound-healing, oral-mucosa, epithelium, calculator, education, interactive]
source_wiki:
  - wiki/periodontics/dawes-2003-oral-mucosal-epithelium-turnover-time.md
  - wiki/periodontics/aijima-2014-trpv3-oral-epithelial-wound-healing.md
  - wiki/periodontics/ohshima-2002-egf-saliva-oral-epithelial-migration.md
  - wiki/periodontics/watanabe-2025-prgf-vs-prp-gingival-epithelial.md
output_wiki:
  - interactives/2026-09-08_oral-epithelial-recovery-timeline.html
---

# Goal

구강점막 재상피화 예상 시간을 환자별 변수(병변 크기·TRPV3 온도 보정·EGF 환경)로 추정하는 교육용 계산기. Dawes 2003 migration 모델 기반.

# Input

- `wiki/periodontics/dawes-2003-oral-mucosal-epithelium-turnover-time.md` — 상피 교체주기·migration 기저 모델
- `wiki/periodontics/aijima-2014-trpv3-oral-epithelial-wound-healing.md` — TRPV3 온도 채널 보정 인자
- `wiki/periodontics/ohshima-2002-egf-saliva-oral-epithelial-migration.md` — EGF 타액 농도 → migration 촉진
- `wiki/periodontics/watanabe-2025-prgf-vs-prp-gingival-epithelial.md` — PRGF vs L-PRP 성장인자 효과

# Output

- `interactives/2026-09-08_oral-epithelial-recovery-timeline.html`

# Done criteria

- 병변 직경·부위별 예상 회복일 계산
- 온도 보정(TRPV3) 및 EGF 조건 입력 지원
- 비의료기기 고지 포함
