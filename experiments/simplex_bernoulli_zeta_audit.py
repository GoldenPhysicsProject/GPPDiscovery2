#!/usr/bin/env python3
"""Exact audit of low-dimensional simplex volumes versus Bernoulli/zeta values.

Motivation: the raised-box rational term is -Vol(Delta_3) = -1/6, while
zeta(-1) = -1/12 and B_2 = 1/6.  This script checks whether that match
extends to a systematic dimension ladder or is only a low-order coincidence.

No physical identification is assumed.  All comparisons are exact SymPy
rational identities.
"""

from sympy import Rational, bernoulli, factorial, simplify, zeta


def simplex_volume(d: int):
    return Rational(1, factorial(d))


def main() -> None:
    print("d  Vol(Delta_d)       exact Bernoulli/zeta matches")
    print("-  -----------------  -----------------------------")
    for d in range(1, 16):
        vol = simplex_volume(d)
        matches = []
        for k in range(1, 10):
            B = simplify(bernoulli(2 * k))
            z = simplify(zeta(1 - 2 * k))
            if vol == abs(B):
                matches.append(f"|B_{2*k}|")
            if vol == abs(z):
                matches.append(f"|zeta({1-2*k})|")
        print(f"{d:2d} {str(vol):18s}  {', '.join(matches) if matches else '-'}")

    print("\nOdd-simplex comparison with zeta(1-2k):")
    print("k  d=2k+1  zeta(1-2k)        |zeta| / Vol(Delta_d)")
    print("-  ------  -----------------  -----------------------")
    for k in range(1, 8):
        d = 2 * k + 1
        z = simplify(zeta(1 - 2 * k))
        ratio = simplify(abs(z) / simplex_volume(d))
        print(f"{k:2d} {d:6d}  {str(z):18s}  {ratio}")

    assert simplex_volume(3) == abs(bernoulli(2))
    assert -simplex_volume(3) == 2 * zeta(-1)
    assert simplex_volume(5) == zeta(-3)

    print("\nCertified low-order identities:")
    print("  -Vol(Delta_3) = -1/6 = -B_2 = 2*zeta(-1)")
    print("   Vol(Delta_5) =  1/120 = zeta(-3)")
    print("\nThe pattern does NOT persist: e.g. |zeta(-5)| / Vol(Delta_7) = 20.")
    print("Therefore the raised-box -1/6 is not by itself evidence for a universal")
    print("simplex-dimension = negative-zeta-value rule.  A structural link, if any,")
    print("must come from an additional mechanism such as Euler-Maclaurin/Todd or")
    print("heat-kernel boundary coefficients, not equality of the raw sequences.")


if __name__ == "__main__":
    main()
