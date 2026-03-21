# Research Methodology

## Source hierarchy

### Tier 1: Direct and official
- official leasing site
- fee schedules
- lease drafts
- public property and regulatory records
- direct staff answers captured with date and name

### Tier 2: Credible independent reporting
- local news coverage
- reputable local reporting
- official complaints or public enforcement records when available

### Tier 3: Large review platforms
- Google reviews
- Yelp
- ApartmentRatings
- other major listing/review platforms

### Tier 4: Anecdotal and community sources
- Reddit
- neighborhood groups
- social media

Marketing copy is useful for inventory discovery, not for trust.

## Evidence classes
- `confirmed`: directly supported by a credible source
- `corroborated`: supported by at least two independent sources
- `anecdotal`: single-source subjective account
- `inferred`: reasonable deduction from incomplete evidence
- `unknown`: not enough information yet

## Required provenance for durable claims
For any claim likely to affect the decision, log:
- source URL
- retrieval date
- source type
- scope (`building` or `unit`)
- criterion affected
- short note or quote fragment

Use `data/evidence.csv` for this.

## Conflict-resolution rules
When sources disagree:
1. document the disagreement explicitly
2. prefer newer sources if the issue is time-sensitive
3. prefer official disclosures for fees and policy
4. prefer independent sources for lived experience
5. when in doubt, lower confidence instead of forcing a precise score

## What must be verified on tour
Some facts should stay unresolved until an in-person visit:
- exact unit exposure
- hallway odor and cleanliness
- sound transfer in the stack
- package-room reality versus marketing copy
- whether the staff answers hard questions directly
