# Stage 2 Prompt: Unit Extraction (JSON)

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
- 1 bedroom or larger
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
- Do not guess utilities, deposit, or fees. Leave blank if unavailable.
- If the listing says "available now," convert it to the current date.
- Do not calculate `net_effective_rent` or `true_monthly_cost`; the repo scripts do that deterministically.
