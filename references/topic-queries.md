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
