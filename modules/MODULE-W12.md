---
id: W12
track: foundation
week: 12
concept: Cost modeling (tokens, caching, model choice)
python_skill: functions with defaults, arithmetic, formatting tables, reading usage fields
prompting_skill: context engineering review of your own bot
prerequisites: [W01, W06, W07]
rubric_dimensions: [swe:end-to-end small tool, prompting:8.0 context engineering]
---
## Daily ladder
- Mon: Write cost(input_tokens, output_tokens, cache_read_tokens, prices) with prices from config (NEEDS INPUT: current prices from Anthropic's pricing page). | Stretch: add a per-site monthly projection at a given query volume.
- Tue: Log response.usage from 20 eval runs and compute actual cost per question to one decimal in cents. | Stretch: compare two models on cost vs eval pass rate.
- Wed: Restructure the prompt for caching (stable system and tools first), rerun, compare cache read tokens. | Stretch: one-paragraph recommendation.
- Thu: Prompting. Context engineering audit: list every token block in your bot's context, mark what to cut, retrieve just in time, or compact. Apply 2 cuts and rerun the eval. | Stretch: write the audit as a reusable checklist.
- Fri: SHIP + foundation capstone teach-back + month 3 test (RUBRICS.md F1).
## Friday ship criteria
- [ ] cost_model.py prints a cost table from real usage logs
- [ ] context audit applied with eval results before and after
## Teach-back prompt
Explain the unit economics of an LLM feature for a hospital call center: per-query cost drivers, caching, model choice, and eval-gated trade-offs.
## Retrieval questions
- W12-Q1: Name 3 cost levers besides price per token. | answer: caching, shorter context, model choice, fewer loop iterations
- W12-Q2: Why gate a cheaper model on evals? | answer: cost cuts that drop accuracy are not savings
- W12-Q3: Context engineering in one line? | answer: curating the smallest high-signal set of tokens for each step
## Common misconceptions
- the cheapest model is cheapest overall -> retries and failures can cost more
## Weekend 90-min block
Write a one-page cost memo usable in a solutions-architect interview.
## Resources
- Effective context engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
