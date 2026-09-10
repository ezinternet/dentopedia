---
title: "Digital Workflow — IOS·CAIS·AI·LLM Decision Ladder"
authors: Synthesis (Damian Lee)
year: 2026
date: 2026-05-26
doi: N/A
source: N/A
category: overviews
evidence_level: synthesis
pdf_path: N/A
pdf_filename: N/A
source_collection: synthesis
tags: [digital-workflow, intraoral-scanner, cad-cam, guided-surgery, ai, llm, decision-ladder, overview]
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 핵심 명제: 디지털 치의학을 4축(구강내스캐너(Intraoral Scanner, IOS) 정확도·컴퓨터지원 임플란트수술(Computer-Assisted Implant Surgery, CAIS)·AI 진단·LLM 환자응답)으로 묶은 31편 spine 결정 사다리 (2026-09: +3편).
> - 축1 IOS: 단관·소악궁(3–4 unit)은 임상 표준(trueness 50–100µm), 전악 자연치는 기기 신중 선택(TRIOS 3·Primescan), 무치악 전악은 전통 인상 또는 기공실 스캐너 1차 — IOS는 보조. [확인]
> - 전악 IOS는 후방 연장 시 오차 누적(trueness 50–200µm), 구치부 오차 증가가 일관된 한계.
> - 축1 보강(2026-09): 고정성 교정장치(브라켓±와이어) 존재 시엔 자연치 원칙이 뒤집혀 IOS가 알지네이트보다 우수(28–141 vs 103–212µm, Schlenz 2022); 클리어얼라이너 부착물 모형에서도 Primescan·TRIOS 3가 최상위 재확인, 오차 목표 ~50µm(Oğuz 2026); 정확도가 혼재된 상황에서도 chairside time·환자 편의는 측정된 연구 전부에서 IOS 우위이나 근거는 10편 중 2편 한정(Ramos-Morro 2026). [확인]
> - 축2 CAIS: 즉시식립·심미부·다중 임플란트는 full-static 또는 dynamic이 freehand 우위(Schiavon 2025 NMA, 7 RCT 338 임플란트). 단순 단일치는 freehand 가능, Free flap 재건은 가이드 거의 필수. [확인]
> - 축3 AI: 우식 검출 정확도 약 95%, 임플란트 종류 인식 93.8–98%, 골유착 예측·치근단 품질평가(AUC 0.924–1.000) — 모두 진단·교육 보조 단계, 임상 검증 부족, 자율 치료 결정은 아직. [확인]
> - 축4 LLM: 치과 환자 응답 정확도 약 82%·임상 수용 약 70%, 모델 차이 큼 → instruction 초안 작성 후 술자 검토 필수, 직접 환자 제공 금지, 진단·결정 부적합. [확인]
> - LLM·AI 공통 제약: 환자 식별정보 입력 절대 금지(개인정보보호법+HIPAA), 데이터 프라이버시·알고리즘 편향·블랙박스 인지 필수.
> - 신규 spoke: 자율로봇 CAIS(Yu 2025·Wei 2025·Chen 2025·Wu 2024)는 dynamic navigation 대비 각도·플랫폼·첨부 편차를 개선하나 시술시간 증가 등 trade-off 존재.
> - CBCT 기반 상악동 부피 자동측정(Luz 2018, SMOP)은 sinus lift 계획에 직접 활용 가능하나 측정 정확도 cross-validation 필요.
> - 확신도 등급: IOS·CAIS = [확인](다수 SR+NMA), AI 진단 정확도·LLM = [확인](대부분 retrospective+narrative, 단일 SR+MA).

## Three-line Summary

Synthesis decision-ladder over 31 digital-dentistry papers on four axes: IOS accuracy (4 SR/umbrella + 4 in-vitro + 1 case report, +3 added 2026-09), CAIS (SR+NMA), AI diagnostics (multiple SR/retrospective), and LLM patient communication (SR+MA + umbrella); IOS is the clinical standard for single crowns and short spans (trueness 50–100 µm) but accuracy degrades on full-arch/edentulous (trueness 50–200 µm, posterior error accumulation; laboratory scanner or conventional impression preferred for fully edentulous). Appliance/attachment geometry conditions this further: fixed orthodontic appliances flip the natural-teeth preference toward IOS (Schlenz 2022), clear-aligner attachment scanning reconfirms Primescan/TRIOS 3 as top-tier with a ~50 µm error target (Oğuz 2026), and even where raw accuracy is mixed, chairside time and patient comfort consistently favor IOS (Ramos-Morro 2026 SR, though based on only 2/10 included studies).

