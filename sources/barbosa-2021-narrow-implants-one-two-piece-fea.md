---
title: "Comparative analysis of stress distribution in one-piece and two-piece implants with narrow and extra-narrow diameters: A finite element study"
authors: Fabricia Teixeira Barbosa, Luiz Carlos Silveira Zanatta, Edelcio de Souza Rendohl, Sergio Alexandre Gehrke
year: 2021
doi: 10.1371/journal.pone.0245800
category: [implants]
pdf_path: /Users/oracleneo/llm-wiki/papers/barbosa-2021-narrow-implants-one-two-piece-fea.pdf
pdf_filename: barbosa-2021-narrow-implants-one-two-piece-fea.pdf
source_collection: external
---

## Why Ingested

Narrow- and extra-narrow-diameter implants are frequently selected for anatomically restricted sites; their biomechanical safety — especially in one-piece vs. two-piece configurations — has direct clinical implications. This FEA study fills a gap complementing [[wiki/implants/cao-2023-titanium-zirconium-narrow-diameter-single-crown]] (clinical narrow-implant outcomes) with a stress-distribution analysis across three diameters and two implant-body designs under axial and angled loading.

## One-line Summary

FEA of three narrow/extra-narrow implant models (2.5 mm one-piece, 3.0 mm one-piece, 3.5 mm two-piece Morse taper) under 150 N axial and 30° angled loads shows the 2.5 mm extra-narrow one-piece implant exceeds titanium yield strength under angled loading, while 3.0 mm one-piece and 3.5 mm two-piece designs remain within safe stress limits.

## 한줄요약

FEA 연구(n=3 모델): 2.5 mm 초소경 one-piece 임플란트는 경사하중 시 티타늄 항복강도(1130 MPa)를 93.6% 초과해 위험하고, 3.0 mm one-piece 및 3.5 mm Morse taper two-piece는 축방향·경사 하중 모두에서 안전한 응력 분포를 보임.

## 1. Document Information

- **Journal**: PLOS ONE 16(2): e0245800
- **Published**: February 4, 2021
- **Study type**: In vitro finite element analysis (FEA)
- **Country**: Brazil / Spain / Uruguay

## 2. Key Contributions

- Quantified von Mises stress in three narrow-implant configurations under axial (0°) and angled (30°) 150 N loads
- Demonstrated that the 2.5 mm extra-narrow one-piece implant (G1) exceeds titanium yield limits under angled load (2188 MPa vs. 1130 MPa limit = 93.6% excess)
- Showed the two-piece Morse taper implant (G3) concentrates stress at the internal cone rather than the cortical bone, distributing load more favorably
- Used both von Mises criterion (implant structure) and Mohr-Coulomb analysis (peri-implant bone) for comprehensive stress evaluation

## 3. Methodology and Architecture

**Groups**:
- G1: 2.5 mm extra-narrow one-piece implant (Implacil De Bortoli)
- G2: 3.0 mm narrow one-piece implant
- G3: 3.5 mm narrow two-piece implant with Morse taper connection

**FEA setup**:
- All implants 9.0 mm length; 3D models built in Rhinoceros 5.4.1
- Analyzed in Ansys Workbench 19.0
- Bone model: 1.0 mm cortical bone + cancellous bone; crown modeled as maxillary lateral incisor in feldspathic porcelain
- Materials: isotropic, homogeneous, linearly elastic (except G3 Morse taper: non-linear frictional contact, μ=0.8)
- Mesh elements: 432,020–887,245; nodes: 753,005–1,398,103
- Load: 150 N axial and 30° angled
- Stress limits: titanium 1130 MPa (100%); cortical bone 114 MPa axial / 50 MPa angled

## 4. Key Results and Benchmarks

**Implant structure (von Mises)**:
- G1 axial: 224.26 MPa; G2 axial: 169.2 MPa; G3 axial: 1593.3 MPa (at Morse cone, below limit)
- G1 angled: 2188 MPa — **93.6% ABOVE titanium yield limit** (fracture risk)
- G2 and G3 angled: within safe limits

**Cortical bone (axial)**:
- G1 cortical stress 22.35% higher than G2; 321.23% higher than G3
- G3 shows markedly lower cortical bone stress due to Morse taper stress absorption

**Cortical bone (angled)**:
- G1 and G2 similar values (≤3.5% difference)
- G3 391.8% higher than G1/G2 under angled loading (stress redirection to cone rather than bone is reversed under angled forces)

**Cancellous bone**: All groups low (3–12 MPa), well within limits

**Mohr-Coulomb (bone)**: Confirmed von Mises findings; no bone failure predicted for any group

## 5. Limitations and Future Work

- FEA models assume ideal osseointegration (bonded contact between implant and bone) — does not reflect healing phase or partial integration
- All materials assumed isotropic/homogeneous; real bone is anisotropic
- Single implant-crown design (upper lateral incisor) — results may differ for posterior regions with higher masticatory forces
- No fatigue or cyclic loading analysis (single static load only)
- Clinical validation in long-term prospective studies needed

## 6. Related Work

- Referenced Hussein et al. 2019 (thread depth/shape FEA), Geng et al. (material properties), Álvarez et al. (crown/bone material properties)
- Consistent with prior literature showing one-piece narrow implants have higher stress concentration than two-piece designs with internal connections

## 7. Glossary

- **FEA (Finite Element Analysis)**: Computational method dividing a complex structure into discrete elements to calculate stress distribution
- **von Mises stress**: Equivalent stress criterion used for ductile materials (titanium); always positive, facilitating comparison
- **Mohr-Coulomb criterion**: Failure theory for brittle materials (bone); differentiates tension vs. compression stress
- **Morse taper connection**: Internal conical implant-abutment connection providing friction-based locking and stress distribution
- **Extra-narrow implant**: Diameter ≤2.5 mm
- **Narrow-diameter implant**: Diameter 3.0–3.5 mm
