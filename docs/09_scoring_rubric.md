# Scoring Rubric and Ranking Method

This repo keeps 1-5 category scores for human readability, but the overall ranking is computed through a weighted utility model.

## Category scores

### quiet_score
- 5: Consistently quiet; no chronic internal or external source identified.
- 4: Minor noise tradeoffs, but no pattern suggesting daily disruption.
- 3: Noticeable but likely manageable noise risk.
- 2: Recurring noise issue or risky exposure that could materially affect daily life.
- 1: Severe or chronic noise problem.

### management_score
- 5: Fast, transparent, credible, and well-staffed operations.
- 4: Generally strong with only isolated friction.
- 3: Mixed but workable.
- 2: Repeated signs of slow, evasive, or understaffed operations.
- 1: Operationally broken or clearly untrustworthy.

### amenity_score
- 5: All essentials present plus a strong set of useful extras.
- 4: All essentials present plus some meaningful extras.
- 3: Essentials present, extras unremarkable.
- 2: One essential item is missing or seriously compromised.
- 1: Multiple essential items are missing or unreliable.

### community_stability_score
This replaces the old demographic proxy.

Measure only operational signals:
- quiet-hours enforcement
- short-term-rental presence
- renewal patterns
- turnover signals
- resident complaints about common-area behavior

Scoring:
- 5: Strong evidence of stable long-term operations and enforceable building norms.
- 4: Mostly stable with limited churn.
- 3: Mixed.
- 2: Frequent churn, party behavior, or hotel-like use.
- 1: Highly unstable occupancy pattern or no meaningful enforcement.

### location_fit_score
- 5: Excellent fit for daily routines and preferred orbit.
- 4: Strong fit.
- 3: Acceptable but imperfect.
- 2: Material inconvenience or surrounding-environment tradeoff.
- 1: Bad fit.

### pricing_transparency_score
- 5: Fees and concessions are clear, simple, and stable.
- 4: Mostly clear.
- 3: Some ambiguity but manageable.
- 2: Repeated fee ambiguity or bait-and-switch risk.
- 1: Material pricing opacity.

## Confidence labels
For each score, track confidence separately:
- `high`: direct evidence from multiple credible sources or in-person verification
- `medium`: credible but incomplete evidence
- `low`: thin evidence, mostly soft signals
- `unknown`: not enough to score responsibly

## Evidence count
Use the evidence-count columns to record how many distinct, relevant pieces of evidence support each score.

## Utility mapping
The repo does not treat 1-5 as linear. It maps:
- 1 -> 0.00
- 2 -> 0.25
- 3 -> 0.55
- 4 -> 0.80
- 5 -> 1.00

## Default weights
- quiet_score: 30%
- management_score: 25%
- amenity_score: 15%
- community_stability_score: 15%
- location_fit_score: 10%
- pricing_transparency_score: 5%

## Confidence penalty
Lower-confidence buildings receive a penalty before the final overall-fit score is surfaced. Missing evidence should stay visible rather than being silently converted into a zero.

## Hard-stop rules
A building should normally be marked `hard_stop = yes` if any of the following are true:
- management_score <= 1 and quiet_score <= 2
- approval_speed_business_days > 7
- a required amenity is definitively missing
- security risk is high and no compensating operational control exists

## Conflict handling
When evidence conflicts:
1. prefer newer evidence over stale evidence
2. prefer higher-credibility sources over lower-credibility sources
3. treat recurring operational complaints as more decision-relevant than isolated praise
4. document the conflict instead of averaging it away

## Interpretation rule
The overall-fit score is a triage aid, not a substitute for judgment. A building with a slightly lower score but fewer unknowns can still be the better choice.
