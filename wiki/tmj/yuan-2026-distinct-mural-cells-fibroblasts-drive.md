---
title: "Cellular Basis of Retrodiscal Tissue Remodeling After Disc Displacement (Yuan 2026)"
authors: "Yuan W, Chen Y, Yan R, Liu W, Wang C, Wang Y, Dai Q, Li W, Zhu M, Chen X, Shi J"
year: 2026
date: 2026-02-10
doi: 10.1172/jci.insight.196343
pmcid: PMC13460816
pmid: 41665948
source: yuan-2026-distinct-mural-cells-fibroblasts-drive.md
source_collection: pubmed-text
full_text: true
text_path: /Users/oracleneo/llm-wiki/papers/yuan-2026-distinct-mural-cells-fibroblasts-drive.txt
text_filename: yuan-2026-distinct-mural-cells-fibroblasts-drive.txt
category: tmj
evidence_level: animal
tags: [TMJ, TMD, retrodiscal-tissue, bilaminar-zone, disc-displacement, adaptive-remodeling, fibrochondrogenesis, scRNA-seq, fibroblast, mural-cell, FGF2, BMP5, zaprinast, porcine-model]
relations:
  - target: tmj/sa-2024-conservative-invasive-tmd-disc-displacement-sr
    type: extends
    note: Provides the cellular/molecular mechanism (and a drug candidate) behind "promote retrodiscal adaptation without repositioning the disc" conservative strategy
  - target: tmj/kakimoto-2024-comparison-t2-values-displaced-unilateral
    type: reinforces
    note: Independently reproduces the bilateral (affected + contralateral) retrodiscal response that Kakimoto's T2 mapping shows in patients, and supplies its cellular basis
  - target: tmj/alfaro-2025-sensory-fiber-types-mouse-tmj
    type: extends
    note: Alfaro maps retrodisc innervation; Yuan maps the fibroblast/mural-cell remodeling program of the same tissue (neuronal paracrine input left as open question)
  - target: tmj/song-2023-understanding-tmj-osteoarthritis-pathophysiology
    type: refines
    note: Shows that adequate retrodiscal adaptation can shield the condyle from the osteoarthritic cascade — adaptation status conditions the degeneration outcome
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - **결론/thesis**: 전방 원판 변위 (anterior disc displacement, ADD) 후 후방조직 (retrodiscal tissue, 이중판대 (bilaminar zone))이 하중을 견디는 섬유연골로 바뀌는 "적응성 재형성 (adaptive remodeling)"의 세포 기전을 돼지 단일세포 RNA 시퀀싱 (scRNA-seq)으로 처음 규명 — 섬유아세포 활성화가 핵심이고, 새로 출현하는 벽세포 (mural cell) 아군집 MC4가 이를 구동한다.
> - **양측성 반응**: ADD측뿐 아니라 수술하지 않은 반대측 (CADD)에서도 재형성이 일어났고, ECM 재구성 유전자 신호는 오히려 반대측이 더 강했다 — 임상에서 양측 관절을 함께 봐야 하는 근거.
> - **FB2 = 반응성 전구 섬유아세포**: EFEMP1·APOE 신호, 발생 잠재력 높음; ECM 생산형(FB1·FB3)과 조절형(FB4~6)으로 분화. FB3가 섬유연골 (fibrocartilage) 표현형.
> - **MC4 = 손상 유도 ECM 재형성 벽세포**: 정상 후방조직엔 거의 없음 → ADD 후 혈관주위세포 (pericyte, MC2)에서 유래해 출현; ADD 후 최대 신호 허브.
> - **핵심 축 = MC4 → FB2, FGF2–FGFR1 + BMP5–BMPR1A/BMPR2**: ERK1/2 조기(~6h) → SMAD1/5/9 후기(~24h) 순차 활성 → 증식 → ECM 침착 → 섬유연골화. TGF-β가 벽세포를 MC4로 전환.
> - **경로 신호 (ADD/CADD 후방조직 특이)**: PERIOSTIN·FGF·BMP·TWEAK·SPP1·IL6 상승(섬유화형), PDGF·VISFATIN 하강.
> - **약물 후보 zaprinast** (PDE5 억제제 / GPR35 작용제): P-NET + Seurat + ConnectivityMap 스크리닝으로 도출; 시험관 내 섬유아세포 ECM·연골분화 촉진(ERK1/2 + SMAD1/5/9 경유), 랫드 ADD 모델에서 원판·후방조직 콜라겐 정렬 개선 + 과두 연골기질·연골하골 소실 완화. **원판 재위치가 아니라 조직 적응을 강화**하는 방식의 보존적 약물치료 개념.
> - **임상 takeaway**: 비정복성 ADD의 자연경과가 대개 호전되는 이유가 후방조직의 섬유연골 적응이며, 이를 촉진하는 것이 disc를 되돌리지 못해도 치료가 될 수 있다. 단 이는 조기(5주) 소견 — 부적응성 섬유화(강직·통증)로 갈 수도 있어 장기 추적 필요.
> - **한계**: 극소 표본(scRNA-seq용 돼지 4마리), 암컷만, 인간 조직 검증 없음, 수술 유도 ADD, 랫드는 섬유연골화 재현 안 됨, zaprinast 용량·국소전달 미최적화.

