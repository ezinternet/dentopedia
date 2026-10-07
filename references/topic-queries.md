# Topic Queries — PubMed 쿼리식 카탈로그

새 토픽 추가·쿼리 튜닝은 **이 파일과 `state.json`의 `topics`** 를 함께 고친다.
SKILL.md 본문은 건드리지 않는다.

## 쿼리 작성 규칙

- 핵심어는 동의어를 OR로 묶어 누락을 줄인다. MeSH가 안정적이면 `[MeSH Terms]` 병용.
- publication type은 `state.json`의 `ptyp` 배열로 관리하고, `sweep_state.py load`가 자동으로 절(clause)을 붙인다. 쿼리식 본문에는 ptyp를 직접 쓰지 않는 걸 권장(중복 방지).
- 날짜는 쿼리에 넣지 말 것 — `search_articles`의 `date_from` + `datetype=edat` 파라미터로 건다.
- 너무 넓으면 신규가 매주 수십 건씩 쌓여 큐가 범람한다. 토픽을 쪼개거나 핵심어를 좁혀라.

## ptyp 코드 (state.json에서 사용)

| 코드 | PubMed 태그 |
|---|---|
| RCT | Randomized Controlled Trial[Publication Type] |
| SR | Systematic Review[Publication Type] |
| MA | Meta-Analysis[Publication Type] |
| GUIDE | Guideline[Publication Type] |
| COHORT | Cohort Studies[MeSH Terms] |

기본 권장 조합은 RCT+SR+MA. 가이드라인을 따로 따라잡고 싶으면 GUIDE만 켠 별도 토픽을 만드는 게 깔끔하다.

## 시드 토픽

아래는 출발점일 뿐, 네 관심 도메인에 맞춰 쪼개고 늘려라.

### implant
```
(dental implant OR osseointegration OR peri-implantitis OR "implant stability" OR osseodensification)
```
세분 예: `implant-loading`(progressive loading, ISQ/RFA), `implant-soft-tissue`(keratinized mucosa, soft tissue augmentation), `implant-grafting`(GBR, socket shield, TSFE).

#### implant-iip (검증된 보정판 — 노이즈 차단 실측 완료)
IIP(immediate implant placement)는 핵심어를 풀어 쓰면 osseodensification·ridge augmentation·macrogeometry 등이 "immediately…" 부수표현 때문에 딸려온다(실측: 풀어쓰기 32건 중 노이즈 12건). 반드시 phrase(`[tiab]`)로 묶는다:
```
("immediate implant placement"[tiab] OR "immediately placed implant"[tiab] OR "immediate placement"[tiab] OR "immediate implantation"[tiab])
```
주의: PubMed는 IIP를 `Immediate Dental Implant Loading[MeSH]`로 색인해 IIL(즉시부하)과 섞는다. 식립만 노린다면 abstract 확인 단계에서 IIL(immediate loading/provisionalization)을 한 번 더 분리할 것. MeSH 단독 의존 금지.

### endo
```
(root canal OR endodontic OR "vital pulp therapy" OR "pulp capping" OR "irrigation activation")
```
세분 예: `endo-single-multi`(single-visit vs multi-visit), `endo-glidepath`, `endo-EAL`(electronic apex locator accuracy).

### perio
```
(periodontitis OR "scaling and root planing" OR "keratinized mucosa" OR "soft tissue augmentation")
```

### prostho
```
(zirconia OR "immediate dentin sealing" OR "resin cement" OR "vertical dimension of occlusion")
```

### pharma
```
(NSAID OR antibiotic prophylaxis OR antithrombotic OR "local anesthetic") AND (dentistry OR dental OR oral surgery)
```
약리 토픽은 치과 한정어(dentistry/dental/oral)를 AND로 묶지 않으면 의과 문헌이 범람한다.

### oral-medicine
```
("burning mouth syndrome" OR "oral lichen planus" OR halitosis OR "topical anesthesia")
```

### cracked-tooth
```
("cracked tooth"[tiab] OR "cracked teeth"[tiab] OR "cracked tooth syndrome"[tiab] OR "incomplete tooth fracture"[tiab] OR "incomplete crown fracture"[tiab] OR "tooth crack"[tiab] OR "cuspal fracture"[tiab])
```
niche 토픽 — RCT/SR/MA 전 기간 누계 ~17건뿐. `[tiab]` phrase 필수("tooth fracture" 단독은 root fracture·외상까지 범람). `"vertical root fracture"`는 별개 entity라 제외. ptyp는 RCT/SR/MA로 좁혀도 연 수건 수준이라 noise 적음. 시드 sweep(2026/06/19): SR+MA 3 + RCT 1 적립. **철회 1건(PMID 38517822, Technol Health Care SR)** 은 screened-seen 처리해 영구 제외.

