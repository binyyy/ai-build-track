---
id: A1
track: artifact
weeks: 13-18 (month 4 to mid-5)
concept: Weekly AI-lesson script rebuilt properly
rubric_dimensions: [swe:5.0 deploy + tests + project shape, prompting:6.0 to 8.0 chained prompts + evals]
---
## Rules from here
- Daily floor rises to 30 minutes. Ratio 80% build / 20% reading.
- Bin directs Claude Code; the tutor grades his diff reviews.
## Milestones
- Wk13: Repo skeleton (src/, tests/, config.toml, .env.example, README). Script runs locally.
- Wk14: Config and secrets in GitHub Actions secrets; no key in code. Structured logging.
- Wk15: Prompt chain (outline -> lesson -> self-check), with a 10-case eval on lesson quality.
- Wk16: pytest suite (5 or more tests); CI runs tests on each push.
- Wk17: Scheduled GitHub Actions workflow delivers the Monday lesson (email or Drive).
- Wk18: README with architecture, run, test and cost sections. Blank-folder rebuild test.
## Ship criteria
- [ ] Scheduled workflow ran successfully 2 weeks in a row
- [ ] CI green; 5 or more tests; eval pass rate logged
- [ ] Rebuilt the core from a blank folder in 90 min with hints only
## Rubric evidence
- swe 4.0 to 5.0: deploy, tests, project shape, secrets
- prompting 6.0: chaining plus eval
