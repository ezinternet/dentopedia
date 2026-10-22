---
title: "Ingest batch — bone-graft biological properties (골이식 생물학적 특성 축) 16편"
date: 2026-10-22
type: log
tags: [ingest, bone-regeneration, sinus-lift, ridge-preservation, bone-biology, periodontics, surveillance]
---

# 인제스트 배치 — 골이식 생물학적 특성 축 16편 (2026-10-22)

## 1. 배경

`logs/2026-10-22_surveillance-bone-graft-properties.md`의 서베일런스(`bone-graft-properties` 토픽,
PubMed 검색 515건 → 중복 제거 → 스크리닝 → include 228 / exclude 255) 결과 중 **사용자가 축 지정한
핵심 후보 16건**만 우선 인제스트했다. 남은 212건은 큐에 대기 상태.

## 2. 문헌 확보(Acquisition) — 전문 6편 / 초록 전용 10편

PMC OA API(`oa.fcgi`)가 **404로 폐기**되어 있어(`fetch-oa.py` tier1 경로失效), 전문 확보는
`scripts/pubmed-fetch-fulltext.py`(E-utilities → PMC JATS → `papers/{stem}.txt`)로 대체했다.
OA 사본 탐색은 PMC · Unpaywall · OpenAlex 3경로를 모두 확인했고, 10편은 어디에도 OA 사본이 없었다
(Wiley·Elsevier 직접 PDF도 Cloudflare 403으로 차단). → Illegal 경로는 쓰지 않고 초록 전용 분기
(`source_collection: pubmed-text` + `full_text: false` + 본문 상단 `abstract-only` 고지)로 처리.

| 구분 | 건수 | 처리 |
|---|---|---|
| PMC 전문 확보 | 6 | `full_text: true`, `text_path`/`text_filename` |
| 초록 전용(closed) | 10 | `full_text: false` + `abstract-only — full text not retrieved` 고지 |

전용 6편: 39901815, 37047413, 35224778, 39478364, 42740456, 41289609
초록 전용 10편: 36645164, 41526568, 38905116, 35511290, 36305933, 39946741, 40459982, 40214305, 41944755, 41052564

## 3. 파이프라인

1. **Step 0 중복 게이트** — `scripts/dedup-check.py --doi <doi>` 16건 전부 exit 0 (Tier 1 중복 없음).
2. **Step 3.5 기존 페이지 조회** — `qmd search`(BM25)로 카테고리 경계·supersession·contradicts 후보 확인.
3. **Step 4 카테고리** — `wiki/_meta/categories.md` 기준 확정(아래 §5).
4. **Step 5–6 작성** — `sources/{stem}.md` + `wiki/{category}/{stem}.md` 32개 파일.
   병렬 배치(논문당 서브에이전트 1 → 2 wave × 8편), 부모가 최종 검증·승인.
5. **Step 4 index.md** — 16줄 등재(신규 16줄만 추가, 삭제 0줄).
6. **Phase 2 finalize** — `scripts/ingest-one.py --finish` 16회: 커밋 55건 → `git push origin main` → `qmd update && qmd embed`.

## 4. 인제스트 16건 (결과)

