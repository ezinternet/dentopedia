---
title: "Dental Radiographic Artifacts — A Taxonomy Across Panoramic and Intraoral (PA) Imaging: Ghost Images, Geometry Errors, Receptor/Scanning Artifacts, and Disease-Mimicking Optical Effects"
authors: synthesis (llm-wiki)
year: 2026
date: 2026-07-03
type: overview
category: [overviews]
tags: [radiology, artifact, panoramic, periapical, intraoral, bitewing, ghost-image, pseudo-ghost, cone-cut, focal-trough, magnification, psp, phosphor-plate, scanning-artifact, mach-band, cervical-burnout, triangular-radiolucency, false-positive, overdiagnosis, image-quality, retake, masking-test]
source_papers:
  - radiology/lingam-2023-common-errors-subjective-quality-panoramic
  - radiology/elkhateeb-2022-psp-image-plate-artifacts-prevalence
  - radiology/dioguardi-2025-radiographic-artifacts-caries-diagnosis-sr-ma
  - radiology/kim-2024-real-ghost-pseudo-ghost-images-panoramic
  - radiology/ramos-2016-ghost-images-metal-objects-panoramic
  - radiology/devlin-2013-object-position-magnification-panoramic-radiography
  - radiology/martins-2022-multilayer-panoramic-radiography-device-mapping
  - radiology/farman-2010-panoramic-ccd-storage-phosphor-film
confidence: synthesis
source: synthesis
---

> [!summary] 한국어 핵심요약
> - **결론(요지)**: 치과 방사선 artifact는 원인 기전에 따라 **4계열** — ① 기하/자세(geometry) ② 유령상(ghost) ③ 수용체·스캐닝(receptor/scanning) ④ 해석적·광학(optical) — 으로 나뉜다. 앞 셋은 "**영상이 잘못 찍힌 것**"(재촬영·피폭 문제), 넷째는 "**정상을 병으로 오인**"(과진단·과치료 문제)이다.
> - **파노라마 자세오류(Positioning Error)는 예외가 아니라 규칙**: 2,629장 감사에서 무오류는 32.8%뿐, 77.2%가 오류 1개 이상, 진단 불가(diagnostically unacceptable) ~15%로 권고 기준(≤10%) 초과 (Lingam 2023).
> - **유령상(Ghost Image)의 물리**: 방사선원과 회전중심(center of rotation) 사이의 불투과성 물체가 **반대측·더 높은 위치·확대·흐릿하게** 투영. 원인은 귀걸이·헤어핀·납방어복·갑상선보호대·하악골·경추 등 (Ramos 2016). 실상(real)·유령상(ghost)·유사유령상(pseudo-ghost)이 한 장에 공존할 수 있다 (Kim 2024).
> - **유령상은 드물지만 소아에 몰림**: 파노라마 error 10(reflected/ghost)은 전체 ~2.2%로 최소 빈도지만 5–12세에서 유의(P=0.001), 대표 사례가 갑상선보호대 유령상 (Lingam 2023).
> - **초점골(Focal Trough)이 기하 왜곡의 근원**: 초점골 밖 물체는 수평/수직 배율이 달라 확대·축소·중첩된다. 물체 위치→배율 관계가 이론적으로 규명됐고 (Devlin 2013), 실측 매핑도 됨 (Martins 2022).
> - **구내(PA) artifact는 치근단 영상에 집중**: 구내 PSP(광자극형광판, Photostimulable Phosphor plate) 5만 장 중 7.1%가 artifact로 재촬영, **그중 80.8%가 치근단(Periapical, PA)** (Elkhateeb 2022).
> - **PA 기술 artifact 3범주**: 술자오류(70.4%, cone cut 39.5% 최다) > 판오류(교흔 bite mark 40.3%) > 스캐닝오류(지연 스캐닝 delayed scanning 39.9%). PSP는 필름보다 굽힘·긁힘·스캐닝 artifact가 많음 (Elkhateeb 2022, Farman 2010).
> - **해석적 광학 artifact가 우식을 위조**: 마하밴드(Mach Band, 밀도경계 착시)·치경부소각(Cervical Burnout, 접선투과)·삼각형투과상(Triangular-Shaped Radiolucency, TSR)이 우식으로 오인. 상악 대구치 비우식 TSR ~26%, 위양성(false positive) ~13% (Dioguardi 2025 SR+MA).
> - **소아 과진단 경보**: TSR은 유치(~51%)가 영구치(~27%)보다 훨씬 흔해, 소아 bitewing에서 없는 우식을 치료할 위험이 크다 (Dioguardi 2025).
> - **감별 원칙**: 유령상은 "반대측+상방+흐림+확대", 실상은 정위치·선명. 광학 artifact는 **masking test**(법랑질 변연 가림 → 투과상 소실 시 마하밴드)·회전(cone cut은 재촬영). 최종 확진은 **임상검사·필요시 CBCT**로 보완 — 방사선은 임상을 보조하되 대체하지 않는다.
> - **행동 지침**: (1) 촬영 전 금속·보호대 제거·정확한 자세, (2) PSP 취급·즉시 스캔·스캐너 유지보수, (3) 판독 시 artifact를 먼저 배제한 뒤 병변 진단, (4) 소아·상악 대구치 근심면은 TSR/마하밴드 의심을 기본값으로.

