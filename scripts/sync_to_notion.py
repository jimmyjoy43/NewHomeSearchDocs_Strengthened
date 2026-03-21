#!/usr/bin/env python3
"""Optional Notion sync for the strengthened housing repo.

Dry-run is the default. Use --apply to write to Notion.
This script syncs unit rows when available; otherwise it can sync building placeholders.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
BUILDINGS_CSV = REPO_ROOT / "data" / "buildings.csv"
UNITS_CSV = REPO_ROOT / "data" / "units.csv"


def load_dotenv_if_available() -> None:
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv()
    except Exception:
        pass


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_rows() -> List[Dict[str, str]]:
    buildings = {row["building_id"]: row for row in read_csv(BUILDINGS_CSV)}
    units = read_csv(UNITS_CSV)

    if units:
        flat: List[Dict[str, str]] = []
        for unit in units:
            building = buildings.get(unit.get("building_id", ""), {})
            flat.append(
                {
                    "record_id": unit.get("unit_id", ""),
                    "Name": f"{building.get('building_name', unit.get('building_id', ''))} | Unit {unit.get('unit_number', '')}".strip(),
                    "building_id": unit.get("building_id", ""),
                    "unit_id": unit.get("unit_id", ""),
                    "building_name": building.get("building_name", ""),
                    "address": building.get("address", ""),
                    "status": building.get("status", ""),
                    "hard_stop": building.get("hard_stop", ""),
                    "base_rent": unit.get("base_rent", ""),
                    "net_effective_rent": unit.get("net_effective_rent", ""),
                    "true_monthly_cost": unit.get("true_monthly_cost", ""),
                    "available_date": unit.get("available_date", ""),
                }
            )
        return flat

    return [
        {
            "record_id": row.get("building_id", ""),
            "Name": row.get("building_name", ""),
            "building_id": row.get("building_id", ""),
            "unit_id": "",
            "building_name": row.get("building_name", ""),
            "address": row.get("address", ""),
            "status": row.get("status", ""),
            "hard_stop": row.get("hard_stop", ""),
            "base_rent": "",
            "net_effective_rent": "",
            "true_monthly_cost": "",
            "available_date": "",
        }
        for row in buildings.values()
    ]


def parse_number(value: str):
    if not value:
        return None
    try:
        f = float(value)
        return int(f) if f.is_integer() else f
    except ValueError:
        return None


def parse_checkbox(value: str) -> bool:
    return str(value).strip().lower() in {"yes", "true", "1", "x"}


def build_properties(row: Dict[str, str]) -> Dict:
    props: Dict[str, Dict] = {
        "Name": {"title": [{"text": {"content": row["Name"][:2000]}}]},
        "record_id": {"rich_text": [{"text": {"content": row["record_id"][:2000]}}]},
        "building_id": {"rich_text": [{"text": {"content": row.get("building_id", "")[:2000]}}]},
        "unit_id": {"rich_text": [{"text": {"content": row.get("unit_id", "")[:2000]}}]},
        "building_name": {"rich_text": [{"text": {"content": row.get("building_name", "")[:2000]}}]},
        "address": {"rich_text": [{"text": {"content": row.get("address", "")[:2000]}}]},
        "status": {"rich_text": [{"text": {"content": row.get("status", "")[:2000]}}]},
        "hard_stop": {"checkbox": parse_checkbox(row.get("hard_stop", ""))},
    }
    for number_field in ("base_rent", "net_effective_rent", "true_monthly_cost"):
        num = parse_number(row.get(number_field, ""))
        if num is not None:
            props[number_field] = {"number": num}
    if row.get("available_date"):
        props["available_date"] = {"date": {"start": row["available_date"]}}
    return props


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync housing options to Notion")
    parser.add_argument("--apply", action="store_true", help="Actually write to Notion")
    args = parser.parse_args()

    load_dotenv_if_available()
    rows = build_rows()
    apply = args.apply

    print(f"Prepared {len(rows)} row(s) for Notion sync.")
    if not apply:
        print("DRY RUN: no changes will be sent to Notion.")
        for row in rows[:10]:
            print(f"  - {row['record_id']}: {row['Name']}")
        return 0

    token = os.getenv("NOTION_TOKEN")
    database_id = os.getenv("NOTION_DATABASE_ID")
    if not token or not database_id:
        print("FAIL: NOTION_TOKEN and NOTION_DATABASE_ID are required when using --apply.")
        return 1

    try:
        from notion_client import Client  # type: ignore
        from notion_client.errors import APIResponseError  # type: ignore
    except Exception:
        print("FAIL: notion-client is not installed. Run: pip install -r requirements.txt")
        return 1

    client = Client(auth=token)

    existing: Dict[str, str] = {}
    cursor = None
    while True:
        kwargs = {"database_id": database_id, "page_size": 100}
        if cursor:
            kwargs["start_cursor"] = cursor
        response = client.databases.query(**kwargs)
        for page in response.get("results", []):
            props = page.get("properties", {})
            rt = props.get("record_id", {}).get("rich_text", [])
            record_id = "".join(item.get("plain_text", "") for item in rt)
            if record_id:
                existing[record_id] = page["id"]
        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")

    created = 0
    updated = 0

    for row in rows:
        props = build_properties(row)
        rid = row["record_id"]
        try:
            if rid in existing:
                client.pages.update(page_id=existing[rid], properties=props)
                updated += 1
            else:
                client.pages.create(parent={"database_id": database_id}, properties=props)
                created += 1
        except APIResponseError as exc:  # pragma: no cover - external API path
            print(f"ERROR: {rid}: {exc}")
            return 1

    print(f"Sync complete. Created: {created}. Updated: {updated}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
