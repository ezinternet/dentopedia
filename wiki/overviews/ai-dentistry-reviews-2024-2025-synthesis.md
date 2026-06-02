---
title: "AI in Dentistry and Healthcare — 2024–2025 Review Cluster Synthesis"
authors: synthesis page (compiled by Claude from 9 wiki entries ingested 2026-05-21)
year: 2026
date: 2026-05-21
category: overviews
confidence: synthesis
source_collection: internal
tags: [overview, ai-dentistry, machine-learning, deep-learning, llm, chatgpt, multi-specialty, dental-education, restorative-ai, evidence-quality, claude-synthesis]
source: synthesis
---

## 한줄요약
2024–2025에 ingest한 인공지능 (Artificial Intelligence, AI) 리뷰 9편을 (1) 정량 근거, (2) 치과 다전공 매핑, (3) 분야 특화 합성, (4) 일반 의료 맥락 4개 클러스터로 묶고 — 임상 활용 가능 영역(영상 진단)·신중 활용(LLM 환자 응답)·미성숙(자율 시스템·통합 워크플로우)을 단계적으로 분리한 종합 페이지.

## Scope
이 종합 페이지는 2026-05-21에 `wiki/digital-workflow/` 아래로 ingest된 9편의 AI 관련 리뷰를 정리한다. 9편은 표면적으로 "AI in dentistry/healthcare"라는 동일 주제이지만, 근거 수준·범위·방법론이 크게 달라서 단일 결론으로 평균내면 정보 손실이 크다. 따라서 확신도와 범위로 stratify해서 본다.

| Stem | Type | Scope |
|---|---|---|
| zhang-2025-llm-patient-instructions-dentistry-sr-ma | sr+ma | 치과 LLM 환자 응답 |
| iqbal-2025-chatgpt-healthcare-umbrella-review | sr (umbrella) | ChatGPT 의료 전반 |
| najeeb-2025-ai-restorative-dentistry-review | sr | 수복치의학 AI |
| aminoshariae-2024-ai-endodontic-education-scoping | sr (scoping) | 근관치료 교육 AI |
| gao-2025-ai-dentistry-narrative-review | narrative | 치과 6대 전공 |
| lee-2025-ai-dentistry-emerging-applications-narrative | narrative | 치과(교육·진료·관리) |
| mallineni-2024-ai-dentistry-descriptive-review | narrative | 치과 전 분야(법의치과학 포함) |
| faiyazuddin-2025-ai-healthcare-comprehensive-review | narrative | 의료 전반 |
| mizna-2025-ai-healthcare-practice-review | narrative | 의료 전반(로봇·재활 포함) |

## Cluster 1 — Quantitative anchors (the load-bearing numbers)

이 클러스터에서 풀링 효과 추정치를 제시하는 논문은 **Zhang 2025만 하나**이다. 나머지는 정성 또는 단일 연구 인용. 따라서 정량적 결론을 인용할 때 무게중심은 Zhang에 둔다.

**Zhang 2025 (sr+ma, J Prosthodont 2025 Early View, 25편)** — 치과 환자 응답에서 대형 언어 모델 (Large Language Model, LLM)의 풀링 정확도 81.87% (95% 신뢰구간 (Confidence Interval, CI) 77.24–86.51%), 임상 수용 가능 응답 69.9% (95% CI 57.3–82.6%). ChatGPT-3.5는 Microsoft Bing보다 유의하게 높았고, GPT-4.0/Google Bard와는 차이 없음. [근거강함]

여기서 두 가지 신호가 임상적으로 중요하다.
- **정확도 vs 임상 수용 가능성의 12%p 갭** — 정답률이 높아도 임상 컨텍스트(언어 톤·완결성·안전 권고 누락)에서 실패하는 응답이 따로 존재한다. LLM 출력을 환자에게 그대로 전달하면 안 된다는 직접 근거.
- **GPT-3.5 ≈ GPT-4.0 무차이** — 직관과 어긋난다. 모델 능력보다 태스크 천장(saturation)이 빨리 도달했거나, 평가 루브릭이 거친 가능성. [claude해석]

**Najeeb 2025 (sr, PRISMA, 63편)** — 우식 검출 정확도 "up to 95%" 인용. 단 풀링 추정치가 아니라 최고 성능 단일 연구 인용이므로 정량 강도가 Zhang의 81.87% 풀링치보다 약하다. International Caries Detection and Assessment System (ICDAS) 기준 ground truth가 어디까지인지(D3+ 수준인지, 법랑질만인지) 명시 부족. [합의수준]

