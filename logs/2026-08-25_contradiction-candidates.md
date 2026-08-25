# 논쟁 레이더 백필 후보 — 2026-08-25

명시적 충돌 표현이 있으나 그 쌍에 `relations:` 타입 엣지(어떤 타입이든)도 `superseded_by:` 포인터도 없는 후보. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**

**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. 아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), (2) **양쪽 페이지의 `## 세줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. 충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. (reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것 — 2026-07-17 전수 검토에서 contradicts 계열로 지목된 122건 중 실제 contradicts는 1건이었다.)

**대상은 키워드에 가장 가까운 링크로 특정한다.** 같은 줄의 나머지 링크는 충돌 표현의 대상이라는 근거가 없어 Tier 2(`AMBIG→`)로 강등된다 — 버리지 않으니 진짜 대상이 강등됐다면 Tier 2에서 찾을 수 있다.

- Tier 1 (대상 지목됨, actionable): **2**
- Tier 2 (대상 불명/soft, review): **18**
- (억제됨) 이미 typed 엣지·supersession 포인터가 있어 제외: **278** · 부정문 제외: **101** · 검토·불필요 대장: **461** · 동일 줄 비최근접으로 Tier 2 강등: **0**

## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)

### implants/isq

- `naughton-2023-safemount-osstell-transducer-torque-isq`  —[상반된 · 상반]→  **`kastel-2019-smartpeg-torque-isq-rfa`**
  - **근거 문장**: > - [[implants/isq/kastel-2019-smartpeg-torque-isq-rfa]]과 **상반된 결과**: Kästel은 2–11 Ncm 전 범위 무차별이라 했으나, 본 논문은 수동 조임이 유의하게 낮은 ISQ 산출
  - ▸ 출발(`naughton-2023-safemount-osstell-transducer-torque-isq`) 세줄: 체외 폴리우레탄 뼈 블록 연구 (임플란트 7종, 56개, D1–D4 골질): 스마트팩 조임 방법 4종 비교 — 수동, 플라스틱 마운트, SafeMount, 정확한 토크 렌치 6 Ncm. 수동 조임이 정확한 토크 렌치 대비 유의하게 낮은 임플란트 안정성 지수 (Implant Stability Quotient, ISQ) 산출 (계수 −2.05, p<.001); SafeMount와 표준 플라스틱 마운트는 대조군과 유의차 없음. 골밀도가 ISQ 변이의 36%를 차지해 가장 큰 영향 인자였고, 술자는 6%
  - ▸ 대상(`kastel-2019-smartpeg-torque-isq-rfa`) 세줄: 체외 폴리우레탄 폼 연구(임플란트 4종, 스마트팩 3종): 수동 조임(2–11 Ncm)과 기계 조임(2–6 Ncm) 간 임플란트 안정성 지수 (Implant Stability Quotient, ISQ) 차이 없음(근심 p=0.343, 협측 p=0.890). 4가지 임플란트 시스템 전 군에서 조임 방법에 따른 ISQ 차이 없이 일관된 결과 확인. 임상에서 스마트팩 수동 조임은 공명주파수분석 (Resonance Frequency Analysis, RFA) 측정의 신뢰성을 충족하며, 별도의 토크 조절 


### oral-microbiology

- `pignatelli-2020-periodontal-disease-nitric-oxide-blood-pressure`  —[counterpoint · 반대 논점]→  **`elzein-2021-chlorhexidine-povidone-iodine-mouthwash-salivary-sars-cov-2-rct`**
  - **근거 문장**: This narrative review introduces a clinically important paradox: chlorhexidine mouthwash—widely recommended for preprocedural rinsing and ICU oral hygiene—may raise systemic blood pressure by 2–3.5 mmHg through disruption of oral nitrate-reducing bacteria essential to the nitric oxide vasodilatory pathway. This systemic risk is especially relevant for hypertensive patients and provides a critical 
  - ▸ 출발(`pignatelli-2020-periodontal-disease-nitric-oxide-blood-pressure`) 세줄: 이 내러티브 리뷰는 산화질소(NO) 경로를 통해 구강 미생물, 특히 질산염 환원 박테리아 및 치주 질환과 전신 혈압(BP) 간의 연관성을 탐구합니다. 내인성 NO는 주요 혈관 확장제이며, 식이 질산염(예: 채소)이 구강 내 공생 박테리아에 의해 아질산염으로 환원되고 위와 순환계에서 NO로 전환되는 "질산염-아질산염-NO 경로"에 의해 보충됩니다. 항균 구강 세정액(예: 클로르헥시딘) 또는 혀 세척에 의한 이 경로의 교란은 타액 아질산염 생성을 감소시켜 혈압 상승을 초래할 수 있습니다. 반대로, 병
  - ▸ 대상(`elzein-2021-chlorhexidine-povidone-iodine-mouthwash-salivary-sars-cov-2-rct`) 세줄: 본 연구는 COVID-19 양성 환자 61명(평균 연령 45.3 ± 16.7세)을 대상으로 0.2% 클로르헥시딘과 1% 포비돈-아이오딘 구강 세정액의 타액 내 SARS-CoV-2 불활성화 효과를 평가한 평행군, 이중맹검, 무작위배정, 위약대조 임상시험으로, 2020년 6월부터 9월까지 레바논 라피크 하리리 대학병원에서 수행되었다. 시술 전후(세정 30초, 5분 후) 타액을 채취하여 rRT-PCR로 주기 역치(CT) 변화를 측정하였다. 0.2% 클로르헥시딘과 1% 포비돈-아이오딘 모두 증류수 대비 


## Tier 2 — 대상 식별 필요 / soft signal (review only)

- `greenstein-2018-need-replace-missing-second-molar` [occlusion] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Synthesizes the paradox that super-eruption is common but occlusal interference is not a predictable downstream consequence, refuting reflexive replacement.
  - ▸ 출발(`greenstein-2018-need-replace-missing-second-molar`) 세줄: 제2대구치 (Second Molar) 결손 후 임플란트 (Implant) 수복 여부를 평가한 서술적 문헌고찰 — 저작효율 (Masticatory Efficiency)·과맹출·교합간섭 (Occlusal Interference) 데이터 종합. 제1대구치 교합만으로 저작효율 약 90% 달성; 대합치 없는 구치의 약 20%가 ≥2 mm 정출 (Supraeruption)하나, 정출 정도와 교합간섭 발생은 강한 상관이 없음. 수복 여부는 환자 선호 (Patient Preference)에 따름 — 저작 불편감

- `non-surgical-periodontal-therapy-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **CHX 대안·착색 완화**: 칫솔질 병행 상황에서 CPC는 CHX와 동등(Windhorst 2025 SR+MA, 14 RCT), 착색 유의 적음; CHX+ADS는 효능 비손상으로 착색 유의 감소(Van Swaaij 2019 SR+MA) — "착색 없으면 효과 없다" 통념 반박; 착색 우려 환자엔 CPC(칫솔질) 또는 CHX+ADS(비칫솔질) 선택. [확인]
  - ▸ 출발(`non-surgical-periodontal-therapy-overview`) 세줄: 치주 비수술 치료 31편 종합: SRP는 만성 치주염 1차 치료로 강력 권고(Smiley 2015 ADA), PPD 1-2mm 감소·CAL 0.5-1mm 획득; 전신 항생제 보조는 매우 낮은 확실성·임상 이득 미미로 routine 금지(Cochrane 2020, 45 RCT). NSPT는 구강 밖 선택적 항염증 효과가 있음 — CRP·IL-6·수축기혈압 감소하나 지질 프로필은 변화 없음(Meng 2024 SR+MA, 21 RCT); GBT는 환자 편의성 우수하나 임상 결과는 전통 SRD와 동등(Y

- `non-surgical-periodontal-therapy-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: **결론**: CHX+ADS는 수술 후 창상 보호 기간에 효능을 유지하면서 착색을 유의하게 줄임 — "착색이 없으면 효과도 없다"는 통념 반박. 착색 우려로 CHX 순응도가 낮을 환자에게 CHX+ADS 복합 제제 우선 권고.
  - ▸ 출발(`non-surgical-periodontal-therapy-overview`) 세줄: 치주 비수술 치료 31편 종합: SRP는 만성 치주염 1차 치료로 강력 권고(Smiley 2015 ADA), PPD 1-2mm 감소·CAL 0.5-1mm 획득; 전신 항생제 보조는 매우 낮은 확실성·임상 이득 미미로 routine 금지(Cochrane 2020, 45 RCT). NSPT는 구강 밖 선택적 항염증 효과가 있음 — CRP·IL-6·수축기혈압 감소하나 지질 프로필은 변화 없음(Meng 2024 SR+MA, 21 RCT); GBT는 환자 편의성 우수하나 임상 결과는 전통 SRD와 동등(Y

- `immediate-implant-evidence-survival-timing-infected-loading-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 즉시 vs 지연 생존 갈등은 해소: Mello 2017(관찰포함 30편 ~3%p 열세)은 **García-Sánchez 2022에 의해 완전 superseded**(2026-08) — RCT만 보면 생존 무차이이고 설계 편향이 원인. 동일한 트레이드오프(골·PES 우세, 실패율 비유의 증가)가 **하나의 210명 3군 RCT 내부**(Felice 2016/Esposito 2017)에서도 재현 — 즉시·즉시지연이 골·PES는 유의 우위이나 실패율은 비유의하게 더 높은 경향(4개월→1년 안정). 부위·직경이 방향을 뒤집기도 함 — Checchi 2017(구치·광경직경)은 지연군이 PES·변연골 모두 우위(전치부 Puisys 2022와 정반대).
  - ▸ 출발(`immediate-implant-evidence-survival-timing-infected-loading-overview`) 세줄: 즉시식립(Type 1)의 5개 결정축(생존·타이밍·감염소켓·부하/보철·환자체감)을 19편으로 종합한 허브: 생존율의 새 기준은 Gallucci 2026(PROSPERO 갱신 SR, 140편·10,456임플란트) — 9조합 가중생존율에서 Type 1A(즉시+즉시부하) 98.0%(검증됨) 대비 **Type 1B(즉시+조기부하) 91.6%(미검증)**로 손실률 약 4배 차이. 즉시 vs 지연 생존 갈등은 해소: Mello 2017(관찰포함 30편 ~3%p 열세)은 **García-Sánchez 2022

- `antibiotics-comprehensive-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: [확인] Torof 2023 SR+MA: 단일 술전 Amoxicillin 2g이 조기 실패 유의 감소(Momand과 상충 → 방법론 차이).
  - ▸ 출발(`antibiotics-comprehensive-overview`) 세줄: 근관치료·치주치료·구강외과·임플란트를 아우르는 21편 종합: 항생제는 전신 증상 동반 감염에만 적응, 염증성 치수염(SIP)에는 금지 (Lockhart 2019 ADA CPG, Tampi 2019 SR+MA). 치주치료 보조 전신 항생제는 CAL 0.3-0.4mm 개선이나 근거 질 "약함" (Botelho 2025 우산형 고찰); 술전 단일 Amoxicillin 2g이 구강외과 표준, 24시간 초과 연장은 AMR만 증가. 약물 선택: Amoxicillin 1차(치명 0.1/million), Cli

- `mandibular-third-molar-management-overview` [overviews] (HIGH-far→canellas-2020-intrasocket-ao-third-molar-sr-nma, '상충' · 상충)
  - **근거 문장**: - [[oral-surgery/third-molar/canellas-2020-intrasocket-ao-third-molar-sr-nma]] — SR+NMA (37 RCTs): 발치와 내 소독재와 치조골염(Alveolar Osteitis, AO) 예방 — 혈소판 풍부 피브린(Platelet-Rich Fibrin, PRF) OR 0.28, 0.2% CHX 젤 OR 0.52로 최상위; iodoform 거즈·SurgicelⓇ 劣; PRF+CHX 병용 효과 상충. 적응증: 고위험 발치(흡연·여성·고령·매복) 시 PRF 우선 고려. (sr+nma, 2020)
  - ▸ 출발(`mandibular-third-molar-management-overview`) 세줄: 하악 사랑니 관리 4편 종합: 매복은 측정 가능한 병리 부담(치관주위염 82.4%, M2M 원심 우식 18.8%, 치주병변 14.8%; Ye 2021, n=432)을 만들고 매복 형태가 병리 종류를 예측하며, 전문가 합의(Sun 2026)가 3단계 적응증(확정적 병리·치료적·예방적)을 제시한다. 치관주위염의 1차 치료는 국소 세척·NSAIDs이며 항생제는 감염 확산·전신 증상 시에만 한정해야 하나 실제로 치과의사 약 75%가 처방(Schmidt 2021 SR); 발치 후 morbidity는 CGF

- `unopposed-tooth-overeruption-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - 흔한 오판: "엔도한 치아라 더/덜 정출한다"(근거 없음·기전상 무관), "크라운 씌우면 정출 안 한다"(전체 치아가 이동), "대합치 없으면 무조건 빨리 보철"(저위험치는 과한 개입), "정출은 수직만"(경사·회전 동반), "인접 치아가 공간 채우면 정출 해결"(Smith 1996 반박).
  - ▸ 출발(`unopposed-tooth-overeruption-overview`) 세줄: 16편 종합: 대합치 없는 후방 치아의 ~83%가 정출(단기 ~9개월 평균 0.43 mm / 최대 0.75 mm; CBCT 5년 기준 근심교두 1.37 mm [Hong 2023]; ~72%는 1 mm 미만; 초기 최대 속도; 수직+협측경사+회전 3D); ~18%는 전혀 안 움직임; 정출은 PDL·치조골 매개라 치수 생활력 무관. 고정 retention도 부분접촉 대비 효과 없어(Livas 2016); 5년 후 인접 하악 제2대구치 근심 경사 (Mesial Tipping) 57.47°·협측 CEJ 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Synthesis of 17 papers on noncarious cervical lesions (NCCL) — etiology, diagnosis, and monitor-vs-restore decision: NCCLs are multifactorial (stress/abfraction + friction/abrasion + biocorrosion/erosion as a case-specific combination), the "abfraction as sole cause" hypothesis is clinically unproven with SR evidence directly contradicting across three systematic reviews (Senna 2012 — association 
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 17편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 17편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 불가).
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 17편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `miroshnychenko-2023-analgesics-acute-dental-pain` [drug/analgesics] (SOFT→di-spirito-2022-endodontic-pain-management-overview, 'unlike' · 다름)
  - **근거 문장**: - [[wiki/drug/analgesics/di-spirito-2022-endodontic-pain-management-overview]] — endodontic pain pharmacologic management overview; complementary adult context where pulpitis pain IS covered, unlike this pediatric review's extraction-only evidence.
  - ▸ 출발(`miroshnychenko-2023-analgesics-acute-dental-pain`) 세줄: - 소아(≤ 12세) 발치 후 급성 치통의 경구 진통제에 관한 체계적 문헌고찰 및 메타분석 (Systematic Review and Meta-Analysis, SRMA): 무작위대조시험 (Randomized Controlled Trial, RCT) 6편(연구당 45–201명, 평균 연령 5.5–9.3세), 2022년 ADA(미국치과협회) 소아 급성 치통 임상지침의 근거. - 이부프로펜과 아세트아미노펜은 위약보다 낫지만 서로 간 차이는 사소했고, 이부프로펜(5 mg/kg)+아세트아미노펜(15 mg/
  - ▸ 대상(`di-spirito-2022-endodontic-pain-management-overview`) 세줄: 체계적 고찰 개요(Healthcare 2022)와 기술적 요인 서술 고찰 통합: 근관 술후통증(환자의 2.5–60%, 6–12시간 최고조) 약물·비약물 관리 포괄. NSAIDs(ibuprofen ± APAP) 1차 약물치료; 코르티코스테로이드(dexamethasone)는 NSAID 보조제로 추가 이득; 술전 예방투여가 술후 반응투여보다 우월. 기구의 근첨 외 이탈·세정액 농도/용량·단일 vs 다회 방문 등 기술적 요인도 통증에 영향; 진통 목적 항생제 사용은 근거 없음.

- `einafshar-2024-importance-precision-cortical-bone-drilling` [implants/osteotomy-thermal] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Resolved contradictory literature on spindle speed: higher speed consistently raises MT while reducing MTF in this validated model framework.
  - ▸ 출발(`einafshar-2024-importance-precision-cortical-bone-drilling`) 세줄: 소 피질골 시편 + DEFORM-3D V6.02 3D 유한요소해석 (Finite Element Analysis, FEA) 통합 연구: 드릴 초기온도 (Initial Temperature, IT)·직경·끝각 (Point Angle)·스핀들 속도 (225–2700 rpm)·이송속도 (0.5–3 mm/s) 4개 변수가 최대 온도 (Maximum Temperature, MT)·최대 추력 (Maximum Thrust Force, MTF)에 미치는 영향 예측. IT 25 → 5°C 강하 시 MT −26.14

- `ceddia-2025-finite-element-analysis-of-implant` [implants/isq] (HIGH-no-target, 'counter to' · 반대)
  - **근거 문장**: - Demonstrates that ISQ increases slightly with inclination under horizontal load — counter to intuitive concern about instability
  - ▸ 출발(`ceddia-2025-finite-element-analysis-of-implant`) 세줄: Cyroth 임플란트(4 mm×15 mm)를 D2·D3 폴리우레탄 블록에 0°·15°·20° 경사 식립 후, 유한요소분석(FEA) 미세운동→ISQ 방정식 결과를 Osstell RFA 실측치와 비교한 in vitro 연구. FEA ISQ 오차 D3 1.27%, D2 2.86%; 경사 증가 시 ISQ 소폭 상승(D2 60.96→61.10); 피질골 응력 55.4→68.4 MPa(20°), 피크 임플란트 응력 220.2 MPa — 소성변형 한계(130 MPa) 미만. FEA로 다양한 경사 조건 ISQ 

- `naughton-2023-safemount-osstell-transducer-torque-isq` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Demonstrated hand tightening yields significantly lower ISQ than 6 Ncm calibrated torque (p<.001), contradicting Kästel 2019
  - ▸ 출발(`naughton-2023-safemount-osstell-transducer-torque-isq`) 세줄: 체외 폴리우레탄 뼈 블록 연구 (임플란트 7종, 56개, D1–D4 골질): 스마트팩 조임 방법 4종 비교 — 수동, 플라스틱 마운트, SafeMount, 정확한 토크 렌치 6 Ncm. 수동 조임이 정확한 토크 렌치 대비 유의하게 낮은 임플란트 안정성 지수 (Implant Stability Quotient, ISQ) 산출 (계수 −2.05, p<.001); SafeMount와 표준 플라스틱 마운트는 대조군과 유의차 없음. 골밀도가 ISQ 변이의 36%를 차지해 가장 큰 영향 인자였고, 술자는 6%

- `namuangchan-2023-iodine-mouthwash-oral-mucositis-ccrt-rct` [oral-medicine/mucositis] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: The study failed to demonstrate statistically significant superiority of IS mouthwash over NSS for preventing CCRT-induced OM, likely due to small sample size and possibly insufficient iodine concentration. Larger-scale studies are warranted to confirm or refute any potential benefit.
  - ▸ 출발(`namuangchan-2023-iodine-mouthwash-oral-mucositis-ccrt-rct`) 세줄: 본 연구는 태국 콘켄 대학에서 2019년 1월부터 12월까지 수행된, 단일기관, 전향적, 이중맹검, 무작위대조 임상시험으로, 동시항암방사선치료(CCRT)를 받는 두경부암 환자 20명(1:1 배정)을 대상으로 자체 제조한 요오드 용액(IS) 가글의 구강점막염(OM) 예방 효과를 정상 생리식염수(NSS)와 비교 평가하였다. 1차 평가변수는 주간 구강점막염 평가 척도(OMAS) 점수로, CCRT 시작 전부터 치료 종료 4주 후까지 측정되었다. IS군과 NSS군 간 주간 평균 OMAS 점수(전체 평균 차

- `ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency` [endodontics/shaping] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나, 개별 연구 간 증거는 여전히 상충된다.
  - ▸ 출발(`ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency`) 세줄: 종합 리뷰(Comprehensive Review, 비체계적) — 근단 개통성(Apical Patency)의 임상적 의의, 술후 통증(Postoperative Pain)과의 상관관계, 해부학적 고려사항, 협상(Negotiation) 기구·모터 키네마틱스(Motor Kinematics)를 기존 메타분석·임상연구 근거로 종합 검토. 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나(Apical Patency가 통증 악화가 아닌 감소), 개별 연구 간 증거는 여전히 상충 — 사전 CB

- `ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency` [endodontics/shaping] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나(Apical Patency가 통증 악화가 아닌 감소), 개별 연구 간 증거는 여전히 상충 — 사전 CBCT는 MB2 근관 등 복잡 해부학 확인에 필수, 특수 NiTi 파일과 왕복형(Reciprocating) 모터 키네마틱스가 활주로(Glide Path) 형성 예측가능성을 높인다.
  - ▸ 출발(`ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency`) 세줄: 종합 리뷰(Comprehensive Review, 비체계적) — 근단 개통성(Apical Patency)의 임상적 의의, 술후 통증(Postoperative Pain)과의 상관관계, 해부학적 고려사항, 협상(Negotiation) 기구·모터 키네마틱스(Motor Kinematics)를 기존 메타분석·임상연구 근거로 종합 검토. 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나(Apical Patency가 통증 악화가 아닌 감소), 개별 연구 간 증거는 여전히 상충 — 사전 CB

- `ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency` [endodontics/shaping] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Regarding the contentious relationship between patency and postoperative pain, the review notes that recent meta-analyses suggest patency may actually alleviate discomfort intensity — a finding that contradicts longstanding clinical anxiety about patency maneuvers causing flare-ups. However, the evidence across individual studies remains conflicting, and the authors call for further RCTs with stan
  - ▸ 출발(`ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency`) 세줄: 종합 리뷰(Comprehensive Review, 비체계적) — 근단 개통성(Apical Patency)의 임상적 의의, 술후 통증(Postoperative Pain)과의 상관관계, 해부학적 고려사항, 협상(Negotiation) 기구·모터 키네마틱스(Motor Kinematics)를 기존 메타분석·임상연구 근거로 종합 검토. 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나(Apical Patency가 통증 악화가 아닌 감소), 개별 연구 간 증거는 여전히 상충 — 사전 CB

- `ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency` [endodontics/shaping] (HIGH-no-target, 'conflicting evidence' · 상충 결과)
  - **근거 문장**: 3. **Pain–patency relationship**: Synthesizes conflicting evidence from recent meta-analyses, showing the relationship is more nuanced than the traditional fear that patency increases postoperative pain.
  - ▸ 출발(`ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency`) 세줄: 종합 리뷰(Comprehensive Review, 비체계적) — 근단 개통성(Apical Patency)의 임상적 의의, 술후 통증(Postoperative Pain)과의 상관관계, 해부학적 고려사항, 협상(Negotiation) 기구·모터 키네마틱스(Motor Kinematics)를 기존 메타분석·임상연구 근거로 종합 검토. 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나(Apical Patency가 통증 악화가 아닌 감소), 개별 연구 간 증거는 여전히 상충 — 사전 CB
