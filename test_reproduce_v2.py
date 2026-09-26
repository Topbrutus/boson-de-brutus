#!/usr/bin/env python3
"""Integrity tests for the high-precision Boson de Brutus V2 chain."""

import subprocess
import sys
import unittest
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "calculs" / "reproduce_v2.py"

sys.path.insert(0, str(ROOT / "calculs"))
import reproduce_v2 as v2


class TestBosonDeBrutusV2(unittest.TestCase):
    def test_exact_frequency_fraction(self):
        self.assertEqual(
            v2.F_ABS,
            Fraction(2401000000000000000, 9999999999997599),
        )

    def test_exact_neo_fraction(self):
        self.assertEqual(
            v2.NEO_EXACT,
            Fraction(5764801000000000000000, 9999999999997599),
        )

    def test_exact_boson_v2_fraction(self):
        self.assertEqual(
            v2.BOSON_V2,
            Fraction(
                5764800999990000000000002401,
                9999999999997599000000,
            ),
        )

    def test_four_sevenths_neo_exact(self):
        self.assertEqual(
            v2.FOUR_SEVENTHS_NEO,
            Fraction(3294172000000000000000, 9999999999997599),
        )

    def test_four_sevenths_boson_exact(self):
        self.assertEqual(
            v2.FOUR_SEVENTHS_BOSON,
            Fraction(
                5764800999990000000000002401,
                17499999999995798250000,
            ),
        )

    def test_decimal_prefixes(self):
        self.assertTrue(
            v2.decimal_string(v2.NEO_EXACT, 180).startswith(
                "576480.1000001384128720100332329305696089792266297631159"
            )
        )
        self.assertTrue(
            v2.decimal_string(v2.BOSON_V2, 180).startswith(
                "576480.0999991384128720100332329305696089792266297631159"
            )
        )
        self.assertTrue(
            v2.decimal_string(v2.FOUR_SEVENTHS_BOSON, 180).startswith(
                "329417.1999995076644982914475616746112051309866455789233"
            )
        )

    def test_v1_frozen_spec_still_exists(self):
        self.assertTrue((ROOT / "FORMULE-FIGEE-2026-09-19.md").is_file())
        self.assertTrue((ROOT / "test_reproduce.py").is_file())

    def test_reproduction_script_executes(self):
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("Boson V2 exact =", completed.stdout)
        self.assertIn("4/7 Boson V2 exact =", completed.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