CAIS: dynamic or full-static guidance beats freehand for immediate, esthetic, and multiple implants (Schiavon 2025 SR+NMA, 7 RCTs, 338 implants); AI diagnostics achieve caries detection ≈95% accuracy, implant-type recognition 93.8–98%, and osseointegration prediction AUC 0.924–1.000 — all diagnostic/educational aids only, insufficient clinical validation for autonomous treatment decisions.

LLM dental responses reach ≈82% accuracy and ≈70% clinically acceptable responses (Zhang 2025 SR+MA, 25 studies; ChatGPT leads); must be used only for drafting patient instructions with mandatory clinician review, never for direct patient delivery or diagnostic decisions; no patient-identifying data input (HIPAA/Korean data-protection law).

## 세줄요약

28편 4축 결정 사다리(IOS 정확도 4 SR/우산형+2 in-vitro, CAIS SR+NMA, AI 진단 다수 SR/후향, LLM SR+MA+우산형): IOS는 단관·소악궁 임상 표준(trueness 50–100µm)이나 전악·무치악 오차 누적(50–200µm), 무치악은 기공실 스캐너·전통 인상 우선.

CAIS: 즉시식립·심미·다중 임플란트에서 dynamic/full-static이 freehand 우위(Schiavon 2025 SR+NMA, 7 RCT, 338 임플란트); AI 진단은 우식 검출 ≈95%·임플란트 종류 인식 93.8–98%·골유착 예측 AUC 0.924–1.000 — 모두 진단·교육 보조 단계, 자율 치료 결정 불가.

LLM 치과 응답 정확도 ≈82%·임상 수용 ≈70%(Zhang 2025 SR+MA, 25편); 환자 지침 초안 작성 후 술자 검토 필수·직접 환자 제공 금지·환자 식별정보 입력 절대 금지(HIPAA·개인정보보호법).

## 세줄요약

디지털 치의학 4축 — 구강내 스캐너 (IOS) 정확도·컴퓨터지원 임플란트

외과 (CAIS)·AI 임상 적용·LLM/ChatGPT 환자 응답. Vankos 2026 +

Schiavon 2025 NMA + Najeeb 2025 + Zhang 2025 spine.

## Summary

본 페이지는 wiki/digital-workflow/ 28 paper의 4-axis spine. IOS는 단관·인레이에 임상 표준, 전악·무치악은 여전히 정확도 한계. AI는 진단 보조 단계, LLM은 환자 instruction 보조로 신중 적용.

핵심 명제 5개:
1. **IOS 단관·소악궁 임상 표준. 전악·무치악은 trueness 50-200 μm + 후방 연장 시 오차 누적. 무치악은 기공실 스캐너 우위** — Vitai 2023 NMA, Vankos 2026 SR+MA (34 in-vitro), Singh 2025 umbrella (10 SR), Achmadi 2025 scoping. [확인]
2. **즉시식립 CAIS (dynamic 또는 full-static) > freehand. NMA가 정확도 순위 정량화** — Schiavon 2025 SR+NMA (7 RCT 338 implant). [확인]
3. **AI 우식 검출 95% 정확도. 임플란트 종류 인식 93.8-98%. 임상 검증 부족 단계** — Najeeb 2025 SR (63편), Revilla-Leon 2021 SR (17편), Park 2023 retrospective. [확인]
4. **LLM 치과 환자 응답 정확도 82%, 임상 수용 가능 응답 70%. 모델 차이 큼, 사용자 검토 필수** — Zhang 2025 SR+MA (25편). [확인]
5. **AI CBCT 임플란트 drilling protocol 예측 93.8% 정확도. 1차 안정성 보조** — Sakai 2023 retrospective. [확인]

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
| [[digital-workflow/schlenz-2022-transfer-accuracy-digital-conventional-full-arch]] | in-vitro (reference-aid, 5 IOS) | 고정성 교정장치(브라켓±와이어) 존재 시 IOS가 알지네이트보다 전이정확도 우수(28–141 µm vs 103–212 µm, p<0.001); 자연치 단독은 알지네이트가 최상(21±20 µm) |
| [[digital-workflow/oguz-2026-trueness-precision-intraoral-scanners-3d-printed]] | in-vitro (5 IOS, 3D프린팅 모형) | 클리어얼라이너 컴포지트 부착물 모형에서 Primescan·TRIOS 3 최상위 동률, Rapideye MI-1000 최하위(p<0.001); 얼라이너 워크플로 스캐너 오차 목표 ~50µm 제안(1단계 이동량 ~250µm의 20%) |

