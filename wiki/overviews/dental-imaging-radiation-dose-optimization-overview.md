---
title: "Dental Imaging Radiation Dose Optimization — Modality Hierarchy, Optimization Levers, and the Shielding/MRI Paradigm Shift"
authors: synthesis (llm-wiki)
year: 2026
date: 2026-06-05
type: overview
category: [overviews]
tags: [radiology, radiation-dose, dose-optimization, CBCT, panoramic, effective-dose, ALADAIP, ALARA, paediatric, collimation, FOV, voxel, kVp, mAs, Monte-Carlo, OSLD, TLD, diagnostic-reference-level, DRL, thyroid-shielding, low-field-MRI, focal-trough, ghost-image, dosimetry, occupational-dose, operator-safety, handheld-xray, justification, lead-apron, scatter, background-radiation, orthodontic]
source_papers:
  - radiology/lee-2021-dental-imaging-doses-web-dose-calculator
  - radiology/fontenele-2025-cbct-dentistry-clinical-recommendations-indication
  - radiology/jacobs-2018-cbct-implant-dentistry-recommendations-clinical
  - radiology/kaasalainen-2021-dental-cone-beam-ct-updated-review
  - radiology/benavides-2023-patient-shielding-dentomaxillofacial-radiography
  - radiology/oenning-2019-halve-dose-paediatric-cone-beam-ct
  - radiology/hidalgo-rivas-2015-low-dose-cbct-anterior-maxilla-children
  - radiology/charuakkra-2023-low-dose-cbct-image-dose-comparison
  - radiology/ozaki-2021-cbct-effective-dose-monte-carlo-simulation
  - radiology/lee-2019-cbct-dose-osl-monte-carlo-comparison
  - radiology/benchimol-2018-collimation-panoramic-effective-dose-reduction
  - radiology/lee-2019-monte-carlo-paediatric-panoramic-dose-reduction
  - radiology/schindler-2025-panoramic-thyroid-eye-lens-dose
  - radiology/willershausen-2025-low-field-mri-pediatric-dental
  - radiology/khafaji-2023-scattered-dose-eye-dentistry-cbct
  - radiology/kang-2024-national-dental-radiological-dose-management
  - radiology/lee-2024-dental-dose-monitoring-system-establishment
  - radiology/baena-2022-cbct-diagnostic-performance-root-resorption
  - radiology/ludlow-2008-patient-risk-dental-radiographic-examinations
  - radiology/johnson-2020-intraoral-radiograph-dose-collimation-thyroid-shielding
  - radiology/hedesiu-2018-dental-radiological-irradiation-pediatric-population
  - radiology/stervik-2024-radiation-exposure-during-orthodontic-treatment
  - radiology/berkhout-2015-justification-and-good-practice-using
  - radiology/gijbels-2005-dosimetry-digital-panoramic-occupational-exposure
  - radiology/kim-2016-occupational-radiation-procedures-doses-korean-dentists
  - radiology/kabier-2025-xray-radiation-exposure-open-dental-clinics-tld
  - radiology/rottke-2018-operator-safety-during-the-acquisition
