"""Spaced retrieval scheduler. Ladder: 1, 3, 7, 14, 30 days. CSV: id,prompt,box,last_date."""

import csv
import datetime as dt
import sys
from pathlib import Path

LADDER = [1, 3, 7, 14, 30]
PATH = Path(".tutor/retrieval.csv")
LOG = Path(".tutor/retrieval_log.csv")


def load() -> list[dict[str, str]]:
    with PATH.open() as f:
        return list(csv.DictReader(f))


def save(rows: list[dict[str, str]]) -> None:
    with PATH.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "prompt", "box", "last_date"])
        w.writeheader()
        w.writerows(rows)


def due(rows: list[dict[str, str]], today: dt.date) -> list[dict[str, str]]:
    out = []
    for r in rows:
        gap = LADDER[min(int(r["box"]), len(LADDER) - 1)]
        if dt.date.fromisoformat(r["last_date"]) + dt.timedelta(days=gap) <= today:
            out.append(r)
    return out


if __name__ == "__main__":
    rows, today = load(), dt.date.today()
    if len(sys.argv) == 4 and sys.argv[1] == "--record":
        for r in rows:
            if r["id"] == sys.argv[2]:
                ok = sys.argv[3] == "pass"
                r["box"] = str(min(int(r["box"]) + 1, 4)) if ok else "0"
                r["last_date"] = today.isoformat()
        save(rows)
        with LOG.open("a", newline="") as f:
            csv.writer(f).writerow([today.isoformat(), sys.argv[2], sys.argv[3]])
    else:
        for r in due(rows, today):
            print(f"{r['id']}\t{r['prompt']}")
