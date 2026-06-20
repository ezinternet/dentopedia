#!/bin/bash
cd /Users/oracleneo/llm-wiki
mkdir -p wiki/implants/soft-tissue

git mv wiki/implants/oh-2024-keratinized-mucosa-augmentation-functioning-implants.md wiki/implants/soft-tissue/
git mv wiki/implants/sanz-martin-2022-buccal-soft-tissue-dehiscence-implant.md wiki/implants/soft-tissue/
git mv wiki/implants/kim-2009-peri-implant-mucosa-blood-vessels-flap-flapless.md wiki/implants/soft-tissue/
git mv wiki/implants/tavelli-2025-soft-tissue-dehiscences-implant-sites-pstd.md wiki/implants/soft-tissue/
git mv wiki/implants/kim-2009-blood-vessels-peri-implant-mucosa.md wiki/implants/soft-tissue/
git mv wiki/implants/valles-2022-soft-tissue-augmentation-tissue-thickness-mucosal.md wiki/implants/soft-tissue/
git mv wiki/implants/thoma-2018-soft-tissue-augmentation-periimplant-health-review.md wiki/implants/soft-tissue/
git mv wiki/implants/raghoebar-2021-profilometric-mucosa-soft-tissue-augmentation.md wiki/implants/soft-tissue/
git mv wiki/implants/tavelli-2021-soft-tissue-phenotype-modification-peri-implant.md wiki/implants/soft-tissue/
git mv wiki/implants/zwanzig-2025-titanium-pins-fgg-arf-vestibuloplasty.md wiki/implants/soft-tissue/
git mv wiki/implants/sanz-2022-keratinized-mucosa-around-implants-consensus.md wiki/implants/soft-tissue/
git mv wiki/implants/yadav-2025-soft-tissue-substitutes-patient-reported-outcomes.md wiki/implants/soft-tissue/
git mv wiki/implants/dadlani-2024-efficacy-xenogeneic-collagen-matrices-keratinized.md wiki/implants/soft-tissue/
git mv wiki/implants/stefanini-2023-soft-tissue-augmentation-peri-implant-stable-sr.md wiki/implants/soft-tissue/
git mv wiki/implants/cairo-2019-soft-tissue-augmentation-implant-sites-review.md wiki/implants/soft-tissue/
git mv wiki/implants/montero-2022-soft-tissue-substitutes-vs-autogenous-systematic.md wiki/implants/soft-tissue/
git mv wiki/implants/zhang-2025-expert-consensus-km-augmentation-second-stage.md wiki/implants/soft-tissue/
git mv wiki/implants/bassetti-2016-soft-tissue-augmentation-second-stage-surgery.md wiki/implants/soft-tissue/
git mv wiki/implants/jensen-2023-iti-consensus-bone-dimensions-soft-tissue.md wiki/implants/soft-tissue/
git mv wiki/implants/thoma-2021-soft-tissue-management-implants-eao-consensus.md wiki/implants/soft-tissue/
git mv wiki/implants/bhatavadekar-2012-peri-implant-soft-tissue-management-review.md wiki/implants/soft-tissue/

echo "soft-tissue 이동 완료: $(ls wiki/implants/soft-tissue | wc -l)편"
