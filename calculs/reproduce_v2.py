#!/usr/bin/env python3
"""Reproduce Boson de Brutus V2 with exact rational arithmetic."""

from decimal import Decimal, localcontext
from fractions import Fraction

F0 = Fraction(2401, 10)
DT = Fraction(1, 10**15)
SCALE_2401 = 2401
OFFSET = Fraction(1, 10**6)

F_ABS = F0 / (1 - F0 * DT)
NEO_EXACT = SCALE_2401 * F_ABS
BOSON_V2 = NEO_EXACT - OFFSET
FOUR_SEVENTHS_NEO = Fraction(4, 7) * NEO_EXACT
FOUR_SEVENTHS_BOSON = Fraction(4, 7) * BOSON_V2


def decimal_string(value: Fraction, digits: int = 220) -> str:
    with localcontext() as ctx:
        ctx.prec = digits
        return format(Decimal(value.numerator) / Decimal(value.denominator), "f")


def main() -> None:
    print(f"f_abs exact = {F_ABS.numerator}/{F_ABS.denominator}")
    print(f"NEO exact = {NEO_EXACT.numerator}/{NEO_EXACT.denominator}")
    print(f"Boson V2 exact = {BOSON_V2.numerator}/{BOSON_V2.denominator}")
    print(f"4/7 NEO exact = {FOUR_SEVENTHS_NEO.numerator}/{FOUR_SEVENTHS_NEO.denominator}")
    print(f"4/7 Boson V2 exact = {FOUR_SEVENTHS_BOSON.numerator}/{FOUR_SEVENTHS_BOSON.denominator}")
    print("f_abs =", decimal_string(F_ABS))
    print("NEO =", decimal_string(NEO_EXACT))
    print("Boson V2 =", decimal_string(BOSON_V2))
    print("4/7 NEO =", decimal_string(FOUR_SEVENTHS_NEO))
    print("4/7 Boson V2 =", decimal_string(FOUR_SEVENTHS_BOSON))


if __name__ == "__main__":
    main()
