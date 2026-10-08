"""Pre-commit hook: block staged text that looks like PHI. Synthetic fixtures must not look real."""

import re
import sys

PATTERNS = {
    "SSN": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "phone": re.compile(r"\b\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}\b"),
    "DOB": re.compile(r"\b(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(19|20)\d{2}\b"),
    "MRN-like": re.compile(r"\bMRN[:# ]?\s?\d{6,}\b", re.I),
}
ALLOW_MARK = "SYNTHETIC-OK"

bad = 0
for path in sys.argv[1:]:
    try:
        text = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        continue
    for i, line in enumerate(text.splitlines(), 1):
        if ALLOW_MARK in line:
            continue
        for name, pat in PATTERNS.items():
            if pat.search(line):
                print(f"{path}:{i}: {name} pattern. Add '{ALLOW_MARK}' on the line if synthetic.")
                bad += 1
sys.exit(1 if bad else 0)
