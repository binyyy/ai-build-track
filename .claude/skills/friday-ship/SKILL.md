---
name: friday-ship
description: Friday protocol: ship criteria check, 5-bullet teach-back graded, retrieval questions added to the queue.
---
1. Run retrieval as in /start-session.
2. Open this week's module. Check each Friday ship criterion with evidence (file, commit sha, CI run, output). Mark pass or fail.
3. Ask Bin for the 5-bullet teach-back from memory. Grade each bullet 0, 0.5 or 1.0. Quote wrong phrases, give the corrected version. Log misconceptions.
4. Append the module's retrieval questions to .tutor/retrieval.csv (box 0, today's date), one row each: id,prompt,box,last_date.
5. Apply the scoring rule from .tutor/rubric.md. Write the PROGRESS.md entry.
