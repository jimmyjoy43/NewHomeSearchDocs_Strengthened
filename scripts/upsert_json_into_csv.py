#!/usr/bin/env python3
"""Upsert flat JSON rows into a CSV by key column.

Usage:
    python scripts/upsert_json_into_csv.py data/buildings.csv payload.json building_id
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Dict, List


def load_payload(path: Path) -> List[Dict[str, object]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        if isinstance(raw.get("rows"), list):
            return raw["rows"]
        if isinstance(raw.get("data"), list):
            return raw["data"]
    raise ValueError("JSON payload must be an array or an object containing a 'rows' or 'data' array.")


def load_csv(path: Path) -> tuple[list[str], list[Dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return (reader.fieldnames or [], list(reader))


def main(argv: list[str]) -> int:
    if len(argv) < 4:
        print("Usage: python scripts/upsert_json_into_csv.py <csv_path> <json_path> <key_column> [--overwrite]")
        return 1

    csv_path = Path(argv[1])
    json_path = Path(argv[2])
    key_col = argv[3]
    overwrite = "--overwrite" in argv[4:]

    header, rows = load_csv(csv_path)
    payload = load_payload(json_path)

    if key_col not in header:
        print(f"FAIL: key column '{key_col}' does not exist in {csv_path}")
        return 1

    index = {row.get(key_col, ""): row for row in rows if row.get(key_col, "")}

    created = 0
    updated = 0
    for item in payload:
        flat = {str(k): "" if v is None else str(v) for k, v in item.items()}
        extra = [k for k in flat if k not in header]
        if extra:
            print(f"FAIL: payload row contains columns not present in CSV: {extra}")
            return 1
        key = flat.get(key_col, "").strip()
        if not key:
            print(f"FAIL: payload row is missing key column '{key_col}'")
            return 1

        if key in index:
            target = index[key]
            for col in header:
                incoming = flat.get(col, "")
                if incoming == "" and not overwrite:
                    continue
                if incoming != "":
                    target[col] = incoming
                elif overwrite:
                    target[col] = ""
            updated += 1
        else:
            new_row = {col: flat.get(col, "") for col in header}
            rows.append(new_row)
            index[key] = new_row
            created += 1

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Upsert complete. Created: {created}. Updated: {updated}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
