# New Home Search Docs

This repo is a structured apartment-search workspace built around canonical local data, evidence capture, and repeatable review steps.

This root README supersedes the older variants now archived under [`_archive/`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/_archive). The default workflow below mostly follows the former ALT process: use external ChatGPT with web search for the web-heavy research stages, then ingest, validate, score, and review locally in this repo.

## Search Context

### Objective
Find a new apartment in or near Hollywood / West Hollywood that preserves the convenience and amenity level of Camden Hollywood while materially improving on quiet, operational competence, and day-to-day livability.

### Priorities
1. Quiet enough for sleep, work, and normal daily life.
2. Reliable, human, non-chaotic leasing and maintenance operations.
3. Stable building operations with low surprise risk.
4. Strong primary parking that works as a daily default, not just as a fallback.
5. Concierge, 24x7 security, or another real around-the-clock on-site human presence.
6. Strong amenity package.
7. Cat-friendly terms.
8. In-unit laundry.
9. Secure package handling.
10. Clean, well-maintained common spaces.

### Geography
- Primary: Hollywood and West Hollywood
- Secondary: adjacent pockets only if they preserve the same convenience and do not create a commute or noise downgrade

### Budget
- Conservative ceiling: $3,996 all-in
- Strong target band: $3,800 to $4,700 all-in
- Stretch band: up to $5,328 before unusually high recurring fees

### Operating Principles
- Prefer objective signals over branding.
- Treat every unknown as a question to resolve, not as a hidden "no".
- Keep building-level facts separate from unit-level facts.
- Record decisions as they happen.
- Move fast on timeline-sensitive items, but not by skipping validation.

## Canonical Data Model

The canonical sources of truth are the CSV files in [`data/`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data):

