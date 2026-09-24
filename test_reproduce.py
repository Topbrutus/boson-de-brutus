#!/usr/bin/env python3
"""Non-regression tests for the frozen Brutus V1 numerical relation.

These tests protect the already-frozen V1 calculation. They do not establish
physical validity and they do not alter the candidate interpretation.
"""

from pathlib import Path
import math
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parent
FORMULA_SPEC = ROOT / "FORMULE-FIGEE-2026-09-19.md"
RULES_SPEC = ROOT / "REGLES-ET-EXEMPLES-V1.md"
REPRODUCE = ROOT / "calculs" / "reproduce.py"

C_ROUND = 300_000_000
C_EXACT = 299_792_458
SCALE = 3e18
EXPECTED_V1 = 2.2335763974987408e-22


def compute_v1() -> float:
    return (
        ((C_ROUND - C_EXACT) / C_ROUND)
        * (1 / SCALE)
        * (1 - math.pi / 100)
    )


class TestBosonDeBrutusV1(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(FORMULA_SPEC.is_file(), f"Missing: {FORMULA_SPEC}")
        self.assertTrue(RULES_SPEC.is_file(), f"Missing: {RULES_SPEC}")
        self.assertTrue(REPRODUCE.is_file(), f"Missing: {REPRODUCE}")

    def test_frozen_constants_are_unchanged(self) -> None:
        self.assertEqual(C_ROUND, 300_000_000)
        self.assertEqual(C_EXACT, 299_792_458)
        self.assertEqual(SCALE, 3e18)

    def test_frozen_v1_exact_float_result(self) -> None:
        actual = compute_v1()
        self.assertEqual(
            actual,
            EXPECTED_V1,
            f"Frozen V1 numerical drift: got {actual:.25e}",
        )

    def test_reproduce_script_executes_and_reports_frozen_value(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(REPRODUCE)],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"reproduce.py failed:\nSTDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}",
        )
        self.assertIn(
            "Brutus V1 = 2.2335763974987408e-22",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
