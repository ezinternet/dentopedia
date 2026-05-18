#!/usr/bin/env bash
# llm-wiki PDF ingest watcher
# Monitors /Users/oracleneo/llm-wiki root for new PDFs
# Automatically calls claude CLI to ingest them

WIKI_DIR="/Users/oracleneo/llm-wiki"
PAPERS_DIR="$WIKI_DIR/papers"
LOG_FILE="$WIKI_DIR/.claude/scripts/ingest-watcher.log"
CLAUDE_BIN="/Users/oracleneo/.local/bin/claude"

# Skip list - files that are not papers
SKIP_LIST=(
  "Manual_Wiki"
  "5-ext_ridge_pres"
  "Prot_SAP_000"
  "Cone beam CT"
)

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

is_skippable() {
  local filename="$1"
  for skip in "${SKIP_LIST[@]}"; do
    if [[ "$filename" == *"$skip"* ]]; then
      return 0
    fi
  done
  return 1
}

is_already_ingested() {
  local filename="$1"
  local basename="${filename%.pdf}"
  # Check if any file in papers/ matches (loose check on basename)
  if ls "$PAPERS_DIR/"*.pdf 2>/dev/null | xargs -I{} basename {} .pdf | grep -qF "$basename"; then
    return 0
  fi
  return 1
}

process_pdf() {
  local filepath="$1"
  local filename
  filename=$(basename "$filepath")

  log "New PDF detected: $filename"

  # Skip non-papers
  if is_skippable "$filename"; then
    log "Skipping (not a paper): $filename"
    return
  fi

  # Skip if already in papers/
  if is_already_ingested "${filename%.pdf}"; then
    log "Already ingested: $filename"
    return
  fi

  # macOS notification
  osascript -e "display notification \"$filename\" with title \"llm-wiki: 새 논문 감지 → ingest 시작\"" 2>/dev/null

  log "Starting ingest for: $filename"

  # Call claude CLI in the wiki directory
  cd "$WIKI_DIR" || exit 1
  "$CLAUDE_BIN" --dangerously-skip-permissions -p \
    "New PDF found in llm-wiki root: \"$filepath\". Please ingest it now: copy to papers/ with proper stem, write sources/{stem}.md, write wiki/{category}/{stem}.md, update index.md, delete original. Follow CLAUDE.md rules exactly." \
    >> "$LOG_FILE" 2>&1

  local exit_code=$?
  if [ $exit_code -eq 0 ]; then
    log "Ingest complete: $filename"
    osascript -e "display notification \"$filename\" with title \"llm-wiki: ingest 완료 ✅\"" 2>/dev/null
  else
    log "Ingest failed (exit $exit_code): $filename"
    osascript -e "display notification \"$filename 처리 실패 - 수동 확인 필요\" with title \"llm-wiki: ingest 오류 ⚠️\"" 2>/dev/null
  fi
}

log "=== llm-wiki ingest watcher started ==="
log "Watching: $WIKI_DIR"

# Watch for new PDF files in wiki root (depth 1 only)
/opt/homebrew/bin/fswatch \
  --event Created \
  --event Renamed \
  --event MovedTo \
  --latency 2 \
  --exclude ".*/papers/.*" \
  --exclude ".*/wiki/.*" \
  --exclude ".*/sources/.*" \
  --exclude ".*/graphify-out/.*" \
  --exclude ".*/\..*" \
  --include ".*\.pdf$" \
  --recursive \
  "$WIKI_DIR" \
| while read -r changed_path; do
    # Only process PDF files in the root directory
    dir=$(dirname "$changed_path")
    if [ "$dir" = "$WIKI_DIR" ] && [[ "$changed_path" == *.pdf ]]; then
      # Wait briefly for file to be fully written
      sleep 3
      if [ -f "$changed_path" ]; then
        process_pdf "$changed_path"
      fi
    fi
  done