- [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv): one row per building
- [`data/units.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/units.csv): one row per unit
- [`data/evidence.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/evidence.csv): durable claim provenance
- [`data/tours.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/tours.csv): in-person observations
- [`data/contacts.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/contacts.csv): outreach log
- [`data/decisions.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/decisions.csv): decision log source

Supporting files:

- [`config/decision_config.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/config/decision_config.json): weights, utility map, penalties, statuses
- [`schemas/`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/schemas): JSON payload shapes for model output
- [`research/*.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/research): per-building research payloads and packet markdown
- [`docs/`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs): generated and reference docs
- [`prompts/`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts): in-repo prompts
- [`prompts_external/`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts_external): external ChatGPT prompts with web search

## Fresh Restart

If you want to rerun this search from the beginning, treat the current repo as a mixed state: some files are durable reference docs, and some are stale workflow outputs that should be cleared or archived before the new run.

### Keep and refresh before rerunning Stage 1

These are the Stage 1 reference files that should reflect the current search, not the old one:

- [`README.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/README.md): root workflow summary and current assumptions
- [`docs/01_project_brief.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/01_project_brief.md): objective, geography, and budget
- [`docs/03_essential_amenities.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/03_essential_amenities.md): current must-haves
- [`docs/04_nice_to_have_amenities.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/04_nice_to_have_amenities.md): current nice-to-haves
- [`docs/06_management_red_flags.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/06_management_red_flags.md): any updated operational dealbreakers
- [`docs/08_move_timeline.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/08_move_timeline.md): current move window and decision gates
- [`docs/09_scoring_rubric.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/09_scoring_rubric.md): only if your scoring priorities changed
- [`config/decision_config.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/config/decision_config.json): update this if the target move date, search anchor date, weights, or rule thresholds changed

Practical mapping:

- Updated timeline: `docs/08_move_timeline.md` and usually `config/decision_config.json`
- Updated rent targets or budget bands: `docs/01_project_brief.md` and this `README.md`
- Updated essentials or amenity preferences: `docs/03_essential_amenities.md` and `docs/04_nice_to_have_amenities.md`
- Updated operational concerns: `docs/06_management_red_flags.md`

### Clear or archive before a fresh run

These files are outputs or staged payloads from prior runs and should not be treated as current inputs:

- [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv): clear to header-only if starting over from zero
- [`data/units.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/units.csv): clear to header-only
- [`data/evidence.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/evidence.csv): clear to header-only
- [`data/tours.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/tours.csv): clear to header-only
- [`data/contacts.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/contacts.csv): clear to header-only
- [`data/decisions.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/decisions.csv): clear to header-only
- [`payload_buildings.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/payload_buildings.json): replace with the new Stage 1 payload
- [`payload_evidence.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/payload_evidence.json): remove until Stage 3 creates a new one
- [`all_units.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/all_units.json): remove until Stage 2 creates a new one
- [`research/*.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/research): archive or delete old building packets if they are no longer part of the new run
- [`artifacts/all_building_packets.jsonl`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/artifacts/all_building_packets.jsonl): generated output, not canonical input
- [`artifacts/building_packets/`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/artifacts/building_packets): archive output only
- [`docs/02_neighborhood_breadth_scan.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/02_neighborhood_breadth_scan.md): generated
- [`docs/07_decision_log.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/07_decision_log.md): generated
- [`docs/10_unit_comparison.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/10_unit_comparison.md): generated

## Recommended Workflow

Use this operating pattern by default:

1. Keep canonical state in local CSVs.
2. Use external ChatGPT with web search for Stage 2 unit extraction and Stage 3 building research.
3. Download reviewed JSON outputs into the repo.
4. Upsert into the canonical CSVs.
5. Run validation, scoring, and report generation locally.
6. Make tour and final decisions from local data, not from an ad hoc chat transcript.

## Repo Layout

```text
NewHomeSearchDocs_Strengthened/
├── README.md
├── _archive/
│   ├── README.md
│   ├── README_ALT.md
│   └── README_Strengthened repo README.md
├── config/
├── data/
├── docs/
├── prompts/
├── prompts_external/
├── research/
├── schemas/
├── scripts/
├── tests/
├── artifacts/
└── .github/workflows/
```

## Stage 1: Breadth Scan

Goal: identify likely-fit buildings and seed [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv) from a fresh external research pass.

Default mode: external ChatGPT with web search ON.

Primary prompt:
- [`prompts_external/01_breadth_scan_chatgpt.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts_external/01_breadth_scan_chatgpt.md)

If you are running Stage 1 from zero, do not anchor the model on old `buildings.csv` or `decisions.csv` contents. Use the refreshed brief, amenity, timeline, and scoring docs as the source of truth.

Output shape:
- JSON payload matching [`schemas/building_candidate.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/schemas/building_candidate.json)

Workflow:

1. Run the external prompt in ChatGPT.
2. Copy the returned JSON into [`payload_buildings.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/payload_buildings.json).
3. Upsert into [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv).
4. Validate and regenerate reports.

### Safe Stage 1 Run

Use this sequence for a clean restart:

1. Update the current search assumptions in:
   - [`README.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/README.md)
   - [`docs/01_project_brief.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/01_project_brief.md)
   - [`docs/03_essential_amenities.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/03_essential_amenities.md)
   - [`docs/04_nice_to_have_amenities.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/04_nice_to_have_amenities.md)
   - [`docs/06_management_red_flags.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/06_management_red_flags.md)
   - [`docs/08_move_timeline.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/08_move_timeline.md)
   - [`config/decision_config.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/config/decision_config.json) if dates, weights, or thresholds changed
2. Open a new external ChatGPT chat with web search enabled.
3. Use [`prompts_external/01_breadth_scan_chatgpt.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts_external/01_breadth_scan_chatgpt.md).
4. Attach or paste only the current reference files:
   - `README.md`
   - `docs/01_project_brief.md`
   - `docs/03_essential_amenities.md`
   - `docs/04_nice_to_have_amenities.md`
   - `docs/06_management_red_flags.md`
   - `docs/08_move_timeline.md`
   - `docs/09_scoring_rubric.md`
5. Do not attach old `data/buildings.csv` or `data/decisions.csv` for a fresh run.
6. Make sure ChatGPT returns one flat JSON object with a top-level `rows` array and string values only.
7. Paste that JSON into [`payload_buildings.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/payload_buildings.json).
8. Run the local ingest and checks:

```powershell
python scripts\upsert_json_into_csv.py data\buildings.csv payload_buildings.json building_id
python scripts\validate_data.py
python scripts\generate_markdown_reports.py
```

9. Review the resulting [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv) and [`docs/02_neighborhood_breadth_scan.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/02_neighborhood_breadth_scan.md) before moving to Stage 2.

Ingest:

```powershell
python scripts\upsert_json_into_csv.py data\buildings.csv payload_buildings.json building_id
python scripts\validate_data.py
python scripts\generate_markdown_reports.py
```

## Stage 2: Unit Extraction

Default mode: external ChatGPT with web search ON.

Primary prompt:
- [`prompts_external/02_unit_extraction_chatgpt.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts_external/02_unit_extraction_chatgpt.md)

Do not use [`prompts/02_unit_extraction_json.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts/02_unit_extraction_json.md) for the external Stage 2 run. That file is the older single-building template with `[FILL IN]` placeholders.

Attach:
- [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv)
- [`docs/01_project_brief.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/01_project_brief.md)
- [`docs/08_move_timeline.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/08_move_timeline.md)

Expected output:
- one or more JSON files
- usually a combined [`all_units.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/all_units.json)-style payload

Stage 2 does not require the building set to come from one single Stage 1 batch. You can insert additional building rows into the canonical [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv) between stages and then run unit extraction against that current superset.

The current Stage 2 unit-type filter is strict: studios and 1-bedroom units only. Exclude 2-bedroom and larger units unless you intentionally revise the prompt for a different search pass.

By default, the external Stage 2 prompt processes rows whose `status` is not `rejected` and skips rows whose `status` is `leased`. If you want unit extraction to include previously rejected buildings too, say so explicitly in the external chat.

If you add buildings from older runs between Stage 1 and Stage 2, treat any old scores, risks, and open questions as legacy context unless you intentionally decide to carry them forward. Stage 2 only depends on the current building list plus each row's `building_id`, `building_name`, `source_url`, `status`, and `notes`.

Ingest:

```powershell
python scripts\upsert_json_into_csv.py data\units.csv all_units.json unit_id
python scripts\validate_data.py
python scripts\generate_markdown_reports.py
```

Important:
- Do not put building-level facts in `units.csv`.
- If a listing only exposes total monthly price and not base rent, leave `base_rent` blank and explain it in `notes`.
- The repo currently validates and reports `net_effective_rent` and `true_monthly_cost` if present, but it does not yet include a dedicated script that derives those fields automatically.

## Stage 3: Building Research

Default mode: external ChatGPT with web search ON.

Primary prompt:
- [`prompts_external/03_building_research_chatgpt.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts_external/03_building_research_chatgpt.md)

Do not use [`prompts/03_building_research_json.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts/03_building_research_json.md) for the external bulk Stage 3 run. That file is the focused single-building template.

Attach:
- [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv)
- [`data/units.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/units.csv)
- [`docs/01_project_brief.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/01_project_brief.md)
- [`docs/06_management_red_flags.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/06_management_red_flags.md)
- [`docs/08_move_timeline.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/08_move_timeline.md)
- [`docs/09_scoring_rubric.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/09_scoring_rubric.md)
- [`docs/11_legal_and_fair_housing.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/11_legal_and_fair_housing.md)
- [`docs/12_research_methodology.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/12_research_methodology.md)

Expected output per building:
- `building_row`
- `evidence_rows`
- `packet_markdown`

Default Stage 3 target set:
- start from `buildings.csv` rows where `status` is not `rejected`
- skip `leased`
- keep only building IDs that appear in `units.csv` with at least one real unit row
- skip buildings whose only Stage 2 row is `unit_number = NONE`

Store reviewed building payloads under [`research/`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/research). The canonical packet location for this workflow is `research/{building_id}.json`.

### Safe Stage 3 Run

Use this sequence after Stage 2 has already been ingested into [`data/units.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/units.csv):

1. Review [`data/units.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/units.csv) or [`docs/10_unit_comparison.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/10_unit_comparison.md) to confirm the buildings with real qualifying units.
2. Optionally update `status` in [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv) before research if you already know a building should be skipped.
3. Open a new external ChatGPT chat with web search enabled.
4. Paste [`prompts_external/03_building_research_chatgpt.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts_external/03_building_research_chatgpt.md) into the message body.
5. Attach the current Stage 3 reference files listed above.
6. Let ChatGPT process the filtered buildings one at a time and download each `{building_id}.json` file into [`research/`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/research).
7. Also save the optional combined `all_buildings_research.json` file in [`research/`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/research) if ChatGPT produces it.
8. Compile the downloaded research packets into the canonical payload files:

```powershell
python scripts\build_stage3_payloads.py
python scripts\upsert_json_into_csv.py data\buildings.csv payload_buildings.json building_id
python scripts\upsert_json_into_csv.py data\evidence.csv payload_evidence.json evidence_id
python scripts\compute_scores.py
python scripts\validate_data.py
python scripts\generate_markdown_reports.py
```

9. Review the updated [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv), [`data/evidence.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/evidence.csv), and [`docs/02_neighborhood_breadth_scan.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/02_neighborhood_breadth_scan.md) before making tour decisions.

Notes:
- [`payload_buildings.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/payload_buildings.json) should contain only `building_row` objects.
- [`payload_evidence.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/payload_evidence.json) should contain only flattened `evidence_rows`.
- [`scripts/build_stage3_payloads.py`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/scripts/build_stage3_payloads.py) generates those two payload files directly from `research/*.json` and sets `packet_path` automatically when it is blank.
- `review_scan_done` and `deep_research_done` belong in `buildings.csv`, not in `evidence.csv`.

## Stage 3.5: Decision Pass

After Stage 3 is ingested:

1. Review the ranked output in [`docs/02_neighborhood_breadth_scan.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/02_neighborhood_breadth_scan.md).
2. Add explicit advance / reject / hold decisions to [`data/decisions.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/decisions.csv).
3. Regenerate the markdown decision log.

```powershell
python scripts\generate_markdown_reports.py
python scripts\validate_data.py
```

## Stage 4: Tours

Stage 4 is a local, human step. Use it to convert the best Stage 3 candidates into direct observations, concrete decisions, and updated unit/building state.

Before scheduling a tour, confirm:

1. The building is still a plausible candidate in `buildings.csv`.
2. There are qualifying unit rows in `units.csv`.
3. The building's open questions are written down.
4. The exact unit you care about still exists in `units.csv`, or you are explicitly touring a comparable.

Use:
- [`docs/05_tour_questions.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/05_tour_questions.md)

Capture:
- tour observations in [`data/tours.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/tours.csv)
- unit tour state in [`data/units.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/units.csv)
- any real decisions in [`data/decisions.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/decisions.csv)

### Safe Stage 4 Run

1. Pick the building and exact unit you want to tour from [`data/units.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/units.csv).
2. Before the tour, set that unit's `tour_status` to `scheduled` in [`data/units.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/units.csv).
3. Bring [`docs/05_tour_questions.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/05_tour_questions.md) and prioritize the unresolved `open_questions` already stored on the building row.
4. Immediately after the tour, add a row to [`data/tours.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/tours.csv) with:
   - `tour_id`
   - `building_id`
   - `unit_id` if the toured unit is known
   - `tour_date`
   - `tour_type`
   - `leasing_agent`
   - `approval_speed_business_days` if learned
   - `first_impression_score`
   - `noise_observation`
   - `unit_condition`
   - `common_area_condition`
   - `staff_responsiveness`
   - `questions_answered`
   - `red_flags`
   - `follow_up_needed`
   - `notes`
   - `last_updated`
5. Update the corresponding unit row in [`data/units.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/units.csv) to `tour_status = completed`, `skipped`, or `rejected`.
6. Update the building row in [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv) if the tour changed the building-level view:
   - `status`
   - `approval_speed_business_days`
   - `open_questions`
   - `notes`
   - any score or risk field that now has materially better evidence
7. Add a row to [`data/decisions.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/decisions.csv) if the tour produced a real decision such as `finalist`, `backup`, `hold`, or `reject`.

After each tour:

```powershell
python scripts\validate_data.py
python scripts\generate_markdown_reports.py
```

Only rerun `compute_scores.py` if you changed building-level scoring inputs in [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv):

```powershell
python scripts\compute_scores.py
python scripts\validate_data.py
python scripts\generate_markdown_reports.py
```

## Stage 5: Final Review

Run this locally after buildings, units, evidence, tours, and decisions are current.

Primary prompt:
- [`prompts/05_final_review.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts/05_final_review.md)

Use these local inputs:
- [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv)
- [`data/units.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/units.csv)
- [`data/evidence.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/evidence.csv)
- [`data/tours.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/tours.csv)
- [`data/decisions.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/decisions.csv)
- [`research/*.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/research)
- [`docs/02_neighborhood_breadth_scan.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/02_neighborhood_breadth_scan.md)
- [`docs/10_unit_comparison.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/10_unit_comparison.md)

The final review should produce:
- a head-to-head comparison
- confidence-aware score commentary
- a financial comparison
- a red-flag summary tied to evidence
- one clear recommendation
- the biggest remaining risk
- the next 48 hours of actions

### Safe Stage 5 Run

1. Make sure Stage 3 and Stage 4 updates are already reflected in:
   - [`data/buildings.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/buildings.csv)
   - [`data/units.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/units.csv)
   - [`data/evidence.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/evidence.csv)
   - [`data/tours.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/tours.csv)
   - [`data/decisions.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/decisions.csv)
2. Run:

```powershell
python scripts\compute_scores.py
python scripts\validate_data.py
python scripts\generate_markdown_reports.py
```

3. Open [`prompts/05_final_review.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/prompts/05_final_review.md) in your local analysis chat.
4. Let the model derive finalists from current decisions and statuses unless you want to specify a short list manually.
5. Ask for one recommendation, the biggest remaining risk, and the next 48 hours of actions.
6. If the final review changes your actual decision state, write that back into [`data/decisions.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/decisions.csv) and regenerate docs again.

## Scoring

Overall ranking is not a raw average of 1 to 5 scores.

- Category weights, utility mapping, penalties, and hard-stop rules live in [`config/decision_config.json`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/config/decision_config.json).
- Human-readable scoring guidance lives in [`docs/09_scoring_rubric.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/09_scoring_rubric.md).
- `compute_scores.py` updates `overall_fit_score` and `hard_stop` in `buildings.csv`.

## Evidence and Guardrails

- Durable claims belong in [`data/evidence.csv`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/data/evidence.csv) with URL and retrieval date.
- Research hierarchy and evidence classes are defined in [`docs/12_research_methodology.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/12_research_methodology.md).
- Fair-housing constraints are defined in [`docs/11_legal_and_fair_housing.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/docs/11_legal_and_fair_housing.md).
- Do not use demographic or protected-class proxies. Use operational facts only.

## Local Commands

```powershell
python scripts\validate_data.py
python scripts\compute_scores.py
python scripts\generate_markdown_reports.py
python -m unittest discover -s tests
python scripts\sync_to_notion.py --dry-run
```

## Automation

GitHub Actions currently cover:

- validation: [`validate.yml`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/.github/workflows/validate.yml)
- report rebuild on main: [`rebuild-docs.yml`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/.github/workflows/rebuild-docs.yml)
- manual Notion sync: [`sync-notion.yml`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/.github/workflows/sync-notion.yml)

Notion sync is optional and intentionally conservative:

- dry-run is the default
- `--apply` is required for writes
- workflow dispatch is required in CI

## Archived Readmes

The previous README variants were moved intact to:

- [`_archive/README.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/_archive/README.md)
- [`_archive/README_ALT.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/_archive/README_ALT.md)
- [`_archive/README_Strengthened repo README.md`](c:/Users/joyj7/Source/NewHomeSearchDocs_Strengthened/_archive/README_Strengthened%20repo%20README.md)
