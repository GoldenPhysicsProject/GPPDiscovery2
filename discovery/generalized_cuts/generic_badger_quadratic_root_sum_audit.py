#!/usr/bin/env python3
"""Branch-free symmetric root sums for generic quadratic Badger subtraction poles.

A generic topology-subtraction pole on a one-complex-parameter cut often appears as

    q(y) = A y^2 + B y + C,

with two roots y_+, y_-.  Individual roots introduce sqrt(B^2-4AC), but Badger-style
subtraction formulas require sums over both pole locations.  Those symmetric sums can
be reconstructed rationally from A,B,C, without ever choosing a square-root branch.

This audit proves the Newton recurrences for positive and negative powers, checks the
explicit moments through cubic order (the range needed by the first T1/T2/T3 Laurent
moments), and verifies a generic Laurent-polynomial root sum against the explicit
quadratic roots.  It is infrastructure only: no box/triangle/bubble master coefficient
is claimed until the topology-specific subtraction and normalization map is inserted.
"""
from __future__ import annotations

import sympy as sp

A, B, C = sp.symbols("A B C", nonzero=True)


def power_sums(sum_roots, product_roots, nmax: int):
    """Return P_n=r1^n+r2^n from P_0=2, P_1=r1+r2 and Newton recurrence."""
    out = [sp.Integer(2), sp.factor(sum_roots)]
    for _n in range(2, nmax + 1):
        out.append(sp.factor(sum_roots * out[-1] - product_roots * out[-2]))
    return out


def main() -> None:
    # Vieta data for q(y)=A y^2+B y+C.
    sigma1 = -B / A
    sigma2 = C / A

    # Reciprocal roots obey C z^2+B z+A=0.
    tau1 = -B / C
    tau2 = A / C

    P = power_sums(sigma1, sigma2, 6)
    Q = power_sums(tau1, tau2, 6)

    # Explicit branch-free moments through cubic order.
    assert sp.factor(P[1] + B / A) == 0
    assert sp.factor(P[2] - (B**2 - 2 * A * C) / A**2) == 0
    assert sp.factor(P[3] - (-B**3 + 3 * A * B * C) / A**3) == 0

    assert sp.factor(Q[1] + B / C) == 0
    assert sp.factor(Q[2] - (B**2 - 2 * A * C) / C**2) == 0
    assert sp.factor(Q[3] - (-B**3 + 3 * A * B * C) / C**3) == 0

    # Direct comparison with explicit quadratic roots.  The discriminant disappears
    # from every symmetric sum, proving branch independence rather than assuming it.
    disc = B**2 - 4 * A * C
    yp = (-B + sp.sqrt(disc)) / (2 * A)
    ym = (-B - sp.sqrt(disc)) / (2 * A)
    for n in range(0, 7):
        assert sp.simplify(sp.together(P[n] - (yp**n + ym**n))) == 0
    for n in range(1, 7):
        assert sp.simplify(sp.together(Q[n] - (yp**(-n) + ym**(-n)))) == 0

    # Generic Laurent data through |k|<=3, sufficient for the first three symmetric
    # positive/negative moments.  This is the object that can be fed into a later
    # topology-specific T1/T2/T3 subtraction map without solving for either root.
    am3, am2, am1, a0, a1, a2, a3 = sp.symbols(
        "a_m3 a_m2 a_m1 a0 a1 a2 a3"
    )

    def L(y):
        return (
            am3 * y**-3 + am2 * y**-2 + am1 * y**-1 + a0
            + a1 * y + a2 * y**2 + a3 * y**3
        )

    branch_free = sp.factor(
        am3 * Q[3] + am2 * Q[2] + am1 * Q[1] + 2 * a0
        + a1 * P[1] + a2 * P[2] + a3 * P[3]
    )
    explicit = sp.together(L(yp) + L(ym))
    assert sp.simplify(sp.together(explicit - branch_free)) == 0

    # Recheck the recurrence itself symbolically through a higher order than needed
    # for T1/T2/T3 so later extensions do not rely on the displayed low-order forms.
    for n in range(2, 7):
        assert sp.factor(P[n] - sigma1 * P[n - 1] + sigma2 * P[n - 2]) == 0
        assert sp.factor(Q[n] - tau1 * Q[n - 1] + tau2 * Q[n - 2]) == 0

    print("P1 =", P[1])
    print("P2 =", P[2])
    print("P3 =", P[3])
    print("Q1 =", Q[1])
    print("Q2 =", Q[2])
    print("Q3 =", Q[3])
    print("branch-free Laurent root sum =", branch_free)
    print("PASS: quadratic Badger root sums are rational in A,B,C and branch-independent")
    print("NEXT: insert the topology-specific pole polynomial and T1/T2/T3 subtraction weights")


if __name__ == "__main__":
    main()
