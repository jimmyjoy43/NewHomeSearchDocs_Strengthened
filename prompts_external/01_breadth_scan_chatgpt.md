# Stage 1 External Prompt: Breadth Scan (ChatGPT + Web Search)

**Model:** o3 or o4-mini, heavy thinking, web search ON

Attach or paste the current versions of:

- `README.md`
- `docs/01_project_brief.md`
- `docs/03_essential_amenities.md`
- `docs/04_nice_to_have_amenities.md`
- `docs/06_management_red_flags.md`
- `docs/08_move_timeline.md`
- `docs/09_scoring_rubric.md`

Do not attach old `data/buildings.csv` or `data/decisions.csv` if this is a fresh restart.

---

## Prompt

```text
# Task: Stage 1 Breadth Scan for Apartment Search

You are a meticulous apartment-search research assistant. I am restarting this search from the beginning, so do not anchor on any old candidate list unless I explicitly provide one.

Use the attached repo files as the source of truth for:
- geography
- budget
- move timing
- essential amenities
- nice-to-have amenities
- operational red flags
- scoring philosophy

## Important rules

1. Do not assume you can read a remote GitHub repo unless the contents were actually attached or pasted here.
2. Use current live web information.
3. Use `unknown` rather than guessing.
4. Do not use demographic or protected-class proxies.
5. Focus on building-level facts only. Do not create unit rows in this stage.
6. Every value in the final JSON must be a string. No JSON numbers, no nulls.

## Task

Find likely-fit apartment buildings in the target geography that plausibly match the current brief.

Use a mix of:
- official leasing sites
- at least one major listing aggregator when available
- review or independent sources only when they add meaningful signal
- local reporting only when risk signals appear

For each building:
- capture durable building-level facts only
- flag clear unknowns and obvious risks in `notes`
- leave score fields blank unless there is enough evidence for a responsible preliminary value

## Output format

Return exactly one JSON object with this shape:

{
  "rows": [
    {
      "building_id": "",
      "building_name": "",
      "address": "",
      "neighborhood": "",
      "source_url": "",
      "management_company": "",
      "building_class": "",
      "cat_friendly": "yes|no|unknown",
      "controlled_access": "yes|no|unknown",
      "gym": "yes|no|unknown",
      "pool": "yes|no|unknown",
      "coworking": "yes|no|unknown",
      "conference_room": "yes|no|unknown",
      "ev_charging": "yes|no|unknown",
      "rooftop": "yes|no|unknown",
      "location_fit_score": "",
      "pricing_transparency_score": "",
      "status": "candidate",
      "notes": "short factual note",
      "last_updated": "YYYY-MM-DD"
    }
  ]
}

## Output rules

1. One building per object.
2. Keep the JSON flat. No nested objects.
3. Do not fabricate URLs, dates, or operators.
4. Use bare strings for every field.
5. Do not include unit-level pricing or unit numbers.
6. In `notes`, include only concrete risks, conflicts, or unresolved unknowns.

Return only the final JSON object, with no prose before or after it.
```
