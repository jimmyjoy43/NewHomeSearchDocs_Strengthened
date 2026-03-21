#!/usr/bin/env python3
"""Validate all canonical CSV files for the housing search repo.

Usage:
    python scripts/validate_data.py
    python scripts/validate_data.py data
"""

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"

TRISTATE = {"yes", "no", "unknown", ""}
CONFIDENCE = {"high", "medium", "low", "unknown", ""}
RISK = {"low", "medium", "high", "unknown", ""}
STATUS = {
    "candidate",
    "screened",
    "research_complete",
    "tour_candidate",
    "toured",
    "backup",
    "finalist",
    "rejected",
    "leased",
    "",
}
TOUR_STATUS = {"not_scheduled", "scheduled", "completed", "skipped", "", "rejected"}
DECISIONS = {
    "reject",
    "advance_to_tour",
    "backup",
    "finalist",
    "apply",
    "sign",
    "hold",
    "",
}
SCOPE_TYPES = {"building", "unit", "portfolio", "neighborhood", ""}
EVIDENCE_CLASS = {"confirmed", "corroborated", "anecdotal", "inferred", "unknown", ""}
SENTIMENT = {"positive", "mixed", "negative", "neutral", ""}


@dataclass
class Schema:
    required_columns: List[str]
    nonempty: List[str]
    numeric: List[str]
    nonnegative: List[str]
    score_fields: List[str]
    date_fields: List[str]
    enums: Dict[str, set]
    unique_key: str | None = None