## Three-line Summary

Porcine unilateral anterior disc displacement (ADD) model (Ni-Ti-spring elastic traction; 2 sham + 2 ADD pigs; single-cell RNA-seq of disc and retrodiscal tissue at 5 weeks; separate rat ADD model for drug testing) resolving the cellular basis of retrodiscal adaptive remodeling — the histologically known but mechanistically opaque conversion of loose connective tissue into load-bearing fibrocartilage. Both the ADD side and the untreated contralateral side remodeled (dense connective tissue + Alcian-blue+ cartilaginous masses replacing loose tissue and fat); a progenitor-like fibroblast subcluster (FB2) expanded and a new ECM-remodeling mural-cell subcluster (MC4, pericyte-derived) emerged, with MC4→FB2 paracrine FGF2 and BMP5 signaling driving fibrosis and chondrogenesis via sequential ERK1/2 then SMAD1/5/9 activation. Computational drug screening nominated zaprinast (PDE5 inhibitor / GPR35 agonist), which enhanced fibroblast ECM synthesis and chondrogenesis in vitro and reduced disc/retrodiscal deformation plus condylar cartilage and subchondral-bone loss in the rat ADD model — a conservative pharmacotherapy concept that promotes tissue adaptation rather than repositioning the disc.

## 세줄요약

돼지 편측 전방 원판 변위 (anterior disc displacement, ADD) 모델(Ni-Ti 스프링 탄성 견인; 대조 2 + ADD 2마리; 5주째 원판·후방조직 단일세포 RNA 시퀀싱 (scRNA-seq); 약물 검증용 랫드 ADD 모델 별도)로, 조직학적으로만 알려졌던 후방조직 (retrodiscal tissue) 적응성 재형성 — 성긴 결합조직이 하중을 견디는 섬유연골로 전환 — 의 세포 기전을 규명했다. ADD측·반대측(무처치) 모두에서 성긴 조직·지방이 치밀 결합조직과 Alcian blue 양성 연골성 덩어리로 대체되었고, 전구세포 유사 섬유아세포 아군집 FB2가 증식하고 혈관주위세포 유래 ECM 재형성 벽세포 아군집 MC4가 출현하여, MC4→FB2 방향의 FGF2·BMP5 곁분비 신호가 ERK1/2에 이어 SMAD1/5/9를 순차 활성화해 섬유화·연골화를 구동했다. 계산적 약물 스크리닝으로 zaprinast(PDE5 억제제 / GPR35 작용제)를 도출했고, 시험관 내에서 섬유아세포 ECM 합성·연골분화를 촉진하며 랫드 ADD 모델에서 원판·후방조직 변형과 과두 연골·연골하골 소실을 줄여 — 원판을 되돌리는 대신 조직 적응을 촉진하는 보존적 약물치료 개념을 제시한다.

## Summary

