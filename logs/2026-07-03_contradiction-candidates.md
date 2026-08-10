# 논쟁 레이더 백필 후보 — 2026-07-03

명시적 충돌 표현이 있으나 `relations: contradicts/refines` 엣지가 없는 후보. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**

**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. 아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), (2) **양쪽 페이지의 `## 한줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. 충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. (reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것.)

- Tier 1 (대상 지목됨, actionable): **82**
- Tier 2 (대상 불명/soft, review): **281**

## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)

### behavioral-dentistry/dental-anxiety

- `alhomoud-2023-behavior-anxiety-levels-pediatric-patient`  —[대비되는 · 대비]→  **`jkda-2021-60-1-003`**
  - **근거 문장**: dental-anxiety 하위 카테고리의 실측 데이터 축. [[wiki/behavioral-dentistry/dental-anxiety/jkda-2021-60-1-003]](성인 phobia)와 대비되는 소아 데이터 — Frankl·Venham·categorical scale로 150명 측정. 연령·성별 효과를 정량화해 [[wiki/behavioral-dentistry/dental-anxiety/pediatric-2026-dental-anxiety-contemporary-assessment-management]](소아 불안 관리 review)의 primary 근거로 연결.
  - ▸ 출발(`alhomoud-2023-behavior-anxiety-levels-pediatric-patient`) 한줄: 소아 단면연구(2–14세 150명; Frankl·Venham·categorical) — 성별 차이 없음, 연령군 차이 유의(11–14세: 울음 p=.034·협조 p=.002·불안감 p=.003). 소아는 내원 시 불안 고조.
  - ▸ 대상(`jkda-2021-60-1-003`) 한줄: Review (연세대 통합치의학 정지은, JKDA 2022): dental phobia 환자의 외래 의사소통·sedation·전신마취 결정 framework. 단계별 접근·시술 후 예방 교육 강조.

- `alhomoud-2023-behavior-anxiety-levels-pediatric-patient`  —[대비되는 · 대비]→  **`pediatric-2026-dental-anxiety-contemporary-assessment-management`**
  - **근거 문장**: dental-anxiety 하위 카테고리의 실측 데이터 축. [[wiki/behavioral-dentistry/dental-anxiety/jkda-2021-60-1-003]](성인 phobia)와 대비되는 소아 데이터 — Frankl·Venham·categorical scale로 150명 측정. 연령·성별 효과를 정량화해 [[wiki/behavioral-dentistry/dental-anxiety/pediatric-2026-dental-anxiety-contemporary-assessment-management]](소아 불안 관리 review)의 primary 근거로 연결.
  - ▸ 출발(`alhomoud-2023-behavior-anxiety-levels-pediatric-patient`) 한줄: 소아 단면연구(2–14세 150명; Frankl·Venham·categorical) — 성별 차이 없음, 연령군 차이 유의(11–14세: 울음 p=.034·협조 p=.002·불안감 p=.003). 소아는 내원 시 불안 고조.
  - ▸ 대상(`pediatric-2026-dental-anxiety-contemporary-assessment-management`) 한줄: 소아 치과불안 narrative review — 검증 평가도구는 연령·인지·맥락 따라 선택. 비약물 관리(tell-show-do, modeling, 보호자 안내, 시청각·VR distraction) 일관 효과. 구조화 평가 + 다중모드 전략이 협조도·효율 향상.


### bone-regeneration

- `khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma`  —[overturn · 결론 뒤집음]→  **`simion-1992-jawbone-enlargement-split-crest-gtr`**
  - **근거 문장**: This SR+MA directly informs the staging decision behind [[wiki/bone-regeneration/enislidis-2006-staged-ridge-splitting-implant-mandible]] (a two-stage staged ridge-split technique): the pooled comparative analysis finds the **one-stage** ridge split superior to the two-stage approach (SMD favouring one-stage ~0.89). It refines — but does not overturn — the enislidis staged-technique anchor, and co
  - ▸ 출발(`khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma`) 한줄: PRISMA 체계적 문헌고찰+메타분석(정성 11편, 메타분석 3편, 전부 중-고 비뚤림위험): 1단계 치조제 분할술(one-stage ridge split)이 2단계보다 우수(통합 SMD ~0.89, one-stage 유리). 단, 이질성 불량·깔때기 비대칭(출판편향 가능성)으로 근거 강도는 제한적.
  - ▸ 대상(`simion-1992-jawbone-enlargement-split-crest-gtr`) 한줄: split-crest 고전 증례군(n=5): 치조제를 길이방향으로 분할해 녹색골절을 유발하고 끌로 피질판을 벌린 뒤 즉시 임플란트 식립·e-PTFE 막(GTR) 적용 → 폭 1–4 mm 증가(상악에서 더 큼), 조직학적으로 분할면 사이 골재생 확인.

- `vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`  —[overturn · 결론 뒤집음]→  **`simion-1992-jawbone-enlargement-split-crest-gtr`**
  - **근거 문장**: This is the key HEAD-TO-HEAD synthesis for choosing a horizontal ridge augmentation modality for the narrow ridge — GBR vs ridge-split (RS) vs osseodensification (OD) ridge expansion — ranking them by mean horizontal bone gain in one meta-analysis. It directly ties together the wiki's previously separate technique pages: the ridge-split case literature ([[wiki/bone-regeneration/simion-1992-jawbone
  - ▸ 출발(`vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`) 한줄: 수평 치조제 증대 3종을 직접 비교한 SR+MA(18편, 메타분석 17편, 환자 336명/임플란트 665개): 평균 수평 골증대량은 **가이드골재생(GBR) 4.04 mm > 치조제분할(RS) 3.66 mm > 골밀도화 치조제확장(OD) 2.15 mm** (P=0.002). 임플란트 생존율은 세 방법 모두 ~99%로 차이 없음. OD는 가장 넓은 치조제(4.37 mm)에, RS는 가장 좁은 치조제(3.43 mm)에 적용됨.
  - ▸ 대상(`simion-1992-jawbone-enlargement-split-crest-gtr`) 한줄: split-crest 고전 증례군(n=5): 치조제를 길이방향으로 분할해 녹색골절을 유발하고 끌로 피질판을 벌린 뒤 즉시 임플란트 식립·e-PTFE 막(GTR) 적용 → 폭 1–4 mm 증가(상악에서 더 큼), 조직학적으로 분할면 사이 골재생 확인.

- `vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`  —[overturn · 결론 뒤집음]→  **`ayoub-2018-ridge-splitting-horizontal-augmentation-case`**
  - **근거 문장**: This is the key HEAD-TO-HEAD synthesis for choosing a horizontal ridge augmentation modality for the narrow ridge — GBR vs ridge-split (RS) vs osseodensification (OD) ridge expansion — ranking them by mean horizontal bone gain in one meta-analysis. It directly ties together the wiki's previously separate technique pages: the ridge-split case literature ([[wiki/bone-regeneration/simion-1992-jawbone
  - ▸ 출발(`vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`) 한줄: 수평 치조제 증대 3종을 직접 비교한 SR+MA(18편, 메타분석 17편, 환자 336명/임플란트 665개): 평균 수평 골증대량은 **가이드골재생(GBR) 4.04 mm > 치조제분할(RS) 3.66 mm > 골밀도화 치조제확장(OD) 2.15 mm** (P=0.002). 임플란트 생존율은 세 방법 모두 ~99%로 차이 없음. OD는 가장 넓은 치조제(4.37 mm)에, RS는 가장 좁은 치조제(3.43 mm)에 적용됨.
  - ▸ 대상(`ayoub-2018-ridge-splitting-horizontal-augmentation-case`) 한줄: 증례보고(스플릿마우스): 위축된 상악 수평골 부족 시 변형 치조골 분리술 — 피에조서저리·스티키본·알부민 동종골 적용; 동시 임플란트 식립 성공

- `vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`  —[overturn · 결론 뒤집음]→  **`enislidis-2006-staged-ridge-splitting-implant-mandible`**
  - **근거 문장**: This is the key HEAD-TO-HEAD synthesis for choosing a horizontal ridge augmentation modality for the narrow ridge — GBR vs ridge-split (RS) vs osseodensification (OD) ridge expansion — ranking them by mean horizontal bone gain in one meta-analysis. It directly ties together the wiki's previously separate technique pages: the ridge-split case literature ([[wiki/bone-regeneration/simion-1992-jawbone
  - ▸ 출발(`vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`) 한줄: 수평 치조제 증대 3종을 직접 비교한 SR+MA(18편, 메타분석 17편, 환자 336명/임플란트 665개): 평균 수평 골증대량은 **가이드골재생(GBR) 4.04 mm > 치조제분할(RS) 3.66 mm > 골밀도화 치조제확장(OD) 2.15 mm** (P=0.002). 임플란트 생존율은 세 방법 모두 ~99%로 차이 없음. OD는 가장 넓은 치조제(4.37 mm)에, RS는 가장 좁은 치조제(3.43 mm)에 적용됨.
  - ▸ 대상(`enislidis-2006-staged-ridge-splitting-implant-mandible`) 한줄: 2단계 하악 치조제 분할(prospective 기술노트, 환자 5명·17 임플란트): 협측 corticotomy로 녹색골절 위치를 미리 정하고 40일 치유 후 분할 → 협측 분절을 골막 유경피판으로 유지, 전 분절이 계획대로 골절되고 6개월에 전 임플란트 안정·부하 성공.

- `vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`  —[overturn · 결론 뒤집음]→  **`chen-2022-reverse-drilling-technique-alveolar-ridge-expansion`**
  - **근거 문장**: This is the key HEAD-TO-HEAD synthesis for choosing a horizontal ridge augmentation modality for the narrow ridge — GBR vs ridge-split (RS) vs osseodensification (OD) ridge expansion — ranking them by mean horizontal bone gain in one meta-analysis. It directly ties together the wiki's previously separate technique pages: the ridge-split case literature ([[wiki/bone-regeneration/simion-1992-jawbone
  - ▸ 출발(`vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`) 한줄: 수평 치조제 증대 3종을 직접 비교한 SR+MA(18편, 메타분석 17편, 환자 336명/임플란트 665개): 평균 수평 골증대량은 **가이드골재생(GBR) 4.04 mm > 치조제분할(RS) 3.66 mm > 골밀도화 치조제확장(OD) 2.15 mm** (P=0.002). 임플란트 생존율은 세 방법 모두 ~99%로 차이 없음. OD는 가장 넓은 치조제(4.37 mm)에, RS는 가장 좁은 치조제(3.43 mm)에 적용됨.
  - ▸ 대상(`chen-2022-reverse-drilling-technique-alveolar-ridge-expansion`) 한줄: 인공골(sawbone) 벤치 실험(27블록, 골폭 3종 × 드릴링 3종): 반시계(역회전, reverse) Densah 골밀도화(Osseodensification, OD) 드릴은 좁은 치조제(6.75 mm)에서만 표준 정회전보다 골폭을 유의하게 확장했지만, 더 큰 골 응력과 탄성 반발 때문에 임플란트 식립 깊이는 유의하게 더 얕았다.

- `vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`  —[overturn · 결론 뒤집음]→  **`tian-2019-alveolar-ridge-expansion-osseodensification-osteotome`**
  - **근거 문장**: This is the key HEAD-TO-HEAD synthesis for choosing a horizontal ridge augmentation modality for the narrow ridge — GBR vs ridge-split (RS) vs osseodensification (OD) ridge expansion — ranking them by mean horizontal bone gain in one meta-analysis. It directly ties together the wiki's previously separate technique pages: the ridge-split case literature ([[wiki/bone-regeneration/simion-1992-jawbone
  - ▸ 출발(`vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`) 한줄: 수평 치조제 증대 3종을 직접 비교한 SR+MA(18편, 메타분석 17편, 환자 336명/임플란트 665개): 평균 수평 골증대량은 **가이드골재생(GBR) 4.04 mm > 치조제분할(RS) 3.66 mm > 골밀도화 치조제확장(OD) 2.15 mm** (P=0.002). 임플란트 생존율은 세 방법 모두 ~99%로 차이 없음. OD는 가장 넓은 치조제(4.37 mm)에, RS는 가장 좁은 치조제(3.43 mm)에 적용됨.
  - ▸ 대상(`tian-2019-alveolar-ridge-expansion-osseodensification-osteotome`) 한줄: 동물 in vivo 연구 (atrophic 돼지 하악, n=12 임플란트, 4주 치유) — 골밀도화 (Osseodensification, OD) 군이 골-임플란트 접촉률 (Bone-to-Implant Contact, BIC) 62.5% vs 일반 osteotome 31.4% (P=0.018)로 우월. 단 표본이 6/6에 불과하고 골면적분율 (Bone Area Fraction Occupancy, BAFO)은 차이 없음 (P=0.198) — 짧은 관찰기간·소표본 한계 명시.

- `vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`  —[overturn · 결론 뒤집음]→  **`koutouzis-2019-alveolar-ridge-expansion-osseodensification-multicenter-retrospective`**
  - **근거 문장**: This is the key HEAD-TO-HEAD synthesis for choosing a horizontal ridge augmentation modality for the narrow ridge — GBR vs ridge-split (RS) vs osseodensification (OD) ridge expansion — ranking them by mean horizontal bone gain in one meta-analysis. It directly ties together the wiki's previously separate technique pages: the ridge-split case literature ([[wiki/bone-regeneration/simion-1992-jawbone
  - ▸ 출발(`vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`) 한줄: 수평 치조제 증대 3종을 직접 비교한 SR+MA(18편, 메타분석 17편, 환자 336명/임플란트 665개): 평균 수평 골증대량은 **가이드골재생(GBR) 4.04 mm > 치조제분할(RS) 3.66 mm > 골밀도화 치조제확장(OD) 2.15 mm** (P=0.002). 임플란트 생존율은 세 방법 모두 ~99%로 차이 없음. OD는 가장 넓은 치조제(4.37 mm)에, RS는 가장 좁은 치조제(3.43 mm)에 적용됨.
  - ▸ 대상(`koutouzis-2019-alveolar-ridge-expansion-osseodensification-multicenter-retrospective`) 한줄: 다기관 후향 연구 (retrospective), n=21 환자/28 임플란트 — 골밀도화 (Osseodensification, OD)로 좁은 능선(3–4 mm)에서 평균 2.83±0.66 mm의 능선 폭 확장이 가능했고 평균 삽입토크 61.2±13.9 Ncm, 임플란트 안정성 지수 (Implant Stability Quotient, ISQ) 77±3.74를 보였으나 임플란트 생존율 92.8% (28개 중 2개 실패)로 표준 임플란트 시리즈 대비 낮고 비교군 없는 후향 디자인이 한계.

- `vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`  —[overturn · 결론 뒤집음]→  **`bone-regeneration-protocol-ladder`**
  - **근거 문장**: This is the key HEAD-TO-HEAD synthesis for choosing a horizontal ridge augmentation modality for the narrow ridge — GBR vs ridge-split (RS) vs osseodensification (OD) ridge expansion — ranking them by mean horizontal bone gain in one meta-analysis. It directly ties together the wiki's previously separate technique pages: the ridge-split case literature ([[wiki/bone-regeneration/simion-1992-jawbone
  - ▸ 출발(`vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`) 한줄: 수평 치조제 증대 3종을 직접 비교한 SR+MA(18편, 메타분석 17편, 환자 336명/임플란트 665개): 평균 수평 골증대량은 **가이드골재생(GBR) 4.04 mm > 치조제분할(RS) 3.66 mm > 골밀도화 치조제확장(OD) 2.15 mm** (P=0.002). 임플란트 생존율은 세 방법 모두 ~99%로 차이 없음. OD는 가장 넓은 치조제(4.37 mm)에, RS는 가장 좁은 치조제(3.43 mm)에 적용됨.
  - ▸ 대상(`bone-regeneration-protocol-ladder`) 한줄: 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의사결정 ladder. 자연 치유 dimensional change · graft material 비교 · membrane/flap 조합 · soft tissue seal 4축. EFP/AO consensus + Cochrane review spine.


### bone-regeneration/ridge-preservation

- `adams-2022-clinical-evidence-alveolar-ridge-preservation`  —[contradict · 반박·충돌]→  **`bone-regeneration-socket-biology-and-arp-critique`**
  - **근거 문장**: Provides the skeptical counterweight that [[overviews/bone-regeneration-socket-biology-and-arp-critique]] needs — documents late xenograft failure (5–13 yr) and argues statistical dimensional preservation does not equal patient-centred benefit, contradicting the ARP-positive SR/MA pool in [[overviews/socket-preservation-arp-overview]]. Re-frames Carmagnola histology and the commercial drivers behi
  - ▸ 출발(`adams-2022-clinical-evidence-alveolar-ridge-preservation`) 한줄: BDJ 게재 narrative review + 2개 case report로 ARP의 통계적 효과가 임상적 환자 이득으로 직결되지 않음을 지적, 5~13년 후 xenograft 만성 실패(섬유 포함·peri-implantitis 양상) 사례를 제시하며 ARP의 무차별 적용에 회의를 표함.
  - ▸ 대상(`bone-regeneration-socket-biology-and-arp-critique`) 한줄: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.

- `adams-2022-clinical-evidence-alveolar-ridge-preservation`  —[contradict · 반박·충돌]→  **`socket-preservation-arp-overview`**
  - **근거 문장**: Provides the skeptical counterweight that [[overviews/bone-regeneration-socket-biology-and-arp-critique]] needs — documents late xenograft failure (5–13 yr) and argues statistical dimensional preservation does not equal patient-centred benefit, contradicting the ARP-positive SR/MA pool in [[overviews/socket-preservation-arp-overview]]. Re-frames Carmagnola histology and the commercial drivers behi
  - ▸ 출발(`adams-2022-clinical-evidence-alveolar-ridge-preservation`) 한줄: BDJ 게재 narrative review + 2개 case report로 ARP의 통계적 효과가 임상적 환자 이득으로 직결되지 않음을 지적, 5~13년 후 xenograft 만성 실패(섬유 포함·peri-implantitis 양상) 사례를 제시하며 ARP의 무차별 적용에 회의를 표함.
  - ▸ 대상(`socket-preservation-arp-overview`) 한줄: 발치와 보존술 종합 — ST 분류·골형태 CBCT 지표·소켓 무결성이 술식 선택 기준이며, 콜라겐 플러그 단독은 높이만 보존·폭경 불충분; 이종골(±PRF)이 폭경 유지 개선; 재료(DBBM·자가 DDM·Bio-Oss Collagen)·입자크기는 차원 보존에서 대체로 등가, 생물학적 보강은 rhBMP-2>L-PRF; DBBM 기반 ARP 후에도 다수는 임플란트 시 추가 골증대 필요(단 73–98%는 식립 가능).


### complaint-management

- `van-dael-2022-national-policies-complaint-handling`  —[contradict · 반박·충돌]→  **`gillespie-2025-complaint-handlers-bind-defensive`**
  - **근거 문장**: - [[complaint-management/gillespie-2025-complaint-handlers-bind-defensive]] -- reinforces: policy generates the contradictory demands behind defensiveness.
  - ▸ 출발(`van-dael-2022-national-policies-complaint-handling`) 한줄: NHS 트러스트 사례연구(직원 20명 인터뷰+문서) — 국가 민원정책이 혼란한 경로·'타당성' 심사·무용한 데이터수집·역인센티브로 개선을 저해함.
  - ▸ 대상(`gillespie-2025-complaint-handlers-bind-defensive`) 한줄: 온라인 비판에 응답하는 영국 병원 직원 혼합방법 연구 — 모순된 업무 요구에서 비롯된 6가지 방어 전술 규명.

- `mccreaddie-2021-qualitative-study-nhs-complaint`  —[contradict · 반박·충돌]→  **`friele-2006-patient-expectations-fair-complaint`**
  - **근거 문장**: - [[complaint-management/friele-2006-patient-expectations-fair-complaint]] -- contradicts: these responses violate complainants' fairness expectations.
  - ▸ 출발(`mccreaddie-2021-qualitative-study-nhs-complaint`) 한줄: NHS 서면 민원 응답 59건 담화분석 — 거짓 사과(fauxpology)와 불만의 주관화로 책임을 회피하는 패턴 규명.
  - ▸ 대상(`friele-2006-patient-expectations-fair-complaint`) 한줄: 병원 민원인 424명 설문 — 최우선 목표는 '재발 방지', 공정한 절차·(사과보다) 설명을 중시하고 금전 보상 요구는 드묾.

- `mccreaddie-2021-qualitative-study-nhs-complaint`  —[contradict · 반박·충돌]→  **`elias-2025-successful-handling-patient-complaints`**
  - **근거 문장**: - [[complaint-management/elias-2025-successful-handling-patient-complaints]] -- contradicts: CODE training teaches the opposite (genuine de-escalation/empathy).
  - ▸ 출발(`mccreaddie-2021-qualitative-study-nhs-complaint`) 한줄: NHS 서면 민원 응답 59건 담화분석 — 거짓 사과(fauxpology)와 불만의 주관화로 책임을 회피하는 패턴 규명.
  - ▸ 대상(`elias-2025-successful-handling-patient-complaints`) 한줄: CODE(Compassion·Operational Support·De-escalation·Empowerment) 모델 소개 — 운영·절차 트랙과 대인 커뮤니케이션 트랙을 결합한 민원담당자 이중구조 교육과정.

- `gillespie-2025-complaint-handlers-bind-defensive`  —[contradict · 반박·충돌]→  **`elias-2025-successful-handling-patient-complaints`**
  - **근거 문장**: - [[complaint-management/elias-2025-successful-handling-patient-complaints]] -- contradicts: training + operational support as the remedy.
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 한줄: 온라인 비판에 응답하는 영국 병원 직원 혼합방법 연구 — 모순된 업무 요구에서 비롯된 6가지 방어 전술 규명.
  - ▸ 대상(`elias-2025-successful-handling-patient-complaints`) 한줄: CODE(Compassion·Operational Support·De-escalation·Empowerment) 모델 소개 — 운영·절차 트랙과 대인 커뮤니케이션 트랙을 결합한 민원담당자 이중구조 교육과정.


### drug/antibiotics

- `thornhill-2019-adverse-reactions-oral-antibiotics-dentists`  —[상반 · 상반]→  **`drug-antibiotic-stewardship-overview`**
  - **근거 문장**: 치과의사가 처방하는 항생제별 백만건당 이상반응(Adverse Drug Reaction, ADR)·사망률을 실세계 분모로 정량화한 근거 — 아목시실린(Amoxicillin) 최안전, 클린다마이신(Clindamycin) 최고 사망률(주로 C. difficile)을 보여 "페니실린 알레르기→클린다마이신" 반사를 재고하게 한다. 항생제 스튜어드십 종합의 안전성 축을 보강한다. See [[overviews/drug-antibiotic-stewardship-overview]].
  - ▸ 출발(`thornhill-2019-adverse-reactions-oral-antibiotics-dentists`) 한줄: NHS England 처방 데이터(2010–2017) + Yellow Card 부작용(Adverse Drug Reaction, ADR) 보고: amoxicillin이 압도적으로 가장 안전(전체 21.5·치명적 0.1/백만 처방), clindamycin은 치명적 ADR 최고(2.9/백만, 대부분 Clostridiodes difficile 장염) — "amoxicillin 알레르기 → clindamycin 대체" 반사가 위험할 수 있음을 시사.
  - ▸ 대상(`drug-antibiotic-stewardship-overview`) 한줄: 치과 항생제 처방의 1차 원칙은 **제한 (restrictive)** — 감염성 심내막염 (Infective Endocarditis, IE) 고위험군·면역저하·IV BP·방사선 두경부·매복 발치·임플란트 일부에 한정. 단순 발치·치근단치주염(Apical Periodontitis)에는 prophylaxis 효과 없음. 1차 선택은 Amoxicillin (최저 부작용·치명률), Clindamycin은 회피. 치주 깊은 낭에는 전신 대신 국소 전달 항생제 우선. ---

- `momand-2024-antibiotic-prophylaxis-early-implant-failure`  —[대비되는 · 대비]→  **`uesugi-2024-risk-factors-early-failure-all-on-four`**
  - **근거 문장**: 조기 임플란트 실패 surveillance 배치에서 "예방 가능한가?"라는 개입 측 질문을 담당하는 최신 SR+MA. 위험인자 코호트인 [[implants/yari-2023-risk-factors-early-implant-failure]]·[[implants/uesugi-2024-risk-factors-early-failure-all-on-four]]가 흡연·해부·로딩을 강조하는 반면, 본 연구는 항생제 예방이 조기 실패를 거의 줄이지 못함(NNT 143)을 보여 개입 우선순위를 재정렬한다. 기존 [[drug/antibiotics/torof-2023-antibiotic-dental-implant-procedures-sr-ma]](술전 단일 amoxicillin 권고)와 대비되는 결과 — placebo-RCT
  - ▸ 출발(`momand-2024-antibiotic-prophylaxis-early-implant-failure`) 한줄: 체계적 고찰+메타분석(위약대조 이중맹검 RCT 7편, 환자 1859명 / 임플란트 3014개): 술전 항생제 예방은 조기 임플란트 실패를 유의하게 줄이지 못함(RR 0.66, 95% CI 0.30-1.47; 위험차 -0.007; NNT 143), GRADE 중간 — 비복잡 임플란트 수술에서 통상적 항생제 예방은 근거 부족.
  - ▸ 대상(`uesugi-2024-risk-factors-early-failure-all-on-four`) 한줄: 후향 코호트(환자 561명 / 임플란트 2364개, all-on-four 즉시로딩): 1년 임플란트 단위 생존율 상악 98.9% vs 하악 99.6%; 조기 실패 다변량 위험인자는 상악(OR 3.12)·흡연(OR 2.92), 광기능화(photofunctionalisation)는 보호 경향(OR 0.51)이나 비유의(p=0.25).

- `feldman-2023-metronidazole-disulfiram-reaction-case-control`  —[refut · 반증]→  **`orire-2026-revisiting-disulfiram-reaction-alcohol-metronidazole`**
  - **근거 문장**: A retrospective case-control chart review at a single Milwaukee academic ED (Dec 2010–Dec 2020) tested whether metronidazole actually causes a disulfiram-like reaction when ethanol is present. 36 patients (18 metronidazole + ethanol vs 18 ethanol-only matched on age, sex, and ethanol concentration) were compared for documented disulfiram-like effects (nausea, vomiting, flushing, tachycardia, hyper
  - ▸ 출발(`feldman-2023-metronidazole-disulfiram-reaction-case-control`) 한줄: 후향적 응급실 (ED) case-control 차트 리뷰 (n=36; 메트로니다졸 (Metronidazole) 18 + 알코올 매칭 대조 18): 혈중 알코올이 검출된 메트로니다졸 환자 중 디설피람 유사 반응 (Disulfiram-like Reaction) 기록 **0건**, 고혈압은 오히려 유의하게 적음 (16.7% vs 61.1%, P<0.0001) → 임상적으로 의미 있는 알코올-메트로니다졸 상호작용 부재 지지.
  - ▸ 대상(`orire-2026-revisiting-disulfiram-reaction-alcohol-metronidazole`) 한줄: 집중 문헌 리뷰 (4개 DB, 1970–2024, 11편): 알코올과 경구 메트로니다졸 (Metronidazole) 사이의 임상적으로 유의한 디설피람 유사 반응 (Disulfiram-like Reaction) 근거는 **약함** — 증례보고는 양성이나 대조시험·차트리뷰·동물실험은 음성 → 엄격한 금주 권고의 재고 필요. (초록 기반)

- `low-2026-dental-antibiotic-prescribing-practices-singapore`  —[contradict · 반박·충돌]→  **`de-angelis-2025-antibiotic-third-molar-extraction-prevention-sr`**
  - **근거 문장**: - [[drug/antibiotics/de-angelis-2025-antibiotic-third-molar-extraction-prevention-sr]] — evidence base contradicting the 71.2% routine third-molar prophylaxis seen here.
  - ▸ 출발(`low-2026-dental-antibiotic-prescribing-practices-singapore`) 한줄: 싱가포르 치과의사 280명 단면조사(2024): 적절한 항생제 처방률이 임상상황별 6.5~97.7%로 편차가 컸고(치주 30.4%·구강외과 34.0% 최저), 사랑니 발치 후 71.2%·임플란트 식립 전 73.5%로 예방적 항생제를 과처방했으며, 공공부문·국내수련·저경력 치과의사가 더 적절히 처방했고 AMR 지식은 부족했다(59.3%가 내성균 전파 가능성 인지 못함).
  - ▸ 대상(`de-angelis-2025-antibiotic-third-molar-extraction-prevention-sr`) 한줄: Univ Genoa SR (Dent J 2025): 제3대구치 발치 항생제 예방 — 단순 발치에 효과 미미, 매복·외과적 발치에 한정 적응. Camps-Font 2024 NMA의 NNT=25 결론과 일치.


### endodontics

- `abada-2025-obturation-techniques-post-obturation-pain-rct`  —[counterpoint · 반대 논점]→  **`shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment`**
  - **근거 문장**: - [[endodontics/shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment]] — retreatment/retrievability counterpoint to the obturation choice studied here.
  - ▸ 출발(`abada-2025-obturation-techniques-post-obturation-pain-rct`) 한줄: RCT(하악 제1대구치 150개, 단일내원, 무증상 비가역적 치수염): CeraSeal vs AH Plus를 측방가압·연속파가압·단일콘 충전으로 비교. 모든 군 통증 낮음(VAS 0–1.4). 충전법 자체는 통증 무관(p=0.124)이나 AH Plus가 CeraSeal보다 통증 유의하게 높음(전체 p<0.001, 연속파가압에서 p<0.001). 실러 일출 빈도는 군간 차이 없으나(p=0.499) 일출 시 통증 증가(p<0.001).
  - ▸ 대상(`shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment`) 한줄: In-vitro 마이크로-CT 연구 (하악소구치 36개, 군당 12개): AH Plus Bioceramic(AHB)·Ceraseal(CER) 단일콘 충전이 에폭시 레진 AH Plus Jet(AHJ)보다 재근관치료 시 제거가 잘 됨 — WaveOne Gold + XP-endo Finisher 후 제거율 94.8%·92.5% vs 87.1%.


### endodontics/diagnosis

- `yamamoto-silva-2017-chondroblastic-osteosarcoma-mimicking-periapical-abscess`  —[반론 · 반론]→  **`karamifar-2020-endodontic-periapical-lesion-an-overview`**
  - **근거 문장**: [[wiki/endodontics/diagnosis/karamifar-2020-endodontic-periapical-lesion-an-overview]]는 근단 방사선투과상(periapical radiolucency)이 비치성(non-endodontic) 병변일 수 있음을 일반론으로 다루지만, 악성 종양이 치근단 농양(periapical abscess)을 모방한 구체적 증례가 부족했다. 본 증례보고(Yamamoto-Silva 2017)는 생활치(vital pulp)에 동반된 근단 방사선투과상·치주인대강 확대가 실제로는 연골모세포성 골육종(chondroblastic osteosarcoma)이었던 사례로, 근관치료 전 비치성 악성 종양을 감별진단에 포함해야 함을 보강한다. 방사선학적으로는 [[wiki/radi
  - ▸ 출발(`yamamoto-silva-2017-chondroblastic-osteosarcoma-mimicking-periapical-abscess`) 한줄: 증례보고(J Appl Oral Sci 2017): 18세 남성에서 생활치 #29/#30/#31에 근단 방사선투과상·치주인대강 확대·치조백선 소실이 보여 치근단 농양으로 의심했으나 절개생검에서 연골모세포성 골육종으로 확진된 사례 — 근단병소 감별진단에 비치성 악성 종양을 반드시 포함해야 함.
  - ▸ 대상(`karamifar-2020-endodontic-periapical-lesion-an-overview`) 한줄: 근단병소(치근단성 치주염)의 병인·진단·치료를 정리한 narrative overview — 진단 표준은 여전히 조직병리이나 CBCT·MRI·echography가 육아종/낭종 감별에 유망.

- `yamamoto-silva-2017-chondroblastic-osteosarcoma-mimicking-periapical-abscess`  —[반론 · 반론]→  **`mortazavi-2016-lesions-associated-with-periodontal-ligament`**
  - **근거 문장**: [[wiki/endodontics/diagnosis/karamifar-2020-endodontic-periapical-lesion-an-overview]]는 근단 방사선투과상(periapical radiolucency)이 비치성(non-endodontic) 병변일 수 있음을 일반론으로 다루지만, 악성 종양이 치근단 농양(periapical abscess)을 모방한 구체적 증례가 부족했다. 본 증례보고(Yamamoto-Silva 2017)는 생활치(vital pulp)에 동반된 근단 방사선투과상·치주인대강 확대가 실제로는 연골모세포성 골육종(chondroblastic osteosarcoma)이었던 사례로, 근관치료 전 비치성 악성 종양을 감별진단에 포함해야 함을 보강한다. 방사선학적으로는 [[wiki/radi
  - ▸ 출발(`yamamoto-silva-2017-chondroblastic-osteosarcoma-mimicking-periapical-abscess`) 한줄: 증례보고(J Appl Oral Sci 2017): 18세 남성에서 생활치 #29/#30/#31에 근단 방사선투과상·치주인대강 확대·치조백선 소실이 보여 치근단 농양으로 의심했으나 절개생검에서 연골모세포성 골육종으로 확진된 사례 — 근단병소 감별진단에 비치성 악성 종양을 반드시 포함해야 함.
  - ▸ 대상(`mortazavi-2016-lesions-associated-with-periodontal-ligament`) 한줄: 치주인대(PDL) 확장을 유발하는 병변군을 영상의학적으로 감별 정리한 review — 양성(교합외상·교정력)부터 중대(골육종·비호지킨림프종·경피증)까지 포괄.


### food-impaction

- `mehanna-2021-proximal-contact-alterations-prospective`  —[대비되는 · 대비]→  **`pang-2017-prevalence-proximal-contact-loss-prospective`**
  - **근거 문장**: food-impaction 카테고리의 단기 전향(3개월) 측정연구로 인제스트. [[food-impaction/pang-2017-prevalence-proximal-contact-loss-prospective]] 장기 데이터와 대비되는 조기 contact tightness 감소 동역학을 정량 제시하고, restoration type·implant system을 인자로 강조한다.
  - ▸ 출발(`mehanna-2021-proximal-contact-alterations-prospective`) 한줄: 3개월 전향연구(43명, 구치부 IFP 43개): 3개월 내 접촉 강도 유의 감소; restoration type이 mesial·distal에, implant system이 distal에 영향.
  - ▸ 대상(`pang-2017-prevalence-proximal-contact-loss-prospective`) 한줄: 7년 전향연구(150명, IFP 234개): 근접접촉 59.9%에서 PCL; 인접치 골지지 저하·상악·mesial이 유의 위험인자.


### immediate-implant/socket-shield

- `lu-2025-socket-shield-conventional-aesthetic-meta`  —[overturn · 결론 뒤집음]→  **`socket-shield-technique-overview`**
  - **근거 문장**: This 2025 meta-analysis is the **largest pooled comparison of SST vs CIIP in the esthetic zone to date** — 27 studies (22 RCTs, 5 NRSI), 1307 implants — and notably folds in 13 Chinese-language studies that English-only predecessors omitted. It does **not overturn** the existing wiki thesis ([[wiki/overviews/socket-shield-technique-overview]]): SST again wins on buccal-bone preservation, PES, and 
  - ▸ 출발(`lu-2025-socket-shield-conventional-aesthetic-meta`) 한줄: 소켓실드 기법(Socket Shield Technique, SST) vs 전통 즉시식립(CIIP) 메타분석(27편·1307임플란트). SST가 협측 수평 골소실 −0.50 mm·수직 −0.56 mm, 핑크심미점수(PES) +1.25, 임플란트 안정성지수(ISQ) +5.83 우월, 생존율 동등(RR 1.00). 실드 높이·두께·골이식 무관하게 SST 우월. 현존 최대 풀이나 이질성 높고 장기 데이터 부족.
  - ▸ 대상(`socket-shield-technique-overview`) 한줄: 소켓실드 기법(Socket Shield Technique, SST) 17개 페이지 + 초록 수준 신규 4편 종합. SR/MA + RCT가 협측 골판·핑크 심미 보존 우월로 수렴(협측 골판 흡수 BBPR 약 0.32 vs 1.05 mm, 변연골 소실 MBL 약 0.39 vs 1.00 mm, 핑크 심미 점수 PES +1.3). 단 근거 다수가 증례보고이고 장기(≥5년) 데이터 부족, 실드 관련 합병증 4–17%로 숙련자·선별 심미부 증례에 한정. 신규 FEA는 잔존 실드가 주위골 응력 집중을 최대화함


### implants

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`  —[contradict · 반박·충돌]→  **`ruhstorfer-2024-customized-vs-conventional-healing-abutments-sr`**
  - **근거 문장**: Healing-abutment batch — where [[wiki/implants/ruhstorfer-2024-customized-vs-conventional-healing-abutments-sr]] asks whether abutment *shape/customization* governs soft-tissue outcomes, this paper isolates the orthogonal variable: does abutment *surface* (machined vs anodized/laser/other modifications) drive peri-implant soft-tissue attachment, inflammation, and maintenance? Reinforces the siblin
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 한줄: 체계적 문헌고찰 + 메타분석 (10편 포함, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 표면은 단기적으로 플라크 지수·탐침 시 출혈(BoP)·탐침 깊이(PD)에서 대조군과 유의한 차이가 없었고, 장기(5~6년) 연구는 표면 처리 기법에 따라 상반된 결과를 보였다.
  - ▸ 대상(`ruhstorfer-2024-customized-vs-conventional-healing-abutments-sr`) 한줄: 체계적 문헌고찰(5편 — RCT 2·전향 2·후향 1; 임플란트 190개, 생존율 100%, 6–36개월)로, 맞춤형 치유지대주(customized healing abutment)가 기성 티타늄 치유지대주 대비 임플란트주위 연·경조직과 심미가 더 좋아지는 경향을 보이고 치료 통증은 줄이며 생물학적·심미적 불리함은 없다고 결론.

- `hussein-2019-thread-depth-implant-shape-stress-mandible-fea`  —[상반 · 상반]→  **`leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress`**
  - **근거 문장**: 임플란트 body shape(tapered vs cylinder)·thread depth가 하중기 골 응력에 미치는 영향을 FEA로 본 연구로, [[implants/leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress]] 의 design×bone density 응력 결과와 짝을 이루는 FEA 클러스터 구성. tapered body가 응력 peak가 높다는 상반된 신호를 제공해 macrogeometry 선택의 trade-off를 보강.
  - ▸ 출발(`hussein-2019-thread-depth-implant-shape-stress-mandible-fea`) 한줄: 하악 FEA — 임플란트 경부 crestal cortical bone에 최대 응력, tapered body가 cylinder보다 모든 골종에서 peak 응력 높음.
  - ▸ 대상(`leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress`) 한줄: FEA — D4 저밀도골·cortical 두께 감소가 임플란트 주위 응력을 높이고, 나사 설계·지대주 각도가 경사하중 응력분포를 좌우.

- `chen-2022-reverse-drilling-technique-alveolar-ridge-expansion`  —[Counterpoint · 반대 논점]→  **`rittipakorn-2025-clockwise-osseodensification-primary-stability-cadaveric`**
  - **근거 문장**: Counterpoint and mechanistic complement to [[wiki/implants/versah-protocols/rittipakorn-2025-clockwise-osseodensification-primary-stability-cadaveric]], which is a cadaveric study contrasting bur **rotation direction** (clockwise vs counter-clockwise) for bone compaction/primary stability. This Chen 2022 sawbone bench study addresses the same core mechanism — the **reverse (counter-clockwise) dril
  - ▸ 출발(`chen-2022-reverse-drilling-technique-alveolar-ridge-expansion`) 한줄: 인공골(sawbone) 벤치 실험(27블록, 골폭 3종 × 드릴링 3종): 반시계(역회전, reverse) Densah 골밀도화(Osseodensification, OD) 드릴은 좁은 치조제(6.75 mm)에서만 표준 정회전보다 골폭을 유의하게 확장했지만, 더 큰 골 응력과 탄성 반발 때문에 임플란트 식립 깊이는 유의하게 더 얕았다.
  - ▸ 대상(`rittipakorn-2025-clockwise-osseodensification-primary-stability-cadaveric`) 한줄: 사람 경골(tibia) 사체 짝지음-부위 연구(임플란트 40개, D3/D4 저밀도골)로 **시계방향 골밀도화(CW-OD, 800 rpm)** vs 표준 드릴링(SD) 비교: OD가 ISQ(67.5 vs 62.9, p=0.077)·삽입토크(34.0 vs 29.5 Ncm, p=0.052)에서 더 높은 경향이나 비유의했고, 분산은 더 좁았으며 IT–ISQ 상관은 OD에서만 유의(ρ=0.577, p=0.0077)했다.

- `kim-2026-implant-angulation-peri-implant-bone`  —[반박 · 반박]→  **`implant-occlusion-loading-biomechanics-overview`**
  - **근거 문장**: 비축방향(nonaxial) 식립이 변연골 소실(MBL)에 미치는 영향을 CAD 기반 3차원 각도 측정으로 정량화한 한국 박사학위 연구(506개 임플란트, 5.1년). 기존 [[occlusion/di-fiore-2022-periimplant-bone-loss-overload-occlusal-analysis]]·[[overviews/implant-occlusion-loading-biomechanics-overview]]가 교합 과부하–골소실을 다루지만, 선행 연구(Koutouzis 2007, Lee)는 근원심 2D 각도만 측정해 "비축 하중이 MBL을 늘리지 않는다"는 음성 결과를 냈다. 이 연구는 협설 각도를 포함한 다방향 측정으로 그 음성 결과를 보강·반박하며, [[implants/stilwell-2024-
  - ▸ 출발(`kim-2026-implant-angulation-peri-implant-bone`) 한줄: CAD 3D 각도 측정을 쓴 5년 후향연구(288명·506개). 비축방향 임플란트 변연골 소실이 유의하게 컸고(0.22±0.48 vs 0.10±0.39 mm, P<.05), 상악>하악(P<.001), 비축방향이 임플란트 지지 고정성 보철과 대합할 때 골소실이 가장 컸다(상호작용 Δ0.373 mm).
  - ▸ 대상(`implant-occlusion-loading-biomechanics-overview`) 한줄: 교합 클러스터를 임플란트 관점으로 종합. 골유착 임플란트는 치주인대가 없어 교합력이 완충도 감지도 안 되므로, 설계 목표는 하중 최소화·분산이다. 임상·FEA 근거는 4점으로 수렴 — 임플란트 교합접촉은 6-12개월 내 변동(대개 상대적 저위교합 방향); "약교합(light occlusion)"은 힘을 낮추나 시간이 지나며 불안정; 교합양식·보철 구성(캔틸레버·치아-임플란트 연결·full-arch)이 임플란트주위 응력을 좌우; 체어사이드 레버는 단일 이상적 양식이 아니라 정기 교합 재점검(T-Sc

- `kim-2026-implant-angulation-peri-implant-bone`  —[반박 · 반박]→  **`stilwell-2024-occlusal-considerations-implant-maintenance`**
  - **근거 문장**: 비축방향(nonaxial) 식립이 변연골 소실(MBL)에 미치는 영향을 CAD 기반 3차원 각도 측정으로 정량화한 한국 박사학위 연구(506개 임플란트, 5.1년). 기존 [[occlusion/di-fiore-2022-periimplant-bone-loss-overload-occlusal-analysis]]·[[overviews/implant-occlusion-loading-biomechanics-overview]]가 교합 과부하–골소실을 다루지만, 선행 연구(Koutouzis 2007, Lee)는 근원심 2D 각도만 측정해 "비축 하중이 MBL을 늘리지 않는다"는 음성 결과를 냈다. 이 연구는 협설 각도를 포함한 다방향 측정으로 그 음성 결과를 보강·반박하며, [[implants/stilwell-2024-
  - ▸ 출발(`kim-2026-implant-angulation-peri-implant-bone`) 한줄: CAD 3D 각도 측정을 쓴 5년 후향연구(288명·506개). 비축방향 임플란트 변연골 소실이 유의하게 컸고(0.22±0.48 vs 0.10±0.39 mm, P<.05), 상악>하악(P<.001), 비축방향이 임플란트 지지 고정성 보철과 대합할 때 골소실이 가장 컸다(상호작용 Δ0.373 mm).
  - ▸ 대상(`stilwell-2024-occlusal-considerations-implant-maintenance`) 한줄: narrative-review(BDJ 2024): 임플란트 유지관리 교합 점검 총론 — 임플란트 파절 0.5%; PDL 없어 과부하 위험; 4단계 연간 교합 평가 프로토콜 제시; 이갈이 보호장치 필수.

- `huwais-2017-autografting-tool-enhanced-flute-profile`  —[대비되는 · 대비]→  **`huwais-2017-novel-osseous-densification-osteotomy-primary-stability`**
  - **근거 문장**: 대화에서 다룬 **덴샤버(Densah/Versah)의 "날 모양(flute profile)"과 CW=절삭 / CCW=압축 양방향 메커니즘의 1차 원천 문서**다. 기존 [[wiki/implants/huwais-2017-novel-osseous-densification-osteotomy-primary-stability]] 는 동일 발명자(Huwais)의 *벤치 검증 논문*일 뿐 도구 자체의 기하·청구항은 담지 않는다. 이 PCT 특허는 negative rake angle flute, densifying face/cutting face/land/working edge 구조와 hydraulic autografting 원리를 직접 청구·기술해, 해냄 콘덴싱 스크류 특허 [[wiki/implants/kim-2019-
  - ▸ 출발(`huwais-2017-autografting-tool-enhanced-flute-profile`) 한줄: Huwais IP Holding LLC / 발명자 Salah Huwais의 PCT 특허(WO 2017/124079): 골밀도화 Densah/Versah 회전 osteotome. 개량 핵심은 연속 음의 레이크각(negative rake angle) flute이며, 각 flute이 cutting face와 densifying face를 함께 가져 같은 도구가 한 방향=절삭 / 반대 방향=압축·hydraulic autografting을 수행 — 덴샤버 "날 모양"의 원천 문서.
  - ▸ 대상(`huwais-2017-novel-osseous-densification-osteotomy-primary-stability`) 한줄: 시험관 벤치 연구 (in vitro), 돼지 경골 (porcine tibia) 72 골삭제 (osteotomy) — 같은 다중날 (multi-fluted) 버 (bur)를 반시계방향으로 회전시키는 골밀도화 (Osseodensification, OD)가 표준 드릴링 대비 삽입·제거 토크 (Insertion/Removal Torque)와 골-임플란트 접촉률 (Bone-to-Implant Contact, BIC, 약 3배)을 유의하게 상승시키고 골삭제 둘레에 골밀도 (Bone Mineral Densit

- `kim-2019-double-spiral-condensing-screw-implant`  —[대비되는 · 대비]→  **`changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift`**
  - **근거 문장**: 대화에서 다룬 해냄버(HaeNaem bur)의 회전방향-압축 메커니즘의 **공학적 1차 근거 문서**다. 임상 데이터 [[wiki/sinus-lift/transcrestal/changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift]] 는 "HaeNaem이 시계방향(CW)으로 골치밀화한다"는 결과만 보여줄 뿐 *왜·어떻게*는 설명하지 못한다. 이 (주)해냄 특허는 그 스크류 기하(이중 스파이럴: 압착나사산부 + 본파우더안내홈 + 하부압착돔)와 "회전방향과 반대방향 나사산" 원리를 직접 기술해, 골밀도화(Osseodensification, OD) 발명 원리를 정리한 [[wiki/implants/huwais-2017-novel-osseous-densification-
  - ▸ 출발(`kim-2019-double-spiral-condensing-screw-implant`) 한줄: (주)해냄 특허출원(공개 10-2021-0014513, 발명자 김성주): 이중 스파이럴(압착나사산부 + 본파우더안내홈 + 하부압착돔) 콘덴싱 스크류. 골삭제·측방 골치밀화를 동시에 하면서 분쇄골을 하부압착돔으로 보내 근단(내측)까지 치밀화 → 종래 버의 측방-편중 한계를 보완하고 단일 기구로 상악동 거상까지 수행. 해냄버의 설계 근거 문서.
  - ▸ 대상(`changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift`) 한줄: 전향적 단일군 연구(n=12, 잔존 골고 6–8mm): HaeNaem Zero Bone Loss CW-OD 버 키트로 무이식 경치조골 간접 거상 동시 임플란트 식립 후 4개월 CBCT에서 근심·원심·협측·구개측 4개 방향 모두 유의한 골 높이 증가(p<0.01).

- `surendra-2025-flapless-versus-flapped-crestal-bone`  —[contradict · 반박·충돌]→  **`pitman-2023-immediate-implant-flap-flapless-sr-ma`**
  - **근거 문장**: User requested a PubMed ingest on flapless implant placement. The wiki's flapless evidence is concentrated in the *immediate*-implant context ([[immediate-implant/pitman-2023-immediate-implant-flap-flapless-sr-ma]], [[immediate-implant/mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma]], [[immediate-implant/paknejad-2017-flapless-immediate-implant-buccal-gap-rct]]); this RCT addresses t
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 한줄: 하악 구치부 치유된 치조제 단일치 RCT (n=40)에서 무피판(flapless)이 피판(flapped)보다 치조정 골소실을 유의하게 적게 (6개월 0.48 vs 0.82 mm, p<0.001) — 양군 생존율 100%.
  - ▸ 대상(`pitman-2023-immediate-implant-flap-flapless-sr-ma`) 한줄: SR+MA (Cosyn 그룹): 단일 즉시식립 시 mucoperiosteal flap vs flapless — 협측 hard/soft tissue 변화, 임상·심미·PROMs 비교; RCT만 포함.

- `surendra-2025-flapless-versus-flapped-crestal-bone`  —[contradict · 반박·충돌]→  **`mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma`**
  - **근거 문장**: User requested a PubMed ingest on flapless implant placement. The wiki's flapless evidence is concentrated in the *immediate*-implant context ([[immediate-implant/pitman-2023-immediate-implant-flap-flapless-sr-ma]], [[immediate-implant/mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma]], [[immediate-implant/paknejad-2017-flapless-immediate-implant-buccal-gap-rct]]); this RCT addresses t
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 한줄: 하악 구치부 치유된 치조제 단일치 RCT (n=40)에서 무피판(flapless)이 피판(flapped)보다 치조정 골소실을 유의하게 적게 (6개월 0.48 vs 0.82 mm, p<0.001) — 양군 생존율 100%.
  - ▸ 대상(`mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma`) 한줄: SR+MA: flapless 즉시식립 시 peri-implant gap에 골이식 추가 vs 비추가 — hard/soft tissue 변화를 평가; RCT 한정.

- `surendra-2025-flapless-versus-flapped-crestal-bone`  —[contradict · 반박·충돌]→  **`paknejad-2017-flapless-immediate-implant-buccal-gap-rct`**
  - **근거 문장**: User requested a PubMed ingest on flapless implant placement. The wiki's flapless evidence is concentrated in the *immediate*-implant context ([[immediate-implant/pitman-2023-immediate-implant-flap-flapless-sr-ma]], [[immediate-implant/mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma]], [[immediate-implant/paknejad-2017-flapless-immediate-implant-buccal-gap-rct]]); this RCT addresses t
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 한줄: 하악 구치부 치유된 치조제 단일치 RCT (n=40)에서 무피판(flapless)이 피판(flapped)보다 치조정 골소실을 유의하게 적게 (6개월 0.48 vs 0.82 mm, p<0.001) — 양군 생존율 100%.
  - ▸ 대상(`paknejad-2017-flapless-immediate-implant-buccal-gap-rct`) 한줄: 무피판 즉시식립 협측 틈새 이종골 충전 RCT — 충전군에서 6·12개월 협측 골 흡수 유의 감소.


### implants/peri-implantitis

- `sbricoli-2026-peri-implant-disease-prevalence-type2-diabetes`  —[contradict · 반박·충돌]→  **`lin-2025-influence-of-prosthetic-designs`**
  - **근거 문장**: Most existing peri-implantitis pages in our wiki frame T2DM as an established systemic risk factor and focus on keratinized mucosa, prosthetic design, and surface decontamination. This Italian single-center cross-sectional study (Sbricoli 2026) provides a direct **T2DM vs non-DM head-to-head prevalence** data point that *contradicts* the prevailing "diabetes as major risk factor" narrative — findi
  - ▸ 출발(`sbricoli-2026-peri-implant-disease-prevalence-type2-diabetes`) 한줄: 단일기관 횡단연구(70명·임플란트 227개; 제2형 당뇨 35명 vs 비당뇨 35명): 임플란트주위질환(80% vs 77%, p=0.99)·점막염(51% vs 63%, p=0.47)·주위염(51% vs 43%, p=0.63) 모두 두 군 간 유의차 없음. 단, 검정력 부족 + 양 군 모두 치주염 과거력(83~94%)이 높아 당뇨 단독 효과가 가려졌을 가능성.
  - ▸ 대상(`lin-2025-influence-of-prosthetic-designs`) 한줄: 93편 AO/AAP SR+MA: 비연결·플랫폼스위칭·원추형 내부연결·어버트먼트 높이 ≥2 mm·one-abutment-one-time이 변연골소실(MBL)을 줄였고, 나사/시멘트 유지·치관-임플란트 비는 MBL에 영향 없음.

- `kim-2025-toothpick-method-cibotium-peri-implant-mucositis-rct`  —[counterpoint · 반대 논점]→  **`jepsen-2015-primary-prevention-periimplantitis-managing-mucositis`**
  - **근거 문장**: RCT (Kim 2025, n=60) that uses the **toothpick method (TPM)** of professional toothbrushing as the mechanical delivery vehicle for a natural Cibotium barometz (CB) extract to treat peri-implant mucositis — the first study to combine TPM with a natural anti-inflammatory agent against PIM-related bacteria, extending the toothpick method into peri-implant maintenance. Reinforces [[implants/peri-impla
  - ▸ 출발(`kim-2025-toothpick-method-cibotium-peri-implant-mucositis-rct`) 한줄: 이중맹검 RCT(n=60: CB-TPM 21 / 클로르헥시딘-TPM 20 / 생리식염수-TPM 19) — 세 군 모두 토스픽 방법(Toothpick Method, TPM)으로 전달했을 때, CB-TPM만 타액 잠혈을 감소(Cohen's d=1.148)시켰고 P. micra·T. forsythia·P. intermedia에서 단독으로 큰 효과(d≥0.8)를 보여, 천연 Cibotium barometz 추출물+TPM이 부작용 없는 비수술적 임플란트주위 점막염 옵션임을 제시.
  - ▸ 대상(`jepsen-2015-primary-prevention-periimplantitis-managing-mucositis`) 한줄: European Workshop Group 4 합의 — 점막염 관리 = 주위염 1차 예방. 가중평균 유병률 점막염 43%·주위염 22%, BoP가 핵심 임상지표, 정기 SPT 결여가 위험 증가.

- `kim-2025-toothpick-method-cibotium-peri-implant-mucositis-rct`  —[counterpoint · 반대 논점]→  **`mauriello-2026-peri-implant-mucositis-adjunctive-narrative-review`**
  - **근거 문장**: RCT (Kim 2025, n=60) that uses the **toothpick method (TPM)** of professional toothbrushing as the mechanical delivery vehicle for a natural Cibotium barometz (CB) extract to treat peri-implant mucositis — the first study to combine TPM with a natural anti-inflammatory agent against PIM-related bacteria, extending the toothpick method into peri-implant maintenance. Reinforces [[implants/peri-impla
  - ▸ 출발(`kim-2025-toothpick-method-cibotium-peri-implant-mucositis-rct`) 한줄: 이중맹검 RCT(n=60: CB-TPM 21 / 클로르헥시딘-TPM 20 / 생리식염수-TPM 19) — 세 군 모두 토스픽 방법(Toothpick Method, TPM)으로 전달했을 때, CB-TPM만 타액 잠혈을 감소(Cohen's d=1.148)시켰고 P. micra·T. forsythia·P. intermedia에서 단독으로 큰 효과(d≥0.8)를 보여, 천연 Cibotium barometz 추출물+TPM이 부작용 없는 비수술적 임플란트주위 점막염 옵션임을 제시.
  - ▸ 대상(`mauriello-2026-peri-implant-mucositis-adjunctive-narrative-review`) 한줄: Narrative review (Quintessence Int 2026, 9 RCTs / 414 patients): professional mechanical plaque removal (PMPR) remains the gold standard for peri-implant mucositis; chlorhexidine, local antibiotics, sodium hypochlorite, probiotics, and bioactive agents show within-group improveme

- `pujarern-2024-biofilm-removal-implant-airflow-erythritol`  —[반박 · 반박]→  **`peri-implantitis-management-overview`**
  - **근거 문장**: Peri-implantitis 비수술/유지 단계의 핵심은 임플란트 표면 생물막 제거인데, [[overviews/peri-implantitis-management-overview]]의 표면 decontamination 분기에서 air-polishing powder 선택(어떤 powder가 가장 효율적이고 표면 손상이 적은가)에 대한 직접 비교 근거를 보강하기 위해 인제스트. 본 in-vitro RCT-design 비교는 SB(40 µm) vs ERY(14 µm) 두 파우더의 생물막 제거 효율을 직접 대조해, 큰 입자가 더 잘 제거할 것이라는 통념을 반박하고 작은 입자(ERY) 쪽이 표면 손상이 적어 임상적으로 선호된다는 결론을 제공한다. 또한 [[implants/peri-implantitis/baima-202
  - ▸ 출발(`pujarern-2024-biofilm-removal-implant-airflow-erythritol`) 한줄: 체외(in-vitro) 연구(임플란트 33개, 3군 각 n=11): 탄산수소나트륨(Sodium Bicarbonate, SB, 40 µm)과 에리스리톨(Erythritol, ERY, 14 µm) air-polishing 파우더 모두 무처치 대조군 대비 생물막을 훨씬 잘 제거(평균 광학밀도 OD 0.130·0.129 vs 0.728; p<0.05)했고 둘 사이 차이는 유의하지 않아(p>0.05), 표면 손상이 적은 에리스리톨이 임상적으로 선호된다.
  - ▸ 대상(`peri-implantitis-management-overview`) 한줄: 10편 종합: 환자 단위 유병률 19.5%, 점막염 관리 = 1차 예방, 단일 표면제염 프로토콜 우위 없음, 보철 디자인(플랫폼스위칭·원추형 연결·어버트먼트 높이 ≥2 mm·one-abutment-one-time)이 MBL을 유의하게 줄임. 더해 보철·해부학적 위험축 — 출현각 >30°+볼록 윤곽(Soulami), RM-AC ≤1.5 mm → MBL 3.42배(Basak IDRA), 얇은 치은 표현형의 간접 골소실 위험(da Silva) — 이 조절·평가 가능한 design/host 인자를 보강.

- `pujarern-2024-biofilm-removal-implant-airflow-erythritol`  —[반박 · 반박]→  **`baima-2022-surface-decontamination-protocols-surgical-periimplantitis`**
  - **근거 문장**: Peri-implantitis 비수술/유지 단계의 핵심은 임플란트 표면 생물막 제거인데, [[overviews/peri-implantitis-management-overview]]의 표면 decontamination 분기에서 air-polishing powder 선택(어떤 powder가 가장 효율적이고 표면 손상이 적은가)에 대한 직접 비교 근거를 보강하기 위해 인제스트. 본 in-vitro RCT-design 비교는 SB(40 µm) vs ERY(14 µm) 두 파우더의 생물막 제거 효율을 직접 대조해, 큰 입자가 더 잘 제거할 것이라는 통념을 반박하고 작은 입자(ERY) 쪽이 표면 손상이 적어 임상적으로 선호된다는 결론을 제공한다. 또한 [[implants/peri-implantitis/baima-202
  - ▸ 출발(`pujarern-2024-biofilm-removal-implant-airflow-erythritol`) 한줄: 체외(in-vitro) 연구(임플란트 33개, 3군 각 n=11): 탄산수소나트륨(Sodium Bicarbonate, SB, 40 µm)과 에리스리톨(Erythritol, ERY, 14 µm) air-polishing 파우더 모두 무처치 대조군 대비 생물막을 훨씬 잘 제거(평균 광학밀도 OD 0.130·0.129 vs 0.728; p<0.05)했고 둘 사이 차이는 유의하지 않아(p>0.05), 표면 손상이 적은 에리스리톨이 임상적으로 선호된다.
  - ▸ 대상(`baima-2022-surface-decontamination-protocols-surgical-periimplantitis`) 한줄: 16 RCT(22편) SR+MA — 외과적 주위염 치료 시 기계·화학·물리 표면제염 프로토콜 비교, 어느 단일 프로토콜도 임상·방사선 결과에서 명확한 우월성 입증 못함.

- `fathi-2025-keratinized-mucosa-implant-health-umbrella-review`  —[상충 · 상충]→  **`roccuzzo-2025-keratinized-mucosa-peri-implant-20year-mandible`**
  - **근거 문장**: 각화점막 폭경(Keratinized Mucosa Width, KMW)이 임플란트 주위염 위험인자인지에 대한 문헌은 수십 년간 상충된 결과를 보여왔다. 이 우산 리뷰는 기존 10개 SR/MA를 집대성하여 KMW ≥2 mm 기준의 임상적 근거를 종합한다는 점에서, 기존 개별 SR 논문인 [[implants/peri-implantitis/roccuzzo-2025-keratinized-mucosa-peri-implant-20year-mandible]]에서 제시된 20년 장기 단일기관 관찰 결과를 보강하고 더 넓은 증거 기반으로 확장한다.
  - ▸ 출발(`fathi-2025-keratinized-mucosa-implant-health-umbrella-review`) 한줄: 10개 SR/MA(7,139명) 우산 리뷰: 각화점막 폭경(KMW) ≥2 mm이 임플란트 주위 염증·치태·점막퇴축·주위염 감소(부재 시 OR 2.78)와 일관되게 연관; 각화점막 증대는 FGG가 최우선이나 XCM도 심미 부위에서 대안 가능.
  - ▸ 대상(`roccuzzo-2025-keratinized-mucosa-peri-implant-20year-mandible`) 한줄: 20년 전향적 코호트(n=64, 하악 구치부 조직수준 SLA 임플란트)에서 각화점막 없는 임플란트의 임플란트주위염 발생률은 25%(각화점막 있는 군 4.2%, OR 6.67)이고 연조직 열개 발생률은 100%였으며, 유지치료 중 시행한 유리치은이식(FGG)은 각화점막이 처음부터 있던 군에 상응하는 보호 효과를 20년간 유지했다.


### interdental-cleaning

- `jung-2025-flossing-performance-plaque-removal`  —[counterpoint · 반대 논점]→  **`min-2024-brushing-flossing-mouthrinsing-plaque-microbiota`**
  - **근거 문장**: A common defense of flossing's weak trial record is that participants simply floss badly — so "proper technique" should rescue efficacy. This study tests that assumption head-on by measuring whether instruction-improved flossing technique actually removes more plaque, directly extending the flossing-questioned theme in [[interdental-cleaning/min-2024-brushing-flossing-mouthrinsing-plaque-microbiot
  - ▸ 출발(`jung-2025-flossing-performance-plaque-removal`) 한줄: 전향적 단일 코호트 전후 중재연구(n=37, 젊은 성인): 동영상 교육으로 치실 술식(FPS 2.0→2.83, p<.001)은 향상됐으나 치태 제거량은 개선되지 않았고(PSPI 감소 0.17 vs 0.21, p=.112) 술식 숙련도와도 무관 — 올바른 치실 사용조차 치간 치태를 의미 있게 줄이지 못한다.
  - ▸ 대상(`min-2024-brushing-flossing-mouthrinsing-plaque-microbiota`) 한줄: 12주 평행군 RCT (치은염 256명, 5군)에서 샷건 메타게놈 정량분석 결과, 치솔질+치실(BF)은 치솔질 단독(B) 대비 치은연상 플라크 미생물군집(Supragingival Plaque Microbiome)에 유의한 차이 없었으나, 에센셜오일 가글(BA·BZ·BFZ)은 다양성(Shannon-Weaver)·종 풍부도·총 세균량을 유의하게 감소시켰고, 치실+가글 병용(BFZ)만이 치은연하(Subgingival)에서 상승효과(Synergy)를 나타냈다.

- `jung-2025-flossing-performance-plaque-removal`  —[counterpoint · 반대 논점]→  **`interdental-cleaning-devices-synthesis`**
  - **근거 문장**: A common defense of flossing's weak trial record is that participants simply floss badly — so "proper technique" should rescue efficacy. This study tests that assumption head-on by measuring whether instruction-improved flossing technique actually removes more plaque, directly extending the flossing-questioned theme in [[interdental-cleaning/min-2024-brushing-flossing-mouthrinsing-plaque-microbiot
  - ▸ 출발(`jung-2025-flossing-performance-plaque-removal`) 한줄: 전향적 단일 코호트 전후 중재연구(n=37, 젊은 성인): 동영상 교육으로 치실 술식(FPS 2.0→2.83, p<.001)은 향상됐으나 치태 제거량은 개선되지 않았고(PSPI 감소 0.17 vs 0.21, p=.112) 술식 숙련도와도 무관 — 올바른 치실 사용조차 치간 치태를 의미 있게 줄이지 못한다.
  - ▸ 대상(`interdental-cleaning-devices-synthesis`) 한줄: 치간 청소도구 8편 종합(+토스픽법 overview) — 치실·치간칫솔·구강세정기/워터픽·나무이쑤시개 비교: **보편적 우승 도구는 없고 순응도가 도구보다 중요**. 치간칫솔이 들어가는 공간이면 1순위(Carrouel 2026 임신치은염 BOP 56%→12%, OR 3.14), 치실은 좁은 접촉 한정(에어플로스·세정기와 동등), 워터픽은 변연출혈·치주염 보조엔 강하나 교정·임플란트 부가는 이점 없음, 나무 이쑤시개는 치간유두 위해로 회피.

- `mohapatra-2024-water-flosser-vs-floss-plaque-sr`  —[counterpoint · 반대 논점]→  **`mancinelli-lyle-2024-water-flosser-vs-interdental-brush-rct`**
  - **근거 문장**: Adds a head-to-head water-flosser-vs-dental-floss SR focused specifically on the *plaque-reduction* endpoint, complementing [[interdental-cleaning/mancinelli-lyle-2024-water-flosser-vs-interdental-brush-rct]] (water flosser vs interdental brush) and providing the general-adult counterpoint to the orthodontic-only [[interdental-cleaning/yiamwattana-2025-oral-irrigator-vs-floss-orthodontic-sr-ma]], 
  - ▸ 출발(`mohapatra-2024-water-flosser-vs-floss-plaque-sr`) 한줄: 성인에서 물치실(water flosser) vs 치실(dental floss)의 치면세균막 감소 효과를 비교한 체계적 문헌고찰(RCT 7편, PRISMA·PROSPERO 등록; 정량 메타분석은 I²=97% 이질성으로 미시행). 7편 중 4편이 물치실 우위(특히 접근 어려운 인접면), 3편은 차이 없음 — GRADE 근거 "moderate".
  - ▸ 대상(`mancinelli-lyle-2024-water-flosser-vs-interdental-brush-rct`) 한줄: RCT(단일맹검 평행, n=78 중등도 치은염 청년, 사분악당 ≥4 치간칫솔 진입공간): 물세정기(WF, n=40) vs 치간칫솔(IDB, n=38)을 수동칫솔질 보조로 4주 비교 — 두 기기 모두 BOMP/BOPP 감소(p=0.000)했으나, WF가 변연치은 건강(전체부위 BOMP p=0.003, BOPP p=0.030; 치간 BOMP p=0.019이나 치간 BOPP는 NS p=0.219)에서 유의하게 더 효과적이었고, 치은마모(GAS)는 군간 차이가 없었다.


### local-anesthesia

- `ramanathan-2023-efficacy-reliability-single-tooth-anesthesia`  —[대비되는 · 대비]→  **`malamed-2011-mandibular-nerve-block-passe`**
  - **근거 문장**: 바늘없는/압력제어 침윤마취기(computer-controlled delivery system) 관련 질의 맥락에서, WANDSTA를 이용한 single tooth anesthesia (STA, intra-ligamentary injection)가 매복 제3대구치 외과적 발치에서 전통적 IANB의 대안이 될 수 있는지 확인하기 위해 인제스트. IANB 실패기전을 다루는 기존 [[local-anesthesia/malamed-2011-mandibular-nerve-block-passe]], [[local-anesthesia/haas-2011-alternative-mandibular-nerve-block-techniques]]과 대비되는, computer-controlled intraligamentary syste
  - ▸ 출발(`ramanathan-2023-efficacy-reliability-single-tooth-anesthesia`) 한줄: RCT(n=60): 매복 하악 제3대구치 외과적 발치에서 WANDSTA 컴퓨터 제어 단일치아마취(치주인대내 주사, 4% articaine)가 전통적 IANB(4% articaine) 대비 발현 시간이 2.2(±0.25)분 더 빠르고(p<0.05) 술후 통증·개구제한은 낮았으나, 장협신경 추가블록 필요율이 더 높았고(50% vs 23.3%) 발치 시 VAS는 더 높았음.
  - ▸ 대상(`malamed-2011-mandibular-nerve-block-passe`) 한줄: JADA supplement 서론: 표준 IANB의 높은 실패율(예: 측절치 81%) 원인 — 피질골 두께, 연조직 두께로 인한 바늘 편향, 신경 위치 파악의 어려움, 부가신경 지배 — 을 정리하며 대안적 하악마취 기법의 필요성을 제기.

- `ramanathan-2023-efficacy-reliability-single-tooth-anesthesia`  —[대비되는 · 대비]→  **`haas-2011-alternative-mandibular-nerve-block-techniques`**
  - **근거 문장**: 바늘없는/압력제어 침윤마취기(computer-controlled delivery system) 관련 질의 맥락에서, WANDSTA를 이용한 single tooth anesthesia (STA, intra-ligamentary injection)가 매복 제3대구치 외과적 발치에서 전통적 IANB의 대안이 될 수 있는지 확인하기 위해 인제스트. IANB 실패기전을 다루는 기존 [[local-anesthesia/malamed-2011-mandibular-nerve-block-passe]], [[local-anesthesia/haas-2011-alternative-mandibular-nerve-block-techniques]]과 대비되는, computer-controlled intraligamentary syste
  - ▸ 출발(`ramanathan-2023-efficacy-reliability-single-tooth-anesthesia`) 한줄: RCT(n=60): 매복 하악 제3대구치 외과적 발치에서 WANDSTA 컴퓨터 제어 단일치아마취(치주인대내 주사, 4% articaine)가 전통적 IANB(4% articaine) 대비 발현 시간이 2.2(±0.25)분 더 빠르고(p<0.05) 술후 통증·개구제한은 낮았으나, 장협신경 추가블록 필요율이 더 높았고(50% vs 23.3%) 발치 시 VAS는 더 높았음.
  - ▸ 대상(`haas-2011-alternative-mandibular-nerve-block-techniques`) 한줄: 리뷰: Gow-Gates 하악신경차단(개구위, 하악과두경 근처·정원공을 나온 삼차신경 부근에 마취제 침착)과 Akinosi-Vazirani 폐구위 차단(익돌하악강을 마취제로 채움)은 표준 IANB의 신뢰할 만한 대안이며, 해부학적 변이·부가신경 지배로 IANB 실패 이력이 있는 환자에 특히 유용하다.


### nccl

- `worawongvasu-2021-nccl-sem-characterization`  —[contradict · 반박·충돌]→  **`nascimento-2016-abfraction-etiology-diagnosis-treatment`**
  - **근거 문장**: - [[nccl/nascimento-2016-abfraction-etiology-diagnosis-treatment]] — contradicts (offers ultrastructural support where Nascimento calls abfraction unproven)
  - ▸ 출발(`worawongvasu-2021-nccl-sem-characterization`) 한줄: NCCL 소구치 10개 SEM 연구 — 4/10에서 abfraction 지지 microfracture, 전체에서 abrasion/erosion 흔적을 관찰해 다인성 병인을 뒷받침.
  - ▸ 대상(`nascimento-2016-abfraction-etiology-diagnosis-treatment`) 한줄: Abfraction 이론 미입증, 무증상 NCCL은 진행 예방 목적의 수복·교합조정 대신 6개월 이상 monitoring하라고 주장한 review.


### occlusion

- `kiliaridis-2000-vertical-position-rotation-tipping-molars`  —[refut · 반증]→  **`unopposed-tooth-overeruption-overview`**
  - **근거 문장**: Foundational evidence for the qualifier that **not every unopposed tooth overerupts** — directly tests and refutes the long-held "every tooth without an antagonist overerupts" belief, supplying the "~18% show no overeruption" non-eruptor figure used in [[wiki/overviews/unopposed-tooth-overeruption-overview]]. Reinforces [[wiki/occlusion/livas-2016-fixed-retention-unopposed-molar-overeruption]] by 
  - ▸ 출발(`kiliaridis-2000-vertical-position-rotation-tipping-molars`) 한줄: 단면 인체 연구 (53명, 10년 이상 대합치 없는 대구치 84개): 18%는 정출 징후가 전혀 없었고 중등도-중증 정출(≥2 mm)은 24%뿐 — 대합치 없는 모든 치아가 정출하는 것은 아니다.
  - ▸ 대상(`unopposed-tooth-overeruption-overview`) 한줄: 대합치 없는 치아 정출 종합: 후방 치아의 ~83%가 정출(약 9개월에 평균 0.43 mm, 대부분 1 mm 미만, 초기 최대, 수직+경사+회전의 3D 움직임)하나 ~18%는 전혀 안 움직임; 정출은 PDL·치조골 매개라 치수 생활력과 무관(엔도치 vs 생활치 차이 근거 없음); 고정 retention도 부분접촉 대비 효과 없어 저위험치는 모니터링이 방어 가능한 기본값이며, 젊은 나이·상악·완전무대합·치주염·발치 직후가 고위험 프로파일이다.

- `kiliaridis-2000-vertical-position-rotation-tipping-molars`  —[refut · 반증]→  **`livas-2016-fixed-retention-unopposed-molar-overeruption`**
  - **근거 문장**: Foundational evidence for the qualifier that **not every unopposed tooth overerupts** — directly tests and refutes the long-held "every tooth without an antagonist overerupts" belief, supplying the "~18% show no overeruption" non-eruptor figure used in [[wiki/overviews/unopposed-tooth-overeruption-overview]]. Reinforces [[wiki/occlusion/livas-2016-fixed-retention-unopposed-molar-overeruption]] by 
  - ▸ 출발(`kiliaridis-2000-vertical-position-rotation-tipping-molars`) 한줄: 단면 인체 연구 (53명, 10년 이상 대합치 없는 대구치 84개): 18%는 정출 징후가 전혀 없었고 중등도-중증 정출(≥2 mm)은 24%뿐 — 대합치 없는 모든 치아가 정출하는 것은 아니다.
  - ▸ 대상(`livas-2016-fixed-retention-unopposed-molar-overeruption`) 한줄: 후향적 파노라마 연구(Class II 1류 65명): 고정 sectional wire로 잡아둔 대합치 없는 하악 2대구치는 부분접촉 비고정 대조군과 비교해 통계적으로 유의한 정출이 없었고, 양쪽 모두 약 0.1mm(임상적으로 무의미)만 이동 — 부분 교합접촉도 고정 retainer만큼 정출을 억제했다.

- `bhambhani-2020-choosing-denture-occlusion-systematic-review`  —[대비되는 · 대비]→  **`velasquez-2022-occlusal-analysis-natural-dentition-sr`**
  - **근거 문장**: 신설 occlusion 카테고리의 가철성 보철(denture occlusion) 축. [[occlusion/velasquez-2022-occlusal-analysis-natural-dentition-sr]](자연치)와 대비되는 무치악 교합 설계 근거.
  - ▸ 출발(`bhambhani-2020-choosing-denture-occlusion-systematic-review`) 한줄: 총의치 교합양식(balanced·lingualized·monoplane) 선택을 비교한 SR; 단일 우월 양식은 없고 치조제 형태·신경근 조절·환자 요인에 따라 결정.
  - ▸ 대상(`velasquez-2022-occlusal-analysis-natural-dentition-sr`) 한줄: SR(10편) - 디지털 교합분석이 교합지(주관적)보다 객관적; 교합외상이 치아 민감·TMD와 연관; 최대 접촉력은 비기능 교두에서(48%).


### oral-surgery

- `derbishi-2026-coronectomy-versus-total-extraction-third`  —[overturn · 결론 뒤집음]→  **`cervera-espert-2016-coronectomy-mandibular-third-molar-sr`**
  - **근거 문장**: [[wiki/oral-surgery/cervera-espert-2016-coronectomy-mandibular-third-molar-sr]] established the IAN-protective effect but predates modern meta-analytic rigor (Peto OR for rare events, GRADE, trial sequential analysis). This 2026 SR+MA reinforces the anchor with a conclusive effect estimate (Peto OR 0.23 for IAN injury, TSA-confirmed) and modern certainty grading, strengthening rather than overturn
  - ▸ 출발(`derbishi-2026-coronectomy-versus-total-extraction-third`) 한줄: SR+MA (8편 — RCT 3 + 코호트 5, 1488치): 치관절제가 발치 대비 하치조신경 손상 감소 (Peto OR 0.23, 95% CI 0.13–0.39, p<0.0001, TSA 확정), 건성치조염·감염 차이 없음, 치근 회수 재수술률 1.2%.
  - ▸ 대상(`cervera-espert-2016-coronectomy-mandibular-third-molar-sr`) 한줄: SR+MA (12편): 관상절제술은 완전 발치 대비 하치조신경 감각 손실·건성발치창 유의하게 감소 — 치근편 평균 2년 내 2mm 이동, 동통·감염 차이 없음.


### orthodontics/clear-aligner

- `huang-2026-clear-aligner-mandibular-advancement-vs-functional-class-ii-sr-ma`  —[overturn · 결론 뒤집음]→  **`yu-2023-mandibular-advancement-aligner-vs-functional-class-ii-sr-ma`**
  - **근거 문장**: This 2026 SR+MA is the larger, newer counterpart to [[wiki/orthodontics/clear-aligner/yu-2023-mandibular-advancement-aligner-vs-functional-class-ii-sr-ma]] on the identical CAMA-vs-functional-appliance Class II question. Both independently conclude comparable skeletal effect plus superior lower-incisor torque control with CAMA, so it **reinforces** (does not overturn) Yu, and adds a Herbst-specifi
  - ▸ 출발(`huang-2026-clear-aligner-mandibular-advancement-vs-functional-class-ii-sr-ma`) 한줄: 9편(RCT 1 + NRSI 8, n=465) SR+MA: 투명교정 하악전방유도(CAMA)의 골격효과는 트윈블록·Herbst와 동등(SNA/SNB/ANB·수직 모두 NS). overjet 감소는 CAMA가 약간 우위(MD -0.46 mm, 임상적으로 미미), 하악전치 순측경사는 CAMA가 유의하게 적음(IMPA MD -0.90°, P=0.0002). 근거수준 낮음(대부분 후향).
  - ▸ 대상(`yu-2023-mandibular-advancement-aligner-vs-functional-class-ii-sr-ma`) 한줄: SR+MA(대조연구 9편, n=283): MA 투명교정장치와 전통적 기능성장치의 골격·치성 Class II 교정은 유사(SNA/SNB/ANB/Go-Pog/U1-SN/overjet 무의미). aligner가 하악 전치 순측경사를 더 잘 억제(1.94° 적음)하나 하악지 성장(Co-Go)은 1.10 mm 적음 — 성장 의존 교정에서 한계.


### overviews

- `osseodensification-clinical-applications`  —[대비되는 · 대비]→  **`changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift`**
  - **근거 문장**: - [[sinus-lift/transcrestal/changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift]] — **(retracted/철회됨 — 인용 금지)** CW-OD 버(HaeNaem) 경치조 간접 거상 전향적 단일군 (n=12, RCBH 6–8mm, 무이식, 4mo CBCT 4방향 골고↑): Densah CCW 패러다임과 대비되는 유일한 CW OD 임상 데이터였으나 이후 철회됨 [근거 무효]
  - ▸ 출발(`osseodensification-clinical-applications`) 한줄: 골밀도화 (Osseodensification, OD)는 반시계회전 (Counterclockwise, CCW) 800–1500 rpm으로 Densahbur가 자가골을 압축·자가이식하여 4개 임상 시나리오 (상악동저 보강·좁은 ridge·저밀도골 D3–D4·즉시식립)에 적용된다 — 삽입토크 (Insertion Torque, IT) 일관되게 상승 [근거강함], 임플란트 안정성 지수 (Implant Stability Quotient, ISQ)는 **저밀도골 인체 SR+MA(mohammadi 2025)에서
  - ▸ 대상(`changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift`) 한줄: 전향적 단일군 연구(n=12, 잔존 골고 6–8mm): HaeNaem Zero Bone Loss CW-OD 버 키트로 무이식 경치조골 간접 거상 동시 임플란트 식립 후 4개월 CBCT에서 근심·원심·협측·구개측 4개 방향 모두 유의한 골 높이 증가(p<0.01).

- `drug-analgesics-postop-pain-overview`  —[contradict · 반박·충돌]→  **`tamgadge-2025-preoperative-dexamethasone-third-molar-pain-swelling-trismus`**
  - **근거 문장**: - [[drug/analgesics/tamgadge-2025-preoperative-dexamethasone-third-molar-pain-swelling-trismus]] — contradicts/extends: NSAID-preemptive 무효(Costa)와 달리 술전 dexamethasone은 third molar에 유효 (rct, 2025)
  - ▸ 출발(`drug-analgesics-postop-pain-overview`) 한줄: 치과 술후 통증 1차 선택은 **Ibuprofen 400mg + Acetaminophen 1000mg 병용** — Network MA에서 가장 낮은 NNT (~1.5). Opioid는 비-opioid 대비 우월하지 않으며 부작용·중독 위험 → 회피. Preemptive NSAID는 third molar에선 약하나 치주·임플란트엔 효과 있고, 술전 dexamethasone은 third molar에 명확히 유효. 근관치료는 시간대 의존 — Diclofenac+APAP·Ketorolac이 6–8h 최강
  - ▸ 대상(`tamgadge-2025-preoperative-dexamethasone-third-molar-pain-swelling-trismus`) 한줄: split-mouth 단일맹검 위약대조 시험 (n=60, 양측 매복 하악 사랑니): 술전 dexamethasone 4 mg 근육주사 1회가 위약 대비 술후 통증(2일 1.2 vs 2.3, 7일 0.4 vs 1.6, p<0.001), 개구량(3.5 vs 2.7 cm, p<0.001)을 유의하게 개선하고 7일째 부종도 줄였으며(2.1 vs 2.8 cm, p=0.04) 이상반응은 없었다.

- `sinus-lift-lateral-2026-synthesis`  —[contradict · 반박·충돌]→  **`akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height`**
  - **근거 문장**: - [[sinus-lift/lateral/akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height]] — lower residual ridge height correlates with greater MT (contradicts Maska null finding)
  - ▸ 출발(`sinus-lift-lateral-2026-synthesis`) 한줄: 측방창 (Lateral Window) 상악동거상술 (Sinus Floor Elevation, SFE)에서 슈나이더 막 (Schneiderian Membrane) 천공 (Sinus Membrane Perforation, SMP)과 부비동염 (Sinusitis) 예방·관리를 다룬 34편에 이식재 선택 및 PRF (Platelet-Rich Fibrin) 보조 근거 3편을 추가해 총 37편으로 확장한 종합 페이지 — L-PRF·A-PRF 보조 시 신생골 +7~11% 유의 증가, BCP가 DBBM 대비 신
  - ▸ 대상(`akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height`) 한줄: 임플란트 후보 141명 CBCT(240 상악동): 잔존 치조제 높이가 낮을수록 상악동 점막비후 정도가 유의하게 크며, >3mm를 병적 기준으로 사용.

- `bone-regeneration-socket-biology-and-arp-critique`  —[counterpoint · 반대 논점]→  **`bone-regeneration-protocol-ladder`**
  - **근거 문장**: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 한줄: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.
  - ▸ 대상(`bone-regeneration-protocol-ladder`) 한줄: 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의사결정 ladder. 자연 치유 dimensional change · graft material 비교 · membrane/flap 조합 · soft tissue seal 4축. EFP/AO consensus + Cochrane review spine.

- `bone-regeneration-socket-biology-and-arp-critique`  —[반박 · 반박]→  **`araujo-2009-ridge-alterations-flap-vs-flapless`**
  - **근거 문장**: | [[bone-regeneration/ridge-preservation/araujo-2009-ridge-alterations-flap-vs-flapless]] | animal (dog, split-mouth) | **"Flapless = ridge 보존" myth 반박**. flap 유무가 ridge 흡수 크기를 의미있게 바꾸지 않음. Flapless 의 가치는 vascular preservation 가설 아닌 술자·환자 부담 감소 |
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 한줄: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.
  - ▸ 대상(`araujo-2009-ridge-alterations-flap-vs-flapless`) 한줄: 개 5마리 split-mouth(전층 판막 vs flapless) 6개월 조직학 비교 — 두 군 모두 발치 후 ridge resorption 발생, flap 거상 여부가 흡수량을 의미 있게 바꾸지 않음 → "flapless 발치만으로 ridge 보존" 주장 반박.

- `bone-regeneration-socket-biology-and-arp-critique`  —[counterpoint · 반대 논점]→  **`adams-2022-clinical-evidence-alveolar-ridge-preservation`**
  - **근거 문장**: | [[bone-regeneration/ridge-preservation/adams-2022-clinical-evidence-alveolar-ridge-preservation]] | narrative-review + case (BDJ) | **수정주의 counterpoint**. 5-13y 후 xenograft 만성 섬유 포함·peri-implantitis 양상 case. "통계적 dimensional preservation" ≠ "long-term patient benefit". 상업적 압력 (BSM 시장 ARP 29%) 환기 |
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 한줄: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.
  - ▸ 대상(`adams-2022-clinical-evidence-alveolar-ridge-preservation`) 한줄: BDJ 게재 narrative review + 2개 case report로 ARP의 통계적 효과가 임상적 환자 이득으로 직결되지 않음을 지적, 5~13년 후 xenograft 만성 실패(섬유 포함·peri-implantitis 양상) 사례를 제시하며 ARP의 무차별 적용에 회의를 표함.

- `suture-wound-closure-decision-ladder`  —[상충 · 상충]→  **`kumar-2022-suture-versus-sutureless-third-molar-impactions`**
  - **근거 문장**: - [[suture-wound-closure/kumar-2022-suture-versus-sutureless-third-molar-impactions]] — sutureless 초기 morbidity 우월 (takadoum과 부분 상충)
  - ▸ 출발(`suture-wound-closure-decision-ladder`) 한줄: 봉합·창상폐쇄 결정은 **창상 장력(wound tension)** 이라는 단일 상류 변수로 갈린다 — 저장력 발치와에서는 술식이 결과에 무관하고 sutureless가 초기 morbidity만 약간 줄이지만(치주치유 차이 없음), 고장력 골증대/GBR 부위에서는 폐쇄 자체가 성패를 결정한다(설측 관상전진피판으로 mesh 노출 83.3%→0%, 골막이완절개 +5.5 mm 전진, 노출 시 골증대량 약 1/6). RCT 7편·SR 1편·in-vitro 4편 종합. [근거강함] ---
  - ▸ 대상(`kumar-2022-suture-versus-sutureless-third-molar-impactions`) 한줄: 작은 변형 Szmyd V자형 판막을 사용한 하악 매복 사랑니 발치에서 봉합 대 무봉합을 비교한 무작위배정 임상시험(n=50, 군당 25명). 무봉합이 초기 통증·부종·개구장애를 유의하게 줄였고(p<0.001), 치주 후유증과 건성발치와에는 차이가 없었다.

- `implant-occlusion-loading-biomechanics-overview`  —[뒤집 · 뒤집음]→  **`mojaver-2025-occlusal-overload-peri-implant-health-sr`**
  - **근거 문장**: 4. **교합 과부하와 임플란트주위 골소실의 연관은 시사되나 근거 질이 낮다(정량 교합분석 표준화 부재).** — Di Fiore 2022 SR(7편). [합의수준/미검증] 더 넓은 근거 풀로 본 Mojaver 2025 SR(160→80편, narrative, 메타분석 없음)도 같은 방향을 재확인하면서 수치를 붙인다: 교합인자 변연골소실 ~0.65–1.20 mm, 외상력 시 골수준 변화 1.0–3.0 mm, 임플란트주위염 발생률 20–50%. 핵심 기여는 **dual-pathway 모델** — 기계적 과부하가 단독으로 작용하기보다 biofilm 유발 염증과 **상승작용(synergy)**해 임플란트주위 조직 붕괴를 가속한다는 것(Mattheos: 염증 없는 dog 모델에서는 변연골소실 없이 골유착 상실; N
  - ▸ 출발(`implant-occlusion-loading-biomechanics-overview`) 한줄: 교합 클러스터를 임플란트 관점으로 종합. 골유착 임플란트는 치주인대가 없어 교합력이 완충도 감지도 안 되므로, 설계 목표는 하중 최소화·분산이다. 임상·FEA 근거는 4점으로 수렴 — 임플란트 교합접촉은 6-12개월 내 변동(대개 상대적 저위교합 방향); "약교합(light occlusion)"은 힘을 낮추나 시간이 지나며 불안정; 교합양식·보철 구성(캔틸레버·치아-임플란트 연결·full-arch)이 임플란트주위 응력을 좌우; 체어사이드 레버는 단일 이상적 양식이 아니라 정기 교합 재점검(T-Sc
  - ▸ 대상(`mojaver-2025-occlusal-overload-peri-implant-health-sr`) 한줄: 서술적 SR(160→80편, 메타분석 없음) — 교합 과부하·외상이 임플란트 변연골소실(0.65–3.0 mm)·임플란트주위염 발생률(20–50%)과 연관되며, 기계적 과부하 × biofilm 염증 이중 경로가 동인.

- `computerized-needle-free-anesthesia-delivery-overview`  —[상반 · 상반]→  **`garret-bernardin-2017-pain-experience-behavior-management-pediatric`**
  - **근거 문장**: - [[local-anesthesia/garret-bernardin-2017-pain-experience-behavior-management-pediatric]] — 소아 맥락에서의 상반된 결과
  - ▸ 출발(`computerized-needle-free-anesthesia-delivery-overview`) 한줄: 컴퓨터제어(CCLAD/The Wand/STA)·압력조절·바늘없는 마취 전달장치 9편을 종합하면, 엄격한 맹검 RCT일수록 주사통증 자체의 우위는 재현되지 않지만 공포·불안 감소, 보충마취 회피, 소아 협조도 개선은 일관되게 관찰된다 — 임상적 가치는 "덜 아프게"가 아니라 "덜 무섭고 덜 재주사하게"에 있으며, 근거 수준은 강한 RCT부터 비맹검 전후비교 코호트까지 폭넓게 갈린다.
  - ▸ 대상(`garret-bernardin-2017-pain-experience-behavior-management-pediatric`) 한줄: 관찰형 crossover split-mouth 연구(소아·청소년 67명, 7-15세): Wand STA 컴퓨터 제어 마취기가 전통 syringe 대비 통증 VAS 유의하게 낮음(-1.09점, P=0.0003), 심박수 증가폭 작음(-3.4bpm, P=0.028), 이완된 행동(Venham=0) 더 빈번(P=0.019), 만족도 더 높음(P=0.0003).

- `abutment-emergence-profile-peri-implant-tissue-overview`  —[contradict · 반박·충돌]→  **`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`**
  - **근거 문장**: | [[implants/canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma]] | SR+MA | 6 pooled / 182 implants | (a) surface | No short-term difference in PI/BoP/PD (P=0.091/0.099/0.488); long-term contradictory |
  - ▸ 출발(`abutment-emergence-profile-peri-implant-tissue-overview`) 한줄: 10편 종합(SR+MA 1·SR 2·scoping review 1·RCT 3·후향 1·전임상 동물 2): 임플란트주위 조직 안정성의 지배 인자는 출현윤곽의 **형태·각도** — 전치부 볼록은 오목 대비 퇴축 위험 ~13배(Siegenthaler 2022), 구치부 W/H 기반 낮은 출현각도(~32°)는 퇴축을 절반으로(Wang 2022), 개 모델 RCT는 각도→골소실/봉쇄실패 용량반응을 인과적으로 확립(80°가 20°의 ~4배 MBL, ≥60°에서 접합상피 붕괴; 각도 <40° 유지: Strau
  - ▸ 대상(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 한줄: 체계적 문헌고찰 + 메타분석 (10편 포함, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 표면은 단기적으로 플라크 지수·탐침 시 출혈(BoP)·탐침 깊이(PD)에서 대조군과 유의한 차이가 없었고, 장기(5~6년) 연구는 표면 처리 기법에 따라 상반된 결과를 보였다.

- `watanabe-toothpick-method-toothbrushing-synthesis`  —[counterpoint · 반대 논점]→  **`el-haddad-2026-toothpick-use-interdental-papilla-loss-cross-sectional`**
  - **근거 문장**: - [[interdental-cleaning/el-haddad-2026-toothpick-use-interdental-papilla-loss-cross-sectional]] — wooden-toothpick harm (papilla loss) — naming counterpoint
  - ▸ 출발(`watanabe-toothpick-method-toothbrushing-synthesis`) 한줄: 와타나베 이쑤시개법(TPM, 칫솔질법) 위키 7편(1995–2026) 종합 — 2열모 칫솔로 치간을 닦는 기법으로 인접면 플라그 제거 + 치은 치유 자극(기저세포 증식 약 2.5배)의 이중 기전. 원전 RCT는 TPM>Bass(Morita 1998), 당뇨 치주염·임플란트 주위 점막염으로 효과 확장(단, 기계적 단독은 세균 재증식→항균제 병용 필요), 지도 빈도가 중요하나 기법 비교근거는 약함(Rajwani SR). *목재* 이쑤시개(치간도구)는 반대로 치간유두 소실·블랙트라이앵글 유발(El Ha
  - ▸ 대상(`el-haddad-2026-toothpick-use-interdental-papilla-loss-cross-sectional`) 한줄: 단면연구(n=69, 20–29세, 87%가 이쑤시개 사용) — 나무 이쑤시개의 습관적 치간 사용은 상악 전치부 치간유두를 유의하게 소실시켜(PPI, P<.05) '블랙트라이앵글'을 유발하며, 수직(상하) 기법·하루 3회 초과·3년 초과 사용에서 더 심함. 치조골 수준·접촉면 길이는 무영향 (초록 기반).

- `unopposed-tooth-overeruption-overview`  —[refut · 반증]→  **`kiliaridis-2000-vertical-position-rotation-tipping-molars`**
  - **근거 문장**: - [[occlusion/kiliaridis-2000-vertical-position-rotation-tipping-molars]] — Kiliaridis 2000, cross-sectional (n=53, 84 molars unopposed ≥10 y): **~18% show no overeruption at all**, ~49–58% slight (<2 mm), ~20–24% moderate-to-severe (≥2 mm) — directly refutes "every unopposed tooth over-erupts."
  - ▸ 출발(`unopposed-tooth-overeruption-overview`) 한줄: 대합치 없는 치아 정출 종합: 후방 치아의 ~83%가 정출(약 9개월에 평균 0.43 mm, 대부분 1 mm 미만, 초기 최대, 수직+경사+회전의 3D 움직임)하나 ~18%는 전혀 안 움직임; 정출은 PDL·치조골 매개라 치수 생활력과 무관(엔도치 vs 생활치 차이 근거 없음); 고정 retention도 부분접촉 대비 효과 없어 저위험치는 모니터링이 방어 가능한 기본값이며, 젊은 나이·상악·완전무대합·치주염·발치 직후가 고위험 프로파일이다.
  - ▸ 대상(`kiliaridis-2000-vertical-position-rotation-tipping-molars`) 한줄: 단면 인체 연구 (53명, 10년 이상 대합치 없는 대구치 84개): 18%는 정출 징후가 전혀 없었고 중등도-중증 정출(≥2 mm)은 24%뿐 — 대합치 없는 모든 치아가 정출하는 것은 아니다.

- `implant-spacing-proximity-crestal-bone-overview`  —[overturn · 결론 뒤집음]→  **`morales-schwarz-2025-1mm-interimplant-distance-10year-case`**
  - **근거 문장**: - [[implants/morales-schwarz-2025-1mm-interimplant-distance-10year-case]] — 10-year case report (n=1) + literature/animal review showing a 1 mm IID maintainable with modern implant design; provides the "exception" that qualifies — but does not overturn — Tarnow's rule.
  - ▸ 출발(`implant-spacing-proximity-crestal-bone-overview`) 한줄: 4편 종합: 치간 치조정골은 수평 간격이 지배 — 임플란트간 거리 ≥3 mm (Tarnow 2000; 현대 디자인은 1–2 mm까지 가능 — Morales Schwarz 2025, n=1)와 임플란트-치근 거리 ≥1.5 mm (Joshi 2025 SR+MA; Ng 2018)가 치조정 골소실·주위염·인접치 치수손상을 최소화한다.
  - ▸ 대상(`morales-schwarz-2025-1mm-interimplant-distance-10year-case`) 한줄: 케이스보고+문헌고찰 (IID=1 mm, 플랫폼 스위칭 BL 임플란트, 10년): 치조정 IAC보다 1.40 mm 상방 골 유지; 1 mm IID 동물실험 2편도 넓은 거리 대비 골소실 없음; 3 mm 룰은 구식 외부 헥스 기반.

- `tmd-management-evidence-ladder`  —[반박 · 반박]→  **`valenzuela-fuenzalida-2026-arthrocentesis-vs-other-modalities-tmd-sr-ma`**
  - **근거 문장**: - [[tmj/valenzuela-fuenzalida-2026-arthrocentesis-vs-other-modalities-tmd-sr-ma]] — 비교군 확장 시 관절천자 우월성 없음; 기존 IJOMS 2023(+1.12mm)의 modest-benefit 결론을 재맥락화(축 5 갱신·일부 반박).
  - ▸ 출발(`tmd-management-evidence-ladder`) 한줄: TMD 관리 SR+MA·가이드라인 27편 + 편측저작·과두형태·이명 5편 통합(2026-06-15 업데이트). BMJ NMA 2023 (233 RCT, 59 개입): CBT+운동·하악 가동화 최우수 → 약물 낮은 근거 → arthrocentesis 보존 실패 시. 근육형 TMD 특화·QoL 정량화·MAD/VD 축 신설. 편측저작 → 과두 위치·형태 변화·이명(동측) 상관 5편 추가(축 10).
  - ▸ 대상(`valenzuela-fuenzalida-2026-arthrocentesis-vs-other-modalities-tmd-sr-ma`) 한줄: 32개 RCT(1247명) SR+MA: 관절천자(Arthrocentesis)는 다른 치료법(보존·관절내주사·관절경 등) 대비 통증(VAS) 차이 없고(MD −0.25, p=0.55), 최대개구량(MMO)·최대절치개구(MIO)는 오히려 비교군 우세 — 우월성 미입증, 근거확실성 매우 낮음, 단계적 치료의 보조옵션으로만 해석.

- `nccl-etiology-diagnosis-management-overview`  —[반박 · 반박]→  **`dioguardi-2024-abfraction-theory-controversy-scoping-review`**
  - **근거 문장**: | [[nccl/dioguardi-2024-abfraction-theory-controversy-scoping-review]] | Scoping review (PRISMA-ScR) | 6편 | 교합부하의 abfraction 역할 확정·반박 모두 불가; Duangthip 재비판 | sr |
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 한줄: NCCL은 stress·friction·biocorrosion 다인성이며 abfraction 단독원인설은 미입증, 무증상은 monitoring이 원칙, 수복 시 유지력은 접착·산부식 단계에 좌우(selective enamel etching 유리, self-adhesive flowable 실패).
  - ▸ 대상(`dioguardi-2024-abfraction-theory-controversy-scoping-review`) 한줄: PRISMA-ScR scoping review(1449→6편) — 교합부하의 abfraction 원인 역할 확정·반박 모두 불가, 전향 종단연구 필요.

- `topical-anesthetic-injection-pain-overview`  —[상충 · 상충]→  **`karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb`**
  - **근거 문장**: - [[local-anesthesia/karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb]] — 제제 비교 (차이 없음, 상충점)
  - ▸ 출발(`topical-anesthetic-injection-pain-overview`) 한줄: 표면마취제는 위약 대비 needle·주사 통증을 확실히 줄이지만, 제제 간(lidocaine·benzocaine·EMLA) 직접비교 차이는 작고 비일관적이다 — 어떤 약물이냐보다 전달제형·농도·도포술기가 더 결정적이며, 표면마취가 통증강도에서 주사마취를 완전히 대체하진 못해도 SRP 같은 맥락에선 덜 침습적 대안으로 유효하다.
  - ▸ 대상(`karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb`) 한줄: 삼중맹검 RCT(소아 45명, 6-10세): IANB에서 8% lidocaine 겔이 20% benzocaine·5% EMLA보다 우월하지 않음 — FLACC·Wong-Baker FACES·맥박 모두 유의차 없음.


### periodontics

- `fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr`  —[contradict · 반박·충돌]→  **`heo-2022-omega-3-fatty-acids-periodontitis-ma`**
  - **근거 문장**: CoQ10 ("잇몸 영양제") is one of the most heavily marketed periodontal supplements, yet the wiki held **zero pages** on it. This Fernandez 2025 SR is the cited evidence behind the CoQ10 claim and the most current (search to May 2024), most methodologically careful answer: it **stratifies by administration route**, which is exactly what resolves the controversy — local CoQ10 gel shows no effect on PD/CAL
  - ▸ 출발(`fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr`) 한줄: 10편 RCT 체계적 고찰 — 국소 CoQ10 겔은 효과 없음, 경구 120 mg/일은 12주에 작은 유의 개선(PD −0.41 mm, CAL −0.52 mm). 근거 확실성 very low → 근거기반 권고 불가. 마케팅이 앞서간 영역.
  - ▸ 대상(`heo-2022-omega-3-fatty-acids-periodontitis-ma`) 한줄: 13편 RCT 메타분석 — 오메가-3 지방산(보충제·식이)이 치주염에서 유의한 치주낭 깊이 감소(−0.44 mm), 임상부착수준 획득(−0.51 mm), 출혈 감소(−9.45%)를 보임. 비뚤림 낮고 출판 비뚤림 없음. 단, 효과 크기는 작고 EFP 가이드라인은 반대 권고.

- `farina-2026-pmpr-biofilm-gingivitis-sr-ma`  —[대비되는 · 대비]→  **`lamont-2018-routine-scale-and-polish-periodontal-health`**
  - **근거 문장**: "Oral prophylaxis" 요청의 두 번째 코어 논문. 21st European Workshop on Periodontology(EFP) Working Group 1 SR로, [[periodontics/lamont-2018-routine-scale-and-polish-periodontal-health]](저위험 성인 루틴 프로필락시스 무효)과 대비되는 **established gingivitis 치료 맥락**에서 PMPR의 역할을 규명한다 — OHI가 1차, PMPR은 OHI에 대한 adjunct일 때만 이득. 또한 [[periodontics/cyris-2024-guided-biofilm-therapy-versus-conventional]]·[[overviews/professional-biofilm-
  - ▸ 출발(`farina-2026-pmpr-biofilm-gingivitis-sr-ma`) 한줄: 치태-유발 치은염에서 구강위생교육(OHI)이 1차 치료이고 전문가 기계적 치태제거(PMPR)는 OHI에 더해질 때만 이득(low certainty)을 주며, 에어폴리싱+초음파가 초음파+러버컵 폴리싱과 동등하면서 더 빠르고, 다이오드 레이저는 부가 이득이 없다는 EFP SR+MA(11편).
  - ▸ 대상(`lamont-2018-routine-scale-and-polish-periodontal-health`) 한줄: 중증 치주염이 없는 정기 내원 성인에서 루틴 스케일링·폴리싱(프로필락시스)이 치은염·치주낭 깊이·삶의 질에 2~3년간 거의 차이를 만들지 않는다는 코크란 SR+MA(RCT 2편, 1711명); 치석만 소폭 감소하나 임상적 의미는 불확실.

- `farina-2026-pmpr-biofilm-gingivitis-sr-ma`  —[대비되는 · 대비]→  **`cyris-2024-guided-biofilm-therapy-versus-conventional`**
  - **근거 문장**: "Oral prophylaxis" 요청의 두 번째 코어 논문. 21st European Workshop on Periodontology(EFP) Working Group 1 SR로, [[periodontics/lamont-2018-routine-scale-and-polish-periodontal-health]](저위험 성인 루틴 프로필락시스 무효)과 대비되는 **established gingivitis 치료 맥락**에서 PMPR의 역할을 규명한다 — OHI가 1차, PMPR은 OHI에 대한 adjunct일 때만 이득. 또한 [[periodontics/cyris-2024-guided-biofilm-therapy-versus-conventional]]·[[overviews/professional-biofilm-
  - ▸ 출발(`farina-2026-pmpr-biofilm-gingivitis-sr-ma`) 한줄: 치태-유발 치은염에서 구강위생교육(OHI)이 1차 치료이고 전문가 기계적 치태제거(PMPR)는 OHI에 더해질 때만 이득(low certainty)을 주며, 에어폴리싱+초음파가 초음파+러버컵 폴리싱과 동등하면서 더 빠르고, 다이오드 레이저는 부가 이득이 없다는 EFP SR+MA(11편).
  - ▸ 대상(`cyris-2024-guided-biofilm-therapy-versus-conventional`) 한줄: 분악 RCT (60명, stage III/IV 치주염, 감독하 치대생이 시술): 비외과적 치주치료에서 가이드 바이오필름 치료(GBT, 에리스리톨 에어폴리싱+초음파)와 전통적 SRP(수기 큐렛/소닉+회전연마)의 PPD 감소·포켓 폐쇄 효과는 동등했고, GBT가 사분악당 시술시간만 유의하게 짧았다(30.3 vs 34.6분, p<0.001).

- `farina-2026-pmpr-biofilm-gingivitis-sr-ma`  —[대비되는 · 대비]→  **`professional-biofilm-management-gbt-air-polishing-overview`**
  - **근거 문장**: "Oral prophylaxis" 요청의 두 번째 코어 논문. 21st European Workshop on Periodontology(EFP) Working Group 1 SR로, [[periodontics/lamont-2018-routine-scale-and-polish-periodontal-health]](저위험 성인 루틴 프로필락시스 무효)과 대비되는 **established gingivitis 치료 맥락**에서 PMPR의 역할을 규명한다 — OHI가 1차, PMPR은 OHI에 대한 adjunct일 때만 이득. 또한 [[periodontics/cyris-2024-guided-biofilm-therapy-versus-conventional]]·[[overviews/professional-biofilm-
  - ▸ 출발(`farina-2026-pmpr-biofilm-gingivitis-sr-ma`) 한줄: 치태-유발 치은염에서 구강위생교육(OHI)이 1차 치료이고 전문가 기계적 치태제거(PMPR)는 OHI에 더해질 때만 이득(low certainty)을 주며, 에어폴리싱+초음파가 초음파+러버컵 폴리싱과 동등하면서 더 빠르고, 다이오드 레이저는 부가 이득이 없다는 EFP SR+MA(11편).
  - ▸ 대상(`professional-biofilm-management-gbt-air-polishing-overview`) 한줄: 치아·임플란트 12편(SR 2·RCT 4·in-vitro SR+서술고찰·in-vitro 2·증례 1)을 종합하면, GBT·에어폴리싱은 편안함·시술시간·최소 치질 마모라는 환자 중심 이득은 있으나 PPD·CAL·BoP 같은 단단한 임상지표에서는 전통적 기계적 청결관리(SRP/PMPR)와 **동등할 뿐 우월하지 않다**; 분말은 에리스리톨이 표면 손상이 적어 선호되고, 임플란트에서 보조요법은 추가 이득이 미미하며, 치은연하 에어폴리싱은 드물지만 실재하는 피하기종 위험이 있다.

- `dasilveira-2026-subgingival-irrigation-chemical-agents-nspt-sr-ma`  —[대비되는 · 대비]→  **`khattri-2020-adjunctive-systemic-antimicrobials-non-surgical-treatment`**
  - **근거 문장**: 기존 [[periodontics/ramanauskaite-2020-antiseptics-adjuncts-scaling-root-planing]]가 항균제를 SRP 보조로 다룬 반면, 이 2026 SR+MA는 **약제(PVP-I/CHX/EO/OW/BA)를 치은연하 세척(subgingival irrigation)으로 전달**하는 좁은 시나리오만 16편 RCT로 모아, 어떤 약제·전달법(시린지 vs 초음파)·추적기간에서도 PPD·CAL·BOP에 추가 이득이 없음을 보여 "세척 보조"라는 흔한 임상 습관의 근거 결핍을 정량화한다. [[periodontics/khattri-2020-adjunctive-systemic-antimicrobials-non-surgical-treatment]]의 전신 항균제 논의와 대비되는
  - ▸ 출발(`dasilveira-2026-subgingival-irrigation-chemical-agents-nspt-sr-ma`) 한줄: 16편 RCT(712명) SR+MA — NSPT에 약제(PVP-I·CHX·정유·오존수·붕산) 치은연하 세척을 더해도 물/식염수 대비 PPD(MD 0.01mm)·CAL(MD 0.09mm)·BOP에 추가 이득 없음(근거수준 낮음~매우낮음).
  - ▸ 대상(`khattri-2020-adjunctive-systemic-antimicrobials-non-surgical-treatment`) 한줄: Cochrane 체계적고찰+메타분석(RCT 45편): SRP에 전신 항생제(가장 많이 연구된 조합은 아목시실린+메트로니다졸)를 추가해도 비외과적 치주염 치료에서 CAL·PD·closed pocket·BOP 개선 효과는 모두 매우 낮은 확실성이며 임상적으로 미미하고, 특정 항생제가 더 우수하다는 신뢰할 만한 근거도 없음.

- `periodontal-adjunctive-therapy-probiotics-pdt-overview`  —[counterpoint · 반대 논점]→  **`jungbauer-2026-naocl-hyaluronic-acid-subgingival-reinstrumentation-rct`**
  - **근거 문장**: - [[periodontics/jungbauer-2026-naocl-hyaluronic-acid-subgingival-reinstrumentation-rct]] — "clean and seal" (AA-NaOCl + cross-linked HA) adjunct to SRI in maintenance; positive ~0.5 mm PD / 0.57 mm CAL gain, doubled pocket closure — delivery-mode counterpoint to da Silveira's null irrigation
  - ▸ 출발(`periodontal-adjunctive-therapy-probiotics-pdt-overview`) 한줄: NSPT/SRP 보조요법 2026년 프로바이오틱스·이중광 aPDT RCT를 2017 NMA 벤치마크와 종합: 모든 보조요법의 추가 CAL 이득은 ~0.3 mm에 불과하고, 프로바이오틱스는 BoP와 PPD ≥5 mm 부위를 개선하되 CAL은 미개선, 가정용 이중광 aPDT는 기존 구강위생에 추가적 치태 감소를 제공하며, 아직 우월한 단일 보조요법은 없다.
  - ▸ 대상(`jungbauer-2026-naocl-hyaluronic-acid-subgingival-reinstrumentation-rct`) 한줄: 단일기관 RCT (환자 42명, 군당 21명) — 유지치료 단계 잔존 포켓의 재기구조작(SRI)에 아미노산-차아염소산나트륨(AA-NaOCl) + 가교 히알루론산(xHA, "clean and seal")을 보조로 추가하니 6개월에 PD 0.50 mm 추가 감소·CAL 0.57 mm 추가 회복, 포켓 폐쇄율 88.1% 대 38.1%, 8개 중 5개 치주병원균 유의 감소했고, 깊은 포켓일수록 효과가 더 컸다.


### post-and-core

- `mously-2024-anterior-endocrowns-alternative-core-crown`  —[counterpoint · 반대 논점]→  **`alenezi-2024-endodontically-treated-teeth-post-placement-survival`**
  - **근거 문장**: Brings the modern minimally-invasive alternative (endocrown) into the new `post-and-core` category, directly framing when NOT to use a post — the conservative counterpoint to the post-necessity finding in [[post-and-core/alenezi-2024-endodontically-treated-teeth-post-placement-survival]]. Full-text PMC ingest gives detailed material/ferrule/extension-depth decision factors and connects to fracture
  - ▸ 출발(`mously-2024-anterior-endocrowns-alternative-core-crown`) 한줄: 체계적 문헌고찰(in-vitro/FEA 12편, 메타분석 없음·서술적): 전치부 근관치료치아에서 엔도크라운이 포스트-코어-크라운 대비 동등하거나 더 높은 파절저항과 더 수리 가능한 실패양상을 보였고, 페룰이 피로저항의 결정적 인자, 리튬디실리케이트가 최적 재료였음.
  - ▸ 대상(`alenezi-2024-endodontically-treated-teeth-post-placement-survival`) 한줄: SR+MA(정량분석 임상연구 17편, 환자 7,278명·근관치료치아 7,330개): 포스트 식립이 무포스트 대비 근관치료치아 생존율을 유의하게 향상시켰음(P<0.001).

- `mously-2024-anterior-endocrowns-alternative-core-crown`  —[counterpoint · 반대 논점]→  **`susita-2026-comparative-analysis-stress-distribution-teeth`**
  - **근거 문장**: Brings the modern minimally-invasive alternative (endocrown) into the new `post-and-core` category, directly framing when NOT to use a post — the conservative counterpoint to the post-necessity finding in [[post-and-core/alenezi-2024-endodontically-treated-teeth-post-placement-survival]]. Full-text PMC ingest gives detailed material/ferrule/extension-depth decision factors and connects to fracture
  - ▸ 출발(`mously-2024-anterior-endocrowns-alternative-core-crown`) 한줄: 체계적 문헌고찰(in-vitro/FEA 12편, 메타분석 없음·서술적): 전치부 근관치료치아에서 엔도크라운이 포스트-코어-크라운 대비 동등하거나 더 높은 파절저항과 더 수리 가능한 실패양상을 보였고, 페룰이 피로저항의 결정적 인자, 리튬디실리케이트가 최적 재료였음.
  - ▸ 대상(`susita-2026-comparative-analysis-stress-distribution-teeth`) 한줄: 3D FEA — 상악 중절치 근관치료 후 유리섬유·SFRC·Ribbond 포스트 응력 비교; SFRC 포스트가 내부 응력 가장 낮고(5.22 MPa) 상아질 친화적 응력 분포 보임.


### prosthetic-materials

- `aalaei-2017-segmented-nonsegmented-abutment-fea`  —[반론 · 반론]→  **`velez-2020-implant-connection-abutment-design-screw`**
  - **근거 문장**: 세그먼트형(분리형) 어버트먼트와 비세그먼트형(일체형) 어버트먼트가 나사 유지형 보철물의 골 응력 분포에 미치는 영향을 FEA로 비교한 드문 연구. 기존 [[prosthetic-materials/velez-2020-implant-connection-abutment-design-screw]]가 임플란트 연결부·어버트먼트 디자인 일반론을 다루지만, 분절형 vs 비분절형 나사 어버트먼트 간 골 응력 차이를 직접 정량화한 데이터는 없어 보강 근거로 활용.
  - ▸ 출발(`aalaei-2017-segmented-nonsegmented-abutment-fea`) 한줄: 3D 유한요소분석(하악 대구치, 100 N 수직·45° 각도 하중): 세그먼트형 어버트먼트가 각도 하중 시 골 응력을 4배 낮추지만(31 vs 126 MPa), 나사 응력은 약간 높다(430 vs 375 MPa).
  - ▸ 대상(`velez-2020-implant-connection-abutment-design-screw`) 한줄: In-vitro 연구(임플란트 120개 — 외측육각 60 vs 11° Morse taper 내측 원추형 60, 어버트먼트 스크류를 10/20/30 Ncm로 체결 후 열·기계 하중): 임플란트-어버트먼트 변연 부적합은 Morse taper 연결에서 가장 낮고(~0.6 µm) 체결 토크가 높을수록 감소해 제조사 권장값 30 Ncm에서 ≈0 µm였으나 **20→30 Ncm 사이 유의차는 없었음**.


### sinus-lift/lateral

- `sartori-2003-msfa-bio-oss-10year-case-report`  —[상충 · 상충]→  **`rogova-2025-histomorphometric-non-decalcified-bone-substitute-sr`**
  - **근거 문장**: - [[bone-regeneration/rogova-2025-histomorphometric-non-decalcified-bone-substitute-sr]] — histomorphometry 방법론 SR — 평가 방법 차이로 inter-study 결과 상충 가능.
  - ▸ 출발(`sartori-2003-msfa-bio-oss-10year-case-report`) 한줄: 단일 환자 case report — Bio-Oss 단독 MSFA 후 8개월 / 2년 / 10년 시점 trephine biopsy histomorphometry: 골조직(골수강 포함) 29.8% → 69.7% → 86.7%로 증가, Bio-Oss 입자는 점진적 흡수 — 10년 remodeling을 시간순으로 시각화한 교과서적 trajectory.
  - ▸ 대상(`rogova-2025-histomorphometric-non-decalcified-bone-substitute-sr`) 한줄: 체계적 문헌고찰(118편, 2015–2024, 비탈회 plastic-embedded specimens): 골재생 연구의 동물모델은 rat>rabbit>sheep>dog 순; 염색은 toluidine blue 우세; 평가지표는 신생골 형성·잔존 이식재·MAR(Mineral Apposition Rate, calcein green) 중심 — 연구방법론 표준화 필요성 지적.

- `sartori-2003-msfa-bio-oss-10year-case-report`  —[상충 · 상충]→  **`sinus-lift-lateral-2026-synthesis`**
  - **근거 문장**: 측방 상악동거상술(Maxillary Sinus Floor Augmentation, MSFA)에서 Bio-Oss(탈단백우골, DPBB)가 점진적으로 흡수·골치환되는지를 단일 환자 8개월·2년·10년 연속 생검으로 보여주는 유일한 10년 궤적 자료. Mordenfeld 2010의 "유의한 흡수 없음" 소견과 상충해 연구 간 변이를 이해하는 데 필수적이다. See [[overviews/sinus-lift-lateral-2026-synthesis]].
  - ▸ 출발(`sartori-2003-msfa-bio-oss-10year-case-report`) 한줄: 단일 환자 case report — Bio-Oss 단독 MSFA 후 8개월 / 2년 / 10년 시점 trephine biopsy histomorphometry: 골조직(골수강 포함) 29.8% → 69.7% → 86.7%로 증가, Bio-Oss 입자는 점진적 흡수 — 10년 remodeling을 시간순으로 시각화한 교과서적 trajectory.
  - ▸ 대상(`sinus-lift-lateral-2026-synthesis`) 한줄: 측방창 (Lateral Window) 상악동거상술 (Sinus Floor Elevation, SFE)에서 슈나이더 막 (Schneiderian Membrane) 천공 (Sinus Membrane Perforation, SMP)과 부비동염 (Sinusitis) 예방·관리를 다룬 34편에 이식재 선택 및 PRF (Platelet-Rich Fibrin) 보조 근거 3편을 추가해 총 37편으로 확장한 종합 페이지 — L-PRF·A-PRF 보조 시 신생골 +7~11% 유의 증가, BCP가 DBBM 대비 신


### sinus-lift/pseudocyst

- `shenoy-2013-maxillary-antrolith-recurrent-sinusitis-case`  —[대비되는 · 대비]→  **`tan-2020-maxillary-antrolith-case-report-management`**
  - **근거 문장**: 상악동석이 재발성 상악동염과 구강상악동루(Oroantral Fistula)를 유발한 증례. Caldwell-Luc 수술 과거력이 있는 환자에서 잔류 골편이 상악동석의 nidus가 된 메커니즘을 설명. [[sinus-lift/pseudocyst/tan-2020-maxillary-antrolith-case-report-management]]의 무증상 소형 증례와 대비되는 증상성 대형(2×1cm) 증례.
  - ▸ 출발(`shenoy-2013-maxillary-antrolith-recurrent-sinusitis-case`) 한줄: 과거 Caldwell-Luc 수술 잔류 골편을 nidus로 한 2×1cm 대형 상악동석이 재발성 상악동염·구강상악동루 유발; ESS+Caldwell-Luc 복합 제거 후 완치 — ESS 후 충분한 세척으로 예방 권고.
  - ▸ 대상(`tan-2020-maxillary-antrolith-case-report-management`) 한줄: 67세 여성 CBCT 우연 발견 3.1×3.6mm 무증상 상악동석 증례 — 소형 무증상 상악동석은 경과관찰, 합병증 동반 시 수술 제거(Caldwell-Luc/ESS).

- `wang-2023-antral-pseudocyst-drift-osteotome-case`  —[반론 · 반론]→  **`nosaka-2024-sinus-elevation-radiopaque-lesions-review`**
  - **근거 문장**: - [[sinus-lift/pseudocyst/nosaka-2024-sinus-elevation-radiopaque-lesions-review]] — sinus lesion 일반론
  - ▸ 출발(`wang-2023-antral-pseudocyst-drift-osteotome-case`) 한줄: Case report + literature review (Sichuan University, JCM 2023): **OSFE (osteotome sinus floor elevation) + 동시 implant** 후 AP가 sinus 내에서 drift — implant 안정 유지. Transcrestal 접근에서의 AP 핸들링 datapoint.
  - ▸ 대상(`nosaka-2024-sinus-elevation-radiopaque-lesions-review`) 한줄: Clinical review (Nosaka·Showa University, JCM 2024): 상악동 내 well-defined faintly radiopaque lesion의 sinus floor elevation 결정 framework — AP/MRC 외 다양한 mass 감별진단·차등 접근 가이드.


### veneers

- `lim-2023-resin-composite-laminate-veneer-survival-sr-ma`  —[대비되는 · 대비]→  **`klein-2025-ceramic-laminate-veneer-survival-complications-sr-ma`**
  - **근거 문장**: 레진 복합재 라미네이트 비니어의 생존율에 대한 체계적 SR+MA가 부재하여 세라믹 비니어와의 비교 근거를 보완하기 위해 인제스트. [[veneers/klein-2025-ceramic-laminate-veneer-survival-complications-sr-ma]]에서 다루는 세라믹 비니어 생존율과 직접 대비되는 레진 계열 근거를 제공한다.
  - ▸ 출발(`lim-2023-resin-composite-laminate-veneer-survival-sr-ma`) 한줄: 7편 연구(RCT 3 + 코호트 4, 추적 24–97개월) SR+MA: 레진 복합재 라미네이트 비니어 생존율 88%, 직접법(91%) > 간접법(84%); 표면거칠기·색 불일치가 가장 흔한 합병증.
  - ▸ 대상(`klein-2025-ceramic-laminate-veneer-survival-complications-sr-ma`) 한줄: SR+MA (29편, 7,753개 비니어): LDS 96.81% 생존율, 기술적 합병증 6.1%로 최고 성적; 소재 간 생존율 차이 없음; 지르코니아 2.6년 100% 생존이나 장기 데이터 부족.


## Tier 2 — 대상 식별 필요 / soft signal (review only)

- `han-2023-software-automated-tooth-preparation-evaluation` [digital-workflow] (SOFT→revilla-leon-2025-tooth-preparation-factors-ios-accuracy-sr, 'whereas' · 반면(대조))
  - **근거 문장**: On 35 scanned graduate-student crown preparations, SAE produced **identical scores across three rounds (perfect intra-rater agreement)**, whereas human DAE was only moderate-to-good. SAE–DAE inter-rater agreement was almost-perfect to substantial (moderate only for MD TOC), with no significant score difference (p>0.05). SAE thus offers a reliable, reproducible objective measurement of exactly the 
  - ▸ 출발(`han-2023-software-automated-tooth-preparation-evaluation`) 한줄: In-vitro 타당성 연구(대학원생 형성 하악 제1대구치 35개): computational geometric algorithm 기반 자동 평가(SAE)는 crown 형성치의 교합면 삭제량·TOC를 완벽한 재현성으로 평가했고, 인간의 디지털 보조 평가(DAE, moderate~good)보다 일관됐으며 SAE–DAE 간 일치도도 거의 완벽했다.
  - ▸ 대상(`revilla-leon-2025-tooth-preparation-factors-ios-accuracy-sr`) 한줄: 체계적 문헌고찰(39편): 형성 형태가 단순하고 축면 경사(TOC)가 크며 교합면을 해부학적으로 삭제하고 finish line이 치은연 위·chamfer일수록, 인접치 간격이 넓을수록 구강스캐너(IOS) 정확도가 좋아지며, 기존 코어 수복물과 치은연하 finish line은 정확도를 떨어뜨린다.

- `han-2023-software-automated-tooth-preparation-evaluation` [digital-workflow] (SOFT→sadid-zadeh-2020-teeth-prepared-students-cadcam, 'whereas' · 반면(대조))
  - **근거 문장**: On 35 scanned graduate-student crown preparations, SAE produced **identical scores across three rounds (perfect intra-rater agreement)**, whereas human DAE was only moderate-to-good. SAE–DAE inter-rater agreement was almost-perfect to substantial (moderate only for MD TOC), with no significant score difference (p>0.05). SAE thus offers a reliable, reproducible objective measurement of exactly the 
  - ▸ 출발(`han-2023-software-automated-tooth-preparation-evaluation`) 한줄: In-vitro 타당성 연구(대학원생 형성 하악 제1대구치 35개): computational geometric algorithm 기반 자동 평가(SAE)는 crown 형성치의 교합면 삭제량·TOC를 완벽한 재현성으로 평가했고, 인간의 디지털 보조 평가(DAE, moderate~good)보다 일관됐으며 SAE–DAE 간 일치도도 거의 완벽했다.
  - ▸ 대상(`sadid-zadeh-2020-teeth-prepared-students-cadcam`) 한줄: 단면연구(루브릭, 타이포돈트 형성치 334개): 본과 4학년 학생의 CAD/CAM 형성치에서 finish line(변연선) 품질 오류가 가장 빈번(223건 중 136건)했으며, 이는 CAD/CAM 수복물 적합도에 가장 결정적인 항목이다.

- `shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment` [endodontics] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refutes the worry that biomineralizing CSBSs are hard to retrieve: both removed **more** material than AH Plus.
  - ▸ 출발(`shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment`) 한줄: In-vitro 마이크로-CT 연구 (하악소구치 36개, 군당 12개): AH Plus Bioceramic(AHB)·Ceraseal(CER) 단일콘 충전이 에폭시 레진 AH Plus Jet(AHJ)보다 재근관치료 시 제거가 잘 됨 — WaveOne Gold + XP-endo Finisher 후 제거율 94.8%·92.5% vs 87.1%.

- `abada-2025-obturation-techniques-post-obturation-pain-rct` [endodontics] (SOFT→song-2022-sealer-based-obturation-epoxy-calcium-silicate-rct, 'whereas' · 반면(대조))
  - **근거 문장**: - [[endodontics/song-2022-sealer-based-obturation-epoxy-calcium-silicate-rct]] — extends; Song found no pain/extrusion difference between calcium-silicate and AH Plus, whereas this RCT detects an AH Plus pain penalty.
  - ▸ 출발(`abada-2025-obturation-techniques-post-obturation-pain-rct`) 한줄: RCT(하악 제1대구치 150개, 단일내원, 무증상 비가역적 치수염): CeraSeal vs AH Plus를 측방가압·연속파가압·단일콘 충전으로 비교. 모든 군 통증 낮음(VAS 0–1.4). 충전법 자체는 통증 무관(p=0.124)이나 AH Plus가 CeraSeal보다 통증 유의하게 높음(전체 p<0.001, 연속파가압에서 p<0.001). 실러 일출 빈도는 군간 차이 없으나(p=0.499) 일출 시 통증 증가(p<0.001).
  - ▸ 대상(`song-2022-sealer-based-obturation-epoxy-calcium-silicate-rct`) 한줄: RCT(등록 80개, 분석 71개 치아, 4개 실러군 각 n=20: AH Plus·ADseal·CeraSeal·EndoSeal TCS): 칼슘실리케이트 실러와 에폭시레진 실러 사이에 기포·실러 압출·3개월 술후통증의 유의한 차이가 없었고, 충전 품질 차이는 실러 종류가 아니라 제품 특성에 따랐다.

- `de-almeida-junior-2024-cytotoxicity-bioactivity-ceraseal-bioroot` [endodontics] (SOFT→spinelli-2024-three-year-single-cone-ceraseal-cohort, 'Whereas' · 반면(대조))
  - **근거 문장**: Seeds the wiki's first CeraSeal / bioceramic-sealer biocompatibility cluster, complementing the clinical CeraSeal cohort and obturation papers already held ([[endodontics/spinelli-2024-three-year-single-cone-ceraseal-cohort]], [[endodontics/zamparini-2023-premixed-calcium-silicate-carrier-based-2year]]). Whereas those track clinical/survival outcomes, this paper supplies the cell-level (MC3T3 pre-
  - ▸ 출발(`de-almeida-junior-2024-cytotoxicity-bioactivity-ceraseal-bioroot`) 한줄: In-vitro MC3T3 전조골세포 연구 (ISO 10993-5): CeraSeal·BioRoot RCS·AH Plus 모두 48시간 시점 비독성 (BioRoot만 24시간·1:10에서 일시적 독성), 염증·광화 유전자를 차등 유도 (AH Plus는 Tnf↑, CeraSeal/BioRoot는 Ptgs2·Dmp1↑) 했으나 28일째 광화 결절 형성에는 차이가 없었다.
  - ▸ 대상(`spinelli-2024-three-year-single-cone-ceraseal-cohort`) 한줄: 전향 코호트(환자 52명·근관치료 58건, Ceraseal + 단일콘): 36개월 생존율 92.7%, per-protocol 치유율(PAI ≤2) 92.1%로 Ceraseal 최장 추적 보고; 치수염·치수괴사 치아는 100% 치유.

- `de-almeida-junior-2024-cytotoxicity-bioactivity-ceraseal-bioroot` [endodontics] (SOFT→zamparini-2023-premixed-calcium-silicate-carrier-based-2year, 'Whereas' · 반면(대조))
  - **근거 문장**: Seeds the wiki's first CeraSeal / bioceramic-sealer biocompatibility cluster, complementing the clinical CeraSeal cohort and obturation papers already held ([[endodontics/spinelli-2024-three-year-single-cone-ceraseal-cohort]], [[endodontics/zamparini-2023-premixed-calcium-silicate-carrier-based-2year]]). Whereas those track clinical/survival outcomes, this paper supplies the cell-level (MC3T3 pre-
  - ▸ 출발(`de-almeida-junior-2024-cytotoxicity-bioactivity-ceraseal-bioroot`) 한줄: In-vitro MC3T3 전조골세포 연구 (ISO 10993-5): CeraSeal·BioRoot RCS·AH Plus 모두 48시간 시점 비독성 (BioRoot만 24시간·1:10에서 일시적 독성), 염증·광화 유전자를 차등 유도 (AH Plus는 Tnf↑, CeraSeal/BioRoot는 Ptgs2·Dmp1↑) 했으나 28일째 광화 결절 형성에는 차이가 없었다.
  - ▸ 대상(`zamparini-2023-premixed-calcium-silicate-carrier-based-2year`) 한줄: 전향 코호트 (볼로냐 마스터 과정), 24개월 근관치료 89건: Ceraseal 프리믹스 칼슘실리케이트 실러를 warm carrier-based(Thermafil) 충전과 병용 시 AH Plus와 치유율(91.1% vs 88.6%, 무의차)·생존율(전체 97.8%) 동등, 근단부 sealer 일출은 더 낮았고(13.3% vs 25%), Ceraseal 일출 6건 중 3건은 24개월 내 방사선학적으로 소실됨.

- `muehlemann-2025-cost-efficiency-digital-conventional-denture` [complete-denture] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[complete-denture/jafarpour-2024-cadcam-versus-traditional-complete-dentures]] — earlier SR+MA reported CAD/CAM RCDs as significantly cheaper (lower laboratory and total costs); this paper's cost-efficiency meta-analysis (accounting for patient outcomes and rigorous currency harmonization) contradicts that cost-only conclusion, finding no significant cost difference.
  - ▸ 출발(`muehlemann-2025-cost-efficiency-digital-conventional-denture`) 한줄: SR+MA (5편, n=184명, J Prosthodont 2025): 디지털(CAD/CAM) 대 전통(conventional) 총의치(완전의치) 워크플로우 간 기공비(MD -239.77달러, p=0.106), 임상비(MD 74.39달러, p=0.451), 총비용(MD -357.76달러, p=0.258), 내원횟수(MD -1.47, p=0.351) 모두 통계적으로 유의한 차이 없음; 술자 숙련도(operator experience)가 임상비와 내원횟수에 유의한 영향을 미침.

- `muehlemann-2025-cost-efficiency-digital-conventional-denture` [complete-denture] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: 사용자가 CAD/CAM 치과 기공(dental laboratory) 관련 논문을 요청하여 인제스트. 기존 [[wiki/complete-denture/jafarpour-2024-cadcam-versus-traditional-complete-dentures]]는 CAD/CAM 총의치가 기공·총비용에서 유의하게 저렴하다고 보고했으나, 본 SR+MA는 비용-효율성(cost-efficiency) 메타분석 방법론으로 재검증한 결과 유의한 차이가 없음을 보여 상반된 결론을 제공한다.
  - ▸ 출발(`muehlemann-2025-cost-efficiency-digital-conventional-denture`) 한줄: SR+MA (5편, n=184명, J Prosthodont 2025): 디지털(CAD/CAM) 대 전통(conventional) 총의치(완전의치) 워크플로우 간 기공비(MD -239.77달러, p=0.106), 임상비(MD 74.39달러, p=0.451), 총비용(MD -357.76달러, p=0.258), 내원횟수(MD -1.47, p=0.351) 모두 통계적으로 유의한 차이 없음; 술자 숙련도(operator experience)가 임상비와 내원횟수에 유의한 영향을 미침.

- `rodriguez-sanchez-2017-chlorhexidine-alveolar-osteitis-third` [oral-surgery] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: SR+MA (23 RCT, 2,824 발치) — 사랑니 발치 후 CHX (제형·농도 무관)는 건성발치와 위험 약 47% 감소 (RR=0.53, NNT=8); 겔이 가글보다 약간 우수; 이상반응은 위약과 차이 없음.
  - ▸ 출발(`rodriguez-sanchez-2017-chlorhexidine-alveolar-osteitis-third`) 한줄: SR+MA (23 RCT, 2,824 발치) — 사랑니 발치 후 CHX (제형·농도 무관)는 건성발치와 위험 약 47% 감소 (RR=0.53, NNT=8); 겔이 가글보다 약간 우수; 이상반응은 위약과 차이 없음.

- `rodriguez-sanchez-2017-chlorhexidine-alveolar-osteitis-third` [oral-surgery] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: **부작용**: CHX와 위약 간 이상반응 빈도 차이 없음 — 안전성 확인.
  - ▸ 출발(`rodriguez-sanchez-2017-chlorhexidine-alveolar-osteitis-third`) 한줄: SR+MA (23 RCT, 2,824 발치) — 사랑니 발치 후 CHX (제형·농도 무관)는 건성발치와 위험 약 47% 감소 (RR=0.53, NNT=8); 겔이 가글보다 약간 우수; 이상반응은 위약과 차이 없음.

- `derbishi-2026-coronectomy-versus-total-extraction-third` [oral-surgery] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: This 2026 meta-analysis is the methodologically strongest coronectomy-vs-total-extraction synthesis to date. Using Peto odds ratios (appropriate for the rare-event IAN injury), HKSJ-adjusted random-effects CIs, GRADE, and trial sequential analysis, it shows coronectomy cuts IAN injury roughly fourfold (Peto OR 0.23) and — critically — TSA confirms the evidence is *conclusive*, not just statistical
  - ▸ 출발(`derbishi-2026-coronectomy-versus-total-extraction-third`) 한줄: SR+MA (8편 — RCT 3 + 코호트 5, 1488치): 치관절제가 발치 대비 하치조신경 손상 감소 (Peto OR 0.23, 95% CI 0.13–0.39, p<0.0001, TSA 확정), 건성치조염·감염 차이 없음, 치근 회수 재수술률 1.2%.

- `bodner-2012-cutaneous-sinus-tract-dental` [oral-surgery] (SOFT→gargava-2022-deep-neck-space-infection-150-cases, 'whereas' · 반면(대조))
  - **근거 문장**: - [[oral-surgery/gargava-2022-deep-neck-space-infection-150-cases]] — Both address surgical presentations of odontogenic infection; this paper covers the chronic cutaneous-draining variant whereas Gargava covers acute deep-neck-space spread.
  - ▸ 출발(`bodner-2012-cutaneous-sinus-tract-dental`) 한줄: 후향적 증례군(소아 28명, 평균 10.25세): 치성 피부누공(CST)은 주로 우식이 있는 하악 제1대구치에서 기원해 하악-하악하부 피부에 나타나며, 평균 6.5개월의 진단 지연 후 근관치료 또는 발치로 빠르게 치유되고, 병변 기간이 긴 29% 환자에서 흉터 교정술이 필요했다.
  - ▸ 대상(`gargava-2022-deep-neck-space-infection-150-cases`) 한줄: 전향적 연구(n=150): 심경부 감염의 원인은 치성(42.66%)이 가장 많고, 루드비히 앙기나가 가장 흔한 침범 공간(24.66%)이며, 주요 원인균은 연쇄구균(31.33%), 절개배농 38%, 응급기관절개술 일부에서 시행.

- `ali-2023-conventional-minimally-invasive-veneers-sr` [veneers] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refuted the prior assumption of CV superiority: MPVs showed equal or better outcomes in survival and longevity
  - ▸ 출발(`ali-2023-conventional-minimally-invasive-veneers-sr`) 한줄: 4편 비교 연구 체계적 문헌고찰: 최소삭제 비니어(MPV)가 생존율·성공 기간에서 동등 이상; 미세누출·변연적합도·색 안정성은 준비 방식·재료에 따라 차이, 장석질 도재 MPV(0.2–0.5 mm)가 우수.

- `komine-2024-clinical-performance-laminate-veneers-review` [veneers] (HIGH-no-target, 'conflicting result' · 상충 결과)
  - **근거 문장**: - **Vitality**: Nonvital teeth have higher failure risk per Beier; conflicting results in other studies
  - ▸ 출발(`komine-2024-clinical-performance-laminate-veneers-review`) 한줄: 내러티브 리뷰 (55개 임상연구): 실리카 기반 세라믹 라미네이트 비니어 (Laminate Veneer, LV) 생존율은 72–100%, 상아질 노출(Dentin Exposure)·이갈이(Bruxism)·접착 프로토콜이 핵심 수정 가능 예후 인자이며, 지르코니아(Zirconia) LV는 3년 이상 임상 데이터 없음.

- `nelson-2011-text-vs-voice-reminder-pediatric-dental-rct` [practice-management] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: This randomized controlled trial in the pediatric dentistry clinic at the University of Washington tested whether **SMS text messages** are as effective as **automated voice messages** for reducing appointment no-shows. Of 543 caregiver/child dyads invited, **318 pairs (59% response)** enrolled and were randomized to receive either an SMS text reminder (n=158) or a voice-message reminder (control,
  - ▸ 출발(`nelson-2011-text-vs-voice-reminder-pediatric-dental-rct`) 한줄: 치과대학 소아치과 RCT (n=318 보호자/아동 쌍): 음성 메시지 알림의 미내원율(8.2%)이 문자(SMS) 알림(17.7%)보다 낮았다 — 무작위 배정 상황에서 SMS가 음성만큼 효과적이지 않았다 (보정 OR 2.12).

- `nelson-2011-text-vs-voice-reminder-pediatric-dental-rct` [practice-management] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: The result is a useful counterpoint to reminder-vs-none studies: here the comparison is **channel vs channel**, and channel choice clearly mattered. The authors flag a key caveat — patients were *randomly assigned* a reminder channel, so the SMS disadvantage may not hold when patients **self-select** their preferred channel.
  - ▸ 출발(`nelson-2011-text-vs-voice-reminder-pediatric-dental-rct`) 한줄: 치과대학 소아치과 RCT (n=318 보호자/아동 쌍): 음성 메시지 알림의 미내원율(8.2%)이 문자(SMS) 알림(17.7%)보다 낮았다 — 무작위 배정 상황에서 SMS가 음성만큼 효과적이지 않았다 (보정 OR 2.12).

- `nelson-2011-text-vs-voice-reminder-pediatric-dental-rct` [practice-management] (HIGH-no-target, 'Counterpoint' · 반대 논점)
  - **근거 문장**: Counterpoint reminder RCT for the no-show overview: in a university pediatric dental clinic, **voice messages beat SMS text** at reducing no-shows — the opposite-channel result qualifies the blanket "send a reminder" recommendation by showing channel choice (and population) matters. Refines [[overviews/dental-appointment-no-show-overview]] by adding a head-to-head channel comparison rather than re
  - ▸ 출발(`nelson-2011-text-vs-voice-reminder-pediatric-dental-rct`) 한줄: 치과대학 소아치과 RCT (n=318 보호자/아동 쌍): 음성 메시지 알림의 미내원율(8.2%)이 문자(SMS) 알림(17.7%)보다 낮았다 — 무작위 배정 상황에서 SMS가 음성만큼 효과적이지 않았다 (보정 OR 2.12).

- `garcia-2023-teledentistry-acceptability-latino-rural-virginia` [practice-management] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: Contrary to prior literature reporting positive pre-experience attitudes toward telehealth among Latinos and rural residents, **57.1% reported no interest** in video/internet dental consultations even if available. In bivariate (chi-squared) analysis, only two factors were significantly associated with acceptability: **household income >$24,000 (p=.04)** and — counter-intuitively — **not having de
  - ▸ 출발(`garcia-2023-teledentistry-acceptability-latino-rural-virginia`) 한줄: 농촌 라티노 성인 91명 대상 단면조사 — 57%가 원격치의학(Teledentistry)에 무관심, 가구소득 >$24k와 치과보험 미보유만 수용성과 유의 연관; 단순 가용성만으로는 접근격차가 해소되지 않으며 보건형평성(health equity)의 명시적 통합이 필요.

- `silva-2013-occlusal-factors-nccl-systematic-review` [nccl] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[nccl/duangthip-2017-occlusal-stress-nccl-abfraction-sr]] — contradicts (lab-weighted SR finding 81% association)
  - ▸ 출발(`silva-2013-occlusal-factors-nccl-systematic-review`) 한줄: 교합위험인자-NCCL SR 9편 — 다수 무연관, 3편만 특정 변수서 유의(p<0.05), 이질성 높음.

- `duangthip-2017-occlusal-stress-nccl-abfraction-sr` [nccl] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[nccl/senna-2012-nccl-occlusion-systematic-review]] — contradicts (clinical SR, no conclusion)
  - ▸ 출발(`duangthip-2017-occlusal-stress-nccl-abfraction-sr`) 한줄: abfraction SR 69편 — 81%가 교합응력-NCCL 연관 보고하나, 응력 단독 원인 입증 임상연구는 전무.

- `duangthip-2017-occlusal-stress-nccl-abfraction-sr` [nccl] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[nccl/silva-2013-occlusal-factors-nccl-systematic-review]] — contradicts (clinical SR, majority null)
  - ▸ 출발(`duangthip-2017-occlusal-stress-nccl-abfraction-sr`) 한줄: abfraction SR 69편 — 81%가 교합응력-NCCL 연관 보고하나, 응력 단독 원인 입증 임상연구는 전무.

- `dioguardi-2024-abfraction-theory-controversy-scoping-review` [nccl] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: PRISMA-ScR scoping review (only 6 of 1449 studies included) concluding the evidence is insufficient to confirm or refute occlusal loads as a cause of abfraction, and that prospective longitudinal studies isolating abfraction from erosion/abrasion are needed.
  - ▸ 출발(`dioguardi-2024-abfraction-theory-controversy-scoping-review`) 한줄: PRISMA-ScR scoping review(1449→6편) — 교합부하의 abfraction 원인 역할 확정·반박 모두 불가, 전향 종단연구 필요.

- `dioguardi-2024-abfraction-theory-controversy-scoping-review` [nccl] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: PRISMA-ScR scoping review(1449→6편) — 교합부하의 abfraction 원인 역할 확정·반박 모두 불가, 전향 종단연구 필요.
  - ▸ 출발(`dioguardi-2024-abfraction-theory-controversy-scoping-review`) 한줄: PRISMA-ScR scoping review(1449→6편) — 교합부하의 abfraction 원인 역할 확정·반박 모두 불가, 전향 종단연구 필요.

- `dioguardi-2024-abfraction-theory-controversy-scoping-review` [nccl] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: This registered scoping review (PRISMA-ScR, INPLASY protocol, ROBINS-I bias assessment) is the most methodologically rigorous appraisal of the abfraction controversy to date. Searching PubMed and Scopus for "abfraction" AND "NCCL," the authors screened 1449 articles and included only 6 that correlated NCCL progression with applied forces. Their analysis found that these studies do not provide suff
  - ▸ 출발(`dioguardi-2024-abfraction-theory-controversy-scoping-review`) 한줄: PRISMA-ScR scoping review(1449→6편) — 교합부하의 abfraction 원인 역할 확정·반박 모두 불가, 전향 종단연구 필요.

- `dioguardi-2024-abfraction-theory-controversy-scoping-review` [nccl] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: 6 included studies; insufficient evidence to confirm or refute occlusal-load aetiology of abfraction. NCCL prevalence framed at ~10-40% of adults over 30, premolars predominant. Calls for prospective longitudinal designs.
  - ▸ 출발(`dioguardi-2024-abfraction-theory-controversy-scoping-review`) 한줄: PRISMA-ScR scoping review(1449→6편) — 교합부하의 abfraction 원인 역할 확정·반박 모두 불가, 전향 종단연구 필요.

- `dioguardi-2024-abfraction-theory-controversy-scoping-review` [nccl] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[nccl/duangthip-2017-occlusal-stress-nccl-abfraction-sr]] — refines/contradicts (re-analyzes and critiques its pro-abfraction conclusion)
  - ▸ 출발(`dioguardi-2024-abfraction-theory-controversy-scoping-review`) 한줄: PRISMA-ScR scoping review(1449→6편) — 교합부하의 abfraction 원인 역할 확정·반박 모두 불가, 전향 종단연구 필요.

- `senna-2012-nccl-occlusion-systematic-review` [nccl] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[nccl/duangthip-2017-occlusal-stress-nccl-abfraction-sr]] — contradicts (later SR reporting 81% of studies found an association)
  - ▸ 출발(`senna-2012-nccl-occlusion-systematic-review`) 한줄: 임상연구 28편 SR — 이질성·편향으로 교합의 NCCL 병인 역할 결론 불가, 메타분석 불가.

- `sirikatitham-2026-fracture-resistance-partial-coverage-scoping` [inlay] (SOFT→prott-2025-partial-coverage-restorations-posterior-scoping, 'whereas' · 반면(대조))
  - **근거 문장**: Extends [[wiki/inlay/prott-2025-partial-coverage-restorations-posterior-scoping]] from a different angle: Prott (2025) scoped clinical *survival* of posterior PCRs by material, whereas this scoping review maps in-vitro *fracture resistance and fracture patterns* by preparation design (overlay / MOD overlay / MOD onlay), occlusal thickness, and ceramic type (LDS / ZLS / PICN / RNC). It also synthes
  - ▸ 출발(`sirikatitham-2026-fracture-resistance-partial-coverage-scoping`) 한줄: 세라믹 부분피개수복물(PCR)의 파절저항·파절양상을 프렙 디자인별로 정리한 스코핑 리뷰(34편: 소구치 9·대구치 25) — MOD overlay는 대구치에서 anatomic overlay보다 파절하중이 낮았고, 교합 두께 증가는 대체로 유리, proximal box/MOD는 파절 양상을 악화시켰으나 모든 디자인이 최대 교합력을 상회.
  - ▸ 대상(`prott-2025-partial-coverage-restorations-posterior-scoping`) 한줄: 구치부 부분 피개 수복물(인레이·온레이·엔도크라운) 생존율 스코핑 리뷰 — 세라믹 93–96%, 엔도크라운 92–95%.

- `sirikatitham-2026-fracture-resistance-partial-coverage-scoping` [inlay] (SOFT→hofsteenge-2023-preparation-design-fracture-strength-disilicate-inlay, 'whereas' · 반면(대조))
  - **근거 문장**: Extends [[wiki/inlay/prott-2025-partial-coverage-restorations-posterior-scoping]] from a different angle: Prott (2025) scoped clinical *survival* of posterior PCRs by material, whereas this scoping review maps in-vitro *fracture resistance and fracture patterns* by preparation design (overlay / MOD overlay / MOD onlay), occlusal thickness, and ceramic type (LDS / ZLS / PICN / RNC). It also synthes
  - ▸ 출발(`sirikatitham-2026-fracture-resistance-partial-coverage-scoping`) 한줄: 세라믹 부분피개수복물(PCR)의 파절저항·파절양상을 프렙 디자인별로 정리한 스코핑 리뷰(34편: 소구치 9·대구치 25) — MOD overlay는 대구치에서 anatomic overlay보다 파절하중이 낮았고, 교합 두께 증가는 대체로 유리, proximal box/MOD는 파절 양상을 악화시켰으나 모든 디자인이 최대 교합력을 상회.
  - ▸ 대상(`hofsteenge-2023-preparation-design-fracture-strength-disilicate-inlay`) 한줄: 인비트로+FEA(n=64 대구치): 리튬디실리케이트 수복 시 4가지 와동형성 디자인(UI/EI/RO/EO) 비교 — 오버레이 디자인이 파절강도 우수; IDS 적용; FEA에서 교두 피개 시 치아 변형 감소

- `sirikatitham-2026-fracture-resistance-partial-coverage-scoping` [inlay] (SOFT→griffis-2022-tooth-cusp-preservation-lithium-disilicate-onlay-fatigue, 'whereas' · 반면(대조))
  - **근거 문장**: Extends [[wiki/inlay/prott-2025-partial-coverage-restorations-posterior-scoping]] from a different angle: Prott (2025) scoped clinical *survival* of posterior PCRs by material, whereas this scoping review maps in-vitro *fracture resistance and fracture patterns* by preparation design (overlay / MOD overlay / MOD onlay), occlusal thickness, and ceramic type (LDS / ZLS / PICN / RNC). It also synthes
  - ▸ 출발(`sirikatitham-2026-fracture-resistance-partial-coverage-scoping`) 한줄: 세라믹 부분피개수복물(PCR)의 파절저항·파절양상을 프렙 디자인별로 정리한 스코핑 리뷰(34편: 소구치 9·대구치 25) — MOD overlay는 대구치에서 anatomic overlay보다 파절하중이 낮았고, 교합 두께 증가는 대체로 유리, proximal box/MOD는 파절 양상을 악화시켰으나 모든 디자인이 최대 교합력을 상회.
  - ▸ 대상(`griffis-2022-tooth-cusp-preservation-lithium-disilicate-onlay-fatigue`) 한줄: in-vitro 피로시험 - 치아 교두를 보존하는 lithium disilicate 온레이가 양호한 피로저항을 보여, 전교두 삭제보다 보존적(교두 보존) 온레이 형성을 지지.

- `devlin-2013-object-position-magnification-panoramic-radiography` [radiology] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: Refutes the assumption that placing teeth in the focal trough avoids distortion — magnification is not simply constant at the plane of focus; positioning precision matters for any metric use of panoramic.
  - ▸ 출발(`devlin-2013-object-position-magnification-panoramic-radiography`) 한줄: 이론+볼베어링 실험: 파노라마 확대율 수평 ~1.29·수직 ~1.26. 초점골 내 특정 위치에서만 왜곡 0. 보정용은 6 mm 구체가 우수.

- `devlin-2013-object-position-magnification-panoramic-radiography` [radiology] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: Refutes the assumption that placing teeth in the focal trough avoids distortion — magnification is not simply constant at the plane of focus; positioning precision matters for any metric use of panoramic.
  - ▸ 출발(`devlin-2013-object-position-magnification-panoramic-radiography`) 한줄: 이론+볼베어링 실험: 파노라마 확대율 수평 ~1.29·수직 ~1.26. 초점골 내 특정 위치에서만 왜곡 0. 보정용은 6 mm 구체가 우수.

- `willershausen-2025-low-field-mri-pediatric-dental` [radiology] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Positions low-field MRI as an emerging radiation-free alternative for selected paediatric dental indications, with current spatial-resolution limits — the conceptual counterpoint to the dose-reduction cluster.
  - ▸ 출발(`willershausen-2025-low-field-mri-pediatric-dental`) 한줄: 전향적 소아 16명: 무피폭 0.55 T MRI가 치축·치근·치근흡수·낭종에서 초저선량 CT와 동등 화질, 단 모든 구조엔 미흡.

- `willershausen-2025-low-field-mri-pediatric-dental` [radiology] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Positions low-field MRI as an emerging radiation-free alternative for selected paediatric dental indications, with current spatial-resolution limits — the conceptual counterpoint to the dose-reduction cluster.
  - ▸ 출발(`willershausen-2025-low-field-mri-pediatric-dental`) 한줄: 전향적 소아 16명: 무피폭 0.55 T MRI가 치축·치근·치근흡수·낭종에서 초저선량 CT와 동등 화질, 단 모든 구조엔 미흡.

- `al-sulimman-2025-composite-amalgam-failure-risk-sr-ma` [dental-materials] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - No statistically significant difference in failure risk between composite resin and amalgam (RR 0.96) — contradicts real-world HR data (Tobias 2024: HR 1.29)
  - ▸ 출발(`al-sulimman-2025-composite-amalgam-failure-risk-sr-ma`) 한줄: 복합레진 vs 아말감 실패위험 SR+MA (Int Dent J 2025): 13편; RR 0.96 (95% CI 0.68–1.34), 통계적으로 유의한 차이 없음; 실패비율 아말감 0–50%, 레진 0–62.7%; 연구 간 실패 정의 이질성이 핵심 제한점.

- `tobias-2024-amalgam-composite-survival-big-data` [dental-materials] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[dental-materials/al-sulimman-2025-composite-amalgam-failure-risk-sr-ma]] — SR+MA; no significant RR difference (RR 0.96); contradicts real-world HR gap
  - ▸ 출발(`tobias-2024-amalgam-composite-survival-big-data`) 한줄: Big-data 후향적 코호트 (이스라엘 Maccabi, 58개소, 650,000명 이상, 2014–2021): 아말감(Amalgam) 연간 실패율 3.5% vs 복합레진(Composite Resin) 4.5%; HR 1.29; 다면(Multi-surface) 레진에서만 유의한 차이.

- `khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma` [bone-regeneration] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: This page **refines** the staging decision underlying the staged (two-stage) technique anchored by Enislidis 2006: a contemporary comparative SR tilts the timing choice toward one-stage, without overturning the standalone validity of the staged greenstick technique as a documented option for difficult ridges.
  - ▸ 출발(`khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma`) 한줄: PRISMA 체계적 문헌고찰+메타분석(정성 11편, 메타분석 3편, 전부 중-고 비뚤림위험): 1단계 치조제 분할술(one-stage ridge split)이 2단계보다 우수(통합 SMD ~0.89, one-stage 유리). 단, 이질성 불량·깔때기 비대칭(출판편향 가능성)으로 근거 강도는 제한적.

- `khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma` [bone-regeneration] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: - [[bone-regeneration/enislidis-2006-staged-ridge-splitting-implant-mandible]] — staged (two-stage) ridge-split technique anchor; this SR refines the timing decision toward one-stage but does not overturn the staged technique's role.
  - ▸ 출발(`khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma`) 한줄: PRISMA 체계적 문헌고찰+메타분석(정성 11편, 메타분석 3편, 전부 중-고 비뚤림위험): 1단계 치조제 분할술(one-stage ridge split)이 2단계보다 우수(통합 SMD ~0.89, one-stage 유리). 단, 이질성 불량·깔때기 비대칭(출판편향 가능성)으로 근거 강도는 제한적.

- `lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma` [bone-regeneration] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Foregrounds the **clinical-vs-preclinical contradiction**: clinical pooling favors densification, but sheep/porcine/murine models show no BIC or osseointegration gain, and one RCT (Rizk 2024) attributed 3 implant failures to over-densifying the narrow crest (reduced blood supply, heat) — leading the authors to position these techniques behind GBR / bone blocks / crestal split when those are feas
  - ▸ 출발(`lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma`) 한줄: SR+MA (10편, n=241; PROSPERO 등록) — 좁은(수평위축 ≤2.5 mm) 치조제에서 골확장·압축·골밀도화(Osseodensification, OD)가 대조군 대비 골밀도(Bone Density, BD; SMD −0.71, p=0.002)·치조정확장(Crestal Expansion, CE; SMD −1.12, p=0.04)·임플란트안정성지수(Implant Stability Quotient, ISQ; SMD −8.88, p=0.0005)를 유의하게 향상시킴. 단 CE·ISQ는 이질성

- `lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma` [bone-regeneration] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Bottom line**: expansion / compaction / osseodensification can render a narrow crest implant-ready and improve BD, CE, and ISQ, but the CE and ISQ evidence is fragile (heterogeneity + publication bias) and clinical benefit is contradicted by preclinical models — use cautiously, with adequate operator experience, and reserve for cases where staged augmentation is not preferable.
  - ▸ 출발(`lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma`) 한줄: SR+MA (10편, n=241; PROSPERO 등록) — 좁은(수평위축 ≤2.5 mm) 치조제에서 골확장·압축·골밀도화(Osseodensification, OD)가 대조군 대비 골밀도(Bone Density, BD; SMD −0.71, p=0.002)·치조정확장(Crestal Expansion, CE; SMD −1.12, p=0.04)·임플란트안정성지수(Implant Stability Quotient, ISQ; SMD −8.88, p=0.0005)를 유의하게 향상시킴. 단 CE·ISQ는 이질성

- `manfro-2013-bovine-bone-substitutes-comparative-histomorphometric` [bone-regeneration] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Rabbit calvaria titanium-cylinder model (n=8, 8/12 weeks): Bone-Fill and Bio-Oss (DBBM) are equivalent in new bone formation and clearly superior to Gen-Ox and blood clot — a direct comparison refuting the assumption that all bovine bone substitutes perform equally.
  - ▸ 출발(`manfro-2013-bovine-bone-substitutes-comparative-histomorphometric`) 한줄: 토끼 두개관 티타늄 실린더 모델(n=8, 8/12주): Bone-Fill와 탈단백 우골(Deproteinized Bovine Bone Mineral, DBBM, Bio-Oss)이 신생골 형성에서 동등하고 Gen-Ox·혈병보다 명확히 우수 — "이종골은 다 같다"는 가정을 반증하는 직접비교 동물연구.

- `souza-2020-citrus-sweets-enamel-erosion-invitro` [dental-erosion] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Coca-Cola (pH 2.6, 1.4 μm), refuting the assumption that pH alone predicts erosive rank.
  - ▸ 출발(`souza-2020-citrus-sweets-enamel-erosion-invitro`) 한줄: In-vitro 연구 (n=90 소 법랑질, 7일): 시트러스 젤리(pH 2.6~3.5)가 1.3–2.4 μm 법랑질 마모 유발; Fini Diet(pH 3.3)·Fini Regaliz(pH 3.1)는 0.1% 구연산 수준으로 Coca-Cola보다 더 침식적 — 복합산(구연산+젖산/말레산)이 pH보다 침식력 결정에 중요.

- `kiliaridis-2000-vertical-position-rotation-tipping-molars` [occlusion] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Provides large-sample human evidence that **overeruption is not inevitable** for unopposed molars, refuting the universal-overeruption belief.
  - ▸ 출발(`kiliaridis-2000-vertical-position-rotation-tipping-molars`) 한줄: 단면 인체 연구 (53명, 10년 이상 대합치 없는 대구치 84개): 18%는 정출 징후가 전혀 없었고 중등도-중증 정출(≥2 mm)은 24%뿐 — 대합치 없는 모든 치아가 정출하는 것은 아니다.

- `craddock-2007-overeruption-posterior-teeth-partial-occlusal` [occlusion] (HIGH-no-target, 'Overturn' · 결론 뒤집음)
  - **근거 문장**: - Overturns the intuitive assumption that "some contact = stability": partial contact neither reduces overeruption nor stabilises the tooth, and is associated with *more* tipping.
  - ▸ 출발(`craddock-2007-overeruption-posterior-teeth-partial-occlusal`) 한줄: 후향적 임상연구 (91명, 부분/완전 대합치 상실 후방치). 부분 교합접촉 (Partial Occlusal Contact) 은 완전 무대합 대비 정출 (Overeruption) 양을 줄이지 못했고, 부분대합치는 오히려 더 많이 경사 (Tipping) 됨 — 부분접촉만으로 수직 치아위치를 유지한다고 믿어선 안 된다.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Narrative review (abstract-only) arguing centric relation (CR) is a reproducible, clinically validated reference position for diagnosis and full-arch reconstruction; the real problem is the lack of consensus on its definition and recording method, not the concept — this is the counterpoint to "abandon CR."
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 한줄: 서술적 리뷰(초록만): 중심위(Centric Relation, CR)는 재현 가능하고 검증된 진단·전악 재건 기준위이며, 문제는 개념이 아니라 정의·기록법 합의 부재라고 주장하는, "CR 폐기" 주장에 대한 반론.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, '반론' · 반론)
  - **근거 문장**: 서술적 리뷰(초록만): 중심위(Centric Relation, CR)는 재현 가능하고 검증된 진단·전악 재건 기준위이며, 문제는 개념이 아니라 정의·기록법 합의 부재라고 주장하는, "CR 폐기" 주장에 대한 반론.
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 한줄: 서술적 리뷰(초록만): 중심위(Centric Relation, CR)는 재현 가능하고 검증된 진단·전악 재건 기준위이며, 문제는 개념이 아니라 정의·기록법 합의 부재라고 주장하는, "CR 폐기" 주장에 대한 반론.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Goldstein responds to the "uprising to abolish" centric relation (CR) — most directly the position advanced by Zonnenberg (2021) — by defending CR as a *needed* reference position rather than a disposable one. The bottom line is deliberately balanced: CR is a **universally recognized term with a long history of clinical success**, and it remains a **reproducible** maxillomandibular reference posit
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 한줄: 서술적 리뷰(초록만): 중심위(Centric Relation, CR)는 재현 가능하고 검증된 진단·전악 재건 기준위이며, 문제는 개념이 아니라 정의·기록법 합의 부재라고 주장하는, "CR 폐기" 주장에 대한 반론.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Defends CR as **reproducible** and clinically validated for **diagnostic and full-arch restorative** use, citing a long track record and the absence of contradicting clinical research.
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 한줄: 서술적 리뷰(초록만): 중심위(Centric Relation, CR)는 재현 가능하고 검증된 진단·전악 재건 기준위이며, 문제는 개념이 아니라 정의·기록법 합의 부재라고 주장하는, "CR 폐기" 주장에 대한 반론.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - Serves as the **counterpoint** to the abandon-CR argument within the CR/CO/MICP terminology debate.
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 한줄: 서술적 리뷰(초록만): 중심위(Centric Relation, CR)는 재현 가능하고 검증된 진단·전악 재건 기준위이며, 문제는 개념이 아니라 정의·기록법 합의 부재라고 주장하는, "CR 폐기" 주장에 대한 반론.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Consensus supports CR as the restorative position for full-arch reconstruction; no substantive clinical research contradicts it.
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 한줄: 서술적 리뷰(초록만): 중심위(Centric Relation, CR)는 재현 가능하고 검증된 진단·전악 재건 기준위이며, 문제는 개념이 아니라 정의·기록법 합의 부재라고 주장하는, "CR 폐기" 주장에 대한 반론.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[occlusion/zonnenberg-2021-centric-relation-critically-revisited-clinical]] — the abandon-CR view this paper directly rebuts (contradicts).
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 한줄: 서술적 리뷰(초록만): 중심위(Centric Relation, CR)는 재현 가능하고 검증된 진단·전악 재건 기준위이며, 문제는 개념이 아니라 정의·기록법 합의 부재라고 주장하는, "CR 폐기" 주장에 대한 반론.

- `fornai-2022-centric-relation-matter-form-substance` [occlusion] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: Zonnenberg(2021)에 대한 반박 서신으로, "centric relation" 용어는 폐기하되 교합 변경 시 과두 위치를 모니터링해야 한다고 주장하며 대체 개념으로 "Reference Position (RP)"을 제안한다.
  - ▸ 출발(`fornai-2022-centric-relation-matter-form-substance`) 한줄: Zonnenberg(2021)에 대한 반박 서신으로, "centric relation" 용어는 폐기하되 교합 변경 시 과두 위치를 모니터링해야 한다고 주장하며 대체 개념으로 "Reference Position (RP)"을 제안한다.

- `fornai-2022-centric-relation-matter-form-substance` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[occlusion/zonnenberg-2021-centric-relation-critically-revisited-clinical]] — the rebutted review (concludes condylar position can be disregarded in most orthodontic patients); this paper directly contradicts its clinical recommendation.
  - ▸ 출발(`fornai-2022-centric-relation-matter-form-substance`) 한줄: Zonnenberg(2021)에 대한 반박 서신으로, "centric relation" 용어는 폐기하되 교합 변경 시 과두 위치를 모니터링해야 한다고 주장하며 대체 개념으로 "Reference Position (RP)"을 제안한다.

- `zonnenberg-2021-centric-relation-critically-revisited-clinical` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[occlusion/goldstein-2022-centric-relation-needed-reference-position]] — counter-position arguing CR remains a needed reference position (this page contradicts it).
  - ▸ 출발(`zonnenberg-2021-centric-relation-critically-revisited-clinical`) 한줄: 약 70년 문헌을 검토한 서술적 비판 리뷰로, "중심위(CR)" 용어가 의미·개념·실용 모든 면에서 결함이 있어 폐기해야 하며, 건강한 유치악 환자에서는 최대교두감합(MIP)이 턱관절 관계를 결정하고 생물학적으로 수용 가능하다고 결론.

- `lamont-2018-routine-scale-and-polish-periodontal-health` [periodontics] (SOFT→farina-2026-pmpr-biofilm-gingivitis-sr-ma, 'whereas' · 반면(대조))
  - **근거 문장**: - [[periodontics/farina-2026-pmpr-biofilm-gingivitis-sr-ma]] — contrast: PMPR adds benefit as an adjunct to OHI in *established* gingivitis, whereas this review finds no benefit of *routine* prophylaxis in low-risk healthy adults (different population/question).
  - ▸ 출발(`lamont-2018-routine-scale-and-polish-periodontal-health`) 한줄: 중증 치주염이 없는 정기 내원 성인에서 루틴 스케일링·폴리싱(프로필락시스)이 치은염·치주낭 깊이·삶의 질에 2~3년간 거의 차이를 만들지 않는다는 코크란 SR+MA(RCT 2편, 1711명); 치석만 소폭 감소하나 임상적 의미는 불확실.
  - ▸ 대상(`farina-2026-pmpr-biofilm-gingivitis-sr-ma`) 한줄: 치태-유발 치은염에서 구강위생교육(OHI)이 1차 치료이고 전문가 기계적 치태제거(PMPR)는 OHI에 더해질 때만 이득(low certainty)을 주며, 에어폴리싱+초음파가 초음파+러버컵 폴리싱과 동등하면서 더 빠르고, 다이오드 레이저는 부가 이득이 없다는 EFP SR+MA(11편).

- `fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This contradicts the earlier pooled meta-analysis **Rasoolzadeh 2022**, which mixed routes and gingivitis-leaning indices (Plaque/Bleeding/Gingival index) and concluded *in favour* of CoQ10 gel. The disagreement is methodological: pooling routes inflates the apparent gel benefit. For practice, CoQ10 should be presented to patients as low/very-low-certainty, route-dependent, and adjunctive only — n
  - ▸ 출발(`fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr`) 한줄: 10편 RCT 체계적 고찰 — 국소 CoQ10 겔은 효과 없음, 경구 120 mg/일은 12주에 작은 유의 개선(PD −0.41 mm, CAL −0.52 mm). 근거 확실성 very low → 근거기반 권고 불가. 마케팅이 앞서간 영역.

- `fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[periodontics/rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma]] — earlier CoQ10 SR+MA endorsing gel; the direct contradiction (route-pooling artifact).
  - ▸ 출발(`fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr`) 한줄: 10편 RCT 체계적 고찰 — 국소 CoQ10 겔은 효과 없음, 경구 120 mg/일은 12주에 작은 유의 개선(PD −0.41 mm, CAL −0.52 mm). 근거 확실성 very low → 근거기반 권고 불가. 마케팅이 앞서간 영역.

- `jeon-2026-probioticcmu-gingivitis-rct` [periodontics] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: 성인 치은염·초기 치주염 80명 이중맹검 위약대조 RCT: OraCMU/ProbioticCMU 경구 프로바이오틱 정제 8주 복용군이 위약군 대비 치은지수(GI −0.19 vs −0.08, p=.035)와 탐침시 출혈(BOP −7.74 vs −2.82, p=.030)을 유의하게 더 감소시켰고 염증 마커·구강 미생물총을 조절, 중대 이상반응 없음.
  - ▸ 출발(`jeon-2026-probioticcmu-gingivitis-rct`) 한줄: 성인 치은염·초기 치주염 80명 이중맹검 위약대조 RCT: OraCMU/ProbioticCMU 경구 프로바이오틱 정제 8주 복용군이 위약군 대비 치은지수(GI −0.19 vs −0.08, p=.035)와 탐침시 출혈(BOP −7.74 vs −2.82, p=.030)을 유의하게 더 감소시켰고 염증 마커·구강 미생물총을 조절, 중대 이상반응 없음.

- `farina-2026-pmpr-biofilm-gingivitis-sr-ma` [periodontics] (SOFT→lamont-2018-routine-scale-and-polish-periodontal-health, 'whereas' · 반면(대조))
  - **근거 문장**: - [[periodontics/lamont-2018-routine-scale-and-polish-periodontal-health]] — extends: routine prophylaxis has no benefit in low-risk healthy adults, whereas PMPR+OHI helps in *established* gingivitis; together they bracket the indication for professional cleaning.
  - ▸ 출발(`farina-2026-pmpr-biofilm-gingivitis-sr-ma`) 한줄: 치태-유발 치은염에서 구강위생교육(OHI)이 1차 치료이고 전문가 기계적 치태제거(PMPR)는 OHI에 더해질 때만 이득(low certainty)을 주며, 에어폴리싱+초음파가 초음파+러버컵 폴리싱과 동등하면서 더 빠르고, 다이오드 레이저는 부가 이득이 없다는 EFP SR+MA(11편).
  - ▸ 대상(`lamont-2018-routine-scale-and-polish-periodontal-health`) 한줄: 중증 치주염이 없는 정기 내원 성인에서 루틴 스케일링·폴리싱(프로필락시스)이 치은염·치주낭 깊이·삶의 질에 2~3년간 거의 차이를 만들지 않는다는 코크란 SR+MA(RCT 2편, 1711명); 치석만 소폭 감소하나 임상적 의미는 불확실.

- `rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma` [periodontics] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - Serves as the cautionary counterpoint to the route-stratified 2025 SR.
  - ▸ 출발(`rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma`) 한줄: 11편 SR+MA — CoQ10가 치주염 5개 지표를 유의하게 개선(치주낭 SMD −0.96)하며 gel 사용을 권장한다고 결론. 단 이질성 매우 높고(I² 72–89%) 비뚤림 위험 높은 연구에서 효과 과대 → 신뢰도 제한, 신형 route-stratified SR과 충돌.

- `rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[periodontics/fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr]] — newer route-stratified SR finding gel null; the direct contradiction.
  - ▸ 출발(`rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma`) 한줄: 11편 SR+MA — CoQ10가 치주염 5개 지표를 유의하게 개선(치주낭 SMD −0.96)하며 gel 사용을 권장한다고 결론. 단 이질성 매우 높고(I² 72–89%) 비뚤림 위험 높은 연구에서 효과 과대 → 신뢰도 제한, 신형 route-stratified SR과 충돌.

- `dasilveira-2026-subgingival-irrigation-chemical-agents-nspt-sr-ma` [periodontics] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: The bottom line: **adjunctive CA subgingival irrigation provides no additional clinical benefit over NSPT alone** for PPD reduction, CAL gain, or BOP, with evidence rated low to very low (GRADE). This updates and partially overturns Van der Sluijs 2016 (which had reported a slight PVP-I CAL gain not confirmed here). The authors invoke antimicrobial-stewardship: in the absence of demonstrated benef
  - ▸ 출발(`dasilveira-2026-subgingival-irrigation-chemical-agents-nspt-sr-ma`) 한줄: 16편 RCT(712명) SR+MA — NSPT에 약제(PVP-I·CHX·정유·오존수·붕산) 치은연하 세척을 더해도 물/식염수 대비 PPD(MD 0.01mm)·CAL(MD 0.09mm)·BOP에 추가 이득 없음(근거수준 낮음~매우낮음).

- `mucogingival-surgery-apf-fgg-ctg` [periodontics] (HIGH-no-target, '반론' · 반론)
  - **근거 문장**: - **KT "필요 최소치" 논쟁**: 고전적 2mm 각화치은 / 1mm 부착치은 기준은 절대 기준이 아니라는 반론 — 구강위생이 유지되면 KT가 좁아도 부착소실이 진행되지 않는다는 보고. FGG 적응은 수치보다 진행성 퇴축·증상·보철 계획 같은 동적 요인으로 판단하는 흐름. [미검증](원전 미확인, 기억 기반)
  - ▸ 출발(`mucogingival-surgery-apf-fgg-ctg`) 한줄: _(한줄요약 없음 — 페이지 확인 필요)_

- `zini-2026-electric-vs-manual-toothbrush-children-plaque-rct` [periodontics] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: 4주 검사자-맹검 병렬군 RCT (n=60, 6–10세 아동, 이스라엘): 첨단 회전-진동(OR) 전동칫솔(Oral-B iO2)이 수동칫솔보다 전악 치면세균막(TQHPI) 감소가 51% 더 컸고(0.67 vs 0.44; p=0.003), 모든 하위부위(협·설·인접·구치)에서 42–64% 더 큰 감소(p≤0.021)를 보였으며 이상반응은 없었다.
  - ▸ 출발(`zini-2026-electric-vs-manual-toothbrush-children-plaque-rct`) 한줄: 4주 검사자-맹검 병렬군 RCT (n=60, 6–10세 아동, 이스라엘): 첨단 회전-진동(OR) 전동칫솔(Oral-B iO2)이 수동칫솔보다 전악 치면세균막(TQHPI) 감소가 51% 더 컸고(0.67 vs 0.44; p=0.003), 모든 하위부위(협·설·인접·구치)에서 42–64% 더 큰 감소(p≤0.021)를 보였으며 이상반응은 없었다.

- `ramirez-martinez-acitores-2020-antihypertensive-xerostomia-salivary-flow-sr` [oral-medicine] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 2. **Clinical trials (5 studies)**: only Nederfors et al. 2004 assessed xerostomia degree directly, finding thiazide/furosemide groups' xerostomia levels increased vs. stable placebo. Only 1/5 trials found a statistically significant unstimulated whole saliva (UWS) decrease (with an α-/β-adrenergic blocker combination, propranolol+phentolamine); one trial found a statistically significant stimulat
  - ▸ 출발(`ramirez-martinez-acitores-2020-antihypertensive-xerostomia-salivary-flow-sr`) 한줄: 체계적 문헌고찰(PRISMA, 13편: RCT 5편+환자대조군 8편) — 항고혈압제 복용군이 대조군보다 미각/침분비저하(xerostomia/hyposalivation)가 더 심하다는 확증적 근거는 부족하며 전반적 방법론적 질도 낮음; 임상시험은 침분비량 변화가 혼재되고 유의성 없음이 많았으나, 환자대조군 연구는(완전히 일관되지는 않지만) 대체로 항고혈압제군의 침분비량이 낮았음; 연구 이질성으로 어떤 약물군이 가장 침분비저하를 유발하는지 특정 불가.

- `bisla-2022-odontogenic-infections-maxillary-sinus-changes` [oral-medicine] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 2. **Periapical lesion size does not predict mucosal change** severity (p=0.646) — contradicts some prior literature (Nunes et al.) but consistent with others (Aksoy et al.).
  - ▸ 출발(`bisla-2022-odontogenic-infections-maxillary-sinus-changes`) 한줄: 단면연구(213명, 404개 상악동 CBCT)에서 치주골소실이 치근단병소보다 상악동 점막비후의 더 강한 예측인자(OR 2.2)이며 전체 점막변화 유병률 49.5%.

- `sierra-rebolledo-2021-undersized-drilling-immediate-tapered-implants-maxilla` [immediate-implant] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/versah-protocols/rittipakorn-2025-clockwise-osseodensification-primary-stability-cadaveric]] — cadaveric study positioning undersized drilling among primary-stability-enhancing techniques; this RCT contradicts the premise by showing undersizing raises IT but not RFA stability in immediate maxillary implants.
  - ▸ 출발(`sierra-rebolledo-2021-undersized-drilling-immediate-tapered-implants-maxilla`) 한줄: RCT (즉시식립 tapered 임플란트 30개, 상악 전치부; 통상 16 vs 축경 14): 축경(undersized) 드릴링은 1차 안정성을 유의하게 개선하지 못함 — 삽입 토크는 축경군이 약간 높았으나(41.36 vs 38.44 Ncm, p=0.654) RFA/ISQ는 오히려 통상군이 모든 시점에서 더 높았고 12주간 군간 ISQ 차이는 유의하지 않았다.

- `sierra-rebolledo-2021-undersized-drilling-immediate-tapered-implants-maxilla` [immediate-implant] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 골밀도화 시계방향 osteotomy의 cadaveric 1차 안정성 연구 [[wiki/implants/versah-protocols/rittipakorn-2025-clockwise-osseodensification-primary-stability-cadaveric]]는 undersized drilling을 1차 안정성을 높이는 대안 술식으로 함께 논의한다. 이 RCT는 그 대안 술식(undersized drilling)을 즉시식립 상악 전치부에서 직접 검증해, "축경 드릴링이 IT는 올리지만 RFA 안정성은 개선하지 않는다"는 임상 근거를 제공한다 — cadaveric/벤치 모델의 IT↑ 소견을 RCT에서 한정/반박하는 자료.
  - ▸ 출발(`sierra-rebolledo-2021-undersized-drilling-immediate-tapered-implants-maxilla`) 한줄: RCT (즉시식립 tapered 임플란트 30개, 상악 전치부; 통상 16 vs 축경 14): 축경(undersized) 드릴링은 1차 안정성을 유의하게 개선하지 못함 — 삽입 토크는 축경군이 약간 높았으나(41.36 vs 38.44 Ncm, p=0.654) RFA/ISQ는 오히려 통상군이 모든 시점에서 더 높았고 12주간 군간 ISQ 차이는 유의하지 않았다.

- `krishnakumar-2024-hvgic-composite-primary-teeth-sr` [glass-ionomer] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This review compared the clinical effectiveness of high-viscosity GIC (HVGIC) versus direct composite resin (CR) in single- and multi-surface cavities in primary teeth of children aged 3–13. Major databases were searched for publications 2000–2021. Four studies met inclusion (three RCTs, one non-randomized controlled trial). No statistically significant difference between HVGIC and CR was found in
  - ▸ 출발(`krishnakumar-2024-hvgic-composite-primary-teeth-sr`) 한줄: 임상시험 4편 SR — 유치 수복에서 HVGIC와 composite resin 간 통계적 유의차 없음.

- `krishnakumar-2024-hvgic-composite-primary-teeth-sr` [glass-ionomer] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: No statistically significant difference between HVGIC and CR in any included study. Evidence base small; durability findings across the wider literature remain contradictory.
  - ▸ 출발(`krishnakumar-2024-hvgic-composite-primary-teeth-sr`) 한줄: 임상시험 4편 SR — 유치 수복에서 HVGIC와 composite resin 간 통계적 유의차 없음.

- `ge-2023-glass-ionomer-secondary-caries-sr-ma` [caries] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refutes legacy belief that amalgam's metal content provides superior anti-caries effect
  - ▸ 출발(`ge-2023-glass-ionomer-secondary-caries-sr-ma`) 한줄: GIC 수복은 아말감 대비 이차 우식을 유의하게 적게 발생시키고(영구치 RR=0.20, 유치 RR=0.55), 레진 컴포지트와는 동등한 예방 효과를 보였다 (64 RCT 메타분석, 2023).

- `bhandari-2026-saliva-substitute-fluoride-varnish-radiation-caries-rct` [caries] (SOFT→kumar-2026-fluoride-varnish-caries-prevention-cost-effectiveness-sr-ma, 'Whereas' · 반면(대조))
  - **근거 문장**: Extends the fluoride-varnish caries-prevention evidence base in [[wiki/caries/kumar-2026-fluoride-varnish-caries-prevention-cost-effectiveness-sr-ma]] into the high-risk radiation-caries population. Whereas the cost-effectiveness SR+MA addresses general caries prevention, this RCT tests whether fluoride varnish (and/or saliva substitute) actually halts the aggressive DMFS progression seen in irrad
  - ▸ 출발(`bhandari-2026-saliva-substitute-fluoride-varnish-radiation-caries-rct`) 한줄: 3군 무작위대조시험 (방사선 조사 두경부암 환자 482명) — 타액대용제·불소바니시·병용 어느 군에서도 DMFS가 모든 시점에서 유의하게 증가했고 (P<0.05) 군간 차이는 없었다 (본페로니 비유의); 단독·병용 모두 방사선 우식 진행을 막지 못함.
  - ▸ 대상(`kumar-2026-fluoride-varnish-caries-prevention-cost-effectiveness-sr-ma`) 한줄: 23개 경제성평가 연구 SR+MA (836편 스크리닝): 소아 우식예방에서 불소바니시(FV) vs 다른 예방중재의 통합 증분순화폐편익(INMB)이 $124.1 (I²=0%)로 비용효과 차이 없음 — 고소득국 의료공급자/지불자 관점에서 FV의 비용효과는 불확실. (임상효능이 아닌 경제성 분석)

- `kumar-2026-fluoride-varnish-caries-prevention-cost-effectiveness-sr-ma` [caries] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: > **Scope note:** This page concerns **economic cost-effectiveness**, not clinical caries-prevention efficacy. FV's clinical efficacy is documented in other wiki pages and is not contradicted here.
  - ▸ 출발(`kumar-2026-fluoride-varnish-caries-prevention-cost-effectiveness-sr-ma`) 한줄: 23개 경제성평가 연구 SR+MA (836편 스크리닝): 소아 우식예방에서 불소바니시(FV) vs 다른 예방중재의 통합 증분순화폐편익(INMB)이 $124.1 (I²=0%)로 비용효과 차이 없음 — 고소득국 의료공급자/지불자 관점에서 FV의 비용효과는 불확실. (임상효능이 아닌 경제성 분석)

- `jung-2025-flossing-performance-plaque-removal` [interdental-cleaning] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Instruction worked on technique — FPS rose from 2.0 to 2.83 (p<.001), with large gains in correct floss adaptation and vertical movements, and flossing time grew from 60 to 89 seconds. But the cleaning result barely moved: plaque removal was 0.17 (habitual) vs 0.21 (instructed), p=.112, only about 3% more plaque cleared. Crucially, flossing performance was **not correlated** with plaque removed, a
  - ▸ 출발(`jung-2025-flossing-performance-plaque-removal`) 한줄: 전향적 단일 코호트 전후 중재연구(n=37, 젊은 성인): 동영상 교육으로 치실 술식(FPS 2.0→2.83, p<.001)은 향상됐으나 치태 제거량은 개선되지 않았고(PSPI 감소 0.17 vs 0.21, p=.112) 술식 숙련도와도 무관 — 올바른 치실 사용조차 치간 치태를 의미 있게 줄이지 못한다.

- `kim-2023-multichannel-oral-irrigator-periodontal-microbiome-rct` [interdental-cleaning] (SOFT→liu-2025-water-flossing-adjunct-nspt-periodontitis-rct, 'whereas' · 반면(대조))
  - **근거 문장**: This Seoul National University randomized two-group preliminary trial tested whether a **multichannel oral irrigator (MCOI; COMORAL)** — a mouthpiece that fires dozens of water jets simultaneously at the gingival margin, with synchronized suction to prevent aspiration — could protect periodontal health and oral-microbiome ecology under a deliberately harsh **3-day no-brushing challenge**. In healt
  - ▸ 출발(`kim-2023-multichannel-oral-irrigator-periodontal-microbiome-rct`) 한줄: 소규모 예비 무작위대조시험 (Randomized Controlled Trial, RCT; 건강한 성인 29명, 3일 무칫솔질 모델): 다채널 구강세정기 (Multichannel Oral Irrigator, MCOI; COMORAL, 잇몸변연 45° 분사 + 석션)는 치태지수·치은열구출혈지수를 유지하고 탐침시출혈 (Bleeding on Probing, BOP) 비율을 유의하게 낮췄으며, 무세정 대조군의 Prevotella(+114%, p=0.003)·Bacteroidetes(p=0.031) 증가를 
  - ▸ 대상(`liu-2025-water-flossing-adjunct-nspt-periodontitis-rct`) 한줄: 6개월 3군 RCT (n=72, stage I-II 치주염) — 전악 스케일링·치은연하 기구조작(NSPT) 후 매일 가정용 **워터플로싱**이 칫솔질 단독 대비 치태·치주지수를 유의하게 개선하고 치은연하 미생물군(16S rRNA)을 변화시켰으며, **허브 함유 가글** 추가는 미생물군을 더 바꿨으나 워터플로싱 단독 대비 **추가 임상 이득은 없었다**.

- `ren-2023-oral-irrigator-plaque-gingivitis-efficacy-safety-rct` [interdental-cleaning] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: 12주 단일맹검 평행 RCT(치은염 환자 90명; FAS 88) — 수동 칫솔질에 WaterPik 구강세정기(Oral Irrigator, 10–100 psi 조절형)를 더하면 칫솔질 단독보다 치은염(MGI/BI/BOP%, 4주부터·8–12주 모두 p<0.001)과 치태(T-QH, 8주부터 유의)를 유의하게 개선했고, 중대 이상반응·통증·상아질과민증 증가는 없었다.
  - ▸ 출발(`ren-2023-oral-irrigator-plaque-gingivitis-efficacy-safety-rct`) 한줄: 12주 단일맹검 평행 RCT(치은염 환자 90명; FAS 88) — 수동 칫솔질에 WaterPik 구강세정기(Oral Irrigator, 10–100 psi 조절형)를 더하면 칫솔질 단독보다 치은염(MGI/BI/BOP%, 4주부터·8–12주 모두 p<0.001)과 치태(T-QH, 8주부터 유의)를 유의하게 개선했고, 중대 이상반응·통증·상아질과민증 증가는 없었다.

- `thomassen-2025-airfloss-essential-oils-vs-floss-rct` [interdental-cleaning] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: 검사자 맹검 평행 RCT (n=82, 건강 성인, 하악 BOMP ≥25%, 치주염 없음; 3주 실험적 치은염 유도 후 4주 회복): 정유 함유 에어플로스(AFeo) vs 왁스 치실(DF), 둘 다 1일 2회 불소 칫솔질 보조 — 두 군 모두 치은출혈(BOMP)·치면세균막(MPI)·치은마모(GAS) 유의 감소했으나 어느 시점에서도 군간 유의차 없음(p>0.05), 중대 이상반응 없음. AFeo와 왁스 치실은 임상적으로 동등하며 둘 다 안전.
  - ▸ 출발(`thomassen-2025-airfloss-essential-oils-vs-floss-rct`) 한줄: 검사자 맹검 평행 RCT (n=82, 건강 성인, 하악 BOMP ≥25%, 치주염 없음; 3주 실험적 치은염 유도 후 4주 회복): 정유 함유 에어플로스(AFeo) vs 왁스 치실(DF), 둘 다 1일 2회 불소 칫솔질 보조 — 두 군 모두 치은출혈(BOMP)·치면세균막(MPI)·치은마모(GAS) 유의 감소했으나 어느 시점에서도 군간 유의차 없음(p>0.05), 중대 이상반응 없음. AFeo와 왁스 치실은 임상적으로 동등하며 둘 다 안전.

- `thomassen-2025-airfloss-essential-oils-vs-floss-rct` [interdental-cleaning] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[periodontics/tsilingaridis-2026-biofilm-induced-gingivitis-children-adolescents]] — contradicts/qualifies: that EFP/EAPD SR concludes self-performed floss adds little for gingivitis, whereas this RCT shows a powered air-flosser performs *no better* than floss — i.e. neither is a strong adjunct, and equivalence does not imply superiority of the device.
  - ▸ 출발(`thomassen-2025-airfloss-essential-oils-vs-floss-rct`) 한줄: 검사자 맹검 평행 RCT (n=82, 건강 성인, 하악 BOMP ≥25%, 치주염 없음; 3주 실험적 치은염 유도 후 4주 회복): 정유 함유 에어플로스(AFeo) vs 왁스 치실(DF), 둘 다 1일 2회 불소 칫솔질 보조 — 두 군 모두 치은출혈(BOMP)·치면세균막(MPI)·치은마모(GAS) 유의 감소했으나 어느 시점에서도 군간 유의차 없음(p>0.05), 중대 이상반응 없음. AFeo와 왁스 치실은 임상적으로 동등하며 둘 다 안전.

- `hardan-2022-treatment-tooth-wear-using-direct` [prosthetic-materials] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Tooth wear is a common clinical problem with no standardized treatment protocol. This PRISMA 2020 systematic review (search up to 29 April 2022 across PubMed/MedLine, Scopus, ISI Web of Science, Scielo, EMBASE) asked whether **direct or indirect restorations** give better clinical outcomes for treating worn dentition. From 2776 records, 16 clinical studies (RCTs and observational) were included fo
  - ▸ 출발(`hardan-2022-treatment-tooth-wear-using-direct`) 한줄: 치아 마모(tooth wear) 수복에서 직접 vs 간접 수복을 비교한 체계적 문헌고찰(16편 임상연구, 최대 10년 추적, PRISMA 2020): 이질성이 높아 메타분석은 불가했고, 어떤 수복 기법·재료도 임상 성적에서 우월하다는 근거는 없었다.

- `varvara-2020-retightening-preload-loss-abutment-screws` [prosthetic-materials] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 1. **Optimal retightening window is 2 minutes**, not 5 or 10 minutes (contradicts most prior in vitro guidance).
  - ▸ 출발(`varvara-2020-retightening-preload-loss-abutment-screws`) 한줄: 체외 연구(내·외부 육각 각 40개, 35 Ncm): 초기 조임 후 2분 재조임이 전조임 소실을 가장 효과적으로 감소시켰으며, 5분·10분·비재조임 대비 유의한 차이(P<0.05).

- `scheffel-2015-transdentinal-cytotoxicity-glutaraldehyde-odontoblast` [dentin-hypersensitivity] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Using artificial pulp chambers with dentin discs, this study measured whether glutaraldehyde — the active in Gluma-type desensitizers — diffuses across dentin to harm odontoblast-like cells. Glutaraldehyde-containing treatments reduced MDPC-23 viability in a concentration-dependent fashion, confirming transdentinal cytotoxicity. The findings provide the mechanistic safety counterpoint to glutarald
  - ▸ 출발(`scheffel-2015-transdentinal-cytotoxicity-glutaraldehyde-odontoblast`) 한줄: In vitro 경상아질 모델: 글루타르알데히드 함유 탈감작제가 농도 의존적으로 치수측 오도노블라스트 유사세포 생존율을 감소시킴.

- `rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety` [local-anesthesia] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: [근거중간] A single-blinded RCT at the University of Barcelona Dental Hospital randomized 68 patients (34/arm) undergoing upper third molar extraction to receive, or not receive, a standardized verbal explanation of **The Wand** — a computerized, pressure-regulated, footswitch-activated local anesthesia delivery system — before injection. All patients received identical anesthesia (The Wand, supraperi
  - ▸ 출발(`rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety`) 한줄: 단일맹검 RCT (n=68, 바르셀로나, 상악 제3대구치 발치): The Wand 컴퓨터 제어 마취 시스템 작동원리에 대한 상세 구두 설명이 불안(ISAR/MDAS/DFS/STAI-S)이나 통증(VAS)을 유의하게 줄이지 못함; 술중 재마취 필요율(42.6%)은 불안도와 무관했으나 수술시간 증가와는 유의한 관련(p=0.007).

- `rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety` [local-anesthesia] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: - Contradicts prior literature suggesting information/explanation reduces dental fear (Wang, Heaton) — authors note the format/amount of information (and specifically its target: an unfamiliar computerized device with sounds/beeps) may behave differently from general procedural information.
  - ▸ 출발(`rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety`) 한줄: 단일맹검 RCT (n=68, 바르셀로나, 상악 제3대구치 발치): The Wand 컴퓨터 제어 마취 시스템 작동원리에 대한 상세 구두 설명이 불안(ISAR/MDAS/DFS/STAI-S)이나 통증(VAS)을 유의하게 줄이지 못함; 술중 재마취 필요율(42.6%)은 불안도와 무관했으나 수술시간 증가와는 유의한 관련(p=0.007).

- `rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety` [local-anesthesia] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[behavioral-dentistry/dental-anxiety/appukuttan-2016-strategies-manage-dental-anxiety-phobia]] — narrative review proposing a stepwise dental-anxiety management framework where patient information/communication is an early-line strategy; this RCT provides a specific negative/contradicting data point for the "information reduces anxiety" component of that framework in the context of computerized
  - ▸ 출발(`rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety`) 한줄: 단일맹검 RCT (n=68, 바르셀로나, 상악 제3대구치 발치): The Wand 컴퓨터 제어 마취 시스템 작동원리에 대한 상세 구두 설명이 불안(ISAR/MDAS/DFS/STAI-S)이나 통증(VAS)을 유의하게 줄이지 못함; 술중 재마취 필요율(42.6%)은 불안도와 무관했으나 수술시간 증가와는 유의한 관련(p=0.007).

- `cabral-2026-comparative-efficacy-anesthetic-techniques-periodontal` [local-anesthesia] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 바늘없는/컴퓨터제어 압력 침윤마취기(Wand-type computerized delivery system) 관련 질의 대응 목적으로 인제스트. 기존 [[local-anesthesia/wambier-2017-intrapocket-topical-versus-injected-anesthetic-srp]] (SR+MA)는 SRP에서 injected anesthetic이 topical gel보다 통증강도·rescue 필요성에서 우위라고 결론지었는데, 본 RCT(Cabral 2026)는 통증 강도 자체는 두 기법이 동등하다고 보고해 부분적으로 상충하며, 대신 "보충마취 필요성"이라는 secondary outcome에서 컴퓨터제어 침습기법의 우위(24% vs 100%, p<0.001)를 명확히 정량화해 기존 근거를 정제
  - ▸ 출발(`cabral-2026-comparative-efficacy-anesthetic-techniques-periodontal`) 한줄: 평행·맹검 RCT(n=76), 비외과적 치주기구조작 시 컴퓨터제어 침습마취 vs 비침습 리도카인/프릴로카인 겔 비교: 통증강도(NRS-11)는 두 군 유사했으나, 비침습 겔군은 100%가 보충마취 필요 vs 컴퓨터제어군 24%만 필요(p<0.001); 혈역학은 양 군 모두 안정.

- `uzbelger-feldman-2024-buffered-anesthetic-without-epinephrine-invivo` [local-anesthesia] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: [claude해석] This sits **upstream** of the clinical buffered-lidocaine RCTs in the wiki — those buffer a *conventional* LW/E cartridge chairside to improve onset/comfort; this paper instead designs a *vasoconstrictor-free* buffered product whose duration comes from osmolality/viscosity. It is positioned as `contradicts` to the epinephrine-concentration framing of [[drug/karm-2017-lidocaine-epinephri
  - ▸ 출발(`uzbelger-feldman-2024-buffered-anesthetic-without-epinephrine-invivo`) 한줄: In-vivo(Sprague-Dawley 랫드) 개발 연구 — 에피네프린 없는 완충 2% lidocaine 제형(LW/O/E "Sample 3A": 락테이트 링거 + 덱스트로스 + 아미노산 쓴맛차단제, pH 6.7–7.0, 590–610 mOsm/kg)이 점도·주사성·마취 지속시간(꼬리튕김·핫플레이트 잠복기)에서 상용 2% lidocaine+1:100,000 에피네프린(LW/E)과 동등, 쓴맛 감소·일시적 경미 홍반/부종만 관찰.

- `karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb` [local-anesthesia] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[local-anesthesia/subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric]] — pediatric RCT reporting benzocaine > lignocaine; this stricter triple-blind RCT finds no agent difference (contradicts)
  - ▸ 출발(`karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb`) 한줄: 삼중맹검 RCT(소아 45명, 6-10세): IANB에서 8% lidocaine 겔이 20% benzocaine·5% EMLA보다 우월하지 않음 — FLACC·Wong-Baker FACES·맥박 모두 유의차 없음.

- `karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb` [local-anesthesia] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 소아 IANB 전 표면마취제 3종(8% lidocaine, 20% benzocaine, 5% EMLA) 비교 triple-blind RCT. [[local-anesthesia/subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric]]가 benzocaine > lignocaine 우위를 보고한 것과 대비되는 "차이 없음" 결과를 더 엄격한 blinding으로 제시하므로, 표면마취제 제제 선택의 임상적 의미를 재검토하는 근거가 된다.
  - ▸ 출발(`karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb`) 한줄: 삼중맹검 RCT(소아 45명, 6-10세): IANB에서 8% lidocaine 겔이 20% benzocaine·5% EMLA보다 우월하지 않음 — FLACC·Wong-Baker FACES·맥박 모두 유의차 없음.

- `li-2023-articaine-lidocaine-adverse-effects-pediatric-ma` [local-anesthesia] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: 8개 RCT(articaine 470명 vs lidocaine 441명, 3–13세) SR+MA: 소아치과에서 4% articaine과 2% lidocaine의 전체 이상반응 위험에 차이 없음(RR 1.08, 95% CI 0.54–2.15, p=0.83), I²=57%, GRADE "moderate".
  - ▸ 출발(`li-2023-articaine-lidocaine-adverse-effects-pediatric-ma`) 한줄: 8개 RCT(articaine 470명 vs lidocaine 441명, 3–13세) SR+MA: 소아치과에서 4% articaine과 2% lidocaine의 전체 이상반응 위험에 차이 없음(RR 1.08, 95% CI 0.54–2.15, p=0.83), I²=57%, GRADE "moderate".

- `subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric` [local-anesthesia] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 소아 IANB 전 표면마취제 선택(lignocaine vs benzocaine)의 통증 감소 효과를 다룬 소규모 RCT. [[local-anesthesia/karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb]]가 동일 비교(lidocaine·benzocaine·EMLA, IANB)를 더 엄격한 triple-blind RCT로 수행하므로, 본 연구는 그 비교군의 짝 근거이자 대비점(상충 결과)을 제공한다.
  - ▸ 출발(`subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric`) 한줄: RCT(소아 40명, 6-10세): IANB 전 20% benzocaine 겔이 2% lignocaine 겔보다 주사 통증을 유의하게 더 줄임(4점 척도 1.2 ± 0.6 vs 2.1 ± 0.5, P<0.05).

- `al-obaida-2019-comparison-perceived-pain-patients-satisfaction` [local-anesthesia] (SOFT→ramanathan-2023-efficacy-reliability-single-tooth-anesthesia, 'whereas' · 반면(대조))
  - **근거 문장**: - [[local-anesthesia/ramanathan-2023-efficacy-reliability-single-tooth-anesthesia]] — companion STA evidence in a surgical (impacted third-molar extraction) context, comparing WANDSTA STA against IANB; that trial found faster onset but higher supplemental-block need and higher intra-operative VAS during elevation, whereas this trial finds STA's advantage concentrated in post-injection procedural c
  - ▸ 출발(`al-obaida-2019-comparison-perceived-pain-patients-satisfaction`) 한줄: RCT(n=80): 상악 구치부 수복치료에서 컴퓨터 제어 단일치아마취(Single Tooth Anesthesia, STA) 시스템과 전통적 침윤마취를 비교한 결과, 주사 시 통증(p=0.59)과 수축기혈압(p=0.09)은 유의차가 없었으나, 수복치료 중 STA군의 통증이 유의하게 낮았고(p<0.001) 치료 경험 만족도와 향후 재선호도도 STA가 유의하게 높았음(p=0.04). 다만 STA군의 심박수는 기저치부터 이미 높았고 전 구간에서 유의하게 상승.
  - ▸ 대상(`ramanathan-2023-efficacy-reliability-single-tooth-anesthesia`) 한줄: RCT(n=60): 매복 하악 제3대구치 외과적 발치에서 WANDSTA 컴퓨터 제어 단일치아마취(치주인대내 주사, 4% articaine)가 전통적 IANB(4% articaine) 대비 발현 시간이 2.2(±0.25)분 더 빠르고(p<0.05) 술후 통증·개구제한은 낮았으나, 장협신경 추가블록 필요율이 더 높았고(50% vs 23.3%) 발치 시 VAS는 더 높았음.

- `de-menezes-torres-2025-chatgpt-oral-maxillofacial-surgery` [artificial-intelligence] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: This is the LLM (text-reasoning) counterpoint to the image-diagnosis CNN papers: unlike 2D cephalometric landmarking — which already clears its clinical bar — LLMs are usable for communication/documentation drafting but not for autonomous complex decisions, mirroring the staged-adoption framing of the AI overview.
  - ▸ 출발(`de-menezes-torres-2025-chatgpt-oral-maxillofacial-surgery`) 한줄: 구강악안면외과 ChatGPT 체계적 문헌고찰(10편): GPT-4는 객관식 76.8%·동의서 작성·환자 소통에서 우수(전공의 능가)하나 약리·복잡 임상결정에서는 미흡 — 인간 판단의 보조일 뿐 대체 불가. (Based on articles retrieved from PubMed; abstract-only)

- `restorative-margin-periodontal-interface-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Axis 2 — Margin location, and the Ercoli-vs-Schätzle tension.** Srimaneepong (2022) states the default cleanly: supragingival (and equigingival) margins permit hygiene and do not provoke caries or periodontal disease, whereas subgingival margins impede hygiene and risk biologic-width violation. The apparent conflict is between two reviews/cohorts. **Ercoli (2021)** — a systematically-searched na
  - ▸ 출발(`restorative-margin-periodontal-interface-overview`) 한줄: 7편 종합 — 수복 변연과 치주의 관계는 ① 생물학적 폭경/SCTA 존중(~2 mm, Hamasni 임상값 1.13 mm로 부위 편차 큼), ② 변연 위치(치은연상 최선, 치은연하는 탁월한 위생 시에만), ③ 변연 적합·외형(부적합·overhang이 biofilm→골소실 cascade 유발), ④ finish line 디자인(수평 vs 수직 BOPT) 4축의 상호작용 결과이며, Ercoli(통제 위생) vs Schätzle(실제 장기 위생)의 외관상 충돌은 위생 조건 차이로 해소된다.

- `drug-analgesics-postop-pain-overview` [overviews] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: > - 단, **술전 corticosteroid는 매복 제3대구치에서 명확히 유효** — 술전 dexamethasone 4mg 근육주사 1회가 위약 대비 통증·개구량·부종 모두 개선(Tamgadge 2025 split-mouth RCT, n=60, day7 VAS 0.4 vs 1.6 p<0.001). NSAID-preemptive 무효(Costa)와 대비되는, 제3대구치 술전 약제의 핵심 옵션.
  - ▸ 출발(`drug-analgesics-postop-pain-overview`) 한줄: 치과 술후 통증 1차 선택은 **Ibuprofen 400mg + Acetaminophen 1000mg 병용** — Network MA에서 가장 낮은 NNT (~1.5). Opioid는 비-opioid 대비 우월하지 않으며 부작용·중독 위험 → 회피. Preemptive NSAID는 third molar에선 약하나 치주·임플란트엔 효과 있고, 술전 dexamethasone은 third molar에 명확히 유효. 근관치료는 시간대 의존 — Diclofenac+APAP·Ketorolac이 6–8h 최강

- `drug-analgesics-postop-pain-overview` [overviews] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: > - 이상반응(Adverse Event, AE)에서 NSAID를 "위험"으로 내리지 말 것 — 제3대구치 단회 NSAID 단독이 SUCRA 안전성 최하위지만 **위약이 2위**라 노세보(nocebo, 부정적 기대) 효과가 주된 기전; AE는 경미·일시적 오심 수준(Magesty 2026 NMA, 28 RCT n=5,306, 확실성 매우 낮음~낮음). 효능 우위가 단회 AE를 압도 → NSAID 1차 유지.
  - ▸ 출발(`drug-analgesics-postop-pain-overview`) 한줄: 치과 술후 통증 1차 선택은 **Ibuprofen 400mg + Acetaminophen 1000mg 병용** — Network MA에서 가장 낮은 NNT (~1.5). Opioid는 비-opioid 대비 우월하지 않으며 부작용·중독 위험 → 회피. Preemptive NSAID는 third molar에선 약하나 치주·임플란트엔 효과 있고, 술전 dexamethasone은 third molar에 명확히 유효. 근관치료는 시간대 의존 — Diclofenac+APAP·Ketorolac이 6–8h 최강

- `drug-analgesics-postop-pain-overview` [overviews] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: [근거중간] **Tamgadge 2025 RCT** (split-mouth single-blind, n=60, 양측 매복 하악 제3대구치) — preemptive **corticosteroid는 third molar에 명확히 유효**. 술전 dexamethasone 4mg 근육주사 1회가 위약 대비 day2·day7 통증(VAS day7 0.4 vs 1.6, p<0.001), 개구량(3.5 vs 2.7 cm, p<0.001), day7 부종(2.1 vs 2.8 cm, p=0.04) 모두 개선, 이상반응 없음. **NSAID-preemptive 무효(Costa)와의 핵심 차이** — 제3대구치 술전 약제는 NSAID가 아니라 corticosteroid가 정답. (Abusamak 2025 약동학 설명과 일치: 
  - ▸ 출발(`drug-analgesics-postop-pain-overview`) 한줄: 치과 술후 통증 1차 선택은 **Ibuprofen 400mg + Acetaminophen 1000mg 병용** — Network MA에서 가장 낮은 NNT (~1.5). Opioid는 비-opioid 대비 우월하지 않으며 부작용·중독 위험 → 회피. Preemptive NSAID는 third molar에선 약하나 치주·임플란트엔 효과 있고, 술전 dexamethasone은 third molar에 명확히 유효. 근관치료는 시간대 의존 — Diclofenac+APAP·Ketorolac이 6–8h 최강

- `drug-analgesics-postop-pain-overview` [overviews] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: ### 6-0. 단회투여 이상반응은 대부분 nocebo (만성 위해와 구분)
  - ▸ 출발(`drug-analgesics-postop-pain-overview`) 한줄: 치과 술후 통증 1차 선택은 **Ibuprofen 400mg + Acetaminophen 1000mg 병용** — Network MA에서 가장 낮은 NNT (~1.5). Opioid는 비-opioid 대비 우월하지 않으며 부작용·중독 위험 → 회피. Preemptive NSAID는 third molar에선 약하나 치주·임플란트엔 효과 있고, 술전 dexamethasone은 third molar에 명확히 유효. 근관치료는 시간대 의존 — Diclofenac+APAP·Ketorolac이 6–8h 최강

- `drug-analgesics-postop-pain-overview` [overviews] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: - 전체 사망률 **51%**. SJS/TEN은 가장 치명적인 중증피부이상반응(Severe Cutaneous Adverse Reaction, SCAR)이다.
  - ▸ 출발(`drug-analgesics-postop-pain-overview`) 한줄: 치과 술후 통증 1차 선택은 **Ibuprofen 400mg + Acetaminophen 1000mg 병용** — Network MA에서 가장 낮은 NNT (~1.5). Opioid는 비-opioid 대비 우월하지 않으며 부작용·중독 위험 → 회피. Preemptive NSAID는 third molar에선 약하나 치주·임플란트엔 효과 있고, 술전 dexamethasone은 third molar에 명확히 유효. 근관치료는 시간대 의존 — Diclofenac+APAP·Ketorolac이 6–8h 최강

- `keratinized-mucosa-peri-implant-health-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 6. **Apparent contradictions between Ravidà's TSA-null results and the positive MBL signals from Zhang 2025 and Sabri 2025 are resolvable by study design differences, not biological inconsistency.** Ravidà 2022 restricted to interventional designs with comparison arms (1 RCT, 3 non-RCTs, 5 prospective cohorts) to avoid reverse-causation bias — this is methodologically correct but drastically limit
  - ▸ 출발(`keratinized-mucosa-peri-implant-health-overview`) 한줄: 10편 종합(우산 2, SR+MA 3, 전향 1, 전문가합의 2, SR 1, 서술고찰 1): 각화점막 폭 ≥2 mm 역치는 치태·염증·점막퇴축(OR 2.78–eOR 5.34) 연관성이 가장 강하고 일관되며, 임플란트주위염·변연골소실과의 연관성은 방향성은 존재하나 근거 수준이 낮거나 TSA상 미확정이고, 유리치은이식(FGG)은 표준 증대술식으로 이식 후에도 원발 각화점막에 상응하는 20년 보호 효과를 유지한다.

- `veneer-preparation-design-minimally-invasive-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: 4. **Minimal-prep veneers (0.2–0.5 mm) equal or exceed conventional (0.3–1.0 mm) in survival.** Ali (2023), SR of 4 comparative studies, refuting prior assumption of conventional superiority; ultra-thin contact-lens feldspathic types add no-anesthesia / no-temporary benefits. [SR — no comparative RCT]
  - ▸ 출발(`veneer-preparation-design-minimally-invasive-overview`) 한줄: 6편 종합(전향 임상 1·SR 1·SR+MA 1·내러티브 1·증례 2): 최소침습 비니어 삭제는 목업/APT를 통과해 최종 보철 형태 기준으로 시행하고 삭제량은 기질-목표색 차이로 정량화(P = LT − EV)하며, 아날로그(Gürel 2007)→색 수식(Coachman 2014)→디지털 CAD-CAM(Cattoni 2016)으로 진화 — 법랑질 한정 변연을 지키는 한 최소/무삭제가 통상 삭제와 동등 이상.

- `interdental-cleaning-devices-synthesis` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **올바른 술식조차 치실 효능을 살리지 못한다(Jung 2025, 전향 n=37)**: 동영상 교육으로 치실 술식(Flossing Performance Score, FPS 2.0→2.83, p<.001)은 향상됐으나 치태 제거(PSPI 차이 0.17 vs 0.21, p=.112)는 개선되지 않았고 술식과 무관 — "치실은 기술만 가르치면 된다"는 통념을 반박, DF를 좁은 접촉 한정으로 두는 결정을 보강.
  - ▸ 출발(`interdental-cleaning-devices-synthesis`) 한줄: 치간 청소도구 8편 종합(+토스픽법 overview) — 치실·치간칫솔·구강세정기/워터픽·나무이쑤시개 비교: **보편적 우승 도구는 없고 순응도가 도구보다 중요**. 치간칫솔이 들어가는 공간이면 1순위(Carrouel 2026 임신치은염 BOP 56%→12%, OR 3.14), 치실은 좁은 접촉 한정(에어플로스·세정기와 동등), 워터픽은 변연출혈·치주염 보조엔 강하나 교정·임플란트 부가는 이점 없음, 나무 이쑤시개는 치간유두 위해로 회피.

- `interdental-cleaning-devices-synthesis` [overviews] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: > - **일반 인구에서 칫솔질 보조로 효과적·안전(Ren 2023, RCT n=90, 12주)**: WaterPik 추가가 칫솔질 단독보다 치은염(4주부터)·치태(8주부터) 유의 개선, 압력-출혈 용량반응, 중대 이상반응·통증·상아질과민증·치은퇴축 없음 — 일반인구 효능+안전 공백을 메움.
  - ▸ 출발(`interdental-cleaning-devices-synthesis`) 한줄: 치간 청소도구 8편 종합(+토스픽법 overview) — 치실·치간칫솔·구강세정기/워터픽·나무이쑤시개 비교: **보편적 우승 도구는 없고 순응도가 도구보다 중요**. 치간칫솔이 들어가는 공간이면 1순위(Carrouel 2026 임신치은염 BOP 56%→12%, OR 3.14), 치실은 좁은 접촉 한정(에어플로스·세정기와 동등), 워터픽은 변연출혈·치주염 보조엔 강하나 교정·임플란트 부가는 이점 없음, 나무 이쑤시개는 치간유두 위해로 회피.

- `abutment-screw-preload-joint-stability-overview` [overviews] (SOFT→varvara-2020-retightening-preload-loss-abutment-screws, 'challenges the' · 도전)
  - **근거 문장**: - [[prosthetic-materials/varvara-2020-retightening-preload-loss-abutment-screws]] — retightening-interval study: 2 min minimized preload loss better than 5/10 min (challenges the 10-min standard); internal hex retains more preload than external hex at every interval.
  - ▸ 출발(`abutment-screw-preload-joint-stability-overview`) 한줄: 임플란트 어버트먼트 나사 체결부에 관한 18편 종합. 나사 풀림(최다 기계적 합병증; 5년 ~10.4%, 10년 ~20.8%)의 원인은 전하중 손실이며, 기전은 세틀링(무하중에서도 2–10%)과 동적 피로(총 제거토크 손실 16.1–39%) 둘이다. 마찰·나사산 조도가 핵심 레버(Bulaqi 2015; Sagheb 2023 — 탄소코팅 나사 10회 재사용 시 머리 마찰↑로 전하중 329.9→253.7 N 감소, 재사용 금지), 재조임이 세틀링을 보상하되 최적 시점은 논쟁적(10분: Nithyapr
  - ▸ 대상(`varvara-2020-retightening-preload-loss-abutment-screws`) 한줄: 체외 연구(내·외부 육각 각 40개, 35 Ncm): 초기 조임 후 2분 재조임이 전조임 소실을 가장 효과적으로 감소시켰으며, 5분·10분·비재조임 대비 유의한 차이(P<0.05).

- `sinus-lift-lateral-2026-synthesis` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **점막비후(Mucosal Thickening, MT)의 원인은 치성·치주성** — MT 자체는 임플란트 금기가 아님(Maska 2017: 93%에 MT·65%가 >5mm여도 임플란트·이식 생존율 100%, 치주질환 과거력만 유일 예측인자 p=0.004). 무엇이 MT를 만드는가는 정량화됨: Khalil 2024(992치)에서 치근단병소(보정교차비 AOR 32.7)·제1대구치(AOR 3.97)·중증치주염(AOR 2.75)이 독립 예측인자이고, **발치된 부위가 MT 위험 최저** → 치아의 존재 자체가 MT의 odontogenic 동력. 잔존치조골높이(Residual Ridge Height, RRH)가 낮을수록 MT 심함(Akbari 2022, 240동 — RRH↓↔MT↑ 역상관; 단 Maska 20
  - ▸ 출발(`sinus-lift-lateral-2026-synthesis`) 한줄: 측방창 (Lateral Window) 상악동거상술 (Sinus Floor Elevation, SFE)에서 슈나이더 막 (Schneiderian Membrane) 천공 (Sinus Membrane Perforation, SMP)과 부비동염 (Sinusitis) 예방·관리를 다룬 34편에 이식재 선택 및 PRF (Platelet-Rich Fibrin) 보조 근거 3편을 추가해 총 37편으로 확장한 종합 페이지 — L-PRF·A-PRF 보조 시 신생골 +7~11% 유의 증가, BCP가 DBBM 대비 신

- `sinus-lift-lateral-2026-synthesis` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **What drives mucosal thickening — odontogenic and periodontal sources.** Mucosal thickening (MT) is overwhelmingly a marker of adjacent tooth/periodontal disease rather than a primary sinus disorder, which reframes it as a preoperative *risk-stratification* finding rather than a contraindication. Maska 2017 (retrospective CBCT, n=29, mean follow-up 3.3 yr) found 93.1% of sinuses had MT (65.5% s
  - ▸ 출발(`sinus-lift-lateral-2026-synthesis`) 한줄: 측방창 (Lateral Window) 상악동거상술 (Sinus Floor Elevation, SFE)에서 슈나이더 막 (Schneiderian Membrane) 천공 (Sinus Membrane Perforation, SMP)과 부비동염 (Sinusitis) 예방·관리를 다룬 34편에 이식재 선택 및 PRF (Platelet-Rich Fibrin) 보조 근거 3편을 추가해 총 37편으로 확장한 종합 페이지 — L-PRF·A-PRF 보조 시 신생골 +7~11% 유의 증가, BCP가 DBBM 대비 신

- `periodontal-host-modulation-nutraceutical-adjuncts-overview` [periodontics] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: > - **CoQ10 — 구형 SR과의 충돌**: 기존 11편 SR+MA는 CoQ10가 5개 지표를 유의 개선(PD SMD −0.96)하며 **겔 사용을 권장**한다고 결론했으나, 이질성 매우 높고(I² 72–89%) 비뚤림 위험 높은 연구에서 효과가 과대평가됨 (Rasoolzadeh 2022). → 두 SR의 상반된 결론은 RoB·route 층화로 설명됨; 신형 SR이 우선.
  - ▸ 출발(`periodontal-host-modulation-nutraceutical-adjuncts-overview`) 한줄: 기계적 치주치료에 더하는 숙주조절·영양보조제(오메가-3·CoQ10·항산화 비타민·ASU·MMP 억제) 7편 종합: 모두 통계적으로는 검출되나 1 mm 미만·low~very-low 확실성의 PD/CAL 이득에 그치고, 양성 메타분석이 가이드라인(EFP 오메가-3 반대) 및 서로(CoQ10 경로·비뚤림)와 충돌하며, 임상적으로 의미있는 효과는 단독 보충제가 아니라 재생수술에 병용한 국소 독시사이클린(NNT=2.73)에서만 나온다 — 기계적 치석제거가 비타협 기반.

- `periodontal-host-modulation-nutraceutical-adjuncts-overview` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Reconciliation:** the contradiction (gel recommended vs gel inert) is an artifact of pooling high-RoB trials without route stratification. Prefer the newer route-stratified appraisal; treat any CoQ10 claim as very-low certainty.
  - ▸ 출발(`periodontal-host-modulation-nutraceutical-adjuncts-overview`) 한줄: 기계적 치주치료에 더하는 숙주조절·영양보조제(오메가-3·CoQ10·항산화 비타민·ASU·MMP 억제) 7편 종합: 모두 통계적으로는 검출되나 1 mm 미만·low~very-low 확실성의 PD/CAL 이득에 그치고, 양성 메타분석이 가이드라인(EFP 오메가-3 반대) 및 서로(CoQ10 경로·비뚤림)와 충돌하며, 임상적으로 의미있는 효과는 단독 보충제가 아니라 재생수술에 병용한 국소 독시사이클린(NNT=2.73)에서만 나온다 — 기계적 치석제거가 비타협 기반.

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: > - 이 페이지의 핵심 명제: 치조제 보존술(Alveolar Ridge Preservation, ARP)은 보편 권고가 아니라 **시나리오 의존적 개입**이며, "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나"를 다루는 do-ARP의 짝(counterpoint) 페이지다.
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 한줄: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Synthesis (counterpoint to the do-ARP protocol-ladder page) organizing ~20 unsynthesized bone-regeneration papers across 5 axes — socket healing biology, ARP critical appraisal (when NOT to graft), ARP-then-implant failure predictors, adjunct materials, and beyond-ARP scenarios. Core thesis: Alveolar Ridge Preservation (ARP) is a scenario-dependent intervention, not a universal recommendation — po
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 한줄: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: 본 페이지는 wiki/bone-regeneration/ 의 20 개 미합성 paper (생물학 기초·비판적 review·실패 예측인자·보조 재료·인접 시나리오) 를 5축으로 재분류한 spine. Protocol-ladder 페이지의 do-ARP 흐름에 대한 counterpoint — clinical paralysis 가 아닌 patient-specific 결정 도구로 사용.
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 한줄: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "즉시식립이면 골 보존된다" — Araujo 2005 반박. 즉시식립도 협측 붕괴 막지 못함.
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 한줄: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "Flapless 발치가 ridge 를 보존한다" — Araujo 2009 반박. flap 유무가 흡수 크기를 거의 안 바꿈.
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 한줄: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: **손상된(damaged) socket 의 biologic 보강 — Kim 2020 · Park 2022 (Yonsei 비글견)**: 위 adjunct 논의는 대체로 intact socket 가정인데, 두 Yonsei 동물 study 는 **2벽 결손/손상 socket** 의 생물학적 보강을 직접 다룬다. Kim 2020(비글견 n=5, split-mouth)은 rhBMP-2 의 적용 **timing** 을 분리 — CBCP 에 BMP-2 를 즉시 적용한 군이 2주 지연 주입군보다 신생골 면적이 유의하게 컸다(10.8 vs 6.3 mm², p=0.043; 폭경 차이 없음). 초기 염증은 즉시군에서 더 강했으나 결과를 악화시키지 않아, "염증 가라앉은 뒤 지연 주입이 낫다"는 가설을 반박하고 **손상 sock
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 한줄: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [ ] 본 페이지는 do-ARP 의 counterpoint. 새 critical review · 새 failure predictor study ingest 시 갱신.
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 한줄: 발치 socket 자연 치유 생물학 (Araujo·Cardaropoli·Schropp 고전 axis) + 치조제 보존술 (Alveolar Ridge Preservation, ARP) 의 한계·실패·과잉치료 비판 axis 를 합성. [[bone-regeneration-protocol-ladder]] (do-ARP) 의 counterpoint 페이지 — "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나" 의 spine.

- `drug-antibiotic-stewardship-overview` [overviews] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: - 통합 이상반응 비율: 0.21 (95% CI: 0.13–0.28, I²=0%)
  - ▸ 출발(`drug-antibiotic-stewardship-overview`) 한줄: 치과 항생제 처방의 1차 원칙은 **제한 (restrictive)** — 감염성 심내막염 (Infective Endocarditis, IE) 고위험군·면역저하·IV BP·방사선 두경부·매복 발치·임플란트 일부에 한정. 단순 발치·치근단치주염(Apical Periodontitis)에는 prophylaxis 효과 없음. 1차 선택은 Amoxicillin (최저 부작용·치명률), Clindamycin은 회피. 치주 깊은 낭에는 전신 대신 국소 전달 항생제 우선. ---

- `socket-shield-technique-overview` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: Synthesis of 17 wiki pages plus 4 abstract-level 2021–2025 reviews/RCTs on the Socket Shield Technique (SST): pooled SR/MA + RCTs converge on superior buccal-bone and pink-esthetic preservation (BBPR ~0.32 vs ~1.05 mm, MBL ~0.39 vs ~1.00 mm, PES +1.3), but evidence is dominated by case reports, long-term (≥5y) data are thin, a 4–17% shield-related complication rate restricts SST to experienced ope
  - ▸ 출발(`socket-shield-technique-overview`) 한줄: 소켓실드 기법(Socket Shield Technique, SST) 17개 페이지 + 초록 수준 신규 4편 종합. SR/MA + RCT가 협측 골판·핑크 심미 보존 우월로 수렴(협측 골판 흡수 BBPR 약 0.32 vs 1.05 mm, 변연골 소실 MBL 약 0.39 vs 1.00 mm, 핑크 심미 점수 PES +1.3). 단 근거 다수가 증례보고이고 장기(≥5년) 데이터 부족, 실드 관련 합병증 4–17%로 숙련자·선별 심미부 증례에 한정. 신규 FEA는 잔존 실드가 주위골 응력 집중을 최대화함

- `socket-shield-technique-overview` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: A 2026-06-28 update folds in four further reviews/RCTs at **abstract level only** (full text not yet retrieved, so no point estimates are imported — direction-of-effect citations only): **Brazyte 2025** (SR+MA, *Stomatologija*, PMID 41628481) as a newer pooled estimate of SST vs conventional; **Gurbuz 2024** (RCT, *Int J Oral Maxillofac Surg*, PMID 39648089) testing the shield in a **non-grafted**
  - ▸ 출발(`socket-shield-technique-overview`) 한줄: 소켓실드 기법(Socket Shield Technique, SST) 17개 페이지 + 초록 수준 신규 4편 종합. SR/MA + RCT가 협측 골판·핑크 심미 보존 우월로 수렴(협측 골판 흡수 BBPR 약 0.32 vs 1.05 mm, 변연골 소실 MBL 약 0.39 vs 1.00 mm, 핑크 심미 점수 PES +1.3). 단 근거 다수가 증례보고이고 장기(≥5년) 데이터 부족, 실드 관련 합병증 4–17%로 숙련자·선별 심미부 증례에 한정. 신규 FEA는 잔존 실드가 주위골 응력 집중을 최대화함

- `zirconia-types-clinical-selection` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: **오판 패턴**: "유약이 매끄러워서 마모 적다" — Shah 2024 + Steiner 2024 직접 반박. 유약이 첫 layer 마모 후 거친 표면 노출. [근거강함]
  - ▸ 출발(`zirconia-types-clinical-selection`) 한줄: 치과용 지르코니아 grade 선택의 5축 spine — (1) 결정학·강도-투명도 trade-off 기초, (2) grade × 적응증 매트릭스, (3) 두께-파절 임계값, (4) 대합치 마모, (5) 접착·표면처리 차이. [[dental-materials-decision-ladder]] 축 2 의 sub-overview, [[dental-materials-decision-ladder]] Phase 2 stub 의 첫 실현.

- `zirconia-types-clinical-selection` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: **오판 패턴**: "5Y-PSZ 는 cubic 이라 MDP 약하다" — Comba 2021 반박. Cubic 도 hydroxyl group 노출되어 MDP 반응. [근거강함]
  - ▸ 출발(`zirconia-types-clinical-selection`) 한줄: 치과용 지르코니아 grade 선택의 5축 spine — (1) 결정학·강도-투명도 trade-off 기초, (2) grade × 적응증 매트릭스, (3) 두께-파절 임계값, (4) 대합치 마모, (5) 접착·표면처리 차이. [[dental-materials-decision-ladder]] 축 2 의 sub-overview, [[dental-materials-decision-ladder]] Phase 2 stub 의 첫 실현.

- `resin-dentin-bond-durability-degradation-overview` [overviews] (SOFT→talungchit-2014-ethanol-wet-bonding-chlorhexidine-resin-dentin-durability, 'However, the' · 그러나(단서))
  - **근거 문장**: Ethanol-wet bonding (replacing water with ethanol before hydrophobic resin) plus CHX improves in-vitro durability ([[resin-bonding/talungchit-2014-ethanol-wet-bonding-chlorhexidine-resin-dentin-durability]]). However, the "moist dentin" dogma is weakening clinically: across 5 split-mouth NCCL RCTs, **dry vs wet etch-and-rinse bonding showed no difference** in retention or sensitivity ([[resin-bond
  - ▸ 출발(`resin-dentin-bond-durability-degradation-overview`) 한줄: 위키 15편 종합: 레진-상아질 결합은 친수성수지 가수분해 + MMP/cathepsin 콜라겐분해(잔류 물이 매개, nanoleakage/water-tree)로 열화하며, 대응 전략(에탄올습윤·MMP억제·가교·MDP nanolayer·재광화·conditioner)은 모두 "물 제거·효소 차단·콜라겐 보존"으로 수렴 — MDP·습윤접착의 in-vitro 우월성은 임상서 약화.
  - ▸ 대상(`talungchit-2014-ethanol-wet-bonding-chlorhexidine-resin-dentin-durability`) 한줄: 에탄올 습식 접착(ethanol-wet bonding, EW)이 수습식(water-wet bonding, WW)보다 소수성 단량체를 혼성층(hybrid layer)에 더 깊이 침투시켜 즉시·노화 후 미세인장결합강도(microtensile bond strength, μTBS)를 높였고, 클로르헥시딘(chlorhexidine, CHX)을 더하면 1년 후 콜라겐 보존·나노누출(nanoleakage) 감소가 향상되는 in-vitro 벤치 연구 (초록만 확보).

- `resin-dentin-bond-durability-degradation-overview` [overviews] (SOFT→forville-2024-moist-dentin-adhesive-systems-reevaluation, 'However, the' · 그러나(단서))
  - **근거 문장**: Ethanol-wet bonding (replacing water with ethanol before hydrophobic resin) plus CHX improves in-vitro durability ([[resin-bonding/talungchit-2014-ethanol-wet-bonding-chlorhexidine-resin-dentin-durability]]). However, the "moist dentin" dogma is weakening clinically: across 5 split-mouth NCCL RCTs, **dry vs wet etch-and-rinse bonding showed no difference** in retention or sensitivity ([[resin-bond
  - ▸ 출발(`resin-dentin-bond-durability-degradation-overview`) 한줄: 위키 15편 종합: 레진-상아질 결합은 친수성수지 가수분해 + MMP/cathepsin 콜라겐분해(잔류 물이 매개, nanoleakage/water-tree)로 열화하며, 대응 전략(에탄올습윤·MMP억제·가교·MDP nanolayer·재광화·conditioner)은 모두 "물 제거·효소 차단·콜라겐 보존"으로 수렴 — MDP·습윤접착의 in-vitro 우월성은 임상서 약화.
  - ▸ 대상(`forville-2024-moist-dentin-adhesive-systems-reevaluation`) 한줄: 체계적 문헌고찰+메타분석 (분할구강 RCT 5편, 환자 195명, 비우식성 치경부 병소, 최대 5년 추적): 산부식-수세 (Etch-and-Rinse, ER) 전략에서 건조 접착 vs 습윤 접착 간 유지율·술후 과민증에 유의한 차이 없음 (GRADE 중등도 확실성).

- `resin-dentin-bond-durability-degradation-overview` [overviews] (SOFT→zheng-2024-dentin-conditioners-bond-strength-sr, 'However, the' · 그러나(단서))
  - **근거 문장**: Ethanol-wet bonding (replacing water with ethanol before hydrophobic resin) plus CHX improves in-vitro durability ([[resin-bonding/talungchit-2014-ethanol-wet-bonding-chlorhexidine-resin-dentin-durability]]). However, the "moist dentin" dogma is weakening clinically: across 5 split-mouth NCCL RCTs, **dry vs wet etch-and-rinse bonding showed no difference** in retention or sensitivity ([[resin-bond
  - ▸ 출발(`resin-dentin-bond-durability-degradation-overview`) 한줄: 위키 15편 종합: 레진-상아질 결합은 친수성수지 가수분해 + MMP/cathepsin 콜라겐분해(잔류 물이 매개, nanoleakage/water-tree)로 열화하며, 대응 전략(에탄올습윤·MMP억제·가교·MDP nanolayer·재광화·conditioner)은 모두 "물 제거·효소 차단·콜라겐 보존"으로 수렴 — MDP·습윤접착의 in-vitro 우월성은 임상서 약화.
  - ▸ 대상(`zheng-2024-dentin-conditioners-bond-strength-sr`) 한줄: SR+MA (정성 23편, 정량 15편, random-effects SMD): 산 기반 (acid-based) 상아질 조정제 (dentin conditioner)는 건·습 본딩 모두에서 장기 레진-상아질 결합 내구성을 유의하게 향상시켰고, 선택적 섬유외 탈회 (selective extrafibrillar demineralization) 조정제는 건식 본딩에서 결합강도를 높였다 (P<.001).

- `occlusal-veneer-tooth-wear-erosion-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 피로(fatigue) vs 정적파절 순위 상충: maldonado는 3편 중 2편 복합레진 피로 우위, al-akhali는 세라믹 정적 우위, schlichting은 복합레진 표면 열화(거칠기 p=.003)↑ — 피로·정적·표면내구성 순위가 갈림.
  - ▸ 출발(`occlusal-veneer-tooth-wear-erosion-overview`) 한줄: 교합면 비니어 7편 종합: 초박형 세라믹은 구치 교합력을 상회하고 재료(세라믹 vs 복합레진)는 생존율에 무의미하나, 최소두께(0.5~1.0mm)는 기질·재료·이악물기에 따라 논쟁적이며 표면처리는 모노본드 Etch&Prime≥HF≫APF, 위치(후방)가 유일 유의 실패인자이고 실패는 대개 수리가능한 chipping임.

- `occlusal-veneer-tooth-wear-erosion-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 3. **The minimum-thickness threshold is unsettled between 0.5 and 1.0 mm and depends on substrate.** Sasse et al. (2015) found only the 0.7/1.0 mm group survived undamaged (100%), while thin 0.3/0.6 mm enamel-only fell to 12.5% survival — arguing a 0.7/1.0 mm minimum. Essam et al. (2023) validated 0.5 mm LD (fracture loads 962–1277 N with APF/HF/Monobond) as sufficient for molar forces, and Maldon
  - ▸ 출발(`occlusal-veneer-tooth-wear-erosion-overview`) 한줄: 교합면 비니어 7편 종합: 초박형 세라믹은 구치 교합력을 상회하고 재료(세라믹 vs 복합레진)는 생존율에 무의미하나, 최소두께(0.5~1.0mm)는 기질·재료·이악물기에 따라 논쟁적이며 표면처리는 모노본드 Etch&Prime≥HF≫APF, 위치(후방)가 유일 유의 실패인자이고 실패는 대개 수리가능한 chipping임.

- `occlusal-veneer-tooth-wear-erosion-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: - **피로 vs 정적파절 vs 표면내구성 순위 상충**: maldonado(복합레진 피로 우위) vs al-akhali(세라믹 정적 우위) vs schlichting(복합레진 표면 열화). 어느 실패양식이 임상 지배인지 미해결.
  - ▸ 출발(`occlusal-veneer-tooth-wear-erosion-overview`) 한줄: 교합면 비니어 7편 종합: 초박형 세라믹은 구치 교합력을 상회하고 재료(세라믹 vs 복합레진)는 생존율에 무의미하나, 최소두께(0.5~1.0mm)는 기질·재료·이악물기에 따라 논쟁적이며 표면처리는 모노본드 Etch&Prime≥HF≫APF, 위치(후방)가 유일 유의 실패인자이고 실패는 대개 수리가능한 chipping임.

- `endodontic-access-cavity-decision-tree` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - MIA(닌자 와동·트러스 와동)는 치관 구조 보존이 목표이나, 파절 저항성 향상 근거가 상충·불확실하고 임상 RCT 없음; 오히려 잔류 debris↑·근관구 탐지↓·천공 위험↑(Kapetanaki 2021, Dioguardi 2024) → 숙련 술자의 단순 단근관 케이스에서만 선택적.
  - ▸ 출발(`endodontic-access-cavity-decision-tree`) 한줄: 정상 해부학 → TEC(전통 직선 접근) 표준; 보존 MIA는 근거 불충분; 석회화(PCO)·복잡 해부 → 유도 근관치료(정적 3D 가이드 또는 동적 실시간 내비게이션) 적용. ---

- `endodontic-access-cavity-decision-tree` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: | **파절 저항성** | 표준 | 상충 근거 (일부 향상, 일부 무관) | 유지 |
  - ▸ 출발(`endodontic-access-cavity-decision-tree`) 한줄: 정상 해부학 → TEC(전통 직선 접근) 표준; 보존 MIA는 근거 불충분; 석회화(PCO)·복잡 해부 → 유도 근관치료(정적 3D 가이드 또는 동적 실시간 내비게이션) 적용. ---

- `endodontic-access-cavity-decision-tree` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: | 치아 파절 저항성 향상 | 상충 (일부 향상, 일부 무관) | 불확실 |
  - ▸ 출발(`endodontic-access-cavity-decision-tree`) 한줄: 정상 해부학 → TEC(전통 직선 접근) 표준; 보존 MIA는 근거 불충분; 석회화(PCO)·복잡 해부 → 유도 근관치료(정적 3D 가이드 또는 동적 실시간 내비게이션) 적용. ---

- `c-shaped-canal-anatomy-prevalence-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The individual population CBCT studies in this collection mostly **corroborate** the spine and, where they deviate, the deviation is explained by population, tooth choice, or counting method rather than by contradicting the underlying biology:
  - ▸ 출발(`c-shaped-canal-anatomy-prevalence-overview`) 한줄: 12편(CBCT 101편 SR+MA 1, 인구별 CBCT 횡단연구 7, 서술적 리뷰 1, 횡단 형태 분석 1, 증례 2)을 종합하면 C형 근관 유병률은 치아종류 구배(하악 제2대구치 17.3% 최다 → 상악 제1대구치 0.8% 최소), 아시아 우세 지역 구배, 일관된 여성 우세로 결정되며, 대구치는 Fan C2형이 우세하고, 협·설측 radicular-groove의 얇은 벽(최소 0.26 mm)이 strip-perforation 위험을 만들며, 치료의 핵심은 CBCT·현미경·초음파 isthmus 

- `c-shaped-canal-anatomy-prevalence-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Deviating high (counting method)**: the Indian overall 22% (Singh 2022) is inflated by **per-patient (not per-tooth)** reporting and Melton-based classification, a caveat that explains the apparent excess without contradicting the spine.
  - ▸ 출발(`c-shaped-canal-anatomy-prevalence-overview`) 한줄: 12편(CBCT 101편 SR+MA 1, 인구별 CBCT 횡단연구 7, 서술적 리뷰 1, 횡단 형태 분석 1, 증례 2)을 종합하면 C형 근관 유병률은 치아종류 구배(하악 제2대구치 17.3% 최다 → 상악 제1대구치 0.8% 최소), 아시아 우세 지역 구배, 일관된 여성 우세로 결정되며, 대구치는 Fan C2형이 우세하고, 협·설측 radicular-groove의 얇은 벽(최소 0.26 mm)이 strip-perforation 위험을 만들며, 치료의 핵심은 CBCT·현미경·초음파 isthmus 

- `c-shaped-canal-anatomy-prevalence-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **3. Anticipate asymmetry along the root and the heuristic of contralateral symmetry.** Shemesh 2017: 55% unilateral and config changes along the root in 63% — so the orifice does not predict the apex, and one side does not guarantee the other within a tooth. Yet at the *patient* level, Yousefi 2025's non-significant side difference and Abdalrahman's predominantly bilateral mandibular pattern supp
  - ▸ 출발(`c-shaped-canal-anatomy-prevalence-overview`) 한줄: 12편(CBCT 101편 SR+MA 1, 인구별 CBCT 횡단연구 7, 서술적 리뷰 1, 횡단 형태 분석 1, 증례 2)을 종합하면 C형 근관 유병률은 치아종류 구배(하악 제2대구치 17.3% 최다 → 상악 제1대구치 0.8% 최소), 아시아 우세 지역 구배, 일관된 여성 우세로 결정되며, 대구치는 Fan C2형이 우세하고, 협·설측 radicular-groove의 얇은 벽(최소 0.26 mm)이 strip-perforation 위험을 만들며, 치료의 핵심은 CBCT·현미경·초음파 isthmus 

- `implant-surface-comparison` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: **갱신 메모 (2026-06-26)**: 이번 갱신의 핵심은 **본 overview가 명시했던 두 가지 "부재" 갭이 충전**된 것 — (1) UV-PF 임상 SR+MA(Lang 2022), (2) SLA vs SLActive 직접 비교 RCT(Vílchez 2025). 임상 권장 자체는 불변(SLA 표준·친수성 D3/D4·UV-PF 위축골)이나, **근거의 질이 한 단계 상승**했고 두 신규 근거 모두 thesis를 반박이 아닌 보강 방향으로 정렬한다: UV-PF는 "절대 안정성"이 아니라 "안정성 도달 속도(OSI)"를 높이고(Lang), SLActive는 SLA 대비 절대 우위가 아니라 특정 시나리오 한정(Vílchez). 남은 갭은 SLA·SLActive·CA **3자 동시 비교** 다기관 RCT.
  - ▸ 출발(`implant-surface-comparison`) 한줄: **SLA = 임상 표준**, **친수성 (SLActive/CA) = D3/D4 골에서 stability dip 제거**, **UV 광기능화 (Photofunctionalization) = 위축골·복잡증례에서 ISQ +21.9 상승 (7년 100% 성공)**, **골밀도화 (Osseodensification, OD) = 표면이 아닌 술기 — TSFE에서 ISQ 우위**; 표면처리의 핵심 기전은 친수성보다 **탄화수소 (Hydrocarbon) 제거를 통한 생물학적 노화 (Biological Agin

- `antiseptic-mouthrinse-chlorhexidine-essential-oil-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **EO의 미생물 "reset" (단, 이해상충 주의)**: spike-in 절대정량 메타게놈 RCT에서 EO 가글이 4주 만에 이상증식(dysbiosis) 치태를 건강 조성으로 전환, 치은염 ≥37% 감소 — 단 Johnson & Johnson 후원 연구로 해석 주의 (Min 2024). 기전은 광범위 살균 후 건강 상재균 우선 재정착.
  - ▸ 출발(`antiseptic-mouthrinse-chlorhexidine-essential-oil-overview`) 한줄: 항균 가글 7편 종합(치주+구강미생물 교차). 가글은 기계적 위생의 보조일 뿐 PD/CAL은 개선 못 함. ①효능순위 — EO ≥ CHX ≥0.10% ≈ triclosan(Figuero NMA). ②치태억제 1위 = CHX(Cochrane SMD −1.45). ③CHX 농도 — 0.12% 표준이나 0.05%도 유효, "농도 우열 근거 없음". ④CHX 아킬레스건 = 착색(SMD +1.07) → 단기 한정. ⑤EO = 무착색 + 미생물 친화(12주 안전, dysbiosis reset). ⑥수술후 =

- `complaint-management-pipeline-classification-expectation-response-education` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: | Gillespie 2025 | Respond | Mixed methods | online responses | 6 defensive tactics from contradictory demands | cross-sectional |
  - ▸ 출발(`complaint-management-pipeline-classification-expectation-response-education`) 한줄: 환자 민원을 (1) 분류하고 (2) 민원인이 무엇을 기대하는지 파악하고 (3) 방어적이지 않게 대응하며 (4) 그 역량을 교육으로 정착시키는 4단계 파이프라인. 일반 healthcare 근거 + 치과 적용층으로 구성.

- `cold-plasma-endodontic-disinfection-synthesis` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 최고 임상근거 & 한계: Lyu 2025 — 수중방전 플라즈마 (Underwater Discharge Plasma, UDP) vs 6% NaOCl 최초 사람 RCT 파일럿(n=28, 4개월). 통증(VAS)·치근단 치유(PAI) 동등, 부작용 0, 임피던스(>5000 Ω) 자동차단 안전장치 검증. 단 치유율 71.4% vs 92.9%(NS, 검정력 0.65로 과소검정)·기관-기기 이해상충·미생물 종결점 부재 — 임상 도입 전 대규모·장기 RCT 필수. [claude해석: 전체 근거는 in-vitro 편중, 임상은 단일 파일럿]
  - ▸ 출발(`cold-plasma-endodontic-disinfection-synthesis`) 한줄: 근관소독용 냉대기압 플라즈마(CAP)/비열 플라즈마 7편(in-vitro 5·리뷰 1·RCT 1) 통합. 플라즈마는 40°C 이하에서 ROS/RNS를 생성해 E. faecalis 바이오필름을 열·화학독성·내성 없이 사멸; 직접 ≥8–12분이면 성숙 바이오필름 완전 제거(Li 2015 12분 0 CFU, Armand 2019 ~5.2 log). Ca(OH)₂보다 우수하나 NaOCl(속도·완전성)·TAP에는 미달(Kumar 2023, Asnaashari 2022), NaOCl/CHX와 병용 시 시너지

- `oral-mucositis-cancer-therapy-overview` [overviews] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: > - **저출력레이저(Low-Level Laser Therapy, LLLT)는 소아 풀링에서 효과 없음**(RR=0.99) — 성인/타 점막질환 데이터와 대비되는 핵심 반전. 단 통증(pain) 완화에서는 보조적 언급.
  - ▸ 출발(`oral-mucositis-cancer-therapy-overview`) 한줄: 항암치료 유발 구강점막염 논문 3편(소아 SR 2편 + 성인 두경부암 방사선 RCT 1편) 종합: 메타분석으로 지지되는 유일 약제는 국소 꿀(중증 소아 OM 입원 −4.33일)이고 LLLT는 소아 풀링서 무효(RR=0.99); 약제는 목표 결과지표별로 선택(발생률→클로르헥시딘, 기간→꿀, 통증→올리브유), 성인 방사선 OM에는 L-아르기닌·L-글루타민 모두 대조군보다 우수하고 아르기닌이 글루타민에 비열등 — 단 전반적 근거는 이질성이 커 확정 프로토콜엔 불충분.

- `oral-mucositis-cancer-therapy-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **팔리퍼민(palifermin, 재조합 KGF):** 발생률·중증도·지속기간 모두 감소(급성백혈병) — 그러나 **안전성 보고가 상충**, 무비판적 적용 금지.
  - ▸ 출발(`oral-mucositis-cancer-therapy-overview`) 한줄: 항암치료 유발 구강점막염 논문 3편(소아 SR 2편 + 성인 두경부암 방사선 RCT 1편) 종합: 메타분석으로 지지되는 유일 약제는 국소 꿀(중증 소아 OM 입원 −4.33일)이고 LLLT는 소아 풀링서 무효(RR=0.99); 약제는 목표 결과지표별로 선택(발생률→클로르헥시딘, 기간→꿀, 통증→올리브유), 성인 방사선 OM에는 L-아르기닌·L-글루타민 모두 대조군보다 우수하고 아르기닌이 글루타민에 비열등 — 단 전반적 근거는 이질성이 커 확정 프로토콜엔 불충분.

- `gbr-barrier-membrane-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Scope limitation of Darby 2024**: a 5×3 mm anterior maxillary dehiscence defect is a self-contained, small-volume defect. The membrane-positive findings in Friedmann 2022 (more new bone with RCLC vs NCM) pertain to larger chronic horizontal defects — a different geometry and healing challenge. These findings are complementary, not contradictory: in small contained dehiscence defects, membrane se
  - ▸ 출발(`gbr-barrier-membrane-overview`) 한줄: 12편(서술적 고찰 3·동물 5·임상 전향 1·체계적 고찰 1·벤치 1) 종합 — GBR 차폐막은 흡수성/비흡수성이라는 단일 상류 변수로 분기하며, 가교화 전략이 콜라겐막의 16–24주 차단기능 충족 여부를 결정한다; 차세대 '프로그래머블 인터페이스'(금속-페놀 전기방사막으로 구현)와 임상 진입한 합성 흡수성막(노출 0건의 3D PLGA)이 현재 최전선이다. ---

- `direct-resin-restoration-adhesion-placement-overview` [overviews] (SOFT→tay-2003-dentin-adhesives-hydrophilic, 'disagree' · 불일치)
  - **근거 문장**: **Reading the disagreement**: Hong 2021 (general restorations) and Assis 2023 (NCCL) favor E&R; Doshi 2023 (NCCL, more recent search) finds no difference. The Oza 2022 RCT — which Doshi/Assis postdate — is the cleanest signal: **universal adhesive in pure SE mode failed at 24 months on cervical lesions**, while selective-enamel-etch (SLE) and full E&R modes did not. The mechanism is the establishe
  - ▸ 출발(`direct-resin-restoration-adhesion-placement-overview`) 한줄: 일반 직접 컴포짓 수복의 두 축 종합 — ① 접착방식: 법랑질 가장자리가 있으면 선택적 법랑질 산부식 또는 3-step EAR이 SR+MA·RCT에서 일관되게 우세, 유니버설 SE 단독은 NCCL 24개월 RCT에서 임상 부적합; ② 충전방식: 벌크필과 적층충전은 9 RCT MA·12 RCT NMA·우산형 리뷰 모두에서 임상 동등, "저수축 = 임상 우월" 명제는 21 RCT MA로 부정. 둘 다 "재료 선택"보다 "프로토콜 실행"이 결과를 좌우.
  - ▸ 대상(`tay-2003-dentin-adhesives-hydrophilic`) 한줄: 서술적 리뷰(Tay & Pashley 2003): 간편화된 자가산부식 접착제일수록 과도한 친수성 → 수분 투과·수포 형성·결합 열화; 3단계 산부식 시스템이 가장 안정적

- `direct-resin-restoration-adhesion-placement-overview` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: ### Critical / counterpoint
  - ▸ 출발(`direct-resin-restoration-adhesion-placement-overview`) 한줄: 일반 직접 컴포짓 수복의 두 축 종합 — ① 접착방식: 법랑질 가장자리가 있으면 선택적 법랑질 산부식 또는 3-step EAR이 SR+MA·RCT에서 일관되게 우세, 유니버설 SE 단독은 NCCL 24개월 RCT에서 임상 부적합; ② 충전방식: 벌크필과 적층충전은 9 RCT MA·12 RCT NMA·우산형 리뷰 모두에서 임상 동등, "저수축 = 임상 우월" 명제는 21 RCT MA로 부정. 둘 다 "재료 선택"보다 "프로토콜 실행"이 결과를 좌우.

- `periodontal-adjunctive-therapy-probiotics-pdt-overview` [periodontics] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: This **updates and partially overturns Van der Sluijs 2016**, which had reported a slight PVP-I CAL gain not confirmed here. da Silveira frames the negative finding under **antimicrobial-stewardship**: with no demonstrated benefit and given CHX tolerance/resistance concerns, routine adjunctive subgingival irrigation is not supported. The MD of ~0.01–0.09 mm sits *below* even the ~0.3 mm John 2017 
  - ▸ 출발(`periodontal-adjunctive-therapy-probiotics-pdt-overview`) 한줄: NSPT/SRP 보조요법 2026년 프로바이오틱스·이중광 aPDT RCT를 2017 NMA 벤치마크와 종합: 모든 보조요법의 추가 CAL 이득은 ~0.3 mm에 불과하고, 프로바이오틱스는 BoP와 PPD ≥5 mm 부위를 개선하되 CAL은 미개선, 가정용 이중광 aPDT는 기존 구강위생에 추가적 치태 감소를 제공하며, 아직 우월한 단일 보조요법은 없다.

- `periodontal-adjunctive-therapy-probiotics-pdt-overview` [periodontics] (HIGH-no-target, 'Counterpoint' · 반대 논점)
  - **근거 문장**: ### "Clean and Seal" (AA-NaOCl + Cross-linked HA) — the Positive Counterpoint (Jungbauer 2026)
  - ▸ 출발(`periodontal-adjunctive-therapy-probiotics-pdt-overview`) 한줄: NSPT/SRP 보조요법 2026년 프로바이오틱스·이중광 aPDT RCT를 2017 NMA 벤치마크와 종합: 모든 보조요법의 추가 CAL 이득은 ~0.3 mm에 불과하고, 프로바이오틱스는 BoP와 PPD ≥5 mm 부위를 개선하되 CAL은 미개선, 가정용 이중광 aPDT는 기존 구강위생에 추가적 치태 감소를 제공하며, 아직 우월한 단일 보조요법은 없다.

- `narrow-diameter-implants-clinical-outcomes-overview` [overviews] (SOFT→witek-2021-surgical-instrumentation-narrow-wide-short-implants, 'whereas' · 반면(대조))
  - **근거 문장**: - **Drilling protocol optimisation for narrow implants.** [[implants/witek-2021-surgical-instrumentation-narrow-wide-short-implants]] (in-vivo sheep, 144 plateau-root-form implants, 3.5 mm narrow vs. 6.0 mm wide, 3 × 2 factorial RPM × irrigation design) shows that irrigation is most critical for narrow implants at low speed (50 RPM BIC: 30.6 ± 6.1% with irrigation vs. 19.7 ± 6.1% without; signific
  - ▸ 출발(`narrow-diameter-implants-clinical-outcomes-overview`) 한줄: SR/MA 4편(전치부 상악·구치부 고정성 보철·하악 피개의치·TiZr 단일크라운) 종합 — 좁은 직경 임플란트(NDI, <3.75 mm)는 정규 직경(RDI)과 생존율·변연골소실(MBL)이 동등하고 환자보고결과(PROM)·심미 합병증에서는 오히려 우위. 선택 기준은 생존율 손해가 아니라 "골증대 회피"다.
  - ▸ 대상(`witek-2021-surgical-instrumentation-narrow-wide-short-implants`) 한줄: 양 12마리에 협소경(3.5 mm)·광경(6.0 mm) 단단 임플란트 144개를 식립한 동물실험으로, 수냉이 BIC에 미치는 영향은 직경·회전속도에 따라 달라지며 BAFO는 치유 기간에 의해서만 유의한 차이를 보임.

- `black-stain-caries-protection-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Surfaces the **microbiome controversy**: Actinomyces-dominance (pediatric/culture/16S) vs Capnocytophaga/Neisseria-dominance (adult permanent/NGS) — a method- and age-dependent split, not a contradiction to be averaged away
  - ▸ 출발(`black-stain-caries-protection-overview`) 한줄: 치아 흑색착색(Black Stain, BS) 6편 종합. BS는 세균 H₂S + 타액 Fe³⁺ → 황화철(FeS) 외인성 치경부 착색이며 우식과 일관된 역상관(SR+MA OR 0.67). ①착색기전 = Fe/S 화학 + 식이 chromogen. ②우식역상관 = OR 0.67·우식치 −0.98개(Mousa), 성인·취학전 모두 재확인. ③미생물 = 소아는 Actinomyces 우점이나 성인 영구치 NGS는 Capnocytophaga/Neisseria 우점(Çelik) — "Actinomyces 단독

- `diabetic-patient-immediate-implant-decision` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **The contradiction that shapes the answer.** Andrade 2021 (SR+MA, 5 quantitative studies) found **no survival penalty** for immediately *loaded* implants in type 2 DM — even in uncontrolled (high-HbA1c) patients (RR 1.08, 95% CI 0.87–1.33). Taken alone, this reads as "HbA1c is not a gate." But Al-Ansari 2022 — the largest meta-analysis (89 studies, 68,290 implants) — reports a real diabetic failu
  - ▸ 출발(`diabetic-patient-immediate-implant-decision`) 한줄: 당뇨 환자 즉시식립 가부를 여러 논문으로 종합한 페이지: DM은 절대 금기가 아니며, 결정은 **HbA1c 밴드(<8%/8–9%/≥9%)** 와 **부위(상악은 당뇨 실패 유의, 하악은 비유의)** 로 갈린다 — 두 SR+MA는 단기·하악 생존에선 일치하나 상악·장기 위험에선 충돌한다.

- `veneer-material-survival-protocol-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: 4. **Minimally invasive veneers (0.2–0.5 mm) demonstrate equal or superior survival to conventional preparations (0.3–1.0 mm).** Ali (2023), a SR of 4 comparative studies, found MPVs showed higher survival rates and longer mean success periods than CVs, refuting the prior assumption of conventional preparation superiority. Ultra-thin contact-lens feldspathic veneers (0.2–0.3 mm) additionally elimi
  - ▸ 출발(`veneer-material-survival-protocol-overview`) 한줄: 라미네이트 비니어 10편 종합 (SR+MA 5편 포함): 소재별 생존율은 유사하나 합병증 부담은 LDS가 가장 낮고 (기술적 합병증 6.1% vs 장석 41.48%@10년), 접착 기질·제작기법·HF 에칭 시간이 결합강도를 결정하는 핵심 변수임.

- `gothic-arch-jaw-relation-recording-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **정확도(reference 대비 일치) 위계는 reference에 따라 뒤집힌다**: 무치악 split-cast 검증에서는 **nick-and-notch(0.15/0.23mm) < 구내 고딕아치(0.42/0.51) < 구외 고딕아치(0.74/0.86)** 로 정적(static) 왁스기록이 최소 오차 (Singh 2026). 즉 GAT은 **재현성은 최고지만 정적 기준 대비 오차는 더 큼** — "재현성 ≠ 정확도"의 핵심 모순.
  - ▸ 출발(`gothic-arch-jaw-relation-recording-overview`) 한줄: 고딕아치(arrow-point) 트레이싱과 수평 악간관계(중심위) 기록 7편 종합 — **재현성**(디지털 고딕아치 ~0.98·체위무관 > 턱끝유도 > 삼킴; 양손조작 ≥ 턱끝유도)과 **기준 대비 정확도**(무치악 split-cast에서 nick-and-notch < 구내 고딕아치 < 구외 고딕아치)를 분리하고, 오차의 **방향**(고딕아치=전방, 턱후퇴=후방, 모두 ±1mm 내)과 **구내>구외** 우위, OPG의 교합기 프로그래밍 대체 가능성, 그리고 단발 기록→10년 안정 기능위 확장을 정

- `gothic-arch-jaw-relation-recording-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Here the two non-GAT-friendly results live, and they are not contradictions but different *reference standards*:
  - ▸ 출발(`gothic-arch-jaw-relation-recording-overview`) 한줄: 고딕아치(arrow-point) 트레이싱과 수평 악간관계(중심위) 기록 7편 종합 — **재현성**(디지털 고딕아치 ~0.98·체위무관 > 턱끝유도 > 삼킴; 양손조작 ≥ 턱끝유도)과 **기준 대비 정확도**(무치악 split-cast에서 nick-and-notch < 구내 고딕아치 < 구외 고딕아치)를 분리하고, 오차의 **방향**(고딕아치=전방, 턱후퇴=후방, 모두 ±1mm 내)과 **구내>구외** 우위, OPG의 교합기 프로그래밍 대체 가능성, 그리고 단발 기록→10년 안정 기능위 확장을 정

- `pdrn-dentistry-evidence-synthesis` [overviews] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: > - 안전성 양호(농도의존 세포독성 없음, 이상반응 HA 동등) → **저비용·저위험 보조**로서는 합리적이나 1차 재생치료나 표준 graft 대체 근거로는 미흡.
  - ▸ 출발(`pdrn-dentistry-evidence-synthesis`) 한줄: PDRN(폴리데옥시리보뉴클레오티드, Polydeoxyribonucleotide) 치과 적용 17편 종합 — 기전(A2A 아데노신 수용체 + 뉴클레오티드 구제경로)은 탄탄하다. 근거가 둘로 갈린다: **진통·항염** 효과는 human 근거가 가장 강하고(치과 RCT 1 + TMJ 후향코호트 1 + 비치과 SR/MA 2), **재생** 효과는 전부 animal·in vitro이며 zone·outcome 한정 + 시간적으로 초기 전엽(early acceleration 후 종점에서 격차 축소)이다. 초기

- `pdrn-dentistry-evidence-synthesis` [overviews] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: 6. **안전성 프로파일은 양호 — 저위험 adjunct로서의 합리성** — In vitro에서 농도 의존적 세포독성 없음(Lee 2024), 기전이 항염. 비치과 RCT 합성에서도 이상반응이 HA와 차이 없음(Kim 2019, RR 2.15, P=0.55). downside가 작아 "저비용·저위험 보조"로서의 사용은 합리적이나, 1차 재생치료로 청구하거나 표준 graft를 대체하는 근거로 쓰기엔 미흡. [claude해석]
  - ▸ 출발(`pdrn-dentistry-evidence-synthesis`) 한줄: PDRN(폴리데옥시리보뉴클레오티드, Polydeoxyribonucleotide) 치과 적용 17편 종합 — 기전(A2A 아데노신 수용체 + 뉴클레오티드 구제경로)은 탄탄하다. 근거가 둘로 갈린다: **진통·항염** 효과는 human 근거가 가장 강하고(치과 RCT 1 + TMJ 후향코호트 1 + 비치과 SR/MA 2), **재생** 효과는 전부 animal·in vitro이며 zone·outcome 한정 + 시간적으로 초기 전엽(early acceleration 후 종점에서 격차 축소)이다. 초기

- `computerized-needle-free-anesthesia-delivery-overview` [overviews] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: - 성인 대상 대형 5-arm RCT(Küçükkurt)와 소아 crossover(Garret-Bernardin)의 상반된 결과를 같은 프로토콜로 직접 비교하는 연구 부재 — 연령·주사부위(구개 vs 협측)가 진짜 조절변수인지 확인 필요.
  - ▸ 출발(`computerized-needle-free-anesthesia-delivery-overview`) 한줄: 컴퓨터제어(CCLAD/The Wand/STA)·압력조절·바늘없는 마취 전달장치 9편을 종합하면, 엄격한 맹검 RCT일수록 주사통증 자체의 우위는 재현되지 않지만 공포·불안 감소, 보충마취 회피, 소아 협조도 개선은 일관되게 관찰된다 — 임상적 가치는 "덜 아프게"가 아니라 "덜 무섭고 덜 재주사하게"에 있으며, 근거 수준은 강한 RCT부터 비맹검 전후비교 코호트까지 폭넓게 갈린다.

- `abutment-emergence-profile-peri-implant-tissue-overview` [overviews] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: > - 표면 축은 무효: 변형 티타늄 표면은 단기 플라크지수·탐침시출혈 (Bleeding on Probing, BoP)·탐침깊이 (Probing Depth, PD)에서 대조군과 차이 없음(P=0.091/0.099/0.488), 장기는 상반(Canullo 2020 SR+MA).
  - ▸ 출발(`abutment-emergence-profile-peri-implant-tissue-overview`) 한줄: 10편 종합(SR+MA 1·SR 2·scoping review 1·RCT 3·후향 1·전임상 동물 2): 임플란트주위 조직 안정성의 지배 인자는 출현윤곽의 **형태·각도** — 전치부 볼록은 오목 대비 퇴축 위험 ~13배(Siegenthaler 2022), 구치부 W/H 기반 낮은 출현각도(~32°)는 퇴축을 절반으로(Wang 2022), 개 모델 RCT는 각도→골소실/봉쇄실패 용량반응을 인과적으로 확립(80°가 20°의 ~4배 MBL, ≥60°에서 접합상피 붕괴; 각도 <40° 유지: Strau

- `abutment-emergence-profile-peri-implant-tissue-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Canullo 2020 (SR+MA, 10 studies; 6 pooled — 4 RCT/2 CCT, 118 patients, 182 implants) tested whether **titanium healing-abutment surface modifications** (machined vs anodized/laser/other) change peri-implant soft-tissue behavior. Short-term, modified surfaces showed **no significant difference** vs controls in plaque index (P=0.091), bleeding on probing (P=0.099), or probing depth (P=0.488), with n
  - ▸ 출발(`abutment-emergence-profile-peri-implant-tissue-overview`) 한줄: 10편 종합(SR+MA 1·SR 2·scoping review 1·RCT 3·후향 1·전임상 동물 2): 임플란트주위 조직 안정성의 지배 인자는 출현윤곽의 **형태·각도** — 전치부 볼록은 오목 대비 퇴축 위험 ~13배(Siegenthaler 2022), 구치부 W/H 기반 낮은 출현각도(~32°)는 퇴축을 절반으로(Wang 2022), 개 모델 RCT는 각도→골소실/봉쇄실패 용량반응을 인과적으로 확립(80°가 20°의 ~4배 MBL, ≥60°에서 접합상피 붕괴; 각도 <40° 유지: Strau

- `abutment-emergence-profile-peri-implant-tissue-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Shape > surface/disconnection is a hierarchy, not a contradiction.** The two shape RCTs deliver large, significant, same-direction effects (recession 13× higher convex; recession halved at lower angle), while the surface SR+MA and the OAOT RCT are flatly null on tissue outcomes. There is no genuine conflict — the levers simply differ in magnitude, and clinical attention should track the magnit
  - ▸ 출발(`abutment-emergence-profile-peri-implant-tissue-overview`) 한줄: 10편 종합(SR+MA 1·SR 2·scoping review 1·RCT 3·후향 1·전임상 동물 2): 임플란트주위 조직 안정성의 지배 인자는 출현윤곽의 **형태·각도** — 전치부 볼록은 오목 대비 퇴축 위험 ~13배(Siegenthaler 2022), 구치부 W/H 기반 낮은 출현각도(~32°)는 퇴축을 절반으로(Wang 2022), 개 모델 RCT는 각도→골소실/봉쇄실패 용량반응을 인과적으로 확립(80°가 20°의 ~4배 MBL, ≥60°에서 접합상피 붕괴; 각도 <40° 유지: Strau

- `abutment-emergence-profile-peri-implant-tissue-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/rios-santos-2020-one-abutment-one-time-rct]] — disconnection axis (b): RCT finding OAOT confers no bone benefit vs repeated disconnection, but height ≥2 mm does — contradicts the disconnection-avoidance rationale
  - ▸ 출발(`abutment-emergence-profile-peri-implant-tissue-overview`) 한줄: 10편 종합(SR+MA 1·SR 2·scoping review 1·RCT 3·후향 1·전임상 동물 2): 임플란트주위 조직 안정성의 지배 인자는 출현윤곽의 **형태·각도** — 전치부 볼록은 오목 대비 퇴축 위험 ~13배(Siegenthaler 2022), 구치부 W/H 기반 낮은 출현각도(~32°)는 퇴축을 절반으로(Wang 2022), 개 모델 RCT는 각도→골소실/봉쇄실패 용량반응을 인과적으로 확립(80°가 20°의 ~4배 MBL, ≥60°에서 접합상피 붕괴; 각도 <40° 유지: Strau

- `tilted-axial-implant-angled-abutment-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **The gap resolved**: FEA reports *relative* stress increases; it does not say the implant fails. Bilgi-Ozyetim's absolute numbers (all <550 MPa) and Murat's peak of 266 MPa both sit well inside the safe envelope. So "tilted has higher FEA stress" and "tilted is clinically equivalent" are **not contradictory** — the extra stress is real but sub-critical, expressed clinically only as the small long
  - ▸ 출발(`tilted-axial-implant-angled-abutment-overview`) 한줄: 7편 종합: 의도적 경사식립은 생존율·단기 변연골에서 수직식립과 임상적으로 동등(Del Fabbro 2014; Lin 2018)하고 장기엔 작은 MBL 페널티만 있다(Del Fabbro 2022, P<.0001) — FEA는 각도·축외 하중 증가 시 응력이 오르지만 모두 티타늄 항복강도 한참 아래라 in-vitro와 임상의 간극이 해소된다; 각도지대주는 emergence를 교정하나 각도·하중 방향·골질에 따라 응력·피로 페널티를 진다.

- `complete-denture-digital-overdenture-overview` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: - This **updates and partly overturns** an earlier SR (Ahmed et al.) that had reported *better* implant survival for 1-IOD; once post-2017 RCTs are added, that survival advantage disappears.
  - ▸ 출발(`complete-denture-digital-overdenture-overview`) 한줄: 24편 기반 총합 개요: 총의치 수명(10.1년), 디지털·전통 제작 동등성, 피개의치 임플란트 수·어태치먼트 선택, 의치 접착제 효능, 유지관리 프로토콜을 망라한 무치악 환자 임상 의사결정 가이드. ---

- `mandibular-anesthesia-failure-accessory-innervation-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "이설골근신경은 운동신경이라 통증과 무관" — Stein 2007이 반박: 혼합 감각. [저등급~합의]
  - ▸ 출발(`mandibular-anesthesia-failure-accessory-innervation-overview`) 한줄: IANB가 *왜* 해부학적으로 실패하는지 다룬 local-anesthesia 6편 통합. 실패는 다인성(피질골·바늘편향·신경위치·부신경지배, 측절치 실패율 81%)이며, 해부학적으로 구별되는 세 부신경지배 경로(이설골근신경, 경부신경총의 횡경부신경, CBCT상 16%에서 보이는 후구치관)가 술기적으로 성공한 마취에도 치아 감각을 남길 수 있어 대체 기법(Gow-Gates, Akinosi-Vazirani)이 필요하다.

- `watanabe-toothpick-method-toothbrushing-synthesis` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: The **Watanabe toothpick method (TPM, 이쑤시개법)** is a manual toothbrushing technique using a **double-row (2-row) toothbrush** whose bristle tips are pressed into the interdental embrasures in a toothpick-like motion. This page synthesizes the 7 papers the wiki holds, spanning the method's **origin (1998)** to its most recent **peri-implant application (2025)**, plus the **naming-confusion counterpo
  - ▸ 출발(`watanabe-toothpick-method-toothbrushing-synthesis`) 한줄: 와타나베 이쑤시개법(TPM, 칫솔질법) 위키 7편(1995–2026) 종합 — 2열모 칫솔로 치간을 닦는 기법으로 인접면 플라그 제거 + 치은 치유 자극(기저세포 증식 약 2.5배)의 이중 기전. 원전 RCT는 TPM>Bass(Morita 1998), 당뇨 치주염·임플란트 주위 점막염으로 효과 확장(단, 기계적 단독은 세균 재증식→항균제 병용 필요), 지도 빈도가 중요하나 기법 비교근거는 약함(Rajwani SR). *목재* 이쑤시개(치간도구)는 반대로 치간유두 소실·블랙트라이앵글 유발(El Ha

- `dbbm-bone-substitute-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Clinicians reading PRF studies should discriminate: (a) solid PRF vs liquid PRF (i-PRF) — different growth factor concentrations; (b) L-PRF centrifugation protocol (Dohan high-speed vs Choukroun protocols) — different fibrin architecture; (c) A-PRF low-speed (2700 rpm) — different platelet/cell distribution; (d) PRF mixed into graft vs used as membrane layer. Idiri 2023's null result and Almutairi
  - ▸ 출발(`dbbm-bone-substitute-overview`) 한줄: 10편(동물·전향·RCT·SR+MA) 종합: DBBM은 탁월한 골전도 공간 유지 재료이나 흡수가 느려 단독 사용 시 신생골 형성 열등; BCP 혼합·PRF 보조가 이 간극을 일관되게 메우고, 콜라겐 변형과 BMP2 기능화가 차세대 가능성을 제시하며, 부분탈회 동종골 plug는 DBBM과 동등한 차원 안정성·생활골에 더 빠른 graft turnover를 보인다.

- `implant-spacing-proximity-crestal-bone-overview` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: | Implant ↔ implant (modern designs) | ~2 mm acceptable; 1 mm maintainable in select cases | Morales Schwarz 2025 (n=1) + 2 animal studies | Internal conical + platform-switching + concave abutment + subcrestal placement defend the gap; n=1 → does not overturn ≥3 mm |
  - ▸ 출발(`implant-spacing-proximity-crestal-bone-overview`) 한줄: 4편 종합: 치간 치조정골은 수평 간격이 지배 — 임플란트간 거리 ≥3 mm (Tarnow 2000; 현대 디자인은 1–2 mm까지 가능 — Morales Schwarz 2025, n=1)와 임플란트-치근 거리 ≥1.5 mm (Joshi 2025 SR+MA; Ng 2018)가 치조정 골소실·주위염·인접치 치수손상을 최소화한다.

- `ceraseal-bioceramic-sealer-clinical-material-synthesis` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **재근관치료 제거성**: Shim 2025 (in-vitro, micro-CT) — 세라실 92.5%·AH Plus Bioceramic 94.8% > 에폭시 AH Plus Jet 87.1% 제거(WaveOne Gold + XP-endo Finisher). **"생광화 실러는 못 뺀다"는 우려를 반박** — 오히려 더 잘 빠짐, 단 XPF로 apical 보강 필요.
  - ▸ 출발(`ceraseal-bioceramic-sealer-clinical-material-synthesis`) 한줄: 세라실(프리믹스 칼슘실리케이트 생체세라믹 실러)에 대한 임상 4편(전향 코호트 2 + RCT 2) + 벤치 6편 종합: 24~36개월 치유(약 91~92%)·생존(약 93~98%)이 AH Plus gold standard와 동등하며, 술후통증은 더 적고, 압출은 같거나 적고(일부 흡수), 재근관치료 제거성 우수, 경화 후 생체적합·생체활성. 단 미경화 상태는 일시적 세포독성·강알칼리이므로 **실러 선택보다 정밀 충전(과충전 회피)이 더 중요**.

- `ceraseal-bioceramic-sealer-clinical-material-synthesis` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: **The bench data explain why and add three practical reassurances.** (1) *Retrievability* — Shim 2025 refutes the fear that biomineralizing CSBSs can't be removed: Ceraseal was 92.5% retrievable vs 87.1% for epoxy AH Plus Jet (with XP-endo Finisher adding apical removal). (2) *Bioactivity* — Maharti 2024 shows Ceraseal deposits more interfacial apatite and sustains higher pH than AH Plus Biocerami
  - ▸ 출발(`ceraseal-bioceramic-sealer-clinical-material-synthesis`) 한줄: 세라실(프리믹스 칼슘실리케이트 생체세라믹 실러)에 대한 임상 4편(전향 코호트 2 + RCT 2) + 벤치 6편 종합: 24~36개월 치유(약 91~92%)·생존(약 93~98%)이 AH Plus gold standard와 동등하며, 술후통증은 더 적고, 압출은 같거나 적고(일부 흡수), 재근관치료 제거성 우수, 경화 후 생체적합·생체활성. 단 미경화 상태는 일시적 세포독성·강알칼리이므로 **실러 선택보다 정밀 충전(과충전 회피)이 더 중요**.

- `single-vs-multivisit-endodontic-outcomes-overview` [overviews] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: > - nuance 2 — 상반된 치유 우위: Rossi-Fedele 2023 SR+MA가 단일내원 소폭 치유 우위(RR 1.10) 보고 → 즉시 충전이 내원간 재오염을 약간 줄일 가능성, 작은 효과로 "최소한 비열등, 가능하면 소폭 우위"로 해석.
  - ▸ 출발(`single-vs-multivisit-endodontic-outcomes-overview`) 한줄: 가장 큰 Cochrane SR+MA(Mergoni 2022, 47 RCT), TSA를 적용한 두 번째 SR+MA(Schwendicke 2017, 29 RCT), 그리고 1차성 근단치주염(Bobba 2026)·술후 통증(Chaitanya 2024)·재치료(Karaoğlan 2022)를 다룬 최근 RCT 3편이 모두 — 단일내원과 다회내원 근관치료 사이에 방사선학적 치유·술후 통증의 임상적으로 유의한 차이가 없다는 결론으로 수렴한다. 유일하게 일관된 nuance는 단일내원군의 작고 일시적인 초기 통증

- `ridge-split-expansion-technique-selection-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: López-Valverde 2025 pools expansion + compaction + densification together for the narrow (≤2.5 mm) crest and finds all three favour the experimental group for **bone density** (SMD −0.71, p=0.002, homogeneous/trustworthy), **crestal expansion** (SMD −1.12, p=0.04, but I²≥75%), and **ISQ** (SMD −8.88, p=0.0005, but I²=96%) — with the honest caveat that only the bone-density signal is solid; CE and 
  - ▸ 출발(`ridge-split-expansion-technique-selection-overview`) 한줄: 좁은 치조제 수평 골증대에서 치조제 분할·확장술 10개 위키 페이지를 종합: 분할술은 공여부 없이 폭 +3.3–3.7 mm·생존 ~98–99%를 신뢰성 있게 달성하며(Lin 2023), GBR 4.04 > RS 3.66 > OD 2.15 mm로 골증대량은 GBR이 가장 크지만 생존율은 세 술식 동등(~99%, Vorovenci 2024)이라 선택은 시작 골폭(가장 좁으면 RS, 저밀도골이면 OD)·단계(1단계 우세하나 근거 낮음, 하악 치밀골은 2단계)·이식 여부(≥3 mm 단독, <3 mm 선택

- `supportive-peri-implant-therapy-maintenance-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: There is **no genuine contradiction across the four** — all four point the same way (individualized maintenance reduces peri-implant disease). The real tension is **strength of evidence vs strength of recommendation**:
  - ▸ 출발(`supportive-peri-implant-therapy-maintenance-overview`) 한줄: 4편 종합(SR 2·내러티브/임상 2): 지지 임플란트주위 치료(SPiT)는 효과가 있으나 고정 연 1회가 아닌 **위험도 기반 개별화 recall**이라야 한다 — 진단 측정(탐침·%BoP·방사선)이 recall 주기(3~12개월)를 산출하고 그 recall이 질환을 늦춤(PD −1.0~1.5 mm, BoP −10~25%p, 순응 환자 임플란트주위염 40~70%↓); full-arch는 6개월 OH + ≥연 1회 보철 제거; 근거는 방향 일관하나 이질성 커 메타분석 불가.

- `vitamin-d-osseointegration-implant-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Vitamin D is biologically tied to bone metabolism (calcium homeostasis, osteoblast differentiation, immunomodulation), so a pro-osseointegration role is mechanistically plausible. The wiki holds 8 papers spanning the full evidence ladder, and they do **not** all agree. This page resolves the apparent contradiction.
  - ▸ 출발(`vitamin-d-osseointegration-implant-overview`) 한줄: 8편 종합(우산형 1·SR 3·RCT 1·전향 2·후향 1): 비타민 D의 골유착 촉진 효과는 동물·기전에서는 일관되나 사람에서는 갈린다 — 양성 신호는 중증 결핍(<10~20 ng/mL)+동반위험에 몰리고 충분군에서는 무차이; 고위험군 술전 선별 + *중증 결핍만* 교정이 방어 가능, 충분군 루틴 보충은 미입증.

- `vitamin-d-osseointegration-implant-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/vitamin-d/francis-2024-low-serum-vitamin-d-early-implant-failure]] — the key null/contradicting cohort (replete population)
  - ▸ 출발(`vitamin-d-osseointegration-implant-overview`) 한줄: 8편 종합(우산형 1·SR 3·RCT 1·전향 2·후향 1): 비타민 D의 골유착 촉진 효과는 동물·기전에서는 일관되나 사람에서는 갈린다 — 양성 신호는 중증 결핍(<10~20 ng/mL)+동반위험에 몰리고 충분군에서는 무차이; 고위험군 술전 선별 + *중증 결핍만* 교정이 방어 가능, 충분군 루틴 보충은 미입증.

- `flapless-vs-flapped-implant-surgery-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **발치 단독 차원에서는 flapless가 능사 아님**: Araujo 2009(개 5마리 split-mouth)는 flapless 발치도 피판 발치와 동등한 치조제 흡수 — "flapless = 치조제 보존"이라는 통념 반박. [근거강함]
  - ▸ 출발(`flapless-vs-flapped-implant-surgery-overview`) 한줄: 무피판 vs 피판 임플란트 수술 6편을 3축(실패율·치조정골·통증/연조직)으로 종합 — 결과 변수별로 우열이 갈림. 실패율 우려(RR 1.75)는 저질 연구 의존이라 약하고, 치조정골은 RCT(flapless 우위)와 코호트(차이없음)가 충돌하나, 술후 통증·단기 연조직은 flapless 일관 우위. 치유 치조제·단순 단일치엔 flapless가 합리적, 증대·시야 필요 시 피판.

- `flapless-vs-flapped-implant-surgery-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Axis 2 — Crestal/marginal bone (the live controversy).** Two 2025 papers in healed posterior ridges reach opposite conclusions. Surendra 2025 (RCT, n=40, posterior mandible) found flapless preserved significantly more crestal bone at both 3 months (0.32 vs 0.56 mm) and 6 months (0.48 vs 0.82 mm, both p<0.001) — roughly 40% less loss — with 100% survival in both arms, attributing the advantage to
  - ▸ 출발(`flapless-vs-flapped-implant-surgery-overview`) 한줄: 무피판 vs 피판 임플란트 수술 6편을 3축(실패율·치조정골·통증/연조직)으로 종합 — 결과 변수별로 우열이 갈림. 실패율 우려(RR 1.75)는 저질 연구 의존이라 약하고, 치조정골은 RCT(flapless 우위)와 코호트(차이없음)가 충돌하나, 술후 통증·단기 연조직은 flapless 일관 우위. 치유 치조제·단순 단일치엔 flapless가 합리적, 증대·시야 필요 시 피판.

- `flapless-vs-flapped-implant-surgery-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: **A foundational caution.** Araujo 2009 (5-dog split-mouth histology) showed flapless extraction produced ridge resorption equivalent to flapped extraction, refuting the notion that avoiding a flap by itself preserves the ridge. Flapless preserves *periosteal vascularity around an implant*, not the post-extraction ridge dimension per se.
  - ▸ 출발(`flapless-vs-flapped-implant-surgery-overview`) 한줄: 무피판 vs 피판 임플란트 수술 6편을 3축(실패율·치조정골·통증/연조직)으로 종합 — 결과 변수별로 우열이 갈림. 실패율 우려(RR 1.75)는 저질 연구 의존이라 약하고, 치조정골은 RCT(flapless 우위)와 코호트(차이없음)가 충돌하나, 술후 통증·단기 연조직은 flapless 일관 우위. 치유 치조제·단순 단일치엔 flapless가 합리적, 증대·시야 필요 시 피판.

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - SR 충돌 상세: 임상 SR(Senna 2012·Silva 2013)=연관 약함/불가 vs abfraction SR(Duangthip 2017)=81% 연관(단 lab/FEA 가중·응력단독 원인 임상입증 전무) vs scoping review(Dioguardi 2024, 6편)=확정·반박 모두 불가. SEM은 microfracture 일부 관찰(Worawongvasu).
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 한줄: NCCL은 stress·friction·biocorrosion 다인성이며 abfraction 단독원인설은 미입증, 무증상은 monitoring이 원칙, 수복 시 유지력은 접착·산부식 단계에 좌우(selective enamel etching 유리, self-adhesive flowable 실패).

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "교합응력→abfraction"이 모든 NCCL의 주원인이라는 강한 주장은 임상적으로 미입증이다. SR 근거가 정면으로 갈린다: 임상연구 SR(Senna 2012·Silva 2013)은 연관 약함/결론불가, abfraction 키워드 SR(Duangthip 2017)은 81% 연관(단 lab/FEA 가중·응력단독 원인 임상입증 전무), 최신 PRISMA-ScR scoping(Dioguardi 2024)은 6편만으로 확정·반박 모두 불가로 정리. 초미세구조(SEM)에선 microfracture 증거 일부 관찰. **종합: lab은 응력집중을 보이나 in-vivo 인과는 미입증.** [합의수준 — SR 충돌]
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 한줄: NCCL은 stress·friction·biocorrosion 다인성이며 abfraction 단독원인설은 미입증, 무증상은 monitoring이 원칙, 수복 시 유지력은 접착·산부식 단계에 좌우(selective enamel etching 유리, self-adhesive flowable 실패).

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - Abfraction 기전 — SR-level 충돌이 미해결의 핵심: 임상 SR(Senna 2012·Silva 2013)=연관 약함/불가 vs abfraction SR(Duangthip 2017)=81% 연관(lab 가중) vs scoping(Dioguardi 2024)=6편으로 확정·반박 불가. SEM microfracture(Worawongvasu)와 임상 음성 연관이 상충. Dioguardi 2024가 제시한 해법 = 침식/마모를 분리한 전향적 종단연구.
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 한줄: NCCL은 stress·friction·biocorrosion 다인성이며 abfraction 단독원인설은 미입증, 무증상은 monitoring이 원칙, 수복 시 유지력은 접착·산부식 단계에 좌우(selective enamel etching 유리, self-adhesive flowable 실패).

- `topical-anesthetic-injection-pain-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 중심 긴장점: 명제3·4의 상충 — blinding·검정력이 강해질수록 제제 간 차이가 사라지는 패턴은 관찰된 "우위"가 상당 부분 측정·기대 편향일 가능성을 시사. [claude해석]
  - ▸ 출발(`topical-anesthetic-injection-pain-overview`) 한줄: 표면마취제는 위약 대비 needle·주사 통증을 확실히 줄이지만, 제제 간(lidocaine·benzocaine·EMLA) 직접비교 차이는 작고 비일관적이다 — 어떤 약물이냐보다 전달제형·농도·도포술기가 더 결정적이며, 표면마취가 통증강도에서 주사마취를 완전히 대체하진 못해도 SRP 같은 맥락에선 덜 침습적 대안으로 유효하다.

- `topical-anesthetic-injection-pain-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: → 명제 3·4의 **상충**은 이 overview의 중심 긴장점이다. blinding·검정력이 강해질수록 제제 간 차이가 사라지는 패턴은, 관찰된 "우위"가 상당 부분 측정·기대 편향일 수 있음을 시사한다. [claude해석]
  - ▸ 출발(`topical-anesthetic-injection-pain-overview`) 한줄: 표면마취제는 위약 대비 needle·주사 통증을 확실히 줄이지만, 제제 간(lidocaine·benzocaine·EMLA) 직접비교 차이는 작고 비일관적이다 — 어떤 약물이냐보다 전달제형·농도·도포술기가 더 결정적이며, 표면마취가 통증강도에서 주사마취를 완전히 대체하진 못해도 SRP 같은 맥락에선 덜 침습적 대안으로 유효하다.

- `pachipulusu-2018-primary-secondary-closure-third-molar` [suture-wound-closure] (SOFT→takadoum-2022-sutureless-socket-technique-third-molars, 'whereas' · 반면(대조))
  - **근거 문장**: - [[suture-wound-closure/takadoum-2022-sutureless-socket-technique-third-molars]] — contrasts: Takadoum's larger multicentric RCT found no pain/swelling difference, whereas this trial does favor the open (secondary) approach.
  - ▸ 출발(`pachipulusu-2018-primary-secondary-closure-third-molar`) 한줄: 하악 매복 사랑니 발치 후 1차 폐쇄 대 2차 폐쇄를 비교한 무작위배정 임상시험(n=60, 군당 30명). 2차 폐쇄군이 통증·부종이 유의하게 적고 개구량이 더 컸으며(p<0.05), 6개월 시점 치주 치유에는 차이가 없었다(건성발치와는 2차 폐쇄군 1명, 3.3%).
  - ▸ 대상(`takadoum-2022-sutureless-socket-technique-third-molars`) 한줄: 4개 매복 사랑니를 전신마취 하에 발치하면서 봉합 대 무봉합을 비교한 프랑스 3개 병원 다기관 공개 무작위배정 임상시험(분석 n=94: 봉합 44, 무봉합 50). 3일째 통증(p=0.904)과 모든 2차 결과에서 차이가 없었고, 무봉합이 수술시간이 짧았으며 흡연이 합병증 위험인자였다(3.65배, p=0.0244).

- `de-oliveira-2024-otc-bleaching-color-adverse-effects` [tooth-whitening] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This NMA covers the consumer/unsupervised whitening route — strips, paint-on gels, prefilled trays — which is the most common entry point patients ask about. The headline: low-concentration OTC products do produce real short-term lightening over placebo and are generally well tolerated (minimal sensitivity, minimal gingival irritation), with longer daily wear time being the key driver of effect. F
  - ▸ 출발(`de-oliveira-2024-otc-bleaching-color-adverse-effects`) 한줄: SR + 빈도주의 NMA (정성 37편, 메타 10편, n=1932) — OTC 미백은 단기적으로 위약보다 효과적: ΔEab*는 6% HP 스트립(≥14h), ΔSGU는 10% CP(≥14h)가 최고이며 민감도·치은 자극은 거의 없음(근거 낮음).

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Systematic review + meta-analysis (10 studies; 6 pooled — 4 RCT/2 CCT, 118 patients, 182 implants): modified titanium abutment surfaces show no significant short-term difference vs controls in plaque index, bleeding on probing, or probing depth; long-term (5–6 y) studies report contradictory results depending on surface technique.
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 한줄: 체계적 문헌고찰 + 메타분석 (10편 포함, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 표면은 단기적으로 플라크 지수·탐침 시 출혈(BoP)·탐침 깊이(PD)에서 대조군과 유의한 차이가 없었고, 장기(5~6년) 연구는 표면 처리 기법에 따라 상반된 결과를 보였다.

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: 체계적 문헌고찰 + 메타분석 (10편 포함, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 표면은 단기적으로 플라크 지수·탐침 시 출혈(BoP)·탐침 깊이(PD)에서 대조군과 유의한 차이가 없었고, 장기(5~6년) 연구는 표면 처리 기법에 따라 상반된 결과를 보였다.
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 한줄: 체계적 문헌고찰 + 메타분석 (10편 포함, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 표면은 단기적으로 플라크 지수·탐침 시 출혈(BoP)·탐침 깊이(PD)에서 대조군과 유의한 차이가 없었고, 장기(5~6년) 연구는 표면 처리 기법에 따라 상반된 결과를 보였다.

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: According to PubMed ([DOI 10.1007/s00784-020-03210-x](https://doi.org/10.1007/s00784-020-03210-x)), this systematic review with meta-analysis (abstract-only — full text not retrieved) evaluated whether **titanium healing-abutment surface modifications** (machined vs anodized/laser/other treatments) affect peri-implant soft-tissue healing, inflammation, and maintenance. A database search through 30
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 한줄: 체계적 문헌고찰 + 메타분석 (10편 포함, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 표면은 단기적으로 플라크 지수·탐침 시 출혈(BoP)·탐침 깊이(PD)에서 대조군과 유의한 차이가 없었고, 장기(5~6년) 연구는 표면 처리 기법에 따라 상반된 결과를 보였다.

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Documents that long-term (5–6 y) evidence is contradictory and technique-dependent — a caution flag rather than a green light.
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 한줄: 체계적 문헌고찰 + 메타분석 (10편 포함, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 표면은 단기적으로 플라크 지수·탐침 시 출혈(BoP)·탐침 깊이(PD)에서 대조군과 유의한 차이가 없었고, 장기(5~6년) 연구는 표면 처리 기법에 따라 상반된 결과를 보였다.

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **4 studies** with 5–6 y follow-up too heterogeneous/contradictory to pool.
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 한줄: 체계적 문헌고찰 + 메타분석 (10편 포함, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 표면은 단기적으로 플라크 지수·탐침 시 출혈(BoP)·탐침 깊이(PD)에서 대조군과 유의한 차이가 없었고, 장기(5~6년) 연구는 표면 처리 기법에 따라 상반된 결과를 보였다.

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Long-term (4 studies, 5–6 y):** contradictory results depending on the surface-modification technique.
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 한줄: 체계적 문헌고찰 + 메타분석 (10편 포함, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 표면은 단기적으로 플라크 지수·탐침 시 출혈(BoP)·탐침 깊이(PD)에서 대조군과 유의한 차이가 없었고, 장기(5~6년) 연구는 표면 처리 기법에 따라 상반된 결과를 보였다.

- `koyama-2025-single-vs-two-implant-mandibular-overdenture-sr-ma` [implants] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: This updates and partly overturns an earlier SR (Ahmed et al.) that had reported *better* implant survival for 1-IOD; with post-2017 RCTs added, that survival advantage disappears.
  - ▸ 출발(`koyama-2025-single-vs-two-implant-mandibular-overdenture-sr-ma`) 한줄: 하악 단일(1-IOD) vs 2개(2-IOD) 임플란트 오버덴쳐를 비교한 17편 RCT SR+MA — 임플란트 생존율은 5년까지 동등하지만, 의치 파절(5Y RR 2.10)·재제작(5Y RR 2.57)·메탈하우징 재부착(5Y RR 2.31) 같은 보철 합병증은 1-IOD에서 약 2배 잦다. 리라이닝·O-ring 교체 빈도는 차이 없음.

- `koyama-2025-single-vs-two-implant-mandibular-overdenture-sr-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Updates the literature**: contradicts the earlier higher-survival-for-1-IOD finding once recent RCTs are included.
  - ▸ 출발(`koyama-2025-single-vs-two-implant-mandibular-overdenture-sr-ma`) 한줄: 하악 단일(1-IOD) vs 2개(2-IOD) 임플란트 오버덴쳐를 비교한 17편 RCT SR+MA — 임플란트 생존율은 5년까지 동등하지만, 의치 파절(5Y RR 2.10)·재제작(5Y RR 2.57)·메탈하우징 재부착(5Y RR 2.31) 같은 보철 합병증은 1-IOD에서 약 2배 잦다. 리라이닝·O-ring 교체 빈도는 차이 없음.

- `mello-machado-2021-osseodensification-low-quality-bone-rct` [implants] (HIGH-no-target, 'at odds' · 상충)
  - **근거 문장**: - Living-document note: the abstract's headline ("OD enables the healing chamber without reduction in stability") is supported by ISQ equivalence; the simultaneous IT increase is interesting but somewhat at odds with the "healing chamber = gap = lower IT" rationale and deserves cautious interpretation.
  - ▸ 출발(`mello-machado-2021-osseodensification-low-quality-bone-rct`) 한줄: 무작위대조시험 (Randomized Controlled Trial, RCT), 이중맹검, n=16 환자/55 임플란트 — Misch D3/D4 저밀도골에서 골밀도화 (Osseodensification, OD) 군이 표준 언더사이즈 드릴링 대비 삽입토크는 유의하게 높았으나(39.0±6.4 vs 32.0±3.4 Ncm, p<0.001) 임플란트 안정성 지수 (Implant Stability Quotient, ISQ)는 placement(67.1 vs 65.5)·6개월(74.0 vs 73.3) 모두 동

- `benic-2014-loading-protocols-single-implant-crowns-sr-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This meta-analysis of 11 RCTs established that immediately and conventionally loaded single-implant crowns achieve equivalent implant survival and marginal bone loss from 1 through 5 years, with no difference in papilla level. Critically, this equivalence holds for implants placed with adequate primary stability — insertion torque ≥20–45 Ncm or ISQ ≥60–65 — and without simultaneous bone augmentati
  - ▸ 출발(`benic-2014-loading-protocols-single-implant-crowns-sr-ma`) 한줄: 11개 RCT SR+MA — 단일 임플란트 단관에서 즉시 로딩과 통상 로딩은 5년까지 생존율(1년 OR 0.75)·변연골소실(SMD −0.05 mm)이 동등하며, 이는 삽입토크 ≥20–45 Ncm 또는 ISQ ≥60–65·동시 골증대 불필요 조건에서 성립한다.

- `tarpara-2025-flapless-flapped-clinical-outcomes-cohort` [implants] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - Provides the cohort counterpoint to RCT data claiming a crestal-bone advantage for flapless.
  - ▸ 출발(`tarpara-2025-flapless-flapped-clinical-outcomes-cohort`) 한줄: 단일 구치부 임플란트 비무작위 코호트 (n=20, 부하 후 12개월)에서 무피판(flapless)이 술후 통증·6개월 탐침깊이는 유의하게 낮았으나, 치조정 골높이(CBH)는 피판군과 어느 시점에도 차이 없음.

- `tarpara-2025-flapless-flapped-clinical-outcomes-cohort` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/surendra-2025-flapless-versus-flapped-crestal-bone]] — contradicts: an RCT (n=40) found flapless preserved significantly more crestal bone at 3 and 6 months; this cohort found no crestal difference at 12 months.
  - ▸ 출발(`tarpara-2025-flapless-flapped-clinical-outcomes-cohort`) 한줄: 단일 구치부 임플란트 비무작위 코호트 (n=20, 부하 후 12개월)에서 무피판(flapless)이 술후 통증·6개월 탐침깊이는 유의하게 낮았으나, 치조정 골높이(CBH)는 피판군과 어느 시점에도 차이 없음.

- `huwais-2017-novel-osseous-densification-osteotomy-primary-stability` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Two findings deserve careful clinical interpretation. First, **ISQ did not differ significantly among the three groups** even though insertion torque did — a dissociation that recurs in subsequent OD literature and reflects the fact that ISQ measures lateral stiffness while torque measures axial resistance; OD's effect appears axial-dominant in this model. Second, **temperatures did not rise with 
  - ▸ 출발(`huwais-2017-novel-osseous-densification-osteotomy-primary-stability`) 한줄: 시험관 벤치 연구 (in vitro), 돼지 경골 (porcine tibia) 72 골삭제 (osteotomy) — 같은 다중날 (multi-fluted) 버 (bur)를 반시계방향으로 회전시키는 골밀도화 (Osseodensification, OD)가 표준 드릴링 대비 삽입·제거 토크 (Insertion/Removal Torque)와 골-임플란트 접촉률 (Bone-to-Implant Contact, BIC, 약 3배)을 유의하게 상승시키고 골삭제 둘레에 골밀도 (Bone Mineral Densit

- `kim-2026-implant-angulation-peri-implant-bone` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[occlusion/di-fiore-2022-periimplant-bone-loss-overload-occlusal-analysis]] — contradicts/refines: occlusal-overload framing; this study supplies positive clinical evidence that off-axis geometry (not just overload magnitude) tracks MBL, where some overload analyses found weaker links.
  - ▸ 출발(`kim-2026-implant-angulation-peri-implant-bone`) 한줄: CAD 3D 각도 측정을 쓴 5년 후향연구(288명·506개). 비축방향 임플란트 변연골 소실이 유의하게 컸고(0.22±0.48 vs 0.10±0.39 mm, P<.05), 상악>하악(P<.001), 비축방향이 임플란트 지지 고정성 보철과 대합할 때 골소실이 가장 컸다(상호작용 Δ0.373 mm).

- `stubinger-2015-piezosurgery-implant-dentistry` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Narrative clinical review (Clin Cosmet Investig Dent 2015) of piezoelectric bone surgery in implant dentistry: outlines its claimed advantages (precise selective cutting of mineralized tissue, soft-tissue/nerve/membrane preservation, improved visibility) across implant site prep, bone grafting, sinus floor elevation, ridge splitting, and IAN lateralization, while noting longer surgical time, learn
  - ▸ 출발(`stubinger-2015-piezosurgery-implant-dentistry`) 한줄: 서술적 고찰(Clin Cosmet Investig Dent 2015): piezo bone surgery 임상 overview — 정밀·선택적 cutting, 연조직 보존, 임플란트 site prep·골이식·sinus floor·ridge split·하치조신경 lateralization 적용; 단 "열손상 회피" 주장은 후속 연구(aquilanti, jain)와 모순.

- `stubinger-2015-piezosurgery-implant-dentistry` [implants] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "thermal damage 회피" 주장은 [근거강함] aquilanti 2023, jain 2024 SR 결과로 부분적으로 반박됨 — 정확한 piezo protocol(권장 load, quarter-turn 회전, 차가운 saline) 준수가 전제.
  - ▸ 출발(`stubinger-2015-piezosurgery-implant-dentistry`) 한줄: 서술적 고찰(Clin Cosmet Investig Dent 2015): piezo bone surgery 임상 overview — 정밀·선택적 cutting, 연조직 보존, 임플란트 site prep·골이식·sinus floor·ridge split·하치조신경 lateralization 적용; 단 "열손상 회피" 주장은 후속 연구(aquilanti, jain)와 모순.

- `rugova-2024-thermal-evaluation-bone-drilling-sequential` [implants] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: A custom-press in vitro study tested 5 drill bits in sequential drilling protocols with infrared thermography. The principal finding overturns a long-standing assumption: sequential drilling does not eliminate thermal trauma. The first (pilot) drill produces peak temperatures over 100°C, creating a thermal damage zone that spreads up to 10 mm from the osteotomy. Subsequent enlarging drills cannot 
  - ▸ 출발(`rugova-2024-thermal-evaluation-bone-drilling-sequential`) 한줄: 인비트로(Bioengineering 2024, 5 drill, IR 카메라, **irrigation 없음**): sequential drilling이 thermal damage zone을 제거하지 못함 — pilot drill >100°C, 70°C 발열이 osteotomy로부터 측방 10mm까지 확산; **후속 enlarging drill(~4.2mm)이 절제하는 반경(~2mm)을 넘는 범위라 thermal-damaged 측방 골은 남음**. RPM·load 감소 + peck drilling이 

- `rugova-2024-thermal-evaluation-bone-drilling-sequential` [implants] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Directly refutes the implicit clinical belief that "sequential drilling protects from heat." Identifies the pilot drill as the dominant thermal event and the peri-osteotomy zone (up to 10 mm) as the affected region.
  - ▸ 출발(`rugova-2024-thermal-evaluation-bone-drilling-sequential`) 한줄: 인비트로(Bioengineering 2024, 5 drill, IR 카메라, **irrigation 없음**): sequential drilling이 thermal damage zone을 제거하지 못함 — pilot drill >100°C, 70°C 발열이 osteotomy로부터 측방 10mm까지 확산; **후속 enlarging drill(~4.2mm)이 절제하는 반경(~2mm)을 넘는 범위라 thermal-damaged 측방 골은 남음**. RPM·load 감소 + peck drilling이 

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - Provides a clean RCT counterpoint to cohort data showing no crestal difference.
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 한줄: 하악 구치부 치유된 치조제 단일치 RCT (n=40)에서 무피판(flapless)이 피판(flapped)보다 치조정 골소실을 유의하게 적게 (6개월 0.48 vs 0.82 mm, p<0.001) — 양군 생존율 100%.

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/tarpara-2025-flapless-flapped-clinical-outcomes-cohort]] — contradicts: a non-randomized 12-month cohort found no crestal-bone difference between flapless and flapped (only pain/early probing-depth benefit).
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 한줄: 하악 구치부 치유된 치조제 단일치 RCT (n=40)에서 무피판(flapless)이 피판(flapped)보다 치조정 골소실을 유의하게 적게 (6개월 0.48 vs 0.82 mm, p<0.001) — 양군 생존율 100%.

- `bento-2023-steel-versus-zirconia-drills-heat` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: SR+MA (10 in vitro studies, inverse-variance pooling) of zirconia (Zr) vs stainless-steel (SS) implant drills: Zr drills produced significantly lower bone temperature variation than SS during implant site preparation — a quantitative material-pair signal that qualifies (rather than contradicts) the broader chakraborty-2024 "drill material inconclusive" SR.
  - ▸ 출발(`bento-2023-steel-versus-zirconia-drills-heat`) 한줄: SR+MA(Saudi Dent J 2024, 10편 in vitro): 지르코니아(Zr) drill이 스테인리스스틸(SS) drill보다 골내 온도 변화 유의하게 낮음(IV pooling) — chakraborty의 "material 결론 불가" 결과와 대립되는 특정 material pair에 대한 정량적 신호.

- `theracem-bisco-product-reference` [resin] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: - Chen et al. 2018 (Am J Dent, in vitro, 제조사 BISCO 연구): pH 4.0→9.0 안정화, calcium release(첫산>물), 지르코니아 SBS가 UniCem 2·FujiCEM 2 중 최고, 산성에서 결합 저하 없음. [근거강함] 단 저자 전원 BISCO 소속(이해상충)이라 독립 재현 필요. [claude해석]
  - ▸ 출발(`theracem-bisco-product-reference`) 한줄: calcium silicate 기반·10-MDP 함유, Ca·fluoride 방출형 dual-cure 자가접착 레진시멘트 TheraCem(BISCO) 제품 reference.

- `tian-2015-paucity-nanolayering-mdp-resin-dentin` [resin-bonding] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: **Clinically**: this is the principal counterpoint to the Yoshihara 2011 nanolayering hypothesis. It does not deny that 10-MDP can self-assemble into ordered nanolayers, but it shows the structure is **concentration-dependent and largely absent in the formulations dentists actually use**. The implication is that the durable, well-documented clinical performance of 10-MDP adhesives is more likely d
  - ▸ 출발(`tian-2015-paucity-nanolayering-mdp-resin-dentin`) 한줄: In-vitro TEM·박막 XRD 연구(상용 10-MDP 접착제 7종, TEM n=6/XRD n=4; 실험용 15/10/5 wt% 프라이머): 15% 10-MDP에서만 ~3.7 nm 주기의 풍부한 나노레이어링이 나타나고 상용 접착제에서는 거의 관찰되지 않아, 나노레이어링이 결합 내구성의 임상적 기전이라는 주장에 의문을 제기.

- `tian-2015-paucity-nanolayering-mdp-resin-dentin` [resin-bonding] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[resin-bonding/yoshihara-2011-nanolayering-mdp-enamel-dentin]] — **refines / contradicts**: Yoshihara established 10-MDP nanolayering and tied it to bond durability; Tian shows commercial adhesives nanolayer sparsely, narrowing that hypothesis to high-concentration experimental systems.
  - ▸ 출발(`tian-2015-paucity-nanolayering-mdp-resin-dentin`) 한줄: In-vitro TEM·박막 XRD 연구(상용 10-MDP 접착제 7종, TEM n=6/XRD n=4; 실험용 15/10/5 wt% 프라이머): 15% 10-MDP에서만 ~3.7 nm 주기의 풍부한 나노레이어링이 나타나고 상용 접착제에서는 거의 관찰되지 않아, 나노레이어링이 결합 내구성의 임상적 기전이라는 주장에 의문을 제기.

- `tian-2015-paucity-nanolayering-mdp-resin-dentin` [resin-bonding] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Direct counterpoint to the foundational nanolayering claim. [[wiki/resin-bonding/yoshihara-2011-nanolayering-mdp-enamel-dentin]] established that 10-MDP self-assembles into ordered nanolayers at the resin-dentin interface and hypothesized this drives bond durability. Tian et al. (2015) tested whether seven *commercialized* 10-MDP self-etch/universal adhesives actually reproduce this structure on h
  - ▸ 출발(`tian-2015-paucity-nanolayering-mdp-resin-dentin`) 한줄: In-vitro TEM·박막 XRD 연구(상용 10-MDP 접착제 7종, TEM n=6/XRD n=4; 실험용 15/10/5 wt% 프라이머): 15% 10-MDP에서만 ~3.7 nm 주기의 풍부한 나노레이어링이 나타나고 상용 접착제에서는 거의 관찰되지 않아, 나노레이어링이 결합 내구성의 임상적 기전이라는 주장에 의문을 제기.

- `anithakumari-2022-desensitizing-agents-bond-strength-sr` [resin-bonding] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: SR(in vitro 23편): 탈감작제가 dentin bonding agent 결합강도에 미치는 영향은 제제·프로토콜 의존적이며 결과 상충.
  - ▸ 출발(`anithakumari-2022-desensitizing-agents-bond-strength-sr`) 한줄: SR(in vitro 23편): 탈감작제가 dentin bonding agent 결합강도에 미치는 영향은 제제·프로토콜 의존적이며 결과 상충.

- `alghauli-2025-clinical-benefits-immediate-dentin-sealing` [resin-bonding] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The IDS-favorable POS result directly contradicts Josic 2022 SR+MA (4 studies, GRADE low: no difference). The two reviews likely differ in inclusion period (through 2021 vs through Dec 2023), study count (4 vs 11), and outcome definition. Clinical decisions should weigh: more recent and larger evidence base (Alghauli) vs more rigorous GRADE assessment (Josic).
  - ▸ 출발(`alghauli-2025-clinical-benefits-immediate-dentin-sealing`) 한줄: JPD 2025 SR+MA (11 clinical studies): IDS 적용 indirect restoration은 non-IDS 대비 complication ↓, survival 96.4–100% vs 81.8–96.7%, POS intensity·incidence 유의 감소 (P<.05). 단 josic-2022 SR+MA는 POS no-difference 결론 — 직접 충돌.

- `friele-2006-patient-expectations-fair-complaint` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Documents that only 7% want financial compensation -- contradicting the litigation-first assumption.
  - ▸ 출발(`friele-2006-patient-expectations-fair-complaint`) 한줄: 병원 민원인 424명 설문 — 최우선 목표는 '재발 방지', 공정한 절차·(사과보다) 설명을 중시하고 금전 보상 요구는 드묾.

- `friele-2006-patient-expectations-fair-complaint` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[complaint-management/mccreaddie-2021-qualitative-study-nhs-complaint]] -- contradicts: NHS responses violate these fairness expectations (fauxpology).
  - ▸ 출발(`friele-2006-patient-expectations-fair-complaint`) 한줄: 병원 민원인 424명 설문 — 최우선 목표는 '재발 방지', 공정한 절차·(사과보다) 설명을 중시하고 금전 보상 요구는 드묾.

- `elias-2025-successful-handling-patient-complaints` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[complaint-management/mccreaddie-2021-qualitative-study-nhs-complaint]] -- contradicts: teaches genuine empathy vs the fauxpology.
  - ▸ 출발(`elias-2025-successful-handling-patient-complaints`) 한줄: CODE(Compassion·Operational Support·De-escalation·Empowerment) 모델 소개 — 운영·절차 트랙과 대인 커뮤니케이션 트랙을 결합한 민원담당자 이중구조 교육과정.

- `gillespie-2025-complaint-handlers-bind-defensive` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Mixed-methods study of UK hospital staff responding to online criticism, identifying six defensive tactics arising from contradictory work demands.
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 한줄: 온라인 비판에 응답하는 영국 병원 직원 혼합방법 연구 — 모순된 업무 요구에서 비롯된 6가지 방어 전술 규명.

- `gillespie-2025-complaint-handlers-bind-defensive` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Gillespie and Reader studied how UK hospital staff respond to online criticism and found six reliably-coded defensive tactics -- from redirecting and evading to psychologising and quietly closing the episode. Crucially, they show defensiveness is not mainly a personal flaw but a response to a structural 'bind': handlers are simultaneously asked to be transparent and to protect the organisation's r
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 한줄: 온라인 비판에 응답하는 영국 병원 직원 혼합방법 연구 — 모순된 업무 요구에서 비롯된 6가지 방어 전술 규명.

- `gillespie-2025-complaint-handlers-bind-defensive` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Reframes defensiveness as a *structural* product of contradictory demands, not individual failing.
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 한줄: 온라인 비판에 응답하는 영국 병원 직원 혼합방법 연구 — 모순된 업무 요구에서 비롯된 6가지 방어 전술 규명.

- `gillespie-2025-complaint-handlers-bind-defensive` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Six defensive tactics were reliably identified. They were generally associated with lower-quality engagement (less issue resolution, less learning). Defensiveness arose where handlers faced contradictory demands -- being responsive/transparent while also protecting organisational reputation and managing workload.
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 한줄: 온라인 비판에 응답하는 영국 병원 직원 혼합방법 연구 — 모순된 업무 요구에서 비롯된 6가지 방어 전술 규명.

- `gillespie-2025-complaint-handlers-bind-defensive` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Explains WHY responders default to the defensive moves catalogued in [[complaint-management/12913_2021_Article_6733]]: contradictory organisational demands. Moves the response axis from blaming individuals to fixing the system -- the lever a clinic owner actually controls.
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 한줄: 온라인 비판에 응답하는 영국 병원 직원 혼합방법 연구 — 모순된 업무 요구에서 비롯된 6가지 방어 전술 규명.

- `chen-2022-interpretation-hba1c-analytical-methodology-hematology` [drug/systemic-disease] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Discordance protocol**: when HbA1c contradicts fingerstick or clinical impression, treat HbA1c as suspect; do not delay urgent extraction in clearly symptomatic infection based on isolated high HbA1c.
  - ▸ 출발(`chen-2022-interpretation-hba1c-analytical-methodology-hematology`) 한줄: 서술적 고찰 (Exp Ther Med 2022, Kunming Medical Univ) — HbA1c 간섭을 3축 (① 측정법 특이 변이체·유도체 ② 생화학적 글리케이션 속도 ③ 적혈구 수명 변화) 으로 체계화; 빈혈·CKD·HbS/C/D/E·임신·약물 (아스피린·비타민C·dapsone) 별 위양성·위음성 방향 카탈로그. 발치·임플란트 전 평가에서 HbA1c 단독 판단의 한계 근거.

- `momand-2024-antibiotic-prophylaxis-early-implant-failure` [drug/antibiotics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[drug/antibiotics/torof-2023-antibiotic-dental-implant-procedures-sr-ma]] — contradicts (earlier SR+MA recommended preoperative single-dose amoxicillin; this placebo-RCT-only analysis finds no significant benefit)
  - ▸ 출발(`momand-2024-antibiotic-prophylaxis-early-implant-failure`) 한줄: 체계적 고찰+메타분석(위약대조 이중맹검 RCT 7편, 환자 1859명 / 임플란트 3014개): 술전 항생제 예방은 조기 임플란트 실패를 유의하게 줄이지 못함(RR 0.66, 95% CI 0.30-1.47; 위험차 -0.007; NNT 143), GRADE 중간 — 비복잡 임플란트 수술에서 통상적 항생제 예방은 근거 부족.

- `torof-2023-antibiotic-dental-implant-procedures-sr-ma` [drug/antibiotics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Demonstrates that postoperative course offers no incremental benefit — directly contradicts widespread 7-day post-op courses.
  - ▸ 출발(`torof-2023-antibiotic-dental-implant-procedures-sr-ma`) 한줄: SR+MA (Wolverhampton, Medicina 2023): 임플란트 식립 (DIP) 항생제 예방 — 술전 단일 amoxicillin 2g 권고; 술후 연장은 incremental benefit 없음. PRISMA-P/PROSPERO 등록.

- `rajan-2025-doxycycline-safety-children-dental-sr` [drug/antibiotics] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: SR+MA (5개 연구, n=162명, 8세 미만): 단기 독시사이클린(doxycycline, Doxy) 투여(중앙값 8.5일) 후 치아 착색(tooth staining)은 162명 중 1명(0.62%, 미숙아 신생아 1건)에서만 발생, 통합 이상반응 비율 0.21 (95% CI: 0.13–0.28)로 AAP/CDC의 생명위협 적응증 소아 사용 지침 개정을 지지한다.
  - ▸ 출발(`rajan-2025-doxycycline-safety-children-dental-sr`) 한줄: SR+MA (5개 연구, n=162명, 8세 미만): 단기 독시사이클린(doxycycline, Doxy) 투여(중앙값 8.5일) 후 치아 착색(tooth staining)은 162명 중 1명(0.62%, 미숙아 신생아 1건)에서만 발생, 통합 이상반응 비율 0.21 (95% CI: 0.13–0.28)로 AAP/CDC의 생명위협 적응증 소아 사용 지침 개정을 지지한다.

- `tamgadge-2025-preoperative-dexamethasone-third-molar-pain-swelling-trismus` [drug/analgesics] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: split-mouth 단일맹검 위약대조 시험 (n=60, 양측 매복 하악 사랑니): 술전 dexamethasone 4 mg 근육주사 1회가 위약 대비 술후 통증(2일 1.2 vs 2.3, 7일 0.4 vs 1.6, p<0.001), 개구량(3.5 vs 2.7 cm, p<0.001)을 유의하게 개선하고 7일째 부종도 줄였으며(2.1 vs 2.8 cm, p=0.04) 이상반응은 없었다.
  - ▸ 출발(`tamgadge-2025-preoperative-dexamethasone-third-molar-pain-swelling-trismus`) 한줄: split-mouth 단일맹검 위약대조 시험 (n=60, 양측 매복 하악 사랑니): 술전 dexamethasone 4 mg 근육주사 1회가 위약 대비 술후 통증(2일 1.2 vs 2.3, 7일 0.4 vs 1.6, p<0.001), 개구량(3.5 vs 2.7 cm, p<0.001)을 유의하게 개선하고 7일째 부종도 줄였으며(2.1 vs 2.8 cm, p=0.04) 이상반응은 없었다.

- `magesty-2026-adverse-events-oral-analgesics-third-molar-nma` [drug/analgesics] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: 28개 RCT(5306명, 하악 제3대구치 발치)의 빈도주의 네트워크 메타분석: 단회 경구 NSAID 단독이 SUCRA 안전성 순위에서 가장 위험(86.5%)·위약이 2위(81.7%), NSAID+비마약성+마약성 3제 병용이 가장 안전(15.5%)했으나, 근거 확실성이 매우 낮음~낮음이고 위약군 이상반응도 높아 실제 NSAID 위해보다 노세보 효과가 주된 기전으로 해석됨.
  - ▸ 출발(`magesty-2026-adverse-events-oral-analgesics-third-molar-nma`) 한줄: 28개 RCT(5306명, 하악 제3대구치 발치)의 빈도주의 네트워크 메타분석: 단회 경구 NSAID 단독이 SUCRA 안전성 순위에서 가장 위험(86.5%)·위약이 2위(81.7%), NSAID+비마약성+마약성 3제 병용이 가장 안전(15.5%)했으나, 근거 확실성이 매우 낮음~낮음이고 위약군 이상반응도 높아 실제 NSAID 위해보다 노세보 효과가 주된 기전으로 해석됨.

- `franco-de-la-torre-2021-analgesic-efficacy-etoricoxib-following-third` [drug/analgesics] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: 8편의 고품질 임상시험(6편 메타분석)을 종합한 SR+MA로, etoricoxib(주로 120 mg)가 사랑니 수술 후 비선택적 NSAID 대비 구제 진통제가 필요한 환자 수를 유의하게 줄였고(p=0.0004, 이부프로펜 400 mg 대비 p=0.00001), 이상반응에는 유의한 차이가 없었다.
  - ▸ 출발(`franco-de-la-torre-2021-analgesic-efficacy-etoricoxib-following-third`) 한줄: 8편의 고품질 임상시험(6편 메타분석)을 종합한 SR+MA로, etoricoxib(주로 120 mg)가 사랑니 수술 후 비선택적 NSAID 대비 구제 진통제가 필요한 환자 수를 유의하게 줄였고(p=0.0004, 이부프로펜 400 mg 대비 p=0.00001), 이상반응에는 유의한 차이가 없었다.

- `gousias-2025-preemptive-analgesia-periodontal-implant-sr-ma` [drug/analgesics] (HIGH-no-target, 'in contrast to' · 대조)
  - **근거 문장**: JCP 2025 SR+MA (Gousias, 18 RCTs included, 1,995 titles screened): preemptive analgesia vs placebo in periodontal and implant surgery (OFD, gingival augmentation, implant site development, implant placement) evaluated at multiple timepoints — preemptive analgesia significantly reduces pain; positive update specific to this specialty context, in contrast to Costa 2015's negative finding for third-m
  - ▸ 출발(`gousias-2025-preemptive-analgesia-periodontal-implant-sr-ma`) 한줄: JCP 2025 SR+MA (Gousias, 18 RCT 포함, 1,995 titles screened): 치주 + 임플란트 수술 (OFD, gingival augmentation, implant site development, implant placement) — preemptive 진통제 vs 위약 다중 timepoint 평가; preemptive analgesia가 통증 유의 감소 — Costa 2015 (제3대구치 부정적)의 specialty-specific 양성 update.

- `watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma` [drug/analgesics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This evidence directly contradicts the long-standing US prescribing pattern of opioid combination products for routine third molar pain and supports the modern opioid-sparing dental prescribing position (ADA 2022 acute dental pain guidelines).
  - ▸ 출발(`watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma`) 한줄: SR+MA (Pain Med 2022, SIU/WashU/UH): 제3대구치 발치 후 통증 — APAP 600 + codeine 60 병용 vs ibuprofen 400 단독 — ibuprofen 단독이 동등 또는 우수, opioid combination 정당화 부족 → ADA 2022 opioid-sparing 가이드라인 직접 지지.

- `etikala-2019-nsaids-periodontal-implant-therapy-review` [drug/analgesics] (HIGH-no-target, 'conflicting result' · 상충 결과)
  - **근거 문장**: Narrative review (9 periodontal studies, 6 implant studies): NSAIDs produce conflicting results for periodontal wound healing; selective COX-2 inhibitors may inhibit peri-implant bone formation; very limited human clinical evidence — clinicians prescribing NSAIDs after dental surgery should be aware of potential impact on osseous healing (Compend 2019).
  - ▸ 출발(`etikala-2019-nsaids-periodontal-implant-therapy-review`) 한줄: 서술적 고찰(치주 9편·임플란트 6편): NSAIDs가 치주 상처 치유에 상충된 결과; 선택적 COX-2 억제제는 임플란트 주위 골형성 억제 가능; 인체 임상 근거 매우 부족 — 치과 외과술 후 NSAID 처방 시 골유착 영향 인지 필요 (Compend 2019).

- `etikala-2019-nsaids-periodontal-implant-therapy-review` [drug/analgesics] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 서술적 고찰(치주 9편·임플란트 6편): NSAIDs가 치주 상처 치유에 상충된 결과; 선택적 COX-2 억제제는 임플란트 주위 골형성 억제 가능; 인체 임상 근거 매우 부족 — 치과 외과술 후 NSAID 처방 시 골유착 영향 인지 필요 (Compend 2019).
  - ▸ 출발(`etikala-2019-nsaids-periodontal-implant-therapy-review`) 한줄: 서술적 고찰(치주 9편·임플란트 6편): NSAIDs가 치주 상처 치유에 상충된 결과; 선택적 COX-2 억제제는 임플란트 주위 골형성 억제 가능; 인체 임상 근거 매우 부족 — 치과 외과술 후 NSAID 처방 시 골유착 영향 인지 필요 (Compend 2019).

- `etikala-2019-nsaids-periodontal-implant-therapy-review` [drug/analgesics] (HIGH-no-target, 'conflicting result' · 상충 결과)
  - **근거 문장**: Narrative literature review addressing two clinical questions: (1) how do NSAIDs affect periodontal wound healing? (2) do NSAIDs affect osseointegration of dental implants? 9 clinical studies on periodontal healing showed conflicting results — no clear conclusion. For dental implant osseointegration, 4 animal studies and 2 human clinical studies were reviewed; selective COX-2 inhibitors specifical
  - ▸ 출발(`etikala-2019-nsaids-periodontal-implant-therapy-review`) 한줄: 서술적 고찰(치주 9편·임플란트 6편): NSAIDs가 치주 상처 치유에 상충된 결과; 선택적 COX-2 억제제는 임플란트 주위 골형성 억제 가능; 인체 임상 근거 매우 부족 — 치과 외과술 후 NSAID 처방 시 골유착 영향 인지 필요 (Compend 2019).

- `etikala-2019-nsaids-periodontal-implant-therapy-review` [drug/analgesics] (HIGH-no-target, 'conflicting result' · 상충 결과)
  - **근거 문장**: - Periodontal healing: NSAIDs produce conflicting results; not established as harmful or helpful
  - ▸ 출발(`etikala-2019-nsaids-periodontal-implant-therapy-review`) 한줄: 서술적 고찰(치주 9편·임플란트 6편): NSAIDs가 치주 상처 치유에 상충된 결과; 선택적 COX-2 억제제는 임플란트 주위 골형성 억제 가능; 인체 임상 근거 매우 부족 — 치과 외과술 후 NSAID 처방 시 골유착 영향 인지 필요 (Compend 2019).

- `ruggiero-2022-aaoms-mronj-position-paper-update` [drug/mronj] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - No RCT data sufficient to support or refute
  - ▸ 출발(`ruggiero-2022-aaoms-mronj-position-paper-update`) 한줄: AAOMS 2022 MRONJ 포지션 페이퍼: 진단기준·스테이징 2014년 동일, romosozumab 추가, 약물 중단(drug holiday) 권고 없이 논쟁 중, CTX 더 이상 권장 안 함, denosumab 중단 시 6주~3개월 timing 제안.

- `ufcd-2019-medically-complex-patients-management-guidelines` [drug/mronj] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: - 치료 중 사용 약물(항생제, LA, 혈관수축제, N2O, NSAIDs)에 대한 이상반응 위험
  - ▸ 출발(`ufcd-2019-medically-complex-patients-management-guidelines`) 한줄: UF 치과대학 임상 가이드라인(148쪽): 23개 전신질환 카테고리 × 치과 관리 프로토콜; ASA 분류; 혈관수축제 사용 지침; 의과 협진 적응증 — 가장 포괄적인 단일 레퍼런스 문서

- `mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma` [implants/peri-implantitis] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Underscored that even patients under regular implant maintenance with inadequate KM carry elevated peri-implantitis risk (OR=2.08), contradicting the view that maintenance compensates for tissue deficiency.
  - ▸ 출발(`mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma`) 한줄: 22편 SR+MA(환자 4,044명, 임플란트 13,265개)에서 각화점막 부족이 주위염의 독립적 위험인자임을 5가지 하위군 분석(교란변수 보정 포함)으로 일관되게 확인하였다(전체 OR=2.78, 95% CI 2.07–3.74).

- `diaz-2022-what-is-the-prevalence` [implants/peri-implantitis] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: Fills a 5-year currency gap against the older epidemiology anchor [[wiki/implants/derks-2015-peri-implant-health-disease-epidemiology]]: a 57-study SR+MA (search window through Dec 2021) that re-estimates peri-implantitis prevalence and quantifies how case definition, probing-depth use, and function time move the number. It refines, not overturns, the older anchor by showing the estimate is still 
  - ▸ 출발(`diaz-2022-what-is-the-prevalence`) 한줄: 57편 SR+MA: 임플란트주위염 유병률 환자 단위 19.53% (95% CI 12.87–26.19), 임플란트 단위 12.53%; 진단 정의에 크게 좌우되며 탐침 깊이 기준 사용 시 더 높음.

- `sbricoli-2026-peri-implant-disease-prevalence-type2-diabetes` [implants/peri-implantitis] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/peri-implantitis/diaz-2022-what-is-the-prevalence]] — contradicts: this T2DM-vs-non-DM null result tempers the systemic-risk-factor framing of peri-implantitis prevalence.
  - ▸ 출발(`sbricoli-2026-peri-implant-disease-prevalence-type2-diabetes`) 한줄: 단일기관 횡단연구(70명·임플란트 227개; 제2형 당뇨 35명 vs 비당뇨 35명): 임플란트주위질환(80% vs 77%, p=0.99)·점막염(51% vs 63%, p=0.47)·주위염(51% vs 43%, p=0.63) 모두 두 군 간 유의차 없음. 단, 검정력 부족 + 양 군 모두 치주염 과거력(83~94%)이 높아 당뇨 단독 효과가 가려졌을 가능성.

- `pujarern-2024-biofilm-removal-implant-airflow-erythritol` [implants/peri-implantitis] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refuted the larger-particle-cleans-better hypothesis: SB and ERY equivalent in biofilm removal.
  - ▸ 출발(`pujarern-2024-biofilm-removal-implant-airflow-erythritol`) 한줄: 체외(in-vitro) 연구(임플란트 33개, 3군 각 n=11): 탄산수소나트륨(Sodium Bicarbonate, SB, 40 µm)과 에리스리톨(Erythritol, ERY, 14 µm) air-polishing 파우더 모두 무처치 대조군 대비 생물막을 훨씬 잘 제거(평균 광학밀도 OD 0.130·0.129 vs 0.728; p<0.05)했고 둘 사이 차이는 유의하지 않아(p>0.05), 표면 손상이 적은 에리스리톨이 임상적으로 선호된다.

- `francis-2024-low-serum-vitamin-d-early-implant-failure` [implants/vitamin-d] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: This prospective cohort assessed whether serum vitamin D levels measured on the day of implant placement relate to early dental implant failure. Across 174 implants in 109 patients followed to restoration (~3–6 months), 8 patients experienced an early failure (defined as ≥50% bone loss or implant mobility). Contrary to the prevailing hypothesis, the failed cases had a *higher* mean serum vitamin D
  - ▸ 출발(`francis-2024-low-serum-vitamin-d-early-implant-failure`) 한줄: 전향적 코호트(임플란트 174개 / 환자 109명)에서 낮은 혈청 25-하이드록시비타민 D(serum 25(OH)D)와 조기 임플란트 실패(Early Dental Implant Failure, EDIF) 사이에 유의한 상관관계가 없었던 음성 결과(negative/no-correlation) 연구 — 실패한 8건은 오히려 성공군(31.92 ng/mL)보다 높은 평균 비타민 D(42.54 ng/mL)를 보임.

- `francis-2024-low-serum-vitamin-d-early-implant-failure` [implants/vitamin-d] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/vitamin-d/mohsen-2024-vitamin-d-deficiency-osseointegration-prospective]] — **contradicts**: Mohsen's prospective study reports a positive vitamin D → osseointegration association; this cohort finds the opposite directionality (higher vitamin D in failures, no significant correlation).
  - ▸ 출발(`francis-2024-low-serum-vitamin-d-early-implant-failure`) 한줄: 전향적 코호트(임플란트 174개 / 환자 109명)에서 낮은 혈청 25-하이드록시비타민 D(serum 25(OH)D)와 조기 임플란트 실패(Early Dental Implant Failure, EDIF) 사이에 유의한 상관관계가 없었던 음성 결과(negative/no-correlation) 연구 — 실패한 8건은 오히려 성공군(31.92 ng/mL)보다 높은 평균 비타민 D(42.54 ng/mL)를 보임.

- `francis-2024-low-serum-vitamin-d-early-implant-failure` [implants/vitamin-d] (SOFT→miron-2025-vitamin-d-deficiency-early-implant-failure, 'Unlike' · 다름)
  - **근거 문장**: This is the contrarian / negative-evidence anchor for the vitamin D → implant-failure subdomain. Unlike the consensus signal in the systematic-review and the strongly-positive prospective findings of Mohsen 2024, this cohort found NO correlation between low serum vitamin D and early implant failure — and notably the failed implants occurred in patients with a *higher* mean serum vitamin D (42.54 n
  - ▸ 출발(`francis-2024-low-serum-vitamin-d-early-implant-failure`) 한줄: 전향적 코호트(임플란트 174개 / 환자 109명)에서 낮은 혈청 25-하이드록시비타민 D(serum 25(OH)D)와 조기 임플란트 실패(Early Dental Implant Failure, EDIF) 사이에 유의한 상관관계가 없었던 음성 결과(negative/no-correlation) 연구 — 실패한 8건은 오히려 성공군(31.92 ng/mL)보다 높은 평균 비타민 D(42.54 ng/mL)를 보임.
  - ▸ 대상(`miron-2025-vitamin-d-deficiency-early-implant-failure`) 한줄: 체계적 문헌고찰(43편 = 동물 16편 + 사람 27편, 2025년 5월까지 검색)로, 비타민 D 결핍(Vitamin D deficiency)이 조기 임플란트 실패(Early Dental Implant Failure, EDIF)를 최대 4배까지 증가시키며, 수술 전 보충이 당뇨 등 고위험군에서도 골-임플란트 접촉(Bone-to-Implant Contact, BIC)과 골유착을 개선했다고 보고.

- `francis-2024-low-serum-vitamin-d-early-implant-failure` [implants/vitamin-d] (SOFT→moy-2005-dental-implant-failure-rates-risk, 'Unlike' · 다름)
  - **근거 문장**: This is the contrarian / negative-evidence anchor for the vitamin D → implant-failure subdomain. Unlike the consensus signal in the systematic-review and the strongly-positive prospective findings of Mohsen 2024, this cohort found NO correlation between low serum vitamin D and early implant failure — and notably the failed implants occurred in patients with a *higher* mean serum vitamin D (42.54 n
  - ▸ 출발(`francis-2024-low-serum-vitamin-d-early-implant-failure`) 한줄: 전향적 코호트(임플란트 174개 / 환자 109명)에서 낮은 혈청 25-하이드록시비타민 D(serum 25(OH)D)와 조기 임플란트 실패(Early Dental Implant Failure, EDIF) 사이에 유의한 상관관계가 없었던 음성 결과(negative/no-correlation) 연구 — 실패한 8건은 오히려 성공군(31.92 ng/mL)보다 높은 평균 비타민 D(42.54 ng/mL)를 보임.
  - ▸ 대상(`moy-2005-dental-implant-failure-rates-risk`) 한줄: 코호트 (4,680개, 21년): 당뇨 RR 2.75·두경부방사선 RR 2.73·흡연 RR 1.56 유의; 하악전치부 최저 실패율(2.89%)

- `keller-2026-3d-printed-titanium-mesh-autologous-bone` [implants/vertical-ridge-augmentation] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Directly contradicts the assumption that 3D-printed Ti mesh = high exposure (cf. Soares 2025)
  - ▸ 출발(`keller-2026-3d-printed-titanium-mesh-autologous-bone`) 한줄: 후향 연구 (n=16): DMLS 마이크로퍼포레이션 grade-2 Ti 메쉬 + 순수 자가골 → 16증례 연속 메쉬 노출 0%; 계획 골증대량과 실제 CBCT 결과가 통계적으로 동등.

- `keller-2026-3d-printed-titanium-mesh-autologous-bone` [implants/vertical-ridge-augmentation] (HIGH-no-target, '상반' · 상반)
  - **근거 문장**: 노출 0% 사례를 보고한 소규모 후향 연구로서, 메쉬 설계(마이크로퍼포레이션 grade-2 Ti) + 순수 자가골 조합이 [[wiki/implants/vertical-ridge-augmentation/sabri-2024-titanium-mesh-bone-augmentation-sr-ma]] 풀드 노출률(10.8%)과 상반되는 실제 zero-exposure 사례를 제공한다. 왜 노출이 생기지 않았는지에 대한 기술적 가설(micro-perforated design, 2-screw, pure autograft)을 문헌화.
  - ▸ 출발(`keller-2026-3d-printed-titanium-mesh-autologous-bone`) 한줄: 후향 연구 (n=16): DMLS 마이크로퍼포레이션 grade-2 Ti 메쉬 + 순수 자가골 → 16증례 연속 메쉬 노출 0%; 계획 골증대량과 실제 CBCT 결과가 통계적으로 동등.

- `iwasa-2011-tio2-micro-nano-hybrid-biological-aging` [implants/surface] (HIGH-no-target, 'in contrast to' · 대조)
  - **근거 문장**: In vitro study showing that TiO2 nanonodules (300 nm) deposited on micropit titanium create a micro-nano-hybrid surface that sustains bioactivity for ≥7 days after UV photofunctionalization — in contrast to micropit-only surfaces which show 30-50% bioactivity decay. Key finding: the anti-aging mechanism is sustained electropositivity from TiO2 nanonodules, independent of hydrophilicity (hybrid sur
  - ▸ 출발(`iwasa-2011-tio2-micro-nano-hybrid-biological-aging`) 한줄: 인비트로(IJN 2011): TiO2 나노결절(300 nm) + 마이크로피트 하이브리드 표면 → UV 광기능화 (Photofunctionalization) 후 7일까지 생체활성 유지 (마이크로 단독 대비 30–50% 감소 방지); 기전은 친수성이 아닌 양전하 (Electropositivity) 지속.

- `witek-2020-boronized-surface-osseointegration` [implants/surface] (HIGH-no-target, 'contrary to' · 상반된 결과)
  - **근거 문장**: The central finding was unexpected and contrary to in vitro predictions: both boronized groups showed declining BIC and BAFO from 3 to 6 weeks, while both control groups showed significant increases. At 6 weeks, CAA controls demonstrated the highest osseointegration, while BAA implants showed the sharpest decline in BIC (21.73% at 3 wk → 5.93% at 6 wk). Non-decalcified histology confirmed the abse
  - ▸ 출발(`witek-2020-boronized-surface-osseointegration`) 한줄: 양 장골 동물 모델(n=5, 3·6주)에서 보론화 티타늄 임플란트의 BIC와 BAFO가 산부식 대조군보다 유의하게 낮고 시간 경과에 따라 감소하여, 보론화 표면처리가 골유착을 억제함을 확인하였다.

- `lages-2018-isq-insertion-torque-correlation-sr` [implants/isq] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: > 48-study SR+MA (pooled r=0.44, p<0.001, moderate significant) overturns this 12-study NS result (r=0.366, p=0.079). Prefer Tisci 2026 for the IT–ISQ correlation question. (set 2026-05-31)
  - ▸ 출발(`lages-2018-isq-insertion-torque-correlation-sr`) 한줄: SR (12편, PRISMA): 삽입토크와 ISQ 간 유의한 상관관계 없음(r=0.366, p=0.079); 두 측정법은 독립적·비교 불가 — 임상 결정 시 한 가지 방법만 사용할 것 권고; 근거 확실도 낮음 (CIDRE 2018).

- `kim-2013-implant-stability-retrospective-rfa-isq` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Bischof et al. (cited) — found jaw position significant but diameter/length not significant; partially contradicts this study's diameter finding
  - ▸ 출발(`kim-2013-implant-stability-retrospective-rfa-isq`) 한줄: Osstem 임플란트 90개 후향적 RFA 연구: 직경 5 mm가 4 mm보다, 하악이 상악보다 ISQ 유의하게 높음; 길이(10–13 mm)는 ISQ에 유의한 영향 없음; 전 군에서 식립 후 인상채득 시 ISQ 증가.

- `al-ahmari-2022-osseodensification-conventional-low-density-jaw` [implants/isq] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Split-mouth in vivo clinical study in low-density jaw bone (20 patients, 40 implants): osseodensification (OD) vs conventional drilling differed significantly only in immediate post-op bone density, while primary/secondary stability, plaque index, BOP, pocket depth, and marginal bone loss showed no significant difference — a human counterpoint to OD-favorable pooled literature.
  - ▸ 출발(`al-ahmari-2022-osseodensification-conventional-low-density-jaw`) 한줄: 저밀도 골 split-mouth 인체 연구(20명, 40 implant): 골밀도만 OD에서 유의하게 높고, 1차/2차 안정성·PI·BOP·PD·MBL은 유의차 없음 — OD 안정성 우위의 임상 반례.

- `al-ahmari-2022-osseodensification-conventional-low-density-jaw` [implants/isq] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Provides a human controlled counterpoint to the OD-favorable pooled literature: when stability is measured directly in a split-mouth design, OD's advantage largely fails to reach significance (only density). Important for bounding OD claims.
  - ▸ 출발(`al-ahmari-2022-osseodensification-conventional-low-density-jaw`) 한줄: 저밀도 골 split-mouth 인체 연구(20명, 40 implant): 골밀도만 OD에서 유의하게 높고, 1차/2차 안정성·PI·BOP·PD·MBL은 유의차 없음 — OD 안정성 우위의 임상 반례.

- `oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma` [implants/soft-tissue] (SOFT→mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma, 'Unlike' · 다름)
  - **근거 문장**: It complements the risk-factor SRs ([[mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma]], [[ravida-2022-keratinized-mucosa-width-peri-implant-disease-sr-ma]]) by quantifying the *upside of intervention*, and pairs with the consensus/technique guidance ([[sanz-2022-keratinized-mucosa-around-implants-consensus]], [[zhang-2025-expert-consensus-km-augmentation-second-stage]]). Unlike Sanz
  - ▸ 출발(`oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma`) 한줄: SR+MA(임상 11편, 290명): 기능 중인 임플란트에서 FGG는 각화점막을 가중평균 2.6 mm 늘리고 염증을 줄였으며 4년까지 치조정골 변화가 없었고, CTG는 점막 퇴축을 가중평균 2 mm 감소시켰다.
  - ▸ 대상(`mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma`) 한줄: 22편 SR+MA(환자 4,044명, 임플란트 13,265개)에서 각화점막 부족이 주위염의 독립적 위험인자임을 5가지 하위군 분석(교란변수 보정 포함)으로 일관되게 확인하였다(전체 OR=2.78, 95% CI 2.07–3.74).

- `oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma` [implants/soft-tissue] (SOFT→ravida-2022-keratinized-mucosa-width-peri-implant-disease-sr-ma, 'Unlike' · 다름)
  - **근거 문장**: It complements the risk-factor SRs ([[mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma]], [[ravida-2022-keratinized-mucosa-width-peri-implant-disease-sr-ma]]) by quantifying the *upside of intervention*, and pairs with the consensus/technique guidance ([[sanz-2022-keratinized-mucosa-around-implants-consensus]], [[zhang-2025-expert-consensus-km-augmentation-second-stage]]). Unlike Sanz
  - ▸ 출발(`oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma`) 한줄: SR+MA(임상 11편, 290명): 기능 중인 임플란트에서 FGG는 각화점막을 가중평균 2.6 mm 늘리고 염증을 줄였으며 4년까지 치조정골 변화가 없었고, CTG는 점막 퇴축을 가중평균 2 mm 감소시켰다.
  - ▸ 대상(`ravida-2022-keratinized-mucosa-width-peri-implant-disease-sr-ma`) 한줄: SR+MA+TSA (9연구, 685임플란트, 개입 연구 한정): 각화점막폭(KMW) <2 mm는 플라크 지수만 유의하게 높았고(MD 0.37, TSA 확정), 변연골소실·탐침깊이·연조직 퇴축은 TSA상 검정력 부족으로 결론 불확정 — KMW 양 자체가 임플란트 주위 질환의 위험인자로 작용하는 근거 수준은 낮음(GRADE: very low~low).

- `oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma` [implants/soft-tissue] (SOFT→sanz-2022-keratinized-mucosa-around-implants-consensus, 'Unlike' · 다름)
  - **근거 문장**: It complements the risk-factor SRs ([[mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma]], [[ravida-2022-keratinized-mucosa-width-peri-implant-disease-sr-ma]]) by quantifying the *upside of intervention*, and pairs with the consensus/technique guidance ([[sanz-2022-keratinized-mucosa-around-implants-consensus]], [[zhang-2025-expert-consensus-km-augmentation-second-stage]]). Unlike Sanz
  - ▸ 출발(`oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma`) 한줄: SR+MA(임상 11편, 290명): 기능 중인 임플란트에서 FGG는 각화점막을 가중평균 2.6 mm 늘리고 염증을 줄였으며 4년까지 치조정골 변화가 없었고, CTG는 점막 퇴축을 가중평균 2 mm 감소시켰다.
  - ▸ 대상(`sanz-2022-keratinized-mucosa-around-implants-consensus`) 한줄: DGI/SEPA/Osteology 2022 합의 보고서 (34개 성명·2편 SR): KPIM < 2 mm는 임플란트 주위염·치태·점막퇴축·변연골소실 증가와 연관되고, 자유치은이식(FGG)이 표준술식이며 이종이식(xenograft)은 결합조직이식(CTG)과 동등하면서도 이환율이 낮은 대안으로 합의된다.

- `oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma` [implants/soft-tissue] (SOFT→zhang-2025-expert-consensus-km-augmentation-second-stage, 'Unlike' · 다름)
  - **근거 문장**: It complements the risk-factor SRs ([[mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma]], [[ravida-2022-keratinized-mucosa-width-peri-implant-disease-sr-ma]]) by quantifying the *upside of intervention*, and pairs with the consensus/technique guidance ([[sanz-2022-keratinized-mucosa-around-implants-consensus]], [[zhang-2025-expert-consensus-km-augmentation-second-stage]]). Unlike Sanz
  - ▸ 출발(`oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma`) 한줄: SR+MA(임상 11편, 290명): 기능 중인 임플란트에서 FGG는 각화점막을 가중평균 2.6 mm 늘리고 염증을 줄였으며 4년까지 치조정골 변화가 없었고, CTG는 점막 퇴축을 가중평균 2 mm 감소시켰다.
  - ▸ 대상(`zhang-2025-expert-consensus-km-augmentation-second-stage`) 한줄: 중국 다기관 전문가 컨센서스(IJOS 2025, 저자 29인): 임플란트 2차 수술 시 각화점막 증대를 위해 임플란트 위치·잔존 각화점막 폭·점막 두께에 따른 ARF·FGG·SFGG·소프트티슈 대체재 선택 결정 트리를 제시한 실용적 임상 가이드.

- `bhatavadekar-2012-peri-implant-soft-tissue-management-narrative` [implants/soft-tissue] (HIGH-no-target, 'conflicting evidence' · 상충 결과)
  - **근거 문장**: On the keratinized mucosa (KM) debate, the author acknowledges conflicting evidence — some studies finding no statistical long-term advantage, others linking KM to better health and patient satisfaction — and expresses a clinical opinion that KM provides a "layer of protection" against plaque accumulation and mechanical insult, supported by a cited study showing thick mucosa (≥1 mm) correlates wit
  - ▸ 출발(`bhatavadekar-2012-peri-implant-soft-tissue-management-narrative`) 한줄: J Indian Soc Periodontol 2012 단신으로, 임플란트 주위 연조직 관리의 진화(소켓 압박→보존 철학 전환, 각화점막 논쟁, 결합조직이식·VIP-CT 술식, 유두 재건 원칙)를 임상 관점에서 종합 기술하였다.

- `rios-osorio-2025-xcm-vs-ctg-fgg-implant-soft-tissue-sr-ma` [implants/soft-tissue] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - First SR+MA to separately analyse crosslinked (VCMX) vs non-crosslinked (XCM*) porcine collagen matrices against CTG, resolving previous contradictions from pooled analyses.
  - ▸ 출발(`rios-osorio-2025-xcm-vs-ctg-fgg-implant-soft-tissue-sr-ma`) 한줄: 17편 RCT SR+MA: 임플란트 부위 연조직 증대에서 비가교 이종 콜라겐 매트릭스 (XCM, Xenogeneic Collagen Matrix)는 결합조직이식 (CTG, Connective Tissue Graft) 대비 점막두께 (MT, Mucosal Thickness) 열위(MD −0.27 mm, P=0.01)이나 가교형 VCMX는 CTG와 동등; 유리치은이식 (FGG, Free Gingival Graft)은 XCM 대비 각화점막폭 (KMW, Keratinized Mucosa Width) 1.

- `neves-2023-socket-shield-stress-distribution-fea` [immediate-implant/socket-shield] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - Provides a biomechanical counterpoint to clinical socket-shield outcome studies.
  - ▸ 출발(`neves-2023-socket-shield-stress-distribution-fea`) 한줄: 유한요소분석 — 소켓 쉴드(SS, 2.0 mm 치근편)·이종골이식(HBG)·완전 골내 대조(C) 비교에서 SS와 HBG 모두 대조군보다 주위골 응력이 높았고, SS가 주위 조직 응력 집중이 가장 컸다.

- `araujo-2026-buccal-gap-width-alveolar-reduction-iip-cbct` [immediate-implant/esthetic-soft-tissue] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[immediate-implant/esthetic-soft-tissue/yang-2019-labial-bone-thickness-esthetics-iipp]] — contradicts: Yang found buccal bone thickness < 0.5 mm worsens resorption; here baseline buccal thickness was non-significant once gap width was accounted for in thin-walled central-incisor sites.
  - ▸ 출발(`araujo-2026-buccal-gap-width-alveolar-reduction-iip-cbct`) 한줄: 후향적 CBCT 코호트(상악 중절치 28부위, 반대측 자연치 대조, 평균 6년): DBBM으로 이식한 협측 gap이 2 mm 초과면 치조제 단면적의 90% 이상(8.5% 감소)을 보존했으나, 2 mm 이하 좁은 gap은 약 41% 흡수(p<0.001). gap 폭이 유일한 흡수 예측인자였고 기준 협측골 두께·결합조직이식(CTG)은 비유의.

- `bragues-2024-oral-mucositis-children-cancer-management-sr` [oral-medicine/mucositis] (SOFT→dean-2022-oral-chronic-gvhd-review, 'whereas' · 반면(대조))
  - **근거 문장**: The wiki's oral mucosal-disease coverage in `oral-medicine` (aphthous stomatitis, lichen planus, BMS) had no entry on cancer-therapy-induced oral mucositis — a high-incidence (40–100%) inflammatory condition distinct from those entities. This SR fills that gap and pairs with [[oral-medicine/dean-2022-oral-chronic-gvhd-review]], which covers the adjacent oncology context (oral chronic GVHD after he
  - ▸ 출발(`bragues-2024-oral-mucositis-children-cancer-management-sr`) 한줄: 소아 항암치료 구강점막염 치료를 다룬 체계적 문헌고찰 (PRISMA, 39편, n=14–148): 발생률엔 클로르헥시딘, 기간엔 꿀, 통증엔 올리브유가 가장 효과적이고 팔리퍼민은 발생률·중증도·기간을 줄였으나, 칼슘인산염은 효과 없음 — 전반적 근거는 아직 불충분.
  - ▸ 대상(`dean-2022-oral-chronic-gvhd-review`) 한줄: 구강 만성 GVHD 미니리뷰(동종 HCT 수혜자 30-50%): 태선양 점막염·타액선 기능저하·조직경화/개구장애 3주체, NIH 2014 기준과 국소→전신 면역억제 단계.

- `shahood-2024-cgf-bio-oss-osteotome-sinus-elevation` [sinus-lift/transcrestal] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[sansupakorn-2024-osfe-bcp-graft-versus-no-graft-rct]] — contradicts: BCP graft shows no benefit in RCT
  - ▸ 출발(`shahood-2024-cgf-bio-oss-osteotome-sinus-elevation`) 한줄: RBH ≤5mm OSFE 전향적 3군 비교(126임플란트): Bio-Oss Collagen+CGF 조합이 생존율 96%, 골이득·통증 측면에서 무이식·Bio-Oss 단독보다 우수.

- `sansupakorn-2024-osfe-bcp-graft-versus-no-graft-rct` [sinus-lift/transcrestal] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[shahood-2024-cgf-bio-oss-osteotome-sinus-elevation]] — contradicts: CGF+Bio-Oss Collagen superior to no-graft (graft type matters)
  - ▸ 출발(`sansupakorn-2024-osfe-bcp-graft-versus-no-graft-rct`) 한줄: RCT(30임플란트, 1년): OSFE+BCP(HA30:TCP70)는 무이식 OSFE 대비 ISQ·생존율·골이득 모두 차이 없으며, 오히려 변연골 변화는 무이식 군이 유의미하게 적음.

- `changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift` [sinus-lift/transcrestal] (HIGH-no-target, 'in contrast to' · 대조)
  - **근거 문장**: This prospective single-arm study from Bharati Vidyapeeth Dental College, Pune, India, evaluated the HaeNaem Zero Bone Loss Kit — a proprietary 골밀도화 (osseodensification, OD) bur system — for 경치조골 간접 상악동 거상 (indirect transcrestal sinus lift) in 12 patients with 잔존 치조골 높이 (residual crestal bone height, RCBH) of 6–8 mm. The study's primary contribution is clinical data on an alternative OD bur system
  - ▸ 출발(`changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift`) 한줄: 전향적 단일군 연구(n=12, 잔존 골고 6–8mm): HaeNaem Zero Bone Loss CW-OD 버 키트로 무이식 경치조골 간접 거상 동시 임플란트 식립 후 4개월 CBCT에서 근심·원심·협측·구개측 4개 방향 모두 유의한 골 높이 증가(p<0.01).

- `kozuma-2017-chronic-sinusitis-sinus-augmentation-infection` [sinus-lift/lateral] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: 4. **Membrane perforation is not the primary driver**: Contrary to common clinical emphasis, membrane perforation ranked below chronic sinusitis in both outcome models.
  - ▸ 출발(`kozuma-2017-chronic-sinusitis-sinus-augmentation-infection`) 한줄: 후향적 코호트 연구 (109명, 121개 상악동, 252개 임플란트): 술 전 만성 부비동염 (Chronic Sinusitis, CS)이 측방 상악동거상술 (Lateral Sinus Augmentation, LSA) 후 감염 (p=0.007) 및 임플란트 실패 (p=0.007)의 최강 예측인자로, 수술 전 이비인후과 평가·치료가 필수임을 다변량 분석으로 제시.

- `akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height` [sinus-lift/lateral] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: - Contradicts Maska 2017 finding (no significant ridge height association) — population difference likely
  - ▸ 출발(`akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height`) 한줄: 임플란트 후보 141명 CBCT(240 상악동): 잔존 치조제 높이가 낮을수록 상악동 점막비후 정도가 유의하게 크며, >3mm를 병적 기준으로 사용.

- `akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height` [sinus-lift/lateral] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[sinus-lift/lateral/maska-2017-implant-grafting-success-mucosal-thickening-sinus]] — contradictory: no significant ridge height association (different population, 4-tier index)
  - ▸ 출발(`akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height`) 한줄: 임플란트 후보 141명 CBCT(240 상악동): 잔존 치조제 높이가 낮을수록 상악동 점막비후 정도가 유의하게 크며, >3mm를 병적 기준으로 사용.

- `akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height` [sinus-lift/lateral] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 잔존 치조제 높이와 상악동 점막비후 간의 관계를 CBCT로 분석한 연구. 골 높이가 낮을수록 점막비후 위험이 높은지를 평가 — 임플란트 계획 시 사전 위험 계층화에 직접 활용 가능. [[sinus-lift/lateral/maska-2017-implant-grafting-success-mucosal-thickening-sinus]]와 대비되는 결과(ridge height 연관성 있음 vs 없음) 제공.
  - ▸ 출발(`akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height`) 한줄: 임플란트 후보 141명 CBCT(240 상악동): 잔존 치조제 높이가 낮을수록 상악동 점막비후 정도가 유의하게 크며, >3mm를 병적 기준으로 사용.

- `maska-2017-implant-grafting-success-mucosal-thickening-sinus` [sinus-lift/lateral] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[sinus-lift/lateral/akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height]] — found ridge height association (contradicts; different population/threshold)
  - ▸ 출발(`maska-2017-implant-grafting-success-mucosal-thickening-sinus`) 한줄: CBCT 후향적 연구(n=29, 평균 추적 3.3년): 93.1%에서 점막비후(65.5%가 중증 >5mm)에도 임플란트·골이식 생존율 100%, 치주질환 과거력만이 유의한 예측인자.

- `sartori-2003-msfa-bio-oss-10year-case-report` [sinus-lift/lateral] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: Sartori 등(2003)은 단일 환자에서 Bio-Oss 단독 상악동 거상 후 8개월·2년·10년에 동일 부위에서 trephine biopsy를 얻어 histomorphometry를 시행했다. 결과는 골 조직(골수강 포함) 비율이 29.8% → 69.7% → 86.7%로 단조 증가하고, Bio-Oss 입자는 그에 따라 70% → 30% → 13%로 진행성 흡수됐다. 단일 환자라는 결정적 한계가 있으나 10년 시간 trajectory의 인체 데이터는 매우 드물어, Bio-Oss의 "장기적으로 점진 흡수된다" 명제의 historical 근거. 단, Mordenfeld 2010(n=11, 11년 시점)에서는 "Bio-Oss 입자가 흡수되지 않는다"는 반대 결론이 나옴 — 두 논문의 상충은 [claude해석] g
  - ▸ 출발(`sartori-2003-msfa-bio-oss-10year-case-report`) 한줄: 단일 환자 case report — Bio-Oss 단독 MSFA 후 8개월 / 2년 / 10년 시점 trephine biopsy histomorphometry: 골조직(골수강 포함) 29.8% → 69.7% → 86.7%로 증가, Bio-Oss 입자는 점진적 흡수 — 10년 remodeling을 시간순으로 시각화한 교과서적 trajectory.

- `mordenfeld-2010-msfa-dpbb-biopsies-11year` [sinus-lift/lateral] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "DPBB가 흡수되지 않고 평생 잔존한다"는 명제 — 흡수성 이식재 marketing에 대한 반박 근거.
  - ▸ 출발(`mordenfeld-2010-msfa-dpbb-biopsies-11year`) 한줄: 11년 후 인체 biopsy (n=11, 80% DPBB + 20% 자가골 MSFA): 라멜라골 44.7% / 골수강 38% / DPBB 17.3%; DPBB-bone contact 61.5%; 입자 크기 6개월 시점·미사용 입자와 차이 없음 — DPBB는 흡수되지 않고 영구 osteoconductive scaffold로 통합.

- `mordenfeld-2010-msfa-dpbb-biopsies-11year` [sinus-lift/lateral] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: - [[sinus-lift/lateral/sartori-2003-msfa-bio-oss-10year-case-report]] — Bio-Oss 단독 10년 case report (DPBB 비율 70.2% → 13.3%로 감소 보고 — Mordenfeld 결과와 다소 상충).
  - ▸ 출발(`mordenfeld-2010-msfa-dpbb-biopsies-11year`) 한줄: 11년 후 인체 biopsy (n=11, 80% DPBB + 20% 자가골 MSFA): 라멜라골 44.7% / 골수강 38% / DPBB 17.3%; DPBB-bone contact 61.5%; 입자 크기 6개월 시점·미사용 입자와 차이 없음 — DPBB는 흡수되지 않고 영구 osteoconductive scaffold로 통합.

- `abullais-2024-maxillary-sinus-membrane-lateral-wall-cbct` [sinus-lift/lateral] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: The primary finding was **no significant correlation between facial index and either MT or LWT** (all p>0.05), refuting the hypothesis that facial morphotype could serve as a clinical surrogate for sinus anatomy. This means clinicians cannot use a patient's face shape to estimate surgical risk without a CBCT.
  - ▸ 출발(`abullais-2024-maxillary-sinus-membrane-lateral-wall-cbct`) 한줄: 후향적 원뿔빔 전산화 단층 촬영 (CBCT) 연구 (n=75, 150 상악동, 사우디): 안면지수 (Facial Index) 유형이 상악동 막 두께 (Membrane Thickness, MT) 및 측벽 두께 (Lateral Wall Thickness, LWT)와 무관; 여성의 LWT가 남성보다 유의하게 두꺼움(p<0.05); 소구치 MT > 대구치 MT (p<0.001).

- `schriber-2019-pneumatisation-maxillary-sinus-tooth-loss` [sinus-lift/lateral] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Direct radiographic refutation of "post-extraction sinus pneumatisation" as a meaningful driver of vertical bone loss in the posterior maxilla.
  - ▸ 출발(`schriber-2019-pneumatisation-maxillary-sinus-tooth-loss`) 한줄: 후향적 콘빔 컴퓨터단층촬영 (Cone-Beam Computed Tomography, CBCT) 체적 분석 (유치악 50명 vs 무치악 50명 후방 상악): 상악동 부피·표면·최대 직경에서 유의차 없음 → 발치 후 후방 상악의 수직 골량 감소는 상악동 함기화 (Pneumatisation)가 아닌 치조정 흡수 (Alveolar Crest Resorption)에 기인함을 시사. 남성이 여성보다 상악동이 유의하게 큼.

- `shenoy-2013-maxillary-antrolith-recurrent-sinusitis-case` [sinus-lift/pseudocyst] (HIGH-no-target, 'in contrast to' · 대조)
  - **근거 문장**: This Indian case report demonstrates the large/symptomatic end of the antrolith spectrum, in contrast to Tan 2020's asymptomatic small antrolith. The 47-year-old patient had a 1984 Caldwell-Luc surgery history for polypoid disease — residual bone chips left behind became the endogenous nidus for antrolith formation over decades.
  - ▸ 출발(`shenoy-2013-maxillary-antrolith-recurrent-sinusitis-case`) 한줄: 과거 Caldwell-Luc 수술 잔류 골편을 nidus로 한 2×1cm 대형 상악동석이 재발성 상악동염·구강상악동루 유발; ESS+Caldwell-Luc 복합 제거 후 완치 — ESS 후 충분한 세척으로 예방 권고.

- `bassir-2018-alveolar-ridge-preservation-meta-analysis` [bone-regeneration/ridge-preservation] (HIGH-no-target, 'Counterpoint' · 반대 논점)
  - **근거 문장**: - [[bone-regeneration/ridge-preservation/mardas-2023-alveolar-ridge-preservation-overtreatment]] — Counterpoint: when ARP may be overtreatment.
  - ▸ 출발(`bassir-2018-alveolar-ridge-preservation-meta-analysis`) 한줄: 체계적 문헌고찰 + 메타분석 (21편): 치조제 보존술(Alveolar Ridge Preservation, ARP)은 발치만 시행한 경우 대비 수평 골흡수를 평균 1.86 mm 감소시키며, 골 결손 형태·창상 폐쇄 방식·이식재·차폐막·성장인자 사용이 결과를 유의하게 좌우한다.

- `atieh-2021-interventions-replacing-missing-teeth` [bone-regeneration/ridge-preservation] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 16 RCT·524 socket·426명을 종합한 2021 Cochrane update — xenograft ARP가 자연치유 대비 width −1.18 mm·height −1.35 mm 감소를 보이나 GRADE 등급이 "very low"로 강등; 2015 결론을 뒤집어 "ARP의 임상적 의미는 불확실"이 새 메시지.
  - ▸ 출발(`atieh-2021-interventions-replacing-missing-teeth`) 한줄: 16 RCT·524 socket·426명을 종합한 2021 Cochrane update — xenograft ARP가 자연치유 대비 width −1.18 mm·height −1.35 mm 감소를 보이나 GRADE 등급이 "very low"로 강등; 2015 결론을 뒤집어 "ARP의 임상적 의미는 불확실"이 새 메시지.

- `adams-2022-clinical-evidence-alveolar-ridge-preservation` [bone-regeneration/ridge-preservation] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Avila-Ortiz·Majzoub 같은 ARP-positive SR 흐름에 대한 **수정주의적 counterpoint**. 영국 일반의가 자신의 진료실 케이스(5–10년 후 xenograft가 fibrous encapsulation·만성 감염·peri-implantitis 양상으로 실패)를 BDJ에 보고하며, "통계적 dimensional preservation"이 "long-term patient benefit"으로 자동 변환되지 않는다는 점을 강조. Adams 본인이 SR을 쓴 게 아니므로 evidence 등급은 낮으나, 동시기 Atieh 2021 Cochrane의 "very low certainty" 결론과 결이 맞아 ARP 임상 판단에 균형추로 인용 가치가 있음.
  - ▸ 출발(`adams-2022-clinical-evidence-alveolar-ridge-preservation`) 한줄: BDJ 게재 narrative review + 2개 case report로 ARP의 통계적 효과가 임상적 환자 이득으로 직결되지 않음을 지적, 5~13년 후 xenograft 만성 실패(섬유 포함·peri-implantitis 양상) 사례를 제시하며 ARP의 무차별 적용에 회의를 표함.

- `adams-2022-clinical-evidence-alveolar-ridge-preservation` [bone-regeneration/ridge-preservation] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[bone-regeneration/ridge-preservation/avila-ortiz-2019-alveolar-ridge-preservation-interventions]] — pro-ARP SR+MA, counterpoint.
  - ▸ 출발(`adams-2022-clinical-evidence-alveolar-ridge-preservation`) 한줄: BDJ 게재 narrative review + 2개 case report로 ARP의 통계적 효과가 임상적 환자 이득으로 직결되지 않음을 지적, 5~13년 후 xenograft 만성 실패(섬유 포함·peri-implantitis 양상) 사례를 제시하며 ARP의 무차별 적용에 회의를 표함.

- `araujo-2009-ridge-alterations-flap-vs-flapless` [bone-regeneration/ridge-preservation] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: 5-dog split-mouth 6-month histological comparison (full-thickness flap vs. flapless extraction) — both groups showed similar ridge resorption, refuting the claim that flapless extraction alone preserves the ridge.
  - ▸ 출발(`araujo-2009-ridge-alterations-flap-vs-flapless`) 한줄: 개 5마리 split-mouth(전층 판막 vs flapless) 6개월 조직학 비교 — 두 군 모두 발치 후 ridge resorption 발생, flap 거상 여부가 흡수량을 의미 있게 바꾸지 않음 → "flapless 발치만으로 ridge 보존" 주장 반박.

- `araujo-2009-ridge-alterations-flap-vs-flapless` [bone-regeneration/ridge-preservation] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 개 5마리 split-mouth(전층 판막 vs flapless) 6개월 조직학 비교 — 두 군 모두 발치 후 ridge resorption 발생, flap 거상 여부가 흡수량을 의미 있게 바꾸지 않음 → "flapless 발치만으로 ridge 보존" 주장 반박.
  - ▸ 출발(`araujo-2009-ridge-alterations-flap-vs-flapless`) 한줄: 개 5마리 split-mouth(전층 판막 vs flapless) 6개월 조직학 비교 — 두 군 모두 발치 후 ridge resorption 발생, flap 거상 여부가 흡수량을 의미 있게 바꾸지 않음 → "flapless 발치만으로 ridge 보존" 주장 반박.

- `araujo-2009-ridge-alterations-flap-vs-flapless` [bone-regeneration/ridge-preservation] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "Flapless = ridge 보존"이라는 1990s–2000s 임상 가설을 동물 모델에서 직접 반박.
  - ▸ 출발(`araujo-2009-ridge-alterations-flap-vs-flapless`) 한줄: 개 5마리 split-mouth(전층 판막 vs flapless) 6개월 조직학 비교 — 두 군 모두 발치 후 ridge resorption 발생, flap 거상 여부가 흡수량을 의미 있게 바꾸지 않음 → "flapless 발치만으로 ridge 보존" 주장 반박.

- `cesar-2024-dental-zirconia-15years-material-processing` [dental-materials/zirconia] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 5102편 문헌 분석 기반 서술적 고찰로, 2008–2023년 치과용 지르코니아의 3Y-TZP에서 다층 조성경사형 5Y-PSZ까지 15년 진화 과정·분말기술·소결·투광성-강도 상충관계를 총괄한다.
  - ▸ 출발(`cesar-2024-dental-zirconia-15years-material-processing`) 한줄: 5102편 문헌 분석 기반 서술적 고찰로, 2008–2023년 치과용 지르코니아의 3Y-TZP에서 다층 조성경사형 5Y-PSZ까지 15년 진화 과정·분말기술·소결·투광성-강도 상충관계를 총괄한다.

- `melini-2020-conscious-sedation-dental-anxiety-third-molar` [behavioral-dentistry/dental-anxiety] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 사랑니 발치 시 치과불안 관리를 위한 의식하 진정(conscious sedation) 체계적 고찰 (BMC Oral Health, RCT 17편·n=1788). 이질성으로 메타분석이 불가능해 서술적 종합을 시행 — 6편에서 불안 개선 신호(특히 midazolam, fentanyl/methohexital 병용)가 있었으나, 표준화된 결과 측정의 부재로 전체적으로 결론을 내릴 수 없고 상충됨.
  - ▸ 출발(`melini-2020-conscious-sedation-dental-anxiety-third-molar`) 한줄: 사랑니 발치 시 치과불안 관리를 위한 의식하 진정(conscious sedation) 체계적 고찰 (BMC Oral Health, RCT 17편·n=1788). 이질성으로 메타분석이 불가능해 서술적 종합을 시행 — 6편에서 불안 개선 신호(특히 midazolam, fentanyl/methohexital 병용)가 있었으나, 표준화된 결과 측정의 부재로 전체적으로 결론을 내릴 수 없고 상충됨.

- `bonetti-2018-general-health-promotion-dental-engage` [behavioral-dentistry/motivational-interviewing] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Quantifies — and largely refutes — the perceived-offense barrier clinicians assume.
  - ▸ 출발(`bonetti-2018-general-health-promotion-dental-engage`) 한줄: 스코틀랜드 ENGAGE 실행가능성 연구 — 검진 중 5분 이내 생활습관(흡연·음주·식이) 위험 전달 + 무료 NHS 상담전화 연결. 환자 거부감 거의 없음(<10%), GDP 18명 중 17명이 실행 가능·현행 개선으로 평가.

- `kapetanaki-2021-access-cavity-designs-endodontic-review` [endodontics/anatomy] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refutes the claim that MIA improves tooth prognosis over conventional TEC
  - ▸ 출발(`kapetanaki-2021-access-cavity-designs-endodontic-review`) 한줄: 문헌고찰: 최소침습 접근와동(MIA)은 근거 불충분 — 전통적 직선 접근와동이 기구 조작·의원성 합병증 예방에 더 안전한 표준.

- `cruz-2014-debris-apical-third-naocl-glyde-in-vivo` [endodontics/irrigation] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: This in vivo study tested whether an EDTA lubricating paste (Glyde File Prep) helps eliminate debris during cleaning and shaping. Contrary to the lubrication rationale, canals prepared with Glyde showed greater debris accumulation in the apical third, while canals prepared with sodium hypochlorite irrigation and a final rinse (no paste) were left with little or no apical debris. The practical impl
  - ▸ 출발(`cruz-2014-debris-apical-third-naocl-glyde-in-vivo`) 한줄: In vivo: 회전 기구조작 중 Glyde(EDTA paste) 사용이 apical third debris를 증가; NaOCl+최종 세척군은 debris 거의 없음.

- `nucera-2022-composite-attachments-clear-aligners-sr` [orthodontics/clear-aligner] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The answer: attachments **mostly increase** treatment effectiveness, with the clearest benefit for **anterior root torque, rotation, mesio-distal movement**, and **posterior anchorage** — exactly the movements aligners express poorly without purchase. Results were **contradictory or non-significant** for some movements; **intrusion** may improve but the evidence is weak; **extrusion** evidence is 
  - ▸ 출발(`nucera-2022-composite-attachments-clear-aligners-sr`) 한줄: SR(임상 5편, medium RoB): 컴포지트 attachment는 대체로 효과를 높임 — 전치부 torque·rotation·근원심 이동·후방 앵커리지 개선. 정출 근거 약함, 함입/후방 확장 근거 부족.

- `porporatti-2026-clear-aligners-bruxism-systematic-review` [orthodontics/clear-aligner] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The dominant signal is **neutrality**. No study showed a change in the overall **SB index**. A recurring nuance is that aligners tend to reduce **tonic** contractions (clenching / occlusal load) while their effect on **phasic** activity (grinding) is inconsistent — one RCT even reported a transient *increase* in phasic contractions. Most EMG effects appear in the first month and then fade, consist
  - ▸ 출발(`porporatti-2026-clear-aligners-bruxism-systematic-review`) 한줄: 체계적 문헌고찰 (11편, n=818, 여성 72.8%, 메타분석 불가): 투명교정장치 (Clear Aligner)는 이갈이 (Bruxism)에 대체로 **중립적** — 긴장성 수축 (tonic/clenching)은 자주 감소하나 위상성 수축 (phasic/grinding)과 수면이갈이지수 (SB index)에는 일관·지속 효과 없음. 보호인자도 위험인자도 아님 (근거수준 RCT 중등도, 비무작위 매우 낮음).
