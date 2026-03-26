# Alternate Workflow: External ChatGPT for Stages 2 & 3

This document describes the **alternate pipeline** where Stages 2 (Unit Extraction)
and 3 (Building Research) are run in ChatGPT with web search enabled, and the
results are ingested back into the repo for Stages 4 and 5.

The original `prompts/` directory contains the in-repo prompts designed for models
that already have the files in context. The `prompts_external/` directory contains
self-contained prompts designed for a standalone ChatGPT session with live web search.

## Why this alternate workflow exists

Stages 2 and 3 depend heavily on **live web data** — current unit listings, review
ratings, Reddit threads, and news coverage. A thinking model with web search
(o3 / o4-mini-high) can visit each building's leasing site and review platforms
directly, rather than requiring you to copy-paste or upload HTML.

Stages 1, 4, and 5 do not change because:
- Stage 1 (Breadth Scan) already ran and produced `buildings.csv`.
- Stage 4 (Tours) is in-person — no model can substitute for that.
- Stage 5 (Final Review) works on local repo data and does not need web search.

---

## Directory layout

```text
prompts_external/
├── 02_unit_extraction_chatgpt.md    ← Stage 2 external prompt
└── 03_building_research_chatgpt.md  ← Stage 3 external prompt
```

---

## Stage 1: Breadth Scan (unchanged)

Already complete. `data/buildings.csv` has 22 rows (16 active, 6 rejected).

---

## Stage 2: Unit Extraction (external)

### Where to run
ChatGPT app — o3 or o4-mini, heavy thinking effort, web search ON.

### Input
Attach `data/buildings.csv` to the ChatGPT conversation.

### Prompt
Copy the full prompt from `prompts_external/02_unit_extraction_chatgpt.md`.

### What you get back
ChatGPT processes buildings one at a time and provides:
- A download link for each `units_{building_id}.json` as it finishes
- A combined `all_units.json` at the end

### Ingest into the repo

```bash
# 1. Download all_units.json from ChatGPT into the repo root

# 2. Upsert into units.csv
python scripts/upsert_json_into_csv.py data/units.csv all_units.json unit_id

# 3. Validate
python scripts/validate_data.py

# 4. Regenerate the unit comparison doc
python scripts/generate_markdown_reports.py
```

### Verify
```bash
# Check row count
python -c "import csv; r=list(csv.DictReader(open('data/units.csv'))); print(f'{len(r)} units ingested')"

# Spot-check a building
python -c "
import csv
units = [r for r in csv.DictReader(open('data/units.csv'))
         if r['building_id'] == 'columbia-square-living-1550-n-el-centro-ave']
for u in units:
    print(f\"  {u['unit_number']:>6}  {u['bedrooms']}BR  \${u['base_rent']}\")
"
```

### What this feeds into
- `data/units.csv` is now populated, which is required by Stage 5 (Final Review)
  for the financial comparison and true-monthly-cost calculation.
- `docs/10_unit_comparison.md` is regenerated with real unit data.

---

## Stage 3: Building Research (external)

### Where to run
ChatGPT app — o3 or o4-mini, heavy thinking effort, web search ON.

### Input
Attach `data/buildings.csv` to the ChatGPT conversation.

### Prompt
Copy the full prompt from `prompts_external/03_building_research_chatgpt.md`.

### What you get back
ChatGPT processes buildings one at a time and provides:
- A download link for each `{building_id}.json` as it finishes
- A combined `all_buildings_research.json` at the end

Each JSON file contains three keys:
- `building_row` — updated scores, risks, status → goes into `buildings.csv`
- `evidence_rows` — sourced claims → goes into `evidence.csv`
- `packet_markdown` — human-readable report → saved as `research/{building_id}.json`

### Ingest into the repo