**임상 ladder (IOS 적응)**:
1. **단관 (전·구치)** → IOS 1st choice. trueness 임상 허용 (50-100 μm). 시간 절약, 환자 편의.
2. **소악궁 부분 무치 (3-4 unit)** → IOS 가능. 정확도 충분.
3. **전악 자연치** → IOS 가능하나 기기 선택 신중 (TRIOS 3·Primescan 추천). 후방 연장 오차 유의.
4. **무치악 전악** → 전통 인상 또는 기공실 스캐너 1차. IOS는 보조.
5. **임플란트 여러 개 splinted 보철** → photogrammetry 또는 splint + IOS hybrid 옵션 (현 본 wiki에 별도 paper 없음).
6. **고정성 교정장치(브라켓±와이어) 환자 전악 인상** → IOS 우선(알지네이트 대비 정확도·시간 모두 우위, Schlenz 2022). 단 자연치만 있는 부위는 알지네이트가 여전히 근소 우위이므로 혼합 치열 전악에서는 IOS 일괄 채득이 실무적.
7. **클리어얼라이너 리파인먼트 스캔(부착물 존재 모형)** → Primescan·TRIOS 3 우선 기기; 스캐너 오차 목표 ~50 µm 유지(1단계 계획 이동량의 ~20%), 인접면·언더컷·부착물 주변부가 오차 집중 구간이므로 해당 부위 재스캔 확인(Oğuz 2026).

### 축 2 — Computer-Assisted Implant Surgery (CAIS)

| Spine paper | Evidence | Key finding |
|---|---|---|
| [[digital-workflow/schiavon-2025-computer-assisted-immediate-implant-accuracy-nma]] | sr+nma (7 RCT 338 imp 291명) | 즉시식립 dynamic/full-static/partial-static vs freehand — 정확도 순위 |
| [[digital-workflow/lu-2021-digital-stackable-osteotomy-template-precision]] | case-report (n=4) | Stackable digital template — 절골+식립 가이드 일체 |
| [[digital-workflow/jamil-2020-surgeon-reliability-implant-high-risk-panoramic]] | prospective (148 imp) | 파노라마만으로 길이 선택 — 술자 신뢰도 측정 |
| [[oral-surgery/cebrian-carretero-2014-free-flap-implant-guided-surgery]] | narrative-review | Free flap 재건 환자 — guided implant가 골/금속 회피에 유리 |

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

### 신규 추가 (2026-06)
#### Robotic CAIS — autonomous robot vs dynamic navigation (2026-06-07)
- [[digital-workflow/yu-2025-autonomous-robotic-versus-dynamic-navigation]] — Yu 2025 prospective: 자율로봇 각도/플랫폼/첨부 편차 ≈½ vs dynamic nav
- [[digital-workflow/wei-2025-autonomous-robotic-surgery-dynamic-navigation]] — Wei 2025 RCT: 동일 tracker 통제 시 로봇은 각도만 유의 개선, 시술시간 ↑
- [[digital-workflow/chen-2025-robot-assisted-dynamic-navigation-accuracy]] — Chen 2025 retro: semi-autonomous robot 플랫폼·첨부 우위, 각도 동등
- [[digital-workflow/wu-2024-autonomous-dental-implant-robotic-accuracy]] — Wu 2024 single-arm: 자율로봇 절대정확도(coronal 0.61mm·angular 2.56°)

- [[digital-workflow/jkda-2025-63-5-003]] — In vitro pilot (경북대 보철과 이규복·김소연, JKDA 2025): 3D 프린팅 zirconia crown의 offset parameter별 marginal·internal fit 비교 — preliminary pilot. (in-vitro, 2025)

### 신규 추가 (2026-09)

