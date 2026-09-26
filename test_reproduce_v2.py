#!/usr/bin/env python3
"""Correction tests for V2 reconstruction semantics."""

import subprocess
import sys
import unittest
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parent
INTERMEDIATE_SCRIPT = ROOT / "calculs" / "reproduce_v2.py"
MASS_SCRIPT = ROOT / "calculs" / "reproduce_mass_high_precision.py"

sys.path.insert(0, str(ROOT / "calculs"))
import reproduce_v2 as v2
import reproduce_mass_high_precision as mass


class TestBosonDeBrutusV2Correction(unittest.TestCase):
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

    def test_offset_value_is_named_intermediate(self):
        self.assertEqual(
            v2.NEO_OFFSET_INTERMEDIATE,
            Fraction(
                5764800999990000000000002401,
                9999999999997599000000,
            ),
        )
        self.assertFalse(hasattr(v2, "BOSON_V2"))

    def test_four_sevenths_is_preserved_as_intermediate(self):
        self.assertEqual(
            v2.FOUR_SEVENTHS_INTERMEDIATE,
            Fraction(
                5764800999990000000000002401,
                17499999999995798250000,
            ),
        )

    def test_small_frozen_v1_high_precision_prefix(self):
        value = format(mass.frozen_v1(120), "e")
        self.assertTrue(
            value.startswith(
                "2.233576397498740792411442896327489490267550118723876865300357561047"
            ),
            value,
        )

    def test_conditional_gev_prefix(self):
        value = format(mass.gev_if_grams(110), "f")
        self.assertTrue(
            value.startswith(
                "125.294447051355389172672924099202511961320161652122704217577"
            ),
            value,
        )

    def test_v1_frozen_files_still_exist(self):
        self.assertTrue((ROOT / "FORMULE-FIGEE-2026-09-19.md").is_file())
        self.assertTrue((ROOT / "calculs" / "reproduce.py").is_file())
        self.assertTrue((ROOT / "test_reproduce.py").is_file())

    def test_both_reproduction_scripts_execute(self):
        for script in (INTERMEDIATE_SCRIPT, MASS_SCRIPT):
            completed = subprocess.run(
                [sys.executable, str(script)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
