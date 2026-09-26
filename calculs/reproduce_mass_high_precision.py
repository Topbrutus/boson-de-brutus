#!/usr/bin/env python3
"""High-precision evaluation of the unchanged Frozen V1 relation.

This does not alter the V1 formula. It only evaluates the same expression
with Decimal arithmetic and a Decimal computation of pi.
"""

from decimal import Decimal, localcontext


def arctan_inverse(n: int, digits: int) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = digits + 12
        x = Decimal(1) / Decimal(n)
        x2 = x * x
        term = x
        total = term
        k = 1
        sign = -1
        threshold = Decimal(10) ** (-(digits + 6))
        while True:
            term *= x2
            add = term / Decimal(2 * k + 1)
            if abs(add) < threshold:
                break
            total = total - add if sign < 0 else total + add
            sign *= -1
            k += 1
        return +total


def decimal_pi(digits: int = 120) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = digits + 10
        value = Decimal(16) * arctan_inverse(5, digits + 5) - Decimal(4) * arctan_inverse(239, digits + 5)
        ctx.prec = digits
        return +value


def frozen_v1(digits: int = 120) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = digits
        p = Decimal(300_000_000)
        c = Decimal(299_792_458)
        pi = decimal_pi(digits)
        return +(((p - c) / p) * (Decimal(1) / (Decimal(3) * (Decimal(10) ** 18))) * (Decimal(1) - pi / Decimal(100)))


def gev_if_grams(digits: int = 120) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = digits
        mass_g = frozen_v1(digits)
        mass_kg = mass_g * Decimal("1e-3")
        e_charge = Decimal("1.602176634e-19")
        c = Decimal("299792458")
        kg_per_gev_c2 = (Decimal("1e9") * e_charge) / (c * c)
        return +(mass_kg / kg_per_gev_c2)


def main() -> None:
    print("Frozen V1 high precision =", frozen_v1())
    print("If unit=g, GeV/c^2 =", gev_if_grams())


if __name__ == "__main__":
    main()