| # | PMID | stem | 카테고리 | 근거등급 | 전문 | 핵심 결과 |
|---|---|---|---|---|---|---|
| 1 | 39901815 | spanninga-2025 | bone-regeneration | sr | ✅ | P-15 펩타이드 이식대체물(ABM/P-15) SR(인체 28편): 경추융합 88.97% vs 자가골 85.82%(비열등성 p=0.0004) |
| 2 | 36645164 | van-2023 | sinus-lift/lateral | rct | ❌ | 골유도성 CaP(나침형 표면) vs 입자상 CaP vs 자가골 — 양 모델 + 10명 전환 RCT |
| 3 | 41526568 | jafari-2026 | **periodontics** | sr+ma | ❌ | bioactive glass 치주재생 SR+MA(12 RCT): PD −1.27mm(p=0.0006), CAL +1.49mm(p=0.0005) |
| 4 | 37047413 | ogui-2023 | bone-regeneration/ridge-preservation | rct | ✅ | 자가골 치아기질(ADG) vs 이종골 혼합 ARP: 신생골 72.55±12.14% |
| 5 | 38905116 | krennmair-2024 | sinus-lift/lateral | rct | ❌ | ABBM 입자 크기 효과 없음(신생골 P=.640), 골-이식재 접촉만 소입자 우위 |
| 6 | 35511290 | harlos-2022 | sinus-lift/lateral | rct | ❌ | 이종골+자가골 70:30이 신생골 면적 최대(2678 μm²), L-PRF 이점 미확인 |
| 7 | 35224778 | galindomoreno-2022 | sinus-lift/lateral | rct | ✅ | 소뼈 vs 돼지골 이종골: 광화조직 29.24% vs 32.51%(p=.570) → 돼지골은 DBBM 대체 가능 |
| 8 | 36305933 | bhatavadekar-2022 | bone-regeneration | rct | ❌ | 소뼈 vs 돼지골, HRA+ESP(군별 10명): 돼지골의 치수변동이 더 작음 |
| 9 | 39946741 | dhondt-2026 | implants/vertical-ridge-augmentation | rct | ❌ | L-PRF 골블록 vs 자가골+DBBM 수직 GBR(6명): VBH 차이 없음(P=.96) |
| 10 | 40459982 | ahmadpour-2025(melatonin) | bone-regeneration | sr | ❌ | 멜라토닌 국소전달 SR(24편): 91.7%가 대조군보다 우위 보고 |
| 11 | 40214305 | ahmadpour-2025(hormonal) | bone-regeneration | sr | ❌ | PTH·GH·칼시토닌 국소전달 SR(22편, 전임상 100%): GH 87.5%·PTH 66.7%·칼시토닌 60% |
| 12 | 39478364 | wei-2025 | bone-regeneration/ridge-preservation | rct | ✅ | ErhBMP-2/β-TCP 발치와 RCT(n=40): 6주 신생골 7.72% vs 2.96% vs 8.37% |
| 13 | 42740456 | monje-2026 | bone-regeneration | sr+ma | ✅ | 생체치료제+스캐폴드 SR+MA(23 RCT, n=1078): 폭 +0.30~0.48mm, 상악동거상은 무효과 |
| 14 | 41289609 | de-2026 | bone-regeneration | sr | ✅ | 협유지방 유래 줄기세포(BFPSC) 골재생 SR(임상 6편 49명), ROBINS-I 5/6편 중대한 위험편향 |
| 15 | 41944755 | chou-2026 | bone-regeneration | sr | ❌ | 소아 치조열 rhBMP-2 동종골 vs ICBG SR(21편): 골형성 무차이 우세, 수술·입원 기간 단축 |
| 16 | 41052564 | hakimiha-2025 | **bone-biology** | sr | ❌ | PBM(광생물조절)이 구강·지방유래 MSC 골형성분화 증진 SR(체외 19편) |

## 5. 부모(메인 세션) 판정 — 3건

### 5-1. supersession — `monje-2026` vs `suarez-lopez-del-amo-2022` (AAP BEC 2022) → **superseded_by 안 함**

서브에이전트가 `escalate:supersession`으로 올린 건을 직접 두 페이지를 읽고 판정했다.