**Faiyazuddin 2025** — 의료 AI 출판물이 Web of Science에서 2014년 158편(3.54%) → 2024년 731편(16.33%)로 약 4.5배 증가. 채택률이 아니라 출판량 지표라는 한계. [근거강함 for the metric itself, claude해석 for impact]

## Cluster 2 — Cross-discipline AI mapping in dentistry

세 편(Gao 2025, Lee 2025, Mallineni 2024)이 동일한 cross-specialty AI overview 포지션을 차지한다. 결론은 수렴하지만 강조점이 다르다.

**공통 결론**
- AI 적용이 가장 성숙한 영역은 **방사선/광학 영상 기반 진단** — 우식 검출, 치근단 병소, 두부 계측, 임플란트 종류 식별 등 영상 라벨링 가능한 작업.
- 비-영상 워크플로우 AI는 데이터 가용성·균일성·연산력에 의해 병목된다.
- 데이터 프라이버시·알고리즘 편향·법적 책임이 공통 장벽으로 거론된다.

**차별점**
- **Lee 2025의 3-pillar 프레임워크** — 교육 / 환자 진료 / 진료실 관리. 진료실 관리 측면(보험 청구, 스케줄링, 환자 커뮤니케이션 자동화)을 명시한 유일한 리뷰. 한국 개원가에서 가장 즉시 적용 가능한 측면이지만 다른 리뷰는 거의 다루지 않는다.
- **Gao 2025의 6대 전공 체인** — 근관·치주·임플란트·교정·보철·구강악안면외과 (Oral and Maxillofacial Surgery, OMFS). 의료 과실·개인정보 법적 위험을 명시적으로 다룬 점이 차별적.
- **Mallineni 2024의 최광역 커버리지** — 위 6대 + 소아치과·법의치과학까지 포함. 다만 narrative descriptive로 깊이는 얕다.

**Synthesis [claude해석]** — 세 편 모두 정확한 단일 진단·결정 지원 사례는 풍부하나 워크플로우 통합 수준의 임상 결과를 제시하지 못한다. 즉 "AI가 무엇을 할 수 있는가"는 잘 정리되어 있지만 "AI를 도입했을 때 임상 결과·환자 안전·진료 효율이 통계적으로 개선되는가"는 아직 답하지 못한다.

**영상 기반 성숙 영역의 구체 근거 (본 wiki 보유 implant-AI 논문)** — "영상 라벨링 작업이 가장 성숙"이라는 공통 결론은 우리가 따로 보유한 임플란트 영역 deep-learning 논문들에서 그대로 확인된다: Park 2023은 파노라마에서 임플란트 종류 분류 deep learning을, Oh 2023은 방사선 기반 골유착 예측 DL을, Chi 2026은 치근단 방사선 촬영 품질 자동 평가를 보고한다. 술식 측면에서는 Sakai 2023이 CBCT 기반 드릴링 프로토콜 AI를 다룬다. 이들은 모두 "영상 입력 → 라벨/수치 출력"으로 cluster 2의 성숙 영역 정의에 정확히 들어맞으며, 반대로 워크플로우 통합·임상 결과 RCT는 여전히 비어 있다.

## Cluster 3 — Domain-specific syntheses

**Aminoshariae 2024 (scoping, J Endod 50(5):562, 251→35편)** — 근관치료 교육에서 AI 활용 10영역 매핑: (1) 방사선 해석, (2) 감별진단, (3) 치료계획·의사결정, (4) 사례 난이도 평가, (5) 술기 전 실습, (6) 시뮬레이션·사례 기반 훈련, (7) 실시간 임상 가이드, (8) 자율 시스템·로봇, (9) 진도 평가·개인화 교육, (10) 캘리브레이션·표준화.

교육 영역에서는 한국 치과의사 양성 현장에서 (4) 사례 난이도 평가와 (10) 캘리브레이션이 가장 즉시 가치가 있다 — 인스트럭터 간 변동성을 줄일 수 있다. (7) 실시간 임상 가이드는 학생-AI-감독자 책임 분담 문제로 한국 의료법상 미정리 영역. [claude해석]

