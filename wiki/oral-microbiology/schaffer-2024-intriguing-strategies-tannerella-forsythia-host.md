---
title: "The intriguing strategies of Tannerella forsythia host interaction"
authors: "Schäffer C, Andrukhov O"
year: 2024
doi: 10.3389/froh.2024.1434217
source: sources/schaffer-2024-intriguing-strategies-tannerella-forsythia-host.md
category: oral-microbiology
evidence_level: narrative-review
source_collection: pubmed-abstract
pmcid: PMC11169705
pmid: "38872984"
date: 2024-05-30
tags:
  - Tannerella-forsythia
  - red-complex
  - periodontal-pathogen
  - S-layer
  - BspA
  - T9SS
  - O-glycosylation
  - sialidase
relations:
  - target: oral-microbiology/socransky-1998-microbial-complexes-subgingival-plaque
    type: extends
  - target: oral-microbiology/hajishengallis-2014-porphyromonas-gingivalis-host-manipulation
    type: reinforces
---

> [!summary] 한국어 핵심요약
> - 타네렐라 포르시티아 (Tannerella forsythia, T. forsythia)는 적색복합체 (Red Complex) 구성원이나, 숙주-미생물총 상호작용 조작 능력은 포르피로모나스 진지발리스 (Porphyromonas gingivalis) 수준의 키스톤 병원체 (keystone pathogen)로 아직 인정되지 않음
> - 핵심 독성인자: S층 (S-layer, TfsA/TfsB), 세균 표면 단백질 BspA (Bacterial Surface Protein A), 시알리다아제 (Sialidase, NanH), KLIKK 프로테아제 (Proteases) — 미로핀·카릴리신·미로리신, 외막소포 (Outer Membrane Vesicles, OMVs), 거친형 지질다당류 (rough-type LPS)
> - 제9형 단백질 분비계 (Type 9 Protein Secretion System, T9SS): P. gingivalis와 공유하는 핵심 분비 경로; T9SS 붕괴 시 숙주 전염증 반응 감소
> - 단백질 O-당화 (O-glycosylation): S층 단백질의 비아눌로손산 (nonulosonic acid) 기반 9당 수식이 면역 회피와 숙주 내 지속을 담당; 당화 패턴 절단 시 Th17 반응 유도 → 치조골 소실 감소
> - BspA는 TLR2/CD14 경로로 대식세포·수지상세포 사이토카인 유도; 마우스 실험에서 BspA 결핍 시 치조골 소실 유의하게 감소
> - N-아세틸무라민산 (N-acetylmuramic acid, MurNAc) 요구증 (auxotrophy): 세포벽 합성 불가, 공생 세균에 의존 → 포스포마이신 내성
> - P. gingivalis와 비교: 진지발리스는 진지파인 (gingipain)으로 IL-8 국소 마비·강력한 단백질 분해; T. forsythia는 사이토카인 단백질 분해 능력 열위, PMN 이주 직접 차단 불가
> - 숙주 세포별 반응: 상피세포 침입(BspA·NanH 매개), PMN 기능 간접 약화, 대식세포 IL-1β/TNF-α/IL-6 유도, 치주인대 간엽줄기세포 IL-6/IL-8/MCP-1 유도
> - BspA는 THP-1 대식세포에서 거품세포 (foam cell) 형성 유도 및 ApoE 마우스 동맥경화 병변 촉진 → 전신 건강 연관성 시사
> - 한계: 단일 배양·마우스 단독감염 모델 중심; 임상 분리주 vs. ATCC 43037 균주 간 독성 차이 미규명; 다균종 생태 조건에서의 역할 불명

## Three-line Summary

*Tannerella forsythia*, the least-studied red-complex member, fields a molecular arsenal — S-layer O-glycosylation, BspA, NanH sialidase, KLIKK proteases, OMVs, and LPS — that modulates innate immune defense without achieving keystone-pathogen equivalence to *P. gingivalis*. Its defining survival adaptation is MurNAc auxotrophy, enforcing biofilm co-dependency. The S-layer glycosylation pattern is the pivotal immunological switch: native nonasaccharide enables persistence; truncation triggers Th17-mediated clearance and reduced bone loss.

## 세줄요약