## One-line Summary

A cross-paper synthesis organizing dental radiographic artifacts into four mechanistic classes — geometry/positioning, ghost/double images, receptor/scanning, and disease-mimicking optical effects — spanning panoramic and intraoral (periapical/bitewing) imaging: the first three degrade or repeat the image (a dose/quality problem), while the fourth causes false-positive diagnoses (an overtreatment problem); it consolidates prevalence figures (77.2% of panoramics carry ≥1 positioning error; PA images = 80.8% of intraoral artifact retakes; ~26% TSR and ~13% optical false-positives), the physics of ghost images and the focal trough, and the clinical rules for telling an artifact from true pathology.

## 한줄요약

치과 방사선 artifact를 4가지 기전(기하/자세·유령상·수용체/스캐닝·해석적 광학)으로 분류해 파노라마와 구내(치근단/bitewing) 영상을 아우르는 종합 페이지: 앞 세 계열은 영상을 망가뜨리거나 재촬영을 부르는 **화질·피폭** 문제, 넷째는 없는 병을 만드는 **과진단** 문제다. 유병률(파노라마 오류 77.2%, 구내 artifact 재촬영의 80.8%가 PA, 상악 대구치 TSR ~26%·위양성 ~13%), 유령상·초점골의 물리, 그리고 artifact와 진짜 병변을 가르는 임상 감별 원칙을 정리한다.

## Why This Overview

Individual artifact papers answer narrow questions (how ghost images form, how often positioning fails, how optical effects fake caries), but a clinician reading a film needs the **whole map at once**: *what class of artifact am I looking at, and is it faking disease?* This page unifies eight wiki pages into a single taxonomy and a differentiation workflow, so an artifact is recognized and dismissed before it becomes a misdiagnosis or an unnecessary retake.

## The Four-Class Taxonomy

Dental radiographic artifacts sort cleanly by **mechanism**, and the mechanism dictates both the fix and the clinical stakes.

| Class | Where | Representative artifacts | Core problem | Key papers |
|---|---|---|---|---|
| **1. Geometry / positioning** | Panoramic + PA | Cone cut, chin tilt (V-shape/gazebo), midline asymmetry, magnification/distortion, focal-trough loss of sharpness | Image degraded → **retake / dose** | Lingam 2023; Devlin 2013; Martins 2022; Elkhateeb 2022 |
| **2. Ghost / double images** | Panoramic (rotational) | Contralateral magnified blurred shadows of jewelry, earrings, lead apron, thyroid collar, spine, mandible | Mimics a lesion / obscures anatomy → **misread** | Ramos 2016; Kim 2024; Lingam 2023 |
| **3. Receptor / scanning** | Intraoral PSP (also CCD) | Bite marks, scratches, image-size reduction, delayed-scan fading, white/black lines, reversed image | Image degraded → **retake / dose** | Elkhateeb 2022; Farman 2010 |
| **4. Optical / interpretive** | PA + bitewing | Mach band, cervical burnout, triangular-shaped radiolucencies (TSR) | Fakes disease → **false-positive / overtreatment** | Dioguardi 2025 |

