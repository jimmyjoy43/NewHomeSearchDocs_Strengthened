# Stage 5 Prompt: Final Review

Use this when the CSVs, decisions, and building packets are up to date.

Run this locally against the current repo state. Do not use stale packet paths or old chat summaries as the primary source of truth.

## Context
Read:
- `README.md`
- `docs/01_project_brief.md`
- `docs/03_essential_amenities.md`
- `docs/06_management_red_flags.md`
- `docs/08_move_timeline.md`
- `docs/09_scoring_rubric.md`
- `docs/02_neighborhood_breadth_scan.md`
- `docs/10_unit_comparison.md`
- `data/buildings.csv`
- `data/units.csv`
- `data/evidence.csv`
- `data/tours.csv`
- `data/decisions.csv`
- `research/*.json`

## Finalists
If finalists are already explicit in `data/decisions.csv` or `data/buildings.csv`, derive them from there.

If you still need a shortlist, prefer buildings that:
- have a current viable unit in `data/units.csv`
- are not `rejected` or `leased`
- have strong current evidence after Stage 3
- remain realistic on timing after any Stage 4 tour findings

If I provide a finalist list manually, use that list instead.

## What to produce
1. Head-to-head table of essential amenities and unresolved unknowns.
2. Score summary, with confidence commentary.
3. Financial comparison using true monthly cost and first-month cash outlay.
4. Red-flag summary with the source and whether it is confirmed, corroborated, anecdotal, or inferred.
5. One clear recommendation in the first sentence.
6. The biggest single remaining risk with that pick.
7. The next 48 hours of actions.

## Rules
- First sentence must contain the recommendation.
- Do not treat missing data as zero.
- Do not let a high amenity score hide a management or quietness problem.
- Use `data/evidence.csv` and `research/*.json` for red-flag sourcing, not memory.
- If a finalist lacks a currently viable unit in `data/units.csv`, say so clearly.
- If a building looks good overall but the toured unit was weak, separate building-level and unit-level conclusions.
- Call out strong primary parking, guest parking, and around-the-clock on-site human presence explicitly because they are current priorities.
- If approval timing makes a finalist unrealistic, say so explicitly.
- If the best-scoring option is also the least certain, say that directly.
- Prefer evidence-backed caveats over smooth prose.
