#!/usr/bin/env python3
"""Reproduce the exact high-precision NEO/cadence intermediate chain.

Important: these values are intermediate mathematical quantities.
They are not the final Boson mass candidate.
"""

from decimal import Decimal, localcontext
from fractions import Fraction

F0 = Fraction(2401, 10)
DT = Fraction(1, 10**15)
SCALE_2401 = 2401
OFFSET = Fraction(1, 10**6)

F_ABS = F0 / (1 - F0 * DT)
NEO_EXACT = SCALE_2401 * F_ABS
NEO_OFFSET_INTERMEDIATE = NEO_EXACT - OFFSET
FOUR_SEVENTHS_NEO = Fraction(4, 7) * NEO_EXACT
FOUR_SEVENTHS_INTERMEDIATE = Fraction(4, 7) * NEO_OFFSET_INTERMEDIATE


def decimal_string(value: Fraction, digits: int = 220) -> str:
    with localcontext() as ctx:
        ctx.prec = digits
        return format(Decimal(value.numerator) / Decimal(value.denominator), "f")


def main() -> None:
    print(f"f_abs exact = {F_ABS.numerator}/{F_ABS.denominator}")
    print(f"NEO exact = {NEO_EXACT.numerator}/{NEO_EXACT.denominator}")
    print(
        "NEO offset intermediate exact = "
        f"{NEO_OFFSET_INTERMEDIATE.numerator}/{NEO_OFFSET_INTERMEDIATE.denominator}"
    )
    print(f"4/7 NEO exact = {FOUR_SEVENTHS_NEO.numerator}/{FOUR_SEVENTHS_NEO.denominator}")
    print(
        "4/7 intermediate exact = "
        f"{FOUR_SEVENTHS_INTERMEDIATE.numerator}/{FOUR_SEVENTHS_INTERMEDIATE.denominator}"
    )
    print("f_abs =", decimal_string(F_ABS))
    print("NEO =", decimal_string(NEO_EXACT))
    print("NEO offset intermediate =", decimal_string(NEO_OFFSET_INTERMEDIATE))
    print("4/7 NEO =", decimal_string(FOUR_SEVENTHS_NEO))
    print("4/7 intermediate =", decimal_string(FOUR_SEVENTHS_INTERMEDIATE))


if __name__ == "__main__":
    main()