### c-shaped-canal
```
("C-shaped canal"[tiab] OR "C-shaped canals"[tiab] OR "C-shaped root canal"[tiab] OR "C-shaped root canals"[tiab] OR "C-shaped configuration"[tiab] OR "C-shaped root canal system"[tiab])
```
C자형 근관(주로 하악 제2대구치) 해부·치료. niche — RCT/SR/MA 전 기간 7건뿐, 대부분 CBCT 유병률·in vitro라 high-evidence 적음. wiki/endodontics/anatomy에 C-shaped 페이지 다수 기보유 → **DOI 교차 dedup 필수**(seen만으로 부족; 시드 sweep에서 yousefi-2025 PMID 41126141이 이미 위키 보유로 제외됨). 시드 sweep(2026/06/19): 신규 2건(40410308 Sci Rep MA OA:PMC, 41042605 Indian JDR SR+MA) 적립, 5건 screened-seen(기보유 1 + 노후/tangential 4).

### clear-aligner
```
("clear aligner"[tiab] OR "clear aligners"[tiab] OR "aligner therapy"[tiab] OR "Invisalign"[tiab] OR "thermoplastic aligner"[tiab] OR "orthodontic aligners"[tiab])
```
투명교정. 활발한 분야 — RCT/SR/MA 전 기간 ~140건. BMC Oral Health·Prog Orthod·PLoS One·Sci Rep 계열이 PMC OA라 ingest 용이. wiki orthodontics 카테고리는 TAD/biology 중심이라 aligner 임상은 신규 축. 시드 sweep(2026/06/20): 7건 적립, fonseca-planells-2026(상악확장 SR+MA, growing) ingest. category는 `orthodontics`.

### pediatric-dentistry
```
("primary teeth"[tiab] OR "primary molar"[tiab] OR "primary molars"[tiab] OR "deciduous teeth"[tiab] OR pulpotomy[tiab] OR "Hall technique"[tiab] OR "stainless steel crown"[tiab] OR "paediatric dentistry"[tiab] OR "pediatric dentistry"[tiab])
```
소아치과 — 매우 광범위(RCT/SR/MA 전 기간 ~1570건). 핵심 임상어(유치·pulpotomy·Hall·SSC)로 좁혀도 물량 많음 → 최신순 triage 후 OA·고가치만 ingest. 의과 소아 범람 방지 위해 치과어 phrase 사용. ingest는 material/category에 맞춰 분산(예: HVGIC RCT→glass-ionomer, pulpotomy→endodontics/vpt, MIH→caries). 시드 sweep(2026/06/20): 7건 적립, ali-eldin-2026(giomer vs HVGIC 유구치 RCT)→glass-ionomer ingest. 하위 세분 토픽: `primary-pulpotomy-ssc`.

### primary-pulpotomy-ssc
```
(pulpotomy[tiab] OR "stainless steel crown"[tiab] OR "stainless steel crowns"[tiab] OR "preformed metal crown"[tiab] OR "preformed metal crowns"[tiab] OR "Hall technique"[tiab] OR "preformed crown"[tiab] OR "preformed crowns"[tiab]) AND ("primary tooth"[tiab] OR "primary teeth"[tiab] OR "primary molar"[tiab] OR "primary molars"[tiab] OR deciduous[tiab] OR "primary dentition"[tiab] OR pediatric[tiab] OR paediatric[tiab])
```
pediatric-dentistry의 세분 — 유치 펄포토미 + SSC/Hall technique. RCT/SR/MA 전 기간 ~302건(활발). ingest 분산: Hall/SSC→`caries`, pulpotomy→`endodontics/vpt`. 시드 sweep(2026/06/20): 7건 적립, konukman-turker-2026(Hall vs modified HT RCT, OA:PMC)→caries · chawla-2026(펄포토미 vs 펄펙토미 SR+MA, abstract-only)→endodontics/vpt ingest. 1건 screened-seen(41317129 neuromodulation MIH 마취, 토픽 외).

### plaque (치과 플라그 / dental biofilm)
```
("dental plaque"[tiab] OR "dental biofilm"[tiab] OR "supragingival plaque"[tiab] OR "plaque control"[tiab] OR "plaque index"[tiab])
```
플라그 핵심어는 `[tiab]` phrase로 묶는다 — 안 묶으면 "biofilm" 단독이 미생물학·산업 표면 문헌까지 끌어온다.
ingest 라우팅: 바이오필름 생태·매트릭스 기전 → `oral-microbiology`, 플라그 control RCT(칫솔·구강세정제) → `periodontics`/위생, 식이·우식 연계 → `caries`.