타네렐라 포르시티아는 가장 덜 연구된 적색복합체 구성원으로, S층 O-당화·BspA·시알리다아제·KLIKK 프로테아제·외막소포·LPS라는 분자 무기고를 통해 선천면역을 조절하지만, P. gingivalis 수준의 키스톤 병원체로는 아직 인정되지 않는다. 고유한 생존 적응 전략은 MurNAc 요구증으로, 생물막 공생 의존성을 강제한다. S층 당화 패턴이 핵심 면역 스위치로 작동해, 완전한 9당 수식은 숙주 내 지속을 허용하고 절단 시 Th17 반응과 치조골 소실 감소를 유도한다.

---

## Background and Scope

*Tannerella forsythia* is a Gram-negative, anaerobic, rod-shaped member of the *Bacteroidota* phylum and a founding member of the **red complex** identified by [[oral-microbiology/socransky-1998-microbial-complexes-subgingival-plaque|Socransky 1998]]. Despite its co-occurrence with *P. gingivalis* and *T. denticola* in severe periodontitis, its molecular virulence mechanisms have received far less attention. This 2024 perspective review by Schäffer and Andrukhov synthesizes current understanding of *T. forsythia* host interaction strategies, explicitly positioning them against the better-characterized *P. gingivalis* ([[oral-microbiology/hajishengallis-2014-porphyromonas-gingivalis-host-manipulation|Hajishengallis 2014]]).

## Shared Infrastructure with *P. gingivalis*

Both red-complex members share two foundational mechanisms:

1. **Type 9 Protein Secretion System (T9SS)** — the *Bacteroidota*-characteristic outer-membrane export machinery for virulence factors with C-terminal targeting domains. T9SS disruption (via PorU deletion) reduces macrophage and fibroblast pro-inflammatory responses to *T. forsythia*.
2. **O-glycosylation** — extensive surface protein modification with species-specific glycans; in *T. forsythia*, a nonasaccharide containing nonulosonic acid mimics host sialic acid to suppress immune recognition.

## Unique Trait: MurNAc Auxotrophy

*T. forsythia* cannot synthesize N-acetylmuramic acid (MurNAc), the essential peptidoglycan building block (no MurAB enzymes). It survives exclusively by scavenging MurNAc from cell wall turnover or bacterial decay in the biofilm community — making it uniquely dependent on cohabitors. A side effect: resistance to **fosfomycin**.

## Virulence Factor Compendium

### S-layer (TfsA/TfsB): Immunological Gatekeeper

The entire cell surface is covered by a 2D-crystalline array of TfsA and TfsB, each multiply modified by a nonasaccharide at the D(S/T)(A/I/L/M/T/V/S/C/G/F/N/E/Q/D/P) motif.

Phenotypic consequences of S-layer deletion:
- Earlier, more intense pro-inflammatory mediator production in macrophages and gingival fibroblasts
- Induction of MCP and GM-CSF in oral epithelial cells
- Significantly reduced adherence to gingival epithelial cells

Glycosylation specificity:
- Native nonasaccharide → immune persistence (Th17 suppression, PMN evasion)
- Truncated glycosylation (Δ nonulosonic acid branch) → robust Th17 response, reduced alveolar bone loss in mice
- Pre-immunization with the Th17-biasing strain protects against subsequent wild-type challenge
- Recognized by macrophage-inducible C-type lectin receptors (Mincle) on myeloid cells
- Governs *T. forsythia* positioning and co-localization with *P. gingivalis* in multispecies biofilm

### Sialidase NanH: Attachment and Nutrient Acquisition

The sialic acid utilization operon (NanH, NanT, NanS):
- NanH cleaves terminal sialic acid from mucins and host glycoproteins → exposes hidden epitopes for bacterial adhesion
- NanT loss diminishes epithelial cell attachment and survival
- NanS (esterase) extends substrate range to diacetylated sialic acids, acting synergistically with *P. gingivalis* sialidase

### KLIKK Proteases: Immune Evasion Arsenal

| Protease | Primary Targets | Mechanism |
|---|---|---|
| Miropin | Neutrophil elastases, cathepsin G | Serine protease inhibitor (serpin); impairs PMN bactericidal function |
| Karylisin | Complement (multiple stages), cathelicidin | Metalloproteinase; antimicrobial peptide degradation |
| Mirolysin | Cathelicidin, host proteases | Metalloproteinase |
| PrtH | Attachment proteins | Associated with attachment loss |
| KLIKK (general) | Collagen, gelatine, elastin, casein | Broad substrate range; transcripts in ~all GCF samples with *T. forsythia* present |

Key distinction from *P. gingivalis*: gingipains degrade host cytokines/chemokines far more efficiently than *T. forsythia* proteases — a major reason *P. gingivalis* achieves "chemokine paralysis" while *T. forsythia* does not.

