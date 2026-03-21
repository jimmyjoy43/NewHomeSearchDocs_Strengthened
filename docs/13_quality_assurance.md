# Quality Assurance Checklist

Use this checklist after every model-assisted research pass.

## Before merging new data
- Confirm the model had the actual file or prompt context; do not assume it could read a remote repo.
- Check that building-level facts are not being written into `units.csv`.
- Check that unit-level pricing is not being copied into `buildings.csv`.
- Check every date format.
- Check every money field.
- Check that `unknown` is used instead of a guessed value.

## Rent math
- Verify base rent from the listing.
- Verify concession math.
- Verify lease term used in the net-effective calculation.
- Verify parking, pet rent, and estimated utilities before claiming a true monthly cost.

## Research QA
- Confirm that major claims have URLs and dates.
- Distinguish `confirmed`, `corroborated`, `anecdotal`, `inferred`, and `unknown`.
- Lower confidence when evidence is thin or contradictory.

## Fair-housing QA
- Remove any demographic or protected-class framing.
- Rewrite questions so they target operations, not people.

## Final pre-tour QA
- Make sure `decisions.csv` explains why a building advanced or was rejected.
- Make sure `docs/02_neighborhood_breadth_scan.md` and `docs/07_decision_log.md` were regenerated.
