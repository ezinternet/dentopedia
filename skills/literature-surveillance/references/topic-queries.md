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
