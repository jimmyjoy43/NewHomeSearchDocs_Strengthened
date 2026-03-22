#!/usr/bin/env python3
"""
Fix buildings.csv:
  1. Remove repeated header rows (keep only the first).
  2. Normalise near-duplicate IDs to a single canonical ID.
  3. Merge any rows that share a building_id into one row.

Run from the repo root:
    python scripts/fix_buildings_duplicates.py
"""
import csv
import io
from collections import OrderedDict
from copy import deepcopy
from pathlib import Path

BUILDINGS_CSV = Path(__file__).resolve().parents[1] / "data" / "buildings.csv"

# Near-duplicate ID pairs → (old_id, canonical_id)
ID_REMAP = {
    "domain-weho-7141-santa-monica-blvd":
        "domain-west-hollywood-7141-santa-monica-blvd",
    "element-weho-1425-n-crescent-height-blvd":
        "element-weho-1425-n-crescent-heights-blvd",
}

# Status priority: lower number = more decisive / informative
STATUS_PRIORITY = {
    "rejected": 0,
    "tour_candidate": 1,
    "candidate": 2,
    "screened": 3,
    "research_complete": 4,
    "toured": 5,
    "finalist": 6,
    "leased": 7,
    "backup": 8,
    "": 99,
    "unknown": 99,
}


def prefer(v1: str, v2: str) -> str:
    """Return whichever value is more informative; v2 (newer) wins when both filled."""
    if not v1 or v1 == "unknown":
        return v2 if v2 else v1
    if not v2 or v2 == "unknown":
        return v1
    return v2  # both non-empty → prefer newer row


def merge_two(older: dict, newer: dict) -> dict:
    merged = deepcopy(older)
    for key in older:
        if key == "building_id":
            continue
        v1, v2 = older[key].strip(), newer[key].strip()

        if key == "status":
            p1 = STATUS_PRIORITY.get(v1, 99)
            p2 = STATUS_PRIORITY.get(v2, 99)
            merged[key] = v1 if p1 <= p2 else v2

        elif key == "hard_stop":
            if "yes" in (v1, v2):
                merged[key] = "yes"
            elif "no" in (v1, v2):
                merged[key] = "no"
            else:
                merged[key] = prefer(v1, v2)

        elif key == "deep_research_done":
            merged[key] = "yes" if "yes" in (v1, v2) else prefer(v1, v2)

        elif key in ("notes", "open_questions"):
            if v1 and v2 and v1 != v2:
                merged[key] = v1 + " | " + v2
            else:
                merged[key] = v1 or v2

        elif key == "last_updated":
            merged[key] = max(v1, v2)  # YYYY-MM-DD sorts lexicographically

        elif key == "address":
            # Prefer the more complete address (with city/state/zip)
            merged[key] = v2 if len(v2) > len(v1) else v1

        else:
            merged[key] = prefer(v1, v2)
    return merged


def main() -> None:
    raw = BUILDINGS_CSV.read_text(encoding="utf-8")
    lines = raw.splitlines()

    # Step 1: strip repeated header rows (keep first occurrence only)
    header_line = lines[0].strip()
    clean_lines = [lines[0]] + [
        ln for ln in lines[1:]
        if ln.strip() and ln.strip() != header_line
    ]
    print(f"Lines after stripping repeated headers: {len(clean_lines) - 1} data rows")

    rows = list(csv.DictReader(io.StringIO("\n".join(clean_lines))))
    fieldnames = list(rows[0].keys())

    # Step 2: normalise near-duplicate IDs
    remapped = 0
    for row in rows:
        canonical = ID_REMAP.get(row["building_id"])
        if canonical:
            print(f"  Remapping ID: {row['building_id']} → {canonical}")
            row["building_id"] = canonical
            remapped += 1
    print(f"IDs remapped: {remapped}")

    # Step 3: group by building_id, preserving first-seen order
    groups: OrderedDict = OrderedDict()
    for row in rows:
        bid = row["building_id"]
        groups.setdefault(bid, []).append(row)

    merged_rows = []
    for bid, group in groups.items():
        if len(group) == 1:
            merged_rows.append(group[0])
        else:
            # Sort oldest-first by last_updated so newer values win prefer()
            group.sort(key=lambda r: r.get("last_updated", ""))
            result = group[0]
            for later in group[1:]:
                result = merge_two(result, later)
            merged_rows.append(result)
            print(f"  Merged {len(group)} rows → {bid}")

    # Write back
    with BUILDINGS_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(merged_rows)

    print(f"\nDone. {len(merged_rows)} unique buildings written to {BUILDINGS_CSV}.")


if __name__ == "__main__":
    main()
