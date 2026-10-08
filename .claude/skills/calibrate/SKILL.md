---
name: calibrate
description: Grader calibration (week 7+). Bin adjudicates grader A vs B disagreements blind.
---
1. Read up to 10 items from evals/queue/ where grader A and grader B disagree.
2. Show the item only. Bin labels it blind. Then show both grader rationales.
3. Bin writes label plus one-line reason into evals/adjudications/<YYYY-WW>.jsonl himself. You never edit that folder.
4. Bin runs `python evals/calibrate.py` (built in week 7). Log kappa in PROGRESS.md.
