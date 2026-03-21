from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / 'scripts'))

from validate_data import validate_repo  # type: ignore


class ValidateDataTests(unittest.TestCase):
    def write_csv(self, path: Path, fieldnames, rows):
        with path.open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def test_repo_fixture_passes(self):
        ok, errors = validate_repo(REPO_ROOT / 'data')
        self.assertTrue(ok, msg='\n'.join(errors))

    def test_cross_file_reference_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            data_dir = tmpdir / 'data'
            data_dir.mkdir()

            from validate_data import SCHEMAS  # type: ignore

            for filename, schema in SCHEMAS.items():
                self.write_csv(data_dir / filename, schema.required_columns, [])

            buildings_header = SCHEMAS['buildings.csv'].required_columns
            self.write_csv(
                data_dir / 'buildings.csv',
                buildings_header,
                [{
                    'building_id': 'b1',
                    'building_name': 'Test Building',
                    'address': '1 Test Way',
                    'neighborhood': 'Hollywood',
                    'status': 'candidate',
                    'hard_stop': 'unknown',
                    'review_scan_done': 'no',
                    'deep_research_done': 'no',
                    'last_updated': '2026-03-21',
                }],
            )

            units_header = SCHEMAS['units.csv'].required_columns
            self.write_csv(
                data_dir / 'units.csv',
                units_header,
                [{
                    'unit_id': 'u1',
                    'building_id': 'missing-building',
                    'unit_number': '101',
                    'last_updated': '2026-03-21',
                }],
            )

            ok, errors = validate_repo(data_dir)
            self.assertFalse(ok)
            self.assertTrue(any('missing-building' in err for err in errors))


if __name__ == '__main__':
    unittest.main()
