# 논쟁 레이더 백필 후보 — 2026-08-05

명시적 충돌 표현이 있으나 그 쌍에 `relations:` 타입 엣지가 (어떤 타입이든) 없는 후보. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**

**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. 아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), (2) **양쪽 페이지의 `## 세줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. 충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. (reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것 — 2026-07-17 전수 검토에서 contradicts 계열로 지목된 122건 중 실제 contradicts는 1건이었다.)

**대상은 키워드에 가장 가까운 링크로 특정한다.** 같은 줄의 나머지 링크는 충돌 표현의 대상이라는 근거가 없어 Tier 2(`AMBIG→`)로 강등된다 — 버리지 않으니 진짜 대상이 강등됐다면 Tier 2에서 찾을 수 있다.

- Tier 1 (대상 지목됨, actionable): **4**
- Tier 2 (대상 불명/soft, review): **54**
- (억제됨) 이미 typed 엣지가 있어 제외: **240** · 부정문 제외: **92** · 검토·불필요 대장: **393** · 동일 줄 비최근접으로 Tier 2 강등: **5**

## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)

### drug/analgesics

- `maurice-szamburski-2025-intravenous-nsaids-perioperative-pain-narrative-review`  —[counterpoint · 반대 논점]→  **`magesty-2026-adverse-events-oral-analgesics-third-molar-nma`**
  - **근거 문장**: - [[drug/analgesics/magesty-2026-adverse-events-oral-analgesics-third-molar-nma]] — NSAID adverse-event ranking in dental extraction; useful counterpoint to this review's IV-route safety data (13.7% vs 14.5% AE for ibuprofen vs paracetamol).
  - ▸ 출발(`maurice-szamburski-2025-intravenous-nsaids-perioperative-pain-narrative-review`) 세줄: 본 내러티브 리뷰는 성인과 소아에서 수술 전후 통증 관리에 사용되는 정맥 내 비스테로이드성 소염진통제(IV NSAIDs)에 관한 최근 10년간(2024년 5월까지)의 문헌을 종합하였으며, ibuprofen, ketorolac, ketoprofen, naproxen, paracetamol, acetylsalicylic acid를 중심으로 유럽의 승인 현황과 임상 관행을 검토하였다. IV NSAIDs는 수술 후 아편유사제(opioid) 사용을 약 20–60% 감소시키며, IV ibuprofen은 아편
  - ▸ 대상(`magesty-2026-adverse-events-oral-analgesics-third-molar-nma`) 세줄: 28개 RCT(5,306명, 하악 제3대구치 발치) 네트워크 메타분석 — 7개 진통제 약물군+위약의 이상반응을 비교한 SUCRA 분석. NSAID 단독군이 SUCRA 안전성 최하위(86.5%)였고 위약이 2위(81.7%)였으며, NSAID+비마약성+마약성 3제 병용군이 최상위(15.5%)로 가장 안전했다. 근거 확실성이 매우 낮음~낮음이고 위약군 이상반응도 높아 NSAID의 겉보기 위험은 실제 약물 독성이 아닌 노세보 효과로 해석되며, NSAIDs는 계속 1차 선택약으로 유지되어야 한다.

- `ibikunle-2016-prednisolone-qol-third-molar-rct`  —[contradict · 반박·충돌]→  **`larsen-2021-methylprednisolone-doses-split-mouth-rct`**
  - **근거 문장**: - [[drug/analgesics/larsen-2021-methylprednisolone-doses-split-mouth-rct]] — OHIP-14 null result for methylprednisolone (contradicts; different drug)
  - ▸ 출발(`ibikunle-2016-prednisolone-qol-third-molar-rct`) 세줄: 줄1: 나이지리아 3차 병원의 3군 무작위대조시험 (Randomized Controlled Trial, RCT) (n=186, 군당 62명)에서 경구 프레드니솔론 (Prednisolone) 40 mg, 점막하 주사 (Submucosal Injection) 40 mg, 무투여 대조군을 비교하여 구강건강관련 삶의 질 (Oral Health-Related Quality of Life, OHRQoL, OHIP-14)을 주요 결과 지표로 평가했다. 줄2: 프레드니솔론 투여군(경구·점막하 모두)은 미투여 대
  - ▸ 대상(`larsen-2021-methylprednisolone-doses-split-mouth-rct`) 세줄: 줄1: 덴마크 알보르 대학병원의 이중맹검 분할구강 (Split-mouth) 무작위대조시험 (Randomized Controlled Trial, RCT) (n=52)에서 양측 하악 사랑니 발치 중 교근 (Masseter) 내 메틸프레드니솔론 (Methylprednisolone) 20/30/40 mg 또는 위약을 주사하고 1·3·7·30일 추적했다. 줄2: 어느 용량에서도 위약 대비 통증(시각통증척도, Visual Analog Scale, VAS)·개구제한 (Trismus)·삶의 질 (OHIP-14)


### immediate-implant

- `puisys-2022-immediate-implant-placement-vs-early`  —[Contradict · 반박·충돌]→  **`checchi-2017-wide-diameter-immediate-post-extractive`**
  - **근거 문장**: - [[immediate-implant/checchi-2017-wide-diameter-immediate-post-extractive]] — **Contradicts** on esthetic-outcome direction: this trial found comparable-to-slightly-better PES for immediate placement (anterior single-tooth, standard diameter); Checchi found significantly worse PES for immediate placement (molar sites, 6.0–8.0mm wide-diameter implants vs. delayed conventional-diameter with ridge p
  - ▸ 출발(`puisys-2022-immediate-implant-placement-vs-early`) 세줄: 무작위 대조 시험 (Randomized Controlled Trial, RCT), n=50명 (즉시 식립 25명, 조기 식립 25명), 1년 추적 — 상악 전치부 심미 부위에서 즉시 식립(즉시 임시치관, 치조제 보존)과 조기 식립(골유도재생, Guided Bone Regeneration, GBR·지연 부하)을 비교, 골벽·치간골 정상 케이스로 한정. 두 군 모두 임플란트 실패 없음(생존율 100%); 1년 후 핑크 심미 지수 (Pink Esthetic Score, PES) 유사 — 즉시군 12.8
  - ▸ 대상(`checchi-2017-wide-diameter-immediate-post-extractive`) 세줄: 무작위대조시험 (Randomized Controlled Trial, RCT)(n=100, 대구치 발치부위, 단일기관) — 즉시 6.0–8.0mm 광경직경 임플란트 식립 vs 4개월 치조제보존(Ridge Preservation, 돈유래골이식+콜라겐차단막) 후 지연 4.0–5.0mm 통상직경 식립 비교, 부하 후 1년 추적. 임플란트 실패 5/47(10.6%) 즉시 vs 2/44(4.6%) 지연(무의미, P=.436); 핑크심미지수 (Pink Esthetic Score, PES)는 4개월(9.65 v


### oral-medicine/salivary-chemosensory

- `nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`  —[뒤집 · 뒤집음]→  **`tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva`**
  - **근거 문장**: 기존 위키에는 침(saliva)이 질병의 *결과물*(COVID 후유증)로만 나타난다 — [[oral-medicine/salivary-chemosensory/tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva]]. 이 JADA 리뷰는 침을 *진단 매체*로 뒤집는 관점(salivaomics·exosomics·liquid biopsy)을 도입해, 침샘 기능/구강건조 라인([[oral-medicine/salivary-chemosensory/poudel-2026-xerostomia-dental-treatment-outcomes-sr]])과 대비되는 "침의 진단적 활용" 축을 새로 연다. Wong 그룹(UCLA)의 salivaomics 프레임워크 원전으로, 향후 침 바이오마
  - ▸ 출발(`nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`) 세줄: 전문가 서술 리뷰(JADA 2023, Wong/UCLA 그룹) — 침 진단(saliva diagnostics)을 살리바오믹스(salivaomics)·침 엑소좀학(saliva exosomics)·침 액체생검(saliva liquid biopsy) 세 축으로 분류, 침·혈장 단백질체 20–30% 중첩으로 전신 바이오마커의 침샘 이송 가능성 지지. 전기화학 센서 EFIRM(Electric Field–Induced Release and Measurement)은 추출·증폭 없이 40–50 µL 침에서 폐암
  - ▸ 대상(`tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva`) 세줄: 내러티브 리뷰(약 90편 이상 연구, 코로나19 환자·완치자 총 6만5천여 명 종합) — 미각장애(ageusia/dysgeusia)와 침분비저하(xerostomia/hyposalivation) 등 구강 후유증의 지속 기간·유병률 종합. 미각장애는 완치 후 3주~12개월 추적에서 1~45%, 침분비저하는 2~40%에서 지속되고 서로 상관관계가 있으며; 지리적 구배(동아시아 3.8% vs 중동 20.6%)가 미각장애에서 뚜렷함. 타액선·미뢰의 ACE2/TRPV1 수용체 발현과 감염 유발 아연결핍이라는


## Tier 2 — 대상 식별 필요 / soft signal (review only)

- `beier-2012-porcelain-veneers-nonvital-bruxism-20year` [veneers] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This study contradicts more recent data (Gresnigt 2019, Etienne 2025) in the ETT finding — the likely explanation is the use of older feldspathic/silicate materials and pre-IDS adhesive protocols from the 1987–2009 era; bruxism remains the strongest identifiable patient risk factor regardless of era.
  - ▸ 출발(`beier-2012-porcelain-veneers-nonvital-bruxism-20year`) 세줄: 후향적 연구 (84명, 318개 장석계 PLV, Innsbruck, 1987–2009, 최장 20년): 5/10/20년 생존율 94.4%/93.5%/82.93%; 주요 실패 원인 세라믹 파절(44.83%). 비생활치(ETT) 실패 위험 유의 증가(p=0.0012); 이갈이(Bruxism) 7.7배 위험(p=0.0004); 흡연자 변연 변색 유의 증가. ETT 소견은 최신 연구(Gresnigt 2019·Etienne 2025)와 상충 — 1987–2009년 구세대 장석계 소재 및 pre-IDS 접착

- `beier-2012-porcelain-veneers-nonvital-bruxism-20year` [veneers] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: ETT 소견은 최신 연구(Gresnigt 2019·Etienne 2025)와 상충 — 1987–2009년 구세대 장석계 소재 및 pre-IDS 접착 프로토콜이 차이의 설명 요인으로 추정; 이갈이는 시대와 무관한 가장 강한 환자 측 위험 인자.
  - ▸ 출발(`beier-2012-porcelain-veneers-nonvital-bruxism-20year`) 세줄: 후향적 연구 (84명, 318개 장석계 PLV, Innsbruck, 1987–2009, 최장 20년): 5/10/20년 생존율 94.4%/93.5%/82.93%; 주요 실패 원인 세라믹 파절(44.83%). 비생활치(ETT) 실패 위험 유의 증가(p=0.0012); 이갈이(Bruxism) 7.7배 위험(p=0.0004); 흡연자 변연 변색 유의 증가. ETT 소견은 최신 연구(Gresnigt 2019·Etienne 2025)와 상충 — 1987–2009년 구세대 장석계 소재 및 pre-IDS 접착

- `selvaraj-2023-fracture-resistance-of-endodontically` [post-and-core] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: FRC(EverX Posterior, Ribbond, Vectris)는 16편 중 15편에서 재래식 하이브리드/나노하이브리드 복합레진 대비 파절저항 우위(강한 근거); 벌크필 (Bulk-fill Composite) 대비 제한적·상충 근거, 파이버 포스트 (Fiber Post)·인레이 (Inlay) 대비 중간 수준 근거, 엔도크라운 (Endocrown) 비교 근거 없음.
  - ▸ 출발(`selvaraj-2023-fracture-resistance-of-endodontically`) 세줄: PRISMA·PROSPERO(CRD42021295212) 기반 체계적 문헌고찰(SR): 근관치료된 구치부 치아의 파절저항에 대해 섬유강화복합레진 (Fiber-Reinforced Composite, FRC) vs 다양한 비교대상 18편 인비트로 연구 종합; 높은 이질성으로 메타분석 불가. FRC(EverX Posterior, Ribbond, Vectris)는 16편 중 15편에서 재래식 하이브리드/나노하이브리드 복합레진 대비 파절저항 우위(강한 근거); 벌크필 (Bulk-fill Composite)

- `carvalho-2020-endodontically-treated-teeth-restoration-adhesive-approach` [post-and-core] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Clinical evidence remains contradictory: in vitro studies favor postless approaches with bonded ceramic crowns to reduce catastrophic failures, but RCTs using PFM crowns show higher success with posts (84% cast vs 95% fiber post over 4 years), highlighting that restoration type (cemented vs bonded) critically influences outcomes and more clinical studies on modern adhesive postless techniques are 
  - ▸ 출발(`carvalho-2020-endodontically-treated-teeth-restoration-adhesive-approach`) 세줄: 본 종설은 근관치료된 치아 (Endodontically Treated Teeth, ETT)의 접착 수복에 관한 현재 지식을 조사하였으며, 부분 피개 대 완전 피개, 페룰 효과, 포스트 종류가 치명적 파절에 미치는 영향, 엔도크라운 및 포스트 없는 코어 축성 (postless build-up)과 같은 무포스트 대안을 검토하였다. 잔존 치아 구조의 보존이 가장 중요하며, 1.5-2 mm 페룰의 존재는 파절 저항성을 향상시키고, 부분 수복물은 완전관과 유사한 생존율을 보였으며 (94-100% 대 91.

- `carvalho-2020-endodontically-treated-teeth-restoration-adhesive-approach` [post-and-core] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: 임상 근거는 여전히 상반된데, 시험관 연구는 접착성 세라믹 크라운과 무포스트 접근법이 치명적 파절을 감소시킨다고 보는 반면, PFM 크라운을 사용한 RCT는 포스트 식립이 더 높은 성공률을 보였으며 (4년간 주조포스트 84% 대 섬유포스트 95%), 이는 수복물 유형 (시멘트형 대 접착형)이 결과에 결정적 영향을 미침을 강조하며, 현대 접착 무포스트 기법에 관한 추가 임상 연구가 필요함을 시사한다.
  - ▸ 출발(`carvalho-2020-endodontically-treated-teeth-restoration-adhesive-approach`) 세줄: 본 종설은 근관치료된 치아 (Endodontically Treated Teeth, ETT)의 접착 수복에 관한 현재 지식을 조사하였으며, 부분 피개 대 완전 피개, 페룰 효과, 포스트 종류가 치명적 파절에 미치는 영향, 엔도크라운 및 포스트 없는 코어 축성 (postless build-up)과 같은 무포스트 대안을 검토하였다. 잔존 치아 구조의 보존이 가장 중요하며, 1.5-2 mm 페룰의 존재는 파절 저항성을 향상시키고, 부분 수복물은 완전관과 유사한 생존율을 보였으며 (94-100% 대 91.

- `carvalho-2020-endodontically-treated-teeth-restoration-adhesive-approach` [post-and-core] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This critical review examines current adhesive approaches for restoring endodontically treated teeth (ETT), focusing on the tension between traditional post-and-core methods and emerging postless alternatives. The authors synthesize evidence from in vitro studies, clinical trials, systematic reviews, and meta-analyses to evaluate partial versus full coverage, the ferrule effect, post type influenc
  - ▸ 출발(`carvalho-2020-endodontically-treated-teeth-restoration-adhesive-approach`) 세줄: 본 종설은 근관치료된 치아 (Endodontically Treated Teeth, ETT)의 접착 수복에 관한 현재 지식을 조사하였으며, 부분 피개 대 완전 피개, 페룰 효과, 포스트 종류가 치명적 파절에 미치는 영향, 엔도크라운 및 포스트 없는 코어 축성 (postless build-up)과 같은 무포스트 대안을 검토하였다. 잔존 치아 구조의 보존이 가장 중요하며, 1.5-2 mm 페룰의 존재는 파절 저항성을 향상시키고, 부분 수복물은 완전관과 유사한 생존율을 보였으며 (94-100% 대 91.

- `acog-2013-oral-health-care-during-pregnancy` [oral-medicine] (HIGH-no-target, 'conflicting evidence' · 상충 결과)
  - **근거 문장**: - Periodontal disease + preeclampsia: conflicting evidence
  - ▸ 출발(`acog-2013-oral-health-care-during-pregnancy`) 세줄: 줄1: ACOG Committee Opinion No. 569 (2013), 미국산부인과학회(ACOG)·미국치과의사협회(ADA)·HRSA 다학제 합의문; 발표 당시 미국 임산부 56%가 임신 중 치과 미방문(2007–2009). 줄2: 치과방사선촬영·국소마취(Local Anesthesia)·대부분의 치과 약물이 전 임신 기간 안전; 임신 중 치주 치료(Periodontal Treatment)는 조산(Preterm Birth)·저체중아 감소 효과 없음(다수 메타분석); 감염성 심내막염 예방적 항생제

- `gotfredsen-2021-patient-perception-timing-concepts-implant` [immediate-implant] (HIGH-far→pommer-2021-maxillary-single-tooth-timing-protocols-sr-ma, 'overturn' · 결론 뒤집음)
  - **근거 문장**: - [[immediate-implant/pommer-2021-maxillary-single-tooth-timing-protocols-sr-ma]] — same-issue companion (Clinical Oral Implants Research 2021;32(Suppl 21), ITI Consensus Conference). Pommer's SR+MA cross-tabulates placement×loading timing against clinician-measured long-term (≥3y) survival and marginal bone remodeling in maxillary single-tooth implants, finding no significant differences across a
  - ▸ 출발(`gotfredsen-2021-patient-perception-timing-concepts-implant`) 세줄: 즉시·조기·종래 임플란트 식립 및 부하 타이밍에 대한 환자 인식(환자보고결과 Patient-Reported Outcome Measure, PROM: 불편감, 만족도, 심미도)을 평가한 35~40건의 무작위/전향적 시험의 체계적 문헌고찰(Systematic Review, SR). 식립 또는 부하 타이밍 단독으로는 환자의 불편감, 기능/심미 만족도, 전체 임플란트 치료 만족도에 강한 근거가 없음; 무치악 완전틀니(Full-Arch Edentulous) 환자군에서만 즉시부하(Immediate Loadi

- `puisys-2022-immediate-implant-placement-vs-early` [immediate-implant] (HIGH-far→asghar-2023-immediate-vs-early-implant-esthetic-zone-sr-ma, 'counter to' · 반대)
  - **근거 문장**: - [[immediate-implant/esthetic-soft-tissue/asghar-2023-immediate-vs-early-implant-esthetic-zone-sr-ma]] — SR+MA of 6 RCTs on this identical immediate-vs-early axis in the esthetic zone; the pooled analysis found a significant PES advantage for early placement (P<0.05), while this individual RCT found no PES difference (12.8 vs 12.5, p=.362) — a primary-study data point running counter to, not conf
  - ▸ 출발(`puisys-2022-immediate-implant-placement-vs-early`) 세줄: 무작위 대조 시험 (Randomized Controlled Trial, RCT), n=50명 (즉시 식립 25명, 조기 식립 25명), 1년 추적 — 상악 전치부 심미 부위에서 즉시 식립(즉시 임시치관, 치조제 보존)과 조기 식립(골유도재생, Guided Bone Regeneration, GBR·지연 부하)을 비교, 골벽·치간골 정상 케이스로 한정. 두 군 모두 임플란트 실패 없음(생존율 100%); 1년 후 핑크 심미 지수 (Pink Esthetic Score, PES) 유사 — 즉시군 12.8

- `checchi-2017-wide-diameter-immediate-post-extractive` [immediate-implant] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 저자 결론: 대구치 소켓의 광경직경 즉시임플란트는 치조제보존+지연 통상직경 식립 대비 심미 결과가 열등 — 전치 심미부 타이밍 시험 일부와 반대 방향의 효율-심미 트레이드오프이며, 즉시식립 문헌 전반에 대한 일반 반박이라기보다 특정 임상 시나리오(구치부·광경직경 선택)의 소견으로 해석해야 함.
  - ▸ 출발(`checchi-2017-wide-diameter-immediate-post-extractive`) 세줄: 무작위대조시험 (Randomized Controlled Trial, RCT)(n=100, 대구치 발치부위, 단일기관) — 즉시 6.0–8.0mm 광경직경 임플란트 식립 vs 4개월 치조제보존(Ridge Preservation, 돈유래골이식+콜라겐차단막) 후 지연 4.0–5.0mm 통상직경 식립 비교, 부하 후 1년 추적. 임플란트 실패 5/47(10.6%) 즉시 vs 2/44(4.6%) 지연(무의미, P=.436); 핑크심미지수 (Pink Esthetic Score, PES)는 4개월(9.65 v

- `abutment-screw-preload-joint-stability-overview` [overviews] (SOFT→varvara-2020-retightening-preload-loss-abutment-screws, 'challenges the' · 도전)
  - **근거 문장**: - [[prosthetic-materials/abutment-screw/varvara-2020-retightening-preload-loss-abutment-screws]] — retightening-interval study: 2 min minimized preload loss better than 5/10 min (challenges the 10-min standard); internal hex retains more preload than external hex at every interval.
  - ▸ 출발(`abutment-screw-preload-joint-stability-overview`) 세줄: 20편 종합: 나사 풀림(5년 ~10.4%, 10년 ~20.8%)은 전하중 손실이 원인이며, 기전은 세틀링(무하중에서도 2–10%)과 동적 피로(제거토크 손실 16.1–39%) 둘 — 마찰·조도가 핵심 레버(가해진 토크 중 ~8–10%만 전하중化; 탄소코팅 나사 10회 재사용 시 전하중 329.9→253.7 N 감소, Sagheb 2023). 재조임이 세틀링 보상(최적 시점 논쟁: 10분 Nithyapriya 2018·Vinhas 2022 vs 2분 Varvara 2020; 2회째에 plateau
  - ▸ 대상(`varvara-2020-retightening-preload-loss-abutment-screws`) 세줄: 체외 연구(n=80; 내부 육각형(Internal Hexagon, IG) 40개·외부 육각형(External Hexagon, EG) 40개; 35 Ncm; 재조임 간격별 n=10: 대조군/2분/5분/10분; 30분 후 제거 토크 측정). 초기 조임 후 2분 재조임이 양쪽 연결부에서 예압(preload) 소실을 가장 효과적으로 최소화(p<0.05 vs 대조군); 내부 육각형이 외부 육각형보다 예압 유지 우수; 기존 권장 10분 재조임은 그 사이 추가 안착(settling)이 발생하여 차선. 최적 재

- `sinus-lift-technique-selection` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: [확인] **루틴 차폐막 사용은 근거 부족.** 천공 봉합용·연조직 차단용으로 선택적 사용. **근거의 시간적 반전에 유의**: Wallace 2003의 메타회귀(43편, 대부분 후향적·증례군, RCT 3편뿐)는 막 피개가 생존율을 높인다고 봤으나, Starch-Jensen 2019가 이 변수 하나만 떼어 RCT 6편으로 다시 검증하자 유의차가 사라졌다 — 오래되고 이질적인 메타회귀 신호가 이후 좁고 엄밀한 RCT-only SR+MA에서 재현되지 않은 사례(relations: contradicts, 양쪽 페이지에 상호 typed edge 설정됨). **현재 근거는 후자(routine 사용 근거 없음)를 우선한다** — 표본 크기가 아니라 설계 엄밀성 차이(관찰연구 혼합 vs RCT-only)로 읽는다.
  - ▸ 출발(`sinus-lift-technique-selection`) 세줄: 22편+3편 종합(측방창 12+3, 경치조골 10) — 잔존골높이(RBH) 기반 알고리듬과 위험인자 매트릭스; 모든 술식 임플란트 생존율 97–99% 동등(Shah 2022 formal head-to-head SR+MA로 재확인: 직접 96.9% vs 간접 97.0%, 유의차 없음). 결정 임계값: RBH ≥5 mm → 경치조골거상(Transcrestal SFE, TSFE) 1순위(골밀도화(OD) 적용 시 4 mm까지 확장), <5 mm → 측방창(Lateral Sinus Approach, LSA

- `sinus-lift-technique-selection` [overviews] (HIGH-far→wallace-2003-effect-maxillary-sinus-augmentation-survival, '반박' · 반박)
  - **근거 문장**: - [[sinus-lift/lateral/wallace-2003-effect-maxillary-sinus-augmentation-survival]] — SR+MA (43편 메타회귀, abstract-only): lateral window 생존율 평균 91.8%(61.7–100%); 거친표면·입자형이식재·측창막피개 시 생존율↑ — 막피개 결론은 이후 Starch-Jensen 2019(RCT-only SR+MA)에서 반박됨(relations: contradicts). (sr+ma, 2003)
  - ▸ 출발(`sinus-lift-technique-selection`) 세줄: 22편+3편 종합(측방창 12+3, 경치조골 10) — 잔존골높이(RBH) 기반 알고리듬과 위험인자 매트릭스; 모든 술식 임플란트 생존율 97–99% 동등(Shah 2022 formal head-to-head SR+MA로 재확인: 직접 96.9% vs 간접 97.0%, 유의차 없음). 결정 임계값: RBH ≥5 mm → 경치조골거상(Transcrestal SFE, TSFE) 1순위(골밀도화(OD) 적용 시 4 mm까지 확장), <5 mm → 측방창(Lateral Sinus Approach, LSA

- `radiology-category-synthesis-overview` [overviews] (SOFT→hasan-2022-prevalence-nutrient-canals-mandibular, 'Unlike' · 다름)
  - **근거 문장**: Nutrient canals (NCs) are radiolucent neurovascular channels visible on mandibular anterior IOPARs. Unlike MC variants, they carry vessels to alveolar bone rather than the IAN. [[radiology/hasan-2022-prevalence-nutrient-canals-mandibular]] (cross-sectional, n=200, India) compared four groups:
  - ▸ 출발(`radiology-category-synthesis-overview`) 세줄: 방사선학 53편은 5개 주제군 — 선량 최적화, CBCT 진단 성능, 이미지 아티팩트, 해부학적 변이, 방사선 감별진단 — 으로 구성되며 각 주제군에 별도 overview가 있다; 이분하악관(Bifid Mandibular Canal, BMC) 유병률은 CT/CBCT 환자 20.7%(Aung 2023 SR+MA, 40편, n=17,714), 영양관(Nutrient Canal, NC)은 당뇨(84%)·고혈압(66%)·치주염(52%) 군에서 건강 대조군(20%) 대비 유의하게 증가(Hasan 2022)
  - ▸ 대상(`hasan-2022-prevalence-nutrient-canals-mandibular`) 세줄: 단면연구(cross-sectional, n=200/800명 스크리닝, 인도, 10개월) — 하악 전치부 치근단방사선사진(IOPAR)에서 영양관(Nutrient Canal, NC) 유병률을 건강대조군·당뇨병(Diabetes Mellitus, DM)·고혈압(Hypertension, HTN)·만성치주염(Chronic Periodontitis) 4개 군에서 비교. 질환군에서 NC 유병률이 대조군 대비 유의하게 높음(DM 84% vs 대조군 20%, p=0.000004; HTN 66%, p=0.000003

- `local-anesthesia-category-synthesis-overview` [overviews] (HIGH-far→subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric, 'contradict' · 반박·충돌)
  - **근거 문장**: [[local-anesthesia/subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric]] provides a contrasting result in a different comparison (lidocaine vs benzocaine in a different pediatric age group) — the two papers are tagged `contradicts` in the wiki; the most likely explanation is methodological heterogeneity rather than a true effect.
  - ▸ 출발(`local-anesthesia-category-synthesis-overview`) 세줄: 국소마취 37편은 ① 하악 마취 효율 ladder, ② 완충·변형 마취제, ③ IANB 실패 해부학, ④ CCLAD·무침주사, ⑤ 전처치·표면마취, ⑥ 안전·합병증 6군으로 정리; 표준 IANB는 증상성 비가역 치수염(SIP)에서 자주 실패 → 4% articaine 협측침윤(RR 1.06, Saatchi 2025 SR+MA), 이부프로펜 >400 mg 전처치(위약 ~20% → ~79%; Khademi 2023 umbrella), 보충주사(RR 2.02, Rujirawan 2025 Network 

- `autogenous-bone-graft-donor-site-selection-overview` [overviews] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: > - **장골능(ICG)은 "열등"이 아니라 "최후 수단"**: Sethi 2020(173명·190그래프트·869임플란트·최장 23년)는 95%±2.7% 장기 생존을 보고 — 대형 결손에서 구강내로 불충분할 때 여전히 유효한 옵션. 공여부 합병증도 혈청종(seroma)뿐, 보행장애·감각이상 보고 없음(McKenna 2022의 "합병증 흔함" 서술과 대비되는 저이환 코호트).
  - ▸ 출발(`autogenous-bone-graft-donor-site-selection-overview`) 세줄: 자가골이식 **공여부** 선택(재료 선택과는 다른 축) 7편 종합 — 구강내 공여부가 전 추적시점에서 장골능(구외)보다 임플란트 생존율 우수(24개월 98.2% vs 85.9%, p<0.001, McKenna 2022 SR+MA), 자가골 vs 동종골 블록은 전체적으로 동등(96.23% vs 97.66% NS, Donkiewicz 2021 SR). 장골능(ICG)은 구강내로 부족한 대형 결손의 최후수단으로 여전히 유효(Sethi 2020, 25년·869임플란트, 생존 95%±2.7%, 합병증은 혈

- `autogenous-bone-graft-donor-site-selection-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **공여부 이환율 서열**: 장골능(통증·보행장애·감각이상) > 하악 이부(하악전치 감각이상) > 후구치·상악결절(합병증 사실상 0). 이환율이 위계를 뒤집는 실제 임상 변수 — 생존율 차이보다 환자가 체감하는 부담 차이가 더 크다.
  - ▸ 출발(`autogenous-bone-graft-donor-site-selection-overview`) 세줄: 자가골이식 **공여부** 선택(재료 선택과는 다른 축) 7편 종합 — 구강내 공여부가 전 추적시점에서 장골능(구외)보다 임플란트 생존율 우수(24개월 98.2% vs 85.9%, p<0.001, McKenna 2022 SR+MA), 자가골 vs 동종골 블록은 전체적으로 동등(96.23% vs 97.66% NS, Donkiewicz 2021 SR). 장골능(ICG)은 구강내로 부족한 대형 결손의 최후수단으로 여전히 유효(Sethi 2020, 25년·869임플란트, 생존 95%±2.7%, 합병증은 혈

- `autogenous-bone-graft-donor-site-selection-overview` [overviews] (HIGH-no-target, 'in contrast to' · 대조)
  - **근거 문장**: **Sethi 2020** (retrospective, 173 patients, 190 ICG onlay grafts, 869 implants, up to 23-year follow-up, mean 109 months) supplies the long-term denominator for the ICG arm that McKenna's SR+MA pooled from shorter multi-study data: Kaplan-Meier survival 95%±2.7%, remaining above 92.3% out to 200 months. This is a **low-morbidity** ICG cohort — the only donor-site complication was seroma (11/173 p
  - ▸ 출발(`autogenous-bone-graft-donor-site-selection-overview`) 세줄: 자가골이식 **공여부** 선택(재료 선택과는 다른 축) 7편 종합 — 구강내 공여부가 전 추적시점에서 장골능(구외)보다 임플란트 생존율 우수(24개월 98.2% vs 85.9%, p<0.001, McKenna 2022 SR+MA), 자가골 vs 동종골 블록은 전체적으로 동등(96.23% vs 97.66% NS, Donkiewicz 2021 SR). 장골능(ICG)은 구강내로 부족한 대형 결손의 최후수단으로 여전히 유효(Sethi 2020, 25년·869임플란트, 생존 95%±2.7%, 합병증은 혈

- `immediate-implant-evidence-survival-timing-infected-loading-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **부위·직경이 방향을 뒤집을 수 있다**: Checchi 2017(구치부 RCT, n=100, 광경직경 6.0–8.0mm 즉시 vs 치조제보존+지연 통상직경)은 **지연군이 심미(PES 9.71 vs 10.86, P=.02)·변연골(1.06 vs 0.63mm, P<.0001) 모두 유의 우위** — 전치부 단일치 RCT(Puisys 2022: PES 12.8 vs 12.5 NS, 협측점막 즉시군 소폭 우세 P=.047)와 정반대 방향. 같은 "즉시식립" 문헌이라도 전치 표준직경과 구치 광경직경은 다른 결론.
  - ▸ 출발(`immediate-implant-evidence-survival-timing-infected-loading-overview`) 세줄: 즉시식립(Type 1)의 5개 결정축(생존·타이밍·감염소켓·부하/보철·환자체감)을 18편으로 종합한 허브: 생존율의 새 기준은 Gallucci 2026(PROSPERO 갱신 SR, 140편·10,456임플란트) — 9조합 가중생존율에서 Type 1A(즉시+즉시부하) 98.0%(검증됨) 대비 **Type 1B(즉시+조기부하) 91.6%(미검증)**로 손실률 약 4배 차이. 기존 즉시 vs 지연 생존 "갈등"(Mello 2017 관찰포함 30편 유의열세 vs García-Sánchez 2022 RCT

- `immediate-implant-evidence-survival-timing-infected-loading-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 기존 즉시 vs 지연 생존 "갈등"(Mello 2017 관찰포함 30편 유의열세 vs García-Sánchez 2022 RCT 6편 무차이)은 설계민감성 문제로 읽는 게 맞으며, 동일한 트레이드오프가 **하나의 210명 3군 RCT 내부**(Felice 2016/Esposito 2017)에서도 재현 — 즉시·즉시지연이 골·PES는 유의 우위이나 실패율은 비유의하게 더 높은 경향(4개월→1년 안정). 부위·직경이 방향을 뒤집기도 함 — Checchi 2017(구치·광경직경)은 지연군이 PES·변연골 모두 우위(전치부 Puisys 2022와 정반대).
  - ▸ 출발(`immediate-implant-evidence-survival-timing-infected-loading-overview`) 세줄: 즉시식립(Type 1)의 5개 결정축(생존·타이밍·감염소켓·부하/보철·환자체감)을 18편으로 종합한 허브: 생존율의 새 기준은 Gallucci 2026(PROSPERO 갱신 SR, 140편·10,456임플란트) — 9조합 가중생존율에서 Type 1A(즉시+즉시부하) 98.0%(검증됨) 대비 **Type 1B(즉시+조기부하) 91.6%(미검증)**로 손실률 약 4배 차이. 기존 즉시 vs 지연 생존 "갈등"(Mello 2017 관찰포함 30편 유의열세 vs García-Sánchez 2022 RCT

- `periodontal-adjunctive-therapy-probiotics-pdt-overview` [periodontics] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: **2026-07-23 update — the pooled tier now confirms the ceiling.** Two meta-analyses added since this page was written (Mendonça 2024, 33 RCTs; Benavides-Reyes 2025, 24 RCTs) agree that probiotics reduce bleeding and plaque and do not produce CAL gain, and disagree on probing depth in a way that tracks methodology rather than biology — the star-network NMA reports PPD MD 1.48 mm while the direct pa
  - ▸ 출발(`periodontal-adjunctive-therapy-probiotics-pdt-overview`) 세줄: 8편 종합(NMA 1·RCT 4·SR+MA 1·RCT 1) — 2017 NMA 벤치마크(John 2017, 61편, 9종 보조요법): 모든 보조요법의 추가 임상부착수준(Clinical Attachment Level, CAL) 이득 ~0.3 mm, 우월한 단일 보조요법 없음. 2026 프로바이오틱스 RCT(Lactobacillus+Enterococcus, n=80; OraCMU, n=80)는 탐침시출혈(Bleeding on Probing, BoP)·심부포켓 수를 유의 감소(p=0.03·p=0.01)

- `periodontal-adjunctive-therapy-probiotics-pdt-overview` [periodontics] (HIGH-far→jungbauer-2026-naocl-hyaluronic-acid-subgingival-reinstrumentation-rct, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[periodontics/non-surgical-instrumentation/jungbauer-2026-naocl-hyaluronic-acid-subgingival-reinstrumentation-rct]] — "clean and seal" (AA-NaOCl + cross-linked HA) adjunct to SRI in maintenance; positive ~0.5 mm PD / 0.57 mm CAL gain, doubled pocket closure — delivery-mode counterpoint to da Silveira's null irrigation
  - ▸ 출발(`periodontal-adjunctive-therapy-probiotics-pdt-overview`) 세줄: 8편 종합(NMA 1·RCT 4·SR+MA 1·RCT 1) — 2017 NMA 벤치마크(John 2017, 61편, 9종 보조요법): 모든 보조요법의 추가 임상부착수준(Clinical Attachment Level, CAL) 이득 ~0.3 mm, 우월한 단일 보조요법 없음. 2026 프로바이오틱스 RCT(Lactobacillus+Enterococcus, n=80; OraCMU, n=80)는 탐침시출혈(Bleeding on Probing, BoP)·심부포켓 수를 유의 감소(p=0.03·p=0.01)

- `suture-wound-closure-decision-ladder` [overviews] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: > - 고장력 — 술식 성능 순위(하악 4군 RCT n=40): 골증대 **CALF > DFI ≈ MPRI > PRI**(PRI 최저, 임상 2.60mm vs CALF 4.12mm, P<.001, Bahaa 2022). DFI 단독비교(Ogata 2013 RCT n=23)도 PRI보다 전진량↑(9.64 vs 7.13mm)·통증/부종↓. 단, ex-vivo(Raabe 2025)에서는 절개기법(MPRI vs MDT)이 아니라 **골막봉합(PS) 유무**가 이식재변위를 좌우(P<.001) — 기법보다 봉합이 이식재 안정성의 진짜 변수라는 상반된 층위의 결론.
  - ▸ 출발(`suture-wound-closure-decision-ladder`) 세줄: 23편 종합(RCT 10, SR 1, 전향적 2, case-report 2, in-vitro 5, 후향적 1, animal 1, narrative-review 1) — 봉합·창상폐쇄 결정은 단일 상류 변수인 창상 장력(wound tension)에 의해 정반대 최적화 목표를 가진 두 맥락으로 분기한다. 저장력 발치와: 봉합 유무는 결과에 무관 — 무봉합(sutureless)은 안전하며 초기 이환도 동등 이상(Takadoum 2022 완전 동등, Kumar/Sen trismus·부종 감소); 흡연자는

- `suture-wound-closure-decision-ladder` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **회색지대**: ogata(임상: 기법선택이 전진량·이환도에 유의 영향)와 raabe(ex-vivo: 기법선택이 이식재변위·전진량에 무영향)는 서로 다른 기법쌍·다른 outcome을 측정하므로 frontmatter상 공식 `contradicts` 관계는 아니지만 방향이 엇갈린다 — 폐쇄 morbidity·전진량엔 기법이 영향을 주지만(임상), 이식재 자체의 안정성은 골막봉합 여부가 결정한다(ex-vivo). [미검증 — 두 결론을 통합한 단일 연구는 없음]
  - ▸ 출발(`suture-wound-closure-decision-ladder`) 세줄: 23편 종합(RCT 10, SR 1, 전향적 2, case-report 2, in-vitro 5, 후향적 1, animal 1, narrative-review 1) — 봉합·창상폐쇄 결정은 단일 상류 변수인 창상 장력(wound tension)에 의해 정반대 최적화 목표를 가진 두 맥락으로 분기한다. 저장력 발치와: 봉합 유무는 결과에 무관 — 무봉합(sutureless)은 안전하며 초기 이환도 동등 이상(Takadoum 2022 완전 동등, Kumar/Sen trismus·부종 감소); 흡연자는

- `conservative-access-cavity-biomechanics-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Synthesis of nine papers (1 network meta-analysis, 2 pairwise meta-analyses, 3 systematic reviews, 3 controlled in vitro studies) resolving an apparent contradiction in conservative access cavity (CEC) biomechanics: pooled analyses report a significant fracture-resistance advantage for CEC over traditional endodontic cavities (TEC) — SUCRA 51.4% vs 15.3%, ~562 N difference (Motiwala 2022, 10 molar
  - ▸ 출발(`conservative-access-cavity-biomechanics-overview`) 세줄: 논문 9편(네트워크 메타분석 1·쌍대 메타분석 2·체계적 고찰 3·통제 체외연구 3) 종합 — 보존적 접근와동 (Conservative Endodontic Cavity, CEC) 생역학의 겉보기 모순을 해소: 풀링 분석은 CEC가 전통 접근와동 (Traditional Endodontic Cavity, TEC)보다 파절저항이 유의하게 높다고 보고하는 반면(Motiwala 2022 — 누적순위곡선하면적 (Surface Under the Cumulative Ranking, SUCRA) 51.4% vs 

- `conservative-access-cavity-biomechanics-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The contradiction resolves on three moderators that the pooled models did not stratify: (1) marginal ridge status — CEC and truss designs beat TEC only when all marginal ridges are intact, and the advantage vanishes once one or more ridges are lost (Ballester 2021, 33 studies), which is precisely the signature that Mrinalini's I²=92% heterogeneity would produce; (2) restoration state — all three n
  - ▸ 출발(`conservative-access-cavity-biomechanics-overview`) 세줄: 논문 9편(네트워크 메타분석 1·쌍대 메타분석 2·체계적 고찰 3·통제 체외연구 3) 종합 — 보존적 접근와동 (Conservative Endodontic Cavity, CEC) 생역학의 겉보기 모순을 해소: 풀링 분석은 CEC가 전통 접근와동 (Traditional Endodontic Cavity, TEC)보다 파절저항이 유의하게 높다고 보고하는 반면(Motiwala 2022 — 누적순위곡선하면적 (Surface Under the Cumulative Ranking, SUCRA) 51.4% vs 

- `recurrent-aphthous-stomatitis-overview` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: A subtle counterpoint to the PFAPA "shared loci" theme: Mumcu 2021 reports **site-specific taxa that distinguish BD ulcer sites from RAS ulcer sites** — so predisposition may overlap while the *local* disease expression is microbiologically distinct.
  - ▸ 출발(`recurrent-aphthous-stomatitis-overview`) 세줄: 성인 ~20%가 겪는 재발성 아프타성 구내염(RAS) 8편을 세 축(분류·병태생리 / 국소→비약물→전신 치료 사다리 / 특발성과 구분되는 증후군성 중첩(PFAPA·베체트))으로 종합 — 핵심 명제는 흔한 특발성 RAS의 국소 1차 치료는 그대로이며, 증후군 중첩이 바꾸는 것은 1차 치료가 아니라 감별·의뢰라는 것. 국소 코르티코스테로이드(트리암시놀론·클로베타솔)가 네 편의 리뷰에서 일치하는 1차 치료이나, 가장 체계적인 치료 종합(D'Amario 2025, 45 RCT)은 비약물(LLLT·오메가-

- `dbbm-bone-substitute-overview` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: **Same graft category, different healing dynamics (Sousa 2026, animal, 54 Wistar rats)**: this is the axis's cautionary counterpoint. Two commercially distinct collagen-containing bovine xenografts — Bio-Oss Collagen® (~90% HA/~10% collagen) and Extra Graft XG13® (~75% HA/~25% collagen) — were compared head-to-head in 5-mm rat calvarial critical-size defects at 7/14/28 days. Early inflammatory and
  - ▸ 출발(`dbbm-bone-substitute-overview`) 세줄: 17편(동물·in-vitro·전향·RCT·SR·SR+MA) 종합: DBBM의 느린 흡수는 부피를 보존하지만 초기 신생골 형성을 역설적으로 억제할 수 있음(DBBM 단독 < 무이식 대조군 4주, p=0.025, Fujioka-Kobayashi 2022); BCP는 토끼 모델서 신생골 +70%(Chakar 2014), 임상 상악동 SR+MA서 +3.48% 신생골·−8.41% 잔존(Alkandari 2025)으로 일관되게 DBBM 초과; DBBM 입자 크기(대 1–2mm vs 소 0.25–1mm)는 상

- `hygienist-periodontal-instrumentation-scaling-overview` [overviews] (HIGH-far→vadvadgi-2024-comparing-effectiveness-traditional-periodontal, 'contradict' · 반박·충돌)
  - **근거 문장**: | [[periodontics/non-surgical-instrumentation/vadvadgi-2024-comparing-effectiveness-traditional-periodontal]] | RCT (n=120) — **data-quality caveat** | 1 · effectiveness | Surgery numerically > hygienist SRP on PPD/CAL; SRP better tolerated. **Narrative text contradicts tables ("illustrative only") — cite direction, not point estimates** |
  - ▸ 출발(`hygienist-periodontal-instrumentation-scaling-overview`) 세줄: 치위생사 스케일링·치주기구조작 14편을 네 전선 — 효과성·적응증, 술자 인체공학, 에어로졸·감염관리, 체어사이드 안전 2건 — 으로 종합. 핵심 적응증 경계: 저위험 건강 성인의 루틴 스케일링·폴리싱은 치주 이득이 거의 없으나(Lamont, Cochrane 고신뢰, n=1,711), 진단된 치주염의 치료적 스케일링·치근활택술(SRP)은 크고 실제 진료에서 재현되는 이득(Tomasi, DH 95명, 치주낭 폐쇄 ~69–72%, 다회 내원 대비 비열등·시술시간 ~17%↓). 술자측: 압전형 초음파 

- `oral-lichen-planus-overview` [overviews] (SOFT→kaur-2022-oral-lichen-planus-malignant-disorder-appraisal, 'challenges the' · 도전)
  - **근거 문장**: OLP is classified as an oral potentially malignant disorder (OPMD), and Warnakulasuriya 2025 cites a transformation rate of **1.14%–2.28%**. But the **synthesis of transformation risk deliberately lives in the `oral-medicine/opmd` subcategory, not here** — this page's job is diagnosis, treatment, and systemic association. For context only: the opmd pages restrict analysis to histopathologically co
  - ▸ 출발(`oral-lichen-planus-overview`) 세줄: 구강편평태선 (Oral Lichen Planus, OLP) 5편을 진단·치료·전신연관 3축으로 종합하되, 악성전환 위험은 `oral-medicine/opmd` 하위카테고리로 분리하고 여기서는 교차참조만 한다. 최고 치료 근거 (Lodi 2020 코크란 SR+MA, 35 RCT/1474명) 는 국소 스테로이드가 위약 대비 통증 해소 RR 1.91 (95% CI 1.08–3.36, 낮은 근거) · 임상적 해소 불확실 (RR 6.00, 매우 낮은 근거) · 타크롤리무스가 클로베타솔보다 나을 수 있음 (
  - ▸ 대상(`kaur-2022-oral-lichen-planus-malignant-disorder-appraisal`) 세줄: 구강편평태선(Oral Lichen Planus, OLP)을 구강잠재악성질환(Oral Potentially Malignant Disorder, OPMD)으로 분류하는 근거의 한계를 문헌 분석으로 비판한 내러티브 논평. 이형성 태선양 병소가 조직학적으로 OLP와 혼동되어 역학연구에서 자주 오분류되고, 이로 인해 악성전환율(Malignant Transformation Rate, MTR) 추정치가 과대산출됨; WHO 기준 적용 연구만 선별하면 MTR 현저히 낮아짐. 진정한 OLP MTR은 엄격한 WHO 

- `oral-lichen-planus-overview` [overviews] (AMBIG→chiang-2021-lichen-planus-malignant-transformation-review, 'challenges the' · 도전)
  - **근거 문장**: OLP is classified as an oral potentially malignant disorder (OPMD), and Warnakulasuriya 2025 cites a transformation rate of **1.14%–2.28%**. But the **synthesis of transformation risk deliberately lives in the `oral-medicine/opmd` subcategory, not here** — this page's job is diagnosis, treatment, and systemic association. For context only: the opmd pages restrict analysis to histopathologically co
  - ▸ 출발(`oral-lichen-planus-overview`) 세줄: 구강편평태선 (Oral Lichen Planus, OLP) 5편을 진단·치료·전신연관 3축으로 종합하되, 악성전환 위험은 `oral-medicine/opmd` 하위카테고리로 분리하고 여기서는 교차참조만 한다. 최고 치료 근거 (Lodi 2020 코크란 SR+MA, 35 RCT/1474명) 는 국소 스테로이드가 위약 대비 통증 해소 RR 1.91 (95% CI 1.08–3.36, 낮은 근거) · 임상적 해소 불확실 (RR 6.00, 매우 낮은 근거) · 타크롤리무스가 클로베타솔보다 나을 수 있음 (

- `oral-lichen-planus-overview` [overviews] (AMBIG→gonzalez-moles-2021-lichen-planus-malignant-transformation-sr, 'challenges the' · 도전)
  - **근거 문장**: OLP is classified as an oral potentially malignant disorder (OPMD), and Warnakulasuriya 2025 cites a transformation rate of **1.14%–2.28%**. But the **synthesis of transformation risk deliberately lives in the `oral-medicine/opmd` subcategory, not here** — this page's job is diagnosis, treatment, and systemic association. For context only: the opmd pages restrict analysis to histopathologically co
  - ▸ 출발(`oral-lichen-planus-overview`) 세줄: 구강편평태선 (Oral Lichen Planus, OLP) 5편을 진단·치료·전신연관 3축으로 종합하되, 악성전환 위험은 `oral-medicine/opmd` 하위카테고리로 분리하고 여기서는 교차참조만 한다. 최고 치료 근거 (Lodi 2020 코크란 SR+MA, 35 RCT/1474명) 는 국소 스테로이드가 위약 대비 통증 해소 RR 1.91 (95% CI 1.08–3.36, 낮은 근거) · 임상적 해소 불확실 (RR 6.00, 매우 낮은 근거) · 타크롤리무스가 클로베타솔보다 나을 수 있음 (

- `osteotomy-drilling-heat-determinants-irrigation-overview` [overviews] (HIGH-far→saxena-2024-guided-implant-drilling-bone-temperature, 'overturn' · 결론 뒤집음)
  - **근거 문장**: **Tier 3 — situational amplifiers.** Guided surgery: Markovic localizes the guide penalty to the *cortical entrance only* (entrance p<0.001; middle/bottom NS), driven by sleeve obstruction of irrigation plus conductive heating from the metal sleeve itself (guide-temp ↔ bone-temp Spearman rho=0.868); Saxena's SR ([[implants/osteotomy-thermal/saxena-2024-guided-implant-drilling-bone-temperature]]) c
  - ▸ 출발(`osteotomy-drilling-heat-determinants-irrigation-overview`) 세줄: 임플란트 골절제 드릴링 발열 28편을 "요인 나열"이 아니라 **무엇을 실제로 통제할지의 근거가중 순위**로 재구성: 47°C/1분 괴사 역치(Timon 2019 교차검증; 정형외과 ~50°C), 다인자 프레이밍(Chauhan 2018 SR 34편; Jung 2021 내부·외부 인자 분류), 생물학적 endpoint(Heuzeroth 2021 in vivo 미니피그 n=36; Kosior 2025 조직학적 골상 점수). 여러 결정인자를 맞대결시킨 연구에서 **관주 온도가 가장 재현성 높은 지렛대*

- `osteotomy-drilling-heat-determinants-irrigation-overview` [overviews] (SOFT→gehrke-2020-technique-drill-design-osteotomy, 'disagree' · 불일치)
  - **근거 문장**: **Peck drilling is conditional, not a general escalation — a correction to this page's own earlier guidance.** Intermittent ("peck") drilling is recommended above and in most protocol lists as if it were an independent thermal lever. Two studies that tested it directly say otherwise, and they disagree with each other in an informative way. Gehrke ([[implants/osteotomy-thermal/gehrke-2020-technique
  - ▸ 출발(`osteotomy-drilling-heat-determinants-irrigation-overview`) 세줄: 임플란트 골절제 드릴링 발열 28편을 "요인 나열"이 아니라 **무엇을 실제로 통제할지의 근거가중 순위**로 재구성: 47°C/1분 괴사 역치(Timon 2019 교차검증; 정형외과 ~50°C), 다인자 프레이밍(Chauhan 2018 SR 34편; Jung 2021 내부·외부 인자 분류), 생물학적 endpoint(Heuzeroth 2021 in vivo 미니피그 n=36; Kosior 2025 조직학적 골상 점수). 여러 결정인자를 맞대결시킨 연구에서 **관주 온도가 가장 재현성 높은 지렛대*
  - ▸ 대상(`gehrke-2020-technique-drill-design-osteotomy`) 세줄: In vivo 토끼 연구(n=48 골절제, 4군): 원통형 vs 원추형 드릴 × 연속 vs 간헐 동작(Peck drilling)이 골절제 온도·30일 골 치유에 미치는 영향. 간헐 동작(0→3mm / 0→5mm / 0→8mm 3단계)은 원통형 드릴에서 2.6°C 감소(p=0.001, −37%)했으나 원추형에서는 효과 없음(p=0.977); 원추형은 기법 무관 모든 지표 우수. 드릴 형태가 Peck drilling 효익을 결정: 원추형은 드릴 자체가 발열을 통제하므로 기법 의존성 낮음; 원통형에서는

- `osteotomy-drilling-heat-determinants-irrigation-overview` [overviews] (AMBIG→di-fiore-2018-continuous-intermittent-drilling-temperature, 'disagree' · 불일치)
  - **근거 문장**: **Peck drilling is conditional, not a general escalation — a correction to this page's own earlier guidance.** Intermittent ("peck") drilling is recommended above and in most protocol lists as if it were an independent thermal lever. Two studies that tested it directly say otherwise, and they disagree with each other in an informative way. Gehrke ([[implants/osteotomy-thermal/gehrke-2020-technique
  - ▸ 출발(`osteotomy-drilling-heat-determinants-irrigation-overview`) 세줄: 임플란트 골절제 드릴링 발열 28편을 "요인 나열"이 아니라 **무엇을 실제로 통제할지의 근거가중 순위**로 재구성: 47°C/1분 괴사 역치(Timon 2019 교차검증; 정형외과 ~50°C), 다인자 프레이밍(Chauhan 2018 SR 34편; Jung 2021 내부·외부 인자 분류), 생물학적 endpoint(Heuzeroth 2021 in vivo 미니피그 n=36; Kosior 2025 조직학적 골상 점수). 여러 결정인자를 맞대결시킨 연구에서 **관주 온도가 가장 재현성 높은 지렛대*

- `osteotomy-drilling-heat-determinants-irrigation-overview` [overviews] (HIGH-far→jain-2024-heat-generation-pain-piezosurgery-drilling, 'contradict' · 반박·충돌)
  - **근거 문장**: *Piezosurgery inverts its own marketing.* The canonical review ([[implants/osteotomy-thermal/stubinger-2015-piezosurgery-implant-dentistry]]) lists avoidance of thermal damage among piezo's advantages alongside selective mineralized-tissue cutting and soft-tissue/membrane/nerve preservation. That specific claim does not survive the measurements: Aquilanti recorded piezo ΔT of **53–65°C against rot
  - ▸ 출발(`osteotomy-drilling-heat-determinants-irrigation-overview`) 세줄: 임플란트 골절제 드릴링 발열 28편을 "요인 나열"이 아니라 **무엇을 실제로 통제할지의 근거가중 순위**로 재구성: 47°C/1분 괴사 역치(Timon 2019 교차검증; 정형외과 ~50°C), 다인자 프레이밍(Chauhan 2018 SR 34편; Jung 2021 내부·외부 인자 분류), 생물학적 endpoint(Heuzeroth 2021 in vivo 미니피그 n=36; Kosior 2025 조직학적 골상 점수). 여러 결정인자를 맞대결시킨 연구에서 **관주 온도가 가장 재현성 높은 지렛대*

- `maurice-szamburski-2025-intravenous-nsaids-perioperative-pain-narrative-review` [drug/analgesics] (SOFT→costa-2015-preemptive-nsaids-third-molar-pain-meta, 'whereas' · 반면(대조))
  - **근거 문장**: - [[drug/analgesics/costa-2015-preemptive-nsaids-third-molar-pain-meta]] — contrast: found no significant benefit from *oral* preemptive NSAIDs in third-molar extraction specifically, whereas this review's preemptive-IV-ibuprofen data (45% opioid reduction) comes from non-dental general surgery — consistent with Costa's own caveat that the effect may be indication-specific.
  - ▸ 출발(`maurice-szamburski-2025-intravenous-nsaids-perioperative-pain-narrative-review`) 세줄: 본 내러티브 리뷰는 성인과 소아에서 수술 전후 통증 관리에 사용되는 정맥 내 비스테로이드성 소염진통제(IV NSAIDs)에 관한 최근 10년간(2024년 5월까지)의 문헌을 종합하였으며, ibuprofen, ketorolac, ketoprofen, naproxen, paracetamol, acetylsalicylic acid를 중심으로 유럽의 승인 현황과 임상 관행을 검토하였다. IV NSAIDs는 수술 후 아편유사제(opioid) 사용을 약 20–60% 감소시키며, IV ibuprofen은 아편
  - ▸ 대상(`costa-2015-preemptive-nsaids-third-molar-pain-meta`) 세줄: SR+MA(Anesth Prog 2015; 6편 RCT 확인, 4편 정량분석 가능, n=298): 제3대구치 외과적 발치 전 경구 NSAID 선제 투여의 술후 통증 감소 효과 검증. 선제적 경구 NSAID vs 대조군의 통합 효과 유의하지 않음(P=0.2227); 제3대구치 발치에 대한 routine 선제 처방 정당화 근거 불충분. 정량분석에 포함된 RCT 4편만으로 검정력 제한적이며 방법론적 이질성 높음; 치주/임플란트 수술 맥락의 후속 SR은 부분적 이득 제안 → 이 음성 결과는 적응증 특이적

- `bakri-2024-prednisolone-prescribing-styles-third-molar` [drug/analgesics] (HIGH-far→satpathi-2024-corticosteroids-dentistry-review, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[drug/analgesics/satpathi-2024-corticosteroids-dentistry-review]] — narrative review's relative-potency table lists prednisolone at 4× hydrocortisone; this paper's Discussion cites 5–6×. Minor reference-figure discrepancy between two secondary sources (neither is this paper's own measured data) — not a primary-outcome conflict, no `contradicts` edge warranted.
  - ▸ 출발(`bakri-2024-prednisolone-prescribing-styles-third-molar`) 세줄: 무작위 분악(split-mouth) 단일맹검 임상시험(n=15, 18–30세, 양측 매복 하악 사랑니, Jazan University): 술후 경구 프레드니솔론(Prednisolone) 처방 스타일 2종 비교 — 단일용량(25mg 1회) vs 체감용량(tapered dose, 5mg을 1일차 3회·2일차 2회·3일차 1회). 체감용량군이 단일용량군 대비 술후 개구량(day 1/3/7)이 유의하게 크고, 안면부종(구각-이주 거리 및 외안각-하악각 거리)이 유의하게 적음; 통증 VAS는 두 군 간 전

- `ibikunle-2016-prednisolone-qol-third-molar-rct` [drug/analgesics] (SOFT→larsen-2021-methylprednisolone-doses-split-mouth-rct, '대조적' · 대조)
  - **근거 문장**: QoL (OHIP-14) 엔드포인트 + 투여 경로(경구 vs 점막하 주사) 비교 RCT. [[drug/larsen-2021-methylprednisolone-doses-split-mouth-rct]]의 OHIP-14 결과(null)와 대조적으로 프레드니솔론의 QoL 개선 효과를 보고해 약물·경로 차이 논의에 직접 데이터를 제공.
  - ▸ 출발(`ibikunle-2016-prednisolone-qol-third-molar-rct`) 세줄: 줄1: 나이지리아 3차 병원의 3군 무작위대조시험 (Randomized Controlled Trial, RCT) (n=186, 군당 62명)에서 경구 프레드니솔론 (Prednisolone) 40 mg, 점막하 주사 (Submucosal Injection) 40 mg, 무투여 대조군을 비교하여 구강건강관련 삶의 질 (Oral Health-Related Quality of Life, OHRQoL, OHIP-14)을 주요 결과 지표로 평가했다. 줄2: 프레드니솔론 투여군(경구·점막하 모두)은 미투여 대
  - ▸ 대상(`larsen-2021-methylprednisolone-doses-split-mouth-rct`) 세줄: 줄1: 덴마크 알보르 대학병원의 이중맹검 분할구강 (Split-mouth) 무작위대조시험 (Randomized Controlled Trial, RCT) (n=52)에서 양측 하악 사랑니 발치 중 교근 (Masseter) 내 메틸프레드니솔론 (Methylprednisolone) 20/30/40 mg 또는 위약을 주사하고 1·3·7·30일 추적했다. 줄2: 어느 용량에서도 위약 대비 통증(시각통증척도, Visual Analog Scale, VAS)·개구제한 (Trismus)·삶의 질 (OHIP-14)

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants/mbl] (HIGH-far→paknejad-2017-flapless-immediate-implant-buccal-gap-rct, 'contradict' · 반박·충돌)
  - **근거 문장**: User requested a PubMed ingest on flapless implant placement. The wiki's flapless evidence is concentrated in the *immediate*-implant context ([[immediate-implant/pitman-2023-immediate-implant-flap-flapless-sr-ma]], [[immediate-implant/gap-grafting/mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma]], [[immediate-implant/gap-grafting/paknejad-2017-flapless-immediate-implant-buccal-gap-rc
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 세줄: 전향적 RCT (n=40, 하악 구치부 치유된 치조제 단일치 임플란트, 1:1 무작위 배정: 무피판 펀치 vs 전층 점막골막 피판; 4.0 × 10 mm 임플란트; 6개월 치조정 골소실 방사선 평가). 무피판군이 피판군 대비 치조정 골소실 유의하게 적음 — 3개월 (0.32 vs 0.56 mm) 및 6개월 (0.48 vs 0.82 mm, 모두 p<0.001); 양군 생존율 100%, 합병증 없음. 무피판 술식이 치유된 하악 구치부에서 조기 치조정 골소실 감소 이점 제공; 단, 6개월·2D·단일기관

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants/mbl] (AMBIG→mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma, 'contradict' · 반박·충돌)
  - **근거 문장**: User requested a PubMed ingest on flapless implant placement. The wiki's flapless evidence is concentrated in the *immediate*-implant context ([[immediate-implant/pitman-2023-immediate-implant-flap-flapless-sr-ma]], [[immediate-implant/gap-grafting/mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma]], [[immediate-implant/gap-grafting/paknejad-2017-flapless-immediate-implant-buccal-gap-rc
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 세줄: 전향적 RCT (n=40, 하악 구치부 치유된 치조제 단일치 임플란트, 1:1 무작위 배정: 무피판 펀치 vs 전층 점막골막 피판; 4.0 × 10 mm 임플란트; 6개월 치조정 골소실 방사선 평가). 무피판군이 피판군 대비 치조정 골소실 유의하게 적음 — 3개월 (0.32 vs 0.56 mm) 및 6개월 (0.48 vs 0.82 mm, 모두 p<0.001); 양군 생존율 100%, 합병증 없음. 무피판 술식이 치유된 하악 구치부에서 조기 치조정 골소실 감소 이점 제공; 단, 6개월·2D·단일기관

- `kindaro-2026-parathyroid-hormone-implant-osseointegration-osteoporosis-sr` [implants/survival] (SOFT→drug-mronj-antiresorptive-overview, 'whereas' · 반면(대조))
  - **근거 문장**: The wiki frames osteoporosis and its drugs almost entirely as **hazards** to implant therapy: osteoporosis lowers long-term implant survival (short-term 97.9–100% but 5–10 yr 82.6–94.1% with greater marginal bone loss, per [[implants/survival/kim-2026-dental-implant-osteoporosis-osteosclerosis]]), and the antiresorptive agents used to treat it (bisphosphonates, denosumab) raise MRONJ risk ([[overv
  - ▸ 출발(`kindaro-2026-parathyroid-hormone-implant-osseointegration-osteoporosis-sr`) 세줄: 골다공증 유발 난소/고환 절제 쥐·토끼 모델에서 부갑상선호르몬(Parathyroid Hormone, PTH; 테리파라타이드, PTH 1–34)의 임플란트 골유착 효과를 다룬 12편 전임상 연구의 업데이트 체계적 문헌고찰 (Systematic Review, PRISMA·INPLASY·SYRCLE, 2015–2025.8) — 사람 연구는 0편. 간헐적 PTH 투여는 골-임플란트 접촉률(BIC)·골부피율(BV/TV)·제거토크를 대조군 대비 일관되게 증가; 병용요법(PTH+비타민 D, PTH+랄록시펜, 
  - ▸ 대상(`drug-mronj-antiresorptive-overview`) 세줄: 약물관련악골괴사(Medication-Related Osteonecrosis of the Jaw, MRONJ) 14편 통합: 예방 1차 전략은 항흡수제 시작 전 치과 클리어런스(Baghalipour 2025 4단계 프레임워크); 데노수맙(Denosumab) 위험은 누적 용량 의존 — 유방암 골전이 코호트 ≥32회 시 MRONJ 31.2%(Yokoo 2025 ROC AUC 0.83); 발치력 OR 4.40; 미국구강악안면외과학회(AAOMS) 2022는 수술 치료를 전 병기로 확대, 약물 중단(drug

- `wang-2020-volumetric-facial-contour-changes-immediately` [immediate-implant/esthetic-soft-tissue] (HIGH-far→pitman-2022-immediate-implant-provisionalization-sr-ma, 'in contrast to' · 대조)
  - **근거 문장**: - [[immediate-implant/esthetic-soft-tissue/pitman-2022-immediate-implant-provisionalization-sr-ma]] — this paper's volumetric finding (provisionalization favors soft-tissue contour) is directionally consistent with Pitman's pooled SR+MA conclusion that immediate provisionalization favors papilla/soft-tissue contour, in contrast to Chan 2019's own null finding on the identical cohort. No structured
  - ▸ 출발(`wang-2020-volumetric-facial-contour-changes-immediately`) 세줄: 무작위대조시험 (Randomized Controlled Trial, RCT), 발치가 불가피한 상악 전치부·소구치에 즉시식립 (Immediate Implant Placement, IIP)된 단일임플란트 환자 n=40명 대상; 임시크라운을 이용한 즉시 임시보철 (Immediate Provisionalization)군과 치유지대주 (Healing Abutment)군의 12개월 3차원 안면 치조정 윤곽 변화를 비교. 선형 3차원 공간적 흡수 (Linear 3D Spatial Resorption)는 0.

- `block-2009-prospective-evaluation-immediate-delayed` [immediate-implant/esthetic-soft-tissue] (SOFT→asghar-2023-immediate-vs-early-implant-esthetic-zone-sr-ma, 'unlike' · 다름)
  - **근거 문장**: - [[immediate-implant/esthetic-soft-tissue/asghar-2023-immediate-vs-early-implant-esthetic-zone-sr-ma]] — SR+MA of immediate-vs-early (rather than delayed) placement in the esthetic zone; extends the timing-comparison question to an adjacent timing pair, similarly finding no bone-level difference but (unlike this trial) a Pink Esthetic Score disadvantage for immediate placement.
  - ▸ 출발(`block-2009-prospective-evaluation-immediate-delayed`) 세줄: 전향적 RCT, n=55명 2년 추적 (초기 모집 76명), 즉시 임플란트 식립·즉시 가철성 임시치관 (Immediate Provisionalization) vs. 지연 식립(4개월 경과) 후 즉시 임시치관 비교; 양 군 모두 유사한 골정 반응 및 임플란트 골유착 (Osseointegration)을 보임. 즉시 식립군은 지연 식립군 대비 협측 치은변연 (Facial Gingival Margin) 위치를 1mm 더 보존 (P < .05); 변연골수준 (Crestal Bone Level, CBL)은 
  - ▸ 대상(`asghar-2023-immediate-vs-early-implant-esthetic-zone-sr-ma`) 세줄: 건강한 성인의 심미부위 단일치 수복에서 즉시식립 (Immediate Implant Placement, IIP)과 조기식립 (Early Implant Placement, EIP)을 비교한 무작위대조시험(RCT) 6편의 체계적 문헌고찰+메타분석 (Systematic Review + Meta-Analysis, SR+MA), Cochrane ROB-2 도구로 비뚤림 위험 평가. 수직 골레벨(4개 연구, 148명, MD 0.10, P>0.05)과 치은열구탐침깊이 (Probing Depth, PD)(2개 연

- `bragues-2024-oral-mucositis-children-cancer-management-sr` [oral-medicine/mucositis] (SOFT→dean-2022-oral-chronic-gvhd-review, 'whereas' · 반면(대조))
  - **근거 문장**: The wiki's oral mucosal-disease coverage in `oral-medicine` (aphthous stomatitis, lichen planus, BMS) had no entry on cancer-therapy-induced oral mucositis — a high-incidence (40–100%) inflammatory condition distinct from those entities. This SR fills that gap and pairs with [[oral-medicine/immune-mediated/dean-2022-oral-chronic-gvhd-review]], which covers the adjacent oncology context (oral chron
  - ▸ 출발(`bragues-2024-oral-mucositis-children-cancer-management-sr`) 세줄: PRISMA 체계적 문헌고찰(PROSPERO CRD42022347208; 2655건 → 39편 포함, n=14–148; 이질성으로 메타분석 불가) — 소아(≤18세) 항암·방사선·조혈모세포이식 유발 구강점막염(OM) 관리 중재 비교. OM 발생률엔 클로르헥시딘, 기간엔 꿀, 통증엔 올리브유가 최적; 팔리퍼민(KGF)은 급성백혈병에서 발생률·중증도·기간 모두 감소; 칼슘인산염은 3편 모두 효과 없음; LLLT/광생체조절이 가장 많이 연구된 중재(8편, 20%)이나 결과 불일치. 소아 OM 프로토콜 
  - ▸ 대상(`dean-2022-oral-chronic-gvhd-review`) 세줄: 동종 조혈모세포이식(alloHCT) 수혜자 30–50%에서 발생하는 구강 만성 이식편대숙주병(cGVHD) 내러티브 미니리뷰 — 태선양 점막염·면역성 타액선 기능저하·조직 경화/개구장애 세 아형 정리. NIH 2014 진단·병기 기준 적용; 국소 스테로이드 세척 → 전신 면역억제로 단계적 관리, 난치성은 표적 면역억제제로 전환. 구강 cGVHD는 주요 이환율 원인인 동시에 악성전환 부위(OPMD)로 인식되어 전신 질환 관리와 함께 장기적 구강 감시 필요.

- `nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy` [oral-medicine/salivary-chemosensory] (AMBIG→poudel-2026-xerostomia-dental-treatment-outcomes-sr, '뒤집' · 뒤집음)
  - **근거 문장**: 기존 위키에는 침(saliva)이 질병의 *결과물*(COVID 후유증)로만 나타난다 — [[oral-medicine/salivary-chemosensory/tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva]]. 이 JADA 리뷰는 침을 *진단 매체*로 뒤집는 관점(salivaomics·exosomics·liquid biopsy)을 도입해, 침샘 기능/구강건조 라인([[oral-medicine/salivary-chemosensory/poudel-2026-xerostomia-dental-treatment-outcomes-sr]])과 대비되는 "침의 진단적 활용" 축을 새로 연다. Wong 그룹(UCLA)의 salivaomics 프레임워크 원전으로, 향후 침 바이오마
  - ▸ 출발(`nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`) 세줄: 전문가 서술 리뷰(JADA 2023, Wong/UCLA 그룹) — 침 진단(saliva diagnostics)을 살리바오믹스(salivaomics)·침 엑소좀학(saliva exosomics)·침 액체생검(saliva liquid biopsy) 세 축으로 분류, 침·혈장 단백질체 20–30% 중첩으로 전신 바이오마커의 침샘 이송 가능성 지지. 전기화학 센서 EFIRM(Electric Field–Induced Release and Measurement)은 추출·증폭 없이 40–50 µL 침에서 폐암

- `lamont-2018-routine-scale-and-polish-periodontal-health` [periodontics/non-surgical-instrumentation] (SOFT→farina-2026-pmpr-biofilm-gingivitis-sr-ma, 'whereas' · 반면(대조))
  - **근거 문장**: - [[periodontics/non-surgical-instrumentation/farina-2026-pmpr-biofilm-gingivitis-sr-ma]] — contrast: PMPR adds benefit as an adjunct to OHI in *established* gingivitis, whereas this review finds no benefit of *routine* prophylaxis in low-risk healthy adults (different population/question).
  - ▸ 출발(`lamont-2018-routine-scale-and-polish-periodontal-health`) 세줄: 코크란 SR+MA (RCT 2편, n=1711, 영국 일반 치과) — 중증 치주염 없는 정기 내원 성인에서 6개월·12개월 루틴 스케일링·폴리싱 대 무처치를 2~3년간 비교. 루틴 스케일링·폴리싱은 치은염·치주낭 깊이·구강건강 삶의 질에 거의 차이 없음(고신뢰도); 치석만 소폭 감소(6개월 > 12개월)하나 임상적 의의 불분명. 저위험 건강 성인에서 고정 간격 예방처치는 치주건강에 근거가 없으며, 개인 위험도 기반 리콜로의 전환을 지지.
  - ▸ 대상(`farina-2026-pmpr-biofilm-gingivitis-sr-ma`) 세줄: EFP 21차 워크숍 SR+MA (11편, 주로 RCT): 판막방해 인자 없는 성인의 치태-유발 치은염에서 전문가 기계적 치태제거 (Professional Mechanical Plaque Removal, PMPR)에 대한 3개 집중 질문 검토. PMPR 단독은 구강위생 불량 지속 환자에서 효과 없음; PMPR+구강위생교육(OHI) > OHI 단독 (low certainty); 에어폴리싱+초음파 = 초음파+러버컵 폴리싱 (효과 동등, 더 빠름, very low certainty); 다이오드 레이저 

- `wallace-2003-effect-maxillary-sinus-augmentation-survival` [sinus-lift/lateral] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Landmark early synthesis but abstract-only in this ingest (no PMC full text) and methodologically dated — pre-CBCT, pre-GRADE, mostly retrospective/case-series evidence (only 3 of 43 studies were RCTs); its membrane-benefit finding is directly contradicted by a later, RCT-only SR+MA.
  - ▸ 출발(`wallace-2003-effect-maxillary-sinus-augmentation-survival`) 세줄: 체계적 문헌고찰 + 메타회귀 (43개 연구: lateral window 34편, osteotome 5편, 국소 상악동저 관리 2편, crestal core 2편) — 2003년 4월까지 발표된, 상악동 거상술 후 임플란트 생존율. Lateral window 임플란트 생존율 평균 91.8%(범위 61.7–100%); 거친 표면 임플란트, 블록형보다 입자형 (Particulate) 이식재, 측창 (Lateral Window) 막 (Membrane) 피개 시 생존율이 유의하게 높았고, 자가골 함유량·동

- `wallace-2003-effect-maxillary-sinus-augmentation-survival` [sinus-lift/lateral] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 초기의 대표적 종합 연구이지만 이번 인제스트는 초록만 확보(PMC 전문 없음)했고 방법론적으로 오래됨 — CBCT·GRADE 이전 시대, 43편 중 RCT는 3편뿐(대부분 후향적·증례군); 특히 막 피개 효과 결론은 이후 RCT만으로 구성된 SR+MA에서 정면으로 반박됨.
  - ▸ 출발(`wallace-2003-effect-maxillary-sinus-augmentation-survival`) 세줄: 체계적 문헌고찰 + 메타회귀 (43개 연구: lateral window 34편, osteotome 5편, 국소 상악동저 관리 2편, crestal core 2편) — 2003년 4월까지 발표된, 상악동 거상술 후 임플란트 생존율. Lateral window 임플란트 생존율 평균 91.8%(범위 61.7–100%); 거친 표면 임플란트, 블록형보다 입자형 (Particulate) 이식재, 측창 (Lateral Window) 막 (Membrane) 피개 시 생존율이 유의하게 높았고, 자가골 함유량·동

- `kim-2024-advancements-alveolar-bone-grafting-ridge` [bone-regeneration/ridge-preservation] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: (줄3: 선정기준 없는 비체계적 종설이라 인용한 상충 결과를 조정하지 못함 — 예컨대 인용 연구 하나는 임플란트 성공률에서 ARP와 자연치유 간 차이 없음을 보고하는데, 이는 리뷰 전반의 친(親)ARP 기조와 어긋난다.)
  - ▸ 출발(`kim-2024-advancements-alveolar-bone-grafting-ridge`) 세줄: (줄1: 종설 (Narrative Review, 강릉원주대학교 치과대학) — 치조제 보존술 (Alveolar Ridge Preservation, ARP) 재료(동종골/이종골 대체재, 혈소판풍부섬유소 (Platelet-Rich Fibrin, PRF) 등 혈소판농축제제, 콜라겐막, 생체활성·주사형 하이드로겔)와 술식의 발전 종합.) (줄2: 장기 임플란트 생존율 보고(일부 코호트 5–7년 100%, 별도 코호트 환자단위 93.7%, n=108명/308개 임플란트), 1년 심미만족도 시각아날로그척도 (

- `kim-2024-advancements-alveolar-bone-grafting-ridge` [bone-regeneration/ridge-preservation] (HIGH-far→mardas-2023-alveolar-ridge-preservation-overtreatment, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[bone-regeneration/ridge-preservation/mardas-2023-alveolar-ridge-preservation-overtreatment]] — not typed-edged (see note below). Mardas 2023 frames ARP as scenario-dependent and often overtreatment (posterior thick-wall sites, immediate-implant sites, sites already staged for augmentation), citing evidence that ARP does not consistently increase vital bone formation. This review's abstract/con
  - ▸ 출발(`kim-2024-advancements-alveolar-bone-grafting-ridge`) 세줄: (줄1: 종설 (Narrative Review, 강릉원주대학교 치과대학) — 치조제 보존술 (Alveolar Ridge Preservation, ARP) 재료(동종골/이종골 대체재, 혈소판풍부섬유소 (Platelet-Rich Fibrin, PRF) 등 혈소판농축제제, 콜라겐막, 생체활성·주사형 하이드로겔)와 술식의 발전 종합.) (줄2: 장기 임플란트 생존율 보고(일부 코호트 5–7년 100%, 별도 코호트 환자단위 93.7%, n=108명/308개 임플란트), 1년 심미만족도 시각아날로그척도 (

- `barbosa-2020-the-influence-of-endodontic-access` [endodontics/anatomy] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refutation of the fracture-resistance argument for conservative access: post-restoration fracture resistance was equivalent across all three designs (P > 0.05)
  - ▸ 출발(`barbosa-2020-the-influence-of-endodontic-access`) 세줄: 추출 하악대구치(n=30)를 전통 접근와동 (Traditional Endodontic Cavity, TEC), 보존적 접근와동 (Conservative Endodontic Cavity, CEC), 트러스 접근와동 (Truss Access Cavity, TAC)으로 비교한 실험실 연구로, 미세 컴퓨터 단층촬영 (Micro-CT)과 Reciproc Blue 파일로 형성 효율·미생물 감소·충전 품질·파절저항을 측정함. CEC·TAC는 TEC 대비 미형성 근관 표면적(%)과 근관실 내 잔여 충전재 용량이

- `caviedes-bucheli-2026-neuropeptide-y-dental-pulp` [endodontics/anatomy] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: **VIP counterpoint**: Parasympathetic VIP (vasodilatory) increases modestly in mild-moderate caries as a compensatory fine-tuner against NPY vasoconstriction. NPY is ~2× more abundant than VIP in healthy pulp, reflecting greater sympathetic than parasympathetic fibre density.
  - ▸ 출발(`caviedes-bucheli-2026-neuropeptide-y-dental-pulp`) 세줄: PubMed·Web of Science·Scopus 창간~2026년 2월 PRISMA 서사 합성(92편), in vitro·동물·인체 조직 포함. NPY는 교감 혈관주위 섬유에서 분비되어 Gi/Go 결합 Y1/Y2 수용체로 SP/CGRP 유발 혈관확장·수내압 상승을 억제하고, TRPV1 차단으로 진통효과 발휘, BMP-2 경로로 제3기 상아질 형성 촉진; Y1 발현은 경증~중등도 우식 최고→진행 우식 급락. SP/CGRP(흥분) ↔ NPY(억제) 균형이 치수생존 결정하나, RCT 전무하고 현 근거

- `saeed-2021-impact-of-access-cavity` [endodontics/anatomy] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 10편 중 4편만 ConsAC에서 유의미하게 높은 파절저항성 확인; 나머지는 유의차 없음 또는 상충 결과 (하악 대구치에서만 차이, 상악 대구치에서는 아님).
  - ▸ 출발(`saeed-2021-impact-of-access-cavity`) 세줄: 2010~2020년 1월까지의 생체외 실험 10편의 체계적 고찰 (Systematic Review, SR): 추출된 대구치에서 보존적 접근강 (Conservative Access Cavity, ConsAC) vs 전통적 접근강 (Traditional Access Cavity, TradAC)의 파절저항성 (Fracture Resistance) 비교 (105편 스크린 → 10편 포함). 10편 중 4편만 ConsAC에서 유의미하게 높은 파절저항성 확인; 나머지는 유의차 없음 또는 상충 결과 (하악 대
