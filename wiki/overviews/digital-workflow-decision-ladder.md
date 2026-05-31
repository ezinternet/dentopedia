---
title: "Digital Workflow — IOS·CAIS·AI·LLM Decision Ladder"
authors: Synthesis (Damian Lee)
year: 2026
date: 2026-05-26
doi: N/A
source: N/A
category: overviews
confidence: synthesis
pdf_path: N/A
pdf_filename: N/A
source_collection: synthesis
tags: [digital-workflow, intraoral-scanner, cad-cam, guided-surgery, ai, llm, decision-ladder, overview]
---

## 한줄요약

디지털 치의학 4축 — 구강내 스캐너 (IOS) 정확도·컴퓨터지원 임플란트 외과 (CAIS)·AI 임상 적용·LLM/ChatGPT 환자 응답. Vankos 2026 + Schiavon 2025 NMA + Najeeb 2025 + Zhang 2025 spine.

## Summary

본 페이지는 wiki/digital-workflow/ 28 paper의 4-axis spine. IOS는 단관·인레이에 임상 표준, 전악·무치악은 여전히 정확도 한계. AI는 진단 보조 단계, LLM은 환자 instruction 보조로 신중 적용.

핵심 명제 5개:
1. **IOS 단관·소악궁 임상 표준. 전악·무치악은 trueness 50-200 μm + 후방 연장 시 오차 누적. 무치악은 기공실 스캐너 우위** — Vitai 2023 NMA, Vankos 2026 SR+MA (34 in-vitro), Singh 2025 umbrella (10 SR), Achmadi 2025 scoping. [근거강함]
2. **즉시식립 CAIS (dynamic 또는 full-static) > freehand. NMA가 정확도 순위 정량화** — Schiavon 2025 SR+NMA (7 RCT 338 implant). [근거강함]
3. **AI 우식 검출 95% 정확도. 임플란트 종류 인식 93.8-98%. 임상 검증 부족 단계** — Najeeb 2025 SR (63편), Revilla-Leon 2021 SR (17편), Park 2023 retrospective. [합의수준]
4. **LLM 치과 환자 응답 정확도 82%, 임상 수용 가능 응답 70%. 모델 차이 큼, 사용자 검토 필수** — Zhang 2025 SR+MA (25편). [합의수준]
5. **AI CBCT 임플란트 drilling protocol 예측 93.8% 정확도. 1차 안정성 보조** — Sakai 2023 retrospective. [합의수준]

## Results

### 축 1 — Intraoral Scanner (IOS) 정확도

| Spine paper | Evidence | Key finding |
|---|---|---|
| [[digital-workflow/vitai-2023-intraoral-scanner-complete-arch-sr-network-ma]] | sr+nma | 전악 IOS — trueness·precision 기기별 순위. 후방 연장 오차↑ |
| [[digital-workflow/vankos-2026-digital-conventional-implant-impressions-edentulous]] | sr+ma (34편 in-vitro) | 무치악 전악 IOS vs 전통 인상 — RMS NS. 전통도 유효 |
| [[digital-workflow/singh-2025-intraoral-scanners-accuracy-umbrella-review]] | sr+ma (umbrella, 10 SR) | TRIOS 3·Primescan 전악 최상. 무치악 한계 |
| [[digital-workflow/achmadi-2025-intraoral-scanner-edentulous-accuracy-scoping]] | sr (scoping, 8편) | 무치악 — 기공실 스캐너가 IOS보다 우위 |
| [[digital-workflow/buhl-2025-intraoral-scanner-full-arch-accuracy-invitro]] | in-vitro | 전악 trueness 50-200 μm. 기기 간 유의차. 구치부 오차↑ |
| [[digital-workflow/ciocan-2024-intraoral-scanners-comparison-four-in-vitro]] | in-vitro (4종 IOS) | 단일 수복 임상 허용. 전치 vs 구치 순위 상이 |
| [[digital-workflow/alkadi-2023-intraoral-scanner-accuracy-factors]] | narrative-review | 스캐너 기술·악궁 크기·술자 경험·온도·분말 다인자 |