```bash
# 1. Download all individual {building_id}.json files into research/
#    (or download all_buildings_research.json and split it)

# 2. Extract building_rows into a single payload file
python -c "
import json, glob, pathlib
rows = []
for f in sorted(glob.glob('research/*.json')):
    data = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
    if 'building_row' in data:
        rows.append(data['building_row'])
payload = {'rows': rows}
pathlib.Path('payload_buildings.json').write_text(
    json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'Extracted {len(rows)} building rows into payload_buildings.json')
"

# 3. Extract evidence_rows into a single payload file
python -c "
import json, glob, pathlib
rows = []
for f in sorted(glob.glob('research/*.json')):
    data = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
    for ev in data.get('evidence_rows', []):
        rows.append(ev)
payload = {'rows': rows}
pathlib.Path('payload_evidence.json').write_text(
    json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'Extracted {len(rows)} evidence rows into payload_evidence.json')
"

# 4. Upsert building updates
python scripts/upsert_json_into_csv.py data/buildings.csv payload_buildings.json building_id

# 5. Upsert evidence
python scripts/upsert_json_into_csv.py data/evidence.csv payload_evidence.json evidence_id

# 6. Recompute scores (uses config/decision_config.json weights + utility map)
python scripts/compute_scores.py

# 7. Validate everything
python scripts/validate_data.py

# 8. Regenerate all markdown reports
python scripts/generate_markdown_reports.py

# 9. Update the artifact index
python -c "
import csv, pathlib
buildings = list(csv.DictReader(open('data/buildings.csv', encoding='utf-8')))
lines = ['# Building packet index', '']
for b in sorted(buildings, key=lambda r: r['building_name']):
    packet = pathlib.Path(f\"research/{b['building_id']}.json\")
    if packet.exists():
        lines.append(f\"- {b['building_id']}: {b['status']}\")
pathlib.Path('artifacts/INDEX.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('Updated artifacts/INDEX.md')
"
```

### Verify
```bash
# Check that scores were computed
python -c "
import csv
rows = [r for r in csv.DictReader(open('data/buildings.csv'))
        if r['status'] != 'rejected' and r['overall_fit_score']]
print(f'{len(rows)} buildings now have an overall_fit_score')
for r in sorted(rows, key=lambda x: -float(x['overall_fit_score'])):
    print(f\"  {r['building_name']:40s}  {r['overall_fit_score']:>5s}  {r['status']}\")
"

# Check evidence count
python -c "
import csv
rows = list(csv.DictReader(open('data/evidence.csv')))
print(f'{len(rows)} evidence rows ingested')
"

# Full validation
python scripts/validate_data.py
```

### What this feeds into
- `data/buildings.csv` now has scores, confidence, risks, and status for every
  active building — required by Stage 4 (choosing which buildings to tour) and
  Stage 5 (final head-to-head comparison).
- `data/evidence.csv` is populated — provides provenance for Stage 5's red-flag
  summary.
- `research/*.json` packets exist — Stage 5 reads these for the building-level
  detail.
- `docs/02_neighborhood_breadth_scan.md` and `docs/07_decision_log.md` are
  regenerated with live scores and statuses.

---

## Stage 3.5: Decision Pass (local, between Stage 3 and Stage 4)

After Stage 3 results are ingested, make advance/reject decisions:

```bash
# Review the ranked breadth scan
cat docs/02_neighborhood_breadth_scan.md

# For each building you want to advance or reject, add a row to decisions.csv:
python -c "
import csv, pathlib
# Example — edit these to match your actual decisions:
new_decisions = [
    # (decision_id, date, building_id, decision, reason, next_action)
]
if new_decisions:
    path = pathlib.Path('data/decisions.csv')
    with path.open('a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for d in new_decisions:
            writer.writerow([d[0], d[1], d[2], '', d[3], d[4], d[5], 'user', d[1]])
    print(f'Added {len(new_decisions)} decision(s)')
"

# Regenerate the decision log
python scripts/generate_markdown_reports.py
```

---

## Stage 4: Tours (unchanged — in-person)