**The load-bearing distinction**: classes 1–3 make the image *wrong or unusable* (you retake it, costing dose); class 4 makes a *normal image look pathological* (you over-treat). Recognizing which class you face decides whether the next step is "repeat the exposure" or "prove this isn't a real lesion."

## Class 1 — Geometry & Positioning

**Panoramic positioning is the rule-breaker, not the exception.** In a 2,629-image audit only 32.8% were error-free; 77.2% carried ≥1 positioning error and ~15% were diagnostically unacceptable — above the ≤10% benchmark (Lingam 2023). The ten classic errors map to identifiable features: tongue-not-to-palate (commonest, radiolucent airspace over maxillary apices), chin-down "V-shape/gazebo," chin-up flat occlusal plane, midline asymmetry, and slumping (spine "Washington-monument" shadow).

**The focal trough (image layer) is the physical root of distortion.** Objects outside the trough are magnified, minified, overlapped, or blurred because horizontal and vertical magnification differ with object position — a relationship derived theoretically (Devlin 2013) and empirically mapped for a multilayer device (Martins 2022). For intraoral PA, the dominant geometry error is **cone cut** (39.5% of PSP operator errors), plus improper placement and projection-geometry errors (elongation/foreshortening) (Elkhateeb 2022).

## Class 2 — Ghost & Double Images (panoramic)

**Mechanism (Ramos 2016):** a ghost image forms when a radiopaque object lies **between the X-ray source and the machine's center of rotation** with enough density to attenuate the beam. The ghost projects to the **contralateral side, higher, magnified, and blurred**. Typical culprits: earrings, hairpins, piercings, lead apron, **thyroid collar**, and dense anatomy (mandible, cervical spine, hyoid).

**Real vs ghost vs pseudo-ghost (Kim 2024):** all three can coexist on one film. The differentiators — a true (real) image is at the correct location and sharp; a ghost is contralateral, superior, magnified, blurred; a pseudo-ghost arises when the object is near/within the rotation center. Unilateral jewelry misread as a radio-opaque disease entity is the classic trap. **Prevalence is low but pediatric-skewed:** ghost/reflected images (panoramic error 10) were ~2.2% overall but significantly concentrated in 5–12-year-olds (P=0.001), exemplified by a thyroid collar imaged as a ghost (Lingam 2023).

## Class 3 — Receptor & Scanning Artifacts (intraoral PSP)

**PA images bear the brunt of intraoral artifacts.** Across 50,000 intraoral PSP radiographs, 7.1% required artifact retakes and **80.8% of those were periapical** (Elkhateeb 2022). The three sub-causes:

- **Operator (70.4% of retakes)** — cone cut, placement, geometry (overlaps Class 1).
- **Plate (19.3%)** — **bite marks (40.3%)**, image-size reduction, scratches, contamination, coat peeling.
- **Scanning (10.3%)** — **delayed-scan fading (39.9%)** from ambient-light latent-image loss, white lines (scanner-slit dust), black lines (electromagnetic interference), double image (incomplete erasing), reversed image (plate placed backwards).

**Receptor choice modulates the artifact profile:** PSP plates are cordless and film-like but bend/scratch-prone and add scanning-stage artifacts, whereas CCD/CMOS give immediate images without a scanning step (Farman 2010). The fix is training + gentle handling + prompt scanning + scanner maintenance — and every avoided retake is avoided dose.

## Class 4 — Optical / Interpretive Artifacts (the dangerous class)

These do not degrade the image — they make a **normal structure look carious**, and they are the only class that directly causes overtreatment (Dioguardi 2025 SR+MA):

- **Cervical burnout** — tangential beam across the curved proximal surface near the CEJ yields a false radiolucency mimicking root/cervical caries (worse in multirooted teeth).
- **Mach band effect** — a visual-system contrast illusion at a density boundary (e.g., the EDJ) creates an apparent radiolucency.
- **Triangular-shaped radiolucencies (TSR)** — non-carious lucencies on the **mesial of maxillary molars** from Carabelli-cusp superimposition.

