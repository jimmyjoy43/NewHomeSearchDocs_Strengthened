# Automation Notes

## Validation
`python scripts/validate_data.py`

Checks:
- required columns
- allowed enum values
- numeric/date sanity
- unique IDs
- cross-file references

## Score computation
`python scripts/compute_scores.py`

Updates:
- `overall_fit_score`
- `hard_stop`

## Report regeneration
`python scripts/generate_markdown_reports.py`

Rebuilds:
- `docs/02_neighborhood_breadth_scan.md`
- `docs/07_decision_log.md`
- `docs/10_unit_comparison.md`

## Notion sync
`python scripts/sync_to_notion.py --dry-run`

This is optional and intentionally conservative.
- dry-run is the default
- `--apply` is required for writes
- the workflow is manual-dispatch only

## Workflow policy
Validation and report generation should be automatic.
External sync should be explicit.
