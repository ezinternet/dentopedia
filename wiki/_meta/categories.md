# Category Map — llm-wiki (치과학)

이 파일은 `wiki/{category}/` 라우팅의 단일 출처(single source of truth)다 — 아래 라우팅 원칙 5단계·전체 카테고리 목록·서브카테고리 분기 규칙을 전부 여기서 관리한다. **CLAUDE.md는 이 파일로의 포인터만 갖고 원칙·목록 어느 쪽도 복제하지 않는다** — 두 곳에 두면 반드시 drift한다 (2026-07-15엔 카테고리 목록이 CLAUDE.md 트리와 어긋나 있었고, 2026-07-20엔 라우팅 원칙 4단계 예시 목록도 두 파일에서 갈라져 있었던 걸 확인·정리).

**라우팅 원칙**
1. 신규 paper는 먼저 `qmd query`로 유사 페이지를 찾아 그 페이지의 `category`를 따른다.
2. 유사 페이지가 없거나 새 주제면 아래 표에서 가장 가까운 folder를 고른다.
3. 분류 기준은 **method/procedure**이지 disease·anatomy가 아니다.
4. 서브카테고리 분기(예: `implants/surface/plasma`, `immediate-implant/socket-shield`, `endodontics/cold-plasma`)는 표의 `Includes` 열 괄호 안 라우팅 지시(`→ ...`)를 따른다.
5. 어느 folder에도 안 맞으면 신규 카테고리 후보 — CLAUDE.md의 판단 없이 임의 신설하지 말고 이 파일에 항목을 추가하며 신설한다.

**정렬 규약 (2026-07-15~)**: 부모 카테고리별로 그룹핑하고, 각 그룹 안에서 general parent → 서브카테고리 순. 신규 카테고리는 append하지 말고 **해당 부모 그룹에 삽입**한다 (그래야 라우팅 스캔 비용이 낮게 유지된다).

---

## Categories

### 임플란트 (implants)

