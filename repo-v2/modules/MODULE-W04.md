---
id: W04
track: foundation
week: 4
concept: Hybrid search and reranking
python_skill: sorted() with key, lambda, list comprehensions; Git begins
prompting_skill: rubric-based ranking prompt with explicit criteria
prerequisites: [W02, W03]
rubric_dimensions: [swe:Git basics, prompting:6.0 criteria-driven prompts]
---
## Daily ladder
- Mon: git init the ai-build-track repo, add .gitignore, commit weeks 1 to 3. From today, commit every session. Trace a list comprehension before writing one. | Stretch: write a 3-line README.md.
- Tue: Keyword score: count query-term matches per chunk using a comprehension. Rank. Use a query with a CPT code (e.g. 70553) to see why keywords matter. | Stretch: lowercase and strip punctuation first.
- Wed: Combine keyword rank and vector rank with reciprocal rank fusion: score = sum of 1/(60 + rank). Print the fused top 3. | Stretch: write an assert for one known case.
- Thu: Prompting. Write a reranking prompt: given a query and 5 chunks, return chunk ids ordered by relevance against 3 explicit criteria, output in <ranking> tags. | Stretch: add a "none relevant" outcome.
- Fri: SHIP + teach-back.
## Friday ship criteria
- [ ] repo has 4 or more commits with meaningful messages
- [ ] hybrid.py prints the fused ranking; one assert passes
## Teach-back prompt
Explain why hybrid search beats vector-only search for exact terms like CPT or ICD-10 codes and payer names, and what a reranker adds.
## Retrieval questions
- W04-Q1: What does keyword search solve that embeddings miss? | answer: exact identifiers, rare terms, codes
- W04-Q2: What does the constant 60 in RRF do? | answer: dampens the dominance of top ranks
- W04-Q3: git add vs git commit? | answer: stage vs record a snapshot
## Common misconceptions
- reranking retrieves new documents -> it reorders candidates already retrieved
## Weekend 90-min block
Push the repo to GitHub, make a branch, change hybrid.py, merge.
## Resources
- Contextual Retrieval (Anthropic): https://www.anthropic.com/engineering/contextual-retrieval
- Pro Git book ch. 2: https://git-scm.com/book/en/v2
