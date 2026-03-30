# Stage 2 External Prompt: Bulk Unit Extraction (ChatGPT + Web Search)

**Model:** o3 or o4-mini, heavy thinking, web search ON
**Attach:** `data/buildings.csv`

---

## Prompt

```text
# Task: Extract available 1BR+ apartment units from 16 buildings

You are a real estate research assistant. I need you to visit each building's
official leasing website (and listing aggregators like Apartments.com as backup)
and extract every currently available 1-bedroom or larger unit that could
realistically fall within a $3,800–$5,328/month all-in budget, available by
approximately April 20, 2026.

## Buildings to search

I'm attaching my buildings.csv file. Process ONLY rows where status is NOT
"rejected". Here are the 16 active buildings and their primary URLs:

| building_id | building_name | source_url |
|---|---|---|
| columbia-square-living-1550-n-el-centro-ave | Columbia Square Living | https://www.columbiasquareliving.com/ |
| the-baxter-1818-n-cherokee-ave | The Baxter | https://thebaxterhollywood.com/ |
| skyview-sunset-1511-n-fairfax-ave | Skyview Sunset | https://www.skyviewsunset.com/ |
| 7950-west-sunset-7950-w-sunset-blvd | 7950 West Sunset | https://7950westsunset.com/ |
| the-crown-8350-santa-monica-blvd | The Crown | https://thecrownweho.com/ |
| element-weho-1425-n-crescent-heights-blvd | Element WeHo | https://www.elementweho.com/ |
| aka-8500-sunset-8500-sunset-blvd | The Apartment Residences at AKA | https://www.8500sunsetapartments.com/ |
| silhouette-apartments-1233-n-highland-ave | Silhouette Apartments | https://silhouettela.com/ |
| avalon-west-hollywood-7316-santa-monica-blvd | Avalon West Hollywood | https://www.avaloncommunities.com/california/west-hollywood-apartments/avalon-west-hollywood/ |
| line-lofts-1737-n-las-palmas-ave | Line Lofts | https://www.thelinelofts.com/ |
| the-charlie-weho-7617-santa-monica-blvd | The Charlie WeHo | https://thecharlieweho.com/ |
| vantage-hollywood-1710-n-fuller-ave | Vantage Hollywood | https://www.equityapartments.com/los-angeles/west-hollywood/vantage-apartments |
| hanover-hollywood-6200-w-sunset-blvd | Hanover Hollywood | https://www.hanoverhollywood.com/ |
| lumina-hollywood-1522-gordon-st | Lumina Hollywood | https://luminahollywood.com/ |
| el-centro-apartments-and-bungalows-6200-hollywood-blvd | El Centro Apartments & Bungalows | https://www.elcentrohollywood.com/ |
| the-avenue-hollywood-1619-n-la-brea-ave | The Avenue Hollywood | https://theavenuehollywood.com/ |

## For each building

1. Visit the official leasing site first. If it doesn't show live inventory or
   pricing, check Apartments.com and Zillow as backup sources.
2. Extract every 1BR+ unit that is available now through ~April 20, 2026 and has
   a base rent that could plausibly land at or below $5,328/month all-in.
3. If a building has zero qualifying units, include a single row for that
   building with unit_number "NONE" and a note explaining why (e.g., "No 1BR
   currently listed" or "All 1BR units above $5,500").

## Output cadence

Process buildings ONE AT A TIME in the order listed. After each building:

1. Write all unit rows for that building to a file named
   `units_{building_id}.json` using your code tool.
2. Provide a download link immediately.
3. Print a status line:
   `✅ [N/16] {building_name}: {count} unit(s) extracted`
4. Proceed to the next building without waiting.

After all 16, write a combined file `all_units.json` with every row and provide
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

Take your time. Accuracy matters more than speed.
```