- AAP BEC 2022 결론: biologics는 "조직 질 향상제이지 치수 개선제가 아니다"(정성 종합만, 39 RCT).
- monje-2026: 스캐폴드 **병용** 조합에서 골증대 폭 WMD 0.30mm(p<0.001), ARP 폭 0.48mm(p=0.035)·높이 0.40mm(p<0.001) — **통계적 유의, 임상적 1mm 미만**, I² 74–98%, 교란편향 일부 검출, 상악동거상은 무효과(p=0.878).
- 판정: 2022년 페이지의 clinical bottom line을 **뒤집지 않는다**(범위·중재 조합이 다르고, 1mm 미만 효과는 실제로 "치수 개선제"의 근거로 삼기 어려움). 따라서 `superseded_by`를 **쓰지 않**고, typed edge는 `refines`(한정)로 유지. 2022 페이지의 본문·프런트매터는 수정하지 않는다(forward-only 트리거 미해당: "bottom line을 뒤집는가?" = 아니오).

### 5-2. 카테고리 — `jafari-2026` = **periodontics** (브리프 힌트 `bone-regeneration` 아님) → 승인

근거: 지표가 치주 결손 재생(PD/CAL)이고, 동일 형태(골 대체재를 치주 골내결손에 적용한 SR+MA)의 선행 페이지
`periodontics/jasser-2021-effectiveness-beta-tricalcium-phosphate-comparison`(β-TCP)와
`periodontics/mahintach-2026-ha-vs-emd-intrabony-defects-sr-ma`가 `periodontics`에 있음
(categories.md 라우팅 원칙 1: 유사 페이지의 카테고리를 따름). 지시-특정 SR은 `bone-regeneration`의
재료 축(haugen·zhao·spangana 등 일반 서술 페이지)과 축이 달라 `periodontics`가 일관적.

### 5-3. 카테고리 — `hakimiha-2025` = **bone-biology** (브리프 힌트 `bone-regeneration` 아님) → 승인

근거: 광생물조절(PBM)의 MSC 골형성 **분자·세포 기전**이 대상이고 임상 술식이 아님.
`categories.md`의 `bone-biology`("Molecular/cellular bone biology") 정의와 일치.

## 6. 감사 결과 (2026-10-22)

| 감사 | 결과 |
|---|---|
| `scripts/lint.py` | 신규 16건 오류 **0건** (잔여 14건은 기존 파일: baggio·cook·friedmann·huang·smidt·ulm·canullo·smith·yuan) |
| `scripts/content-lint.py` | 신규 16건 오류 **0건** |
| `scripts/orphan-check.py` | 신규 orphan **0건** (잔여 2건: baggio·ulm — 기존) |
| `scripts/pii-guard.py` | 위반 **0건** (13,964 files) |
| `scripts/relations-audit.py` | dangling edge **0건** (circular 4·postdated 43은 기존 신호) |
| `scripts/link-integrity.py` | 신규 broken link **0건** — 단 `monje-2026`의 잘못된 경로 1건(`ridge-preservation/caponio-2023…` → `bone-regeneration/caponio-2023…`) 수정 |
| `scripts/supersession-audit.py` | 0 sync issues ✓ |
| `scripts/ingest-rationale-lint.py` | 신규 오류 0건 (9건은 기존) |

## 7. 정정·기록

- 중국어 문자 유입 2건을 정정: `van-2023` "양(羊)" → "양(sheep)", `de-2026` "협유지방垫" → "협유지방(Buccal Fat Pad)".
- `index.md` 삽입 중 접두 일치로 기존 2줄(franchi-2005·chacon-2024)이 잘렸으나 원문 복구 완료
  (현재 index.md diff = 신규 16줄 추가 / 삭제 0줄).
- 편차 53건은 `logs/ingest-deviations.md`에 기록(abstract-only 10 · category-judgment 9 · relation-judgment 9 · evidence-level-judgment 4 · supersession-judgment 4 · reporting-judgment 2 · source-data-issue 3 · 기타).
- 큐: `.ingest-queue` pending 0 · processed 34 → **50**.

## 8. 남은 작업

- `bone-graft-properties` 큐에 대기 중인 **212건** 미처리(그 중 OA:PMC 약 24건).
- 사용자에게 제시한 나머지 2개 선택지: (b) 동종골(allograft) 서베일런스 라운드, (c) 큐 228건 → 상위 20건 압축.