**Najeeb 2025 (sr, BMC Oral Health 25:592, 63편, 2020–2025.1)** — 수복치의학 도메인 한정. 우식 검출, 근관, 수복, 치아 표면 손실, 색조 측정, 재생 치의학. 3D 프린팅과 AI 통합을 향후 핵심 방향으로 지목.

**Synthesis [claude해석]** — 두 편은 교육과 임상 실무의 양극단을 각각 다루며, AI 도입 전략을 "교육 → 술식 보조 → 임상 결정 지원" 순서로 단계화하면 자연스럽다.

## Cluster 4 — General healthcare AI context

치과 특화가 아닌 의료 AI 리뷰 3편(Faiyazuddin 2025, Iqbal 2025, Mizna 2025)은 치과 임상에 직접 적용은 어렵지만 두 가지 기능이 있다.

**기능 1 — 메타-증거 품질 audit (Iqbal 2025).** ChatGPT 의료 활용 umbrella review (17편, SR 15 + MA 2). AMSTAR-2 평가 결과 중간 5편 / 낮음 12편. 즉 현재 출간된 ChatGPT-in-healthcare SR 대다수의 방법론적 품질이 낮다. 결함은 연구 설계 정당화·연구비 출처 보고. [근거강함 for AMSTAR-2 results]

**임상 함의** — ChatGPT/LLM 관련 단일 SR을 인용할 때 방법론 검증 없이 무비판적으로 옮기면 안 된다. Zhang 2025처럼 PRISMA + QUADAS-2를 명시한 sr+ma가 현재 가장 신뢰할 만한 정량 근거.

**기능 2 — 인접 통합 기술 매핑 (Mizna 2025, Faiyazuddin 2025).** 로봇 보조 수술·재활·증강현실 (Augmented Reality, AR)·가상현실 (Virtual Reality, VR)·사물인터넷 (Internet of Things, IoT)·웨어러블 분석. 치과 직접 적용은 제한적이나, 만성질환 환자(당뇨·심혈관)의 웨어러블 데이터가 치과 사전 처치 위험도 평가로 흘러오는 시나리오는 5–10년 시야에서 현실적. [추정]

## Evidence quality audit (cluster-wide)

| 차원 | 분포 |
|---|---|
| sr+ma | 1 (Zhang 2025) |
| sr (scoping/umbrella/PRISMA) | 3 (Aminoshariae, Najeeb, Iqbal) |
| narrative | 5 (Gao, Lee, Mallineni, Faiyazuddin, Mizna) |
| 치과 특화 | 6 |
| 의료 전반 | 3 |
| PRISMA 명시 | 3 |
| 정량 효과 추정치 제공 | 1 (Zhang의 풀링 정확도/수용성) |

**문제점** — narrative review 비중이 9편 중 5편으로 높다. AI 분야 특성상 빠른 출판 압력 때문이라 짐작되지만, 임상 적용 결정에 narrative review를 단독 인용하는 것은 위험. **Zhang 2025와 Iqbal 2025를 정량/메타-품질 anchor**로 두고, 나머지는 컨텍스트로 활용하는 것이 안전.

## Decision threads for our clinic [claude해석]

작업 가설이며 프로토콜이 아님.

1. **즉시 도입 검토 가능** — 영상 기반 보조 진단(파노라마·치근단·CBCT 자동 라벨링). Gao/Lee/Mallineni 합의가 가장 강한 영역. 단, 한국 식품의약품안전처 (Ministry of Food and Drug Safety, MFDS) 인허가 등급(소프트웨어 의료기기 (Software as a Medical Device, SaMD))과 보험 청구 가능성을 별도 확인. [미검증 for current MFDS lineup]

2. **신중 활용** — LLM 환자 응답. Zhang 2025의 풀링 정확도 81.87%·임상 수용 69.9%는 chairside 직접 출력이 아닌 **front-desk staff 1차 초안 + 임상의 검수**의 워크플로우를 시사. 한국어 LLM 성능은 본 sr+ma에서 직접 측정되지 않았으므로 추가 자체 검증 필요. [근거강함 for the English numbers, 추정 for Korean]

3. **위생사 교육 보조** — Aminoshariae 2024의 (5) 술기 전 실습, (9) 진도 평가에서 AI 보조 가능. 위생사 캘리브레이션(스케일링 평가, 방사선 촬영 품질 평가)에서 inter-rater variability를 줄이는 도구로 검토 가치. [claude해석]