### toothpick-method (이쑤시개법 / Watanabe method)
```
("toothpick method"[tiab] OR "Watanabe method"[tiab] OR "toothpick technique"[tiab]) AND (toothbrush*[tiab] OR toothbrushing[tiab] OR plaque[tiab] OR gingiv*[tiab] OR periodont*[tiab] OR "oral hygiene"[tiab] OR dental[tiab] OR "peri-implant"[tiab])
```
**ptyp 비움 필수** — 초niche(전체 7편)라 RCT/SR/MA로 좁히면 거의 다 빠진다.
**치과 앵커(AND절) 필수** — `"toothpick method"` 단독은 식물병리(균접종법)·화학(Watanabe transference)·바닐라 수분 등 비치과 문헌이 압도(원쿼리 39편 중 절반 이상 노이즈). 앵커 추가 시 7편으로 정제됨.
ingest 라우팅: 칫솔질법 효능 SR/RCT → `periodontics`, peri-implant mucositis 적용 → `implants/peri-implantitis`.

### floss-interdental (치실 · 치간칫솔 · 구강세정기)
```
("dental floss"[tiab] OR flossing[tiab] OR "interdental brush"[tiab] OR "interdental brushes"[tiab] OR "interproximal brush"[tiab] OR "interdental cleaning"[tiab] OR "interdental aids"[tiab] OR "oral irrigator"[tiab] OR "water flosser"[tiab])
```
**노이즈 주의** — `flossing`/`floss` 단독은 스포츠·물리치료의 **"tissue flossing"(압박밴드 ROM 기법)** 문헌을 다수 끌어온다(발목 ROM·요통 RCT 등). ptyp(RCT/SR/MA)로도 안 걸러지므로 abstract 단계에서 dental 여부 확인 필수.
ingest 라우팅: 치실/치간칫솔/구강세정기 효능 RCT·SR → `periodontics`, 교정환자 위생 한정 시 `orthodontics` 고려, 식편압입 맥락 → `food-impaction`.

### water-flosser (워터픽 · 구강세정기 · dental water jet)
```
("oral irrigator"[tiab] OR "oral irrigators"[tiab] OR "oral irrigation"[tiab] OR "water flosser"[tiab] OR "water flossing"[tiab] OR "water jet"[tiab] OR "dental water jet"[tiab] OR Waterpik[tiab] OR "powered irrigation"[tiab]) AND (toothbrush*[tiab] OR plaque[tiab] OR gingiv*[tiab] OR periodont*[tiab] OR interdental[tiab] OR "oral hygiene"[tiab] OR "peri-implant"[tiab] OR orthodontic[tiab])
```
`floss-interdental`의 워터픽 특화 분기. **치과 앵커(AND절) 필수** — `"oral irrigation"` 단독은 비강·창상 세척 등 비치과 문헌을 끌어온다. 교정환자 oral-irrigator RCT/SR이 다수라 중복 ingest 주의(이미 yiamwattana-2025 SR+MA 보유) — 새 각(치주염 보조·임플란트·WF vs 치간칫솔)만 선별.

### implant-primary-stability (초기고정력 / ITV / ISQ · RFA)

**목적**: 임플란트 초기고정력(Primary Stability)·식립토크(Insertion Torque Value, ITV)·ISQ·RFA에 영향을 미치는 변수들을 추적. 기존 `implant` 토픽보다 더 좁은 stability-specific 감시.

```
("insertion torque"[tiab] OR "primary stability"[tiab] OR "initial stability"[tiab] OR "insertion torque value"[tiab] OR ISQ[tiab] OR "resonance frequency"[tiab]) AND ("dental implant"[tiab] OR implant[tiab] OR osseointegration[tiab])
```

**노이즈 주의**:
- `ISQ` 단독은 비치과 두문자어와 겹칠 수 있음 — `AND (dental implant[tiab] OR implant[tiab])` 앵커 필수.
- `"resonance frequency"` 단독은 물리/공학 문헌 다수 → AND 앵커로 차단됨.

**ptyp**: RCT + SR + MA (volume 적당, 연 30~60건 예상).

