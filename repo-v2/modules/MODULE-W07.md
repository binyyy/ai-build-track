---
id: W07
track: foundation
week: 7
concept: Evals and a 20-question golden set
python_skill: reading JSON/CSV files, loops over test cases, pytest basics; directing Claude Code begins
prompting_skill: success criteria and an LLM grading prompt
prerequisites: [W03, W06]
rubric_dimensions: [swe:tests, prompting:6.0 evals]
---
## Daily ladder
- Mon: Write success criteria for the eligibility FAQ bot that are specific, measurable, achievable and relevant. Hand-write 10 golden cases (question, expected key facts, category: copay, deductible, prior auth, network). | Stretch: add 3 edge cases (out of scope, ambiguous, adversarial).
- Tue: Direct Claude Code to write run_eval.py that loads golden.json and calls the bot. Review the diff and find 1 issue before accepting. | Stretch: reach 20 cases.
- Wed: Code-graded check: exact or contains match on key facts. Print a pass rate with one decimal. | Stretch: write a pytest that fails if the pass rate drops below a threshold.
- Thu: Prompting. Write an LLM grading prompt: rubric in XML, grader outputs only "correct" or "incorrect", ideally on a different model than the bot. Grade 5 cases by hand and compare. | Stretch: log disagreements and fix rubric wording.
- Fri: SHIP + teach-back.
## Friday ship criteria
- [ ] golden.json has 20 cases including 3 or more edge cases
- [ ] run_eval.py prints a pass rate; grader agrees with hand grades on 4 of 5
## Teach-back prompt
Explain why an eval set comes before prompt tweaking, and code-graded vs LLM-graded vs human-graded checks.
## Retrieval questions
- W07-Q1: Anthropic's 4 properties of good success criteria? | answer: specific, measurable, achievable, relevant
- W07-Q2: Volume or quality of eval cases? | answer: prioritize volume with automated grading over a few hand-graded cases
- W07-Q3: How do you check an LLM grader? | answer: compare against human labels on a sample
## Common misconceptions
- a high pass rate on 5 cases means the prompt works -> too few cases; edge cases matter
## Weekend 90-min block
Change the system prompt once, rerun the eval, record before/after pass rate in PROGRESS.md.
## Resources
- Define success criteria and build evals: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