confidence: synthesis
source: synthesis
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 핵심 명제: 치과 영상 선량은 상류의 modality 선택에서 대부분 결정되고, 그다음 술자가 조절 가능한 4개 레버로 미세조정된다. ALARA/ALADAIP 실행 = "더 낮은 modality를 고를 수 있는가 → 못 고르면 레버를 조인다" 2단 의사결정.
> - Modality 위계(고정): 구내(intraoral) ~1.32 µSv ≪ 파노라마(panoramic) ~17.93 µSv ≪ CBCT ~121.09 µSv. 즉 CBCT를 파노라마로, 대형 FOV를 소형으로 내리는 것이 단일 최대 선량 절감.
> - 'CBCT'라는 단일 라벨은 선량을 말해주지 않음 — 기기간 유효선량이 파노라마 2~200장 등가로 벌어진다(Jacobs 2018), 87기종 조사에서 3~500 µSv(Fontenele 2025).
> - 레버 A — FOV/Collimation(가장 큰 임상 레버): 파노라마 collimation으로 진단정보 손실 없이 저감(Benchimol 2018). 단 소형 FOV 6회 잇기 = 대형 1회의 약 1.2배(Ozaki 2021) — '작게 여러 번'이 항상 방호적이지 않다.
> - 레버 B — kVp/mAs: 고관전압(high-kVp) ULD/LD 프로토콜이 화질저하 없이 선량 ~6배↓(Charuakkra 2023).
> - 레버 C — 복셀 크기(직관 반대): 70 kVp·16 mAs·180 µm(작은 복셀) 조합이 소아 CBCT 선량 ~45%↓ + 화질 유지. 노출은 낮추되 복셀은 키우지 말 것(Oenning 2019).
> - 레버 D — 파노라마 빔높이(소아 특이): 7개 인자 중 빔높이(수직 조사야)가 선량 최대 결정인자(Lee 2019). 짧은 빔높이 = 소아 선량 저감 직접 전략.
> - 패러다임 전환 1 — 접촉 차폐 중단: 생식선·골반·태아 및 갑상선 차폐를 모든 치과 영상에서 중단 권고(Benavides 2023 AAOMR/JADA 합의). 근거 — 절대선량 매우 낮음(갑상선 0.30~1.46 µSv, Schindler 2025), 칼라가 오히려 재촬영 유발. 단 국내 규정 확인 후 적용.
> - 패러다임 전환 2 — 비전리 대안: 무피폭 0.55 T 저자장 MRI가 치축·치근·치근흡수·낭종에서 초저선량 CT와 동등 화질(Willershausen 2025). 단 PDL 공간·하악관 등 미세구조엔 미흡, ~9:45분 소요, 반복촬영 잦은 소아 매복치/교정에 미래 선택지.
> - 진단정확도-피폭 trade-off: CBCT 외흡수 진단(민감도 78%/특이도 79%, 유효선량 34~1073 µSv, Baena 2022) — modality 격상이 정당할 때만 피폭이 정당.
> - 환자선량 기준선(reference dose table): Ludlow 2008이 ICRP 2007 가중치로 전악구내방사선(Full-Mouth Series, FMS) 선량을 D-speed film+원형조준 388 µSv → PSP+직사각조준 34.9 µSv로 ~91% 저감 가능함을 정량화 — 이후 모든 치과 선량 문헌의 표준 표. Johnson 2020이 최신 직사각조준통(rectangular collimation, RC) 시스템으로 갱신(최저 54 µSv), **직사각조준이 갑상선 차폐(thyroid shield)보다 갑상선선량 저감에 더 효과적**임을 재확인해 차폐 중단 패러다임과 정합.
> - 술자/직업피폭(occupational dose) 분기: 적절히 차폐된 환경에서 술자 피폭은 무시할 수준 — 한국 치과의사 연평균 0.18 mSv(남)/0.13 mSv(여)로 직업한도(20 mSv/y)의 1% 미만(Kim 2016), 파노라마 1 m 거리 산란선 ≤0.60 µGy/촬영(Gijbels 2005), 휴대형(handheld) 장비도 제조사 지침 준수 시 술자측 산란 미검출(Rottke 2018). 단 **구조적 차폐 부재(open clinic)** 시 ~30배↑(이라크 5.6 mSv/y, Kabier 2025) — 차폐 촬영실이 핵심 변수.
> - 정당화(justification) 우선 원칙: 휴대형 구내 X-ray는 시준·재촬영 위험으로 ALARA 위반 소지 → 문서화된 정당화 하에 예외적으로만 사용(Berkhout 2015 EADMFR 합의). 소아·교정에서 누적선량 관리가 특히 중요 — 교정 전 과정(~7장) = 자연배경 5~10일분(Stervik 2024), 소아 CBCT는 촬영의 11%인데 집단선량의 70%(Hedesiu 2018) — 그러나 정당화 기록은 계획단계 촬영의 5%에 불과(Stervik 2024).
> - 근거 한계: 선량 최적화 자체에 대한 SR+MA 부재 — 레버 효과 크기는 대부분 phantom/Monte-Carlo 기반. 한국 DRL(Kang 2024) 수치는 변동 가능.