**주요 변수 축** (ingest 우선순위 판단 기준):
1. 골밀도·골질(HU, D1~D4) × ITV / ISQ
2. 임플란트 매크로 디자인(tapered vs cylindrical, thread depth/pitch/angle) × ITV / ISQ
3. 오스테오토미 프로토콜(sequential / osseodensification / undersized) × ITV / ISQ
4. 부위(상악 vs 하악, 전치 vs 구치, 즉시식립 vs 지연) × ITV / ISQ
5. ITV ↔ ISQ 상관성·해리(ITV 높다고 ISQ 반드시 높지 않음 — 근거 축적 필요)
6. ITV / ISQ 임계값 × 부하 결정

**라우팅**: `wiki/implants/isq/` + 오버뷰 `implants-isq-stability-ladder` · `isq-loading-threshold`.

### antibiotic-dental (치과 항생제 · 항균 치료)

```
(amoxicillin[tiab] OR clindamycin[tiab] OR metronidazole[tiab] OR azithromycin[tiab] OR doxycycline[tiab] OR "antibiotic prophylaxis"[tiab] OR "antibiotic stewardship"[tiab] OR "antimicrobial resistance"[tiab] OR "antibiotic prescribing"[tiab] OR "antibiotic therapy"[tiab]) AND (dental[tiab] OR dentistry[tiab] OR odontogenic[tiab] OR "oral infection"[tiab] OR "tooth extraction"[tiab] OR endodontic[tiab] OR periodontal[tiab] OR "implant surgery"[tiab])
```

**목적**: 치과 항생제 전반 — 예방적 항생제 (Antibiotic Prophylaxis), 치성감염 치료, 항생제 내성 (Antimicrobial Resistance), 처방 패턴·스튜어드십 (Antibiotic Stewardship), 개별 약물(아목시실린·클린다마이신·메트로니다졸·아지스로마이신·독시사이클린) 효능·부작용.

**노이즈 주의**:
- `antibiotic prophylaxis` 단독은 심혈관·정형외과 예방 문헌 대거 포함 → `AND dental` 앵커 필수.
- `antimicrobial resistance` 단독은 비치과 감염내과 문헌 압도 → 앵커 유지.
- `metronidazole` 단독은 소화기·부인과도 포함 → AND 앵커로 차단.

**ptyp**: RCT + SR + MA. volume 중간(연 50–100건 예상).

**주요 변수 축** (ingest 우선순위):
1. 예방적 항생제 필요성 논쟁 — 심장판막·인공관절 환자 치과 시술 전 항생제 권고/근거
2. 치성감염(Odontogenic Infection) 항생제 선택 — amoxicillin vs clindamycin vs amoxicillin+clavulanate
3. 임플란트 수술 전후 항생제 — 생존율·합병증 영향 (SR+MA)
4. 발치 후 항생제 — 예방 효과 vs 내성 위험 trade-off
5. 항생제 스튜어드십 / 처방 패턴 — 치과의사 처방 습관·부적절 처방률
6. 항생제 알러지 교차반응 — 페니실린 알러지 환자 대안 약물
7. 메트로니다졸 병용 — 페리오·근관 감염 병용요법 근거
8. 항생제 내성 — 구강 내 내성균 실태, 처방 연계

**라우팅**: `drug/` (항생제 임상) + `implants/peri-implantitis` (임플란트 주위염 항생제) + `periodontics` (치주 항생제 보조요법) + `endodontics` (근관 항생제) + 오버뷰 `antibiotic-dental-decision-ladder` (신설 가능).

### insadol-egatan (인사돌 · 이가탄)

```
(Insadol[tiab] OR ("Magnoliae cortex"[tiab] AND "Zea mays"[tiab]) OR (carbazochrome[tiab] AND (dental[tiab] OR periodontal[tiab] OR gingival[tiab])))
```

**목적**: 인사돌(Magnoliae cortex + Zea mays L. 추출물)과 이가탄(carbazochrome + lysozyme + vitamin C + E 복합제)에 관한 임상·기초 문헌 추적.

**ptyp 비움** — 전체 문헌이 ~15편 수준의 초niche 토픽. RCT/SR/MA로 좁히면 사실상 검색 결과 없음.

**현황 (2026-06-19 기준)**: PubMed 전수 12편 — 모두 seen_pmids 등록 완료.
- 인사돌 현대 근거: `kim-2024` (개 동물), `kim-2018` (RAW264.7 in vitro), `hong-2019` (이가탄 RCT, n=93)
- `choi-2015` (인사돌 통계 유효성 비판)
- 나머지 8편 (1967–1991, 폴란드·헝가리·독일·프랑스어, 초록 없음) — 인제스트 가치 없음

