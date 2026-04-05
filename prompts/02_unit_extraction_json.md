# Stage 2 Prompt: Unit Extraction (JSON)

> Legacy single-building prompt.
> Do not use this for the external bulk Stage 2 run.
> For the current external workflow, use [`prompts_external/02_unit_extraction_chatgpt.md`](C:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts_external/02_unit_extraction_chatgpt.md), which derives the building list directly from `data/buildings.csv`.

Use this after a building survives the breadth scan.

## Context
Read:
- `README.md`
- `docs/01_project_brief.md`
- `docs/03_essential_amenities.md`
- `docs/09_scoring_rubric.md`
- `data/buildings.csv`
- `data/units.csv`

## Building to search
- building_name: [FILL IN]
- building_id: [FILL IN]
- listing_url: [FILL IN]

## Task
Extract qualifying units from the listing.
Filters:
- studio or 1 bedroom only
- exclude 2 bedroom and larger units
- realistically in budget
- available soon enough for the current move window

## Output format
Return a single JSON object with this shape:

```json
{
  "rows": [
    {
      "unit_id": "",
      "building_id": "",
      "unit_number": "",
      "listing_url": "",
      "bedrooms": "",
      "bathrooms": "",
      "sqft": "",
      "base_rent": "",
      "concession_value_total": "",
      "lease_term_months": "",
      "available_date": "YYYY-MM-DD or blank",
      "application_fee": "",
      "admin_fee": "",
      "security_deposit": "",
      "parking_cost": "",
      "pet_rent": "",
      "estimated_utilities": "",
      "balcony": "yes|no|unknown",
      "in_unit_laundry": "yes|no|unknown",
      "dishwasher": "yes|no|unknown",
      "central_ac": "yes|no|unknown",
      "natural_light": "yes|no|unknown",
      "closet_storage": "yes|no|unknown",
      "exact_unit_shown": "yes|no|unknown",
      "exposure": "",
      "nearest_noise_source": "",
      "notes": "",
      "last_updated": "YYYY-MM-DD"
    }
  ]
}
```

## Rules
- Do not repeat building-level facts here unless they are unit-specific.
- Numeric-like fields must use bare numeric strings only. No `$`, commas, or ranges. Examples: `3305`, `150`, `7048.50`.
- If the source only shows a range or a bundled total monthly price and you cannot isolate the exact field value, leave that field blank and explain it in `notes`.
- Do not guess utilities, deposit, or fees. Leave blank if unavailable.
- If the listing says "available now," convert it to the current date.
- Do not calculate `net_effective_rent` or `true_monthly_cost`; the repo scripts do that deterministically.
