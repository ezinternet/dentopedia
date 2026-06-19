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