For decades, MRI and histology have shown that in long-standing anterior disc displacement without reduction the retrodiscal tissue can transform into a "pseudo-disc" — dense fibrous tissue with scattered chondrocytes and increased glycosaminoglycan — that lets patients regain function even though the disc is never recaptured. This paper is the first cellular-resolution account of how that transformation happens.

Using a porcine unilateral ADD model and single-cell RNA sequencing of disc and retrodiscal tissue, the authors show that the retrodisc (not the disc) is the mechanically responsive compartment: fibroblasts expand markedly after ADD, led by a progenitor-like subcluster (FB2, EFEMP1/APOE signature) that feeds both matrix-producing and matrix-modulating fibroblast fates, with one subcluster (FB3) acquiring a fibrocartilage signature. In parallel, a mural-cell subcluster absent from healthy retrodiscal tissue — MC4, arising from pericytes and carrying an ECM-remodeling signature — emerges after ADD and becomes the dominant signaling hub. MC4 signals to fibroblasts through FGF2 and BMP5, activating ERK1/2 early and SMAD1/5/9 later, together driving proliferation, matrix deposition, and fibrocartilage formation. TGF-β pushes mural cells toward the MC4 phenotype. Both the loaded side and the untreated contralateral side remodel, matching the bilateral biochemical signal seen on patient T2 mapping.

Feeding the fibroblast expression data into a combined deep-learning (P-NET) and differential-expression (Seurat) pipeline against drug databases, the authors nominated five compounds and validated zaprinast — a PDE5 inhibitor / GPR35 agonist — as an enhancer of fibroblast matrix synthesis and chondrogenesis through the same ERK1/2 + SMAD1/5/9 axis. In a rat ADD model, systemic zaprinast improved collagen organization in the posterior band and retrodiscal tissue and partly protected condylar cartilage matrix and subchondral bone. The therapeutic framing is deliberately unconventional: rather than trying to reposition the disc, boost the tissue's own adaptive response.

## Key Contributions

1. **First single-cell atlas of porcine TMJ disc vs retrodiscal tissue** (sham, ADD side, contralateral side) — 5 principal cell types; porcine disc is substantially vascularized, unlike rodent disc.
2. **Retrodiscal tissue is the adaptive compartment** — fibroblast proportion jumps after ADD while the disc barely changes.
3. **FB2 progenitor fibroblast** (EFEMP1, APOE; top pseudotime potential) expands after ADD and gives rise to ECM-producing (FB1, FB3) and modulatory (FB4–6) fibroblasts; FB3 = fibrocartilage signature.
4. **MC4, a pericyte-derived ECM-remodeling mural-cell subcluster**, is nearly absent in healthy retrodiscal tissue and emerges after ADD as the dominant cell–cell signaling hub.
5. **MC4→fibroblast axis = FGF2–FGFR1 + BMP5–BMPR1A/BMPR2**, mechanistically sequential ERK1/2 (~6 h) → SMAD1/5/9 (~24 h); FGF2 + BMP5 act synergistically on fibroblast ECM + chondrogenesis in vitro.
6. **Bilateral remodeling** — contralateral (CADD) retrodiscal tissue remodels too, with even stronger ECM-reorganization gene signatures than the loaded side.
7. **Zaprinast** nominated by P-NET + Seurat + ConnectivityMap/DGIdb and validated in vitro and in a rat ADD model (improved disc/retrodiscal collagen organization; partial condylar cartilage and subchondral-bone protection).
8. **Conservative-therapy reframing** — pharmacologically enhancing retrodiscal adaptation is presented as therapeutic even without resolving displacement.

## Methodology

