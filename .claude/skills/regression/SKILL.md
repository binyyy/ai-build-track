---
name: regression
description: Planted prompt regression (week 10+). Bin must catch a subtle prompt change via evals and transcripts.
---
1. Create branch regress/<YYYY-WW>. Copy one prompt into prompts/regress_copies/ (Bin applies the swap by hand).
2. Describe ONE subtle change to make: remove a constraint, reorder few-shots, loosen a schema, drop tenant scoping.
3. Bin runs evals and reads transcripts and names the regression before diffing.
4. If evals did not catch it, the first task is a new eval case. Log caught yes/no in PROGRESS.md.
