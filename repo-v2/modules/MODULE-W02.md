---
id: W02
track: foundation
week: 2
concept: Embeddings and vector similarity; 20-row pgvector table
python_skill: lists, dicts, list of dicts, for loops, basic math
prompting_skill: give Claude a role; specify output format
prerequisites: [W01]
rubric_dimensions: [swe:data structures, prompting:4.0 role + format]
---
## Daily ladder
- Mon: Worked example: represent 5 payer policy snippets (e.g. prior auth rules for imaging) as dicts {"id", "text", "vec"} with hand-made 3-dimensional toy vectors. Print each id and vec. | Stretch: add a "payer" key to each row.
- Tue: Type a cosine_similarity(a, b) function from a worked example using loops (no numpy). Trace it by hand on [1,0,0] and [0,1,0] before running. | Stretch: handle a zero-length vector with a clear error message.
- Wed: Rank the 5 rows against a query vector and print the top 3. | Stretch: filter to one payer before ranking.
- Thu: SQL day. In a free Postgres with pgvector (Supabase or local Docker), create a table with vector(3), insert 20 synthetic rows, query with ORDER BY embedding <=> query LIMIT 3. Compare against your Python ranking. Prompting: write a role-plus-format prompt asking Claude to explain the result in a fixed 3-line format. | Stretch: add a payer_id column and a WHERE filter.
- Fri: SHIP + teach-back.
## Friday ship criteria
- [ ] similarity.py ranks rows correctly against a hand-checked expected order
- [ ] 20-row pgvector table returns the same top 3 as Python
## Teach-back prompt
Explain what an embedding is, what cosine similarity measures, and why a payer filter belongs in the query, in 5 bullets.
## Retrieval questions
- W02-Q1: What does cosine similarity of 1.0 vs 0.0 mean? | answer: same direction vs orthogonal/unrelated
- W02-Q2: Where should a payer or tenant filter go: before or after ranking, and why? | answer: in the query, so other tenants' rows are never candidates
- W02-Q3: What does <=> do in pgvector? | answer: distance operator; lower is closer
## Common misconceptions
- real embeddings have 3 dimensions -> real models output hundreds to thousands; toy vectors teach the math only
- pgvector <=> returns similarity -> it returns distance
## Weekend 90-min block
Load 20 rows from a Python list into Postgres using psycopg, hand-typed from a worked example.
## Resources
- pgvector README: https://github.com/pgvector/pgvector
