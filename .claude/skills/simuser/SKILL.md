---
name: simuser
description: Simulated-user triage (week 6+). Walks Bin through the worst transcripts.
---
1. Read the latest transcripts in transcripts/ (or the weekly artifact).
2. Pick the 3 worst. For each, Bin labels the failure type: misunderstood intent, hallucinated policy, unsafe advice, scope breach, PHI handling, tone.
3. Bin names the root cause layer: prompt, context, retrieval, or tool.
4. Bin writes one eval case per failure. Log in PROGRESS.md.
