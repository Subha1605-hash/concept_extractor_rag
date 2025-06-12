# LLM Prompt Template for Concept Extraction

## Objective
The goal is to extract the historical or domain-specific **concept(s)** being tested in each competitive exam question.

This prompt was used in a simulated setup using a local LLM or manual LLM interface like ChatGPT. API integration is not yet live but is designed to be added later.

---

## Prompt Template

```text
You are a subject matter expert analyzing competitive exam questions.

Given the question:
"{question}"

Identify the core historical concept(s) this question tests.
Return 2–3 concise concept labels (comma-separated), like:
- "Gupta Period Literature"
- "Harappan Urban Planning"
- "Ancient Indian Science and Technology"