## One-line Summary

Across 27 dental-radiology papers, patient dose is governed by a fixed modality hierarchy (intraoral ~1.3 ≪ panoramic ~18 ≪ CBCT ~121 µSv) onto which four operator-controllable levers act — field-of-view/collimation, kVp/mAs, voxel size, and (panoramic) beam height — anchored by the Ludlow 2008 reference dose table; two further branches extend the frame — an OCCUPATIONAL/OPERATOR-SAFETY axis (negligible operator dose in shielded rooms — Kim 2016 0.18 mSv/y, Gijbels 2005, Rottke 2018 handheld — but ~30× higher without structural shielding, Kabier 2025) and a JUSTIFICATION + cumulative-risk axis (Berkhout 2015 handheld justification, Stervik 2024 orthodontic course ≈5–10 days background, Hedesiu 2018 pediatric CBCT = 70% of collective dose); and two paradigm shifts reframe protection: contact shielding (gonad/thyroid) is now recommended against, and radiation-free 0.55 T MRI emerges as a non-ionizing alternative for selected paediatric indications.

## 한줄요약

치과 영상 선량은 고정된 modality 위계(구내 ~1.3 ≪ 파노라마 ~18 ≪ CBCT ~121 µSv) 위에서 결정되며, 그 위에 술자가 조절 가능한 네 레버(FOV/collimation, kVp/mAs, 복셀 크기, 파노라마 빔높이)가 작용한다 — Ludlow 2008의 ICRP 2007 기준 표가 환자선량 앵커. 여기에 두 분기가 추가된다 — 직업/술자안전 축(차폐 촬영실에서 술자선량 무시 가능: Kim 2016, Gijbels 2005, Rottke 2018 휴대형; 단 구조적 차폐 없으면 ~30배↑ Kabier 2025)과 정당화·누적위험 축(Berkhout 2015 휴대형 정당화, Stervik 2024 교정 전 과정 ≈배경 5~10일, Hedesiu 2018 소아 CBCT=집단선량의 70%). 동시에 두 패러다임 전환이 방호 개념을 바꾼다 — 접촉 차폐(생식선·갑상선)는 이제 권고되지 않고, 무피폭 0.55 T MRI가 일부 소아 적응증의 비전리 대안으로 등장한다. 문헌 27편 횡단 종합. [근거강함 — modality 위계·차폐 권고], [합의수준 — 최적화 레버]

---

## Summary

이 overview는 `wiki/radiology/`의 27편을 횡단 합성한다. 근거 분포: **consensus 2편**(benavides 2023, berkhout 2015 EADMFR) · **narrative/리뷰 5편**(fontenele 2025, jacobs 2018, kaasalainen 2021, lee&badal 2021, kang 2024, lee 2024) · **SR 1편**(khafaji 2023) · **SR+MA 1편**(baena 2022) · **phantom/in-vitro·MC 9편**(oenning 2019, hidalgo-rivas 2015, charuakkra 2023, ozaki 2021, lee 2019 OSLD, benchimol 2018, lee 2019 panoramic, ludlow 2008, johnson 2020, gijbels 2005, rottke 2018) · **prospective 2편**(willershausen 2025, kabier 2025 TLD) · **retrospective 2편**(hedesiu 2018, stervik 2024) · **cross-sectional 1편**(kim 2016). 이 카테고리에는 선량 최적화 자체에 대한 SR+MA가 아직 없다 — 최강 결론도 "일관된 다수 phantom/MC + 합의 권고" 수준이다. [claude해석 — 등급 분포는 리포지토리 계측]

핵심 thesis: **선량은 modality 선택(상류)에서 대부분 결정되고, 그다음 술자가 조절 가능한 4개 레버로 미세조정된다. 따라서 ALARA/ALADAIP의 실행은 "더 낮은 modality를 고를 수 있는가 → 못 고르면 레버를 조인다" 2단 의사결정이다.**

