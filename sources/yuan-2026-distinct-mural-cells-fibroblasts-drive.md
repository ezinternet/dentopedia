---
title: "Distinct mural cells and fibroblasts drive fibrochondrogenesis in retrodiscal tissue following temporomandibular joint disc displacement"
authors: "Yuan W, Chen Y, Yan R, Liu W, Wang C, Wang Y, Dai Q, Li W, Zhu M, Chen X, Shi J"
year: 2026
doi: 10.1172/jci.insight.196343
pmcid: PMC13460816
pmid: 41665948
source_collection: pubmed-text
full_text: true
text_path: /Users/oracleneo/llm-wiki/papers/yuan-2026-distinct-mural-cells-fibroblasts-drive.txt
text_filename: yuan-2026-distinct-mural-cells-fibroblasts-drive.txt
category: tmj
evidence_level: animal
---

## Why Ingested

Adaptive remodeling of the bilaminar zone / retrodiscal tissue after anterior disc displacement has been described histologically for decades ("pseudo-disc" formation) but never at cellular/molecular resolution. This porcine single-cell RNA-seq study is the first mechanistic account of *how* loose retrodiscal connective tissue converts to load-bearing fibrocartilage, and it converts the "adaptation" concept underlying conservative disc-displacement management ([[wiki/tmj/sa-2024-conservative-invasive-tmd-disc-displacement-sr]]) from a black box into a targetable pathway. It complements the innervation map in [[wiki/tmj/alfaro-2025-sensory-fiber-types-mouse-tmj]] and the in-vivo T2 degeneration signal in [[wiki/tmj/kakimoto-2024-comparison-t2-values-displaced-unilateral]], and it independently reproduces the bilateral (affected + contralateral) retrodiscal response those imaging data show.

## Three-line Summary

Porcine unilateral anterior disc displacement (ADD) model (titanium-spring elastic traction, 2 sham + 2 ADD pigs, scRNA-seq of disc and retrodiscal tissue at 5 weeks; rat ADD model for drug testing) mapping the cellular basis of retrodiscal adaptive remodeling. Both the ADD side and the contralateral side underwent remodeling (loose connective tissue + fat replaced by dense connective tissue and Alcian-blue+ cartilaginous masses); a developmentally potent fibroblast subcluster (FB2) expanded and a new extracellular-matrix-related mural-cell subcluster (MC4, arising from pericytes) emerged, with MC4→FB2 crosstalk via FGF2–FGFR1 and BMP5–BMPR1A/BMPR2 signaling driving fibrosis and chondrogenesis through sequential ERK1/2 then SMAD1/5/9 activation. Drug screening (P-NET + Seurat + ConnectivityMap/DGIdb) nominated zaprinast (PDE5 inhibitor / GPR35 agonist), which enhanced fibroblast ECM synthesis and chondrogenesis in vitro and reduced disc/retrodiscal deformation and condylar cartilage/bone loss in the rat ADD model — a candidate conservative pharmacotherapy that works by boosting adaptation rather than repositioning the disc.

## 세줄요약

돼지 편측 전방 원판 변위 (anterior disc displacement, ADD) 모델(티타늄 스프링 탄성 견인, 대조 2 + ADD 2마리, 5주째 원판·후방조직 단일세포 RNA 시퀀싱 (scRNA-seq); 약물 검증은 랫드 ADD 모델)로 후방조직 (retrodiscal tissue) 적응성 재형성 (adaptive remodeling)의 세포 기전을 규명했다. ADD측·반대측 모두에서 성긴 결합조직과 지방이 치밀 결합조직 및 Alcian blue 양성 연골성 덩어리로 대체되었고, 발생 잠재력이 높은 섬유아세포 (fibroblast) 아군집 FB2가 증식하고 혈관주위세포 (pericyte)에서 유래한 새로운 세포외기질 (ECM) 관련 벽세포 (mural cell) 아군집 MC4가 출현하여 — MC4→FB2 간 FGF2–FGFR1·BMP5–BMPR1A/BMPR2 신호가 ERK1/2에 이어 SMAD1/5/9를 순차 활성화해 섬유화·연골화를 유도했다. 약물 스크리닝(P-NET + Seurat + ConnectivityMap/DGIdb)으로 zaprinast(PDE5 억제제 / GPR35 작용제)를 도출했고, 시험관 내에서 섬유아세포 ECM 합성·연골분화를 촉진하고 랫드 ADD 모델에서 원판·후방조직 변형과 과두 연골·골 소실을 감소시켰다 — 원판을 재위치시키는 대신 적응을 강화하는 방식의 보존적 약물치료 후보.

