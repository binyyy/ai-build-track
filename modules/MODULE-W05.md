---
id: W05
track: foundation
week: 5
concept: Tool calling and the agent loop
python_skill: functions as values, dict dispatch, json.dumps/json.loads, while loops
prompting_skill: tool definitions with clear descriptions and input schemas
prerequisites: [W04]
rubric_dimensions: [swe:JSON + functions, prompting:6.0 tool definitions]
---
## Daily ladder
- Mon: Write a tool definition as a Python dict (name, description, input_schema) for check_eligibility(member_id, date_of_service). Print it with json.dumps(indent=2). | Stretch: add an enum field for plan_type.
- Tue: Implement the real Python function against a dict of 5 synthetic members. Dispatch via TOOLS = {"check_eligibility": fn}. | Stretch: return a structured error dict for an unknown id.
- Wed: Simulate the agent loop: a list of fake model responses (tool_use, then final text). The while loop executes tools and appends tool_result until the stop condition. | Stretch: add a max_iterations guard.
- Thu: Prompting. Rewrite the tool description so a new colleague knows when to use it, when not to, and what each field means. The agent grades it against the tool-use guidance. | Stretch: add a second tool (get_prior_auth_status) with a description that does not overlap.
- Fri: SHIP + teach-back.
## Friday ship criteria
- [ ] agent_loop.py runs the simulated loop end to end and stops correctly
- [ ] tool definition JSON validates and has a description of 3 or more sentences
## Teach-back prompt
Explain the agent loop: who decides to call a tool, who executes it, what goes back to the model, when the loop stops.
## Retrieval questions
- W05-Q1: Does the model execute the tool? | answer: no; your code executes it and returns a tool_result
- W05-Q2: Why a max_iterations guard? | answer: prevent runaway loops and cost
- W05-Q3: Workflow vs agent per Anthropic? | answer: workflow = predefined code paths; agent = model directs its own tool use
## Common misconceptions
- longer tool descriptions are always worse -> clear, complete descriptions improve tool selection
## Weekend 90-min block
Add a second tool and route between the two in the simulated loop.
## Resources
- Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- Tool use overview: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
