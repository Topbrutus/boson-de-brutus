#!/usr/bin/env python3
import unittest

from calculs.check_genesis_bridge import (
    DELTA_C,
    LEFT,
    RIGHT,
    GENESIS_REWRITE,
    BRUTUS_NORMALIZED,
    BRUTUS_REWRITE,
)


class TestPostHocGenesisRewrite(unittest.TestCase):
    def test_delta_c(self):
        self.assertEqual(DELTA_C, 207542)

    def test_left_factor(self):
        self.assertEqual(LEFT, 82)

    def test_right_factor(self):
        self.assertEqual(RIGHT, 2531)

    def test_exact_rewrite(self):
        self.assertEqual(GENESIS_REWRITE, 207542)

    def test_normalized_relation_is_identical(self):
        self.assertEqual(BRUTUS_NORMALIZED, BRUTUS_REWRITE)


if __name__ == "__main__":
    unittest.main(verbosity=2)
