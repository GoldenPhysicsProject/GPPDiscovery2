#!/usr/bin/env python3
"""Audit the post-resonance critical-half-density decay margins.

This is a structural arithmetic audit only.  It makes no RH, positivity, or
spectral-completion claim.

Smooth Möbius channel n has exponent e_n = 1/n - 3/2.
Prime-repetition channel m has exponent r_m = -m/2.
For n,m >= 3 the worst cases occur at n=m=3, giving the uniform bounds
    e_n <= -7/6,
    r_m <= -3/2.
Hence all higher channels lie strictly beyond the x^{-1} logarithmic threshold,
with margins at least 1/6 and 1/2 respectively.
"""
from fractions import Fraction


def mobius_exponent(n: int) -> Fraction:
    return Fraction(1, n) - Fraction(3, 2)


def repetition_exponent(m: int) -> Fraction:
    return -Fraction(m, 2)


def main() -> None:
    assert mobius_exponent(1) == Fraction(-1, 2)
    assert mobius_exponent(2) == Fraction(-1, 1)
    assert repetition_exponent(1) == Fraction(-1, 2)
    assert repetition_exponent(2) == Fraction(-1, 1)

    smooth_bound = Fraction(-7, 6)
    repetition_bound = Fraction(-3, 2)

    for n in range(3, 10001):
        assert mobius_exponent(n) <= smooth_bound < -1
    for m in range(3, 10001):
        assert repetition_exponent(m) <= repetition_bound < -1

    print("critical channels:")
    print("  n=1 smooth =", mobius_exponent(1), " m=1 repeat =", repetition_exponent(1))
    print("  n=2 smooth =", mobius_exponent(2), " m=2 repeat =", repetition_exponent(2))
    print("post-resonance uniform bounds:")
    print("  n>=3: e_n <=", smooth_bound, "integrability margin >=", -1 - smooth_bound)
    print("  m>=3: r_m <=", repetition_bound, "integrability margin >=", -1 - repetition_bound)
    print("audit: PASS")


if __name__ == "__main__":
    main()