### Prerequisites from Stages 2 + 3
Before touring, confirm:
1. The building's status in `buildings.csv` is `tour_candidate` (from Stage 3)
2. The building has qualifying units in `units.csv` (from Stage 2)
3. Open questions from Stage 3 are written down to ask on-site

### During the tour
Use the 31-question checklist in `docs/05_tour_questions.md`.

### After each tour
Record observations in `data/tours.csv`:

```bash
# Validate after adding tour rows
python scripts/validate_data.py
```

### What this feeds into
- `data/tours.csv` rows give Stage 5 the in-person signal on noise, staff
  quality, unit condition, and red flags.
- Tour observations may cause you to update scores in `buildings.csv` — if so,
  re-run `python scripts/compute_scores.py`.

---

## Stage 5: Final Review (local, in-repo)

### Prerequisites
All of these must be current before running Stage 5:

| File | Populated by |
|---|---|
| `data/buildings.csv` (with scores) | Stage 3 ingest + `compute_scores.py` |
| `data/units.csv` (with pricing) | Stage 2 ingest |
| `data/evidence.csv` (with provenance) | Stage 3 ingest |
| `data/tours.csv` (with observations) | Stage 4 |
| `data/decisions.csv` (with advance/reject) | Stage 3.5 |
| `research/*.json` (building packets) | Stage 3 download |

### Where to run
This runs **in the repo** (Copilot / Codex / paste into ChatGPT with all files).
No web search needed — all data is local.

### Prompt
Use `prompts/05_final_review.md` (unchanged). Fill in the `[Finalists]` section
with buildings that have status `tour_candidate` or `finalist` and have been
toured.

### What it produces
1. Head-to-head amenity and unknown comparison table
2. Score summary with confidence commentary
3. Financial comparison (true monthly cost + first-month cash outlay)
4. Red-flag summary citing evidence class (confirmed / corroborated / anecdotal)
5. One clear recommendation in the first sentence
6. Biggest remaining risk with that pick
7. Next 48 hours of actions

### Post-review commands
```bash
# After signing: update buildings.csv status to "leased" and add a decision row
python scripts/compute_scores.py
python scripts/generate_markdown_reports.py
python scripts/validate_data.py
```

---

## End-to-end command cheat sheet

```bash
# ── After Stage 2 (unit extraction from ChatGPT) ──
python scripts/upsert_json_into_csv.py data/units.csv all_units.json unit_id
python scripts/validate_data.py
python scripts/generate_markdown_reports.py

# ── After Stage 3 (building research from ChatGPT) ──
# (extract payloads — see Stage 3 section above for the full python -c commands)
python scripts/upsert_json_into_csv.py data/buildings.csv payload_buildings.json building_id
python scripts/upsert_json_into_csv.py data/evidence.csv payload_evidence.json evidence_id
python scripts/compute_scores.py
python scripts/validate_data.py
python scripts/generate_markdown_reports.py

# ── After Stage 4 (tours) ──
python scripts/validate_data.py
python scripts/compute_scores.py        # if you updated any scores
python scripts/generate_markdown_reports.py

# ── Stage 5 (final review) ──
# Run prompts/05_final_review.md with all repo files in context

# ── Optional: Notion sync ──
python scripts/sync_to_notion.py --dry-run
python scripts/sync_to_notion.py --apply  # only when ready
```

---

## File flow diagram

```
Stage 1 (done)         Stage 2 (ChatGPT)           Stage 3 (ChatGPT)
buildings.csv ──────► units.csv                     buildings.csv (updated)
                       │                             evidence.csv
                       │                             research/*.json
                       │                             │
                       ▼                             ▼
              ┌─── compute_scores.py ◄──────────────┘
              │    validate_data.py
              │    generate_markdown_reports.py
              │
              ▼
        Stage 3.5: Decision pass (decisions.csv)
              │
              ▼
        Stage 4: Tours (tours.csv) ← in-person
              │
              ▼
        Stage 5: Final Review ← all CSVs + packets in context
              │
              ▼
        Apply → Sign → Move
```
