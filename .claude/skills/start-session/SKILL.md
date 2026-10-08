---
name: start-session
description: Start every AI Build Track session. Runs retrieval, applies health adjustments, sets the 15-minute objective.
---
1. Run `python tools/due.py`. If output is empty, say "no retrieval due".
2. Ask each due item verbatim, one at a time. Wait for Bin's answer. Grade pass/fail strictly. Record each with `python tools/due.py --record <id> <pass|fail>`.
3. Open the newest file in reports/health/ if any. Quote its Adjustments section. Apply it.
4. Read the last 3 PROGRESS.md entries and the current week's file in modules/.
5. State: today's objective, the AI concept it serves, fade level, exit criterion, and the branch or PR it lands in.
6. Remind the phase rules from CLAUDE.md. Then begin.
