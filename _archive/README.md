# New Home Search Docs (Strengthened)

This is a repaired, normalized, and safer version of the apartment-search operating system.

## What changed

The original design had good intent: structured files, repeatable prompts, and a bias toward evidence over marketing copy. The repaired version keeps that discipline but fixes the weakest parts.

### Major upgrades

1. **Normalized data model**
   - `data/buildings.csv` now stores one row per building.
   - `data/units.csv` now stores one row per unit.
   - `data/evidence.csv` captures source provenance.
   - `data/decisions.csv` is now the canonical decision log.

2. **Safer scoring system**
   - The old "adult vibe" criterion has been replaced with **community_stability_score**.
   - Overall ranking uses a documented weighted utility model instead of pretending that 1-5 scores are linearly additive.
   - Confidence and evidence counts are tracked separately from the score itself.

3. **Explicit uncertainty handling**
   - Tri-state fields use `yes`, `no`, or `unknown`.
   - Missing evidence is not treated as a negative.
   - Unknown-heavy buildings stay visible but receive a confidence penalty and a QA flag.

4. **Better research method**
   - Research now prioritizes official sources, leasing disclosures, public records, local reporting, and only then reviews and social media.
   - Every durable claim should be logged in `data/evidence.csv` with a URL and retrieval date.

5. **Structured model outputs**
   - Prompts now request JSON, not raw CSV blocks.
   - JSON can be reviewed and then merged into canonical CSVs with the included scripts.

6. **Fair-housing and legal guardrails**
   - The repo now prohibits demographic proxies and protected-class inferences.
   - Tour questions and scoring criteria are framed around objective operational signals instead.

7. **Safer automation**
   - Validation is stricter.
   - Report generation is deterministic.
   - Notion sync is optional and manual-dispatch only, with dry-run as the default.

## Directory structure

```text
NewHomeSearchDocs_Strengthened/
├── README.md
├── .gitignore
├── requirements.txt
├── config/
│   └── decision_config.json
├── data/
│   ├── buildings.csv
│   ├── units.csv
│   ├── evidence.csv
│   ├── tours.csv
│   ├── contacts.csv
│   └── decisions.csv
├── docs/
│   ├── 01_project_brief.md
│   ├── 02_neighborhood_breadth_scan.md
│   ├── 03_essential_amenities.md
│   ├── 04_nice_to_have_amenities.md
│   ├── 05_tour_questions.md
│   ├── 06_management_red_flags.md
│   ├── 07_decision_log.md
│   ├── 08_move_timeline.md
│   ├── 09_scoring_rubric.md
│   ├── 10_unit_comparison.md
│   ├── 11_legal_and_fair_housing.md
│   ├── 12_research_methodology.md
│   ├── 13_quality_assurance.md
│   └── 14_automation.md
├── prompts/
│   ├── 01_breadth_scan_json.md
│   ├── 02_unit_extraction_json.md
│   ├── 03_building_research_json.md
│   ├── 04_repo_ingest_operator.md
│   └── 05_final_review.md
├── schemas/
│   ├── building_candidate.json
│   ├── unit_listing.json
│   └── building_research.json
├── research/
│   ├── building_packets/
│   ├── leases/
│   ├── raw_notes/
│   └── screenshots/
├── scripts/
│   ├── validate_data.py
│   ├── compute_scores.py
│   ├── generate_markdown_reports.py
│   ├── upsert_json_into_csv.py
│   └── sync_to_notion.py
├── tests/
│   └── test_validate_data.py
└── .github/workflows/
    ├── validate.yml
    ├── rebuild-docs.yml
    └── sync-notion.yml
```

## Canonical workflow

### Stage 1: Breadth scan
Use `prompts/01_breadth_scan_json.md` with a browsing-capable model.
Output: JSON rows for `data/buildings.csv`.

### Stage 2: Unit extraction
Use `prompts/02_unit_extraction_json.md` on specific listings.
Output: JSON rows for `data/units.csv`.

### Stage 3: Building research
Use `prompts/03_building_research_json.md`.
Output:
- one building update object
- zero or more evidence rows
- a building-packet markdown draft

### Stage 4: Tours
Capture observations in `data/tours.csv` immediately after each visit.
Use the question set in `docs/05_tour_questions.md`.

### Stage 5: Final review
Use `prompts/05_final_review.md` after the CSVs and packets are current.

## Data model notes

- `buildings.csv` holds durable building-level facts and building-level scores.
- `units.csv` holds pricing, concessions, and unit-specific attributes.
- `evidence.csv` stores provenance for claims that are easy to lose over time.
- `decisions.csv` is the source for `docs/07_decision_log.md`.

## Scoring philosophy

The repo still uses 1-5 anchors for human readability, but overall ranking is **not** a raw average of ordinal scores. See `docs/09_scoring_rubric.md` and `config/decision_config.json`.

## Fair-housing note

This repo is for operational decision support, not demographic filtering. Use objective criteria: quiet-hours enforcement, short-term-rental presence, turnover, security, maintenance quality, and approval speed. Do **not** use age, family status, or any other protected-class proxy as a preference signal.

## Local commands

```bash
python scripts/validate_data.py
python scripts/compute_scores.py
python scripts/generate_markdown_reports.py
python -m unittest discover -s tests
python scripts/sync_to_notion.py --dry-run
```

## Migration note

This strengthened repo seeds `buildings.csv` and `decisions.csv` from the existing breadth-scan markdown so the project does not restart from zero. The seeded rows should still be refreshed against current web evidence before any lease decision.
