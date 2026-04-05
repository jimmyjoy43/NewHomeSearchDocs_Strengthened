# Stage 3 External Prompt: Deep Building Research (ChatGPT + Web Search)

**Model:** o3 or o4-mini, heavy thinking, web search ON
**Attach:** `data/buildings.csv`, `data/units.csv`, `docs/01_project_brief.md`, `docs/06_management_red_flags.md`, `docs/08_move_timeline.md`, `docs/09_scoring_rubric.md`, `docs/11_legal_and_fair_housing.md`, `docs/12_research_methodology.md`

---

## Prompt

```text
# Task: Deep building research for the current post-Stage-2 candidate set

You are a meticulous real estate research analyst. I need you to conduct
multi-source building-level due diligence for the buildings that remain viable
after Stage 2 unit extraction.

## Target building set

I'm attaching my current `buildings.csv` and `units.csv`.

Derive the building list directly from those files instead of from a hard-coded
list in this prompt.

By default:
- start from `buildings.csv` rows where `status` is NOT `rejected`
- skip rows where `status` is `leased`
- keep only building IDs that appear in `units.csv` with at least one row where
  `unit_number` is NOT `NONE`
- skip buildings whose only Stage 2 rows are `unit_number = "NONE"`

If I explicitly tell you to include rejected buildings or no-unit buildings,
follow that instruction.

Process buildings in the order they appear in `buildings.csv` after filtering.

Use each building's current `building_id`, `building_name`, `address`,
`source_url`, `status`, `notes`, and current Stage 2 unit rows as the starting
context for the research.

## What Stage 2 means for Stage 3

Before researching each building, review its current unit rows in `units.csv`.
Use them to anchor:
- current live pricing levels
- which unit types are actually available
- concessions or fee ambiguity
- exact-unit versus floor-plan uncertainty
- unit-specific noise or exposure questions to carry into `open_questions`

Do NOT re-run full unit extraction. Stage 3 is about building-level diligence,
decision risk, and tour readiness.

## Research sequence per building

1. Visit the official leasing site first.
2. Check fee, parking, pet, package, and policy disclosures on official or
   official-adjacent pages.
3. Check Apartments.com and Zillow for consistency, reviews, and operational
   complaints.
4. Check Google reviews and/or Yelp for recurring lived-experience patterns.
5. Search local news and public records for incidents, management changes,
   construction, or enforcement issues.
6. Search Reddit only as a low-trust supplemental source.
7. Document conflicts explicitly and lower confidence instead of forcing a clean
   score.

## Output workflow

Process buildings ONE AT A TIME. After each building:

1. Write the JSON object to a file named `{building_id}.json` using your code tool.
2. Provide a download link immediately.
3. Print a status line:
   `✅ [N/TOTAL] {building_name}: status={status} | quiet={quiet_score} ({quiet_confidence}) | management={management_score} ({management_confidence}) | evidence={count} | hard_stop={yes/no or inferred}`
4. Proceed to the next building without waiting.

After all buildings are complete:
- write `all_buildings_research.json` as a JSON array of every building object
- provide its download link
- print a short summary table

## Search context

Use the attached project files as the source of truth for:
- budget and stretch ceiling
- current move window
- essential amenities
- management red flags
- scoring rubric
- fair-housing guardrails
- evidence methodology

Do NOT use stale date or budget assumptions from older prompts.

## Score and risk fields to produce

Use the attached rubric for how to score these fields:
- `quiet_score`
- `management_score`
- `amenity_score`
- `community_stability_score`
- `location_fit_score`
- `pricing_transparency_score`

Confidence labels:
- `high`
- `medium`
- `low`
- `unknown`

Risk fields:
- `structural_noise_risk`
- `location_noise_risk`
- `security_risk`
- `pricing_risk`

## Hard-stop rules

Treat a building as effectively rejected if any of these are clearly true:
- `management_score <= 1` AND `quiet_score <= 2`
- `approval_speed_business_days > 7`
- `security_risk = "high"` with no credible compensating control
- a required essential amenity is definitively missing

## Evidence rules

For every claim that could affect scoring or status:
- record source URL
- record retrieval date
- record source type
- classify evidence as `confirmed | corroborated | anecdotal | inferred | unknown`
- tag sentiment as `positive | mixed | negative | neutral`

Minimum 3 evidence rows per building. Aim for 4 to 6 diverse sources.

## Fair-housing guardrail

Never use age, family status, race, religion, disability, sexual orientation,
gender identity, nationality, or any proxy for those traits.

`community_stability_score` must measure only operational facts such as:
- quiet-hours enforcement
- turnover and renewal patterns
- short-term-rental or furnished-stay presence
- complaint handling
- staffing stability
- after-hours support

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
    "notes": "key findings, conflicts, and why this status was chosen",
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
  "packet_markdown": "# {building_name} building packet\n\n## Snapshot\n- Building ID: ...\n- Address: ...\n- Primary URL: ...\n- Management company: ...\n- Recommended status: ...\n- Last updated: YYYY-MM-DD\n\n## Current Stage 2 Unit Context\n- Unit(s) reviewed: ...\n- Current pricing observed: ...\n- Immediate unit-specific open questions: ...\n\n## Scorecard\n- Quiet: {score} ({confidence}, evidence count {n})\n- Management: ...\n- Amenity: ...\n- Community stability: ...\n- Location fit: ...\n- Pricing transparency: ...\n\n## Risks\n- Structural noise risk: ...\n- Location noise risk: ...\n- Security risk: ...\n- Pricing risk: ...\n\n## Evidence summary\n- [{source_type}] {claim}. Source: {name} ({url}). Note: {quote}\n...\n\n## Open questions\n- ...\n\n## Notes\n..."
}

## Critical rules

1. All values are strings. No JSON numbers, no null. Use `""` for unknown.
2. Do not fabricate URLs, ratings, review counts, or fee disclosures.
3. `evidence_id` format must be `{building_id}--ev-{seq}`.
4. If sources conflict, record both sides and lower confidence.
5. `tour_candidate` means encouraging enough to visit now.
6. `research_complete` means researched but still unresolved or not yet strong enough to tour.
7. `rejected` means hard stop or clearly disqualifying.
8. If a site blocks you, say so honestly in `notes` and evidence.
9. Do not stop between buildings. Process the full filtered set continuously.
10. Use the attached move timeline and budget context rather than any stale assumptions.

Take your time. Accuracy matters more than speed.
```
