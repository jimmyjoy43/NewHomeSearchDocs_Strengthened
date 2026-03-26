# Stage 3 External Prompt: Deep Building Research (ChatGPT + Web Search)

**Model:** o3 or o4-mini, heavy thinking, web search ON  
**Attach:** `data/buildings.csv`

---

## Prompt

```text
# Task: Deep Building Research — 16 Active Apartment Candidates

You are a meticulous real estate research analyst. For each of the 16 buildings
below, conduct multi-source due diligence and produce a structured research
payload.

## CRITICAL: Output workflow

Process buildings ONE AT A TIME in the order listed. After each building:

1. Write the JSON object to a file named `{building_id}.json` using your code tool.
2. Provide a download link immediately.
3. Print a status line:
   ✅ [N/16] {building_name}
      Status: {status} | Quiet: {score} ({confidence}) | Mgmt: {score} ({confidence})
      Evidence rows: {count} | Hard stop: {yes/no}
      📥 Download: [link]
4. Proceed to the next building without waiting.

After all 16:
- Write `all_buildings_research.json` (JSON array of all 16 objects) and provide
  its download link.
- Print a summary table.

---

## Input

I'm attaching my buildings.csv. Process ONLY rows where status is NOT
"rejected." Use each building's existing notes and open_questions columns as
starting points.

## Buildings to research (process in this order)

| # | building_id | building_name | address | source_url |
|---|---|---|---|---|
| 1 | columbia-square-living-1550-n-el-centro-ave | Columbia Square Living | 1550 N El Centro Ave, LA 90028 | https://www.columbiasquareliving.com/ |
| 2 | the-baxter-1818-n-cherokee-ave | The Baxter | 1818 N Cherokee Ave, LA 90028 | https://thebaxterhollywood.com/ |
| 3 | skyview-sunset-1511-n-fairfax-ave | Skyview Sunset | 1511 N. Fairfax Ave, LA 90046 | https://www.skyviewsunset.com/ |
| 4 | 7950-west-sunset-7950-w-sunset-blvd | 7950 West Sunset | 7950 W Sunset Blvd, LA 90046 | https://7950westsunset.com/ |
| 5 | the-crown-8350-santa-monica-blvd | The Crown | 8350 Santa Monica Blvd, WeHo 90069 | https://thecrownweho.com/ |
| 6 | element-weho-1425-n-crescent-heights-blvd | Element WeHo | 1425 N Crescent Heights Blvd, WeHo 90046 | https://www.elementweho.com/ |
| 7 | aka-8500-sunset-8500-sunset-blvd | The Apartment Residences at AKA | 8500 Sunset Blvd, WeHo 90069 | https://www.8500sunsetapartments.com/ |
| 8 | silhouette-apartments-1233-n-highland-ave | Silhouette Apartments | 1233 N Highland Ave, LA 90038 | https://silhouettela.com/ |
| 9 | avalon-west-hollywood-7316-santa-monica-blvd | Avalon West Hollywood | 7316 Santa Monica Blvd, WeHo 90046 | https://www.avaloncommunities.com/california/west-hollywood-apartments/avalon-west-hollywood/ |
| 10 | line-lofts-1737-n-las-palmas-ave | Line Lofts | 1737 N Las Palmas Ave, LA 90028 | https://www.thelinelofts.com/ |
| 11 | the-charlie-weho-7617-santa-monica-blvd | The Charlie WeHo | 7617 Santa Monica Blvd, WeHo 90046 | https://thecharlieweho.com/ |
| 12 | vantage-hollywood-1710-n-fuller-ave | Vantage Hollywood | 1710 N Fuller Ave, LA 90046 | https://www.equityapartments.com/los-angeles/west-hollywood/vantage-apartments |
| 13 | hanover-hollywood-6200-w-sunset-blvd | Hanover Hollywood | 6200 W Sunset Blvd, LA 90028 | https://www.hanoverhollywood.com/ |
| 14 | lumina-hollywood-1522-gordon-st | Lumina Hollywood | 1522 Gordon St, LA 90028 | https://luminahollywood.com/ |
| 15 | el-centro-apartments-and-bungalows-6200-hollywood-blvd | El Centro Apartments & Bungalows | 6200 Hollywood Blvd, LA 90028 | https://www.elcentrohollywood.com/ |
| 16 | the-avenue-hollywood-1619-n-la-brea-ave | The Avenue Hollywood | 1619 N La Brea Ave, LA 90028 | https://theavenuehollywood.com/ |

---

## Search context

Personal apartment search. Key priorities (in order):
1. Quiet — sleep, work, daily peace. #1 deal-breaker.
2. Management quality — responsive, transparent, human.
3. Cat-friendly with reasonable pet terms.
4. In-unit laundry, dishwasher, central AC.
5. Secure packages, controlled access, decent parking.

Budget: $3,800–$5,328/month all-in. Move-in target: April 20, 2026.

## Source hierarchy

Tier 1 (most trusted): Official leasing site, fee schedules, public property
records, direct staff disclosures.
Tier 2: Local news, reputable reporting, official complaints/enforcement.
Tier 3: Google reviews, Yelp, Apartments.com, ApartmentRatings.
Tier 4 (least trusted): Reddit, neighborhood groups, social media.

Marketing copy = discovery tool, not trust signal.

## Scoring rubric

### quiet_score (weight: 30%)
- 5: Consistently quiet; no chronic source identified
- 4: Minor tradeoffs, no daily disruption pattern
- 3: Noticeable but likely manageable noise risk
- 2: Recurring noise issue or risky exposure
- 1: Severe or chronic noise problem

### management_score (weight: 25%)
- 5: Fast, transparent, credible, well-staffed
- 4: Generally strong with isolated friction
- 3: Mixed but workable
- 2: Repeated slow, evasive, or understaffed signals
- 1: Operationally broken or untrustworthy

### amenity_score (weight: 15%)
- 5: All essentials + strong useful extras
- 4: All essentials + some meaningful extras
- 3: Essentials present, extras unremarkable
- 2: One essential missing or seriously compromised
- 1: Multiple essentials missing or unreliable

### community_stability_score (weight: 15%)
Measure ONLY operational signals: quiet-hours enforcement, short-term-rental
presence, renewal patterns, turnover, resident complaints about common areas.
NEVER use demographic language or protected-class proxies.
- 5: Strong stable long-term operations
- 4: Mostly stable, limited churn
- 3: Mixed
- 2: Frequent churn, party behavior, or hotel-like use
- 1: Highly unstable occupancy

### location_fit_score (weight: 10%)
- 5: Excellent Hollywood/WeHo daily-routine fit
- 4: Strong fit
- 3: Acceptable but imperfect
- 2: Material inconvenience
- 1: Bad fit

### pricing_transparency_score (weight: 5%)
- 5: Fees and concessions clear, simple, stable
- 4: Mostly clear
- 3: Some ambiguity
- 2: Repeated fee ambiguity or bait-and-switch risk
- 1: Material pricing opacity

### Confidence labels (one per scored category)
- high: multiple credible sources or in-person verification
- medium: credible but incomplete
- low: thin evidence, mostly soft signals
- unknown: not enough to score responsibly

### Risk fields (one each)
- structural_noise_risk: low | medium | high | unknown
- location_noise_risk: low | medium | high | unknown
- security_risk: low | medium | high | unknown
- pricing_risk: low | medium | high | unknown

## Hard-stop rules (auto-reject if ANY is true)
- management_score <= 1 AND quiet_score <= 2
- approval_speed_business_days > 7
- security_risk = "high" with no compensating control
- A required essential amenity is definitively missing

## Management red flags to look for
- Vague answers on fees, parking, or lease policies
- Cannot show the exact unit
- Pushes concessions while dodging building issues
- Repeated evidence of ignored maintenance
- Chronic noise, theft, elevator, or package failures
- High staff turnover or disorganization
- AI-only leasing contact with no human fallback

## Evidence rules
For each claim that could affect a scoring decision:
- Record source URL, retrieval date, source type
- Classify: confirmed | corroborated | anecdotal | inferred | unknown
- Tag sentiment: positive | mixed | negative | neutral
- Conflicts: document both sides, prefer newer + higher-credibility source,
  lower confidence instead of forcing a score

## Fair-housing guardrail
Never use age, family status, race, religion, disability, sexual orientation,
gender identity, or nationality as criteria or proxies. community_stability_score
measures ONLY operational facts (turnover, enforcement, short-term rentals).

## Research sequence per building

1. Visit official leasing site — amenities, fees, pet policy, parking, concessions
2. Check Apartments.com — rating, review count, resident complaints
3. Check Google reviews and/or Yelp — look for patterns not isolated reviews
4. Search local news — management changes, construction, incidents
5. Search Reddit (r/AskLosAngeles, r/LosAngeles) for the building name
6. Document conflicting evidence on both sides; lower confidence
7. Score only where you have evidence; use "" where you can't

## JSON shape for each building file

{
  "building_row": {
    "building_id": "exact-id-from-buildings-csv",
    "management_company": "",
    "quiet_score": "",
    "quiet_confidence": "high|medium|low|unknown",
    "quiet_evidence_count": "",
    "management_score": "",
    "management_confidence": "high|medium|low|unknown",
    "management_evidence_count": "",
    "amenity_score": "",
    "amenity_confidence": "high|medium|low|unknown",
    "amenity_evidence_count": "",
    "community_stability_score": "",
    "community_stability_confidence": "high|medium|low|unknown",
    "community_stability_evidence_count": "",
    "location_fit_score": "",
    "pricing_transparency_score": "",
    "approval_speed_business_days": "",
    "structural_noise_risk": "low|medium|high|unknown",
    "location_noise_risk": "low|medium|high|unknown",
    "security_risk": "low|medium|high|unknown",
    "pricing_risk": "low|medium|high|unknown",
    "status": "research_complete|tour_candidate|rejected",
    "review_scan_done": "yes",
    "deep_research_done": "yes",
    "open_questions": "what still needs in-person verification",
    "notes": "key findings and any conflicts",
    "last_updated": "YYYY-MM-DD"
  },
  "evidence_rows": [
    {
      "evidence_id": "{building_id}--ev-{seq}",
      "scope_type": "building",
      "scope_id": "same as building_id",
      "criterion": "quiet|management|amenities|community_stability|location_fit|pricing_transparency|security",
      "claim": "one factual statement",
      "source_type": "official|news|review|reddit|public_record|tour|call",
      "source_name": "human-readable source name",
      "source_url": "exact URL you visited",
      "retrieved_date": "YYYY-MM-DD",
      "evidence_class": "confirmed|corroborated|anecdotal|inferred|unknown",
      "sentiment": "positive|mixed|negative|neutral",
      "quote_or_note": "relevant excerpt or summary"
    }
  ],
  "packet_markdown": "# {building_name} building packet\n\n## Snapshot\n- Building ID: ...\n- Address: ...\n- Primary URL: ...\n- Management company: ...\n- Recommended status: ...\n- Last updated: YYYY-MM-DD\n\n## Scorecard\n- Quiet: {score} ({confidence}, evidence count {n})\n- Management: ...\n- Amenity: ...\n- Community stability: ...\n- Location fit: ...\n- Pricing transparency: ...\n\n## Risks\n- Structural noise risk: ...\n- Location noise risk: ...\n- Security risk: ...\n- Pricing risk: ...\n\n## Evidence summary\n- [{source_type}] {claim}. Source: {name} ({url}). Note: {quote}\n...\n\n## Open questions\n- ...\n\n## Notes\n..."
}

## Critical rules

1. All values are strings. No JSON numbers, no null. Use "" for unknown.
2. Do not fabricate URLs. Only cite pages you actually found.
3. Do not fabricate review counts or ratings.
4. evidence_id format: {building_id}--ev-{seq}
5. Status decisions:
   - tour_candidate = encouraging enough to visit
   - research_complete = gathered but not decisive
   - rejected = hard stop or clearly disqualifying
6. Minimum 3 evidence rows per building. Aim for 4–6 diverse sources.
7. If a site blocks you, note that honestly rather than guessing.
8. Do not stop between buildings. Process all 16 continuously.

Take your time on each building. Accuracy matters more than speed.
```
