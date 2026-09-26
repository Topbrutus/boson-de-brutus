#!/usr/bin/env python3
"""Reproduce the exact post-hoc Genesis rewrite of Delta-c.

The identity is exact but was discovered after Delta-c was known.
It is not an independent prediction.
"""

from fractions import Fraction

C_ROUND = 300_000_000
C_EXACT = 299_792_458
DELTA_C = C_ROUND - C_EXACT

LEFT = 7 * 13 - 9
RIGHT = 7**4 + 10 * 13
GENESIS_REWRITE = LEFT * RIGHT

BRUTUS_NORMALIZED = Fraction(DELTA_C, C_ROUND)
BRUTUS_REWRITE = Fraction(GENESIS_REWRITE, 3 * 10**8)


def main() -> None:
    print("Delta-c =", DELTA_C)
    print("left = 7*13-9 =", LEFT)
    print("right = 7^4+10*13 =", RIGHT)
    print("rewrite =", GENESIS_REWRITE)
    print("normalized original =", BRUTUS_NORMALIZED)
    print("normalized rewrite =", BRUTUS_REWRITE)
    print("exact_equal =", DELTA_C == GENESIS_REWRITE)
    print("normalized_equal =", BRUTUS_NORMALIZED == BRUTUS_REWRITE)


if __name__ == "__main__":
    main()