- **Porcine UADD**: 4 female Bama minipigs (5 mo); 2 sham, 2 ADD. ADD surgery released anterior + lateral disc attachments while **preserving the posterior attachment**; zygomatic mini-implant + Ni-Ti spring (extended 4→14 mm ≈ 1 N anterior traction) + anti-osseointegration e-PTFE membrane; nylon suture through anterior disc attachment. Contralateral untreated joint = CADD. Endpoint 5 weeks.
- **scRNA-seq**: disc intermediate zone + retrodiscal tissue near posterior band; 10x Chromium 3′ v3; Seurat v4 (CCA integration), CellChat v1.5.0, Monocle v2.30.1 + CytoTRACE.
- **Histology**: H&E, Alcian blue, safranin O / fast green; modified Mankin score.
- **Primary cells**: porcine retrodiscal fibroblasts and mural cells (pericyte-enrichment medium), passage 3; TGF-β3 on mural cells; batimastat / sunitinib / zaprinast on fibroblasts; chondrogenic pellet culture 3 wk.
- **Drug discovery**: P-NET (Reactome-node deep learning + DeepLIFT) + Seurat DEGs → ConnectivityMap + DGIdb → 5 candidates; CCK-8 → working doses 10 nM batimastat, 1 nM sunitinib, 1 µM zaprinast.
- **Rat ADD**: 18 female SD rats (10 wk); Sham+Vehicle / ADD+Vehicle / ADD+Zaprinast (n=6). Zaprinast 10 mg/kg i.p., 9 doses over 4 weeks. Micro-CT (13 µm) for BV/TV, Tb.Th, Tb.Sp, Tb.N.
- **Statistics**: t-test; 1-way ANOVA + Tukey or Kruskal-Wallis + Dunn; p < 0.05. Female animals only.

## Results

### Histology and cell-proportion changes after ADD

| Feature | Sham retrodiscal tissue | ADD / CADD retrodiscal tissue |
|---|---|---|
| Connective tissue | loose, irregular, interspersed adipose | partly replaced by dense connective tissue + fibroblast proliferation |
| Alcian blue (GAG) | almost none | cartilaginous masses appear |
| Dominant cell shift | — | fibroblasts markedly increased |
| Condyle (5 wk, pig) | normal | no overt degeneration |
| Disc | anteroposterior fiber alignment, GAG+ | small inter-fiber fissures, slightly ↓ GAG (both sides) |

### Signaling (CellChat, retrodiscal tissue)

| Direction | Pathways |
|---|---|
| Exclusively active in ADD + CADD | MK, PERIOSTIN, FGF, BMP, TWEAK, SPP1, IL6, MIF (pro-fibrotic) |
| Decreased after ADD | GAS, PDGF, VISFATIN |
| Dominant hub post-ADD | MC4 (was FB1/FB3 in sham) |
| Key ligand–receptor, MC4→FB | FGF2–FGFR1; BMP5–BMPR1A + BMPR2 |

### Zaprinast

- In vitro: highest chondrogenic-marker expression vs batimastat/sunitinib; ↑COL1A1, ↑APOE (FB2-like remodeling capacity); ↑SOX9/ACAN/COL2A1 in pellet culture; blocked by loss of ERK1/2 + SMAD1/5/9 signaling.
- Rat ADD model vs vehicle: improved collagen orientation/organization in posterior band + retrodiscal tissue; less inflammatory infiltrate; reduced condylar flattening; mitigated cartilage-matrix loss (safranin O); partial recovery of BV/TV, trabecular number, trabecular spacing. No fibrocartilage formed in rat (species difference); no perforations in any group.

## Related Papers

- [[tmj/sa-2024-conservative-invasive-tmd-disc-displacement-sr]] — conservative vs invasive disc-displacement treatment SR; Yuan gives the mechanism and a drug candidate for the "promote adaptation, don't reposition the disc" strategy
- [[tmj/kakimoto-2024-comparison-t2-values-displaced-unilateral]] — patient T2 mapping showing bilateral retrodiscal change; Yuan independently reproduces the bilateral response and explains it cellularly
- [[tmj/alfaro-2025-sensory-fiber-types-mouse-tmj]] — retrodisc innervation map; Yuan adds the fibroblast/mural-cell remodeling program and flags neuronal paracrine input as unexplored
- [[tmj/song-2023-understanding-tmj-osteoarthritis-pathophysiology]] — TMJ osteoarthritis pathophysiology; adequate retrodiscal adaptation is shown to shield the condyle from that cascade
- [[tmj/al-hamed-2026-pharmacological-intraarticular-tmd-nma]] — NMA of intra-articular TMD pharmacotherapy; zaprinast is a mechanistically distinct candidate aimed at tissue adaptation rather than inflammation
