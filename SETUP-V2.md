# SETUP-V2.md: get the zero-human track running (about 60 minutes, one weekend block)

## A. GitHub (10 min)
1. github.com > New repository > name `ai-build-track` > Public (branch protection is free only on public repos; synthetic data only, so public is fine) > create. Alternative: Private plus GitHub Pro ($4/month).
2. Upload this zip's contents to the repo root (drag the folder into the web uploader, or clone and push).
3. Settings > Secrets and variables > Codespaces > New secret: ANTHROPIC_API_KEY (from console.anthropic.com).
4. Settings > Secrets and variables > Actions > New secret: ANTHROPIC_API_KEY (same key, needed in week 5 for the reviewer).
5. Settings > Secrets and variables > Actions > Variables: COV_MIN = 0, REVIEWER_MODEL = NEEDS INPUT (pick a Claude model id different from the one you use in Claude Code).
6. Your profile > Settings > Codespaces: default idle timeout 10 minutes. Billing > Spending limits > Codespaces = 0.

## B. Codespace (10 min)
1. Repo page > Code > Codespaces > Create codespace on main. Wait. The devcontainer installs Python 3.12, Node, gh, pre-commit hooks and Claude Code.
2. Terminal: `python tools/due.py` (prints nothing, that is correct for week 1).
3. Terminal: `pre-commit run --all-files` (should pass).
4. Terminal: `claude` then `/permissions`. Confirm the deny list is loaded. Then ask Claude to "edit tests/test_smoke.py and add a test". It must refuse with the hook message. If it edits the file, stop and fix settings before continuing.
5. Terminal: `gh auth login` (needed for issues and PRs from the terminal).

## C. First session (15 min)
1. `claude` then `/start-session`.
2. Follow W01 Monday. Type the code yourself. Commit and push yourself.

## D. Week 1 extras (5 min each, inside sessions)
- Run `pre-commit autoupdate` once to pin current hook versions. Commit.
- Confirm the `ci` Action ran green on your first push.
- Confirm the `program-health` Action can run: Actions tab > program-health > Run workflow. An issue should appear.

## E. Week 2
- supabase.com free project. Save SUPABASE_URL and SUPABASE_KEY as Codespaces secrets. Restart the Codespace.
- Set Actions variable COV_MIN = 60 at the end of week 3.

## F. Week 4
- Add mirrors-mypy to .pre-commit-config.yaml (you type it). Open your first pull request to yourself and merge it.

## G. Week 5: reviewer and branch protection
1. Move setup-later/week5/reviewer.yml to .github/workflows/reviewer.yml. Commit via PR.
2. Settings > Branches > Add rule for `main`: require a pull request (0 approvals), require status checks (ci / lint-types-tests, ci / settings-guard, reviewer / review-gate), require branches up to date, require conversation resolution, require linear history, include administrators, block force pushes.
3. From now on: every change is a branch plus PR. Answer every reviewer finding in the PR body as `R1: FIXED <sha>` or `R1: WONTFIX <15+ words>`.

## H. Week 6
- Add gitleaks to .pre-commit-config.yaml. Build sim/run.py (W06 task). Run 5 personas for 3 turns.

## I. Week 7 to 8
- Build evals/run.py, evals/grade_transcripts.py, evals/calibrate.py (W07 tasks). Move setup-later/week7/weekly.yml into .github/workflows/.
- Week 8: `npm install -g promptfoo`, move setup-later/week8/promptfooconfig.yaml to redteam/, write redteam/target.py, run it.
- Set `.tutor/phase` to 2 at week 7 and put the date in `.tutor/phase_dates.csv`.

## J. Month 4
- Set `.tutor/phase` to 3 with its date. Actions variable COV_MIN = 70, add a mutation gate. Floor becomes 30 minutes.

## Things to verify in week 1 (secondary sources, not confirmed)
- `disableBypassPermissionsMode` key placement and permission rule syntax: run `/permissions` and do the blocked-edit test in B4.
- claude-code-action tool names in reviewer.yml: check the action's README before week 5.
- Codespaces free hours: github.com/features/codespaces.