| Category folder | Korean | Includes |
|---|---|---|
| `implants` | 임플란트 | Implant macrogeometry/thread & design, osseointegration biology, abutment & connection, bone quality/density, FEA stress analysis, failure risk factors & systemic-condition effects, flapless vs flapped surgery, zirconia vs titanium implants, prosthesis misfit — topics without their own subcategory. (MBL primary → `implants/mbl`; patient-condition survival → `implants/survival`; osteotomy drilling & heat → `implants/osteotomy-thermal`; bone-condensing/OD → `implants/osseodensification`; reduced-dimension implants → `implants/short-narrow`; full-arch/All-on-X → `implants/full-arch`; loading timing → `implants/loading-protocol`) |
| `implants/mbl` | 임플란트·변연골소실 | Marginal bone loss (MBL) / crestal bone loss — platform switching (PS vs PM), bone-level vs tissue-level MBL, implant-tooth proximity bone loss, emergence angle, inter-implant distance, risk-factor umbrella SRs |
| `implants/survival` | 임플란트·생존율·실패위험 | Implant survival/failure as the outcome, and what predicts it — long-term cumulative survival cohorts & SR/MA; **habit** risk (smoking level/cessation, tobacco & smoke-free products, bruxism); **systemic/host** risk (diabetes, hypertension, osteoporosis & PTH, Sjögren, autoimmune & systemic sclerosis, head-and-neck radiotherapy, medications/polypharmacy affecting osseointegration); early-failure risk-factor studies & failure-rate umbrella reviews; evidence-quality appraisal bound to this literature (sponsorship bias, risk-of-bias in smoker SRs); management of the failed implant (explantation/retrieval technique). (survival framed by implant **dimension** → `implants/short-narrow`; peri-implant *disease* as the outcome → `implants/peri-implantitis`; systemic-disease patient management where the outcome is a **medical** event, not implant survival → `drug/systemic-disease`) |
| `implants/isq` | 임플란트·ISQ | ISQ/RFA measurement, stability dip, loading decision thresholds |
| `implants/surface` | 임플란트·표면처리 | SLA, CA, UV surface technology, osseointegration. (cold/atmospheric plasma surface activation → `implants/surface/plasma`) |
| `implants/surface/plasma` | 임플란트·표면처리·플라즈마 | Cold/non-thermal atmospheric plasma (CAP/NTAP) titanium & zirconia surface treatment — osseointegration (animal/RCT), antimicrobial/decontamination, plasma-activated implant/abutment surfaces, vacuum-plasma chairside activation, biocompatibility. (root-canal CAP disinfection → `endodontics/cold-plasma`) |
| `implants/vitamin-d` | 임플란트·비타민 D | Serum/topical vitamin D and osseointegration — deficiency ↔ early implant failure, supplementation & bone/soft-tissue preservation, human SR/umbrella reviews & prospective cohorts |
| `implants/vertical-ridge-augmentation` | 임플란트·수직골증대 | Vertical ridge augmentation, Ti-mesh / PTFE mesh GBR, vertical bone gain, mesh exposure, customized CAD/CAM mesh |
| `implants/peri-implantitis` | 임플란트·주위염 | Peri-implantitis prevalence, risk factors, non-surgical/surgical treatment, surface decontamination, GBR for peri-implant defects |
| `implants/soft-tissue` | 임플란트·연조직 | Peri-implant soft tissue augmentation — keratinized mucosa (KM) width/thickness, buccal dehiscence (PSTD), soft tissue substitutes (xenogeneic collagen matrix vs autograft FGG/CTG), second-stage surgery, vestibuloplasty |
| `implants/osseodensification` | 임플란트·골밀도화 | Osseodensification (OD) osteotomy — bone-condensing bidirectional burs (Densah/Versah, negative-rake flute design), primary stability & ISQ/insertion-torque vs conventional drilling, low-density bone & alveolar ridge expansion, BIC/histomorphometry (animal & human), OD applied to orthopedic fixation; brand-specific Versah clinical protocols (sinus lift I/II, IDR, immediate placement). Named by **method**, not brand — `versah-protocols` was renamed 2026-07-29. (drill heat/thermal injury & conventional drill design → `implants/osteotomy-thermal`) |
| `implants/osteotomy-thermal` | 임플란트·골절개·발열 | Implant osteotomy preparation & thermal injury — bone-drilling heat generation and thermal-osteonecrosis thresholds, drill design/material/wear, irrigation & cooling (internal/external, CFD modelling), drilling speed and continuous vs intermittent protocols, piezosurgery, undersized preparation & tapping, guided-sleeve drilling temperature, histologic/histomorphometric implant-bed studies. (bone-condensing/OD → `implants/osseodensification`) |
| `implants/short-narrow` | 임플란트·단폭경(짧은·좁은) | Implants defined by reduced **dimension** — short (≤8 mm) and extra-short (4–6 mm) implants vs standard-length-plus-augmentation/sinus-elevation alternatives, narrow-diameter implants (NDI, ≤3.3 mm) & one- vs two-piece narrow designs, titanium-zirconium narrow implants, diameter/length outcome distributions, survival & MBL of reduced-dimension implants. (survival framed by patient condition → `implants/survival`) |
| `implants/full-arch` | 임플란트·전악수복 | Full-arch / edentulous-jaw implant rehabilitation — All-on-4/-6, tilted vs axial distal implants, immediate full-arch loading & flapless full-arch, implant overdentures (single/two-implant, CAD-CAM bar), framework & load-direction FEA, severely atrophic-jaw solutions (zygomatic, customized subperiosteal). (loading timing as the study's own axis → `implants/loading-protocol`) |
| `implants/loading-protocol` | 임플란트·부하시기 | Loading timing for **conventionally placed (healed-site)** implants — immediate vs early vs conventional/delayed loading, placement-and-loading protocol classifications (ITI consensus, Cochrane), single-crown & partial-arch loading SR/MA, methodological quality of loading-time trials. (loading of **immediately placed** implants → `immediate-implant/loading-protocol`; full-arch immediate loading → `implants/full-arch`) |

### 골재생 (bone-regeneration)

| Category folder | Korean | Includes |
|---|---|---|
| `bone-regeneration` | 골재생 (general) | Guided bone regeneration (GBR), barrier membranes (collagen/crosslinked/PTFE), bone graft substitutes (DBBM/BCP/β-TCP) & biomaterials, horizontal/vertical augmentation, peri-implantitis GBR, animal/biomechanics models. (socket/ridge preservation → `bone-regeneration/ridge-preservation`) |
| `bone-regeneration/ridge-preservation` | 골재생·치조제보존 | Alveolar ridge preservation (ARP) / socket preservation — post-extraction dimensional changes (Araujo/Tan/Schropp), ARP efficacy SR/MA & Cochrane, grafting materials & sealing/socket-seal, flap vs flapless, biologics/PRF, esthetic-zone ARP, ARP→implant outcomes |
| `bone-biology` | 골생물학 | Molecular/cellular bone biology — osteoclast/osteoblast signaling (SIK, PTHrP, RANKL), residual ridge resorption pathology, basic socket healing biology |

### 즉시식립 (immediate-implant)

| Category folder | Korean | Includes |
|---|---|---|
| `immediate-implant` | 즉시식립 (general) | Immediate (type 1) implant placement — foundational socket-healing & post-extraction dimensional change (Araujo/Botticelli/Covani), placement-timing immediate-vs-delayed evidence (the category's defining axis) & overall survival/outcome SRs, flap-vs-flapless, full-arch/edentulous, and cross-cutting modifiers lacking their own subcategory (systemic/diabetic, digital-guided accuracy, immediate+sinus-elevation adjunct, postoperative infection). (anatomic/CBCT case-selection & sagittal-root-position → `immediate-implant/anatomic-assessment`; molar/inter-radicular-septum → `immediate-implant/molar-septum`; infected/periapical/periodontitis sockets → `immediate-implant/infected-socket`; jumping-gap grafting & GBR/dehiscence → `immediate-implant/gap-grafting`; primary-stability/macrogeometry/drilling → `immediate-implant/primary-stability`; loading protocol → `immediate-implant/loading-protocol`; root-analogue/custom implants → `immediate-implant/root-analog`; socket-shield → `immediate-implant/socket-shield`; esthetic/soft-tissue/provisionalization → `immediate-implant/esthetic-soft-tissue`) |
| `immediate-implant/anatomic-assessment` | 즉시식립·해부학적평가 | Preoperative CBCT anatomic/morphometric case-selection for immediate implant placement (IIP) — Kan sagittal-root-position (SRP) classification & population prevalence, labial/buccal plate thickness & fenestration/dehiscence risk, incisive-canal proximity, alveolar bone dimensions/root inclination, posterior-mandible root-to-IAC safety distance, premolar cortical-perforation risk; anatomy-only datasets & CBCT decision frameworks with no site-specific anchorage technique or implant outcome. (molar inter-radicular-septum anatomy → `immediate-implant/molar-septum`) |
| `immediate-implant/molar-septum` | 즉시식립·구치부·치조중격 | Molar & posterior-site IIP centred on inter-radicular-septum anchorage — Smith-Tarnow A/B/C socket classification, CBCT septum morphology/dimension studies, osseodensification septum expansion, palatal-root-socket anchorage, pre-extractive site preparation, maxillary-molar case-selection guidelines, molar-IIP survival SR/MA |
| `immediate-implant/infected-socket` | 즉시식립·감염치조부 | IIP into infected/compromised extraction sockets — periapical/endodontic pathology (acute vs chronic) & periodontitis-compromised sites; decontamination + antibiotic protocols, immediate provisionalization in infected zones, survival/MBL/WKG vs non-infected controls; acute-purulent/sinus-perforation contraindication threshold. (postoperative infection as a failure event stays general) |
| `immediate-implant/gap-grafting` | 즉시식립·간극이식·GBR | Jumping-gap/buccal-gap management & GBR at IIP — bone-substitute (xenograft/alloplast/BSM) & collagen gap grafting, PRF/CGF and barrier-membrane/Ti-mesh GBR, buccal-dehiscence/defect correction (SPAL, BioARP, vestibular socket therapy, tuberosity block/IDR), ≥2 mm jump-space grafting thresholds, membrane wound-management |
| `immediate-implant/primary-stability` | 즉시식립·초기고정 | Achieving & measuring primary/early-secondary stability specific to IIP — implant macrogeometry (wide-thread/tapered/body-shift), undersized/osteotome drilling protocols, ISQ/RFA stability-dip trajectory, CBCT primary-stability prediction (five-thread guideline), low/absent-primary-stability salvage, osseointegration biomechanics. (generic ISQ/RFA measurement science → `implants/isq`) |
| `immediate-implant/loading-protocol` | 즉시식립·부하프로토콜 | Loading timing/protocol for immediately-placed implants — immediate vs early vs conventional/delayed loading, primary-stability thresholds for immediate loading (IT ≥35 Ncm, ISQ ≥70), single-tooth & full-arch/edentulous immediate-loading survival & MBL, PROMs in loading-timing trials. Distinct from placement-timing (immediate-vs-delayed *placement* stays general) |
| `immediate-implant/root-analog` | 즉시식립·치근유사임플란트 | Root-analogue implants (RAI) & custom-fabricated implants for immediate drill-free single-tooth replacement — CAD-CAM-milled/additively-manufactured (DMLS/SLM) titanium, zirconia or hybrid; socket-fit macroretentive design, survival/MBL/PES-WES outcomes & fracture/marginal-fit failure modes, RAI vs forced-orthodontic-extrusion, custom metal-free (ZrO2) implants |
| `immediate-implant/socket-shield` | 즉시식립·소켓실드 | Socket-shield technique / partial extraction therapy (PET) — root/dentin shield to preserve buccal bone; survival/MBL/PES vs conventional, complications/failure, FEA stress, reviews/SR-MA |
| `immediate-implant/esthetic-soft-tissue` | 즉시식립·심미연조직 | Immediate implant esthetic & soft-tissue outcomes — immediate provisionalization, connective-tissue/soft-tissue grafting (SCTG/CTG), midfacial recession & papilla, pink esthetic score, buccal-dehiscence esthetic, esthetic-zone selection criteria |

### 상악동거상술 (sinus-lift)

| Category folder | Korean | Includes |
|---|---|---|
| `sinus-lift/lateral` | 상악동거상술·측방 | Lateral window approach, membrane, grafting materials |
| `sinus-lift/transcrestal` | 상악동거상술·경치조골 | Transcrestal (osteotome/balloon/osseodensification) approaches |
| `sinus-lift/pseudocyst` | 상악동거상술·슈도시스트 | Antral pseudocyst / mucous retention cyst management in sinus lift context — retention vs removal, outcomes, implant impact |

### 근관치료 (endodontics)

| Category folder | Korean | Includes |
|---|---|---|
| `endodontics` | 근관치료 (general) | Root canal treatment topics not covered by a subcategory — endodontic outcomes/prognosis, retreatment, pain/flare-up, general reviews. (subtopics route to `endodontics/{anatomy,diagnosis,eal,irrigation,obturation,shaping,vpt,regenerative,cold-plasma,visit-protocol}`) |
| `endodontics/obturation` | 근관치료·충전 | Root canal obturation — gutta-percha & GP cone handling (contamination/disinfection), sealers (bioceramic/CaSi: CeraSeal/NeoSealer/BioRoot; epoxy: AH Plus), single-cone vs carrier-based, sealer cytotoxicity/bioactivity/wettability, retreatment/sealer removal, pediatric pulpectomy materials (Vitapex/ZOE), post-obturation pain |
| `endodontics/anatomy` | 근관치료·해부 | Canal morphology, access cavity, MB2, CBCT-guided access |
| `endodontics/diagnosis` | 근관치료·진단 | Pulp & periapical diagnosis — pulp sensibility vs vitality test accuracy, pulpitis diagnosis effectiveness, pediatric pulp testing, periapical lesion etiology/diagnosis (granuloma vs cyst) |
| `endodontics/eal` | 근관치료·근관장측정 | EAL accuracy, working length, apex locator devices |
| `endodontics/irrigation` | 근관치료·세정 | Irrigant activation (PUI, ANP, sonic), NaOCl protocols |
| `endodontics/shaping` | 근관치료·근관성형 | Rotary/reciprocating NiTi instruments, shaping strategies (crown-down, single-file), file separation, canal transportation, apical patency |
| `endodontics/vpt` | 근관치료·생활치수요법 | Vital pulp therapy (VPT) — direct pulp capping, partial/full pulpotomy; MTA/Biodentine agents; success criteria; decision thresholds for mature/immature teeth |
| `endodontics/regenerative` | 근관치료·재생근관치료 | Regenerative endodontic procedures (REP) — biologic basis, blood clot scaffold, MTA barrier, outcomes in open-apex teeth |
| `endodontics/cold-plasma` | 근관치료·냉플라즈마 | Cold atmospheric plasma (CAP), non-thermal plasma jet, underwater discharge plasma for root canal disinfection; E. faecalis biofilm, ROS/RNS mechanisms, safety |
| `endodontics/visit-protocol` | 근관치료·내원횟수 | Single-visit vs multi-visit root canal treatment — healing outcomes, postoperative pain, patient preference; retreatment context |

### 치주·치간·미생물 (periodontics & biofilm)

| Category folder | Korean | Includes |
|---|---|---|
| `periodontics` | 치주치료 | Periodontal disease, classification, regeneration/root-coverage, SPT, periodontal-systemic links, general periodontics not covered by a subcategory. (patient/home plaque-control mechanical+chemical → `periodontics/oral-hygiene-instruction`; professional non-surgical instrumentation → `periodontics/non-surgical-instrumentation`; nutraceutical/probiotic/herbal adjuncts → `periodontics/host-modulation`) |
| `periodontics/oral-hygiene-instruction` | 치주치료·치면세균막관리 | Patient/home plaque control — toothbrush (manual/powered/electric) design & technique, Watanabe/Bass toothpick methods, toothpaste/dentifrice, chemical plaque control (chlorhexidine & other mouthrinse adjuncts), plaque-disclosing agents & indices, digital plaque monitoring |
| `periodontics/non-surgical-instrumentation` | 치주치료·비외과적기구처치 | Professional non-surgical periodontal instrumentation — scaling & root planing (SRP), guided biofilm therapy (GBT), air-polishing, hand vs ultrasonic/piezoelectric scaling & instrument biomechanics/ergonomics, subgingival irrigation/reinstrumentation, SRP treatment guidelines |
| `periodontics/host-modulation` | 치주치료·숙주조절요법 | Host-modulation therapy adjuncts to periodontal treatment — probiotics, coenzyme Q10, omega-3, melatonin, vitamins, herbal/nutraceutical extracts (magnoliae cortex, avocado-soybean unsaponifiables, etc.) |
| `interdental-cleaning` | 치간 청소 | Interdental cleaning devices/aids — dental floss, interdental brush (IDB), water flosser / oral irrigator (Waterpik), wooden toothpick; efficacy RCTs/SRs, device head-to-heads, adherence, gingival abrasion, papilla harm. (Watanabe toothpick *toothbrushing* method → `periodontics/oral-hygiene-instruction`; peri-implant device comparisons → `implants/peri-implantitis`) |
| `oral-microbiology` | 구강미생물학 | Oral microbiome ecology & dysbiosis, dental/biofilm matrix (EPS, glucans, eDNA, matrixome), keystone pathogens (P. gingivalis, F. nucleatum), polymicrobial synergy & dysbiosis (PSD) model, Streptococcus/Candida interactions, microbiome–systemic/cancer links |
| `halitosis` | 구취 | Halitosis etiology (VSC, bacteria, systemic), prevalence, measurement (organoleptic/halitometric), management (oral hygiene, probiotics, PDT), systemic associations (periodontitis, H. pylori, OHRQoL) |

### 수복·재료 (restorative & materials)

| Category folder | Korean | Includes |
|---|---|---|
| `dental-materials` | 치과재료 (general) | Amalgam/composite longevity, impression materials (dimensional stability/flowability), PEEK, liners, mixed material-failure SRs. (ceramic-specific → `dental-materials/ceramic`; zirconia-specific → `dental-materials/zirconia`) |
| `dental-materials/ceramic` | 치과재료·세라믹 | Non-zirconia dental ceramics — lithium disilicate (LDS/e.max), leucite-reinforced glass-ceramic, ZLS (Celtra), all-ceramic FDP/crown survival SRs, material selection guide, nanoceramic, CAD/CAM ceramic failure reasons, intraoral repair, resin bonding to high-strength ceramics |
| `dental-materials/zirconia` | 치과재료·지르코니아 | Dental zirconia (Y-TZP/3Y/4Y/5Y, monolithic) — material types/processing, strength/defects, antagonist enamel wear, LTD/aging, survival/clinical, bonding & saliva-contamination cleaning (Ivoclean/primers/MDP), grinding/polishing/glazing |
| `glass-ionomer` | 글래스아이오노머 | GIC / RMGIC / HVGIC: composition, restorative & preventive use, longevity, bioactivity/remineralization, biocompatibility, fissure sealant |
| `resin` | 레진 | Composite resin, polymerization, shrinkage |
| `resin-bonding` | 레진접착 | Adhesive systems, bonding mechanisms, dentin adhesion |
| `inlay` | 인레이 | Inlay/onlay restorations, ceramic inlays |
| `veneers` | 비니어·라미네이트 | Ceramic laminate veneers (feldspathic, leucite, lithium disilicate, zirconia), composite veneers — preparation techniques, fabrication (platinum foil vs refractory die), survival/complication rates, incisal coverage, minimally invasive vs conventional, cementation |
| `post-and-core` | 포스트앤코어 | Restoration of endodontically treated teeth — post-vs-no-post decision, fiber vs metal/cast post survival, ferrule effect, endocrown alternative, post length/material/cementation, failure mode (root fracture vs repairable). (fiber-post adhesion/bonding → `resin-bonding`; fiber-post FEA → `resin`) |

### 보철 (prosthodontics)

| Category folder | Korean | Includes |
|---|---|---|
| `prosthetic-materials` | 보철재료 | Zirconia/ceramic crown survival, full-arch prosthetics, luting cements, provisional materials, general prosthetic-materials not covered by a subcategory. (abutment screw/retention biomechanics → `prosthetic-materials/abutment-screw`; tooth preparation geometry → `prosthetic-materials/tooth-preparation`) |
| `prosthetic-materials/abutment-screw` | 보철재료·지대주나사 | Implant abutment screw & retention biomechanics — preload, removal/insertion torque, screw-loosening, settling effect, retightening, screw coatings, morse-taper/conical connections, screw- vs cement-retention comparisons |
| `prosthetic-materials/tooth-preparation` | 보철재료·지대치형성 | Tooth preparation geometry for crowns/FPDs — total occlusal convergence (TOC)/taper, finish-line design, marginal adaptation/gap, resistance & retention form, preparation-quality assessment |
| `complete-denture` | 총의치·가철성보철 | Complete/removable denture prosthodontics — occlusal vertical dimension (OVD/VDO) determination (rest position, freeway space, anthropometric/facial, phonetics, cephalometric), jaw relation records, signs of excessive/reduced VD, edentulous prosthodontics. (denture *occlusal scheme* balanced/lingualized → `occlusion`) |
| `removable-partial-denture` | 국소의치 | Removable partial denture (RPD) **selection decision** for the partially dentate — when an RPD is indicated versus a shortened dental arch (SDA), tooth-supported fixed prosthesis, or implant; Kennedy-class-driven indications, long-term prosthesis & abutment survival bearing on the choice, patient-reported outcomes/OHRQoL, discontinuation and patient factors, cost-effectiveness comparisons. (implant-assisted/-supported RPD (IARPD/ISRPD), attachment systems, framework materials & CAD-CAM fabrication → not yet split out; edentulous/complete-denture prosthodontics → `complete-denture`) |
| `occlusion` | 교합 | Occlusal analysis (digital/T-Scan vs articulating paper), implant occlusion, occlusal overload, occlusal scheme/adjustment |
| `digital-workflow` | 디지털워크플로우 | IOS accuracy, CBCT, CAD/CAM, guided surgery |

### 우식·경조직·표면 (caries & hard tissue)

| Category folder | Korean | Includes |
|---|---|---|
| `caries` | 우식 | Caries detection, risk assessment, minimal intervention dentistry, fluoride, fissure sealants, ICDAS, stepwise/selective excavation |
| `cracked-tooth` | 균열치 증후군 | Cracked tooth syndrome — classification (Ellis/Baird), diagnosis, prognosis, restoration design, FEA stress analysis |
| `dentin-hypersensitivity` | 상아질 과민증 | Dentinal hypersensitivity — etiology (hydrodynamic theory), in-office and at-home management, desensitizing agents |
| `dental-erosion` | 치아침식 | Erosive tooth wear (ETW) — etiology (intrinsic/extrinsic acids, dietary soft drinks/citrus), enamel demineralization/mineral loss chemistry, erosion measurement (profilometry), risk factors & prevention |
| `nccl` | 비우식성 치경부 병소 | Noncarious cervical lesions / abfraction — morphology (saucer/V-shape), progression (D/H ratio), prevalence, multifactorial etiology (stress/friction/biocorrosion schema), demineralization pathophysiology, SEM/stereomicroscopic characterization, monitor-vs-restore decision. (NCCL adhesive-restoration RCTs → `resin-bonding`) |
| `tooth-whitening` | 치아미백 | Vital tooth bleaching (in-office vs at-home, hydrogen/carbamide peroxide concentration, efficacy/longevity), bleaching-induced tooth sensitivity & management, effect on enamel/restorations, non-vital internal (walking-bleach), OTC strips/gels/LED. (white-spot lesion remineralization/resin infiltration → `caries`) |

### 외과·마취·봉합 (surgery, anesthesia, closure)

| Category folder | Korean | Includes |
|---|---|---|
| `oral-surgery` | 구강외과 | Extractions, surgical complications not covered by a subcategory (oroantral fistula, hemostasis, deep neck infection, free flap). (third molar/wisdom tooth surgery → `oral-surgery/third-molar`; IAN/lingual/trigeminal nerve injury → `oral-surgery/nerve-injury`) |
| `oral-surgery/third-molar` | 구강외과·제3대구치(사랑니) | Third molar (wisdom tooth) extraction — surgical indications/technique (flap design, bone removal, sectioning), coronectomy, pericoronitis, extraction complications (mandibular fracture, dry socket/alveolar osteitis), postop adjuncts (PRF/CGF, LLLT, cooled irrigation, pain management) |
| `oral-surgery/nerve-injury` | 구강외과·신경손상 | Inferior alveolar nerve (IAN) / lingual / trigeminal nerve injury — etiology, diagnosis (CBCT risk assessment, neurosensory testing), management (corticosteroids, vitamin B12, LLLT/photobiomodulation); any cause (third-molar extraction, implant placement, orthognathic surgery); includes peripheral nerve regeneration basic science |
| `suture-wound-closure` | 봉합·창상폐쇄 | Suture techniques/patterns & biomechanics, primary vs secondary closure, sutureless surgery, tissue adhesives, flap design for tension-free primary closure (PASS, periosteal releasing, advancement flaps) |
| `local-anesthesia` | 국소마취·진정 | LA agents (articaine/lidocaine/mepivacaine), IANB/buccal infiltration, buffered/preheated LA, N2O & procedural sedation, topical anesthetics, injection landmarks; pregnancy/pediatric LA; supplemental injections for irreversible pulpitis |
| `dental-trauma` | 외상치학 | Traumatic dental injuries — tooth avulsion & replantation (storage media, root resorption), splinting (rigid vs flexible, duration), luxation injuries & pulp survival, crown/root fracture, mouthguard prevention, IADT guidelines. (REP for traumatized immature teeth also → `endodontics/regenerative`) |
| `dental-handpiece` | 치과 핸드피스·엔진 | Dental rotary handpieces / the dental engine — air turbine (high-speed air-driven), electric high-speed handpiece, low-speed micromotor contra-angle; aerosol/splatter generation & size distribution, occupational/infection-control hazard, high-volume evacuation efficacy, heat generation, mechanics/maintenance. (caries removal *clinical outcome* → `caries`; ultrasonic-scaler *periodontal* use → `periodontics`) |
| `infection-control` | 감염관리 | Dental infection control / cross-infection prevention — instrument sterilization & disinfection protocols, dental unit waterline (DUWL) contamination & treatment, electrolyzed/disinfectant water, surface/environmental decontamination, practice compliance. (aerosol generation from handpieces → `dental-handpiece`) |

### 약물·전신질환 (drug & systemic)

| Category folder | Korean | Includes |
|---|---|---|
| `drug/antibiotics` | 전신질환·약물·항생제 | Dental antibiotic prescribing, prophylaxis, antibiotic stewardship; AMX/CLV, clindamycin, azithromycin, metronidazole, cephalosporins; periodontal/endodontic/surgical adjunct use |
| `drug/analgesics` | 전신질환·약물·진통소염제 | NSAIDs (ibuprofen, ketorolac, naproxen, etoricoxib), acetaminophen, opioids, corticosteroids (dexamethasone), preemptive analgesia; postoperative pain management |
| `drug/anticoagulants` | 전신질환·약물·항응고·지혈 | Anticoagulants (warfarin, DOACs: apixaban/rivaroxaban/dabigatran), antiplatelets (aspirin, clopidogrel), perioperative management, hemostasis, DAPT |
| `drug/mronj` | 전신질환·약물·MRONJ | MRONJ/ONJ — bisphosphonates, denosumab, antiresorptive/antiangiogenic agents; prevention, staging, management |
| `drug/systemic-disease` | 전신질환·약물·전신질환관리 | Medically compromised patients — diabetes (HbA1c assay & interpretation), cardiovascular disease & perioperative hemodynamics, Sjögren classification criteria, renal/hepatic impairment, polypharmacy, drug–drug interactions, immunosuppression; systemic-disease ↔ oral-disease relationship reviews. The outcome is a **medical/systemic** one. (systemic condition studied as a risk factor for **implant survival/failure** → `implants/survival`) |
| `pdrn` | PDRN(폴리뉴클레오티드) | Polydeoxyribonucleotide (PDRN) biology, bone/soft-tissue regeneration with PDRN, peri-implant/sinus/extraction socket adjunct, A2A receptor mechanism |

### 구강내과·통증 (oral medicine & pain)

| Category folder | Korean | Includes |
|---|---|---|
| `oral-medicine` | 구강내과 | Oral-medicine topics not covered by a subcategory — miscellaneous/differential-diagnosis case reports, oral tori/exostoses (bony normal variants), saliva-as-diagnostic-fluid/biomarkers (salivaomics/liquid biopsy). (HSV/herpes → `oral-medicine/hsv`; potentially-malignant disorders & OLP malignant transformation → `oral-medicine/opmd`; cancer-therapy mucositis → `oral-medicine/mucositis`; benign mucosal normal variants → `oral-medicine/normal-variants`; odontogenic maxillary sinusitis → `oral-medicine/odontogenic-sinusitis`; burning mouth syndrome → `oral-medicine/burning-mouth-syndrome`; RAS & PFAPA/Behçet → `oral-medicine/aphthous-stomatitis`; oral lichen planus → `oral-medicine/lichen-planus`; pemphigus/pemphigoid/EM/lupus/GVHD → `oral-medicine/immune-mediated`; trigeminal neuralgia/neuropathic pain → `oral-medicine/trigeminal-neuralgia`; xerostomia & taste disorders → `oral-medicine/salivary-chemosensory`) |
| `oral-medicine/hsv` | 구강내과·헤르페스 | Oral herpes simplex virus (HSV) — primary herpetic gingivostomatitis (PHGS), recurrent/labial herpes, antiviral agents (aciclovir/docosanol, helicase-primase inhibitors), topical vs systemic therapy SRs, anti-HSV-1 pharmacology update |
| `oral-medicine/opmd` | 구강내과·구강잠재악성질환 | Oral potentially malignant disorders (OPMD) — leukoplakia/erythroplakia/OSMF/proliferative verrucous leukoplakia, malignant transformation rate & risk factors (incl. oral lichen planus malignant transformation), recurrence, SR/MA of transformation. (clinical management of a specific mucosal lesion → `oral-medicine`; OLP treatment/diagnosis → `oral-medicine/lichen-planus`) |
| `oral-medicine/mucositis` | 구강내과·구강점막염 | Cancer-therapy-induced oral mucositis (OM) — chemo/radiotherapy/HSCT toxicity, prevention & management (honey, LLLT/photobiomodulation, palifermin/KGF, chlorhexidine, glutamine/arginine, cryotherapy), pediatric OM & adult head-and-neck radiation-induced OM (RIOM), MASCC/ISOO supportive care. (immune-mediated/idiopathic mucosal disease → `oral-medicine`) |
| `oral-medicine/normal-variants` | 구강내과·정상변이병소 | Benign normal-variant oral mucosal findings — Fordyce granules (포다이스 그래뉼), linea alba / morsicatio buccarum-labiorum (교흔, cheek/lip biting), frictional keratosis, tobacco pouch keratosis, leukoedema; prevalence/epidemiology, dermoscopic/mucoscopic differentiation from potentially malignant or immune-mediated mimics (e.g., OLP). (actual disease/OPMD → `oral-medicine`/`oral-medicine/opmd`) |
| `oral-medicine/odontogenic-sinusitis` | 구강내과·치성상악동염 | Odontogenic maxillary sinusitis (ODS) — maxillary sinusitis of dental origin (periapical/periodontal infection, oroantral communication, iatrogenic implant/graft/endodontic causes), diagnosis (CBCT unilateral opacification, odontogenic vs rhinogenic differentiation), sinonasal complications of dental disease, multidisciplinary dental–ENT management (dental source removal, FESS, antibiotics), state-of-art reviews & expert consensus |
| `oral-medicine/burning-mouth-syndrome` | 구강내과·구강작열감증후군 | Burning mouth syndrome (BMS) — primary/idiopathic intraoral burning with normal exam, pathophysiology (peripheral small-fiber neuropathy, central sensitization, estrogen decline, psychological factors), peripheral vs central subtypes, ICD-11 nomenclature & diagnostic algorithms, clinical management (topical/systemic clonazepam, others). (molecular nociception/ion-channel mechanisms → `orofacial-pain`) |
| `oral-medicine/aphthous-stomatitis` | 구강내과·아프타구내염 | Recurrent aphthous stomatitis (RAS) & syndromic recurrent oral ulceration — aphthous pathophysiology & classification, topical/systemic treatment ladders (corticosteroids, colchicine, thalidomide SR/MA), and aphthae-associated systemic syndromes sharing susceptibility loci: PFAPA (periodic fever) and Behçet disease oral ulceration |
| `oral-medicine/lichen-planus` | 구강내과·구강편평태선 | Oral lichen planus (OLP) — diagnosis/subtypes (reticular/erosive/atrophic), topical/systemic corticosteroid & immunomodulator treatment (Cochrane/SR), OLP as a sentinel for systemic comorbidity (thyroid, hepatitis C, diabetes, celiac, mood). (OLP malignant transformation → `oral-medicine/opmd`) |
| `oral-medicine/immune-mediated` | 구강내과·면역매개·수포성점막질환 | Immune-mediated & vesiculobullous oral mucosal disease other than lichen planus/aphthae — pemphigus vulgaris & mucous membrane pemphigoid, desquamative gingivitis (pharmacologic treatment), erythema multiforme (HSV/Mycoplasma-triggered), and oral manifestations of systemic autoimmune/alloimmune disease (systemic lupus erythematosus, chronic graft-versus-host disease). (lichen planus → `oral-medicine/lichen-planus`; recurrent aphthae/Behçet → `oral-medicine/aphthous-stomatitis`) |
| `oral-medicine/trigeminal-neuralgia` | 구강내과·삼차신경통·신경병성통증 | Neuropathic orofacial pain of clinical/therapeutic focus — trigeminal neuralgia (TN) pharmacotherapy (carbamazepine/oxcarbazepine, therapeutic-strategy SRs), post-traumatic trigeminal neuropathy (PTTN) after endodontic/surgical injury & dentist awareness, non-pharmacological adjuncts (acupuncture for neuropathic orofacial pain). (molecular neuropathic-pain mechanisms → `orofacial-pain`; burning mouth syndrome → `oral-medicine/burning-mouth-syndrome`) |
| `oral-medicine/salivary-chemosensory` | 구강내과·타액선·미각기능장애 | Salivary secretory & chemosensory dysfunction — xerostomia/hyposalivation (etiology & cellular targets, drug-induced/antihypertensive, artificial saliva, pharmacological & traditional management, impact on dental-treatment outcomes) and taste/chemosensory disorders (dysgeusia/ageusia from zinc deficiency, head-and-neck radiation, COVID-19, Sjögren-related chemosensory impairment). (saliva-as-diagnostic-fluid/biomarkers → `oral-medicine` general) |
| `orofacial-pain` | 구강안면통증·통증 신경기전 | Nociception/neuropathic-pain molecular mechanisms underlying orofacial pain & BMS — chloride homeostasis (NKCC1/KCC2), GABA-A/glycine disinhibition, peripheral nociceptor ion channels (anoctamin/TMEM16, TRPV1, Nav), T-type Ca²⁺ channels, neurosteroid modulation. (BMS clinical/diagnostic papers → `oral-medicine`) |
| `tmj` | 턱관절·악관절장애 | TMD diagnosis & management — arthrocentesis, splint therapy, pharmacotherapy, chronic pain, TMJ osteoarthritis, sleep bruxism |
| `botulinum-toxin` | 보툴리눔 독소 | Botulinum toxin type A (BoNT-A) for bruxism, TMD/myogenous pain, gummy smile, lip aesthetics; injection landmarks, dosing, longevity |

### 교정 (orthodontics)

| Category folder | Korean | Includes |
|---|---|---|
| `orthodontics` | 교정학 | Orthodontic miniscrews (TADs) — stability, failure risk, reuse; periodontal-orthodontic interactions; force biology |
| `orthodontics/myofunctional` | 교정학·근기능교정/탄성교정 | Myofunctional / elastodontic orthodontics (EF Line, AMCOP, Eptamed Equilibrator, Occlus-o-Guide prefabricated silicone/elastomeric bio-activators) — interceptive treatment of malocclusion in growing/mixed-dentition patients: Class II sagittal correction (overjet/overbite, SNB/ANB), transverse/palatal expansion & posterior crossbite, vertical/open-bite & neuromuscular (sEMG) balance, pharyngeal airway, appliance material/mechanical characterization. Distinct from fixed-appliance & clear-aligner orthodontics |
| `orthodontics/clear-aligner` | 교정학·투명교정 | Clear aligner therapy (CAT) indications & limitations — efficacy vs fixed appliances (mild-moderate equivalence; inferior torque/rotation/extrusion), Class II strategies (molar distalization, mandibular advancement), biomechanics (attachments, trimline design), maxillary expansion, safety (root resorption), periodontal/oral-hygiene, masticatory muscle/TMJ changes, accelerated-orthodontics adjuncts, aligner biofilm |

### 행동치의학 (behavioral-dentistry)

| Category folder | Korean | Includes |
|---|---|---|
| `behavioral-dentistry/motivational-interviewing` | 행동치의학·동기면담 | Motivational interviewing (MI/brief MI) efficacy & uptake, behavior-change counseling, oral-health/general-health promotion |
| `behavioral-dentistry/communication-relationship` | 행동치의학·커뮤니케이션 | Dentist–patient communication skills/training, dentist–patient relationship determinants, shared decision-making, patient expectation management |
| `behavioral-dentistry/patient-reported-outcomes` | 행동치의학·환자보고결과 | PRO/PROM/PREM, OHRQoL, patient satisfaction/experience, behavioral assessment of the patient |
| `behavioral-dentistry/dental-anxiety` | 행동치의학·치과불안 | Dental anxiety/fear/phobia assessment & management (pediatric + adult), behavior-rating scales, non-pharmacological strategies |
| `behavioral-dentistry/body-dysmorphic-disorder` | 행동치의학·신체이형장애 | Body dysmorphic disorder (BDD) prevalence & screening in esthetic-procedure candidates, preoperative psychological evaluation, patient selection for cosmetic/esthetic dentistry, BDD-driven postoperative dissatisfaction |

### 기타 임상·경영·근거 (cross-cutting)

| Category folder | Korean | Includes |
|---|---|---|
| `radiology` | 방사선학 | CBCT diagnostic performance, radiation dose/collimation, panoramic, cephalometric, CBCT-guided endodontics/implant, shielding protocols |
| `geriatric-dentistry` | 노년치의학 | Oral frailty, xerostomia/hyposalivation, root caries in elderly, professionally applied fluoride, polypharmacy oral effects |
| `food-impaction` | 식편압입·치간이개 | Food impaction & proximal/interproximal contact loss (PCL/ICL) between implant prostheses (or natural teeth) and adjacent teeth — prevalence, risk factors, mesial>distal pattern, time-progression, clinical implications (caries, periodontal), management. (natural-tooth open contact, plunger cusp, marginal-ridge contour included) |
| `artificial-intelligence` | 인공지능·기계학습 | AI/ML/deep-learning in dentistry — diagnostic performance (caries detection, anomaly/lesion identification, risk prediction), CNN/imaging models, methodological quality (AMSTAR-2, QUADAS-2) & evidence-overlap appraisal of AI systematic reviews. Classify by method (AI/ML) not by population/disease |
| `evidence-appraisal` | 근거평가·통계방법론 | EBM/EBD critical appraisal, SR/MA methodology, biostatistics (p-value/CI/OR/RR/HR/NNT), common mistakes |
| `professional-wellbeing` | 치과의사 직업적 웰빙 | Burnout prevalence, risk factors, protective factors, wellbeing interventions among dental professionals; COVID impact |
| `practice-management` | 치과경영 | Dental practice management — legal/regulatory decisions (헌법재판소 등), operational policies, clinic administration |
| `complaint-management` | 환자 민원·컴플레인 관리 | Patient complaint science — complaint classification taxonomies (Reader taxonomy, HCAT) & reliability, complainant expectations & fairness (justice theory), complaint-response quality (defensive tactics, fauxpology), service recovery, staff training (CODE), national complaint policy, dental-specific complaints/malpractice/medico-legal. (general healthcare + dental applied) |
| `dental-history` | 치과 역사 | Historical figures, milestones in dentistry (Korean and international) |

### 종합 (overviews)

| Category folder | Korean | Includes |
|---|---|---|
| `overviews` | 종합 | Synthesis pages spanning multiple categories |

Classify by **method/procedure**, not by disease or anatomy.
