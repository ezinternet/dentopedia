---
title: "Dental Imaging Radiation Dose Optimization — Modality Hierarchy, Optimization Levers, and the Shielding/MRI Paradigm Shift"
authors: synthesis (llm-wiki)
year: 2026
date: 2026-06-05
type: overview
category: [overviews]
tags: [radiology, radiation-dose, dose-optimization, CBCT, panoramic, effective-dose, ALADAIP, ALARA, paediatric, collimation, FOV, voxel, kVp, mAs, Monte-Carlo, OSLD, TLD, diagnostic-reference-level, DRL, thyroid-shielding, low-field-MRI, focal-trough, ghost-image, dosimetry]
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
confidence: synthesis
source: synthesis
---

## One-line Summary

Across 18 dental-radiology papers, patient dose is governed by a fixed modality hierarchy (intraoral ~1.3 ≪ panoramic ~18 ≪ CBCT ~121 µSv) onto which four operator-controllable levers act — field-of-view/collimation, kVp/mAs, voxel size, and (panoramic) beam height — while two paradigm shifts reframe protection: contact shielding (gonad/thyroid) is now recommended against, and radiation-free 0.55 T MRI emerges as a non-ionizing alternative for selected paediatric indications.

## 한줄요약

치과 영상 선량은 고정된 modality 위계(구내 ~1.3 ≪ 파노라마 ~18 ≪ CBCT ~121 µSv) 위에서 결정되며, 그 위에 술자가 조절 가능한 네 레버(FOV/collimation, kVp/mAs, 복셀 크기, 파노라마 빔높이)가 작용한다. 동시에 두 패러다임 전환이 방호 개념을 바꾼다 — 접촉 차폐(생식선·갑상선)는 이제 권고되지 않고, 무피폭 0.55 T MRI가 일부 소아 적응증의 비전리 대안으로 등장한다. 문헌 18편 횡단 종합. [근거강함 — modality 위계·차폐 권고], [합의수준 — 최적화 레버]

---

## Summary

이 overview는 `wiki/radiology/`의 18편을 횡단 합성한다. 근거 분포: **consensus 1편**(benavides 2023) · **narrative/리뷰 5편**(fontenele 2025, jacobs 2018, kaasalainen 2021, lee&badal 2021, kang 2024, lee 2024) · **SR 1편**(khafaji 2023) · **SR+MA 1편**(baena 2022) · **phantom/in-vitro·MC 6편**(oenning 2019, hidalgo-rivas 2015, charuakkra 2023, ozaki 2021, lee 2019 OSLD, benchimol 2018, lee 2019 panoramic) · **prospective 1편**(willershausen 2025). 이 카테고리에는 선량 최적화 자체에 대한 SR+MA가 아직 없다 — 최강 결론도 "일관된 다수 phantom/MC + 합의 권고" 수준이다. [claude해석 — 등급 분포는 리포지토리 계측]

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

## 임상 의사결정 ladder (요약)

1. **이 정보가 2D로 충분한가?** → 충분하면 파노라마/구내로 내린다 (CBCT 회피 = 최대 절감). [근거강함]
2. **3D가 필요한가?** → 적응증 정당화(jacobs 2018, fontenele 2025 전공별 차트). FOV는 진단과제에 맞춰 최소화(ozaki, khafaji).
3. **노출 파라미터:** 고관전압 + 저mAs, 복셀은 진단 한도 내 유지(charuakkra, oenning). 소아는 ALADAIP + 짧은 빔높이(oenning, lee 2019, hidalgo-rivas).
4. **차폐:** 구내·파노라마·CBCT 갑상선 칼라 루틴 미사용(benavides, schindler) — 국내 규정 확인 단서.
5. **반복촬영 소아·교정:** 0.55 T MRI 비전리 대안 검토(willershausen).

## 미해결·검증 필요
- 선량 최적화 자체에 대한 **SR+MA 부재** — 본 thesis의 레버 효과 크기는 대부분 phantom/MC 기반. [claude해석]
- 한국 DRL(kang 2024) 최신 시행상태·수치는 변동 가능 — 인용 시 식약처/질병청 최신 고시 확인 필요. [미검증 — 본 wiki는 web search 미사용 정책]
- 0.55 T MRI는 단일기관 소표본 — 진단정확도 SR 축적 전까지 보조적 위치. [근거강함→적용 한정]

## Related Papers

선량·최적화 군:
- [[radiology/lee-2021-dental-imaging-doses-web-dose-calculator]] — modality 선량 위계 기준선
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

파노라마 기하·판독(선량 비직접, 별도 서브클러스터):
- [[radiology/martins-2022-multilayer-panoramic-radiography-device-mapping]] · [[radiology/devlin-2013-object-position-magnification-panoramic-radiography]] · [[radiology/farman-2010-panoramic-ccd-storage-phosphor-film]] · [[radiology/ramos-2016-ghost-images-metal-objects-panoramic]] · [[radiology/kim-2024-real-ghost-pseudo-ghost-images-panoramic]]
