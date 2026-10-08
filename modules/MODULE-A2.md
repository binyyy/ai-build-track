---
id: A2
track: artifact
weeks: 19-26 (months 5 to 6)
concept: Hostie HubSpot onboarding automation with a real user
rubric_dimensions: [swe:5.0 multi-file changes with a real API, prompting:8.0 production system prompt + tools]
---
## Milestones
- Wk19: Write the onboarding spec with the Hostie user; success criteria agreed in writing.
- Wk20: HubSpot private app token in secrets; read contacts and deals (sandbox first).
- Wk21: Agent with 3 tools (find_company, create_onboarding_tasks, draft_welcome_email); tool definitions reviewed against the docs.
- Wk22: Golden set of 20 real-shaped onboarding cases, plus 5 injection cases from inbound form text.
- Wk23: Human-approval step before any HubSpot write; idempotency check.
- Wk24: Real user pilot on 5 restaurants; transcript review log naming failure modes.
- Wk25-26: Fix the top 3 failure modes, rerun evals, write a handoff doc.
## Ship criteria
- [ ] Real user ran it on 5 or more real onboardings
- [ ] Eval pass rate before and after fixes recorded; injection cases pass
- [ ] Transcript debugging log with 5 or more named failure modes and fixes
## Rubric evidence
- swe 5.0: Claude Code multi-file change caught when wrong (logged), real API, approvals
- prompting 8.0 lines: production system prompt with tools, injection handling, transcript debugging