## 1단 — Modality 위계 (상류 결정)

lee&badal (2021)의 문헌 집계가 기준선을 준다 [합의수준 — 문헌 aggregate, SR 아님]:

| Modality | 평균 유효선량 (범위) | CBCT 대비 |
|---|---|---|
| 구내 (intraoral) | 1.32 µSv (0.60–2.56) | ~1% |
| 파노라마 (panoramic) | 17.93 µSv (3.47–75.0) | ~15% |
| CBCT | 121.09 µSv (17.1–392.2) | 100% |

- jacobs (2018)는 CBCT 기기간 유효선량이 **파노라마 2~200장 등가**로 벌어진다고 보고 — "CBCT"라는 단일 라벨이 선량을 말해주지 못한다. [합의수준]
- fontenele (2025)는 87기종 조사에서 유효선량 3~500 µSv, DAP 10~5600 mGy·cm²로 같은 결론을 정량 확장. [근거강함 — 기기 실측 파라미터]
- 소아 가산: lee&badal (2021)에서 소아 CBCT가 성인 대비 약 29% 높고, 대형 FOV(>150 cm²)가 소형(<50 cm²)의 약 1.6배. [합의수준]

함의: **CBCT를 파노라마로, 대형 FOV를 소형으로 내릴 수 있으면 그것이 단일 최대 선량 절감.** baena (2022)가 보여준 진단정확도-피폭 trade-off(외흡수 민감도 78%/특이도 79%, 유효선량 34~1073 µSv)는 modality 격상을 정당화할 때만 피폭이 정당함을 상기시킨다. [근거강함 — SR+MA]

## 2단 — 술자 조절 레버 (못 내리면 조인다)

### 레버 A — FOV / Collimation (가장 큰 임상 레버)
- ludlow (2008): 이 군의 환자선량 기준선. Alderson-Rando 팬텀 + 28개 장기 TLD로 ICRP 2007 가중치 재계산 — 전악구내방사선(FMS)이 D-speed film+원형조준 388 µSv → PSP+원형 170.7 µSv → **PSP+직사각조준 34.9 µSv**로 ~91% 저감, 4매 바이트윙 5.0 µSv, 파노라마 14.2~24.3 µSv. 이후 거의 모든 치과 선량 문헌이 인용하는 표준 표 — collimation이 단일 최대 환자선량 레버임을 정량 확립. [근거강함 — phantom 표준 표]
- johnson (2020): ludlow 2008을 최신 직사각조준통(RC) 7종으로 갱신 (OSLD, 70 kVp). 최저 Focus-RC 54 µSv(성인, 원형 86 µSv 대비 37%↓), 소아 44 µSv. 핵심 — **직사각조준이 갑상선 차폐(thyroid shield)보다 갑상선선량 저감에 더 효과적**, NCRP Report 177(2019) 권고(RC = 구내촬영 표준) 검증. → 차폐보다 조사야 제한이 우선. [합의수준 — phantom OSLD]
- benchimol (2018): 풀 파노라마 17.6 µSv, collimation 프로토콜로 진단정보 손실 없이 선량 저감 → **루틴 적용 권고**. 의뢰 252건 후향분석으로 임상 적용성 확인. [합의수준 — phantom+audit]
- ozaki (2021): 소형 FOV 6회를 이어붙이면 대형 FOV 1회의 약 1.2배 선량 → "작게 여러 번"이 항상 방호적이지 않다. 정당화될 때만 다회 소형. [claude해석 — phantom MC]
- khafaji (2023): CBCT 안구 산란선량 0.103~8.3 mSv가 FOV 의존 → FOV 축소는 산란까지 함께 줄인다. [합의수준 — SR]

### 레버 B — kVp / mAs (고관전압 역설)
- charuakkra (2023): ULD/LD 프로토콜이 표준 대비 선량 ~6배↓, 화질은 '수용~양호' 유지. **고관전압(high-kVp)이 화질저하 없이 선량 저감** → 일상 진료 채택 가능. [합의수준 — phantom, 주관적 화질]