- [[digital-workflow/lee-2019-full-mouth-rehabilitation-reduced]] — 증례보고 (서울대 보철과, 78세 여성): 다발성 상실치·심한 마모에 의한 교합 수직 고경(OVD) 감소 환자에 전악 디지털 워크플로우 적용. 심미·기능 회복의 디지털 계획·제작 파이프라인 실례. (case-report, 2019)
- [[digital-workflow/schlenz-2022-transfer-accuracy-digital-conventional-full-arch]] — in-vitro (팬텀헤드, reference-aid): 고정성 교정장치(브라켓±와이어) 유무별 IOS 5종 vs 알지네이트 전악 전이정확도. 장치 있으면 IOS 역전 우위. (in-vitro, 2022)
- [[digital-workflow/oguz-2026-trueness-precision-intraoral-scanners-3d-printed]] — in-vitro (İnönü대): 클리어얼라이너 컴포지트 부착물 3D프린팅 모형 30개, IOS 5종 trueness/precision 비교. Primescan·TRIOS 3 최상위. (in-vitro, 2026)
- [[digital-workflow/ramos-morro-2026-patient-perception-reliability-reproducibility-chairside]] — SR (PRISMA 2020+QUADAS-2, 10편): IOS vs 재래식 인상 정확도(혼재)·chairside time·환자 편의(VAS, 둘 다 IOS 우위). (sr, 2026)

## Additional Spokes — CBCT 해부학 평가 (2026-05-26 추가)

| Spine paper | Evidence | Key finding |
|---|---|---|
| [[digital-workflow/luz-2018-maxillary-sinus-3d-cbct-evaluation]] | retrospective (128 sinus, 64명) | SMOP 임플란트 계획 SW로 상악동 osseous + 점막(공기화) 부피 정량화 — 술전 계획 표준화 시도 |

**임상 함의**: CBCT 기반 sinus 부피 자동 측정은 sinus lift 계획에 직접 활용. SMOP 같은 implant planning SW의 측정 정확도는 cross-validation 필요. [확인]

## Related overviews

- [[overviews/immediate-implant-decision-ladder]] — IIP guided surgery (축 2)
- [[overviews/implants-clinical-decision-ladder]] — 임플란트 디자인·AI 예측 (축 3)
- [[overviews/prosthetic-materials-decision-ladder]] — CAD/CAM 보철

확신도 등급:
- 축 1 IOS = [확인] (다수 SR + NMA).
- 축 2 CAIS = [확인] (Schiavon 2025 NMA).
- 축 3 AI 진단 정확도 = [확인] (대부분 retrospective + narrative).

## Evidence Update — Full-Arch IOS Accuracy for Implant Frameworks (Fouda 2025)

Fouda 2025 (in vitro micro-CT, 10 full-arch titanium frameworks from TRIOS 5 IOS scans, 4-implant edentulous model; Scanco µ100 as reference at 36.8 µm voxel) provides a sobering precision benchmark for implant-supported full-arch workflows. Only 3/10 frameworks passed micro-CT passivity criteria; 0/10 met the single-screw-test; and only 2/10 intraoral scans fell within 150 µm RMS deviation. The authors identified IOS scanning error — not milling or design — as the dominant source of misfit. For full-arch implant cases, this data argues for: (1) laboratory scan verification of IOS accuracy before milling, (2) clinical passive-fit verification protocols at try-in, and (3) accepting that even modern IOS systems may have difficulty with long-span full-arch implant cases at the precision required for passive fit.

- [[digital-workflow/fouda-2025-accuracy-digital-workflow-implant-fullarch]] — micro-CT: 70% of full-arch IOS-to-framework cases fail passivity; scanning error dominates; laboratory verification essential.
- 축 4 LLM = [확인] (단일 SR+MA + umbrella).

## Evidence Update — Appliance/Attachment Geometry & Patient-Facing Outcomes (2026-09)

세 편 추가로 축1을 보강: (1) **고정장치·부착물이 있을 때의 IOS 정확도**, (2) **정확도와 별개로 일관된 시간·편의 우위**.

