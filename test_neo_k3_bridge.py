#!/usr/bin/env python3
import unittest
from fractions import Fraction

from calculs.check_neo_k3_bridge import (
    K3,
    DOUBLING_CHAIN,
    DELTA_C,
    PRE_PI_SCALED,
    GENESIS_NUMERATOR,
    GENESIS_PRE_PI_SCALED,
    ABS_DIFF,
    REL_DIFF,
    RESIDUAL_977,
    GENESIS_DIFF,
)


class TestNeoK3BrutusBridge(unittest.TestCase):
    def test_k3(self):
        self.assertEqual(K3, Fraction(3, 13))

    def test_exact_doubling_chain(self):
        self.assertEqual(
            DOUBLING_CHAIN,
            (
                Fraction(3, 13),
                Fraction(6, 13),
                Fraction(12, 13),
                Fraction(24, 13),
            ),
        )

    def test_delta_c(self):
        self.assertEqual(DELTA_C, 207542)

    def test_pre_pi_scaled(self):
        self.assertEqual(PRE_PI_SCALED, Fraction(103771, 450000))

    def test_genesis_rewrite(self):
        self.assertEqual(GENESIS_NUMERATOR, 207542)
        self.assertEqual(GENESIS_PRE_PI_SCALED, PRE_PI_SCALED)

    def test_exact_difference(self):
        self.assertEqual(ABS_DIFF, Fraction(977, 5850000))

    def test_relative_difference(self):
        self.assertEqual(REL_DIFF, Fraction(977, 1350000))

    def test_residual_rewrite(self):
        self.assertEqual(RESIDUAL_977, 977)
        self.assertEqual(GENESIS_DIFF, ABS_DIFF)


if __name__ == "__main__":
    unittest.main(verbosity=2)
