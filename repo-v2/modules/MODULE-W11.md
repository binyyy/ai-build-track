---
id: W11
track: foundation
week: 11
concept: Governance (NIST AI RMF, Joint Commission RUAIH, FDA CDS)
python_skill: dataclasses, generating Markdown from data
prompting_skill: write a Claude Code Skill for the project, evals first
prerequisites: [W07, W09]
rubric_dimensions: [swe:modeling data, prompting:8.0 Skills for Claude Code]
---
## Daily ladder
- Mon: Define a dataclass ModelCard (purpose, users, data, evals, known failure modes, owner) and render it to Markdown. | Stretch: load it from config.toml.
- Tue: Map the eligibility bot to the NIST AI RMF functions (Govern, Map, Measure, Manage), one evidence line each, linking to your eval and redaction files. | Stretch: the FDA CDS question: does the tool meet the non-device CDS criteria? Mark as judgment, not legal advice.
- Wed: Skill evals first: write 3 test scenarios for a "run-evals-and-report" Skill and run Claude Code on them without the Skill for a baseline. | Stretch: record the baseline failures.
- Thu: Write SKILL.md (frontmatter name and description, concise steps), rerun the 3 scenarios, compare with baseline. | Stretch: trim the Skill to the minimum that still passes.
- Fri: SHIP + teach-back.
## Friday ship criteria
- [ ] model_card.md generated from code
- [ ] .claude/skills/run-evals/SKILL.md committed, with 3 scenarios and before/after results
## Teach-back prompt
Explain how you would show a health-system CTO that the bot is governed: what the model card, evals and NIST mapping each prove.
## Retrieval questions
- W11-Q1: The 4 NIST AI RMF functions? | answer: Govern, Map, Measure, Manage
- W11-Q2: What does Anthropic say to create before writing a Skill? | answer: evaluations (at least three scenarios) and a baseline
- W11-Q3: CLAUDE.md vs Skill? | answer: CLAUDE.md = always-loaded project context; Skill = loaded when relevant for a repeatable task
## Common misconceptions
- governance = a policy document -> governance needs measurable evidence (evals, logs, owners)
## Weekend 90-min block
Write a RUAIH-aligned one-pager for a health-system AI committee from your model card.
## Resources
- Skill authoring best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
