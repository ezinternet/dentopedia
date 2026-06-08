---
title: "Cariology·구강미생물학 chairside 인터랙티브 3종 batch"
type: agenda
date: 2026-06-07
status: done
owner: 원장
priority: P2
source_wiki:
  - wiki/overviews/dental-erosion-etiology-prevention-synthesis.md
  - wiki/dental-erosion/barac-2015-erosive-effect-soft-drinks-enamel-profilometry.md
  - wiki/dental-erosion/souza-2020-citrus-sweets-enamel-erosion-invitro.md
  - wiki/caries/moynihan-2016-sugars-dental-caries-threshold-intake.md
  - wiki/caries/hajishafiee-2023-ssb-taxation-sugars-caries-umbrella.md
  - wiki/overviews/oral-microbiome-biofilm-dysbiosis-synthesis.md
  - wiki/oral-microbiology/hajishengallis-2012-psd-model-periodontal-disease.md
  - wiki/oral-microbiology/lamont-2014-polymicrobial-synergy-dysbiosis-inflammatory.md
  - wiki/oral-microbiology/koo-2013-exopolysaccharides-matrix-biofilm-virulence.md
output_wiki:
  - interactives/2026-06-07_dental-erosion-risk-matrix.html
  - interactives/2026-06-07_free-sugars-caries-ssb-tax-calculator.html
  - interactives/2026-06-07_psd-dysbiosis-model-flow.html
tags: [cariology, dental-erosion, oral-microbiology, chairside, interactive, batch, retroactive]
---

# Goal

2026-06-07 cariology·erosion·구강미생물학 도메인 ingest 직후, 환자 상담·교육 chairside에서 즉시 쓸 수 있는 단일 HTML 인터랙티브 3종을 한 묶음으로 제작. (retroactive agenda — 산출물 선행 생성됨, operations-lint orphan 해소 목적으로 backfill)

# Input

- wiki/dental-erosion/barac-2015-erosive-effect-soft-drinks-enamel-profilometry.md — 음료 pH·titratable acidity 침식 근거
- wiki/dental-erosion/souza-2020-citrus-sweets-enamel-erosion-invitro.md — 사탕·citrus 침식 in-vitro
- wiki/overviews/dental-erosion-etiology-prevention-synthesis.md — erosion 종합
- wiki/caries/moynihan-2016-sugars-dental-caries-threshold-intake.md — free sugars 임계값 (≤10%E / <5%E)
- wiki/caries/hajishafiee-2023-ssb-taxation-sugars-caries-umbrella.md — SSB 과세 umbrella
- wiki/oral-microbiology/hajishengallis-2012-psd-model-periodontal-disease.md — PSD 모델 원전
- wiki/oral-microbiology/hajishengallis-2014-porphyromonas-gingivalis-host-manipulation.md — keystone pathogen
- wiki/oral-microbiology/lamont-2014-polymicrobial-synergy-dysbiosis-inflammatory.md — PSD synergy
- wiki/oral-microbiology/lamont-2018-oral-microbiota-dynamic-communities-host.md — community dynamics
- wiki/oral-microbiology/koo-2013-exopolysaccharides-matrix-biofilm-virulence.md — EPS matrix
- wiki/overviews/oral-microbiome-biofilm-dysbiosis-synthesis.md — 미생물 종합

# Output

3개 단일 HTML (CDN 없음, 오프라인 chairside):

- interactives/2026-06-07_dental-erosion-risk-matrix.html — 음료·사탕 pH·산종류·침식지표 비교 매트릭스 ("pH 단독 판단 금지" 패널)
- interactives/2026-06-07_free-sugars-caries-ssb-tax-calculator.html — free sugars %E 환산 + SSB 과세 우식영향 추정
- interactives/2026-06-07_psd-dysbiosis-model-flow.html — 치주염·우식 병렬 루프를 dysbiosis 공통개념으로 통합한 노드 플로우

각 산출물 frontmatter에 `agenda: agenda/2026-06-07_cariology-microbiology-interactives.md` 백링크 박음.

# Done Criteria

- [x] 3개 HTML 모두 단일 파일·인라인 CSS/JS·외부 의존 없음
- [x] 각 HTML frontmatter에 source_wiki 박힘
- [x] 각 HTML frontmatter에 agenda 백링크 박힘 (2026-06-08 backfill)
- [x] erosion 매트릭스: 연구 간 절대수치 비교 금지 명시 (Barac 사람 법랑질 Ra vs Souza 소 법랑질 wear)
- [x] free-sugars: WHO/Moynihan 밴드 (≤10%E 강·<5%E 조건부) + Hajishafiee 2023 umbrella 인용
- [x] PSD 플로우: 노드 클릭 시 기전·출처 표시
- [x] index.md "Chairside 인터렉티브" 섹션에 3 entry 등록
- [x] operations-lint 통과 (orphan 0)

# Notes / Decisions

- 2026-06-08: retroactive agenda. 6/7 batch 제작 시 robotic/dh/irrigant 3종은 agenda를 챙겼으나 cariology 클러스터 3종은 누락 → operations-lint ERROR 3건. 동일 날짜 cariology·미생물 테마라 단일 batch agenda로 묶어 backfill (dh-irrigation-interactives 선례와 동일 1:N 구조).

# References

- [[agenda/2026-06-03_ingest-candidates-5domains]] — 본 인터랙티브들의 ingest 모태
- [[agenda/2026-06-07_dh-irrigation-interactives]] — 동일 6/7 batch 선례
