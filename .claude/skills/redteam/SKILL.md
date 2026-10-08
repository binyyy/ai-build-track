---
name: redteam
description: Red-team triage (week 8+). Reviews promptfoo results and plans defenses.
---
1. Read reports/redteam.json. List successful attacks by plugin and strategy.
2. For each success Bin writes: attack family, why the defense failed, which layer to change (prompt, input filter, tool permission, output check, data scope).
3. Bin makes the change by hand. Re-run before closing. Log ASR before and after.
