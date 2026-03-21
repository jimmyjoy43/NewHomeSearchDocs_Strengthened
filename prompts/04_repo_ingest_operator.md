# Repo Ingest Operator Prompt

You are updating the canonical housing-search repo.

## Files to read first
- `README.md`
- `data/buildings.csv`
- `data/units.csv`
- `data/evidence.csv`
- `data/decisions.csv`
- `docs/02_neighborhood_breadth_scan.md`
- `docs/07_decision_log.md`

## Your job
1. Accept reviewed JSON output from a prior research step.
2. Validate that each object uses only allowed CSV columns.
3. Upsert the rows into the correct CSV file.
4. Preserve existing data when the new payload leaves a field blank.
5. Regenerate markdown reports.
6. Summarize exactly what changed.

## Rules
- Never guess missing values.
- Never replace a non-empty existing value with an empty value unless I explicitly say to overwrite.
- If a payload contains a column that does not exist in the target CSV, stop and list the mismatches.
- If a row changes a score, also update the notes or evidence so the score remains auditable.
