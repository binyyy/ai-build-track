---
id: W06
track: foundation
week: 6
concept: MCP; first real API call; move to Claude Code
python_skill: pip install, environment variables, the anthropic SDK, reading response objects
prompting_skill: CLAUDE.md v0 for the repo
prerequisites: [W05]
rubric_dimensions: [swe:API + env vars, prompting:6.0 instructions for Claude Code]
---
## Daily ladder
- Mon: Install Claude Code. Store ANTHROPIC_API_KEY in your shell environment (never in code), add .env to .gitignore. Type first_call.py by hand: one messages.create call with no temperature or top_p. Print response.content and response.usage. | Stretch: print input_tokens and output_tokens on separate lines.
- Tue: Swap the simulated responses from W05 for a real tool call using your check_eligibility definition. | Stretch: handle the case where the model answers without calling the tool.
- Wed: MCP concept. Read the Python MCP server quickstart, trace one tool function, explain host, client and server roles. | Stretch: list which W05 tools you would expose as MCP tools, and why.
- Thu: Prompting. Write CLAUDE.md v0 (under 40 lines): project purpose, layout, run and test commands, rules (synthetic data only, no sampling params, commit every session). | Stretch: ask Claude Code to explain the repo using only CLAUDE.md, and fix gaps.
- Fri: SHIP + teach-back. Last week of hand-typing.
## Friday ship criteria
- [ ] first_call.py and real_tool_call.py run with the key from the environment
- [ ] CLAUDE.md committed
## Teach-back prompt
Explain MCP to a revenue cycle director: what problem it solves versus custom integrations, and the host/client/server roles.
## Retrieval questions
- W06-Q1: Why omit temperature on current Claude models? | answer: non-default sampling params return 400; steer with prompts
- W06-Q2: MCP server vs client? | answer: server exposes tools/resources; client inside the host connects to it
- W06-Q3: Where does the API key live? | answer: environment variable or secrets store, never in code or Git
## Common misconceptions
- MCP replaces tool calling -> MCP standardizes how tools are exposed; the model still calls tools
## Weekend 90-min block
Connect one existing MCP server to Claude Code and use it in a task.
## Resources
- MCP docs: https://modelcontextprotocol.io
- Claude Code best practices: https://www.anthropic.com/engineering/claude-code-best-practices
