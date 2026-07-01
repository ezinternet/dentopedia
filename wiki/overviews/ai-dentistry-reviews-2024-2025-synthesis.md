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

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 핵심 명제: 2024–2025 인공지능(Artificial Intelligence, AI) 리뷰 9편은 근거 수준이 제각각이라 단일 결론으로 평균내면 안 되고, 확신도·범위로 4개 클러스터(정량 근거·다전공 매핑·분야특화·일반의료)로 stratify해야 한다.
> - 정량 anchor는 사실상 Zhang 2025 한 편 — 치과 대형언어모델(Large Language Model, LLM) 환자 응답 풀링 정확도 81.87%(95% CI 77.24–86.51), 임상 수용 가능 응답 69.9%(95% CI 57.3–82.6).
> - 정확도와 임상 수용성 사이 약 12%p 갭 — 정답률이 높아도 톤·완결성·안전권고 누락으로 실패하는 응답이 따로 존재 → LLM 출력을 환자에게 그대로 전달 금지.
> - GPT-3.5 ≈ GPT-4.0 무차이(직관과 어긋남), GPT-3.5는 Bing보다 유의 우위 — 모델 능력보다 태스크 천장 도달 가능성.
> - 가장 성숙한 AI 영역은 방사선·광학 영상 기반 진단(우식 검출, 치근단 병소, 두부계측, 임플란트 식별) — 영상 라벨링 가능 작업. 비-영상 워크플로우는 데이터·연산 병목.
> - 9편 중 narrative review가 5편으로 과다 → 임상 결정에 narrative 단독 인용은 위험. Zhang 2025(정량)와 Iqbal 2025(메타품질)를 anchor로.
> - Iqbal 2025 umbrella review(17편): ChatGPT-in-healthcare SR 대다수가 AMSTAR-2 중간 5편·낮음 12편 — 방법론 품질 낮음, 무비판 인용 금지.
> - 임상 적용 단계: 즉시 도입 검토(영상 보조 진단, MFDS 인허가·보험 별도 확인) → 신중 활용(LLM 환자 응답은 front-desk 초안+임상의 검수, 한국어 성능 미검증) → 미성숙 회피(자율 술식 로봇·end-to-end 자동화).
> - 법적 원칙: AI가 보조해도 진단·치료 책임은 의사 귀속, AI 출력은 확진이 아닌 screening 도구로만, 개인정보보호법(PIPA) 적용.
> - 소아치과 AI 확장(2026, `artificial-intelligence/` 신설): 엄브렐러 리뷰(Garg 2026)에서 영상용 합성곱 신경망(Convolutional Neural Network, CNN) 민감도/특이도 80–83%·곡선하면적(AUC) 0.87–0.91이나 포함 SR 대부분 AMSTAR-2 낮음/매우 낮음 — 성인 cluster와 동일하게 "영상 진단 우위 + 근거 품질 경고" 패턴 재확인(Gómez-Ríos 2025 머신러닝 SR은 우식 예측 14/20편 집중).
> - 과제별 영상진단 정량 anchor 확보(2026-06-22, cluster 6): 우식 검출 민감도 76%·특이도 91%·AUC 92%(Abbott 2024), 치근단 병소 민감도 0.925·dOR 71.7로 **유일 GRADE high**(Sadr 2023), 치주골소실 민감도 87%(Khubrani 2025), 두부계측 2D 오차 1.39 mm(Hendrickx 2024), OMFS ChatGPT GPT-4 MCQ 76.8%(de Menezes Torres 2025) — "영상 진단 우위"가 정성 주장에서 과제별 풀링 수치로 격상, 단 풀링비율 낮고 RoB·이질성 높아 근거 품질 경고는 유지.
> - 영상진단 SR·1차연구 추가(2026-07-01, cluster 7): 방사선 우식검출 SR은 민감도 0.44–0.86·특이도 0.85–0.98·곡선하면적(Area Under the Curve, AUC) 0.84–0.98로 합성곱 신경망(Convolutional Neural Network, CNN)이 약 70% 차지하나 데이터셋이 작고 이질적이라 메타분석 불가(Albano 2024); 병소검출 지도형 SR은 5개 병소·3개 영상양식·14개 아키텍처(U-Net 최다 27.6%)를 정리하되 한 모델이 치근단 병변 49%를 놓친 사례를 경고(Demir 2024).
> - 파노라마 우식 다단계 검출 1차연구(Pornprasertsuk 2025): 당일 바이트윙을 gold standard로 삼아 파노라마에서 법랑질/상아질/치수 단계별 분할, 구치부 F1 0.85·정확도 0.93·재현율 0.96(가중 κ 0.907–0.981)이나 위양성(519)이 위음성(67)보다 많아 단독 진단이 아닌 결정보조로 자리매김.
> - 파노라마 AI 상위(umbrella) 리뷰(Turosz 2023, 12편 SR·ROBIS): 과제별 정확도 우식 91.5%·골다공증 89.29%·상악동염 87.5%·치주골소실 93.09%·치아식별 93.67%, 치근단 병소 민감도 99.95%·특이도 92%이나 원천 연구가 적고 이질적이며 AI SR은 빨리 노후화 → 신중 해석. 성인 영상진단 cluster의 "영상 우위 + 근거 품질 경고" 패턴 재확인.
> - 공통 공백: AI 도입 vs 미도입을 비교한 환자-결과 RCT 부재, 한국어·한국 인구 검증 부재, 5년 이상 장기 추적 데이터 부재.