## 1. Document Information

- **Journal**: JCI Insight, vol 11, issue 13 (published 2026-02-10)
- **DOI**: 10.1172/jci.insight.196343 | **PMID**: 41665948 | **PMCID**: PMC13460816
- **Institution**: Stomatology Hospital, School of Stomatology, Zhejiang University School of Medicine (Hangzhou, China); Dr. Li Dak Sum & Yip Yio Chin Center for Stem Cells and Regenerative Medicine; Liangzhu Laboratory
- **Ethics**: Animal Ethics Committee of Zhejiang Chinese Medical University (approval 20230227-08)
- **Study design**: Experimental animal study (porcine + rat) with scRNA-seq, in-vitro primary-cell functional assays, and in-vivo drug intervention
- **Sex-as-biological-variable**: female animals only (5-month-old female Bama miniature pigs; 10-week-old female Sprague-Dawley rats), rationale = higher TMD incidence in young women
- **Data**: sequencing deposited in Genome Sequence Archive, accession CRA034150

## 2. Key Contributions

1. **First single-cell transcriptomic atlas of porcine TMJ disc vs retrodiscal tissue** in health and after ADD — 7 clusters / 5 principal cell types (endothelial, fibroblast, mural, immune, cycling).
2. **Bilateral retrodiscal remodeling** — both the ADD side and the untreated contralateral side (CADD) remodeled; the contralateral side showed *superior* ECM-reorganization gene signatures.
3. **FB2 as the responsive progenitor fibroblast** — cholesterol-metabolism / ECM-integrity signature (EFEMP1, APOE), high developmental potential by pseudotime; differentiates into ECM-producing (FB1, FB3) and modulatory (FB4–6) fibroblasts. FB3 carries the fibrocartilage signature (COL2A1/ACAN-type genes).
4. **MC4 — a new ECM-remodeling mural-cell (smooth-muscle-like) subcluster** essentially absent in sham retrodiscal tissue, emerging after ADD, derived from pericytes (MC2), and acting as the dominant signaling hub post-ADD.
5. **MC4→fibroblast paracrine axis = FGF2 + BMP5**, receptor pairs FGF2–FGFR1 and BMP5–BMPR1A+BMPR2; mechanism = early ERK1/2 activation (~6 h) then SMAD1/5/9 (~24 h) driving proliferation → ECM deposition → fibrocartilage.
6. **TGF-β drives mural cells toward the MC4 phenotype** in vitro (↑FN1, COL1A1, DCN, ACTA2; ↑FGF2, BMP5); MC4-conditioned medium enhances fibroblast ECM + chondrogenic markers.
7. **Zaprinast identified and validated** as a compound enhancing fibroblast remodeling capacity (↑COL1A1, APOE; ↑SOX9/ACAN/COL2A1 under chondrogenic induction) via ERK1/2 + SMAD1/5/9; in the rat ADD model it improved disc/retrodiscal collagen organization and partly preserved condylar cartilage matrix and subchondral bone (↑BV/TV, trabecular number; ↓trabecular spacing).
8. **Reframes conservative ADD therapy** — pharmacologically promoting retrodiscal adaptation can be therapeutic even without resolving the displacement.

## 3. Methodology and Architecture

