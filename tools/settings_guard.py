"""CI guard: the deny list in .claude/settings.json may only shrink after the phase date."""

import csv
import datetime as dt
import json
import sys

REQUIRED_PHASE1 = {
    "Edit(**/*.py)",
    "Edit(**/prompts/**)",
    "Edit(**/evals/adjudications/**)",
    "Bash(git commit:*)",
}
ALWAYS = {"Edit(**/prompts/**)", "Edit(**/evals/adjudications/**)", "Read(**/.github/reviewer/**)"}

deny = set(json.load(open(".claude/settings.json"))["permissions"]["deny"])
phase = int(open(".tutor/phase").read().strip())
dates = {
    int(r["phase"]): r["earliest_date"] for r in csv.DictReader(open(".tutor/phase_dates.csv"))
}
missing = ALWAYS - deny
if phase == 1:
    missing |= REQUIRED_PHASE1 - deny
if phase > 1:
    try:
        earliest = dt.date.fromisoformat(dates[phase])
    except (KeyError, ValueError):
        print("phase_dates.csv needs a real date for this phase")
        sys.exit(1)
    if dt.date.today() < earliest:
        print(f"Phase {phase} not allowed before {earliest}")
        sys.exit(1)
if missing:
    print("Deny list missing:", sorted(missing))
    sys.exit(1)
print("settings guard ok")