## One-line Summary

Synthesis/overview stratifying 9 AI-in-dentistry/healthcare review papers (ingested 2024–2025) into 4 clusters — quantitative anchors, cross-discipline dental AI mapping, domain-specific syntheses, and general-healthcare AI context — because their evidence levels differ too widely to average into a single conclusion; the load-bearing quantitative anchor is essentially Zhang 2025 (dental LLM pooled answer accuracy 81.87% [95% CI 77.24–86.51], clinically acceptable responses 69.9% [95% CI 57.3–82.6]), the most mature AI domain is image-based diagnosis (caries detection, periapical lesions, cephalometrics, implant identification), and 5 of 9 reviews are narrative — so the clinical takeaway is staged adoption (image-assisted diagnosis now with regulatory checks; LLM patient responses only as clinician-reviewed front-desk drafts; autonomous/end-to-end systems avoided), with AI kept as a screening tool while diagnostic/treatment liability stays with the clinician.

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

이 클러스터에서 (LLM 도메인의) 풀링 효과 추정치를 제시하는 논문은 **Zhang 2025만 하나**였다. 나머지는 정성 또는 단일 연구 인용. **단 2026-06-22 surveillance 추가로 영상 진단 과제별 풀링 정확도(우식·치근단·치주·두부계측)가 cluster 6에 확보되어, 이제 정량 anchor는 LLM(Zhang)뿐 아니라 영상 진단 4과제로 확장되었다** — 아래 cluster 6 참조.

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

## Cluster 5 — Pediatric-dentistry AI (2026 extension)

본 종합은 2026-05-21 9편으로 시작했으나, 2026년에 신설된 `artificial-intelligence/` 카테고리의 소아치과 AI 2편이 cluster 1(정량 anchor)·cluster 4(메타-품질 audit)의 핵심 명제를 **독립적으로 재확인**한다.

**Garg 2026 (umbrella review, 7 SR / 1차 109편)** — 소아치과 인공지능 (Artificial Intelligence, AI), 특히 영상용 합성곱 신경망 (Convolutional Neural Network, CNN)이 통합 민감도/특이도 80–83%·곡선하면적 (Area Under the Curve, AUC) 0.87–0.91을 달성. 그러나 포함 SR 대부분이 A MeaSurement Tool to Assess systematic Reviews v2 (AMSTAR-2) 기준 낮음/매우 낮음 질, 중복은 보정중복면적 (Corrected Covered Area, CCA) 8.27%로 중등도. **Iqbal 2025와 동일한 메타-품질 경고 — 강한 영상 진단 metric이 약한 1차 근거 위에 서 있다.** [근거강함 for the metric, 근거약함 for underlying SR quality]