- **Porcine UADD model**: 4 female Bama minipigs (5 mo). 2 sham (left TMJ opened, disc untouched), 2 ADD (left TMJ; anterior + lateral attachments partially released, **posterior attachment preserved**; orthodontic mini-implant in zygomatic arch + Ni-Ti spring + Ti-reinforced e-PTFE anti-osseointegration membrane; 4-0 nylon through anterior disc attachment; spring extended 4→14 mm = 1 N anterior traction). Contralateral right TMJ = CADD (untreated). Euthanized at 5 weeks; ADD confirmed grossly.
- **scRNA-seq**: disc intermediate zone + retrodiscal tissue near posterior band, 5×5×5 mm; Pronase + collagenase P digestion; 10x Chromium 3′ v3; Illumina HiSeq. Seurat v4 (CCA integration, top 15 PCs), Metascape GO, CellChat v1.5.0, Monocle v2.30.1 + CytoTRACE trajectory.
- **Histology**: H&E, Alcian blue, safranin O / fast green; modified Mankin score; condyle decalcified 0.5 M EDTA ×3 mo.
- **Primary cells**: porcine retrodiscal fibroblasts (4-h adherence enrichment) and mural cells (non-adherent fraction, low-glucose/low-FBS pericyte medium); passage 3. MCs treated with TGF-β3; FBs with batimastat / sunitinib / zaprinast. Chondrogenic induction (dexamethasone, ascorbate, proline, ITS, TGF-β3), pellet culture 3 wk.
- **Drug discovery**: P-NET (pathway-aware deep learning, Reactome nodes, DeepLIFT importance) + Seurat DEGs → top 150 up/down DEGs → ConnectivityMap + DGIdb → 5 candidates; batimastat, sunitinib, zaprinast tested (CCK-8 cytotoxicity → 10 nM batimastat, 1 nM sunitinib, 1 µM zaprinast).
- **Rat ADD model**: 18 female Sprague-Dawley rats (10 wk), 3 groups (Sham+Vehicle, ADD+Vehicle, ADD+Zaprinast n=6 each). Zaprinast 10 mg/kg i.p. on day −1 and days 1,3,5,7,10,14,21,28. Micro-CT (SkyScan1276, 60 kV, 13 µm) for BV/TV, Tb.Th, Tb.Sp, Tb.N.
- **Statistics**: unpaired 2-tailed t-test; 1-way ANOVA + Tukey or Kruskal-Wallis + Dunn; p < 0.05.

## 4. Key Results and Benchmarks

- **Histology after ADD (both sides)**: retrodiscal loose connective tissue + adipose → dense connective tissue + fibroblast proliferation + Alcian-blue+ cartilaginous masses. Disc: small inter-fiber fissures, slightly reduced GAG. **Condyle showed no overt degeneration** at 5 weeks in the pig.
- **Cell-proportion shift**: disc barely changed; retrodiscal tissue showed marked fibroblast increase — "highly adaptive and sensitive to mechanical stress."
- **FB2**: similar disc/retrodiscal proportion in sham → substantial retrodiscal increase in ADD and CADD; APOE+ cells ↑ and more proliferative in ADD/CADD retrodiscal tissue (immunofluorescence confirmed).
- **MC4**: nearly absent in sham retrodiscal tissue → present in ADD and CADD (immunofluorescence confirmed); pseudotime: pericyte (MC2) → MC4 → typical SMC (MC1) / immune SMC (MC3).
- **CellChat**: pathways exclusively active in ADD/CADD retrodiscal tissue = MK, PERIOSTIN, FGF, BMP, TWEAK, SPP1, IL6, MIF (pro-fibrotic); decreased = GAS, PDGF, VISFATIN. MC4 = dominant post-ADD signaling hub.
- **Signaling detail**: MC4→FB, FGF2–FGFR1 (FGF) and BMP5–BMPR1A+BMPR2 (BMP) top contributors; FGF2 and BMP5 immunofluorescence ↑ in mural cells of ADD/CADD retrodiscal tissue; in vitro FGF2 + BMP5 synergistically ↑ fibroblast ECM + chondrogenesis; ERK1/2 at ~6 h, SMAD1/5/9 at ~24 h.
- **P-NET top genes**: CST3 (cystatin C — pro-fibrotic), FGL2, B2M (ADD + CADD); CADD additionally collagen-formation / ECM-organization genes (consistent with superior CADD remodeling).
- **Compound testing**: sunitinib cytotoxic even at 1 nM; batimastat minimal ECM effect; **zaprinast** highest chondrogenic-marker expression, ↑COL1A1 + APOE, ↑SOX9/ACAN/COL2A1 in pellet culture, via ERK1/2 + SMAD1/5/9.
- **Rat in vivo (zaprinast vs vehicle after ADD)**: improved collagen orientation/organization in posterior band + retrodiscal tissue; less inflammatory infiltrate; mitigated condylar cartilage-matrix loss (safranin O), reduced condylar flattening; partially restored BV/TV, trabecular number, trabecular spacing. **No fibrocartilage formation seen in the rat** (species difference); no perforations/tears in any group.

