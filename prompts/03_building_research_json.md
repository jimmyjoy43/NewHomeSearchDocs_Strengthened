# Stage 3 Prompt: Building Research (JSON + packet draft)

Use this for the deeper diligence pass on a serious candidate.

## Context
Read:
- `README.md`
- `docs/03_essential_amenities.md`
- `docs/06_management_red_flags.md`
- `docs/09_scoring_rubric.md`
- `docs/11_legal_and_fair_housing.md`
- `docs/12_research_methodology.md`
- `data/buildings.csv`
- `data/evidence.csv`
- `data/decisions.csv`

## Building to research
- building_name: [FILL IN]
- building_id: [FILL IN]
- address: [FILL IN]
- primary_url: [FILL IN]

## Task
1. Gather evidence from multiple source tiers.
2. Assign scores only where evidence supports them.
3. Log durable claims as evidence rows.
4. Draft a building packet.

## Output format
Return a single JSON object with this exact top-level shape:

```json
{
  "building_row": {
    "building_id": "",
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
    "status": "research_complete or tour_candidate or rejected",
    "review_scan_done": "yes",
    "deep_research_done": "yes",
    "open_questions": "",
    "notes": "",
    "last_updated": "YYYY-MM-DD"
  },
  "evidence_rows": [
    {
      "evidence_id": "",
      "scope_type": "building",
      "scope_id": "",
      "criterion": "",
      "claim": "",
      "source_type": "official|news|review|reddit|public_record|tour|call",
      "source_name": "",
      "source_url": "",
      "retrieved_date": "YYYY-MM-DD",
      "evidence_class": "confirmed|corroborated|anecdotal|inferred|unknown",
      "sentiment": "positive|mixed|negative|neutral",
      "quote_or_note": ""
    }
  ],
  "packet_markdown": "full markdown packet as a string"
}
```

## Rules
- Use `community_stability_score`, not demographic language.
- When evidence conflicts, lower confidence and explain the conflict in `notes` and `packet_markdown`.
- If the building trips a hard stop, state that clearly in `notes`.
- Do not fabricate URLs, dates, or evidence IDs.