**Gómez-Ríos 2025 (sr, PRISMA·QUADAS-2; 1945→20편)** — 소아치과 머신러닝 (Machine Learning, ML)은 우식 예측(20편 중 14편, 사회인구·행동·생물학적 예측인자)에 집중; ML 비용분석은 실란트+불소가 비용 절감에 유리. ML 전용 보고지침·질 평가 척도 부재를 명시. [합의수준]

**Synthesis [claude해석]** — 두 편은 cluster 2의 "영상 라벨링 작업이 가장 성숙"이라는 공통 결론을 소아 인구에서 재현하면서(영상 CNN > 비영상 ML), 동시에 cluster 4의 "방법론 품질이 낮아 무비판 인용 금지"를 강화한다. 즉 AI 성숙도 지형(영상 진단 우위)과 근거 품질 경고(낮은 SR 질)는 성인·소아를 가로질러 일관된다.

## Cluster 6 — Per-task image-diagnosis accuracy anchors (2026-06-22 surveillance addition)

이전까지 본 종합의 정량 무게중심은 Zhang 2025(LLM)뿐이었다. 2026-06-22 surveillance 인제스트로 **영상 진단 4대 과제별 풀링 진단정확도 SR+MA**가 확보되어, cluster 2가 정성적으로 주장한 "영상 라벨링 = 가장 성숙"이 이제 **과제별 풀링 수치로 뒷받침**된다.

- **Abbott 2024 (sr+ma)** — 우식 검출 AI 21개 플랫폼: 통합 민감도 76%·특이도 91%·곡선하면적 (Area Under the Curve, AUC) 92%(45편 중 7편만 풀링, 이질성 높음); 임상사진 입력이 교익(bitewing)보다 우수. [근거강함 for the pooled metric, 합의수준 for heterogeneity]
- **Sadr 2023 (sr+ma)** — 치근단(periapical) 방사선투과병소 deep learning: 민감도 0.925·특이도 0.852·진단오즈비 (diagnostic Odds Ratio, dOR) 71.7, **클러스터 전체에서 유일한 GRADE high**. 영상 진단 과제 중 근거 강도가 가장 단단한 사례. [근거강함]
- **Khubrani 2025 (sr+ma)** — 2D 방사선 치주골소실/치주염 ML·DL(APPRAISE-AI 적용): 민감도 87%·특이도 76%·정확도 84%; 30편 중 "매우우수" 0편. 성능은 임상 유용하나 방법론 품질은 여전히 낮음. [근거강함 for metric, 근거약함 for study quality]
- **Hendrickx 2024 (sr+ma)** — AI 측모두부계측(cephalometric) 자동화: 2D 평균방사오차 1.39 mm(<2 mm 임상허용 기준)·1분 미만, 3D는 1.0–5.8 mm로 편차 큼; 비뚤림위험(Risk of Bias, RoB) 높음. 2D는 임상 사용 가능 수준에 도달. [근거강함 for 2D]
- **de Menezes Torres 2025 (sr)** — LLM 도메인 확장: 구강악안면외과 (Oral and Maxillofacial Surgery, OMFS)에서 ChatGPT(10편) — GPT-4 객관식 (Multiple-Choice Question, MCQ) 76.8%, 동의서 작성·환자 소통은 강점이나 복잡한 임상 의사결정은 취약. Zhang 2025의 LLM anchor를 OMFS 맥락으로 보강. [합의수준]

**Synthesis [claude해석]** — 네 영상 과제(우식·치근단·치주·두부계측)의 풀링 수치가 모두 임상 유용 범위(민감도 76–93%·특이도 76–91%, 2D 계측오차 <2 mm)에 들어오면서, "영상 진단 우위"는 더 이상 정성 주장이 아니라 **수치로 확인된 성숙 영역**이다. 그러나 (1) 풀링 비율이 낮고 이질성·RoB가 높으며(Abbott 7/45편, Khubrani "매우우수" 0편), (2) GRADE high는 Sadr 치근단 1과제에 불과하고, (3) 여전히 임상 결과(환자-아웃컴) RCT는 전무하다. 즉 **진단 metric은 성숙·근거 품질은 미성숙**이라는 본 종합의 핵심 이중 명제가 과제별 데이터로 재확인된다. 정량 인용 시 무게중심은 Sadr 2023(GRADE high)과 Zhang 2025(LLM 풀링)에 둔다.