**임상 ladder (IOS 적응)**:
1. **단관 (전·구치)** → IOS 1st choice. trueness 임상 허용 (50-100 μm). 시간 절약, 환자 편의.
2. **소악궁 부분 무치 (3-4 unit)** → IOS 가능. 정확도 충분.
3. **전악 자연치** → IOS 가능하나 기기 선택 신중 (TRIOS 3·Primescan 추천). 후방 연장 오차 유의.
4. **무치악 전악** → 전통 인상 또는 기공실 스캐너 1차. IOS는 보조.
5. **임플란트 여러 개 splinted 보철** → photogrammetry 또는 splint + IOS hybrid 옵션 (현 본 wiki에 별도 paper 없음).

### 축 2 — Computer-Assisted Implant Surgery (CAIS)

| Spine paper | Evidence | Key finding |
|---|---|---|
| [[digital-workflow/schiavon-2025-computer-assisted-immediate-implant-accuracy-nma]] | sr+nma (7 RCT 338 imp 291명) | 즉시식립 dynamic/full-static/partial-static vs freehand — 정확도 순위 |
| [[digital-workflow/lu-2021-digital-stackable-osteotomy-template-precision]] | case-report (n=4) | Stackable digital template — 절골+식립 가이드 일체 |
| [[digital-workflow/jamil-2020-surgeon-reliability-implant-high-risk-panoramic]] | prospective (148 imp) | 파노라마만으로 길이 선택 — 술자 신뢰도 측정 |
| [[digital-workflow/cebrian-carretero-2014-free-flap-implant-guided-surgery]] | narrative-review | Free flap 재건 환자 — guided implant가 골/금속 회피에 유리 |

**임상 ladder (CAIS 선택)**:
1. **단순 single-tooth implant + 단순 anatomy** → Freehand 가능 (술자 숙련).
2. **다중 implant 또는 심미부위** → Full-static (template) 권장. 정확도 우위 NMA에서 확인.
3. **즉시식립 + buccal plate 보존 우선** → Schiavon 2025 NMA — dynamic 또는 full-static.
4. **Free flap 재건 환자** → Guided가 거의 필수.
5. **All-on-X full-arch** → Full-static + photogrammetry verification 권장.

### 축 3 — AI in Dental Practice (이미지·진단·예측)

| Spine paper | Evidence | Key finding |
|---|---|---|
| [[digital-workflow/najeeb-2025-ai-restorative-dentistry-review]] | sr (63편, 2020-2025) | 수복치의학 AI — 우식 검출 정확도 95%. 진료시간 단축 |
| [[digital-workflow/revilla-leon-2021-artificial-intelligence-implant-dentistry-sr]] | sr (17편) | 임플란트 AI — 종류인식 93.8-98%, 성공예측 62.4-80.5% |
| [[digital-workflow/sakai-2023-ai-drilling-protocol-cbct-implants]] | retrospective | CBCT 기반 drilling protocol 예측 — 93.8% 정확도 |
| [[digital-workflow/park-2023-deep-learning-implant-size-classification]] | retrospective | 임플란트 직경·길이 9그룹 — 정확도 > 0.994 |
| [[digital-workflow/oh-2023-deep-learning-osseointegration-prediction-radiographs]] | retrospective (580명) | 파노라마+PA로 골유착 예측 — 신뢰성 있음. 다기관 검증 필요 |
| [[digital-workflow/chi-2026-deep-learning-periapical-radiograph-quality]] | retrospective (3594 PA) | PA 품질 평가 — AUC 0.924-1.000. 재촬영 감소 |
| [[digital-workflow/aminoshariae-2024-ai-endodontic-education-scoping]] | sr (35편) | 근관치료 교육 AI 10영역 |
| [[digital-workflow/gao-2025-ai-dentistry-narrative-review]] | narrative-review | 6대 전공 AI 진단·치료 적용 총론 |
| [[digital-workflow/lee-2025-ai-dentistry-emerging-applications-narrative]] | narrative-review (120편) | 3축 — 교육·환자 진료·진료실 관리 |
| [[digital-workflow/srinivasan-2025-artificial-intelligence-dental-implants-review]] | narrative-review | 임플란트 AI 임상 적용 총론 |
| [[digital-workflow/mallineni-2024-ai-dentistry-descriptive-review]] | descriptive-review | 모든 치과 분야 AI 진입 — 방사선 진단 위주 |
| [[digital-workflow/faiyazuddin-2025-ai-healthcare-comprehensive-review]] | narrative-review | 의료 AI 광역 리뷰 |
| [[digital-workflow/mizna-2025-ai-healthcare-practice-review]] | narrative-review | 의료 AI 실무 — 로봇 보조 수술·재활·영상 |
| [[digital-workflow/altalhi-2023-artificial-intelligence-impact-dental-implantology]] | narrative-review | 임플란트 AI 임상 주의 (표준화 부재) |
| [[digital-workflow/saeed-2023-robotic-artificial-intelligence-implant-dentistry]] | narrative-review | 로보틱스+AI 임플란트 — 윤리·비용·책임 과제 |

