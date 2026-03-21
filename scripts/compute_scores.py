#!/usr/bin/env python3
"""Compute overall building fit scores and hard-stop flags."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "config" / "decision_config.json"
BUILDINGS_CSV = REPO_ROOT / "data" / "buildings.csv"

CONF_COLS = {
    "quiet_score": "quiet_confidence",
    "management_score": "management_confidence",
    "amenity_score": "amenity_confidence",
    "community_stability_score": "community_stability_confidence",
}


def read_config() -> Dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def load_rows() -> Tuple[List[str], List[Dict[str, str]]]:
    with BUILDINGS_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return (reader.fieldnames or []), list(reader)


def to_float(value: str) -> float | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def score_to_utility(score: float, utility_map: Dict[str, float]) -> float:
    return float(utility_map[str(int(score))])


def confidence_penalty(row: Dict[str, str], score_col: str, penalty_map: Dict[str, float]) -> float:
    conf_col = CONF_COLS.get(score_col, "")
    conf_value = row.get(conf_col, "unknown").strip().lower() if conf_col else "unknown"
    return float(penalty_map.get(conf_value, penalty_map.get("unknown", 0.15)))


def compute_overall(row: Dict[str, str], cfg: Dict) -> str:
    weights = cfg["default_weights"]
    utility_map = cfg["utility_map"]
    penalty_map = cfg["confidence_penalty"]

    scored = []
    for col, weight in weights.items():
        raw = to_float(row.get(col, ""))
        if raw is None:
            continue
        scored.append((col, float(weight), score_to_utility(raw, utility_map), confidence_penalty(row, col, penalty_map)))

    required = {"quiet_score", "management_score"}
    present = {col for col, _, _, _ in scored}
    if not required.issubset(present) or len(scored) < 3:
        return ""

    total_weight = sum(weight for _, weight, _, _ in scored)
    utility = sum(weight * val for _, weight, val, _ in scored) / total_weight
    penalty = sum(weight * pen for _, weight, _, pen in scored) / total_weight
    overall = max(0.0, min(100.0, round(100.0 * (utility - penalty), 1)))
    return f"{overall:.1f}"


def compute_hard_stop(row: Dict[str, str], cfg: Dict) -> str:
    rules = cfg["hard_stop_rules"]
    mgmt = to_float(row.get("management_score", ""))
    quiet = to_float(row.get("quiet_score", ""))
    approval = to_float(row.get("approval_speed_business_days", ""))
    security = row.get("security_risk", "").strip().lower()

    existing = row.get("hard_stop", "").strip().lower()
    if existing == "yes":
        return "yes"

    if mgmt is not None and quiet is not None:
        if mgmt <= rules["management_score_lte"] and quiet <= rules["quiet_score_lte"]:
            return "yes"

    if approval is not None and approval > rules["approval_speed_business_days_gt"]:
        return "yes"

    if security == rules["security_risk_equals"]:
        return "yes"

    return "no" if existing in {"", "unknown", "no"} else existing


def write_rows(header: List[str], rows: List[Dict[str, str]]) -> None:
    with BUILDINGS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    cfg = read_config()
    header, rows = load_rows()
    for row in rows:
        row["overall_fit_score"] = compute_overall(row, cfg)
        row["hard_stop"] = compute_hard_stop(row, cfg)
    write_rows(header, rows)
    print(f"Updated {len(rows)} building row(s) in {BUILDINGS_CSV}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