## Cluster 7 — Image-diagnosis SRs & primary studies (2026-07-01 ingest)

2026-07-01 surveillance 인제스트로 영상 진단 SR·overview 3편과 파노라마 우식 1차연구 1편이 추가되어, cluster 2의 "영상 라벨링 = 가장 성숙"과 cluster 6의 "진단 metric 성숙·근거 품질 미성숙" 이중 명제를 **독립 재확인**한다. 세 편 모두 정성 주장을 과제별·아키텍처별 수치로 뒷받침하되 데이터·일반화 병목을 명시한다.

- **Albano 2024 (sr, PRISMA/QUADAS-2, 20편·영상 6346장)** — 방사선 우식 검출 AI: 민감도 0.44–0.86·특이도 0.85–0.98·정확도 0.73–0.98·곡선하면적 (Area Under the Curve, AUC) 0.84–0.98·F1 0.64–0.92, 합성곱 신경망 (Convolutional Neural Network, CNN)이 약 70%. 대부분 낮은 비뚤림 위험(QUADAS-2)이었으나 데이터셋이 작고(최소 15장) 이질적이라 **메타분석 불가**. bitewing이 인접면 우식에 최적 modality, AI는 저경력 검사자에게 특히 유용. cluster 6 Abbott 2024(풀링 SR+MA)의 저변 데이터를 modality·아키텍처로 분해(refines). [근거강함 for per-metric ranges, 합의수준 for no-pooling]
- **Demir 2024 (sr, PRISMA/Kitchenham, 29편, 2019–2024)** — 딥러닝 병소검출 지도형 리뷰: 5개 병소유형(치근단 62%·apical 34%·낭종·우식·악골)×3개 영상양식(파노라마·치근단·CBCT)×14개 아키텍처(U-Net 최다 27.6%). 정확도 pooling 없음. **경고 신호**: 한 U-Net 모델(2902 파노라마)이 sens 92%·spec 84%에도 치근단 방사선투과 병소의 **49%를 놓침** — headline accuracy 과독 위험. Sadr 2022(치근단 풀링 SR+MA)를 5병소·3양식으로 확장(extends). [근거강함 for the field map, 근거약함 for generalizability]
- **Pornprasertsuk 2025 (retrospective, 파노라마 500장·치아 14,997개·우식 1,792개)** — 당일 bitewing을 gold standard로 삼아 파노라마에서 우식을 법랑질/상아질/치수 단계별 분할하는 2단계 파이프라인(YOLOv5s 치아검출 + Attention U-Net 우식분할): 구치부 F1 0.85·정확도 0.93·재현율 0.96, 방사선과 전문의와 가중 κ 0.907–0.981(거의 완벽). 단 위양성 519 > 위음성 67로 healthy tooth 과예측 → 단독 진단 아닌 결정보조. Albano 2024 SR이 집계하는 우식 AI trend의 구체 1차연구 인스턴스(applies-to). [retrospective, single-center, 외부검증 필요]
- **Turosz 2023 (sr, umbrella/overview of SRs, 12편 SR·ROBIS)** — 파노라마 AI 상위 리뷰: 과제별 최신 정확도 우식 91.5%·골다공증 89.29%·상악동염 87.5%·치주골소실 93.09%·치아식별·번호매김 93.67%, 치근단 병소 민감도 99.95%·특이도 92%. 단 원천 연구가 적고 이질적이며 AI SR은 빨리 노후화 → 신중 해석. cluster 6 과제별 anchor(치주 Khubrani, 우식 Abbott)와 수렴하는 cross-task 정확도 landscape. **abstract-only(전문 미확보)이라 per-review ROBIS·과제별 review 수는 미포착.** [합의수준]

