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

### toothpaste (투쓰페이스트 / dentifrice)
```
(toothpaste[tiab] OR dentifrice[tiab] OR dentifrices[tiab])
```
**초고volume**(RCT/SR/MA만 1700+편) — sweep는 newest-first로 받아 **하위 테마별 1~2편**만 선별. 주요 축: 불소/항우식(고불소·아르기닌·NaF), 지각과민(SnF₂·바이오글라스·NovaMin·아르기닌), 항침식(stannous), 미백(blue covarine·과산화물), 치석(SnF₂+zinc), 천연/허브, 의치세정. DH(지각과민) RCT가 특히 많아 중복 주의. 라우팅: 항우식→`caries`, 지각과민→`dentin-hypersensitivity`, 침식→`dental-erosion`, 미백/연마→`dental-materials`.