SCHEMAS: Dict[str, Schema] = {
    "buildings.csv": Schema(
        required_columns=[
            "building_id", "building_name", "address", "neighborhood", "source_url",
            "management_company", "building_class", "construction_type", "rso_status",
            "cat_friendly", "package_handling", "controlled_access", "gym", "pool",
            "coworking", "conference_room", "ev_charging", "rooftop", "parking_solution",
            "quiet_score", "quiet_confidence", "quiet_evidence_count", "management_score",
            "management_confidence", "management_evidence_count", "amenity_score",
            "amenity_confidence", "amenity_evidence_count", "community_stability_score",
            "community_stability_confidence", "community_stability_evidence_count",
            "location_fit_score", "pricing_transparency_score", "approval_speed_business_days",
            "structural_noise_risk", "location_noise_risk", "security_risk", "pricing_risk",
            "overall_fit_score", "hard_stop", "status", "review_scan_done",
            "deep_research_done", "packet_path", "open_questions", "notes", "last_updated",
        ],
        nonempty=["building_id", "building_name", "address", "neighborhood"],
        numeric=[
            "quiet_score", "quiet_evidence_count", "management_score", "management_evidence_count",
            "amenity_score", "amenity_evidence_count", "community_stability_score",
            "community_stability_evidence_count", "location_fit_score",
            "pricing_transparency_score", "approval_speed_business_days", "overall_fit_score",
        ],
        nonnegative=[
            "quiet_evidence_count", "management_evidence_count", "amenity_evidence_count",
            "community_stability_evidence_count", "approval_speed_business_days", "overall_fit_score",
        ],
        score_fields=[
            "quiet_score", "management_score", "amenity_score",
            "community_stability_score", "location_fit_score", "pricing_transparency_score",
        ],
        date_fields=["last_updated"],
        enums={
            "cat_friendly": TRISTATE,
            "package_handling": TRISTATE,
            "controlled_access": TRISTATE,
            "gym": TRISTATE,
            "pool": TRISTATE,
            "coworking": TRISTATE,
            "conference_room": TRISTATE,
            "ev_charging": TRISTATE,
            "rooftop": TRISTATE,
            "quiet_confidence": CONFIDENCE,
            "management_confidence": CONFIDENCE,
            "amenity_confidence": CONFIDENCE,
            "community_stability_confidence": CONFIDENCE,
            "structural_noise_risk": RISK,
            "location_noise_risk": RISK,
            "security_risk": RISK,
            "pricing_risk": RISK,
            "hard_stop": TRISTATE,
            "status": STATUS,
            "review_scan_done": TRISTATE,
            "deep_research_done": TRISTATE,
        },
        unique_key="building_id",
    ),
    "units.csv": Schema(
        required_columns=[
            "unit_id", "building_id", "unit_number", "listing_url", "bedrooms", "bathrooms",
            "sqft", "base_rent", "concession_value_total", "lease_term_months", "available_date",
            "application_fee", "admin_fee", "security_deposit", "parking_cost", "pet_rent",
            "estimated_utilities", "balcony", "in_unit_laundry", "dishwasher", "central_ac",
            "natural_light", "closet_storage", "exact_unit_shown", "exposure",
            "nearest_noise_source", "net_effective_rent", "true_monthly_cost", "tour_status",
            "notes", "last_updated",
        ],
        nonempty=["unit_id", "building_id"],
        numeric=[
            "bedrooms", "bathrooms", "sqft", "base_rent", "concession_value_total",
            "lease_term_months", "application_fee", "admin_fee", "security_deposit",
            "parking_cost", "pet_rent", "estimated_utilities", "net_effective_rent",
            "true_monthly_cost",
        ],
        nonnegative=[
            "bedrooms", "bathrooms", "sqft", "base_rent", "concession_value_total",
            "lease_term_months", "application_fee", "admin_fee", "security_deposit",
            "parking_cost", "pet_rent", "estimated_utilities", "net_effective_rent",
            "true_monthly_cost",
        ],
        score_fields=[],
        date_fields=["available_date", "last_updated"],
        enums={
            "balcony": TRISTATE,
            "in_unit_laundry": TRISTATE,
            "dishwasher": TRISTATE,
            "central_ac": TRISTATE,
            "natural_light": TRISTATE,
            "closet_storage": TRISTATE,
            "exact_unit_shown": TRISTATE,
            "tour_status": TOUR_STATUS,
        },
        unique_key="unit_id",
    ),
    "evidence.csv": Schema(
        required_columns=[
            "evidence_id", "scope_type", "scope_id", "criterion", "claim", "source_type",
            "source_name", "source_url", "retrieved_date", "evidence_class", "sentiment",
            "quote_or_note",
        ],
        nonempty=["evidence_id", "scope_type", "scope_id", "criterion", "claim"],
        numeric=[],
        nonnegative=[],
        score_fields=[],
        date_fields=["retrieved_date"],
        enums={
            "scope_type": SCOPE_TYPES,
            "evidence_class": EVIDENCE_CLASS,
            "sentiment": SENTIMENT,
        },
        unique_key="evidence_id",
    ),
    "tours.csv": Schema(
        required_columns=[
            "tour_id", "building_id", "unit_id", "tour_date", "tour_type", "leasing_agent",
            "approval_speed_business_days", "first_impression_score", "noise_observation",
            "unit_condition", "common_area_condition", "staff_responsiveness", "questions_answered",
            "red_flags", "follow_up_needed", "notes", "last_updated",
        ],
        nonempty=["tour_id", "building_id", "tour_date"],
        numeric=["approval_speed_business_days", "first_impression_score"],
        nonnegative=["approval_speed_business_days"],
        score_fields=["first_impression_score"],
        date_fields=["tour_date", "last_updated"],
        enums={},
        unique_key="tour_id",
    ),
    "contacts.csv": Schema(
        required_columns=[
            "contact_id", "building_id", "unit_id", "contact_name", "role", "phone", "email",
            "date_contacted", "method", "response_received", "approval_speed_business_days",
            "notes", "last_updated",
        ],
        nonempty=["contact_id", "building_id", "date_contacted"],
        numeric=["approval_speed_business_days"],
        nonnegative=["approval_speed_business_days"],
        score_fields=[],
        date_fields=["date_contacted", "last_updated"],
        enums={"response_received": TRISTATE},
        unique_key="contact_id",
    ),
    "decisions.csv": Schema(
        required_columns=[
            "decision_id", "date", "building_id", "unit_id", "decision", "reason", "next_action",
            "decided_by", "last_updated",
        ],
        nonempty=["decision_id", "date", "building_id", "decision"],
        numeric=[],
        nonnegative=[],
        score_fields=[],
        date_fields=["date", "last_updated"],
        enums={"decision": DECISIONS},
        unique_key="decision_id",
    ),
}


