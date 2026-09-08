#!/usr/bin/env bash
# llm-wiki 주간 근거 다이제스트 러너 (launchd 매주 월 09:00 구동).
# 1) build-weekly-digest.py → logs/{date}_weekly-digest.md
# 2) build-team-card.py    → interactives/{date}_team-weekly-card.html
# 무인 git push는 하지 않는다 — 생성만 하고, 원장이 확인 후 단톡방에 공유하거나 커밋.
# launchd plist: ~/Library/LaunchAgents/com.llmwiki.weekly-digest.plist

set -euo pipefail
export PATH="/opt/homebrew/bin:/Users/oracleneo/.local/bin:/usr/local/bin:/usr/bin:/bin"
WIKI_DIR="/Users/oracleneo/llm-wiki"
LOG_FILE="$WIKI_DIR/.claude/scripts/weekly-digest.log"
cd "$WIKI_DIR"

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] weekly-digest start"
  python3 scripts/build-weekly-digest.py --days 7
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] → logs/$(date +%Y-%m-%d)_weekly-digest.md 생성 완료"
  python3 scripts/build-team-card.py
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] → interactives/$(date +%Y-%m-%d)_team-weekly-card.html 생성 완료 (팀 채팅에 공유 가능)"
} >> "$LOG_FILE" 2>&1