**주요 성분 대응**:
- 인사돌: Magnoliae Cortex 추출물 + Zea mays L. 추출물 → NF-κB 억제, 항염
- 이가탄: carbazochrome 10mg + tocopherol acetate 10mg + ascorbic acid 80mg + lysozyme 60mg

**라우팅**: `drug/` (임상 효능 RCT), `periodontics/` (치주 보조요법), `evidence-appraisal/` (통계 방법론 비판).

---

### pdrn (폴리뉴클레오티드 / PDRN 치과 적용)

```
(PDRN[tiab] OR polydeoxyribonucleotide[tiab] OR "poly deoxyribonucleotide"[tiab] OR "polynucleotide"[tiab]) AND (dental[tiab] OR dentistry[tiab] OR implant[tiab] OR periodontal[tiab] OR endodontic[tiab] OR oral[tiab] OR osseointegration[tiab] OR "bone regeneration"[tiab] OR osteoblast[tiab] OR osteoclast[tiab] OR TMJ[tiab] OR "temporomandibular"[tiab])
```

**목적**: 치과 영역 PDRN — 골 재생(GBR·발치와·상악동), 연조직 증대, TMJ 주사 치료(prolotherapy), MRONJ 세포보호, 임플란트 골유착, in vitro 기전 연구.

**노이즈 주의**: `polynucleotide` 단독은 분자생물학·비치과 주사 미용 문헌 대거 포함. `PDRN` 단독은 비교적 깨끗하나 AND 치과 앵커 필수.

**ptyp**: RCT + SR + MA (현 volume 연 20~40건 예상 — 아직 소량 토픽).

**주요 변수 축**:
1. 골 재생 — GBR·ARP·상악동 내 PDRN soaking/주사 효과 (BIC·new bone area)
2. 연조직 — KT 증대·연조직 볼륨(SCT 대비)
3. TMJ prolotherapy — PDRN vs dextrose 통증·MMO
4. MRONJ 세포보호 기전 (TBK1·PKB·ROS 경로)
5. in vitro 기전 — 오스테오블라스트/오스테오클라스트 선택적 효과 (A2A 수용체)
6. 발치 후 통증 관리 (human RCT)

**라우팅**: `pdrn/` + 오버뷰 `pdrn-dentistry-evidence-synthesis`.

**현황 (2026-06-19)**: 17편 보유. 2026-06 신규: jeon-2026 (in vitro 기전 — 오스테오블라스트 선택적 활성화, 오스테오클라스트 무영향).

---

### botulinum-toxin (보툴리눔 독소 / BTX 치과 적용)

```
("botulinum toxin"[tiab] OR "botulinum toxin type A"[tiab] OR BoNT-A[tiab] OR BTX-A[tiab] OR onabotulinumtoxinA[tiab] OR incobotulinumtoxinA[tiab] OR abobotulinumtoxinA[tiab] OR Botox[tiab] OR Xeomin[tiab] OR Dysport[tiab]) AND (dental[tiab] OR dentistry[tiab] OR bruxism[tiab] OR masseter[tiab] OR temporalis[tiab] OR TMD[tiab] OR "temporomandibular"[tiab] OR "gummy smile"[tiab] OR orofacial[tiab] OR "myofascial pain"[tiab])
```

**목적**: 치과 BoNT-A — TMD/근육성 통증, 수면 브럭시즘, 교근 비대·심미, gummy smile, 임플란트 골유착 영향.

**노이즈 주의**: `Botox` 단독은 피부과·성형외과 미용 문헌 압도. `bruxism` + `masseter` 앵커로 치과 한정 가능하나 완벽하지 않음 — abstract 단계에서 치과 맥락 확인 필수.

**ptyp**: RCT + SR + MA (volume 중간; 연 50~100건 예상 — ptyp 없이 하면 범람).

**주요 변수 축**:
1. TMD/근육성 통증 — BoNT-A vs 위약·스플린트·물리치료 효능 비교
2. 수면브럭시즘 — EMG·교합력·통증·수면질(PSQI) 개선
3. 저작근 형태 변화 — 두께 감소·탄성 회복 타임라인 (초음파 elastography)
4. 하악골 형태 — 피질골 두께·하악각 방사선학적 변화
5. gummy smile / lip aesthetics — 주사 부위·용량·지속 기간
6. 임플란트 골유착에 대한 BoNT-A 근마비 영향 (동물 연구)
7. 제제 비교 — Botox(ona) vs Xeomin(inco) vs Dysport(abo)

