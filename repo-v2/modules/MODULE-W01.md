---
id: W01
track: foundation
week: 1
concept: Tokens, context windows, prompt caching
python_skill: running a script, variables, strings, f-strings, len(), print
prompting_skill: clear and direct system prompt (role, context, why, output format)
prerequisites: []
rubric_dimensions: [swe:run and edit scripts, prompting:4.0 clear and direct]
---
## Daily ladder
- Mon: Install Python 3.12 and make a venv. Type the worked example tokens.py: store a prompt in a variable, print len(text) and a rough token estimate (chars / 4, labeled as an approximation). | Stretch: print the estimate for 3 prompts of different lengths.
- Tue: Trace first: predict the output of a 6-line f-string snippet, then run it. Then build a context "budget" printout: system + history + question as variables, with a total. | Stretch: print a warning line if the total exceeds a budget variable.
- Wed: Caching concept. Split the prompt into stable_prefix and variable_suffix strings. Print which part is cacheable and explain why the prefix must stay identical. | Stretch: rewrite it so the variable part is a function argument.
- Thu: Prompting. Write a clear-and-direct system prompt for a "patient eligibility and benefits FAQ" bot for a front-desk team: role, context, why each constraint exists, output format. Run the colleague test: the agent plays a new hire with no context and lists any confusion. | Stretch: rewrite one "NEVER" rule as a positive instruction with its reason.
- Fri: SHIP + teach-back.
## Friday ship criteria
- [ ] tokens.py runs and prints the budget and the cacheable split
- [ ] system_prompt_v1.md exists with role, context, reasons and output format
## Teach-back prompt
Explain tokens, context windows and prompt caching to a patient access analyst in 5 bullets, including why prompt order matters for caching.
## Retrieval questions
- W01-Q1: Why must the cached part of a prompt be a stable prefix? | answer: cache matches identical leading content; any change before the breakpoint invalidates it
- W01-Q2: What is a context window? | answer: max tokens of input plus output the model attends to in one request
- W01-Q3: Rewrite "NEVER use jargon" per Anthropic guidance. | answer: positive instruction plus reason, e.g. "Use plain language because readers are front-desk staff"
## Common misconceptions
- tokens = words -> tokens are sub-word units; chars/4 is a rough estimate
- caching saves output tokens -> caching applies to repeated input prefixes
## Weekend 90-min block
Write 3 system prompt variants for the FAQ bot and have the agent critique each against the clear-and-direct guidance.
## Resources
- Prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Prompt caching docs: search "Anthropic prompt caching" on platform.claude.com