## 5. Limitations and Future Work

- Very small animal n (2 sham + 2 ADD pigs for scRNA-seq); female animals only (authors argue mechanism likely sex-independent but not tested).
- Porcine surrogate for early human ADD tissue (chosen for anatomical/physiological similarity); no human-tissue or human-cell validation — flagged by authors as essential next step.
- Surgical (not naturally occurring) ADD; 5-week endpoint = early adaptation only; long-term trajectory (beneficial adaptation vs maladaptive fibrosis/stiffness/pain) unknown.
- Rat model does not reproduce fibrocartilage metaplasia, limiting the in-vivo drug readout to organization/degeneration measures.
- Tissue-dissociation bias may under-represent adipocytes; single-nucleus RNA-seq suggested for follow-up.
- Zaprinast dose/route (10 mg/kg i.p., frequent dosing) not yet optimized or tested for TMJ-local delivery; off-target PDE5/GPR35 effects not characterized in this context.
- Neuronal paracrine contribution to remodeling not examined.

## 6. Related Work

- [[wiki/tmj/alfaro-2025-sensory-fiber-types-mouse-tmj]] — innervation of the retrodisc; Yuan adds the fibroblast/mural-cell remodeling program of the same tissue (authors note neuronal paracrine signaling as unexplored)
- [[wiki/tmj/kakimoto-2024-comparison-t2-values-displaced-unilateral]] — in-vivo T2 evidence of bilateral retrodiscal change in patients; Yuan independently reproduces the bilateral (ADD + contralateral) response and gives its cellular basis
- [[wiki/tmj/sa-2024-conservative-invasive-tmd-disc-displacement-sr]] — conservative vs invasive disc-displacement treatment SR; Yuan supplies a mechanistic rationale (and a drug candidate) for the "promote adaptation without repositioning the disc" strategy
- [[wiki/tmj/song-2023-understanding-tmj-osteoarthritis-pathophysiology]] — TMJ osteoarthritis pathophysiology; Yuan shows retrodiscal adaptation can protect the condyle from the degenerative cascade
- [[wiki/tmj/al-hamed-2026-pharmacological-intraarticular-tmd-nma]] — network meta-analysis of intra-articular TMD pharmacotherapy; Yuan proposes a mechanistically distinct oral/systemic candidate (zaprinast) targeting tissue adaptation rather than inflammation

## 7. Glossary

- **Retrodiscal tissue / bilaminar zone**: loosely organized, highly vascular, innervated connective tissue posterior to the articular disc; after ADD, part of it bears abnormal load between condyle and fossa
- **Adaptive remodeling / "pseudo-disc"**: conversion of loose retrodiscal connective tissue to dense connective tissue or fibrocartilage capable of load bearing; historically seen in ~45% of long-standing ADDWOR
- **ADD / CADD**: anterior disc displacement (surgically induced side) / contralateral untreated side in the unilateral model
- **scRNA-seq**: single-cell RNA sequencing — transcriptome of individual cells, resolving subpopulations invisible to bulk assays
- **FB2**: fibroblast subcluster with progenitor-like signature (EFEMP1, APOE), expanding after ADD; upstream of ECM-producing and modulatory fibroblasts
- **Mural cells**: cells wrapping vascular endothelium — smooth-muscle cells and pericytes; stabilize vessels, and here contribute to fibrosis
- **MC4**: ADD-induced ECM-remodeling mural-cell subcluster derived from pericytes; principal source of FGF2 and BMP5 to fibroblasts
- **FGF2 / BMP5**: fibroblast growth factor 2 / bone morphogenetic protein 5 — paracrine ligands from MC4; activate ERK1/2 and SMAD1/5/9 respectively
- **ERK1/2, SMAD1/5/9**: intracellular kinase / transcription-factor cascades; sequential activation drives fibroblast proliferation then ECM reorganization and fibrocartilage formation
- **Zaprinast**: phosphodiesterase-5 (PDE5) inhibitor and GPR35 agonist; here repurposed as an enhancer of retrodiscal fibrocartilage adaptation
- **P-NET**: pathway-aware multilayered hierarchical (deep-learning) network that maps genes onto Reactome pathway nodes for interpretable target prediction
- **BV/TV, Tb.N, Tb.Sp**: bone volume fraction, trabecular number, trabecular separation — micro-CT subchondral-bone metrics