**Schlenz 2022** (in-vitro, reference-aid 방식·팬텀헤드, IOS 5종 vs 알지네이트, 5개 세팅 × 12회 반복)는 고정성 교정장치(FOA: 금속/세라믹 브라켓 ± 와이어) 존재가 전악 전이정확도에 미치는 영향을 best-fit superimposition이 아닌 독립 기준체(4개 강구, CMM 측정)로 검증했다. 브라켓이 있는 모든 세팅에서 IOS가 알지네이트보다 편차가 작았다(IOS 28±23–141±140 µm vs CAI 103±103–212±204 µm, 전 비교 p<0.001) — 단 자연치만 있는 경우엔 알지네이트가 최상(21±20 µm). 즉 "자연치엔 알지네이트가 유리하나, 브라켓·와이어가 들어가면 IOS로 역전"이라는 조건부 결론이며, 이는 기존 축1의 "IOS는 단관·소악궁 표준" 원칙에 **appliance 유무라는 새 조건**을 추가한다. Medit i500이 IOS 중 편차가 가장 컸지만 알지네이트보다는 항상 우수했다.

**Oğuz 2026** (in-vitro, IOS 5종, 3D프린팅 교정모형 30개, 클리어얼라이너 컴포지트 부착물)는 Schlenz의 "장치 geometry가 스캔 정확도를 좌우한다"는 축을 고정장치(브라켓)에서 클리어얼라이너 부착물로 확장했다. Primescan과 TRIOS 3가 trueness·precision 모두 최상위 동률(Kruskal-Wallis 둘 다 p<0.001), iTero Element 2 Plus·5D는 중간이나 임상 허용범위, Rapideye MI-1000은 전 지표 최하위. 저자들은 얼라이너 1단계당 계획 치아이동량(~250 µm)의 약 20%인 **~50 µm를 스캐너 오차 허용선**으로 제안했고, 오차는 인접면·언더컷·부착물 주변부에 집중됐다. 기존 축1의 기기 순위(TRIOS 3·Primescan 상위)를 얼라이너 워크플로에서도 재확인하는 결과다.

**Ramos-Morro 2026** (SR, PRISMA 2020+OSF 등록, 10편 횡단연구, 2016–2024, 성인/청소년 완전 치열)는 정확도만 놓고 보면 혼재된 결과(다수는 재래식 인상이 전악·후방부·장거리에서 우위, 일부는 IOS 우위, 다수는 동등)를 보고해 이 오버뷰의 "전악 IOS는 신중히"라는 기존 기조와 **모순되지 않는다**. 그러나 chairside time·환자 편의(VAS)를 측정한 소수 연구(각 2/10편)는 **예외 없이** IOS가 유의하게 빠르고 편했다(Sfondrini: 총 소요 5분49초 vs 22분6초, p=0.001; Janosi: 12분 vs 75.5분, p=0.001; VAS 편의 9.14 vs 2.57, 9.02 vs 6.5, 모두 p<0.001). 다만 QUADAS-2 상 대부분 연구가 환자선정 영역에서 위험도 불명확/높음(젊고 건강한 완전 치열 표본에 국한)이라 확정적 정확도 결론은 아니다. **임상 함의**: 정확도가 재래식과 동등하거나 근소 열세인 상황에서도, 총 진료시간·환자 편의라는 별개 축에서 IOS를 선택할 근거는 일관되다 — 단 이 시간 절감의 대부분은 의자옆(chairside) 시술 자체가 아니라 **석고모형 제작 등 후속 공정 생략**에서 온다는 점(Sfondrini: chairside만 비교 시 5분49초 vs 7분32초로 격차 훨씬 작음)을 감안해야 한다.

- [[digital-workflow/schlenz-2022-transfer-accuracy-digital-conventional-full-arch]] — in-vitro: FOA(브라켓±와이어) 존재 시 IOS가 알지네이트보다 전이정확도 우수(28–141 vs 103–212 µm); 자연치 단독은 알지네이트 우위(21±20 µm).
- [[digital-workflow/oguz-2026-trueness-precision-intraoral-scanners-3d-printed]] — in-vitro: 클리어얼라이너 부착물 모형에서 Primescan·TRIOS 3 최상위, Rapideye 최하위; 스캐너 오차 목표 ~50µm 제안.
- [[digital-workflow/ramos-morro-2026-patient-perception-reliability-reproducibility-chairside]] — SR(10편): 정확도는 혼재(재래식 인상이 전악·후방부 우위 다수)이나 chairside time·환자 편의는 측정된 모든 연구에서 IOS 우위; 시간 절감은 주로 후속 공정 생략분. 젊고 건강한 완전 치열 표본에 국한(QUADAS-2 환자선정 위험).
- 축1 확신도 보강: schlenz-2022·oguz-2026 = [확인](in-vitro, 오늘 세션에서 직접 읽음); ramos-morro-2026 정확도 결론 = [확인](SR 원문, 단 QUADAS-2 patient-selection risk 높음으로 일반화는 제한); 시간·편의 우위는 10편 중 2편 근거이므로 표본 크기 한계를 함께 표기.