**Synthesis [claude해석]** — 네 편은 cluster 2·6의 이중 명제를 다시 확증한다: (1) 영상 진단 metric은 과제·아키텍처를 가로질러 임상 유용 범위(파노라마 우식 91.5%, 치근단 sens 99.95%, F1 0.85)에 반복 도달하고, (2) 그러나 데이터셋이 작고 이질적이라 메타분석이 반복적으로 좌절되며(Albano 풀링 불가), 한 모델이 병변 49%를 놓치고(Demir), 위양성이 위음성을 초과하며(Pornprasertsuk), umbrella 수준에서도 원천 SR이 적고 빨리 노후화된다(Turosz). 즉 **"진단 정확도는 성숙, 근거 품질·일반화는 미성숙"**이 SR·overview·1차연구 세 층위 모두에서 일관된다. 임상 인용 시 정량 무게중심은 여전히 Sadr 2023(GRADE high)과 Zhang 2025(LLM)에 두고, 본 4편은 영상 진단 성숙도 지형의 폭·깊이를 채운다.

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
- [[artificial-intelligence/garg-2026-artificial-intelligence-pediatric-dentistry-umbrella-review]] — 소아치과 AI 엄브렐러 리뷰 (CNN 영상 80–83%/AUC 0.87–0.91, SR 질 낮음); cluster 1·4 재확인 (sr, 2026)
- [[artificial-intelligence/gomez-rios-2025-machine-learning-data-analysis-pediatric-dentistry-sr]] — 소아치과 ML SR (우식 예측 14/20편); 영상 우위·근거 품질 경고 reinforce (sr, 2025)
- [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]] — cluster 6 우식 검출 풀링 anchor (민감도 76%/특이도 91%/AUC 92%) (sr+ma, 2024)
- [[artificial-intelligence/sadr-2022-deep-learning-periapical-radiolucent-lesions]] — cluster 6 치근단 병소, 유일 GRADE high (sens 0.925) (sr+ma, 2023)
- [[artificial-intelligence/khubrani-2025-periodontal-bone-loss-periodontitis-detection]] — cluster 6 치주골소실 (APPRAISE-AI, sens 87%) (sr+ma, 2025)
- [[artificial-intelligence/hendrickx-2024-ai-cephalometric-analysis-manual-tracing]] — cluster 6 두부계측 자동화 (2D 오차 1.39 mm) (sr+ma, 2024)
- [[artificial-intelligence/de-menezes-torres-2025-chatgpt-oral-maxillofacial-surgery]] — cluster 6 LLM 확장 (OMFS ChatGPT, GPT-4 76.8%) (sr, 2025)

### 신규 ingest cluster — AI 영상진단 (caries/lesion detection, panoramic) (2026-07-01)
- [[artificial-intelligence/albano-2024-artificial-intelligence-radiographic-caries-detection]] — cluster 7 방사선 우식검출 SR (PRISMA/QUADAS-2, 20편; sens 0.44–0.86·spec 0.85–0.98·AUC 0.84–0.98·CNN ~70%; 데이터 이질성으로 메타분석 불가) (sr, 2024)
- [[artificial-intelligence/demir-2024-artificial-intelligence-dental-lesion-detection]] — cluster 7 병소검출 지도형 SR (29편; 5병소·3양식·14아키텍처, U-Net 27.6%; 한 모델 치근단 병변 49% 놓침 경고) (sr, 2024)
- [[artificial-intelligence/pornprasertsuk-2025-deep-learning-multistage-caries-panoramic]] — cluster 7 파노라마 다단계 우식 1차연구 (YOLOv5+Attention U-Net; 구치부 F1 0.85·acc 0.93·recall 0.96·κ 0.907–0.981; FP>FN → 결정보조) (retrospective, 2025)
- [[artificial-intelligence/turosz-2023-artificial-intelligence-panoramic-radiographs-overview]] — cluster 7 파노라마 AI umbrella (12편 SR·ROBIS; 우식 91.5%·치주 93.09%·치아식별 93.67%·치근단 sens 99.95%; abstract-only, AI SR 빠른 노후화 경고) (sr, 2023)
