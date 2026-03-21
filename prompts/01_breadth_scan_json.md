# Stage 1 Prompt: Breadth Scan (JSON)

Use this with a browsing-capable model.

## Context
Read these project files first:
- `README.md`
- `docs/01_project_brief.md`
- `docs/03_essential_amenities.md`
- `docs/04_nice_to_have_amenities.md`
- `docs/06_management_red_flags.md`
- `docs/09_scoring_rubric.md`
- `data/buildings.csv`
- `data/decisions.csv`

Important:
- Do not assume you can read a remote GitHub repo unless the contents were actually pasted or uploaded in the current workspace.
- Use `unknown` rather than guessing.
- Do not use demographic or protected-class proxies.

## Task
Find likely-fit buildings in the target geography.
Use a mix of:
- official leasing sites
- at least one large listing aggregator
- independent review surfaces if immediately relevant
- local reporting only when risk signals appear

## Output format
Return a single JSON object with this shape:

```json
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
```

## Rules
- One building per object.
- Do not create unit rows in this stage.
- Leave scores blank unless evidence is strong enough to support a preliminary value.
- In `notes`, flag only concrete risks or decision-relevant unknowns.
- Keep the JSON flat; do not nest sub-objects.
