---
id: W10
track: foundation
week: 10
concept: FHIR, SMART on FHIR, EHR integration patterns
python_skill: requests, HTTP GET, nested JSON traversal
prompting_skill: long-context layout (documents first, query last, quote grounding)
prerequisites: [W09]
rubric_dimensions: [swe:HTTP APIs, prompting:6.0 long context]
---
## Daily ladder
- Mon: GET a Patient resource from a public FHIR test server (synthetic data only) using requests. Print name and birthDate. | Stretch: handle a 404 cleanly.
- Tue: Fetch a Bundle of Coverage or Observation resources; extract key fields into a list of dicts. | Stretch: handle a missing field.
- Wed: Read the SMART App Launch overview and trace the OAuth flow steps in your own words; note what Epic adds (app registration, scopes). | Stretch: list the scopes a prior-auth status tool would need.
- Thu: Prompting. Build a long-context prompt: the FHIR bundle in <document> tags at the top, instructions and query at the end, "quote the relevant entries first". Compare with a query-first version on 3 questions. | Stretch: add the comparison to golden.json.
- Fri: SHIP + teach-back.
## Friday ship criteria
- [ ] fhir_fetch.py prints a clean table
- [ ] long-context prompt comparison logged
## Teach-back prompt
Explain FHIR resources, what SMART on FHIR adds, and why an LLM summary of a FHIR bundle needs quote grounding.
## Retrieval questions
- W10-Q1: What is a FHIR Bundle? | answer: a container of resources returned by a search or transaction
- W10-Q2: SMART on FHIR in one line? | answer: OAuth 2.0-based authorization and app launch profile on top of FHIR
- W10-Q3: Where does long data go in a prompt per Anthropic? | answer: at the top, query at the end
## Common misconceptions
- FHIR is a database -> it is an API and data standard
## Weekend 90-min block
Write a coverage check (active coverage on date of service) over synthetic bundles.
## Resources
- HL7 FHIR R4: https://hl7.org/fhir/R4/
- SMART App Launch: https://hl7.org/fhir/smart-app-launch/
