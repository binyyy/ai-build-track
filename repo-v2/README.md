# AI Build Track (v2, zero-human)

A 15-minute-a-day self-study system. Tutor runs in Claude Code with file edits blocked in phase 1. Objective graders (ruff, mypy, pytest, coverage) run in CI. A separate reviewer agent lands in week 5. Simulated users, red team and grader calibration land in weeks 6 to 8.

## Daily
1. Open the Codespace. In the terminal: `claude`
2. Type: `/start-session`
3. Do the task in the editor. Run it in the terminal. Paste errors into Claude.
4. Commit yourself: `git add -A && git commit -m "W01 Mon" && git push`

## Weekly
- Friday: `/friday-ship`
- Saturday (optional): weekend block from the module
- Sunday: the program-health Action opens an issue. Read it before Monday.

## Commands
`/start-session` `/friday-ship` `/kata` (wk3+) `/simuser` (wk6+) `/calibrate` (wk7+) `/redteam` (wk8+) `/regression` (wk10+)

## Phases
`.tutor/phase` = 1 now. Change to 2 at week 7 and 3 at month 4, and put the dates in `.tutor/phase_dates.csv`. CI blocks early changes.

## Setup checklist
See SETUP-V2.md.