**라우팅**: `botulinum-toxin/` (주 카테고리) + `tmj/` (TMD 중첩) + `implants/` (골유착 영향).

**현황 (2026-06-19)**: 26편 보유. 2026-06 신규: angelo-2026(Xeomin TMD), abdulrahman-2026(2yr VAS), eberlikose-2026(골 형태), hira-2026(수면질), aldosari-2026(SR+MA 스플린트vs보톡스), yan-2025(USE elastography), ergezen-2025(수면브럭시즘 수면질).

---

### toothpaste (투쓰페이스트 / dentifrice)
```
(toothpaste[tiab] OR dentifrice[tiab] OR dentifrices[tiab])
```
**초고volume**(RCT/SR/MA만 1700+편) — sweep는 newest-first로 받아 **하위 테마별 1~2편**만 선별. 주요 축: 불소/항우식(고불소·아르기닌·NaF), 지각과민(SnF₂·바이오글라스·NovaMin·아르기닌), 항침식(stannous), 미백(blue covarine·과산화물), 치석(SnF₂+zinc), 천연/허브, 의치세정. DH(지각과민) RCT가 특히 많아 중복 주의. 라우팅: 항우식→`caries`, 지각과민→`dentin-hypersensitivity`, 침식→`dental-erosion`, 미백/연마→`dental-materials`.

---

### implant-submerged-fixture (매몰식 vs 비매몰식 식립 / fixture 프로토콜)

```
("submerged implant"[tiab] OR "submerged implants"[tiab] OR "non-submerged"[tiab] OR "nonsubmerged"[tiab] OR "submerged healing"[tiab] OR "submerged placement"[tiab] OR "submerged technique"[tiab] OR "submerged approach"[tiab]) AND ("dental implant"[tiab] OR "dental implants"[tiab] OR "oral implant"[tiab] OR "oral implants"[tiab] OR "implant fixture"[tiab] OR "implant fixtures"[tiab] OR osseointegration[tiab])
```

**목적**: fixture 매몰 여부(submerged vs non-submerged healing, 2차 수술 유무)가 생존율·크레스탈 골소실·연조직 치유에 미치는 영향. `implant` 상위 토픽과 `implant-primary-stability` 사이의 중간 해상도 축.

**노이즈 실측 (2026-10-04 시드 sweep)**:
- 코어 쿼리(위 문장 그대로) = **411편** 전 기간, `+RCT/SR/MA` = **57편** → ptyp 켜면 triage 물량이manageable.
- 6쿼리 합집합 스윕(761 unique PMID, 쿼리별 retmax 200 상한)에서 **대량 노이즈는 3군데에 집중**: ① 2-piece zirconia 임플란트 시트(zirconia는 통상 `submerged`(피복)·`two-piece`와 짝지어 서술됨) ② whole-arch / full-arch fixed prosthesis 리뷰 ③ peri-implantitis 치료·.Diagnostics. 셋 다 `[tiab]` 앵커로 걸러지지 않으므로 **abstract 단계에서 dental fixture 프로토콜 비교인지부터 확인**할 것.
- **ptyp를 비우면 411편 전체가 살아난다** — Brånemark 원형 2단계 코호트, Albrektsson 원격 교부 등 **고전 submerged 1차 논문**이 여기 실려 있다. 매몰식 프로토콜의 원론을 다시 잡아야 할 때는 ptyp 빈 토픽을 임시로 쓴 뒤 되돌릴 것.

**주요 변수 축** (ingest 우선순위):
1. 매몰식 vs 비매몰식 × **생존율** 및 조기실패(early failure) / 만기실패(late failure) 분리
2. 매몰식 vs 비매몰식 × **크레스탈 골소실(MBL)** — 이 축이 논문 간 불일치 최대 지점(§tension 참조)
3. 연결형태(internal hexagonal / conical / tapered)가 매몰식 효과에 미치는 **교차축**(두 토픽의 접합점)
4. 매몰식 vs 비매몰식 × 연조직 치유·점막염·미용적 결과
5. 2차 수술(second-stage surgery) 시점·방식(closed/open, flap vs flapless)

**라우팅**: 실패·생존율 → `implants/survival`, 골소실 → `implants/mbl`, 프로토콜·임상성능 → `implants`. 선행 근거: `kim-2022-abutment-connection-mbl-survival`(연결형태→MBL)이 `implants/mbl`에 있음.

**현황 (2026-10-04)**: ingest 4편 — `moustafa-ali-2018`(SR+MA), `troiano-2018`(SR+MA+TSA, `implants/survival`), `al-amri-2016`(SR, `implants/mbl`), `wu-2018`(5년 회고적, internal hexagonal).

