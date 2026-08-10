# 논쟁 레이더 백필 후보 — 2026-07-24

명시적 충돌 표현이 있으나 그 쌍에 `relations:` 타입 엣지가 (어떤 타입이든) 없는 후보. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**

**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. 아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), (2) **양쪽 페이지의 `## 세줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. 충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. (reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것 — 2026-07-17 전수 검토에서 contradicts 계열로 지목된 122건 중 실제 contradicts는 1건이었다.)

**대상은 키워드에 가장 가까운 링크로 특정한다.** 같은 줄의 나머지 링크는 충돌 표현의 대상이라는 근거가 없어 Tier 2(`AMBIG→`)로 강등된다 — 버리지 않으니 진짜 대상이 강등됐다면 Tier 2에서 찾을 수 있다.

- Tier 1 (대상 지목됨, actionable): **1**
- Tier 2 (대상 불명/soft, review): **27**
- (억제됨) 이미 typed 엣지가 있어 제외: **229** · 부정문 제외: **82** · 검토·불필요 대장: **397** · 동일 줄 비최근접으로 Tier 2 강등: **4**

## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)

### oral-medicine

- `nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`  —[뒤집 · 뒤집음]→  **`tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva`**
  - **근거 문장**: 기존 위키에는 침(saliva)이 질병의 *결과물*(COVID 후유증)로만 나타난다 — [[oral-medicine/salivary-chemosensory/tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva]]. 이 JADA 리뷰는 침을 *진단 매체*로 뒤집는 관점(salivaomics·exosomics·liquid biopsy)을 도입해, 침샘 기능/구강건조 라인([[oral-medicine/salivary-chemosensory/poudel-2026-xerostomia-dental-treatment-outcomes-sr]])과 대비되는 "침의 진단적 활용" 축을 새로 연다. Wong 그룹(UCLA)의 salivaomics 프레임워크 원전으로, 향후 침 바이오마
  - ▸ 출발(`nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`) 세줄: 전문가 서술 리뷰(JADA 2023, Wong/UCLA 그룹) — 침 진단(saliva diagnostics)을 살리바오믹스(salivaomics)·침 엑소좀학(saliva exosomics)·침 액체생검(saliva liquid biopsy) 세 축으로 분류, 침·혈장 단백질체 20–30% 중첩으로 전신 바이오마커의 침샘 이송 가능성 지지. 전기화학 센서 EFIRM(Electric Field–Induced Release and Measurement)은 추출·증폭 없이 40–50 µL 침에서 폐암
  - ▸ 대상(`tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva`) 세줄: 내러티브 리뷰(약 90편 이상 연구, 코로나19 환자·완치자 총 6만5천여 명 종합) — 미각장애(ageusia/dysgeusia)와 침분비저하(xerostomia/hyposalivation) 등 구강 후유증의 지속 기간·유병률 종합. 미각장애는 완치 후 3주~12개월 추적에서 1~45%, 침분비저하는 2~40%에서 지속되고 서로 상관관계가 있으며; 지리적 구배(동아시아 3.8% vs 중동 20.6%)가 미각장애에서 뚜렷함. 타액선·미뢰의 ACE2/TRPV1 수용체 발현과 감염 유발 아연결핍이라는


## Tier 2 — 대상 식별 필요 / soft signal (review only)

- `caviedes-bucheli-2026-neuropeptide-y-dental-pulp` [endodontics] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: **VIP counterpoint**: Parasympathetic VIP (vasodilatory) increases modestly in mild-moderate caries as a compensatory fine-tuner against NPY vasoconstriction. NPY is ~2× more abundant than VIP in healthy pulp, reflecting greater sympathetic than parasympathetic fibre density.
  - ▸ 출발(`caviedes-bucheli-2026-neuropeptide-y-dental-pulp`) 세줄: PubMed·Web of Science·Scopus 창간~2026년 2월 PRISMA 서사 합성(92편), in vitro·동물·인체 조직 포함. NPY는 교감 혈관주위 섬유에서 분비되어 Gi/Go 결합 Y1/Y2 수용체로 SP/CGRP 유발 혈관확장·수내압 상승을 억제하고, TRPV1 차단으로 진통효과 발휘, BMP-2 경로로 제3기 상아질 형성 촉진; Y1 발현은 경증~중등도 우식 최고→진행 우식 급락. SP/CGRP(흥분) ↔ NPY(억제) 균형이 치수생존 결정하나, RCT 전무하고 현 근거

- `selvaraj-2023-fracture-resistance-of-endodontically` [post-and-core] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: FRC(EverX Posterior, Ribbond, Vectris)는 16편 중 15편에서 재래식 하이브리드/나노하이브리드 복합레진 대비 파절저항 우위(강한 근거); 벌크필 (Bulk-fill Composite) 대비 제한적·상충 근거, 파이버 포스트 (Fiber Post)·인레이 (Inlay) 대비 중간 수준 근거, 엔도크라운 (Endocrown) 비교 근거 없음.
  - ▸ 출발(`selvaraj-2023-fracture-resistance-of-endodontically`) 세줄: PRISMA·PROSPERO(CRD42021295212) 기반 체계적 문헌고찰(SR): 근관치료된 구치부 치아의 파절저항에 대해 섬유강화복합레진 (Fiber-Reinforced Composite, FRC) vs 다양한 비교대상 18편 인비트로 연구 종합; 높은 이질성으로 메타분석 불가. FRC(EverX Posterior, Ribbond, Vectris)는 16편 중 15편에서 재래식 하이브리드/나노하이브리드 복합레진 대비 파절저항 우위(강한 근거); 벌크필 (Bulk-fill Composite)

- `nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy` [oral-medicine] (AMBIG→poudel-2026-xerostomia-dental-treatment-outcomes-sr, '뒤집' · 뒤집음)
  - **근거 문장**: 기존 위키에는 침(saliva)이 질병의 *결과물*(COVID 후유증)로만 나타난다 — [[oral-medicine/salivary-chemosensory/tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva]]. 이 JADA 리뷰는 침을 *진단 매체*로 뒤집는 관점(salivaomics·exosomics·liquid biopsy)을 도입해, 침샘 기능/구강건조 라인([[oral-medicine/salivary-chemosensory/poudel-2026-xerostomia-dental-treatment-outcomes-sr]])과 대비되는 "침의 진단적 활용" 축을 새로 연다. Wong 그룹(UCLA)의 salivaomics 프레임워크 원전으로, 향후 침 바이오마
  - ▸ 출발(`nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`) 세줄: 전문가 서술 리뷰(JADA 2023, Wong/UCLA 그룹) — 침 진단(saliva diagnostics)을 살리바오믹스(salivaomics)·침 엑소좀학(saliva exosomics)·침 액체생검(saliva liquid biopsy) 세 축으로 분류, 침·혈장 단백질체 20–30% 중첩으로 전신 바이오마커의 침샘 이송 가능성 지지. 전기화학 센서 EFIRM(Electric Field–Induced Release and Measurement)은 추출·증폭 없이 40–50 µL 침에서 폐암

- `abutment-screw-preload-joint-stability-overview` [overviews] (SOFT→varvara-2020-retightening-preload-loss-abutment-screws, 'challenges the' · 도전)
  - **근거 문장**: - [[prosthetic-materials/abutment-screw/varvara-2020-retightening-preload-loss-abutment-screws]] — retightening-interval study: 2 min minimized preload loss better than 5/10 min (challenges the 10-min standard); internal hex retains more preload than external hex at every interval.
  - ▸ 출발(`abutment-screw-preload-joint-stability-overview`) 세줄: 18편 종합: 나사 풀림(5년 ~10.4%, 10년 ~20.8%)은 전하중 손실이 원인이며, 기전은 세틀링(무하중에서도 2–10%)과 동적 피로(제거토크 손실 16.1–39%) 둘 — 마찰·조도가 핵심 레버(가해진 토크 중 ~8–10%만 전하중化; 탄소코팅 나사 10회 재사용 시 전하중 329.9→253.7 N 감소, Sagheb 2023). 재조임이 세틀링 보상(최적 시점 논쟁: 10분 Nithyapriya 2018·Vinhas 2022 vs 2분 Varvara 2020; 2회째에 plateau
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

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants] (HIGH-far→paknejad-2017-flapless-immediate-implant-buccal-gap-rct, 'contradict' · 반박·충돌)
  - **근거 문장**: User requested a PubMed ingest on flapless implant placement. The wiki's flapless evidence is concentrated in the *immediate*-implant context ([[immediate-implant/pitman-2023-immediate-implant-flap-flapless-sr-ma]], [[immediate-implant/gap-grafting/mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma]], [[immediate-implant/gap-grafting/paknejad-2017-flapless-immediate-implant-buccal-gap-rc
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 세줄: 전향적 RCT (n=40, 하악 구치부 치유된 치조제 단일치 임플란트, 1:1 무작위 배정: 무피판 펀치 vs 전층 점막골막 피판; 4.0 × 10 mm 임플란트; 6개월 치조정 골소실 방사선 평가). 무피판군이 피판군 대비 치조정 골소실 유의하게 적음 — 3개월 (0.32 vs 0.56 mm) 및 6개월 (0.48 vs 0.82 mm, 모두 p<0.001); 양군 생존율 100%, 합병증 없음. 무피판 술식이 치유된 하악 구치부에서 조기 치조정 골소실 감소 이점 제공; 단, 6개월·2D·단일기관

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants] (AMBIG→mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma, 'contradict' · 반박·충돌)
  - **근거 문장**: User requested a PubMed ingest on flapless implant placement. The wiki's flapless evidence is concentrated in the *immediate*-implant context ([[immediate-implant/pitman-2023-immediate-implant-flap-flapless-sr-ma]], [[immediate-implant/gap-grafting/mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma]], [[immediate-implant/gap-grafting/paknejad-2017-flapless-immediate-implant-buccal-gap-rc
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 세줄: 전향적 RCT (n=40, 하악 구치부 치유된 치조제 단일치 임플란트, 1:1 무작위 배정: 무피판 펀치 vs 전층 점막골막 피판; 4.0 × 10 mm 임플란트; 6개월 치조정 골소실 방사선 평가). 무피판군이 피판군 대비 치조정 골소실 유의하게 적음 — 3개월 (0.32 vs 0.56 mm) 및 6개월 (0.48 vs 0.82 mm, 모두 p<0.001); 양군 생존율 100%, 합병증 없음. 무피판 술식이 치유된 하악 구치부에서 조기 치조정 골소실 감소 이점 제공; 단, 6개월·2D·단일기관

- `bragues-2024-oral-mucositis-children-cancer-management-sr` [oral-medicine/mucositis] (SOFT→dean-2022-oral-chronic-gvhd-review, 'whereas' · 반면(대조))
  - **근거 문장**: The wiki's oral mucosal-disease coverage in `oral-medicine` (aphthous stomatitis, lichen planus, BMS) had no entry on cancer-therapy-induced oral mucositis — a high-incidence (40–100%) inflammatory condition distinct from those entities. This SR fills that gap and pairs with [[oral-medicine/immune-mediated/dean-2022-oral-chronic-gvhd-review]], which covers the adjacent oncology context (oral chron
  - ▸ 출발(`bragues-2024-oral-mucositis-children-cancer-management-sr`) 세줄: PRISMA 체계적 문헌고찰(PROSPERO CRD42022347208; 2655건 → 39편 포함, n=14–148; 이질성으로 메타분석 불가) — 소아(≤18세) 항암·방사선·조혈모세포이식 유발 구강점막염(OM) 관리 중재 비교. OM 발생률엔 클로르헥시딘, 기간엔 꿀, 통증엔 올리브유가 최적; 팔리퍼민(KGF)은 급성백혈병에서 발생률·중증도·기간 모두 감소; 칼슘인산염은 3편 모두 효과 없음; LLLT/광생체조절이 가장 많이 연구된 중재(8편, 20%)이나 결과 불일치. 소아 OM 프로토콜 
  - ▸ 대상(`dean-2022-oral-chronic-gvhd-review`) 세줄: 동종 조혈모세포이식(alloHCT) 수혜자 30–50%에서 발생하는 구강 만성 이식편대숙주병(cGVHD) 내러티브 미니리뷰 — 태선양 점막염·면역성 타액선 기능저하·조직 경화/개구장애 세 아형 정리. NIH 2014 진단·병기 기준 적용; 국소 스테로이드 세척 → 전신 면역억제로 단계적 관리, 난치성은 표적 면역억제제로 전환. 구강 cGVHD는 주요 이환율 원인인 동시에 악성전환 부위(OPMD)로 인식되어 전신 질환 관리와 함께 장기적 구강 감시 필요.

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

- `barbosa-2020-the-influence-of-endodontic-access` [endodontics/anatomy] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refutation of the fracture-resistance argument for conservative access: post-restoration fracture resistance was equivalent across all three designs (P > 0.05)
  - ▸ 출발(`barbosa-2020-the-influence-of-endodontic-access`) 세줄: 추출 하악대구치(n=30)를 전통 접근와동 (Traditional Endodontic Cavity, TEC), 보존적 접근와동 (Conservative Endodontic Cavity, CEC), 트러스 접근와동 (Truss Access Cavity, TAC)으로 비교한 실험실 연구로, 미세 컴퓨터 단층촬영 (Micro-CT)과 Reciproc Blue 파일로 형성 효율·미생물 감소·충전 품질·파절저항을 측정함. CEC·TAC는 TEC 대비 미형성 근관 표면적(%)과 근관실 내 잔여 충전재 용량이

- `saeed-2021-impact-of-access-cavity` [endodontics/anatomy] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 10편 중 4편만 ConsAC에서 유의미하게 높은 파절저항성 확인; 나머지는 유의차 없음 또는 상충 결과 (하악 대구치에서만 차이, 상악 대구치에서는 아님).
  - ▸ 출발(`saeed-2021-impact-of-access-cavity`) 세줄: 2010~2020년 1월까지의 생체외 실험 10편의 체계적 고찰 (Systematic Review, SR): 추출된 대구치에서 보존적 접근강 (Conservative Access Cavity, ConsAC) vs 전통적 접근강 (Traditional Access Cavity, TradAC)의 파절저항성 (Fracture Resistance) 비교 (105편 스크린 → 10편 포함). 10편 중 4편만 ConsAC에서 유의미하게 높은 파절저항성 확인; 나머지는 유의차 없음 또는 상충 결과 (하악 대
