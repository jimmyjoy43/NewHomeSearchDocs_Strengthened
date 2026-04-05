# Stage 2 External Prompt: Bulk Unit Extraction (ChatGPT + Web Search)

**Model:** o3 or o4-mini, heavy thinking, web search ON
**Attach:** `data/buildings.csv`, `docs/01_project_brief.md`, `docs/08_move_timeline.md`

---

## Prompt

```text
# Task: Extract available studio and 1BR apartment units from the current building set

You are a real estate research assistant. I need you to visit each building's
official leasing website (and listing aggregators like Apartments.com as backup)
and extract every currently available studio or 1-bedroom unit that could
realistically fall within the current all-in budget and current move window
defined in the attached project files.

## Buildings to search

I'm attaching my buildings.csv file. Derive the building list directly from the
attached CSV instead of from a hard-coded list in this prompt.

By default:
- process rows where `status` is NOT `rejected`
- skip rows where `status` is `leased`

If I explicitly tell you to include rejected buildings too, follow that instruction.

Use each row's `building_id`, `building_name`, `source_url`, `status`, and `notes`
as the starting context for the building.

## For each building

1. Visit the official leasing site first. If it doesn't show live inventory or
   pricing, check Apartments.com and Zillow as backup sources.
2. Extract every studio or 1-bedroom unit that is available now through ~April 20, 2026,
   exclude 2-bedroom and larger units, and keep only units whose base rent could
   plausibly land at or below $5,328/month all-in.
3. If a building has zero qualifying units, include a single row for that
   building with unit_number "NONE" and a note explaining why (e.g., "No 1BR
   or studio currently listed" or "All studio / 1BR units above $5,500").

## Output cadence

Process buildings ONE AT A TIME in the order they appear in the attached CSV after
filtering. After each building:

1. Write all unit rows for that building to a file named
   `units_{building_id}.json` using your code tool.
2. Provide a download link immediately.
3. Print a status line:
   `✅ [N/TOTAL] {building_name}: {count} unit(s) extracted`
4. Proceed to the next building without waiting.

After all buildings are complete, write a combined file `all_units.json` with every row and provide
its download link plus a summary table.

## Output format

Every file uses this shape. Every value must be a string. No numbers, no nulls.

{
  "rows": [
    {
      "unit_id": "{building_id}--{unit_number}",
      "building_id": "",
      "unit_number": "",
      "listing_url": "URL where you found this unit",
      "bedrooms": "",
      "bathrooms": "",
      "sqft": "",
      "base_rent": "",
      "concession_value_total": "total dollar value of concession over full lease",
      "lease_term_months": "",
      "available_date": "YYYY-MM-DD or blank",
      "application_fee": "",
      "admin_fee": "",
      "security_deposit": "",
      "parking_cost": "monthly",
      "pet_rent": "monthly",
      "estimated_utilities": "",
      "balcony": "yes|no|unknown",
      "in_unit_laundry": "yes|no|unknown",
      "dishwasher": "yes|no|unknown",
      "central_ac": "yes|no|unknown",
      "natural_light": "unknown",
      "closet_storage": "unknown",
      "exact_unit_shown": "unknown",
      "exposure": "",
      "nearest_noise_source": "",
      "notes": "floor, view, promo terms, etc.",
      "last_updated": "YYYY-MM-DD"
    }
  ]
}

## Critical rules

1. Every value is a string. No JSON numbers, no null. Use "" for unknown.
2. Numeric-like fields must be bare numeric strings only. No `$`, commas, text, or ranges. Examples: `3305`, `150`, `7048.50`.
3. If a site only shows a range or bundled total monthly price and you cannot isolate the exact field value, leave that field blank and explain it in `notes`.
4. Do not calculate net_effective_rent or true_monthly_cost — leave them out.
5. Do not guess fees. Leave blank if undisclosed.
6. "Available now" → today's date.
7. Concession math: record total dollar savings and lease_term_months separately.
8. One row per unit. Same floor plan at different prices = separate rows.
9. unit_id format: {building_id}--{unit_number} with double dash.
10. Do not include building-level facts (scores, management, amenity flags).
11. Source preference: Official site > Apartments.com > Zillow.
12. If a site blocks you, say so in notes rather than fabricating data.
13. Use the attached move timeline and budget context rather than any stale date or price assumptions.
14. Unit type filter is strict: include studios and 1-bedroom units only. Exclude 2BR+ even if they fit the budget.

Take your time. Accuracy matters more than speed.
```
