#!/usr/bin/env python3
"""Regenerate markdown reports from canonical CSV files."""

from __future__ import annotations

import csv
from datetime import date
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
DOCS_DIR = REPO_ROOT / "docs"
AUTO_MARKER = "<!-- AUTO-GENERATED: do not edit below this line -->"

BUILDINGS_CSV = DATA_DIR / "buildings.csv"
UNITS_CSV = DATA_DIR / "units.csv"
DECISIONS_CSV = DATA_DIR / "decisions.csv"

BREADTH_MD = DOCS_DIR / "02_neighborhood_breadth_scan.md"
DECISION_MD = DOCS_DIR / "07_decision_log.md"
UNITS_MD = DOCS_DIR / "10_unit_comparison.md"

STATUS_ORDER = {
    "tour_candidate": 0,
    "finalist": 1,
    "backup": 2,
    "research_complete": 3,
    "screened": 4,
    "candidate": 5,
    "toured": 6,
    "rejected": 7,
    "leased": 8,
    "": 9,
}


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def money(value: str) -> str:
    if not value:
        return ""
    try:
        return f"${float(value):,.0f}" if float(value).is_integer() else f"${float(value):,.2f}"
    except ValueError:
        return value


def update_file_with_auto_section(path: Path, auto_section: str) -> None:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if AUTO_MARKER in existing:
        before = existing.split(AUTO_MARKER)[0].rstrip()
        new_content = before + "\n\n" + auto_section + "\n"
    else:
        new_content = existing.rstrip() + "\n\n" + auto_section + "\n"
    path.write_text(new_content, encoding="utf-8")


def build_breadth(buildings: List[Dict[str, str]]) -> str:
    today = date.today().isoformat()
    rows = sorted(
        buildings,
        key=lambda r: (STATUS_ORDER.get(r.get("status", ""), 99), -(float(r.get("overall_fit_score") or 0)), r.get("building_name", "")),
    )
    lines = [
        AUTO_MARKER,
        f"\n_Last regenerated: {today}_\n",
        "| Building | Neighborhood | Status | Hard stop | Quiet | Mgmt | Community | Overall fit | Unknowns | Notes |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]

    key_fields = [
        "quiet_score", "management_score", "amenity_score",
        "community_stability_score", "location_fit_score", "pricing_transparency_score",
    ]

    for row in rows:
        unknowns = sum(1 for field in key_fields if not row.get(field, "").strip())
        lines.append(
            "| {name} | {neighborhood} | {status} | {hard_stop} | {quiet} | {mgmt} | {community} | {overall} | {unknowns} | {notes} |".format(
                name=row.get("building_name", ""),
                neighborhood=row.get("neighborhood", ""),
                status=row.get("status", ""),
                hard_stop=row.get("hard_stop", ""),
                quiet=row.get("quiet_score", ""),
                mgmt=row.get("management_score", ""),
                community=row.get("community_stability_score", ""),
                overall=row.get("overall_fit_score", ""),
                unknowns=unknowns,
                notes=(row.get("notes", "") or "")[:90].replace("|", "/"),
            )
        )

    return "\n".join(lines)


def build_decision_log(decisions: List[Dict[str, str]], building_names: Dict[str, str]) -> str:
    today = date.today().isoformat()
    rows = sorted(decisions, key=lambda r: (r.get("date", ""), r.get("decision_id", "")), reverse=True)
    lines = [
        AUTO_MARKER,
        f"\n_Last regenerated: {today}_\n",
        "| Date | Building | Decision | Reason | Next action |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            "| {date} | {building} | {decision} | {reason} | {next_action} |".format(
                date=row.get("date", ""),
                building=building_names.get(row.get("building_id", ""), row.get("building_id", "")),
                decision=row.get("decision", ""),
                reason=(row.get("reason", "") or "")[:110].replace("|", "/"),
                next_action=(row.get("next_action", "") or "")[:110].replace("|", "/"),
            )
        )
    return "\n".join(lines)


def build_units(units: List[Dict[str, str]], buildings: Dict[str, Dict[str, str]]) -> str:
    today = date.today().isoformat()
    lines = [
        AUTO_MARKER,
        f"\n_Last regenerated: {today}. Sorted by true monthly cost ascending._\n",
        "| Building | Unit | Beds | Baths | sqft | Base rent | Net effective | True monthly cost | Available | Tour status | Building status |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]

    def sort_key(row: Dict[str, str]) -> Tuple[float, str]:
        val = row.get("true_monthly_cost") or row.get("net_effective_rent") or row.get("base_rent") or "9999999"
        try:
            return (float(val), row.get("unit_id", ""))
        except ValueError:
            return (9999999.0, row.get("unit_id", ""))

    for row in sorted(units, key=sort_key):
        building = buildings.get(row.get("building_id", ""), {})
        lines.append(
            "| {building_name} | {unit_number} | {bedrooms} | {bathrooms} | {sqft} | {base} | {net} | {true} | {available} | {tour_status} | {building_status} |".format(
                building_name=building.get("building_name", row.get("building_id", "")),
                unit_number=row.get("unit_number", ""),
                bedrooms=row.get("bedrooms", ""),
                bathrooms=row.get("bathrooms", ""),
                sqft=row.get("sqft", ""),
                base=money(row.get("base_rent", "")),
                net=money(row.get("net_effective_rent", "")),
                true=money(row.get("true_monthly_cost", "")),
                available=row.get("available_date", ""),
                tour_status=row.get("tour_status", ""),
                building_status=building.get("status", ""),
            )
        )

    if not units:
        lines.append("| _No unit rows yet_ |  |  |  |  |  |  |  |  |  |  |")

    return "\n".join(lines)


def main() -> int:
    buildings = read_csv(BUILDINGS_CSV)
    units = read_csv(UNITS_CSV)
    decisions = read_csv(DECISIONS_CSV)
    building_lookup = {row["building_id"]: row for row in buildings}
    building_names = {row["building_id"]: row["building_name"] for row in buildings}

    update_file_with_auto_section(BREADTH_MD, build_breadth(buildings))
    update_file_with_auto_section(DECISION_MD, build_decision_log(decisions, building_names))
    UNITS_MD.write_text(
        "# Unit Comparison\n\nGenerated from `data/units.csv` and `data/buildings.csv`.\n\n" + build_units(units, building_lookup) + "\n",
        encoding="utf-8",
    )

    print("Regenerated 02_neighborhood_breadth_scan.md, 07_decision_log.md, and 10_unit_comparison.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