### BspA: TLR2 Agonist and Systemic Virulence

Glycosylated leucine-rich repeat protein mediating CD14/TLR2 activation (motif: GC(S/T)GLXSIT):
- Drives IL-6, IL-12 production in macrophages and dendritic cells
- Mediates epithelial invasion via PI3K activation
- Animal studies: BspA-deficient *T. forsythia* produces significantly less alveolar bone loss; bone loss linked to Th2 activation; absent in TLR2-knockout mice
- BspA genotype prevalence elevated in chronic and aggressive periodontitis
- Systemic: *T. forsythia* + BspA induce foam cell formation in THP-1 macrophages and atherosclerotic lesion progression in ApoE-knockout mice

### Outer Membrane Vesicles (OMVs)

OMVs carry O-glycosylated virulence factor cargo and elicit:
- IL-1β, TNF-α, IL-6, IL-8, MCP-1 in macrophages and PDL mesenchymal stromal cells (concentration-dependent)
- Responses comparable to or stronger than whole-bacterium infection
- TLR2-mediated; monocytes and differentiated macrophages phagocytose OMVs → pro-inflammatory activation

### LPS

Rough-type; concentration-dependent macrophage activation. Synergistic co-stimulation with *P. gingivalis* or *T. denticola* LPS markedly elevates IL-1β and TNF-α in whole blood from periodontitis patients.

## Cell-Type Response Summary

| Host Cell | Key Response | Mediators |
|---|---|---|
| Oral epithelial cells | Invasion (BspA, NanH); partial migration inhibition | IL-8, IL-24, IL-1α, IL-1Rα, VEGF |
| PMNs | Phagocytosis of non-opsonized bacteria; indirect inhibition via dental follicle MSCs | ROS; ↓ chemotaxis, phagocytosis, NET formation |
| Macrophages | Pro-inflammatory activation; apoptosis induction (caspase-1) | IL-1β, TNF-α, IL-6, IL-8, IL-23, MCP-1 |
| PDL/gingival MSCs | Cytokine induction | IL-6, IL-8, MCP-1 |

## *T. forsythia* vs. *P. gingivalis*: Comparative Virulence

| Dimension | *T. forsythia* | *P. gingivalis* |
|---|---|---|
| Keystone pathogen classification | Not established | Established |
| Cytokine protein degradation | Modest | High (gingipain "chemokine paralysis") |
| PMN direct inhibition | Not demonstrated in mouse subcutaneous model | Direct neutrophil migration block |
| Complement evasion | Karylisin (metalloproteinase) | Multiple strategies |
| Cathelicidin degradation | Mirolysin + karylisin | Gingipains |
| MurNAc dependency | Auxotrophic | Independent |
| Biofilm interaction | Inhibits *P. gingivalis* epithelial invasion; scavenges NOD-2 ligands | Synergistic bone loss (ligature model) |

## Biofilm Ecology

- *T. forsythia* scavenges NOD-2 ligands secreted by *P. gingivalis* → dampens NOD-2 activation of epithelial cells
- Inhibits *P. gingivalis* invasion of oral epithelial cells
- Co-infection (ligature model) synergistically augments alveolar bone loss
- Strain variation: clinical isolates differ substantially from ATCC 43037 in IP-10 activation of THP-1 macrophages; *BspA* and [unspecified] genotype prevalences higher in periodontitis patients vs. healthy

## Evidence Quality and Limitations

- Evidence level: **narrative review** — synthesizes existing primary literature, no new data
- Most primary studies are monoculture (single-species infection) or mouse models; subgingival plaque is polymicrobial — translation is challenged
- Limited *T. forsythia*-specific mouse periodontitis models; ligature models predominantly use *P. gingivalis*
- Strain-level virulence variation incompletely characterized
- Cannot yet establish *T. forsythia* as a dysbiosis-driving keystone pathogen

## Clinical Relevance

- Miropin and karylisin reduce PMN effectiveness → may contribute to sustained bacterial biomass in the sulcus
- BspA-TLR2 axis on bone loss: potential therapeutic target analogous to TLR2 antagonism studied for *P. gingivalis*
- BspA genotype screening could stratify periodontitis risk
- Systemic link (foam cells, atherosclerosis via BspA): consistent with periodontal-systemic disease connections documented for the red complex
- Fosfomycin resistance (MurNAc auxotrophy) is a practical antibiotic consideration
