from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path

import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from build_stage3_payloads import build_payloads  # type: ignore
from validate_data import SCHEMAS  # type: ignore


class BuildStage3PayloadsTests(unittest.TestCase):
    def write_buildings_csv(self, path: Path) -> None:
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=SCHEMAS["buildings.csv"].required_columns)
            writer.writeheader()

    def test_build_payloads_compiles_individual_and_combined_packets(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            research_dir = tmpdir / "research"
            data_dir = tmpdir / "data"
            research_dir.mkdir()
            data_dir.mkdir()

            buildings_csv = data_dir / "buildings.csv"
            self.write_buildings_csv(buildings_csv)

            combined_packet = [
                {
                    "building_row": {
                        "building_id": "b-combined",
                        "management_company": "Combined Mgmt",
                        "quiet_score": "4",
                        "notes": "from combined",
                        "last_updated": "2026-04-05",
                    },
                    "evidence_rows": [
                        {
                            "evidence_id": "b-combined--ev-1",
                            "scope_type": "building",
                            "scope_id": "b-combined",
                            "criterion": "quiet",
                            "claim": "quiet on upper floors",
                            "source_type": "review",
                            "source_name": "Example Reviews",
                            "source_url": "https://example.com/review",
                            "retrieved_date": "2026-04-05",
                            "evidence_class": "anecdotal",
                            "sentiment": "positive",
                            "quote_or_note": "sample",
                        }
                    ],
                    "packet_markdown": "# Combined",
                }
            ]
            (research_dir / "all_buildings_research.json").write_text(
                json.dumps(combined_packet),
                encoding="utf-8",
            )

            single_packet = {
                "building_row": {
                    "building_id": "b-single",
                    "management_company": "Single Mgmt",
                    "quiet_score": "3",
                    "notes": "from single",
                    "last_updated": "2026-04-05",
                    "extra_field_not_in_csv": "ignored",
                },
                "evidence_rows": [
                    {
                        "evidence_id": "b-single--ev-1",
                        "scope_type": "building",
                        "scope_id": "b-single",
                        "criterion": "management",
                        "claim": "manager responded quickly",
                        "source_type": "official",
                        "source_name": "Leasing Office",
                        "source_url": "https://example.com/official",
                        "retrieved_date": "2026-04-05",
                        "evidence_class": "confirmed",
                        "sentiment": "positive",
                        "quote_or_note": "sample",
                    }
                ],
                "packet_markdown": "# Single",
            }
            (research_dir / "b-single.json").write_text(json.dumps(single_packet), encoding="utf-8")

            building_rows, evidence_rows = build_payloads(research_dir, buildings_csv)

            self.assertEqual(2, len(building_rows))
            self.assertEqual(2, len(evidence_rows))

            by_id = {row["building_id"]: row for row in building_rows}
            self.assertEqual("research/all_buildings_research.json", by_id["b-combined"]["packet_path"])
            self.assertEqual("research/b-single.json", by_id["b-single"]["packet_path"])
            self.assertNotIn("extra_field_not_in_csv", by_id["b-single"])


if __name__ == "__main__":
    unittest.main()