**Numbers:** non-carious TSR prevalence on maxillary molars ≈ **26%** (pooled 0.308), and optical effects were **misread as caries/fracture in ~13%** of observations. The pediatric alarm: TSR is far commoner in **primary (~51%) than permanent (~27%)** molars — so children's bitewings are where phantom caries most often gets treated. Certainty is low–very low (5 observational studies, I²>90%), but the direction is clear and clinically consequential.

## Differentiating Artifact from True Pathology — A Practical Workflow

1. **Localize the class.** Contralateral + superior + blurred + magnified → **ghost** (Class 2). Clear unexposed border → **cone cut** (Class 1). Lines/bite marks/uneven density → **receptor/scanning** (Class 3). Radiolucency at CEJ / EDJ / mesial maxillary molar → suspect **optical** (Class 4).
2. **For optical effects, run the masking test.** Cover the radiopaque enamel margin: if the radiolucency disappears it was a **Mach band**; if it persists it may be a true outer-dentine lesion (Dioguardi 2025). Digital grey-level/contrast analysis and beam-angle change help similarly.
3. **For ghosts, use position + a second view.** A ghost has no true anatomic correlate on the ipsilateral side; a repeat with the object removed, or a small-FOV/PA/CBCT view, confirms unilaterality (Ramos 2016; Kim 2024).
4. **For geometry/receptor errors, retake correctly** — reposition, remove metal, re-place/re-scan the plate — rather than over-interpreting a distorted image.
5. **Always correlate with clinical examination** (and, when justified, CBCT). Radiography supports, not replaces, the clinical diagnosis — the recurring conclusion across the interpretive-artifact and ghost-image literature.

## Clinical Bottom Line

- **Recognize the class before diagnosing.** Three of four artifact classes are image-quality/dose problems solved by better technique; the fourth is an overdiagnosis problem solved by disciplined interpretation.
- **Prevention up front:** remove jewelry/metal and position the thyroid collar to avoid ghosts; accurate patient positioning; careful PSP handling and prompt scanning.
- **Interpretation discipline:** default to suspecting Mach band / cervical burnout / TSR at the CEJ, EDJ, and mesial maxillary molars — especially in **children** — and confirm with the masking test and clinical exam before restoring.
- **Every avoidable retake is avoidable radiation** — linking artifact control to the wiki's dose-optimization overviews.

## Source Papers

- [[radiology/lingam-2023-common-errors-subjective-quality-panoramic]] — panoramic positioning-error prevalence (77.2% ≥1 error; ghost = error 10, pediatric-skewed).
- [[radiology/elkhateeb-2022-psp-image-plate-artifacts-prevalence]] — intraoral PSP artifact prevalence; PA = 80.8% of retakes; operator/plate/scanning taxonomy.
- [[radiology/dioguardi-2025-radiographic-artifacts-caries-diagnosis-sr-ma]] — SR+MA of optical artifacts (Mach band, cervical burnout, TSR); ~26% TSR, ~13% false-positive.
- [[radiology/kim-2024-real-ghost-pseudo-ghost-images-panoramic]] — real vs ghost vs pseudo-ghost differentiation on one film.
- [[radiology/ramos-2016-ghost-images-metal-objects-panoramic]] — ghost-image formation physics from facial metal objects.
- [[radiology/devlin-2013-object-position-magnification-panoramic-radiography]] — object-position/magnification theory (focal-trough distortion).
- [[radiology/martins-2022-multilayer-panoramic-radiography-device-mapping]] — empirical focal-trough/device mapping.
- [[radiology/farman-2010-panoramic-ccd-storage-phosphor-film]] — receptor comparison (CCD vs PSP vs film) contextualizing receptor-dependent artifacts.

## Related Overviews

- [[overviews/dental-imaging-radiation-dose-optimization-overview]] — the dose side; artifact-driven retakes are an avoidable dose source.
- [[overviews/dental-imaging-effective-dose-background-equivalent-overview]] — communicating imaging dose in relatable terms.