### 레버 C — 복셀 크기 (직관 반대)
- oenning (2019): 70 kVp·16 mAs·**180 µm(작은 복셀)** 조합이 화질·선예도 유지하며 소아 CBCT 선량 ~45%↓. 반대로 400 µm·7.4 mAs '초저선량'은 해부평가 부적합. → **노출을 낮추되 복셀은 키우지 말 것.** [근거강함 — phantom+검증된 MC]
- hidalgo-rivas (2015): 소아 전치부 CBCT에서 DAP ≥127 mGy·cm²·CNR ≥4.8 기준으로 제조사 권장 대비 ~50%↓ (소아 임상 CBCT 선량 최적화 선구 연구). [합의수준 — phantom]

### 레버 D — 파노라마 빔높이 (소아 특이)
- lee (2019, 파노라마 MC): 7개 인자 중 **빔높이(수직 조사야)가 선량 최대 결정인자**, 회전각·초점-환자 거리는 최소. 짧은 빔높이 = 소아 선량 저감 직접 전략. MC(3.474 µSv)가 TLD(3.850 µSv) 대체 가능. [근거강함 — 검증된 MC]

### dosimetry 방법 신뢰도 (레버를 측정하는 도구)
- lee (2019, OSLD): CBCT OSLD vs MC 유효선량 차이 4.0~14.3%, FOV 작을수록 수렴 → 공개 선량 수치 해석 시 ±10% 여유. [합의수준 — phantom]
- kaasalainen (2021): dosimetry·DRL의 의학물리 프레임. kang (2024)·lee (2024)의 한국 국가 DRL·선량 모니터링이 이 레버들의 거버넌스 층. [합의수준]

## 패러다임 전환 1 — 접촉 차폐 중단
benavides (2023, AAOMR/JADA 합의): 생식선·골반·태아 차폐 **및 갑상선 차폐를 모든 치과 영상에서 중단** 권고. 근거 — 인체 유전적 영향 부재, 생식선/태아 선량 무시 가능, 갑상선암 위험 무시 가능, 칼라가 오히려 화질저하·재촬영 유발. [합의수준 — consensus, SR 아님]

- schindler (2025)가 실측 뒷받침: 파노라마 갑상선 등가선량 0.30~1.46 µSv, 수정체 0.88~4.24 µSv (기기간 유의차 p<0.001). 절대선량이 매우 낮아 차폐 무용론과 정합. [근거강함 — phantom 실측]
- 단, 우리 클리닉 적용은 **국내 규정 확인 후** 결정 — 합의 권고가 지역 법령을 자동 대체하지 않음. [claude해석]

> [!note] Trade-off / 대안
> 차폐 중단의 반대 입장: 환자 심리적 안심·소송 방어 차원에서 갑상선 칼라 유지 주장 가능. 단 칼라가 시야를 가려 재촬영→누적선량 증가 위험이 더 크다는 게 benavides·schindler의 함의. 절충안 = 구내·파노라마는 미사용, 환자 요구 시에만 설명 후 적용.

## 패러다임 전환 2 — 비전리 대안 (MRI)
willershausen (2025, 전향적 n=16, Invest Radiol): 무피폭 **0.55 T 저자장 MRI**가 초저선량 CT(CTDI 0.43 mGy) 대비 치축·치근·치근흡수·낭종에서 동등 화질. 단 PDL 공간·하악관 등 미세구조엔 미흡, 촬영 ~9:45분, 고해상도 필요 시 CT/CBCT 여전히 필요. [근거강함 — 전향적, 단 소표본]

함의: 선량 최적화군이 "전리방사선을 얼마나 줄이나"라면, MRI는 "아예 안 쓰는" 근본 대안 — 특히 반복촬영이 잦은 소아 매복치/교정에서 미래 선택지. [claude해석]

## 분기 — 직업피폭 / 술자·조무사 안전 (Occupational dose)

