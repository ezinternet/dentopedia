#!/usr/bin/env bash
# llm-wiki 주간 근거 다이제스트 러너 (launchd 매주 월 09:00 구동).
# scripts/build-weekly-digest.py를 실행해 logs/{date}_weekly-digest.md 를 생성한다.
# 무인 git push는 하지 않는다 — 생성만 하고, 원장이 확인 후 단톡방에 붙여넣거나 커밋.
# launchd plist: ~/Library/LaunchAgents/com.llmwiki.weekly-digest.plist

set -euo pipefail
export PATH="/opt/homebrew/bin:/Users/oracleneo/.local/bin:/usr/local/bin:/usr/bin:/bin"
WIKI_DIR="/Users/oracleneo/llm-wiki"
LOG_FILE="$WIKI_DIR/.claude/scripts/weekly-digest.log"
cd "$WIKI_DIR"

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] weekly-digest start"
  python3 scripts/build-weekly-digest.py --days 7
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] → logs/$(date +%Y-%m-%d)_weekly-digest.md 생성 완료 (단톡방에 복붙 가능)"
} >> "$LOG_FILE" 2>&1