4. **개인정보·법적 책임** — 한국 개인정보보호법 (Personal Information Protection Act, PIPA) 추론 정보 처리 조항이 AI 진단 결과를 진료기록부에 포함할 의무·삭제 요청 처리 절차에 적용. 의료법상 진단·치료 책임이 의사에게 귀속되는 원칙은 AI가 보조해도 변하지 않음. AI 출력을 임상 결정의 1차 근거로 인용하지 말 것(=확진 도구가 아니라 screening 도구로 자리매김). [합의수준]

5. **미성숙 영역 회피** — 자율 술식 시스템(robotics for direct dental procedures), end-to-end 워크플로우 자동화. Mallineni 2024·Gao 2025 모두 "연구 단계"로 명시. 도입 ROI 부정적. [합의수준]

## Cluster-wide gaps

- **임상 결과 RCT 부재** — 9편 어디에도 AI 도입 vs 미도입을 비교한 환자-결과 RCT가 등장하지 않는다. 지금까지의 evidence는 "AI 단독 정확도" 또는 "AI 보조 진단 정확도"에 머문다. 임플란트 영역 리뷰 계보(Revilla-Leon 2021 sr, Altalhi 2023·Srinivasan 2025·Saeed 2023 narrative)도 같은 한계를 공유한다 — 진단·식별 정확도는 축적됐으나 도입 후 임플란트 생존·합병증을 비교한 전향 비교연구는 부재.
- **한국어/한국 인구 검증 부재** — Zhang sr+ma 25편 중 한국어 LLM 평가는 명시되지 않음. 한국 우식 검출 AI(예: PointCare, VisualDX 류) 성능 직접 비교 데이터 별도 검색 필요.
- **장기 추적 데이터 부재** — 영상 진단 AI를 적용한 환자군의 5년 이상 임상 결과 데이터는 본 9편에 없음.
- **윤리·법적 운영 가이드 부재** — Iqbal 2025가 17편 ChatGPT SR 중 윤리·법적 우려를 다룬 비중을 명시하지만 *어떻게 운영할지*에 대한 구체적 가이드는 거의 없음.

## Related Papers
- [[digital-workflow/zhang-2025-llm-patient-instructions-dentistry-sr-ma]] — 클러스터 1 정량 anchor
- [[digital-workflow/iqbal-2025-chatgpt-healthcare-umbrella-review]] — 메타-증거 품질 anchor
- [[digital-workflow/najeeb-2025-ai-restorative-dentistry-review]] — 수복 도메인 합성
- [[digital-workflow/aminoshariae-2024-ai-endodontic-education-scoping]] — 교육 영역 10-domain 프레임
- [[digital-workflow/gao-2025-ai-dentistry-narrative-review]] — 치과 6대 전공 + 법적 위험 명시
- [[digital-workflow/lee-2025-ai-dentistry-emerging-applications-narrative]] — 3-pillar(교육·진료·관리)
- [[digital-workflow/mallineni-2024-ai-dentistry-descriptive-review]] — 최광역 커버리지
- [[digital-workflow/faiyazuddin-2025-ai-healthcare-comprehensive-review]] — 의료 일반 AI 성장 트렌드
- [[digital-workflow/mizna-2025-ai-healthcare-practice-review]] — 인접 통합 기술(AR/VR/IoT)
- [[digital-workflow/revilla-leon-2021-artificial-intelligence-implant-dentistry-sr]] — 기존 임플란트 AI sr
- [[digital-workflow/sakai-2023-ai-drilling-protocol-cbct-implants]] — CBCT 드릴링 프로토콜 AI
- [[digital-workflow/oh-2023-deep-learning-osseointegration-prediction-radiographs]] — 골유착 예측 DL
- [[digital-workflow/park-2023-deep-learning-implant-size-classification]] — 임플란트 식별 DL
- [[digital-workflow/chi-2026-deep-learning-periapical-radiograph-quality]] — 치근단 품질 평가 DL
- [[digital-workflow/srinivasan-2025-artificial-intelligence-dental-implants-review]] — 임플란트 AI 2025 narrative
- [[digital-workflow/altalhi-2023-artificial-intelligence-impact-dental-implantology]] — 임플란트 AI 2023 narrative
- [[digital-workflow/saeed-2023-robotic-artificial-intelligence-implant-dentistry]] — 임플란트 로보틱스·AI
