#!/usr/bin/env python3
"""Exact arithmetic checks for the NEO K3 ↔ Brutus pre-pi bridge.

All identities are post-hoc observations. No physical interpretation follows
from the arithmetic alone.
"""

from fractions import Fraction

K3 = Fraction(3, 13)
DOUBLING_CHAIN = tuple(K3 * (2**i) for i in range(4))

DELTA_C = 300_000_000 - 299_792_458
PRE_PI_SCALED = Fraction(DELTA_C, 900_000)

GENESIS_NUMERATOR = (7 * 13 - 9) * (7**4 + 10 * 13)
GENESIS_PRE_PI_SCALED = Fraction(GENESIS_NUMERATOR, 9 * 10**5)

ABS_DIFF = K3 - PRE_PI_SCALED
REL_DIFF = ABS_DIFF / K3

RESIDUAL_977 = 3 * 7**3 - (13 - 9) * 13
GENESIS_DIFF = Fraction(
    (9 - 7) * RESIDUAL_977,
    13 * 9 * 10**5,
)


def main() -> None:
    print("K3 =", K3)
    print("doubling chain =", DOUBLING_CHAIN)
    print("Delta-c =", DELTA_C)
    print("pre-pi scaled =", PRE_PI_SCALED)
    print("Genesis numerator =", GENESIS_NUMERATOR)
    print("Genesis pre-pi scaled =", GENESIS_PRE_PI_SCALED)
    print("absolute difference =", ABS_DIFF)
    print("relative difference =", REL_DIFF)
    print("relative percent =", float(REL_DIFF * 100))
    print("residual numerator rewrite =", RESIDUAL_977)
    print("Genesis difference =", GENESIS_DIFF)


if __name__ == "__main__":
    main()
