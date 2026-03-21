# Legal and Fair-Housing Guardrails

This repo uses objective housing-quality criteria only.

## Never use these as decision criteria
- age
- family status
- race or ethnicity
- religion
- disability status
- sexual orientation or gender identity
- nationality or immigration background
- any proxy for the protected classes above

## Practical translation
Do **not** ask for or infer whether a building is full of "young people," "families," "professionals," or any other demographic grouping.

Instead, ask about:
- quiet-hours enforcement
- building turnover and renewal patterns
- short-term-rental or furnished-stay presence
- staffing stability
- complaint-handling process
- after-hours support
- package and garage security

## Safe replacement for the old "adult vibe" concept
The operationally valid question is:

> Does this building behave like a stable, well-run residential community, or like a churn-heavy party or hotel environment?

That is what `community_stability_score` measures.

## Question-writing rule
If a question would require a leasing agent to describe protected classes, rewrite the question.

Bad:
- "What kind of people live here?"

Good:
- "How are quiet hours enforced?"
- "Are short-term furnished stays allowed?"
- "What is the typical lease term and renewal pattern?"
