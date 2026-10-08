"""Fails until every reviewer finding is answered in the PR body.
Accepts "Rn: FIXED <sha>" or "Rn: WONTFIX <15+ words>". HIGH must be FIXED.
Reads the reviewer comment that starts with <!-- reviewer-findings -->."""

import argparse
import json
import re
import subprocess
import sys

p = argparse.ArgumentParser()
p.add_argument("--pr", required=True)
a = p.parse_args()

body = subprocess.check_output(
    ["gh", "pr", "view", a.pr, "--json", "body", "-q", ".body"], text=True
)
comments = json.loads(
    subprocess.check_output(
        ["gh", "pr", "view", a.pr, "--json", "comments", "-q", ".comments"], text=True
    )
)
findings = []
for c in comments:
    txt = c.get("body", "")
    if txt.startswith("<!-- reviewer-findings -->"):
        m = re.search(r"```json\s*(\{.*?\})\s*```", txt, re.S)
        if m:
            findings = json.loads(m.group(1)).get("findings", [])
if not findings:
    print("No reviewer findings found yet")
    sys.exit(1)
fail = 0
for f in findings:
    fid, sev = f["id"], f["severity"]
    fixed = re.search(rf"{fid}:\s*FIXED\s+[0-9a-f]{{7,40}}", body)
    wontfix = re.search(rf"{fid}:\s*WONTFIX\s+(.+)", body)
    if fixed:
        continue
    if wontfix and len(wontfix.group(1).split()) >= 15 and sev != "HIGH":
        continue
    print(f"{fid} ({sev}) unresolved")
    fail += 1
sys.exit(1 if fail else 0)
