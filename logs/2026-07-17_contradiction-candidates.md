# 논쟁 레이더 백필 후보 — 2026-07-17

명시적 충돌 표현이 있으나 그 쌍에 `relations:` 타입 엣지가 (어떤 타입이든) 없는 후보. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**

**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. 아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), (2) **양쪽 페이지의 `## 세줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. 충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. (reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것 — 2026-07-17 전수 검토에서 contradicts 계열로 지목된 122건 중 실제 contradicts는 1건이었다.)

**대상은 키워드에 가장 가까운 링크로 특정한다.** 같은 줄의 나머지 링크는 충돌 표현의 대상이라는 근거가 없어 Tier 2(`AMBIG→`)로 강등된다 — 버리지 않으니 진짜 대상이 강등됐다면 Tier 2에서 찾을 수 있다.

- Tier 1 (대상 지목됨, actionable): **4**
- Tier 2 (대상 불명/soft, review): **569**
- (억제됨) 이미 typed 엣지가 있어 제외: **240** · 동일 줄 비최근접으로 Tier 2 강등: **11**

## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)

### bone-regeneration

- `vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`  —[overturn · 결론 뒤집음]→  **`bone-regeneration-protocol-ladder`**
  - **근거 문장**: This is the key HEAD-TO-HEAD synthesis for choosing a horizontal ridge augmentation modality for the narrow ridge — GBR vs ridge-split (RS) vs osseodensification (OD) ridge expansion — ranking them by mean horizontal bone gain in one meta-analysis. It directly ties together the wiki's previously separate technique pages: the ridge-split case literature ([[wiki/bone-regeneration/simion-1992-jawbone
  - ▸ 출발(`vorovenci-2024-horizontal-ridge-augmentation-od-gbr-ridge-split-sr-ma`) 세줄: SR+MA(PRISMA, 17편 메타분석 21군; 환자 336명·임플란트 665개; 2017–2022): 수평 치조제 증대 3종 — 가이드골재생(Guided Bone Regeneration, GBR)·치조제분할(Ridge Split, RS)·골밀도화(Osseodensification, OD) — 최초 풀링 직접비교. 평균 수평 골증대: GBR 4.036 mm > RS 3.661 mm > OD 2.151 mm (P=0.002); GBR vs RS 차이 NS(P=0.09), 둘 다 OD보다 유의하게 
  - ▸ 대상(`bone-regeneration-protocol-ladder`) 세줄: 치조제 보존술 (Alveolar Ridge Preservation, ARP) 4축 결정 ladder 종합 — 자연 치유 흡수(수평 −3.79mm, 수직 −1.24~1.67mm, 6개월; 수평 우세), ARP 효과(수평 1.86–2.19mm 감소), 이식재 비교, 차폐막·연조직봉쇄 조합. 이식재 간 임상 차이는 미미(Bio-Oss ≈ 자가골); 표준 조합 = DBBM + 콜라겐 차폐막, 심미부위 높이 보존 최우수 = 유리치은이식(Free Gingival Graft, FGG); dPTFE 차폐막은 노


### oral-medicine

- `nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`  —[뒤집 · 뒤집음]→  **`tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva`**
  - **근거 문장**: 기존 위키에는 침(saliva)이 질병의 *결과물*(COVID 후유증)로만 나타난다 — [[oral-medicine/tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva]]. 이 JADA 리뷰는 침을 *진단 매체*로 뒤집는 관점(salivaomics·exosomics·liquid biopsy)을 도입해, 침샘 기능/구강건조 라인([[oral-medicine/poudel-2026-xerostomia-dental-treatment-outcomes-sr]])과 대비되는 "침의 진단적 활용" 축을 새로 연다. Wong 그룹(UCLA)의 salivaomics 프레임워크 원전으로, 향후 침 바이오마커 overview의 앵커.
  - ▸ 출발(`nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`) 세줄: 전문가 서술 리뷰(JADA 2023, Wong/UCLA 그룹) — 침 진단(saliva diagnostics)을 살리바오믹스(salivaomics)·침 엑소좀학(saliva exosomics)·침 액체생검(saliva liquid biopsy) 세 축으로 분류, 침·혈장 단백질체 20–30% 중첩으로 전신 바이오마커의 침샘 이송 가능성 지지. 전기화학 센서 EFIRM(Electric Field–Induced Release and Measurement)은 추출·증폭 없이 40–50 µL 침에서 폐암
  - ▸ 대상(`tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva`) 세줄: 내러티브 리뷰(약 90편 이상 연구, 코로나19 환자·완치자 총 6만5천여 명 종합) — 미각장애(ageusia/dysgeusia)와 침분비저하(xerostomia/hyposalivation) 등 구강 후유증의 지속 기간·유병률 종합. 미각장애는 완치 후 3주~12개월 추적에서 1~45%, 침분비저하는 2~40%에서 지속되고 서로 상관관계가 있으며; 지리적 구배(동아시아 3.8% vs 중동 20.6%)가 미각장애에서 뚜렷함. 타액선·미뢰의 ACE2/TRPV1 수용체 발현과 감염 유발 아연결핍이라는


### oral-microbiology

- `momeni-2024-intraspecies-interactions-streptococcus-mutans`  —[대비되는 · 대비]→  **`lueyar-2023-dynamic-interactions-between-candida-albicans`**
  - **근거 문장**: 기존 S. mutans 페이지들([[oral-microbiology/bowen-2011-streptococcus-mutans-glucosyltransferases]], [[oral-microbiology/klein-2012-mutans-protein-synthesis-mixed-species-biofilm]])은 단일 균주 또는 종간(interspecies) 상호작용에 집중했으나, 같은 종 내 여러 유전형(genotype) 간 상호작용이 우식원성에 미치는 영향은 공백이었다. 본 논문(Momeni 2024)은 임상 분리주 G09·G18의 co-culture가 biofilm 산도·구조·집락화를 상승시킴을 in vitro/in vivo로 보여, "다수 S. mutans 유전형 = ECC 위험인자"라는 역학 관찰의
  - ▸ 출발(`momeni-2024-intraspecies-interactions-streptococcus-mutans`) 세줄: 8년 종단 코호트에서 선정된 고위험 아동 1명의 환자 매칭 임상 S. mutans 두 유전형(G09·G18)을 대상으로 한 In vitro CLSM 바이오필름 + In vivo 초파리 집락화 연구 (+ 후향적 중첩 연관 분석, n=78). G09·G18 공동 배양 시 단독 배양 대비 9/10 아동 및 전체 집단에서 유의하게 낮은 바이오필름 pH(산도 증가), CLSM 세포 밀도·두께 약 2배 증가, in vivo 집락화 강화 — 각 균주는 서로 겹치지 않는 공간 영역 차지(G18: 평탄한 "law
  - ▸ 대상(`lueyar-2023-dynamic-interactions-between-candida-albicans`) 세줄: Zürich in-vitro 8종 상연골상 (supragingival) 바이오필름 모델 (3회·삼중, CFU + FISH/CLSM) — 개별 연쇄상구균 종이 *C. albicans*에 미치는 영향 분석. 연쇄상구균 종 다양성 증가 → *C. albicans* CFU 감소 (*S. gordonii* + *S. mutans* 최저, p<0.01); *S. mutans* + mitis군 단일종 → 균사형 (hypha) 유도, mitis 다종 공존 → 효모형 (yeast) 회귀. 구강 연쇄상구균 군집 복


### sinus-lift/lateral

- `sartori-2003-msfa-bio-oss-10year-case-report`  —[상충 · 상충]→  **`rogova-2025-histomorphometric-non-decalcified-bone-substitute-sr`**
  - **근거 문장**: - [[bone-regeneration/rogova-2025-histomorphometric-non-decalcified-bone-substitute-sr]] — histomorphometry 방법론 SR — 평가 방법 차이로 inter-study 결과 상충 가능.
  - ▸ 출발(`sartori-2003-msfa-bio-oss-10year-case-report`) 세줄: 단일 환자 증례보고: Bio-Oss 단독 상악동거상술 (Maxillary Sinus Floor Augmentation, MSFA) 후 8개월·2년·10년 시점 연속 트레핀 생검 (Trephine Biopsy) 조직형태계측 — 인체 장기 MSFA 리모델링 궤적을 기록한 매우 드문 연구. 골조직 (골수강 포함) 비율 29.8% → 69.7% → 86.7%로 단조 증가; Bio-Oss 입자 ~70% → ~30% → ~13%로 점진적 감소 — 10년에 걸친 완만하지만 진행적인 흡수 시사. Mordenfe
  - ▸ 대상(`rogova-2025-histomorphometric-non-decalcified-bone-substitute-sr`) 세줄: 방법론 체계적 문헌고찰(PCC 프레임워크, 118편, 2015–2024): 이식재를 사용한 골재생 비탈회 플라스틱 포매 조직형태계측 연구의 방법론 분포 지도 작성. 동물모델: rat > rabbit > sheep > dog > mini-pig; 주요 염색: toluidine blue; 가장 흔한 단일 평가지표: 신생골 형성률(NB%); 표준 부지표: 잔존 이식재(RG%)·입자 골유착률(OI%)·골임플란트 접촉률(BIC)·광화부착속도(Mineral Apposition Rate, MAR, calcei


## Tier 2 — 대상 식별 필요 / soft signal (review only)

- `achmadi-2025-intraoral-scanner-edentulous-accuracy-scoping` [digital-workflow] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: [역소급 작성 2026-07-05 — 원 인제스트(2026-05-18) 당시 동기 기록 없음. [[overviews/digital-workflow-decision-ladder]]에서 확인되는 현재 역할을 백필.] [[overviews/digital-workflow-decision-ladder]] 무치악 IOS 정확도 스펙트럼에서 유일하게 "기공실 스캐너가 IOS보다 우위"라는 반대축을 제공 — vankos-2026·singh-2025의 IOS 우호적 결과와 대비되는 근거로 배치됨.
  - ▸ 출발(`achmadi-2025-intraoral-scanner-edentulous-accuracy-scoping`) 세줄: 스코핑 리뷰 (BDJ Open 2025, PRISMA-ScR, Arksey & O'Malley 방법론): 무치악 악궁 IOS vs 기공실 스캐너 인상 정확도 비교; 312건 검색, 8편 포함. IOS는 무치악에서도 활용 가능하나, 편평하고 해부학적 표식이 없는 점막 능선이 특징점 매칭 및 스티칭 알고리즘을 방해해 정확도를 제한하며, 스캔 경로가 길어질수록 누적 오차가 증가한다. 기공실 스캐너(기존 인상 → 석고 모델 → 디지털화 간접법)가 완전 무치악에서 대체로 높은 정확도를 유지하며, 부분 무치

- `aucinaite-2025-naocl-chx-gutta-percha-cone-decontamination-sr` [endodontics] (HIGH-no-target, 'Conflicting finding' · 상충 결과)
  - **근거 문장**: - **Conflicting findings**: neither 5.25% NaOCl nor 2% CHX eliminated *E. faecalis* after 5 min in one study; another found no significant 2.5% NaOCl vs 2% CHX difference at 5 min — attributed to methodological/assessment differences.
  - ▸ 출발(`aucinaite-2025-naocl-chx-gutta-percha-cone-decontamination-sr`) 세줄: 줄1: NaOCl vs CHX의 거타퍼차(GP) cone chairside 소독 효과(E. faecalis, S. aureus, C. albicans, 0–10분)를 비교한 최초 PRISMA 체계적 문헌고찰(309편 스크리닝 → in vitro 7편 포함, INPLASY 등록). 줄2: 고농도 NaOCl(5.25%/6%)이 1–5분 내 세균을 가장 효과적으로 제거; CHX(cetrimide 병용 포함)는 Candida에 유망하고 GP 탄성 보존 장점; 7편 모두 중등도/높은 비뚤림 위험. 줄3: 

- `shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment` [endodontics] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: Contrary to concern about biomineralizing sealers being irretrievable, both AHB and Ceraseal were actually more removable than epoxy AH Plus; the supplementary XP-endo Finisher step added meaningful removal especially apically.
  - ▸ 출발(`shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment`) 세줄: 사람 하악 단근치(단일 타원형 근관) 36개(군당 12개)를 3주 경화 후 WaveOne Gold + XP-endo Finisher로 재치료하면서 마이크로-CT로 3D 충전물 제거량을 비교한 in-vitro 연구다. WaveOne Gold + XPF 후 충전 제거율이 AH Plus Bioceramic 94.8%, Ceraseal 92.5%, AH Plus Jet 87.1%였으며, 두 칼슘실리케이트 실러 모두 전체·치근단부 잔류량이 AH Plus Jet보다 유의하게 적었다(p<0.05); SEM/E

- `shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment` [endodontics] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refutes the worry that biomineralizing CSBSs are hard to retrieve: both removed **more** material than AH Plus.
  - ▸ 출발(`shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment`) 세줄: 사람 하악 단근치(단일 타원형 근관) 36개(군당 12개)를 3주 경화 후 WaveOne Gold + XP-endo Finisher로 재치료하면서 마이크로-CT로 3D 충전물 제거량을 비교한 in-vitro 연구다. WaveOne Gold + XPF 후 충전 제거율이 AH Plus Bioceramic 94.8%, Ceraseal 92.5%, AH Plus Jet 87.1%였으며, 두 칼슘실리케이트 실러 모두 전체·치근단부 잔류량이 AH Plus Jet보다 유의하게 적었다(p<0.05); SEM/E

- `abada-2025-obturation-techniques-post-obturation-pain-rct` [endodontics] (SOFT→song-2022-sealer-based-obturation-epoxy-calcium-silicate-rct, 'whereas' · 반면(대조))
  - **근거 문장**: - [[endodontics/song-2022-sealer-based-obturation-epoxy-calcium-silicate-rct]] — extends; Song found no pain/extrusion difference between calcium-silicate and AH Plus, whereas this RCT detects an AH Plus pain penalty.
  - ▸ 출발(`abada-2025-obturation-techniques-post-obturation-pain-rct`) 세줄: 줄1: 무증상 비가역적 치수염 하악 제1대구치 150개(5군×30)를 대상으로 CeraSeal(bioceramic) vs AH Plus(epoxy-resin)와 측방가압·연속파가압·단일콘 충전을 교차 비교한 전향적 CONSORT RCT (6/12/24/48/72시간 VAS 통증, 방사선 실러 일출 평가). 줄2: 모든 군에서 통증 낮음(VAS 0–1.4); 충전법 자체는 통증에 무영향(p=0.124); AH Plus가 CeraSeal보다 전체적으로 통증 유의 증가(p<0.001), 특히 연속파가압
  - ▸ 대상(`song-2022-sealer-based-obturation-epoxy-calcium-silicate-rct`) 세줄: 단일 기관 파일럿 RCT(등록 80개, 분석 71개 치아; 4개 실러군 각 n=20: AH Plus·ADseal[에폭시레진], CeraSeal·EndoSeal TCS[칼슘실리케이트]; 3개월 추적)로 단일콘 실러 기반 충전의 기포·압출·술후통증을 비교했다. 모든 평가 항목(기포·압출·VAS 통증·타진/촉진·치근단 방사선 소실 회복)에서 칼슘실리케이트와 에폭시레진 실러 간 통계적 유의차가 없었고(전부 p>0.05), 충전 품질 차이는 제품 특성·근관 해부학적 요인에 기인했다. 이 파일럿 RCT는 3

- `abada-2025-obturation-techniques-post-obturation-pain-rct` [endodontics] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[endodontics/shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment]] — retreatment/retrievability counterpoint to the obturation choice studied here.
  - ▸ 출발(`abada-2025-obturation-techniques-post-obturation-pain-rct`) 세줄: 줄1: 무증상 비가역적 치수염 하악 제1대구치 150개(5군×30)를 대상으로 CeraSeal(bioceramic) vs AH Plus(epoxy-resin)와 측방가압·연속파가압·단일콘 충전을 교차 비교한 전향적 CONSORT RCT (6/12/24/48/72시간 VAS 통증, 방사선 실러 일출 평가). 줄2: 모든 군에서 통증 낮음(VAS 0–1.4); 충전법 자체는 통증에 무영향(p=0.124); AH Plus가 CeraSeal보다 전체적으로 통증 유의 증가(p<0.001), 특히 연속파가압

- `de-almeida-junior-2024-cytotoxicity-bioactivity-ceraseal-bioroot` [endodontics] (SOFT→zamparini-2023-premixed-calcium-silicate-carrier-based-2year, 'Whereas' · 반면(대조))
  - **근거 문장**: Seeds the wiki's first CeraSeal / bioceramic-sealer biocompatibility cluster, complementing the clinical CeraSeal cohort and obturation papers already held ([[endodontics/spinelli-2024-three-year-single-cone-ceraseal-cohort]], [[endodontics/zamparini-2023-premixed-calcium-silicate-carrier-based-2year]]). Whereas those track clinical/survival outcomes, this paper supplies the cell-level (MC3T3 pre-
  - ▸ 출발(`de-almeida-junior-2024-cytotoxicity-bioactivity-ceraseal-bioroot`) 세줄: 사람 전조골세포(MC3T3) ISO 10993-5 in-vitro 연구로 CeraSeal·BioRoot RCS·AH Plus를 24시간/48시간 세포독성 및 28일 광화결절로 비교했다. 48시간 시점에서 세 실러 모두 비독성(생존율 >90%)이었으며, AH Plus만 Tnf(TNF-α)를 상향 발현, CeraSeal·BioRoot는 Ptgs2·Dmp1을 상향 발현하는 차별적 유전자 발현 패턴을 보였다. 유전자 발현 차이에도 불구하고 28일 광화 결절 형성에는 군간 차이가 없어 '비독성 ≠ 골유도성
  - ▸ 대상(`zamparini-2023-premixed-calcium-silicate-carrier-based-2year`) 세줄: 전향 코호트(볼로냐 마스터 과정, 24개월 분석 89건) — 프리믹스 Ceraseal 칼슘실리케이트 실러를 Thermafil warm carrier-based 충전에 적용, AH Plus 대조군과 술자 수준 무작위 배정 비교. 치유율 동등(91.1% vs 88.6%, p=0.624), 전체 생존율 97.8%; Ceraseal은 근단 실러 압출이 유의하게 낮고(13.3% vs 25%), 압출된 Ceraseal 6건 중 3건은 24개월 내 방사선학적으로 소실됨. 치유 실패 예측인자는 술전 PAI>3·

- `de-almeida-junior-2024-cytotoxicity-bioactivity-ceraseal-bioroot` [endodontics] (AMBIG→spinelli-2024-three-year-single-cone-ceraseal-cohort, 'Whereas' · 반면(대조))
  - **근거 문장**: Seeds the wiki's first CeraSeal / bioceramic-sealer biocompatibility cluster, complementing the clinical CeraSeal cohort and obturation papers already held ([[endodontics/spinelli-2024-three-year-single-cone-ceraseal-cohort]], [[endodontics/zamparini-2023-premixed-calcium-silicate-carrier-based-2year]]). Whereas those track clinical/survival outcomes, this paper supplies the cell-level (MC3T3 pre-
  - ▸ 출발(`de-almeida-junior-2024-cytotoxicity-bioactivity-ceraseal-bioroot`) 세줄: 사람 전조골세포(MC3T3) ISO 10993-5 in-vitro 연구로 CeraSeal·BioRoot RCS·AH Plus를 24시간/48시간 세포독성 및 28일 광화결절로 비교했다. 48시간 시점에서 세 실러 모두 비독성(생존율 >90%)이었으며, AH Plus만 Tnf(TNF-α)를 상향 발현, CeraSeal·BioRoot는 Ptgs2·Dmp1을 상향 발현하는 차별적 유전자 발현 패턴을 보였다. 유전자 발현 차이에도 불구하고 28일 광화 결절 형성에는 군간 차이가 없어 '비독성 ≠ 골유도성

- `muehlemann-2025-cost-efficiency-digital-conventional-denture` [complete-denture] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[complete-denture/jafarpour-2024-cadcam-versus-traditional-complete-dentures]] — earlier SR+MA reported CAD/CAM RCDs as significantly cheaper (lower laboratory and total costs); this paper's cost-efficiency meta-analysis (accounting for patient outcomes and rigorous currency harmonization) contradicts that cost-only conclusion, finding no significant cost difference.
  - ▸ 출발(`muehlemann-2025-cost-efficiency-digital-conventional-denture`) 세줄: SR+MA (5편, n=184명): 디지털(CAD/CAM 밀링·3D프린팅) 대 전통(압축성형) 총의치(완전의치) 워크플로우의 비용 및 내원횟수를 비교. 기공비(MD −239.77달러, p=0.106), 임상비(MD +74.39달러, p=0.451), 총비용(MD −357.76달러, p=0.258), 내원횟수(MD −1.47, p=0.351) 모두 통계적으로 유의한 차이 없음; 술자 숙련도(학생 대 전문의)가 비용 변동의 주요 결정 인자(p<0.0001). 디지털 워크플로우의 비용 우위를 당연하게 

- `muehlemann-2025-cost-efficiency-digital-conventional-denture` [complete-denture] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: 사용자가 CAD/CAM 치과 기공(dental laboratory) 관련 논문을 요청하여 인제스트. 기존 [[wiki/complete-denture/jafarpour-2024-cadcam-versus-traditional-complete-dentures]]는 CAD/CAM 총의치가 기공·총비용에서 유의하게 저렴하다고 보고했으나, 본 SR+MA는 비용-효율성(cost-efficiency) 메타분석 방법론으로 재검증한 결과 유의한 차이가 없음을 보여 상반된 결론을 제공한다.
  - ▸ 출발(`muehlemann-2025-cost-efficiency-digital-conventional-denture`) 세줄: SR+MA (5편, n=184명): 디지털(CAD/CAM 밀링·3D프린팅) 대 전통(압축성형) 총의치(완전의치) 워크플로우의 비용 및 내원횟수를 비교. 기공비(MD −239.77달러, p=0.106), 임상비(MD +74.39달러, p=0.451), 총비용(MD −357.76달러, p=0.258), 내원횟수(MD −1.47, p=0.351) 모두 통계적으로 유의한 차이 없음; 술자 숙련도(학생 대 전문의)가 비용 변동의 주요 결정 인자(p<0.0001). 디지털 워크플로우의 비용 우위를 당연하게 

- `yeung-2023-functional-neuroplasticity-denture-rehabilitation-fmri` [complete-denture] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 4. Task-dependent contradiction: gum-chewing can show overdentures with LOWER activation than complete dentures — opposite direction to the clenching hierarchy — cautioning against reading "more activation = better."
  - ▸ 출발(`yeung-2023-functional-neuroplasticity-denture-rehabilitation-fmri`) 세줄: 체계적 문헌고찰 (PICO + 3개 DB 검색 + 비뚤림평가, 메타분석 불가) — 9편의 기능적 자기공명영상 (functional MRI, fMRI) 연구(각 n≈4–20; 8편 완전무치악, 1편 부분무치악)에서 총의치·임플란트지지 피개의치·임플란트지지 고정성의치가 과제유발 뇌활성을 어떻게 바꾸는지 종합. 이악물기 (Jaw-clenching) 시 임플란트지지 고정성의치가 일차감각운동피질(중심전회 PreCG·중심후회 PostCG)에서 가장 높은 활성과 연관; 새 총의치는 일시적 활성 증가 후 약 3

- `derbishi-2026-coronectomy-versus-total-extraction-third` [oral-surgery] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: This 2026 meta-analysis is the methodologically strongest coronectomy-vs-total-extraction synthesis to date. Using Peto odds ratios (appropriate for the rare-event IAN injury), HKSJ-adjusted random-effects CIs, GRADE, and trial sequential analysis, it shows coronectomy cuts IAN injury roughly fourfold (Peto OR 0.23) and — critically — TSA confirms the evidence is *conclusive*, not just statistical
  - ▸ 출발(`derbishi-2026-coronectomy-versus-total-extraction-third`) 세줄: SR+MA (8편 — RCT 3편 + 코호트 5편, 1,488치): 하악 제3대구치에서 치관절제술(coronectomy) 대 완전 발치를 GRADE·TSA까지 적용한 방법론적으로 가장 강력한 합성 연구. 치관절제술이 하치조신경(IAN) 손상을 Peto OR 0.23(95% CI 0.13–0.39, p<0.0001, TSA 확정적)으로 약 4배 감소; 건성치조염·감염은 유의한 차이 없음. 잔존 치근 회수를 위한 재수술률은 1.2%에 불과해, 치근 이동은 대개 양성 경과로 임상적 우려가 낮다.

- `derbishi-2026-coronectomy-versus-total-extraction-third` [oral-surgery] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: [[wiki/oral-surgery/cervera-espert-2016-coronectomy-mandibular-third-molar-sr]] established the IAN-protective effect but predates modern meta-analytic rigor (Peto OR for rare events, GRADE, trial sequential analysis). This 2026 SR+MA reinforces the anchor with a conclusive effect estimate (Peto OR 0.23 for IAN injury, TSA-confirmed) and modern certainty grading, strengthening rather than overturn
  - ▸ 출발(`derbishi-2026-coronectomy-versus-total-extraction-third`) 세줄: SR+MA (8편 — RCT 3편 + 코호트 5편, 1,488치): 하악 제3대구치에서 치관절제술(coronectomy) 대 완전 발치를 GRADE·TSA까지 적용한 방법론적으로 가장 강력한 합성 연구. 치관절제술이 하치조신경(IAN) 손상을 Peto OR 0.23(95% CI 0.13–0.39, p<0.0001, TSA 확정적)으로 약 4배 감소; 건성치조염·감염은 유의한 차이 없음. 잔존 치근 회수를 위한 재수술률은 1.2%에 불과해, 치근 이동은 대개 양성 경과로 임상적 우려가 낮다.

- `bodner-2012-cutaneous-sinus-tract-dental` [oral-surgery] (SOFT→gargava-2022-deep-neck-space-infection-150-cases, 'whereas' · 반면(대조))
  - **근거 문장**: - [[oral-surgery/gargava-2022-deep-neck-space-infection-150-cases]] — Both address surgical presentations of odontogenic infection; this paper covers the chronic cutaneous-draining variant whereas Gargava covers acute deep-neck-space spread.
  - ▸ 출발(`bodner-2012-cutaneous-sinus-tract-dental`) 세줄: 후향적 증례군(소아 28명, 평균 10.25세, 범위 4–16세; 남:녀 1:1.74) — 치성 피부누공(Cutaneous Sinus Tract, CST)의 가장 흔한 양상은 우식이 있는 하악 제1대구치에서 기원하여 하악·하악하부 피부에 나타남. 평균 진단 지연 6.5개월(범위 0.3–12개월) — CST가 피부과적 병변으로 반복 오진되어 발치 부위 치료가 늦어짐; 원인치 근관치료 또는 발치 후 피부 누공은 신속 치유. 흉터 교정술이 8/28명(29%)에게 필요했으며, 이는 병변 기간이 긴 증례에
  - ▸ 대상(`gargava-2022-deep-neck-space-infection-150-cases`) 세줄: 인도 3차 병원 전향적 관찰 연구(n=150): 심경부감염(Deep Neck Space Infection, DNSI)의 원인·균학·치료·결과 기술. 원인은 치성(42.66%) 1위, 루드비히 앙기나(Ludwig's Angina)가 가장 흔한 침범 공간(24.66%), 주요 원인균 연쇄구균(31.33%), 절개배농(I&D) 38%, 응급기관절개술 일부 시행, 종격동염이 가장 심각한 합병증. 심경부감염은 기도 폐쇄·종격동염 위험을 지닌 응급 상황 — 치성 원인이 가장 예방 가능하며, 당뇨 환자는 그람

- `ali-2023-conventional-minimally-invasive-veneers-sr` [veneers] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: MPVs demonstrated equal or superior survival rates and longer mean success periods versus CVs, contradicting the review's hypothesis of CV superiority; ultra-thin contact-lens type feldspathic porcelain (0.2–0.3 mm) showed favorable outcomes across most dimensions.
  - ▸ 출발(`ali-2023-conventional-minimally-invasive-veneers-sr`) 세줄: PRISMA 체계적 문헌고찰 (8개 데이터베이스, 4편 비교 연구): 통상 비니어(Conventional Veneer, CV; 0.3–1.0 mm)와 최소/무삭제 비니어(Minimally/No-Preparation Veneer, MPV; 0.2–0.5 mm)를 심미성·수명·치주 건강·미세누출·변연적합도·색 안정성 6개 차원에서 비교. 초박형 contact-lens형 장석질 도재 MPV(0.2–0.3 mm)가 생존율과 성공 기간에서 CV와 동등 이상 — 기존 CV 우위 가설 반박; 미세누출·변연적합

- `ali-2023-conventional-minimally-invasive-veneers-sr` [veneers] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 초박형 contact-lens형 장석질 도재 MPV(0.2–0.3 mm)가 생존율과 성공 기간에서 CV와 동등 이상 — 기존 CV 우위 가설 반박; 미세누출·변연적합도·색 안정성은 술식과 재료에 따라 차이.
  - ▸ 출발(`ali-2023-conventional-minimally-invasive-veneers-sr`) 세줄: PRISMA 체계적 문헌고찰 (8개 데이터베이스, 4편 비교 연구): 통상 비니어(Conventional Veneer, CV; 0.3–1.0 mm)와 최소/무삭제 비니어(Minimally/No-Preparation Veneer, MPV; 0.2–0.5 mm)를 심미성·수명·치주 건강·미세누출·변연적합도·색 안정성 6개 차원에서 비교. 초박형 contact-lens형 장석질 도재 MPV(0.2–0.3 mm)가 생존율과 성공 기간에서 CV와 동등 이상 — 기존 CV 우위 가설 반박; 미세누출·변연적합

- `ali-2023-conventional-minimally-invasive-veneers-sr` [veneers] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refuted the prior assumption of CV superiority: MPVs showed equal or better outcomes in survival and longevity
  - ▸ 출발(`ali-2023-conventional-minimally-invasive-veneers-sr`) 세줄: PRISMA 체계적 문헌고찰 (8개 데이터베이스, 4편 비교 연구): 통상 비니어(Conventional Veneer, CV; 0.3–1.0 mm)와 최소/무삭제 비니어(Minimally/No-Preparation Veneer, MPV; 0.2–0.5 mm)를 심미성·수명·치주 건강·미세누출·변연적합도·색 안정성 6개 차원에서 비교. 초박형 contact-lens형 장석질 도재 MPV(0.2–0.3 mm)가 생존율과 성공 기간에서 CV와 동등 이상 — 기존 CV 우위 가설 반박; 미세누출·변연적합

- `komine-2024-clinical-performance-laminate-veneers-review` [veneers] (HIGH-no-target, 'conflicting result' · 상충 결과)
  - **근거 문장**: - **Vitality**: Nonvital teeth have higher failure risk per Beier; conflicting results in other studies
  - ▸ 출발(`komine-2024-clinical-performance-laminate-veneers-review`) 세줄: 내러티브 리뷰 (일본 Nihon 대학; 2000–2023년 4월, ≥3년 추적 55편): 장석질·LRG·LDS·간접 레진 라미네이트 비니어(Laminate Veneer, LV) 생존율·합병증·수정 가능 위험인자 종합. 시간 경과에 따른 생존율 감소: ≤5년 95–100%, ≤10년 83–100%, >10년 73–95%; 즉시 상아질 실링(Immediate Dentin Sealing, IDS) 적용 시 11년 생존율 81.8% → 96.4%; 이갈이(Bruxism) + 교합장치 없이 8년 63.9%

- `lim-2023-resin-composite-laminate-veneer-survival-sr-ma` [veneers] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 레진 복합재 라미네이트 비니어의 생존율에 대한 체계적 SR+MA가 부재하여 세라믹 비니어와의 비교 근거를 보완하기 위해 인제스트. [[veneers/klein-2025-ceramic-laminate-veneer-survival-complications-sr-ma]]에서 다루는 세라믹 비니어 생존율과 직접 대비되는 레진 계열 근거를 제공한다.
  - ▸ 출발(`lim-2023-resin-composite-laminate-veneer-survival-sr-ma`) 세줄: PROSPERO 등록 SR+MA (CRD42022336857; 827건 검색, 7편 포함 — RCT 3 + 코호트 4, 영구치, ≥2년 추적 24–97개월): 레진 복합재 라미네이트 비니어(Resin Composite Laminate Veneer) 생존율·합병증 평가. RCT 합산 생존율 88% (95% CI 81–94%); 직접법(Direct) 91% vs 간접법(Indirect) 84%; 표면거칠기·색 불일치·변연 변색이 가장 흔한 합병증(대부분 수리 가능); I²=50.5% 중등도 이질성. 

- `nelson-2011-text-vs-voice-reminder-pediatric-dental-rct` [practice-management] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: This randomized controlled trial in the pediatric dentistry clinic at the University of Washington tested whether **SMS text messages** are as effective as **automated voice messages** for reducing appointment no-shows. Of 543 caregiver/child dyads invited, **318 pairs (59% response)** enrolled and were randomized to receive either an SMS text reminder (n=158) or a voice-message reminder (control,
  - ▸ 출발(`nelson-2011-text-vs-voice-reminder-pediatric-dental-rct`) 세줄: 소아치과 RCT(n=318 보호자/아동 쌍, 워싱턴대 소아치과): SMS 문자 vs 자동 음성 메시지 예약 알림을 무작위 채널 배정으로 비교. 음성 알림군의 미내원율(8.2%)이 SMS군(17.7%)보다 유의하게 낮았고(보정 OR 2.12, p=.04), 보호자 연령이 낮을수록 미내원 위험도 유의하게 증가(p=.02). 채널을 무작위 배정했기 때문에 환자가 선호 채널을 직접 선택하는 실제 진료환경에서는 SMS 열세 결과가 재현되지 않을 수 있어 일반화에 주의가 필요.

- `nelson-2011-text-vs-voice-reminder-pediatric-dental-rct` [practice-management] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: The result is a useful counterpoint to reminder-vs-none studies: here the comparison is **channel vs channel**, and channel choice clearly mattered. The authors flag a key caveat — patients were *randomly assigned* a reminder channel, so the SMS disadvantage may not hold when patients **self-select** their preferred channel.
  - ▸ 출발(`nelson-2011-text-vs-voice-reminder-pediatric-dental-rct`) 세줄: 소아치과 RCT(n=318 보호자/아동 쌍, 워싱턴대 소아치과): SMS 문자 vs 자동 음성 메시지 예약 알림을 무작위 채널 배정으로 비교. 음성 알림군의 미내원율(8.2%)이 SMS군(17.7%)보다 유의하게 낮았고(보정 OR 2.12, p=.04), 보호자 연령이 낮을수록 미내원 위험도 유의하게 증가(p=.02). 채널을 무작위 배정했기 때문에 환자가 선호 채널을 직접 선택하는 실제 진료환경에서는 SMS 열세 결과가 재현되지 않을 수 있어 일반화에 주의가 필요.

- `nelson-2011-text-vs-voice-reminder-pediatric-dental-rct` [practice-management] (HIGH-no-target, 'Counterpoint' · 반대 논점)
  - **근거 문장**: Counterpoint reminder RCT for the no-show overview: in a university pediatric dental clinic, **voice messages beat SMS text** at reducing no-shows — the opposite-channel result qualifies the blanket "send a reminder" recommendation by showing channel choice (and population) matters. Refines [[overviews/dental-appointment-no-show-overview]] by adding a head-to-head channel comparison rather than re
  - ▸ 출발(`nelson-2011-text-vs-voice-reminder-pediatric-dental-rct`) 세줄: 소아치과 RCT(n=318 보호자/아동 쌍, 워싱턴대 소아치과): SMS 문자 vs 자동 음성 메시지 예약 알림을 무작위 채널 배정으로 비교. 음성 알림군의 미내원율(8.2%)이 SMS군(17.7%)보다 유의하게 낮았고(보정 OR 2.12, p=.04), 보호자 연령이 낮을수록 미내원 위험도 유의하게 증가(p=.02). 채널을 무작위 배정했기 때문에 환자가 선호 채널을 직접 선택하는 실제 진료환경에서는 SMS 열세 결과가 재현되지 않을 수 있어 일반화에 주의가 필요.

- `team-feedback-system-johari` [practice-management] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: | 저격성·감정성 답변 | 공개 석상에서 절대 언급 금지. 반박도 언급이다. 무시가 유일한 정답 |
  - ▸ 출발(`team-feedback-system-johari`) 세줄: 위생사 약 20명(실장·파트 혼합)을 위한, 조하리의 창에 기반한 3단계 팀 피드백 시스템 운영 매뉴얼 — Phase 1 상향 익명 → Phase 2 1:1 실명 → Phase 3 수평. 피드백은 맹점을, 자기개방은 숨긴 창을 줄인다는 역학을 적용 — 리더(원장)의 자기개방과 익명 상향 피드백에서 출발해 실장 1:1 실명 피드백을 거쳐 파트 단위 수평 피드백으로 확산. 핵심 설계 원칙 — 리더가 먼저 받는다, 성격이 아니라 행동, 루프를 닫는다(수집→선별→변경 공표→실행), 수직은 익명·수평은 실

- `garcia-2023-teledentistry-acceptability-latino-rural-virginia` [practice-management] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: Contrary to prior positive-attitude literature, 57.1% of participants reported no interest in teledentistry even if available; only household income >$24,000 (p=.04) and lacking dental insurance (p=.01) were significantly associated with acceptability; non-receptive respondents were disproportionately Spanish-speaking (61.5%) and foreign-born (63.5%).
  - ▸ 출발(`garcia-2023-teledentistry-acceptability-latino-rural-virginia`) 세줄: 단면 REDCap 설문 (N=91명; 버지니아 남서부 농촌 14개 ZIP코드의 라티노 성인, 2020년 5월~2021년 2월; COVID-19 팬데믹 중): 구강건강 취약 집단에서 원격치의학(teledentistry) 수용성을 카이제곱 이변량 분석으로 평가. 선행 연구의 긍정적 태도 결과와 달리 57.1%가 원격치의학에 관심 없다고 응답; 가구소득 >$24,000(p=.04)과 치과보험 미보유(p=.01)만 수용성과 유의 연관; 비수용자는 스페인어 사용(61.5%)·외국 태생(63.5%) 비율 높

- `garcia-2023-teledentistry-acceptability-latino-rural-virginia` [practice-management] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: Contrary to prior literature reporting positive pre-experience attitudes toward telehealth among Latinos and rural residents, **57.1% reported no interest** in video/internet dental consultations even if available. In bivariate (chi-squared) analysis, only two factors were significantly associated with acceptability: **household income >$24,000 (p=.04)** and — counter-intuitively — **not having de
  - ▸ 출발(`garcia-2023-teledentistry-acceptability-latino-rural-virginia`) 세줄: 단면 REDCap 설문 (N=91명; 버지니아 남서부 농촌 14개 ZIP코드의 라티노 성인, 2020년 5월~2021년 2월; COVID-19 팬데믹 중): 구강건강 취약 집단에서 원격치의학(teledentistry) 수용성을 카이제곱 이변량 분석으로 평가. 선행 연구의 긍정적 태도 결과와 달리 57.1%가 원격치의학에 관심 없다고 응답; 가구소득 >$24,000(p=.04)과 치과보험 미보유(p=.01)만 수용성과 유의 연관; 비수용자는 스페인어 사용(61.5%)·외국 태생(63.5%) 비율 높

- `silva-2013-occlusal-factors-nccl-systematic-review` [nccl] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[nccl/duangthip-2017-occlusal-stress-nccl-abfraction-sr]] — contradicts (lab-weighted SR finding 81% association)
  - ▸ 출발(`silva-2013-occlusal-factors-nccl-systematic-review`) 세줄: 6개 DB 체계적 문헌고찰(1082편 → 9편: 단면 6 + 환자대조 2 + 임상시험 1; Kappa 0.8): 성인 NCCL에서 교합위험인자(ORF: 편심위 간섭·교합력·조기접촉·유도 유형·편심위)의 역할 평가. 연구 대부분이 NCCL-교합 무연관; 단 3편만 특정 변수(교합접촉면적·우측 견치유도·중심위 조기접촉·작업측 접촉)에서 유의(p<0.05); 높은 이질성으로 풀링 불가. 임상적 의미: 임상근거는 교합을 NCCL 원인으로 강하게 지지하지 않음; 표준화된 교합 측정방법 부재가 근거 합성의 

- `duangthip-2017-occlusal-stress-nccl-abfraction-sr` [nccl] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[nccl/senna-2012-nccl-occlusion-systematic-review]] — contradicts (clinical SR, no conclusion)
  - ▸ 출발(`duangthip-2017-occlusal-stress-nccl-abfraction-sr`) 세줄: PubMed·Web of Science·EMBASE 체계적 문헌고찰("abfraction" 단일 키워드; 영어; 372편 → 69편: 임상 31 + 실험실 38): 교합응력이 NCCL 형성 기전인지를 평가. 56/69편(81%)이 교합응력-NCCL 연관 보고; 실험실 연구 24/38편(FEA 위주)이 치경부 응력 집중 확인; 그러나 응력을 NCCL 단독 원인으로 입증한 임상연구는 전무. abfraction에 가장 우호적인 SR이나, 81% 수치는 FEA 등 실험실 연구 편중·단일 키워드 검색·병변

- `duangthip-2017-occlusal-stress-nccl-abfraction-sr` [nccl] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[nccl/silva-2013-occlusal-factors-nccl-systematic-review]] — contradicts (clinical SR, majority null)
  - ▸ 출발(`duangthip-2017-occlusal-stress-nccl-abfraction-sr`) 세줄: PubMed·Web of Science·EMBASE 체계적 문헌고찰("abfraction" 단일 키워드; 영어; 372편 → 69편: 임상 31 + 실험실 38): 교합응력이 NCCL 형성 기전인지를 평가. 56/69편(81%)이 교합응력-NCCL 연관 보고; 실험실 연구 24/38편(FEA 위주)이 치경부 응력 집중 확인; 그러나 응력을 NCCL 단독 원인으로 입증한 임상연구는 전무. abfraction에 가장 우호적인 SR이나, 81% 수치는 FEA 등 실험실 연구 편중·단일 키워드 검색·병변

- `dioguardi-2024-abfraction-theory-controversy-scoping-review` [nccl] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: The 6 included studies provide insufficient evidence to confirm or refute occlusal-load aetiology; some suggestive clues exist but Duangthip 2017's pro-abfraction 81% figure is criticized as lab/FEA-weighted and unable to isolate true abfraction from erosive/abrasive lesions.
  - ▸ 출발(`dioguardi-2024-abfraction-theory-controversy-scoping-review`) 세줄: PRISMA-ScR 등록 scoping review(INPLASY 프로토콜; PubMed+Scopus; 1449편 → 6편 포함; ROBINS-I 비뚤림 평가): 교합부하가 abfraction 병변을 유발하는가를 평가. 6편의 포함 연구는 교합부하의 병인 역할을 확정하거나 반박하기에 불충분 — Duangthip 2017의 81% 연관 결과는 FEA 등 실험실 연구 편중, abfraction-erosion/abrasion 미분리 방법론 문제로 비판. abfraction 논쟁에 대한 가장 엄밀한 방법

- `dioguardi-2024-abfraction-theory-controversy-scoping-review` [nccl] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 6편의 포함 연구는 교합부하의 병인 역할을 확정하거나 반박하기에 불충분 — Duangthip 2017의 81% 연관 결과는 FEA 등 실험실 연구 편중, abfraction-erosion/abrasion 미분리 방법론 문제로 비판.
  - ▸ 출발(`dioguardi-2024-abfraction-theory-controversy-scoping-review`) 세줄: PRISMA-ScR 등록 scoping review(INPLASY 프로토콜; PubMed+Scopus; 1449편 → 6편 포함; ROBINS-I 비뚤림 평가): 교합부하가 abfraction 병변을 유발하는가를 평가. 6편의 포함 연구는 교합부하의 병인 역할을 확정하거나 반박하기에 불충분 — Duangthip 2017의 81% 연관 결과는 FEA 등 실험실 연구 편중, abfraction-erosion/abrasion 미분리 방법론 문제로 비판. abfraction 논쟁에 대한 가장 엄밀한 방법

- `dioguardi-2024-abfraction-theory-controversy-scoping-review` [nccl] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: This registered scoping review (PRISMA-ScR, INPLASY protocol, ROBINS-I bias assessment) is the most methodologically rigorous appraisal of the abfraction controversy to date. Searching PubMed and Scopus for "abfraction" AND "NCCL," the authors screened 1449 articles and included only 6 that correlated NCCL progression with applied forces. Their analysis found that these studies do not provide suff
  - ▸ 출발(`dioguardi-2024-abfraction-theory-controversy-scoping-review`) 세줄: PRISMA-ScR 등록 scoping review(INPLASY 프로토콜; PubMed+Scopus; 1449편 → 6편 포함; ROBINS-I 비뚤림 평가): 교합부하가 abfraction 병변을 유발하는가를 평가. 6편의 포함 연구는 교합부하의 병인 역할을 확정하거나 반박하기에 불충분 — Duangthip 2017의 81% 연관 결과는 FEA 등 실험실 연구 편중, abfraction-erosion/abrasion 미분리 방법론 문제로 비판. abfraction 논쟁에 대한 가장 엄밀한 방법

- `dioguardi-2024-abfraction-theory-controversy-scoping-review` [nccl] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: 6 included studies; insufficient evidence to confirm or refute occlusal-load aetiology of abfraction. NCCL prevalence framed at ~10-40% of adults over 30, premolars predominant. Calls for prospective longitudinal designs.
  - ▸ 출발(`dioguardi-2024-abfraction-theory-controversy-scoping-review`) 세줄: PRISMA-ScR 등록 scoping review(INPLASY 프로토콜; PubMed+Scopus; 1449편 → 6편 포함; ROBINS-I 비뚤림 평가): 교합부하가 abfraction 병변을 유발하는가를 평가. 6편의 포함 연구는 교합부하의 병인 역할을 확정하거나 반박하기에 불충분 — Duangthip 2017의 81% 연관 결과는 FEA 등 실험실 연구 편중, abfraction-erosion/abrasion 미분리 방법론 문제로 비판. abfraction 논쟁에 대한 가장 엄밀한 방법

- `dioguardi-2024-abfraction-theory-controversy-scoping-review` [nccl] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[nccl/duangthip-2017-occlusal-stress-nccl-abfraction-sr]] — refines/contradicts (re-analyzes and critiques its pro-abfraction conclusion)
  - ▸ 출발(`dioguardi-2024-abfraction-theory-controversy-scoping-review`) 세줄: PRISMA-ScR 등록 scoping review(INPLASY 프로토콜; PubMed+Scopus; 1449편 → 6편 포함; ROBINS-I 비뚤림 평가): 교합부하가 abfraction 병변을 유발하는가를 평가. 6편의 포함 연구는 교합부하의 병인 역할을 확정하거나 반박하기에 불충분 — Duangthip 2017의 81% 연관 결과는 FEA 등 실험실 연구 편중, abfraction-erosion/abrasion 미분리 방법론 문제로 비판. abfraction 논쟁에 대한 가장 엄밀한 방법

- `worawongvasu-2021-nccl-sem-characterization` [nccl] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[nccl/nascimento-2016-abfraction-etiology-diagnosis-treatment]] — contradicts (offers ultrastructural support where Nascimento calls abfraction unproven)
  - ▸ 출발(`worawongvasu-2021-nccl-sem-characterization`) 세줄: NCCL을 가진 소구치 발치치 10개를 JEOL JSM-6480 LV SEM(x40–x20,000)으로 검사한 ex vivo 서술적 연구 — 환자당 치아 1개, 다양한 형태(오목형·쐐기형·불규칙형 포함). 10개 중 4개에서 파절선·파절면 등 abfraction(교합 미세파절)에 부합하는 초미세구조 소견; 나머지 6개는 선형 긁힘(abrasion)과 상아세관 노출·불량고정 콜라겐섬유(erosion) 소견 — 다인성 병인 지지. 소규모 서술 연구로 인과관계를 확립하기 어렵고, abfraction을 

- `senna-2012-nccl-occlusion-systematic-review` [nccl] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Clinical implication: the NCCL–occlusion hypothesis is methodologically weak, not clearly confirmed or refuted — the null finding of this SR (and the parallel Silva 2013 SR) contrasts with Duangthip 2017's lab-weighted 81% association, anchoring the "inconclusive" clinical position.
  - ▸ 출발(`senna-2012-nccl-occlusion-systematic-review`) 세줄: NCCL-교합 연관 임상연구 체계적 문헌고찰(MEDLINE; 286편 → 28편: 전향 3 + 단면 25) — 교합을 NCCL 병인인자로 평가한 임상연구만 다룬 최초 SR. 연구설계·진단기준·교합변수·분석방법의 극심한 이질성과 비맹검 검사자 편향으로 교합의 NCCL 병인 역할에 대한 결론 도출 불가; 메타분석 불가. 임상적 의미: NCCL-교합 가설은 방법론적으로 취약 — 이 SR과 Silva 2013의 null 결과는 실험실 연구 편중 Duangthip 2017의 81% 연관과 대비되어 "임상적

- `senna-2012-nccl-occlusion-systematic-review` [nccl] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[nccl/duangthip-2017-occlusal-stress-nccl-abfraction-sr]] — contradicts (later SR reporting 81% of studies found an association)
  - ▸ 출발(`senna-2012-nccl-occlusion-systematic-review`) 세줄: NCCL-교합 연관 임상연구 체계적 문헌고찰(MEDLINE; 286편 → 28편: 전향 3 + 단면 25) — 교합을 NCCL 병인인자로 평가한 임상연구만 다룬 최초 SR. 연구설계·진단기준·교합변수·분석방법의 극심한 이질성과 비맹검 검사자 편향으로 교합의 NCCL 병인 역할에 대한 결론 도출 불가; 메타분석 불가. 임상적 의미: NCCL-교합 가설은 방법론적으로 취약 — 이 SR과 Silva 2013의 null 결과는 실험실 연구 편중 Duangthip 2017의 81% 연관과 대비되어 "임상적

- `wang-2019-fiber-posts-vs-metal-posts-severely-damaged` [post-and-core] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: GRADE 고급 수준의 생존 이점 (RR 0.57 = 파이버 사용 시 실패 위험 약 43% 감소)은 심한 손상 ETT에 대한 가장 방법론적으로 엄격한 포스트 재료 비교이며 — 강성 금속포스트가 손상된 치아의 치근파절을 더 잘 방지한다는 기존 우려를 반박한다.
  - ▸ 출발(`wang-2019-fiber-posts-vs-metal-posts-severely-damaged`) 세줄: Cochrane 방법론 SR+MA (RCT 한정, 추적 ≥3년; 4편, 모두 낮은 비뚤림 위험, 3–7년): 잔존 치질 ≤2벽의 심한 손상 근관치료치 — 가장 고위험 수복 시나리오 — 를 대상으로 파이버 vs 금속 포스트 비교. 파이버포스트 생존율이 금속포스트보다 유의하게 높음 (RR 0.57, 95% CI 0.33–0.97, P=.04; GRADE 고); 성공률·포스트 탈락·치근파절에서는 유의차 없음. GRADE 고급 수준의 생존 이점 (RR 0.57 = 파이버 사용 시 실패 위험 약 43% 감

- `mously-2024-anterior-endocrowns-alternative-core-crown` [post-and-core] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Brings the modern minimally-invasive alternative (endocrown) into the new `post-and-core` category, directly framing when NOT to use a post — the conservative counterpoint to the post-necessity finding in [[post-and-core/alenezi-2024-endodontically-treated-teeth-post-placement-survival]]. Full-text PMC ingest gives detailed material/ferrule/extension-depth decision factors and connects to fracture
  - ▸ 출발(`mously-2024-anterior-endocrowns-alternative-core-crown`) 세줄: PRISMA 체계적 문헌고찰 (인비트로/FEA 12편, 서술적·메타분석 불가, 1307건 검색): 심한 치관 손상 전치부 근관치료치에서 엔도크라운과 포스트-코어-크라운(PCC)의 생체역학적 성능을 비교. 엔도크라운이 동등하거나 더 높은 파절저항과 더 수리 가능한 파절 양상 제공; 페룰(1–2 mm)이 재료·술식과 무관하게 피로저항의 결정인자; 리튬디실리케이트 최적, 지르코니아의 높은 탄성계수는 치명적 치근파절 유발; 근관 내 연장 3–5 mm 권장. 포스트의 역할은 치아 강화가 아닌 코어 유지로 

- `abdar-esfahani-2013-mandibular-anterior-nutrient-canals` [radiology] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: Contradicts the "NC as a hypertension diagnostic clue" claim reported elsewhere in the literature; this paper's null result aligns instead with Yilmaz et al. and Patni et al., indicating the NC–hypertension association is not a settled clinical marker.
  - ▸ 출발(`abdar-esfahani-2013-mandibular-anterior-nutrient-canals`) 세줄: 증례-대조군 연구 (n=64: 고혈압 환자 32명, 정상혈압 대조군 32명, 이란 이스파한) — 하악 전치부 견치-중절치 부위 치근단 방사선사진에서 영양관 (Nutrient Canal, NC) 유무 평가. 영양관 발생률은 고혈압군 37.5% vs 정상혈압군 53.1%로 통계적으로 유의하지 않음 (P = 0.209); 고혈압 유병기간(P = 0.292)·조절 여부(P = 0.144)와도 무관; 전체 인구에서 NC 존재군이 더 고령(47.1 vs 42.6세, P = 0.002). "영양관이 고혈압 진

- `abdar-esfahani-2013-mandibular-anterior-nutrient-canals` [radiology] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Explicitly situates its null finding against both camps in the literature: aligns with Yilmaz et al. and Patni et al. (no NC–HTN association) and contradicts Mani et al. and the broader positive-association literature (higher NC prevalence in hypertensive patients).
  - ▸ 출발(`abdar-esfahani-2013-mandibular-anterior-nutrient-canals`) 세줄: 증례-대조군 연구 (n=64: 고혈압 환자 32명, 정상혈압 대조군 32명, 이란 이스파한) — 하악 전치부 견치-중절치 부위 치근단 방사선사진에서 영양관 (Nutrient Canal, NC) 유무 평가. 영양관 발생률은 고혈압군 37.5% vs 정상혈압군 53.1%로 통계적으로 유의하지 않음 (P = 0.209); 고혈압 유병기간(P = 0.292)·조절 여부(P = 0.144)와도 무관; 전체 인구에서 NC 존재군이 더 고령(47.1 vs 42.6세, P = 0.002). "영양관이 고혈압 진

- `abdar-esfahani-2013-mandibular-anterior-nutrient-canals` [radiology] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[radiology/kumar-2014-incidence-nutrient-canals-hypertensive]] — **contradicts**: Kumar 2014 reports significantly higher NC incidence in hypertensive patients, supporting NC as an HTN diagnostic clue; this paper's blinded case-control found no such association (and a numerically lower NC incidence in the HTN group), directly conflicting with that conclusion.
  - ▸ 출발(`abdar-esfahani-2013-mandibular-anterior-nutrient-canals`) 세줄: 증례-대조군 연구 (n=64: 고혈압 환자 32명, 정상혈압 대조군 32명, 이란 이스파한) — 하악 전치부 견치-중절치 부위 치근단 방사선사진에서 영양관 (Nutrient Canal, NC) 유무 평가. 영양관 발생률은 고혈압군 37.5% vs 정상혈압군 53.1%로 통계적으로 유의하지 않음 (P = 0.209); 고혈압 유병기간(P = 0.292)·조절 여부(P = 0.144)와도 무관; 전체 인구에서 NC 존재군이 더 고령(47.1 vs 42.6세, P = 0.002). "영양관이 고혈압 진

- `abdar-esfahani-2013-mandibular-anterior-nutrient-canals` [radiology] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Ingested as part of a topical sweep on mandibular/alveolar "nutrient canals" as a radiographic marker of systemic disease. This case-control study is a **negative/contradicting result** relative to the hypertension-association literature: it found NO significant difference in nutrient-canal incidence between hypertensive (37.5%) and normotensive (53.1%) subjects (P = 0.209), directly contradicting
  - ▸ 출발(`abdar-esfahani-2013-mandibular-anterior-nutrient-canals`) 세줄: 증례-대조군 연구 (n=64: 고혈압 환자 32명, 정상혈압 대조군 32명, 이란 이스파한) — 하악 전치부 견치-중절치 부위 치근단 방사선사진에서 영양관 (Nutrient Canal, NC) 유무 평가. 영양관 발생률은 고혈압군 37.5% vs 정상혈압군 53.1%로 통계적으로 유의하지 않음 (P = 0.209); 고혈압 유병기간(P = 0.292)·조절 여부(P = 0.144)와도 무관; 전체 인구에서 NC 존재군이 더 고령(47.1 vs 42.6세, P = 0.002). "영양관이 고혈압 진

- `devlin-2013-object-position-magnification-panoramic-radiography` [radiology] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: Refutes the assumption that placing teeth in the focal trough avoids distortion — magnification is not simply constant at the plane of focus; positioning precision matters for any metric use of panoramic.
  - ▸ 출발(`devlin-2013-object-position-magnification-panoramic-radiography`) 세줄: 파노라마 확대율 수식과 볼베어링 팬텀 실험(플라스틱 두개골, 2.5 mm·6 mm 강구, 21회 반복 촬영)을 결합해 물체 위치·크기·장비 파라미터와 확대율의 관계를 도출한 연구. 수평 확대율 ~1.29·수직 ~1.26; 왜곡 0이 되는 것은 초점골(Focal Trough) 내 특정 위치에서만, 수평 위치 오차 시 초점골 내에서도 왜곡 발생; 6 mm 구체가 2.5 mm보다 확대율·위치 추정에 신뢰도 높음. 파노라마 영상은 개별 보정 없이 계측 도구로 사용 불가; 치수 측정이 필요한 경우 6 mm

- `devlin-2013-object-position-magnification-panoramic-radiography` [radiology] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: Refutes the assumption that placing teeth in the focal trough avoids distortion — magnification is not simply constant at the plane of focus; positioning precision matters for any metric use of panoramic.
  - ▸ 출발(`devlin-2013-object-position-magnification-panoramic-radiography`) 세줄: 파노라마 확대율 수식과 볼베어링 팬텀 실험(플라스틱 두개골, 2.5 mm·6 mm 강구, 21회 반복 촬영)을 결합해 물체 위치·크기·장비 파라미터와 확대율의 관계를 도출한 연구. 수평 확대율 ~1.29·수직 ~1.26; 왜곡 0이 되는 것은 초점골(Focal Trough) 내 특정 위치에서만, 수평 위치 오차 시 초점골 내에서도 왜곡 발생; 6 mm 구체가 2.5 mm보다 확대율·위치 추정에 신뢰도 높음. 파노라마 영상은 개별 보정 없이 계측 도구로 사용 불가; 치수 측정이 필요한 경우 6 mm

- `willershausen-2025-low-field-mri-pediatric-dental` [radiology] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Positions low-field MRI as an emerging radiation-free alternative for selected paediatric dental indications, with current spatial-resolution limits — the conceptual counterpoint to the dose-reduction cluster.
  - ▸ 출발(`willershausen-2025-low-field-mri-pediatric-dental`) 세줄: 줄1: 전향적 단일기관 연구(소아 16명, 평균 12.4세, 과잉치·이소치 49개) — 방사선 없는 0.55 T MRI(~10분 촬영)와 동일 날 초저선량 CT(CTDI 0.43 mGy)를 7개 치아 구조에 대해 화질 비교. 줄2: 0.55 T MRI는 치축·치근·치근흡수·낭종에서 초저선량 CT와 유사한 유효 화질 달성; 운동 인공물 차이 없음; 일부 구조에서는 미흡. 줄3: 저자기장 MRI는 특정 소아 치과 적응증(과잉치·이소치)에서 방사선 없는 대안이 될 수 있으나, 고해상도 영상이 필요한 진

- `willershausen-2025-low-field-mri-pediatric-dental` [radiology] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Positions low-field MRI as an emerging radiation-free alternative for selected paediatric dental indications, with current spatial-resolution limits — the conceptual counterpoint to the dose-reduction cluster.
  - ▸ 출발(`willershausen-2025-low-field-mri-pediatric-dental`) 세줄: 줄1: 전향적 단일기관 연구(소아 16명, 평균 12.4세, 과잉치·이소치 49개) — 방사선 없는 0.55 T MRI(~10분 촬영)와 동일 날 초저선량 CT(CTDI 0.43 mGy)를 7개 치아 구조에 대해 화질 비교. 줄2: 0.55 T MRI는 치축·치근·치근흡수·낭종에서 초저선량 CT와 유사한 유효 화질 달성; 운동 인공물 차이 없음; 일부 구조에서는 미흡. 줄3: 저자기장 MRI는 특정 소아 치과 적응증(과잉치·이소치)에서 방사선 없는 대안이 될 수 있으나, 고해상도 영상이 필요한 진

- `abreu-2024-assessment-detoxification-strategies-used-dental` [infection-control] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[infection-control/kyaw-2023-effect-chemical-electrochemical-decontamination-protocols]] — **contradicts** on the biologic-response axis: Kyaw's RCT concludes reuse is acceptable with a combined chemical/electrochemical protocol, whereas Abreu finds that even the best-cleaned HAs remain inflammatory in vitro, so cleanliness alone does not justify reuse.
  - ▸ 출발(`abreu-2024-assessment-detoxification-strategies-used-dental`) 세줄: 사용된 힐링어버트먼트 50개를 효소세정제 5개 프로토콜(A–E, 각 n=10)로 처리 후 신품 10개와 비교 — 육안/Micro BCA 단백질 잔류(세정 품질)와 인간 대식세포 9종 사이토카인(생물학적 불활성도)을 동시 평가. D/E군이 잔여 debris·단백질 최소(A군 최대); 그러나 가장 깨끗한 군 포함, 세정된 모든 군이 대조(신품) 대비 최대 5일간 높은 염증 사이토카인 분비 유발 → "세정 품질 ≠ 생물학적 불활성도" 디커플링 확인. 임상 의미: 이 batch에서 가장 강한 재사용 금지

- `burioni-2024-could-dental-material-reuse-play` [infection-control] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[infection-control/kyaw-2023-effect-chemical-electrochemical-decontamination-protocols]] — RCT suggesting reuse is acceptable with a combined chemical/electrochemical protocol — a more permissive counterpoint on the reuse question.
  - ▸ 출발(`burioni-2024-could-dental-material-reuse-play`) 세줄: 산 라파엘레 병원 인 비트로 연구(재사용+멸균 40개 vs 신품 35개 Winsix 티타늄 힐링어버트먼트) — Micro BCA 단백질 분석과 탁도 기반 무균 검사로 멸균 효과와 표면 청결도를 분리 평가. 세척+오토클레이브 프로토콜은 100% 무균 달성(양 군 모두 세균 무성장)했으나, 재사용 어버트먼트 잔류 표면 단백질이 신품보다 유의하게 많음(18.76 vs 9.35 µg/mL; 평균차 9.41, 95% CI 4.28–14.54, p<0.001; 스크류당 약 12 µg); 이 잔류 단백질 차이

- `dioguardi-2020-management-instrument-sterilization-workflow-endodontics` [infection-control] (HIGH-no-target, 'conflicting evidence' · 상충 결과)
  - **근거 문장**: - **Mechanical effects of repeated autoclaving on files**: conflicting evidence — NiTi files may show improved fatigue resistance after autoclaving (a thermal-treatment side effect), while steel files show reduced torsional resistance and cutting capacity with repeated cycles. Cutting-capacity reduction reported at 20% after 7 cycles in one study and 1–12% after 5–10 cycles in another. **Recommend
  - ▸ 출발(`dioguardi-2020-management-instrument-sterilization-workflow-endodontics`) 세줄: 체계적 문헌고찰+메타분석(PRISMA, PubMed/Scopus 130편, 40년 검색창)으로 근관치료 기구·근관충전재의 멸균/소독 방법을 평가. 메타분석 결과 오토클레이브가 글루타르알데히드보다 우수(I²=0%, 고정효과모형), 글루타르알데히드가 유리구슬 멸균보다 우수(I²=73%, 랜덤효과모형); 최소 120°C·30분 이상 오토클레이브가 최적 방법으로 확인되었고, NiTi 파일 재사용은 오토클레이브 5회 이하로 제한, 열처리 불가능한 거타퍼차/레진 콘은 화학적 소독(NaOCl 2–5.25% 또

- `al-sulimman-2025-composite-amalgam-failure-risk-sr-ma` [dental-materials] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Heterogeneity in failure definitions across studies is the key limitation; the null RR contradicts real-world big-data findings (Tobias 2024: HR 1.29 for composite), and standardized failure criteria are needed for future studies.
  - ▸ 출발(`al-sulimman-2025-composite-amalgam-failure-risk-sr-ma`) 세줄: SR+MA(PRISMA; PubMed·Cochrane·Google Scholar; 13편; 추적 ≥12개월; 1990~): 영구 구치부 복합레진(Composite Resin) vs 아말감(Amalgam) 수복물 실패 위험 비교. 무작위 효과 메타분석: RR 0.96(95% CI 0.68–1.34) — 통계적 유의차 없음; 아말감 실패비율 0–50%, 레진 0–62.7%; 출판 비뚤림 없음(Egger's p>0.05). 연구 간 실패 정의 이질성이 핵심 제한점 — Tobias 2024(빅데이터 HR

- `al-sulimman-2025-composite-amalgam-failure-risk-sr-ma` [dental-materials] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 연구 간 실패 정의 이질성이 핵심 제한점 — Tobias 2024(빅데이터 HR 1.29 레진 불리)와 결과 상충; 표준화된 실패 기준과 교란 통제가 요구됨.
  - ▸ 출발(`al-sulimman-2025-composite-amalgam-failure-risk-sr-ma`) 세줄: SR+MA(PRISMA; PubMed·Cochrane·Google Scholar; 13편; 추적 ≥12개월; 1990~): 영구 구치부 복합레진(Composite Resin) vs 아말감(Amalgam) 수복물 실패 위험 비교. 무작위 효과 메타분석: RR 0.96(95% CI 0.68–1.34) — 통계적 유의차 없음; 아말감 실패비율 0–50%, 레진 0–62.7%; 출판 비뚤림 없음(Egger's p>0.05). 연구 간 실패 정의 이질성이 핵심 제한점 — Tobias 2024(빅데이터 HR

- `al-sulimman-2025-composite-amalgam-failure-risk-sr-ma` [dental-materials] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - No statistically significant difference in failure risk between composite resin and amalgam (RR 0.96) — contradicts real-world HR data (Tobias 2024: HR 1.29)
  - ▸ 출발(`al-sulimman-2025-composite-amalgam-failure-risk-sr-ma`) 세줄: SR+MA(PRISMA; PubMed·Cochrane·Google Scholar; 13편; 추적 ≥12개월; 1990~): 영구 구치부 복합레진(Composite Resin) vs 아말감(Amalgam) 수복물 실패 위험 비교. 무작위 효과 메타분석: RR 0.96(95% CI 0.68–1.34) — 통계적 유의차 없음; 아말감 실패비율 0–50%, 레진 0–62.7%; 출판 비뚤림 없음(Egger's p>0.05). 연구 간 실패 정의 이질성이 핵심 제한점 — Tobias 2024(빅데이터 HR

- `tobias-2024-amalgam-composite-survival-big-data` [dental-materials] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[dental-materials/al-sulimman-2025-composite-amalgam-failure-risk-sr-ma]] — SR+MA; no significant RR difference (RR 0.96); contradicts real-world HR gap
  - ▸ 출발(`tobias-2024-amalgam-composite-survival-big-data`) 세줄: 이스라엘 Maccabi 58개 클리닉의 전자 건강 기록(환자 65만 명 이상, 약 26만 905명 수복물 보유, 2014–2021)을 이용한 후향적 코호트로, 나이·성별·면 수·치아 유형·술자 보정 Cox 회귀분석 시행. 연간 실패율: 아말감(Amalgam) 3.5% vs 복합레진(Composite Resin) 4.5%(HR 1.29, p<0.001) — 다면(Multi-surface) 복합레진이 주요 원인; 단면(Single-surface) 수복물은 재료 간 유의한 차이 없음. 미나마타 협약(M

- `bubalo-2026-bone-substitutes-alveolar-ridge-augmentation` [bone-regeneration] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Explicit heterogeneity flagging on adjuncts**: Notes contradictory hyaluronic acid (HYA) evidence — some studies show benefit in socket preservation/early bone formation, others report limited effect or even increased crestal bone loss with HYA/PRF — modeling appropriate epistemic caution rather than overselling adjunct biologics.
  - ▸ 출발(`bubalo-2026-bone-substitutes-alveolar-ridge-augmentation`) 세줄: PubMed/Scopus 기반 narrative review(2000–2025, 메타분석 없음)로, 치과 임플란트를 위한 치조제 증대에 사용되는 7개 골이식재 범주의 생물학적 원리와 임상 결과를 종합. 자가골(autogenous bone)은 골형성+골유도+골전도 특성을 모두 갖춘 생물학적 gold standard이지만 6개월 내 최대 55% 부피 소실을 보이며, 이종골(xenograft):자가골(autograft) 1:1 혼합이 최고 신생골형성률(65.8%)을 보고했고, defect 유형별 선택 

- `bubalo-2026-bone-substitutes-alveolar-ridge-augmentation` [bone-regeneration] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: 기존 [[wiki/bone-regeneration/buser-2023-gbr-implant-35years-basic-principle-review]]가 GBR의 35년 기본원리를 다뤘다면, 본 narrative review(Bubalo 2026)는 autograft·allograft·xenograft·alloplast·demineralized tooth matrix·PRF/PRP·3D-printed scaffold 7개 그래프트 유형을 defect-type(horizontal/vertical/complex)별 알고리즘과 비교표(Table 1~4)로 정리해 임상 선택 프레임워크를 보강한다. 특히 xenograft:autograft 1:1 비율에서 최고 신생골형성(65.8%)을 보고한 Kamat 2025 pil
  - ▸ 출발(`bubalo-2026-bone-substitutes-alveolar-ridge-augmentation`) 세줄: PubMed/Scopus 기반 narrative review(2000–2025, 메타분석 없음)로, 치과 임플란트를 위한 치조제 증대에 사용되는 7개 골이식재 범주의 생물학적 원리와 임상 결과를 종합. 자가골(autogenous bone)은 골형성+골유도+골전도 특성을 모두 갖춘 생물학적 gold standard이지만 6개월 내 최대 55% 부피 소실을 보이며, 이종골(xenograft):자가골(autograft) 1:1 혼합이 최고 신생골형성률(65.8%)을 보고했고, defect 유형별 선택 

- `khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma` [bone-regeneration] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: This page **refines** the staging decision underlying the staged (two-stage) technique anchored by Enislidis 2006: a contemporary comparative SR tilts the timing choice toward one-stage, without overturning the standalone validity of the staged greenstick technique as a documented option for difficult ridges.
  - ▸ 출발(`khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma`) 세줄: 1단계 vs 2단계 치조제 분할술을 직접 비교한 최초 PRISMA SR+MA(정성 11편, 메타분석 3편, 2000–2021년). 통합 표준화평균차(Standardized Mean Difference, SMD) ~0.89로 1단계 우위; 전체 11편 중-고 비뚤림 위험, 깔때기도 비대칭(출판편향 가능성) — 근거 신뢰도 낮음. 방향성 신호는 1단계 선호를 지지하지만, 하악 고밀도 피질골·극세 치조제 등 위험 증례에서 2단계 접근의 임상적 타당성을 부정하지는 않음.

- `khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma` [bone-regeneration] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: - [[bone-regeneration/enislidis-2006-staged-ridge-splitting-implant-mandible]] — staged (two-stage) ridge-split technique anchor; this SR refines the timing decision toward one-stage but does not overturn the staged technique's role.
  - ▸ 출발(`khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma`) 세줄: 1단계 vs 2단계 치조제 분할술을 직접 비교한 최초 PRISMA SR+MA(정성 11편, 메타분석 3편, 2000–2021년). 통합 표준화평균차(Standardized Mean Difference, SMD) ~0.89로 1단계 우위; 전체 11편 중-고 비뚤림 위험, 깔때기도 비대칭(출판편향 가능성) — 근거 신뢰도 낮음. 방향성 신호는 1단계 선호를 지지하지만, 하악 고밀도 피질골·극세 치조제 등 위험 증례에서 2단계 접근의 임상적 타당성을 부정하지는 않음.

- `khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma` [bone-regeneration] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: This SR+MA directly informs the staging decision behind [[wiki/bone-regeneration/enislidis-2006-staged-ridge-splitting-implant-mandible]] (a two-stage staged ridge-split technique): the pooled comparative analysis finds the **one-stage** ridge split superior to the two-stage approach (SMD favouring one-stage ~0.89). It refines — but does not overturn — the enislidis staged-technique anchor, and co
  - ▸ 출발(`khanum-2024-one-stage-vs-two-stage-ridge-splitting-sr-ma`) 세줄: 1단계 vs 2단계 치조제 분할술을 직접 비교한 최초 PRISMA SR+MA(정성 11편, 메타분석 3편, 2000–2021년). 통합 표준화평균차(Standardized Mean Difference, SMD) ~0.89로 1단계 우위; 전체 11편 중-고 비뚤림 위험, 깔때기도 비대칭(출판편향 가능성) — 근거 신뢰도 낮음. 방향성 신호는 1단계 선호를 지지하지만, 하악 고밀도 피질골·극세 치조제 등 위험 증례에서 2단계 접근의 임상적 타당성을 부정하지는 않음.

- `lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma` [bone-regeneration] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 임상과 전임상 간 상충(전임상은 골임플란트접촉률, Bone-to-Implant Contact, BIC·골통합 개선 없음; 과밀도화로 임플란트 실패 1건 RCT 보고) — 기법 경험 충분 시에만 사용, 단계적 골증대가 가능한 경우 우선.
  - ▸ 출발(`lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma`) 세줄: PROSPERO 등록 SR+MA(10편, n=241, RCT 5+관찰 5): 수평위축 ≤2.5 mm 성인에서 골확장(Ridge Expansion)·압축(Compaction)·골밀도화(Osteodensification, ODT)의 골밀도(Bone Density, BD)·치조정확장(Crestal Expansion, CE)·임플란트안정성지수(Implant Stability Quotient, ISQ) 통합. BD SMD −0.71(p=0.002, I²=0%·신뢰도 높음)·CE SMD −1.12(민감도 분

- `lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma` [bone-regeneration] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Foregrounds the **clinical-vs-preclinical contradiction**: clinical pooling favors densification, but sheep/porcine/murine models show no BIC or osseointegration gain, and one RCT (Rizk 2024) attributed 3 implant failures to over-densifying the narrow crest (reduced blood supply, heat) — leading the authors to position these techniques behind GBR / bone blocks / crestal split when those are feas
  - ▸ 출발(`lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma`) 세줄: PROSPERO 등록 SR+MA(10편, n=241, RCT 5+관찰 5): 수평위축 ≤2.5 mm 성인에서 골확장(Ridge Expansion)·압축(Compaction)·골밀도화(Osteodensification, ODT)의 골밀도(Bone Density, BD)·치조정확장(Crestal Expansion, CE)·임플란트안정성지수(Implant Stability Quotient, ISQ) 통합. BD SMD −0.71(p=0.002, I²=0%·신뢰도 높음)·CE SMD −1.12(민감도 분

- `lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma` [bone-regeneration] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Bottom line**: expansion / compaction / osseodensification can render a narrow crest implant-ready and improve BD, CE, and ISQ, but the CE and ISQ evidence is fragile (heterogeneity + publication bias) and clinical benefit is contradicted by preclinical models — use cautiously, with adequate operator experience, and reserve for cases where staged augmentation is not preferable.
  - ▸ 출발(`lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma`) 세줄: PROSPERO 등록 SR+MA(10편, n=241, RCT 5+관찰 5): 수평위축 ≤2.5 mm 성인에서 골확장(Ridge Expansion)·압축(Compaction)·골밀도화(Osteodensification, ODT)의 골밀도(Bone Density, BD)·치조정확장(Crestal Expansion, CE)·임플란트안정성지수(Implant Stability Quotient, ISQ) 통합. BD SMD −0.71(p=0.002, I²=0%·신뢰도 높음)·CE SMD −1.12(민감도 분

- `elgali-2017-guided-bone-regeneration-materials-mechanisms` [bone-regeneration] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: As a narrative (non-systematic) review without meta-analysis, conclusions on optimal membrane porosity remain explicitly unresolved (contradictory in vivo results across studies), and the "active membrane" mechanistic model is drawn mostly from the authors' own rat/human studies rather than an independently replicated body of evidence.
  - ▸ 출발(`elgali-2017-guided-bone-regeneration-materials-mechanisms`) 세줄: Narrative literature review(PubMed/MEDLINE, 2016년 6월 16일까지 문헌 검색, 출판연도 제한 없음)로, 골유도재생술(Guided Bone Regeneration, GBR) 차폐막(barrier membrane) 재료 분류·물리화학적/기계적 개질(modification)·세포분자 기전을 종합. GBR은 수평·수직 골증대 후 약 95% 임플란트 생존율을 보이고 골유착(osseointegration) 임플란트의 최대 40%가 GBR을 필요로 하며, 본 리뷰의 핵심

- `elgali-2017-guided-bone-regeneration-materials-mechanisms` [bone-regeneration] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: 메타분석 없는 narrative review이므로 최적 막 기공 크기(porosity)에 대한 결론은 연구간 상반된 결과로 명시적으로 미해결 상태이며, "능동적 막" 기전 모델은 대부분 저자 자신의 rat/인체 연구에서 도출되어 독립적으로 반복검증된 근거체계는 아니다.
  - ▸ 출발(`elgali-2017-guided-bone-regeneration-materials-mechanisms`) 세줄: Narrative literature review(PubMed/MEDLINE, 2016년 6월 16일까지 문헌 검색, 출판연도 제한 없음)로, 골유도재생술(Guided Bone Regeneration, GBR) 차폐막(barrier membrane) 재료 분류·물리화학적/기계적 개질(modification)·세포분자 기전을 종합. GBR은 수평·수직 골증대 후 약 95% 임플란트 생존율을 보이고 골유착(osseointegration) 임플란트의 최대 40%가 GBR을 필요로 하며, 본 리뷰의 핵심

- `elgali-2017-guided-bone-regeneration-materials-mechanisms` [bone-regeneration] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Unresolved porosity controversy flagged explicitly**: contradictory in vivo evidence on whether larger membrane pore size promotes (via vascularization/nutrient diffusion) or impairs (via soft-tissue cell invasion) bone regeneration — the review calls this an open question rather than adjudicating a consensus.
  - ▸ 출발(`elgali-2017-guided-bone-regeneration-materials-mechanisms`) 세줄: Narrative literature review(PubMed/MEDLINE, 2016년 6월 16일까지 문헌 검색, 출판연도 제한 없음)로, 골유도재생술(Guided Bone Regeneration, GBR) 차폐막(barrier membrane) 재료 분류·물리화학적/기계적 개질(modification)·세포분자 기전을 종합. GBR은 수평·수직 골증대 후 약 95% 임플란트 생존율을 보이고 골유착(osseointegration) 임플란트의 최대 40%가 GBR을 필요로 하며, 본 리뷰의 핵심

- `elgali-2017-guided-bone-regeneration-materials-mechanisms` [bone-regeneration] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: | Porosity | Contradictory: some studies show pores >10-100 μm improve bone formation (vascularization/nutrient diffusion); others show occlusive/dense (d-PTFE, 0.2 μm) membranes equal or outperform porous membranes and resist bacterial penetration better |
  - ▸ 출발(`elgali-2017-guided-bone-regeneration-materials-mechanisms`) 세줄: Narrative literature review(PubMed/MEDLINE, 2016년 6월 16일까지 문헌 검색, 출판연도 제한 없음)로, 골유도재생술(Guided Bone Regeneration, GBR) 차폐막(barrier membrane) 재료 분류·물리화학적/기계적 개질(modification)·세포분자 기전을 종합. GBR은 수평·수직 골증대 후 약 95% 임플란트 생존율을 보이고 골유착(osseointegration) 임플란트의 최대 40%가 GBR을 필요로 하며, 본 리뷰의 핵심

- `domic-2023-hyaluronic-acid-tooth-extraction-sr-ma` [bone-regeneration] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Clinical implication: HyA may modestly reduce late post-LM3-extraction pain and support soft-tissue socket closure after regular extractions, but evidence for a ridge-preservation/hard-tissue benefit is weak-to-contradictory (one study reported significantly MORE coronal horizontal bone loss with HyA), and overall GRADE certainty is low-to-moderate.
  - ▸ 출발(`domic-2023-hyaluronic-acid-tooth-extraction-sr-ma`) 세줄: PROSPERO 등록 체계적 문헌고찰(SR)+메타분석(MA)으로, 발치 후 또는 치조골염(AO) 치료 목적의 국소 히알루론산(hyaluronic acid, HyA) 적용을 다룬 전임상연구 5편(쥐/개)과 임상연구 22편(최종평가 1,062명)을 통합. 메타분석에서 HyA는 하악 제3대구치(LM3) 수술적 발치 후 7일째 통증을 유의하게 감소시켰으나(effect size 0.32, 95% CI 0.12-0.51, p=0.01) 초기 통증·부종·개구제한(trismus)에는 유의한 효과가 없었고, 전임

- `domic-2023-hyaluronic-acid-tooth-extraction-sr-ma` [bone-regeneration] (HIGH-no-target, '상반되' · 상반)
  - **근거 문장**: 임상적 의미: HyA는 LM3 발치 후 후기 통증 및 정상 발치 후 연조직 치유에 제한적 도움이 될 수 있으나, 치조제 보존/경조직 효과 근거는 약하거나 상반되며(한 연구는 오히려 치관측 수평골소실 증가 보고), 전체 GRADE 근거 확실성은 낮음-중등도.
  - ▸ 출발(`domic-2023-hyaluronic-acid-tooth-extraction-sr-ma`) 세줄: PROSPERO 등록 체계적 문헌고찰(SR)+메타분석(MA)으로, 발치 후 또는 치조골염(AO) 치료 목적의 국소 히알루론산(hyaluronic acid, HyA) 적용을 다룬 전임상연구 5편(쥐/개)과 임상연구 22편(최종평가 1,062명)을 통합. 메타분석에서 HyA는 하악 제3대구치(LM3) 수술적 발치 후 7일째 통증을 유의하게 감소시켰으나(effect size 0.32, 95% CI 0.12-0.51, p=0.01) 초기 통증·부종·개구제한(trismus)에는 유의한 효과가 없었고, 전임

- `domic-2023-hyaluronic-acid-tooth-extraction-sr-ma` [bone-regeneration] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Documents a clinically important contradictory finding: intra-/post-operative HyA gel applied after ridge preservation (collagen-enriched deproteinized bovine bone mineral + collagen matrix sealing) was associated with significantly MORE coronal horizontal bone loss vs no HyA.
  - ▸ 출발(`domic-2023-hyaluronic-acid-tooth-extraction-sr-ma`) 세줄: PROSPERO 등록 체계적 문헌고찰(SR)+메타분석(MA)으로, 발치 후 또는 치조골염(AO) 치료 목적의 국소 히알루론산(hyaluronic acid, HyA) 적용을 다룬 전임상연구 5편(쥐/개)과 임상연구 22편(최종평가 1,062명)을 통합. 메타분석에서 HyA는 하악 제3대구치(LM3) 수술적 발치 후 7일째 통증을 유의하게 감소시켰으나(effect size 0.32, 95% CI 0.12-0.51, p=0.01) 초기 통증·부종·개구제한(trismus)에는 유의한 효과가 없었고, 전임

- `domic-2023-hyaluronic-acid-tooth-extraction-sr-ma` [bone-regeneration] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[bone-regeneration/bubalo-2026-bone-substitutes-alveolar-ridge-augmentation]] — Bubalo 2026's narrative review cites HyA as a ridge-augmentation adjunct with "inconsistent/contradictory findings"; this SR+MA (Domic 2023) is the primary quantitative evidence behind that characterization, showing HyA's benefit is confined to post-LM3-extraction pain at day 7 and does not extend to bone/ridge pres
  - ▸ 출발(`domic-2023-hyaluronic-acid-tooth-extraction-sr-ma`) 세줄: PROSPERO 등록 체계적 문헌고찰(SR)+메타분석(MA)으로, 발치 후 또는 치조골염(AO) 치료 목적의 국소 히알루론산(hyaluronic acid, HyA) 적용을 다룬 전임상연구 5편(쥐/개)과 임상연구 22편(최종평가 1,062명)을 통합. 메타분석에서 HyA는 하악 제3대구치(LM3) 수술적 발치 후 7일째 통증을 유의하게 감소시켰으나(effect size 0.32, 95% CI 0.12-0.51, p=0.01) 초기 통증·부종·개구제한(trismus)에는 유의한 효과가 없었고, 전임

- `domic-2023-hyaluronic-acid-tooth-extraction-sr-ma` [bone-regeneration] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: 이 논문은 [[wiki/bone-regeneration/bubalo-2026-bone-substitutes-alveolar-ridge-augmentation]] narrative review가 인용한 hyaluronic acid (HyA, 히알루론산) 보조재의 "상반된 결과"를 뒷받침하는 원전 SR+MA다. Bubalo 2026이 HyA를 "일부 연구에서 crestal bone loss 증가"로 짧게 언급한 것과 달리, 본 논문(Domic 2023)은 5편의 전임상 연구 + 22편의 임상 연구(최종평가 1,062명)를 정량적으로 통합해 HyA의 발치와(extraction socket) 치유 효과를 부위·적응증별로(하악 제3대구치 수술적 발치 vs 정상 맹출치 발치 vs 치조골염 치료) 세분화한다. 특히 Hy
  - ▸ 출발(`domic-2023-hyaluronic-acid-tooth-extraction-sr-ma`) 세줄: PROSPERO 등록 체계적 문헌고찰(SR)+메타분석(MA)으로, 발치 후 또는 치조골염(AO) 치료 목적의 국소 히알루론산(hyaluronic acid, HyA) 적용을 다룬 전임상연구 5편(쥐/개)과 임상연구 22편(최종평가 1,062명)을 통합. 메타분석에서 HyA는 하악 제3대구치(LM3) 수술적 발치 후 7일째 통증을 유의하게 감소시켰으나(effect size 0.32, 95% CI 0.12-0.51, p=0.01) 초기 통증·부종·개구제한(trismus)에는 유의한 효과가 없었고, 전임

- `sun-2025-3d-printed-scaffold-bone-defect-repair` [bone-regeneration] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 이상적 스캐폴드는 상충하는 설계 제약의 균형이 필요(큰 기공/높은 다공성은 세포 침투·혈관신생에 유리하지만 기계적 강도 저하; 피질골에 근접한 목표치는 Young's modulus 7-30 GPa, 압축강도 50-200 MPa, 인장강도 ~150 MPa), 복합/코팅 설계(예: 티타늄+SiHA+VEGF, PCL/β-TCP+BMP-2, 마그네슘 가교 하이드로겔)가 단일재료 스캐폴드보다 전임상 모델에서 일관되게 우수.
  - ▸ 출발(`sun-2025-3d-printed-scaffold-bone-defect-repair`) 세줄: 일반 정형외과 골결손 수복을 위한 3D 프린팅 스캐폴드 기술 narrative review(Biomed Eng Online 2025) — 재료 선택(금속·고분자·생체세라믹), 계층적 다공성/생체역학적 설계, 생물학적 기능화, 바이오프린팅 방법을 종합. 이상적 스캐폴드는 상충하는 설계 제약의 균형이 필요(큰 기공/높은 다공성은 세포 침투·혈관신생에 유리하지만 기계적 강도 저하; 피질골에 근접한 목표치는 Young's modulus 7-30 GPa, 압축강도 50-200 MPa, 인장강도 ~150 M

- `rokn-2011-bone-formation-two-grafting-materials` [bone-regeneration] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Directly tested and refuted the hypothesis that higher material resorption rate predicts more new bone formation within a short (4-8 week) window.
  - ▸ 출발(`rokn-2011-bone-formation-two-grafting-materials`) 세줄: 동물실험(토끼 두개골) 조직학·조직계측학 연구, n=13마리 토끼에 동일 규격 6.5mm 두개골 결손 52개를 형성해 Straumann Bone Ceramic(대·소입자, HA/beta-TCP 이상재료)과 Bio-Oss(우골 이종이식재), 무처치 대조군을 4주·8주 시점에 비교. 네 군 간 골충전량에 통계적으로 유의한 차이 없음(Bio-Oss가 수치상 최고, 이어서 대조군·L-SBC·S-SBC 순); 대입자 골세라믹(L-SBC)이 Bio-Oss·대조군보다 유의하게 더 많은 염증반응과 이물반응(fo

- `assiri-2026-iprf-prf-beta-tcp-bone-regeneration-goat` [bone-regeneration] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[bone-regeneration/ridge-preservation/park-2022-prf-gbr-damaged-socket-yonsei]] — Beagle-dog 2-wall alveolar defect study found PRF-based sticky bone (i-PRF+DPBM) only *non-inferior* to conventional GBR, not superior; this goat metacarpal study instead finds β-TCP+i-PRF clearly *superior* to β-TCP+PRF and β-TCP alone, suggesting i-PRF's incremental benefit over PRF/GBR-alone may depend on defec
  - ▸ 출발(`assiri-2026-iprf-prf-beta-tcp-bone-regeneration-goat`) 세줄: 동물 실험 연구 (수컷 Najdi종 염소 18마리, 좌측 중수골에 72개 임계크기결손, 마리당 4군: 자연치유, β-삼인산칼슘(β-Tricalcium Phosphate, β-TCP) 단독, β-TCP+혈소판풍부피브린(Platelet-Rich Fibrin, PRF), β-TCP+주사형혈소판풍부피브린(injectable Platelet-Rich Fibrin, i-PRF); 2/5/8주 마이크로 전산화단층촬영(micro-CT) 평가). 8주 시점 β-TCP+i-PRF군이 신생골량(BV-NFB 80.08

- `assiri-2026-iprf-prf-beta-tcp-bone-regeneration-goat` [bone-regeneration] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: i-PRF·PRF의 골재생 보조효과를 β-TCP 이식재와 직접 head-to-head로 비교한 대형동물(goat) critical-size defect micro-CT 연구로, 기존 [[bone-regeneration/ridge-preservation/park-2022-prf-gbr-damaged-socket-yonsei]](비글견 2벽성 결손에서 sticky bone vs GBR 비열등성)과 대비되는 결과를 보인다 — 본 연구는 i-PRF+β-TCP가 β-TCP 단독·PRF+β-TCP보다 8주 시점 신생골량·골밀도에서 유의하게 우수함을 보고해, i-PRF의 부가 이득이 결손 유형(장골 metacarpal critical-size defect vs 치조 2벽성 결손)에 따라 달라질 수 있음을 시사한다.
  - ▸ 출발(`assiri-2026-iprf-prf-beta-tcp-bone-regeneration-goat`) 세줄: 동물 실험 연구 (수컷 Najdi종 염소 18마리, 좌측 중수골에 72개 임계크기결손, 마리당 4군: 자연치유, β-삼인산칼슘(β-Tricalcium Phosphate, β-TCP) 단독, β-TCP+혈소판풍부피브린(Platelet-Rich Fibrin, PRF), β-TCP+주사형혈소판풍부피브린(injectable Platelet-Rich Fibrin, i-PRF); 2/5/8주 마이크로 전산화단층촬영(micro-CT) 평가). 8주 시점 β-TCP+i-PRF군이 신생골량(BV-NFB 80.08

- `inchingolo-2025-bovine-xenograft-longterm-histological-clinical` [bone-regeneration] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[sinus-lift/lateral/sartori-2003-msfa-bio-oss-10year-case-report]] — 10-year Bio-Oss biopsy case report showing progressive bone-to-graft ratio increase over time; a relevant counterpoint on whether DBBM truly remains inert long-term, worth weighing against this SR's cautious conclusions.
  - ▸ 출발(`inchingolo-2025-bovine-xenograft-longterm-histological-clinical`) 세줄: 체계적 문헌고찰 (PRISMA 2020, PROSPERO CRD420251111685; 217편 스크리닝 중 11편 최종 포함) — 상악동거상술·치조제증대·발치와보존(ARP) 전반에서 우골유래 이종골이식재(Bio-Oss/DBBM)의 장기 조직학적·임상적 결과를 평가. GRADE 평가상 단기·중기 임플란트 생존·이식재 통합의 근거등급은 중등도(moderate)였으나 장기 합병증(입자 이동·만성염증·부비동 병리)은 낮음(low); ROBINS-I 평가에서 11편 중 대부분이 중등도 비뚤림 위험을 보였

- `souza-2020-citrus-sweets-enamel-erosion-invitro` [dental-erosion] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Coca-Cola (pH 2.6, 1.4 μm), refuting the assumption that pH alone predicts erosive rank.
  - ▸ 출발(`souza-2020-citrus-sweets-enamel-erosion-invitro`) 세줄: In-vitro 연구 (n=90 소 법랑질, 7일): 시트러스 젤리(pH 2.6~3.5)가 1.3–2.4 μm 법랑질 마모 유발; Fini Diet(pH 3.3)·Fini Regaliz(pH 3.1)는 0.1% 구연산 수준으로 Coca-Cola보다 더 침식적 — 복합산(구연산+젖산/말레산)이 pH보다 침식력 결정에 중요.

- `kiliaridis-2000-vertical-position-rotation-tipping-molars` [occlusion] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Provides large-sample human evidence that **overeruption is not inevitable** for unopposed molars, refuting the universal-overeruption belief.
  - ▸ 출발(`kiliaridis-2000-vertical-position-rotation-tipping-molars`) 세줄: 단면 임상·석고모형 연구(53명, 10년 이상 대합치 없는 대구치 84개[상악 61·하악 23]): 정출 없음·경미·중등도-중증의 3단계로 수직위치, 회전, 경사를 평가했다. 중등도-중증 정출(≥2 mm)은 24%에 불과했고 18%는 전혀 정출하지 않았으며, 성인기 이후 대합치 소실이면 위험이 낮고, 회전은 상악에서, 경사는 하악에서 더 흔했다. 장기간 대합치가 없더라도 모든 대구치가 정출하지는 않는다 — 이 "비정출" 비율(~18%)은 대합치 없는 공간 보철 여부를 결정하는 핵심 근거로 활용된다

- `kiliaridis-2000-vertical-position-rotation-tipping-molars` [occlusion] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Foundational evidence for the qualifier that **not every unopposed tooth overerupts** — directly tests and refutes the long-held "every tooth without an antagonist overerupts" belief, supplying the "~18% show no overeruption" non-eruptor figure used in [[wiki/overviews/unopposed-tooth-overeruption-overview]]. Reinforces [[wiki/occlusion/livas-2016-fixed-retention-unopposed-molar-overeruption]] by 
  - ▸ 출발(`kiliaridis-2000-vertical-position-rotation-tipping-molars`) 세줄: 단면 임상·석고모형 연구(53명, 10년 이상 대합치 없는 대구치 84개[상악 61·하악 23]): 정출 없음·경미·중등도-중증의 3단계로 수직위치, 회전, 경사를 평가했다. 중등도-중증 정출(≥2 mm)은 24%에 불과했고 18%는 전혀 정출하지 않았으며, 성인기 이후 대합치 소실이면 위험이 낮고, 회전은 상악에서, 경사는 하악에서 더 흔했다. 장기간 대합치가 없더라도 모든 대구치가 정출하지는 않는다 — 이 "비정출" 비율(~18%)은 대합치 없는 공간 보철 여부를 결정하는 핵심 근거로 활용된다

- `bhambhani-2020-choosing-denture-occlusion-systematic-review` [occlusion] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 신설 occlusion 카테고리의 가철성 보철(denture occlusion) 축. [[occlusion/velasquez-2022-occlusal-analysis-natural-dentition-sr]](자연치)와 대비되는 무치악 교합 설계 근거.
  - ▸ 출발(`bhambhani-2020-choosing-denture-occlusion-systematic-review`) 세줄: 총의치 3대 교합양식 — 양측성 균형교합(Bilaterally Balanced Occlusion), 설화교합(Lingualized Occlusion), 단일평면교합(Monoplane Occlusion) — 의 임상 결과(저작 효율, 환자 만족, 치조제 흡수, 안정성·유지력)를 비교한 체계적 고찰이다. 어느 교합양식도 모든 결과에서 보편적으로 우월하지 않았으며, 치조제 형태·신경근 적응력·심미 요구·환자 개별 요인에 따라 선택이 달라진다. 불량한 치조제에는 설화교합이, 신경근 조절이 제한된 환자에는

- `craddock-2007-overeruption-posterior-teeth-partial-occlusal` [occlusion] (HIGH-no-target, 'Overturn' · 결론 뒤집음)
  - **근거 문장**: - Overturns the intuitive assumption that "some contact = stability": partial contact neither reduces overeruption nor stabilises the tooth, and is associated with *more* tipping.
  - ▸ 출발(`craddock-2007-overeruption-posterior-teeth-partial-occlusal`) 세줄: 완전 무대합 또는 부분 교합접촉(Partial Occlusal Contact)만 남은 구치를 가진 성인 91명의 수직 과맹출(Overeruption)과 경사(Tipping)를 비교한 후향적 임상 관찰 연구. 부분 교합접촉은 완전 무대합 대비 과맹출 양을 유의하게 줄이지 못했으며, 부분 대합치는 완전 무대합보다 유의하게 더 많이 경사졌고 부분접촉 존재와 경사 정도 사이에 유의한 상관이 있었다. 부분적 교합접촉은 수직 치아위치를 유지하지 못하므로 이를 기대하는 경과 관찰은 부적절하며, 적극적인 보철 

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: CR is reproducible and clinically validated for diagnostic and full-arch restorative use; no substantive clinical research contradicts this use; the core problem is lack of consensus on CR's definition and recording method, not on the concept itself.
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 세줄: 보철학의 중심위 (Centric Relation, CR) 논쟁을 다룬 서술적 리뷰 (초록만) — "CR 폐기" 주장 (Zonnenberg 2021)에 대한 직접 반론. CR은 재현 가능하고 진단·전악 보철 재건에 임상적으로 검증된 기준위이며, 이를 반박하는 임상 연구 없음; 문제의 핵심은 개념이 아니라 CR의 정의 및 기록 방법 합의 부재. 다른 하악 위치를 사용할 경우 별도 명칭 부여 필요 — 포기가 아닌 용어 규율이 논쟁 해결책; 하악와 내 정확한 과두 위치를 특정할 증거 불충분.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, '반론' · 반론)
  - **근거 문장**: 보철학의 중심위 (Centric Relation, CR) 논쟁을 다룬 서술적 리뷰 (초록만) — "CR 폐기" 주장 (Zonnenberg 2021)에 대한 직접 반론.
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 세줄: 보철학의 중심위 (Centric Relation, CR) 논쟁을 다룬 서술적 리뷰 (초록만) — "CR 폐기" 주장 (Zonnenberg 2021)에 대한 직접 반론. CR은 재현 가능하고 진단·전악 보철 재건에 임상적으로 검증된 기준위이며, 이를 반박하는 임상 연구 없음; 문제의 핵심은 개념이 아니라 CR의 정의 및 기록 방법 합의 부재. 다른 하악 위치를 사용할 경우 별도 명칭 부여 필요 — 포기가 아닌 용어 규율이 논쟁 해결책; 하악와 내 정확한 과두 위치를 특정할 증거 불충분.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: CR은 재현 가능하고 진단·전악 보철 재건에 임상적으로 검증된 기준위이며, 이를 반박하는 임상 연구 없음; 문제의 핵심은 개념이 아니라 CR의 정의 및 기록 방법 합의 부재.
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 세줄: 보철학의 중심위 (Centric Relation, CR) 논쟁을 다룬 서술적 리뷰 (초록만) — "CR 폐기" 주장 (Zonnenberg 2021)에 대한 직접 반론. CR은 재현 가능하고 진단·전악 보철 재건에 임상적으로 검증된 기준위이며, 이를 반박하는 임상 연구 없음; 문제의 핵심은 개념이 아니라 CR의 정의 및 기록 방법 합의 부재. 다른 하악 위치를 사용할 경우 별도 명칭 부여 필요 — 포기가 아닌 용어 규율이 논쟁 해결책; 하악와 내 정확한 과두 위치를 특정할 증거 불충분.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Goldstein responds to the "uprising to abolish" centric relation (CR) — most directly the position advanced by Zonnenberg (2021) — by defending CR as a *needed* reference position rather than a disposable one. The bottom line is deliberately balanced: CR is a **universally recognized term with a long history of clinical success**, and it remains a **reproducible** maxillomandibular reference posit
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 세줄: 보철학의 중심위 (Centric Relation, CR) 논쟁을 다룬 서술적 리뷰 (초록만) — "CR 폐기" 주장 (Zonnenberg 2021)에 대한 직접 반론. CR은 재현 가능하고 진단·전악 보철 재건에 임상적으로 검증된 기준위이며, 이를 반박하는 임상 연구 없음; 문제의 핵심은 개념이 아니라 CR의 정의 및 기록 방법 합의 부재. 다른 하악 위치를 사용할 경우 별도 명칭 부여 필요 — 포기가 아닌 용어 규율이 논쟁 해결책; 하악와 내 정확한 과두 위치를 특정할 증거 불충분.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Defends CR as **reproducible** and clinically validated for **diagnostic and full-arch restorative** use, citing a long track record and the absence of contradicting clinical research.
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 세줄: 보철학의 중심위 (Centric Relation, CR) 논쟁을 다룬 서술적 리뷰 (초록만) — "CR 폐기" 주장 (Zonnenberg 2021)에 대한 직접 반론. CR은 재현 가능하고 진단·전악 보철 재건에 임상적으로 검증된 기준위이며, 이를 반박하는 임상 연구 없음; 문제의 핵심은 개념이 아니라 CR의 정의 및 기록 방법 합의 부재. 다른 하악 위치를 사용할 경우 별도 명칭 부여 필요 — 포기가 아닌 용어 규율이 논쟁 해결책; 하악와 내 정확한 과두 위치를 특정할 증거 불충분.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - Serves as the **counterpoint** to the abandon-CR argument within the CR/CO/MICP terminology debate.
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 세줄: 보철학의 중심위 (Centric Relation, CR) 논쟁을 다룬 서술적 리뷰 (초록만) — "CR 폐기" 주장 (Zonnenberg 2021)에 대한 직접 반론. CR은 재현 가능하고 진단·전악 보철 재건에 임상적으로 검증된 기준위이며, 이를 반박하는 임상 연구 없음; 문제의 핵심은 개념이 아니라 CR의 정의 및 기록 방법 합의 부재. 다른 하악 위치를 사용할 경우 별도 명칭 부여 필요 — 포기가 아닌 용어 규율이 논쟁 해결책; 하악와 내 정확한 과두 위치를 특정할 증거 불충분.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Consensus supports CR as the restorative position for full-arch reconstruction; no substantive clinical research contradicts it.
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 세줄: 보철학의 중심위 (Centric Relation, CR) 논쟁을 다룬 서술적 리뷰 (초록만) — "CR 폐기" 주장 (Zonnenberg 2021)에 대한 직접 반론. CR은 재현 가능하고 진단·전악 보철 재건에 임상적으로 검증된 기준위이며, 이를 반박하는 임상 연구 없음; 문제의 핵심은 개념이 아니라 CR의 정의 및 기록 방법 합의 부재. 다른 하악 위치를 사용할 경우 별도 명칭 부여 필요 — 포기가 아닌 용어 규율이 논쟁 해결책; 하악와 내 정확한 과두 위치를 특정할 증거 불충분.

- `goldstein-2022-centric-relation-needed-reference-position` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[occlusion/zonnenberg-2021-centric-relation-critically-revisited-clinical]] — the abandon-CR view this paper directly rebuts (contradicts).
  - ▸ 출발(`goldstein-2022-centric-relation-needed-reference-position`) 세줄: 보철학의 중심위 (Centric Relation, CR) 논쟁을 다룬 서술적 리뷰 (초록만) — "CR 폐기" 주장 (Zonnenberg 2021)에 대한 직접 반론. CR은 재현 가능하고 진단·전악 보철 재건에 임상적으로 검증된 기준위이며, 이를 반박하는 임상 연구 없음; 문제의 핵심은 개념이 아니라 CR의 정의 및 기록 방법 합의 부재. 다른 하악 위치를 사용할 경우 별도 명칭 부여 필요 — 포기가 아닌 용어 규율이 논쟁 해결책; 하악와 내 정확한 과두 위치를 특정할 증거 불충분.

- `fornai-2022-centric-relation-matter-form-substance` [occlusion] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: Zonnenberg(2021) 반박 서신(새로운 1차 데이터 없음)으로, 기존 문헌을 근거로 치과교정의가 적응 개형(Adaptive Remodelling)에 의존해 과두 위치를 무시해도 된다는 주장에 반박했다.
  - ▸ 출발(`fornai-2022-centric-relation-matter-form-substance`) 세줄: Zonnenberg(2021) 반박 서신(새로운 1차 데이터 없음)으로, 기존 문헌을 근거로 치과교정의가 적응 개형(Adaptive Remodelling)에 의존해 과두 위치를 무시해도 된다는 주장에 반박했다. "중심위(Centric Relation, CR)" 용어 폐기에는 동의하지만(GPT-9 전문가 합의 29%), 임상 결론은 반대: 교합 변경 시 과두 위치를 반드시 모니터링해야 하며, 적응 개형은 염증·퇴행성 관절에서 감소하고 성인에서 제한적이며, 무증상 개체에서 2 mm 초과 활주가 전혀 

- `fornai-2022-centric-relation-matter-form-substance` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[occlusion/zonnenberg-2021-centric-relation-critically-revisited-clinical]] — the rebutted review (concludes condylar position can be disregarded in most orthodontic patients); this paper directly contradicts its clinical recommendation.
  - ▸ 출발(`fornai-2022-centric-relation-matter-form-substance`) 세줄: Zonnenberg(2021) 반박 서신(새로운 1차 데이터 없음)으로, 기존 문헌을 근거로 치과교정의가 적응 개형(Adaptive Remodelling)에 의존해 과두 위치를 무시해도 된다는 주장에 반박했다. "중심위(Centric Relation, CR)" 용어 폐기에는 동의하지만(GPT-9 전문가 합의 29%), 임상 결론은 반대: 교합 변경 시 과두 위치를 반드시 모니터링해야 하며, 적응 개형은 염증·퇴행성 관절에서 감소하고 성인에서 제한적이며, 무증상 개체에서 2 mm 초과 활주가 전혀 

- `zonnenberg-2021-centric-relation-critically-revisited-clinical` [occlusion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[occlusion/goldstein-2022-centric-relation-needed-reference-position]] — counter-position arguing CR remains a needed reference position (this page contradicts it).
  - ▸ 출발(`zonnenberg-2021-centric-relation-critically-revisited-clinical`) 세줄: 약 70년간의 중심위(Centric Relation, CR) 관련 문헌을 검토한 서술적 비판 리뷰로, 반복적인 정의 변경과 그 임상적 결과를 분석. CR 용어는 후퇴위에서 전상방 과두위로 수차례 재정의되어 불필요한 CR 채득·과두위 평가·교합 치료를 야기하는 지속적 혼란을 초래. 저자들은 CR이 의미·개념·실용 면에서 결함이 있어 폐기해야 하며, 건강한 유치악 환자에서는 최대교두감합(Maximum Intercuspation, MIP)이 생물학적으로 수용 가능한 기준위라고 결론 — 일상적 과두위 평

- `scannapieco-2021-dysbiosis-oral-microbiome-periodontitis` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[oral-microbiology/hajishengallis-2012-psd-model-periodontal-disease]] — the keystone-pathogen/PSD dysbiosis model that this commentary directly critiques as a poor fit for common (diversity-increasing) periodontitis (contradicts/refines)
  - ▸ 출발(`scannapieco-2021-dysbiosis-oral-microbiome-periodontitis`) 세줄: 치은염·치주염 병인론에서 "미생물 dysbiosis(불균형)" 개념이 실제로 타당한지 재검토한 비평 논평(J Periodontol, 2021) — 장·피부 질환의 고전적 dysbiosis 기준과 치주 문헌을 대조. 전신적으로 건강한 성인의 흔한 치주염은 건강 상태보다 오히려 미생물 다양성이 증가하는 양상을 보여(IBD·피부염 등 고전적 dysbiosis는 다양성 감소가 특징), 소수 병원균(keystone pathobiont) 과증식이 아니라 진화적으로 안정된 다양한 공생균총의 총 생물량·대사활성

- `scannapieco-2021-dysbiosis-oral-microbiome-periodontitis` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[oral-microbiology/lamont-2014-polymicrobial-synergy-dysbiosis-inflammatory]] — broader PSD/inflammatory-disease extension that shares the keystone-pathogen framing this paper questions (contradicts)
  - ▸ 출발(`scannapieco-2021-dysbiosis-oral-microbiome-periodontitis`) 세줄: 치은염·치주염 병인론에서 "미생물 dysbiosis(불균형)" 개념이 실제로 타당한지 재검토한 비평 논평(J Periodontol, 2021) — 장·피부 질환의 고전적 dysbiosis 기준과 치주 문헌을 대조. 전신적으로 건강한 성인의 흔한 치주염은 건강 상태보다 오히려 미생물 다양성이 증가하는 양상을 보여(IBD·피부염 등 고전적 dysbiosis는 다양성 감소가 특징), 소수 병원균(keystone pathobiont) 과증식이 아니라 진화적으로 안정된 다양한 공생균총의 총 생물량·대사활성

- `dasilva-2022-periodontal-status-salivary-leptin-sle` [periodontics] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: [[periodontics/dolcezza-2024-rheumatoid-arthritis-periodontal-disease-sr-ma]]로 이미 RA에서는 치주치료가 전신 질병활성도(DAS28)를 유의하게 낮춘다는 근거를 위키에 확보했는데, 같은 자가면역질환 계열인 SLE에서도 치주-전신 연결이 성립하는지 확인하려고 인제스트. 그러나 이 case-control 연구(n=38 SLE vs n=29 대조군)의 SEM 분석 결과는 대비되는 방향 — 타액 렙틴(salivary leptin)이 SLE 자체와는 유의한 역상관(표준화계수 −0.289, P=0.023)을 보이지만, 치주 상태(PPD·CAL·BOP 잠재변수)와는 유의한 직접효과가 없었다(SLE 그룹 내 상관도 비유의). 즉 "치주 개입이 전신 자가면역 바
  - ▸ 출발(`dasilva-2022-periodontal-status-salivary-leptin-sle`) 세줄: 케이스-대조군 연구 (전신홍반루푸스, Systemic Lupus Erythematosus, SLE 환자 38명(전원 여성, 평균 39.6세) vs 건강대조군 29명(평균 46.3세); 브라질 상루이스) — 치주 임상지표(치주낭깊이, Periodontal Probing Depth, PPD; 임상부착소실, Clinical Attachment Level, CAL; 탐침시출혈, Bleeding on Probing, BOP)와 자극 타액 렙틴(leptin)을 측정, 구조방정식모형(Structural Equ

- `lamont-2018-routine-scale-and-polish-periodontal-health` [periodontics] (SOFT→farina-2026-pmpr-biofilm-gingivitis-sr-ma, 'whereas' · 반면(대조))
  - **근거 문장**: - [[periodontics/farina-2026-pmpr-biofilm-gingivitis-sr-ma]] — contrast: PMPR adds benefit as an adjunct to OHI in *established* gingivitis, whereas this review finds no benefit of *routine* prophylaxis in low-risk healthy adults (different population/question).
  - ▸ 출발(`lamont-2018-routine-scale-and-polish-periodontal-health`) 세줄: 코크란 SR+MA (RCT 2편, n=1711, 영국 일반 치과) — 중증 치주염 없는 정기 내원 성인에서 6개월·12개월 루틴 스케일링·폴리싱 대 무처치를 2~3년간 비교. 루틴 스케일링·폴리싱은 치은염·치주낭 깊이·구강건강 삶의 질에 거의 차이 없음(고신뢰도); 치석만 소폭 감소(6개월 > 12개월)하나 임상적 의의 불분명. 저위험 건강 성인에서 고정 간격 예방처치는 치주건강에 근거가 없으며, 개인 위험도 기반 리콜로의 전환을 지지.
  - ▸ 대상(`farina-2026-pmpr-biofilm-gingivitis-sr-ma`) 세줄: EFP 21차 워크숍 SR+MA (11편, 주로 RCT): 판막방해 인자 없는 성인의 치태-유발 치은염에서 전문가 기계적 치태제거 (Professional Mechanical Plaque Removal, PMPR)에 대한 3개 집중 질문 검토. PMPR 단독은 구강위생 불량 지속 환자에서 효과 없음; PMPR+구강위생교육(OHI) > OHI 단독 (low certainty); 에어폴리싱+초음파 = 초음파+러버컵 폴리싱 (효과 동등, 더 빠름, very low certainty); 다이오드 레이저 

- `maybodi-2022-periodontal-treatment-sle-disease-activity-rct` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Found periodontal treatment produced a statistically significant between-group CRP reduction (P=0.032), contradicting Fabbri et al.'s null CRP/ESR finding.
  - ▸ 출발(`maybodi-2022-periodontal-treatment-sle-disease-activity-rct`) 세줄: 이중맹검 RCT, 활동성 SLE + 치주염 환자 90명(SRP+구강위생교육군 45명 vs 구강위생교육단독군 45명), 3개월 추적. SRP군은 치주지표가 임상적으로 유의하게 개선(PD −2.10mm, CAL −2.02mm)되었고 CRP는 군간 유의한 차이(P=0.032)를 보였으나, SLEDAI 변화는 군간 유의한 차이가 없었음(P=0.894). 비외과적 치주치료는 SLE 환자의 급성기 염증표지자(CRP, ESR 경향)는 낮추지만 3개월 시점 전신 루푸스 질병활동도 자체를 유의하게 바꾸지는 못함 

- `maybodi-2022-periodontal-treatment-sle-disease-activity-rct` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Found SLEDAI improved in both groups with no significant between-group difference, contradicting Fabbri et al.'s finding of a significant SLEDAI benefit from periodontal treatment — an open contradiction in this small literature.
  - ▸ 출발(`maybodi-2022-periodontal-treatment-sle-disease-activity-rct`) 세줄: 이중맹검 RCT, 활동성 SLE + 치주염 환자 90명(SRP+구강위생교육군 45명 vs 구강위생교육단독군 45명), 3개월 추적. SRP군은 치주지표가 임상적으로 유의하게 개선(PD −2.10mm, CAL −2.02mm)되었고 CRP는 군간 유의한 차이(P=0.032)를 보였으나, SLEDAI 변화는 군간 유의한 차이가 없었음(P=0.894). 비외과적 치주치료는 SLE 환자의 급성기 염증표지자(CRP, ESR 경향)는 낮추지만 3개월 시점 전신 루푸스 질병활동도 자체를 유의하게 바꾸지는 못함 

- `cosin-villanueva-2024-micrornas-gingival-crevicular-fluid-periodontal` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Study characteristics**: 16 observational case-control studies; sample sizes 18–216; mean ages 27.8–65.3 y. Two-thirds used the 2018 periodontal classification, one-third the Armitage classification. Most miRNAs were **upregulated** in disease, with some contradictory reports.
  - ▸ 출발(`cosin-villanueva-2024-micrornas-gingival-crevicular-fluid-periodontal`) 세줄: PRISMA 체계적 고찰(PROSPERO CRD42024544648) — 치은열구액(Gingival Crevicular Fluid, GCF) miRNA를 치주질환 진단 바이오마커로 평가한 16편 환자대조군 연구(3222건 스크린, 연구당 n=18–216); 이질성으로 메타분석 불가. AUC >0.8 기준으로 miR-146a·miR-200b(특히 miR-200b-3p)·miR-223·miR-23a는 치주염 진단 타당성 적정; miR-203은 적격 미달(VEGFA 표적, 발현 감소 — 치료 표적 후보

- `fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: CoQ10 gel marketed for gum health lacks efficacy evidence; oral 120 mg/day shows a signal but is overall very-low-certainty evidence, insufficient for an evidence-based recommendation and contradicting the earlier pooled MA (Rasoolzadeh 2022) that mixed delivery routes.
  - ▸ 출발(`fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr`) 세줄: PROSPERO 등록 체계적 고찰 (10편 RCT, 검색 2024년 5월까지): SRP 보조제로서의 코엔자임 Q10 (CoQ10)을 투여 경로별(국소 겔 vs 경구 보충제)로 층화 분석. 국소 CoQ10 겔(도포/치주낭내)은 치주낭깊이(PD)·임상부착수준(CAL)에 유의한 효과 없음; 경구 120 mg/일은 12주 시 소폭 유의 개선(PD −0.41 mm; CAL −0.52 mm). '잇몸 제품'으로 판매되는 CoQ10 겔은 근거 없음; 경구 120 mg/일은 신호는 있으나 근거 확실성 very 

- `fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr` [periodontics] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: '잇몸 제품'으로 판매되는 CoQ10 겔은 근거 없음; 경구 120 mg/일은 신호는 있으나 근거 확실성 very low로 권고 불가, 투여 경로를 혼합하여 겔 효과를 과장한 이전 MA (Rasoolzadeh 2022)와 직접 상충한다.
  - ▸ 출발(`fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr`) 세줄: PROSPERO 등록 체계적 고찰 (10편 RCT, 검색 2024년 5월까지): SRP 보조제로서의 코엔자임 Q10 (CoQ10)을 투여 경로별(국소 겔 vs 경구 보충제)로 층화 분석. 국소 CoQ10 겔(도포/치주낭내)은 치주낭깊이(PD)·임상부착수준(CAL)에 유의한 효과 없음; 경구 120 mg/일은 12주 시 소폭 유의 개선(PD −0.41 mm; CAL −0.52 mm). '잇몸 제품'으로 판매되는 CoQ10 겔은 근거 없음; 경구 120 mg/일은 신호는 있으나 근거 확실성 very 

- `fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This contradicts the earlier pooled meta-analysis **Rasoolzadeh 2022**, which mixed routes and gingivitis-leaning indices (Plaque/Bleeding/Gingival index) and concluded *in favour* of CoQ10 gel. The disagreement is methodological: pooling routes inflates the apparent gel benefit. For practice, CoQ10 should be presented to patients as low/very-low-certainty, route-dependent, and adjunctive only — n
  - ▸ 출발(`fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr`) 세줄: PROSPERO 등록 체계적 고찰 (10편 RCT, 검색 2024년 5월까지): SRP 보조제로서의 코엔자임 Q10 (CoQ10)을 투여 경로별(국소 겔 vs 경구 보충제)로 층화 분석. 국소 CoQ10 겔(도포/치주낭내)은 치주낭깊이(PD)·임상부착수준(CAL)에 유의한 효과 없음; 경구 120 mg/일은 12주 시 소폭 유의 개선(PD −0.41 mm; CAL −0.52 mm). '잇몸 제품'으로 판매되는 CoQ10 겔은 근거 없음; 경구 120 mg/일은 신호는 있으나 근거 확실성 very 

- `fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[periodontics/rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma]] — earlier CoQ10 SR+MA endorsing gel; the direct contradiction (route-pooling artifact).
  - ▸ 출발(`fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr`) 세줄: PROSPERO 등록 체계적 고찰 (10편 RCT, 검색 2024년 5월까지): SRP 보조제로서의 코엔자임 Q10 (CoQ10)을 투여 경로별(국소 겔 vs 경구 보충제)로 층화 분석. 국소 CoQ10 겔(도포/치주낭내)은 치주낭깊이(PD)·임상부착수준(CAL)에 유의한 효과 없음; 경구 120 mg/일은 12주 시 소폭 유의 개선(PD −0.41 mm; CAL −0.52 mm). '잇몸 제품'으로 판매되는 CoQ10 겔은 근거 없음; 경구 120 mg/일은 신호는 있으나 근거 확실성 very 

- `fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: CoQ10 ("잇몸 영양제") is one of the most heavily marketed periodontal supplements, yet the wiki held **zero pages** on it. This Fernandez 2025 SR is the cited evidence behind the CoQ10 claim and the most current (search to May 2024), most methodologically careful answer: it **stratifies by administration route**, which is exactly what resolves the controversy — local CoQ10 gel shows no effect on PD/CAL
  - ▸ 출발(`fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr`) 세줄: PROSPERO 등록 체계적 고찰 (10편 RCT, 검색 2024년 5월까지): SRP 보조제로서의 코엔자임 Q10 (CoQ10)을 투여 경로별(국소 겔 vs 경구 보충제)로 층화 분석. 국소 CoQ10 겔(도포/치주낭내)은 치주낭깊이(PD)·임상부착수준(CAL)에 유의한 효과 없음; 경구 120 mg/일은 12주 시 소폭 유의 개선(PD −0.41 mm; CAL −0.52 mm). '잇몸 제품'으로 판매되는 CoQ10 겔은 근거 없음; 경구 120 mg/일은 신호는 있으나 근거 확실성 very 

- `ifrim-2026-edta-air-polishing-root-surface-sem` [periodontics] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: EDTA+에어폴리싱 분말 병용이 SRP 단독 대비 스미어층을 의미 있게 감소시키지 못하고 에리스리톨은 기구흔-균열 상충을 초래; 그룹당 치아 2개의 탐색적 연구로 임상 프로토콜 변경 전 확증 연구 필요.
  - ▸ 출발(`ifrim-2026-edta-air-polishing-root-surface-sem`) 세줄: 치주염 발치치 10개(시편 20개) SEM 인비트로 연구: 3가지 치근면 처리 프로토콜 — SRP+EDTA(S), SRP+에리스리톨 에어폴리싱+EDTA(Se), SRP+글라이신 에어폴리싱+EDTA(Sg) — 를 기구흔·균열·스미어층(smear layer) 순서 점수로 비교. 에리스리톨 에어폴리싱은 기구흔 감소(Se<S, p=0.001)하나 균열 증가(Se>S, p=0.001); 글라이신은 SRP 단독과 유의 차 없음; 스미어층 점수는 모든 프로토콜 동등(p=0.950); CEJ는 기구흔에서만 치근

- `botelho-2022-umbrella-review-oral-systemic` [periodontics] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 암 5종·당뇨·심혈관질환·류마티스관절염·염증성장질환·다낭성난소증후군·비만·천식을 포함한 28개 NCD가 구강질환(주로 치주염)과 강한 연관성을 보였으나, AMSTAR2 방법론적 질이 high/moderate인 메타분석은 10.3%에 불과했고, fail-safe number 분석상 suggestive~strong 연관성의 97.5%는 향후 연구로도 뒤집히기 어려운 것으로 나타남.
  - ▸ 출발(`botelho-2022-umbrella-review-oral-systemic`) 세줄: 293편의 SR/MA(855개 비교)를 종합한 엄브렐라 리뷰로, 구강질환과 전신 비전염성질환(Noncommunicable Disease, NCD)의 양방향 연관성을 평가함 (PROSPERO CRD42022300740). 암 5종·당뇨·심혈관질환·류마티스관절염·염증성장질환·다낭성난소증후군·비만·천식을 포함한 28개 NCD가 구강질환(주로 치주염)과 강한 연관성을 보였으나, AMSTAR2 방법론적 질이 high/moderate인 메타분석은 10.3%에 불과했고, fail-safe number 분석상 

- `botelho-2022-umbrella-review-oral-systemic` [periodontics] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: - **Robustness**: FSN indicates 97.5% of suggestive-to-strong associations are unlikely to be overturned by future null studies (median FSN 51, range 1–87,973).
  - ▸ 출발(`botelho-2022-umbrella-review-oral-systemic`) 세줄: 293편의 SR/MA(855개 비교)를 종합한 엄브렐라 리뷰로, 구강질환과 전신 비전염성질환(Noncommunicable Disease, NCD)의 양방향 연관성을 평가함 (PROSPERO CRD42022300740). 암 5종·당뇨·심혈관질환·류마티스관절염·염증성장질환·다낭성난소증후군·비만·천식을 포함한 28개 NCD가 구강질환(주로 치주염)과 강한 연관성을 보였으나, AMSTAR2 방법론적 질이 high/moderate인 메타분석은 10.3%에 불과했고, fail-safe number 분석상 

- `farina-2026-pmpr-biofilm-gingivitis-sr-ma` [periodontics] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: "Oral prophylaxis" 요청의 두 번째 코어 논문. 21st European Workshop on Periodontology(EFP) Working Group 1 SR로, [[periodontics/lamont-2018-routine-scale-and-polish-periodontal-health]](저위험 성인 루틴 프로필락시스 무효)과 대비되는 **established gingivitis 치료 맥락**에서 PMPR의 역할을 규명한다 — OHI가 1차, PMPR은 OHI에 대한 adjunct일 때만 이득. 또한 [[periodontics/cyris-2024-guided-biofilm-therapy-versus-conventional]]·[[overviews/professional-biofilm-
  - ▸ 출발(`farina-2026-pmpr-biofilm-gingivitis-sr-ma`) 세줄: EFP 21차 워크숍 SR+MA (11편, 주로 RCT): 판막방해 인자 없는 성인의 치태-유발 치은염에서 전문가 기계적 치태제거 (Professional Mechanical Plaque Removal, PMPR)에 대한 3개 집중 질문 검토. PMPR 단독은 구강위생 불량 지속 환자에서 효과 없음; PMPR+구강위생교육(OHI) > OHI 단독 (low certainty); 에어폴리싱+초음파 = 초음파+러버컵 폴리싱 (효과 동등, 더 빠름, very low certainty); 다이오드 레이저 

- `rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma` [periodontics] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: The pro-CoQ10 conclusion is likely an artifact of pooling heterogeneous routes and biased trials; the newer route-stratified SR (Fernandez 2025) finds the gel route null, making this page the cautionary counterpoint in the CoQ10 evidence pair.
  - ▸ 출발(`rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma`) 세줄: SR+MA (11편 대조 연구, 1980–2020.08) — CoQ10의 치주치료 보조 효과를 5개 지표(치면세균막·출혈·치주낭 깊이·부착 수준·치은 지수)에서 평가. CoQ10은 5개 지표 모두 유의하게 개선(치주낭 SMD −0.96, 출혈 지수 SMD −1.05); 인트라포켓 투여 > 국소 도포; 단 전 지표 I² 72–89% (이질성 매우 높음), 비뚤림 위험 높은 연구일수록 효과 과대. 친-CoQ10 결론은 투여 경로 혼합·비뚤림 연구 효과 과대의 결과일 가능성; 신형 route-strat

- `rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma` [periodontics] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - Serves as the cautionary counterpoint to the route-stratified 2025 SR.
  - ▸ 출발(`rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma`) 세줄: SR+MA (11편 대조 연구, 1980–2020.08) — CoQ10의 치주치료 보조 효과를 5개 지표(치면세균막·출혈·치주낭 깊이·부착 수준·치은 지수)에서 평가. CoQ10은 5개 지표 모두 유의하게 개선(치주낭 SMD −0.96, 출혈 지수 SMD −1.05); 인트라포켓 투여 > 국소 도포; 단 전 지표 I² 72–89% (이질성 매우 높음), 비뚤림 위험 높은 연구일수록 효과 과대. 친-CoQ10 결론은 투여 경로 혼합·비뚤림 연구 효과 과대의 결과일 가능성; 신형 route-strat

- `rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[periodontics/fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr]] — newer route-stratified SR finding gel null; the direct contradiction.
  - ▸ 출발(`rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma`) 세줄: SR+MA (11편 대조 연구, 1980–2020.08) — CoQ10의 치주치료 보조 효과를 5개 지표(치면세균막·출혈·치주낭 깊이·부착 수준·치은 지수)에서 평가. CoQ10은 5개 지표 모두 유의하게 개선(치주낭 SMD −0.96, 출혈 지수 SMD −1.05); 인트라포켓 투여 > 국소 도포; 단 전 지표 I² 72–89% (이질성 매우 높음), 비뚤림 위험 높은 연구일수록 효과 과대. 친-CoQ10 결론은 투여 경로 혼합·비뚤림 연구 효과 과대의 결과일 가능성; 신형 route-strat

- `mendonca-2024-effects-probiotic-therapy-periodontal` [periodontics] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 근거가 상충하여 프로바이오틱스 보조요법에 대한 찬반 확정적 결론 불가; 포함된 SR 중 골소실·임플란트 생존율·발치율을 보고한 것은 없었고, 교란변수를 통제한 고품질 1차 RCT가 필요함.
  - ▸ 출발(`mendonca-2024-effects-probiotic-therapy-periodontal`) 세줄: 우산리뷰(umbrella review, PRISMA/PROSPERO 등록) — 성인 치주질환(periodontal disease)·임플란트주위질환(peri-implant disease) 환자에서 비수술치료 보조요법으로서 프로바이오틱스(probiotics) 효과를 다룬 체계적 문헌고찰(Systematic Review, SR) 30편 종합; 임상적 이질성이 커 SR 간 메타분석은 불가능했음. 31편 중 17편이 임상적으로 유의미한 이득 보고; SR 수준 근거는 치아(tooth) 기질에서 단기(3개월 

- `mendonca-2024-effects-probiotic-therapy-periodontal` [periodontics] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 기존 [[overviews/periodontal-adjunctive-therapy-probiotics-pdt-overview]]은 2026년 개별 RCT(Lundtorp-Olsen, Jeon)에서 프로바이오틱스가 BoP·심부포켓 수를 유의 감소시킨다는 근거를 다루지만, umbrella review 수준의 상위 근거는 아직 없었다. 본 논문(Mendonça 2024, PROSPERO 등록 umbrella review, SR 30편)은 그 근거 기반을 SR 메타수준에서 재검토해 "결과가 상충하며 확정적 결론 불가"라는 신중한 caveat을 제공하여, overview의 ~0.3mm CAL ceiling 프레이밍을 보강한다.
  - ▸ 출발(`mendonca-2024-effects-probiotic-therapy-periodontal`) 세줄: 우산리뷰(umbrella review, PRISMA/PROSPERO 등록) — 성인 치주질환(periodontal disease)·임플란트주위질환(peri-implant disease) 환자에서 비수술치료 보조요법으로서 프로바이오틱스(probiotics) 효과를 다룬 체계적 문헌고찰(Systematic Review, SR) 30편 종합; 임상적 이질성이 커 SR 간 메타분석은 불가능했음. 31편 중 17편이 임상적으로 유의미한 이득 보고; SR 수준 근거는 치아(tooth) 기질에서 단기(3개월 

- `dasilveira-2026-subgingival-irrigation-chemical-agents-nspt-sr-ma` [periodontics] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: The bottom line: **adjunctive CA subgingival irrigation provides no additional clinical benefit over NSPT alone** for PPD reduction, CAL gain, or BOP, with evidence rated low to very low (GRADE). This updates and partially overturns Van der Sluijs 2016 (which had reported a slight PVP-I CAL gain not confirmed here). The authors invoke antimicrobial-stewardship: in the absence of demonstrated benef
  - ▸ 출발(`dasilveira-2026-subgingival-irrigation-chemical-agents-nspt-sr-ma`) 세줄: NSPT 중 약제(PVP-I·CHX·정유·오존수·붕산) 치은연하 세척이 물/식염수 대비 추가 이득을 주는지 평가한 16편 RCT(712명; ≥3개월 추적) SR+MA(PRISMA; PROSPERO 1011516). PPD(MD 0.01 mm)·CAL(MD 0.09 mm)·BOP 감소 모두 추가 이득 없음; 약제별·세척방법별·추적기간별·치근분지별 하위분석에서도 음성 결과 유지; 근거수준 낮음~매우낮음(GRADE). 항균제 내성 관리 원칙하에 NSPT 중 약제 치은연하 세척의 일상적 사용은 현재 근거

- `dasilveira-2026-subgingival-irrigation-chemical-agents-nspt-sr-ma` [periodontics] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 기존 [[periodontics/ramanauskaite-2020-antiseptics-adjuncts-scaling-root-planing]]가 항균제를 SRP 보조로 다룬 반면, 이 2026 SR+MA는 **약제(PVP-I/CHX/EO/OW/BA)를 치은연하 세척(subgingival irrigation)으로 전달**하는 좁은 시나리오만 16편 RCT로 모아, 어떤 약제·전달법(시린지 vs 초음파)·추적기간에서도 PPD·CAL·BOP에 추가 이득이 없음을 보여 "세척 보조"라는 흔한 임상 습관의 근거 결핍을 정량화한다. [[periodontics/khattri-2020-adjunctive-systemic-antimicrobials-non-surgical-treatment]]의 전신 항균제 논의와 대비되는
  - ▸ 출발(`dasilveira-2026-subgingival-irrigation-chemical-agents-nspt-sr-ma`) 세줄: NSPT 중 약제(PVP-I·CHX·정유·오존수·붕산) 치은연하 세척이 물/식염수 대비 추가 이득을 주는지 평가한 16편 RCT(712명; ≥3개월 추적) SR+MA(PRISMA; PROSPERO 1011516). PPD(MD 0.01 mm)·CAL(MD 0.09 mm)·BOP 감소 모두 추가 이득 없음; 약제별·세척방법별·추적기간별·치근분지별 하위분석에서도 음성 결과 유지; 근거수준 낮음~매우낮음(GRADE). 항균제 내성 관리 원칙하에 NSPT 중 약제 치은연하 세척의 일상적 사용은 현재 근거

- `mucogingival-surgery-apf-fgg-ctg` [periodontics] (HIGH-no-target, '반론' · 반론)
  - **근거 문장**: - **KT "필요 최소치" 논쟁**: 고전적 2mm 각화치은 / 1mm 부착치은 기준은 절대 기준이 아니라는 반론 — 구강위생이 유지되면 KT가 좁아도 부착소실이 진행되지 않는다는 보고. FGG 적응은 수치보다 진행성 퇴축·증상·보철 계획 같은 동적 요인으로 판단하는 흐름. [미검증](원전 미확인, 기억 기반)
  - ▸ 출발(`mucogingival-surgery-apf-fgg-ctg`) 세줄: 3가지 치주성형 술식의 임상 선택 기준 정리: 치은판막근단변위술(APF, 이식편 없이 낭감소), 유리치은이식술(FGG, 상피포함 전층이식으로 각화치은 폭증), 결합조직이식술(CTG, 상피하 결합조직이식으로 피개·심미). APF는 기존 각화치은 충분할 때; FGG는 KT 폭증(Shakiliyeva 2025 RCT: 치은단위이식 기법이 수축 감소 우수); CTG는 치근피개·심미부위 황금표준(Cairo RT1~RT2, Miller I~II). 임상 의사결정은 3갈래 분기점 기준: 기존 각화치은 충분 여

- `ramirez-martinez-acitores-2020-antihypertensive-xerostomia-salivary-flow-sr` [oral-medicine] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 2. **Clinical trials (5 studies)**: only Nederfors et al. 2004 assessed xerostomia degree directly, finding thiazide/furosemide groups' xerostomia levels increased vs. stable placebo. Only 1/5 trials found a statistically significant unstimulated whole saliva (UWS) decrease (with an α-/β-adrenergic blocker combination, propranolol+phentolamine); one trial found a statistically significant stimulat
  - ▸ 출발(`ramirez-martinez-acitores-2020-antihypertensive-xerostomia-salivary-flow-sr`) 세줄: PRISMA 체계적 문헌고찰 (13편: 임상시험 5 + 환자대조군 8) — 항고혈압제(베타차단제·ACE억제제·이뇨제·칼슘채널차단제·중추성 제제) 복용군 vs 무처치 대조군의 구강건조증·침분비저하 비교. 항고혈압제 복용군이 대조군보다 구강건조증/침분비저하가 더 심하다는 결론 불가; 임상시험은 혼재·비유의(캅토프릴은 이하선 침분비 유의 증가), 환자대조군은 대체로 침분비 감소 경향 — 그러나 전반적 방법론 질 낮음~보통. 가장 침분비저하를 일으키는 약물군 특정 불가; 13편 모두 유일한 검증 도구인 

- `bisla-2022-odontogenic-infections-maxillary-sinus-changes` [oral-medicine] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 2. **Periapical lesion size does not predict mucosal change** severity (p=0.646) — contradicts some prior literature (Nunes et al.) but consistent with others (Aksoy et al.).
  - ▸ 출발(`bisla-2022-odontogenic-infections-maxillary-sinus-changes`) 세줄: 단면 분석 CBCT 연구 (n=213, 상악동 404개; 치성 감염군 111명 vs 대조군 102명; CS 9300; 인도): MS 평가 점수 0–6과 로지스틱 회귀로 상악동 점막변화 예측인자 평가. 전체 점막변화 유병률 49.5%; 치주골소실(OR 2.2)이 치근단병소 크기(p=0.646, 유의차 없음)나 동 저부 근접성(p=0.49, 유의차 없음)보다 강한 예측인자; 중증 치주골소실 → 72% 점막비후(p=0.008). 치주골소실이 치근단병소보다 상악동 점막비후의 주요 치성 원인; CBCT 기

- `nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy` [oral-medicine] (AMBIG→poudel-2026-xerostomia-dental-treatment-outcomes-sr, '뒤집' · 뒤집음)
  - **근거 문장**: 기존 위키에는 침(saliva)이 질병의 *결과물*(COVID 후유증)로만 나타난다 — [[oral-medicine/tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva]]. 이 JADA 리뷰는 침을 *진단 매체*로 뒤집는 관점(salivaomics·exosomics·liquid biopsy)을 도입해, 침샘 기능/구강건조 라인([[oral-medicine/poudel-2026-xerostomia-dental-treatment-outcomes-sr]])과 대비되는 "침의 진단적 활용" 축을 새로 연다. Wong 그룹(UCLA)의 salivaomics 프레임워크 원전으로, 향후 침 바이오마커 overview의 앵커.
  - ▸ 출발(`nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`) 세줄: 전문가 서술 리뷰(JADA 2023, Wong/UCLA 그룹) — 침 진단(saliva diagnostics)을 살리바오믹스(salivaomics)·침 엑소좀학(saliva exosomics)·침 액체생검(saliva liquid biopsy) 세 축으로 분류, 침·혈장 단백질체 20–30% 중첩으로 전신 바이오마커의 침샘 이송 가능성 지지. 전기화학 센서 EFIRM(Electric Field–Induced Release and Measurement)은 추출·증폭 없이 40–50 µL 침에서 폐암

- `pan-2025-acupuncture-neuropathic-orofacial-pain-review` [oral-medicine] (HIGH-no-target, 'conflicting result' · 상충 결과)
  - **근거 문장**: Evidence is presented as generally favorable (reduced pain intensity, improved quality of life, good safety) across all four subtypes, but the review itself flags that most primary studies are small, methodologically heterogeneous, and non-standardized in acupoint/protocol selection with short follow-up; for TMD it explicitly notes conflicting results (some trials showing no advantage over sham).
  - ▸ 출발(`pan-2025-acupuncture-neuropathic-orofacial-pain-review`) 세줄: 신경병증성 구강안면통증 (Neuropathic Orofacial Pain, NOP)에 대한 침술 (Acupuncture) narrative review — 삼차신경통 (Trigeminal Neuralgia, TN)·구강작열감증후군 (Burning Mouth Syndrome, BMS)·측두하악장애 (Temporomandibular Disorders, TMD)·대상포진후신경통 (Postherpetic Neuralgia, PHN) 4개 아형의 신경화학적/항염 기전과 1차 연구(대부분 개별 RCT, TN

- `pan-2025-acupuncture-neuropathic-orofacial-pain-review` [oral-medicine] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: 전반적으로 통증감소·삶의 질 개선·양호한 안전성 등 우호적으로 서술되지만, 저자 스스로도 대부분 1차 연구가 소규모·방법론적 이질성·경혈/프로토콜 비표준화·단기 추적임을 인정하며, TMD 항목에서는 sham 대비 우월성이 없었다는 상반된 결과도 명시.
  - ▸ 출발(`pan-2025-acupuncture-neuropathic-orofacial-pain-review`) 세줄: 신경병증성 구강안면통증 (Neuropathic Orofacial Pain, NOP)에 대한 침술 (Acupuncture) narrative review — 삼차신경통 (Trigeminal Neuralgia, TN)·구강작열감증후군 (Burning Mouth Syndrome, BMS)·측두하악장애 (Temporomandibular Disorders, TMD)·대상포진후신경통 (Postherpetic Neuralgia, PHN) 4개 아형의 신경화학적/항염 기전과 1차 연구(대부분 개별 RCT, TN

- `pan-2025-acupuncture-neuropathic-orofacial-pain-review` [oral-medicine] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 기존 [[wiki/oral-medicine/khan-2023-trigeminal-neuralgia-therapeutic-approach-sr]]는 삼차신경통 (Trigeminal Neuralgia, TN)의 약물 사다리(카르바마제핀 1차)를 정리했지만 침술 (Acupuncture) 같은 비약물 대안은 다루지 않았다. 본 narrative review는 TN·구강작열감증후군 (Burning Mouth Syndrome, BMS)·측두하악장애 (Temporomandibular Disorders, TMD)·대상포진후신경통 (Postherpetic Neuralgia, PHN) 전반에 걸친 침술의 기전·임상근거를 정리해 신경병증성 구강안면통증 (Neuropathic Orofacial Pain, NOP) 관리 옵션을 확
  - ▸ 출발(`pan-2025-acupuncture-neuropathic-orofacial-pain-review`) 세줄: 신경병증성 구강안면통증 (Neuropathic Orofacial Pain, NOP)에 대한 침술 (Acupuncture) narrative review — 삼차신경통 (Trigeminal Neuralgia, TN)·구강작열감증후군 (Burning Mouth Syndrome, BMS)·측두하악장애 (Temporomandibular Disorders, TMD)·대상포진후신경통 (Postherpetic Neuralgia, PHN) 4개 아형의 신경화학적/항염 기전과 1차 연구(대부분 개별 RCT, TN

- `jkda-2025-63-8-006` [dental-history] (HIGH-no-target, 'counter to' · 반대)
  - **근거 문장**: Ham founded the Hansung Dental Association as a Korean counter to Japanese dental organizations, establishing multiple "firsts" in Korean dental history and anchoring the professional identity thread that leads to the modern Korean Dental Association.
  - ▸ 출발(`jkda-2025-63-8-006`) 세줄: 한국 최초 정규 치과대학 졸업자·등록 치과의사인 함석태(1889–?)를 기록한 역사적 내러티브 논문 (변웅래, 대한치과의사협회지 2025; 1차 사료 접근 제한 있음) — 일제강점기(1910–1945) 배경. 함석태는 일본 치과단체에 대응해 한성치과의사회를 창립하고 한국 치과 역사의 다수 "최초" 기록을 남겨, 현 대한치과의사협회로 이어지는 전문직 정체성의 출발점이 됨. 한국 조직 치과학의 기원을 추적하는 학술·기념·환자 교육 자료에서 전문직 정체성 역사 참고문헌으로 활용.

- `zaki-2021-bone-substitute-materials-immediate-implant-sr-ma` [immediate-implant] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 즉시식립 gap 이식은 협측골·심미 보존에 유효하나 합병증 증가 상충(trade-off)을 고려해야 하며, RCT 기반 최대 메타분석으로 gap 이식 결정의 기준 문헌.
  - ▸ 출발(`zaki-2021-bone-substitute-materials-immediate-implant-sr-ma`) 세줄: SR+MA (RCT 20편, 848명·916부위): 즉시식립 임플란트–소켓 gap에 골대체재(Bone Substitute Material, BSM) 이식 vs 비이식 비교. BSM 이식이 수평 협측골 흡수 감소(MD −0.52 mm)와 심미점수 개선(MD +1.49)에 유의; 임플란트 실패율에는 차이 없음(RR 0.92); 반면 합병증 3.5배 증가(RR 3.50). GRADE 확실성 대부분 중등도. 즉시식립 gap 이식은 협측골·심미 보존에 유효하나 합병증 증가 상충(trade-off)을 고려해

- `lang-2012-immediate-implant-survival-success-sr` [immediate-implant] (HIGH-no-target, 'In contrast to' · 대조)
  - **근거 문장**: This landmark systematic review by Lang et al. (2012, Clinical Oral Implants Research, Suppl. 5) pooled 46 prospective studies (mean follow-up 2.08 years) identified via MEDLINE and the Cochrane Library (1991–July 2010) to quantify survival and success of Type I (immediate) implants placed into fresh extraction sockets. Using STATA and an inverse-variance weighting method, the review derived an an
  - ▸ 출발(`lang-2012-immediate-implant-survival-success-sr`) 세줄: 전향적 연구 46편(평균 추적 2.08년) 대상 체계적 문헌고찰(Lang 2012, Clin Oral Implants Res) — 발치와 즉시식립(Type I immediate implant) 임플란트의 생존율·성공률을 MEDLINE/Cochrane Library 검색(1991–2010.7)으로 평가. 연간 실패율 0.82% (95% CI 0.48–1.39%), 2년 생존율 98.4% (97.3–99%); 분석한 5개 요인(발치 원인, 항생제 사용, 임플란트 위치, 부하 방식) 중 수술 후 항생제

- `pommer-2021-maxillary-single-tooth-timing-protocols-sr-ma` [immediate-implant] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 즉시식립 관련 SR/MA는 대부분 식립 타이밍(immediate/early/delayed placement)만 다루는데, 본 논문(Pommer 2021, COIR Suppl 21)은 상악 심미부위 single-tooth implant에서 식립 타이밍(IP/EP/DP)과 부하 타이밍(IL/EL/DL)을 **교차(cross-tabulate)**해 ≥3년 장기 결과(생존율·변연골흡수)를 비교한 드문 연구다. 기존 [[immediate-implant/esthetic-soft-tissue/buser-2017-implant-placement-timing-post-extraction-esthetic]]가 Type 1–4 식립 타이밍 분류체계를 제시했고 [[immediate-implant/lang-2012-immediat
  - ▸ 출발(`pommer-2021-maxillary-single-tooth-timing-protocols-sr-ma`) 세줄: 상악 심미부위 단일치아 임플란트를 ≥3년 추적한 체계적고찰+메타분석; 식립 타이밍(즉시식립 Immediate Placement, IP / 조기식립 Early Placement, EP / 지연식립 Delayed Placement, DP)과 부하 타이밍(즉시부하 Immediate Loading, IL / 조기부하 Early Loading, EL / 지연부하 Delayed Loading, DL)을 교차 비교 — 대조군 연구 7편 메타분석 + 총 29편(임플란트 965개) pooled 분석. 식립×부하 

- `prati-2017-immediate-early-delayed-implants-endodontic-infections` [immediate-implant] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[immediate-implant/munoz-camara-2020-immediate-implants-acute-periapical-infected]] — contradicts: Murcia group placed immediately in acute sites and found 100% survival; protocol difference (CHX debridement + AMOX/CLV vs Bologna's defer-to-early approach)
  - ▸ 출발(`prati-2017-immediate-early-delayed-implants-endodontic-infections`) 세줄: 전향적 코호트 (n=85명, 131 ZirTi 임플란트), 볼로냐대학교; 발치전 근관 진단으로 식립 타이밍 결정 — 급성 농양→조기 (8–12주), 만성 병변→즉시, 정상→지연; 2년 추적. 생존율 100%; 변연골 소실 (Marginal Bone Loss, MBL) 24개월: 조기 0.48 mm (최소) < 즉시 0.78 mm < 지연 1.02 mm; 조기 vs 지연 p=0.0001 유의. 급성 치근단 농양 = 즉시식립 금기; 8–12주 조기식립 (Early Placement)이 변연골 보존 최

- `fan-2024-immediate-implant-ridge-preservation-comparative-sr-ma` [immediate-implant] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: IIP는 치료 단계를 줄이고 심미·생존율이 동등하나 MBL 감소와 합병증 증가라는 상충이 있어, 환자별 시간·비용·위험 선호도를 고려한 개별화 결정이 필요하며 장기 RCT가 요구됨.
  - ▸ 출발(`fan-2024-immediate-implant-ridge-preservation-comparative-sr-ma`) 세줄: SR+MA (11 RCT, n=701: IIP 353 vs ARP 348; PROSPERO CRD42024503989): 즉시식립(IIP) vs 치조제 보존 후 지연식립(ARP) — 비구치 및 구치 부위 모두 포함. IIP가 MBL 유의하게 더 크게 감소 (비구치 MD −0.36 mm, 구치 MD −0.41 mm); 술후 합병증도 IIP에서 유의하게 높음; PES·임플란트 실패율·경조직·연조직·환자 만족도는 두 전략 간 차이 없음. IIP는 치료 단계를 줄이고 심미·생존율이 동등하나 MBL 감소와

- `mello-2017-immediate-fresh-extraction-vs-delayed-healed-socket-sr-ma` [immediate-implant] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[immediate-implant/lang-2012-immediate-implant-survival-success-sr]] — SR reporting generally favorable immediate-implant survival rates; useful counterpoint when weighing this paper's significant survival gap.
  - ▸ 출발(`mello-2017-immediate-fresh-extraction-vs-delayed-healed-socket-sr-ma`) 세줄: 체계적 문헌고찰+메타분석 (PROSPERO CRD42016043309; 적격 연구 30편, 2016년 11월까지 검색): 발치와 신선 소켓 3,049개 임플란트(환자 1,435명, 평균 46.68세, 최소 6개월 추적) — 즉시식립 (Immediate Implant Placement, IIP) vs 치유된 소켓 지연식립 비교. 지연식립 생존율(98.38%)이 즉시식립보다 유의하게 높음(95.21%, p=.001); 변연골소실 (Marginal Bone Loss, MBL, p=.32), 임플란트 안

- `mello-2017-immediate-fresh-extraction-vs-delayed-healed-socket-sr-ma` [immediate-implant] (HIGH-far→asghar-2023-immediate-vs-early-implant-esthetic-zone-sr-ma, '대비되는' · 대비)
  - **근거 문장**: 즉시식립 (Immediate Implant Placement, IIP) vs 지연식립 (Delayed Implant Placement, DIP) 시기 비교 SR/MA를 이번 배치에서 4편 함께 인제스트한다 ([[immediate-implant/garcia-sanchez-2022-immediate-vs-delayed-implant-placement-sr-ma]], [[immediate-implant/pommer-2021-maxillary-single-tooth-timing-protocols-sr-ma]], [[immediate-implant/asghar-2023-immediate-vs-early-implant-esthetic-zone-sr-ma]]). 이 Mello 2017 논문(30편 SR, 3,049 임플
  - ▸ 출발(`mello-2017-immediate-fresh-extraction-vs-delayed-healed-socket-sr-ma`) 세줄: 체계적 문헌고찰+메타분석 (PROSPERO CRD42016043309; 적격 연구 30편, 2016년 11월까지 검색): 발치와 신선 소켓 3,049개 임플란트(환자 1,435명, 평균 46.68세, 최소 6개월 추적) — 즉시식립 (Immediate Implant Placement, IIP) vs 치유된 소켓 지연식립 비교. 지연식립 생존율(98.38%)이 즉시식립보다 유의하게 높음(95.21%, p=.001); 변연골소실 (Marginal Bone Loss, MBL, p=.32), 임플란트 안

- `mello-2017-immediate-fresh-extraction-vs-delayed-healed-socket-sr-ma` [immediate-implant] (AMBIG→pommer-2021-maxillary-single-tooth-timing-protocols-sr-ma, '대비되는' · 대비)
  - **근거 문장**: 즉시식립 (Immediate Implant Placement, IIP) vs 지연식립 (Delayed Implant Placement, DIP) 시기 비교 SR/MA를 이번 배치에서 4편 함께 인제스트한다 ([[immediate-implant/garcia-sanchez-2022-immediate-vs-delayed-implant-placement-sr-ma]], [[immediate-implant/pommer-2021-maxillary-single-tooth-timing-protocols-sr-ma]], [[immediate-implant/asghar-2023-immediate-vs-early-implant-esthetic-zone-sr-ma]]). 이 Mello 2017 논문(30편 SR, 3,049 임플
  - ▸ 출발(`mello-2017-immediate-fresh-extraction-vs-delayed-healed-socket-sr-ma`) 세줄: 체계적 문헌고찰+메타분석 (PROSPERO CRD42016043309; 적격 연구 30편, 2016년 11월까지 검색): 발치와 신선 소켓 3,049개 임플란트(환자 1,435명, 평균 46.68세, 최소 6개월 추적) — 즉시식립 (Immediate Implant Placement, IIP) vs 치유된 소켓 지연식립 비교. 지연식립 생존율(98.38%)이 즉시식립보다 유의하게 높음(95.21%, p=.001); 변연골소실 (Marginal Bone Loss, MBL, p=.32), 임플란트 안

- `alqutaibi-2026-root-analog-dental-implants` [immediate-implant] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 기존 [[wiki/immediate-implant/lee-2021-immediate-implant-placement-in-fresh]]가 발치 즉시 표준 나사형 임플란트 식립의 gap-management 원칙을 다뤘다면, 본 SR(Alqutaibi 2026, PROSPERO CRD420251162616)은 발치와 형태를 그대로 복제해 소켓과의 gap 자체를 없애는 root-analog implant(RAI, 치근형태모사 임플란트) 28개 임상연구(432개 RAI)를 정리해 대안적 즉시식립 전략의 근거를 보강한다. 소켓 형태를 보존한다는 목표는 [[wiki/immediate-implant/socket-shield/ahamed-2022-partial-extraction-therapy-implant-placeme
  - ▸ 출발(`alqutaibi-2026-root-analog-dental-implants`) 세줄: 체계적 문헌고찰(메타분석 없음; PRISMA/PROSPERO CRD420251162616)로, 발거 치아의 치근 형태를 그대로 복제해 제작한 root-analog implant(RAI, 치근형태모사 임플란트) 28개 임상연구(432개 RAI, 티타늄·지르코니아·하이브리드 티타늄-지르코니아, CAD-CAM 밀링 또는 SLM/DLMS/DLMF 적층제조)를 종합. 대부분 연구에서 생존율 71–100%, 성공률 64.5–100%를 보고했으며, 티타늄·하이브리드 RAI가 가장 예측 가능(생존율 최대 100

- `sierra-rebolledo-2021-undersized-drilling-immediate-tapered-implants-maxilla` [immediate-implant] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/versah-protocols/rittipakorn-2025-clockwise-osseodensification-primary-stability-cadaveric]] — cadaveric study positioning undersized drilling among primary-stability-enhancing techniques; this RCT contradicts the premise by showing undersizing raises IT but not RFA stability in immediate maxillary implants.
  - ▸ 출발(`sierra-rebolledo-2021-undersized-drilling-immediate-tapered-implants-maxilla`) 세줄: RCT (즉시식립 테이퍼드 임플란트 n=30, 상악 전치부; 통상 드릴링 16 vs 축경 [undersized, 3.0 mm twist 드릴 생략] 14) — 삽입 토크와 RFA/ISQ를 삽입·6주·12주에 측정. 축경 드릴링은 1차 안정성을 유의하게 개선하지 못함: 삽입 토크 UD군에서 약간 높았으나(41.36 vs 38.44 Ncm, p=0.654, 비유의), RFA/ISQ는 모든 시점에서 통상군이 더 높고 군간 차이 비유의. 토크-ISQ 해리(UD에서 토크↑·ISQ↓)는 높은 토크에 의한 골

- `sierra-rebolledo-2021-undersized-drilling-immediate-tapered-implants-maxilla` [immediate-implant] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 골밀도화 시계방향 osteotomy의 cadaveric 1차 안정성 연구 [[wiki/implants/versah-protocols/rittipakorn-2025-clockwise-osseodensification-primary-stability-cadaveric]]는 undersized drilling을 1차 안정성을 높이는 대안 술식으로 함께 논의한다. 이 RCT는 그 대안 술식(undersized drilling)을 즉시식립 상악 전치부에서 직접 검증해, "축경 드릴링이 IT는 올리지만 RFA 안정성은 개선하지 않는다"는 임상 근거를 제공한다 — cadaveric/벤치 모델의 IT↑ 소견을 RCT에서 한정/반박하는 자료.
  - ▸ 출발(`sierra-rebolledo-2021-undersized-drilling-immediate-tapered-implants-maxilla`) 세줄: RCT (즉시식립 테이퍼드 임플란트 n=30, 상악 전치부; 통상 드릴링 16 vs 축경 [undersized, 3.0 mm twist 드릴 생략] 14) — 삽입 토크와 RFA/ISQ를 삽입·6주·12주에 측정. 축경 드릴링은 1차 안정성을 유의하게 개선하지 못함: 삽입 토크 UD군에서 약간 높았으나(41.36 vs 38.44 Ncm, p=0.654, 비유의), RFA/ISQ는 모든 시점에서 통상군이 더 높고 군간 차이 비유의. 토크-ISQ 해리(UD에서 토크↑·ISQ↓)는 높은 토크에 의한 골

- `garcia-sanchez-2022-immediate-vs-delayed-implant-placement-sr-ma` [immediate-implant] (HIGH-no-target, 'at odds' · 상충)
  - **근거 문장**: - [[immediate-implant/mello-2017-immediate-fresh-extraction-vs-delayed-healed-socket-sr-ma]] — contrasting finding (RCT-only vs all-design pooling): reports a significant survival disadvantage for immediate placement using a broader, non-RCT-restricted study pool, directly at odds with this paper's RCT-only Q1 no-difference finding.
  - ▸ 출발(`garcia-sanchez-2022-immediate-vs-delayed-implant-placement-sr-ma`) 세줄: 즉시식립 (Immediate Implant Placement, IIP) vs 지연식립 (Delayed Implant Placement) 비교 체계적 문헌고찰+메타분석(2019년 11월까지 검색): Q1은 즉시-지연 head-to-head RCT 6편, Q2는 즉시식립 단독 53편(RCT 22+CCT 11+증례군 20)을 각각 풀링. Q1 메타분석에서 임플란트 생존율 차이는 유의하지 않았으나, 1년 부하 후 변연골수준 (Marginal Bone Level, MBL)·핑크심미점수 (Pink Esthe

- `garcia-sanchez-2022-immediate-vs-delayed-implant-placement-sr-ma` [immediate-implant] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 배치 내에서 특히 중요한 것은 이 논문이 같은 배치의 [[immediate-implant/mello-2017-immediate-fresh-extraction-vs-delayed-healed-socket-sr-ma]]와 정반대 결론을 낸다는 점이다 — Mello 2017은 (RCT 제한 없는) 넓은 study pool에서 즉시식립의 유의한 생존율 열세를 보고한 반면, 본 연구는 RCT-only Q1에서 생존율 차이 없음(변연골수준·PES는 오히려 즉시군 우위)을 보고한다. Study-design inclusion criteria(RCT-only vs all-design pooling)가 헤드라인 결론을 뒤집을 수 있음을 보여주는 근거평가 교육 사례로, [[overviews/evidence-appraisal-t
  - ▸ 출발(`garcia-sanchez-2022-immediate-vs-delayed-implant-placement-sr-ma`) 세줄: 즉시식립 (Immediate Implant Placement, IIP) vs 지연식립 (Delayed Implant Placement) 비교 체계적 문헌고찰+메타분석(2019년 11월까지 검색): Q1은 즉시-지연 head-to-head RCT 6편, Q2는 즉시식립 단독 53편(RCT 22+CCT 11+증례군 20)을 각각 풀링. Q1 메타분석에서 임플란트 생존율 차이는 유의하지 않았으나, 1년 부하 후 변연골수준 (Marginal Bone Level, MBL)·핑크심미점수 (Pink Esthe

- `krishnakumar-2024-hvgic-composite-primary-teeth-sr` [glass-ionomer] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: No statistically significant difference between HVGIC and CR was found in any included study; the wider literature reports contradictory durability findings for primary-teeth restorations.
  - ▸ 출발(`krishnakumar-2024-hvgic-composite-primary-teeth-sr`) 세줄: 유치 단면·다면 와동에서 HVGIC vs 직접 레진(CR)을 비교한 임상시험 4편(RCT 3편+비무작위 1편; 2000–2021; 3–13세) SR. 포함된 모든 연구에서 HVGIC와 CR 간 통계적 유의차 없음; 광범위한 문헌은 유치 수복 내구성에서 상반된 결과를 보고함. 임상시험 4편이라는 매우 작은 근거 기반이 핵심 한계; HVGIC는 비열등 옵션으로 정당화되며, 특히 방습·조작 편의가 중요한 임상 환경에서 유효하다.

- `krishnakumar-2024-hvgic-composite-primary-teeth-sr` [glass-ionomer] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: 포함된 모든 연구에서 HVGIC와 CR 간 통계적 유의차 없음; 광범위한 문헌은 유치 수복 내구성에서 상반된 결과를 보고함.
  - ▸ 출발(`krishnakumar-2024-hvgic-composite-primary-teeth-sr`) 세줄: 유치 단면·다면 와동에서 HVGIC vs 직접 레진(CR)을 비교한 임상시험 4편(RCT 3편+비무작위 1편; 2000–2021; 3–13세) SR. 포함된 모든 연구에서 HVGIC와 CR 간 통계적 유의차 없음; 광범위한 문헌은 유치 수복 내구성에서 상반된 결과를 보고함. 임상시험 4편이라는 매우 작은 근거 기반이 핵심 한계; HVGIC는 비열등 옵션으로 정당화되며, 특히 방습·조작 편의가 중요한 임상 환경에서 유효하다.

- `krishnakumar-2024-hvgic-composite-primary-teeth-sr` [glass-ionomer] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This review compared the clinical effectiveness of high-viscosity GIC (HVGIC) versus direct composite resin (CR) in single- and multi-surface cavities in primary teeth of children aged 3–13. Major databases were searched for publications 2000–2021. Four studies met inclusion (three RCTs, one non-randomized controlled trial). No statistically significant difference between HVGIC and CR was found in
  - ▸ 출발(`krishnakumar-2024-hvgic-composite-primary-teeth-sr`) 세줄: 유치 단면·다면 와동에서 HVGIC vs 직접 레진(CR)을 비교한 임상시험 4편(RCT 3편+비무작위 1편; 2000–2021; 3–13세) SR. 포함된 모든 연구에서 HVGIC와 CR 간 통계적 유의차 없음; 광범위한 문헌은 유치 수복 내구성에서 상반된 결과를 보고함. 임상시험 4편이라는 매우 작은 근거 기반이 핵심 한계; HVGIC는 비열등 옵션으로 정당화되며, 특히 방습·조작 편의가 중요한 임상 환경에서 유효하다.

- `krishnakumar-2024-hvgic-composite-primary-teeth-sr` [glass-ionomer] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: No statistically significant difference between HVGIC and CR in any included study. Evidence base small; durability findings across the wider literature remain contradictory.
  - ▸ 출발(`krishnakumar-2024-hvgic-composite-primary-teeth-sr`) 세줄: 유치 단면·다면 와동에서 HVGIC vs 직접 레진(CR)을 비교한 임상시험 4편(RCT 3편+비무작위 1편; 2000–2021; 3–13세) SR. 포함된 모든 연구에서 HVGIC와 CR 간 통계적 유의차 없음; 광범위한 문헌은 유치 수복 내구성에서 상반된 결과를 보고함. 임상시험 4편이라는 매우 작은 근거 기반이 핵심 한계; HVGIC는 비열등 옵션으로 정당화되며, 특히 방습·조작 편의가 중요한 임상 환경에서 유효하다.

- `panetta-2024-gic-longevity-umbrella-review` [glass-ionomer] (HIGH-no-target, 'conflicting evidence' · 상충 결과)
  - **근거 문장**: AMSTAR-2 showed none of the 13 SRs met all criteria and none had an a priori design (4 SRs lacked a quality-analysis tool; 2 SRs used no risk-of-bias tool; 2 SRs — Amorim et al. and Mickenautsch et al. — disclosed a conflict of interest tied to GIC-technique teaching). ROBIS rated 7/13 SRs at low risk of bias (2 very low + 5 low), 1/13 (Ruengrungsom et al.) at high risk, and 1/13 at very high risk
  - ▸ 출발(`panetta-2024-gic-longevity-umbrella-review`) 세줄: 우산 리뷰 (PROSPERO CRD42022320602; J Funct Biomater 2024; MedLine/PubMed·WoS·Scopus 검색 132편 → 최종 13편, 추적기간 6개월–6년): 유치·영구치에서 GIC·RMGIC·컴포머의 임상 수명을 평가했다. 포함된 SR 중 AMSTAR-2 전 기준을 충족한 연구는 없었고, 사전 설계(a priori) SR도 없었으며, ROBIS 기준 13편 중 7편이 저비뚤림·1편이 고비뚤림 위험이었다. 종합 GRADE 평가는 권고등급 Class II·

- `durrant-2024-gic-load-bearing-restorations-sr` [glass-ionomer] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 하중부 GIC 적용에 대한 오랜 우려를 RCT 근거로 직접 반박하나, 변색·색조 일치·반투명도 등 일부 심미 지표에서 비교재료 대비 차이가 있었다.
  - ▸ 출발(`durrant-2024-gic-load-bearing-restorations-sr`) 세줄: RCT만 포함한 SR (EBSCO/PubMed/Embase/Cochrane, 12편) — Class I·II 하중부 수복에서 USPHS 유형 지표 별 GIC 임상 성능 평가. 표면 변연·수복 형태·유지/파절·변연 적합·교합면 윤곽·마모·인접면에서 GIC가 기존 재료와 동등; 술후 과민증·이차우식·치아 온전성에 유의차 없음; 환자 및 치주 반응은 GIC 유리. 하중부 GIC 적용에 대한 오랜 우려를 RCT 근거로 직접 반박하나, 변색·색조 일치·반투명도 등 일부 심미 지표에서 비교재료 대비 차이가 

- `ge-2023-glass-ionomer-secondary-caries-sr-ma` [caries] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refutes legacy belief that amalgam's metal content provides superior anti-caries effect
  - ▸ 출발(`ge-2023-glass-ionomer-secondary-caries-sr-ma`) 세줄: 64 RCT SR+MA (GIC 수복 8,310개 vs 아말감·컴포지트 5,857개, 1–10년 추적): 유치·영구치 이차 우식 발생률 비교. GIC < 아말감(영구치 RR=0.20, 유치 RR=0.55); GIC ≈ 레진 컴포지트(두 치아형 모두 NS); 기존 GIC vs RMGIC 차이 없음. 고우식 위험 환자·소아·노년 치료에서 GIC 사용을 지지하며, 아말감의 우식예방 우위 믿음은 근거가 없다.

- `kumar-2026-fluoride-varnish-caries-prevention-cost-effectiveness-sr-ma` [caries] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: > **Scope note:** This page concerns **economic cost-effectiveness**, not clinical caries-prevention efficacy. FV's clinical efficacy is documented in other wiki pages and is not contradicted here.
  - ▸ 출발(`kumar-2026-fluoride-varnish-caries-prevention-cost-effectiveness-sr-ma`) 세줄: SR+MA (경제성 평가 연구 23편, 836편 스크리닝, PROSPERO 등록): 고소득국 소아 우식예방에서 전문가 불소바니시(FV) vs 다른 예방중재의 비용효과성 평가. 통합 증분순화폐편익(INMB) $124.1 (I²=0%, 95% CI zero 교차) — 비용효과 유의 차이 없음. 고소득국 의료공급자/지불자 관점에서 FV의 비용효과는 불확실; 이 결과는 FV의 임상 효능을 부정하는 것이 아니라 경제적 우위가 입증되지 않음을 의미한다.

- `kotsakis-2018-network-meta-analysis-interproximal` [interdental-cleaning] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Interdental brushes (IB) emerged as the top-ranked aid for gingival index and plaque index reduction, with water-jet (WJ) a consistent second. For bleeding-on-probing, toothpick with intensive instruction (TO) ranked highest, followed by WJ — though this result rested on a single trial and should be interpreted cautiously. Unsupervised flossing and unaided toothpick use ranked at or near the botto
  - ▸ 출발(`kotsakis-2018-network-meta-analysis-interproximal`) 세줄: 22편 RCT, 10종 치간 구강위생(IOH) 보조기구를 대상으로 한 베이지안 네트워크 메타분석(BNMA) — 칫솔질 보조수단으로서 치태·치은염증(GI/BOP)·치주낭깊이 감소 비교. 치간칫솔(IB)이 치은지수 감소에서 최고 순위(0.23 [95% CI 0.09-0.37], 최선일 확률 64.7%)이자 치태지수도 최고, 그다음이 물세정기(WJ, 0.19 [95% CI 0.14-0.24]); 비지도 치실질과 이쑤시개는 최하위(최선일 확률 거의 0). 임상적 의미: 단일 IOH 도구가 보편적 금표준은

- `kotsakis-2018-network-meta-analysis-interproximal` [interdental-cleaning] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Importantly, the authors are careful to frame this as a technique/adherence problem rather than a mechanistic refutation of floss: correctly and consistently performed flossing likely remains effective, but its technical difficulty and poor real-world execution likely explain its low ranking against easier-to-use alternatives.
  - ▸ 출발(`kotsakis-2018-network-meta-analysis-interproximal`) 세줄: 22편 RCT, 10종 치간 구강위생(IOH) 보조기구를 대상으로 한 베이지안 네트워크 메타분석(BNMA) — 칫솔질 보조수단으로서 치태·치은염증(GI/BOP)·치주낭깊이 감소 비교. 치간칫솔(IB)이 치은지수 감소에서 최고 순위(0.23 [95% CI 0.09-0.37], 최선일 확률 64.7%)이자 치태지수도 최고, 그다음이 물세정기(WJ, 0.19 [95% CI 0.14-0.24]); 비지도 치실질과 이쑤시개는 최하위(최선일 확률 거의 0). 임상적 의미: 단일 IOH 도구가 보편적 금표준은

- `jung-2025-flossing-performance-plaque-removal` [interdental-cleaning] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Even correct flossing technique does not substantially reduce interdental plaque — the "inadequate application" explanation for floss's weak trial record is refuted, shifting the rationale toward alternative interdental approaches.
  - ▸ 출발(`jung-2025-flossing-performance-plaque-removal`) 세줄: 전향적 단일 코호트 전후 중재연구(n=37, 독일 대학생): 동영상 교육+1주 연습 전후에 치실 술식(Flossing Performance Score, FPS)과 치태 제거량(구강 내 스캔 기반 Proximal Surface Plaque Index, PSPI)을 측정. 동영상 교육으로 치실 술식은 유의하게 향상됐으나(FPS 2.0→2.83, p<.001), 치태 제거량은 개선되지 않았고(PSPI 0.17 vs 0.21, p=.112), FPS와 치태 제거량은 무상관; 치실 전 치태 수준이 치실 후

- `jung-2025-flossing-performance-plaque-removal` [interdental-cleaning] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 올바른 치실 기법도 치간 치태를 의미 있게 줄이지 못한다 — "기술 부족" 설명이 반박되며, 치실의 낮은 효능은 기법 문제가 아니라 기기 자체의 한계임을 시사한다.
  - ▸ 출발(`jung-2025-flossing-performance-plaque-removal`) 세줄: 전향적 단일 코호트 전후 중재연구(n=37, 독일 대학생): 동영상 교육+1주 연습 전후에 치실 술식(Flossing Performance Score, FPS)과 치태 제거량(구강 내 스캔 기반 Proximal Surface Plaque Index, PSPI)을 측정. 동영상 교육으로 치실 술식은 유의하게 향상됐으나(FPS 2.0→2.83, p<.001), 치태 제거량은 개선되지 않았고(PSPI 0.17 vs 0.21, p=.112), FPS와 치태 제거량은 무상관; 치실 전 치태 수준이 치실 후

- `jung-2025-flossing-performance-plaque-removal` [interdental-cleaning] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Instruction worked on technique — FPS rose from 2.0 to 2.83 (p<.001), with large gains in correct floss adaptation and vertical movements, and flossing time grew from 60 to 89 seconds. But the cleaning result barely moved: plaque removal was 0.17 (habitual) vs 0.21 (instructed), p=.112, only about 3% more plaque cleared. Crucially, flossing performance was **not correlated** with plaque removed, a
  - ▸ 출발(`jung-2025-flossing-performance-plaque-removal`) 세줄: 전향적 단일 코호트 전후 중재연구(n=37, 독일 대학생): 동영상 교육+1주 연습 전후에 치실 술식(Flossing Performance Score, FPS)과 치태 제거량(구강 내 스캔 기반 Proximal Surface Plaque Index, PSPI)을 측정. 동영상 교육으로 치실 술식은 유의하게 향상됐으나(FPS 2.0→2.83, p<.001), 치태 제거량은 개선되지 않았고(PSPI 0.17 vs 0.21, p=.112), FPS와 치태 제거량은 무상관; 치실 전 치태 수준이 치실 후

- `jung-2025-flossing-performance-plaque-removal` [interdental-cleaning] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: A common defense of flossing's weak trial record is that participants simply floss badly — so "proper technique" should rescue efficacy. This study tests that assumption head-on by measuring whether instruction-improved flossing technique actually removes more plaque, directly extending the flossing-questioned theme in [[interdental-cleaning/min-2024-brushing-flossing-mouthrinsing-plaque-microbiot
  - ▸ 출발(`jung-2025-flossing-performance-plaque-removal`) 세줄: 전향적 단일 코호트 전후 중재연구(n=37, 독일 대학생): 동영상 교육+1주 연습 전후에 치실 술식(Flossing Performance Score, FPS)과 치태 제거량(구강 내 스캔 기반 Proximal Surface Plaque Index, PSPI)을 측정. 동영상 교육으로 치실 술식은 유의하게 향상됐으나(FPS 2.0→2.83, p<.001), 치태 제거량은 개선되지 않았고(PSPI 0.17 vs 0.21, p=.112), FPS와 치태 제거량은 무상관; 치실 전 치태 수준이 치실 후

- `mohapatra-2024-water-flosser-vs-floss-plaque-sr` [interdental-cleaning] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Adds a head-to-head water-flosser-vs-dental-floss SR focused specifically on the *plaque-reduction* endpoint, complementing [[interdental-cleaning/mancinelli-lyle-2024-water-flosser-vs-interdental-brush-rct]] (water flosser vs interdental brush) and providing the general-adult counterpoint to the orthodontic-only [[interdental-cleaning/yiamwattana-2025-oral-irrigator-vs-floss-orthodontic-sr-ma]], 
  - ▸ 출발(`mohapatra-2024-water-flosser-vs-floss-plaque-sr`) 세줄: 체계적 문헌고찰(PRISMA/PROSPERO 등록; 6개 데이터베이스, 2002–2022; RCT 7편, n=34–83, I²=97%로 메타분석 불가, 정성 합성만): 성인에서 워터플로서 vs 치실의 치태 감소 비교. 7편 중 4편이 워터플로서 우위(예: Goyal 2013 전악 74.4% vs 57.7%), 특히 접근 어려운 후방부·인접면에서; 3편은 차이 없음; GRADE "moderate," 부정확도 "심각". 워터플로서가 치태 감소에서 치실보다 방향적으로 우세하며, 특히 손재주가 부족하거나

- `thomassen-2025-airfloss-essential-oils-vs-floss-rct` [interdental-cleaning] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[periodontics/tsilingaridis-2026-biofilm-induced-gingivitis-children-adolescents]] — contradicts/qualifies: that EFP/EAPD SR concludes self-performed floss adds little for gingivitis, whereas this RCT shows a powered air-flosser performs *no better* than floss — i.e. neither is a strong adjunct, and equivalence does not imply superiority of the device.
  - ▸ 출발(`thomassen-2025-airfloss-essential-oils-vs-floss-rct`) 세줄: 검사자 맹검 평행 RCT(n=82, 건강 성인, ACTA 암스테르담; 하악 21일 무구강위생 후 4주 회복 모델): Philips AirFloss Ultra + Listerine Cool Mint (AFeo, n=41) vs 왁스 치실(DF, n=41)을 1일 1회 칫솔질 보조로 비교. 두 군 모두 치은출혈(Bleeding on Marginal Probing, BOMP)·치면세균막(MPI)·치은마모(GAS)를 군내 유의하게 감소(모두 p<0.01)했으나, 어느 시점에서도 군간 유의차 없음(BOMP

- `wen-2026-dental-floss-sequence-plaque-removal` [interdental-cleaning] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: Clinically, the trial does not overturn the basic recommendation to floss daily — all three sequences are safe (zero adverse events) and all reduced plaque/bleeding versus baseline. What it adds is a caution against over-interpreting short (7-day) trials of flossing *timing* variables, since the plaque benefit that looked sequence-dependent at day 7 was gone by day 21. It also contradicts two earl
  - ▸ 출발(`wen-2026-dental-floss-sequence-plaque-removal`) 세줄: 단일맹검 RCT, 중국 대학생 54명 대상, 칫솔질 전(FB)·후(BF)·중간(BFB) 치실질 3개 병렬군을 21일간 비교하여 RMNPI 치태지수·출혈지수(BI)·탐침깊이(PD)를 측정. 칫솔질 중간 치실질(BFB)군이 7일째 RMNPI 감소가 가장 컸고(p=0.039, BF 대비 유의), BI 감소도 7일·21일 모두 유의하게 컸으나(p=0.028, p=0.015), 21일째 RMNPI 차이는 소실(p=0.933)되었고 PD는 두 시점 모두 군간 차이 없음(p=0.742, p=0.422). 칫솔

- `hardan-2022-treatment-tooth-wear-using-direct` [prosthetic-materials] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Tooth wear is a common clinical problem with no standardized treatment protocol. This PRISMA 2020 systematic review (search up to 29 April 2022 across PubMed/MedLine, Scopus, ISI Web of Science, Scielo, EMBASE) asked whether **direct or indirect restorations** give better clinical outcomes for treating worn dentition. From 2776 records, 16 clinical studies (RCTs and observational) were included fo
  - ▸ 출발(`hardan-2022-treatment-tooth-wear-using-direct`) 세줄: 체계적 문헌고찰(PRISMA 2020, 임상연구 16편, 최대 10년 추적): 치아 마모(tooth wear) 수복에서 직접(direct) vs 간접(indirect) 수복을 비교. 높은 이질성으로 메타분석 불가; 어떤 수복 기법·재료도 임상 성적에서 우월하다는 근거 없음. 현재 근거는 보존적·가역적·첨가적(additive) 수복 접근을 지지; 레진 복합재는 수리 가능 파절로 실패, 도재-금속은 완전 탈락으로 실패하는 경향.

- `varvara-2020-retightening-preload-loss-abutment-screws` [prosthetic-materials] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The optimal retightening window is 2 minutes after initial torque placement, contradicting prior guidance of 10 minutes; internal hexagon connections are mechanically superior for preload retention.
  - ▸ 출발(`varvara-2020-retightening-preload-loss-abutment-screws`) 세줄: 체외 연구(n=80; 내부 육각형(Internal Hexagon, IG) 40개·외부 육각형(External Hexagon, EG) 40개; 35 Ncm; 재조임 간격별 n=10: 대조군/2분/5분/10분; 30분 후 제거 토크 측정). 초기 조임 후 2분 재조임이 양쪽 연결부에서 예압(preload) 소실을 가장 효과적으로 최소화(p<0.05 vs 대조군); 내부 육각형이 외부 육각형보다 예압 유지 우수; 기존 권장 10분 재조임은 그 사이 추가 안착(settling)이 발생하여 차선. 최적 재

- `varvara-2020-retightening-preload-loss-abutment-screws` [prosthetic-materials] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 1. **Optimal retightening window is 2 minutes**, not 5 or 10 minutes (contradicts most prior in vitro guidance).
  - ▸ 출발(`varvara-2020-retightening-preload-loss-abutment-screws`) 세줄: 체외 연구(n=80; 내부 육각형(Internal Hexagon, IG) 40개·외부 육각형(External Hexagon, EG) 40개; 35 Ncm; 재조임 간격별 n=10: 대조군/2분/5분/10분; 30분 후 제거 토크 측정). 초기 조임 후 2분 재조임이 양쪽 연결부에서 예압(preload) 소실을 가장 효과적으로 최소화(p<0.05 vs 대조군); 내부 육각형이 외부 육각형보다 예압 유지 우수; 기존 권장 10분 재조임은 그 사이 추가 안착(settling)이 발생하여 차선. 최적 재

- `yang-2015-auxiliary-resistance-marginal-fitness-short-molar` [prosthetic-materials] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 저항-적합 상충관계(trade-off): 기본 유지력이 충분하면 보조 형태 추가 금지 — 치경 높이·수렴각 부족 시에만 groove/hole 고려.
  - ▸ 출발(`yang-2015-auxiliary-resistance-marginal-fitness-short-molar`) 세줄: In-vitro 연구 (West China J Stom 2015;33(5):474, Shandong Univ., 70 Nissin 레진치아, 20° TOC + 2.5 mm 짧은 대구치): proximal groove·occlusal hole × 0°/6°/20° 외전도, 탈락저항력·변연 부유(marginal float) 측정. 0° groove(443 N)·0° hole(485 N)·6° hole(444 N)이 control(328 N) 대비 저항력 유의 증가; 그러나 20° groove 제외 모

- `scheffel-2015-transdentinal-cytotoxicity-glutaraldehyde-odontoblast` [dentin-hypersensitivity] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Using artificial pulp chambers with dentin discs, this study measured whether glutaraldehyde — the active in Gluma-type desensitizers — diffuses across dentin to harm odontoblast-like cells. Glutaraldehyde-containing treatments reduced MDPC-23 viability in a concentration-dependent fashion, confirming transdentinal cytotoxicity. The findings provide the mechanistic safety counterpoint to glutarald
  - ▸ 출발(`scheffel-2015-transdentinal-cytotoxicity-glutaraldehyde-odontoblast`) 세줄: In vitro 경상아질 세포독성 연구: 인간 상아질 디스크 하방에 MDPC-23 오도노블라스트 유사세포를 배치한 인공 치수강 모델에서 글루타르알데히드 함유 탈감작제를 적용. 글루타르알데히드 처치가 농도 의존적으로 MDPC-23 세포 생존율 감소 — 경상아질 확산과 치수 세포독성 확인. Gluma계 탈감작제의 효과와 농도 의존적 치수 세포독성 간 균형 필요 — 생활치 적용 시 용량·농도 주의를 뒷받침하는 기초 근거.

- `rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety` [local-anesthesia] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: [근거중간] A single-blinded RCT at the University of Barcelona Dental Hospital randomized 68 patients (34/arm) undergoing upper third molar extraction to receive, or not receive, a standardized verbal explanation of **The Wand** — a computerized, pressure-regulated, footswitch-activated local anesthesia delivery system — before injection. All patients received identical anesthesia (The Wand, supraperi
  - ▸ 출발(`rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety`) 세줄: 단일맹검 무작위대조시험 (n=68, 바르셀로나): The Wand 컴퓨터 제어 마취 시스템의 작동 원리를 상세히 구두 설명하는 군 vs 설명 없는 군을 상악 제3대구치 발치 환자에서 비교. 상세 설명은 불안(ISAR/MDAS/DFS/STAI-S)이나 통증(VAS)을 유의하게 줄이지 못했으며, 술중 재마취 필요율은 42.6%였다. 재마취 필요성은 불안도와 무관하고 수술시간 증가(p=0.007)와만 관련 — 낯선 컴퓨터 장비에 대한 사전 설명이 불안 감소로 이어지지 않을 수 있다는 임상적 시사점.

- `rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety` [local-anesthesia] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: - Contradicts prior literature suggesting information/explanation reduces dental fear (Wang, Heaton) — authors note the format/amount of information (and specifically its target: an unfamiliar computerized device with sounds/beeps) may behave differently from general procedural information.
  - ▸ 출발(`rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety`) 세줄: 단일맹검 무작위대조시험 (n=68, 바르셀로나): The Wand 컴퓨터 제어 마취 시스템의 작동 원리를 상세히 구두 설명하는 군 vs 설명 없는 군을 상악 제3대구치 발치 환자에서 비교. 상세 설명은 불안(ISAR/MDAS/DFS/STAI-S)이나 통증(VAS)을 유의하게 줄이지 못했으며, 술중 재마취 필요율은 42.6%였다. 재마취 필요성은 불안도와 무관하고 수술시간 증가(p=0.007)와만 관련 — 낯선 컴퓨터 장비에 대한 사전 설명이 불안 감소로 이어지지 않을 수 있다는 임상적 시사점.

- `rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety` [local-anesthesia] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[behavioral-dentistry/dental-anxiety/appukuttan-2016-strategies-manage-dental-anxiety-phobia]] — narrative review proposing a stepwise dental-anxiety management framework where patient information/communication is an early-line strategy; this RCT provides a specific negative/contradicting data point for the "information reduces anxiety" component of that framework in the context of computerized
  - ▸ 출발(`rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety`) 세줄: 단일맹검 무작위대조시험 (n=68, 바르셀로나): The Wand 컴퓨터 제어 마취 시스템의 작동 원리를 상세히 구두 설명하는 군 vs 설명 없는 군을 상악 제3대구치 발치 환자에서 비교. 상세 설명은 불안(ISAR/MDAS/DFS/STAI-S)이나 통증(VAS)을 유의하게 줄이지 못했으며, 술중 재마취 필요율은 42.6%였다. 재마취 필요성은 불안도와 무관하고 수술시간 증가(p=0.007)와만 관련 — 낯선 컴퓨터 장비에 대한 사전 설명이 불안 감소로 이어지지 않을 수 있다는 임상적 시사점.

- `cabral-2026-comparative-efficacy-anesthetic-techniques-periodontal` [local-anesthesia] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 바늘없는/컴퓨터제어 압력 침윤마취기(Wand-type computerized delivery system) 관련 질의 대응 목적으로 인제스트. 기존 [[local-anesthesia/wambier-2017-intrapocket-topical-versus-injected-anesthetic-srp]] (SR+MA)는 SRP에서 injected anesthetic이 topical gel보다 통증강도·rescue 필요성에서 우위라고 결론지었는데, 본 RCT(Cabral 2026)는 통증 강도 자체는 두 기법이 동등하다고 보고해 부분적으로 상충하며, 대신 "보충마취 필요성"이라는 secondary outcome에서 컴퓨터제어 침습기법의 우위(24% vs 100%, p<0.001)를 명확히 정량화해 기존 근거를 정제
  - ▸ 출발(`cabral-2026-comparative-efficacy-anesthetic-techniques-periodontal`) 세줄: 브라질 평행·맹검 RCT (n=76): 비외과적 치주기구조작에서 컴퓨터제어 침습마취(Morpheus, 2% 리도카인/1:100,000 에피네프린) vs 비침습 리도카인/프릴로카인 겔(Oraqix) 비교. 두 군 모두 통증강도(NRS-11 중앙값 0 vs 1, P>0.05)는 유사한 '경증' 수준이었으나, 겔군은 100%에서 보충마취 필요 vs 컴퓨터제어군 24% (P<0.001). 두 방법 모두 SRP 중 통증을 적절히 조절하지만, 컴퓨터제어 침습마취는 재마취 필요를 76% 줄여 시술 흐름의 예측

- `uzbelger-feldman-2024-buffered-anesthetic-without-epinephrine-invivo` [local-anesthesia] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: [미검증] This sits **upstream** of the clinical buffered-lidocaine RCTs in the wiki — those buffer a *conventional* LW/E cartridge chairside to improve onset/comfort; this paper instead designs a *vasoconstrictor-free* buffered product whose duration comes from osmolality/viscosity. It is positioned as `contradicts` to the epinephrine-concentration framing of [[drug/karm-2017-lidocaine-epinephrine-20
  - ▸ 출발(`uzbelger-feldman-2024-buffered-anesthetic-without-epinephrine-invivo`) 세줄: Sprague-Dawley 랫드를 이용한 완충·에피네프린-비함유 2% 리도카인(LW/O/E "Sample 3A": 락테이트 링거 비히클 + 덱스트로스 + 아미노산 쓴맛 차단제, pH 6.7–7.0, ~600 mOsm/kg) 제형 개발 연구로, 상용 2% 리도카인+1:100,000 에피네프린(LW/E)과 비교. 점도·주사성·마취 지속시간(꼬리튕김·핫플레이트 잠복기)에서 LW/E와 동등(대부분 시점 NS); 쓴맛 감소(전자혀 검증), 국소 독성 경미·일시적(6시간 홍반 1.4 ± 0.6, 24시간 내

- `karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb` [local-anesthesia] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[local-anesthesia/subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric]] — pediatric RCT reporting benzocaine > lignocaine; this stricter triple-blind RCT finds no agent difference (contradicts)
  - ▸ 출발(`karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb`) 세줄: 삼중맹검 3군 RCT (n=45 학령기 소아, 6–10세, 군당 15명): IANB 전 20% benzocaine 겔·8% lidocaine 겔·5% EMLA 크림을 2분 도포 후 FLACC 행동 척도·Wong-Baker FACES·맥박으로 비교. 모든 결과에서 통계적 유의차 없음 — FLACC p=0.806, Wong-Baker FACES p=0.593, 마취 후 맥박 p=0.351 — 8% lidocaine 겔은 표준 20% benzocaine 또는 EMLA 대비 우월하지 않음. 군당 15명으

- `karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb` [local-anesthesia] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 소아 IANB 전 표면마취제 3종(8% lidocaine, 20% benzocaine, 5% EMLA) 비교 triple-blind RCT. [[local-anesthesia/subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric]]가 benzocaine > lignocaine 우위를 보고한 것과 대비되는 "차이 없음" 결과를 더 엄격한 blinding으로 제시하므로, 표면마취제 제제 선택의 임상적 의미를 재검토하는 근거가 된다.
  - ▸ 출발(`karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb`) 세줄: 삼중맹검 3군 RCT (n=45 학령기 소아, 6–10세, 군당 15명): IANB 전 20% benzocaine 겔·8% lidocaine 겔·5% EMLA 크림을 2분 도포 후 FLACC 행동 척도·Wong-Baker FACES·맥박으로 비교. 모든 결과에서 통계적 유의차 없음 — FLACC p=0.806, Wong-Baker FACES p=0.593, 마취 후 맥박 p=0.351 — 8% lidocaine 겔은 표준 20% benzocaine 또는 EMLA 대비 우월하지 않음. 군당 15명으

- `ramanathan-2023-efficacy-reliability-single-tooth-anesthesia` [local-anesthesia] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 바늘없는/압력제어 침윤마취기(computer-controlled delivery system) 관련 질의 맥락에서, WANDSTA를 이용한 single tooth anesthesia (STA, intra-ligamentary injection)가 매복 제3대구치 외과적 발치에서 전통적 IANB의 대안이 될 수 있는지 확인하기 위해 인제스트. IANB 실패기전을 다루는 기존 [[local-anesthesia/malamed-2011-mandibular-nerve-block-passe]], [[local-anesthesia/haas-2011-alternative-mandibular-nerve-block-techniques]]과 대비되는, computer-controlled intraligamentary syste
  - ▸ 출발(`ramanathan-2023-efficacy-reliability-single-tooth-anesthesia`) 세줄: RCT(n=60, 군당 30명): 매복 하악 제3대구치 외과적 발치에서 WANDSTA 컴퓨터 제어 치주인대내 단일치아마취(STA, 4% articaine) vs 전통적 IANB(4% articaine) 비교. STA는 발현이 2.2(±0.25)분 더 빠르고(p<0.05) 24시간 술후 통증·개구제한이 낮았으나, 장협신경 추가블록 필요율이 더 높았고(50% vs 23.3%) 치아 거상 단계 술중 VAS가 높았음. WANDSTA STA는 IANB 금기 시 대안이 될 수 있으나 추가블록 필요율이 높아 

- `karm-2023-clinical-practice-guidelines-diagnostic-procedural-sedation` [local-anesthesia] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: The guideline explicitly addresses the risk of unintentional deep-sedation progression from moderate sedation, and its existence is the institutional counterpoint to the paired position paper calling for a still-absent Korean local-anesthesia guideline.
  - ▸ 출발(`karm-2023-clinical-practice-guidelines-diagnostic-procedural-sedation`) 세줄: JKDA 특집: 2022년 발표된 한국 진정·수면 가이드라인(1차 연구 아님)을 임상가에게 소개 — Moderate sedation 중심, 마취과 전문의가 아닌 치과의사 포함 대상, 15개 PICO 권고. 다루는 항목: 술자 교육·약물/장비 요건·환자 선택·금식·성인/소아 약물 비교·술중 모니터링(호흡·순환·진정 깊이)·소아 호흡 합병증 관리·퇴원 기준; 1차 결과치 없음. moderate sedation에서 deep sedation으로의 비의도적 이행 위험을 명시하며, 아직 국소마취 가이드라인이

- `subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric` [local-anesthesia] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 소아 IANB 전 표면마취제 선택(lignocaine vs benzocaine)의 통증 감소 효과를 다룬 소규모 RCT. [[local-anesthesia/karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb]]가 동일 비교(lidocaine·benzocaine·EMLA, IANB)를 더 엄격한 triple-blind RCT로 수행하므로, 본 연구는 그 비교군의 짝 근거이자 대비점(상충 결과)을 제공한다.
  - ▸ 출발(`subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric`) 세줄: 소아 40명(6–10세, 군당 20명)을 대상으로 IANB 전 2% 리그노카인 겔 vs 20% 벤조카인 겔을 비교한 2군 무작위대조시험. 20% 벤조카인이 2% 리그노카인보다 주사 통증을 유의하게 더 줄였다(4점 행동 척도 1.2 ± 0.6 vs 2.1 ± 0.5, P<0.05). 소아 IANB 전 표면마취로 벤조카인 20%가 더 우수해 보이나 소규모 표본·거친 척도·맹검 세부 사항 부족이 결론의 강도를 제한한다.

- `khademi-2023-premedication-inferior-alveolar-nerve-block-pulpitis-umbrella` [local-anesthesia] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 성인 하악 구치 증상성 비가역 치수염(symptomatic irreversible pulpitis)에서 IANB 성공률을 높이기 위한 술전 전처치 약물(premedication)을 다룬 4편의 체계적 문헌고찰(SR)을 종합한 우산리뷰(umbrella review). PROSPERO 등록(CRD42021286004), PRISMA 준수, AMSTAR 2로 4편 SR 자체를 메타 평가하고, 상충 시 JADAD 알고리즘으로 최적근거 SR을 선정하는 구조. 4편 SR이 모두 이부프로펜 >400 mg 전처치가 IANB 성공률을 유의하게 높인다는 결론에 수렴했기 때문에, 저자들은 우산리뷰 차원의 추가 메타분석 없이 질적 종합으로 마무리했다.
  - ▸ 출발(`khademi-2023-premedication-inferior-alveolar-nerve-block-pulpitis-umbrella`) 세줄: 성인 하악 구치 증상성 비가역 치수염(symptomatic irreversible pulpitis) 환자에서 하치조신경차단(inferior alveolar nerve block, IANB) 전 전처치(premedication)를 다룬 체계적 문헌고찰 4편(3편 메타분석 포함, 1편 미포함; 개별 RCT 7~35편)을 종합한 우산리뷰(umbrella review). 포함된 4편 모두 이부프로펜(ibuprofen) >400 mg 전처치가 IANB 마취 성공률을 유의하게 높인다는 동일한 결론에 도달(d

- `khademi-2023-premedication-inferior-alveolar-nerve-block-pulpitis-umbrella` [local-anesthesia] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: - JADAD 결정 알고리즘으로 상충되는 SR 간 최적근거를 선정(Nagendrababu 2018 — AMSTAR 2 "high").
  - ▸ 출발(`khademi-2023-premedication-inferior-alveolar-nerve-block-pulpitis-umbrella`) 세줄: 성인 하악 구치 증상성 비가역 치수염(symptomatic irreversible pulpitis) 환자에서 하치조신경차단(inferior alveolar nerve block, IANB) 전 전처치(premedication)를 다룬 체계적 문헌고찰 4편(3편 메타분석 포함, 1편 미포함; 개별 RCT 7~35편)을 종합한 우산리뷰(umbrella review). 포함된 4편 모두 이부프로펜(ibuprofen) >400 mg 전처치가 IANB 마취 성공률을 유의하게 높인다는 동일한 결론에 도달(d

- `khademi-2023-premedication-inferior-alveolar-nerve-block-pulpitis-umbrella` [local-anesthesia] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: - 상충 SR 발생 시 JADAD 결정 알고리즘으로 최적근거 선정.
  - ▸ 출발(`khademi-2023-premedication-inferior-alveolar-nerve-block-pulpitis-umbrella`) 세줄: 성인 하악 구치 증상성 비가역 치수염(symptomatic irreversible pulpitis) 환자에서 하치조신경차단(inferior alveolar nerve block, IANB) 전 전처치(premedication)를 다룬 체계적 문헌고찰 4편(3편 메타분석 포함, 1편 미포함; 개별 RCT 7~35편)을 종합한 우산리뷰(umbrella review). 포함된 4편 모두 이부프로펜(ibuprofen) >400 mg 전처치가 IANB 마취 성공률을 유의하게 높인다는 동일한 결론에 도달(d

- `al-obaida-2019-comparison-perceived-pain-patients-satisfaction` [local-anesthesia] (SOFT→ramanathan-2023-efficacy-reliability-single-tooth-anesthesia, 'whereas' · 반면(대조))
  - **근거 문장**: - [[local-anesthesia/ramanathan-2023-efficacy-reliability-single-tooth-anesthesia]] — companion STA evidence in a surgical (impacted third-molar extraction) context, comparing WANDSTA STA against IANB; that trial found faster onset but higher supplemental-block need and higher intra-operative VAS during elevation, whereas this trial finds STA's advantage concentrated in post-injection procedural c
  - ▸ 출발(`al-obaida-2019-comparison-perceived-pain-patients-satisfaction`) 세줄: 평행 RCT(n=80; STA 40/침윤 40; 리야드): 상악 구치부 Class I/II 수복치료에서 컴퓨터 제어 단일치아마취(STA) vs 전통 침윤마취 비교. 주사 중 통증(p=0.59)·수축기혈압(p=0.09) 유의차 없음; STA군이 수복 처치 중 통증 유의하게 낮음(군간 p=0.008); 치료 경험 만족도·향후 재선호도 STA 유의하게 우수(p=0.04). STA의 임상 이점은 주사 통증 감소가 아닌 처치 중 편안함·환자 만족도 향상; 기저치 심박수 불균형으로 심혈관 해석 제한.
  - ▸ 대상(`ramanathan-2023-efficacy-reliability-single-tooth-anesthesia`) 세줄: RCT(n=60, 군당 30명): 매복 하악 제3대구치 외과적 발치에서 WANDSTA 컴퓨터 제어 치주인대내 단일치아마취(STA, 4% articaine) vs 전통적 IANB(4% articaine) 비교. STA는 발현이 2.2(±0.25)분 더 빠르고(p<0.05) 24시간 술후 통증·개구제한이 낮았으나, 장협신경 추가블록 필요율이 더 높았고(50% vs 23.3%) 치아 거상 단계 술중 VAS가 높았음. WANDSTA STA는 IANB 금기 시 대안이 될 수 있으나 추가블록 필요율이 높아 

- `de-menezes-torres-2025-chatgpt-oral-maxillofacial-surgery` [artificial-intelligence] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: This is the LLM (text-reasoning) counterpoint to the image-diagnosis CNN papers: unlike 2D cephalometric landmarking — which already clears its clinical bar — LLMs are usable for communication/documentation drafting but not for autonomous complex decisions, mirroring the staged-adoption framing of the AI overview.
  - ▸ 출발(`de-menezes-torres-2025-chatgpt-oral-maxillofacial-surgery`) 세줄: 구강악안면외과에서 ChatGPT 활용을 다룬 10편의 체계적 문헌고찰(PRISMA; PROSPERO CRD42024625882): 임상 의사결정·수술 계획·환자 교육·연구 4개 영역 포괄. GPT-4는 객관식 정답률 76.8%, 동의서 작성·환자 소통에서 다른 AI 모델과 전공의를 능가(정확성·완성도·가독성); 약리학 및 복잡 임상 결정에서는 성능 저하 및 가변성. ChatGPT는 인간 판단을 보완할 수 있지만 대체 불가 — 감독·임상 데이터베이스 통합 필요, 초록만 확보.

- `peri-implant-emergence-profile-soft-tissue-conditioning-overview` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Five further papers extend this arc along three lines. On the **material-choice axis**, Ríos-Osorio et al. (2025) contribute the first SR+MA-tier evidence comparing xenogeneic collagen matrices against autogenous grafts, splitting the XCM class into crosslinked and non-crosslinked variants — a resolution the earlier case-level core papers could not offer. Blašković & Blašković (2021) supply the su
  - ▸ 출발(`peri-implant-emergence-profile-soft-tissue-conditioning-overview`) 세줄: 임플란트 출현윤곽(Emergence Profile) 설계·맞춤 연조직 컨디셔닝 11편 종합 — 임계윤곽(Critical Contour, Zone3)이 치은연 위치를, 준임계윤곽(Sub-critical Contour, Zone2)이 치조정골 안정을 결정하며(Gomez-Meda 2021), 임시보철·맞춤 치유지대주(Customized Healing Abutment)가 1차 성형 도구. 임시보철 제거 0초부터 윤곽 붕괴 시작·로그함수 회복(Li 2019) → 임시보철 유지 상태 또는 윤곽 복제 scan

- `smoking-tobacco-periodontal-implant-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Reading the OR direction**: Fan 2024 reports odds of *failure* (OR 2.59 = higher failure risk in smokers); Calciolari 2026 reports odds of *survival* (OR 0.40 = lower survival odds in smokers, i.e. roughly consistent ~2.5× relative failure risk when inverted). The two framings are complementary, not contradictory — early-window failure (Fan) and full-follow-up survival (Calciolari) both land in 
  - ▸ 출발(`smoking-tobacco-periodontal-implant-overview`) 세줄: 흡연·담배제품과 치주-임플란트 위험 9편 종합 — 기전(Apatzidou 2022) → 임플란트 생존/MBL 수렴 근거(Mustapha 2022·Fan 2024·**Calciolari 2026**) → 용량-반응(Naseri 2020) → 금연 효과(Caggiano 2022) → 수술 합병증(Wang 2023, 슈나이더막 천공) → 2026년 신규 노출경로(Ye 2026 비흡연자 간접흡연, La Rosa 2026 전자담배 미생물총, Calciolari 2026의 무연담배·전자담배 하위분석). 궐련

- `osseodensification-clinical-applications` [overviews] (HIGH-far→changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift, '대비되는' · 대비)
  - **근거 문장**: - [[sinus-lift/transcrestal/changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift]] — **(retracted/철회됨 — 인용 금지)** CW-OD 버(HaeNaem) 경치조 간접 거상 전향적 단일군 (n=12, RCBH 6–8mm, 무이식, 4mo CBCT 4방향 골고↑): Densah CCW 패러다임과 대비되는 유일한 CW OD 임상 데이터였으나 이후 철회됨 [근거 무효]
  - ▸ 출발(`osseodensification-clinical-applications`) 세줄: Fontes Pereira 2023 SR을 spine으로 33편을 4개 임상 시나리오(상악동저 보강·좁은 ridge·저밀도골 D3–D4·즉시식립)에 허브-스포크로 통합. 일관된 이득은 삽입토크(Insertion Torque, IT) 상승 — 벤치·사체·동물·임상 전 계층에서 재현; in vitro 골-임플란트 접촉률(BIC) ~3배; 그러나 임플란트 안정성 지수(Implant Stability Quotient, ISQ)는 2025년 두 독립 인체 SR+MA(Mohammadi 2025 7편 NS·S

- `resin-light-curing-degree-of-conversion-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 간접수복에서는 하이브리드 세라믹(hybrid ceramic, CAD/CAM) 두께가 광감쇠(light attenuation) 변수: 2.5mm 두께에서 이중중합 레진 시멘트(dual-cure resin cement)만 적절한 DC 유지(30.88%); 플로어블 복합레진은 11.69%로 급락; 이중중합 시멘트 선택에는 pH(NX3 Nexus 5.84, 더 중성) vs 방사선불투과도(Variolink N 2.00mmAl, ytterbium, 유의 우위) 상충관계(Aguirre-Gil 2026).
  - ▸ 출발(`resin-light-curing-degree-of-conversion-overview`) 세줄: 4편의 in-vitro 연구(2025–2026) 종합: 직접 복합레진에서 전환율(Degree of Conversion, DC) 저하의 1차 변수는 큐어링 팁-표면 거리 — 6mm 이상에서 ISO 70% 세포생존율 임계값 미달(Hashemian 2025); 노출 모드(exposure mode)는 하면 DC를 결정해 벌크필(bulk-fill)이 표준 모드에서도 45% 미만으로 떨어짐(Lehmann 2026). 간접수복에서는 하이브리드 세라믹(hybrid ceramic, CAD/CAM) 두께가 광감쇠(

- `resin-light-curing-degree-of-conversion-overview` [overviews] (HIGH-no-target, 'in contrast to' · 대조)
  - **근거 문장**: 1. **Dual-cure resin cement's chemical (self-)cure component compensates for attenuated light beneath thick indirect restorations** — this is directly demonstrated by its thickness-stable DC (Yalçinkaya), in contrast to flowable/bulk-fill composites that depend entirely on light penetration and fail once the restoration exceeds ~2.0 mm.
  - ▸ 출발(`resin-light-curing-degree-of-conversion-overview`) 세줄: 4편의 in-vitro 연구(2025–2026) 종합: 직접 복합레진에서 전환율(Degree of Conversion, DC) 저하의 1차 변수는 큐어링 팁-표면 거리 — 6mm 이상에서 ISO 70% 세포생존율 임계값 미달(Hashemian 2025); 노출 모드(exposure mode)는 하면 DC를 결정해 벌크필(bulk-fill)이 표준 모드에서도 45% 미만으로 떨어짐(Lehmann 2026). 간접수복에서는 하이브리드 세라믹(hybrid ceramic, CAD/CAM) 두께가 광감쇠(

- `trigeminal-injury-neuropathic-pain-cascade-overview` [overviews] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: ## 논쟁·불일치 (Contradiction radar)
  - ▸ 출발(`trigeminal-injury-neuropathic-pain-cascade-overview`) 세줄: 위키 13편을 엮어 치과 유래 삼차신경 손상이 만성 신경병증통증이 되는 단일 캐스케이드를 조립한 종합 페이지 — 말초/중추 경계에서 갈라진 두 문헌을 접합한다: Korczeniewska 2022는 중추 기전을 명시적으로 제외했고, Kim 2024가 정확히 그 빠진 절반(Sp5C의 NMDA/mGluR 의존 장기강화 LTP·중추감작)을 공급한다. 캐스케이드는 세 개의 정량적 게이트로 통제된다 — 손상 발생(임플란트 첨부–하악관 이격 ≥1mm에서 신경감각변화 0% vs 0–1mm 68%; Peña-Ca

- `restorative-margin-periodontal-interface-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Axis 2 — Margin location, and the Ercoli-vs-Schätzle tension.** Srimaneepong (2022) states the default cleanly: supragingival (and equigingival) margins permit hygiene and do not provoke caries or periodontal disease, whereas subgingival margins impede hygiene and risk biologic-width violation. The apparent conflict is between two reviews/cohorts. **Ercoli (2021)** — a systematically-searched na
  - ▸ 출발(`restorative-margin-periodontal-interface-overview`) 세줄: 7편 종합 — 수복 변연과 치주의 관계는 ① 생물학적 폭경/SCTA(Hamasni 2017 임상값 1.13 mm, 부위 편차 큼), ② 변연 위치(치은연상 최선, 치은연하는 탁월한 위생 시에만), ③ 변연 적합·외형(부적합·overhang이 biofilm→골소실 cascade 유발), ④ finish line 디자인(수평 vs 수직 BOPT)이라는 4축의 상호작용 결과이다. Schätzle 2001 26년 코호트는 치은연하 변연이 모든 7회 조사에서 치은지수 악화(p<0.001)를 보였고, Lam

- `trigeminal-neuralgia-neuropathy-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - TN 치료 사다리 독립 보강 (Villegas-Díaz 2024, narrative-review): 별개 문헌이 카르바마제핀(100–1200 mg/일) 1차·거의 100% 증상감소를 재확인하고, 수술 modality를 수치로 대비한다 — 미세혈관감압술 (MVD) 초기 성공률 92.7%(사망률 0.7%·연 2% 재발) vs 고주파 근절제술(Radiofrequency Rhizotomy) 즉시완화 97%이나 5년 재발 42%. 발생률 4.3/10만/년(여:남 5.9:3.4). 저자 입장: 치과에서는 약물요법이 중심, 수술은 약물저항성 사례로 한정. (narrative라 근거등급은 Khan SR보다 낮음 — 사다리를 *보강*하되 뒤집지 않음)
  - ▸ 출발(`trigeminal-neuralgia-neuropathy-overview`) 세줄: 치과 관련 신경병성 구강안면통증 wiki 6편 종합 — TN(발작성·유발점·1차 카르바마제핀/옥스카르바제핀·MVD 수술; 독립 narrative-review가 MVD-근절제술 내구성 수치로 보강)과 PTTN(시술 후 지속통; 근관치료가 의인성 신경손상의 8%), 하악 구치부 임플란트 후 감각이상(IAN/이신경, 0–55%, 대부분 6개월 내 회복), 국소마취 자체의 일과성 신경학적 합병증(안면마비·안구합병증·약제의존 감각이상), 치과의사 인식 공백(29%가 PTTN 모름·>80%가 교육 미경험)을

- `drug-analgesics-postop-pain-overview` [overviews] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: > - 단, **술전 corticosteroid는 매복 제3대구치에서 명확히 유효** — 술전 dexamethasone 4mg 근육주사 1회가 위약 대비 통증·개구량·부종 모두 개선(Tamgadge 2025 split-mouth RCT, n=60, day7 VAS 0.4 vs 1.6 p<0.001). NSAID-preemptive 무효(Costa)와 대비되는, 제3대구치 술전 약제의 핵심 옵션.
  - ▸ 출발(`drug-analgesics-postop-pain-overview`) 세줄: 치과 술후 통증 24편(Network MA 5·SR+MA 4·SR 1·Cochrane overview 2·RCT 6·narrative 6) 통합: 1차 선택은 Ibuprofen 400mg + Acetaminophen 1000mg 병용, NNT ≈1.5(Miroshnychenko 2023 NMA 82 RCT n=9,095); Opioid는 비-opioid 대비 우월하지 않음(Feldman 2024 RCT n=1,815, 전 시점 열등·tramadol=위약); 교대 투약이 구제 투약 필요 15% vs

- `drug-analgesics-postop-pain-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[drug/analgesics/tamgadge-2025-preoperative-dexamethasone-third-molar-pain-swelling-trismus]] — contradicts/extends: NSAID-preemptive 무효(Costa)와 달리 술전 dexamethasone은 third molar에 유효 (rct, 2025)
  - ▸ 출발(`drug-analgesics-postop-pain-overview`) 세줄: 치과 술후 통증 24편(Network MA 5·SR+MA 4·SR 1·Cochrane overview 2·RCT 6·narrative 6) 통합: 1차 선택은 Ibuprofen 400mg + Acetaminophen 1000mg 병용, NNT ≈1.5(Miroshnychenko 2023 NMA 82 RCT n=9,095); Opioid는 비-opioid 대비 우월하지 않음(Feldman 2024 RCT n=1,815, 전 시점 열등·tramadol=위약); 교대 투약이 구제 투약 필요 15% vs

- `keratinized-mucosa-peri-implant-health-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 6. **Apparent contradictions between Ravidà's TSA-null results and the positive MBL signals from Zhang 2025 and Sabri 2025 are resolvable by study design differences, not biological inconsistency.** Ravidà 2022 restricted to interventional designs with comparison arms (1 RCT, 3 non-RCTs, 5 prospective cohorts) to avoid reverse-causation bias — this is methodologically correct but drastically limit
  - ▸ 출발(`keratinized-mucosa-peri-implant-health-overview`) 세줄: 10편 종합(우산 2, SR+MA 3, 전향 1, 전문가합의 2, SR 1, 서술고찰 1): 각화점막 폭(KMW) ≥2 mm 역치는 모든 근거 등급에서 수렴; 연조직 대리지표(치태 TSA-확정 OR 2.78, 염증 eOR 3.13–5.34, 퇴축 eOR 4.05)에는 연관성이 강하고 일관적; 임플란트주위염·MBL 연관성은 방향성 존재하나 TSA상 검정력 부족(I²=80–97%). Roccuzzo 2025 전향 코호트(20년, n=64, 하악 구치부): KM 없음 → 임플란트주위염 25% vs KT

- `veneer-preparation-design-minimally-invasive-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: 4. **Minimal-prep veneers (0.2–0.5 mm) equal or exceed conventional (0.3–1.0 mm) in survival.** Ali (2023), SR of 4 comparative studies, refuting prior assumption of conventional superiority; ultra-thin contact-lens feldspathic types add no-anesthesia / no-temporary benefits. [SR — no comparative RCT]
  - ▸ 출발(`veneer-preparation-design-minimally-invasive-overview`) 세줄: 6편 종합(전향 임상 1·SR 1·SR+MA 1·내러티브 1·증례 2): 최소침습 비니어 삭제는 목업/APT를 통과해 최종 보철 형태 기준으로 시행하며 삭제량은 기질-목표색 차이로 정량화(P = LT − EV); 추가부피 ≥ 도재두께이면 P = 0(진정한 무삭제). 패러다임 진화: 아날로그 APT(Gürel 2007) → 색 수식(Coachman 2014) → 디지털 CAD-CAM 목업(Cattoni 2016, 108 PLV 2년); 생존 근거(Ali SR·Reis 12년·Chandode·Alba

- `interdental-cleaning-devices-synthesis` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **올바른 술식조차 치실 효능을 살리지 못한다(Jung 2025, 전향 n=37)**: 동영상 교육으로 치실 술식(Flossing Performance Score, FPS 2.0→2.83, p<.001)은 향상됐으나 치태 제거(PSPI 차이 0.17 vs 0.21, p=.112)는 개선되지 않았고 술식과 무관 — "치실은 기술만 가르치면 된다"는 통념을 반박, DF를 좁은 접촉 한정으로 두는 결정을 보강.
  - ▸ 출발(`interdental-cleaning-devices-synthesis`) 세줄: 치간 청소도구 21편 종합(+토스픽법 overview), Cochrane 우산 SR(Worthington 2019, RCT 35편·n=3929: 치실/치간칫솔+칫솔질이 칫솔질 단독보다 나을 가능성은 있으나 low~very low certainty, 치간 우식 평가 연구 0편)이 전체 틀을 제공: 보편적 우승 도구 없음 — **순응도가 도구보다 중요**(Yilmaz 2025 RCT n=54: 고무 치간 픽 12.61주 vs 치실 4.96주 규칙적 사용, p=0.003; Jung 2025 n=37: 

- `abutment-screw-preload-joint-stability-overview` [overviews] (SOFT→varvara-2020-retightening-preload-loss-abutment-screws, 'challenges the' · 도전)
  - **근거 문장**: - [[prosthetic-materials/varvara-2020-retightening-preload-loss-abutment-screws]] — retightening-interval study: 2 min minimized preload loss better than 5/10 min (challenges the 10-min standard); internal hex retains more preload than external hex at every interval.
  - ▸ 출발(`abutment-screw-preload-joint-stability-overview`) 세줄: 18편 종합: 나사 풀림(5년 ~10.4%, 10년 ~20.8%)은 전하중 손실이 원인이며, 기전은 세틀링(무하중에서도 2–10%)과 동적 피로(제거토크 손실 16.1–39%) 둘 — 마찰·조도가 핵심 레버(가해진 토크 중 ~8–10%만 전하중化; 탄소코팅 나사 10회 재사용 시 전하중 329.9→253.7 N 감소, Sagheb 2023). 재조임이 세틀링 보상(최적 시점 논쟁: 10분 Nithyapriya 2018·Vinhas 2022 vs 2분 Varvara 2020; 2회째에 plateau
  - ▸ 대상(`varvara-2020-retightening-preload-loss-abutment-screws`) 세줄: 체외 연구(n=80; 내부 육각형(Internal Hexagon, IG) 40개·외부 육각형(External Hexagon, EG) 40개; 35 Ncm; 재조임 간격별 n=10: 대조군/2분/5분/10분; 30분 후 제거 토크 측정). 초기 조임 후 2분 재조임이 양쪽 연결부에서 예압(preload) 소실을 가장 효과적으로 최소화(p<0.05 vs 대조군); 내부 육각형이 외부 육각형보다 예압 유지 우수; 기존 권장 10분 재조임은 그 사이 추가 안착(settling)이 발생하여 차선. 최적 재

- `immediate-implant-infected-sites-decision` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Apparent contradiction**: Muñoz-Cámara 2020 shows 100% survival placing implants immediately in "acute periapical infection" sites. Prati 2017 recommends 8–12 weeks for acute abscess.
  - ▸ 출발(`immediate-implant-infected-sites-decision`) 세줄: 10편(SR+MA 2·SR 2·전향 3·후향 2·MA 1; 2015–2025) 합성: 핵심 변수는 '감염 자체'가 아닌 **감염 유형** — 만성 치근단 병변(chronic periapical lesion)은 철저한 소파+항생제 예방 시 비감염 부위와 생존율 동등(RR=0.99, Saijeva 2020; Pranckeviciene 2024 SR+MA); 급성 화농성 농양(acute purulent abscess)은 8–12주 조기식립(Early placement)이 24개월 변연골 소실(Margi

- `sinus-lift-lateral-2026-synthesis` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **점막비후(Mucosal Thickening, MT)의 원인은 치성·치주성** — MT 자체는 임플란트 금기가 아님(Maska 2017: 93%에 MT·65%가 >5mm여도 임플란트·이식 생존율 100%, 치주질환 과거력만 유일 예측인자 p=0.004). 무엇이 MT를 만드는가는 정량화됨: Khalil 2024(992치)에서 치근단병소(보정교차비 AOR 32.7)·제1대구치(AOR 3.97)·중증치주염(AOR 2.75)이 독립 예측인자이고, **발치된 부위가 MT 위험 최저** → 치아의 존재 자체가 MT의 odontogenic 동력. 잔존치조골높이(Residual Ridge Height, RRH)가 낮을수록 MT 심함(Akbari 2022, 240동 — RRH↓↔MT↑ 역상관; 단 Maska 20
  - ▸ 출발(`sinus-lift-lateral-2026-synthesis`) 세줄: 측방창(Lateral Window) 상악동거상술(Sinus Floor Elevation, SFE) 37편 종합(5개 클러스터) — 슈나이더막 천공(Sinus Membrane Perforation, SMP)·부비동염·술식 변형·이식재/PRF 보조. 수리된 천공은 임플란트 식립 금기가 아님(임플란트 손실 ~4%, OR 1.35 비유의; Soares 2024 SR+MA 130편, Sala 2024 6,860개); 격벽(OR 4.03, HR 8.07)·점액저류낭(HR 27.75)이 해부학적 최대 위험인자

- `sinus-lift-lateral-2026-synthesis` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **What drives mucosal thickening — odontogenic and periodontal sources.** Mucosal thickening (MT) is overwhelmingly a marker of adjacent tooth/periodontal disease rather than a primary sinus disorder, which reframes it as a preoperative *risk-stratification* finding rather than a contraindication. Maska 2017 (retrospective CBCT, n=29, mean follow-up 3.3 yr) found 93.1% of sinuses had MT (65.5% s
  - ▸ 출발(`sinus-lift-lateral-2026-synthesis`) 세줄: 측방창(Lateral Window) 상악동거상술(Sinus Floor Elevation, SFE) 37편 종합(5개 클러스터) — 슈나이더막 천공(Sinus Membrane Perforation, SMP)·부비동염·술식 변형·이식재/PRF 보조. 수리된 천공은 임플란트 식립 금기가 아님(임플란트 손실 ~4%, OR 1.35 비유의; Soares 2024 SR+MA 130편, Sala 2024 6,860개); 격벽(OR 4.03, HR 8.07)·점액저류낭(HR 27.75)이 해부학적 최대 위험인자

- `sinus-lift-lateral-2026-synthesis` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[sinus-lift/lateral/akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height]] — lower residual ridge height correlates with greater MT (contradicts Maska null finding)
  - ▸ 출발(`sinus-lift-lateral-2026-synthesis`) 세줄: 측방창(Lateral Window) 상악동거상술(Sinus Floor Elevation, SFE) 37편 종합(5개 클러스터) — 슈나이더막 천공(Sinus Membrane Perforation, SMP)·부비동염·술식 변형·이식재/PRF 보조. 수리된 천공은 임플란트 식립 금기가 아님(임플란트 손실 ~4%, OR 1.35 비유의; Soares 2024 SR+MA 130편, Sala 2024 6,860개); 격벽(OR 4.03, HR 8.07)·점액저류낭(HR 27.75)이 해부학적 최대 위험인자

- `periodontal-host-modulation-nutraceutical-adjuncts-overview` [periodontics] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: > - **CoQ10 — 구형 SR과의 충돌**: 기존 11편 SR+MA는 CoQ10가 5개 지표를 유의 개선(PD SMD −0.96)하며 **겔 사용을 권장**한다고 결론했으나, 이질성 매우 높고(I² 72–89%) 비뚤림 위험 높은 연구에서 효과가 과대평가됨 (Rasoolzadeh 2022). → 두 SR의 상반된 결론은 RoB·route 층화로 설명됨; 신형 SR이 우선.
  - ▸ 출발(`periodontal-host-modulation-nutraceutical-adjuncts-overview`) 세줄: 숙주조절·영양보조제(오메가-3·CoQ10·항산화비타민·아보카도/대두 불검화물(ASU)·멜라토닌·국소 독시사이클린) 7편 종합 — 모두 통계적으로는 검출되나 1 mm 미만·low~very-low 확실성의 치주낭깊이(Probing Pocket Depth, PPD)/임상부착수준(Clinical Attachment Level, CAL) 이득에 그침. 양성 메타분석이 가이드라인(유럽치주학회(EFP) 오메가-3 반대) 및 서로(CoQ10: 겔 권장 구형 SR vs 겔 무효 신형 경로층화 SR)와 충돌; 임상

- `periodontal-host-modulation-nutraceutical-adjuncts-overview` [periodontics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Reconciliation:** the contradiction (gel recommended vs gel inert) is an artifact of pooling high-RoB trials without route stratification. Prefer the newer route-stratified appraisal; treat any CoQ10 claim as very-low certainty.
  - ▸ 출발(`periodontal-host-modulation-nutraceutical-adjuncts-overview`) 세줄: 숙주조절·영양보조제(오메가-3·CoQ10·항산화비타민·아보카도/대두 불검화물(ASU)·멜라토닌·국소 독시사이클린) 7편 종합 — 모두 통계적으로는 검출되나 1 mm 미만·low~very-low 확실성의 치주낭깊이(Probing Pocket Depth, PPD)/임상부착수준(Clinical Attachment Level, CAL) 이득에 그침. 양성 메타분석이 가이드라인(유럽치주학회(EFP) 오메가-3 반대) 및 서로(CoQ10: 겔 권장 구형 SR vs 겔 무효 신형 경로층화 SR)와 충돌; 임상

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: > - 이 페이지의 핵심 명제: 치조제 보존술(Alveolar Ridge Preservation, ARP)은 보편 권고가 아니라 **시나리오 의존적 개입**이며, "언제 안 해도 되나·왜 실패하나·무엇을 더할 수 있나"를 다루는 do-ARP의 짝(counterpoint) 페이지다.
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 세줄: 발치와 자연 치유 생물학 + ARP 한계·과잉치료 비판 5축 종합 — do-ARP 페이지의 대응쌍: 협측골 흡수는 다발골(bundle bone) 의존으로 생물학적 불가피(Araujo 2005), 협설폭 1년 ~50% 감소의 2/3이 첫 3개월 발생(Schropp 2003). ARP는 차원 보존이지 골 질 향상이 아님 — 6개월 신생골 16%·잔류 이종골 32%(Poli 2017); ARP 후 임플란트 실패 단일 유의 예측인자 = 순수골 결합(Pristine Bone Engagement, PBE) 

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Synthesis (counterpoint to the do-ARP protocol-ladder page) across 5 axes — socket healing biology, ARP critical appraisal (when NOT to graft), post-ARP implant failure predictors, adjunct materials, and beyond-ARP scenarios: post-extraction buccal resorption is biologically inevitable (bundle-bone dependence; Araujo 2005 dog histology), ~50% of buccolingual width lost by 1 year with 2/3 occurring
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 세줄: 발치와 자연 치유 생물학 + ARP 한계·과잉치료 비판 5축 종합 — do-ARP 페이지의 대응쌍: 협측골 흡수는 다발골(bundle bone) 의존으로 생물학적 불가피(Araujo 2005), 협설폭 1년 ~50% 감소의 2/3이 첫 3개월 발생(Schropp 2003). ARP는 차원 보존이지 골 질 향상이 아님 — 6개월 신생골 16%·잔류 이종골 32%(Poli 2017); ARP 후 임플란트 실패 단일 유의 예측인자 = 순수골 결합(Pristine Bone Engagement, PBE) 

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: 본 페이지는 wiki/bone-regeneration/ 의 20 개 미합성 paper (생물학 기초·비판적 review·실패 예측인자·보조 재료·인접 시나리오) 를 5축으로 재분류한 spine. Protocol-ladder 페이지의 do-ARP 흐름에 대한 counterpoint — clinical paralysis 가 아닌 patient-specific 결정 도구로 사용.
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 세줄: 발치와 자연 치유 생물학 + ARP 한계·과잉치료 비판 5축 종합 — do-ARP 페이지의 대응쌍: 협측골 흡수는 다발골(bundle bone) 의존으로 생물학적 불가피(Araujo 2005), 협설폭 1년 ~50% 감소의 2/3이 첫 3개월 발생(Schropp 2003). ARP는 차원 보존이지 골 질 향상이 아님 — 6개월 신생골 16%·잔류 이종골 32%(Poli 2017); ARP 후 임플란트 실패 단일 유의 예측인자 = 순수골 결합(Pristine Bone Engagement, PBE) 

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: | [[bone-regeneration/ridge-preservation/araujo-2009-ridge-alterations-flap-vs-flapless]] | animal (dog, split-mouth) | **"Flapless = ridge 보존" myth 반박**. flap 유무가 ridge 흡수 크기를 의미있게 바꾸지 않음. Flapless 의 가치는 vascular preservation 가설 아닌 술자·환자 부담 감소 |
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 세줄: 발치와 자연 치유 생물학 + ARP 한계·과잉치료 비판 5축 종합 — do-ARP 페이지의 대응쌍: 협측골 흡수는 다발골(bundle bone) 의존으로 생물학적 불가피(Araujo 2005), 협설폭 1년 ~50% 감소의 2/3이 첫 3개월 발생(Schropp 2003). ARP는 차원 보존이지 골 질 향상이 아님 — 6개월 신생골 16%·잔류 이종골 32%(Poli 2017); ARP 후 임플란트 실패 단일 유의 예측인자 = 순수골 결합(Pristine Bone Engagement, PBE) 

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "즉시식립이면 골 보존된다" — Araujo 2005 반박. 즉시식립도 협측 붕괴 막지 못함.
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 세줄: 발치와 자연 치유 생물학 + ARP 한계·과잉치료 비판 5축 종합 — do-ARP 페이지의 대응쌍: 협측골 흡수는 다발골(bundle bone) 의존으로 생물학적 불가피(Araujo 2005), 협설폭 1년 ~50% 감소의 2/3이 첫 3개월 발생(Schropp 2003). ARP는 차원 보존이지 골 질 향상이 아님 — 6개월 신생골 16%·잔류 이종골 32%(Poli 2017); ARP 후 임플란트 실패 단일 유의 예측인자 = 순수골 결합(Pristine Bone Engagement, PBE) 

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "Flapless 발치가 ridge 를 보존한다" — Araujo 2009 반박. flap 유무가 흡수 크기를 거의 안 바꿈.
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 세줄: 발치와 자연 치유 생물학 + ARP 한계·과잉치료 비판 5축 종합 — do-ARP 페이지의 대응쌍: 협측골 흡수는 다발골(bundle bone) 의존으로 생물학적 불가피(Araujo 2005), 협설폭 1년 ~50% 감소의 2/3이 첫 3개월 발생(Schropp 2003). ARP는 차원 보존이지 골 질 향상이 아님 — 6개월 신생골 16%·잔류 이종골 32%(Poli 2017); ARP 후 임플란트 실패 단일 유의 예측인자 = 순수골 결합(Pristine Bone Engagement, PBE) 

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: | [[bone-regeneration/ridge-preservation/adams-2022-clinical-evidence-alveolar-ridge-preservation]] | narrative-review + case (BDJ) | **수정주의 counterpoint**. 5-13y 후 xenograft 만성 섬유 포함·peri-implantitis 양상 case. "통계적 dimensional preservation" ≠ "long-term patient benefit". 상업적 압력 (BSM 시장 ARP 29%) 환기 |
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 세줄: 발치와 자연 치유 생물학 + ARP 한계·과잉치료 비판 5축 종합 — do-ARP 페이지의 대응쌍: 협측골 흡수는 다발골(bundle bone) 의존으로 생물학적 불가피(Araujo 2005), 협설폭 1년 ~50% 감소의 2/3이 첫 3개월 발생(Schropp 2003). ARP는 차원 보존이지 골 질 향상이 아님 — 6개월 신생골 16%·잔류 이종골 32%(Poli 2017); ARP 후 임플란트 실패 단일 유의 예측인자 = 순수골 결합(Pristine Bone Engagement, PBE) 

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: **손상된(damaged) socket 의 biologic 보강 — Kim 2020 · Park 2022 (Yonsei 비글견)**: 위 adjunct 논의는 대체로 intact socket 가정인데, 두 Yonsei 동물 study 는 **2벽 결손/손상 socket** 의 생물학적 보강을 직접 다룬다. Kim 2020(비글견 n=5, split-mouth)은 rhBMP-2 의 적용 **timing** 을 분리 — CBCP 에 BMP-2 를 즉시 적용한 군이 2주 지연 주입군보다 신생골 면적이 유의하게 컸다(10.8 vs 6.3 mm², p=0.043; 폭경 차이 없음). 초기 염증은 즉시군에서 더 강했으나 결과를 악화시키지 않아, "염증 가라앉은 뒤 지연 주입이 낫다"는 가설을 반박하고 **손상 sock
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 세줄: 발치와 자연 치유 생물학 + ARP 한계·과잉치료 비판 5축 종합 — do-ARP 페이지의 대응쌍: 협측골 흡수는 다발골(bundle bone) 의존으로 생물학적 불가피(Araujo 2005), 협설폭 1년 ~50% 감소의 2/3이 첫 3개월 발생(Schropp 2003). ARP는 차원 보존이지 골 질 향상이 아님 — 6개월 신생골 16%·잔류 이종골 32%(Poli 2017); ARP 후 임플란트 실패 단일 유의 예측인자 = 순수골 결합(Pristine Bone Engagement, PBE) 

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - [[bone-regeneration/ridge-preservation/araujo-2009-ridge-alterations-flap-vs-flapless]] — flapless myth 반박
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 세줄: 발치와 자연 치유 생물학 + ARP 한계·과잉치료 비판 5축 종합 — do-ARP 페이지의 대응쌍: 협측골 흡수는 다발골(bundle bone) 의존으로 생물학적 불가피(Araujo 2005), 협설폭 1년 ~50% 감소의 2/3이 첫 3개월 발생(Schropp 2003). ARP는 차원 보존이지 골 질 향상이 아님 — 6개월 신생골 16%·잔류 이종골 32%(Poli 2017); ARP 후 임플란트 실패 단일 유의 예측인자 = 순수골 결합(Pristine Bone Engagement, PBE) 

- `bone-regeneration-socket-biology-and-arp-critique` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [ ] 본 페이지는 do-ARP 의 counterpoint. 새 critical review · 새 failure predictor study ingest 시 갱신.
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 세줄: 발치와 자연 치유 생물학 + ARP 한계·과잉치료 비판 5축 종합 — do-ARP 페이지의 대응쌍: 협측골 흡수는 다발골(bundle bone) 의존으로 생물학적 불가피(Araujo 2005), 협설폭 1년 ~50% 감소의 2/3이 첫 3개월 발생(Schropp 2003). ARP는 차원 보존이지 골 질 향상이 아님 — 6개월 신생골 16%·잔류 이종골 32%(Poli 2017); ARP 후 임플란트 실패 단일 유의 예측인자 = 순수골 결합(Pristine Bone Engagement, PBE) 

- `immediate-dentin-sealing-evidence-synthesis` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Clinical outcomes are contested — SR+MAs on postoperative sensitivity (POS) directly conflict: Alghauli 2025 (11 studies) reports IDS significantly reduces POS (P<.05) and improves clinical survival (96.4–100% vs non-IDS 81.8–96.7%), while Josic 2022 (4 studies, GRADE low) finds no significant POS difference; the gap is insufficient sample size and heterogeneity, not a refutation.
  - ▸ 출발(`immediate-dentin-sealing-evidence-synthesis`) 세줄: 8편 종합 — 근거가 2층으로 갈림: ①**in-vitro 결합강도**는 강하고 일관됨(Hardan 2022 SR+MA 21편: IDS > DDS; Magne 2005: IDS 58 MPa vs DDS 12 MPa; 임시보철 12주까지 결합 보존(Magne 2007); Abo-Alazm 2022: 생리적 치수압+universal 접착제 조건 확인) — 효과 최대는 3-step E&R 또는 접착제+flowable, MDP-함유 universal 우선. ②**임상 outcome**은 논쟁적 — 술후과

- `immediate-dentin-sealing-evidence-synthesis` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: ②**임상 outcome**은 논쟁적 — 술후과민(Postoperative Sensitivity, POS)에서 Alghauli 2025(11편, IDS 유의 감소 P<.05 + 생존율 이득: IDS 96.4–100% vs non-IDS 81.8–96.7%)와 Josic 2022(4편, GRADE low, 차이 없음)가 정면충돌; 차이의 원인은 표본 크기 부족·이질성이지 반박이 아님.
  - ▸ 출발(`immediate-dentin-sealing-evidence-synthesis`) 세줄: 8편 종합 — 근거가 2층으로 갈림: ①**in-vitro 결합강도**는 강하고 일관됨(Hardan 2022 SR+MA 21편: IDS > DDS; Magne 2005: IDS 58 MPa vs DDS 12 MPa; 임시보철 12주까지 결합 보존(Magne 2007); Abo-Alazm 2022: 생리적 치수압+universal 접착제 조건 확인) — 효과 최대는 3-step E&R 또는 접착제+flowable, MDP-함유 universal 우선. ②**임상 outcome**은 논쟁적 — 술후과

- `socket-shield-technique-overview` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: SST is appropriate for esthetic-zone single immediate implants where buccal-plate preservation is critical and CTG/xenograft alternatives are insufficient: thin but intact buccal plate, no vertical fracture or active infection — not appropriate for operators without SST-specific training or rescue-plan capability; newer abstract-only evidence (Brazyte 2025 SR+MA, Gurbuz 2024 non-grafted RCT, Kotsa
  - ▸ 출발(`socket-shield-technique-overview`) 세줄: 17개 위키 페이지 + 초록 수준 4편 — 소켓실드 기법(Socket Shield Technique, SST): 즉시식립 시 협측 치근 조각("실드")을 남겨 다발골(bundle bone)과 치주인대(PDL) 혈류를 보존함으로써 발치 후 협측골 흡수에 대응. SR+MA+RCT가 통상 즉시식립 대비 협측 골판·핑크 심미 보존 우월로 수렴(Oliva 2023 SR: 협측골 흡수(BBPR) 0.32 vs 1.05 mm, 변연골소실(MBL) 0.39 vs 1.00 mm, 핑크심미점수(PES) 12.08 

- `socket-shield-technique-overview` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: A 2026-06-28 update folds in four further reviews/RCTs at **abstract level only** (full text not yet retrieved, so no point estimates are imported — direction-of-effect citations only): **Brazyte 2025** (SR+MA, *Stomatologija*, PMID 41628481) as a newer pooled estimate of SST vs conventional; **Gurbuz 2024** (RCT, *Int J Oral Maxillofac Surg*, PMID 39648089) testing the shield in a **non-grafted**
  - ▸ 출발(`socket-shield-technique-overview`) 세줄: 17개 위키 페이지 + 초록 수준 4편 — 소켓실드 기법(Socket Shield Technique, SST): 즉시식립 시 협측 치근 조각("실드")을 남겨 다발골(bundle bone)과 치주인대(PDL) 혈류를 보존함으로써 발치 후 협측골 흡수에 대응. SR+MA+RCT가 통상 즉시식립 대비 협측 골판·핑크 심미 보존 우월로 수렴(Oliva 2023 SR: 협측골 흡수(BBPR) 0.32 vs 1.05 mm, 변연골소실(MBL) 0.39 vs 1.00 mm, 핑크심미점수(PES) 12.08 

- `zirconia-types-clinical-selection` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: **오판 패턴**: "유약이 매끄러워서 마모 적다" — Shah 2024 + Steiner 2024 직접 반박. 유약이 첫 layer 마모 후 거친 표면 노출. [확인]
  - ▸ 출발(`zirconia-types-clinical-selection`) 세줄: 치과용 지르코니아 grade 선택 5축 sub-overview: 이트리아 함량 ↑ = 투명도 ↑·강도 ↓(3Y-TZP ~1200 MPa → 5Y-PSZ ~600–800 → UHTZ ~300–500 MPa; Ban 2023); grade × 적응증 매트릭스 — 후방부 FPD/고하중 → 3Y-TZP, 전치부 단관 → 5Y-PSZ/multilayer, 전치부 단교 → 4Y-PSZ. 모든 grade 공통 최소 교합면 두께 1.5 mm 필수, 두께 <1 mm 시 파절 급증(Ali 2023 SR+MA); 대

- `zirconia-types-clinical-selection` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: **오판 패턴**: "5Y-PSZ 는 cubic 이라 MDP 약하다" — Comba 2021 반박. Cubic 도 hydroxyl group 노출되어 MDP 반응. [확인]
  - ▸ 출발(`zirconia-types-clinical-selection`) 세줄: 치과용 지르코니아 grade 선택 5축 sub-overview: 이트리아 함량 ↑ = 투명도 ↑·강도 ↓(3Y-TZP ~1200 MPa → 5Y-PSZ ~600–800 → UHTZ ~300–500 MPa; Ban 2023); grade × 적응증 매트릭스 — 후방부 FPD/고하중 → 3Y-TZP, 전치부 단관 → 5Y-PSZ/multilayer, 전치부 단교 → 4Y-PSZ. 모든 grade 공통 최소 교합면 두께 1.5 mm 필수, 두께 <1 mm 시 파절 급증(Ali 2023 SR+MA); 대

- `cracked-tooth-syndrome-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - [[endodontics/shaping/rathke-2024-ex-vivo-minimally-invasive-endodontic]] — Ex vivo (n=18/군): 최소침습 근관성형(#40/.04)이 관행확대(#80) 대비 VRF·균열 유의하게 줄이지 못함 — "성형 최소화=파절 예방" 통념에 대한 반증적 신호(직접 반박은 아니나 근거 부재)
  - ▸ 출발(`cracked-tooth-syndrome-overview`) 세줄: 20편 종합: CTS는 종방향 파절 5-type(craze line → fractured cusp → cracked tooth → split tooth → VRF) 중 incomplete fracture 항목 — ESE Patel 2025 합의문이 표준 용어 확정 및 "CTS" 라벨 폐기 권고; 진단은 multi-modal framework 필수(정량 정확도: 투조 특이도 53.6%, 현미경 특이도 93%, QLF κ 0.66–0.74, AI AUC 0.82). 핵심 tension: Kaur 20

- `resin-dentin-bond-durability-degradation-overview` [overviews] (SOFT→talungchit-2014-ethanol-wet-bonding-chlorhexidine-resin-dentin-durability, 'However, the' · 그러나(단서))
  - **근거 문장**: Ethanol-wet bonding (replacing water with ethanol before hydrophobic resin) plus CHX improves in-vitro durability ([[resin-bonding/talungchit-2014-ethanol-wet-bonding-chlorhexidine-resin-dentin-durability]]). However, the "moist dentin" dogma is weakening clinically: across 5 split-mouth NCCL RCTs, **dry vs wet etch-and-rinse bonding showed no difference** in retention or sensitivity ([[resin-bond
  - ▸ 출발(`resin-dentin-bond-durability-degradation-overview`) 세줄: 위키 16편 7축 종합: 레진-상아질 결합 열화의 두 기전은 친수성 수지의 가수분해(hydrolysis)와 물이 많고 수지가 적은 혼성층(hybrid layer) 콜라겐의 기질금속단백분해효소(Matrix Metalloproteinase, MMP)/카텝신(cathepsin) 분해이며, 공통 원흉은 잔류 물(residual water) — 형태학적으로 나노누출(nanoleakage)·수분수(water-tree, Tay 2003·2005)로 나타남. 임상 지지 근거가 있는 유일한 내구성 보조법은 클로르
  - ▸ 대상(`talungchit-2014-ethanol-wet-bonding-chlorhexidine-resin-dentin-durability`) 세줄: In vitro micro-Raman + µTBS + TEM 연구 (3단계 산부식 접착제 하에서 에탄올 습식 접착[ethanol-wet bonding, EW] vs 수습식[WW]; ±클로르헥시딘[CHX]; 즉시·7개월·1년 노화 측정; 초록만 확보). EW가 혼성층 전역에 걸쳐 bis-GMA·TEG-DMA 몰 농도와 µTBS를 즉시 및 노화 후 모두 WW 대비 유의하게 향상; CHX 추가 시 1년 후 EW군에서 콜라겐 보존 강화 및 나노누출 감소. 잔류 수분을 에탄올로 치환 후 소수성 접착제를 적

- `resin-dentin-bond-durability-degradation-overview` [overviews] (AMBIG→forville-2024-moist-dentin-adhesive-systems-reevaluation, 'However, the' · 그러나(단서))
  - **근거 문장**: Ethanol-wet bonding (replacing water with ethanol before hydrophobic resin) plus CHX improves in-vitro durability ([[resin-bonding/talungchit-2014-ethanol-wet-bonding-chlorhexidine-resin-dentin-durability]]). However, the "moist dentin" dogma is weakening clinically: across 5 split-mouth NCCL RCTs, **dry vs wet etch-and-rinse bonding showed no difference** in retention or sensitivity ([[resin-bond
  - ▸ 출발(`resin-dentin-bond-durability-degradation-overview`) 세줄: 위키 16편 7축 종합: 레진-상아질 결합 열화의 두 기전은 친수성 수지의 가수분해(hydrolysis)와 물이 많고 수지가 적은 혼성층(hybrid layer) 콜라겐의 기질금속단백분해효소(Matrix Metalloproteinase, MMP)/카텝신(cathepsin) 분해이며, 공통 원흉은 잔류 물(residual water) — 형태학적으로 나노누출(nanoleakage)·수분수(water-tree, Tay 2003·2005)로 나타남. 임상 지지 근거가 있는 유일한 내구성 보조법은 클로르

- `resin-dentin-bond-durability-degradation-overview` [overviews] (AMBIG→zheng-2024-dentin-conditioners-bond-strength-sr, 'However, the' · 그러나(단서))
  - **근거 문장**: Ethanol-wet bonding (replacing water with ethanol before hydrophobic resin) plus CHX improves in-vitro durability ([[resin-bonding/talungchit-2014-ethanol-wet-bonding-chlorhexidine-resin-dentin-durability]]). However, the "moist dentin" dogma is weakening clinically: across 5 split-mouth NCCL RCTs, **dry vs wet etch-and-rinse bonding showed no difference** in retention or sensitivity ([[resin-bond
  - ▸ 출발(`resin-dentin-bond-durability-degradation-overview`) 세줄: 위키 16편 7축 종합: 레진-상아질 결합 열화의 두 기전은 친수성 수지의 가수분해(hydrolysis)와 물이 많고 수지가 적은 혼성층(hybrid layer) 콜라겐의 기질금속단백분해효소(Matrix Metalloproteinase, MMP)/카텝신(cathepsin) 분해이며, 공통 원흉은 잔류 물(residual water) — 형태학적으로 나노누출(nanoleakage)·수분수(water-tree, Tay 2003·2005)로 나타남. 임상 지지 근거가 있는 유일한 내구성 보조법은 클로르

- `occlusal-veneer-tooth-wear-erosion-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 피로(fatigue) vs 정적파절 순위 상충: maldonado는 3편 중 2편 복합레진 피로 우위, al-akhali는 세라믹 정적 우위, schlichting은 복합레진 표면 열화(거칠기 p=.003)↑ — 피로·정적·표면내구성 순위가 갈림.
  - ▸ 출발(`occlusal-veneer-tooth-wear-erosion-overview`) 세줄: 교합면 비니어(Occlusal/Table-top Veneer) 7편 종합(in-vitro 4·SR 1·RCT 1·후향 case series 1): 초박형 세라믹(0.5–0.8 mm)은 생리적 구치 교합력(400–800 N)을 훨씬 상회하고(al-Akhali 2017: 120만 회·98N 저작 100% 생존), 재료 종류(세라믹 vs CAD/CAM 복합레진)는 임상 생존율에 무의미(세라믹 93–100% vs 복합레진 84–87%, 모두 NS). 최소두께 논쟁은 미해결: 0.7/1.0 mm만 안전하다

- `occlusal-veneer-tooth-wear-erosion-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 3. **The minimum-thickness threshold is unsettled between 0.5 and 1.0 mm and depends on substrate.** Sasse et al. (2015) found only the 0.7/1.0 mm group survived undamaged (100%), while thin 0.3/0.6 mm enamel-only fell to 12.5% survival — arguing a 0.7/1.0 mm minimum. Essam et al. (2023) validated 0.5 mm LD (fracture loads 962–1277 N with APF/HF/Monobond) as sufficient for molar forces, and Maldon
  - ▸ 출발(`occlusal-veneer-tooth-wear-erosion-overview`) 세줄: 교합면 비니어(Occlusal/Table-top Veneer) 7편 종합(in-vitro 4·SR 1·RCT 1·후향 case series 1): 초박형 세라믹(0.5–0.8 mm)은 생리적 구치 교합력(400–800 N)을 훨씬 상회하고(al-Akhali 2017: 120만 회·98N 저작 100% 생존), 재료 종류(세라믹 vs CAD/CAM 복합레진)는 임상 생존율에 무의미(세라믹 93–100% vs 복합레진 84–87%, 모두 NS). 최소두께 논쟁은 미해결: 0.7/1.0 mm만 안전하다

- `occlusal-veneer-tooth-wear-erosion-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: - **피로 vs 정적파절 vs 표면내구성 순위 상충**: maldonado(복합레진 피로 우위) vs al-akhali(세라믹 정적 우위) vs schlichting(복합레진 표면 열화). 어느 실패양식이 임상 지배인지 미해결.
  - ▸ 출발(`occlusal-veneer-tooth-wear-erosion-overview`) 세줄: 교합면 비니어(Occlusal/Table-top Veneer) 7편 종합(in-vitro 4·SR 1·RCT 1·후향 case series 1): 초박형 세라믹(0.5–0.8 mm)은 생리적 구치 교합력(400–800 N)을 훨씬 상회하고(al-Akhali 2017: 120만 회·98N 저작 100% 생존), 재료 종류(세라믹 vs CAD/CAM 복합레진)는 임상 생존율에 무의미(세라믹 93–100% vs 복합레진 84–87%, 모두 NS). 최소두께 논쟁은 미해결: 0.7/1.0 mm만 안전하다

- `endodontic-access-cavity-decision-tree` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - MIA(닌자 와동·트러스 와동)는 치관 구조 보존이 목표이나, 파절 저항성 향상 근거가 상충·불확실하고 임상 RCT 없음; 오히려 잔류 debris↑·근관구 탐지↓·천공 위험↑(Kapetanaki 2021, Dioguardi 2024) → 숙련 술자의 단순 단근관 케이스에서만 선택적.
  - ▸ 출발(`endodontic-access-cavity-decision-tree`) 세줄: 근관 접근와동(Access Cavity) 3전략 결정 트리: 전통 접근와동(Traditional Endodontic Cavity, TEC)은 정상 해부학에서 확립된 표준(직선 진입, 잔류 debris 최소); 최소침습 접근(Minimally Invasive Access, MIA — 닌자/트러스 와동)은 임상 무작위대조시험(Randomized Controlled Trial, RCT) 없음·잔류 debris↑·근관구 탐지↓·천공↑(Kapetanaki 2021·Dioguardi 2024) — 숙련 술자

- `endodontic-access-cavity-decision-tree` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: | **파절 저항성** | 표준 | 상충 근거 (일부 향상, 일부 무관) | 유지 |
  - ▸ 출발(`endodontic-access-cavity-decision-tree`) 세줄: 근관 접근와동(Access Cavity) 3전략 결정 트리: 전통 접근와동(Traditional Endodontic Cavity, TEC)은 정상 해부학에서 확립된 표준(직선 진입, 잔류 debris 최소); 최소침습 접근(Minimally Invasive Access, MIA — 닌자/트러스 와동)은 임상 무작위대조시험(Randomized Controlled Trial, RCT) 없음·잔류 debris↑·근관구 탐지↓·천공↑(Kapetanaki 2021·Dioguardi 2024) — 숙련 술자

- `endodontic-access-cavity-decision-tree` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: | 치아 파절 저항성 향상 | 상충 (일부 향상, 일부 무관) | 불확실 |
  - ▸ 출발(`endodontic-access-cavity-decision-tree`) 세줄: 근관 접근와동(Access Cavity) 3전략 결정 트리: 전통 접근와동(Traditional Endodontic Cavity, TEC)은 정상 해부학에서 확립된 표준(직선 진입, 잔류 debris 최소); 최소침습 접근(Minimally Invasive Access, MIA — 닌자/트러스 와동)은 임상 무작위대조시험(Randomized Controlled Trial, RCT) 없음·잔류 debris↑·근관구 탐지↓·천공↑(Kapetanaki 2021·Dioguardi 2024) — 숙련 술자

- `high-insertion-torque-primary-stability-crestal-bone-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **Lemos 2020 (체계적 문헌고찰·메타분석 (Systematic Review + Meta-Analysis, SR+MA), 6편/651개)의 무의(null)는 "효과 없음"이 아니라 "정보 없음"**: 생존 RR 0.51 (95% CI 0.06–4.06) — 신뢰구간이 두 자릿수를 가로지른다. MBL MD 0.15 mm (95% CI −0.14–0.44) — 상한 0.44 mm는 임상적으로 사소하지 않다. 게다가 **부호가 뒤집히는 집단들을 함께 pooling**했으므로 평균이 0에 가까운 것은 당연하다.
  - ▸ 출발(`high-insertion-torque-primary-stability-crestal-bone-overview`) 세줄: 고삽입토크(IT) 5편은 서로 어긋나 보이지만 — Trisi 2011(양 분할구강 조직학, 40개, 110 vs 10 Ncm), Marconcini 2018(RCT, 치유부위 단일 116개, 3년), Aldahlawi 2018(후향, NobelActive 113개), Faot 2019(전향, 위축 무치악 하악 세경 ø2.9mm 62개, 1년), Lemos 2020(SR+MA, 6편/651개) — IT를 *투여한 용량*이 아니라 *저항한 골을 읽은 값*으로 보면 정합적으로 풀린다. 해악은 실재하나 

- `high-insertion-torque-primary-stability-crestal-bone-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Harm is real but compartment- and population-bound: it appears at the **crestal cortex of the healed mandible over a long horizon** (Marconcini CSR 91.3% vs 98.2% at 3 y; Aldahlawi MBL 0.95±1.60 vs 0.18±0.68 mm, P<0.05, with mandible 2.12±1.99 vs maxilla 0.25±0.65 mm), whereas benefit appears across the **whole interface in soft/atrophic bone over a short horizon** (Trisi: no necrosis at 110 Ncm p
  - ▸ 출발(`high-insertion-torque-primary-stability-crestal-bone-overview`) 세줄: 고삽입토크(IT) 5편은 서로 어긋나 보이지만 — Trisi 2011(양 분할구강 조직학, 40개, 110 vs 10 Ncm), Marconcini 2018(RCT, 치유부위 단일 116개, 3년), Aldahlawi 2018(후향, NobelActive 113개), Faot 2019(전향, 위축 무치악 하악 세경 ø2.9mm 62개, 1년), Lemos 2020(SR+MA, 6편/651개) — IT를 *투여한 용량*이 아니라 *저항한 골을 읽은 값*으로 보면 정합적으로 풀린다. 해악은 실재하나 

- `high-insertion-torque-primary-stability-crestal-bone-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 해악은 실재하나 구획·집단에 묶여 있다: **치유된 하악 치조정 피질골에서 장기간에** 나타나고(Marconcini 3년 CSR 91.3% vs 98.2%; Aldahlawi MBL 0.95±1.60 vs 0.18±0.68 mm, P<0.05, 하악 2.12±1.99 vs 상악 0.25±0.65 mm), 이익은 **연질·위축골에서 전체 계면에 걸쳐 단기간에** 나타난다(Trisi 110 Ncm 괴사 없음 + 1–6주 전 시점 골형성 우위; Faot G4 ≥45 Ncm 생존율 95% 최고) — 그리고 Faot의 비단조 생존 사다리(75 → 81.3 → **64.3** → 95%)가 용량-반응 해석을 정면으로 반박한다.
  - ▸ 출발(`high-insertion-torque-primary-stability-crestal-bone-overview`) 세줄: 고삽입토크(IT) 5편은 서로 어긋나 보이지만 — Trisi 2011(양 분할구강 조직학, 40개, 110 vs 10 Ncm), Marconcini 2018(RCT, 치유부위 단일 116개, 3년), Aldahlawi 2018(후향, NobelActive 113개), Faot 2019(전향, 위축 무치악 하악 세경 ø2.9mm 62개, 1년), Lemos 2020(SR+MA, 6편/651개) — IT를 *투여한 용량*이 아니라 *저항한 골을 읽은 값*으로 보면 정합적으로 풀린다. 해악은 실재하나 

- `high-insertion-torque-primary-stability-crestal-bone-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This page synthesizes the five unsynthesized papers in `implants/isq/` that address one chairside question: **does driving an implant to high insertion torque damage the crest?** Read at face value they contradict each other flatly — an animal histology study finds 110 Ncm harmless and even osteogenic, a 3-year RCT finds ≥50 Ncm damaging, a retrospective cohort corroborates the damage at >55 Ncm, 
  - ▸ 출발(`high-insertion-torque-primary-stability-crestal-bone-overview`) 세줄: 고삽입토크(IT) 5편은 서로 어긋나 보이지만 — Trisi 2011(양 분할구강 조직학, 40개, 110 vs 10 Ncm), Marconcini 2018(RCT, 치유부위 단일 116개, 3년), Aldahlawi 2018(후향, NobelActive 113개), Faot 2019(전향, 위축 무치악 하악 세경 ø2.9mm 62개, 1년), Lemos 2020(SR+MA, 6편/651개) — IT를 *투여한 용량*이 아니라 *저항한 골을 읽은 값*으로 보면 정합적으로 풀린다. 해악은 실재하나 

- `high-insertion-torque-primary-stability-crestal-bone-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: They stop contradicting each other under one reframing: **insertion torque is not an independent variable the operator sets — it is a measurement of the bone that resisted the drill.** Once that is granted, the disagreement becomes a predictable consequence of three design differences: *which compartment* was measured, *over what horizon*, and *in what bone*. The papers are not measuring the same 
  - ▸ 출발(`high-insertion-torque-primary-stability-crestal-bone-overview`) 세줄: 고삽입토크(IT) 5편은 서로 어긋나 보이지만 — Trisi 2011(양 분할구강 조직학, 40개, 110 vs 10 Ncm), Marconcini 2018(RCT, 치유부위 단일 116개, 3년), Aldahlawi 2018(후향, NobelActive 113개), Faot 2019(전향, 위축 무치악 하악 세경 ø2.9mm 62개, 1년), Lemos 2020(SR+MA, 6편/651개) — IT를 *투여한 용량*이 아니라 *저항한 골을 읽은 값*으로 보면 정합적으로 풀린다. 해악은 실재하나 

- `high-insertion-torque-primary-stability-crestal-bone-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This is the load-bearing claim of the page, and it is what makes Faot and Aldahlawi stop contradicting each other.
  - ▸ 출발(`high-insertion-torque-primary-stability-crestal-bone-overview`) 세줄: 고삽입토크(IT) 5편은 서로 어긋나 보이지만 — Trisi 2011(양 분할구강 조직학, 40개, 110 vs 10 Ncm), Marconcini 2018(RCT, 치유부위 단일 116개, 3년), Aldahlawi 2018(후향, NobelActive 113개), Faot 2019(전향, 위축 무치악 하악 세경 ø2.9mm 62개, 1년), Lemos 2020(SR+MA, 6편/651개) — IT를 *투여한 용량*이 아니라 *저항한 골을 읽은 값*으로 보면 정합적으로 풀린다. 해악은 실재하나 

- `high-insertion-torque-primary-stability-crestal-bone-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: ### 2. Faot's G3 paradox refutes dose-response directly
  - ▸ 출발(`high-insertion-torque-primary-stability-crestal-bone-overview`) 세줄: 고삽입토크(IT) 5편은 서로 어긋나 보이지만 — Trisi 2011(양 분할구강 조직학, 40개, 110 vs 10 Ncm), Marconcini 2018(RCT, 치유부위 단일 116개, 3년), Aldahlawi 2018(후향, NobelActive 113개), Faot 2019(전향, 위축 무치악 하악 세경 ø2.9mm 62개, 1년), Lemos 2020(SR+MA, 6편/651개) — IT를 *투여한 용량*이 아니라 *저항한 골을 읽은 값*으로 보면 정합적으로 풀린다. 해악은 실재하나 

- `high-insertion-torque-primary-stability-crestal-bone-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Trisi refuted the **mechanism** Marconcini proposed (osseocompression → ischemia → necrosis → resorption): at 110 Ncm in dense sheep cortical bone there was no osteocyte lacunar emptying and no avascular necrotic zone. Marconcini's **outcome** (3-year crestal MBL and recession) is untouched by that. A finding of "no necrosis" does not license "no crestal bone loss," because necrosis was never the 
  - ▸ 출발(`high-insertion-torque-primary-stability-crestal-bone-overview`) 세줄: 고삽입토크(IT) 5편은 서로 어긋나 보이지만 — Trisi 2011(양 분할구강 조직학, 40개, 110 vs 10 Ncm), Marconcini 2018(RCT, 치유부위 단일 116개, 3년), Aldahlawi 2018(후향, NobelActive 113개), Faot 2019(전향, 위축 무치악 하악 세경 ø2.9mm 62개, 1년), Lemos 2020(SR+MA, 6편/651개) — IT를 *투여한 용량*이 아니라 *저항한 골을 읽은 값*으로 보면 정합적으로 풀린다. 해악은 실재하나 

- `high-insertion-torque-primary-stability-crestal-bone-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - [[implants/isq/trisi-2011-high-low-implant-torque-histology-sheep]] — the only study that assigned torque; refutes necrosis at 110 Ncm but measures the wrong compartment and window to see crestal harm
  - ▸ 출발(`high-insertion-torque-primary-stability-crestal-bone-overview`) 세줄: 고삽입토크(IT) 5편은 서로 어긋나 보이지만 — Trisi 2011(양 분할구강 조직학, 40개, 110 vs 10 Ncm), Marconcini 2018(RCT, 치유부위 단일 116개, 3년), Aldahlawi 2018(후향, NobelActive 113개), Faot 2019(전향, 위축 무치악 하악 세경 ø2.9mm 62개, 1년), Lemos 2020(SR+MA, 6편/651개) — IT를 *투여한 용량*이 아니라 *저항한 골을 읽은 값*으로 보면 정합적으로 풀린다. 해악은 실재하나 

- `high-insertion-torque-primary-stability-crestal-bone-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - [[implants/isq/faot-2019-insertion-torque-mandibular-overdenture]] — the sign-flip population: ≥45 Ncm best survival (95%); the G3 paradox refutes dose-response
  - ▸ 출발(`high-insertion-torque-primary-stability-crestal-bone-overview`) 세줄: 고삽입토크(IT) 5편은 서로 어긋나 보이지만 — Trisi 2011(양 분할구강 조직학, 40개, 110 vs 10 Ncm), Marconcini 2018(RCT, 치유부위 단일 116개, 3년), Aldahlawi 2018(후향, NobelActive 113개), Faot 2019(전향, 위축 무치악 하악 세경 ø2.9mm 62개, 1년), Lemos 2020(SR+MA, 6편/651개) — IT를 *투여한 용량*이 아니라 *저항한 골을 읽은 값*으로 보면 정합적으로 풀린다. 해악은 실재하나 

- `gp-cone-decontamination-chairside-protocol-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The two rates differ mainly because of **what was screened** (any aerobic/anaerobic growth vs a targeted *S. aureus* selective medium), not a real contradiction. The shared message: contamination is **prevalence-low but non-negligible**, and can include a nosocomially important, methicillin-resistant pathogen. Bracciale further showed contamination is **unrelated to brand** and instead concentrate
  - ▸ 출발(`gp-cone-decontamination-chairside-protocol-overview`) 세줄: 4편(체계적 문헌고찰 1 + in vitro 3) 종합: 거타퍼차(gutta-percha, GP) 콘은 열가소성으로 열멸균 불가능해 근관충전(obturation) 직전 화학 소독이 필수; 사용 중 콘 오염률은 MRSA/MSSA 표적 검사 1.9%, 전체 세균 배양 22.9%로 낮지만 MRSA를 포함하며, 오염은 브랜드가 아닌 취급·박스 체류시간 의존적(덜 쓰이는 큰 사이즈가 집중). 근거 전체가 **차아염소산나트륨(Sodium Hypochlorite, NaOCl) 3–5.25% 1분 침적** 으로

- `c-shaped-canal-anatomy-prevalence-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The individual population CBCT studies in this collection mostly **corroborate** the spine and, where they deviate, the deviation is explained by population, tooth choice, or counting method rather than by contradicting the underlying biology:
  - ▸ 출발(`c-shaped-canal-anatomy-prevalence-overview`) 세줄: C형 근관(C-shaped Canal) 12편 종합: 유병률은 3개 독립 구배 — 치아종류(하악 제2대구치 17.3% 최다 → 상악 제1대구치 0.8% 최소; Yousefi 2025 SR+MA, CBCT 101편), 아시아 우세 지역(한국 31–46%·중국 ≤41% vs 이스라엘 4.6%·이란 2%), 일관된 여성 우세(23.6% vs 16.7%; 이라크·멕시코 두 대륙 재현). 대구치 우세 형태 = Fan C2형(세미콜론); 소구치는 제1소구치(~10%)가 제2소구치(~1%)보다 약 10배 많음

- `c-shaped-canal-anatomy-prevalence-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Deviating high (counting method)**: the Indian overall 22% (Singh 2022) is inflated by **per-patient (not per-tooth)** reporting and Melton-based classification, a caveat that explains the apparent excess without contradicting the spine.
  - ▸ 출발(`c-shaped-canal-anatomy-prevalence-overview`) 세줄: C형 근관(C-shaped Canal) 12편 종합: 유병률은 3개 독립 구배 — 치아종류(하악 제2대구치 17.3% 최다 → 상악 제1대구치 0.8% 최소; Yousefi 2025 SR+MA, CBCT 101편), 아시아 우세 지역(한국 31–46%·중국 ≤41% vs 이스라엘 4.6%·이란 2%), 일관된 여성 우세(23.6% vs 16.7%; 이라크·멕시코 두 대륙 재현). 대구치 우세 형태 = Fan C2형(세미콜론); 소구치는 제1소구치(~10%)가 제2소구치(~1%)보다 약 10배 많음

- `c-shaped-canal-anatomy-prevalence-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **3. Anticipate asymmetry along the root and the heuristic of contralateral symmetry.** Shemesh 2017: 55% unilateral and config changes along the root in 63% — so the orifice does not predict the apex, and one side does not guarantee the other within a tooth. Yet at the *patient* level, Yousefi 2025's non-significant side difference and Abdalrahman's predominantly bilateral mandibular pattern supp
  - ▸ 출발(`c-shaped-canal-anatomy-prevalence-overview`) 세줄: C형 근관(C-shaped Canal) 12편 종합: 유병률은 3개 독립 구배 — 치아종류(하악 제2대구치 17.3% 최다 → 상악 제1대구치 0.8% 최소; Yousefi 2025 SR+MA, CBCT 101편), 아시아 우세 지역(한국 31–46%·중국 ≤41% vs 이스라엘 4.6%·이란 2%), 일관된 여성 우세(23.6% vs 16.7%; 이라크·멕시코 두 대륙 재현). 대구치 우세 형태 = Fan C2형(세미콜론); 소구치는 제1소구치(~10%)가 제2소구치(~1%)보다 약 10배 많음

- `bone-graft-material-selection-matrix-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **디지털 맞춤화는 유망하나 아직 예비적**: CAD/CAM 3D 프린팅(CBCT→STL→설계→출력) 워크플로우서 티타늄 메쉬 지배적(23편 중 16편), 맞춤형 골이식재/동종골 블록이 기존 블록 대비 골부피↑·흡수↓·수술시간↓ 보고하나 RCT 근거 소수·이질적(Elrefaei 2025); 3D 스캐폴드 설계는 다공성↔강도 상충 균형이 관건이고 혈관화·하중지지·제조표준화는 미해결(Sun 2025).
  - ▸ 출발(`bone-graft-material-selection-matrix-overview`) 세줄: bone-regeneration 미합성 17편(narrative review 6, SR/SR+MA 5, 동물 2, 전향 1, 후향 1, 사체 1, scoping review 1)을 골이식재 선택 매트릭스로 종합: 4대 생물학적 특성(골형성+골유도+골전도+골유착) 프레임에서 자가골만이 4특성을 모두 갖춘 유일 재료이자 gold standard이고, 시판 동종/이종/합성 대체재는 사실상 골전도성만 충족(Zhao 2021, DePace 2025, Bubalo 2026). Head-to-head 근거는 

- `implant-surface-comparison` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: **갱신 메모 (2026-06-26)**: 이번 갱신의 핵심은 **본 overview가 명시했던 두 가지 "부재" 갭이 충전**된 것 — (1) UV-PF 임상 SR+MA(Lang 2022), (2) SLA vs SLActive 직접 비교 RCT(Vílchez 2025). 임상 권장 자체는 불변(SLA 표준·친수성 D3/D4·UV-PF 위축골)이나, **근거의 질이 한 단계 상승**했고 두 신규 근거 모두 thesis를 반박이 아닌 보강 방향으로 정렬한다: UV-PF는 "절대 안정성"이 아니라 "안정성 도달 속도(OSI)"를 높이고(Lang), SLActive는 SLA 대비 절대 우위가 아니라 특정 시나리오 한정(Vílchez). 남은 갭은 SLA·SLActive·CA **3자 동시 비교** 다기관 RCT.
  - ▸ 출발(`implant-surface-comparison`) 세줄: 임플란트 표면처리 15편 + 3편 횡단인용 종합 매트릭스: SLA/SA = 임상 표준(8년 생존 94.8%, Kim 2020 n=96); 친수성(CA/SLActive) = D3/D4 골에서 stability dip 제거, 절대 ISQ 상승은 아님(CA 5.2년 97.3%, MBL 0.074 mm, Kim 2022 n=258); UV 광기능화(UV-PF) = 위축골·복잡증례 1순위(ISQ +21.9, 7년 100% 성공, Hirota 2020 전향적). 표면처리의 핵심 기전은 친수성이 아니라 탄화수

- `guided-robotic-accuracy-immediate-implant-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - 반대 방향 신호 2개(중요): ① freehand가 **생물학적 합병증이 더 적었다**(P=.04). ② **점막지지형(tissue-supported) 가이드**는 freehand보다 MBL이 오히려 나빴다(P=.03) — 가이드를 쓰더라도 지지형식(치아지지 vs 점막지지)과 판막 설계가 결과를 뒤집을 수 있다. 근거확실성은 GRADE very-low~moderate, 9편 중 6편이 비뚤림 고위험.
  - ▸ 출발(`guided-robotic-accuracy-immediate-implant-overview`) 세줄: 즉시식립 전용 NMA 2편 + 로봇/내비 임상시험 5편 종합: IIP에서 모든 guided(partial/full-static, dynamic, robotic CAIS)가 freehand 대비 각도·플랫폼·첨부 편차를 유의하게 줄이며, 발치와 빈 공간이 freehand 드릴을 사면 방향으로 밀기 때문에 IIP에서 guided 이득이 가장 크다. Nava 2026 NMA(18편, 780 IIP)에서 rCAIS > dCAIS > FG-sCAIS 순위이나, rCAIS vs dCAIS의 플랫폼·첨부 편차

- `guided-robotic-accuracy-immediate-implant-overview` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: **The accuracy–outcome dissociation.** Everything above is measured in millimeters and degrees of planned-vs-actual deviation, which is a *surrogate*. **Shirani 2026** (SR+MA restricted to 9 RCTs, 395 patients, 1,242 implants, search to Nov 2024) is the first synthesis in this wiki to test whether that surrogate cashes out clinically, and the headline answer is that it does not: overall marginal b
  - ▸ 출발(`guided-robotic-accuracy-immediate-implant-overview`) 세줄: 즉시식립 전용 NMA 2편 + 로봇/내비 임상시험 5편 종합: IIP에서 모든 guided(partial/full-static, dynamic, robotic CAIS)가 freehand 대비 각도·플랫폼·첨부 편차를 유의하게 줄이며, 발치와 빈 공간이 freehand 드릴을 사면 방향으로 밀기 때문에 IIP에서 guided 이득이 가장 크다. Nava 2026 NMA(18편, 780 IIP)에서 rCAIS > dCAIS > FG-sCAIS 순위이나, rCAIS vs dCAIS의 플랫폼·첨부 편차

- `guided-robotic-accuracy-immediate-implant-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Read Shirani's subgroups, though, and the dissociation resolves into agreement with this page's thesis rather than a contradiction of it. The places CAIS *does* win are precisely the deflection-prone ones: **fresh-socket placements** (MBL, P=.04), patient satisfaction (P=.03), and pink esthetic score (P=.009). That is the immediate-implant scenario. Meanwhile two findings cut the other way and des
  - ▸ 출발(`guided-robotic-accuracy-immediate-implant-overview`) 세줄: 즉시식립 전용 NMA 2편 + 로봇/내비 임상시험 5편 종합: IIP에서 모든 guided(partial/full-static, dynamic, robotic CAIS)가 freehand 대비 각도·플랫폼·첨부 편차를 유의하게 줄이며, 발치와 빈 공간이 freehand 드릴을 사면 방향으로 밀기 때문에 IIP에서 guided 이득이 가장 크다. Nava 2026 NMA(18편, 780 IIP)에서 rCAIS > dCAIS > FG-sCAIS 순위이나, rCAIS vs dCAIS의 플랫폼·첨부 편차

- `clinical-principles-100-master-distillation` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: — 한글: 당뇨 환자의 즉시식립 go/no-go는 당화혈색소 (HbA1c) 밴드 (<8% / 8–9% / ≥9%) 와 부위로 갈린다 — 유의한 DM 실패 신호는 상악이 지니고 하악은 아니다; 두 주요 SR+MA는 상악/장기 위험에서 진짜로 상충한다.
  - ▸ 출발(`clinical-principles-100-master-distillation`) 세줄: 위키 182개 overview를 체어사이드 임상원칙 100개로 압축한 최상위 종합 페이지 — 19개 도메인, 근거등급 표지(🟢🟡🟠⚪), 영어 규칙 + 완전한 한국어 번역 병기, 각 원칙은 근거 overview 링크로 연결. 대표 원칙: 부하 게이트 = 임플란트 안정성 지수(ISQ) ≥70 + 삽입토크(IT) ≥35 Ncm; 짧은/좁은 임플란트 생존 동등; 생활치수요법(VPT) 성공 >93%(바이오덴틴/MTA); 이갈이는 공통 상류 인자; 통증-only 내원자 ~1/3이나 개입 근거 빈약; "덜 하

- `mandibular-canal-nutrient-canal-cbct-anatomy-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **영양관–전신질환 연관은 미해결 논쟁 (cluster 내부 상충)**: 4편 중 3편은 양성, 1편은 null.
  - ▸ 출발(`mandibular-canal-nutrient-canal-cbct-anatomy-overview`) 세줄: 하악 후방부 신경·혈관 변이 방사선해부 논문 10편을 두 축으로 종합 — 이분/삼분하악관(BMC/TMC) 변이·영상 검출력, 그리고 영양관(NC) 유병률·전신질환 연관 논쟁. BMC는 CT 촬영 환자의 약 20.7%(Aung 2023 SR+MA, 40편; 반악 단위 14.3%, 남성·우측 우세)에서 나타나며 파노라마에서는 거의 검출되지 않아(MRI/CBCT 대비 0건 — Wamasing 2018, Kuribayashi 2010) CBCT가 하악 술전 계획의 표준; NC–전신질환 연관은 미해결 — 

- `mandibular-canal-nutrient-canal-cbct-anatomy-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 상충 근거 (null): Abdar-Esfahani 2013 (증례-대조 n=64) — NC가 HTN 37.5% vs 정상 53.1%로 오히려 반대 방향, 유의성 없음 (p=0.209); NC는 고혈압이 아니라 **연령·치조골소실**과 상관 (Kumar도 골소실 22.1%→75.8%로 동조). **메시지: NC는 단독 진단 표지자가 아니라, 있으면 미진단 DM/HTN 의심을 높이는 보조 단서**. 대부분 교란보정 없는 단일기관 χ² 비교라 인과 미확립.
  - ▸ 출발(`mandibular-canal-nutrient-canal-cbct-anatomy-overview`) 세줄: 하악 후방부 신경·혈관 변이 방사선해부 논문 10편을 두 축으로 종합 — 이분/삼분하악관(BMC/TMC) 변이·영상 검출력, 그리고 영양관(NC) 유병률·전신질환 연관 논쟁. BMC는 CT 촬영 환자의 약 20.7%(Aung 2023 SR+MA, 40편; 반악 단위 14.3%, 남성·우측 우세)에서 나타나며 파노라마에서는 거의 검출되지 않아(MRI/CBCT 대비 0건 — Wamasing 2018, Kuribayashi 2010) CBCT가 하악 술전 계획의 표준; NC–전신질환 연관은 미해결 — 

- `mandibular-canal-nutrient-canal-cbct-anatomy-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 2. **Do nutrient canals (NC) on routine periapical films signal systemic disease?** — a contested cross-sectional literature where the cluster itself contains a genuine contradiction.
  - ▸ 출발(`mandibular-canal-nutrient-canal-cbct-anatomy-overview`) 세줄: 하악 후방부 신경·혈관 변이 방사선해부 논문 10편을 두 축으로 종합 — 이분/삼분하악관(BMC/TMC) 변이·영상 검출력, 그리고 영양관(NC) 유병률·전신질환 연관 논쟁. BMC는 CT 촬영 환자의 약 20.7%(Aung 2023 SR+MA, 40편; 반악 단위 14.3%, 남성·우측 우세)에서 나타나며 파노라마에서는 거의 검출되지 않아(MRI/CBCT 대비 0건 — Wamasing 2018, Kuribayashi 2010) CBCT가 하악 술전 계획의 표준; NC–전신질환 연관은 미해결 — 

- `mandibular-canal-nutrient-canal-cbct-anatomy-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: ### The contradicting null (Abdar-Esfahani 2013)
  - ▸ 출발(`mandibular-canal-nutrient-canal-cbct-anatomy-overview`) 세줄: 하악 후방부 신경·혈관 변이 방사선해부 논문 10편을 두 축으로 종합 — 이분/삼분하악관(BMC/TMC) 변이·영상 검출력, 그리고 영양관(NC) 유병률·전신질환 연관 논쟁. BMC는 CT 촬영 환자의 약 20.7%(Aung 2023 SR+MA, 40편; 반악 단위 14.3%, 남성·우측 우세)에서 나타나며 파노라마에서는 거의 검출되지 않아(MRI/CBCT 대비 0건 — Wamasing 2018, Kuribayashi 2010) CBCT가 하악 술전 계획의 표준; NC–전신질환 연관은 미해결 — 

- `mandibular-canal-nutrient-canal-cbct-anatomy-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Case-control (n=64: 32 HTN vs 32 normotensive, Iran): NC incidence **37.5% in HTN vs 53.1% in normotensives — direction reversed and not significant (P=0.209)**; no association with HTN duration or control status. NC correlated instead with **older age** (47.1 vs 42.6 y, P=0.002). This page is explicitly flagged in the wiki as *contradicting* Kumar 2014.
  - ▸ 출발(`mandibular-canal-nutrient-canal-cbct-anatomy-overview`) 세줄: 하악 후방부 신경·혈관 변이 방사선해부 논문 10편을 두 축으로 종합 — 이분/삼분하악관(BMC/TMC) 변이·영상 검출력, 그리고 영양관(NC) 유병률·전신질환 연관 논쟁. BMC는 CT 촬영 환자의 약 20.7%(Aung 2023 SR+MA, 40편; 반악 단위 14.3%, 남성·우측 우세)에서 나타나며 파노라마에서는 거의 검출되지 않아(MRI/CBCT 대비 0건 — Wamasing 2018, Kuribayashi 2010) CBCT가 하악 술전 계획의 표준; NC–전신질환 연관은 미해결 — 

- `mandibular-canal-nutrient-canal-cbct-anatomy-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[radiology/abdar-esfahani-2013-mandibular-anterior-nutrient-canals]] — contradicting null (P=0.209); NC tracks age
  - ▸ 출발(`mandibular-canal-nutrient-canal-cbct-anatomy-overview`) 세줄: 하악 후방부 신경·혈관 변이 방사선해부 논문 10편을 두 축으로 종합 — 이분/삼분하악관(BMC/TMC) 변이·영상 검출력, 그리고 영양관(NC) 유병률·전신질환 연관 논쟁. BMC는 CT 촬영 환자의 약 20.7%(Aung 2023 SR+MA, 40편; 반악 단위 14.3%, 남성·우측 우세)에서 나타나며 파노라마에서는 거의 검출되지 않아(MRI/CBCT 대비 0건 — Wamasing 2018, Kuribayashi 2010) CBCT가 하악 술전 계획의 표준; NC–전신질환 연관은 미해결 — 

- `complaint-management-pipeline-classification-expectation-response-education` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: | Gillespie 2025 | Respond | Mixed methods | online responses | 6 defensive tactics from contradictory demands | cross-sectional |
  - ▸ 출발(`complaint-management-pipeline-classification-expectation-response-education`) 세줄: 20편 종합: 환자 민원을 분류(Reader 2014 SR 88,069건 — 임상 33.7%·관리 35.1%·관계 29.1%; HCAT 7범주) → 기대 파악(민원인은 재발방지·정직한 설명 우선, 금전 7%뿐, Friele 2006) → 대응(방어성은 구조적 문제, "fauxpology"·주관화가 실패 패턴, Gillespie 2025) → 교육(CODE 모델: 운영·대인 훈련 병행, Elias 2025)의 4단계 파이프라인. 치과 적용층: 치과의사 민원율 최고(42.7/1,000/년, Thoma

- `maxillary-sinus-incidental-cbct-pathology-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Reading the two numbers together requires care.** Salari used a higher mucosal-thickening threshold (>5mm) than Küçükkurt (>3mm), yet still landed a comparable — even slightly lower — overall prevalence. This is consistent, not contradictory: a stricter threshold under-detects thickening, so Salari's 63.5% likely undercounts mild pathology relative to a >2-3mm consensus standard. The take-away i
  - ▸ 출발(`maxillary-sinus-incidental-cbct-pathology-overview`) 세줄: 임플란트·상악동거상술 전 CBCT 우연 발견 상악동 병변 4편 종합(후향 CBCT 유병률 연구 2편 n=140/1,000 + 상악동석 증례 2편): 전체 유병률 63.5–68%(기준값 의존), 점막비후(Mucosal Thickening, MT)가 가장 흔함(31.4–47%), 점액저류낭종 17.1%가 두 번째, 상악동석(Antrolith)은 드물지만(0.15–3.2%) 무증상 소형(관찰 가능)에서 증상성 대형(재발성 부비동염·구강상악동루, 수술 필요)까지 스펙트럼 넓음. 점막비후는 치주골소실·치근

- `digital-complete-denture-cost-consensus-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This meta-analysis contradicts the conclusion of Jafarpour 2024 (an earlier SR+MA that reported CAD/CAM RCDs as significantly cheaper). Muehlemann et al. attribute the discrepancy to Jafarpour's cost-analysis-only methodology — which did not adjust for patient outcomes or apply rigorous currency harmonization. Once those adjustments are applied, the cost difference disappears.
  - ▸ 출발(`digital-complete-denture-cost-consensus-overview`) 세줄: 2025년 두 편의 연구(27인 합의문 Feng + SR+MA 5편 Muehlemann, n=184)가 동일한 결론으로 수렴: 디지털 총의치는 임상적으로 중요한 결과(비용·만족도·OHRQoL·내원횟수)에서 전통 의치와 동등하되, 임상시간은 58–233분 절감된다. 4개 비용 지표(기공비·임상비·총비용·내원횟수) 모두 통계적으로 유의한 차이 없고, 비용 변동의 주결정 인자는 워크플로우 종류가 아닌 술자 숙련도(p<0.0001)이며, 환자 만족도·OHRQoL도 디지털 대 전통 간 유의차 없다. 남은 

- `digital-complete-denture-cost-consensus-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[complete-denture/jafarpour-2024-cadcam-versus-traditional-complete-dentures]] — prior SR+MA reporting CAD/CAM as significantly cheaper; contradicted by Muehlemann 2025's rigorous harmonization
  - ▸ 출발(`digital-complete-denture-cost-consensus-overview`) 세줄: 2025년 두 편의 연구(27인 합의문 Feng + SR+MA 5편 Muehlemann, n=184)가 동일한 결론으로 수렴: 디지털 총의치는 임상적으로 중요한 결과(비용·만족도·OHRQoL·내원횟수)에서 전통 의치와 동등하되, 임상시간은 58–233분 절감된다. 4개 비용 지표(기공비·임상비·총비용·내원횟수) 모두 통계적으로 유의한 차이 없고, 비용 변동의 주결정 인자는 워크플로우 종류가 아닌 술자 숙련도(p<0.0001)이며, 환자 만족도·OHRQoL도 디지털 대 전통 간 유의차 없다. 남은 

- `full-arch-fixed-four-vs-six-implants-overview` [overviews] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: > - 무치악 고정성 풀아치 수복에서 **임플란트 4개 vs 6개** 결정을 임상 근거(생존·변연골·비용·합병증)와 생체역학 근거(유한요소분석, FEA)의 *상반된* 두 축으로 종합한 5편 페이지. 핵심 긴장: **임상 성적은 동등, 생체역학은 6개 우위** — 이 괴리가 결정 규칙을 만든다.
  - ▸ 출발(`full-arch-fixed-four-vs-six-implants-overview`) 세줄: 무치악 고정성 풀아치에서 임플란트 4개 vs 6개 결정을 임상 성적 축(RCT 2편+대규모 후향 1편)과 생체역학 축(FEA 2편)의 상반된 두 관점으로 종합한 5편. 임상적으로 4개는 생존·변연골소실에서 6개에 비열등(Toia 3년·5년 RCT: 생존 양군 ~100%, MBL 유의차 없음; Caramés 2025 후향 943명/5,989 임플란트: 5년 생존 98.4% vs 98.7%, p=0.343, 개수가 아니라 악궁·연령이 실패 예측), 4개는 저비용·무증대이나 기술적 합병증↑; 생체역학적

- `full-arch-fixed-four-vs-six-implants-overview` [overviews] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: 무치악 고정성 풀아치에서 임플란트 4개 vs 6개 결정을 임상 성적 축(RCT 2편+대규모 후향 1편)과 생체역학 축(FEA 2편)의 상반된 두 관점으로 종합한 5편.
  - ▸ 출발(`full-arch-fixed-four-vs-six-implants-overview`) 세줄: 무치악 고정성 풀아치에서 임플란트 4개 vs 6개 결정을 임상 성적 축(RCT 2편+대규모 후향 1편)과 생체역학 축(FEA 2편)의 상반된 두 관점으로 종합한 5편. 임상적으로 4개는 생존·변연골소실에서 6개에 비열등(Toia 3년·5년 RCT: 생존 양군 ~100%, MBL 유의차 없음; Caramés 2025 후향 943명/5,989 임플란트: 5년 생존 98.4% vs 98.7%, p=0.343, 개수가 아니라 악궁·연령이 실패 예측), 4개는 저비용·무증대이나 기술적 합병증↑; 생체역학적

- `full-arch-fixed-four-vs-six-implants-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The axes are not contradictory once framed correctly: **equivalent clinical survival means four implants stay within physiological bone-loading limits in standard cases.** The FEA stress difference is a **safety-margin difference, not a failure-rate difference** — six implants "waste" capacity that a standard case never needs, but that a high-load case does.
  - ▸ 출발(`full-arch-fixed-four-vs-six-implants-overview`) 세줄: 무치악 고정성 풀아치에서 임플란트 4개 vs 6개 결정을 임상 성적 축(RCT 2편+대규모 후향 1편)과 생체역학 축(FEA 2편)의 상반된 두 관점으로 종합한 5편. 임상적으로 4개는 생존·변연골소실에서 6개에 비열등(Toia 3년·5년 RCT: 생존 양군 ~100%, MBL 유의차 없음; Caramés 2025 후향 943명/5,989 임플란트: 5년 생존 98.4% vs 98.7%, p=0.343, 개수가 아니라 악궁·연령이 실패 예측), 4개는 저비용·무증대이나 기술적 합병증↑; 생체역학적

- `oral-mucositis-cancer-therapy-overview` [overviews] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: > - **저출력레이저(Low-Level Laser Therapy, LLLT)는 소아 풀링에서 효과 없음**(RR=0.99) — 성인/타 점막질환 데이터와 대비되는 핵심 반전. 단 통증(pain) 완화에서는 보조적 언급.
  - ▸ 출발(`oral-mucositis-cancer-therapy-overview`) 세줄: 항암치료 유발 구강점막염(Oral Mucositis, OM) 3편 종합(소아 SR+MA 1편 + 소아 SR 1편 + 성인 두경부암 방사선 RCT 1편 n=69): 소아 항암 OM 발생률 최대 91.5%; 메타분석으로 지지되는 유일 약제는 국소 꿀(중증 소아 OM 입원 −4.33일, p=0.002; Andriakopoulou 2024), LLLT는 소아 풀링서 무효(RR=0.99); 칼슘인산염은 3편 모두 무효. 약제는 목표 결과지표별 선택: 발생률→클로르헥시딘, 기간→꿀, 통증→올리브유(Bragu

- `oral-mucositis-cancer-therapy-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **팔리퍼민(palifermin, 재조합 KGF):** 발생률·중증도·지속기간 모두 감소(급성백혈병) — 그러나 **안전성 보고가 상충**, 무비판적 적용 금지.
  - ▸ 출발(`oral-mucositis-cancer-therapy-overview`) 세줄: 항암치료 유발 구강점막염(Oral Mucositis, OM) 3편 종합(소아 SR+MA 1편 + 소아 SR 1편 + 성인 두경부암 방사선 RCT 1편 n=69): 소아 항암 OM 발생률 최대 91.5%; 메타분석으로 지지되는 유일 약제는 국소 꿀(중증 소아 OM 입원 −4.33일, p=0.002; Andriakopoulou 2024), LLLT는 소아 풀링서 무효(RR=0.99); 칼슘인산염은 3편 모두 무효. 약제는 목표 결과지표별 선택: 발생률→클로르헥시딘, 기간→꿀, 통증→올리브유(Bragu

- `oral-mucositis-cancer-therapy-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 약제는 목표 결과지표별 선택: 발생률→클로르헥시딘, 기간→꿀, 통증→올리브유(Braguès 2024); 팔리퍼민(Palifermin, KGF)은 효과 있으나 안전성 상충 → 무비판적 적용 금지.
  - ▸ 출발(`oral-mucositis-cancer-therapy-overview`) 세줄: 항암치료 유발 구강점막염(Oral Mucositis, OM) 3편 종합(소아 SR+MA 1편 + 소아 SR 1편 + 성인 두경부암 방사선 RCT 1편 n=69): 소아 항암 OM 발생률 최대 91.5%; 메타분석으로 지지되는 유일 약제는 국소 꿀(중증 소아 OM 입원 −4.33일, p=0.002; Andriakopoulou 2024), LLLT는 소아 풀링서 무효(RR=0.99); 칼슘인산염은 3편 모두 무효. 약제는 목표 결과지표별 선택: 발생률→클로르헥시딘, 기간→꿀, 통증→올리브유(Bragu

- `gbr-barrier-membrane-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Scope limitation of Darby 2024**: a 5×3 mm anterior maxillary dehiscence defect is a self-contained, small-volume defect. The membrane-positive findings in Friedmann 2022 (more new bone with RCLC vs NCM) pertain to larger chronic horizontal defects — a different geometry and healing challenge. These findings are complementary, not contradictory: in small contained dehiscence defects, membrane se
  - ▸ 출발(`gbr-barrier-membrane-overview`) 세줄: 12편(서술적 고찰 3·동물 5·임상 전향 1·SR 1·벤치 1) 종합: 골유도재생술(Guided Bone Regeneration, GBR) 차폐막은 흡수성/비흡수성이라는 단일 상류 변수로 분기하며, 가교화(crosslinking) 전략이 콜라겐막의 16–24주 차단기능 충족 여부를 결정한다(천연 콜라겐은 2–4주에 흡수되어 부족, EDC·리보스 가교화가 해법). 공간 유지는 모든 경우에 이식재가 필수(막 단독군은 2주에 함몰; Park 2015), 결손 유형이 막 선택을 결정하며(수평 → 가교화

- `peri-implantitis-management-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: > - **유병률 섹션 추가 — Sbricoli 2026 (횡단연구, n=70/임플란트 227개)**: 제2형 당뇨 vs 비당뇨 간 임플란트주위질환·점막염·주위염 유의차 없음(모두 p>0.4) — 당뇨를 독립 위험인자로 보는 통념에 반하나(contradicts), 검정력 부족 + 양군 모두 높은 치주염 과거력(83–94%)이 교란요인. 메시지는 "당뇨 진단"보다 "대사조절의 질"로 재구성.
  - ▸ 출발(`peri-implantitis-management-overview`) 세줄: 임플란트주위염(Peri-implantitis) 23+편 종합 — 병인/면역병리(Smeets 2014·Galarraga-Vinueza 2020·Cafferata 2025·Kotsakis 2025 티타늄 exposome)·역학(Diaz 2022 SR+MA: 환자 단위 19.5%)·비외과/점막염 관리·외과 제염·GBR 재건·보철 변연골소실(MBL) 레버·수술위치/보철/해부 위험축. 단일 표면제염 프로토콜 우위 없음(Baima 2022, 16 RCT); 보철 디자인(플랫폼스위칭·원추형 연결·어버트먼트 높

- `peri-implantitis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **신규 — 수술·위치 위험축 (surgical/positional) · Monje 2025 (AO/AAP SR 34편, Wang 2025 컨센서스 companion)**: 임플란트 **오식립(malposition, 3D 위치 오류)이 주위염 최강 수술 위험인자**(주위염에만, 점막염엔 무관; OR 2.6–48.2, 최고 Canullo OR=48.2). 임플란트 간 거리 <3mm(OR 2.98–8.6), 치조정하 깊이 ≥6mm(OR 8.5), **수복물변연–치조정 거리 <1.5mm(OR 2.29)** — Basak 2024의 RM-AC 3.42배를 동일 임계값에서 독립 보강. **임플란트 디자인·표면·시스템은 일관된 우열 없음** → "특정 브랜드가 주위염에 강하다"는 마케팅 주장 반박. 메시지: 주
  - ▸ 출발(`peri-implantitis-management-overview`) 세줄: 임플란트주위염(Peri-implantitis) 23+편 종합 — 병인/면역병리(Smeets 2014·Galarraga-Vinueza 2020·Cafferata 2025·Kotsakis 2025 티타늄 exposome)·역학(Diaz 2022 SR+MA: 환자 단위 19.5%)·비외과/점막염 관리·외과 제염·GBR 재건·보철 변연골소실(MBL) 레버·수술위치/보철/해부 위험축. 단일 표면제염 프로토콜 우위 없음(Baima 2022, 16 RCT); 보철 디자인(플랫폼스위칭·원추형 연결·어버트먼트 높

- `peri-implantitis-management-overview` [overviews] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: - **Contradicts** the conventional framing of diabetes as a major independent peri-implantitis risk factor — but the study was **underpowered** (observed ~50% peri-implantitis prevalence in both arms vs an 8% planning assumption) and a very high history-of-periodontitis rate in both groups (83% diabetic, 94% non-DM) likely confounded/masked any T2DM-specific effect
  - ▸ 출발(`peri-implantitis-management-overview`) 세줄: 임플란트주위염(Peri-implantitis) 23+편 종합 — 병인/면역병리(Smeets 2014·Galarraga-Vinueza 2020·Cafferata 2025·Kotsakis 2025 티타늄 exposome)·역학(Diaz 2022 SR+MA: 환자 단위 19.5%)·비외과/점막염 관리·외과 제염·GBR 재건·보철 변연골소실(MBL) 레버·수술위치/보철/해부 위험축. 단일 표면제염 프로토콜 우위 없음(Baima 2022, 16 RCT); 보철 디자인(플랫폼스위칭·원추형 연결·어버트먼트 높

- `peri-implantitis-management-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Reframes the clinical message toward **quality of metabolic control** rather than the T2DM diagnosis itself; plaque index, longer loading time, and cement retention (vs screw) were the operative correlates of disease in this cohort [cross-sectional, underpowered — treat as hypothesis-generating, not a refutation of diabetes risk]
  - ▸ 출발(`peri-implantitis-management-overview`) 세줄: 임플란트주위염(Peri-implantitis) 23+편 종합 — 병인/면역병리(Smeets 2014·Galarraga-Vinueza 2020·Cafferata 2025·Kotsakis 2025 티타늄 exposome)·역학(Diaz 2022 SR+MA: 환자 단위 19.5%)·비외과/점막염 관리·외과 제염·GBR 재건·보철 변연골소실(MBL) 레버·수술위치/보철/해부 위험축. 단일 표면제염 프로토콜 우위 없음(Baima 2022, 16 RCT); 보철 디자인(플랫폼스위칭·원추형 연결·어버트먼트 높

- `peri-implantitis-management-overview` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: - **Convergence with the mucositis evidence:** the "best" PM adjunct being top-ranked-but-non-significant is the same signal Mauriello 2026 and Brunello 2026 report — mechanical debridement is the backbone and adjuncts add little *consistent, significant* benefit. Bai adds the quantitative ranking layer without overturning that bottom line. [sr+ma / network MA, 33 RCTs — 10 low-RoB, low publicatio
  - ▸ 출발(`peri-implantitis-management-overview`) 세줄: 임플란트주위염(Peri-implantitis) 23+편 종합 — 병인/면역병리(Smeets 2014·Galarraga-Vinueza 2020·Cafferata 2025·Kotsakis 2025 티타늄 exposome)·역학(Diaz 2022 SR+MA: 환자 단위 19.5%)·비외과/점막염 관리·외과 제염·GBR 재건·보철 변연골소실(MBL) 레버·수술위치/보철/해부 위험축. 단일 표면제염 프로토콜 우위 없음(Baima 2022, 16 RCT); 보철 디자인(플랫폼스위칭·원추형 연결·어버트먼트 높

- `peri-implantitis-management-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Implant macro-/micro-design, surface, and brand show no consistent superiority** for peri-implantitis resistance across comparative RCTs/cohorts (a few outlier signals: anodized/fluoride surface OR ~3.6–3.8 vs SLA; brand OR 3.5–3.7 in Derks 2016 — but not reproduced as a class effect). Clinically this **contradicts single-brand/single-surface marketing claims** and relocates the prevention lev
  - ▸ 출발(`peri-implantitis-management-overview`) 세줄: 임플란트주위염(Peri-implantitis) 23+편 종합 — 병인/면역병리(Smeets 2014·Galarraga-Vinueza 2020·Cafferata 2025·Kotsakis 2025 티타늄 exposome)·역학(Diaz 2022 SR+MA: 환자 단위 19.5%)·비외과/점막염 관리·외과 제염·GBR 재건·보철 변연골소실(MBL) 레버·수술위치/보철/해부 위험축. 단일 표면제염 프로토콜 우위 없음(Baima 2022, 16 RCT); 보철 디자인(플랫폼스위칭·원추형 연결·어버트먼트 높

- `direct-resin-restoration-adhesion-placement-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Bulk-fill and incremental placement are clinically equivalent through ≥24 months (9-RCT MA RR 0.82 NS; 12-RCT NMA no significant difference; umbrella review; Zailai 2025, Chaple-Gil 2026), and the claim "low-shrinkage = clinically superior" is refuted by 21-RCT MA (Kruly 2018 — only 12-month marginal adaptation favors conventional methacrylate; all other outcomes equal).
  - ▸ 출발(`direct-resin-restoration-adhesion-placement-overview`) 세줄: Cochrane SR·우산형 리뷰·SR+MA/NMA·대규모 RCT를 아우르는 직접 복합레진 수복의 두 축 종합; 법랑질 가장자리가 있으면 선택적 법랑질 산부식 또는 3-step EAR이 일관 우세(Hong 2021 SR+MA; Oza 2022 RCT: 유니버설 SE 단독은 NCCL 24개월에서 임상 부적합). 벌크필과 적층충전은 ≥24개월 임상 동등(9-RCT MA RR 0.82 NS·12-RCT NMA 차이 없음; Zailai 2025·Chaple-Gil 2026); "저수축=임상 우월" 명제는

- `direct-resin-restoration-adhesion-placement-overview` [overviews] (SOFT→tay-2003-dentin-adhesives-hydrophilic, 'disagree' · 불일치)
  - **근거 문장**: **Reading the disagreement**: Hong 2021 (general restorations) and Assis 2023 (NCCL) favor E&R; Doshi 2023 (NCCL, more recent search) finds no difference. The Oza 2022 RCT — which Doshi/Assis postdate — is the cleanest signal: **universal adhesive in pure SE mode failed at 24 months on cervical lesions**, while selective-enamel-etch (SLE) and full E&R modes did not. The mechanism is the establishe
  - ▸ 출발(`direct-resin-restoration-adhesion-placement-overview`) 세줄: Cochrane SR·우산형 리뷰·SR+MA/NMA·대규모 RCT를 아우르는 직접 복합레진 수복의 두 축 종합; 법랑질 가장자리가 있으면 선택적 법랑질 산부식 또는 3-step EAR이 일관 우세(Hong 2021 SR+MA; Oza 2022 RCT: 유니버설 SE 단독은 NCCL 24개월에서 임상 부적합). 벌크필과 적층충전은 ≥24개월 임상 동등(9-RCT MA RR 0.82 NS·12-RCT NMA 차이 없음; Zailai 2025·Chaple-Gil 2026); "저수축=임상 우월" 명제는
  - ▸ 대상(`tay-2003-dentin-adhesives-hydrophilic`) 세줄: 기초 서술 리뷰 (Tay & Pashley, J Can Dent Assoc 2003): 3단계 전부식 → 1단계 자가산부식으로 이어지는 접착제 단순화 각 단계가 친수성과 수분 투과성을 높이는 과정을 추적하며, 수포 형성, 술후 과민증, 혼성층 열화, 이중경화 부적합을 다룸. 단순화할수록 친수성 증가; 1단계 자가산부식이 가장 친수적이고 내구성 최저; 중합된 접착제막을 통해 상아질 수분이 투과해 수포(water blister)를 형성하고 혼성층 가수분해 열화를 촉진; 간편화된 산성 접착제는 이중경화

- `direct-resin-restoration-adhesion-placement-overview` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: ### Critical / counterpoint
  - ▸ 출발(`direct-resin-restoration-adhesion-placement-overview`) 세줄: Cochrane SR·우산형 리뷰·SR+MA/NMA·대규모 RCT를 아우르는 직접 복합레진 수복의 두 축 종합; 법랑질 가장자리가 있으면 선택적 법랑질 산부식 또는 3-step EAR이 일관 우세(Hong 2021 SR+MA; Oza 2022 RCT: 유니버설 SE 단독은 NCCL 24개월에서 임상 부적합). 벌크필과 적층충전은 ≥24개월 임상 동등(9-RCT MA RR 0.82 NS·12-RCT NMA 차이 없음; Zailai 2025·Chaple-Gil 2026); "저수축=임상 우월" 명제는

- `immediate-implant-evidence-survival-timing-infected-loading-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The Mello↔García-Sánchez conflict is not a contradiction about biology — it is a difference in inclusion criteria. Restrict to RCTs and the gap vanishes; add weaker observational cohorts and a ~3-point penalty appears. Practically: immediate survival is high, the immediate-vs-delayed decision should be driven by site/soft-tissue and complication tolerance, not a survival cliff.
  - ▸ 출발(`immediate-implant-evidence-survival-timing-infected-loading-overview`) 세줄: 즉시식립(Type 1)의 4개 결정축(생존·타이밍·감염소켓·부하/보철)을 8편으로 종합한 허브: 절대 생존은 높으나(Lang 2012 연간실패 0.82%, 2년 98.4%) 즉시 vs 지연 비교는 설계의존적 — Mello 2017(관찰포함 30편)은 즉시 95.21% vs 지연 98.38% 유의 열세(p=.001), García-Sánchez 2022(RCT 6편)는 생존 무차이 + 즉시가 1년 변연골·심미 우세. 타이밍 프로토콜 우열 없음(Pommer 2021 전 조합 NS), MBL은 조기집중

- `periodontal-adjunctive-therapy-probiotics-pdt-overview` [periodontics] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: This **updates and partially overturns Van der Sluijs 2016**, which had reported a slight PVP-I CAL gain not confirmed here. da Silveira frames the negative finding under **antimicrobial-stewardship**: with no demonstrated benefit and given CHX tolerance/resistance concerns, routine adjunctive subgingival irrigation is not supported. The MD of ~0.01–0.09 mm sits *below* even the ~0.3 mm John 2017 
  - ▸ 출발(`periodontal-adjunctive-therapy-probiotics-pdt-overview`) 세줄: 8편 종합(NMA 1·RCT 4·SR+MA 1·RCT 1) — 2017 NMA 벤치마크(John 2017, 61편, 9종 보조요법): 모든 보조요법의 추가 임상부착수준(Clinical Attachment Level, CAL) 이득 ~0.3 mm, 우월한 단일 보조요법 없음. 2026 프로바이오틱스 RCT(Lactobacillus+Enterococcus, n=80; OraCMU, n=80)는 탐침시출혈(Bleeding on Probing, BoP)·심부포켓 수를 유의 감소(p=0.03·p=0.01)

- `periodontal-adjunctive-therapy-probiotics-pdt-overview` [periodontics] (HIGH-no-target, 'Counterpoint' · 반대 논점)
  - **근거 문장**: ### "Clean and Seal" (AA-NaOCl + Cross-linked HA) — the Positive Counterpoint (Jungbauer 2026)
  - ▸ 출발(`periodontal-adjunctive-therapy-probiotics-pdt-overview`) 세줄: 8편 종합(NMA 1·RCT 4·SR+MA 1·RCT 1) — 2017 NMA 벤치마크(John 2017, 61편, 9종 보조요법): 모든 보조요법의 추가 임상부착수준(Clinical Attachment Level, CAL) 이득 ~0.3 mm, 우월한 단일 보조요법 없음. 2026 프로바이오틱스 RCT(Lactobacillus+Enterococcus, n=80; OraCMU, n=80)는 탐침시출혈(Bleeding on Probing, BoP)·심부포켓 수를 유의 감소(p=0.03·p=0.01)

- `periodontal-adjunctive-therapy-probiotics-pdt-overview` [periodontics] (HIGH-far→jungbauer-2026-naocl-hyaluronic-acid-subgingival-reinstrumentation-rct, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[periodontics/jungbauer-2026-naocl-hyaluronic-acid-subgingival-reinstrumentation-rct]] — "clean and seal" (AA-NaOCl + cross-linked HA) adjunct to SRI in maintenance; positive ~0.5 mm PD / 0.57 mm CAL gain, doubled pocket closure — delivery-mode counterpoint to da Silveira's null irrigation
  - ▸ 출발(`periodontal-adjunctive-therapy-probiotics-pdt-overview`) 세줄: 8편 종합(NMA 1·RCT 4·SR+MA 1·RCT 1) — 2017 NMA 벤치마크(John 2017, 61편, 9종 보조요법): 모든 보조요법의 추가 임상부착수준(Clinical Attachment Level, CAL) 이득 ~0.3 mm, 우월한 단일 보조요법 없음. 2026 프로바이오틱스 RCT(Lactobacillus+Enterococcus, n=80; OraCMU, n=80)는 탐침시출혈(Bleeding on Probing, BoP)·심부포켓 수를 유의 감소(p=0.03·p=0.01)

- `root-analogue-implants-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: > - **자연치근 보존이 RAI를 이긴다 — Bose 2023 (RAI 20 vs 강제교정정출 FOE 20)**: 양군 생존 100%이나 **FOE가 MBL(p<0.01)·인접치간 유두/접촉·점막질에서 RAI보다 유의하게 우수**; 복합 FIPS FOE ~9.0 vs RAI ~7.5. 함의: 가능하면 **강제교정정출로 자연치근/치조골을 보존**하는 편이 즉시 RAI보다 조직 보존적 — RAI는 대안이지 우월책이 아님. (contradicts RAI 우위 가정)
  - ▸ 출발(`root-analogue-implants-overview`) 세줄: 발치된 치아 뿌리 형태를 복제해 즉시식립하는 근관유사 임플란트(RAI, CAD-CAM/적층제조) 5편을 근거·재료·적응증으로 종합. 최고 근거(Alqutaibi 2026 SR, 28편/432 RAI)는 생존 71–100%이나 재료 의존적 예측성(티타늄/하이브리드 최상, MBL 0.7 mm까지; 지르코니아 33.3–100%로 파절위험↑)을 보이고 근거 기반은 단일증례·추적 ≤2년·RCT 1편에 그침; 최대 시리즈(Bose 2020, 107 RAI)는 생존 94.4%이나 복합성공률 64.5%(변연적합

- `suture-wound-closure-decision-ladder` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: - [[suture-wound-closure/kumar-2022-suture-versus-sutureless-third-molar-impactions]] — sutureless 초기 morbidity 우월 (takadoum과 부분 상충)
  - ▸ 출발(`suture-wound-closure-decision-ladder`) 세줄: 15편 종합(RCT 7, SR 1, 전향적 2, 증례 1, in-vitro 4) — 봉합·창상폐쇄 결정은 단일 상류 변수인 창상 장력(wound tension)에 의해 정반대 최적화 목표를 가진 두 맥락으로 분기한다. 저장력 발치와: 봉합 유무는 결과에 무관 — 무봉합(sutureless)은 안전하며 초기 이환도 동등 이상(Takadoum 2022 완전 동등, Kumar/Sen trismus·부종 감소); 흡연자는 폐쇄 방식과 무관하게 합병증 3.65배↑; 봉합 시 패턴 선택(sling > sin

- `healing-abutment-reuse-single-use-controversy-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: > - **축 간 충돌(contradiction)**: Kyaw(청결도 축, RCT) "엄격 프로토콜이면 다회 재사용 OK" ↔ Abreu(생물학 축, in vitro) "깨끗해도 염증 유발 → 재사용 불가". 둘 다 옳을 수 있다 — 서로 **다른 종말점(endpoint)** 을 측정하기 때문. 이 충돌이 논쟁의 미해결 핵심.
  - ▸ 출발(`healing-abutment-reuse-single-use-controversy-overview`) 세줄: 힐링 어버트먼트 재사용 논쟁을 청결도 축(미사용 표면 복원 가능?)과 생물학적 반응 축(깨끗해도 염증 안 내나?)으로 분리한 8편 종합: 2편 SR은 어떤 통상 프로토콜도 100% 미사용 표면을 복원 못 하고, 멸균 후 잔류 단백질이 나사산·드라이버홀 요철부에 집중됨을 일치시킨다. 1% NaOCl + 초음파(바이오필름 99.7% 제거, Çetinsoy 2026), air polishing(Naghsh 2024), 화학+전기화학 병용(Kyaw 2023 RCT)은 청결도 축에서 거의 미사용 표면에 근

- `healing-abutment-reuse-single-use-controversy-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **The core unresolved contradiction:** Kyaw (cleanliness axis, RCT) concludes reuse is acceptable with a rigorous protocol; Abreu (biologic axis, in vitro) concludes reuse is not acceptable because cleanliness ≠ inertness. Both can be internally valid because they measure different endpoints. Neither is a clinical outcome.
  - ▸ 출발(`healing-abutment-reuse-single-use-controversy-overview`) 세줄: 힐링 어버트먼트 재사용 논쟁을 청결도 축(미사용 표면 복원 가능?)과 생물학적 반응 축(깨끗해도 염증 안 내나?)으로 분리한 8편 종합: 2편 SR은 어떤 통상 프로토콜도 100% 미사용 표면을 복원 못 하고, 멸균 후 잔류 단백질이 나사산·드라이버홀 요철부에 집중됨을 일치시킨다. 1% NaOCl + 초음파(바이오필름 99.7% 제거, Çetinsoy 2026), air polishing(Naghsh 2024), 화학+전기화학 병용(Kyaw 2023 RCT)은 청결도 축에서 거의 미사용 표면에 근

- `periodontal-systemic-links-adjunct-homecare-evidence-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **구강-전신의 중심 노드 = 치주염**: Botelho 2022(umbrella, MA 293개, Nature Comm) — 855개 비교 중 강한근거 66개, 그중 치주염이 암(MA 9)·심혈관(5)·당뇨(3)·임신부작용·신경퇴행 등과 연관. FSN 97.5%가 향후 뒤집힐 가능성 낮음. **단 66개 중 중재수준은 단 2개** — 연관이지 인과 아님.
  - ▸ 출발(`periodontal-systemic-links-adjunct-homecare-evidence-overview`) 세줄: 치주 관리 두 축(전신연관·보조/홈케어)을 5편(umbrella 3 + SR 2)으로 종합한 roundup 허브: 치주염–당뇨 연관은 고확신·양방향(Arbildo-Vega pooled RR ~1.26–1.86, 조절불량 당뇨 치주염 위험 86%↑), 치주염은 구강-전신 중심노드(Botelho MA 293개서 강한근거 66개, 암·심혈관·당뇨 연관, 단 중재수준은 2개뿐 — associational). 보조요법은 근거 약함·효과 작음: 프로바이오틱스(Mendonça SR 30편) 단기 소폭개선(CA

- `black-stain-caries-protection-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Surfaces the **microbiome controversy**: Actinomyces-dominance (pediatric/culture/16S) vs Capnocytophaga/Neisseria-dominance (adult permanent/NGS) — a method- and age-dependent split, not a contradiction to be averaged away
  - ▸ 출발(`black-stain-caries-protection-overview`) 세줄: 치아 흑색착색 (Black Stain, BS) 6편 종합: BS는 세균 황화수소(H₂S) + 타액 철이온(Fe³⁺) → 황화철(FeS) 침착이며 우식과 일관된 역상관 — SR+MA (Mousa 2022, 14편) 에서 우식 교차비(OR) 0.67 (95% CI 0.54–0.82), 우식치 −0.98개, 성인·취학전 아동 모두 재확인. 미생물 정체는 이질적: 소아 유치에서는 Actinomyces 우점(Li 2015, Zheng 2023)이나 성인 영구치 NGS에서는 Capnocytophaga/Nei

- `implant-occlusion-loading-biomechanics-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 4. **교합 과부하와 임플란트주위 골소실의 연관은 시사되나 근거 질이 낮다(정량 교합분석 표준화 부재).** — Di Fiore 2022 SR(7편). [미검증] 더 넓은 근거 풀로 본 Mojaver 2025 SR(160→80편, narrative, 메타분석 없음)도 같은 방향을 재확인하면서 수치를 붙인다: 교합인자 변연골소실 ~0.65–1.20 mm, 외상력 시 골수준 변화 1.0–3.0 mm, 임플란트주위염 발생률 20–50%. 핵심 기여는 **dual-pathway 모델** — 기계적 과부하가 단독으로 작용하기보다 biofilm 유발 염증과 **상승작용(synergy)**해 임플란트주위 조직 붕괴를 가속한다는 것(Mattheos: 염증 없는 dog 모델에서는 변연골소실 없이 골유착 상실; Naert/
  - ▸ 출발(`implant-occlusion-loading-biomechanics-overview`) 세줄: 임플란트 교합 클러스터 ~20편 종합(임상·FEA·동물): 치주인대(PDL) 부재로 교합력이 완충·감지되지 않아 임플란트의 능동 촉각 역치(10–100 µm)가 자연치(<10–50 µm)보다 둔하고(Singh 2026 SR), "약교합"은 즉시 힘을 낮추나 시간이 지나며 교합력이 증가해 유지 안 됨(Zhang 2022 전향, n=50). 4축 임상 근거: 임플란트 교합접촉은 6–12개월 내 상대적 저위교합으로 변동(Mao 2024 SR+MA); 단일 구치 임플란트 수복도 전악 교합력을 재분배함(G

- `implant-occlusion-loading-biomechanics-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: - [[occlusion/mojaver-2025-occlusal-overload-peri-implant-health-sr]] — 명제 4 보강: 넓은 근거풀 SR(80편, narrative)으로 과부하-골소실 정량밴드(MBL 0.65–3.0 mm·임플란트주위염 20–50%)와 dual-pathway(과부하×biofilm 염증 상승작용; 과부하=risk modifier) 제시, di-fiore의 보수적 결론을 뒤집지 않고 수치 보강 (sr, 2025)
  - ▸ 출발(`implant-occlusion-loading-biomechanics-overview`) 세줄: 임플란트 교합 클러스터 ~20편 종합(임상·FEA·동물): 치주인대(PDL) 부재로 교합력이 완충·감지되지 않아 임플란트의 능동 촉각 역치(10–100 µm)가 자연치(<10–50 µm)보다 둔하고(Singh 2026 SR), "약교합"은 즉시 힘을 낮추나 시간이 지나며 교합력이 증가해 유지 안 됨(Zhang 2022 전향, n=50). 4축 임상 근거: 임플란트 교합접촉은 6–12개월 내 상대적 저위교합으로 변동(Mao 2024 SR+MA); 단일 구치 임플란트 수복도 전악 교합력을 재분배함(G

- `cervical-composite-isolation-strategy-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **코드를 무리하게 깊이 넣지 말 것 (역방향 위험)**: Schätzle (2001, 26년 prospective)은 치은연하 충전 마진이 plaque·치은지수(Gingival Index, GI, 7회 조사 전부 p<0.001)·부착소실을 증가시킴을 보고. 격리를 위해 마진을 억지로 치은연하로 만드는 것은 장기 치주 손해가 될 수 있다 — "격리 위해 깊게"와 "치주 위해 얕게"의 상충.
  - ▸ 출발(`cervical-composite-isolation-strategy-overview`) 세줄: 5편 종합: 치경부 레진 성공의 결정 변수는 치은압배코드(retraction cord)가 아닌 오염·수분 차단(dry field) — Cochrane SR+MA(Miao 2021)에서 러버댐 수분통제가 6개월 NCCL 레진 생존율 향상(OR 2.29, 낮은 근거수준); 코드는 치은연하 마진에서 열구액(GCF)을 막는 여러 수단 중 하나이며 접착 원칙이 목적. 마진 위치가 코드 필요성을 결정: 치은연상 마진 → 코드 불필요; 치은연하 마진에서 GCF가 새는 경우에만 기계적 압배가 의미 있음; 치은연

- `cervical-composite-isolation-strategy-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 마진 위치가 코드 필요성을 결정: 치은연상 마진 → 코드 불필요; 치은연하 마진에서 GCF가 새는 경우에만 기계적 압배가 의미 있음; 치은연하 충전 마진은 플라크·치은지수(GI)·부착소실을 증가시킴(Schätzle 2001, 26년 전향, 7회 조사 전부 p<0.001) — "격리 위해 깊게"와 "치주 위해 얕게"의 상충.
  - ▸ 출발(`cervical-composite-isolation-strategy-overview`) 세줄: 5편 종합: 치경부 레진 성공의 결정 변수는 치은압배코드(retraction cord)가 아닌 오염·수분 차단(dry field) — Cochrane SR+MA(Miao 2021)에서 러버댐 수분통제가 6개월 NCCL 레진 생존율 향상(OR 2.29, 낮은 근거수준); 코드는 치은연하 마진에서 열구액(GCF)을 막는 여러 수단 중 하나이며 접착 원칙이 목적. 마진 위치가 코드 필요성을 결정: 치은연상 마진 → 코드 불필요; 치은연하 마진에서 GCF가 새는 경우에만 기계적 압배가 의미 있음; 치은연

- `diabetic-patient-immediate-implant-decision` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **The contradiction that shapes the answer.** Andrade 2021 (SR+MA, 5 quantitative studies) found **no survival penalty** for immediately *loaded* implants in type 2 DM — even in uncontrolled (high-HbA1c) patients (RR 1.08, 95% CI 0.87–1.33). Taken alone, this reads as "HbA1c is not a gate." But Al-Ansari 2022 — the largest meta-analysis (89 studies, 68,290 implants) — reports a real diabetic failu
  - ▸ 출발(`diabetic-patient-immediate-implant-decision`) 세줄: 당뇨 환자 즉시식립 가부를 여러 논문으로 종합한 페이지: DM은 절대 금기가 아니며, 결정은 **HbA1c 밴드(<8%/8–9%/≥9%)** 와 **부위(상악은 당뇨 실패 유의, 하악은 비유의)** 로 갈린다 — 두 SR+MA는 단기·하악 생존에선 일치하나 상악·장기 위험에선 충돌한다. 즉시식립(IIP)에 특화한 리(Li) 2026 SR+MA는 혈당조절 수준과 무관하게 생존율이 동등함을 재확인했으나, 변연골소실·탐침출혈은 혈당조절이 나쁠수록 유의하게 악화됨을 보였다. 임상적으로는 여전히 "생존은 

- `obturation-length-outcome-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - [미검증] 겉보기 상충(Schaeffer "short가 낫다" vs Chugal "AP는 붙여라")은 진단으로 통합됨 — 통일 변수는 "**감염의 근단 확장 지점까지 도달·소독한 뒤 그 종지점까지 extrusion 없이 충전**"이지 절대 mm값이 아님.
  - ▸ 출발(`obturation-length-outcome-overview`) 세줄: 5편의 대표 예후 연구가 수렴 — 근관충전은 근단협착부(방사선 근첨에서 0–2mm short)까지 void 없이 조밀하게, 근단 조직으로의 extrusion 없이; 과충전은 일관되게 성공률을 낮춤. 최적 작업장(WL)은 고정값이 아니라 진단 종속 — 생활치/무병소는 근첨에서 다소 먼 WL을 선호(허용), 괴사+근단치주염은 감염된 근단부를 소독하기 위해 근첨에 가까운 WL이 필요. 술전 치수/근단 상태가 모든 연구에서 지배적 예후 인자이며, 충전 길이는 그 위에 얹히는 조절 가능하지만 이차적 변수.

- `obturation-length-outcome-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This overview answers a single clinical question: **at what apical level should a root canal be prepared and obturated to maximize long-term healing?** The historical framing ("how far short of the apex?") produces an apparent contradiction — Schaeffer's meta-analysis favors staying short of the apex, while Chugal shows that infected cases fail when the WL falls short. The resolution is that the t
  - ▸ 출발(`obturation-length-outcome-overview`) 세줄: 5편의 대표 예후 연구가 수렴 — 근관충전은 근단협착부(방사선 근첨에서 0–2mm short)까지 void 없이 조밀하게, 근단 조직으로의 extrusion 없이; 과충전은 일관되게 성공률을 낮춤. 최적 작업장(WL)은 고정값이 아니라 진단 종속 — 생활치/무병소는 근첨에서 다소 먼 WL을 선호(허용), 괴사+근단치주염은 감염된 근단부를 소독하기 위해 근첨에 가까운 WL이 필요. 술전 치수/근단 상태가 모든 연구에서 지배적 예후 인자이며, 충전 길이는 그 위에 얹히는 조절 가능하지만 이차적 변수.

- `veneer-material-survival-protocol-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: 4. **Minimally invasive veneers (0.2–0.5 mm) demonstrate equal or superior survival to conventional preparations (0.3–1.0 mm).** Ali (2023), a SR of 4 comparative studies, found MPVs showed higher survival rates and longer mean success periods than CVs, refuting the prior assumption of conventional preparation superiority. Ultra-thin contact-lens feldspathic veneers (0.2–0.3 mm) additionally elimi
  - ▸ 출발(`veneer-material-survival-protocol-overview`) 세줄: 10편 종합(SR+MA 5편 포함): 모든 세라믹 비니어 재료의 장기 생존율은 통계적으로 유사(93–97%; feldspathic 96.13%, LDS 96.81%, LRGC 93.70%)하나 LDS가 합병증 부담 가장 낮음(10년 기술적 합병증 6.1% vs 장석 41.48%; Klein 2025, 29편·7,753 비니어). 상아질 변연 노출이 실패율 ≈10배(El-Mowafy 2018); 절단연 피개 디자인은 생존율에 영향 없음(OR 1.25 NS; Albanesi 2016); 최소삭제(0.

- `periodontal-regenerative-platelet-concentrates-overview` [overviews] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: > - **GBR 기전 배경지식**: Cho 2026 스코핑리뷰가 "왜 PRF 효과가 부위별로 들쭉날쭉한가"의 세포·분자적 설명을 제공(섬유소 매트릭스 방출동역학·골면역학) — Assiri 2026(염소 모델)의 결손유형별(장골 vs 치조골) 상반된 효과와 함께 읽으면 트리오의 "결손 술식에 추가하면 대개 돕는다"는 원칙이 결손 해부학적 맥락에 크게 의존함을 시사.
  - ▸ 출발(`periodontal-regenerative-platelet-concentrates-overview`) 세줄: Periodontology 2000 2024년 자매 SR/MA(NMA) 3편 종합 — 자가혈소판농축물(Autologous Platelet Concentrate, APC: PRF/PRP/CGF)을 치근이개부(21 RCT)·골내결손(55 RCT)·근면피복(NMA, 109 RCT) 3대 치주재생 적응증에 걸쳐 지도화. 공통 패턴: PRF를 술식에 추가하면 항상 유의 개선(치근이개부 PPD +1.73mm·골내결손 PPD +1.27mm·근면피복 +6.12%); 확립된 재료와 head-to-head는 대등 

- `periodontal-regenerative-platelet-concentrates-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The three sibling papers' estimates sit inside a wider evidence context that reinforces, extends, or in one case contradicts the "PRF as adjunct" thesis:
  - ▸ 출발(`periodontal-regenerative-platelet-concentrates-overview`) 세줄: Periodontology 2000 2024년 자매 SR/MA(NMA) 3편 종합 — 자가혈소판농축물(Autologous Platelet Concentrate, APC: PRF/PRP/CGF)을 치근이개부(21 RCT)·골내결손(55 RCT)·근면피복(NMA, 109 RCT) 3대 치주재생 적응증에 걸쳐 지도화. 공통 패턴: PRF를 술식에 추가하면 항상 유의 개선(치근이개부 PPD +1.73mm·골내결손 PPD +1.27mm·근면피복 +6.12%); 확립된 재료와 head-to-head는 대등 

- `periodontal-regenerative-platelet-concentrates-overview` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - **PRF's benefit doesn't generalize to non-surgical therapy**: [[periodontics/sherif-2025-iprf-vitamin-c-nonsurgical-periodontitis]] (3-arm RCT, n=45) tested i-PRF±vitamin C as an adjunct to non-surgical PMPR in stage-II periodontitis and found a clean null on BOP/PD/CAL at 6 months — the only durable benefit was reduced post-operative pain (days 2–3, p≤0.021). A floor-effect counterpoint to the 
  - ▸ 출발(`periodontal-regenerative-platelet-concentrates-overview`) 세줄: Periodontology 2000 2024년 자매 SR/MA(NMA) 3편 종합 — 자가혈소판농축물(Autologous Platelet Concentrate, APC: PRF/PRP/CGF)을 치근이개부(21 RCT)·골내결손(55 RCT)·근면피복(NMA, 109 RCT) 3대 치주재생 적응증에 걸쳐 지도화. 공통 패턴: PRF를 술식에 추가하면 항상 유의 개선(치근이개부 PPD +1.73mm·골내결손 PPD +1.27mm·근면피복 +6.12%); 확립된 재료와 head-to-head는 대등 

- `periodontal-regenerative-platelet-concentrates-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Bone regeneration outside the alveolus is defect-geometry-dependent, not uniformly positive**: [[bone-regeneration/assiri-2026-iprf-prf-beta-tcp-bone-regeneration-goat]] (animal, goat critical-size metacarpal defects, micro-CT) found i-PRF + β-TCP significantly outperformed PRF + β-TCP and β-TCP alone on new bone volume/density at 8 weeks — a positive PRF-class signal, but in a long-bone criti
  - ▸ 출발(`periodontal-regenerative-platelet-concentrates-overview`) 세줄: Periodontology 2000 2024년 자매 SR/MA(NMA) 3편 종합 — 자가혈소판농축물(Autologous Platelet Concentrate, APC: PRF/PRP/CGF)을 치근이개부(21 RCT)·골내결손(55 RCT)·근면피복(NMA, 109 RCT) 3대 치주재생 적응증에 걸쳐 지도화. 공통 패턴: PRF를 술식에 추가하면 항상 유의 개선(치근이개부 PPD +1.73mm·골내결손 PPD +1.27mm·근면피복 +6.12%); 확립된 재료와 head-to-head는 대등 

- `gothic-arch-jaw-relation-recording-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **정확도(reference 대비 일치) 위계는 reference에 따라 뒤집힌다**: 무치악 split-cast 검증에서는 **nick-and-notch(0.15/0.23mm) < 구내 고딕아치(0.42/0.51) < 구외 고딕아치(0.74/0.86)** 로 정적(static) 왁스기록이 최소 오차 (Singh 2026). 즉 GAT은 **재현성은 최고지만 정적 기준 대비 오차는 더 큼** — "재현성 ≠ 정확도"의 핵심 모순.
  - ▸ 출발(`gothic-arch-jaw-relation-recording-overview`) 세줄: 고딕아치(arrow-point) 트레이싱과 수평 악간관계(중심위) 기록 7편 종합 — **재현성 위계**: 디지털 고딕아치 ~0.98·체위무관 > 턱끝유도 0.79·앙와위 신뢰 > 삼킴 0.62·직립 한정(Bhagat 2025); 양손조작 ≥ 턱끝유도(de Moraes Melo Neto 2021 SR). **기준 대비 정확도 위계**는 반전: nick-and-notch(0.15/0.23 mm) < 구내 고딕아치(0.42/0.51) < 구외 고딕아치(0.74/0.86)로 정적 왁스기록이 split-

- `gothic-arch-jaw-relation-recording-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Here the two non-GAT-friendly results live, and they are not contradictions but different *reference standards*:
  - ▸ 출발(`gothic-arch-jaw-relation-recording-overview`) 세줄: 고딕아치(arrow-point) 트레이싱과 수평 악간관계(중심위) 기록 7편 종합 — **재현성 위계**: 디지털 고딕아치 ~0.98·체위무관 > 턱끝유도 0.79·앙와위 신뢰 > 삼킴 0.62·직립 한정(Bhagat 2025); 양손조작 ≥ 턱끝유도(de Moraes Melo Neto 2021 SR). **기준 대비 정확도 위계**는 반전: nick-and-notch(0.15/0.23 mm) < 구내 고딕아치(0.42/0.51) < 구외 고딕아치(0.74/0.86)로 정적 왁스기록이 split-

- `oral-microbiome-biofilm-dysbiosis-synthesis` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 구강 미생물·바이오필름 review 19편 통합(Socransky 1998 complex paradigm + Costerton 1999 biofilm paradigm 2개 historical foundation 포함): 3축 — ①매트릭스(EPS/matrixome): glucan이 caries 바이오필름 핵심 virulence, 국소 산성 미세환경(pH 4.5–5.5) 2시간 이상 지속; ②생태(microbiome): ~1,000종·부위당 ~50종, 건강=generalist·질환=specialist(Baker 2024가 종수준 biogeography로 정밀화); ③병인(dysbiosis): 치주염은 keystone pathogen P. gingivalis(<0.01%)가 주도하는 PSD 모델·균주특이적(Mu
  - ▸ 출발(`oral-microbiome-biofilm-dysbiosis-synthesis`) 세줄: 구강 미생물·바이오필름 review 19편 통합(Socransky 1998 complex paradigm + Costerton 1999 biofilm paradigm 2개 historical foundation 포함): 3축 — ①매트릭스(EPS/matrixome): glucan이 caries 바이오필름 핵심 virulence, 국소 산성 미세환경(pH 4.5–5.5) 2시간 이상 지속; ②생태(microbiome): ~1,000종·부위당 ~50종, 건강=generalist·질환=specialis

- `oral-microbiome-biofilm-dysbiosis-synthesis` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[periodontics/scannapieco-2021-dysbiosis-oral-microbiome-periodontitis]] — 흔한 치주염 = 다양성 증가형 personalized pathology, keystone dysbiosis 일반화 비판 (contradicts PSD 모델의 과잉일반화)
  - ▸ 출발(`oral-microbiome-biofilm-dysbiosis-synthesis`) 세줄: 구강 미생물·바이오필름 review 19편 통합(Socransky 1998 complex paradigm + Costerton 1999 biofilm paradigm 2개 historical foundation 포함): 3축 — ①매트릭스(EPS/matrixome): glucan이 caries 바이오필름 핵심 virulence, 국소 산성 미세환경(pH 4.5–5.5) 2시간 이상 지속; ②생태(microbiome): ~1,000종·부위당 ~50종, 건강=generalist·질환=specialis

- `computerized-needle-free-anesthesia-delivery-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Clinical bottom line: market these devices as anxiety-reduction and supplemental-injection-avoidance tools, not as injection pain reducers (rigorous RCTs refute that claim); they are not a primary substitute for surgical anesthesia (higher supplemental-block rates for impacted third molars, Ramanathan 2023), and evidence quality spans strong blinded RCTs to weak unblinded cohorts.
  - ▸ 출발(`computerized-needle-free-anesthesia-delivery-overview`) 세줄: 9편 종합(CCLAD·The Wand·STA·바늘없는 주사기): 가장 엄격한 5군 RCT(Küçükkurt 2026, n=200)는 5개 전달시스템 간 주사통증 유의차 없음(p=0.380, 모든 g<0.20); 장비 작동원리 사전 설명도 불안·통증 감소 못 함(Rizzo-Lorenzo 2020 RCT). 맥락별 2차 효과는 존재: 소아 RCT에서 The Wand가 통증·심박수·행동 모두 우위(Garret-Bernardin 2017); 치주기구조작에서 컴퓨터제어가 보충마취 필요율 100% → 24%

- `computerized-needle-free-anesthesia-delivery-overview` [overviews] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: - 성인 대상 대형 5-arm RCT(Küçükkurt)와 소아 crossover(Garret-Bernardin)의 상반된 결과를 같은 프로토콜로 직접 비교하는 연구 부재 — 연령·주사부위(구개 vs 협측)가 진짜 조절변수인지 확인 필요.
  - ▸ 출발(`computerized-needle-free-anesthesia-delivery-overview`) 세줄: 9편 종합(CCLAD·The Wand·STA·바늘없는 주사기): 가장 엄격한 5군 RCT(Küçükkurt 2026, n=200)는 5개 전달시스템 간 주사통증 유의차 없음(p=0.380, 모든 g<0.20); 장비 작동원리 사전 설명도 불안·통증 감소 못 함(Rizzo-Lorenzo 2020 RCT). 맥락별 2차 효과는 존재: 소아 RCT에서 The Wand가 통증·심박수·행동 모두 우위(Garret-Bernardin 2017); 치주기구조작에서 컴퓨터제어가 보충마취 필요율 100% → 24%

- `computerized-needle-free-anesthesia-delivery-overview` [overviews] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: - [[local-anesthesia/garret-bernardin-2017-pain-experience-behavior-management-pediatric]] — 소아 맥락에서의 상반된 결과
  - ▸ 출발(`computerized-needle-free-anesthesia-delivery-overview`) 세줄: 9편 종합(CCLAD·The Wand·STA·바늘없는 주사기): 가장 엄격한 5군 RCT(Küçükkurt 2026, n=200)는 5개 전달시스템 간 주사통증 유의차 없음(p=0.380, 모든 g<0.20); 장비 작동원리 사전 설명도 불안·통증 감소 못 함(Rizzo-Lorenzo 2020 RCT). 맥락별 2차 효과는 존재: 소아 RCT에서 The Wand가 통증·심박수·행동 모두 우위(Garret-Bernardin 2017); 치주기구조작에서 컴퓨터제어가 보충마취 필요율 100% → 24%

- `implant-length-selection-why-not-always-short` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: 2. **Head-to-head without grafting, MBL is equal — and length is not the determinant.** Kim 2026 (6 mm vs 8.5 mm, mean 6.5 y, no augmentation confound in the short arm) found MBL statistically **no different** (0.05 vs 0.12 mm, NS). Crucially, the higher crown-to-implant ratio of short implants (1.96 vs 1.41) was **not** associated with MBL (r=0.079, p=0.477) — refuting the "short = worse lever ar
  - ▸ 출발(`implant-length-selection-why-not-always-short`) 세줄: 9편 종합(SR+MA/umbrella 6, 후향 2, 전향 1): 숏 임플란트(≤8mm)는 1–3년 head-to-head 메타분석에서 긴 임플란트와 생존율이 동등하면서 변연골소실(MBL)이 더 적고 생물학적 합병증도 더 적다(Yu 2021: MBL WMD −0.22; Mester 2023: 생물학적 합병증 RR 0.46). 숏 임플란트가 최선이 아닌 세 가지 상황 — ①잔존골고(RBH) <4–5 mm이면 자리 자체가 없음, ②불리한 치관-임플란트 비(C/I)/이갈이/긴 span은 lever ar

- `abutment-emergence-profile-peri-implant-tissue-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Canullo 2020 (SR+MA, 10 studies; 6 pooled — 4 RCT/2 CCT, 118 patients, 182 implants) tested whether **titanium healing-abutment surface modifications** (machined vs anodized/laser/other) change peri-implant soft-tissue behavior. Short-term, modified surfaces showed **no significant difference** vs controls in plaque index (P=0.091), bleeding on probing (P=0.099), or probing depth (P=0.488), with n
  - ▸ 출발(`abutment-emergence-profile-peri-implant-tissue-overview`) 세줄: 10편 종합(SR+MA 1·SR 2·scoping review 1·RCT 3·후향 1·전임상 동물 2): 출현윤곽 형태·각도, 지대주 표면 처리, 분리 횟수, 맞춤형 치유지대주, 디지털 윤곽 전달 5축 평가. 출현윤곽 형태·각도가 지배 인자: 전치부 볼록은 오목 대비 퇴축 위험 ~13배(Siegenthaler 2022); 구치부 W/H 기반 ~32° 각도가 퇴축 절반(Wang 2022); 개 모델이 각도→골소실 용량반응 인과 확립(80° vs 20° ~4배 MBL, ≥60° 접합상피 붕괴; <40

- `abutment-emergence-profile-peri-implant-tissue-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Clinical/conceptual bridge to peri-implantitis management.** **Pirc 2026** (narrative review, University of Zurich, plus a clinical case) does not add new quantitative evidence but performs the field-consolidating move this axis needed: it unifies four overlapping nomenclatures for the transmucosal zone (Supracrestal Tissue Height/STH, Implant Supracrestal Complex/ISC, Supraplatform Complex, and
  - ▸ 출발(`abutment-emergence-profile-peri-implant-tissue-overview`) 세줄: 10편 종합(SR+MA 1·SR 2·scoping review 1·RCT 3·후향 1·전임상 동물 2): 출현윤곽 형태·각도, 지대주 표면 처리, 분리 횟수, 맞춤형 치유지대주, 디지털 윤곽 전달 5축 평가. 출현윤곽 형태·각도가 지배 인자: 전치부 볼록은 오목 대비 퇴축 위험 ~13배(Siegenthaler 2022); 구치부 W/H 기반 ~32° 각도가 퇴축 절반(Wang 2022); 개 모델이 각도→골소실 용량반응 인과 확립(80° vs 20° ~4배 MBL, ≥60° 접합상피 붕괴; <40

- `abutment-emergence-profile-peri-implant-tissue-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: | [[implants/canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma]] | SR+MA | 6 pooled / 182 implants | (a) surface | No short-term difference in PI/BoP/PD (P=0.091/0.099/0.488); long-term contradictory |
  - ▸ 출발(`abutment-emergence-profile-peri-implant-tissue-overview`) 세줄: 10편 종합(SR+MA 1·SR 2·scoping review 1·RCT 3·후향 1·전임상 동물 2): 출현윤곽 형태·각도, 지대주 표면 처리, 분리 횟수, 맞춤형 치유지대주, 디지털 윤곽 전달 5축 평가. 출현윤곽 형태·각도가 지배 인자: 전치부 볼록은 오목 대비 퇴축 위험 ~13배(Siegenthaler 2022); 구치부 W/H 기반 ~32° 각도가 퇴축 절반(Wang 2022); 개 모델이 각도→골소실 용량반응 인과 확립(80° vs 20° ~4배 MBL, ≥60° 접합상피 붕괴; <40

- `abutment-emergence-profile-peri-implant-tissue-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Shape > surface/disconnection is a hierarchy, not a contradiction.** The two shape RCTs deliver large, significant, same-direction effects (recession 13× higher convex; recession halved at lower angle), while the surface SR+MA and the OAOT RCT are flatly null on tissue outcomes. There is no genuine conflict — the levers simply differ in magnitude, and clinical attention should track the magnit
  - ▸ 출발(`abutment-emergence-profile-peri-implant-tissue-overview`) 세줄: 10편 종합(SR+MA 1·SR 2·scoping review 1·RCT 3·후향 1·전임상 동물 2): 출현윤곽 형태·각도, 지대주 표면 처리, 분리 횟수, 맞춤형 치유지대주, 디지털 윤곽 전달 5축 평가. 출현윤곽 형태·각도가 지배 인자: 전치부 볼록은 오목 대비 퇴축 위험 ~13배(Siegenthaler 2022); 구치부 W/H 기반 ~32° 각도가 퇴축 절반(Wang 2022); 개 모델이 각도→골소실 용량반응 인과 확립(80° vs 20° ~4배 MBL, ≥60° 접합상피 붕괴; <40

- `abutment-emergence-profile-peri-implant-tissue-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/rios-santos-2020-one-abutment-one-time-rct]] — disconnection axis (b): RCT finding OAOT confers no bone benefit vs repeated disconnection, but height ≥2 mm does — contradicts the disconnection-avoidance rationale
  - ▸ 출발(`abutment-emergence-profile-peri-implant-tissue-overview`) 세줄: 10편 종합(SR+MA 1·SR 2·scoping review 1·RCT 3·후향 1·전임상 동물 2): 출현윤곽 형태·각도, 지대주 표면 처리, 분리 횟수, 맞춤형 치유지대주, 디지털 윤곽 전달 5축 평가. 출현윤곽 형태·각도가 지배 인자: 전치부 볼록은 오목 대비 퇴축 위험 ~13배(Siegenthaler 2022); 구치부 W/H 기반 ~32° 각도가 퇴축 절반(Wang 2022); 개 모델이 각도→골소실 용량반응 인과 확립(80° vs 20° ~4배 MBL, ≥60° 접합상피 붕괴; <40

- `nsaid-osseointegration-impairment-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 핵심 명제: 비스테로이드소염제(Non-Steroidal Anti-Inflammatory Drug, NSAID)의 임플란트 골유착(Osseointegration) 저해는 **근거 층위마다 신호 강도가 다르다** — 세포·동물에선 뚜렷하나 인체 임상에선 약하고 상충한다. 6편(리뷰 2·SR 1·RCT 1·대규모 코호트 1·동물 1)을 근거 사다리로 재배열.
  - ▸ 출발(`nsaid-osseointegration-impairment-overview`) 세줄: 6편(리뷰 2·PRISMA SR 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열. 기전상 COX-2 억제가 초기 임플란트 주위 골형성에 필요한 PGE2를 낮추며, 범인은 COX-2(COX-1 억제는 무해), 효과는 용량·기간·선택성 의존(동물서 장기·고용량 COX-2만 저해); 인체 RCT(ibuprofen 7일·naproxen 파일럿)는 비유의하나 과소검정·점추정은

- `nsaid-osseointegration-impairment-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **치과 술후 진통제 결정**: ①아세트아미노펜(Acetaminophen) 1순위(경로 무관·무저해) → ②NSAID 필요 시 **단기(3–7일)·최저용량**, 만성 상용 회피 → ③이부프로펜은 대규모 코호트 신호가 가장 커 신선 임플란트부에서 신중 → ④위험군(고령·당뇨·골다공증·골질 불량)일수록 보수적. 근거강도: 기전·용량축 = 강, 인체 인과 = 약(상충).
  - ▸ 출발(`nsaid-osseointegration-impairment-overview`) 세줄: 6편(리뷰 2·PRISMA SR 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열. 기전상 COX-2 억제가 초기 임플란트 주위 골형성에 필요한 PGE2를 낮추며, 범인은 COX-2(COX-1 억제는 무해), 효과는 용량·기간·선택성 의존(동물서 장기·고용량 COX-2만 저해); 인체 RCT(ibuprofen 7일·naproxen 파일럿)는 비유의하나 과소검정·점추정은

- `nsaid-osseointegration-impairment-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 6편(리뷰 2·PRISMA SR 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열.
  - ▸ 출발(`nsaid-osseointegration-impairment-overview`) 세줄: 6편(리뷰 2·PRISMA SR 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열. 기전상 COX-2 억제가 초기 임플란트 주위 골형성에 필요한 PGE2를 낮추며, 범인은 COX-2(COX-1 억제는 무해), 효과는 용량·기간·선택성 의존(동물서 장기·고용량 COX-2만 저해); 인체 RCT(ibuprofen 7일·naproxen 파일럿)는 비유의하나 과소검정·점추정은

- `nsaid-osseointegration-impairment-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 4. **인체 임상은 약·상충**: ibuprofen 7일 RCT 2편·naproxen 파일럿 RCT는 골유착 지표 비유의(단 과소검정, 점추정 저해 방향) — Kumchai 2025, Luo 2018(Alissa·Sakka). 그러나 대규모 후향코호트는 ibuprofen 조기실패 OR 2.29–2.87 — Chatzopoulos 2025. [상충: RCT 무영향 vs 코호트 위험신호]
  - ▸ 출발(`nsaid-osseointegration-impairment-overview`) 세줄: 6편(리뷰 2·PRISMA SR 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열. 기전상 COX-2 억제가 초기 임플란트 주위 골형성에 필요한 PGE2를 낮추며, 범인은 COX-2(COX-1 억제는 무해), 효과는 용량·기간·선택성 의존(동물서 장기·고용량 COX-2만 저해); 인체 RCT(ibuprofen 7일·naproxen 파일럿)는 비유의하나 과소검정·점추정은

- `nsaid-osseointegration-impairment-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 5. **COX-2 딜레마 + 공백**: 아스피린 항혈소판 보존엔 셀레콕시브가 안전하나([[nsaid-aspirin-antiplatelet-interaction-overview]]), 골형성엔 COX-2 선택제가 위험 방향 — 두 목표 상충. 게다가 **인체에서 COX-2 선택제 골유착을 직접 본 연구 부재** — Luo 2018 명시. [Rule #4 공백]
  - ▸ 출발(`nsaid-osseointegration-impairment-overview`) 세줄: 6편(리뷰 2·PRISMA SR 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열. 기전상 COX-2 억제가 초기 임플란트 주위 골형성에 필요한 PGE2를 낮추며, 범인은 COX-2(COX-1 억제는 무해), 효과는 용량·기간·선택성 의존(동물서 장기·고용량 COX-2만 저해); 인체 RCT(ibuprofen 7일·naproxen 파일럿)는 비유의하나 과소검정·점추정은

- `tilted-axial-implant-angled-abutment-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **The gap resolved**: FEA reports *relative* stress increases; it does not say the implant fails. Bilgi-Ozyetim's absolute numbers (all <550 MPa) and Murat's peak of 266 MPa both sit well inside the safe envelope. So "tilted has higher FEA stress" and "tilted is clinically equivalent" are **not contradictory** — the extra stress is real but sub-critical, expressed clinically only as the small long
  - ▸ 출발(`tilted-axial-implant-angled-abutment-overview`) 세줄: 7편 종합: 의도적 경사식립은 생존율·단기 변연골에서 수직식립과 임상적으로 동등(Del Fabbro 2014; Lin 2018)하며 장기(3–18년)엔 통계적으로 유의하나 작은 MBL 페널티가 존재(Del Fabbro 2022, P<.0001); 임플란트 생존율 93.91%·보철 생존율 99.31%. FEA는 각도·축외 하중 증가 시 응력이 오르지만 최대값(~266 MPa)이 티타늄 항복강도(550 MPa)보다 훨씬 낮아 in-vitro와 임상의 간극이 해소되며, 협설(BL) 하중 방향이 임플란트

- `clear-aligner-indications-limitations` [overviews] (SOFT→charoenrat-2025-clear-aligner-anterior-open-bite-molar-intrusion-sr-ma, 'whereas' · 반면(대조))
  - **근거 문장**: Vertical correction — specifically anterior open bite — shows a distinctive aligner mechanism: an SR+MA ([[orthodontics/clear-aligner/charoenrat-2025-clear-aligner-anterior-open-bite-molar-intrusion-sr-ma]], 10 studies, no RCTs) found CAT closes open bite predominantly via **incisor extrusion** (U1 +0.87 mm, L1 +1.06 mm) with **no significant molar intrusion**, whereas fixed appliances with tempor
  - ▸ 출발(`clear-aligner-indications-limitations`) 세줄: 투명교정(Clear Aligner Therapy, CAT) 위키 56편을 효율(착용 프로토콜·개방교합 기전·제품라인별 예측성 포함)·이동특이 한계(발치 Roller Coaster Effect·스피 곡선 성형 실패 포함)·Class II 전략·Class III camouflage/성장기 증례·생체역학/설계(attachment 재료과학·실측 force/moment 포함)·확장·치근흡수/치조골(발치 프로토콜별 위험 포함)·치주(구강미생물총 기전 포함)·저작/턱관절/이갈이·가속보조·환자 기대/동의 11축
  - ▸ 대상(`charoenrat-2025-clear-aligner-anterior-open-bite-molar-intrusion-sr-ma`) 세줄: SR+MA (PRISMA/PROSPERO, 10편 — non-RCT 4편·전후비교 6편): 전치부 개방교합 교정에서 투명교정(Clear Aligner Treatment, CAT)과 TAD 병용 고정식 장치(FATADs)를 비교. CAT는 절치 정출(상악 +0.87 mm, 하악 +1.06 mm)로 overbite를 +2.77 mm 증가시키나 구치 압하는 유의하지 않았고, FATADs는 구치 압하(상악 +1.88 mm, 하악 +0.45 mm)를 통해 CAT보다 +1.64 mm 더 큰 overbite 

- `clear-aligner-indications-limitations` [overviews] (AMBIG→meade-2026-invisalign-lite-efficacy-retrospective, 'whereas' · 반면(대조))
  - **근거 문장**: Vertical correction — specifically anterior open bite — shows a distinctive aligner mechanism: an SR+MA ([[orthodontics/clear-aligner/charoenrat-2025-clear-aligner-anterior-open-bite-molar-intrusion-sr-ma]], 10 studies, no RCTs) found CAT closes open bite predominantly via **incisor extrusion** (U1 +0.87 mm, L1 +1.06 mm) with **no significant molar intrusion**, whereas fixed appliances with tempor
  - ▸ 출발(`clear-aligner-indications-limitations`) 세줄: 투명교정(Clear Aligner Therapy, CAT) 위키 56편을 효율(착용 프로토콜·개방교합 기전·제품라인별 예측성 포함)·이동특이 한계(발치 Roller Coaster Effect·스피 곡선 성형 실패 포함)·Class II 전략·Class III camouflage/성장기 증례·생체역학/설계(attachment 재료과학·실측 force/moment 포함)·확장·치근흡수/치조골(발치 프로토콜별 위험 포함)·치주(구강미생물총 기전 포함)·저작/턱관절/이갈이·가속보조·환자 기대/동의 11축

- `clear-aligner-indications-limitations` [overviews] (SOFT→zhang-2025-clear-aligner-based-multidisciplinary, 'Unlike' · 다름)
  - **근거 문장**: Unlike Class II, where SR+MA-level evidence exists (axis 2), the wiki's Class III aligner evidence started from two single case reports bracketing the age spectrum and has since gained a narrative-review umbrella plus its first controlled comparative studies. In an **adult**, [[orthodontics/clear-aligner/zhang-2025-clear-aligner-based-multidisciplinary]] (n=1, 28-year-old, skeletal Class III just 
  - ▸ 출발(`clear-aligner-indications-limitations`) 세줄: 투명교정(Clear Aligner Therapy, CAT) 위키 56편을 효율(착용 프로토콜·개방교합 기전·제품라인별 예측성 포함)·이동특이 한계(발치 Roller Coaster Effect·스피 곡선 성형 실패 포함)·Class II 전략·Class III camouflage/성장기 증례·생체역학/설계(attachment 재료과학·실측 force/moment 포함)·확장·치근흡수/치조골(발치 프로토콜별 위험 포함)·치주(구강미생물총 기전 포함)·저작/턱관절/이갈이·가속보조·환자 기대/동의 11축
  - ▸ 대상(`zhang-2025-clear-aligner-based-multidisciplinary`) 세줄: 증례보고, n=1, 28세 성인 여성 골격성 Class III 부정교합(Wits −4.92mm, Holdaway angle 11°, 기능적 요소를 동반한 완전 Class III 구치 관계) — 투명교정(Invisalign) + 보철·임플란트를 통합한 다학제 비발치·비수술 camouflage 치료. 하악전치 함입·설측경사 + 상악전치 순측경사(U1-SN 99.17°→109.74°, L1-MP 96.37°→88.08°)를 통한 교합거상, Class III 고무줄, 구치부 교합면 부착물(bite ram

- `clear-aligner-indications-limitations` [overviews] (AMBIG→ye-2025-combined-use-of-miniscrews, 'Unlike' · 다름)
  - **근거 문장**: Unlike Class II, where SR+MA-level evidence exists (axis 2), the wiki's Class III aligner evidence started from two single case reports bracketing the age spectrum and has since gained a narrative-review umbrella plus its first controlled comparative studies. In an **adult**, [[orthodontics/clear-aligner/zhang-2025-clear-aligner-based-multidisciplinary]] (n=1, 28-year-old, skeletal Class III just 
  - ▸ 출발(`clear-aligner-indications-limitations`) 세줄: 투명교정(Clear Aligner Therapy, CAT) 위키 56편을 효율(착용 프로토콜·개방교합 기전·제품라인별 예측성 포함)·이동특이 한계(발치 Roller Coaster Effect·스피 곡선 성형 실패 포함)·Class II 전략·Class III camouflage/성장기 증례·생체역학/설계(attachment 재료과학·실측 force/moment 포함)·확장·치근흡수/치조골(발치 프로토콜별 위험 포함)·치주(구강미생물총 기전 포함)·저작/턱관절/이갈이·가속보조·환자 기대/동의 11축

- `clear-aligner-indications-limitations` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: The growing-patient side gains its first RCT-level counterpart to Ye 2025's case report, though for a narrower **isolated dental (pseudo-Class III)** presentation rather than true skeletal Class III: an RCT in mixed dentition ([[orthodontics/clear-aligner/gok-2025-clear-aligner-z-spring-anterior-crossbite-mixed-dentition]], n=30, 7–12y, Angle Class I molar relationship + isolated anterior crossbit
  - ▸ 출발(`clear-aligner-indications-limitations`) 세줄: 투명교정(Clear Aligner Therapy, CAT) 위키 56편을 효율(착용 프로토콜·개방교합 기전·제품라인별 예측성 포함)·이동특이 한계(발치 Roller Coaster Effect·스피 곡선 성형 실패 포함)·Class II 전략·Class III camouflage/성장기 증례·생체역학/설계(attachment 재료과학·실측 force/moment 포함)·확장·치근흡수/치조골(발치 프로토콜별 위험 포함)·치주(구강미생물총 기전 포함)·저작/턱관절/이갈이·가속보조·환자 기대/동의 11축

- `clear-aligner-indications-limitations` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: In growing patients, CAT can expand the maxilla but **significantly less than conventional expanders** ([[orthodontics/clear-aligner/fonseca-planells-2026-clear-aligner-maxillary-expansion-growing]], 15 studies/7 pooled: intermolar width −1.77 mm, palatal volume −460.6 mm³, arch perimeter −1.75 mm favoring conventional), and the expansion is **mainly dentoalveolar** (tipping of anterior/deciduous 
  - ▸ 출발(`clear-aligner-indications-limitations`) 세줄: 투명교정(Clear Aligner Therapy, CAT) 위키 56편을 효율(착용 프로토콜·개방교합 기전·제품라인별 예측성 포함)·이동특이 한계(발치 Roller Coaster Effect·스피 곡선 성형 실패 포함)·Class II 전략·Class III camouflage/성장기 증례·생체역학/설계(attachment 재료과학·실측 force/moment 포함)·확장·치근흡수/치조골(발치 프로토콜별 위험 포함)·치주(구강미생물총 기전 포함)·저작/턱관절/이갈이·가속보조·환자 기대/동의 11축

- `clear-aligner-indications-limitations` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: CAT's periodontal advantage is consistently *signalled* but **not firmly proven**. Baneshi's RCT-only MA gives favorable pooled effect sizes (plaque/gingival/bleeding), yet the dedicated periodontal SR+MA ([[orthodontics/clear-aligner/crego-ruiz-2023-periodontal-gingival-recession-aligner-vs-fixed-sr-ma]], 12 studies; only plaque mid-term MD −0.99 and PPD long-term −0.93 mm significant, both I²=99
  - ▸ 출발(`clear-aligner-indications-limitations`) 세줄: 투명교정(Clear Aligner Therapy, CAT) 위키 56편을 효율(착용 프로토콜·개방교합 기전·제품라인별 예측성 포함)·이동특이 한계(발치 Roller Coaster Effect·스피 곡선 성형 실패 포함)·Class II 전략·Class III camouflage/성장기 증례·생체역학/설계(attachment 재료과학·실측 force/moment 포함)·확장·치근흡수/치조골(발치 프로토콜별 위험 포함)·치주(구강미생물총 기전 포함)·저작/턱관절/이갈이·가속보조·환자 기대/동의 11축

- `complete-denture-digital-overdenture-overview` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: - This **updates and partly overturns** an earlier SR (Ahmed et al.) that had reported *better* implant survival for 1-IOD; once post-2017 RCTs are added, that survival advantage disappears.
  - ▸ 출발(`complete-denture-digital-overdenture-overview`) 세줄: 24편 기반 종합: 전통 총의치 평균 수명 10.1년(Taylor 2021); 밀링 CAD/CAM은 기계적 물성·유지력에서 우월하나 환자 만족도·OHRQoL은 세 제작법 동등; IOD 임플란트 수가 가장 큰 보철 결정 변수 — 1-IOD는 2-IOD 대비 보철 합병증 약 2배(Koyama 2025 SR+MA). 어태치먼트: LOCATOR가 합병증 최소; 마그넷은 7.4배 높아 비권고; 바(splinted) 선택 시 CAD/CAM 밀링 티타늄 bar가 최강 근거; PEEK·BioHPP 바는 임플란트

- `mandibular-anesthesia-failure-accessory-innervation-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "이설골근신경은 운동신경이라 통증과 무관" — Stein 2007이 반박: 혼합 감각. [저등급~합의]
  - ▸ 출발(`mandibular-anesthesia-failure-accessory-innervation-overview`) 세줄: IANB 해부학적 실패 원인 local-anesthesia 6편 종합: 실패는 다인성(피질골·바늘편향·신경위치·부신경지배, 측절치 실패율 81%; Malamed 2011)이며, 입술 마비가 있는데도 치아 감각이 남으면 반복 IANB가 아니라 부신경지배를 의심해야 한다. 해부학적으로 구별되는 3개 경로: ① 이설골근신경(혼합 운동-감각, 근막 장벽으로 표준 IANB 회피; Stein 2007), ② 경부신경총 횡경부신경(C2–C3, 사체 2례 중 1례 확인; Lin 2013 + Kim 2016 SR

- `bone-quality-implant-risk-modification-overview` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[implants/kindaro-2026-parathyroid-hormone-implant-osseointegration-osteoporosis-sr]] — SR of 12 preclinical studies: intermittent PTH/teriparatide raises BIC, BV/TV, and removal torque in osteoporotic animals; combination > monotherapy; **animal-only, no human data**, 7/12 high risk of blinding bias. The osteoanabolic counterpoint to the antiresorptive-hazard axis.
  - ▸ 출발(`bone-quality-implant-risk-modification-overview`) 세줄: 골질(Bone Quality)을 "위험 축"으로 묶은 11편 종합: 국소 골밀도(Lekholm-Zarb I–IV / Misch D1–D4)가 초기 안정성·실패 위험을 결정하고(type IV는 ~1.5–1.9배 실패, ISQ 58–65 vs type I 72–80; Rosa 2024 SR+MA, 55편·29,905개), 해면골 양이 아닌 **치조정 피질골 두께(Crestal Cortical Thickness)**가 안정성의 핵심이다. 수정 레버는 중첩 가능: 언더드릴링/골밀도화 (Osseodensi

- `watanabe-toothpick-method-toothbrushing-synthesis` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: The **Watanabe toothpick method (TPM, 이쑤시개법)** is a manual toothbrushing technique using a **double-row (2-row) toothbrush** whose bristle tips are pressed into the interdental embrasures in a toothpick-like motion. This page synthesizes the 7 papers the wiki holds, spanning the method's **origin (1998)** to its most recent **peri-implant application (2025)**, plus the **naming-confusion counterpo
  - ▸ 출발(`watanabe-toothpick-method-toothbrushing-synthesis`) 세줄: Watanabe 이쑤시개법(TPM, 칫솔질) 7편(1995–2026) 종합: 2열모 칫솔 치간 삽입 기법으로 인접면 플라그 제거 + 치은 치유 자극(기저세포 증식 ~2.5배)의 이중 기전; 원전 RCT(Morita 1998)는 TPM > Bass on proximal plaque; 당뇨 치주염서 SRP+TPM이 BOP −16.5% vs SRP 단독 −7.3%·혈청 내독소 유일 감소(Lee 2020 RCT); 임플란트 주위 점막염에서 약제 전달 도구로 유효하나 기계적 단독(식염수-TPM)은 12균종

- `watanabe-toothpick-method-toothbrushing-synthesis` [overviews] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[interdental-cleaning/el-haddad-2026-toothpick-use-interdental-papilla-loss-cross-sectional]] — wooden-toothpick harm (papilla loss) — naming counterpoint
  - ▸ 출발(`watanabe-toothpick-method-toothbrushing-synthesis`) 세줄: Watanabe 이쑤시개법(TPM, 칫솔질) 7편(1995–2026) 종합: 2열모 칫솔 치간 삽입 기법으로 인접면 플라그 제거 + 치은 치유 자극(기저세포 증식 ~2.5배)의 이중 기전; 원전 RCT(Morita 1998)는 TPM > Bass on proximal plaque; 당뇨 치주염서 SRP+TPM이 BOP −16.5% vs SRP 단독 −7.3%·혈청 내독소 유일 감소(Lee 2020 RCT); 임플란트 주위 점막염에서 약제 전달 도구로 유효하나 기계적 단독(식염수-TPM)은 12균종

- `dbbm-bone-substitute-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Clinicians reading PRF studies should discriminate: (a) solid PRF vs liquid PRF (i-PRF) — different growth factor concentrations; (b) L-PRF centrifugation protocol (Dohan high-speed vs Choukroun protocols) — different fibrin architecture; (c) A-PRF low-speed (2700 rpm) — different platelet/cell distribution; (d) PRF mixed into graft vs used as membrane layer; (e) crucially, generation/class — firs
  - ▸ 출발(`dbbm-bone-substitute-overview`) 세줄: 14편(동물·전향·RCT·SR·SR+MA) 종합: DBBM의 느린 흡수는 부피를 보존하지만 초기 신생골 형성을 역설적으로 억제할 수 있음(DBBM 단독 < 무이식 대조군 4주, p=0.025, Fujioka-Kobayashi 2022); BCP는 토끼 모델서 신생골 +70%(Chakar 2014), 임상 상악동 SR+MA서 +3.48% 신생골·−8.41% 잔존(Alkandari 2025)으로 일관되게 DBBM 초과; DBBM 입자 크기(대 1–2mm vs 소 0.25–1mm)는 상악동거상 조직학 

- `unopposed-tooth-overeruption-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - [[occlusion/kiliaridis-2000-vertical-position-rotation-tipping-molars]] — Kiliaridis 2000, cross-sectional (n=53, 84 molars unopposed ≥10 y): **~18% show no overeruption at all**, ~49–58% slight (<2 mm), ~20–24% moderate-to-severe (≥2 mm) — directly refutes "every unopposed tooth over-erupts."
  - ▸ 출발(`unopposed-tooth-overeruption-overview`) 세줄: 11편 종합: 대합치 없는 후방 치아의 ~83%가 정출(~9개월 평균 0.43 mm / 최대 0.75 mm, ~72%는 1 mm 미만, 초기 최대 속도, 수직+협측경사+회전의 3D 운동); ~18%는 전혀 안 움직임; 정출은 PDL·치조골 매개라 치수 생활력 무관 — 엔도치 vs 생활치 차이 근거 없음. 고정 retention도 부분접촉 대비 효과 없어(둘 다 ~0.1 mm; Livas 2016) 저위험치는 모니터링이 방어 가능한 기본값; 젊은 나이·상악·완전무대합·치주염·발치 직후가 12년 ≥2

- `implant-spacing-proximity-crestal-bone-overview` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: | Implant ↔ implant (modern designs) | ~2 mm acceptable; 1 mm maintainable in select cases | Morales Schwarz 2025 (n=1) + 2 animal studies | Internal conical + platform-switching + concave abutment + subcrestal placement defend the gap; n=1 → does not overturn ≥3 mm |
  - ▸ 출발(`implant-spacing-proximity-crestal-bone-overview`) 세줄: 4편 종합: 치간 치조정골소실은 수직 깊이가 아닌 수평 간격이 지배 — 각 임플란트에서 측방 골소실 ~1.4 mm 발생, 임플란트간 거리(IID) <3 mm 시 >3 mm 대비 2.3배 치조정 골소실(Tarnow 2000); 현대 내부 원추형+플랫폼 스위칭 디자인은 1–2 mm 간격 방어 가능(Morales Schwarz 2025, n=1+동물 2편)이나 근거 무게는 여전히 ≥3 mm 권장 지지. 임플란트-인접치 위험은 비대칭: 임플란트 생존율 >95% 불변이나, 접촉 케이스서 **인접치** 치수

- `implant-spacing-proximity-crestal-bone-overview` [overviews] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: - [[implants/morales-schwarz-2025-1mm-interimplant-distance-10year-case]] — 10-year case report (n=1) + literature/animal review showing a 1 mm IID maintainable with modern implant design; provides the "exception" that qualifies — but does not overturn — Tarnow's rule.
  - ▸ 출발(`implant-spacing-proximity-crestal-bone-overview`) 세줄: 4편 종합: 치간 치조정골소실은 수직 깊이가 아닌 수평 간격이 지배 — 각 임플란트에서 측방 골소실 ~1.4 mm 발생, 임플란트간 거리(IID) <3 mm 시 >3 mm 대비 2.3배 치조정 골소실(Tarnow 2000); 현대 내부 원추형+플랫폼 스위칭 디자인은 1–2 mm 간격 방어 가능(Morales Schwarz 2025, n=1+동물 2편)이나 근거 무게는 여전히 ≥3 mm 권장 지지. 임플란트-인접치 위험은 비대칭: 임플란트 생존율 >95% 불변이나, 접촉 케이스서 **인접치** 치수

- `ceraseal-bioceramic-sealer-clinical-material-synthesis` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **재근관치료 제거성**: Shim 2025 (in-vitro, micro-CT) — 세라실 92.5%·AH Plus Bioceramic 94.8% > 에폭시 AH Plus Jet 87.1% 제거(WaveOne Gold + XP-endo Finisher). **"생광화 실러는 못 뺀다"는 우려를 반박** — 오히려 더 잘 빠짐, 단 XPF로 apical 보강 필요.
  - ▸ 출발(`ceraseal-bioceramic-sealer-clinical-material-synthesis`) 세줄: 세라실(Ceraseal, 프리믹스 칼슘실리케이트 생체세라믹 실러) 임상 4편(전향 코호트 2 + RCT 2) + 벤치 10편 종합: 24–36개월 치유 ~91–92%·생존 ~93–98%이 AH Plus gold standard와 동등; Elmsmari 2025 SR+MA(RCT 3편, n=259)에서 6/12/18개월 모두 통계적 유의차 없음(OR 1.12–2.09, p>0.05) — 단 GRADE 근거 낮음. AH Plus 대비 이점: 술후통증 ↓(Abada 2025 RCT, p<0.001); 

- `ceraseal-bioceramic-sealer-clinical-material-synthesis` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: **The bench data explain why and add three practical reassurances.** (1) *Retrievability* — Shim 2025 refutes the fear that biomineralizing CSBSs can't be removed: Ceraseal was 92.5% retrievable vs 87.1% for epoxy AH Plus Jet (with XP-endo Finisher adding apical removal). (2) *Bioactivity* — Maharti 2024 shows Ceraseal deposits more interfacial apatite and sustains higher pH than AH Plus Biocerami
  - ▸ 출발(`ceraseal-bioceramic-sealer-clinical-material-synthesis`) 세줄: 세라실(Ceraseal, 프리믹스 칼슘실리케이트 생체세라믹 실러) 임상 4편(전향 코호트 2 + RCT 2) + 벤치 10편 종합: 24–36개월 치유 ~91–92%·생존 ~93–98%이 AH Plus gold standard와 동등; Elmsmari 2025 SR+MA(RCT 3편, n=259)에서 6/12/18개월 모두 통계적 유의차 없음(OR 1.12–2.09, p>0.05) — 단 GRADE 근거 낮음. AH Plus 대비 이점: 술후통증 ↓(Abada 2025 RCT, p<0.001); 

- `single-vs-multivisit-endodontic-outcomes-overview` [overviews] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: > - nuance 2 — 상반된 치유 우위: Rossi-Fedele 2023 SR+MA가 단일내원 소폭 치유 우위(RR 1.10) 보고 → 즉시 충전이 내원간 재오염을 약간 줄일 가능성, 작은 효과로 "최소한 비열등, 가능하면 소폭 우위"로 해석.
  - ▸ 출발(`single-vs-multivisit-endodontic-outcomes-overview`) 세줄: 5편 종합 (Cochrane SR+MA 47 RCT, SR+MA+TSA 29 RCT, RCT 3편 — 1차성 근단치주염·술후 통증·재치료) — 단일내원 vs 다회내원 근관치료 결과 비교. 모든 5편이 수렴: 방사선학적 치유(Mergoni 2022 RR 0.93, 중등도 확실성), 장기 합병증(Schwendicke 2017 RR 1.00), 술후 통증에서 임상적으로 유의한 차이 없음 — 1차성 근단치주염(Bobba 2026 93.3% vs 86.7%, p>0.05)·재치료(Karaoğlan 2022

- `osteotomy-drilling-heat-determinants-irrigation-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **통념 반박 — 순차 드릴링(sequential drilling)은 자동 안전장치가 아니다**: 무관주 조건에서 pilot drill이 >100°C, 열손상대가 측방 10mm까지, 후속 확대드릴은 열을 제거가 아니라 추가(Rugova). 단 이는 관주 없는 합성골 극단 조건.
  - ▸ 출발(`osteotomy-drilling-heat-determinants-irrigation-overview`) 세줄: 임플란트 골절제 드릴링 발열 16편을 "요인 나열"이 아니라 **무엇을 실제로 통제할지의 근거가중 순위**로 재구성: 47°C/1분 괴사 역치(Timon 2019 교차검증; 정형외과 ~50°C), 다인자 프레이밍(Chauhan 2018 SR 34편; Jung 2021 내부·외부 인자 분류), 생물학적 endpoint(Heuzeroth 2021 in vivo 미니피그 n=36). 여러 결정인자를 맞대결시킨 연구에서 **관주 온도가 가장 재현성 높은 지렛대** — 4개 요인 동시비교에서 유일하게 유의

- `osteotomy-drilling-heat-determinants-irrigation-overview` [overviews] (HIGH-far→saxena-2024-guided-implant-drilling-bone-temperature, 'overturn' · 결론 뒤집음)
  - **근거 문장**: **Tier 3 — situational amplifiers.** Guided surgery: Markovic localizes the guide penalty to the *cortical entrance only* (entrance p<0.001; middle/bottom NS), driven by sleeve obstruction of irrigation plus conductive heating from the metal sleeve itself (guide-temp ↔ bone-temp Spearman rho=0.868); Saxena's SR ([[implants/saxena-2024-guided-implant-drilling-bone-temperature]]) confirms guided > n
  - ▸ 출발(`osteotomy-drilling-heat-determinants-irrigation-overview`) 세줄: 임플란트 골절제 드릴링 발열 16편을 "요인 나열"이 아니라 **무엇을 실제로 통제할지의 근거가중 순위**로 재구성: 47°C/1분 괴사 역치(Timon 2019 교차검증; 정형외과 ~50°C), 다인자 프레이밍(Chauhan 2018 SR 34편; Jung 2021 내부·외부 인자 분류), 생물학적 endpoint(Heuzeroth 2021 in vivo 미니피그 n=36). 여러 결정인자를 맞대결시킨 연구에서 **관주 온도가 가장 재현성 높은 지렛대** — 4개 요인 동시비교에서 유일하게 유의

- `tmd-management-evidence-ladder` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - [[tmj/valenzuela-fuenzalida-2026-arthrocentesis-vs-other-modalities-tmd-sr-ma]] — 비교군 확장 시 관절천자 우월성 없음; 기존 IJOMS 2023(+1.12mm)의 modest-benefit 결론을 재맥락화(축 5 갱신·일부 반박).
  - ▸ 출발(`tmd-management-evidence-ladder`) 세줄: TMD 34편(SR+MA·가이드라인 27 + 편측저작·과두·이명 5 + TMJ OA 운동 전향 1 + MPS NMA 1)을 역학·비약물 보존·약물·만성통증 NMA·관절천자·이갈이·BTX·OA·QoL/VD·편측저작 10축으로 정리. 최고 근거 치료(Yao 2023 BMJ NMA, 233 RCT): CBT+운동·하악 가동화(RD 36%)·수기 트리거포인트(32%); 교합 중재 미지지(Cochrane 2024 Singh); 약물 낮은 근거; 관절천자 단독 우월성 미입증(Valenzuela-Fuenzal

- `ridge-split-expansion-technique-selection-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: López-Valverde 2025 pools expansion + compaction + densification together for the narrow (≤2.5 mm) crest and finds all three favour the experimental group for **bone density** (SMD −0.71, p=0.002, homogeneous/trustworthy), **crestal expansion** (SMD −1.12, p=0.04, but I²≥75%), and **ISQ** (SMD −8.88, p=0.0005, but I²=96%) — with the honest caveat that only the bone-density signal is solid; CE and 
  - ▸ 출발(`ridge-split-expansion-technique-selection-overview`) 세줄: 10개 위키 페이지 종합 — 치조제 분할·확장술(Alveolar Ridge Split, ARS/RS)은 공여부 없이 폭 +3.3–3.7 mm·생존율 ~98–99%를 신뢰성 있게 달성하며(Lin 2023 SR+MA), 대안 대비 골증대량 서열은 골유도재생술(GBR) 4.04 > 치조제 분할술(RS) 3.66 > 골밀도화(OD) 2.15 mm이나(Vorovenci 2024, P=0.002) 생존율은 세 술식 모두 ~99%로 동등하다. 술식 선택 기준: 시작 골폭(가장 좁으면 RS, 저밀도골 D3–D4

- `supportive-peri-implant-therapy-maintenance-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: There is **no genuine contradiction across the four** — all four point the same way (individualized maintenance reduces peri-implant disease). The real tension is **strength of evidence vs strength of recommendation**:
  - ▸ 출발(`supportive-peri-implant-therapy-maintenance-overview`) 세줄: 4편 종합(SR 2편, 내러티브/임상 2편) — Mojaver 2025(25편 SR: RCT 9+코호트 13+증례대조 3), Lanzetti 2024(full-arch 11편), Ramseier 2024(883명/11,842회 SPT 방문), Barclay 2026(임상 framing). 위험도 기반 지지 임플란트주위 치료(Supportive Peri-Implant Therapy, SPiT)는 고정주기·무관리 대비 우월: 탐침깊이(PD) −1.0–1.5 mm, 탐침시출혈(BoP) −10–25%p,

- `zirconia-implant-clinical-outcomes` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Why this creates tension with the Thesis above**: Shetty 2026 pools older, heterogeneous SRs (through March 2023) without stratifying by implant design (one-piece vs two-piece) or coronal fabrication method (drill-prepared vs factory-finished) — precisely the two levers Mohseni 2024 identifies as the actual drivers of zirconia failure. Shetty's material-level "Ti > Zr" signal is therefore best r
  - ▸ 출발(`zirconia-implant-clinical-outcomes`) 세줄: 3편 종합(SR+MA 1·SR 2): 지르코니아 임플란트는 중장기 생존율 높음(Mohseni 2024 SR+MA, 25편/4,017개: 10년 누적 95.1%; MBL ~0.005 mm/월), 환자보고결과(PROMs)에서 심미·편안함·저작 유의 향상(Arefnia 2025 SR, 12편), 티타늄과 동등 수준. 잔여 실패 신호는 4가지 수정 가능한 설계·시공 레버에 집중: 2-piece 설계(p=0.017), 협폭경(파절), 의자측 드릴 가공 관상부(p<0.001), 단종·초기세대 제품 — 세라믹

- `zirconia-implant-clinical-outcomes` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/shetty-2026-titanium-vs-zirconia-implants-umbrella]] — umbrella review (SR 6편, 2014–2023): direct Ti-vs-Zr comparison, survival/success favor Ti but not design-stratified — contradicts Mohseni 2024's design-controlled equivalence finding
  - ▸ 출발(`zirconia-implant-clinical-outcomes`) 세줄: 3편 종합(SR+MA 1·SR 2): 지르코니아 임플란트는 중장기 생존율 높음(Mohseni 2024 SR+MA, 25편/4,017개: 10년 누적 95.1%; MBL ~0.005 mm/월), 환자보고결과(PROMs)에서 심미·편안함·저작 유의 향상(Arefnia 2025 SR, 12편), 티타늄과 동등 수준. 잔여 실패 신호는 4가지 수정 가능한 설계·시공 레버에 집중: 2-piece 설계(p=0.017), 협폭경(파절), 의자측 드릴 가공 관상부(p<0.001), 단종·초기세대 제품 — 세라믹

- `vitamin-d-osseointegration-implant-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Vitamin D is biologically tied to bone metabolism (calcium homeostasis, osteoblast differentiation, immunomodulation), so a pro-osseointegration role is mechanistically plausible. The wiki holds 8 papers spanning the full evidence ladder, and they do **not** all agree. This page resolves the apparent contradiction.
  - ▸ 출발(`vitamin-d-osseointegration-implant-overview`) 세줄: 비타민 D[25(OH)D]와 임플란트 골유착(Osseointegration) 8편(우산형 1·SR 3·RCT 1·전향 2·후향 1) 종합 — 기전/동물·SR/MA·사람 임상 근거 사다리 전반; Tallon 2024 우산형 고찰은 메타분석 부재·기준치·용량·결과지표 불일치를 명시. 동물·기전 근거는 일관되게 양성; 사람 근거는 결핍 중증도에 따라 갈림 — 양성 신호가 중증 결핍(<10~20 ng/mL)+동반위험에 몰림(Mohsen 2024: 실패율 <10 ng/mL 46.2% vs >30 ng/mL

- `vitamin-d-osseointegration-implant-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/vitamin-d/francis-2024-low-serum-vitamin-d-early-implant-failure]] — the key null/contradicting cohort (replete population)
  - ▸ 출발(`vitamin-d-osseointegration-implant-overview`) 세줄: 비타민 D[25(OH)D]와 임플란트 골유착(Osseointegration) 8편(우산형 1·SR 3·RCT 1·전향 2·후향 1) 종합 — 기전/동물·SR/MA·사람 임상 근거 사다리 전반; Tallon 2024 우산형 고찰은 메타분석 부재·기준치·용량·결과지표 불일치를 명시. 동물·기전 근거는 일관되게 양성; 사람 근거는 결핍 중증도에 따라 갈림 — 양성 신호가 중증 결핍(<10~20 ng/mL)+동반위험에 몰림(Mohsen 2024: 실패율 <10 ng/mL 46.2% vs >30 ng/mL

- `flapless-vs-flapped-implant-surgery-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **발치 단독 차원에서는 flapless가 능사 아님**: Araujo 2009(개 5마리 split-mouth)는 flapless 발치도 피판 발치와 동등한 치조제 흡수 — "flapless = 치조제 보존"이라는 통념 반박. [확인]
  - ▸ 출발(`flapless-vs-flapped-implant-surgery-overview`) 세줄: 무피판 vs 피판 임플란트 수술 6편을 3축(실패율·치조정골·통증/연조직)으로 종합 — 결과 변수별로 우열이 갈린다: 실패율 우려(RR 1.75)는 저질 연구 의존이라 약하고, 치조정골은 RCT(flapless 6개월 ~40% 덜 소실)와 12개월 코호트(차이없음)가 충돌한다. 술후 통증은 flapless가 일관 절반(VAS day 3: 3.1 vs 5.7)이고 단기 연조직도 유리하며, 즉시식립 맥락에서는 협측 조직 보존에 경향적 우위지만 효과는 작고 술자 의존적이다. 무피판 발치 단독은 치조제를

- `flapless-vs-flapped-implant-surgery-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Axis 2 — Crestal/marginal bone (the live controversy).** Two 2025 papers in healed posterior ridges reach opposite conclusions. Surendra 2025 (RCT, n=40, posterior mandible) found flapless preserved significantly more crestal bone at both 3 months (0.32 vs 0.56 mm) and 6 months (0.48 vs 0.82 mm, both p<0.001) — roughly 40% less loss — with 100% survival in both arms, attributing the advantage to
  - ▸ 출발(`flapless-vs-flapped-implant-surgery-overview`) 세줄: 무피판 vs 피판 임플란트 수술 6편을 3축(실패율·치조정골·통증/연조직)으로 종합 — 결과 변수별로 우열이 갈린다: 실패율 우려(RR 1.75)는 저질 연구 의존이라 약하고, 치조정골은 RCT(flapless 6개월 ~40% 덜 소실)와 12개월 코호트(차이없음)가 충돌한다. 술후 통증은 flapless가 일관 절반(VAS day 3: 3.1 vs 5.7)이고 단기 연조직도 유리하며, 즉시식립 맥락에서는 협측 조직 보존에 경향적 우위지만 효과는 작고 술자 의존적이다. 무피판 발치 단독은 치조제를

- `flapless-vs-flapped-implant-surgery-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: **A foundational caution.** Araujo 2009 (5-dog split-mouth histology) showed flapless extraction produced ridge resorption equivalent to flapped extraction, refuting the notion that avoiding a flap by itself preserves the ridge. Flapless preserves *periosteal vascularity around an implant*, not the post-extraction ridge dimension per se.
  - ▸ 출발(`flapless-vs-flapped-implant-surgery-overview`) 세줄: 무피판 vs 피판 임플란트 수술 6편을 3축(실패율·치조정골·통증/연조직)으로 종합 — 결과 변수별로 우열이 갈린다: 실패율 우려(RR 1.75)는 저질 연구 의존이라 약하고, 치조정골은 RCT(flapless 6개월 ~40% 덜 소실)와 12개월 코호트(차이없음)가 충돌한다. 술후 통증은 flapless가 일관 절반(VAS day 3: 3.1 vs 5.7)이고 단기 연조직도 유리하며, 즉시식립 맥락에서는 협측 조직 보존에 경향적 우위지만 효과는 작고 술자 의존적이다. 무피판 발치 단독은 치조제를

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - SR 충돌 상세: 임상 SR(Senna 2012·Silva 2013)=연관 약함/불가 vs abfraction SR(Duangthip 2017)=81% 연관(단 lab/FEA 가중·응력단독 원인 임상입증 전무) vs scoping review(Dioguardi 2024, 6편)=확정·반박 모두 불가. SEM은 microfracture 일부 관찰(Worawongvasu).
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 16편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Synthesis of 16 papers on noncarious cervical lesions (NCCL) — etiology, diagnosis, and monitor-vs-restore decision: NCCLs are multifactorial (stress/abfraction + friction/abrasion + biocorrosion/erosion as a case-specific combination), the "abfraction as sole cause" hypothesis is clinically unproven with SR evidence directly contradicting across three systematic reviews (Senna 2012 — association 
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 16편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 16편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 불가).
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 16편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "교합응력→abfraction"이 모든 NCCL의 주원인이라는 강한 주장은 임상적으로 미입증이다. SR 근거가 정면으로 갈린다: 임상연구 SR(Senna 2012·Silva 2013)은 연관 약함/결론불가, abfraction 키워드 SR(Duangthip 2017)은 81% 연관(단 lab/FEA 가중·응력단독 원인 임상입증 전무), 최신 PRISMA-ScR scoping(Dioguardi 2024)은 6편만으로 확정·반박 모두 불가로 정리. 초미세구조(SEM)에선 microfracture 증거 일부 관찰. **종합: lab은 응력집중을 보이나 in-vivo 인과는 미입증.** [확인 — SR 충돌]
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 16편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: | [[nccl/dioguardi-2024-abfraction-theory-controversy-scoping-review]] | Scoping review (PRISMA-ScR) | 6편 | 교합부하의 abfraction 역할 확정·반박 모두 불가; Duangthip 재비판 | sr |
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 16편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - Abfraction 기전 — SR-level 충돌이 미해결의 핵심: 임상 SR(Senna 2012·Silva 2013)=연관 약함/불가 vs abfraction SR(Duangthip 2017)=81% 연관(lab 가중) vs scoping(Dioguardi 2024)=6편으로 확정·반박 불가. SEM microfracture(Worawongvasu)와 임상 음성 연관이 상충. Dioguardi 2024가 제시한 해법 = 침식/마모를 분리한 전향적 종단연구.
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 16편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `implant-macrogeometry-length-diameter-primary-stability-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **임상 vs FEA 충돌**: FEA는 갈린다 — Singh 2024는 저밀도(D4) 골에서 10mm 긴 임플란트가 계면 응력을 크게 낮춤(step design 188→35 MPa)을 보이나, Kavitha 2023은 one-piece 즉시부하 모델에서 12mm가 오히려 경부 응력을 소폭 증가시킴을 보임. 길이–응력 관계는 **디자인·골밀도·길이 범위에 따라 방향이 뒤집힌다.**
  - ▸ 출발(`implant-macrogeometry-length-diameter-primary-stability-overview`) 세줄: 임플란트 직경 vs 길이가 1차 안정성/ISQ를 좌우하는지 종합한 8편(임상 RFA 4 + 체외/FEA 4): 이를 검증한 모든 임상연구에서 **직경이 유의한 결정인자(좁을수록 나쁨), 길이는 반복적으로 무의**이거나 연질골에서만 유의 — Gómez-Polo 2016(n=88) IT 26.5→33.8 N/cm(3.75→4.25mm, p=.002); Huang 2016(n=329) 직경이 2차 ISQ 최강 예측인자(β=0.414); Quesada-García 2012(n=235) 좁은 직경→12주 

- `implant-macrogeometry-length-diameter-primary-stability-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 임상의 "직경 우세·길이 미미" 패턴은 FEA와 충돌하며 FEA끼리도 갈림 — Singh 2024는 D4골에서 10mm가 응력을 크게 낮추나(188→35 MPa) Kavitha 2023은 12mm가 경부 응력을 소폭 증가시킴; 길이–응력 관계는 디자인·골밀도에 따라 방향이 뒤집힘. de-Elío 2023은 겉보기 macro-design/IT 차이가 드릴 직경 artifact일 수 있고 Osstell·Penguin RFA 값은 호환 불가(P<.001)임을 경고.
  - ▸ 출발(`implant-macrogeometry-length-diameter-primary-stability-overview`) 세줄: 임플란트 직경 vs 길이가 1차 안정성/ISQ를 좌우하는지 종합한 8편(임상 RFA 4 + 체외/FEA 4): 이를 검증한 모든 임상연구에서 **직경이 유의한 결정인자(좁을수록 나쁨), 길이는 반복적으로 무의**이거나 연질골에서만 유의 — Gómez-Polo 2016(n=88) IT 26.5→33.8 N/cm(3.75→4.25mm, p=.002); Huang 2016(n=329) 직경이 2차 ISQ 최강 예측인자(β=0.414); Quesada-García 2012(n=235) 좁은 직경→12주 

- `implant-failure-mbl-risk-factors-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Loading-protocol timing ([[implants/rismanchian-2025-immediate-nonimmediate-loading-umbrella-review]]) and anatomic-avoidance strategy (zygomatic implants, [[implants/dambrosio-2026-clinical-risk-medico-legal-implications]]) round out the picture. Immediate vs nonimmediate loading of single implants shows no significant survival or MBL difference given adequate primary stability — though this narr
  - ▸ 출발(`implant-failure-mbl-risk-factors-overview`) 세줄: 후기(정착 후) 임플란트 실패·변연골소실(MBL) 관련 논문 10편 종합 — 로딩 전 조기실패는 [[overviews/early-implant-failure-risk-prevention-overview]]와 상호보완. 가장 광범위한 우산리뷰(giok-2026, 메타분석 25편/35개 연관성)는 "확증" 등급 연관성이 전무함을 보이고, 흡연이 유일한 관찰근거 최고등급이며, 이갈이(barboza-2026, OR 4.68)·방사선치료(pacheco-2025, 조사골 81.52% vs 비조사골 94.64

- `topical-anesthetic-injection-pain-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 중심 긴장점: 명제3·4의 상충 — blinding·검정력이 강해질수록 제제 간 차이가 사라지는 패턴은 관찰된 "우위"가 상당 부분 측정·기대 편향일 가능성을 시사. [미검증]
  - ▸ 출발(`topical-anesthetic-injection-pain-overview`) 세줄: 4편 종합: 표면마취제는 위약 대비 needle·주사 통증을 확실히 줄이나(농도 의존, 20%>5%; Khongkhunthian 2018) SRP에서 통증강도는 주사마취가 우위(Wambier 2017 SR+MA), 제제 간 비교는 비일관적 — 소규모 RCT(Subramanian 2023)는 benzocaine 우위, 더 엄격한 triple-blind RCT(Karkoutly 2024)는 차이 없음. 엄격한 blinding이 제제 간 차이를 없애는 패턴은 관찰된 "우위"가 상당 부분 측정·기대 편향

- `topical-anesthetic-injection-pain-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: → 명제 3·4의 **상충**은 이 overview의 중심 긴장점이다. blinding·검정력이 강해질수록 제제 간 차이가 사라지는 패턴은, 관찰된 "우위"가 상당 부분 측정·기대 편향일 수 있음을 시사한다. [미검증]
  - ▸ 출발(`topical-anesthetic-injection-pain-overview`) 세줄: 4편 종합: 표면마취제는 위약 대비 needle·주사 통증을 확실히 줄이나(농도 의존, 20%>5%; Khongkhunthian 2018) SRP에서 통증강도는 주사마취가 우위(Wambier 2017 SR+MA), 제제 간 비교는 비일관적 — 소규모 RCT(Subramanian 2023)는 benzocaine 우위, 더 엄격한 triple-blind RCT(Karkoutly 2024)는 차이 없음. 엄격한 blinding이 제제 간 차이를 없애는 패턴은 관찰된 "우위"가 상당 부분 측정·기대 편향

- `topical-anesthetic-injection-pain-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: - [[local-anesthesia/karkoutly-2024-topical-anesthetics-lidocaine-benzocaine-emla-ianb]] — 제제 비교 (차이 없음, 상충점)
  - ▸ 출발(`topical-anesthetic-injection-pain-overview`) 세줄: 4편 종합: 표면마취제는 위약 대비 needle·주사 통증을 확실히 줄이나(농도 의존, 20%>5%; Khongkhunthian 2018) SRP에서 통증강도는 주사마취가 우위(Wambier 2017 SR+MA), 제제 간 비교는 비일관적 — 소규모 RCT(Subramanian 2023)는 benzocaine 우위, 더 엄격한 triple-blind RCT(Karkoutly 2024)는 차이 없음. 엄격한 blinding이 제제 간 차이를 없애는 패턴은 관찰된 "우위"가 상당 부분 측정·기대 편향

- `kumar-2022-suture-versus-sutureless-third-molar-impactions` [suture-wound-closure] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 소형 피판 설계와 무봉합 병용 시 초기 불편감 이점을 제공하나 단일기관 소규모 연구로 대규모 다기관 RCT(Takadoum)의 차이 없음 결과와 상충하는 점 주의.
  - ▸ 출발(`kumar-2022-suture-versus-sutureless-third-molar-impactions`) 세줄: 작은 변형 Szmyd V자형 판막을 사용한 하악 매복 사랑니 발치에서 봉합 대 무봉합을 비교한 RCT(n=50, 군당 25명), 24h·48h·5·7일·2주 추적. 무봉합군이 초기 통증·부종·개구장애 유의하게 감소(p<0.001); 출혈·치주 후유증·건성발치와 차이 없음. 소형 피판 설계와 무봉합 병용 시 초기 불편감 이점을 제공하나 단일기관 소규모 연구로 대규모 다기관 RCT(Takadoum)의 차이 없음 결과와 상충하는 점 주의.

- `pachipulusu-2018-primary-secondary-closure-third-molar` [suture-wound-closure] (SOFT→takadoum-2022-sutureless-socket-technique-third-molars, 'whereas' · 반면(대조))
  - **근거 문장**: - [[suture-wound-closure/takadoum-2022-sutureless-socket-technique-third-molars]] — contrasts: Takadoum's larger multicentric RCT found no pain/swelling difference, whereas this trial does favor the open (secondary) approach.
  - ▸ 출발(`pachipulusu-2018-primary-secondary-closure-third-molar`) 세줄: 하악 매복 사랑니 발치 후 1차 폐쇄(완전 봉합) 대 2차 폐쇄(배수창 개방)를 비교한 RCT(n=60, 군당 30명); 1주간 통증·부종·개구장애 및 6개월 치주 치유 추적. 2차 폐쇄군이 통증·부종 유의하게 적고 개구량 더 컸으며(p<0.05), 6개월 치주 치유는 차이 없음; 건성발치와 1명(3.3%). 소켓 일부 개방이 조기 이환율을 줄이면서 인접 제2대구치의 6개월 치주 치유에 영향 없음 — 봉합·무봉합 사랑니 발치 연구군의 공통 결론과 일치.
  - ▸ 대상(`takadoum-2022-sutureless-socket-technique-third-molars`) 세줄: 전신마취 하 4개 매복 사랑니 전 발치에서 봉합 대 무봉합을 Day 31까지 추적한 CONSORT 준수 다기관 공개 RCT(프랑스 3개 병원, 분석 n=94: 봉합 44, 무봉합 50). 3일째 통증(p=0.904) 및 모든 2차 결과(부종·개구장애·진통제·치유·합병증·삶의 질)에서 차이 없음; 무봉합이 수술시간 단축; 흡연이 합병증 위험 3.65배 증가(p=0.0244). 이 다기관 충분 검정력 RCT는 무봉합 폐쇄의 비열등성을 확립하며, 무봉합 이점을 보고한 단일기관 연구를 해석하는 동등성 기

- `sen-2024-sutureless-multiple-suture-third-molar-inflammation` [suture-wound-closure] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 무봉합 폐쇄는 중등도 난이도 사랑니 발치에서 개구장애를 줄이는 비열등 옵션이나, 이 단일기관 최대 규모 연구 결과는 다기관 Takadoum 결과(차이 없음)와 상충.
  - ▸ 출발(`sen-2024-sutureless-multiple-suture-third-molar-inflammation`) 세줄: 하악 매복 사랑니(Pederson 5–7) 발치 후 비단 봉합 1차 폐쇄 대 무봉합을 1:1 비교한 전향적 RCT(n=101); 염증 3징후·설신경 감각·합병증 평가. 통증·부종·설신경 기능은 두 군 동등; 무봉합군에서 개구장애 유의하게 감소, 지연 창상 치유 사례도 더 적음. 무봉합 폐쇄는 중등도 난이도 사랑니 발치에서 개구장애를 줄이는 비열등 옵션이나, 이 단일기관 최대 규모 연구 결과는 다기관 Takadoum 결과(차이 없음)와 상충.

- `de-oliveira-2024-otc-bleaching-color-adverse-effects` [tooth-whitening] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This NMA covers the consumer/unsupervised whitening route — strips, paint-on gels, prefilled trays — which is the most common entry point patients ask about. The headline: low-concentration OTC products do produce real short-term lightening over placebo and are generally well tolerated (minimal sensitivity, minimal gingival irritation), with longer daily wear time being the key driver of effect. F
  - ▸ 출발(`de-oliveira-2024-otc-bleaching-color-adverse-effects`) 세줄: SR + 빈도주의 NMA (정성 37편, 메타 10편, n=1,932; GRADE 낮음) — 비감독 소비자 미백(스트립·페인트·충전 트레이) 포맷 비교. ΔEab*(기기측정)은 6% HP 스트립(≥14h), ΔSGU(시각 색조단위)는 10% CP 자가(≥14h)가 최고; 모든 프로토콜에서 치아 민감도·치은 자극은 위약과 거의 차이 없음. 저농도 OTC 제품은 단기적으로 실제 미백 효과가 있고 내약성 우수하나, 단기·저근거 결과이므로 임상적 감독 없는 미백의 한계(병변 미발견, 비현실적 기대)를 상

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Four long-term studies (5–6 years) were too heterogeneous to pool and reported contradictory results by technique, so surface modification cannot yet be recommended as a reliable lever on peri-implant soft-tissue health.
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 세줄: SR+MA (10편 검토, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 (Healing Abutment) 표면 처리가 임플란트주위 연조직에 미치는 영향 평가. 단기 결과: 플라크 지수 (P=0.091)·탐침 시 출혈 (Bleeding on Probing, BoP, P=0.099)·탐침 깊이 (Probing Depth, PD, P=0.488) 모두 대조군과 유의한 차이 없음. 장기 (5–6년) 4편은 이질성 과다로 풀링 불가·기법에 따라 상반된 

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: 장기 (5–6년) 4편은 이질성 과다로 풀링 불가·기법에 따라 상반된 결과 — 표면 처리 단독으로 임플란트주위 조직 건강을 개선하기 어려움.
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 세줄: SR+MA (10편 검토, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 (Healing Abutment) 표면 처리가 임플란트주위 연조직에 미치는 영향 평가. 단기 결과: 플라크 지수 (P=0.091)·탐침 시 출혈 (Bleeding on Probing, BoP, P=0.099)·탐침 깊이 (Probing Depth, PD, P=0.488) 모두 대조군과 유의한 차이 없음. 장기 (5–6년) 4편은 이질성 과다로 풀링 불가·기법에 따라 상반된 

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: According to PubMed ([DOI 10.1007/s00784-020-03210-x](https://doi.org/10.1007/s00784-020-03210-x)), this systematic review with meta-analysis (abstract-only — full text not retrieved) evaluated whether **titanium healing-abutment surface modifications** (machined vs anodized/laser/other treatments) affect peri-implant soft-tissue healing, inflammation, and maintenance. A database search through 30
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 세줄: SR+MA (10편 검토, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 (Healing Abutment) 표면 처리가 임플란트주위 연조직에 미치는 영향 평가. 단기 결과: 플라크 지수 (P=0.091)·탐침 시 출혈 (Bleeding on Probing, BoP, P=0.099)·탐침 깊이 (Probing Depth, PD, P=0.488) 모두 대조군과 유의한 차이 없음. 장기 (5–6년) 4편은 이질성 과다로 풀링 불가·기법에 따라 상반된 

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Documents that long-term (5–6 y) evidence is contradictory and technique-dependent — a caution flag rather than a green light.
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 세줄: SR+MA (10편 검토, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 (Healing Abutment) 표면 처리가 임플란트주위 연조직에 미치는 영향 평가. 단기 결과: 플라크 지수 (P=0.091)·탐침 시 출혈 (Bleeding on Probing, BoP, P=0.099)·탐침 깊이 (Probing Depth, PD, P=0.488) 모두 대조군과 유의한 차이 없음. 장기 (5–6년) 4편은 이질성 과다로 풀링 불가·기법에 따라 상반된 

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **4 studies** with 5–6 y follow-up too heterogeneous/contradictory to pool.
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 세줄: SR+MA (10편 검토, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 (Healing Abutment) 표면 처리가 임플란트주위 연조직에 미치는 영향 평가. 단기 결과: 플라크 지수 (P=0.091)·탐침 시 출혈 (Bleeding on Probing, BoP, P=0.099)·탐침 깊이 (Probing Depth, PD, P=0.488) 모두 대조군과 유의한 차이 없음. 장기 (5–6년) 4편은 이질성 과다로 풀링 불가·기법에 따라 상반된 

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Long-term (4 studies, 5–6 y):** contradictory results depending on the surface-modification technique.
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 세줄: SR+MA (10편 검토, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 (Healing Abutment) 표면 처리가 임플란트주위 연조직에 미치는 영향 평가. 단기 결과: 플라크 지수 (P=0.091)·탐침 시 출혈 (Bleeding on Probing, BoP, P=0.099)·탐침 깊이 (Probing Depth, PD, P=0.488) 모두 대조군과 유의한 차이 없음. 장기 (5–6년) 4편은 이질성 과다로 풀링 불가·기법에 따라 상반된 

- `canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Healing-abutment batch — where [[wiki/implants/ruhstorfer-2024-customized-vs-conventional-healing-abutments-sr]] asks whether abutment *shape/customization* governs soft-tissue outcomes, this paper isolates the orthogonal variable: does abutment *surface* (machined vs anodized/laser/other modifications) drive peri-implant soft-tissue attachment, inflammation, and maintenance? Reinforces the siblin
  - ▸ 출발(`canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma`) 세줄: SR+MA (10편 검토, 6편 풀링 — RCT 4·CCT 2, 환자 118명·임플란트 182개): 변형된 티타늄 어버트먼트 (Healing Abutment) 표면 처리가 임플란트주위 연조직에 미치는 영향 평가. 단기 결과: 플라크 지수 (P=0.091)·탐침 시 출혈 (Bleeding on Probing, BoP, P=0.099)·탐침 깊이 (Probing Depth, PD, P=0.488) 모두 대조군과 유의한 차이 없음. 장기 (5–6년) 4편은 이질성 과다로 풀링 불가·기법에 따라 상반된 

- `szabo-2022-all-on-four-tilted-distal-implants-mbl` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Tilted implants carry a measurable MBL premium vs axial in All-on-Four, contradicting some SRs that pool underpowered studies; absolute values remain clinically acceptable with good hygiene, but disto-approximal surface of posterior maxillary implants is the highest-risk site.
  - ▸ 출발(`szabo-2022-all-on-four-tilted-distal-implants-mbl`) 세줄: 3.5년 단일기관 회고 연구(36명, 288개 All-on-Four 임플란트); OPT 개별 임플란트 레벨 MBL 측정(기준시점 + 18·30·42개월). 생존율 100%; 경사 원심 임플란트는 전방 축방향 임플란트보다 전 추적 시점에서 MBL 유의하게 큼; 3.5년 상악 0.770 mm, 하악 0.713 mm; 최고 손실 부위 14DA·24DA; 흡연·전신질환이 특정 위치 골소실 악화(P<.05). 경사 임플란트의 MBL 프리미엄이 임상적으로 확인 — 절대치는 허용 범위 내이나 상악 후방 경사 

- `szabo-2022-all-on-four-tilted-distal-implants-mbl` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Key finding: **tilted implants had significantly greater MBL than axial implants at every time point** — contradicting the pooled SR literature (e.g., Durkan et al. meta-analysis: 0.34–1.14 mm axial vs 0.43–1.13 mm tilted, no significant difference). This discrepancy is likely because SRs include underpowered studies. In subgroup analyses, smoking and comorbidities produced significantly higher bo
  - ▸ 출발(`szabo-2022-all-on-four-tilted-distal-implants-mbl`) 세줄: 3.5년 단일기관 회고 연구(36명, 288개 All-on-Four 임플란트); OPT 개별 임플란트 레벨 MBL 측정(기준시점 + 18·30·42개월). 생존율 100%; 경사 원심 임플란트는 전방 축방향 임플란트보다 전 추적 시점에서 MBL 유의하게 큼; 3.5년 상악 0.770 mm, 하악 0.713 mm; 최고 손실 부위 14DA·24DA; 흡연·전신질환이 특정 위치 골소실 악화(P<.05). 경사 임플란트의 MBL 프리미엄이 임상적으로 확인 — 절대치는 허용 범위 내이나 상악 후방 경사 

- `szabo-2022-all-on-four-tilted-distal-implants-mbl` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/mehta-2021-tilted-axial-implants-edentulous-maxilla-sr-ma]] — partially contradicts: SR+MA shows no difference; this study's individual-level data shows tilted>axial
  - ▸ 출발(`szabo-2022-all-on-four-tilted-distal-implants-mbl`) 세줄: 3.5년 단일기관 회고 연구(36명, 288개 All-on-Four 임플란트); OPT 개별 임플란트 레벨 MBL 측정(기준시점 + 18·30·42개월). 생존율 100%; 경사 원심 임플란트는 전방 축방향 임플란트보다 전 추적 시점에서 MBL 유의하게 큼; 3.5년 상악 0.770 mm, 하악 0.713 mm; 최고 손실 부위 14DA·24DA; 흡연·전신질환이 특정 위치 골소실 악화(P<.05). 경사 임플란트의 MBL 프리미엄이 임상적으로 확인 — 절대치는 허용 범위 내이나 상악 후방 경사 

- `koyama-2025-single-vs-two-implant-mandibular-overdenture-sr-ma` [implants] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: This updates and partly overturns an earlier SR (Ahmed et al.) that had reported *better* implant survival for 1-IOD; with post-2017 RCTs added, that survival advantage disappears.
  - ▸ 출발(`koyama-2025-single-vs-two-implant-mandibular-overdenture-sr-ma`) 세줄: PRISMA 체계적 문헌고찰 + 메타분석 (SR+MA), 17편 RCT (12–60개월, PROSPERO CRD420250644169): 단일 정중부 임플란트 오버덴처 (1-IOD) vs 2개 임플란트 오버덴처 (2-IOD) 비교. 임플란트 생존율 1·3·5년 모두 동등(로딩 프로토콜 하위군 포함); 그러나 1-IOD에서 의치 파절(5Y RR 2.10)·재제작(5Y RR 2.57)·메탈하우징 재부착(5Y RR 2.31) 모두 약 2배 높음; 리라이닝·O-ring 교체는 차이 없음. 이동성 차이 없

- `koyama-2025-single-vs-two-implant-mandibular-overdenture-sr-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Updates the literature**: contradicts the earlier higher-survival-for-1-IOD finding once recent RCTs are included.
  - ▸ 출발(`koyama-2025-single-vs-two-implant-mandibular-overdenture-sr-ma`) 세줄: PRISMA 체계적 문헌고찰 + 메타분석 (SR+MA), 17편 RCT (12–60개월, PROSPERO CRD420250644169): 단일 정중부 임플란트 오버덴처 (1-IOD) vs 2개 임플란트 오버덴처 (2-IOD) 비교. 임플란트 생존율 1·3·5년 모두 동등(로딩 프로토콜 하위군 포함); 그러나 1-IOD에서 의치 파절(5Y RR 2.10)·재제작(5Y RR 2.57)·메탈하우징 재부착(5Y RR 2.31) 모두 약 2배 높음; 리라이닝·O-ring 교체는 차이 없음. 이동성 차이 없

- `cosola-2026-customized-3d-printed-titanium-subperiosteal-implants-sr-ma` [implants] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[overviews/vertical-ridge-augmentation-overview]] — CSI are the graftless counterpoint applied to the same severe-atrophy population that vertical augmentation targets.
  - ▸ 출발(`cosola-2026-customized-3d-printed-titanium-subperiosteal-implants-sr-ma`) 세줄: 심하게 위축된 악골에 쓰는 최신 맞춤형 CAD/CAM 3D 프린팅 티타늄 골막하 임플란트(CSI)를 다룬 SR+MA로, 2025년 11월까지 검색해 11편(RCT·코호트·증례군; 환자 268명, 임플란트 369개)을 random-effects로 통합했다. 단기 생존율은 높았으나(≤3년 97.8%) 전체 통합 생존율은 92.4%로 장기 데이터가 주도하는 상당한 이질성을 보였고 — 유일한 6년 추적 연구에서 생존율이 54.1%까지 떨어졌으며, 연조직 관련 합병증(임플란트 노출·열개)이 가장 흔한 부작

- `mello-machado-2021-osseodensification-low-quality-bone-rct` [implants] (HIGH-no-target, 'at odds' · 상충)
  - **근거 문장**: - Living-document note: the abstract's headline ("OD enables the healing chamber without reduction in stability") is supported by ISQ equivalence; the simultaneous IT increase is interesting but somewhat at odds with the "healing chamber = gap = lower IT" rationale and deserves cautious interpretation.
  - ▸ 출발(`mello-machado-2021-osseodensification-low-quality-bone-rct`) 세줄: 이중맹검 무작위대조시험 (Randomized Controlled Trial, RCT), n=16명/55 임플란트 — Misch D3/D4 저밀도골에서 골밀도화 (Osseodensification, OD) vs 표준 언더사이즈 드릴링 비교. OD군 삽입토크 유의하게 높음 (39.0±6.4 vs 32.0±3.4 Ncm, p<0.001); 임플란트 안정성 지수 (Implant Stability Quotient, ISQ)는 식립 시(67.1 vs 65.5) 및 6개월 (74.0 vs 73.3) 모두 동등

- `benic-2014-loading-protocols-single-implant-crowns-sr-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Immediately and conventionally loaded single-implant crowns achieved equivalent survival (1-yr OR 0.75, 95% CI 0.32–1.76) and MBL (SMD −0.05 mm, 95% CI −0.41 to +0.31) at 1, 2, 3, and 5 years; no difference in papilla level; buccal mucosa recession evidence was contradictory and inconclusive.
  - ▸ 출발(`benic-2014-loading-protocols-single-implant-crowns-sr-ma`) 세줄: 11개 RCT SR+MA (Medline/Embase, 2012까지): 단일 임플란트 단관에서 즉시 로딩 vs 통상 로딩 비교, 추적 ≥1년, 생존율·변연골소실(MBL)·유두지수·협측 점막 퇴축 평가. 즉시 로딩과 통상 로딩은 1·2·3·5년에서 생존율(1년 OR 0.75, 95% CI 0.32–1.76)·MBL(SMD −0.05 mm, CI −0.41~+0.31) 동등, 유두 수준 차이 없음; 협측 점막 퇴축 결과는 비일관적·결론 불가. 이 동등성은 삽입토크 ≥20–45 Ncm 또는 ISQ ≥6

- `benic-2014-loading-protocols-single-implant-crowns-sr-ma` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This meta-analysis of 11 RCTs established that immediately and conventionally loaded single-implant crowns achieve equivalent implant survival and marginal bone loss from 1 through 5 years, with no difference in papilla level. Critically, this equivalence holds for implants placed with adequate primary stability — insertion torque ≥20–45 Ncm or ISQ ≥60–65 — and without simultaneous bone augmentati
  - ▸ 출발(`benic-2014-loading-protocols-single-implant-crowns-sr-ma`) 세줄: 11개 RCT SR+MA (Medline/Embase, 2012까지): 단일 임플란트 단관에서 즉시 로딩 vs 통상 로딩 비교, 추적 ≥1년, 생존율·변연골소실(MBL)·유두지수·협측 점막 퇴축 평가. 즉시 로딩과 통상 로딩은 1·2·3·5년에서 생존율(1년 OR 0.75, 95% CI 0.32–1.76)·MBL(SMD −0.05 mm, CI −0.41~+0.31) 동등, 유두 수준 차이 없음; 협측 점막 퇴축 결과는 비일관적·결론 불가. 이 동등성은 삽입토크 ≥20–45 Ncm 또는 ISQ ≥6

- `tarpara-2025-flapless-flapped-clinical-outcomes-cohort` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Flapless offers early comfort and soft-tissue benefits without changing long-term crestal bone outcomes in this non-randomized cohort; this finding contradicts the RCT by Surendra 2025 that reported a significant crestal advantage for flapless at 6 months.
  - ▸ 출발(`tarpara-2025-flapless-flapped-clinical-outcomes-cohort`) 세줄: 전향적 비무작위 코호트 (n=20, 단일 구치부 지연식립, 표현형·외과의 판단으로 배정, 부하 후 12개월) — VAS 통증, 탐침깊이(PD), ImageJ 치조정 골높이(Crestal Bone Height, CBH) 비교. 무피판이 조기 VAS 통증 약 절반 감소 (3일차 3.1 vs 5.7, p=0.001)·6개월 탐침깊이 감소; 두 차이는 12개월에 소실; 치조정 골높이는 어느 시점에도 군간 차이 없음 (모두 p>0.05), 양군 모두 시간에 따른 유의한 골소실. 무피판이 조기 편안함·연조직

- `tarpara-2025-flapless-flapped-clinical-outcomes-cohort` [implants] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 무피판이 조기 편안함·연조직 이점은 있으나 장기 치조정 골 결과는 변화 없음; 이 결과는 Surendra 2025 RCT의 6개월 치조정 이점 발견과 상충.
  - ▸ 출발(`tarpara-2025-flapless-flapped-clinical-outcomes-cohort`) 세줄: 전향적 비무작위 코호트 (n=20, 단일 구치부 지연식립, 표현형·외과의 판단으로 배정, 부하 후 12개월) — VAS 통증, 탐침깊이(PD), ImageJ 치조정 골높이(Crestal Bone Height, CBH) 비교. 무피판이 조기 VAS 통증 약 절반 감소 (3일차 3.1 vs 5.7, p=0.001)·6개월 탐침깊이 감소; 두 차이는 12개월에 소실; 치조정 골높이는 어느 시점에도 군간 차이 없음 (모두 p>0.05), 양군 모두 시간에 따른 유의한 골소실. 무피판이 조기 편안함·연조직

- `tarpara-2025-flapless-flapped-clinical-outcomes-cohort` [implants] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - Provides the cohort counterpoint to RCT data claiming a crestal-bone advantage for flapless.
  - ▸ 출발(`tarpara-2025-flapless-flapped-clinical-outcomes-cohort`) 세줄: 전향적 비무작위 코호트 (n=20, 단일 구치부 지연식립, 표현형·외과의 판단으로 배정, 부하 후 12개월) — VAS 통증, 탐침깊이(PD), ImageJ 치조정 골높이(Crestal Bone Height, CBH) 비교. 무피판이 조기 VAS 통증 약 절반 감소 (3일차 3.1 vs 5.7, p=0.001)·6개월 탐침깊이 감소; 두 차이는 12개월에 소실; 치조정 골높이는 어느 시점에도 군간 차이 없음 (모두 p>0.05), 양군 모두 시간에 따른 유의한 골소실. 무피판이 조기 편안함·연조직

- `tarpara-2025-flapless-flapped-clinical-outcomes-cohort` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/surendra-2025-flapless-versus-flapped-crestal-bone]] — contradicts: an RCT (n=40) found flapless preserved significantly more crestal bone at 3 and 6 months; this cohort found no crestal difference at 12 months.
  - ▸ 출발(`tarpara-2025-flapless-flapped-clinical-outcomes-cohort`) 세줄: 전향적 비무작위 코호트 (n=20, 단일 구치부 지연식립, 표현형·외과의 판단으로 배정, 부하 후 12개월) — VAS 통증, 탐침깊이(PD), ImageJ 치조정 골높이(Crestal Bone Height, CBH) 비교. 무피판이 조기 VAS 통증 약 절반 감소 (3일차 3.1 vs 5.7, p=0.001)·6개월 탐침깊이 감소; 두 차이는 12개월에 소실; 치조정 골높이는 어느 시점에도 군간 차이 없음 (모두 p>0.05), 양군 모두 시간에 따른 유의한 골소실. 무피판이 조기 편안함·연조직

- `huwais-2017-novel-osseous-densification-osteotomy-primary-stability` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Two findings deserve careful clinical interpretation. First, **ISQ did not differ significantly among the three groups** even though insertion torque did — a dissociation that recurs in subsequent OD literature and reflects the fact that ISQ measures lateral stiffness while torque measures axial resistance; OD's effect appears axial-dominant in this model. Second, **temperatures did not rise with 
  - ▸ 출발(`huwais-2017-novel-osseous-densification-osteotomy-primary-stability`) 세줄: 기초 in vitro 벤치 연구 (돼지 경골 72 골삭제, 3군 설계: 표준 드릴링 vs 시계방향 추출 vs 반시계방향 골밀도화(OD), 임플란트 직경 4.1·6.0 mm): 같은 다중날 테이퍼형 버를 반시계방향으로 회전시키는 골밀도화(Osseodensification, OD)를 최초 도입한 논문. OD가 삽입·제거 토크를 유의하게 높이고 BIC를 약 3배 증가; SEM·마이크로 CT로 골삭제 주변 골밀도(BMD) 증가층 확인; ISQ와 온도는 군간 유의차 없음 — 토크-ISQ 해리(dissoci

- `hussein-2019-thread-depth-implant-shape-stress-mandible-fea` [implants] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 거시 형태(macrogeometry) 선택은 안정성과 응력의 상충 관계 — taper는 초기 안정성 유리하나 변연골 기능 응력 상승, 두 목표의 균형이 필요.
  - ▸ 출발(`hussein-2019-thread-depth-implant-shape-stress-mandible-fea`) 세줄: 3D 유한요소분석(Finite Element Analysis, FEA) — 하악 전·후방에서 tapered vs cylindrical 임플란트 형태와 나사산 깊이 비교. 모든 모델에서 임플란트 경부의 변연 피질골(crestal cortical bone)에 최대 폰 미세스 응력(von Mises stress) 집중; tapered body가 모든 골 유형에서 cylindrical보다 최대 응력 높음; 나사산 깊이가 분포 패턴 조절. 거시 형태(macrogeometry) 선택은 안정성과 응력의 상충 

- `hussein-2019-thread-depth-implant-shape-stress-mandible-fea` [implants] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: 임플란트 body shape(tapered vs cylinder)·thread depth가 하중기 골 응력에 미치는 영향을 FEA로 본 연구로, [[implants/leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress]] 의 design×bone density 응력 결과와 짝을 이루는 FEA 클러스터 구성. tapered body가 응력 peak가 높다는 상반된 신호를 제공해 macrogeometry 선택의 trade-off를 보강.
  - ▸ 출발(`hussein-2019-thread-depth-implant-shape-stress-mandible-fea`) 세줄: 3D 유한요소분석(Finite Element Analysis, FEA) — 하악 전·후방에서 tapered vs cylindrical 임플란트 형태와 나사산 깊이 비교. 모든 모델에서 임플란트 경부의 변연 피질골(crestal cortical bone)에 최대 폰 미세스 응력(von Mises stress) 집중; tapered body가 모든 골 유형에서 cylindrical보다 최대 응력 높음; 나사산 깊이가 분포 패턴 조절. 거시 형태(macrogeometry) 선택은 안정성과 응력의 상충 

- `chen-2022-reverse-drilling-technique-alveolar-ridge-expansion` [implants] (HIGH-no-target, 'Counterpoint' · 반대 논점)
  - **근거 문장**: Counterpoint and mechanistic complement to [[wiki/implants/versah-protocols/rittipakorn-2025-clockwise-osseodensification-primary-stability-cadaveric]], which is a cadaveric study contrasting bur **rotation direction** (clockwise vs counter-clockwise) for bone compaction/primary stability. This Chen 2022 sawbone bench study addresses the same core mechanism — the **reverse (counter-clockwise) dril
  - ▸ 출발(`chen-2022-reverse-drilling-technique-alveolar-ridge-expansion`) 세줄: 인공골 (Sawbone 35 PCF) 벤치 실험 (27블록, 치조제 폭 3종 × 드릴링 3종): Densah 역회전 1500 rpm, 변형 OD 역회전 200 rpm, 표준 정회전 1600 rpm 비교. Densah 역회전은 좁은 치조제 (6.75 mm)에서만 표준 정회전 대비 유의하게 더 많은 골폭 확장 (p<0.05); 7.25/7.75 mm에서는 군 간 차이 없음 — 확장 이익은 좁은 골에만 조건부. OD군은 탄성 반발 (Elastic Rebound)로 인해 임플란트 식립 깊이가 다른 두 군

- `jain-2024-heat-generation-pain-piezosurgery-drilling` [implants] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 피에조서저리 → 술후 통증(VAS) 유의하게 감소; 그러나 술 중 골내 온도는 회전 drilling보다 더 높음 → 명확한 통증-발열 상충관계(pain-vs-heat trade-off).
  - ▸ 출발(`jain-2024-heat-generation-pain-piezosurgery-drilling`) 세줄: SR (Cureus 2024, 2,279건 → 9편; RCT·비무작위·in vitro 혼합; RoB 2.0/ROBINS-I/QUIN 비뚤림 평가): 임플란트 골삭제에서 피에조서저리 vs 회전 drilling의 발열 및 술후 통증 비교. 피에조서저리 → 술후 통증(VAS) 유의하게 감소; 그러나 술 중 골내 온도는 회전 drilling보다 더 높음 → 명확한 통증-발열 상충관계(pain-vs-heat trade-off). 통증-발열 trade-off를 명시적으로 분석한 최초 SR; 술후 편안함이 우

- `wach-2026-emergence-angle-marginal-bone-loss` [implants] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - Provides a clinical-cohort counterpoint to the preclinical histological signal for wide EA, helping frame when the animal-model risk (very wide, 60° angles) does vs does not translate to the narrower angles seen in routine clinical practice.
  - ▸ 출발(`wach-2026-emergence-angle-marginal-bone-loss`) 세줄: 후향적 연구, n=155명 환자 / MIS 임플란트 (단일크라운/연결크라운/브릿지), 5년 방사선 추적관찰(3개월·60개월 구내촬영). 평균 돌출각 (emergence angle, EA) 31.8°±10.4°; 단일크라운(p=0.369)과 연결크라운(p=0.176)은 EA-변연골소실(marginal bone loss, MBL) 연관성 없음, 브릿지에서만 약하지만 통계적으로 유의한 연관성(p=0.042, R²=7.9%); 3개월·60개월 모두 보철 유형 간 MBL·피질화지수(Corticalizati

- `wach-2026-emergence-angle-marginal-bone-loss` [implants] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - [[overviews/implant-prosthesis-misfit-connection-mbl-overview]] — broader synthesis of prosthetic misfit/connection factors and MBL; this paper adds emergence-angle specifically as a tested (and largely refuted, for single/splinted crowns) risk factor within that framework.
  - ▸ 출발(`wach-2026-emergence-angle-marginal-bone-loss`) 세줄: 후향적 연구, n=155명 환자 / MIS 임플란트 (단일크라운/연결크라운/브릿지), 5년 방사선 추적관찰(3개월·60개월 구내촬영). 평균 돌출각 (emergence angle, EA) 31.8°±10.4°; 단일크라운(p=0.369)과 연결크라운(p=0.176)은 EA-변연골소실(marginal bone loss, MBL) 연관성 없음, 브릿지에서만 약하지만 통계적으로 유의한 연관성(p=0.042, R²=7.9%); 3개월·60개월 모두 보철 유형 간 MBL·피질화지수(Corticalizati

- `wach-2026-emergence-angle-marginal-bone-loss` [implants] (HIGH-far→mikulas-2025-digital-impression-accuracy-peri-implant-emergence-profile-sr, '반박' · 반박)
  - **근거 문장**: 기존 [[overviews/implant-prosthesis-misfit-connection-mbl-overview]]는 보철 부적합·연결부가 변연골소실 (marginal bone loss, MBL)에 미치는 영향을 종합했지만, 크라운 돌출각 (emergence angle, EA) 자체의 영향은 [[prosthetic-materials/mikulas-2025-digital-impression-accuracy-peri-implant-emergence-profile-sr]]가 다룬 디지털 인상 정확도 관점 외에 별도 근거가 부족했다. 본 155환자·5년 후향적 연구는 EA가 단일/연결/브릿지 보철에서 MBL 및 피질화 지수 (Corticalization Index, CI)에 미치는 영향을 직접 비교해, 단일·연
  - ▸ 출발(`wach-2026-emergence-angle-marginal-bone-loss`) 세줄: 후향적 연구, n=155명 환자 / MIS 임플란트 (단일크라운/연결크라운/브릿지), 5년 방사선 추적관찰(3개월·60개월 구내촬영). 평균 돌출각 (emergence angle, EA) 31.8°±10.4°; 단일크라운(p=0.369)과 연결크라운(p=0.176)은 EA-변연골소실(marginal bone loss, MBL) 연관성 없음, 브릿지에서만 약하지만 통계적으로 유의한 연관성(p=0.042, R²=7.9%); 3개월·60개월 모두 보철 유형 간 MBL·피질화지수(Corticalizati

- `kim-2026-implant-angulation-peri-implant-bone` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[occlusion/di-fiore-2022-periimplant-bone-loss-overload-occlusal-analysis]] — contradicts/refines: occlusal-overload framing; this study supplies positive clinical evidence that off-axis geometry (not just overload magnitude) tracks MBL, where some overload analyses found weaker links.
  - ▸ 출발(`kim-2026-implant-angulation-peri-implant-bone`) 세줄: 5년 단일기관 후향 코호트(288명, 506개 임플란트, 평균 추적 5.1년): CAD 3D 각도 측정(근원심 + 협설 방향)으로 비축방향 로딩이 변연골 소실 (Marginal Bone Loss, MBL)에 미치는 영향 분석; 치태지수 ≤5% 환자만 포함, 교합조정으로 미생물 교란 최소화. 비축방향 임플란트가 축방향 대비 MBL 유의하게 큼(0.22 vs 0.10 mm, P<.05); 상악>하악(P<.001); 비축방향×대합치 유형 상호작용 유의(P=0.007) — 비축방향이 임플란트 지지 고정성

- `kim-2026-implant-angulation-peri-implant-bone` [implants] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 비축방향(nonaxial) 식립이 변연골 소실(MBL)에 미치는 영향을 CAD 기반 3차원 각도 측정으로 정량화한 한국 박사학위 연구(506개 임플란트, 5.1년). 기존 [[occlusion/di-fiore-2022-periimplant-bone-loss-overload-occlusal-analysis]]·[[overviews/implant-occlusion-loading-biomechanics-overview]]가 교합 과부하–골소실을 다루지만, 선행 연구(Koutouzis 2007, Lee)는 근원심 2D 각도만 측정해 "비축 하중이 MBL을 늘리지 않는다"는 음성 결과를 냈다. 이 연구는 협설 각도를 포함한 다방향 측정으로 그 음성 결과를 보강·반박하며, [[implants/stilwell-2024-
  - ▸ 출발(`kim-2026-implant-angulation-peri-implant-bone`) 세줄: 5년 단일기관 후향 코호트(288명, 506개 임플란트, 평균 추적 5.1년): CAD 3D 각도 측정(근원심 + 협설 방향)으로 비축방향 로딩이 변연골 소실 (Marginal Bone Loss, MBL)에 미치는 영향 분석; 치태지수 ≤5% 환자만 포함, 교합조정으로 미생물 교란 최소화. 비축방향 임플란트가 축방향 대비 MBL 유의하게 큼(0.22 vs 0.10 mm, P<.05); 상악>하악(P<.001); 비축방향×대합치 유형 상호작용 유의(P=0.007) — 비축방향이 임플란트 지지 고정성

- `ting-2017-surgical-patient-factors-affecting-marginal` [implants] (HIGH-no-target, 'conflicting result' · 상충 결과)
  - **근거 문장**: Statistically significant factors: periodontitis (esp. generalized aggressive vs chronic), male sex, and smoking (incl. greater MBL in maxilla than mandible in smokers) all increased MBL; alveolar socket/ridge preservation with grafts reduced MBL, while ridge augmentation sites had more MBL than sites treated with shorter implants; implant length/type and immediate vs delayed placement showed conf
  - ▸ 출발(`ting-2017-surgical-patient-factors-affecting-marginal`) 세줄: 체계적문헌고찰들의 종합적 개관(umbrella/AMSTAR 평가 종합, 2015년 11월까지 발표된 SR/MA 116편 중 41편 선정 — 임플란트 요인 11편, 환자 요인 10편, 수술 프로토콜 19편, 3요인 모두 1편), 골유착 임플란트 주위 변연골 소실(Marginal Bone Loss, MBL)에 영향을 미치는 수술적·환자적 요인 평가. 통계적으로 유의한 요인: 치주염(특히 전신형 공격성 치주염 > 만성 치주염), 남성, 흡연(흡연자는 하악보다 상악에서 MBL이 더 큼)이 MBL을 증가시

- `ting-2017-surgical-patient-factors-affecting-marginal` [implants] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 통계적으로 유의한 요인: 치주염(특히 전신형 공격성 치주염 > 만성 치주염), 남성, 흡연(흡연자는 하악보다 상악에서 MBL이 더 큼)이 MBL을 증가시켰고; 발치와 보존술(socket/ridge preservation with grafts)은 MBL을 감소, 반면 치조제 증대(ridge augmentation) 부위는 짧은 임플란트 대체 부위보다 MBL이 더 많았음; 임플란트 길이·종류·즉시 vs 지연 식립은 결과 상충, 임플란트 표면·경사(tilted vs axial) 식립·flapless vs flapped 수술·연조직 이식술·삽입 토크·1-stage vs 2-stage는 유의한 영향 없음.
  - ▸ 출발(`ting-2017-surgical-patient-factors-affecting-marginal`) 세줄: 체계적문헌고찰들의 종합적 개관(umbrella/AMSTAR 평가 종합, 2015년 11월까지 발표된 SR/MA 116편 중 41편 선정 — 임플란트 요인 11편, 환자 요인 10편, 수술 프로토콜 19편, 3요인 모두 1편), 골유착 임플란트 주위 변연골 소실(Marginal Bone Loss, MBL)에 영향을 미치는 수술적·환자적 요인 평가. 통계적으로 유의한 요인: 치주염(특히 전신형 공격성 치주염 > 만성 치주염), 남성, 흡연(흡연자는 하악보다 상악에서 MBL이 더 큼)이 MBL을 증가시

- `ting-2017-surgical-patient-factors-affecting-marginal` [implants] (HIGH-no-target, 'Conflicting result' · 상충 결과)
  - **근거 문장**: | Implant length, implant type, immediate vs delayed placement | Conflicting results across SRs |
  - ▸ 출발(`ting-2017-surgical-patient-factors-affecting-marginal`) 세줄: 체계적문헌고찰들의 종합적 개관(umbrella/AMSTAR 평가 종합, 2015년 11월까지 발표된 SR/MA 116편 중 41편 선정 — 임플란트 요인 11편, 환자 요인 10편, 수술 프로토콜 19편, 3요인 모두 1편), 골유착 임플란트 주위 변연골 소실(Marginal Bone Loss, MBL)에 영향을 미치는 수술적·환자적 요인 평가. 통계적으로 유의한 요인: 치주염(특히 전신형 공격성 치주염 > 만성 치주염), 남성, 흡연(흡연자는 하악보다 상악에서 MBL이 더 큼)이 MBL을 증가시

- `shetty-2026-titanium-vs-zirconia-implants-umbrella` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/mohseni-2024-clinical-outcomes-zirconia-implants]] — contradicts (material-level "Ti > Zr" conclusion here is undercut by Mohseni's design-stratified finding that one-piece, non-drill-prepared zirconia matches titanium at 10 years; Mohseni's SR+MA is larger, more recent, and higher evidence weight)
  - ▸ 출발(`shetty-2026-titanium-vs-zirconia-implants-umbrella`) 세줄: Umbrella review(overview of reviews) — 2014–2023년 SR 6편을 종합해 티타늄 vs 지르코니아 임플란트를 생존율·성공률·변연골소실(MBL)·탐침깊이·치태지수·출혈지수·핑크심미점수·골유착 측면에서 비교. 티타늄이 대부분 SR에서 생존율(92.6–100% vs 지르코니아 87.5–93.3%)·성공률 우위(Elnayef 2017: 지르코니아 실패위험 약 89% 높음; Duan 2023 메타분석 성공률 RR 0.87, p=0.03 티타늄 우세), MBL·탐침깊이·치태

- `zarzar-2023-implants-radiotherapy-head-neck` [implants] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 두 논문의 방향성은 일치한다: Zarzar 86.2% vs 95.2%(조사 vs 비조사), Pacheco 81.52% vs 94.64% — 독립적으로 동일한 결론(방사선치료가 임플란트 생존율을 낮춘다)을 재확인. 그러나 Pacheco가 (1) PROSPERO 사전등록, (2) 더 넓은 4개→4+grey lit 데이터베이스, (3) 더 최신 검색 시점(2024-02 vs 2022-07), (4) 훨씬 큰 정량 통합 표본(48,563 vs 24,996), (5) AMSTAR 2 평가의 내적 일관성(11편 전부 critically low vs Zarzar의 15편 중 1편만 high — 이 불일치는 실제로 published comment[PMID 37191480, DOI 10.1111/scd.12875]가 방법론
  - ▸ 출발(`zarzar-2023-implants-radiotherapy-head-neck`) 세줄: Umbrella review (SR 15편, 두경부암 환자 5,487명·임플란트 24,996개, 2022년 7월까지 4개 DB[PubMed/Lilacs/Cochrane/Google Scholar] 검색) — 방사선치료군 vs 비치료군 임플란트 성공률 비교. 방사선치료군 성공률 86.2% vs 비치료군 95.2%; 포함 SR 15편 중 AMSTAR 2 기준 high quality는 단 1편. 두경부암 방사선치료 후 임플란트 재활은 여전히 유효한 치료법이나, 포함 SR 대부분(15편 중 14편)의 낮

- `dambrosio-2023-systemic-diseases-medications-influence` [implants] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 항흡수제(비스포스포네이트)는 골유착·생존율에 유의한 영향 없음(de Medeiros SR-MA: 골다공증군 4.70% vs 건강군 3.57% 실패율, 비유의); SSRI·PPI는 여러 포함 리뷰에서 일관되게 부정적 신호(실패율 차이 각각 약 7.5%, 약 4.5%); 당뇨는 결과가 상충하며 대부분 단기 연구; 신경계질환·HIV·갑상선기능저하증·심혈관질환·항고혈압제/베타차단제/이뇨제는 골유착 저하를 보이지 않음.
  - ▸ 출발(`dambrosio-2023-systemic-diseases-medications-influence`) 세줄: 우산리뷰(umbrella review, SR 8편, 2017년 3월~2022년 7월 영어 논문)로, 전신질환·약물이 임플란트 골유착·성공/생존율·임플란트주위염·임플란트 상실에 미치는 영향을 메타분석 없이 서술적으로 종합; PROSPERO CRD42023397955 등록, AMSTAR 2 품질 평가. 항흡수제(비스포스포네이트)는 골유착·생존율에 유의한 영향 없음(de Medeiros SR-MA: 골다공증군 4.70% vs 건강군 3.57% 실패율, 비유의); SSRI·PPI는 여러 포함 리뷰에서 일

- `dambrosio-2023-systemic-diseases-medications-influence` [implants] (HIGH-no-target, 'conflicting evidence' · 상충 결과)
  - **근거 문장**: - Frames diabetes' conflicting evidence base as a short-term/well-controlled-disease sampling artifact rather than a true null result, aligning with the 2017 World Workshop classification of diabetes as a peri-implant risk factor in poorly-controlled/long-term disease.
  - ▸ 출발(`dambrosio-2023-systemic-diseases-medications-influence`) 세줄: 우산리뷰(umbrella review, SR 8편, 2017년 3월~2022년 7월 영어 논문)로, 전신질환·약물이 임플란트 골유착·성공/생존율·임플란트주위염·임플란트 상실에 미치는 영향을 메타분석 없이 서술적으로 종합; PROSPERO CRD42023397955 등록, AMSTAR 2 품질 평가. 항흡수제(비스포스포네이트)는 골유착·생존율에 유의한 영향 없음(de Medeiros SR-MA: 골다공증군 4.70% vs 건강군 3.57% 실패율, 비유의); SSRI·PPI는 여러 포함 리뷰에서 일

- `stubinger-2015-piezosurgery-implant-dentistry` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The "avoidance of thermal damage" claim promoted in this review is later partly contradicted by Aquilanti (2023) and Jain (2024); piezo's primary value is in anatomically delicate indications (Schneiderian membrane, IAN) rather than routine osteotomy speed.
  - ▸ 출발(`stubinger-2015-piezosurgery-implant-dentistry`) 세줄: 서술적 임상 고찰 (Clin Cosmet Investig Dent 2015) — 임플란트 치과에서 압전 골수술(piezosurgery) 적용 총론; 역사·기술적 근거·적응증(임플란트 site prep, 골이식, 상악동 거상, ridge split, 하치조신경 lateralization) 포괄. 장점으로 무기질화 조직의 정밀 선택적 절삭·연조직·신경·막 보존·시야 개선 제시; 단점으로 수술시간 연장·학습곡선·인서트 마모·비용 명시. "열손상 회피" 주장은 Aquilanti 2023·Jain 2024

- `stubinger-2015-piezosurgery-implant-dentistry` [implants] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: "열손상 회피" 주장은 Aquilanti 2023·Jain 2024로 부분 반박됨 — piezo 최대 가치는 연조직·신경·막이 인접한 해부학적으로 민감한 적응증에 있음.
  - ▸ 출발(`stubinger-2015-piezosurgery-implant-dentistry`) 세줄: 서술적 임상 고찰 (Clin Cosmet Investig Dent 2015) — 임플란트 치과에서 압전 골수술(piezosurgery) 적용 총론; 역사·기술적 근거·적응증(임플란트 site prep, 골이식, 상악동 거상, ridge split, 하치조신경 lateralization) 포괄. 장점으로 무기질화 조직의 정밀 선택적 절삭·연조직·신경·막 보존·시야 개선 제시; 단점으로 수술시간 연장·학습곡선·인서트 마모·비용 명시. "열손상 회피" 주장은 Aquilanti 2023·Jain 2024

- `stubinger-2015-piezosurgery-implant-dentistry` [implants] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "thermal damage 회피" 주장은 [미검증] aquilanti 2023, jain 2024 SR 결과로 부분적으로 반박됨 — 정확한 piezo protocol(권장 load, quarter-turn 회전, 차가운 saline) 준수가 전제.
  - ▸ 출발(`stubinger-2015-piezosurgery-implant-dentistry`) 세줄: 서술적 임상 고찰 (Clin Cosmet Investig Dent 2015) — 임플란트 치과에서 압전 골수술(piezosurgery) 적용 총론; 역사·기술적 근거·적응증(임플란트 site prep, 골이식, 상악동 거상, ridge split, 하치조신경 lateralization) 포괄. 장점으로 무기질화 조직의 정밀 선택적 절삭·연조직·신경·막 보존·시야 개선 제시; 단점으로 수술시간 연장·학습곡선·인서트 마모·비용 명시. "열손상 회피" 주장은 Aquilanti 2023·Jain 2024

- `pirc-2026-one-piece-two-piece-implants-15year-rct` [implants] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 원-피스는 생물학적 유리(골보존), 투-피스는 기술적 유리(합병증↓) — 명확한 생물학적·기술적 상충 관계; BRA 결과를 현대 내부연결·플랫폼 스위칭 투-피스 시스템에 외삽 불가.
  - ▸ 출발(`pirc-2026-one-piece-two-piece-implants-15year-rct`) 세줄: RCT 15–17년 추적(환자 60명, 임플란트 151개; 취리히대학교) — 원-피스(One-piece) Straumann SLA(STM, 65개) vs 투-피스(Two-piece) Brånemark TiUnite(BRA, 86개) 임플란트 최장기 RCT 추적. 전체 생존율(Implant Survival Rate, ISR) 95%(STM 91.84% vs BRA 98.04%); 변연골소실(Marginal Bone Loss, MBL): STM 0.08 mm vs BRA 1.53 mm(원-피스 우수)

- `sahoo-2024-finite-element-analysis-influence-implant` [implants] (HIGH-no-target, 'counter to' · 반대)
  - **근거 문장**: Sahoo et al. (2024) combined a physical in vitro bench experiment with nonlinear finite element analysis (FEA) to compare axial versus 30° distally tilted implants under simulated immediate-loading conditions. Eight NobelReplace Tapered Groovy implants (4 axial, 4 distally tilted) were placed in synthetic polyurethane-foam bone blocks with a fiber-reinforced epoxy cortical shell, then loaded with 
  - ▸ 출발(`sahoo-2024-finite-element-analysis-influence-implant`) 세줄: 인공 골블록(폴리우레탄 폼) 8개·NobelReplace Tapered Groovy 임플란트 8개(축방향 4개, 원위 30° 경사 4개, 11×4.5mm)를 이용한 즉시부하 (immediate loading) 임플란트 in vitro + 유한요소분석 (Finite Element Analysis, FEA) 비교연구 — 180N 수직하중 vs 45° 근원심 사선하중. 사선하중은 각도와 무관하게 수직하중보다 2.6~3.9배 큰 최대 미세운동 (micromotion)을 유발했으며, 수직하중에서는 축방향·

- `song-2024-long-term-clinical-radiographic-outcomes` [implants] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 5편 배치(임플란트 보철 margin/design ↔ MBL) 중 아시아 저널 대표편. Journal of Periodontal & Implant Science(JPIS, 한국치주과학회지)에 실린 연세대학교 치과대학병원의 872개 임플란트·12.3년 평균 추적 초장기(10년+) 후향적 코호트로, 표본크기·추적기간 면에서 이 도메인의 가장 견고한 실사용(real-world) 데이터 중 하나. 동일 저널·동일 국가(한국)의 [[implants/kim-2022-abutment-connection-mbl-survival]]과 함께 연결부 타입·임플란트 길이가 MBL/생존에 미치는 영향을 다루며, [[overviews/implant-prosthesis-misfit-connection-mbl-overview]]의 근거
  - ▸ 출발(`song-2024-long-term-clinical-radiographic-outcomes`) 세줄: 연세대학교 치과대학병원에서 872개 골수준(bone-level), 2-피스, 내부연결 임플란트(코로날 마이크로스레드, Implantium)를 284명 환자에서 평균 12.3±2.0년(모집단 1,845개 임플란트/691명) 후향적으로 추적한 코호트. 10년 누적 생존율은 임플란트수준 95.2% / 환자수준 88.4%, 치료성공률(MBL <2mm)은 87.0% / 76.1%; 생존한 830개 중 113개가 "ailing"(평균 MBL 4.09±1.44mm)으로 분류; 8mm 이하 짧은 임플란트는 실패

- `kavitha-2023-outcome-implant-diameter-length-distribution` [implants] (HIGH-no-target, 'Counter to' · 반대)
  - **근거 문장**: This 3D finite element study models a one-piece LEADER/ITALIA-Fix implant designed specifically for immediate loading, embedded in a homogeneous bone block, to isolate the effect of implant **length** (10 mm vs 12 mm) and **diameter** (3.75 mm vs 4.25 mm) on peri-implant von Mises stress under a fixed 2.0 MPa axial load. Across all four configurations the implant neck/cervical region carried the m
  - ▸ 출발(`kavitha-2023-outcome-implant-diameter-length-distribution`) 세줄: 일체형(one-piece) LEADER/ITALIA-Fix 즉시하중 임플란트를 25×15×15 mm 골블록에 매립한 3D 유한요소해석(Finite Element Analysis, FEA, ANSYS v12)으로, 길이 2종(10, 12 mm)·직경 2종(3.75, 4.25 mm)을 2.0 MPa 축방향 교합하중 하에서 비교. 전 조건에서 임플란트 넥(neck)이 최고 응력 부위였고, 길이를 10→12 mm로 늘리면 계면 von Mises 응력이 소폭 증가(최대 1.32→1.76 MPa)했으며, 직

- `kavitha-2023-outcome-implant-diameter-length-distribution` [implants] (HIGH-no-target, 'counter to' · 반대)
  - **근거 문장**: - Reports a **length-increases-stress** direction (10→12 mm) that runs counter to some other FEA studies in this wiki (see Related Papers), highlighting that the length-stress relationship is not universal across implant macrogeometries and length ranges.
  - ▸ 출발(`kavitha-2023-outcome-implant-diameter-length-distribution`) 세줄: 일체형(one-piece) LEADER/ITALIA-Fix 즉시하중 임플란트를 25×15×15 mm 골블록에 매립한 3D 유한요소해석(Finite Element Analysis, FEA, ANSYS v12)으로, 길이 2종(10, 12 mm)·직경 2종(3.75, 4.25 mm)을 2.0 MPa 축방향 교합하중 하에서 비교. 전 조건에서 임플란트 넥(neck)이 최고 응력 부위였고, 길이를 10→12 mm로 늘리면 계면 von Mises 응력이 소폭 증가(최대 1.32→1.76 MPa)했으며, 직

- `kavitha-2023-outcome-implant-diameter-length-distribution` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/singh-2024-influence-implant-design-length-stress]] — contradicts on direction: Singh 2024 (2D FEA, D4 bone, tapered/step designs, 6 mm vs 10 mm) found longer fixtures **consistently lowered** interface stress (vertical 188→35.44 MPa for step design); Kavitha 2023 (3D FEA, one-piece immediate-loading design, 10 mm vs 12 mm) found the **opposite direction** — a small stress increase wi
  - ▸ 출발(`kavitha-2023-outcome-implant-diameter-length-distribution`) 세줄: 일체형(one-piece) LEADER/ITALIA-Fix 즉시하중 임플란트를 25×15×15 mm 골블록에 매립한 3D 유한요소해석(Finite Element Analysis, FEA, ANSYS v12)으로, 길이 2종(10, 12 mm)·직경 2종(3.75, 4.25 mm)을 2.0 MPa 축방향 교합하중 하에서 비교. 전 조건에서 임플란트 넥(neck)이 최고 응력 부위였고, 길이를 10→12 mm로 늘리면 계면 von Mises 응력이 소폭 증가(최대 1.32→1.76 MPa)했으며, 직

- `kavitha-2023-outcome-implant-diameter-length-distribution` [implants] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: [[implants/singh-2024-influence-implant-design-length-stress]]는 6 mm→10 mm 픽스쳐 길이 증가가 D4 골에서 계면 응력을 일관되게 낮춘다고 보고했다 (수직 188→35.44 MPa). 본 논문(Kavitha 2023)은 다른 임플란트 형태(LEADER/ITALIA-Fix 일체형, 즉시하중)에서 10 mm→12 mm 길이 증가가 오히려 응력을 소폭 증가(1.32→1.76 MPa)시킨다고 보고해, "길이가 길수록 응력 감소"라는 단순 도식에 반례를 제공한다. 직경 증가(3.75→4.25 mm)는 응력에 유의한 영향이 없다는 결과도 함께 기록해, 임플란트 디자인/골질/길이 구간에 따라 길이-응력 관계가 뒤집힐 수 있음을 보여주는 대비 사례로 인제스트.
  - ▸ 출발(`kavitha-2023-outcome-implant-diameter-length-distribution`) 세줄: 일체형(one-piece) LEADER/ITALIA-Fix 즉시하중 임플란트를 25×15×15 mm 골블록에 매립한 3D 유한요소해석(Finite Element Analysis, FEA, ANSYS v12)으로, 길이 2종(10, 12 mm)·직경 2종(3.75, 4.25 mm)을 2.0 MPa 축방향 교합하중 하에서 비교. 전 조건에서 임플란트 넥(neck)이 최고 응력 부위였고, 길이를 10→12 mm로 늘리면 계면 von Mises 응력이 소폭 증가(최대 1.32→1.76 MPa)했으며, 직

- `huwais-2017-autografting-tool-enhanced-flute-profile` [implants] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 대화에서 다룬 **덴샤버(Densah/Versah)의 "날 모양(flute profile)"과 CW=절삭 / CCW=압축 양방향 메커니즘의 1차 원천 문서**다. 기존 [[wiki/implants/huwais-2017-novel-osseous-densification-osteotomy-primary-stability]] 는 동일 발명자(Huwais)의 *벤치 검증 논문*일 뿐 도구 자체의 기하·청구항은 담지 않는다. 이 PCT 특허는 negative rake angle flute, densifying face/cutting face/land/working edge 구조와 hydraulic autografting 원리를 직접 청구·기술해, 해냄 콘덴싱 스크류 특허 [[wiki/implants/kim-2019-
  - ▸ 출발(`huwais-2017-autografting-tool-enhanced-flute-profile`) 세줄: PCT 특허(WO 2017/124079 A1; Huwais IP Holding LLC) — Densah/Versah 골밀도화(Osseodensification, OD) 회전 osteotome 설계 공개. 핵심 개량은 연속 음의 레이크각(negative rake angle) flute으로, 각 flute에 cutting face + densifying face가 함께 존재. 음의 레이크 형상이 동일 도구의 시계방향 = 절삭 / 반시계방향 = 압축·유압 자가이식(hydraulic autograft)을

- `rugova-2024-thermal-evaluation-bone-drilling-sequential` [implants] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: A custom-press in vitro study tested 5 drill bits in sequential drilling protocols with infrared thermography. The principal finding overturns a long-standing assumption: sequential drilling does not eliminate thermal trauma. The first (pilot) drill produces peak temperatures over 100°C, creating a thermal damage zone that spreads up to 10 mm from the osteotomy. Subsequent enlarging drills cannot 
  - ▸ 출발(`rugova-2024-thermal-evaluation-bone-drilling-sequential`) 세줄: 인비트로 적외선 열화상(Infrared Thermography) 연구(Bioengineering 2024; 맞춤 드릴 프레스, 5개 드릴, 합성골, **irrigation 없음**) — sequential drilling이 골 열손상을 방지한다는 임상 가정 검증. Sequential drilling은 열 손상 제거 실패 — 파일럿 드릴(Pilot Drill) 최고 온도 >100°C, 70°C 발열이 osteotomy로부터 측방 10 mm까지 확산; 후속 확대 드릴은 열 추가; RPM 감소·하중 감

- `rugova-2024-thermal-evaluation-bone-drilling-sequential` [implants] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Directly refutes the implicit clinical belief that "sequential drilling protects from heat." Identifies the pilot drill as the dominant thermal event and the peri-osteotomy zone (up to 10 mm) as the affected region.
  - ▸ 출발(`rugova-2024-thermal-evaluation-bone-drilling-sequential`) 세줄: 인비트로 적외선 열화상(Infrared Thermography) 연구(Bioengineering 2024; 맞춤 드릴 프레스, 5개 드릴, 합성골, **irrigation 없음**) — sequential drilling이 골 열손상을 방지한다는 임상 가정 검증. Sequential drilling은 열 손상 제거 실패 — 파일럿 드릴(Pilot Drill) 최고 온도 >100°C, 70°C 발열이 osteotomy로부터 측방 10 mm까지 확산; 후속 확대 드릴은 열 추가; RPM 감소·하중 감

- `kim-2019-double-spiral-condensing-screw-implant` [implants] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 대화에서 다룬 해냄버(HaeNaem bur)의 회전방향-압축 메커니즘의 **공학적 1차 근거 문서**다. 임상 데이터 [[wiki/sinus-lift/transcrestal/changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift]] 는 "HaeNaem이 시계방향(CW)으로 골치밀화한다"는 결과만 보여줄 뿐 *왜·어떻게*는 설명하지 못한다. 이 (주)해냄 특허는 그 스크류 기하(이중 스파이럴: 압착나사산부 + 본파우더안내홈 + 하부압착돔)와 "회전방향과 반대방향 나사산" 원리를 직접 기술해, 골밀도화(Osseodensification, OD) 발명 원리를 정리한 [[wiki/implants/huwais-2017-novel-osseous-densification-
  - ▸ 출발(`kim-2019-double-spiral-condensing-screw-implant`) 세줄: 한국 등록특허(KR 10-2304707, 등록 2021, 발명자 김성주, 출원인 (주)해냄): 이중 스파이럴(압착나사산부 + 본파우더안내홈 + 하부압착돔) 구조로 측방 골치밀화와 근단부 골치밀화를 단일 기구로 수행. 골분말을 하부압착돔으로 유도해 치조골저(근단측)까지 치밀화하는 원리 — 종래 OD 버의 측방 편중 한계를 보완하고 경치조골 상악동 거상까지 가능하게 한다는 설계 주장. 임상·벤치 계측치 없음(발명자 주장만), 유일한 임상 전향 연구(Changrani 2024)는 철회됨 — 현재 이 특

- `kindaro-2026-parathyroid-hormone-implant-osseointegration-osteoporosis-sr` [implants] (SOFT→drug-mronj-antiresorptive-overview, 'whereas' · 반면(대조))
  - **근거 문장**: The wiki frames osteoporosis and its drugs almost entirely as **hazards** to implant therapy: osteoporosis lowers long-term implant survival (short-term 97.9–100% but 5–10 yr 82.6–94.1% with greater marginal bone loss, per [[implants/kim-2026-dental-implant-osteoporosis-osteosclerosis]]), and the antiresorptive agents used to treat it (bisphosphonates, denosumab) raise MRONJ risk ([[overviews/drug
  - ▸ 출발(`kindaro-2026-parathyroid-hormone-implant-osseointegration-osteoporosis-sr`) 세줄: 골다공증 유발 난소/고환 절제 쥐·토끼 모델에서 부갑상선호르몬(Parathyroid Hormone, PTH; 테리파라타이드, PTH 1–34)의 임플란트 골유착 효과를 다룬 12편 전임상 연구의 업데이트 체계적 문헌고찰 (Systematic Review, PRISMA·INPLASY·SYRCLE, 2015–2025.8) — 사람 연구는 0편. 간헐적 PTH 투여는 골-임플란트 접촉률(BIC)·골부피율(BV/TV)·제거토크를 대조군 대비 일관되게 증가; 병용요법(PTH+비타민 D, PTH+랄록시펜, 
  - ▸ 대상(`drug-mronj-antiresorptive-overview`) 세줄: 약물관련악골괴사(Medication-Related Osteonecrosis of the Jaw, MRONJ) 14편 통합: 예방 1차 전략은 항흡수제 시작 전 치과 클리어런스(Baghalipour 2025 4단계 프레임워크); 데노수맙(Denosumab) 위험은 누적 용량 의존 — 유방암 골전이 코호트 ≥32회 시 MRONJ 31.2%(Yokoo 2025 ROC AUC 0.83); 발치력 OR 4.40; 미국구강악안면외과학회(AAOMS) 2022는 수술 치료를 전 병기로 확대, 약물 중단(drug

- `kindaro-2026-parathyroid-hormone-implant-osseointegration-osteoporosis-sr` [implants] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: PTH/teriparatide has strong biological plausibility as an osteoanabolic adjunct to improve implant osseointegration in osteoporotic bone, and preclinical animal data are encouragingly consistent — especially for intermittent dosing, pre-operative timing, local delivery, and combination with vitamin D or raloxifene. **However, this evidence is entirely animal (rat/rabbit) with no human studies, hig
  - ▸ 출발(`kindaro-2026-parathyroid-hormone-implant-osseointegration-osteoporosis-sr`) 세줄: 골다공증 유발 난소/고환 절제 쥐·토끼 모델에서 부갑상선호르몬(Parathyroid Hormone, PTH; 테리파라타이드, PTH 1–34)의 임플란트 골유착 효과를 다룬 12편 전임상 연구의 업데이트 체계적 문헌고찰 (Systematic Review, PRISMA·INPLASY·SYRCLE, 2015–2025.8) — 사람 연구는 0편. 간헐적 PTH 투여는 골-임플란트 접촉률(BIC)·골부피율(BV/TV)·제거토크를 대조군 대비 일관되게 증가; 병용요법(PTH+비타민 D, PTH+랄록시펜, 

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Flapless technique offers a significant early crestal bone advantage in healed posterior-mandibular ridges, but the study is limited to 6 months, uses 2D radiography, and is a single-center single-surgeon trial; this finding contradicts a non-randomized cohort (Tarpara 2025) that found no crestal difference at 12 months.
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 세줄: 전향적 RCT (n=40, 하악 구치부 치유된 치조제 단일치 임플란트, 1:1 무작위 배정: 무피판 펀치 vs 전층 점막골막 피판; 4.0 × 10 mm 임플란트; 6개월 치조정 골소실 방사선 평가). 무피판군이 피판군 대비 치조정 골소실 유의하게 적음 — 3개월 (0.32 vs 0.56 mm) 및 6개월 (0.48 vs 0.82 mm, 모두 p<0.001); 양군 생존율 100%, 합병증 없음. 무피판 술식이 치유된 하악 구치부에서 조기 치조정 골소실 감소 이점 제공; 단, 6개월·2D·단일기관

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 무피판 술식이 치유된 하악 구치부에서 조기 치조정 골소실 감소 이점 제공; 단, 6개월·2D·단일기관 한계이며, 12개월 비무작위 코호트(Tarpara 2025)는 치조정 차이 없음을 보고해 상충.
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 세줄: 전향적 RCT (n=40, 하악 구치부 치유된 치조제 단일치 임플란트, 1:1 무작위 배정: 무피판 펀치 vs 전층 점막골막 피판; 4.0 × 10 mm 임플란트; 6개월 치조정 골소실 방사선 평가). 무피판군이 피판군 대비 치조정 골소실 유의하게 적음 — 3개월 (0.32 vs 0.56 mm) 및 6개월 (0.48 vs 0.82 mm, 모두 p<0.001); 양군 생존율 100%, 합병증 없음. 무피판 술식이 치유된 하악 구치부에서 조기 치조정 골소실 감소 이점 제공; 단, 6개월·2D·단일기관

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - Provides a clean RCT counterpoint to cohort data showing no crestal difference.
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 세줄: 전향적 RCT (n=40, 하악 구치부 치유된 치조제 단일치 임플란트, 1:1 무작위 배정: 무피판 펀치 vs 전층 점막골막 피판; 4.0 × 10 mm 임플란트; 6개월 치조정 골소실 방사선 평가). 무피판군이 피판군 대비 치조정 골소실 유의하게 적음 — 3개월 (0.32 vs 0.56 mm) 및 6개월 (0.48 vs 0.82 mm, 모두 p<0.001); 양군 생존율 100%, 합병증 없음. 무피판 술식이 치유된 하악 구치부에서 조기 치조정 골소실 감소 이점 제공; 단, 6개월·2D·단일기관

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/tarpara-2025-flapless-flapped-clinical-outcomes-cohort]] — contradicts: a non-randomized 12-month cohort found no crestal-bone difference between flapless and flapped (only pain/early probing-depth benefit).
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 세줄: 전향적 RCT (n=40, 하악 구치부 치유된 치조제 단일치 임플란트, 1:1 무작위 배정: 무피판 펀치 vs 전층 점막골막 피판; 4.0 × 10 mm 임플란트; 6개월 치조정 골소실 방사선 평가). 무피판군이 피판군 대비 치조정 골소실 유의하게 적음 — 3개월 (0.32 vs 0.56 mm) 및 6개월 (0.48 vs 0.82 mm, 모두 p<0.001); 양군 생존율 100%, 합병증 없음. 무피판 술식이 치유된 하악 구치부에서 조기 치조정 골소실 감소 이점 제공; 단, 6개월·2D·단일기관

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants] (HIGH-far→paknejad-2017-flapless-immediate-implant-buccal-gap-rct, 'contradict' · 반박·충돌)
  - **근거 문장**: User requested a PubMed ingest on flapless implant placement. The wiki's flapless evidence is concentrated in the *immediate*-implant context ([[immediate-implant/pitman-2023-immediate-implant-flap-flapless-sr-ma]], [[immediate-implant/mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma]], [[immediate-implant/paknejad-2017-flapless-immediate-implant-buccal-gap-rct]]); this RCT addresses t
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 세줄: 전향적 RCT (n=40, 하악 구치부 치유된 치조제 단일치 임플란트, 1:1 무작위 배정: 무피판 펀치 vs 전층 점막골막 피판; 4.0 × 10 mm 임플란트; 6개월 치조정 골소실 방사선 평가). 무피판군이 피판군 대비 치조정 골소실 유의하게 적음 — 3개월 (0.32 vs 0.56 mm) 및 6개월 (0.48 vs 0.82 mm, 모두 p<0.001); 양군 생존율 100%, 합병증 없음. 무피판 술식이 치유된 하악 구치부에서 조기 치조정 골소실 감소 이점 제공; 단, 6개월·2D·단일기관

- `surendra-2025-flapless-versus-flapped-crestal-bone` [implants] (AMBIG→mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma, 'contradict' · 반박·충돌)
  - **근거 문장**: User requested a PubMed ingest on flapless implant placement. The wiki's flapless evidence is concentrated in the *immediate*-implant context ([[immediate-implant/pitman-2023-immediate-implant-flap-flapless-sr-ma]], [[immediate-implant/mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma]], [[immediate-implant/paknejad-2017-flapless-immediate-implant-buccal-gap-rct]]); this RCT addresses t
  - ▸ 출발(`surendra-2025-flapless-versus-flapped-crestal-bone`) 세줄: 전향적 RCT (n=40, 하악 구치부 치유된 치조제 단일치 임플란트, 1:1 무작위 배정: 무피판 펀치 vs 전층 점막골막 피판; 4.0 × 10 mm 임플란트; 6개월 치조정 골소실 방사선 평가). 무피판군이 피판군 대비 치조정 골소실 유의하게 적음 — 3개월 (0.32 vs 0.56 mm) 및 6개월 (0.48 vs 0.82 mm, 모두 p<0.001); 양군 생존율 100%, 합병증 없음. 무피판 술식이 치유된 하악 구치부에서 조기 치조정 골소실 감소 이점 제공; 단, 6개월·2D·단일기관

- `bento-2023-steel-versus-zirconia-drills-heat` [implants] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This material-pair signal qualifies (rather than contradicts) the broader chakraborty-2024 "drill material inconclusive" SR — both conclusions are compatible — but clinical translation requires zirconia drill fracture toughness and wear data before adoption.
  - ▸ 출발(`bento-2023-steel-versus-zirconia-drills-heat`) 세줄: SR+MA(Saudi Dent J 2024, PRISMA, 10편 in vitro): 지르코니아(Zr) drill vs 스테인리스스틸(SS) drill의 골내 온도 변화를 역분산(Inverse-variance) 풀링으로 비교. 지르코니아 drill이 SS drill보다 골내 온도 변화 유의하게 낮음(풀링 후 통계적 유의); 모든 근거는 in vitro. chakraborty-2024의 "drill 재질 결론 불가"와 양립 가능한 특정 material pair 신호 — 임상 적용 전 지르코니아 dr

- `tennert-2024-direct-vs-indirect-composite-longevity-sr-ma` ['resin'] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: All 5 RCTs were rated high risk of bias and evidence certainty was very low by GRADE — this finding contradicts earlier SR+MAs showing no difference, and robust long-term RCTs remain urgently needed.
  - ▸ 출발(`tennert-2024-direct-vs-indirect-composite-longevity-sr-ma`) 세줄: SR+MA (5개 RCT, 627 수복물, 279명; Bern, Dental Materials 2024; 검색 2024년 6월 업데이트): 구치부 영구치 직접 vs 간접 접착 합착형 복합레진 수명 비교(추적 ≥3년). 직접 수복이 간접 수복보다 유의하게 낮은 실패 위험(RR=0.61 [0.47; 0.79]); 간접 연간 실패율(Annual Failure Rate, AFR) 0–15.5% vs 직접 0–5.4%; 주요 실패 원인: 간접 파절/chipping, 직접 이차우식. 5개 RCT 모두 고위험

- `tennert-2024-direct-vs-indirect-composite-longevity-sr-ma` ['resin'] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 5개 RCT 모두 고위험 비뚤림, GRADE 근거 수준 매우 낮음 — 차이 없음을 보인 기존 SR+MA들과 상충하며, 신뢰할 수 있는 장기 RCT 시급.
  - ▸ 출발(`tennert-2024-direct-vs-indirect-composite-longevity-sr-ma`) 세줄: SR+MA (5개 RCT, 627 수복물, 279명; Bern, Dental Materials 2024; 검색 2024년 6월 업데이트): 구치부 영구치 직접 vs 간접 접착 합착형 복합레진 수명 비교(추적 ≥3년). 직접 수복이 간접 수복보다 유의하게 낮은 실패 위험(RR=0.61 [0.47; 0.79]); 간접 연간 실패율(Annual Failure Rate, AFR) 0–15.5% vs 직접 0–5.4%; 주요 실패 원인: 간접 파절/chipping, 직접 이차우식. 5개 RCT 모두 고위험

- `tian-2015-paucity-nanolayering-mdp-resin-dentin` [resin-bonding] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: **Clinically**: this is the principal counterpoint to the Yoshihara 2011 nanolayering hypothesis. It does not deny that 10-MDP can self-assemble into ordered nanolayers, but it shows the structure is **concentration-dependent and largely absent in the formulations dentists actually use**. The implication is that the durable, well-documented clinical performance of 10-MDP adhesives is more likely d
  - ▸ 출발(`tian-2015-paucity-nanolayering-mdp-resin-dentin`) 세줄: 상용 10-MDP 접착제 7종(TEM n=6, XRD n=4)과 실험용 15/10/5 wt% 10-MDP 프라이머를 인간 상아질에 적용한 in-vitro TEM·박막 XRD 연구. ~3.7 nm 주기의 풍부하고 규칙적인 나노레이어링(XRD 피크 2θ 2.40°/4.78°/7.18°)은 15 wt% 10-MDP에서만 나타났고 상용 접착제 7종 모두에서는 거의 관찰되지 않았다. 나노레이어링은 농도 의존적이며 임상 제품에서는 거의 없어, 10-MDP 접착제의 장기 임상 내구성은 나노레이어링보다 MDP–

- `tian-2015-paucity-nanolayering-mdp-resin-dentin` [resin-bonding] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[resin-bonding/yoshihara-2011-nanolayering-mdp-enamel-dentin]] — **refines / contradicts**: Yoshihara established 10-MDP nanolayering and tied it to bond durability; Tian shows commercial adhesives nanolayer sparsely, narrowing that hypothesis to high-concentration experimental systems.
  - ▸ 출발(`tian-2015-paucity-nanolayering-mdp-resin-dentin`) 세줄: 상용 10-MDP 접착제 7종(TEM n=6, XRD n=4)과 실험용 15/10/5 wt% 10-MDP 프라이머를 인간 상아질에 적용한 in-vitro TEM·박막 XRD 연구. ~3.7 nm 주기의 풍부하고 규칙적인 나노레이어링(XRD 피크 2θ 2.40°/4.78°/7.18°)은 15 wt% 10-MDP에서만 나타났고 상용 접착제 7종 모두에서는 거의 관찰되지 않았다. 나노레이어링은 농도 의존적이며 임상 제품에서는 거의 없어, 10-MDP 접착제의 장기 임상 내구성은 나노레이어링보다 MDP–

- `tian-2015-paucity-nanolayering-mdp-resin-dentin` [resin-bonding] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Direct counterpoint to the foundational nanolayering claim. [[wiki/resin-bonding/yoshihara-2011-nanolayering-mdp-enamel-dentin]] established that 10-MDP self-assembles into ordered nanolayers at the resin-dentin interface and hypothesized this drives bond durability. Tian et al. (2015) tested whether seven *commercialized* 10-MDP self-etch/universal adhesives actually reproduce this structure on h
  - ▸ 출발(`tian-2015-paucity-nanolayering-mdp-resin-dentin`) 세줄: 상용 10-MDP 접착제 7종(TEM n=6, XRD n=4)과 실험용 15/10/5 wt% 10-MDP 프라이머를 인간 상아질에 적용한 in-vitro TEM·박막 XRD 연구. ~3.7 nm 주기의 풍부하고 규칙적인 나노레이어링(XRD 피크 2θ 2.40°/4.78°/7.18°)은 15 wt% 10-MDP에서만 나타났고 상용 접착제 7종 모두에서는 거의 관찰되지 않았다. 나노레이어링은 농도 의존적이며 임상 제품에서는 거의 없어, 10-MDP 접착제의 장기 임상 내구성은 나노레이어링보다 MDP–

- `hong-2021-universal-adhesive-etching-modes-sr-ma` [resin-bonding] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 일반 수복에서 최적 유지율·변연 질이 목표일 때 유니버설 접착제의 E&R 방식이 권장됨 — 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL)에서 차이 없음을 보인 메타분석들과 대비되는 결과.
  - ▸ 출발(`hong-2021-universal-adhesive-etching-modes-sr-ma`) 세줄: PRISMA 체계적 문헌고찰+메타분석(PubMed·Cochrane·Embase, 2000년 1월~2020년 3월; 초기 2,516건; 13개 RCT 포함; RevMan 5.3.5): 임상 수복에서 유니버설 접착제의 산부식-세척(Etch-and-Rinse, E&R)과 자가산부식(Self-Etch, SE) 방식 비교. E&R이 유지율(OR 0.35; 95% CI 0.18–0.71; p=0.003), 변연적합도(OR 0.49; p<0.001), 변연착색(OR 0.49; p<0.001) 모두에서 SE보다

- `alghauli-2025-clinical-benefits-immediate-dentin-sealing` [resin-bonding] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The IDS-favorable POS result directly contradicts Josic 2022 SR+MA (4 studies, GRADE low: no difference). The two reviews likely differ in inclusion period (through 2021 vs through Dec 2023), study count (4 vs 11), and outcome definition. Clinical decisions should weigh: more recent and larger evidence base (Alghauli) vs more rigorous GRADE assessment (Josic).
  - ▸ 출발(`alghauli-2025-clinical-benefits-immediate-dentin-sealing`) 세줄: SR+MA (JPD 2025, 2023년 12월까지 검색) — 11개 임상 연구에서 즉시 상아질 피개 (IDS, Immediate Dentin Sealing) vs 비IDS(DDS/전통) 프로토콜의 간접 수복물 합병증·생존율·술후 과민증 비교. IDS 생존율 96.4–100% vs 비IDS 81.8–96.7%, 합병증 감소, 술후 과민증 (POS, Postoperative Sensitivity) 강도·발생률 유의 감소(P<0.05); 생존율 차이는 추적기간과 음의 상관; Josic 2022 SR+

- `mehanna-2021-proximal-contact-alterations-prospective` [food-impaction] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: food-impaction 카테고리의 단기 전향(3개월) 측정연구로 인제스트. [[food-impaction/pang-2017-prevalence-proximal-contact-loss-prospective]] 장기 데이터와 대비되는 조기 contact tightness 감소 동역학을 정량 제시하고, restoration type·implant system을 인자로 강조한다.
  - ▸ 출발(`mehanna-2021-proximal-contact-alterations-prospective`) 세줄: 3개월 전향연구(43명·구치부 IFP 43개·64 proximal contact): 장착 직후(T0)·1개월(T1)·3개월(T2)에 0.05 mm metal strip으로 접촉 강도 측정. T0→T2 접촉 강도 유의 감소; restoration type이 free-end의 mesial 소실(P=0.008)과 distal 소실(P<0.001)에 영향; implant system은 distal contact에만 영향(P=0.002). 접촉 소실은 기능 3개월 이내부터 측정 가능 — 조기 모니터링 지지

- `friele-2006-patient-expectations-fair-complaint` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Documents that only 7% want financial compensation -- contradicting the litigation-first assumption.
  - ▸ 출발(`friele-2006-patient-expectations-fair-complaint`) 세줄: 네덜란드 74개 병원 민원인 424명(응답률 75%) 횡단 설문: 민원 절차 시작 시점에 정의이론(justice theory)으로 공정한 절차·소통·결과 기대 측정. 재발 방지가 최우선 동기; 87%가 공정한 위원회 우선시; 설명이 중요하다는 응답 65% vs 사과 41%; 금전 보상 원하는 경우 7% 불과. 민원 응대는 사과나 금전 보상보다 공정한 절차·투명한 설명·조직 개선에 초점을 맞춰야 한다 — 이것이 민원인의 실제 기대이다.

- `friele-2006-patient-expectations-fair-complaint` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[complaint-management/mccreaddie-2021-qualitative-study-nhs-complaint]] -- contradicts: NHS responses violate these fairness expectations (fauxpology).
  - ▸ 출발(`friele-2006-patient-expectations-fair-complaint`) 세줄: 네덜란드 74개 병원 민원인 424명(응답률 75%) 횡단 설문: 민원 절차 시작 시점에 정의이론(justice theory)으로 공정한 절차·소통·결과 기대 측정. 재발 방지가 최우선 동기; 87%가 공정한 위원회 우선시; 설명이 중요하다는 응답 65% vs 사과 41%; 금전 보상 원하는 경우 7% 불과. 민원 응대는 사과나 금전 보상보다 공정한 절차·투명한 설명·조직 개선에 초점을 맞춰야 한다 — 이것이 민원인의 실제 기대이다.

- `elias-2025-successful-handling-patient-complaints` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[complaint-management/mccreaddie-2021-qualitative-study-nhs-complaint]] -- contradicts: teaches genuine empathy vs the fauxpology.
  - ▸ 출발(`elias-2025-successful-handling-patient-complaints`) 세줄: 환자경험 및 민원담당 직원을 위한 구조화 교육과정 CODE(Compassion·Operational Support·De-escalation·Empowerment)를 소개한 프로그램 기술 논문. CODE는 두 병행 트랙으로 구성: 트랙1 — 운영 시스템·자원 활용 절차 교육; 트랙2 — 공감·인간적 연결·긴장 완화를 위한 대인 커뮤니케이션 교육; 대조 효과 데이터는 보고하지 않음. 이중 구조는 민원 문헌에서 확인된 두 가지 실패 모드(관료적 처리 불량, 방어적 관계 실패)를 직접 겨냥한 전이 가능한

- `van-dael-2022-national-policies-complaint-handling` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[complaint-management/gillespie-2025-complaint-handlers-bind-defensive]] -- reinforces: policy generates the contradictory demands behind defensiveness.
  - ▸ 출발(`van-dael-2022-national-policies-complaint-handling`) 세줄: 대형 영국 NHS 트러스트에서 직원 20명 반구조 인터뷰 및 문서 분석을 통해 국가 민원처리 정책이 실제 지역 수준의 질 향상을 지원하는지 검토한 질적 사례연구. 4개 역기능 영역이 확인됐다: 혼란한 민원 경로, 학습이 아닌 '타당성' 심사 중심의 조사, 무용한 데이터 수집 시스템, 방어적 회피를 유도하는 역인센티브. 국가 민원정책의 실제 운영은 학습 중심 의도와 크게 괴리돼 있으며, 민원 시스템이 구조적으로 서비스 개선보다 기관 방어를 지향하고 있음을 보여준다.

- `mccreaddie-2021-qualitative-study-nhs-complaint` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[complaint-management/friele-2006-patient-expectations-fair-complaint]] -- contradicts: these responses violate complainants' fairness expectations.
  - ▸ 출발(`mccreaddie-2021-qualitative-study-nhs-complaint`) 세줄: 스코틀랜드 NHS 서면 민원 응답 59건 담화분석: 1개월 수집 60건 익명 민원·응답 코퍼스에서 응답이 불만을 어느 정도 실질적으로 다루는지 언어적으로 분석. 응답이 민원을 축소하는 4가지 담화 전략: 민원 제기 노력 무시·민원인 계정의 주관화·부주의/예외 상황으로 과실 완화·'fauxpology'("그렇게 느끼신다니 죄송합니다") 사용으로 책임 회피. 이 방어적 언어 패턴이 NHS 지역 민원의 미해결과 옴부즈만 인용의 원인 — 치과 진료에서도 적극적으로 피해야 할 응답 패턴 목록이다.

- `mccreaddie-2021-qualitative-study-nhs-complaint` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[complaint-management/elias-2025-successful-handling-patient-complaints]] -- contradicts: CODE training teaches the opposite (genuine de-escalation/empathy).
  - ▸ 출발(`mccreaddie-2021-qualitative-study-nhs-complaint`) 세줄: 스코틀랜드 NHS 서면 민원 응답 59건 담화분석: 1개월 수집 60건 익명 민원·응답 코퍼스에서 응답이 불만을 어느 정도 실질적으로 다루는지 언어적으로 분석. 응답이 민원을 축소하는 4가지 담화 전략: 민원 제기 노력 무시·민원인 계정의 주관화·부주의/예외 상황으로 과실 완화·'fauxpology'("그렇게 느끼신다니 죄송합니다") 사용으로 책임 회피. 이 방어적 언어 패턴이 NHS 지역 민원의 미해결과 옴부즈만 인용의 원인 — 치과 진료에서도 적극적으로 피해야 할 응답 패턴 목록이다.

- `gillespie-2025-complaint-handlers-bind-defensive` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Defensiveness is a structural product of contradictory demands (be transparent and open vs protect organisational reputation under workload pressure) rather than individual failing; resolving the 'bind' requires addressing contradictory organisational expectations.
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 세줄: 영국 병원 직원의 온라인 비판(Care Opinion) 응답을 대상으로 한 혼합방법 설명적 순차 연구: 방어 전술을 정량 코딩 후 원인 조직 긴장을 질적으로 설명. 6가지 방어 전술 신뢰성 있게 식별 — 다른 채널로 전환·문제 회피·우려의 심리화·불완전 주장 무효화·피드백 에피소드 종결·개인화 해결책 제시 — 모두 낮은 품질·학습 저하 응답과 연관. 방어성은 개인 결함이 아니라 '투명하게 하되 조직 명성도 보호하라'는 모순된 요구에서 비롯된 구조적 산물 — 해결은 조직적 기대 모순 해소에 있다.

- `gillespie-2025-complaint-handlers-bind-defensive` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Gillespie and Reader studied how UK hospital staff respond to online criticism and found six reliably-coded defensive tactics -- from redirecting and evading to psychologising and quietly closing the episode. Crucially, they show defensiveness is not mainly a personal flaw but a response to a structural 'bind': handlers are simultaneously asked to be transparent and to protect the organisation's r
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 세줄: 영국 병원 직원의 온라인 비판(Care Opinion) 응답을 대상으로 한 혼합방법 설명적 순차 연구: 방어 전술을 정량 코딩 후 원인 조직 긴장을 질적으로 설명. 6가지 방어 전술 신뢰성 있게 식별 — 다른 채널로 전환·문제 회피·우려의 심리화·불완전 주장 무효화·피드백 에피소드 종결·개인화 해결책 제시 — 모두 낮은 품질·학습 저하 응답과 연관. 방어성은 개인 결함이 아니라 '투명하게 하되 조직 명성도 보호하라'는 모순된 요구에서 비롯된 구조적 산물 — 해결은 조직적 기대 모순 해소에 있다.

- `gillespie-2025-complaint-handlers-bind-defensive` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Reframes defensiveness as a *structural* product of contradictory demands, not individual failing.
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 세줄: 영국 병원 직원의 온라인 비판(Care Opinion) 응답을 대상으로 한 혼합방법 설명적 순차 연구: 방어 전술을 정량 코딩 후 원인 조직 긴장을 질적으로 설명. 6가지 방어 전술 신뢰성 있게 식별 — 다른 채널로 전환·문제 회피·우려의 심리화·불완전 주장 무효화·피드백 에피소드 종결·개인화 해결책 제시 — 모두 낮은 품질·학습 저하 응답과 연관. 방어성은 개인 결함이 아니라 '투명하게 하되 조직 명성도 보호하라'는 모순된 요구에서 비롯된 구조적 산물 — 해결은 조직적 기대 모순 해소에 있다.

- `gillespie-2025-complaint-handlers-bind-defensive` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Six defensive tactics were reliably identified. They were generally associated with lower-quality engagement (less issue resolution, less learning). Defensiveness arose where handlers faced contradictory demands -- being responsive/transparent while also protecting organisational reputation and managing workload.
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 세줄: 영국 병원 직원의 온라인 비판(Care Opinion) 응답을 대상으로 한 혼합방법 설명적 순차 연구: 방어 전술을 정량 코딩 후 원인 조직 긴장을 질적으로 설명. 6가지 방어 전술 신뢰성 있게 식별 — 다른 채널로 전환·문제 회피·우려의 심리화·불완전 주장 무효화·피드백 에피소드 종결·개인화 해결책 제시 — 모두 낮은 품질·학습 저하 응답과 연관. 방어성은 개인 결함이 아니라 '투명하게 하되 조직 명성도 보호하라'는 모순된 요구에서 비롯된 구조적 산물 — 해결은 조직적 기대 모순 해소에 있다.

- `gillespie-2025-complaint-handlers-bind-defensive` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[complaint-management/elias-2025-successful-handling-patient-complaints]] -- contradicts: training + operational support as the remedy.
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 세줄: 영국 병원 직원의 온라인 비판(Care Opinion) 응답을 대상으로 한 혼합방법 설명적 순차 연구: 방어 전술을 정량 코딩 후 원인 조직 긴장을 질적으로 설명. 6가지 방어 전술 신뢰성 있게 식별 — 다른 채널로 전환·문제 회피·우려의 심리화·불완전 주장 무효화·피드백 에피소드 종결·개인화 해결책 제시 — 모두 낮은 품질·학습 저하 응답과 연관. 방어성은 개인 결함이 아니라 '투명하게 하되 조직 명성도 보호하라'는 모순된 요구에서 비롯된 구조적 산물 — 해결은 조직적 기대 모순 해소에 있다.

- `gillespie-2025-complaint-handlers-bind-defensive` [complaint-management] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Explains WHY responders default to the defensive moves catalogued in [[complaint-management/12913_2021_Article_6733]]: contradictory organisational demands. Moves the response axis from blaming individuals to fixing the system -- the lever a clinic owner actually controls.
  - ▸ 출발(`gillespie-2025-complaint-handlers-bind-defensive`) 세줄: 영국 병원 직원의 온라인 비판(Care Opinion) 응답을 대상으로 한 혼합방법 설명적 순차 연구: 방어 전술을 정량 코딩 후 원인 조직 긴장을 질적으로 설명. 6가지 방어 전술 신뢰성 있게 식별 — 다른 채널로 전환·문제 회피·우려의 심리화·불완전 주장 무효화·피드백 에피소드 종결·개인화 해결책 제시 — 모두 낮은 품질·학습 저하 응답과 연관. 방어성은 개인 결함이 아니라 '투명하게 하되 조직 명성도 보호하라'는 모순된 요구에서 비롯된 구조적 산물 — 해결은 조직적 기대 모순 해소에 있다.

- `allison-2024-bioaerosols-airborne-transmission-dental-clinic` [dental-handpiece] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 치과 bioaerosol 생물학·에어로졸 물리학·감염관리 근거를 종합한 서술적 리뷰 — 5 µm 이하만 공기전파된다는 통념을 반박(최대 100 µm 부유·2 m 초과 이동)하고 통제수단별 효과 크기를 정리.
  - ▸ 출발(`allison-2024-bioaerosols-airborne-transmission-dental-clinic`) 세줄: 치과 bioaerosol 생물학·에어로졸 물리학·감염관리 근거를 종합한 서술적 리뷰 — 5 µm 이하만 공기전파된다는 통념을 반박(최대 100 µm 부유·2 m 초과 이동)하고 통제수단별 효과 크기를 정리. 에어터빈은 조용한 호흡 대비 세균 CFU ~1000배, 재채기 2배 분산; 러버댐 바이러스 에어로졸 92–100% 감소; 고용량 흡인 80–90%; 국소배기 89–93%; 10회/h 환기로 소형 에어로졸 ~30분 내 제거. 5 µm 이분법 무효 — 환자별 위험층화 + 3단계 통제체계(생성감소→

- `wang-2025-crown-vs-porcelain-inlay-cracked-teeth-rct` [cracked-tooth] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 추적 최대 6개월·초록만·DOI 없음·중국어로 일반화 제한; 보존적 관내 수복이 교두피개를 능가한다는 방향은 균열치 주류 문헌과 상충하므로 단독 근거로 임상 변경 불가.
  - ▸ 출발(`wang-2025-crown-vs-porcelain-inlay-cracked-teeth-rct`) 세줄: 전향적 RCT (n=106, 각 53명, 근관치료 후 균열치, 2020-12~2023-12) 포세린 인레이 vs 전부피개관(full crown) 비교; 초록만 확보된 중국어 논문. 포세린 인레이 군이 VAS 통증(1/3/7일: 4.43/3.15/2.04 vs 4.86/3.81/2.86), 6개월 치은지수(GI·PLI·BI·PD), 저작효율(92.57% vs 84.26%), 교합력(143.54 vs 125.36 lbs) 모두에서 유의하게 우수(모두 P<0.05). 추적 최대 6개월·초록만·DOI 없

- `jiang-2024-orofacial-pain-sleep-biobank` [tmj] (HIGH-no-target, 'contrary to' · 상반된 결과)
  - **근거 문장**: - Identifies long sleep duration (not short sleep, contrary to common clinical assumption) as the causally robust risk factor for TMD-related pain after adjusting for metabolic confounders (BMI, T2D).
  - ▸ 출발(`jiang-2024-orofacial-pain-sleep-biobank`) 세줄: 영국 바이오뱅크(UK Biobank) 참가자 196,490명의 단면연구와 GWAS 자료 기반 양방향·다변량 멘델리안 무작위화(Mendelian randomization, MR) 분석(측두하악장애(TMD) 관련 통증 n=377,277; 비정형 안면통 n=331,749; 9개 수면 형질 GWAS)을 결합했다. 전신 통증군은 불량한 수면 패턴과 연관됐고(OR=1.18, p<0.001), 만성 구강안면통증 위험은 수면시간과 비선형 관계(p=0.032, 하루 9시간 이상에서 위험 증가)를 보였으며, MR 

- `aggarwal-2026-third-molar-extraction-tmj-pain` [tmj] (HIGH-no-target, 'counter to' · 반대)
  - **근거 문장**: The headline quantitative result is a pooled RR/OR of 0.49 (95% CI 0.31-0.66, p<0.00001, I2=34%) — extraction patients were about 51% less likely to report TMJ pain/symptoms than non-extraction controls. This runs counter to several earlier reviews (e.g., Damasceno et al., pooled OR 1.81-2.15) that concluded extraction increases TMD risk. The reversal is driven largely by inclusion of therapeutic-
  - ▸ 출발(`aggarwal-2026-third-molar-extraction-tmj-pain`) 세줄: PRISMA 2020 기반 체계적 문헌고찰+메타분석(PROSPERO 등록)으로, 발치(주로 제3대구치)와 TMJ 통증/TMD 증상의 관계를 다룬 8편(RCT 2, 전향적 코호트 1, 후향적/매칭 코호트 2, 단면연구 2, SR 1편; n=42~34,000명 이상)을 분석했다. 6편의 정량 메타분석 결과 발치군이 비발치군 대비 TMJ 통증/증상 위험이 유의하게 낮았다(pooled RR/OR=0.49, 95% CI 0.31-0.66, p<0.00001, I2=34%) — 발치군이 약 51% 덜 통증을

- `chen-2022-interpretation-hba1c-analytical-methodology-hematology` [drug/systemic-disease] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Discordance protocol**: when HbA1c contradicts fingerstick or clinical impression, treat HbA1c as suspect; do not delay urgent extraction in clearly symptomatic infection based on isolated high HbA1c.
  - ▸ 출발(`chen-2022-interpretation-hba1c-analytical-methodology-hematology`) 세줄: 서술적 고찰(Exp Ther Med 2022, Kunming Medical Univ) — PubMed·Embase·Web of Science·Cochrane·CNKI 검색 기반으로 HbA1c 간섭을 3축(① 측정법 특이 변이체·유도체 ② 생화학적 글리케이션 속도 ③ 적혈구 수명 변화)으로 체계화; 측정법(IEC·BAC·CE·IA·효소법) × Hb 변이체 교차표로 각 조건별 위양성·위음성 방향을 카탈로그화. 적혈구 수명 단축(용혈성빈혈·G6PD 결핍·수혈 3개월 내·임신 말기·EPO 치료)→HbA1

- `khalilurrahman-2026-raas-inhibitor-statin-periodontal-status-sr-ma` [drug/systemic-disease] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This systematic review and meta-analysis (PRISMA 2020, PROSPERO CRD42024583905) synthesized evidence on how two major classes of cardiovascular medication — RAAS inhibitors (ACEI/ARB, used for hypertension) and statins (used for hypercholesterolemia) — affect periodontal status. Searching PubMed, ProQuest, EBSCO, and SpringerLink yielded 6,669 records, narrowed to 6 studies for qualitative synthes
  - ▸ 출발(`khalilurrahman-2026-raas-inhibitor-statin-periodontal-status-sr-ma`) 세줄: 심혈관질환 위험군(고혈압·고콜레스테롤혈증) 환자의 RAAS 억제제(ACEI/ARB)·스타틴 복용이 치주 상태에 미치는 영향을 평가한 SR+MA(정성분석 6편, 메타분석 4편, PROSPERO CRD42024583905). RAAS 억제제는 고혈압 환자의 치주 상태에 비일관적 영향(2편만 존재, 효과 판정 불가)을 보였고, 스타틴은 고콜레스테롤혈증 환자의 출혈지수(BOP, -13.4%, p=0.007)와 치주낭깊이(PD, -0.38mm, p<0.00001)를 유의하게 개선했으나 PD 변화의 임상적 

- `esposito-2013-antibiotics-dental-implant-placement-cochrane` [drug/antibiotics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[drug/antibiotics/momand-2024-antibiotic-prophylaxis-early-implant-failure]] — 2024 SR+MA restricted to placebo-controlled/double-blind/low-RoB RCTs only; contradicts this review's significant finding (RR 0.66 NS, NNT 143) — see supersession banner.
  - ▸ 출발(`esposito-2013-antibiotics-dental-implant-placement-cochrane`) 세줄: 코크란 체계적 문헌고찰+메타분석(2013년 6월 17일까지 검색): RCT 6편, 참여자 1162명 — 임플란트 식립 시 예방적 항생제 vs 위약/무투여 비교. 항생제(전부 아목시실린 계열; 대부분 술전 단일 2g 또는 3g 경구 투여) 투여 시 임플란트 실패가 유의하게 감소(RR 0.33, 95% CI 0.16–0.67, P=0.002, I²=0%; NNTB=25); 보철물 실패는 경계선 유의(RR 0.44, 95% CI 0.19–1.00); 술후 감염·이상반응은 유의차 없음. 근거는 중등도 질

- `momand-2024-antibiotic-prophylaxis-early-implant-failure` [drug/antibiotics] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 위약대조 이중맹검 RCT 7편만 포함한 SR+MA(환자 1859명/임플란트 3014개; PROSPERO CRD42021292610): 기존 SR+MA들이 비맹검·고위험-비뚤림 연구를 포함해 상충된 결론을 낸 한계를 방법론적으로 극복.
  - ▸ 출발(`momand-2024-antibiotic-prophylaxis-early-implant-failure`) 세줄: 위약대조 이중맹검 RCT 7편만 포함한 SR+MA(환자 1859명/임플란트 3014개; PROSPERO CRD42021292610): 기존 SR+MA들이 비맹검·고위험-비뚤림 연구를 포함해 상충된 결론을 낸 한계를 방법론적으로 극복. 술전 항생제 예방이 조기 임플란트 실패를 유의하게 줄이지 못함(RR 0.66, 95% CI 0.30–1.47; 위험차 −0.007; NNT 143); GRADE 중간; 즉시 발치 후 임플란트 제외 분석에서 방향 역전(RR 1.10) → 항생제 효과는 발치 후 즉시 식

- `momand-2024-antibiotic-prophylaxis-early-implant-failure` [drug/antibiotics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[drug/antibiotics/torof-2023-antibiotic-dental-implant-procedures-sr-ma]] — contradicts (earlier SR+MA recommended preoperative single-dose amoxicillin; this placebo-RCT-only analysis finds no significant benefit)
  - ▸ 출발(`momand-2024-antibiotic-prophylaxis-early-implant-failure`) 세줄: 위약대조 이중맹검 RCT 7편만 포함한 SR+MA(환자 1859명/임플란트 3014개; PROSPERO CRD42021292610): 기존 SR+MA들이 비맹검·고위험-비뚤림 연구를 포함해 상충된 결론을 낸 한계를 방법론적으로 극복. 술전 항생제 예방이 조기 임플란트 실패를 유의하게 줄이지 못함(RR 0.66, 95% CI 0.30–1.47; 위험차 −0.007; NNT 143); GRADE 중간; 즉시 발치 후 임플란트 제외 분석에서 방향 역전(RR 1.10) → 항생제 효과는 발치 후 즉시 식

- `momand-2024-antibiotic-prophylaxis-early-implant-failure` [drug/antibiotics] (HIGH-far→uesugi-2024-risk-factors-early-failure-all-on-four, '대비되는' · 대비)
  - **근거 문장**: 조기 임플란트 실패 surveillance 배치에서 "예방 가능한가?"라는 개입 측 질문을 담당하는 최신 SR+MA. 위험인자 코호트인 [[implants/yari-2023-risk-factors-early-implant-failure]]·[[implants/uesugi-2024-risk-factors-early-failure-all-on-four]]가 흡연·해부·로딩을 강조하는 반면, 본 연구는 항생제 예방이 조기 실패를 거의 줄이지 못함(NNT 143)을 보여 개입 우선순위를 재정렬한다. 기존 [[drug/antibiotics/torof-2023-antibiotic-dental-implant-procedures-sr-ma]](술전 단일 amoxicillin 권고)와 대비되는 결과 — placebo-RCT
  - ▸ 출발(`momand-2024-antibiotic-prophylaxis-early-implant-failure`) 세줄: 위약대조 이중맹검 RCT 7편만 포함한 SR+MA(환자 1859명/임플란트 3014개; PROSPERO CRD42021292610): 기존 SR+MA들이 비맹검·고위험-비뚤림 연구를 포함해 상충된 결론을 낸 한계를 방법론적으로 극복. 술전 항생제 예방이 조기 임플란트 실패를 유의하게 줄이지 못함(RR 0.66, 95% CI 0.30–1.47; 위험차 −0.007; NNT 143); GRADE 중간; 즉시 발치 후 임플란트 제외 분석에서 방향 역전(RR 1.10) → 항생제 효과는 발치 후 즉시 식

- `torof-2023-antibiotic-dental-implant-procedures-sr-ma` [drug/antibiotics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Demonstrates that postoperative course offers no incremental benefit — directly contradicts widespread 7-day post-op courses.
  - ▸ 출발(`torof-2023-antibiotic-dental-implant-procedures-sr-ma`) 세줄: PRISMA-P/PROSPERO 등록 SR+MA(Wolverhampton; Medicina 2023): 임플란트 식립(Dental Implant Placement, DIP) 항생제 예방의 술전 vs 술후 요법 RCT 근거 평가. 술전 단일 amoxicillin 2g → 초기 임플란트 실패 감소; 술후 항생제 연장은 추가 이득 없음; 페니실린 알레르기 대안은 clindamycin 600mg 단일 투여. 임플란트 식립 후 통상적 5–7일 항생제 처방은 근거 없음; 대부분의 데이터가 단순 단일 임플란트

- `feldman-2023-metronidazole-disulfiram-reaction-case-control` [drug/antibiotics] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: A retrospective case-control chart review at a single Milwaukee academic ED (Dec 2010–Dec 2020) tested whether metronidazole actually causes a disulfiram-like reaction when ethanol is present. 36 patients (18 metronidazole + ethanol vs 18 ethanol-only matched on age, sex, and ethanol concentration) were compared for documented disulfiram-like effects (nausea, vomiting, flushing, tachycardia, hyper
  - ▸ 출발(`feldman-2023-metronidazole-disulfiram-reaction-case-control`) 세줄: 후향적 응급실(ED) case-control 차트 리뷰(n=36; 메트로니다졸(Metronidazole)+알코올 18명 vs 연령·성별·알코올 농도 매칭 대조 18명; Milwaukee 단일기관 10년). 메트로니다졸 환자 중 디설피람 유사 반응(Disulfiram-like Reaction) 기록 0건; 고혈압은 오히려 유의하게 적음(16.7% vs 61.1%, P<0.0001), 기타 지표 유의차 없음. "메트로니다졸 복용 중 금주" 권고는 근거가 취약하며, 혐기성·치성 감염에서 메트로니다졸이 

- `low-2026-dental-antibiotic-prescribing-practices-singapore` [drug/antibiotics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[drug/antibiotics/de-angelis-2025-antibiotic-third-molar-extraction-prevention-sr]] — evidence base contradicting the 71.2% routine third-molar prophylaxis seen here.
  - ▸ 출발(`low-2026-dental-antibiotic-prescribing-practices-singapore`) 세줄: 싱가포르 치과의사 280명 단면조사(2024; 전체 치과의사 ~10.4%): 싱가포르 최초 치과 항생제 처방·지식·태도 종합 연구; 임상 시나리오별 가이드라인 준수율로 적절성 평가. 적절한 처방률이 임상상황별 6.5~97.7%로 극단적 편차(치주 30.4%·구강외과 34.0% 최저); 예방적 항생제 과처방이 가장 심각 — 건강 환자 사랑니 발치 후 71.2%·임플란트 전 73.5% 불필요 처방; 항균제 내성(Antimicrobial Resistance, AMR) 기전 지식 전반적 부족(59.3% 

- `luo-2018-nsaids-osteogenic-activity-osseointegration-sr` [drug/analgesics] (HIGH-no-target, 'COUNTERPOINT' · 반대 논점)
  - **근거 문장**: This is the PRISMA/PROSPERO systematic review that provides the crucial COUNTERPOINT to the animal/in-vitro alarm about NSAIDs and osseointegration: human clinical studies show no effect while experimental animal and in vitro studies show impairment, and it frames the effect along a dose / duration / COX-2-selectivity axis. It balances the overview and directly complements the narrative review in 
  - ▸ 출발(`luo-2018-nsaids-osteogenic-activity-osseointegration-sr`) 세줄: 체계적 문헌고찰 (PRISMA; PROSPERO CRD42016051448; 1999-2018 Ovid/PubMed/Scopus/Web of Science 검색; 875편 → 전문 79편 → 13편 포함: in vitro 2·RCT 2+후향 1·동물 7; 이질성으로 메타분석 없음)이 비스테로이드소염제 (Non-Steroidal Anti-Inflammatory Drugs, NSAIDs)의 골유착 (Osseointegration) 영향을 종합. 인체 임상연구에서는 골유착이 NSAIDs로 부정적 영향을

- `watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma` [drug/analgesics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This directly contradicts long-standing opioid combination prescribing patterns for routine third molar surgery and is a key evidence base for the ADA 2022 acute dental pain guidelines on opioid sparing.
  - ▸ 출발(`watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma`) 세줄: SR+MA (Pain Med 2022): 제3대구치 발치 후 통증에서 아세트아미노펜 600 mg + 코데인 60 mg 병용 vs 이부프로펜 400 mg 단독을 무작위·맹검·위약대조 RCT만 대상으로 비교. 이부프로펜 400 mg 단독이 APAP+코데인 병용과 동등하거나 우수하고 오피오이드 부작용을 피할 수 있음. 제3대구치 수술에 대한 오피오이드 병용 처방 관행을 정면으로 반박 — ADA 2022 급성 치과 통증 opioid sparing 가이드라인의 핵심 근거.

- `watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma` [drug/analgesics] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 제3대구치 수술에 대한 오피오이드 병용 처방 관행을 정면으로 반박 — ADA 2022 급성 치과 통증 opioid sparing 가이드라인의 핵심 근거.
  - ▸ 출발(`watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma`) 세줄: SR+MA (Pain Med 2022): 제3대구치 발치 후 통증에서 아세트아미노펜 600 mg + 코데인 60 mg 병용 vs 이부프로펜 400 mg 단독을 무작위·맹검·위약대조 RCT만 대상으로 비교. 이부프로펜 400 mg 단독이 APAP+코데인 병용과 동등하거나 우수하고 오피오이드 부작용을 피할 수 있음. 제3대구치 수술에 대한 오피오이드 병용 처방 관행을 정면으로 반박 — ADA 2022 급성 치과 통증 opioid sparing 가이드라인의 핵심 근거.

- `watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma` [drug/analgesics] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This evidence directly contradicts the long-standing US prescribing pattern of opioid combination products for routine third molar pain and supports the modern opioid-sparing dental prescribing position (ADA 2022 acute dental pain guidelines).
  - ▸ 출발(`watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma`) 세줄: SR+MA (Pain Med 2022): 제3대구치 발치 후 통증에서 아세트아미노펜 600 mg + 코데인 60 mg 병용 vs 이부프로펜 400 mg 단독을 무작위·맹검·위약대조 RCT만 대상으로 비교. 이부프로펜 400 mg 단독이 APAP+코데인 병용과 동등하거나 우수하고 오피오이드 부작용을 피할 수 있음. 제3대구치 수술에 대한 오피오이드 병용 처방 관행을 정면으로 반박 — ADA 2022 급성 치과 통증 opioid sparing 가이드라인의 핵심 근거.

- `zingel-2025-nsaids-cardiovascular-risk-inflammatory-arthritis` [drug/analgesics] (HIGH-no-target, 'In contrast to' · 대조)
  - **근거 문장**: In contrast to the general population, NSAIDs do NOT increase cardiovascular risk in RA/AS patients and may be cardioprotective by reducing the elevated systemic inflammatory burden inherent to these diseases.
  - ▸ 출발(`zingel-2025-nsaids-cardiovascular-risk-inflammatory-arthritis`) 세줄: 서술적 고찰 (Semin Arthritis Rheum 2025): 오슬로 RA 레지스트리 등 관찰 데이터로 염증성 관절염(RA·AS) 환자에서 NSAIDs의 심혈관 위험 검토. 일반 인구와 달리 RA·AS 환자에서 NSAIDs는 심혈관 위험을 증가시키지 않으며, 전신 염증 부담 억제를 통해 심보호 효과 가능성 있음. 치과 처방 실무에서 RA·AS 환자에게 술후 통증 관리를 위한 NSAID 처방 시 일반 인구 기반 CV 위험 데이터를 과도하게 적용하는 것은 근거 없음.

- `chatzopoulos-2025-nsaid-early-dental-implant-failure-cohort` [drug/analgesics] (HIGH-no-target, 'conflicting finding' · 상충 결과)
  - **근거 문장**: The role of NSAIDs in osseointegration has long been debated, with conflicting findings from animal models and small human trials. This large-scale retrospective cohort used an electronic health record (EHR) database to test whether use of common NSAIDs is associated with early dental implant failure — defined as implant removal within six months of placement — in a real-world population of 12,943
  - ▸ 출발(`chatzopoulos-2025-nsaid-early-dental-implant-failure-cohort`) 세줄: 전자의무기록(Electronic Health Record, EHR) 기반 후향코호트로 12,943명 환자·49,997개 임플란트를 분석했다 (비스테로이드소염제(NSAID)군 n=3133 vs 대조군 n=9810), 1차 결과는 조기 임플란트 실패(식립 6개월 내 제거)다. 연령·성별·당뇨·골다공증 보정 후, 이부프로펜(Ibuprofen)은 임플란트 수준(교차비(Odds Ratio, OR) 2.29)·환자 수준(OR 2.87) 모두 조기 실패를 높였고, 나프록센(Naproxen)은 임플란트 수준(O

- `etikala-2019-nsaids-periodontal-implant-therapy-review` [drug/analgesics] (HIGH-no-target, 'conflicting result' · 상충 결과)
  - **근거 문장**: NSAIDs produce conflicting results for periodontal wound healing (no clear conclusion); selective COX-2 inhibitors specifically inhibit bone formation around implants in animal models; human clinical evidence is poor and conflicting.
  - ▸ 출발(`etikala-2019-nsaids-periodontal-implant-therapy-review`) 세줄: 서술적 고찰(Compend 2019; 치주 임상연구 9편 + 동물연구 4편 + 임플란트 인체 임상연구 2편): NSAIDs가 치주 창상 치유 및 임플란트 골유착(Osseointegration)에 미치는 영향 검토. 치주 창상 치유에 대한 NSAIDs 결과 상충(명확한 결론 없음); 선택적 COX-2 억제제는 동물모델에서 임플란트 주위 골형성 억제; 인체 임상 근거 부족·상충. 임플란트 시술 후 NSAID 처방 시 골유착 영향 인지 필요; 신선 임플란트 부위에서 acetaminophen 우선 또는 

- `etikala-2019-nsaids-periodontal-implant-therapy-review` [drug/analgesics] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 치주 창상 치유에 대한 NSAIDs 결과 상충(명확한 결론 없음); 선택적 COX-2 억제제는 동물모델에서 임플란트 주위 골형성 억제; 인체 임상 근거 부족·상충.
  - ▸ 출발(`etikala-2019-nsaids-periodontal-implant-therapy-review`) 세줄: 서술적 고찰(Compend 2019; 치주 임상연구 9편 + 동물연구 4편 + 임플란트 인체 임상연구 2편): NSAIDs가 치주 창상 치유 및 임플란트 골유착(Osseointegration)에 미치는 영향 검토. 치주 창상 치유에 대한 NSAIDs 결과 상충(명확한 결론 없음); 선택적 COX-2 억제제는 동물모델에서 임플란트 주위 골형성 억제; 인체 임상 근거 부족·상충. 임플란트 시술 후 NSAID 처방 시 골유착 영향 인지 필요; 신선 임플란트 부위에서 acetaminophen 우선 또는 

- `etikala-2019-nsaids-periodontal-implant-therapy-review` [drug/analgesics] (HIGH-no-target, 'conflicting result' · 상충 결과)
  - **근거 문장**: Narrative literature review addressing two clinical questions: (1) how do NSAIDs affect periodontal wound healing? (2) do NSAIDs affect osseointegration of dental implants? 9 clinical studies on periodontal healing showed conflicting results — no clear conclusion. For dental implant osseointegration, 4 animal studies and 2 human clinical studies were reviewed; selective COX-2 inhibitors specifical
  - ▸ 출발(`etikala-2019-nsaids-periodontal-implant-therapy-review`) 세줄: 서술적 고찰(Compend 2019; 치주 임상연구 9편 + 동물연구 4편 + 임플란트 인체 임상연구 2편): NSAIDs가 치주 창상 치유 및 임플란트 골유착(Osseointegration)에 미치는 영향 검토. 치주 창상 치유에 대한 NSAIDs 결과 상충(명확한 결론 없음); 선택적 COX-2 억제제는 동물모델에서 임플란트 주위 골형성 억제; 인체 임상 근거 부족·상충. 임플란트 시술 후 NSAID 처방 시 골유착 영향 인지 필요; 신선 임플란트 부위에서 acetaminophen 우선 또는 

- `etikala-2019-nsaids-periodontal-implant-therapy-review` [drug/analgesics] (HIGH-no-target, 'conflicting result' · 상충 결과)
  - **근거 문장**: - Periodontal healing: NSAIDs produce conflicting results; not established as harmful or helpful
  - ▸ 출발(`etikala-2019-nsaids-periodontal-implant-therapy-review`) 세줄: 서술적 고찰(Compend 2019; 치주 임상연구 9편 + 동물연구 4편 + 임플란트 인체 임상연구 2편): NSAIDs가 치주 창상 치유 및 임플란트 골유착(Osseointegration)에 미치는 영향 검토. 치주 창상 치유에 대한 NSAIDs 결과 상충(명확한 결론 없음); 선택적 COX-2 억제제는 동물모델에서 임플란트 주위 골형성 억제; 인체 임상 근거 부족·상충. 임플란트 시술 후 NSAID 처방 시 골유착 영향 인지 필요; 신선 임플란트 부위에서 acetaminophen 우선 또는 

- `ruggiero-2022-aaoms-mronj-position-paper-update` [drug/mronj] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - No RCT data sufficient to support or refute
  - ▸ 출발(`ruggiero-2022-aaoms-mronj-position-paper-update`) 세줄: AAOMS 2022 MRONJ 포지션 페이퍼(4판) — 2014년 진단 기준·스테이징 유지, romosozumab 위험 약제 추가, CTX 임상 권고 삭제, 데노수맙 drug holiday timing 구체화. Drug holiday 관련 AAOMS 내부 합의 불발(동등 의견 분열); 데노수맙 holiday 선택 시 마지막 투여 3–4개월 후 수술, 술 후 6–8주에 재투여 — 반동성 척추 골절 위험 주의. 임상적 의미: 항흡수제 투여 전 치과 처치 완료가 가장 근거 있는 예방법; 악성종양 적응증

- `patrono-2024-low-dose-aspirin-prevention-atherosclerotic` [drug/anticoagulants] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 혈소판 COX-1 Ser-529의 비가역적 아세틸화로 TXA2 억제(매일 투여 시 ID50 26 mg → ~3 mg); 일부 2차예방 데이터 RR 0.52, NNT 10; 위장관 출혈 증가·대장 선종 재발 감소 상충.
  - ▸ 출발(`patrono-2024-low-dose-aspirin-prevention-atherosclerotic`) 세줄: 저용량 아스피린(75–100 mg/일)에 관한 30년 근거를 통합한 State-of-the-Art 종설(European Heart Journal 2024): 기전·약동·심혈관 효능·안전성·화학예방 포함; Antiplatelet Trialists' Collaboration(145 RCT)과 ASPREE·ARRIVE·ASCEND 기반. 혈소판 COX-1 Ser-529의 비가역적 아세틸화로 TXA2 억제(매일 투여 시 ID50 26 mg → ~3 mg); 일부 2차예방 데이터 RR 0.52, NNT 1

- `mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma` [implants/peri-implantitis] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: KM insufficiency is an independent peri-implantitis risk factor even in regularly maintained patients, contradicting the view that maintenance compensates for tissue deficiency; GRADE certainty is moderate, limited by the cross-sectional design of most included studies.
  - ▸ 출발(`mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma`) 세줄: PROSPERO CRD42022319868; 22편 SR+MA(환자 4,044명, 임플란트 13,265개; 2006–2021; PubMed + Scopus) — 각화점막(Keratinized Mucosa, KM) 부족이 임플란트주위염 위험을 독립적으로 증가시키는지 검토. 전체 통합 오즈비(Odds Ratio, OR) 2.78(95% CI 2.07–3.74; I²=52%)이었으며, 5가지 하위군 분석에서 모두 유의하게 유지됨: 표준화 진단 기준 하위군(OR=1.96; I²=0%), 고정 보철 한정(

- `mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma` [implants/peri-implantitis] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Underscored that even patients under regular implant maintenance with inadequate KM carry elevated peri-implantitis risk (OR=2.08), contradicting the view that maintenance compensates for tissue deficiency.
  - ▸ 출발(`mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma`) 세줄: PROSPERO CRD42022319868; 22편 SR+MA(환자 4,044명, 임플란트 13,265개; 2006–2021; PubMed + Scopus) — 각화점막(Keratinized Mucosa, KM) 부족이 임플란트주위염 위험을 독립적으로 증가시키는지 검토. 전체 통합 오즈비(Odds Ratio, OR) 2.78(95% CI 2.07–3.74; I²=52%)이었으며, 5가지 하위군 분석에서 모두 유의하게 유지됨: 표준화 진단 기준 하위군(OR=1.96; I²=0%), 고정 보철 한정(

- `diaz-2022-what-is-the-prevalence` [implants/peri-implantitis] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: Fills a 5-year currency gap against the older epidemiology anchor [[wiki/implants/derks-2015-peri-implant-health-disease-epidemiology]]: a 57-study SR+MA (search window through Dec 2021) that re-estimates peri-implantitis prevalence and quantifies how case definition, probing-depth use, and function time move the number. It refines, not overturns, the older anchor by showing the estimate is still 
  - ▸ 출발(`diaz-2022-what-is-the-prevalence`) 세줄: 임플란트주위염 유병률을 추정한 57편 SR+MA(PROSPERO CRD42022313472; 기능기간 ≥5년 연구; 2005–2021년) — 환자 단위·임플란트 단위 분석. 유병률은 환자 단위 19.53%(95% CI 12.87–26.19), 임플란트 단위 12.53%(95% CI 11.67–13.39); 탐침깊이(Probing Depth, PD)를 진단 기준에 포함하면 환자 단위 유병률이 24.69%로 상승(미포함 17.56%). 진단 정의에 따른 의존성이 매우 높아, 주요 하위군(BOP + P

- `sbricoli-2026-peri-implant-disease-prevalence-type2-diabetes` [implants/peri-implantitis] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/peri-implantitis/diaz-2022-what-is-the-prevalence]] — contradicts: this T2DM-vs-non-DM null result tempers the systemic-risk-factor framing of peri-implantitis prevalence.
  - ▸ 출발(`sbricoli-2026-peri-implant-disease-prevalence-type2-diabetes`) 세줄: 단일기관 횡단연구 (70명·임플란트 227개; 제2형 당뇨 35명 vs 비당뇨 35명) — EFP S3 진단기준을 사용해 조절된 당뇨환자와 비당뇨환자의 임플란트 주위 질환 유병률 비교. 임플란트 주위 질환 (80% vs 77%, p=0.99)·점막염 (Mucositis, 51% vs 63%, p=0.47)·주위염 (Peri-implantitis, 51% vs 43%, p=0.63) 모두 피험자 및 임플란트 수준에서 유의차 없음. 검정력 부족(실제 ~50% 주위염 vs 계획 8%) + 양 군 치주염

- `sbricoli-2026-peri-implant-disease-prevalence-type2-diabetes` [implants/peri-implantitis] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Most existing peri-implantitis pages in our wiki frame T2DM as an established systemic risk factor and focus on keratinized mucosa, prosthetic design, and surface decontamination. This Italian single-center cross-sectional study (Sbricoli 2026) provides a direct **T2DM vs non-DM head-to-head prevalence** data point that *contradicts* the prevailing "diabetes as major risk factor" narrative — findi
  - ▸ 출발(`sbricoli-2026-peri-implant-disease-prevalence-type2-diabetes`) 세줄: 단일기관 횡단연구 (70명·임플란트 227개; 제2형 당뇨 35명 vs 비당뇨 35명) — EFP S3 진단기준을 사용해 조절된 당뇨환자와 비당뇨환자의 임플란트 주위 질환 유병률 비교. 임플란트 주위 질환 (80% vs 77%, p=0.99)·점막염 (Mucositis, 51% vs 63%, p=0.47)·주위염 (Peri-implantitis, 51% vs 43%, p=0.63) 모두 피험자 및 임플란트 수준에서 유의차 없음. 검정력 부족(실제 ~50% 주위염 vs 계획 8%) + 양 군 치주염

- `kim-2025-toothpick-method-cibotium-peri-implant-mucositis-rct` [implants/peri-implantitis] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: RCT (Kim 2025, n=60) that uses the **toothpick method (TPM)** of professional toothbrushing as the mechanical delivery vehicle for a natural Cibotium barometz (CB) extract to treat peri-implant mucositis — the first study to combine TPM with a natural anti-inflammatory agent against PIM-related bacteria, extending the toothpick method into peri-implant maintenance. Reinforces [[implants/peri-impla
  - ▸ 출발(`kim-2025-toothpick-method-cibotium-peri-implant-mucositis-rct`) 세줄: 이중맹검 RCT(n=60; 부산, 한국; 2023년 1–7월) — 기계적 전달 방식(토스픽 방법, Toothpick Method, TPM)을 세 군 모두 동일하게 유지하고 화학 제제만 변경(Cibotium barometz(CB) 추출물·0.12% 클로르헥시딘·생리식염수)하여 임플란트주위 점막염 환자에 적용. CB-TPM만이 타액 잠혈을 유의하게 감소(Cohen's d = 1.148; p<0.001)시켰으며 — 생리식염수 군은 오히려 증가 — P. micra·T. forsythia·P. interm

- `monje-2025-surgical-implant-factors-peri-implant-diseases` [implants/peri-implantitis] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Establishes that **implant macro-/micro-design/system choice** (bone-level vs tissue-level, rough vs hybrid vs laser-microtextured surfaces, brand) is NOT a reliably differentiating factor for peri-implant disease risk in the current comparative literature — contradicting any single-brand or single-surface marketing claim of superior peri-implantitis resistance.
  - ▸ 출발(`monje-2025-surgical-implant-factors-peri-implant-diseases`) 세줄: 체계적 문헌고찰(34편; 수술요인 21편[환자 2752명/임플란트 7591개], 임플란트요인 13편[환자 1192명/임플란트 4072개]; 2023년 10월까지 검색)로 임플란트주위점막염·임플란트주위염의 수술적·임플란트 관련 예측인자를 정성적으로 종합, AO/AAP 2024 합의회의 근거자료. 부적절한 3차원 임플란트 위치(오식립)가 임플란트주위염의 가장 강력하고 일관된 수술 관련 위험요인(OR 최대 48.2)이었던 반면, 임플란트 거대/미세디자인이나 시스템은 일관된 우위를 보이지 못했고, 보철변

- `pujarern-2024-biofilm-removal-implant-airflow-erythritol` [implants/peri-implantitis] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Both SB and ERY removed biofilm far better than untreated control (mean OD 0.130 / 0.129 vs 0.728; p<0.05) with no significant difference between the powders (p>0.05), refuting the larger-particle-cleans-better hypothesis.
  - ▸ 출발(`pujarern-2024-biofilm-removal-implant-airflow-erythritol`) 세줄: 체외(In-vitro) 연구(덴티움 SuperLine II 골수준 임플란트 33개, 3군 각 n=11): 탄산수소나트륨(Sodium Bicarbonate, SB, 40 µm)과 에리스리톨(Erythritol, ERY, 14 µm) 에어폴리싱 파우더의 임플란트 표면 생물막 제거 효능을 비교. 두 파우더 모두 대조군 대비 생물막을 현저히 제거(평균 광학밀도(Optical Density, OD) 0.130/0.129 vs 0.728; p<0.05)했으며, SB-ERY 간 차이는 유의하지 않아(p>0.0

- `pujarern-2024-biofilm-removal-implant-airflow-erythritol` [implants/peri-implantitis] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 두 파우더 모두 대조군 대비 생물막을 현저히 제거(평균 광학밀도(Optical Density, OD) 0.130/0.129 vs 0.728; p<0.05)했으며, SB-ERY 간 차이는 유의하지 않아(p>0.05) 큰 입자가 더 잘 제거한다는 가설이 반박됨.
  - ▸ 출발(`pujarern-2024-biofilm-removal-implant-airflow-erythritol`) 세줄: 체외(In-vitro) 연구(덴티움 SuperLine II 골수준 임플란트 33개, 3군 각 n=11): 탄산수소나트륨(Sodium Bicarbonate, SB, 40 µm)과 에리스리톨(Erythritol, ERY, 14 µm) 에어폴리싱 파우더의 임플란트 표면 생물막 제거 효능을 비교. 두 파우더 모두 대조군 대비 생물막을 현저히 제거(평균 광학밀도(Optical Density, OD) 0.130/0.129 vs 0.728; p<0.05)했으며, SB-ERY 간 차이는 유의하지 않아(p>0.0

- `pujarern-2024-biofilm-removal-implant-airflow-erythritol` [implants/peri-implantitis] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refuted the larger-particle-cleans-better hypothesis: SB and ERY equivalent in biofilm removal.
  - ▸ 출발(`pujarern-2024-biofilm-removal-implant-airflow-erythritol`) 세줄: 체외(In-vitro) 연구(덴티움 SuperLine II 골수준 임플란트 33개, 3군 각 n=11): 탄산수소나트륨(Sodium Bicarbonate, SB, 40 µm)과 에리스리톨(Erythritol, ERY, 14 µm) 에어폴리싱 파우더의 임플란트 표면 생물막 제거 효능을 비교. 두 파우더 모두 대조군 대비 생물막을 현저히 제거(평균 광학밀도(Optical Density, OD) 0.130/0.129 vs 0.728; p<0.05)했으며, SB-ERY 간 차이는 유의하지 않아(p>0.0

- `pujarern-2024-biofilm-removal-implant-airflow-erythritol` [implants/peri-implantitis] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: Peri-implantitis 비수술/유지 단계의 핵심은 임플란트 표면 생물막 제거인데, [[overviews/peri-implantitis-management-overview]]의 표면 decontamination 분기에서 air-polishing powder 선택(어떤 powder가 가장 효율적이고 표면 손상이 적은가)에 대한 직접 비교 근거를 보강하기 위해 인제스트. 본 in-vitro RCT-design 비교는 SB(40 µm) vs ERY(14 µm) 두 파우더의 생물막 제거 효율을 직접 대조해, 큰 입자가 더 잘 제거할 것이라는 통념을 반박하고 작은 입자(ERY) 쪽이 표면 손상이 적어 임상적으로 선호된다는 결론을 제공한다. 또한 [[implants/peri-implantitis/baima-202
  - ▸ 출발(`pujarern-2024-biofilm-removal-implant-airflow-erythritol`) 세줄: 체외(In-vitro) 연구(덴티움 SuperLine II 골수준 임플란트 33개, 3군 각 n=11): 탄산수소나트륨(Sodium Bicarbonate, SB, 40 µm)과 에리스리톨(Erythritol, ERY, 14 µm) 에어폴리싱 파우더의 임플란트 표면 생물막 제거 효능을 비교. 두 파우더 모두 대조군 대비 생물막을 현저히 제거(평균 광학밀도(Optical Density, OD) 0.130/0.129 vs 0.728; p<0.05)했으며, SB-ERY 간 차이는 유의하지 않아(p>0.0

- `fathi-2025-keratinized-mucosa-implant-health-umbrella-review` [implants/peri-implantitis] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 각화점막 폭경(Keratinized Mucosa Width, KMW)이 임플란트 주위염 위험인자인지에 대한 문헌은 수십 년간 상충된 결과를 보여왔다. 이 우산 리뷰는 기존 10개 SR/MA를 집대성하여 KMW ≥2 mm 기준의 임상적 근거를 종합한다는 점에서, 기존 개별 SR 논문인 [[implants/peri-implantitis/roccuzzo-2025-keratinized-mucosa-peri-implant-20year-mandible]]에서 제시된 20년 장기 단일기관 관찰 결과를 보강하고 더 넓은 증거 기반으로 확장한다.
  - ▸ 출발(`fathi-2025-keratinized-mucosa-implant-health-umbrella-review`) 세줄: 각화점막(Keratinized Mucosa, KM)이 임플란트 건강에 미치는 의의를 다룬 10개 SR/MA(원발연구 132편, 7,139명) 우산리뷰 — AMSTAR 2 질 평가 포함. KM 폭경(KM Width, KMW) ≥2 mm이 모든 10개 리뷰에서 임플란트 주위 염증·치태·점막퇴축·변연골소실(Marginal Bone Loss, MBL) 감소와 일관되게 연관되었으며, KM 부족 시 임플란트주위염 오즈비(Odds Ratio, OR)는 2.78(Mahardawi 2023), 유병률은 KT ≥2

- `francis-2024-low-serum-vitamin-d-early-implant-failure` [implants/vitamin-d] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: This prospective cohort assessed whether serum vitamin D levels measured on the day of implant placement relate to early dental implant failure. Across 174 implants in 109 patients followed to restoration (~3–6 months), 8 patients experienced an early failure (defined as ≥50% bone loss or implant mobility). Contrary to the prevailing hypothesis, the failed cases had a *higher* mean serum vitamin D
  - ▸ 출발(`francis-2024-low-serum-vitamin-d-early-implant-failure`) 세줄: 전향적 코호트(임플란트 174개/환자 109명): 임플란트 식립 당일 혈청 25-하이드록시비타민 D(serum 25-hydroxyvitamin D, 25(OH)D) 측정 후 보철 수복(약 3–6개월)까지 추적해 조기 임플란트 실패(Early Dental Implant Failure, EDIF)와의 상관관계를 분석. 낮은 혈청 비타민 D와 조기 실패 사이에 유의한 상관관계 없음(음성 결과); 오히려 실패 8건의 평균 비타민 D(42.54 ng/mL)가 성공군(31.92 ng/mL)보다 높아 역방향성

- `francis-2024-low-serum-vitamin-d-early-implant-failure` [implants/vitamin-d] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/vitamin-d/mohsen-2024-vitamin-d-deficiency-osseointegration-prospective]] — **contradicts**: Mohsen's prospective study reports a positive vitamin D → osseointegration association; this cohort finds the opposite directionality (higher vitamin D in failures, no significant correlation).
  - ▸ 출발(`francis-2024-low-serum-vitamin-d-early-implant-failure`) 세줄: 전향적 코호트(임플란트 174개/환자 109명): 임플란트 식립 당일 혈청 25-하이드록시비타민 D(serum 25-hydroxyvitamin D, 25(OH)D) 측정 후 보철 수복(약 3–6개월)까지 추적해 조기 임플란트 실패(Early Dental Implant Failure, EDIF)와의 상관관계를 분석. 낮은 혈청 비타민 D와 조기 실패 사이에 유의한 상관관계 없음(음성 결과); 오히려 실패 8건의 평균 비타민 D(42.54 ng/mL)가 성공군(31.92 ng/mL)보다 높아 역방향성

- `francis-2024-low-serum-vitamin-d-early-implant-failure` [implants/vitamin-d] (SOFT→miron-2025-vitamin-d-deficiency-early-implant-failure, 'Unlike' · 다름)
  - **근거 문장**: This is the contrarian / negative-evidence anchor for the vitamin D → implant-failure subdomain. Unlike the consensus signal in the systematic-review and the strongly-positive prospective findings of Mohsen 2024, this cohort found NO correlation between low serum vitamin D and early implant failure — and notably the failed implants occurred in patients with a *higher* mean serum vitamin D (42.54 n
  - ▸ 출발(`francis-2024-low-serum-vitamin-d-early-implant-failure`) 세줄: 전향적 코호트(임플란트 174개/환자 109명): 임플란트 식립 당일 혈청 25-하이드록시비타민 D(serum 25-hydroxyvitamin D, 25(OH)D) 측정 후 보철 수복(약 3–6개월)까지 추적해 조기 임플란트 실패(Early Dental Implant Failure, EDIF)와의 상관관계를 분석. 낮은 혈청 비타민 D와 조기 실패 사이에 유의한 상관관계 없음(음성 결과); 오히려 실패 8건의 평균 비타민 D(42.54 ng/mL)가 성공군(31.92 ng/mL)보다 높아 역방향성
  - ▸ 대상(`miron-2025-vitamin-d-deficiency-early-implant-failure`) 세줄: 체계적 문헌고찰 (43편 = 동물 16 + 사람 27, 2025년 5월까지 검색) — 비타민 D와 임플란트 골유착(Osseointegration)에 관한 현재까지 가장 큰 종합 분석, 보충제 및 표면 코팅 개입 설계 모두 포함. 비타민 D 결핍 (Vitamin D Deficiency)은 조기 임플란트 실패 (Early Dental Implant Failure, EDIF)를 최대 4배 증가시키며; 사람 연구 27편 중 22편에서 수술 전 보충이 골-임플란트 접촉률 (BIC)과 골유착 개선, 당뇨 등

- `francis-2024-low-serum-vitamin-d-early-implant-failure` [implants/vitamin-d] (AMBIG→moy-2005-dental-implant-failure-rates-risk, 'Unlike' · 다름)
  - **근거 문장**: This is the contrarian / negative-evidence anchor for the vitamin D → implant-failure subdomain. Unlike the consensus signal in the systematic-review and the strongly-positive prospective findings of Mohsen 2024, this cohort found NO correlation between low serum vitamin D and early implant failure — and notably the failed implants occurred in patients with a *higher* mean serum vitamin D (42.54 n
  - ▸ 출발(`francis-2024-low-serum-vitamin-d-early-implant-failure`) 세줄: 전향적 코호트(임플란트 174개/환자 109명): 임플란트 식립 당일 혈청 25-하이드록시비타민 D(serum 25-hydroxyvitamin D, 25(OH)D) 측정 후 보철 수복(약 3–6개월)까지 추적해 조기 임플란트 실패(Early Dental Implant Failure, EDIF)와의 상관관계를 분석. 낮은 혈청 비타민 D와 조기 실패 사이에 유의한 상관관계 없음(음성 결과); 오히려 실패 8건의 평균 비타민 D(42.54 ng/mL)가 성공군(31.92 ng/mL)보다 높아 역방향성

- `buzatu-2024-vitamin-d-osseointegration-human-studies-sr` [implants/vitamin-d] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 결핍은 개연성 있는 위험인자이므로 술전 선별검사 및 교정 권고; 고품질 연구는 1편의 RCT에 불과하고 비타민 D 수용체 다형성(Vitamin D Receptor polymorphism, VDR) 결과도 상충(TaqI 무관, rs3782905 allele G는 불량 골유착 관련).
  - ▸ 출발(`buzatu-2024-vitamin-d-osseointegration-human-studies-sr`) 세줄: PRISMA 체계적 고찰 (7편, 2008–2021; 참가자 1,462명·임플란트 4,450개) — 비타민 D 상태와 골유착(Osseointegration)의 사람 대상 근거를 처음으로 지도화한 리뷰. 임플란트 소실률 (Implant Loss Rate) 3.9–11.4% (평균 8.37%); 중증 비타민 D 결핍 (Severe Vitamin D Deficiency)에 흡연·치주염이 겹치면 최고 11.1%; 비타민 D 수치와 골유착 간 통계적으로 유의한 연관성은 입증되지 않음. 결핍은 개연성 있는 

- `keller-2026-3d-printed-titanium-mesh-autologous-bone` [implants/vertical-ridge-augmentation] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Directly contradicts the assumption that 3D-printed Ti mesh = high exposure (cf. Soares 2025)
  - ▸ 출발(`keller-2026-3d-printed-titanium-mesh-autologous-bone`) 세줄: 후향적 연속 증례 시리즈(n=16명, 단일 기관): DMLS(Direct Metal Laser Sintering) 마이크로 퍼포레이션 grade-2 티타늄 메시, 2개 전정 고정 스크류, 순수 자가골 이식재로 골유도재생술(GBR) 시행; CBCT 감산 분석으로 계획 대비 실제 골증대 비교(102개 계측, 3명 측정자). 메시 노출 0%(16증례 연속 0건); 122–160일 치유 후 전 증례 임플란트 식립 충분; 계획·실제 CBCT 골증대량 통계적 동등(선형 혼합 모형, 유의차 없음). 이 0% 

- `keller-2026-3d-printed-titanium-mesh-autologous-bone` [implants/vertical-ridge-augmentation] (HIGH-no-target, '상반되' · 상반)
  - **근거 문장**: 노출 0% 사례를 보고한 소규모 후향 연구로서, 메쉬 설계(마이크로퍼포레이션 grade-2 Ti) + 순수 자가골 조합이 [[wiki/implants/vertical-ridge-augmentation/sabri-2024-titanium-mesh-bone-augmentation-sr-ma]] 풀드 노출률(10.8%)과 상반되는 실제 zero-exposure 사례를 제공한다. 왜 노출이 생기지 않았는지에 대한 기술적 가설(micro-perforated design, 2-screw, pure autograft)을 문헌화.
  - ▸ 출발(`keller-2026-3d-printed-titanium-mesh-autologous-bone`) 세줄: 후향적 연속 증례 시리즈(n=16명, 단일 기관): DMLS(Direct Metal Laser Sintering) 마이크로 퍼포레이션 grade-2 티타늄 메시, 2개 전정 고정 스크류, 순수 자가골 이식재로 골유도재생술(GBR) 시행; CBCT 감산 분석으로 계획 대비 실제 골증대 비교(102개 계측, 3명 측정자). 메시 노출 0%(16증례 연속 0건); 122–160일 치유 후 전 증례 임플란트 식립 충분; 계획·실제 CBCT 골증대량 통계적 동등(선형 혼합 모형, 유의차 없음). 이 0% 

- `iwasa-2011-tio2-micro-nano-hybrid-biological-aging` [implants/surface] (HIGH-no-target, 'in contrast to' · 대조)
  - **근거 문장**: In vitro study showing that TiO2 nanonodules (300 nm) deposited on micropit titanium create a micro-nano-hybrid surface that sustains bioactivity for ≥7 days after UV photofunctionalization — in contrast to micropit-only surfaces which show 30-50% bioactivity decay. Key finding: the anti-aging mechanism is sustained electropositivity from TiO2 nanonodules, independent of hydrophilicity (hybrid sur
  - ▸ 출발(`iwasa-2011-tio2-micro-nano-hybrid-biological-aging`) 세줄: 인비트로(IJN 2011): TiO2 나노결절(300 nm) + 마이크로피트 하이브리드 표면 — UV 광기능화 (Photofunctionalization) 후 7일간 생체활성 유지 여부를 마이크로 단독과 비교. 마이크로-나노 하이브리드는 7일까지 생체활성 유지; 마이크로 단독은 30–50% 감소; 7일째 하이브리드 표면은 소수성으로 전환됐지만 생체활성 유지. 기전은 친수성이 아닌 양전하 (Electropositivity) 지속 — Cl⁻로 양전하 중화 시 생체활성 소실로 확인; 나노 위상 구조가 

- `hasegawa-2020-meso-micro-nano-rough-titanium-surface` [implants/surface] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 다중 계층 위상 구조는 기존 마이크로 거칠기 표면의 증식–분화 상충 극복; 140°C가 메조 돌기 형성과 표면 완전성 간 최적 균형점.
  - ▸ 출발(`hasegawa-2020-meso-micro-nano-rough-titanium-surface`) 세줄: 인비트로+인비보(Int J Mol Sci 2020): H2SO4 140°C 산부식으로 메조+마이크로+나노 계층형 거칠기 티타늄 표면 제작(Ra 마이크로 단독 대비 6–12배). 140°C 표면 — 골아세포 (Osteoblast) 분화(ALP·무기화) 유의 향상, 세포 부착 손상 없음, 인비보 골임플란트 통합 강도 최대 향상; 메조 돌기 크기·밀도가 골전도성 (Osteoconductivity) 1차 예측인자. 다중 계층 위상 구조는 기존 마이크로 거칠기 표면의 증식–분화 상충 극복; 140°C가 메

- `witek-2020-boronized-surface-osseointegration` [implants/surface] (HIGH-no-target, 'contrary to' · 상반된 결과)
  - **근거 문장**: The central finding was unexpected and contrary to in vitro predictions: both boronized groups showed declining BIC and BAFO from 3 to 6 weeks, while both control groups showed significant increases. At 6 weeks, CAA controls demonstrated the highest osseointegration, while BAA implants showed the sharpest decline in BIC (21.73% at 3 wk → 5.93% at 6 wk). Non-decalcified histology confirmed the abse
  - ▸ 출발(`witek-2020-boronized-surface-osseointegration`) 세줄: 양 장골능 동물실험 (5마리, 임플란트 40개, 4군: 보론화 machined/acid-etched vs 대조 machined/acid-etched, 3·6주) — 보론화 (Boronization) TiB/TiB2 확산층이 골유착을 개선하는지 검증. 보론화 임플란트에서 BIC와 골면적분율 (BAFO)이 3→6주에 감소(BAA: BIC 21.73%→5.93%, p<0.01), 양 대조군은 유의하게 증가; 조직학적으로 보론화 표면 인접부에 탈무기질 골 (Osteoid) 관찰. 보론화 표면처리는 in 

- `faot-2019-insertion-torque-mandibular-overdenture` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: G4 (IT ≥45 Ncm) achieved the highest survival rate (95%) and maintained the most stable ISQ; G3 (IT 30–45 Ncm) had the worst survival (64.3%), producing a paradox contradicting linear torque-stability assumptions.
  - ▸ 출발(`faot-2019-insertion-torque-mandibular-overdenture`) 세줄: 위축성 무치악 하악 환자 31명에게 세경 임플란트(ø2.9mm) 62개를 식립, 삽입 토크(삽입 토크, IT)를 4개 구간(<10, 10–30, 30–45, ≥45 Ncm)으로 분류한 전향적 1년 임상시험. IT ≥45 Ncm(G4) 군에서 생존율 95%·최고 임플란트 안정성 지수(Implant Stability Quotient, ISQ)를 달성했으나, IT 30–45 Ncm(G3) 군은 64.3%로 최저 생존율을 기록해 토크-안정성 선형 관계를 반박하는 G3 역설을 임상 데이터로 처음 확인. 변

- `faot-2019-insertion-torque-mandibular-overdenture` [implants/isq] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: IT ≥45 Ncm(G4) 군에서 생존율 95%·최고 임플란트 안정성 지수(Implant Stability Quotient, ISQ)를 달성했으나, IT 30–45 Ncm(G3) 군은 64.3%로 최저 생존율을 기록해 토크-안정성 선형 관계를 반박하는 G3 역설을 임상 데이터로 처음 확인.
  - ▸ 출발(`faot-2019-insertion-torque-mandibular-overdenture`) 세줄: 위축성 무치악 하악 환자 31명에게 세경 임플란트(ø2.9mm) 62개를 식립, 삽입 토크(삽입 토크, IT)를 4개 구간(<10, 10–30, 30–45, ≥45 Ncm)으로 분류한 전향적 1년 임상시험. IT ≥45 Ncm(G4) 군에서 생존율 95%·최고 임플란트 안정성 지수(Implant Stability Quotient, ISQ)를 달성했으나, IT 30–45 Ncm(G3) 군은 64.3%로 최저 생존율을 기록해 토크-안정성 선형 관계를 반박하는 G3 역설을 임상 데이터로 처음 확인. 변

- `faot-2019-insertion-torque-mandibular-overdenture` [implants/isq] (HIGH-no-target, 'contrary to' · 상반된 결과)
  - **근거 문장**: - Demonstrates that IT ≥45 Ncm is clinically safe and associated with higher ISQ and positive bone remodeling in this patient population, contrary to osseocompression-damage theory
  - ▸ 출발(`faot-2019-insertion-torque-mandibular-overdenture`) 세줄: 위축성 무치악 하악 환자 31명에게 세경 임플란트(ø2.9mm) 62개를 식립, 삽입 토크(삽입 토크, IT)를 4개 구간(<10, 10–30, 30–45, ≥45 Ncm)으로 분류한 전향적 1년 임상시험. IT ≥45 Ncm(G4) 군에서 생존율 95%·최고 임플란트 안정성 지수(Implant Stability Quotient, ISQ)를 달성했으나, IT 30–45 Ncm(G3) 군은 64.3%로 최저 생존율을 기록해 토크-안정성 선형 관계를 반박하는 G3 역설을 임상 데이터로 처음 확인. 변

- `de-elio-2023-insertion-torque-resonance-frequency-tapered-parallel-implants` [implants/isq] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: Contrary to the common assumption that tapered geometry produces higher primary stability through apical bone compression, IT was significantly **higher with the parallel implants** (P<.05) — likely explained by the smaller final drill bit used for parallel implants (3.25 mm vs 3.4 mm for tapered, per manufacturer recommendation) rather than by macrogeometry itself. Between-implant-type ISQ differ
  - ▸ 출발(`de-elio-2023-insertion-torque-resonance-frequency-tapered-parallel-implants`) 세줄: split-mouth 예비 연구, 임플란트 60개(테이퍼형 30/평행형 30), 환자 17명에서 같은 치관경(coronal diameter)의 원추형·평행형 임플란트 간 삽입 토크 (Insertion Torque, IT)와 공진주파수분석 (Resonance Frequency Analysis, RFA — Osstell·Penguin 두 기종)으로 1차 안정성을 비교했다. 골밀도·치조제 폭 (Alveolar Ridge Width, ARW)이 두 군 간 유사한데도 평행형 임플란트에서 IT가 유의하게 더

- `nandini-2022-cylindrical-vs-tapered-implant-isq` [implants/isq] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 두 군 모두 생존율 100%이나, ISQ 기반 부하 적합성과 임플란트 주위 조직 건강에서 테이퍼형 우세; 골질이 임플란트 시스템보다 ISQ 변화 궤적을 결정한다는 kim-2009와 결과 상충.
  - ▸ 출발(`nandini-2022-cylindrical-vs-tapered-implant-isq`) 세줄: 분구강 생체내 연구(환자 30명, 임플란트 60개): 테이퍼형 vs 원통형 임플란트의 임플란트 안정성 지수 (Implant Stability Quotient, ISQ)·임플란트 주위 조직 지표를 T0(식립), 3개월, 6개월에 직접 비교. 테이퍼형은 모든 측정 시점에서 유의하게 높은 ISQ(p<0.05)와 낮은 수술 후 통증 VAS, 적은 출혈점 (Bleeding on Probing, BOP), 얕은 탐침 깊이를 보임. 두 군 모두 생존율 100%이나, ISQ 기반 부하 적합성과 임플란트 주위 조

- `lages-2018-isq-insertion-torque-correlation-sr` [implants/isq] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: > 48-study SR+MA (pooled r=0.44, p<0.001, moderate significant) overturns this 12-study NS result (r=0.366, p=0.079). Prefer Tisci 2026 for the IT–ISQ correlation question. (set 2026-05-31)
  - ▸ 출발(`lages-2018-isq-insertion-torque-correlation-sr`) 세줄: PRISMA 체계적 문헌고찰(12편, 2,017편 검색): 삽입토크 (Insertion Torque, IT)와 임플란트 안정성 지수 (Implant Stability Quotient, ISQ)/공명주파수분석 (Resonance Frequency Analysis, RFA)의 상관관계 평가. 통합 Pearson r=0.366, p=0.079 — 통계적으로 유의한 상관 없음; 근거 확실도 낮음(비뚤림위험·간접성으로 하향). 삽입토크와 RFA/ISQ는 서로 독립적인 생체역학적 측면을 측정하므로 상호 대체

- `kim-2013-implant-stability-retrospective-rfa-isq` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Bischof et al. (cited) — found jaw position significant but diameter/length not significant; partially contradicts this study's diameter finding
  - ▸ 출발(`kim-2013-implant-stability-retrospective-rfa-isq`) 세줄: 후향적 RFA 연구(Osstem US II plus 임플란트 90개, 환자 72명, 6군): 식립 시(T1)와 인상채득 전(T2) 임플란트 안정성 지수 (Implant Stability Quotient, ISQ) 측정으로 직경·길이·위치의 영향을 분석. 직경 5 mm가 4 mm보다 유의하게 높은 ISQ(식립 시 79.26 vs 74.33; 인상 시 82.33 vs 77.43, P<.05); 하악이 상악보다 ISQ 약 5단위 높음(P<.05); 길이 10–13 mm 범위에서는 유의한 차이 없음. 전

- `quesada-garcia-2012-implant-diameter-localization-prgf-stability` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/isq/shiffler-2016-implant-length-diameter-location-isq]] — retrospective 200-implant study; agrees on maxilla-worse-than-mandible location effect but **contradicts** this paper on diameter (Shiffler found no significant diameter effect on ISQ, vs P<.001 here).
  - ▸ 출발(`quesada-garcia-2012-implant-diameter-localization-prgf-stability`) 세줄: 전향적 임상 연구(n=235 임플란트, 93명, 그라나다 대학): 다변량 회귀(SUDAAN, 군집 표본)로 식립 12주 후 Osstell 임플란트 안정성 지수(Implant Stability Quotient, ISQ)의 예측 인자를 분석. 환자 변수는 12주 ISQ와 무관; 좁은 임플란트 직경(P<.001)·상악 위치(P=.006)는 낮은 ISQ와 연관; 성장인자 농축 혈장(Plasma Rich in Growth Factors, PRGF) 사용은 가장 높은 12주 ISQ와 연관(P=.011). 넓

- `althobaiti-2023-osseodensification-conventional-drilling-isq-sr` [implants/isq] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: [역소급 작성 2026-07-05 — 원 인제스트(2026-05-18) 당시 동기 기록 없음. [[overviews/osseodensification-clinical-applications]]에서 확인되는 현재 역할을 백필.] [[overviews/osseodensification-clinical-applications]]의 저밀도골(D3-D4) 결정표에서 OD 지지 근거 축 — bergamo-2021·mercier-2022·moghaddas-2025 등과 함께 지지 진영을 이루고, mohammadi-2025·shilpi-2025의 SR+MA 반례 2편과 대비되는 "지지 vs 반례" 구도의 한 축을 담당.
  - ▸ 출발(`althobaiti-2023-osseodensification-conventional-drilling-isq-sr`) 세줄: 골밀도화(OD) 드릴링 대 기존 드릴링의 1차 임플란트 안정성을 비교한 체계적 문헌고찰(PubMed/Scopus/EMBASE/Cochrane/EBSCO, 2013–2022; RCT·NRSI, ISQ 보고, 추적 ≥3개월). 다수 연구에서 OD군이 기존 드릴링 대비 ISQ/RFA 및 골밀도 유의하게 높음; 관찰연구(NRSI)는 비뚤림위험 낮았으나, RCT들의 전체 비뚤림위험(RoB 2)은 '높음'으로 평가되었다. 포함된 RCT의 높은 비뚤림위험으로 OD의 ISQ 이점에 대한 강력한 결론 도출이 제한

- `marconcini-2018-high-insertion-torque-bone-resorption-rct` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/isq/lemos-2020-high-insertion-torque-dental-implants-sr-ma]] — contradicts: SR+MA found no significant MBL difference; discrepancy likely explained by longer follow-up in this RCT (3 years vs shorter studies in the SR)
  - ▸ 출발(`marconcini-2018-high-insertion-torque-bone-resorption-rct`) 세줄: 단일 임플란트 116개 RCT(3년 추적): 동일 거시설계·절삭홈 다른 두 임플란트로 고삽입토크(≥50 Ncm) vs 일반 토크(<50 Ncm) 비교. 고토크 군에서 3년 변연골 소실·협측 점막 퇴축 유의하게 크며 하악에서 더 두드러짐; 누적 성공률 91.3% vs 98.2%. 협측 골판 두께(Buccal Bone Thickness, BBT) ≥1 mm는 고토크에 의한 점막 퇴축을 완화 — 피질골 두께가 과토크 위험의 조절 인자.

- `marconcini-2018-high-insertion-torque-bone-resorption-rct` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/isq/faot-2019-insertion-torque-mandibular-overdenture]] — contradicts: G4 ≥45 Ncm showed best survival (95%) in atrophic edentulous mandible; possible explanation: narrow implant design, no cortical compression, different patient population
  - ▸ 출발(`marconcini-2018-high-insertion-torque-bone-resorption-rct`) 세줄: 단일 임플란트 116개 RCT(3년 추적): 동일 거시설계·절삭홈 다른 두 임플란트로 고삽입토크(≥50 Ncm) vs 일반 토크(<50 Ncm) 비교. 고토크 군에서 3년 변연골 소실·협측 점막 퇴축 유의하게 크며 하악에서 더 두드러짐; 누적 성공률 91.3% vs 98.2%. 협측 골판 두께(Buccal Bone Thickness, BBT) ≥1 mm는 고토크에 의한 점막 퇴축을 완화 — 피질골 두께가 과토크 위험의 조절 인자.

- `trisi-2011-high-low-implant-torque-histology-sheep` [implants/isq] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - **Directly refutes the osseocompression necrosis hypothesis**: 110 Ncm in dense cortical bone produced no histologic evidence of bone necrosis
  - ▸ 출발(`trisi-2011-high-low-implant-torque-histology-sheep`) 세줄: 양 하악 분할-구강 동물실험(5마리, 임플란트 40개, 6주): 과삽입토크(HT=평균 110 Ncm) vs 저토크(LT=10 Ncm) 조직학·생체역학 비교. HT군에서 전 측정 시점 골형성↑·제거토크↑, 결정적으로 **압박괴사 없음** — 110 Ncm의 피질골 압박도 허혈성 골괴사를 유발하지 않음. HT군은 식립 7일째 1차 안정성 유의 감소(리모델링 딥)가 나타났으나 ISQ/공명주파수분석(Resonance Frequency Analysis, RFA)은 이를 감지하지 못함 — RFA의 초기 골유

- `trisi-2011-high-low-implant-torque-histology-sheep` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/isq/marconcini-2018-high-insertion-torque-bone-resorption-rct]] — contradicts at clinical level: 3-year RCT shows ≥50 Ncm → MBL↑ and mucosal recession. Trisi's 6-week histology shows no necrosis; Marconcini's 3-year data shows long-term remodeling harm. The two findings are not necessarily incompatible — necrosis may not be the mechanism of long-term bone loss
  - ▸ 출발(`trisi-2011-high-low-implant-torque-histology-sheep`) 세줄: 양 하악 분할-구강 동물실험(5마리, 임플란트 40개, 6주): 과삽입토크(HT=평균 110 Ncm) vs 저토크(LT=10 Ncm) 조직학·생체역학 비교. HT군에서 전 측정 시점 골형성↑·제거토크↑, 결정적으로 **압박괴사 없음** — 110 Ncm의 피질골 압박도 허혈성 골괴사를 유발하지 않음. HT군은 식립 7일째 1차 안정성 유의 감소(리모델링 딥)가 나타났으나 ISQ/공명주파수분석(Resonance Frequency Analysis, RFA)은 이를 감지하지 못함 — RFA의 초기 골유

- `trisi-2011-high-low-implant-torque-histology-sheep` [implants/isq] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: [[implants/isq/marconcini-2018-high-insertion-torque-bone-resorption-rct]]에서 ≥50 Ncm → 골흡수↑라는 임상 근거가 생겼으나, 이 현상이 **압박괴사(골압축 허혈괴사, Osseocompression Necrosis)** 때문인지 조직학적으로 검증한 연구가 위키에 없었음. Trisi 2011은 양 하악에서 HT(평균 110 Ncm) vs LT(10 Ncm)를 6주간 조직학·생체역학적으로 비교한 **유일한 동물조직학 연구**로, "과토크 = 압박괴사" 가설을 직접 검증해 반박함.
  - ▸ 출발(`trisi-2011-high-low-implant-torque-histology-sheep`) 세줄: 양 하악 분할-구강 동물실험(5마리, 임플란트 40개, 6주): 과삽입토크(HT=평균 110 Ncm) vs 저토크(LT=10 Ncm) 조직학·생체역학 비교. HT군에서 전 측정 시점 골형성↑·제거토크↑, 결정적으로 **압박괴사 없음** — 110 Ncm의 피질골 압박도 허혈성 골괴사를 유발하지 않음. HT군은 식립 7일째 1차 안정성 유의 감소(리모델링 딥)가 나타났으나 ISQ/공명주파수분석(Resonance Frequency Analysis, RFA)은 이를 감지하지 못함 — RFA의 초기 골유

- `aldahlawi-2018-implant-torque-crestal-bone-remodeling` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/isq/faot-2019-insertion-torque-mandibular-overdenture]] — contradicts: G4 ≥45 Ncm best clinical outcomes; different implant system (narrow 2.9 mm), different population (atrophic edentulous), possibly explains discordance
  - ▸ 출발(`aldahlawi-2018-implant-torque-crestal-bone-remodeling`) 세줄: 후향 코호트 연구(NobelActive 113개, 66명): IT >55 Ncm(평균 67.35 Ncm) vs ≤55 Ncm(평균 37.9 Ncm)으로 사후 분류 후 변연골 소실 비교. 고토크군 MBL 유의하게 큼(0.95mm vs 0.18mm, P<0.05); 하악 고토크군 2.12mm vs 상악 0.25mm; 임플란트 실패 6개 전부 고토크군(전체 생존율 94.6%). Marconcini 2018을 다른 임플란트 시스템(NobelActive)으로 보강하며, >55 Ncm에서 하악 피질골 취약성

- `aldahlawi-2018-implant-torque-crestal-bone-remodeling` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/isq/lemos-2020-high-insertion-torque-dental-implants-sr-ma]] — contradicts: SR+MA found no significant MBL difference at ≥50 Ncm; Aldahlawi's >55 Ncm specific harm may not have been captured in that SR's included study pool
  - ▸ 출발(`aldahlawi-2018-implant-torque-crestal-bone-remodeling`) 세줄: 후향 코호트 연구(NobelActive 113개, 66명): IT >55 Ncm(평균 67.35 Ncm) vs ≤55 Ncm(평균 37.9 Ncm)으로 사후 분류 후 변연골 소실 비교. 고토크군 MBL 유의하게 큼(0.95mm vs 0.18mm, P<0.05); 하악 고토크군 2.12mm vs 상악 0.25mm; 임플란트 실패 6개 전부 고토크군(전체 생존율 94.6%). Marconcini 2018을 다른 임플란트 시스템(NobelActive)으로 보강하며, >55 Ncm에서 하악 피질골 취약성

- `lemos-2020-high-insertion-torque-dental-implants-sr-ma` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/isq/marconcini-2018-high-insertion-torque-bone-resorption-rct]] — contradicts: 3-year RCT found high IT (≥50 Ncm) → greater MBL and mucosal recession; may explain if longer follow-up unmasks harm not seen in SR's shorter studies
  - ▸ 출발(`lemos-2020-high-insertion-torque-dental-implants-sr-ma`) 세줄: SR+MA(6편, 환자 389명, 임플란트 651개): 고삽입토크(≥50 Ncm) vs 일반·저토크(<50 Ncm)의 생존율 및 MBL 비교. 생존율(RR 0.51, P=.52)·MBL(MD 0.15mm, P=.30) 모두 통계적 유의차 없음; 단 즉시하중 하위군에서 저토크 실패율 4.2% vs 고토크 1.1%로 수치 차이 존재. 적격 연구 6편에 불과해 결론 도출에 한계 — 안전 상한 토크값 확립을 위한 추가 RCT 필요.

- `al-ahmari-2022-osseodensification-conventional-low-density-jaw` [implants/isq] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: A human controlled counterpoint to OD-favorable pooled literature; the authors' conclusion ("better primary stability") is more favorable than the null stability results warrant — interpret the data, not the abstract.
  - ▸ 출발(`al-ahmari-2022-osseodensification-conventional-low-density-jaw`) 세줄: Split-mouth 전향적 임상 연구 (20명·임플란트 40개, 저밀도 악골) — 골밀도화 (Osseodensification, OD·Densah) vs 통상 드릴링을 환자 자기 대조 설계로 직접 비교. OD가 유의하게 우수한 결과는 수술 직후 CBCT 골밀도뿐; 1차/2차 안정성·치태지수 (PI)·출혈탐침 (BOP)·탐침깊이 (PD)·변연골소실 (MBL) 모두 유의차 없음. OD 우호적 풀링 문헌에 대한 인체 대조 반례; 저자의 결론("더 나은 1차 안정성")은 실제 null 안정성 결과보다 

- `al-ahmari-2022-osseodensification-conventional-low-density-jaw` [implants/isq] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Provides a human controlled counterpoint to the OD-favorable pooled literature: when stability is measured directly in a split-mouth design, OD's advantage largely fails to reach significance (only density). Important for bounding OD claims.
  - ▸ 출발(`al-ahmari-2022-osseodensification-conventional-low-density-jaw`) 세줄: Split-mouth 전향적 임상 연구 (20명·임플란트 40개, 저밀도 악골) — 골밀도화 (Osseodensification, OD·Densah) vs 통상 드릴링을 환자 자기 대조 설계로 직접 비교. OD가 유의하게 우수한 결과는 수술 직후 CBCT 골밀도뿐; 1차/2차 안정성·치태지수 (PI)·출혈탐침 (BOP)·탐침깊이 (PD)·변연골소실 (MBL) 모두 유의차 없음. OD 우호적 풀링 문헌에 대한 인체 대조 반례; 저자의 결론("더 나은 1차 안정성")은 실제 null 안정성 결과보다 

- `oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma` [implants/soft-tissue] (SOFT→zhang-2025-expert-consensus-km-augmentation-second-stage, 'Unlike' · 다름)
  - **근거 문장**: It complements the risk-factor SRs ([[mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma]], [[ravida-2022-keratinized-mucosa-width-peri-implant-disease-sr-ma]]) by quantifying the *upside of intervention*, and pairs with the consensus/technique guidance ([[sanz-2022-keratinized-mucosa-around-implants-consensus]], [[zhang-2025-expert-consensus-km-augmentation-second-stage]]). Unlike Sanz
  - ▸ 출발(`oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma`) 세줄: SR+MA(임상 11편, 290명): 이미 최종 보철이 장착된 기능 중인 임플란트에서의 연조직 이식 효과를 평가한 — 식립 시가 아닌 유지 관리 단계의 이식 질문에 답하였다. 유리치은이식(Free Gingival Graft, FGG)은 각화점막(KM) 가중평균 2.6 mm 증가·점막 염증 감소·4년까지 치조정골 변화 없음; 결합조직이식(CTG)은 임플란트 주위 점막 퇴축 가중평균 2 mm 감소; KM 부재가 임플란트 주위 염증 증가와 연관 확인. 기능 중인 임플란트에서 FGG는 KM 조성에, CT
  - ▸ 대상(`zhang-2025-expert-consensus-km-augmentation-second-stage`) 세줄: 임플란트 2차 노출 수술 시 각화점막(KM) 증대 기법 선택을 위한 중국 20개 학술 기관 29인 전문가 컨센서스(Int J Oral Sci 2025). 잔존 KM 폭·부위별 결정 트리 제시: 하악 KM <2 mm → 2차 수술 전 FGG 필수; 심미 부위 → SFGG + 대체재; 상악 구치부 → ARF; FGG는 KM ~4.1 mm 획득(수축 12–16%), XCM은 ~1.8 mm(수축 34–51%). 2차 수술이 최적의 증대 시점이며, 얇은 생물형은 ARF 단독 불충분 — FGG 또는 MARF

- `oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma` [implants/soft-tissue] (AMBIG→ravida-2022-keratinized-mucosa-width-peri-implant-disease-sr-ma, 'Unlike' · 다름)
  - **근거 문장**: It complements the risk-factor SRs ([[mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma]], [[ravida-2022-keratinized-mucosa-width-peri-implant-disease-sr-ma]]) by quantifying the *upside of intervention*, and pairs with the consensus/technique guidance ([[sanz-2022-keratinized-mucosa-around-implants-consensus]], [[zhang-2025-expert-consensus-km-augmentation-second-stage]]). Unlike Sanz
  - ▸ 출발(`oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma`) 세줄: SR+MA(임상 11편, 290명): 이미 최종 보철이 장착된 기능 중인 임플란트에서의 연조직 이식 효과를 평가한 — 식립 시가 아닌 유지 관리 단계의 이식 질문에 답하였다. 유리치은이식(Free Gingival Graft, FGG)은 각화점막(KM) 가중평균 2.6 mm 증가·점막 염증 감소·4년까지 치조정골 변화 없음; 결합조직이식(CTG)은 임플란트 주위 점막 퇴축 가중평균 2 mm 감소; KM 부재가 임플란트 주위 염증 증가와 연관 확인. 기능 중인 임플란트에서 FGG는 KM 조성에, CT

- `oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma` [implants/soft-tissue] (AMBIG→mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma, 'Unlike' · 다름)
  - **근거 문장**: It complements the risk-factor SRs ([[mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma]], [[ravida-2022-keratinized-mucosa-width-peri-implant-disease-sr-ma]]) by quantifying the *upside of intervention*, and pairs with the consensus/technique guidance ([[sanz-2022-keratinized-mucosa-around-implants-consensus]], [[zhang-2025-expert-consensus-km-augmentation-second-stage]]). Unlike Sanz
  - ▸ 출발(`oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma`) 세줄: SR+MA(임상 11편, 290명): 이미 최종 보철이 장착된 기능 중인 임플란트에서의 연조직 이식 효과를 평가한 — 식립 시가 아닌 유지 관리 단계의 이식 질문에 답하였다. 유리치은이식(Free Gingival Graft, FGG)은 각화점막(KM) 가중평균 2.6 mm 증가·점막 염증 감소·4년까지 치조정골 변화 없음; 결합조직이식(CTG)은 임플란트 주위 점막 퇴축 가중평균 2 mm 감소; KM 부재가 임플란트 주위 염증 증가와 연관 확인. 기능 중인 임플란트에서 FGG는 KM 조성에, CT

- `bhatavadekar-2012-peri-implant-soft-tissue-management-narrative` [implants/soft-tissue] (HIGH-no-target, 'conflicting evidence' · 상충 결과)
  - **근거 문장**: On the keratinized mucosa (KM) debate, the author acknowledges conflicting evidence — some studies finding no statistical long-term advantage, others linking KM to better health and patient satisfaction — and expresses a clinical opinion that KM provides a "layer of protection" against plaque accumulation and mechanical insult, supported by a cited study showing thick mucosa (≥1 mm) correlates wit
  - ▸ 출발(`bhatavadekar-2012-peri-implant-soft-tissue-management-narrative`) 세줄: J Indian Soc Periodontol 2012 단신: 임플란트 첫 시술 ~40년 후 시점에서 임플란트 주위 연조직 관리(각화점막 논쟁, CTG·VIP-CT 혈관경 결합조직이식, 유두 재건)를 임상 관점에서 종합 서술하였다. 참조된 양측 하악 RCT (n=10)에서 CTG 증대는 대조군 대비 조직 두께 +1.3 mm (P<0.001) 및 핑크 심미 점수 우수; VIP-CT 피판은 자가유리 CTG 대비 수축이 적다고 2년 추적에서 보고하였다. 핵심 철학 전환: 연조직 관리는 임플란트 식립 시가

- `rios-osorio-2025-xcm-vs-ctg-fgg-implant-soft-tissue-sr-ma` [implants/soft-tissue] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - First SR+MA to separately analyse crosslinked (VCMX) vs non-crosslinked (XCM*) porcine collagen matrices against CTG, resolving previous contradictions from pooled analyses.
  - ▸ 출발(`rios-osorio-2025-xcm-vs-ctg-fgg-implant-soft-tissue-sr-ma`) 세줄: 17편 RCT SR+MA — 임플란트 부위 점막두께·각화점막폭 증대를 위한 이종 콜라겐 매트릭스 (XCM, Xenogeneic Collagen Matrix) 대 자가이식(CTG/FGG) 비교 연구. 비가교형 XCM은 결합조직이식 (CTG, Connective Tissue Graft) 대비 점막두께 열위(MD −0.27 mm, P=0.01)이나, 가교형 VCMX는 CTG와 동등(MD −0.02 mm, P=0.83); 유리치은이식 (FGG, Free Gingival Graft)은 각화점막폭 (KMW,

- `neves-2023-socket-shield-stress-distribution-fea` [immediate-implant/socket-shield] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - Provides a biomechanical counterpoint to clinical socket-shield outcome studies.
  - ▸ 출발(`neves-2023-socket-shield-stress-distribution-fea`) 세줄: 상악 중절치 임플란트 크라운의 사위 하중(100 N 설측 + 25.5 N 절단) 모델을 3D 유한요소분석(FEA): 협측벽 조건을 소켓 쉴드(SS, 2.0 mm 치근편)·이종골이식(HBG)·대조(완전 치유골)로 비교. SS와 HBG 모두 대조군보다 주위골 응력 높음; SS가 주위 조직 응력 집중 최대. 치근편·이식재·임플란트·보철 구성요소 간 차이는 미미. 소켓 쉴드 임상 문헌의 우호적 결과에 생역학적 경고를 추가 — 치근편 보존이 주위골 응력을 집중시키나, FEA 응력 크기가 임상 실패를 직접 

- `lu-2025-socket-shield-conventional-aesthetic-meta` [immediate-implant/socket-shield] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: This 2025 meta-analysis is the **largest pooled comparison of SST vs CIIP in the esthetic zone to date** — 27 studies (22 RCTs, 5 NRSI), 1307 implants — and notably folds in 13 Chinese-language studies that English-only predecessors omitted. It does **not overturn** the existing wiki thesis ([[wiki/overviews/socket-shield-technique-overview]]): SST again wins on buccal-bone preservation, PES, and 
  - ▸ 출발(`lu-2025-socket-shield-conventional-aesthetic-meta`) 세줄: PRISMA SR+MA (27편: RCT 22 + NRSI 5, 심미부위 1307 임플란트): 소켓실드 기법(SST) vs 전통 즉시식립(CIIP) 비교. 기존 영문 전용 메타분석에서 누락된 중국어 RCT 13편 포함, 현존 최대 풀. SST가 수평 협측골 소실(MD −0.50 mm), 수직 골소실(MD −0.56 mm), 핑크심미점수(PES, +1.25), 임플란트 안정성 지수(ISQ, +5.83) 모두 유의하게 우월; 임플란트 성공률 동등(RR 1.00, I²=0%). 실드 높이·두께·골이식 

- `araujo-2026-buccal-gap-width-alveolar-reduction-iip-cbct` [immediate-implant/esthetic-soft-tissue] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[immediate-implant/esthetic-soft-tissue/yang-2019-labial-bone-thickness-esthetics-iipp]] — contradicts: Yang found buccal bone thickness < 0.5 mm worsens resorption; here baseline buccal thickness was non-significant once gap width was accounted for in thin-walled central-incisor sites.
  - ▸ 출발(`araujo-2026-buccal-gap-width-alveolar-reduction-iip-cbct`) 세줄: 후향적 CBCT 코호트 (상악 중절치 28부위, 반대측 자연치 대조, 평균 6년): DBBM 이식 즉시 임플란트에서 협측 gap 폭이 치조제 보존의 결정인자임을 규명. Gap >2 mm → 치조제 단면적 90% 이상 보존(8.5% 감소); gap ≤2 mm → 약 41% 흡수(p<0.001); 회귀분석에서 gap 폭만 유의 예측인자 — 기준 협측골 두께·CTG 비유의. 협측골 두께가 아닌 gap 충전 부피가 보존을 결정 — >2 mm 기준은 ITI Type-1A 생존 기준에 해당하는 기전적 근거를

- `deng-2024-posterior-open-wound-healing-immediate-implant` [immediate-implant/esthetic-soft-tissue] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: RST·ACS 모두 구치부 즉시식립 개방창 처치에 유효 — 색조 대 섬유성 회복의 상충관계와 자가조직 채취 선호 여부에 따라 선택.
  - ▸ 출발(`deng-2024-posterior-open-wound-healing-immediate-implant`) 세줄: 후향적 코호트(환자 32명 / 후방 즉시식립 40개, 단일기관) — 반응성 연조직(RST, n=20) vs 흡수성 콜라겐 스펀지(ACS, n=20)로 발치와 개방 창상 sealing 비교, 약 6개월 추적. 두 재료 모두 총 연조직 치유 점수·치은퇴축·HBW·MBL 변화 비슷; ACS가 조직 색조 우세(p=0.016), RST가 섬유성 회복 우세(p=0.043). RST·ACS 모두 구치부 즉시식립 개방창 처치에 유효 — 색조 대 섬유성 회복의 상충관계와 자가조직 채취 선호 여부에 따라 선택.

- `bragues-2024-oral-mucositis-children-cancer-management-sr` [oral-medicine/mucositis] (SOFT→dean-2022-oral-chronic-gvhd-review, 'whereas' · 반면(대조))
  - **근거 문장**: The wiki's oral mucosal-disease coverage in `oral-medicine` (aphthous stomatitis, lichen planus, BMS) had no entry on cancer-therapy-induced oral mucositis — a high-incidence (40–100%) inflammatory condition distinct from those entities. This SR fills that gap and pairs with [[oral-medicine/dean-2022-oral-chronic-gvhd-review]], which covers the adjacent oncology context (oral chronic GVHD after he
  - ▸ 출발(`bragues-2024-oral-mucositis-children-cancer-management-sr`) 세줄: PRISMA 체계적 문헌고찰(PROSPERO CRD42022347208; 2655건 → 39편 포함, n=14–148; 이질성으로 메타분석 불가) — 소아(≤18세) 항암·방사선·조혈모세포이식 유발 구강점막염(OM) 관리 중재 비교. OM 발생률엔 클로르헥시딘, 기간엔 꿀, 통증엔 올리브유가 최적; 팔리퍼민(KGF)은 급성백혈병에서 발생률·중증도·기간 모두 감소; 칼슘인산염은 3편 모두 효과 없음; LLLT/광생체조절이 가장 많이 연구된 중재(8편, 20%)이나 결과 불일치. 소아 OM 프로토콜 
  - ▸ 대상(`dean-2022-oral-chronic-gvhd-review`) 세줄: 동종 조혈모세포이식(alloHCT) 수혜자 30–50%에서 발생하는 구강 만성 이식편대숙주병(cGVHD) 내러티브 미니리뷰 — 태선양 점막염·면역성 타액선 기능저하·조직 경화/개구장애 세 아형 정리. NIH 2014 진단·병기 기준 적용; 국소 스테로이드 세척 → 전신 면역억제로 단계적 관리, 난치성은 표적 면역억제제로 전환. 구강 cGVHD는 주요 이환율 원인인 동시에 악성전환 부위(OPMD)로 인식되어 전신 질환 관리와 함께 장기적 구강 감시 필요.

- `gupta-2023-prevalence-distribution-oral-mucosal-nepal` [oral-medicine/normal-variants] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 정상범주 구강내 병소(Fordyce granules, linea alba 등) 전용 서브카테고리 [[oral-medicine/normal-variants]] 신설의 근거 논문. 16,572명 규모의 대표 cross-sectional 자료로 Fordyce's granules(8.84%), linea alba(연령별 최대 37.21%), frictional keratosis 등 normal variant의 인구 기반 유병률을 제공해 케이스 단위 보고([[oral-medicine/normal-variants/baklouti-2023-whitish-patches-buccal-mucosa-dermoscopy]])와 대비되는 역학적 기준선 역할.
  - ▸ 출발(`gupta-2023-prevalence-distribution-oral-mucosal-nepal`) 세줄: 네팔 라릿푸르 3차 치과병원 외래 환자 16,572명 후향적 단면 기록 검토(2016–2019년; WHO 진단 가이드 기반) — 네팔 최초 구강점막병소·정상 변이 인구 기반 유병률 기준선 수립. 구강점막병소(OML) 21.08%; 양성 정상 변이 13.96% — 가장 흔한 정상 변이: 마찰성 각화증·교흔(linea alba)·포다이스 그래뉼(8.84%); 정상 변이의 80.10%가 협점막(buccal mucosa)에 위치. 포다이스 그래뉼 유병률은 연구 간 1.2–82.8%로 극변동 — 단일 글로

- `shahood-2024-cgf-bio-oss-osteotome-sinus-elevation` [sinus-lift/transcrestal] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[sansupakorn-2024-osfe-bcp-graft-versus-no-graft-rct]] — contradicts: BCP graft shows no benefit in RCT
  - ▸ 출발(`shahood-2024-cgf-bio-oss-osteotome-sinus-elevation`) 세줄: 전향적 3군 연구(n=126 임플란트, 123명, 단일 센터) — 잔존골높이(Residual Bone Height, RBH) ≤5 mm 골절단기 상악동거상술(Osteotome Sinus Floor Elevation, OSFE) 동시 식립에서 무이식(A군) vs Bio-Oss 단독(B군) vs Bio-Oss Collagen + 농축성장인자(CGF, C군) 비교. 전체 임플란트 생존율(Implant Survival Rate, ISR) 96%; C군(Bio-Oss Collagen + CGF)이 최대 골

- `sansupakorn-2024-osfe-bcp-graft-versus-no-graft-rct` [sinus-lift/transcrestal] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[shahood-2024-cgf-bio-oss-osteotome-sinus-elevation]] — contradicts: CGF+Bio-Oss Collagen superior to no-graft (graft type matters)
  - ▸ 출발(`sansupakorn-2024-osfe-bcp-graft-versus-no-graft-rct`) 세줄: RCT (30 임플란트, 1년, TCTR20210517008) — 상악 소구치/대구치 단일 결손부에서 OSFE+BCP 이식(HA30:TCP70, n=15) vs 무이식 OSFE(n=15) 비교, 3·6·9·12개월 CBCT 부피 측정·ISQ 평가. BCP 이식군이 1년 ISQ(78.72 vs 79.65, p=0.56)·생존율·골이득 모두 무이식군 대비 유의차 없음; 무이식군에서 6·9·12개월 변연골 변화(Marginal Bone Change)가 유의하게 적음(p<0.05). BCP 이식은 무이식

- `changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift` [sinus-lift/transcrestal] (HIGH-no-target, 'in contrast to' · 대조)
  - **근거 문장**: This prospective single-arm study from Bharati Vidyapeeth Dental College, Pune, India, evaluated the HaeNaem Zero Bone Loss Kit — a proprietary 골밀도화 (osseodensification, OD) bur system — for 경치조골 간접 상악동 거상 (indirect transcrestal sinus lift) in 12 patients with 잔존 치조골 높이 (residual crestal bone height, RCBH) of 6–8 mm. The study's primary contribution is clinical data on an alternative OD bur system
  - ▸ 출발(`changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift`) 세줄: 잔존 치조골 높이(Residual Crestal Bone Height, RCBH) 6–8 mm에서 HaeNaem Zero Bone Loss 시계방향(Clockwise, CW) 골밀도화(Osseodensification, OD) 버를 이용한 무이식 경치조골 간접 거상·동시 식립을 평가한 전향적 단일군 연구(n=12). **철회(Retracted) — 임상 근거로 인용 금지.** 4개월 CBCT에서 근심·원심·협측·구개측 4개 방향 모두 유의한 골 높이 증가(p<0.01); 막 천공 없음; 전 임플란

- `nowzari-2022-migration-bovine-derived-xenograft-particles` [sinus-lift/lateral] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: Nowzari, Teoh, Rodriguez (2022, J Indian Soc Periodontol)는 단일 개인 치과의원에서 7명의 건강한 성인(34–80세, 여5/남2)에게 우골유래 이종골이식재(Bio-Oss 또는 Bio-Oss Collagen)를 전치부 상악(6례) 또는 하악(1례) 임플란트 부위의 발치와 보존 또는 윤곽증대(contour augmentation)에 사용한 뒤 2–6년간 관찰한 증례 시리즈를 보고했다. 즉시식립+즉시부하 프로토콜(Case 3, 6, 7)과 지연/단계적 프로토콜(Case 1, 2, 4, 5)이 혼재하며, 대부분 콜라겐 막(Bio-Gide) 및/또는 결합조직 이식을 병용했다. 7례 전부에서 치유지대주 제거 시점부터 최장 6년 추적 시점까지, 유착된(intact) 이종골 입
  - ▸ 출발(`nowzari-2022-migration-bovine-derived-xenograft-particles`) 세줄: 증례 시리즈 (n=7, 단일 개인 치과의원 코호트, JISP 2022) — 전치부 상악·하악 임플란트 부위에 발치와 보존 또는 윤곽증대 목적으로 우골유래 이종골이식재 (Bio-Oss/Bio-Oss Collagen)를 사용, 이식 후 2–6년 추적. 7례 모두에서 유착 (intact) 상태의 이종골 입자가 치유지대주 단계부터 이식 후 6년까지 임상적·방사선학적으로 임플란트주위구 (peri-implant sulcus)로 이동하거나 표면에 노출됨 — 어떤 증례에서도 생분해 (biodegradation)

- `nowzari-2022-migration-bovine-derived-xenograft-particles` [sinus-lift/lateral] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: - [[sinus-lift/lateral/sartori-2003-msfa-bio-oss-10year-case-report]] — 단일 증례 10년 생검에서 진행성 Bio-Oss 흡수(29.8%→86.7% 골조직)를 보고해 본 논문 및 Mordenfeld 2010과 상충하는 결과(대조군 성격의 반례).
  - ▸ 출발(`nowzari-2022-migration-bovine-derived-xenograft-particles`) 세줄: 증례 시리즈 (n=7, 단일 개인 치과의원 코호트, JISP 2022) — 전치부 상악·하악 임플란트 부위에 발치와 보존 또는 윤곽증대 목적으로 우골유래 이종골이식재 (Bio-Oss/Bio-Oss Collagen)를 사용, 이식 후 2–6년 추적. 7례 모두에서 유착 (intact) 상태의 이종골 입자가 치유지대주 단계부터 이식 후 6년까지 임상적·방사선학적으로 임플란트주위구 (peri-implant sulcus)로 이동하거나 표면에 노출됨 — 어떤 증례에서도 생분해 (biodegradation)

- `kozuma-2017-chronic-sinusitis-sinus-augmentation-infection` [sinus-lift/lateral] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: 4. **Membrane perforation is not the primary driver**: Contrary to common clinical emphasis, membrane perforation ranked below chronic sinusitis in both outcome models.
  - ▸ 출발(`kozuma-2017-chronic-sinusitis-sinus-augmentation-infection`) 세줄: 단일기관 후향 코호트 (109명, 121 상악동, 252 임플란트, 큐슈대학): 측방 접근 상악동거상술 (Lateral Sinus Augmentation, LSA) 후 감염·임플란트 실패 예측인자를 다변량 로지스틱 회귀로 분석. 술전 만성 부비동염 (Chronic Sinusitis)이 감염 (p=0.007)과 임플란트 실패 (p=0.007) 모두의 최강 독립 예측인자; 모든 합병증 (8건, 6.6%)이 만성 부비동염 양성 환자에서 발생; 막 천공은 이차적 위험인자. SNOT-20·비강내시경·CT를

- `akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height` [sinus-lift/lateral] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Findings contradict Maska 2017 (no ridge-height association), likely reflecting population differences; the >3 mm pathological threshold and U-shaped perforation risk curve have direct implications for preoperative sinus-lift planning.
  - ▸ 출발(`akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height`) 세줄: 후향적 콘빔CT(Cone-Beam CT, CBCT) 연구 (임플란트 후보 141명, 240 상악동 — 양측 99·편측 42): 이란 코호트에서 잔존 치조제 높이(Residual Ridge Height)와 슈나이더 막 점막비후(Mucosal Thickening) 상관 분석. 잔존 치조제 높이가 낮을수록 점막비후가 유의하게 크며 (역상관); 천공 위험이 가장 낮은 최적 막 두께는 1.5–2 mm이고, <0.8 mm (얇음)·>3 mm (두꺼움) 양쪽 모두 천공 위험 증가. Maska 2017의 연관 

- `akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height` [sinus-lift/lateral] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: Maska 2017의 연관 없음 결과와 상충 (인구집단 차이 가능성); >3 mm 병적 역치와 U자형 천공 위험 곡선은 상악동거상술(Sinus Floor Elevation, SFE) 술전 계획에 직접 활용 가능.
  - ▸ 출발(`akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height`) 세줄: 후향적 콘빔CT(Cone-Beam CT, CBCT) 연구 (임플란트 후보 141명, 240 상악동 — 양측 99·편측 42): 이란 코호트에서 잔존 치조제 높이(Residual Ridge Height)와 슈나이더 막 점막비후(Mucosal Thickening) 상관 분석. 잔존 치조제 높이가 낮을수록 점막비후가 유의하게 크며 (역상관); 천공 위험이 가장 낮은 최적 막 두께는 1.5–2 mm이고, <0.8 mm (얇음)·>3 mm (두꺼움) 양쪽 모두 천공 위험 증가. Maska 2017의 연관 

- `akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height` [sinus-lift/lateral] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: - Contradicts Maska 2017 finding (no significant ridge height association) — population difference likely
  - ▸ 출발(`akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height`) 세줄: 후향적 콘빔CT(Cone-Beam CT, CBCT) 연구 (임플란트 후보 141명, 240 상악동 — 양측 99·편측 42): 이란 코호트에서 잔존 치조제 높이(Residual Ridge Height)와 슈나이더 막 점막비후(Mucosal Thickening) 상관 분석. 잔존 치조제 높이가 낮을수록 점막비후가 유의하게 크며 (역상관); 천공 위험이 가장 낮은 최적 막 두께는 1.5–2 mm이고, <0.8 mm (얇음)·>3 mm (두꺼움) 양쪽 모두 천공 위험 증가. Maska 2017의 연관 

- `akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height` [sinus-lift/lateral] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[sinus-lift/lateral/maska-2017-implant-grafting-success-mucosal-thickening-sinus]] — contradictory: no significant ridge height association (different population, 4-tier index)
  - ▸ 출발(`akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height`) 세줄: 후향적 콘빔CT(Cone-Beam CT, CBCT) 연구 (임플란트 후보 141명, 240 상악동 — 양측 99·편측 42): 이란 코호트에서 잔존 치조제 높이(Residual Ridge Height)와 슈나이더 막 점막비후(Mucosal Thickening) 상관 분석. 잔존 치조제 높이가 낮을수록 점막비후가 유의하게 크며 (역상관); 천공 위험이 가장 낮은 최적 막 두께는 1.5–2 mm이고, <0.8 mm (얇음)·>3 mm (두꺼움) 양쪽 모두 천공 위험 증가. Maska 2017의 연관 

- `akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height` [sinus-lift/lateral] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 잔존 치조제 높이와 상악동 점막비후 간의 관계를 CBCT로 분석한 연구. 골 높이가 낮을수록 점막비후 위험이 높은지를 평가 — 임플란트 계획 시 사전 위험 계층화에 직접 활용 가능. [[sinus-lift/lateral/maska-2017-implant-grafting-success-mucosal-thickening-sinus]]와 대비되는 결과(ridge height 연관성 있음 vs 없음) 제공.
  - ▸ 출발(`akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height`) 세줄: 후향적 콘빔CT(Cone-Beam CT, CBCT) 연구 (임플란트 후보 141명, 240 상악동 — 양측 99·편측 42): 이란 코호트에서 잔존 치조제 높이(Residual Ridge Height)와 슈나이더 막 점막비후(Mucosal Thickening) 상관 분석. 잔존 치조제 높이가 낮을수록 점막비후가 유의하게 크며 (역상관); 천공 위험이 가장 낮은 최적 막 두께는 1.5–2 mm이고, <0.8 mm (얇음)·>3 mm (두꺼움) 양쪽 모두 천공 위험 증가. Maska 2017의 연관 

- `maska-2017-implant-grafting-success-mucosal-thickening-sinus` [sinus-lift/lateral] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[sinus-lift/lateral/akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height]] — found ridge height association (contradicts; different population/threshold)
  - ▸ 출발(`maska-2017-implant-grafting-success-mucosal-thickening-sinus`) 세줄: 미시간대학교 후향적 CBCT 연구 (n=29, 평균 추적 3.3년): 상악동거상술 (Sinus Floor Elevation, SFE) 환자에서 기존 점막비후 (Mucosal Thickening)가 결과에 미치는 영향 평가. 93.1%에서 점막비후 확인 (65.5%가 중증 >5 mm, 평균 최대 8.34 mm)에도 임플란트·골이식 생존율 100%; 치주질환 (Periodontal Disease) 과거력만 유의한 독립 예측인자 (p=0.004). 활성 부비동염 (Sinusitis)·근단병소 (Peri

- `sartori-2003-msfa-bio-oss-10year-case-report` [sinus-lift/lateral] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The progressive resorption trajectory directly contradicts Mordenfeld 2010 (n=11, 80% DPBB + 20% autograft; no particle size change at 11 years); the discrepancy likely reflects differences in graft composition (Bio-Oss alone vs 80:20 mixture), measurement method, and inter-patient variability — clinicians should not make absolute resorption/non-resorption claims from either paper alone.
  - ▸ 출발(`sartori-2003-msfa-bio-oss-10year-case-report`) 세줄: 단일 환자 증례보고: Bio-Oss 단독 상악동거상술 (Maxillary Sinus Floor Augmentation, MSFA) 후 8개월·2년·10년 시점 연속 트레핀 생검 (Trephine Biopsy) 조직형태계측 — 인체 장기 MSFA 리모델링 궤적을 기록한 매우 드문 연구. 골조직 (골수강 포함) 비율 29.8% → 69.7% → 86.7%로 단조 증가; Bio-Oss 입자 ~70% → ~30% → ~13%로 점진적 감소 — 10년에 걸친 완만하지만 진행적인 흡수 시사. Mordenfe

- `sartori-2003-msfa-bio-oss-10year-case-report` [sinus-lift/lateral] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: Mordenfeld 2010 (n=11, 80% DPBB + 20% 자가골; 11년 입자 크기 변화 없음) 과 반대 결론 — 이식재 조성 차이 (Bio-Oss 단독 vs 혼합), 측정 방법, 개인차에서 비롯된 상충 가능; 두 논문 어느 쪽으로도 흡수·비흡수 단정 위험.
  - ▸ 출발(`sartori-2003-msfa-bio-oss-10year-case-report`) 세줄: 단일 환자 증례보고: Bio-Oss 단독 상악동거상술 (Maxillary Sinus Floor Augmentation, MSFA) 후 8개월·2년·10년 시점 연속 트레핀 생검 (Trephine Biopsy) 조직형태계측 — 인체 장기 MSFA 리모델링 궤적을 기록한 매우 드문 연구. 골조직 (골수강 포함) 비율 29.8% → 69.7% → 86.7%로 단조 증가; Bio-Oss 입자 ~70% → ~30% → ~13%로 점진적 감소 — 10년에 걸친 완만하지만 진행적인 흡수 시사. Mordenfe

- `sartori-2003-msfa-bio-oss-10year-case-report` [sinus-lift/lateral] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: Sartori 등(2003)은 단일 환자에서 Bio-Oss 단독 상악동 거상 후 8개월·2년·10년에 동일 부위에서 trephine biopsy를 얻어 histomorphometry를 시행했다. 결과는 골 조직(골수강 포함) 비율이 29.8% → 69.7% → 86.7%로 단조 증가하고, Bio-Oss 입자는 그에 따라 70% → 30% → 13%로 진행성 흡수됐다. 단일 환자라는 결정적 한계가 있으나 10년 시간 trajectory의 인체 데이터는 매우 드물어, Bio-Oss의 "장기적으로 점진 흡수된다" 명제의 historical 근거. 단, Mordenfeld 2010(n=11, 11년 시점)에서는 "Bio-Oss 입자가 흡수되지 않는다"는 반대 결론이 나옴 — 두 논문의 상충은 [미검증] graft 
  - ▸ 출발(`sartori-2003-msfa-bio-oss-10year-case-report`) 세줄: 단일 환자 증례보고: Bio-Oss 단독 상악동거상술 (Maxillary Sinus Floor Augmentation, MSFA) 후 8개월·2년·10년 시점 연속 트레핀 생검 (Trephine Biopsy) 조직형태계측 — 인체 장기 MSFA 리모델링 궤적을 기록한 매우 드문 연구. 골조직 (골수강 포함) 비율 29.8% → 69.7% → 86.7%로 단조 증가; Bio-Oss 입자 ~70% → ~30% → ~13%로 점진적 감소 — 10년에 걸친 완만하지만 진행적인 흡수 시사. Mordenfe

- `sartori-2003-msfa-bio-oss-10year-case-report` [sinus-lift/lateral] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 측방 상악동거상술(Maxillary Sinus Floor Augmentation, MSFA)에서 Bio-Oss(탈단백우골, DPBB)가 점진적으로 흡수·골치환되는지를 단일 환자 8개월·2년·10년 연속 생검으로 보여주는 유일한 10년 궤적 자료. Mordenfeld 2010의 "유의한 흡수 없음" 소견과 상충해 연구 간 변이를 이해하는 데 필수적이다. See [[overviews/sinus-lift-lateral-2026-synthesis]].
  - ▸ 출발(`sartori-2003-msfa-bio-oss-10year-case-report`) 세줄: 단일 환자 증례보고: Bio-Oss 단독 상악동거상술 (Maxillary Sinus Floor Augmentation, MSFA) 후 8개월·2년·10년 시점 연속 트레핀 생검 (Trephine Biopsy) 조직형태계측 — 인체 장기 MSFA 리모델링 궤적을 기록한 매우 드문 연구. 골조직 (골수강 포함) 비율 29.8% → 69.7% → 86.7%로 단조 증가; Bio-Oss 입자 ~70% → ~30% → ~13%로 점진적 감소 — 10년에 걸친 완만하지만 진행적인 흡수 시사. Mordenfe

- `mordenfeld-2010-msfa-dpbb-biopsies-11year` [sinus-lift/lateral] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "DPBB가 흡수되지 않고 평생 잔존한다"는 명제 — 흡수성 이식재 marketing에 대한 반박 근거.
  - ▸ 출발(`mordenfeld-2010-msfa-dpbb-biopsies-11year`) 세줄: 전향적 인체 조직형태계측 생검 연구 (n=11 재진입 생검, 평균 11.5년): 심한 후방 상악 위축 20명 대상 상악동거상술 (Maxillary Sinus Floor Augmentation, MSFA) — 80% 탈단백 우골 (Deproteinized Bovine Bone, DPBB) + 20% 자가골 혼합. 11년 후 조직 구성: 라멜라골 (Lamellar Bone) 44.7%, 골수강 38%, DPBB 17.3%; DPBB-골 접촉률 61.5%; 입자 길이·면적은 6개월 및 미사용 입자와 통

- `mordenfeld-2010-msfa-dpbb-biopsies-11year` [sinus-lift/lateral] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: - [[sinus-lift/lateral/sartori-2003-msfa-bio-oss-10year-case-report]] — Bio-Oss 단독 10년 case report (DPBB 비율 70.2% → 13.3%로 감소 보고 — Mordenfeld 결과와 다소 상충).
  - ▸ 출발(`mordenfeld-2010-msfa-dpbb-biopsies-11year`) 세줄: 전향적 인체 조직형태계측 생검 연구 (n=11 재진입 생검, 평균 11.5년): 심한 후방 상악 위축 20명 대상 상악동거상술 (Maxillary Sinus Floor Augmentation, MSFA) — 80% 탈단백 우골 (Deproteinized Bovine Bone, DPBB) + 20% 자가골 혼합. 11년 후 조직 구성: 라멜라골 (Lamellar Bone) 44.7%, 골수강 38%, DPBB 17.3%; DPBB-골 접촉률 61.5%; 입자 길이·면적은 6개월 및 미사용 입자와 통

- `rodriguez-2019-long-term-risks-complications-bovine` [sinus-lift/lateral] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[sinus-lift/lateral/sartori-2003-msfa-bio-oss-10year-case-report]] — contrasting 10-year Bio-Oss case report describing a progressive bone-to-graft ratio shift over time (wiki-flagged as `contradicts` Mordenfeld 2010) — relevant counterpoint on whether ABB truly remains inert long-term.
  - ▸ 출발(`rodriguez-2019-long-term-risks-complications-bovine`) 세줄: 증례군 연구 (환자 5명, 개인 클리닉 의뢰 코호트, 소 유래 이종골이식재 (Bovine-derived Xenograft) 식립 후 2-13년 경과 — 대부분 상악동거상술 및 발치와 이식) — 탈단백우골 (Anorganic Bovine Bone, ABB) 이식재의 후기 임상 합병증을 기술. 증례 전반의 합병증: 상악동·상악골 병리, 이식재 입자 전위/산란, 구강상악동 누공 (Oroantral Communication), 임플란트 실패, 이물 반응 (Foreign Body Reaction)과 피막형

- `abullais-2024-maxillary-sinus-membrane-lateral-wall-cbct` [sinus-lift/lateral] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: The primary finding was **no significant correlation between facial index and either MT or LWT** (all p>0.05), refuting the hypothesis that facial morphotype could serve as a clinical surrogate for sinus anatomy. This means clinicians cannot use a patient's face shape to estimate surgical risk without a CBCT.
  - ▸ 출발(`abullais-2024-maxillary-sinus-membrane-lateral-wall-cbct`) 세줄: 안면지수(Facial Index) 유형(광면형/중면형/장면형)이 상악동 막 두께(Membrane Thickness, MT) 및 측벽 두께(Lateral Wall Thickness, LWT)의 대리 예측인자가 될 수 있는지를 검증한 후향적 CBCT 연구(n=75, 150 동, 사우디 남서부). 안면지수 유형과 MT·LWT 간 유의한 상관 없음; 여성의 LWT가 남성보다 소구치(1.83 vs 1.54 mm, p=0.018)·대구치(1.89 vs 1.56 mm, p=0.032) 부위 모두 유의하게 두꺼

- `schriber-2019-pneumatisation-maxillary-sinus-tooth-loss` [sinus-lift/lateral] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Direct radiographic refutation of "post-extraction sinus pneumatisation" as a meaningful driver of vertical bone loss in the posterior maxilla.
  - ▸ 출발(`schriber-2019-pneumatisation-maxillary-sinus-tooth-loss`) 세줄: 후향적 콘빔 컴퓨터단층촬영 (Cone-Beam Computed Tomography, CBCT) 체적 분석: 유치악 50명 vs 무치악 50명 후방 상악을 맞춤 소프트웨어로 부피·표면·최대 직경 비교. 치아 보유 여부에 따른 상악동 크기 차이 없음 (유의차 없음); 남성이 여성보다 상악동 유의하게 크고, 관찰자 간 일치도 양호. 발치 후 후방 상악 수직 골량 감소는 상악동 함기화 (Pneumatisation)가 아닌 치조정 흡수 (Alveolar Crest Resorption)에 기인 — 상악동거상

- `kato-2021-sinus-mucosa-ostium-involvement-septa` [sinus-lift/lateral] (HIGH-no-target, 'Counter to' · 반대)
  - **근거 문장**: Across 30 sinuses imaged pre-op (T0), at 1 week (T1w), and at 9 months (T9m), the swelling peaked at 1 week and **regressed to baseline by 9 months with no residual infundibular obstruction in either group**. Counter to the expectation that septa (which fragment the sinus and complicate elevation) would worsen ostium involvement, the **septa-free control group tended to swell more and obstructed m
  - ▸ 출발(`kato-2021-sinus-mucosa-ostium-involvement-septa`) 세줄: 후향적 CBCT 연구 (n=30 상악동: 격벽 15동 vs 격벽 없는 대조 15동, 모두 측방창 상악동저 거상술, T0/1주/9개월 촬영): 격벽이 술후 슈나이더막 (Schneiderian Membrane) 부종·자연공/누두 폐쇄를 악화시키는지 검증. 1주에 부종 최고조 (점막 높이 증가: 격벽군 ~5.7 mm / 대조군 ~7.1 mm), 누두 폐쇄 격벽군 3/15 vs 대조군 5/15; 9개월 후 폐쇄·부종 모두 완전 소실; 격벽군 천공 4/15 (26.7%), 대조군 0건. 측방 상악동거상술 

- `shenoy-2013-maxillary-antrolith-recurrent-sinusitis-case` [sinus-lift/pseudocyst] (HIGH-no-target, 'in contrast to' · 대조)
  - **근거 문장**: This Indian case report demonstrates the large/symptomatic end of the antrolith spectrum, in contrast to Tan 2020's asymptomatic small antrolith. The 47-year-old patient had a 1984 Caldwell-Luc surgery history for polypoid disease — residual bone chips left behind became the endogenous nidus for antrolith formation over decades.
  - ▸ 출발(`shenoy-2013-maxillary-antrolith-recurrent-sinusitis-case`) 세줄: 증례보고(인도, n=1, 47세): 과거 Caldwell-Luc 수술 후 남겨진 잔류 골편을 핵(Nidus)으로 ~30년에 걸쳐 형성된 2×1 cm 대형 상악동석(Antrolith)이 재발성 상악동염 및 구강상악동루를 유발. 내시경 부비동 수술(Endoscopic Sinus Surgery, ESS) 단독으로 제거 불가, ESS + 반복 Caldwell-Luc 복합 수술로 제거 성공; 조직검사로 골종·악성종양 감별. 이전 부비동 수술 후 남은 골/조직 잔편이 내인성 핵 역할을 하므로, 모든 ESS 

- `shenoy-2013-maxillary-antrolith-recurrent-sinusitis-case` [sinus-lift/pseudocyst] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 상악동석이 재발성 상악동염과 구강상악동루(Oroantral Fistula)를 유발한 증례. Caldwell-Luc 수술 과거력이 있는 환자에서 잔류 골편이 상악동석의 nidus가 된 메커니즘을 설명. [[sinus-lift/pseudocyst/tan-2020-maxillary-antrolith-case-report-management]]의 무증상 소형 증례와 대비되는 증상성 대형(2×1cm) 증례.
  - ▸ 출발(`shenoy-2013-maxillary-antrolith-recurrent-sinusitis-case`) 세줄: 증례보고(인도, n=1, 47세): 과거 Caldwell-Luc 수술 후 남겨진 잔류 골편을 핵(Nidus)으로 ~30년에 걸쳐 형성된 2×1 cm 대형 상악동석(Antrolith)이 재발성 상악동염 및 구강상악동루를 유발. 내시경 부비동 수술(Endoscopic Sinus Surgery, ESS) 단독으로 제거 불가, ESS + 반복 Caldwell-Luc 복합 수술로 제거 성공; 조직검사로 골종·악성종양 감별. 이전 부비동 수술 후 남은 골/조직 잔편이 내인성 핵 역할을 하므로, 모든 ESS 

- `bassir-2018-alveolar-ridge-preservation-meta-analysis` [bone-regeneration/ridge-preservation] (HIGH-no-target, 'Counterpoint' · 반대 논점)
  - **근거 문장**: - [[bone-regeneration/ridge-preservation/mardas-2023-alveolar-ridge-preservation-overtreatment]] — Counterpoint: when ARP may be overtreatment.
  - ▸ 출발(`bassir-2018-alveolar-ridge-preservation-meta-analysis`) 세줄: 체계적 문헌고찰 및 메타분석 (Systematic Review with Meta-Analysis, SR+MA, 21개 대조 연구): 치조제 보존술 (Alveolar Ridge Preservation, ARP) vs 발치 단독, 무작위 효과 모형, 7개 치수 결과 변수, 5개 사전 지정 하위군 분석. ARP가 수평 골흡수를 평균 1.86 mm (95% CI 1.44–2.28; p<.001) 감소; 7개 중 6개 치수 결과에서 ARP 우위; 소켓 형태가 가장 강한 조절 변수 (p<.001), 이식재 

- `adams-2022-clinical-evidence-alveolar-ridge-preservation` [bone-regeneration/ridge-preservation] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Evidence level is low (single narrative review, two cases) but aligns directionally with Atieh 2021 Cochrane's "very low certainty" conclusion and provides a useful clinical counterpoint to pro-ARP SR evidence, particularly relevant for informed consent about long-term xenograft complications.
  - ▸ 출발(`adams-2022-clinical-evidence-alveolar-ridge-preservation`) 세줄: BDJ 서사적 고찰 + 영국 일반의 증례 2건: 치조제 보존술(Alveolar Ridge Preservation, ARP)의 통계적 치수 보존 효과가 임상적 환자 이득으로 자동 변환되지 않음을 지적. ARP 시술 5–13년 후 이종골 만성 실패 사례 2건: 배농 누공·peri-implantitis 양상 발현, 조직학에서 비통합 이식재 입자·육아조직; Elian Type 2/3·협측 골 손실 >50% 등 특정 적응증으로 좁혀야 한다고 권고. 근거 수준 낮음(서사적 고찰·증례 2건)이나 Atieh 2

- `adams-2022-clinical-evidence-alveolar-ridge-preservation` [bone-regeneration/ridge-preservation] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: Avila-Ortiz·Majzoub 같은 ARP-positive SR 흐름에 대한 **수정주의적 counterpoint**. 영국 일반의가 자신의 진료실 케이스(5–10년 후 xenograft가 fibrous encapsulation·만성 감염·peri-implantitis 양상으로 실패)를 BDJ에 보고하며, "통계적 dimensional preservation"이 "long-term patient benefit"으로 자동 변환되지 않는다는 점을 강조. Adams 본인이 SR을 쓴 게 아니므로 evidence 등급은 낮으나, 동시기 Atieh 2021 Cochrane의 "very low certainty" 결론과 결이 맞아 ARP 임상 판단에 균형추로 인용 가치가 있음.
  - ▸ 출발(`adams-2022-clinical-evidence-alveolar-ridge-preservation`) 세줄: BDJ 서사적 고찰 + 영국 일반의 증례 2건: 치조제 보존술(Alveolar Ridge Preservation, ARP)의 통계적 치수 보존 효과가 임상적 환자 이득으로 자동 변환되지 않음을 지적. ARP 시술 5–13년 후 이종골 만성 실패 사례 2건: 배농 누공·peri-implantitis 양상 발현, 조직학에서 비통합 이식재 입자·육아조직; Elian Type 2/3·협측 골 손실 >50% 등 특정 적응증으로 좁혀야 한다고 권고. 근거 수준 낮음(서사적 고찰·증례 2건)이나 Atieh 2

- `adams-2022-clinical-evidence-alveolar-ridge-preservation` [bone-regeneration/ridge-preservation] (HIGH-no-target, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[bone-regeneration/ridge-preservation/avila-ortiz-2019-alveolar-ridge-preservation-interventions]] — pro-ARP SR+MA, counterpoint.
  - ▸ 출발(`adams-2022-clinical-evidence-alveolar-ridge-preservation`) 세줄: BDJ 서사적 고찰 + 영국 일반의 증례 2건: 치조제 보존술(Alveolar Ridge Preservation, ARP)의 통계적 치수 보존 효과가 임상적 환자 이득으로 자동 변환되지 않음을 지적. ARP 시술 5–13년 후 이종골 만성 실패 사례 2건: 배농 누공·peri-implantitis 양상 발현, 조직학에서 비통합 이식재 입자·육아조직; Elian Type 2/3·협측 골 손실 >50% 등 특정 적응증으로 좁혀야 한다고 권고. 근거 수준 낮음(서사적 고찰·증례 2건)이나 Atieh 2

- `adams-2022-clinical-evidence-alveolar-ridge-preservation` [bone-regeneration/ridge-preservation] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Provides the skeptical counterweight that [[overviews/bone-regeneration-socket-biology-and-arp-critique]] needs — documents late xenograft failure (5–13 yr) and argues statistical dimensional preservation does not equal patient-centred benefit, contradicting the ARP-positive SR/MA pool in [[overviews/socket-preservation-arp-overview]]. Re-frames Carmagnola histology and the commercial drivers behi
  - ▸ 출발(`adams-2022-clinical-evidence-alveolar-ridge-preservation`) 세줄: BDJ 서사적 고찰 + 영국 일반의 증례 2건: 치조제 보존술(Alveolar Ridge Preservation, ARP)의 통계적 치수 보존 효과가 임상적 환자 이득으로 자동 변환되지 않음을 지적. ARP 시술 5–13년 후 이종골 만성 실패 사례 2건: 배농 누공·peri-implantitis 양상 발현, 조직학에서 비통합 이식재 입자·육아조직; Elian Type 2/3·협측 골 손실 >50% 등 특정 적응증으로 좁혀야 한다고 권고. 근거 수준 낮음(서사적 고찰·증례 2건)이나 Atieh 2

- `araujo-2009-ridge-alterations-flap-vs-flapless` [bone-regeneration/ridge-preservation] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "Flapless = ridge 보존"이라는 1990s–2000s 임상 가설을 동물 모델에서 직접 반박.
  - ▸ 출발(`araujo-2009-ridge-alterations-flap-vs-flapless`) 세줄: 개 5마리 이분구강 (Split-mouth) 디자인: 전층 판막 (Full-thickness Flap) 거상 발치 vs 판막없는 발치 (Flapless Extraction), 6개월 조직형태계측 비교 — "flapless 발치가 치조제를 보존한다"는 임상 가설 검증. 양 군 모두 치조제 흡수 발생, 흡수 크기에 유의한 군 간 차이 없음 — 다발골 (Bundle Bone) 소실은 발치 방법과 무관하게 발생. Flapless 발치는 치조제 보존의 충분 조건이 아님 — 적극적 치조제 보존술 (Alveo

- `cesar-2024-dental-zirconia-15years-material-processing` [dental-materials/zirconia] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 서술적 고찰(Dental Materials 2024; Web of Science 5,102편, 31개 연구 그룹): 2008–2023년 치과용 지르코니아의 고알루미나 3Y-TZP에서 조성경사형 다층 5Y-PSZ까지 15년 진화를, 분말 기술·소결 매개변수·투광성-강도 상충관계 중심으로 종합.
  - ▸ 출발(`cesar-2024-dental-zirconia-15years-material-processing`) 세줄: 서술적 고찰(Dental Materials 2024; Web of Science 5,102편, 31개 연구 그룹): 2008–2023년 치과용 지르코니아의 고알루미나 3Y-TZP에서 조성경사형 다층 5Y-PSZ까지 15년 진화를, 분말 기술·소결 매개변수·투광성-강도 상충관계 중심으로 종합. 세대별 기준치: 1세대 3Y-TZP 900–1,200 MPa(불투명, 코어 전용) → 4Y-PSZ 700–900 MPa(입방정 >30%, 고투명) → 5Y-PSZ 600–700 MPa(입방정 >50%, 매우 

- `davoudi-2025-zirconia-abutments-biological-mechanical-esthetic` [dental-materials/zirconia] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 변연골소실(Marginal Bone Loss, MBL)은 10편 중 4편 Zr 우세·6편 무차이; 연조직 퇴축·치은 변색도 대체로 무차이 또는 Zr 우세; 기계적 합병증 위험비(Risk Ratio)는 비유의(0.87, 0.52), 생존율도 통계적으로 동등(Zr 98.6~98.8% vs. Ti 98.62~99.4%) — 이론적 파절저항(Ti 1454N vs. Zr 443.6N)·굴곡강도(Ti 2000MPa vs. Zr 900~1200MPa) 상 Ti 우위와 대비되는 임상 결과.
  - ▸ 출발(`davoudi-2025-zirconia-abutments-biological-mechanical-esthetic`) 세줄: 우산형 검토(Umbrella Review) — AMSTAR 체크리스트로 선별된 14편의 체계적 문헌고찰/메타분석(2023년 3월까지, 환자 6,456명·임플란트 10,063개) 대상, 지르코니아(Zirconia, Zr) vs. 티타늄(Titanium, Ti) 임플란트 지대주(abutment)의 생물학적·심미적·기계적/생존 지표 비교. 변연골소실(Marginal Bone Loss, MBL)은 10편 중 4편 Zr 우세·6편 무차이; 연조직 퇴축·치은 변색도 대체로 무차이 또는 Zr 우세; 기계적 합

- `alhomoud-2023-behavior-anxiety-levels-pediatric-patient` [behavioral-dentistry/dental-anxiety] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: dental-anxiety 하위 카테고리의 실측 데이터 축. [[wiki/behavioral-dentistry/dental-anxiety/jkda-2021-60-1-003]](성인 phobia)와 대비되는 소아 데이터 — Frankl·Venham·categorical scale로 150명 측정. 연령·성별 효과를 정량화해 [[wiki/behavioral-dentistry/dental-anxiety/pediatric-2026-dental-anxiety-contemporary-assessment-management]](소아 불안 관리 review)의 primary 근거로 연결.
  - ▸ 출발(`alhomoud-2023-behavior-anxiety-levels-pediatric-patient`) 세줄: 단면연구 (2–14세 소아 150명, 샤르자, 23주 모집) — 방문 종료 시점에 Frankl 행동척도·Venham 불안척도·범주형 척도 3종으로 치과 행동·불안 측정. 성별 차이 없음; 연령군 간 유의차(Kruskal-Wallis) — 11–14세가 울음(p=.034)·협조(p=.002)·불안감(p=.003) 등 거의 모든 척도에서 가장 두드러짐. 소아는 치과 내원 시 불안이 높으며, 성별이 아닌 연령이 주요 인구통계학적 변수; 아동과 보호자 모두에게 효과적인 양방향 소통이 핵심 관리 전략.

- `elwyn-2025-shared-decision-making-primer-clinicians` [behavioral-dentistry/communication-relationship] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: SDM 지지자 집단의 목적 표본이므로 효과 추정치가 아닌 실용 가이드로 활용해야 하며, 임플란트 대 대안 선택, 심미적 상충 결정 등 치과의 선택 민감 결정에 직접 적용할 수 있다.
  - ▸ 출발(`elwyn-2025-shared-decision-making-primer-clinicians`) 세줄: 공유의사결정(Shared Decision-Making, SDM) 임상의용 primer: 13개국 25인(국제SDM학회)이 공동 제작 — SDM을 원칙으로는 지지하지만 실제 진료에서 실행으로 이어지지 않는 간격(principle-to-practice gap)을 다룬다. SDM의 정의와 오해를 정리하고, "시간이 없다", "환자가 원하지 않는다", "이미 동의 받고 있다"는 반복 우려에 구조화된 답변을 제공하며 환자 의사결정 보조도구(Patient Decision Aid, PDA)를 진료 흐름에 위치

- `barber-2019-shared-decision-making-orthodontics` [behavioral-dentistry/communication-relationship] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 교정학에서 공유의사결정(Shared Decision-Making, SDM)을 환자와 "함께" 결정하는 것으로 재정의한 서술적 리뷰 — 발치 여부, 장치 종류, 심미-기능 상충 같은 선호 민감 결정에서 환자 가치가 결정의 핵심이다.
  - ▸ 출발(`barber-2019-shared-decision-making-orthodontics`) 세줄: 교정학에서 공유의사결정(Shared Decision-Making, SDM)을 환자와 "함께" 결정하는 것으로 재정의한 서술적 리뷰 — 발치 여부, 장치 종류, 심미-기능 상충 같은 선호 민감 결정에서 환자 가치가 결정의 핵심이다. SDM의 핵심 단계, 교정 진료에서의 주요 도입 장벽, 그리고 검증된 교정용 환자 의사결정 보조도구(Patient Decision Aid, PDA) 부재 등 통합을 막는 근거 공백을 정리한다. 초록만 확보된 agenda-setting 논문으로 효과 추정치는 없으며, 교정

- `bonetti-2018-general-health-promotion-dental-engage` [behavioral-dentistry/motivational-interviewing] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Quantifies — and largely refutes — the perceived-offense barrier clinicians assume.
  - ▸ 출발(`bonetti-2018-general-health-promotion-dental-engage`) 세줄: 교차단면 실행가능성 연구(스코틀랜드; 환자 n=200, 치과의사(General Dental Practitioner, GDP) 18명) — ENGAGE는 검진 중 5분 이내 생활습관(흡연·음주·식이) 위험 전달 + 무료 NHS 상담전화 연결 중재임. 환자의 10% 미만만 불쾌감을 느끼고, 70% 이상이 전문적 태도에 안심감을 보고했으며, GDP 18명 중 17명이 실행 가능·현행 진료 개선으로 평가. 수용성·실행가능성은 확인되었으나 행동변화 실제 효과는 향후 영국 다기관 무작위대조시험(Randomi

- `kapetanaki-2021-access-cavity-designs-endodontic-review` [endodontics/anatomy] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - Refutes the claim that MIA improves tooth prognosis over conventional TEC
  - ▸ 출발(`kapetanaki-2021-access-cavity-designs-endodontic-review`) 세줄: 문헌고찰(PubMed/Scopus/WoS): 전통 접근와동(TEC)과 최소침습 접근와동(MIA)을 근관구 위치·기구 조작·파절 저항·의원성 위험 측면에서 비교. MIA로의 전환을 지지하는 근거 불충분: MIA는 근관구 탐색 어려움 증가·직선 접근 제한·파절 저항 이득 불명확·의원성 합병증 위험 증가. 유도 근관치료(정적 3D 인쇄 스텐트·동적 실시간 추적)는 근관 석회화에 유망하나 비용-편익 분석·RCT 비교 데이터 부재.

- `cruz-2014-debris-apical-third-naocl-glyde-in-vivo` [endodontics/irrigation] (HIGH-no-target, 'Contrary to' · 상반된 결과)
  - **근거 문장**: This in vivo study tested whether an EDTA lubricating paste (Glyde File Prep) helps eliminate debris during cleaning and shaping. Contrary to the lubrication rationale, canals prepared with Glyde showed greater debris accumulation in the apical third, while canals prepared with sodium hypochlorite irrigation and a final rinse (no paste) were left with little or no apical debris. The practical impl
  - ▸ 출발(`cruz-2014-debris-apical-third-naocl-glyde-in-vivo`) 세줄: 발거 예정 치아를 대상으로 한 in vivo 연구로, Glyde File Prep(EDTA 페이스트 윤활제) 사용 회전 기구 군과 NaOCl 단독 세척 군을 현미경으로 apical third debris를 비교. Glyde 사용 군에서 apical third debris가 더 많이 축적된 반면, NaOCl + 최종 세척 군(페이스트 없음)은 debris가 거의 없었음. EDTA 페이스트 윤활제는 직관과 달리 기구조작 중 근첨부에 debris를 가두므로, 근첨 청결도를 위해서는 페이스트 없이 충분한

- `abraham-2025-instrumentation-kinematics-postendodontic-pain-umbrella` [endodontics/shaping] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[endodontics/shaping/singh-2026-rotary-reciprocating-kinematics-postoperative-pain-retreatment-sr]] — narrower-scope SR limited to endodontic *retreatment* (5 RCT, n=554), found no significant rotary-vs-reciprocating pain difference (though hand files caused significantly more pain at 48h); this umbrella review's broader (non-retreatment-restricted) 8-SR synthesis instead leans toward a rotary 
  - ▸ 출발(`abraham-2025-instrumentation-kinematics-postendodontic-pain-umbrella`) 세줄: 우산연구(Umbrella Review, PROSPERO CRD42024582245) — 근관형성기구 운동학(Instrumentation Kinematics: 회전형 rotary vs 왕복형 reciprocating vs 수동)이 근관치료 후 통증(Post-endodontic Pain, POP)에 미치는 영향을 다룬 SR 8편(7편 메타분석 포함, 2018-2022년 발표)을 AMSTAR-2(전부 고품질, 12.5-15/16)·ROBIS로 통합 평가. 회전형(rotary)이 전반적 통증과 중등도~중

- `lee-2026-residual-pericervical-apical-dentine-vertical` [endodontics/shaping] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 핵심 임상 시사: 대구치에서 치근단 성형 크기 최소화(치경부 상아질 보존만이 아님)가 VRF 예방 핵심 전략; 포스트(Post) 존재는 대구치 한정 분석에서 유의한 위험인자가 아님(기존 다치종 연구와 상충).
  - ▸ 출발(`lee-2026-residual-pericervical-apical-dentine-vertical`) 세줄: 후향적 환자-대조군 연구(STROBE; 수직치근파절 VRF 44례 vs 비VRF 대조군 92례; 근관치료된 대구치 136개, 고립성 치주낭 깊이 PD ≥5 mm; 도쿄 전문의 클리닉 2012–2020) — 방사선 사진 기반 4단계 잔존 상아질 분류(급간일치도 kappa >0.8) + 다변량 로지스틱 회귀. 치근단부(Apical) 잔존 상아질 과다 소실(근관충전물/치근 폭 비율 >0.21; 조정 OR 12.9, p=0.001)이 VRF 가장 강력한 독립 방사선학적 예측인자; 치경부(Pericervi

- `nemec-2026-clear-aligner-patient-needs-expectations` [orthodontics/clear-aligner] (HIGH-far→alhuwaizi-2026-clear-aligner-fixed-oral-hygiene-periodontal-grade-sr, 'counterpoint' · 반대 논점)
  - **근거 문장**: - [[orthodontics/clear-aligner/alhuwaizi-2026-clear-aligner-fixed-oral-hygiene-periodontal-grade-sr]] — oral hygiene/periodontal comparison; relevant since Nemec 2026 found patients rate oral-hygiene impairment as a low-moderate concern (3.1/10), a useful counterpoint for consent discussions.
  - ▸ 출발(`nemec-2026-clear-aligner-patient-needs-expectations`) 세줄: 전향적 코호트 연구(n=82, 빈 2개 기관): 투명교정(CAT) 시작 전 32문항 VAS 설문으로 기대치를 5개 요인 범주로 분석. 치료 예측가능성(8.6/10)·고정식 교정 동등 효과(9.5/10)에 대한 기대가 최고 수준인 반면, 비용·기간 단축을 위해 결과 질을 양보하려는 의향은 거의 없었음(타협 항목 모두 ≤2.6/10). 약 54.8%가 치료 후 불만을 경험한다는 데이터를 고려해, 특히 교합 이상(PAR >17)이 심한 환자에게는 통증·식이제한 우려에 대해 사전 충분한 설명이 필요.

- `charoenrat-2025-clear-aligner-anterior-open-bite-molar-intrusion-sr-ma` [orthodontics/clear-aligner] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 기존 [[wiki/orthodontics/clear-aligner/yassir-2022-cat-vs-fat-overview-systematic-reviews]]는 투명교정 (Clear Aligner Treatment, CAT)이 sagittal/transverse 이동(torque·정출·회전)에서 고정식 장치 (Fixed Appliance Treatment, FAT)보다 열등하다는 severity boundary만 제시할 뿐, 수직적 문제(anterior open bite)에 대한 상세 메커니즘은 다루지 않았다. 본 SR+MA (Charoenrat 2025)는 open bite 교정 시 CAT이 절치 정출 (incisor extrusion)과 구치 압하 (molar intrusion) 중 무엇으로 overb
  - ▸ 출발(`charoenrat-2025-clear-aligner-anterior-open-bite-molar-intrusion-sr-ma`) 세줄: SR+MA (PRISMA/PROSPERO, 10편 — non-RCT 4편·전후비교 6편): 전치부 개방교합 교정에서 투명교정(Clear Aligner Treatment, CAT)과 TAD 병용 고정식 장치(FATADs)를 비교. CAT는 절치 정출(상악 +0.87 mm, 하악 +1.06 mm)로 overbite를 +2.77 mm 증가시키나 구치 압하는 유의하지 않았고, FATADs는 구치 압하(상악 +1.88 mm, 하악 +0.45 mm)를 통해 CAT보다 +1.64 mm 더 큰 overbite 

- `monisha-2024-efficacy-of-clear-aligner` [orthodontics/clear-aligner] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - GRADE certainty: **very low** for both 7-day-vs-14-day and 10-day-vs-14-day OTM efficacy comparisons (downgraded for risk of bias and very serious inconsistency — contradictory results between studies with comparable designs, e.g., Al-Nadawi vs. Zhao for 10-day vs 14-day).
  - ▸ 출발(`monisha-2024-efficacy-of-clear-aligner`) 세줄: 체계적 문헌고찰 (PROSPERO CRD42021288179), 6개 연구 (RCT 3편, 비RCT 3편; n=449)로 성인에서 단축 투명교정장치 착용 프로토콜(7일, 10일)과 기존 14일 프로토콜의 치아이동(OTM) 효율성을 비교. 6편 중 4편은 프로토콜 간 유의한 차이 없음; 2편(RCT 포함)은 특정 후방 치아이동(상악 압하/원심경사/협측토크, 하악 압하/정출)에서 14일 프로토콜이 유의하게 더 정확; GRADE 근거수준은 OTM 효율성에 대해 매우 낮음, 통증에 대해서는 높음(10일 

- `monisha-2024-efficacy-of-clear-aligner` [orthodontics/clear-aligner] (SOFT→nakornnoi-2024-aligner-trimline-biomechanics-tooth-movement-sr, 'unlike' · 다름)
  - **근거 문장**: This SR addresses a concrete chairside protocol question — how many days a patient should wear each aligner tray before advancing — that is directly actionable at the operatory level, unlike most clear-aligner papers in this wiki that focus on biomechanics or material properties. It complements [[orthodontics/clear-aligner/nakornnoi-2024-aligner-trimline-biomechanics-tooth-movement-sr]] (trimline/
  - ▸ 출발(`monisha-2024-efficacy-of-clear-aligner`) 세줄: 체계적 문헌고찰 (PROSPERO CRD42021288179), 6개 연구 (RCT 3편, 비RCT 3편; n=449)로 성인에서 단축 투명교정장치 착용 프로토콜(7일, 10일)과 기존 14일 프로토콜의 치아이동(OTM) 효율성을 비교. 6편 중 4편은 프로토콜 간 유의한 차이 없음; 2편(RCT 포함)은 특정 후방 치아이동(상악 압하/원심경사/협측토크, 하악 압하/정출)에서 14일 프로토콜이 유의하게 더 정확; GRADE 근거수준은 OTM 효율성에 대해 매우 낮음, 통증에 대해서는 높음(10일 
  - ▸ 대상(`nakornnoi-2024-aligner-trimline-biomechanics-tooth-movement-sr`) 세줄: 체계적 문헌고찰 (5개 데이터베이스, 2000년 1월–2024년 8월, ROBINS-I, 12편, 낮음–중등도 비뚤림): aligner trimline(치은연 형태·연장)이 치아이동에 미치는 역학적 영향 — attachment·앵커리지와 함께 세 번째 예측성 결정인자로 분리. Straight/extended trimline margin이 scalloped/short 대비 높은 force·moment, 우수한 유지력 → 함입·translation·tipping·root torque에서 더 큰 치아이

- `nucera-2022-composite-attachments-clear-aligners-sr` [orthodontics/clear-aligner] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The answer: attachments **mostly increase** treatment effectiveness, with the clearest benefit for **anterior root torque, rotation, mesio-distal movement**, and **posterior anchorage** — exactly the movements aligners express poorly without purchase. Results were **contradictory or non-significant** for some movements; **intrusion** may improve but the evidence is weak; **extrusion** evidence is 
  - ▸ 출발(`nucera-2022-composite-attachments-clear-aligners-sr`) 세줄: 체계적 문헌고찰 (8개 데이터베이스, 2020년 3월까지, 임상 5편, 중등도 비뚤림): 컴포지트 attachment가 투명교정 효과에 미치는 영향 — 6개 이동 카테고리에서 도움이 되는 곳과 안 되는 곳을 분리. 컴포지트 attachment는 대체로 효과를 높임: 전치부 root torque·rotation·근원심 이동·후방 앵커리지에서 가장 뚜렷한 이득(attachment 없이 잘 발현 안 되는 이동들 정확히); 함입(intrusion)은 개선 가능하나 근거 약함, 정출(extrusion)·후

- `wang-2025-clear-aligner-premolar-extraction-3d-tooth-movement` [orthodontics/clear-aligner] (HIGH-no-target, 'Overturn' · 결론 뒤집음)
  - **근거 문장**: - Overturns the prior crown-only assumption that canines (U3) lingually incline during extraction-space closure: root-inclusive data show U3 actually moves **buccally** as a whole, with the crown outpacing the root.
  - ▸ 출발(`wang-2025-clear-aligner-premolar-extraction-3d-tooth-movement`) 세줄: 후향적 연구, 47명(542개 치아) 4소구치 발치 투명교정(CAT) 증례; 치료 전후 CBCT 중첩으로 크라운뿐 아니라 치근의 3차원 이동을 측정하여 ClinCheck 설계값과 비교. 치근 이동은 크라운 대비 일관되게 미달성 — 전후방(APD)에서 U1 치근이 최대 불일치(5.49±2.30 mm); 전치는 함입 설계에도 불구하고 오히려 정출되었고, U3 크라운은 설계된 원심이동의 71.5%만 달성; 연령, 발치부위(U4 vs U5), 고정원 방법, 단계화 방식, 부착물 설계가 불일치에 유의한 영

- `tang-2025-evaluating-the-effectiveness-of-clear` [orthodontics/clear-aligner] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Pre-treatment CoS was **NOT correlated with** age, crowding, gender, or craniofacial patterns (sagittal/vertical skeletal classification)—contradicting some older literature (Trouten, Orthlieb) but supporting recent studies (Halimi, Rozzi, Farella, Krüsi).
  - ▸ 출발(`tang-2025-evaluating-the-effectiveness-of-clear`) 세줄: 회상적 연구 (n=60: 추출 30명, 비추출 30명)로 투명교정(Invisalign) 하에서 하악 스피 곡선 성형을 비교; 3D 모델 측정 (Geomagic Studio). 추출군은 예측된 것과 실제 스피 곡선 변화 사이의 현저히 큰 불일치 (−1.38±0.74 mm vs. −0.84±0.58 mm, p<0.001)를 보여, 비추출군 대비 효과성 저하 나타냄. 치료 후 스피 곡선은 치료 전 스피 곡선 및 예측된 스피 곡선과 양의 상관, 초기 혼잡과는 음의 상관; 추출 환자는 현재 부착 설계로 극

- `shi-2026-pre-treatment-associated-factors` [orthodontics/clear-aligner] (HIGH-no-target, 'contrary to' · 상반된 결과)
  - **근거 문장**: Gingival biotype and amount of anterior tooth retraction were NOT significant predictors, contrary to hypothesis; small sample (only 13 OGE events) and single-center, single-ethnicity design limit generalizability pending external multicenter validation.
  - ▸ 출발(`shi-2026-pre-treatment-associated-factors`) 세줄: 후향적 단일기관 코호트 연구(초기 630명 중 75명) — 영구치열기 환자에서 Invisalign 투명교정장치(Clear Aligner Therapy, CAT)로 시행한 순차적 양측 상악 대구치 원심이동(Molar Distalization, 측당 2-4mm) 후 Jemt 유두지수로 평가한 상악 중절치 개방형 치은유두(Open Gingival Embrasure, OGE, 일명 black triangle) 발생. OGE 발생률 17.3%(13/75); 다변량 로지스틱 회귀에서 나이(OR 1.17), 

- `goncalves-2023-invisalign-upper-incisor-accuracy-sr` [orthodontics/clear-aligner] (HIGH-no-target, 'Overturn' · 결론 뒤집음)
  - **근거 문장**: - Overturns the common clinical assumption that vertical movement is uniformly hard for aligners: intrusion is unreliable (down to 0%), but extrusion is one of the *most* accurate movements (up to 142.4%).
  - ▸ 출발(`goncalves-2023-invisalign-upper-incisor-accuracy-sr`) 세줄: 체계적 문헌고찰(PRISMA, PROSPERO CRD42020190272)로 비무작위 연구 5편(후향 4 + 전향 1, 환자 20–38명, 상악절치 이동 총 612건)에서 Invisalign 상악 중절치·측절치 예측-달성 이동 정확도를 2010년 SmartTrack 도입 이후 자료로 정량화. 정확도는 0%(예측된 함입이 반대로 정출됨)부터 155.7%(설측경사 과달성)까지; torque는 일관되게 가장 낮은 정확도 축(49.1–51.5%), tip 38.5–155.7%, rotation 41.8–

- `kim-2026-efficacy-and-stability-of` [orthodontics/clear-aligner] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[orthodontics/clear-aligner/fonseca-planells-2026-clear-aligner-maxillary-expansion-growing]] — refines: that SR+MA (mostly retrospective studies) found CA significantly *inferior* to conventional expanders on intermolar distance (−1.77 mm) and palatal volume; this prospective non-inferiority cohort found no significant intermolar/molar-region difference, refining the picture to show CA "catche
  - ▸ 출발(`kim-2026-efficacy-and-stability-of`) 세줄: 전향적 다기관 코호트 연구, 상악 횡적 부족 성장기 환자 48명(평균연령 9.3±1.7세; 투명교정군 24명, 완속상악확장장치(SME)군 24명) 대상, 치료전·확장후·유지후(3개월 이상) 시점에서 투명교정(Invisalign) vs SME 확장 비교. 사전 설정 비열등성 마진(1.6mm) 기준 1차 결과지표(구치간 횡적 확장)에서 투명교정이 SME 대비 비열등; 견치 첨두부 확장은 투명교정군이 유의하게 더 컸고 연령이 견치부 확장의 음의 예측인자였으며, 투명교정군에서만 구치 협측경사 재발이 유의

- `zhuo-2026-the-roller-coaster-effect` [orthodontics/clear-aligner] (HIGH-no-target, 'counter to' · 반대)
  - **근거 문장**: - **Between-group comparison**: Mi group showed significantly greater FCD increases than Mo-Se group across compared sites (all p<0.05) — i.e., mild-crowding cases are at *higher* risk of RCE than more severely crowded cases, an outcome that runs counter to a naive assumption that "more crowding = more complex treatment = more risk."
  - ▸ 출발(`zhuo-2026-the-roller-coaster-effect`) 세줄: 회고적 연구, 4개 제1소구치 발치 후 투명교정(CAT)을 받은 65명 (경도 총생 34명, 중등도-중증 총생 31명); 3D 디지털 모델에서 치료 전후 구치부 기능교두거리(FCD) 측정. 경도 총생군에서는 모든 구치부 부위에서 치료 후 FCD가 유의하게 증가(제1대구치에서 가장 큼: 협측근심 1.64±1.39mm, 협측원심 1.48±1.55mm, 모두 p<0.001)했고, 중등도-중증 총생군은 제1대구치 협측근심 교두에서만 증가(p<0.001); 작은 ANB각과 큰 상악전치 순측경사(U1-NA,

- `porporatti-2026-clear-aligners-bruxism-systematic-review` [orthodontics/clear-aligner] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The dominant signal is **neutrality**. No study showed a change in the overall **SB index**. A recurring nuance is that aligners tend to reduce **tonic** contractions (clenching / occlusal load) while their effect on **phasic** activity (grinding) is inconsistent — one RCT even reported a transient *increase* in phasic contractions. Most EMG effects appear in the first month and then fade, consist
  - ▸ 출발(`porporatti-2026-clear-aligners-bruxism-systematic-review`) 세줄: 이갈이(Bruxism)와 투명교정(CAT)에 대한 최초 체계적 문헌고찰 (PROSPERO CRD420251053793; PRISMA 2020; GRADE; 857건 → 11편, n=818, 여성 72.8%; RCT 5 + 비무작위 6; 진단방법·추적기간 이질성으로 메타분석 불가). 수면이갈이지수(SB index)를 변화시킨 연구 없음; 투명교정은 긴장성 수축(tonic/clenching)을 자주 감소시키나 위상성 수축(phasic/grinding)에는 비일관·일시적(한 RCT는 일시적 증가 보고)

- `huang-2026-clear-aligner-mandibular-advancement-vs-functional-class-ii-sr-ma` [orthodontics/clear-aligner] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: This 2026 SR+MA is the larger, newer counterpart to [[wiki/orthodontics/clear-aligner/yu-2023-mandibular-advancement-aligner-vs-functional-class-ii-sr-ma]] on the identical CAMA-vs-functional-appliance Class II question. Both independently conclude comparable skeletal effect plus superior lower-incisor torque control with CAMA, so it **reinforces** (does not overturn) Yu, and adds a Herbst-specifi
  - ▸ 출발(`huang-2026-clear-aligner-mandibular-advancement-vs-functional-class-ii-sr-ma`) 세줄: PROSPERO 등록 SR+MA (PRISMA 2020, 1589건 → 9편, RCT 1 + NRSI 8, n=465 성장기 골격성 Class II): 투명교정 하악전방유도(CAMA)와 트윈블록·Herbst·Vanbeek Activator 비교. CAMA는 트윈블록·Herbst 대비 모든 시상 골격 지표(SNA/SNB/ANB/Wits) 및 수직 지표에서 유의차 없음(NS); 미처치 대조군 대비 실제 골격 변화 확인(SNB +1.00°, ANB −1.55°); 트윈블록 대비 overjet 감소 약간

- `yassir-2022-cat-vs-fat-overview-systematic-reviews` [orthodontics/clear-aligner] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: CAT는 경증~중등도 부정교합(주로 비발치)에 임상적으로 유효하나 중증 케이스 및 특정 어려운 이동(전치 torque·정출·회전)에서 열등; 치주 건강은 CAT 우위(가철식, 위생 접근 용이), 치근흡수 위험 낮은 경향, 재발은 CAT에서 더 큼, 기간 근거 상충(경증에서 더 짧을 수 있음).
  - ▸ 출발(`yassir-2022-cat-vs-fat-overview-systematic-reviews`) 세줄: SR 통합 umbrella review (PROSPERO CRD42021246855; 361편 검색 → 18편 포함): 효능·부작용·치주 건강·재발·기간·편의 전반에서 투명교정(CAT) vs 고정장치(FAT)를 비교한 최고 수준 합성. CAT는 경증~중등도 부정교합(주로 비발치)에 임상적으로 유효하나 중증 케이스 및 특정 어려운 이동(전치 torque·정출·회전)에서 열등; 치주 건강은 CAT 우위(가철식, 위생 접근 용이), 치근흡수 위험 낮은 경향, 재발은 CAT에서 더 큼, 기간 근거 상충(

- `tabone-2026-clear-aligner-oral-microbiome-sr` [orthodontics/clear-aligner] (HIGH-no-target, '반론' · 반론)
  - **근거 문장**: 단기(4–24시간) CA 착용은 일시적 alpha diversity 감소, Firmicutes 증가, aligner 내 액체 pH 산성화; 중장기(1–12개월) CA는 치태지수(PI), S. mutans/유산균 고위험 비율(~8–10% vs 브라켓 ~40%), 치주 안정성에서 FA 대비 일관 우위 — 단, Wang et al.(기능성 메타게놈)은 Invisalign이 FA 대비 미생물총 구성·기능에서 우월하지 않다는 반론 결과 보고.
  - ▸ 출발(`tabone-2026-clear-aligner-oral-microbiome-sr`) 세줄: PRISMA/PROSPERO 등록 체계적 문헌고찰 (PROSPERO 628072; 34건 → 관찰연구 12편, 4시간~12개월 추적; RCT 없음; AXIS 비뚤림 도구): 투명교정 전체 기간에 걸쳐 구강 미생물총 구성 데이터(16S rRNA, qPCR)와 임상 치주·우식 지표를 통합한 최초 SR. 단기(4–24시간) CA 착용은 일시적 alpha diversity 감소, Firmicutes 증가, aligner 내 액체 pH 산성화; 중장기(1–12개월) CA는 치태지수(PI), S. mutan

- `tabone-2026-clear-aligner-oral-microbiome-sr` [orthodontics/clear-aligner] (HIGH-no-target, '반론' · 반론)
  - **근거 문장**: 근거 질 전반 취약: 12편 모두 비무작위 관찰 연구, 대부분 대조군 없음, 방법론 이질성으로 메타분석 불가, Wang et al.의 반론 결과는 CA 미생물총 이점의 일관성 결론 전 주의 요망.
  - ▸ 출발(`tabone-2026-clear-aligner-oral-microbiome-sr`) 세줄: PRISMA/PROSPERO 등록 체계적 문헌고찰 (PROSPERO 628072; 34건 → 관찰연구 12편, 4시간~12개월 추적; RCT 없음; AXIS 비뚤림 도구): 투명교정 전체 기간에 걸쳐 구강 미생물총 구성 데이터(16S rRNA, qPCR)와 임상 치주·우식 지표를 통합한 최초 SR. 단기(4–24시간) CA 착용은 일시적 alpha diversity 감소, Firmicutes 증가, aligner 내 액체 pH 산성화; 중장기(1–12개월) CA는 치태지수(PI), S. mutan

- `tabone-2026-clear-aligner-oral-microbiome-sr` [orthodontics/clear-aligner] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: However, the review explicitly flags a **dissenting result**: one included study (Wang et al., functional/inferred metagenome analysis) found that both FA and Invisalign caused oral microbiome dysbiosis, that Invisalign was not superior to FA in microbiome composition or function, and that the Invisalign group showed higher predisposition to periodontal-disease-associated metabolic pathway enrichm
  - ▸ 출발(`tabone-2026-clear-aligner-oral-microbiome-sr`) 세줄: PRISMA/PROSPERO 등록 체계적 문헌고찰 (PROSPERO 628072; 34건 → 관찰연구 12편, 4시간~12개월 추적; RCT 없음; AXIS 비뚤림 도구): 투명교정 전체 기간에 걸쳐 구강 미생물총 구성 데이터(16S rRNA, qPCR)와 임상 치주·우식 지표를 통합한 최초 SR. 단기(4–24시간) CA 착용은 일시적 alpha diversity 감소, Firmicutes 증가, aligner 내 액체 pH 산성화; 중장기(1–12개월) CA는 치태지수(PI), S. mutan

- `tabone-2026-clear-aligner-oral-microbiome-sr` [orthodontics/clear-aligner] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Surfaces a genuine internal contradiction in the evidence base (Wang et al.'s functional-metagenome finding that Invisalign does not outperform FA), rather than smoothing it into the dominant favorable narrative — useful for calibrating confidence.
  - ▸ 출발(`tabone-2026-clear-aligner-oral-microbiome-sr`) 세줄: PRISMA/PROSPERO 등록 체계적 문헌고찰 (PROSPERO 628072; 34건 → 관찰연구 12편, 4시간~12개월 추적; RCT 없음; AXIS 비뚤림 도구): 투명교정 전체 기간에 걸쳐 구강 미생물총 구성 데이터(16S rRNA, qPCR)와 임상 치주·우식 지표를 통합한 최초 SR. 단기(4–24시간) CA 착용은 일시적 alpha diversity 감소, Firmicutes 증가, aligner 내 액체 pH 산성화; 중장기(1–12개월) CA는 치태지수(PI), S. mutan

- `tabone-2026-clear-aligner-oral-microbiome-sr` [orthodontics/clear-aligner] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: **Contradicting study:** Wang et al.'s functional/inferred-metagenome analysis found both FA and Invisalign caused dysbiosis, with Invisalign showing higher predisposition to periodontal-disease-associated metabolic pathways (energy, amino acid, carbohydrate, terpenoid metabolism) versus FA (membrane transport, nucleotide metabolism) — concluding Invisalign did not outperform FA microbiologically,
  - ▸ 출발(`tabone-2026-clear-aligner-oral-microbiome-sr`) 세줄: PRISMA/PROSPERO 등록 체계적 문헌고찰 (PROSPERO 628072; 34건 → 관찰연구 12편, 4시간~12개월 추적; RCT 없음; AXIS 비뚤림 도구): 투명교정 전체 기간에 걸쳐 구강 미생물총 구성 데이터(16S rRNA, qPCR)와 임상 치주·우식 지표를 통합한 최초 SR. 단기(4–24시간) CA 착용은 일시적 alpha diversity 감소, Firmicutes 증가, aligner 내 액체 pH 산성화; 중장기(1–12개월) CA는 치태지수(PI), S. mutan

- `tabone-2026-clear-aligner-oral-microbiome-sr` [orthodontics/clear-aligner] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: 기존 [[wiki/orthodontics/clear-aligner/alhuwaizi-2026-clear-aligner-fixed-oral-hygiene-periodontal-grade-sr]]는 CA(clear aligner) vs FA(fixed appliance)의 구강위생·치주 지표(PI, GI, BOP 등) 임상 결과를 다루지만, 그 표면적 지표를 만들어내는 **구강 미생물총(oral microbiome) 조성 변화** 자체는 다루지 않는 gap이었다. 본 SR(Tabone 2026, PRISMA, 12편 관찰연구 정성종합, PROSPERO 628072)은 CA 착용 중 alpha/beta diversity, 특정 taxa(균종) 변화를 시간대별(4시간~12개월)로 정리해 그 gap을 직접 메운다. 
  - ▸ 출발(`tabone-2026-clear-aligner-oral-microbiome-sr`) 세줄: PRISMA/PROSPERO 등록 체계적 문헌고찰 (PROSPERO 628072; 34건 → 관찰연구 12편, 4시간~12개월 추적; RCT 없음; AXIS 비뚤림 도구): 투명교정 전체 기간에 걸쳐 구강 미생물총 구성 데이터(16S rRNA, qPCR)와 임상 치주·우식 지표를 통합한 최초 SR. 단기(4–24시간) CA 착용은 일시적 alpha diversity 감소, Firmicutes 증가, aligner 내 액체 pH 산성화; 중장기(1–12개월) CA는 치태지수(PI), S. mutan