def read_csv(path: Path) -> Tuple[List[str], List[Dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return (reader.fieldnames or []), list(reader)


def is_date(value: str) -> bool:
    if value == "":
        return True
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_numeric(value: str) -> bool:
    if value == "":
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False


def validate_rows(filename: str, header: List[str], rows: List[Dict[str, str]]) -> List[str]:
    schema = SCHEMAS[filename]
    errors: List[str] = []

    missing = [c for c in schema.required_columns if c not in header]
    if missing:
        errors.append(f"{filename}: missing required columns: {missing}")
        return errors

    extra = [c for c in header if c not in schema.required_columns]
    if extra:
        errors.append(f"{filename}: unexpected extra columns: {extra}")

    seen = set()

    for idx, row in enumerate(rows, start=2):
        for col in schema.nonempty:
            if not row.get(col, "").strip():
                errors.append(f"{filename} row {idx}: '{col}' is required")

        for col in schema.numeric:
            val = row.get(col, "").strip()
            if not is_numeric(val):
                errors.append(f"{filename} row {idx}: '{col}' must be numeric (got '{val}')")

        for col in schema.nonnegative:
            val = row.get(col, "").strip()
            if val != "" and is_numeric(val) and float(val) < 0:
                errors.append(f"{filename} row {idx}: '{col}' must be non-negative (got '{val}')")

        for col in schema.score_fields:
            val = row.get(col, "").strip()
            if val != "" and (not is_numeric(val) or not (1 <= float(val) <= 5)):
                errors.append(f"{filename} row {idx}: '{col}' must be between 1 and 5 (got '{val}')")

        for col in schema.date_fields:
            val = row.get(col, "").strip()
            if not is_date(val):
                errors.append(f"{filename} row {idx}: '{col}' must be YYYY-MM-DD (got '{val}')")

        for col, allowed in schema.enums.items():
            val = row.get(col, "").strip().lower()
            if val not in allowed:
                errors.append(
                    f"{filename} row {idx}: '{col}' must be one of {sorted(v for v in allowed if v != '') + [''] if '' in allowed else sorted(allowed)} (got '{row.get(col, '')}')"
                )

        if schema.unique_key:
            key = row.get(schema.unique_key, "").strip()
            if key:
                if key in seen:
                    errors.append(f"{filename} row {idx}: duplicate {schema.unique_key} '{key}'")
                seen.add(key)

    return errors


def validate_cross_file(data: Dict[str, List[Dict[str, str]]]) -> List[str]:
    errors: List[str] = []
    buildings = {r["building_id"] for r in data["buildings.csv"] if r.get("building_id")}
    units = {r["unit_id"] for r in data["units.csv"] if r.get("unit_id")}

    for row in data["units.csv"]:
        bid = row.get("building_id", "").strip()
        if bid and bid not in buildings:
            errors.append(f"units.csv: building_id '{bid}' does not exist in buildings.csv")
        net = row.get("net_effective_rent", "").strip()
        base = row.get("base_rent", "").strip()
        true = row.get("true_monthly_cost", "").strip()
        if net and base and float(net) > float(base) + 1e-9:
            errors.append(
                f"units.csv: unit_id '{row.get('unit_id')}' has net_effective_rent greater than base_rent"
            )
        if true and net and float(true) + 1e-9 < float(net):
            errors.append(
                f"units.csv: unit_id '{row.get('unit_id')}' has true_monthly_cost lower than net_effective_rent"
            )

    for filename in ("tours.csv", "contacts.csv", "decisions.csv"):
        for row in data[filename]:
            bid = row.get("building_id", "").strip()
            uid = row.get("unit_id", "").strip()
            if bid and bid not in buildings:
                errors.append(f"{filename}: building_id '{bid}' does not exist in buildings.csv")
            if uid and uid not in units:
                errors.append(f"{filename}: unit_id '{uid}' does not exist in units.csv")

    for row in data["evidence.csv"]:
        scope_type = row.get("scope_type", "").strip()
        scope_id = row.get("scope_id", "").strip()
        if scope_type == "building" and scope_id not in buildings:
            errors.append(f"evidence.csv: building scope_id '{scope_id}' does not exist in buildings.csv")
        if scope_type == "unit" and scope_id not in units:
            errors.append(f"evidence.csv: unit scope_id '{scope_id}' does not exist in units.csv")

    return errors


def validate_repo(data_dir: Path = DATA_DIR) -> Tuple[bool, List[str]]:
    data: Dict[str, List[Dict[str, str]]] = {}
    errors: List[str] = []

    for filename in SCHEMAS:
        path = data_dir / filename
        if not path.exists():
            errors.append(f"Missing required file: {path}")
            continue
        header, rows = read_csv(path)
        data[filename] = rows
        errors.extend(validate_rows(filename, header, rows))

    if not errors and all(name in data for name in SCHEMAS):
        errors.extend(validate_cross_file(data))

    return (len(errors) == 0, errors)


def main(argv: List[str]) -> int:
    data_dir = Path(argv[1]) if len(argv) > 1 else DATA_DIR
    ok, errors = validate_repo(data_dir)
    if ok:
        print("OK: all canonical CSV files passed validation.")
        return 0
    for err in errors:
        print(f"FAIL: {err}")
    print(f"\nValidation failed with {len(errors)} issue(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
