# RUBRICS.md

Scores move only on dated evidence in PROGRESS.md. Never on self-report.

## B1. Software / AI engineering (10 = entry-level software/AI engineer)

| Level | Observable capability (alone) | Test that proves it |
|---|---|---|
| 1.0 | Can run a given script | Runs `python hello.py` |
| 2.0 | Edits variables and strings in an existing script. Reads a short traceback and finds the line it points to | Changes a provided script and it still runs |
| 3.0 | Writes a 30 to 60 line script from scratch with functions, lists, dicts, loops and file or JSON I/O. Sets up a venv and installs packages. Commits with Git (add, commit, push) | Builds a CSV-to-JSON transformer in 30 minutes with hints only |
| 4.0 | Calls an API with a key held in an environment variable. Handles errors with try/except. Writes 3 pytest tests. Uses branches | Script calls the Claude API, saves structured output, and passes its tests |
| 5.0 | Starts from a blank folder and deploys a small working tool (GitHub Actions or similar). Finds a bug from a traceback in under 10 minutes on 4 of 5 attempts. Uses Git without fear (branch, merge, revert). Writes a handful of tests. Knows the shape of a reasonable project (src/, tests/, config, README, .env.example). Directs Claude Code through a multi-file change and catches when it is wrong | Monthly blank-folder test: a deployed tool in 90 minutes with hints only, plus a planted-bug review of a Claude Code diff |
| 6.0 | Designs a small service with a database and retrieval. Writes integration tests. Reads unfamiliar repos | Adds a feature to an open-source repo he has not seen before |
| 7.0 | Owns a production tool used by other people. Adds logging, monitoring and CI. Reasons about latency and cost. Reviews code from others | Artifact 3 is in use, with CI and an incident log |
| 8.0 to 9.0 | Multiple languages. Schema migrations, authentication, multi-tenant isolation in depth | Out of scope |
| 10.0 | Passes an entry-level SWE/AI-engineer loop | Out of scope |

## B2. Prompting skill (10 = expert prompt/context engineer for production agents and evals)

| Level | Observable capability |
|---|---|
| 2.0 | Writes single-turn requests that work most of the time |
| 4.0 | Writes clear, direct system prompts with role, context, the "why" behind constraints, and an explicit output format. Applies the "colleague" test. Uses XML tags to separate instructions, context and input. Uses 3 to 5 diverse examples wrapped in example tags |
| 6.0 | Chains prompts for multi-step tasks. Lays out long context with documents first and the query last, with quote grounding. Defines tools with clear descriptions. Writes success criteria that are specific, measurable, achievable and relevant. Builds a 20-case golden set and a code-graded or LLM-graded eval. Knows current models reject non-default sampling parameters and prefill |
| 8.0 | Designs system prompts for production agents with tool definitions. Writes evals and golden sets and runs them on every prompt change. Uses structured outputs. Lays out prompts for caching (stable prefix first). Uses few-shot and thinking appropriately. Handles prompt injection with a trust boundary plus tests. Debugs failures by reading transcripts and naming the failure mode. Writes Skills and CLAUDE.md files with evals built first. Applies context engineering (just-in-time retrieval, compaction, structured notes) to long-running agents |
| 10.0 | Owns the prompt and eval stack for a production multi-agent system. Designs grader calibration and regression suites. Teaches others |

Sampling note: current Claude models return a 400 error on non-default temperature, top_p or top_k, and on assistant prefill. Consistency comes from prompts, structured outputs and evals.

Anthropic sources:
- Prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Define success criteria and build evals: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- Effective context engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Claude Code best practices: https://www.anthropic.com/engineering/claude-code-best-practices
- Skill authoring best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

## F1. Monthly test protocol (first weekend block of each month, 90 minutes, hints only)

| Month | SWE test | Prompting test | Pass moves score to |
|---|---|---|---|
| 1 | Blank file: 40-line script that loads JSON claim rows, ranks them by cosine similarity, prints top 3 | System prompt with role, XML and 3 examples for a new use case; graded against the 4.0 line | SWE 3.0 (partial), prompting 4.0 |
| 2 | Simulated agent loop with 2 tools and error handling; Git branch and merge | Tool definitions plus 10-case golden set for a new tool | SWE 3.0, prompting 5.0 |
| 3 | Blank folder: real API call with structured output, validated, 3 tests, committed | 20-case eval with LLM grader agreeing with hand grades on 4 of 5; 5 injection cases | SWE 4.0, prompting 6.0 |
| 4 to 5 | Rebuild A1's core from a blank folder and deploy it in 90 minutes | Prompt chain plus an eval-gated change | SWE 4.5 to 5.0 |
| 6 to 7 | Planted-bug test: 3-file Claude Code diff with 2 planted bugs, find both in 20 minutes. Fix a traceback in under 10 minutes on 4 of 5 attempts | Read 5 failing transcripts, name each failure mode and fix | SWE 5.0, prompting 7.0 |
| 8 to 9 | A3 shipped with CI and tenant isolation | Production agent system prompt with tools, caching layout, injection defenses and a Skill, graded line by line against 8.0 | Prompting 7.5 to 8.0 |

## F3. Thresholds that trigger plan changes (rolling 2 weeks)

| Signal | Diagnosis | Change |
|---|---|---|
| Teach-backs at 4.0/5.0 or better, but code tasks unfinished 3 or more days | Concept without code | Add a Saturday 30-minute code-only block: trace plus Parsons |
| Code runs, but teach-backs at 3.0/5.0 or worse | Code without concept | Halve lesson length; add a daily 1-minute "why" question; double retrieval items from that module |
| Retrieval accuracy below 60.0% | Forgetting | Freeze new retrieval items for 1 week |
| Retrieval accuracy above 90.0% for 3 weeks | Too easy | Two questions per session; advance fading one step |
| Fewer than 4 sessions in a week, twice | Overload | Cut the floor to retrieval plus one 5-minute trace |
| Traceback fixes over 10 minutes at month 6 | Debugging gap | Weekly 15-minute planted-bug kata |
| Claude Code errors not caught in 2 of last 3 reviews | Over-trust | Every diff review must name one risk and one missing test |
| Monthly test failed | Not at level | Repeat that month's milestone; scores hold |