## Clinical Quiz
<!-- quiz_spec -->

**Q1.** 전악 임플란트 지지 보철을 위한 최종 인상을 구강내스캐너(IOS)로 채득하려 합니다. 이 오버뷰의 결정 사다리에서 이 계획의 한계와 권장 대안은 무엇입니까? *(근거: 전악 IOS 오차 누적 + 무치악 적응증)*

> **모범답안**: **전악 임플란트 무치악 최종 인상에 IOS를 단독으로 쓰는 것은 권장하지 않는다.** 이 오버뷰에서 IOS의 임상 표준 적응증은 단관·소악궁(3–4 유닛)이다(trueness 50–100 µm). 전악 자연치는 기기 신중 선택(TRIOS 3·Primescan)이 필요하고, **무치악 전악은 기공실 스캐너 1차 또는 전통 인상이 권장된다** — IOS는 보조 역할. 근거: 전악 IOS는 후방 연장 시 오차 누적(trueness 50–200 µm)이 일관된 한계이며, 구치부 오차가 증가한다. 임플란트 보철에서 무치악 전악 IOS의 정확도는 자연치보다 더 복잡한 변수(임플란트 각도·scan body 간섭)가 추가된다. 권장: 전악 임플란트 최종 보철은 기공실 스캐너 + 전통 인상술을 우선하고, IOS는 진단·임시 보철 단계에서 활용한다.

**Q2.** 상악 전치부 즉시식립에서 가이드 수술(CAIS)을 쓸지 프리핸드(freehand)로 할지 결정해야 합니다. 이 오버뷰의 증거는 무엇을 지지합니까? *(근거: Schiavon 2025 NMA — 즉시식립·심미부)*

> **모범답안**: **즉시식립·심미부에는 full-static 또는 dynamic CAIS가 freehand보다 우월하다.** Schiavon 2025 NMA(7 RCT, 338 임플란트): 즉시식립·심미부·다중 임플란트 시나리오에서 full-static 또는 dynamic 가이드가 freehand 대비 각도·위치 편차를 유의하게 줄였다. 이 오버뷰에서 CAIS 결정 원칙: 단순 단일치 후방 식립은 freehand로 가능하지만, ① **즉시식립** ② **심미부(상악 전치)** ③ **다중 임플란트** 는 가이드 수술을 권장한다. 특히 상악 전치부 즉시식립은 협측 골벽·임플란트 위치·발출 축 정밀도가 장기 심미 결과를 결정하므로, 프리핸드의 인적 오차를 배제하는 가이드 수술의 이득이 명확하다.

**Q3.** AI가 방사선 사진에서 우식을 검출했다고 합니다. 이 결과를 환자에게 "AI가 우식이라고 확진했습니다"라고 전달해도 됩니까? *(근거: AI 진단 보조 단계 + 자율 치료 결정 부적합)*

> **모범답안**: **절대 안 된다 — AI는 진단 보조 도구이지 확진 도구가 아니다.** 이 오버뷰에서 AI 우식 검출 정확도는 약 95%이고 임플란트 종류 인식은 93.8–98%로 높지만, 이는 모두 **진단·교육 보조 단계이며 임상 검증이 부족**하다. 자율 치료 결정은 아직 AI가 담당할 수 없다. 환자에게 전달해야 할 올바른 표현: **"AI 보조 분석에서 우식 의심 소견이 있어 정밀 검사를 권고한다"** — 술자가 최종 진단 주체임을 명시해야 한다. 추가 제약: 환자 식별정보(이름·주민번호·연락처)를 AI 시스템에 입력하는 것은 개인정보보호법·HIPAA 위반이며, LLM이 생성한 환자용 설명 초안도 **술자 검토 없이 직접 환자에게 제공해서는 안 된다**(임상 수용도 약 70%이므로 나머지 30%는 오류 가능성이 있다).