위 thesis가 **환자** 선량을 다뤘다면, 같은 영상이 **술자·조무사**에게 주는 직업피폭은 별개 축이다. 핵심 메시지: **적절히 차폐된 환경에서 직업피폭은 무시할 수준이지만, 그 결론은 "구조적 차폐(structural shielding)가 있을 때"라는 단서에 전적으로 의존한다.**

- **물리 기준선** — gijbels (2005): 5종 디지털 파노라마 팬텀 실험에서 1 m 거리 산란선량 ≤0.60 µGy/촬영(환자선량 대비 3桁 낮음). 연 500회 고부하 가정 시 술자 갑상선 5~15 µSv, 생식선 5~40 µSv — 공중선량한도(1 mSv/y)에도 못 미친다. 기기간 최대 10배 차이 → 장비 선택도 직업피폭에 영향. [근거강함 — phantom]
- **실측 검증(차폐 촬영실)** — kim (2016): 한국 치과의사 658명 국가선량레지스트리 연계, 연평균 유효선량 남 0.18 mSv·여 0.13 mSv = 직업한도(20 mSv/y)의 **<1%**. 파노라마가 가장 빈번한 방사선 시술. gijbels의 phantom 예측을 실제 코호트가 뒷받침. [합의수준 — cross-sectional + registry]
- **차폐 부재의 대가** — kabier (2025): 이라크 개방형 클리닉(차폐 촬영실 없음) TLD-200 실측, 납복(lead apron) 위 흉부 치과의사 5.623 mSv/y·조무사 5.279 mSv/y — 한국 대비 **~30배↑**(여전히 20 mSv/y 한도 내). 즉 직업피폭의 단일 최대 결정인자는 PPE가 아니라 **차폐 촬영실의 유무**. 일반병원 치과가 환자 처리량 때문에 단독 클리닉보다 高피폭. [근거강함 — prospective TLD]
- **휴대형(handheld)도 안전** — rottke (2018): 휴대형 구내 X-ray(Aribex NOMAD Pro 2) RANDO 팬텀 실험, 초점 수직면 뒤(술자 위치)에서 산란선 미검출, 관리구역(4000회 모의노출 평균 16.7 cm)이 유럽·국제 기준보다 훨씬 작음 → 제조사 지침 준수 시 술자 위험 증가 없음(내장 backscatter shield 기여). [합의수준 — phantom]

> [!note] 술자 안전 함의
> 환자 차폐 중단(benavides 2023)과 직업피폭 데이터는 같은 결론으로 수렴 — 절대선량이 워낙 낮아 추가 차폐의 한계효용이 작다. 단 술자 측에서 흔들리는 변수는 **거리(≥1 m)·차폐 촬영실**이지 납복 그 자체가 아니다(kabier의 5.6 mSv도 납복 위 측정값). 핵심 실무 = 촬영 중 ≥1 m 후퇴 + 차폐 구조 확보.

## 분기 — 정당화(Justification) + 누적 위험

선량을 줄이는 레버 이전에 "이 촬영이 정당한가"가 먼저다(ALARA의 첫 기둥). 이 분기는 특히 **소아·교정**에서 반복촬영의 누적 위험과 정당화 실행률을 다룬다.

