---
id: W09
track: foundation
week: 9
concept: Trust boundary, BAA, zero data retention
python_skill: logging module, regex redaction, config files
prompting_skill: data-handling rules in the system prompt plus PHI-leak eval cases
prerequisites: [W08]
rubric_dimensions: [swe:logging + config, prompting:8.0 production constraints]
---
## Daily ladder
- Mon: Draw (in Markdown) the trust boundary for the eligibility bot: where data enters, what leaves for the model API, where logs go. | Stretch: mark which arrows would carry PHI in a real health-system deployment.
- Tue: Direct Claude Code to add the logging module with levels; review that no prompt text is logged at INFO. | Stretch: move settings into config.toml.
- Wed: Write redact(text) with regex for synthetic MRNs, member IDs, phone numbers and DOBs. Add 5 pytest cases. | Stretch: add a failing case you find and fix it.
- Thu: Prompting. Add data-handling rules to the system prompt and 4 eval cases where the user pastes synthetic PHI; expected behavior defined by you. | Stretch: write a one-page vendor checklist: BAA, ZDR status, retention, subprocessors.
- Fri: SHIP + teach-back.
## Friday ship criteria
- [ ] redact.py passes 5 or more tests
- [ ] trust_boundary.md and vendor_checklist.md committed
## Teach-back prompt
Explain to a compliance officer what a BAA covers, what ZDR changes, and where your redaction sits in the trust boundary.
## Retrieval questions
- W09-Q1: Does a BAA make any vendor use HIPAA-compliant? | answer: no; contractual requirement, not a technical control; scope and configuration matter
- W09-Q2: What should never appear in INFO logs? | answer: PHI and raw prompt or response content
- W09-Q3: Why redact before the API call even with a BAA? | answer: minimum necessary and lower blast radius
## Common misconceptions
- ZDR means no data ever touches the vendor -> data is processed but not retained; check the terms
## Weekend 90-min block
Map Hostie's call-transcript flow onto the same trust-boundary template.
## Resources
- HHS business associates guidance: https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html
- Anthropic API and data retention: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
