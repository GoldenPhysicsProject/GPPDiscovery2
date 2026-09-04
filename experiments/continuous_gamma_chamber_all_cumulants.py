#!/usr/bin/env python3
"""Exact all-even cumulants for the continuous Gamma/Wiener–Hopf chamber family.

For rho_c with characteristic function phi_c(t) = sech(t/2)^(2c),

    log phi_c(t) = -2 c log cosh(t/2).

Using the Bernoulli expansion of log cosh, the even cumulants are

    kappa_{2n}(c) = c (2^(2n)-1) |B_{2n}| / n,

and all odd cumulants vanish.  This script verifies the first values exactly
with rational arithmetic and checks additivity in the chamber parameter.
"""

from fractions import Fraction
from math import comb


def bernoulli_numbers(nmax: int):
    """Return B_0,...,B_nmax using the standard recurrence exactly."""
    B = [Fraction(0) for _ in range(nmax + 1)]
    B[0] = Fraction(1)
    for m in range(1, nmax + 1):
        total = sum(Fraction(comb(m + 1, k)) * B[k] for k in range(m))
        B[m] = -total / Fraction(m + 1)
    return B


def even_cumulant_coefficient(n: int) -> Fraction:
    """Return kappa_{2n}(c)/c exactly."""
    B = bernoulli_numbers(2 * n)[2 * n]
    return Fraction(2 ** (2 * n) - 1, n) * abs(B)


def main() -> None:
    expected = {
        1: Fraction(1, 2),
        2: Fraction(1, 4),
        3: Fraction(1, 2),
        4: Fraction(17, 8),
        5: Fraction(31, 2),
        6: Fraction(691, 4),
    }

    print("n  kappa_(2n)(c)/c")
    for n in range(1, 7):
        got = even_cumulant_coefficient(n)
        print(f"{n}  {got}")
        assert got == expected[n], (n, got, expected[n])

    # Exact chamber additivity: kappa_{2n}(c+d) = kappa_{2n}(c)+kappa_{2n}(d).
    c = Fraction(37, 100)
    d = Fraction(83, 100)
    for n in range(1, 7):
        a = even_cumulant_coefficient(n)
        assert a * (c + d) == a * c + a * d

    print("all exact cumulant and additivity checks passed")


if __name__ == "__main__":
    main()