- **휴대형 정당화 게이트** — berkhout (2015, EADMFR 합의/position paper): 휴대형 구내 X-ray는 시준(rectangular collimation) 적용 곤란·노출시간 연장·통제 안 된 환경 사용으로 (재)피폭을 늘려 ALARA를 위반할 소지 → **문서화된 평가 + 의학물리 지원 + 명확한 이득 + 술자·제3자 신규 위험 없음**을 충족할 때만 "매우 예외적으로" 사용. rottke의 측정 안전성과 berkhout의 정당화 신중론은 상보적(안전하다고 무분별 사용 금지). [합의수준 — consensus]
- **소아 누적선량의 집중** — hedesiu (2018, 후향 n=7,150 루마니아 소아): 2D 촬영 중앙값 <20 µSv인 반면 **CBCT 중앙값 127 µSv**, 최대값은 자연배경 **34.1일분**(11~15세 교정 CBCT에 집중). CBCT는 촬영의 **11%인데 집단선량의 70%** — 소아 선량관리의 표적은 CBCT 정당화임을 정량 확립. [근거강함 — 대규모 retrospective]
- **교정 전 과정의 배경-일 앵커** — stervik (2024, 후향 n=1,790 스웨덴): 교정 1코스(환자당 ~7장: 파노라마 1 + 측방두부계측 1 + 치근단 ~3) = 자연배경 **5~10일분**, 추정 치명적 암위험 <10만 명당 1. 측방두부계측 5.6 µSv·파노라마는 그 ~6배. 그러나 **정당화 기록은 계획단계 촬영의 5%**(치료 60%, 추적 15%)에 그쳐 — 위험은 작아도 高빈도 시술이므로 정당화 실행률이 ALARA 품질지표. hedesiu·stervik이 서로 독립적 "배경-일" 데이터로 교차검증. [근거강함 — retrospective]

> [!note] 정당화 실무 함의
> 소아·청소년에서 per-patient 위험은 작지만(stervik, hedesiu) CBCT가 집단선량을 지배(hedesiu 70%)하고 정당화 기록은 5%에 불과(stervik) → 클리닉 액션 = ① 소아 CBCT는 적응증 정당화 문서화를 루틴 강제, ② 교정 진단 시 2D로 충분하면 CBCT 회피, ③ 반복촬영 누적분을 환자기록에 명시.

## 임상 의사결정 ladder (요약)

0. **이 촬영이 정당한가?** → 적응증 없으면 안 찍는다(ALARA 첫 기둥). 소아 CBCT·휴대형 장비는 정당화 문서화 강제(berkhout 2015, hedesiu 2018, stervik 2024 — 정당화 기록률 5% 격차).
1. **이 정보가 2D로 충분한가?** → 충분하면 파노라마/구내로 내린다 (CBCT 회피 = 최대 절감). [근거강함]
2. **3D가 필요한가?** → 적응증 정당화(jacobs 2018, fontenele 2025 전공별 차트). FOV는 진단과제에 맞춰 최소화(ozaki, khafaji).
3. **노출 파라미터·조사야:** 직사각조준 표준화(ludlow 2008, johnson 2020 — FMS 34.9~54 µSv), 고관전압 + 저mAs, 복셀은 진단 한도 내 유지(charuakkra, oenning). 소아는 ALADAIP + 짧은 빔높이(oenning, lee 2019, hidalgo-rivas).
4. **차폐:** 구내·파노라마·CBCT 갑상선 칼라 루틴 미사용(benavides, schindler, johnson 2020 — 직사각조준 > 갑상선 차폐) — 국내 규정 확인 단서.
5. **술자·조무사 안전:** 촬영 중 ≥1 m 후퇴 + 차폐 촬영실 확보(gijbels 2005, kim 2016 0.18 mSv/y; kabier 2025 차폐 부재 시 30배↑; rottke 2018 휴대형도 지침 준수 시 안전).
6. **반복촬영 소아·교정:** 0.55 T MRI 비전리 대안 검토(willershausen).

## 미해결·검증 필요
- 선량 최적화 자체에 대한 **SR+MA 부재** — 본 thesis의 레버 효과 크기는 대부분 phantom/MC 기반. [claude해석]
- 한국 DRL(kang 2024) 최신 시행상태·수치는 변동 가능 — 인용 시 식약처/질병청 최신 고시 확인 필요. [미검증 — 본 wiki는 web search 미사용 정책]
- 0.55 T MRI는 단일기관 소표본 — 진단정확도 SR 축적 전까지 보조적 위치. [근거강함→적용 한정]

## Related Papers

