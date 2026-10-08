---
id: W03
track: foundation
week: 3
concept: Chunking and metadata
python_skill: string slicing, split(), functions with parameters, return values
prompting_skill: XML tags and multishot examples
prerequisites: [W02]
rubric_dimensions: [swe:functions, prompting:4.0 XML + examples]
---
## Daily ladder
- Mon: Parsons problem: reorder the lines of chunk_by_chars(text, size). Run it on a synthetic 1-page payer prior-auth policy. | Stretch: add an overlap parameter.
- Tue: Write chunk_by_paragraph(text) from a partial skeleton. Print chunk count and lengths. | Stretch: merge paragraphs shorter than 100 chars into the next one.
- Wed: Attach metadata: each chunk becomes {"chunk_id", "doc_id", "section", "payer_id", "effective_date", "text"}. | Stretch: derive "section" from heading lines.
- Thu: Prompting. Write a prompt that wraps 3 chunks in <document index="n"> tags with <source> and <document_content>, and includes 3 diverse examples in <examples> of good answers that cite chunk ids. | Stretch: add an edge-case example where the answer is not in the documents.
- Fri: SHIP + teach-back.
## Friday ship criteria
- [ ] chunker.py produces chunks with all metadata fields for the policy doc
- [ ] prompt_w03.md uses XML document structure and 3 examples
## Teach-back prompt
Explain the chunk size trade-off, why metadata matters for retrieval and access control, and why examples go in example tags.
## Retrieval questions
- W03-Q1: One cost of chunks too small and one of chunks too large? | answer: small loses context; large dilutes relevance and wastes tokens
- W03-Q2: Why wrap examples in <example> tags? | answer: so Claude separates examples from instructions
- W03-Q3: What does overlap protect against? | answer: splitting a key sentence across chunk boundaries
## Common misconceptions
- one chunk size fits all documents -> tune per document type with evals
## Weekend 90-min block
Chunk 3 synthetic documents of different types (policy, EOB explainer, denial letter) and compare chunk counts.
## Resources
- Prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
