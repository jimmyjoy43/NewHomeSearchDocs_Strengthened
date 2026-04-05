#!/usr/bin/env python3
"""Compile Stage 3 research packets into payload JSON files.

Usage:
    python scripts/build_stage3_payloads.py
    python scripts/build_stage3_payloads.py --research-dir research
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESEARCH_DIR = REPO_ROOT / "research"
DEFAULT_BUILDINGS_CSV = REPO_ROOT / "data" / "buildings.csv"
DEFAULT_BUILDINGS_OUT = REPO_ROOT / "payload_buildings.json"
DEFAULT_EVIDENCE_OUT = REPO_ROOT / "payload_evidence.json"


def load_building_header(path: Path) -> List[str]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        return next(reader)


def stringify_map(data: Dict[str, object]) -> Dict[str, str]:
    return {str(k): "" if v is None else str(v) for k, v in data.items()}


def iter_packets_from_file(path: Path) -> Iterable[Dict[str, object]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, dict) and "building_row" in raw:
        yield raw
        return
    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict) and "building_row" in item:
                yield item
        return
    raise ValueError(f"{path} is not a Stage 3 packet object or array of packet objects.")


def packet_path_for(path: Path, research_dir: Path) -> str:
    try:
        rel = path.relative_to(research_dir.parent)
    except ValueError:
        rel = path
    return rel.as_posix()


def build_payloads(research_dir: Path, buildings_csv: Path) -> Tuple[List[Dict[str, str]], List[Dict[str, str]]]:
    header = load_building_header(buildings_csv)
    building_rows: Dict[str, Dict[str, str]] = {}
    evidence_rows: Dict[str, Dict[str, str]] = {}

    files = sorted(
        research_dir.glob("*.json"),
        key=lambda p: (0 if p.name.lower() == "all_buildings_research.json" else 1, p.name.lower()),
    )
    if not files:
        raise ValueError(f"No JSON research packets found in {research_dir}")

    for path in files:
        source_packet_path = packet_path_for(path, research_dir)
        for packet in iter_packets_from_file(path):
            raw_building = packet.get("building_row")
            if not isinstance(raw_building, dict):
                raise ValueError(f"{path} is missing a valid building_row object")

            building = stringify_map(raw_building)
            building_id = building.get("building_id", "").strip()
            if not building_id:
                raise ValueError(f"{path} contains a building_row without building_id")

            normalized = {col: building.get(col, "") for col in header}
            if "packet_path" in normalized and not normalized["packet_path"]:
                normalized["packet_path"] = source_packet_path
            building_rows[building_id] = normalized

            raw_evidence = packet.get("evidence_rows", [])
            if raw_evidence is None:
                raw_evidence = []
            if not isinstance(raw_evidence, list):
                raise ValueError(f"{path} contains non-list evidence_rows for {building_id}")

            for item in raw_evidence:
                if not isinstance(item, dict):
                    raise ValueError(f"{path} contains an invalid evidence row for {building_id}")
                evidence = stringify_map(item)
                evidence_id = evidence.get("evidence_id", "").strip()
                if not evidence_id:
                    raise ValueError(f"{path} contains an evidence row without evidence_id for {building_id}")
                evidence_rows[evidence_id] = evidence

    return list(building_rows.values()), list(evidence_rows.values())


def write_payload(path: Path, rows: List[Dict[str, str]]) -> None:
    path.write_text(json.dumps({"rows": rows}, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile Stage 3 research packets into payload JSON files.")
    parser.add_argument("--research-dir", default=str(DEFAULT_RESEARCH_DIR))
    parser.add_argument("--buildings-csv", default=str(DEFAULT_BUILDINGS_CSV))
    parser.add_argument("--buildings-out", default=str(DEFAULT_BUILDINGS_OUT))
    parser.add_argument("--evidence-out", default=str(DEFAULT_EVIDENCE_OUT))
    args = parser.parse_args()

    research_dir = Path(args.research_dir)
    buildings_csv = Path(args.buildings_csv)
    buildings_out = Path(args.buildings_out)
    evidence_out = Path(args.evidence_out)

    building_rows, evidence_rows = build_payloads(research_dir, buildings_csv)
    write_payload(buildings_out, building_rows)
    write_payload(evidence_out, evidence_rows)

    print(f"Compiled {len(building_rows)} building row(s) into {buildings_out}.")
    print(f"Compiled {len(evidence_rows)} evidence row(s) into {evidence_out}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