**임상 ladder (AI 적응)**:
1. **AI 우식 검출** — 판독 보조로 활용. 최종 판단 술자.
2. **임플란트 종류 식별** — 환자 기록 누락 시 보조 도구로 합리적 (정확도 ≥ 93.8%).
3. **AI 골유착 예측·1차 안정성 예측** — 임상 검증 부족. 술자 판단 우선.
4. **AI 진단** — 정확도 높으나 데이터 프라이버시·알고리즘 편향·블랙박스 인지 필수.
5. **현재 수준** — AI는 진단 보조·교육 보조. 자율 치료 결정은 아직.

### 축 4 — LLM (ChatGPT 등) Patient Communication

| Spine paper | Evidence | Key finding |
|---|---|---|
| [[digital-workflow/zhang-2025-llm-patient-instructions-dentistry-sr-ma]] | sr+ma (25편) | LLM 치과 응답 — 정확도 82%, 임상 수용 70%. ChatGPT 우위 |
| [[digital-workflow/iqbal-2025-chatgpt-healthcare-umbrella-review]] | sr (umbrella, 17편) | ChatGPT 의료 — 진단·임상 결정 주제. AMSTAR-2 품질 등급 중-낮음 |

**임상 ladder (LLM 사용)**:
1. **환자 instruction 초안 작성** — LLM 활용 후 술자 검토. 직접 환자 제공 금지.
2. **환자 질문 빈출 응답** — FAQ 초안 LLM, 의학적 정확성 검증 필수.
3. **진단·치료 결정** — LLM 직접 사용 부적합. 보조 reasoning 도구 정도.
4. **개인정보 입력 금지** — 환자 식별 정보 LLM에 절대 입력 안 함 (한국 개인정보 보호법 + HIPAA 등).

## Phase 2 확장 후보 (Stub)

- [ ] `wiki/overviews/ios-edentulous-protocols.md` — 무치악 IOS 정확도 향상 strategy.
- [ ] `wiki/overviews/cais-dynamic-vs-static.md` — Dynamic vs static guided surgery 깊이.
- [ ] `wiki/overviews/ai-caries-detection-deep-dive.md` — 우식 검출 AI 임상 도입 평가.
- [ ] `wiki/overviews/llm-patient-communication-protocol.md` — 환자 응답 LLM 사용 SOP + 한국 법적 frame.

## Related Papers (전체 28편, 위 본문 인용)

## Additional Spokes — CBCT 해부학 평가 (2026-05-26 추가)

| Spine paper | Evidence | Key finding |
|---|---|---|
| [[digital-workflow/luz-2018-maxillary-sinus-3d-cbct-evaluation]] | retrospective (128 sinus, 64명) | SMOP 임플란트 계획 SW로 상악동 osseous + 점막(공기화) 부피 정량화 — 술전 계획 표준화 시도 |

**임상 함의**: CBCT 기반 sinus 부피 자동 측정은 sinus lift 계획에 직접 활용. SMOP 같은 implant planning SW의 측정 정확도는 cross-validation 필요. [합의수준]

## Related overviews

- [[overviews/immediate-implant-decision-ladder]] — IIP guided surgery (축 2)
- [[overviews/implants-clinical-decision-ladder]] — 임플란트 디자인·AI 예측 (축 3)
- [[overviews/prosthetic-materials-decision-ladder]] — CAD/CAM 보철

확신도 등급:
- 축 1 IOS = [근거강함] (다수 SR + NMA).
- 축 2 CAIS = [근거강함] (Schiavon 2025 NMA).
- 축 3 AI 진단 정확도 = [합의수준] (대부분 retrospective + narrative).
- 축 4 LLM = [합의수준] (단일 SR+MA + umbrella).
