---
name: kata
description: Weekly planted-bug kata (week 3+). Plants one bug in a copy, times Bin's fix.
---
1. Create branch kata/<YYYY-WW>. Copy one small source file to katas/<YYYY-WW>/<name>.py.kata (Bin renames it by hand).
2. Introduce ONE realistic bug (off-by-one, wrong sort key, None not handled, wrong dict key, tenant filter dropped).
3. Write katas/<YYYY-WW>/KATA.md with the symptom only (what a user would see), never the cause.
4. Append the sha256 of "file:line:cause" to .tutor/kata_answers.csv. Do not reveal it.
5. Time starts at branch creation. Bin must: state the cause, then fix, then add a test that would have caught it. Count hints.
6. Log time-to-fix and hints in PROGRESS.md.