**tension (파일에 이미 기록)**: MBL 축에서 세 편이 서로 어긋난다 — Moustafa Ali는 submerged에서 **유의한 증가**(MD 0.12 mm), Al Amri는 **무차이**, Troiano은 **비매몰형이 유리**(0.13 mm). 조기실패는 Troiano만 비매몰형에 +2% 페널티. 단일 "정답"을 내지 말고 축별로 쪼개 참조할 것.

---

### implant-internal-connection (내부형 연결 / internal connection · conical · hex · tapered)

```
("internal connection"[tiab] OR "internal connections"[tiab] OR "internal hex"[tiab] OR "internal hexagon"[tiab] OR "internal hexagonal"[tiab] OR "internal tapered"[tiab] OR "internal torque"[tiab] OR "internal screw"[tiab]) AND ("dental implant"[tiab] OR "dental implants"[tiab] OR "implant abutment"[tiab] OR "implant abutments"[tiab] OR "implant fixture"[tiab] OR "dental implant-abutment"[tiab])
```

**목적**: fixture–abutment **연결 설계**(internal conical vs internal tapered vs internal hexagonal vs non-tapered vs external hex)의 임상·방사사·기계적 결과. `implant-submerged-fixture`의 형제축이며, 두 토픽의 교차점(내부 hex 임플란트에 매몰식 vs 비매몰식 비교)이 `wu-2018`로 이미 기보유.

**노이즈 실측 (2026-10-04 시드 sweep)**:
- 코어 쿼리 = **457편** 전 기간, `+RCT/SR/MA` = **44편**.
- `internal connection`은 fixture 종류에 구애되지 않고 **수술 가이드·유인치·부하요법· abutment 색인 문헌**까지 모인다 — 반드시 `dental implant OR implant abutment OR implant fixture` 앵커를 유지할 것(앵커 제거 시 치과 외 문헌이 압도).
- `internal torque`·`internal screw`는 대개 **기계적 micromotion·유격 시험(in vitro)**이라 clinical evidence tier가 낮다. `design[tiab]` 결합으로 clinical-only 축을 더 좁힐 수도 있음.
- **ptyp 비우면 고전 코호트가 열린다** — 수정체 원판 스크류 유지형 코호트, 구형 internal hex 설계의 5~10년 생존 코호트가 여기 실려 있다.

**주요 변수 축** (ingest 우선순위):
1. internal conical vs **non-conical**(내부 평측 / butt-joint) — MBL·생존율
2. internal **tapered** vs internal **nontapered** — 미세변위·Retainer loosening·MBL
3. internal **hexagonal**(모서리 유닛 수) vs internal **conical** — 콜스탈 크림프, AOF 증가 여부
4. 연결형태 × 매몰식/비매몰식(2차 수술 존재가 미seal을 바꾸므로)
5. 연결형태 × **점막염·연조직 seal** 및 생물학적 실패
6. one-piece(연결 자체가 없음) vs two-piece(내부 연결) — `liu-2021`↔`pirc-2026`이 이 축에서 서로 반대 결론

**라우팅**: MBL·치주 기준 → `implants/mbl`, 연결 생존·실패 → `implants/survival`, 설계 비교·임상성능 → `implants`.

**현황 (2026-10-04)**: ingest 4편 — `rodrigues-2023`(SR+MA), `yu-2020`(SR+MA), `walter-2022`(RCT, PMC 전문 — 두 2-piece 시스템 8년 추적), `liu-2021`(SR+MA, one-piece vs two-piece). 큐 잔여 3편: `34830709`(PMID, J Clin Med RCT pilot, PMC8621760), `36382704`(structured review), `37654392`(PMID, PMC10466507, one- vs two-piece).

**주의**: `walter-2022` 출판사 초록은 분모 오타(6/24, 12/25)가 있고 본문(PMC9303227)은 35.7% vs 16.7% 임플란트 레벨 기술적 합병증을 보고 — 분모를 인용할 때 항상 PMC 전문 값 사용.

---

### all-on-x (All-on-4/6/X · full-arch 임플란트 고정성 보철)

```
(("all-on-four"[tiab] OR "all on four"[tiab] OR "allonfour"[tiab] OR "all-on-4"[tiab] OR "all on 4"[tiab] OR "allon4"[tiab] OR "all-on-six"[tiab] OR "all-on-6"[tiab] OR "allon six"[tiab] OR "all-on-x"[tiab] OR "allonx"[tiab]) OR (("full-arch"[tiab] OR "full arch"[tiab] OR "full-mouth"[tiab] OR "full mouth"[tiab]) AND implant*[tiab]))
```

