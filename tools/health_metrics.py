"""Weekly program health. Deterministic rules only. Writes reports/health/<YYYY-WW>.md.
Phase 1 version: sessions per week, retrieval accuracy, streak. Extend as tooling lands."""

import collections
import csv
import datetime as dt
import re
from pathlib import Path

today = dt.date.today()
week = today.isocalendar()
start = today - dt.timedelta(days=14)

entries = re.findall(r"^### (\d{4}-\d{2}-\d{2})", Path("PROGRESS.md").read_text(), re.M)
dates = [dt.date.fromisoformat(d) for d in entries]
by_week = collections.Counter(d.isocalendar()[:2] for d in dates if d >= start)
sessions_last_2 = sorted(by_week.values())

log = list(csv.DictReader(open(".tutor/retrieval_log.csv")))
recent = [r for r in log if dt.date.fromisoformat(r["date"]) >= start]
acc = (sum(r["result"] == "pass" for r in recent) / len(recent) * 100.0) if recent else None

adjust = []
if len(sessions_last_2) == 2 and all(n < 4 for n in sessions_last_2):
    adjust.append("Minimum viable week: retrieval plus one 5-minute trace only. No new content.")
if acc is not None and acc < 70.0:
    adjust.append("Pause advancement one week. Review due queue only.")
if acc is not None and acc > 90.0 and len(recent) >= 10:
    adjust.append("Fade scaffolding one step for the current topic.")
if not adjust:
    adjust.append("None. Continue the module as planned.")

out = Path("reports/health") / f"{week[0]}-W{week[1]:02d}.md"
out.write_text(
    f"# Program health {week[0]}-W{week[1]:02d}\n\n"
    f"- sessions (last 2 weeks, per week): {sessions_last_2 or [0]}\n"
    f"- retrieval accuracy (last 14 days): {f'{acc:.1f}%' if acc is not None else 'n/a'}\n\n"
    "## Adjustments\n" + "".join(f"- {a}\n" for a in adjust)
)
print(out.read_text())
