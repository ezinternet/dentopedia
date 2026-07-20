#!/usr/bin/env bash
set -euo pipefail

# Netlify build entrypoint — mirrors .github/workflows/deploy-pages.yml build steps
# (everything before actions/upload-pages-artifact). Runs from repo root.

echo "--- env check ---"
python3 --version || echo "WARNING: python3 not found"
node --version
git log --oneline | wc -l | xargs echo "git history commit count:"
echo "-----------------"

STAMP=$(TZ='Asia/Seoul' date '+%Y-%m-%d %H:%M KST')
PAPER_COUNT=$(ls sources/*.md 2>/dev/null | wc -l | tr -d ' ')
OVERVIEW_COUNT=$(ls wiki/overviews/*.md 2>/dev/null | wc -l | tr -d ' ')
CATEGORY_COUNT=$(find wiki -mindepth 1 -maxdepth 2 -type d | grep -v overviews | wc -l | tr -d ' ')
INTERACTIVE_COUNT=$(ls interactives/*.html 2>/dev/null | grep -v 'wiki-evolution\|wiki-growth\|wiki-stats\|overviews-map\|contradiction-radar\|index\.html' | wc -l | tr -d ' ')
LECTURE_COUNT=$(ls lectures/*.html 2>/dev/null | grep -v 'index\.html' | wc -l | tr -d ' ')
DEBATE_COUNT=$(grep -oE '<b>[0-9]+</b> 논쟁' interactives/contradiction-radar.html 2>/dev/null | head -1 | grep -oE '[0-9]+' || echo 0)

sed -i "s|<!-- LAST_UPDATED -->.*<!-- /LAST_UPDATED -->|<!-- LAST_UPDATED -->${STAMP}<!-- /LAST_UPDATED -->|" wiki/index.md
sed -i "s|<!-- PAPER_COUNT -->.*<!-- /PAPER_COUNT -->|<!-- PAPER_COUNT -->${PAPER_COUNT}<!-- /PAPER_COUNT -->|" wiki/index.md
sed -i "s|<!-- OVERVIEW_COUNT -->.*<!-- /OVERVIEW_COUNT -->|<!-- OVERVIEW_COUNT -->${OVERVIEW_COUNT}<!-- /OVERVIEW_COUNT -->|" wiki/index.md
sed -i "s|<!-- CATEGORY_COUNT -->.*<!-- /CATEGORY_COUNT -->|<!-- CATEGORY_COUNT -->${CATEGORY_COUNT}<!-- /CATEGORY_COUNT -->|" wiki/index.md
sed -i "s|<!-- INTERACTIVE_COUNT -->.*<!-- /INTERACTIVE_COUNT -->|<!-- INTERACTIVE_COUNT -->${INTERACTIVE_COUNT}<!-- /INTERACTIVE_COUNT -->|" wiki/index.md
sed -i "s|<!-- LECTURE_COUNT -->.*<!-- /LECTURE_COUNT -->|<!-- LECTURE_COUNT -->${LECTURE_COUNT}<!-- /LECTURE_COUNT -->|" wiki/index.md
sed -i "s|<!-- DEBATE_COUNT -->.*<!-- /DEBATE_COUNT -->|<!-- DEBATE_COUNT -->${DEBATE_COUNT}<!-- /DEBATE_COUNT -->|" wiki/index.md

python3 scripts/build-category-map.py

rm -rf quartz/content
mkdir -p quartz/content
cp -r wiki/. quartz/content/

(cd quartz && npm ci && npx quartz build)

python3 scripts/build-overviews-map.py
python3 scripts/build-contradiction-radar.py
python3 scripts/build-wiki-stats.py
python3 scripts/build-interactives-index.py
python3 scripts/interactive-staleness.py || true

mkdir -p quartz/public/interactives
cp -r interactives/. quartz/public/interactives/

python3 scripts/build-lectures-index.py

mkdir -p quartz/public/lectures
cp -r lectures/. quartz/public/lectures/

cp robots.txt quartz/public/robots.txt

echo "Build complete: quartz/public"