선량·최적화 군:
- [[radiology/lee-2021-dental-imaging-doses-web-dose-calculator]] — modality 선량 위계 기준선
- [[radiology/ludlow-2008-patient-risk-dental-radiographic-examinations]] — ICRP 2007 환자선량 표준 표·직사각조준 91% 저감
- [[radiology/johnson-2020-intraoral-radiograph-dose-collimation-thyroid-shielding]] — 최신 RC 시스템·RC > 갑상선 차폐
- [[radiology/fontenele-2025-cbct-dentistry-clinical-recommendations-indication]] — 전공별 CBCT 파라미터 차트
- [[radiology/jacobs-2018-cbct-implant-dentistry-recommendations-clinical]] — 임플란트 CBCT 정당화
- [[radiology/kaasalainen-2021-dental-cone-beam-ct-updated-review]] — dosimetry·DRL 의학물리 프레임
- [[radiology/oenning-2019-halve-dose-paediatric-cone-beam-ct]] — 복셀·노출 레버, ALADAIP
- [[radiology/hidalgo-rivas-2015-low-dose-cbct-anterior-maxilla-children]] — 소아 저선량 프로토콜
- [[radiology/charuakkra-2023-low-dose-cbct-image-dose-comparison]] — 고관전압 ULD/LD
- [[radiology/ozaki-2021-cbct-effective-dose-monte-carlo-simulation]] — FOV 전략·MC 효율
- [[radiology/lee-2019-cbct-dose-osl-monte-carlo-comparison]] — dosimetry 방법 신뢰도
- [[radiology/benchimol-2018-collimation-panoramic-effective-dose-reduction]] — 파노라마 collimation
- [[radiology/lee-2019-monte-carlo-paediatric-panoramic-dose-reduction]] — 빔높이 레버
- [[radiology/khafaji-2023-scattered-dose-eye-dentistry-cbct]] — FOV-산란선량 의존

방호·거버넌스·대안:
- [[radiology/benavides-2023-patient-shielding-dentomaxillofacial-radiography]] — 차폐 중단 합의
- [[radiology/schindler-2025-panoramic-thyroid-eye-lens-dose]] — 갑상선·수정체 실측
- [[radiology/kang-2024-national-dental-radiological-dose-management]] — 국가 DRL
- [[radiology/lee-2024-dental-dose-monitoring-system-establishment]] — 선량 모니터링
- [[radiology/baena-2022-cbct-diagnostic-performance-root-resorption]] — 진단정확도-피폭 trade-off
- [[radiology/willershausen-2025-low-field-mri-pediatric-dental]] — 비전리 MRI 대안

직업피폭·술자 안전 군:
- [[radiology/gijbels-2005-dosimetry-digital-panoramic-occupational-exposure]] — 파노라마 1 m 산란 ≤0.60 µGy/촬영
- [[radiology/kim-2016-occupational-radiation-procedures-doses-korean-dentists]] — 한국 치과의사 0.18 mSv/y (차폐 촬영실)
- [[radiology/kabier-2025-xray-radiation-exposure-open-dental-clinics-tld]] — 개방형 클리닉 5.6 mSv/y (차폐 부재 30배↑)
- [[radiology/rottke-2018-operator-safety-during-the-acquisition]] — 휴대형 구내 X-ray 술자측 산란 미검출

정당화·누적 위험 군:
- [[radiology/berkhout-2015-justification-and-good-practice-using]] — 휴대형 정당화 우선 EADMFR 합의
- [[radiology/hedesiu-2018-dental-radiological-irradiation-pediatric-population]] — 소아 CBCT = 집단선량 70%
- [[radiology/stervik-2024-radiation-exposure-during-orthodontic-treatment]] — 교정 1코스 = 배경 5~10일·정당화 기록 5%

파노라마 기하·판독(선량 비직접, 별도 서브클러스터):
- [[radiology/martins-2022-multilayer-panoramic-radiography-device-mapping]] · [[radiology/devlin-2013-object-position-magnification-panoramic-radiography]] · [[radiology/farman-2010-panoramic-ccd-storage-phosphor-film]] · [[radiology/ramos-2016-ghost-images-metal-objects-panoramic]] · [[radiology/kim-2024-real-ghost-pseudo-ghost-images-panoramic]]
