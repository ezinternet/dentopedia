# Relation Negatives — 검토했고 엣지 불필요

논쟁 레이더 후보를 두 페이지 다 읽고 판정한 결과 **엣지가 필요 없다**고 결론난 건들.
`find-contradiction-candidates.py`가 이 파일을 읽어 해당 후보를 억제한다.

키는 `(source, target, 문장해시)`다 — 문장이 바뀌면 해시가 달라져 **자동으로
재검토 대상이 된다.** 페이지가 개정돼 진짜 충돌이 새로 생기는 경우를 놓치지 않기 위함.

부정 판정도 지식이다. 지우지 말 것 — 지우면 그 판정 노동이 사라진다.

| date | source | target | snippet_hash | reason |
|------|--------|--------|--------------|--------|
| 2026-07-20 | tang-2025-chitosan-antibacterial-hemostatic-sponge-extraction | dinkova-2025-local-hemostasis-oral-surgery-review | deaafa2efcb7 | preclinical/animal study adds material layer beneath clinical review; different evidence tier not conflicting claims |
| 2026-07-18 | achmadi-2025-intraoral-scanner-edentulous-accuracy-scoping | digital-workflow-decision-ladder | 259af0ffb738 | contrast is against vankos-2026 and singh-2025 not the overview |
| 2026-07-18 | de-almeida-junior-2024-cytotoxicity-bioactivity-ceraseal-bioroot | zamparini-2023-premixed-calcium-silicate-carrier-based-2year | da231582d55a | in-vitro cytotoxicity complements clinical cohort; Whereas contrasts study type |
| 2026-07-18 | de-almeida-junior-2024-cytotoxicity-bioactivity-ceraseal-bioroot | spinelli-2024-three-year-single-cone-ceraseal-cohort | da231582d55a | lab-versus-clinical framing no conflicting claim |
| 2026-07-18 | li-2022-digital-edentulous-maxillomandibular-relationship-jaw-tracking | singh-2026-nick-notch-intraoral-gothic-arch-jaw-relation | 68a6e00abbd9 | However refers to Li own cautionary result Singh is concordant benchmark |
| 2026-07-18 | bodner-2012-cutaneous-sinus-tract-dental | gargava-2022-deep-neck-space-infection-150-cases | c7aa104465e8 | chronic sinus tract vs acute deep-neck spread are complementary presentations |
| 2026-07-18 | kiliaridis-2000-vertical-position-rotation-tipping-molars | unopposed-tooth-overeruption-overview | 115e8476e9ff | refutation targets clinical belief; overview already has applies-to edge back |
| 2026-07-18 | yu-2024-clinical-decision-centric-relation-dentate | kattadiyil-2021-relationship-centric-occlusion-maximal-intercuspal | 9309ad61bfe3 | contrast is evidence class narrative review vs consensus not finding |
| 2026-07-18 | lamont-2018-routine-scale-and-polish-periodontal-health | farina-2026-pmpr-biofilm-gingivitis-sr-ma | da20d786a426 | different population and question; Farina already carries extends edge |
| 2026-07-18 | nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy | poudel-2026-xerostomia-dental-treatment-outcomes-sr | e81a34e89337 | reframing saliva as diagnostic medium opens new axis not conflict |
| 2026-07-18 | mello-2017-immediate-fresh-extraction-vs-delayed-healed-socket-sr-ma | asghar-2023-immediate-vs-early-implant-esthetic-zone-sr-ma | 13e604c8dcb1 | Asghar compares immediate vs early esthetic zone different question |
| 2026-07-18 | al-obaida-2019-comparison-perceived-pain-patients-satisfaction | ramanathan-2023-efficacy-reliability-single-tooth-anesthesia | 07e3b022c706 | different procedure type and comparator framed as complementary scope |
| 2026-07-18 | abutment-screw-preload-joint-stability-overview | varvara-2020-retightening-preload-loss-abutment-screws | c50c170d9691 | retightening debate among own source papers Varvara vs Nithyapriya |
| 2026-07-18 | complete-denture-ovd-determination-overview | singh-2026-nick-notch-intraoral-gothic-arch-jaw-relation | 923baf097049 | sentence is about Satin 2023 Singh cited only as magnitude yardstick |
| 2026-07-18 | resin-dentin-bond-durability-degradation-overview | talungchit-2014-ethanol-wet-bonding-chlorhexidine-resin-dentin-durability | 4aa73444cb6a | however contrasts different technique not Talungchit finding |
| 2026-07-18 | resin-dentin-bond-durability-degradation-overview | forville-2024-moist-dentin-adhesive-systems-reevaluation | 4aa73444cb6a | Forville reported descriptively as supporting evidence |
| 2026-07-18 | resin-dentin-bond-durability-degradation-overview | zheng-2024-dentin-conditioners-bond-strength-sr | 4aa73444cb6a | Zheng cited descriptively no disagreement |
| 2026-07-18 | direct-resin-restoration-adhesion-placement-overview | tay-2003-dentin-adhesives-hydrophilic | 86ac4c142419 | disagreement among Hong Assis Doshi Oza; Tay invoked as mechanism |
| 2026-07-18 | periodontal-adjunctive-therapy-probiotics-pdt-overview | jungbauer-2026-naocl-hyaluronic-acid-subgingival-reinstrumentation-rct | c54821f1f4cc | counterpoint between two constituent papers Jungbauer and da Silveira |
| 2026-07-18 | treatment-planning-decision-variability-overview | li-2026-root-canal-timing-autotransplanted-teeth-prognosis-sr-ma | b55de636beaa | heterogeneity internal to Li meta-analysis |
| 2026-07-18 | treatment-planning-decision-variability-overview | ziaei-2025-ai-orthodontic-extraction-treatment-planning-sr-ma | ce0a8ba16bd7 | critique already on Ziaei page which has applies-to edge |
| 2026-07-18 | treatment-planning-decision-variability-overview | cangul-2026-full-pulpotomy-adoption-determinants-trainee-decision-making | f37dc05517c5 | internal Abstract-vs-Results inconsistency inside Cangul |
| 2026-07-18 | clear-aligner-indications-limitations | charoenrat-2025-clear-aligner-anterior-open-bite-molar-intrusion-sr-ma | 3dd8ab44e169 | whereas contrasts CAT with fixed TADs inside Charoenrat own MA |
| 2026-07-18 | clear-aligner-indications-limitations | meade-2026-invisalign-lite-efficacy-retrospective | 3dd8ab44e169 | Meade described neutrally keyword belongs to adjacent sentence |
| 2026-07-18 | clear-aligner-indications-limitations | zhang-2025-clear-aligner-based-multidisciplinary | a04478037234 | Unlike compares evidence maturity Class II vs III |
| 2026-07-18 | clear-aligner-indications-limitations | ye-2025-combined-use-of-miniscrews | a04478037234 | Unlike contrasts Class II vs III maturity Ye described as case report |
| 2026-07-18 | osteotomy-drilling-heat-determinants-irrigation-overview | saxena-2024-guided-implant-drilling-bone-temperature | 64dd1e6d558f | overturns belongs to Rugova not Saxena |
| 2026-07-18 | osteotomy-drilling-heat-determinants-irrigation-overview | gehrke-2020-technique-drill-design-osteotomy | 19437370a583 | disagreement between constituent papers Gehrke and Di Fiore |
| 2026-07-18 | osteotomy-drilling-heat-determinants-irrigation-overview | di-fiore-2018-continuous-intermittent-drilling-temperature | 19437370a583 | constituent heterogeneity overview restates Di Fiore conclusion |
| 2026-07-18 | osteotomy-drilling-heat-determinants-irrigation-overview | jain-2024-heat-generation-pain-piezosurgery-drilling | 437c01ea75bf | contradiction is Stubinger already a contradicts edge in frontmatter |
| 2026-07-18 | wach-2026-emergence-angle-marginal-bone-loss | mikulas-2025-digital-impression-accuracy-peri-implant-emergence-profile-sr | df71e5a5c0dd | 반박 targets wide-emergence-angle dogma not Mikulas |
| 2026-07-18 | kindaro-2026-parathyroid-hormone-implant-osseointegration-osteoporosis-sr | drug-mronj-antiresorptive-overview | cc67c9b92cbc | PTH different drug class opposite mechanism rhetorical contrast |
| 2026-07-18 | surendra-2025-flapless-versus-flapped-crestal-bone | paknejad-2017-flapless-immediate-implant-buccal-gap-rct | 225f8c2cd218 | contradiction is Tarpara already in frontmatter Paknejad background |
| 2026-07-18 | surendra-2025-flapless-versus-flapped-crestal-bone | mansouri-2025-flapless-immediate-implant-bone-grafting-sr-ma | 225f8c2cd218 | Mansouri listed as related evidence no conflicting finding |
| 2026-07-18 | momand-2024-antibiotic-prophylaxis-early-implant-failure | uesugi-2024-risk-factors-early-failure-all-on-four | 20f2a903fe1b | Momand intervention vs Uesugi risk-factor different population |
| 2026-07-18 | francis-2024-low-serum-vitamin-d-early-implant-failure | moy-2005-dental-implant-failure-rates-risk | 94f0e4f3a3c2 | Moy 2005 general risk anchor with no vitamin D claim |
| 2026-07-18 | althobaiti-2023-osseodensification-conventional-drilling-isq-sr | osseodensification-clinical-applications | e25101662128 | contrast is mohammadi-2025 and shilpi-2025; althobaiti is supporting constituent |
| 2026-07-18 | oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma | zhang-2025-expert-consensus-km-augmentation-second-stage | 56c3b18848d0 | Unlike targets Sanz 2022 not Zhang 2025 prose pairs as complementary |
| 2026-07-18 | oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma | ravida-2022-keratinized-mucosa-width-peri-implant-disease-sr-ma | 56c3b18848d0 | Oh quantifies benefit explicitly complements Ravida risk-factor SR |
| 2026-07-18 | oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma | mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma | 56c3b18848d0 | same complements framing toward Mahardawi |
| 2026-07-18 | bragues-2024-oral-mucositis-children-cancer-management-sr | dean-2022-oral-chronic-gvhd-review | 2f14402f423a | Bragues fills coverage gap distinct disease entity |
| 2026-07-18 | adams-2022-clinical-evidence-alveolar-ridge-preservation | bone-regeneration-socket-biology-and-arp-critique | 7abd9578a077 | contradicting clause points at socket-preservation-arp-overview already refined |
| 2026-07-18 | nemec-2026-clear-aligner-patient-needs-expectations | alhuwaizi-2026-clear-aligner-fixed-oral-hygiene-periodontal-grade-sr | bd5a1c514a2a | patient-rated concern vs objective outcome different constructs |
| 2026-07-18 | monisha-2024-efficacy-of-clear-aligner | nakornnoi-2024-aligner-trimline-biomechanics-tooth-movement-sr | 758325e95548 | unlike contrasts monisha with aligner papers generally |
| 2026-07-18 | aucinaite-2025-naocl-chx-gutta-percha-cone-decontamination-sr | NOTARGET | c939683a1533 | methodological heterogeneity among in-vitro studies the review included |
| 2026-07-18 | shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment | NOTARGET | d492c21a34f1 | refutes generic literature-wide retrievability worry no counterpart page |
| 2026-07-18 | shim-2025-retrieval-ahplus-bioceramic-ceraseal-retreatment | NOTARGET | 3cf3d6370379 | same generic-concern refutation restated |
| 2026-07-18 | yeung-2023-functional-neuroplasticity-denture-rehabilitation-fmri | NOTARGET | ae6be4613b87 | task-dependent reversal within review own constituent fMRI studies |
| 2026-07-18 | ali-2023-conventional-minimally-invasive-veneers-sr | NOTARGET | 78f6ad61c743 | contradicts review own a-priori hypothesis not a wiki page |
| 2026-07-18 | ali-2023-conventional-minimally-invasive-veneers-sr | NOTARGET | ee875d6af28d | Korean restatement of T011 |
| 2026-07-18 | ali-2023-conventional-minimally-invasive-veneers-sr | NOTARGET | 2e52e9c39c61 | Key Contributions restatement; chandode-2026 agrees and has reinforces edge |
| 2026-07-18 | komine-2024-clinical-performance-laminate-veneers-review | NOTARGET | f59bec828338 | conflicting vitality findings among studies inside narrative review |
| 2026-07-18 | nelson-2011-text-vs-voice-reminder-pediatric-dental-rct | NOTARGET | 7ffaee61ec1e | generic assumption about text reminders concrete counterpart under T016 |
| 2026-07-18 | cangul-2026-full-pulpotomy-adoption-determinants-trainee-decision-making | NOTARGET | bfabf328c17f | internal Abstract-vs-Results inconsistency |
| 2026-07-18 | cangul-2026-full-pulpotomy-adoption-determinants-trainee-decision-making | NOTARGET | a3a5b99d5ef4 | same internal inconsistency in English prose |
| 2026-07-18 | team-feedback-system-johari | NOTARGET | 52ec8dbf4945 | staff-feedback operational advice no research counterpart |
| 2026-07-18 | garcia-2023-teledentistry-acceptability-latino-rural-virginia | NOTARGET | ff469fb34a28 | duplicate sentence edge recorded under T021 |
| 2026-07-18 | dioguardi-2024-abfraction-theory-controversy-scoping-review | NOTARGET | 42400211bb16 | refines edge to duangthip-2017 already exists in frontmatter |
| 2026-07-18 | dioguardi-2024-abfraction-theory-controversy-scoping-review | NOTARGET | 63a380af97bf | review own inconclusiveness plus already-edged Duangthip critique |
| 2026-07-18 | dioguardi-2024-abfraction-theory-controversy-scoping-review | NOTARGET | 01982b3b9fd6 | generic confirm-or-refute phrasing |
| 2026-07-18 | dioguardi-2024-abfraction-theory-controversy-scoping-review | NOTARGET | d0de7ab7fea0 | same confirm-or-refute plus already-edged critique |
| 2026-07-18 | wang-2019-fiber-posts-vs-metal-posts-severely-damaged | NOTARGET | d999c0e77328 | counters metal-post rigidity belief no held page asserts it |
| 2026-07-18 | devlin-2013-object-position-magnification-panoramic-radiography | NOTARGET | 790b29df278f | refutes textbook focal-trough assumption martins-2022 agrees reinforces edge exists |
| 2026-07-18 | willershausen-2025-low-field-mri-pediatric-dental | NOTARGET | f30fb79447d8 | contradicts edge to oenning-2019 already in frontmatter |
| 2026-07-18 | dioguardi-2020-management-instrument-sterilization-workflow-endodontics | NOTARGET | beee50ab39b7 | within-review heterogeneity wiki NiTi papers agree |
| 2026-07-18 | al-sulimman-2025-composite-amalgam-failure-risk-sr-ma | NOTARGET | 25381922e9d8 | contradicts edge to tobias-2024 already exists |
| 2026-07-18 | al-sulimman-2025-composite-amalgam-failure-risk-sr-ma | NOTARGET | 1fe8b9c8678d | Korean restatement of same existing edge |
| 2026-07-18 | al-sulimman-2025-composite-amalgam-failure-risk-sr-ma | NOTARGET | 76e4f54e465b | third restatement of same existing edge |
| 2026-07-18 | bubalo-2026-bone-substitutes-alveolar-ridge-augmentation | NOTARGET | 2c3895e464ed | heterogeneity inside narrative review domic-2023 corroborates |
| 2026-07-18 | lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma | NOTARGET | fd7a6e264bf0 | clinical-vs-preclinical internal discrepancy gaikwad-2022 confirms |
| 2026-07-18 | lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma | NOTARGET | 8e1db53e2658 | same claim as T039 restated in bottom line |
| 2026-07-18 | elgali-2017-guided-bone-regeneration-materials-mechanisms | NOTARGET | 8b3f1f5d2742 | porosity heterogeneity among review own in vivo studies left unresolved |
| 2026-07-18 | elgali-2017-guided-bone-regeneration-materials-mechanisms | NOTARGET | 826ea1e67aeb | Korean restatement of T041 |
| 2026-07-18 | elgali-2017-guided-bone-regeneration-materials-mechanisms | NOTARGET | 5fd32a1d4870 | review flags porosity as open question no claim asserted |
| 2026-07-18 | elgali-2017-guided-bone-regeneration-materials-mechanisms | NOTARGET | 305069daeeff | results-table cell summarizing disagreement across cited studies |
| 2026-07-18 | domic-2023-hyaluronic-acid-tooth-extraction-sr-ma | NOTARGET | 2a156e46c13b | more-bone-loss result from one study inside the SR no wiki HyA benefit claim |
| 2026-07-18 | domic-2023-hyaluronic-acid-tooth-extraction-sr-ma | NOTARGET | 3fc8ee65f65a | Korean restatement of T045 |
| 2026-07-18 | domic-2023-hyaluronic-acid-tooth-extraction-sr-ma | NOTARGET | e6d936100f29 | HyA gel adjunct vs scarano-2025 sinus fill different indication bubalo already applies-to |
| 2026-07-18 | sun-2025-3d-printed-scaffold-bone-defect-repair | NOTARGET | 1df1e373a5fc | porosity vs mechanical strength engineering tradeoff inside one review |
| 2026-07-18 | rokn-2011-bone-formation-two-grafting-materials | NOTARGET | fd631b5b345e | paper refutes its own a-priori hypothesis within one animal study |
| 2026-07-18 | souza-2020-citrus-sweets-enamel-erosion-invitro | NOTARGET | 698262302306 | refutes general pH-alone assumption barac-2015 agrees |
| 2026-07-18 | kiliaridis-2000-vertical-position-rotation-tipping-molars | NOTARGET | acfd106c9239 | refuted universal-overeruption belief is surveyed clinician belief edges already exist |
| 2026-07-18 | rani-2024-bite-registration-materials-vertical-relationship-accuracy | NOTARGET | d931f9c7c8d3 | source paper own internally inconsistent Discussion |
| 2026-07-18 | goldstein-2022-centric-relation-needed-reference-position | NOTARGET | 29fc8dd97f62 | keyword inside negation and contradicts edge to zonnenberg-2021 already exists |
| 2026-07-18 | goldstein-2022-centric-relation-needed-reference-position | NOTARGET | 5ce5f22f1f8c | contradicts edge to zonnenberg-2021 already in goldstein-2022 frontmatter |
| 2026-07-18 | goldstein-2022-centric-relation-needed-reference-position | NOTARGET | b5b48f799d28 | restates same existing contradicts edge |
| 2026-07-18 | goldstein-2022-centric-relation-needed-reference-position | NOTARGET | 3e8a485dbd3a | duplicate of already-recorded contradicts edge |
| 2026-07-18 | goldstein-2022-centric-relation-needed-reference-position | NOTARGET | cfe4e2e496a7 | general-literature claim that no clinical research contradicts CR |
| 2026-07-18 | goldstein-2022-centric-relation-needed-reference-position | NOTARGET | 991ed23dc6be | counterpoint role already captured by existing contradicts edge |
| 2026-07-18 | goldstein-2022-centric-relation-needed-reference-position | NOTARGET | 369b4dc0fa70 | literature-wide assertion not page-to-page conflict |
| 2026-07-18 | utz-2026-neuromuscular-position-tmj-condyle-dentate | NOTARGET | f9c2b512dc3c | page documents deliberate decision that Utz and Fukushima measure different constructs |
| 2026-07-18 | fornai-2022-centric-relation-matter-form-substance | NOTARGET | 8cee832141a4 | fornai-2022 already carries contradicts to zonnenberg-2021 |
| 2026-07-18 | maybodi-2022-periodontal-treatment-sle-disease-activity-rct | NOTARGET | a5575e33fcb8 | Fabbri et al not a wiki page no SLE periodontal trial page exists |
| 2026-07-18 | maybodi-2022-periodontal-treatment-sle-disease-activity-rct | NOTARGET | 0ef6ad0b935f | same missing counterpart |
| 2026-07-18 | cosin-villanueva-2024-micrornas-gingival-crevicular-fluid-periodontal | NOTARGET | b1c05f8e02e9 | heterogeneity among 16 case-control studies the review included |
| 2026-07-18 | fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr | NOTARGET | 8bf367e9f7c8 | contradicts edge to rasoolzadeh-2022 already present |
| 2026-07-18 | fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr | NOTARGET | 38a88007b2b7 | Korean restatement of same existing edge |
| 2026-07-18 | fernandez-2025-coenzyme-q10-nonsurgical-periodontal-sr | NOTARGET | ccbb5459ef3a | same disagreement already encoded bidirectionally |
| 2026-07-18 | ifrim-2026-edta-air-polishing-root-surface-sem | NOTARGET | 3aaeef0ebe91 | marks-versus-cracks tradeoff internal to single SEM study |
| 2026-07-18 | botelho-2022-umbrella-review-oral-systemic | NOTARGET | 8e5478a750ad | keyword inside negation fail-safe analysis |
| 2026-07-18 | botelho-2022-umbrella-review-oral-systemic | NOTARGET | b0b330339f11 | FSN sentence is internal robustness statistic |
| 2026-07-18 | rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma | NOTARGET | c7d8ae1a66a6 | contradicts edge to fernandez-2025 already exists |
| 2026-07-18 | rasoolzadeh-2022-coenzyme-q10-periodontitis-sr-ma | NOTARGET | d68bf8d523d1 | same already-encoded edge |
| 2026-07-18 | mendonca-2024-effects-probiotic-therapy-periodontal | NOTARGET | 51fd4617bb0d | conflicting evidence among SRs the umbrella included |
| 2026-07-18 | dasilveira-2026-subgingival-irrigation-chemical-agents-nspt-sr-ma | NOTARGET | 89b2489806e1 | Van der Sluijs 2016 has no page in wiki or sources |
| 2026-07-18 | mucogingival-surgery-apf-fgg-ctg | NOTARGET | b469f5c856e4 | rebuts 2mm keratinized textbook criterion no page asserts it |
| 2026-07-18 | ramirez-martinez-acitores-2020-antihypertensive-xerostomia-salivary-flow-sr | NOTARGET | 6c2727ce51e7 | refutes general drug-class assumption counterpart already refines-linked |
| 2026-07-18 | bisla-2022-odontogenic-infections-maxillary-sinus-changes | NOTARGET | 03a362622572 | contradicts Nunes et al not a wiki page in-wiki counterparts already edged |
| 2026-07-18 | pan-2025-acupuncture-neuropathic-orofacial-pain-review | NOTARGET | e13886b067dd | heterogeneity among narrative review own cited primaries |
| 2026-07-18 | pan-2025-acupuncture-neuropathic-orofacial-pain-review | NOTARGET | 166c5be077ac | Korean restatement TMD note agrees with held ma-2026 |
| 2026-07-18 | jkda-2025-63-8-006 | NOTARGET | a6fa51172c98 | historical organizational prose not evidential conflict |
| 2026-07-18 | zaki-2021-bone-substitute-materials-immediate-implant-sr-ma | NOTARGET | 70b1416ac617 | 상충 is glossed clinical trade-off esthetic vs complication |
| 2026-07-18 | lang-2012-immediate-implant-survival-success-sr | NOTARGET | 8a9eba9a90a4 | internal contrast survival vs unassessable success within same SR |
| 2026-07-18 | fan-2024-immediate-implant-ridge-preservation-comparative-sr-ma | NOTARGET | 1f032f652c5d | 상충 denotes within-paper benefit-risk tradeoff |
| 2026-07-18 | krishnakumar-2024-hvgic-composite-primary-teeth-sr | NOTARGET | c5180a3c26c9 | contradictory durability in wider unheld literature held GIC pages report equivalence |
| 2026-07-18 | krishnakumar-2024-hvgic-composite-primary-teeth-sr | NOTARGET | b8bf0b3698c3 | Korean restatement of T091 |
| 2026-07-18 | krishnakumar-2024-hvgic-composite-primary-teeth-sr | NOTARGET | 75731531b444 | heterogeneity across wider primary-teeth literature the review surveys |
| 2026-07-18 | krishnakumar-2024-hvgic-composite-primary-teeth-sr | NOTARGET | e49ad0ca3993 | same self-referential heterogeneity ali-eldin-2026 already reinforces |
| 2026-07-18 | panetta-2024-gic-longevity-umbrella-review | NOTARGET | ac5076ecfbe8 | GRADE conflicting-evidence label and disclosed COI among constituent SRs |
| 2026-07-18 | ge-2023-glass-ionomer-secondary-caries-sr-ma | NOTARGET | a96fbe6f81e7 | refutes legacy amalgam metal-content belief different comparator pair |
| 2026-07-18 | jung-2025-flossing-performance-plaque-removal | NOTARGET | 67607b7a4da3 | refutes poor-technique defense of floss worthington-2019 already reinforces |
| 2026-07-18 | jung-2025-flossing-performance-plaque-removal | NOTARGET | 476a10772354 | Korean restatement of T098 |
| 2026-07-18 | jung-2025-flossing-performance-plaque-removal | NOTARGET | 1fc263f15835 | within-study dissociation technique vs plaque removal |
| 2026-07-18 | hardan-2022-treatment-tooth-wear-using-direct | NOTARGET | c0432aa6930f | contradictory describes disagreement among 16 studies the SR reviewed |
| 2026-07-18 | varvara-2020-retightening-preload-loss-abutment-screws | NOTARGET | 883e7e530658 | contradicted guidance is Dixon 1995 and Bakaeen 2002 not ingested |
| 2026-07-18 | scheffel-2015-transdentinal-cytotoxicity-glutaraldehyde-odontoblast | NOTARGET | 6d6dfb9e6dd7 | in-vitro pulpal safety vs clinical efficacy different outcomes reinforces edge exists |
| 2026-07-18 | rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety | NOTARGET | 2cbe61cf9e31 | contrary to study hypothesis is internal null result |
| 2026-07-18 | rizzo-lorenzo-2020-influence-information-computerized-anesthesia-anxiety | NOTARGET | dad0830dd829 | Wang and Heaton not in wiki claim already covered by contradicts appukuttan-2016 |
| 2026-07-18 | karm-2023-clinical-practice-guidelines-diagnostic-procedural-sedation | NOTARGET | e0d5b91e208d | sedation guideline and position paper are complementary institutional documents |
| 2026-07-18 | khademi-2023-premedication-inferior-alveolar-nerve-block-pulpitis-umbrella | NOTARGET | 820448b08d0b | 상충 refers to JADAD algorithm the four SRs converged |
| 2026-07-18 | khademi-2023-premedication-inferior-alveolar-nerve-block-pulpitis-umbrella | NOTARGET | 16ab237ce69f | umbrella review own JADAD disagreement-resolution method |
| 2026-07-18 | khademi-2023-premedication-inferior-alveolar-nerve-block-pulpitis-umbrella | NOTARGET | 1313aa3ffbf6 | same internal methodology restated |
| 2026-07-18 | de-menezes-torres-2025-chatgpt-oral-maxillofacial-surgery | NOTARGET | 81ecbc48f990 | contradicts edge to hendrickx-2024 already declared |
| 2026-07-18 | peri-implant-emergence-profile-soft-tissue-conditioning-overview | NOTARGET | fedd92750059 | overview prose describing own constituents extending each other |
| 2026-07-18 | osseodensification-clinical-applications | NOTARGET | d5136308903f | overview noting heterogeneity across own 30-plus constituents |
| 2026-07-18 | osseodensification-clinical-applications | NOTARGET | 966cc6f88553 | contrasting paper is retracted and annotated evidence-void |
| 2026-07-18 | resin-light-curing-degree-of-conversion-overview | NOTARGET | ef938a8268c0 | pH vs radiopacity tradeoff between two cements inside one study |
| 2026-07-18 | resin-light-curing-degree-of-conversion-overview | NOTARGET | 1a23467104da | dual-cure vs flowable within same in-vitro comparison |
| 2026-07-18 | trigeminal-injury-neuropathic-pain-cascade-overview | NOTARGET | 4d2b132fdd74 | overview narrates clash between own constituents edge already on pan-2025 |
| 2026-07-18 | trigeminal-neuralgia-neuropathy-overview | NOTARGET | de95620a8572 | explicit negation Villegas-Diaz reinforces and does not overturn |
| 2026-07-18 | drug-analgesics-postop-pain-overview | NOTARGET | 94a6166a6886 | corticosteroid vs NSAID different drug classes complementary |
| 2026-07-18 | keratinized-mucosa-peri-implant-health-overview | NOTARGET | 0eed5cb12d75 | sentence explicitly resolves apparent contradiction as design difference |
| 2026-07-18 | veneer-preparation-design-minimally-invasive-overview | NOTARGET | 8e1d453003fe | refutes general conventional-veneer superiority assumption no page holds |
| 2026-07-18 | interdental-cleaning-devices-synthesis | NOTARGET | 2b400b3364e3 | refutes folk belief about flossing technique |
| 2026-07-18 | immediate-implant-infected-sites-decision | NOTARGET | 6d7dbc7ceeea | overview resolves Munoz-Camara vs Prati as differing definitions |
| 2026-07-18 | complete-denture-ovd-determination-overview | NOTARGET | b37de264013a | negation Khan 2023 RCT fails to overturn synthesis conclusion |
| 2026-07-18 | tmj-inflammatory-arthritis-overview | NOTARGET | f3100fda406f | overview reporting disease-specific ultrasound differences among own constituents |
| 2026-07-18 | tmj-inflammatory-arthritis-overview | NOTARGET | bfbe3437b9e6 | labelled hypothesis source states no comparative study exists |
| 2026-07-18 | tmj-inflammatory-arthritis-overview | NOTARGET | d01aa5958981 | summary restatement of same within-overview heterogeneity |
| 2026-07-18 | sinus-lift-lateral-2026-synthesis | NOTARGET | 7a8e34c87601 | keyword matched contraindication in mucosal-thickening prose |
| 2026-07-18 | sinus-lift-lateral-2026-synthesis | NOTARGET | 42564922021d | contradict is substring of contraindication |
| 2026-07-18 | periodontal-host-modulation-nutraceutical-adjuncts-overview | NOTARGET | f8fd01ce2ee6 | CoQ10 conflict is between constituents already bidirectionally edged |
| 2026-07-18 | periodontal-host-modulation-nutraceutical-adjuncts-overview | NOTARGET | 4392991a4bd4 | English reconciliation restating already-recorded contradiction |
| 2026-07-18 | bone-regeneration-socket-biology-and-arp-critique | NOTARGET | dcd65549632c | same edge found independently by second judge |
| 2026-07-18 | bone-regeneration-socket-biology-and-arp-critique | NOTARGET | b7e15e9fb98c | same counterpoint relation captured under T135 |
| 2026-07-18 | bone-regeneration-socket-biology-and-arp-critique | NOTARGET | 128cda3b2c58 | refutes belief that immediate placement preserves bone Araujo is the refuting evidence |
| 2026-07-18 | bone-regeneration-socket-biology-and-arp-critique | NOTARGET | 54c07980db87 | refutes flapless-preserves-ridge belief Araujo itself refutes it |
| 2026-07-18 | bone-regeneration-socket-biology-and-arp-critique | NOTARGET | fc9bd693770b | describes Kim 2020 and Park 2022 adjunct findings no contradiction |
| 2026-07-18 | bone-regeneration-socket-biology-and-arp-critique | NOTARGET | 8fac240f186e | checklist restatement of same counterpoint |
| 2026-07-18 | socket-shield-technique-overview | NOTARGET | 3e8f67a9aaf2 | negation new studies reinforce direction none overturns anchors |
| 2026-07-18 | zirconia-types-clinical-selection | NOTARGET | db97ff801b19 | refutes lay glaze-reduces-wear assumption held pages agree |
| 2026-07-18 | zirconia-types-clinical-selection | NOTARGET | 7eb63511a89c | Comba refutes textbook cubic-zirconia belief no page asserts |
| 2026-07-18 | occlusal-veneer-tooth-wear-erosion-overview | NOTARGET | 5f2d5db98ef7 | fatigue vs static ranking disagreement among own constituents |
| 2026-07-18 | occlusal-veneer-tooth-wear-erosion-overview | NOTARGET | 24ada61e6de0 | Sasse vs Essam thickness heterogeneity synthesized by design |
| 2026-07-18 | occlusal-veneer-tooth-wear-erosion-overview | NOTARGET | 89a56c8206d4 | duplicate open-question note within own evidence base |
| 2026-07-18 | endodontic-access-cavity-decision-tree | NOTARGET | 8a68e548c447 | conflicting MIA evidence refers to studies inside Kapetanaki review |
| 2026-07-18 | endodontic-access-cavity-decision-tree | NOTARGET | 92ae1f879efb | table cell restating within-literature heterogeneity |
| 2026-07-18 | endodontic-access-cavity-decision-tree | NOTARGET | 71cfaf53361d | same conflicting-evidence label in summary table |
| 2026-07-18 | high-insertion-torque-primary-stability-crestal-bone-overview | NOTARGET | 3cf341f2f192 | sign-reversal critique targets Lemos refines edge already exists |
| 2026-07-18 | high-insertion-torque-primary-stability-crestal-bone-overview | NOTARGET | ca9daedb8cd0 | overview contrasting harm and benefit among own six constituents |
| 2026-07-18 | high-insertion-torque-primary-stability-crestal-bone-overview | NOTARGET | 8bf8f889292b | describes limitations within papers the overview synthesizes |
| 2026-07-18 | high-insertion-torque-primary-stability-crestal-bone-overview | NOTARGET | 8aa5e0c9b970 | Korean mirror of T155 |
| 2026-07-18 | high-insertion-torque-primary-stability-crestal-bone-overview | NOTARGET | 5d551cde1cbc | explicitly framed as apparent disagreement the reframing resolves |
| 2026-07-18 | high-insertion-torque-primary-stability-crestal-bone-overview | NOTARGET | 2084cfca04b3 | states papers stop contradicting under reframing |
| 2026-07-18 | high-insertion-torque-primary-stability-crestal-bone-overview | NOTARGET | e16580fe441a | says Faot and Aldahlawi stop contradicting both already edged |
| 2026-07-18 | high-insertion-torque-primary-stability-crestal-bone-overview | NOTARGET | 08591bb00fa8 | refutes dose-response interpretation a general belief |
| 2026-07-18 | high-insertion-torque-primary-stability-crestal-bone-overview | NOTARGET | e005c60043c4 | Trisi refuted only mechanism not outcome both already refines-edged |
| 2026-07-18 | high-insertion-torque-primary-stability-crestal-bone-overview | NOTARGET | d46760d8581a | Trisi and Coyac can both be true on different beds both already edged |
| 2026-07-18 | high-insertion-torque-primary-stability-crestal-bone-overview | NOTARGET | 475f7bd99f07 | evidence-gap statement no held paper defines compression ceiling |
| 2026-07-18 | bone-graft-material-selection-matrix-overview | NOTARGET | 99e958a0c014 | 상충 is porosity vs strength engineering tradeoff |
| 2026-07-18 | tooth-wear-vdo-space-creation-overview | NOTARGET | 4e3d1d47831f | refutes clinical intuition about space-gaining axis |
| 2026-07-18 | tooth-wear-vdo-space-creation-overview | NOTARGET | 3200af39fb4d | confidence-tag line summarizing animal vs clinical divergence Wang edge exists |
| 2026-07-18 | tooth-wear-vdo-space-creation-overview | NOTARGET | 4905364d5b65 | same intuition-reversal framing |
| 2026-07-18 | tooth-wear-vdo-space-creation-overview | NOTARGET | 2414b748538c | heterogeneity among 16 studies Hardan reviewed |
| 2026-07-18 | tooth-wear-vdo-space-creation-overview | NOTARGET | b6f46cba3c4c | page states Wang and Zhang differ in species dose duration outcome |
| 2026-07-18 | tooth-wear-vdo-space-creation-overview | NOTARGET | 7fb076436e09 | overview narrating animal vs clinical design difference |
| 2026-07-18 | guided-robotic-accuracy-immediate-implant-overview | NOTARGET | 0fff31e4ab48 | Shirani own subgroup reversals refines edge already exists |
| 2026-07-18 | clinical-principles-100-master-distillation | NOTARGET | ccc1dd3d0470 | master distillation conflict lives in downstream overview already linked |
| 2026-07-18 | mandibular-canal-nutrient-canal-cbct-anatomy-overview | NOTARGET | d132df09d164 | self-described cluster-internal heterogeneity |
| 2026-07-18 | mandibular-canal-nutrient-canal-cbct-anatomy-overview | NOTARGET | a136e952bfd1 | Abdar-Esfahani vs Kumar already encoded |
| 2026-07-18 | mandibular-canal-nutrient-canal-cbct-anatomy-overview | NOTARGET | 5dd73f35f1fe | contested literature is within the cluster the overview reviews |
| 2026-07-18 | mandibular-canal-nutrient-canal-cbct-anatomy-overview | NOTARGET | a24bfa855490 | section heading for already-encoded contradiction |
| 2026-07-18 | mandibular-canal-nutrient-canal-cbct-anatomy-overview | NOTARGET | 33d5a27833c1 | prose notes the edge already exists |
| 2026-07-18 | complaint-management-pipeline-classification-expectation-response-education | NOTARGET | 620e014a5c9c | defensive tactics from contradictory patient demands inside one study |
| 2026-07-18 | digital-complete-denture-cost-consensus-overview | NOTARGET | 6fe933730c7f | contradiction real but edge to jafarpour-2024 already exists |
| 2026-07-18 | full-arch-fixed-four-vs-six-implants-overview | NOTARGET | b6a319e76b41 | clinical vs biomechanical tension among own five constituents |
| 2026-07-18 | full-arch-fixed-four-vs-six-implants-overview | NOTARGET | 25ac75425b9e | same tension restated in three-line summary |
| 2026-07-18 | oral-mucositis-cancer-therapy-overview | NOTARGET | a02ebb89494d | pediatric LLLT null vs adult data not held as a page |
| 2026-07-18 | oral-mucositis-cancer-therapy-overview | NOTARGET | 5285677e4927 | palifermin safety conflict among studies inside reviewed literature |
| 2026-07-18 | oral-mucositis-cancer-therapy-overview | NOTARGET | 7c6a0d4bfc9b | restatement of same intra-literature heterogeneity |
| 2026-07-18 | peri-implantitis-management-overview | NOTARGET | 802a2660d7da | refutes general diabetes belief self-hedged paper-level edge exists |
| 2026-07-18 | peri-implantitis-management-overview | NOTARGET | 4ebdfb21c0a5 | 반박 targets brand marketing claims no page asserts |
| 2026-07-18 | peri-implantitis-management-overview | NOTARGET | 2feafc3a3ddb | refutes textbook diabetes framing self-discounted as underpowered |
| 2026-07-18 | peri-implantitis-management-overview | NOTARGET | bbc4e3907425 | contradicts single-brand marketing claims |
| 2026-07-18 | direct-resin-restoration-adhesion-placement-overview | NOTARGET | 732f6d8d3622 | no page holds low-shrinkage-superior claim all agree |
| 2026-07-18 | direct-resin-restoration-adhesion-placement-overview | NOTARGET | e5ca6f601711 | bare section heading no claim |
| 2026-07-18 | periodontal-adjunctive-therapy-probiotics-pdt-overview | NOTARGET | 3a3d9b05df66 | Van der Sluijs not in wiki ramanauskaite agrees refines edge exists |
| 2026-07-18 | periodontal-adjunctive-therapy-probiotics-pdt-overview | NOTARGET | cd3490103783 | section heading framing Jungbauer as counterpoint to own constituents |
| 2026-07-18 | root-analogue-implants-overview | NOTARGET | 4e596b02f57c | contradicts edge to bose-2023 already exists |
| 2026-07-18 | healing-abutment-reuse-single-use-controversy-overview | NOTARGET | ed5cb3086a9a | overview narrating endpoint difference among own source_papers |
| 2026-07-18 | healing-abutment-reuse-single-use-controversy-overview | NOTARGET | f0e8019d8a9d | English restatement of same internal disagreement |
| 2026-07-18 | treatment-planning-decision-variability-overview | NOTARGET | f342e18b45de | abstract vs own Results section intra-paper defect |
| 2026-07-18 | periodontal-systemic-links-adjunct-homecare-evidence-overview | NOTARGET | ae8838049ffa | keyword in claim that findings are unlikely to be overturned |
| 2026-07-18 | cervical-composite-isolation-strategy-overview | NOTARGET | 9f325adeaa67 | clinical trade-off isolation depth vs periodontal health |
| 2026-07-18 | cervical-composite-isolation-strategy-overview | NOTARGET | c096bf1b4ad6 | duplicate of same trade-off |
| 2026-07-18 | diabetic-patient-immediate-implant-decision | NOTARGET | b1387b2613a3 | Andrade vs Al-Ansari already encoded as refines and applies-to |
| 2026-07-18 | obturation-length-outcome-overview | NOTARGET | 0161f40bfea3 | apparent Schaeffer vs Chugal conflict explicitly reconciled |
| 2026-07-18 | obturation-length-outcome-overview | NOTARGET | 78c46c826d38 | apparent contradiction between two external papers not in wiki |
| 2026-07-18 | veneer-material-survival-protocol-overview | NOTARGET | d91212894e43 | refutes textbook conventional-prep superiority |
| 2026-07-18 | periodontal-regenerative-platelet-concentrates-overview | NOTARGET | 36bfe84d1f3a | defect-geometry heterogeneity between constituents already refines-edged |
| 2026-07-18 | periodontal-regenerative-platelet-concentrates-overview | NOTARGET | 4d1461682ff9 | overview describing counter-evidence among own constituents |
| 2026-07-18 | gothic-arch-jaw-relation-recording-overview | NOTARGET | 5f32093e9c61 | reproducibility vs accuracy two-axes framing within one overview |
| 2026-07-18 | oral-microbiome-biofilm-dysbiosis-synthesis | NOTARGET | b68e5492b07a | prose restates already-present contradicts edge to scannapieco-2021 |
| 2026-07-18 | computerized-needle-free-anesthesia-delivery-overview | NOTARGET | 3f067ea33797 | refutes manufacturer marketing claim |
| 2026-07-18 | computerized-needle-free-anesthesia-delivery-overview | NOTARGET | c73b5db84f84 | adult vs pediatric context-dependence both already linked |
| 2026-07-18 | implant-length-selection-why-not-always-short | NOTARGET | 5201b601d4ce | Kim refutes lever-arm intuition both are constituents |
| 2026-07-18 | abutment-emergence-profile-peri-implant-tissue-overview | NOTARGET | c965d3b735cc | within-review heterogeneity plus explicit negation refines edge exists |
| 2026-07-18 | nsaid-osseointegration-impairment-overview | NOTARGET | a3c0394df324 | overview thesis on evidence-tier discordance among own six |
| 2026-07-18 | nsaid-osseointegration-impairment-overview | NOTARGET | 4d2c664a6d8e | 상충 labels weak human causal evidence inside own synthesis |
| 2026-07-18 | nsaid-osseointegration-impairment-overview | NOTARGET | 9a0c698aaf5b | same statement in three-line summary |
| 2026-07-18 | nsaid-osseointegration-impairment-overview | NOTARGET | 96b9b9ff006d | RCT vs cohort tension between papers this overview pools |
| 2026-07-18 | complete-denture-digital-overdenture-overview | NOTARGET | d78c0d1f0c1e | overturned SR by Ahmed not in wiki |
| 2026-07-18 | mandibular-anesthesia-failure-accessory-innervation-overview | NOTARGET | 65252a3d3126 | Stein refutes textbook mylohyoid teaching |
| 2026-07-18 | watanabe-toothpick-method-toothbrushing-synthesis | NOTARGET | 60ec22f09868 | counterpoint is naming confusion refines edge to el-haddad exists |
| 2026-07-18 | dbbm-bone-substitute-overview | NOTARGET | bc0620a0f5c2 | explicitly declares non-contradictory different PRF generations |
| 2026-07-18 | ceraseal-bioceramic-sealer-clinical-material-synthesis | NOTARGET | 21bd68d8d685 | Shim rebuts general retrievability fear no page asserts |
| 2026-07-18 | ceraseal-bioceramic-sealer-clinical-material-synthesis | NOTARGET | ad373b36a933 | same rebuttal in English |
| 2026-07-18 | single-vs-multivisit-endodontic-outcomes-overview | NOTARGET | 80b07e574efb | Rossi-Fedele small edge presented as supporting non-inferiority |
| 2026-07-18 | osteotomy-drilling-heat-determinants-irrigation-overview | NOTARGET | ee9c98cff7cd | Rugova rebuttal already encoded as refines |
| 2026-07-18 | osteotomy-drilling-heat-determinants-irrigation-overview | NOTARGET | 5ba7c6c28f33 | piezo rebuttal already encoded as contradicts stubinger-2015 |
| 2026-07-18 | osteotomy-drilling-heat-determinants-irrigation-overview | NOTARGET | 9f9c9464fea2 | peck-drilling self-correction using own constituents |
| 2026-07-18 | osteotomy-drilling-heat-determinants-irrigation-overview | NOTARGET | 930fb57d4517 | Korean mirror external clash already encoded |
| 2026-07-18 | ridge-split-expansion-technique-selection-overview | NOTARGET | e22f90a8ac66 | clinical vs preclinical caveat Lopez-Valverde raises about own evidence |
| 2026-07-18 | supportive-peri-implant-therapy-maintenance-overview | NOTARGET | 020fffdf1a61 | explicitly states no genuine contradiction across four papers |
| 2026-07-18 | vitamin-d-osseointegration-implant-overview | NOTARGET | 1e324b59084d | overview reconciling own eight constituents edge to francis-2024 exists |
| 2026-07-18 | flapless-vs-flapped-implant-surgery-overview | NOTARGET | 84c6e7b1bf9c | Araujo refutes general flapless belief |
| 2026-07-18 | flapless-vs-flapped-implant-surgery-overview | NOTARGET | dcf6f90387f0 | Surendra vs Tarpara already tagged contradicts bidirectionally |
| 2026-07-18 | flapless-vs-flapped-implant-surgery-overview | NOTARGET | bfa330c9b482 | English restatement of same Araujo refutation |
| 2026-07-18 | cr-co-micp-reference-position-debate | NOTARGET | b9a20a39b5ef | Rani contradicting own Tukey test intra-study |
| 2026-07-18 | cr-co-micp-reference-position-debate | NOTARGET | 32a2e3c939f9 | critiques weakness within two studies it reviews |
| 2026-07-18 | nccl-etiology-diagnosis-management-overview | NOTARGET | c9c89b64640a | overview summarizing SR disagreement on abfraction |
| 2026-07-18 | nccl-etiology-diagnosis-management-overview | NOTARGET | bea15c626e47 | overview thesis abfraction-sole-cause unproven among own papers |
| 2026-07-18 | nccl-etiology-diagnosis-management-overview | NOTARGET | b3ad65823345 | Korean digest restating same heterogeneity |
| 2026-07-18 | nccl-etiology-diagnosis-management-overview | NOTARGET | 68fcc0978716 | same SR-level split among constituents |
| 2026-07-18 | nccl-etiology-diagnosis-management-overview | NOTARGET | 337999b4bbfd | same unresolved abfraction conflict |
| 2026-07-18 | implant-macrogeometry-length-diameter-primary-stability-overview | NOTARGET | 3ad963f1f14b | Singh vs Kavitha genuine but contradicts edge already on Kavitha page |
| 2026-07-18 | implant-macrogeometry-length-diameter-primary-stability-overview | NOTARGET | 3121734d2728 | FEA studies disagreeing among themselves inside own evidence base |
| 2026-07-18 | implant-failure-mbl-risk-factors-overview | NOTARGET | cd8e03de4adb | overview reconciling own primary layer against umbrella reviews |
| 2026-07-18 | topical-anesthetic-injection-pain-overview | NOTARGET | a75087a035a6 | 상충 between two propositions the overview itself advances |
| 2026-07-18 | topical-anesthetic-injection-pain-overview | NOTARGET | 379bdd4f021c | same internal tension refines edge to karkoutly exists |
| 2026-07-18 | de-oliveira-2024-otc-bleaching-color-adverse-effects | NOTARGET | 9435a7a36363 | prose narrates contradicts edge to de Geus already present |
| 2026-07-18 | canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma | NOTARGET | bd668427d938 | contradictory results among four studies the review pooled |
| 2026-07-18 | canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma | NOTARGET | c06879f89822 | heterogeneity among four long-term studies the review pooled |
| 2026-07-18 | canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma | NOTARGET | f916c8e66a3b | generic summary sentence no external claim |
| 2026-07-18 | canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma | NOTARGET | 21945923af16 | caution flag about own long-term constituent evidence |
| 2026-07-18 | canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma | NOTARGET | b4427cbb139e | four included studies too heterogeneous to pool |
| 2026-07-18 | canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma | NOTARGET | a3668c62c932 | contradictory results among own included studies |
| 2026-07-18 | szabo-2022-all-on-four-tilted-distal-implants-mbl | NOTARGET | fe6f670d841e | pooled-SR counterpart already captured by contradicts mehta-2021 |
| 2026-07-18 | szabo-2022-all-on-four-tilted-distal-implants-mbl | NOTARGET | 74643e23b2b3 | Durkan not in wiki mehta-2021 already carries contradicts |
| 2026-07-18 | koyama-2025-single-vs-two-implant-mandibular-overdenture-sr-ma | NOTARGET | 7845f9121221 | overturned SR by Ahmed not held no page claims survival advantage |
| 2026-07-18 | koyama-2025-single-vs-two-implant-mandibular-overdenture-sr-ma | NOTARGET | 34504f453881 | overturned SR Ahmed not held no page asserts higher survival for 1-IOD |
| 2026-07-18 | mello-machado-2021-osseodensification-low-quality-bone-rct | NOTARGET | 36a98012e913 | self-critical note about own abstract vs insertion-torque data |
| 2026-07-18 | benic-2014-loading-protocols-single-implant-crowns-sr-ma | NOTARGET | d7c0f095c971 | contradictory recession evidence among RCTs this MA reviewed |
| 2026-07-18 | benic-2014-loading-protocols-single-implant-crowns-sr-ma | NOTARGET | a23cf5ea294f | same within-review inconsistency in Summary |
| 2026-07-18 | tarpara-2025-flapless-flapped-clinical-outcomes-cohort | NOTARGET | ffce936577a4 | real conflict with Surendra but contradicts edge already in frontmatter |
| 2026-07-18 | tarpara-2025-flapless-flapped-clinical-outcomes-cohort | NOTARGET | b3ce5c3ec7fc | Korean restatement same existing edge |
| 2026-07-18 | tarpara-2025-flapless-flapped-clinical-outcomes-cohort | NOTARGET | 82664d6ea7c7 | third restatement mirrored on Surendra page |
| 2026-07-18 | hussein-2019-thread-depth-implant-shape-stress-mandible-fea | NOTARGET | d127f5a16645 | 상충 is stability vs stress design tradeoff within one FEA |
| 2026-07-18 | wach-2026-emergence-angle-marginal-bone-loss | NOTARGET | 5a86c7e22904 | preclinical counterpoint is Strauss refines edge already exists |
| 2026-07-18 | ting-2017-surgical-patient-factors-affecting-marginal | NOTARGET | 445239f4d3a2 | conflicting results among SRs this umbrella pooled |
| 2026-07-18 | ting-2017-surgical-patient-factors-affecting-marginal | NOTARGET | 442e0a5e85f9 | same internal heterogeneity in Korean |
| 2026-07-18 | ting-2017-surgical-patient-factors-affecting-marginal | NOTARGET | a83b980f4b49 | evidence-table cell noting conflict across included SRs |
| 2026-07-18 | dambrosio-2023-systemic-diseases-medications-influence | NOTARGET | 7f4a5d00cc96 | diabetes results conflict among reviews d Ambrosio aggregated |
| 2026-07-18 | dambrosio-2023-systemic-diseases-medications-influence | NOTARGET | f9f05dfcd75d | explains away conflict as sampling artifact aligns with consensus |
| 2026-07-18 | stubinger-2015-piezosurgery-implant-dentistry | NOTARGET | 1ac140ad42a1 | same relation already captured by T290 and T291 |
| 2026-07-18 | pirc-2026-one-piece-two-piece-implants-15year-rct | NOTARGET | c1d831e27f19 | 상충 is biological vs technical tradeoff between two arms of one RCT |
| 2026-07-18 | sahoo-2024-finite-element-analysis-influence-implant | NOTARGET | 7ce3913cfb7b | counter to intuitive tilting assumption murat-2025 measures different outcome |
| 2026-07-18 | kavitha-2023-outcome-implant-diameter-length-distribution | NOTARGET | 2f9bbfea4b79 | counters textbook longer-implant assumption specific clash already encoded |
| 2026-07-18 | kavitha-2023-outcome-implant-diameter-length-distribution | NOTARGET | e20a79bcb93d | counter-direction FEA is singh-2024 whose edge already exists |
| 2026-07-18 | rugova-2024-thermal-evaluation-bone-drilling-sequential | NOTARGET | 0cd18bc1c25e | overturns implicit sequential-drilling belief no page asserts it |
| 2026-07-18 | rugova-2024-thermal-evaluation-bone-drilling-sequential | NOTARGET | 47e29393ab46 | refutes general assumption overview already links and bounds rugova |
| 2026-07-18 | kindaro-2026-parathyroid-hormone-implant-osseointegration-osteoporosis-sr | NOTARGET | a8bf5007a808 | counterpoint is complementary osteoanabolic branch already edged |
| 2026-07-18 | surendra-2025-flapless-versus-flapped-crestal-bone | NOTARGET | 549b02115084 | restates Tarpara conflict already a contradicts edge |
| 2026-07-18 | surendra-2025-flapless-versus-flapped-crestal-bone | NOTARGET | b0e52c29cc91 | Korean restatement of same edge |
| 2026-07-18 | surendra-2025-flapless-versus-flapped-crestal-bone | NOTARGET | 4c9aa7bc6de2 | RCT vs cohort counterpoint refers to Tarpara edge exists |
| 2026-07-18 | coyac-2019-preclinical-model-links-osseo-densification-misfit | NOTARGET | 37b0b89439b9 | refers to Trisi already refines-edged |
| 2026-07-18 | coyac-2019-preclinical-model-links-osseo-densification-misfit | NOTARGET | 6e81badac2d6 | explicitly states findings do not literally conflict |
| 2026-07-18 | coyac-2019-preclinical-model-links-osseo-densification-misfit | NOTARGET | 9c2325485cf5 | table row enumerating claims the paper does not make |
| 2026-07-18 | tennert-2024-direct-vs-indirect-composite-longevity-sr-ma | NOTARGET | 5937cf807c77 | Korean restatement of T309 |
| 2026-07-18 | tian-2015-paucity-nanolayering-mdp-resin-dentin | NOTARGET | e4ee49f59127 | refines edge to yoshihara-2011 already exists |
| 2026-07-18 | friele-2006-patient-expectations-fair-complaint | NOTARGET | 5ed1f35d241a | refutes general litigation-first assumption |
| 2026-07-18 | gillespie-2025-complaint-handlers-bind-defensive | NOTARGET | e875f5828963 | contradictory organisational demands is described mechanism |
| 2026-07-18 | gillespie-2025-complaint-handlers-bind-defensive | NOTARGET | bc6b401ecc94 | same structural bind contradicts edge to elias-2025 already exists |
| 2026-07-18 | gillespie-2025-complaint-handlers-bind-defensive | NOTARGET | 48523468ece3 | contradictory demands describes role conflict within studied organisations |
| 2026-07-18 | gillespie-2025-complaint-handlers-bind-defensive | NOTARGET | 011c5884d630 | same organisational-tension construct |
| 2026-07-18 | gillespie-2025-complaint-handlers-bind-defensive | NOTARGET | d3a103c49a06 | contradicts edge to elias-2025 already exists |
| 2026-07-18 | allison-2024-bioaerosols-airborne-transmission-dental-clinic | NOTARGET | 590e402610a5 | refutes general 5um airborne dogma lahdentausta already reinforces |
| 2026-07-18 | aiello-2025-tmj-arthritis-rheumatic-diseases-rehabilitative-pain-relief-sr | NOTARGET | c17fe2be7fdd | discrepancy between own abstract and results table |
| 2026-07-18 | aggarwal-2026-third-molar-extraction-tmj-pain | NOTARGET | c93257978000 | Damasceno not in wiki no page asserts extraction worsens TMD |
| 2026-07-18 | bernardi-2024-psoriatic-arthritis-tmj-pathogenesis-gender-differences | NOTARGET | 7059ff394e5a | contradiction among paper own cited sex-distribution literature |
| 2026-07-18 | chen-2022-interpretation-hba1c-analytical-methodology-hematology | NOTARGET | d44fbbcaaf51 | HbA1c vs fingerstick intra-patient lab discordance protocol |
| 2026-07-18 | khalilurrahman-2026-raas-inhibitor-statin-periodontal-status-sr-ma | NOTARGET | 4a76dfd44eca | contradictory findings between two RAAS studies inside this review |
| 2026-07-18 | momand-2024-antibiotic-prophylaxis-early-implant-failure | NOTARGET | bc14026ad723 | refers to prior SR+MAs generally edge to torof-2023 already exists |
| 2026-07-18 | torof-2023-antibiotic-dental-implant-procedures-sr-ma | NOTARGET | 48227c4528cf | contradicts prescribing habit momand already carries reciprocal edge |
| 2026-07-18 | watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma | NOTARGET | f28031f212c2 | contradicts US opioid prescribing custom not a wiki claim |
| 2026-07-18 | watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma | NOTARGET | 89bc798de782 | Korean restatement of same |
| 2026-07-18 | watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma | NOTARGET | 9b7cc5464657 | same claim in Summary no wiki counterpart |
| 2026-07-18 | zingel-2025-nsaids-cardiovascular-risk-inflammatory-arthritis | NOTARGET | 73cb9dff7b2b | population-specific qualification of general textbook fact |
| 2026-07-18 | chatzopoulos-2025-nsaid-early-dental-implant-failure-cohort | NOTARGET | 9e594c521cde | conflicting findings is heterogeneity in prior trials reinforces edge exists |
| 2026-07-18 | etikala-2019-nsaids-periodontal-implant-therapy-review | NOTARGET | b12e41c34003 | conflicting results among 9 periodontal studies the review included |
| 2026-07-18 | etikala-2019-nsaids-periodontal-implant-therapy-review | NOTARGET | e8a521458319 | Korean same within-review heterogeneity |
| 2026-07-18 | etikala-2019-nsaids-periodontal-implant-therapy-review | NOTARGET | 2d2b3da98694 | conflicting results among own constituent clinical studies |
| 2026-07-18 | etikala-2019-nsaids-periodontal-implant-therapy-review | NOTARGET | 3f5476f32bc9 | key-contribution restating internal heterogeneity |
| 2026-07-18 | ruggiero-2022-aaoms-mronj-position-paper-update | NOTARGET | 05d895a1acbb | evidence-absence statement AAOMS panel itself split |
| 2026-07-18 | patrono-2024-low-dose-aspirin-prevention-atherosclerotic | NOTARGET | d0ad766bd673 | 상충 is benefit-harm tradeoff within aspirin own profile |
| 2026-07-18 | mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma | NOTARGET | ac770dc88192 | refutes general belief all KM pages agree |
| 2026-07-18 | mahardawi-2023-lack-keratinized-mucosa-peri-implantitis-sr-ma | NOTARGET | eea586deab22 | contradicted view is general clinical belief no page holds |
| 2026-07-18 | monje-2025-surgical-implant-factors-peri-implant-diseases | NOTARGET | 3cea9059ef84 | refutes single-brand marketing |
| 2026-07-18 | pujarern-2024-biofilm-removal-implant-airflow-erythritol | NOTARGET | ca0b72dfdcd3 | refutes own a-priori larger-particle hypothesis |
| 2026-07-18 | pujarern-2024-biofilm-removal-implant-airflow-erythritol | NOTARGET | 515656b30512 | Korean restatement |
| 2026-07-18 | pujarern-2024-biofilm-removal-implant-airflow-erythritol | NOTARGET | 2e0a45752675 | key-contributions restatement |
| 2026-07-18 | francis-2024-low-serum-vitamin-d-early-implant-failure | NOTARGET | c2e95e4b09cd | internal reversal genuine counterpart edge to mohsen-2024 exists |
| 2026-07-18 | buzatu-2024-vitamin-d-osseointegration-human-studies-sr | NOTARGET | 040dbd798c15 | 상충 is conflicting VDR polymorphism among own included studies |
| 2026-07-18 | keller-2026-3d-printed-titanium-mesh-autologous-bone | NOTARGET | 5fe3dcac3f1c | contradicts edge to soares-2025 already present |
| 2026-07-18 | iwasa-2011-tio2-micro-nano-hybrid-biological-aging | NOTARGET | f9ed1c0122ba | contrast between study own experimental groups |
| 2026-07-18 | hasegawa-2020-meso-micro-nano-rough-titanium-surface | NOTARGET | 4a202f320ed7 | 상충 is proliferation-differentiation tradeoff |
| 2026-07-18 | witek-2020-boronized-surface-osseointegration | NOTARGET | d5f4f7a6b637 | contrary to generic in vitro boron predictions no page holds |
| 2026-07-18 | faot-2019-insertion-torque-mandibular-overdenture | NOTARGET | 2b640048380d | G3 paradox contradicts general linear assumption counterparts already edged |
| 2026-07-18 | faot-2019-insertion-torque-mandibular-overdenture | NOTARGET | 981e51c32aa0 | Korean restatement |
| 2026-07-18 | faot-2019-insertion-torque-mandibular-overdenture | NOTARGET | 8afa20a97fa8 | refutes osseocompression theory clash already edged from marconcini |
| 2026-07-18 | de-elio-2023-insertion-torque-resonance-frequency-tapered-parallel-implants | NOTARGET | c2dd91c3a5c9 | contradicts marketing assumption authors attribute to drill-diameter confound |
| 2026-07-18 | nandini-2022-cylindrical-vs-tapered-implant-isq | NOTARGET | 369bf97e772a | conflict real but edge already exists from kim-2009 to nandini-2022 |
| 2026-07-18 | lages-2018-isq-insertion-torque-correlation-sr | NOTARGET | 1794dfb8e798 | overturn already machine-readable as superseded_by tisci-2026 |
| 2026-07-18 | trisi-2011-high-low-implant-torque-histology-sheep | NOTARGET | 869c73ebb96c | refutes general osseocompression hypothesis counterpart edge exists |
| 2026-07-18 | al-ahmari-2022-osseodensification-conventional-low-density-jaw | NOTARGET | b9164f5bd86e | same relation as T364 one edge suffices |
| 2026-07-18 | bhatavadekar-2012-peri-implant-soft-tissue-management-narrative | NOTARGET | 4127f7be1d51 | acknowledges heterogeneity in KM literature naming no specific claim |
| 2026-07-18 | rios-osorio-2025-xcm-vs-ctg-fgg-implant-soft-tissue-sr-ma | NOTARGET | 1185e2c620ae | resolving prior contradictions already captured by extends and reinforces |
| 2026-07-18 | neves-2023-socket-shield-stress-distribution-fea | NOTARGET | ccd71fc99ed6 | biomechanical counterpoint already recorded as refines velasco-bohorquez |
| 2026-07-18 | deng-2024-posterior-open-wound-healing-immediate-implant | NOTARGET | cb6172314db8 | 상충관계 is colour vs fibrous-repair tradeoff between two arms |
| 2026-07-18 | nowzari-2022-migration-bovine-derived-xenograft-particles | NOTARGET | a6edef7e222c | refutes generic slow-turnover belief sartori edge already exists |
| 2026-07-18 | akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height | NOTARGET | af5486b03813 | restates already-present contradicts edge to maska-2017 |
| 2026-07-18 | akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height | NOTARGET | 628882abf0b6 | Korean of same |
| 2026-07-18 | akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height | NOTARGET | a884f023475a | key-contribution restating same |
| 2026-07-18 | sartori-2003-msfa-bio-oss-10year-case-report | NOTARGET | c507689879ce | restates already-present contradicts to mordenfeld-2010 |
| 2026-07-18 | sartori-2003-msfa-bio-oss-10year-case-report | NOTARGET | d0bb9d59b64f | Korean of same |
| 2026-07-18 | sartori-2003-msfa-bio-oss-10year-case-report | NOTARGET | a2bcac092803 | Summary restating same |
| 2026-07-18 | mordenfeld-2010-msfa-dpbb-biopsies-11year | NOTARGET | b232df1ea827 | refutes resorbable-graft marketing reciprocal edge exists |
| 2026-07-18 | abullais-2024-maxillary-sinus-membrane-lateral-wall-cbct | NOTARGET | 40c10a6bf9bb | refutes facial-morphotype surrogate hypothesis no page holds |
| 2026-07-18 | schriber-2019-pneumatisation-maxillary-sinus-tooth-loss | NOTARGET | 6743a6ea2c75 | refutes post-extraction pneumatisation belief overview already narrates pushback |
| 2026-07-18 | kato-2021-sinus-mucosa-ostium-involvement-septa | NOTARGET | 5161fd460e43 | counter to study own a-priori expectation about septa |
| 2026-07-18 | shenoy-2013-maxillary-antrolith-recurrent-sinusitis-case | NOTARGET | 6781aba11ad6 | severity-spectrum contrast reinforces edge to Tan already exists |
| 2026-07-18 | adams-2022-clinical-evidence-alveolar-ridge-preservation | NOTARGET | 65626287142b | counterpoint already encoded as contradicts avila-ortiz-2019 |
| 2026-07-18 | adams-2022-clinical-evidence-alveolar-ridge-preservation | NOTARGET | a30f29a279e6 | same restating existing edge |
| 2026-07-18 | cesar-2024-dental-zirconia-15years-material-processing | NOTARGET | b08487cd254f | 상충 is translucency-strength material tradeoff |
| 2026-07-18 | davoudi-2025-zirconia-abutments-biological-mechanical-esthetic | NOTARGET | b704788e8b6e | bench vs clinical internal contrast FEA counterpart already refines-edged |
| 2026-07-18 | elwyn-2025-shared-decision-making-primer-clinicians | NOTARGET | 4df7863ddcbc | 상충 denotes esthetic tradeoff in preference-sensitive decisions |
| 2026-07-18 | barber-2019-shared-decision-making-orthodontics | NOTARGET | 3662a9f7e4be | 상충 denotes esthetics vs function tradeoff |
| 2026-07-18 | bonetti-2018-general-health-promotion-dental-engage | NOTARGET | 105a0d2416e3 | refutes clinician assumption about patient offense |
| 2026-07-18 | kapetanaki-2021-access-cavity-designs-endodontic-review | NOTARGET | 5c40c03e88c2 | refutes general MIA-prognosis belief wiki pages concur |
| 2026-07-18 | cruz-2014-debris-apical-third-naocl-glyde-in-vivo | NOTARGET | ad38169676c3 | contrary to lubrication rationale counterpart already has contradicts edge |
| 2026-07-18 | lee-2026-residual-pericervical-apical-dentine-vertical | NOTARGET | 968ca7dd5216 | contrast with unnamed prior literature no page holds post-VRF risk claim |
| 2026-07-18 | monisha-2024-efficacy-of-clear-aligner | NOTARGET | 79cad19dabd8 | contradictory results between studies the SR pooled |
| 2026-07-18 | nucera-2022-composite-attachments-clear-aligners-sr | NOTARGET | 388b66ef763d | heterogeneity among trials the review pooled |
| 2026-07-18 | wang-2025-clear-aligner-premolar-extraction-3d-tooth-movement | NOTARGET | fb6dea827538 | overturned assumption is general literature belief |
| 2026-07-18 | tang-2025-evaluating-the-effectiveness-of-clear | NOTARGET | a8ce5f7bf060 | contradicts Trouten and Orthlieb not in wiki |
| 2026-07-18 | goncalves-2023-invisalign-upper-incisor-accuracy-sr | NOTARGET | 4ec49f2f65b6 | refutes common clinical assumption about aligner vertical movement |
| 2026-07-18 | zhuo-2026-the-roller-coaster-effect | NOTARGET | 79114cd3f593 | runs counter to naive intuition about crowding severity |
| 2026-07-18 | porporatti-2026-clear-aligners-bruxism-systematic-review | NOTARGET | f571933d5eff | inconsistent phasic findings among own included studies |
| 2026-07-18 | yassir-2022-cat-vs-fat-overview-systematic-reviews | NOTARGET | 34ba8a086164 | umbrella describes conflict among own constituent SRs alhamwi resolves it |
| 2026-07-18 | tabone-2026-clear-aligner-oral-microbiome-sr | NOTARGET | a3a6d0b093d4 | dissenting Wang is an included study not an ingested page |
| 2026-07-18 | tabone-2026-clear-aligner-oral-microbiome-sr | NOTARGET | 4b5c544bcc3b | 반론 refers to Wang an included study no such page in wiki |
| 2026-07-18 | tabone-2026-clear-aligner-oral-microbiome-sr | NOTARGET | 9ea31601383c | internal heterogeneity among the SR 12 included studies |
| 2026-07-18 | tabone-2026-clear-aligner-oral-microbiome-sr | NOTARGET | cd0d4b76803a | explicitly calls it internal contradiction in the evidence base |
| 2026-07-18 | tabone-2026-clear-aligner-oral-microbiome-sr | NOTARGET | c244b61ffc54 | Wang functional-metagenome has no counterpart page |
| 2026-07-18 | zarzar-2023-implants-radiotherapy-head-neck | NOTARGET | b16ca292d012 | 두 논문 방향성 일치를 명시하는 문장 reinforces 엣지와 부분 supersession 배너가 이미 존재 |
| 2026-07-18 | abada-2025-obturation-techniques-post-obturation-pain-rct | song-2022-sealer-based-obturation-epoxy-calcium-silicate-rct | bc20016c0adf | 검토 완료 — 엣지 부여함 (abada-2025-obturation-techniques-post-obturation-pain-rct --refines--> song-2022-sealer-based-obturation-epoxy-calcium-silicate-rct) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | mello-2017-immediate-fresh-extraction-vs-delayed-healed-socket-sr-ma | pommer-2021-maxillary-single-tooth-timing-protocols-sr-ma | 13e604c8dcb1 | 검토 완료 — 엣지 부여함 (mello-2017-immediate-fresh-extraction-vs-delayed-healed-socket-sr-ma --contradicts--> pommer-2021-maxillary-single-tooth-timing-protocols-sr-ma) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | pachipulusu-2018-primary-secondary-closure-third-molar | takadoum-2022-sutureless-socket-technique-third-molars | 6e5986c7ad52 | 검토 완료 — 엣지 부여함 (pachipulusu-2018-primary-secondary-closure-third-molar --contradicts--> takadoum-2022-sutureless-socket-technique-third-molars) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | francis-2024-low-serum-vitamin-d-early-implant-failure | miron-2025-vitamin-d-deficiency-early-implant-failure | 94f0e4f3a3c2 | 검토 완료 — 엣지 부여함 (francis-2024-low-serum-vitamin-d-early-implant-failure --refines--> miron-2025-vitamin-d-deficiency-early-implant-failure) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | nelson-2011-text-vs-voice-reminder-pediatric-dental-rct | NOTARGET | 597d9a69d45c | 검토 완료 — 엣지 부여함 (nelson-2011-text-vs-voice-reminder-pediatric-dental-rct --refines--> prasad-2012-sms-reminder-dental-attendance-rct) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | garcia-2023-teledentistry-acceptability-latino-rural-virginia | NOTARGET | 9f3a1a5445fe | 검토 완료 — 엣지 부여함 (garcia-2023-teledentistry-acceptability-latino-rural-virginia --refines--> lee-2024-teledentistry-utilisation-australia-sr-ma) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | abdar-esfahani-2013-mandibular-anterior-nutrient-canals | NOTARGET | d9b616812ae7 | 검토 완료 — 엣지 부여함 (abdar-esfahani-2013-mandibular-anterior-nutrient-canals --contradicts--> kaur-2019-evaluation-mandibular-anterior-nutrient) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | abdar-esfahani-2013-mandibular-anterior-nutrient-canals | NOTARGET | ae4fcf254fdd | 검토 완료 — 엣지 부여함 (abdar-esfahani-2013-mandibular-anterior-nutrient-canals --contradicts--> hasan-2022-prevalence-nutrient-canals-mandibular) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma | NOTARGET | a00ae3a3be4b | 검토 완료 — 엣지 부여함 (lopez-valverde-2025-bone-expansion-compaction-densification-narrow-crests-sr-ma --contradicts--> lima-monteiro-2024-osseodensification-biomechanics-histomorphometry-sr-ma) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | craddock-2007-overeruption-posterior-teeth-partial-occlusal | NOTARGET | 28268aa04296 | 검토 완료 — 엣지 부여함 (craddock-2007-overeruption-posterior-teeth-partial-occlusal --contradicts--> livas-2016-fixed-retention-unopposed-molar-overeruption) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | durrant-2024-gic-load-bearing-restorations-sr | NOTARGET | 985aaf68f8ed | 검토 완료 — 엣지 부여함 (durrant-2024-gic-load-bearing-restorations-sr --refines--> gizani-2026-restorative-mih-primary-permanent-molars-sr) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | yang-2015-auxiliary-resistance-marginal-fitness-short-molar | NOTARGET | 25ee7f7f2b7b | 검토 완료 — 엣지 부여함 (yang-2015-auxiliary-resistance-marginal-fitness-short-molar --refines--> roudsari-2011-auxiliary-features-resistance-short-molars-invitro) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | bone-regeneration-socket-biology-and-arp-critique | NOTARGET | acaa71c45075 | 검토 완료 — 엣지 부여함 (bone-regeneration-socket-biology-and-arp-critique --refines--> bone-regeneration-protocol-ladder) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | osteotomy-drilling-heat-determinants-irrigation-overview | NOTARGET | 2fc223e46f51 | 검토 완료 — 엣지 부여함 (osteotomy-drilling-heat-determinants-irrigation-overview --refines--> chauhan-2018-biomechanical-factors-heat-generation-osteotomy) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | kumar-2022-suture-versus-sutureless-third-molar-impactions | NOTARGET | 2ba617b78a35 | 검토 완료 — 엣지 부여함 (kumar-2022-suture-versus-sutureless-third-molar-impactions --contradicts--> takadoum-2022-sutureless-socket-technique-third-molars) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | sen-2024-sutureless-multiple-suture-third-molar-inflammation | NOTARGET | 1cbe3d01e666 | 검토 완료 — 엣지 부여함 (sen-2024-sutureless-multiple-suture-third-molar-inflammation --contradicts--> takadoum-2022-sutureless-socket-technique-third-molars) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | jain-2024-heat-generation-pain-piezosurgery-drilling | NOTARGET | a7383fece650 | 검토 완료 — 엣지 부여함 (jain-2024-heat-generation-pain-piezosurgery-drilling --contradicts--> stubinger-2015-piezosurgery-implant-dentistry) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | stubinger-2015-piezosurgery-implant-dentistry | NOTARGET | 2a0457f1fdb6 | 검토 완료 — 엣지 부여함 (stubinger-2015-piezosurgery-implant-dentistry --?--> ?) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | stubinger-2015-piezosurgery-implant-dentistry | NOTARGET | fb8d92ecfc35 | 검토 완료 — 엣지 부여함 (aquilanti-2023-heat-generation-initial-osteotomy --contradicts--> stubinger-2015-piezosurgery-implant-dentistry) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | tennert-2024-direct-vs-indirect-composite-longevity-sr-ma | NOTARGET | d0b3d33e71b0 | 검토 완료 — 엣지 부여함 (tennert-2024-direct-vs-indirect-composite-longevity-sr-ma --contradicts--> josic-2023-direct-indirect-resin-longevity-sr-ma) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | hong-2021-universal-adhesive-etching-modes-sr-ma | NOTARGET | 2baab64ff009 | 검토 완료 — 엣지 부여함 (hong-2021-universal-adhesive-etching-modes-sr-ma --contradicts--> doshi-2023-universal-adhesive-nccl-strategy-sr-ma) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | alghauli-2025-clinical-benefits-immediate-dentin-sealing | NOTARGET | 9b124d99aac6 | 검토 완료 — 엣지 부여함 (alghauli-2025-clinical-benefits-immediate-dentin-sealing --contradicts--> josic-2022-ids-postoperative-sensitivity-sr-ma) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | wang-2025-crown-vs-porcelain-inlay-cracked-teeth-rct | NOTARGET | 9c90594d49ba | 검토 완료 — 엣지 부여함 (wang-2025-crown-vs-porcelain-inlay-cracked-teeth-rct --contradicts--> ferracane-2023-cracked-tooth-registry-3year-network) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | al-ahmari-2022-osseodensification-conventional-low-density-jaw | NOTARGET | 488642b1b514 | 검토 완료 — 엣지 부여함 (al-ahmari-2022-osseodensification-conventional-low-density-jaw --refines--> althobaiti-2023-osseodensification-conventional-drilling-isq-sr) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-18 | araujo-2009-ridge-alterations-flap-vs-flapless | NOTARGET | 519cd24a758a | 검토 완료 — 엣지 부여함 (araujo-2009-ridge-alterations-flap-vs-flapless --reinforces--> lee-2018-flap-management-alveolar-ridge-preservation) 이 문장엔 wikilink가 없어 감사가 엣지 존재를 못 봄 |
| 2026-07-19 | nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy | tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva | e81a34e89337 | 키워드 2건 모두 오탐 — 하나는 Rab11 knockdown 벤치 반전 다른 하나는 contrasts with 화법; 두 논문은 saliva라는 단어만 공유하고 충돌 가능한 주장이 없음 |
| 2026-07-19 | momeni-2024-intraspecies-interactions-streptococcus-mutans | lueyar-2023-dynamic-interactions-between-candida-albicans | 545f8d90b54e | 대비는 연구 축이 다름을 표시(종내 vs 왕국간)이지 불일치가 아님; 서로 다른 균 다른 질문 공유 주장 없음 |
| 2026-07-19 | bone-regeneration-socket-biology-and-arp-critique | araujo-2009-ridge-alterations-flap-vs-flapless | ac7a2aebb7e5 | 반박 대상은 flapless가 ridge를 보존한다는 통설이고 Araujo 자신이 그걸 반박하는 쪽 — 오버뷰는 자기 spine 논문을 재서술할 뿐 |
| 2026-07-19 | treatment-planning-decision-variability-overview | zhang-2025-intentional-replantation-periapical-periodontitis-prognosis-sr-ma | 71cab2558df3 | 충돌은 Zhang의 풀링값과 제3논문 Dufey-Portilla가 인용한 88-98퍼센트 사이이며 오버뷰는 Zhang 수치를 그대로 채택함 |
| 2026-07-19 | tmd-management-evidence-ladder | tenorio-2026-ultrasonography-tmj-rheumatoid-arthritis-scoping-review | 1ad37f8423e7 | 뒤집힘은 성인 RA와 소아 JIA라는 서로 다른 인구집단 사이이고 tenorio 자신의 소견이며 이미 tenorio extends chana-2026으로 encoded |
| 2026-07-19 | sartori-2003-msfa-bio-oss-10year-case-report | rogova-2025-histomorphometric-non-decalcified-bone-substitute-sr | 63a0a2ed55c2 | 상충은 Sartori와 Mordenfeld 사이이며 그 엣지는 이미 존재 Rogova는 왜 두 연구가 다를 수 있는지 설명으로만 인용됨 |
| 2026-07-19 | lopez-silva-2025-post-extraction-bleeding-heparin | NOTARGET | 08d04b25a56e | 명시된 가이드라인 공백을 채우는 문장이며 기존 경구 항응고제 지속 합의와 정렬 — 관련 상대는 이미 extends reinforces로 연결됨 |
| 2026-07-19 | bone-regeneration-socket-biology-and-arp-critique | araujo-2009-ridge-alterations-flap-vs-flapless | c7616daaaf87 | 반박 대상은 flapless가 ridge를 보존한다는 통설이고 Araujo 자신이 그것을 반박하는 쪽 — 오버뷰가 자기 spine 논문을 재서술할 뿐 (표 행과 같은 판정 다른 문장) |
