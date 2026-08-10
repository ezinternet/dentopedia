#!/usr/bin/env bash
#
# ingest-watcher.sh — llm-wiki PDF ingest watcher (launchd-managed).
#
# WHAT: fswatch-es the llm-wiki root (depth 1) for new PDFs and hands each one to the
# claude CLI to run the full CLAUDE.md ingest pipeline (papers/ → sources/ → wiki/ →
# index.md → qmd re-index → per-file commit → push). KeepAlive=true, so launchd keeps
# the watcher alive across crashes and reboots.
#
# Managed by: ~/Library/LaunchAgents/com.llmwiki.ingest-watcher.plist
# Tracked copy of that plist: .claude/scripts/com.llmwiki.ingest-watcher.plist
#   (launchd only reads ~/Library/LaunchAgents — the in-repo copy is the versioned
#    master; edit it there, then re-install with the cp below.)
#
# Install:    cp .claude/scripts/com.llmwiki.ingest-watcher.plist ~/Library/LaunchAgents/
#             launchctl load -w ~/Library/LaunchAgents/com.llmwiki.ingest-watcher.plist
# Stop it:    launchctl unload ~/Library/LaunchAgents/com.llmwiki.ingest-watcher.plist
# Watch it:   tail -f .claude/scripts/ingest-watcher.log
# Is it on?:  launchctl list | grep ingest-watcher     # also: pgrep -fl fswatch
#
# NOTE: this job auto-ingests UNATTENDED — it invokes the claude CLI with
# --dangerously-skip-permissions and pushes to origin/main without review. Load it only
# when you actually want every PDF dropped in the wiki root to ingest itself. As of
# 2026-07-16 the job is NOT loaded (plist present, launchctl list shows nothing);
# ingests are being run on demand instead. Loading it is a deliberate decision, not a
# repair step.
#
# DEPENDS: fswatch (/opt/homebrew/bin/fswatch — `brew install fswatch`) and the claude
# CLI at $CLAUDE_BIN below. Both are outside this repo; a fresh machine needs them
# installed before this agent does anything.

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
    "New PDF found in llm-wiki root: \"$filepath\". Ingest it now following CLAUDE.md exactly. (1) Step 0 gate: extract DOI, grep sources/ for duplicate, and check for retraction — abort with a log note if either fails. (2) Copy to papers/ with the proper stem, write sources/{stem}.md (include the mandatory ## Why Ingested section with at least one [[wikilink]]), write wiki/{category}/{stem}.md (bilingual One-line Summary + 한줄요약), update index.md, and delete the original PDF from the root. (3) Refresh search: export PATH=\"/opt/homebrew/bin:\$PATH\" && cd /Users/oracleneo/llm-wiki && qmd update && qmd embed. (4) Commit per-file per CLAUDE.md — each wiki page as 'wiki: {category}/{stem}', each source as 'source: {stem}', index.md as its own commit, every commit ending with the trailer 'Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>'. (5) Run: git push origin main. Follow CLAUDE.md rules exactly." \
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
