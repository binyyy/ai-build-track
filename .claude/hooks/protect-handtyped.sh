#!/usr/bin/env bash
# Blocks Claude edits to hand-typed files. Exit 2 = block, stderr goes back to Claude.
input="$(cat)"
path="$(printf '%s' "$input" | python3 -c 'import sys,json;d=json.load(sys.stdin);print(d.get("tool_input",{}).get("file_path",""))')"
phase="$(cat "$CLAUDE_PROJECT_DIR/.tutor/phase" 2>/dev/null || echo 1)"
case "$path" in
  *PROGRESS.md|*/.tutor/*|*/katas/*) exit 0 ;;
  */prompts/*|*/evals/adjudications/*|*/evals/graders/*)
    echo "Blocked: prompts, graders and adjudications are Bin-only in every phase." >&2; exit 2 ;;
  *.py|*.sql|*/.github/*)
    if [ "$phase" -lt 3 ]; then
      echo "Blocked: phase $phase. Bin types source by hand. Give a hint, not code." >&2; exit 2
    fi ;;
esac
exit 0