**목적**: 무치악 고정성 풀아치 임플란트 보철(all-on-four/six, 경사 임플란트, 전악 즉시부하)의 RCT·SR·MA 추적. 기존 `implant` 상위 토픽에서 "full-arch/prosthesis 문헌이 노이즈"로 걸러져 왔던 축을 전용 토픽으로 승격 — `wiki/implants/full-arch/` 폴더 및 `full-arch-fixed-four-vs-six-implants-overview`와 1:1 대응.

**노이즈 실측 (2026-10-07 시드 sweep)**:
- 전 기간 `+RCT/SR/MA` = **159편** (코어 all-on-4/6/x 구문 19 + full-arch×implant 122 + full-mouth×implant 27, 합집합). full-arch×implant 문헌이 대다수 — orthodontic mini-implant "full arch" 문헌·full-arch fixed prosthesis(치아지지) 리뷰 등이 섞이므로 **abstract 단계 topical 확인 필수**.
- `"all-on-x"[tiab]` phrase는 PubMed에서 0건 — 하이픈/숫자 변형(all-on-four/4/6·allonfour 등)을 나열해야 잡힌다.
- ptyp를 RCT/SR/MA로 고정해야 물량이 manageable. 생존 코호트(Caramés 943명, La Monaca 등)는 COHORT를 별도로 켜야 열린다 — 필요 시 ptyp 임시 변경.

**주요 변수 축** (ingest 우선순위):
1. all-on-4 vs all-on-6 vs all-on-x — 생존율·합병증·MBL (overview `full-arch-fixed-four-vs-six-implants-overview`의 임상 축 보강)
2. 경사 원위 임플란트(tilted) vs 축방향 — MBL·응력·생존 (szabo-2022 기보유)
3. 즉시부하 vs 조기/지연부하 × full-arch
4. 제로 캔틸레버·개수 최소화(4개 vs 5~6개) 전략·2026 컨센서스 갱신
5. full-arch 재건 생체역학(FEA·프레임워크 재료) — 단, in-vitro는 낮은 근거등급

**라우팅**: 생존·실패 → `implants/full-arch/`, 개수 결정 → `full-arch-fixed-four-vs-six-implants-overview`, FEA/생체역학 → `implants/full-arch/`(in-vitro 태깅), 보철 설계 → `implants/prosthodontics`.

**현황 (2026-10-07 시드 sweep + 코호트 sweep + 1·2차 ingest 완료)**: 
- **시드 sweep (RCT/SR/MA)**: 159편 검색 → dedup(seen 5·screened 1 제외, 153) → DOI 교차로 기보유 9편 제외 → 144편 topical 스크리닝(분대 4개 병렬) → **include 80** (OA:PMC 13) 큐 적립 + **exclude 64** screened-out(유지관리·점막염 중재·일반 임플란트 SR 등, `restore-screened`로 복구 가능).
- **코호트 sweep (2023~ Cohort, 2026-10-07)**: 120편 검색 → 20편 상세 확인 → **include 18** (OA:PMC 6: 42397653, 41839752, 42129020, 41826858, 41482737, 42668365) 큐 적립 + **exclude 2** screened-out(peri-implantitis 치료·case report).
- **1차 ingest 완료 (시드 sweep OA:PMC 13편)**: pellicer-chover-2013, cappare-2019, gracher-2021, fernandez-ruiz-2021, cattoni-2021, gaonkar-2021, rossi-2021, pera-2021, storelli-2021, bagnasco-2024, pozzi-2025, emam-2025, aboelez-2026 → `wiki/implants/full-arch/` + `sources/` 생성, qmd embed 완료.
- **2차 ingest 완료 (코호트 sweep OA:PMC 6편)**: kernen-gintaute-2026, uesugi-2026, alshahrani-2026, pelser-2026, fan-2026, acar-2026 → `wiki/implants/full-arch/` + `sources/` + index.md + git push + qmd update 완료, **qmd embed 백그라운드 진행 중**.
- **큐 현황**: all-on-x 총 92편 대기 (OA:PMC 13, OA:none 79). 잔여 PDF 확보(Unpaywall·저자 요청·RISS 등) 후 3차 ingest 예정.
- 기보유 all-on-x 관련 페이지: murat-2025, la-monaca-2022, pandey-2023, szabo-2022, uesugi-2024, baki-2025, cabbarova-2026, yaghmai-2025 등 (`index.md` 참조).
