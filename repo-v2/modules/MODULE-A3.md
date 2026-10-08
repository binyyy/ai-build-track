---
id: A3
track: artifact
weeks: 27-39 (months 7 to 9)
concept: LLM-in-the-loop tool over data (Planblx feature, or an RCM tool such as a denial-reason explainer over synthetic claims and payer policy)
rubric_dimensions: [swe:5.0 to 6.0 database + retrieval + tenancy, prompting:8.0 evals + context engineering]
---
## Milestones
- Wk27-28: Choose the use case. Healthcare use is synthetic data only. Write success criteria.
- Wk29-30: Postgres with pgvector, real embeddings, chunking with payer_id or tenant_id metadata.
- Wk31-32: Hybrid retrieval plus reranking; retrieval eval (recall at 5 on 20 questions).
- Wk33-34: A tool call against the database (parameterized SQL, tenant enforced in code).
- Wk35: End-to-end golden set of 30 cases, including cross-tenant and injection cases.
- Wk36: Structured outputs, caching layout, cost per query.
- Wk37: Context engineering pass for long sessions (compaction or notes).
- Wk38: A project Skill and CLAUDE.md; CI runs evals on prompt changes.
- Wk39: Demo plus written case study for job applications.
## Ship criteria
- [ ] Zero cross-tenant leaks across all eval cases
- [ ] Eval suite runs in CI on every prompt change
- [ ] Case study with architecture, eval results, cost per query and trade-offs
## Rubric evidence
- swe 5.0 confirmed; 6.0 lines started (database plus retrieval service)
- prompting 8.0: every line evidenced by files in this repo
