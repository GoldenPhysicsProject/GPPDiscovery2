#!/usr/bin/env python3
"""Exact paired-residue sewing invariant on the full generic triple-cut conic.

This specializes the already-certified phase-times-orthogonal covariance

    R_h(z) = p_h(z) Q(z) R_h(0) Q(z)^T

to the complementary helicity pairs that occur in the existing generic state-sum
audits.  It proves that their little-group phase products are exactly one, so the
Frobenius contraction of the corresponding *already-built residue families* is
independent of the conic coordinate z.

This remains pre-physical-sewing information.  The opposite tree/crossing map has not
been constructed here, so no D_s=4 master coefficient or Badger coefficient is
claimed.  The result instead isolates where nontrivial z dependence can still enter:
through the opposite-tree kinematics/crossing and higher-topology subtraction, not
through the common transverse rotation of the known residue family.
"""
from __future__ import annotations

import sympy as sp

z = sp.symbols("z")
I = sp.I

c = (1 - z**2) / (1 + z**2)
s = 2 * z / (1 + z**2)
Q = sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])

A = sp.Matrix(3, 3, lambda i, j: sp.symbols(f"a{i}{j}"))
B = sp.Matrix(3, 3, lambda i, j: sp.symbols(f"b{i}{j}"))


def phase(leg: int, h: int):
    if leg == 2:
        return -(z - I * h) / (z + I * h)
    if leg == 3:
        return -(z + I * h) / (z - I * h)
    raise ValueError("leg must be 2 or 3")


def channel_phase(h2: int, h3: int):
    return sp.factor(phase(2, h2) * phase(3, h3))


def sew(X: sp.Matrix, Y: sp.Matrix):
    return sp.expand(sum(X[i, j] * Y[i, j] for i in range(3) for j in range(3)))


def check_pair(hA, hB):
    pA = channel_phase(*hA)
    pB = channel_phase(*hB)
    assert sp.factor(sp.cancel(pA * pB - 1)) == 0

    Az = pA * Q * A * Q.T
    Bz = pB * Q * B * Q.T
    assert sp.factor(sp.cancel(sew(Az, Bz) - sew(A, B))) == 0
    return pA, pB


def main() -> None:
    assert sp.simplify(Q.T * Q - sp.eye(3)) == sp.zeros(3, 3)

    pmm, ppp = check_pair((-1, -1), (+1, +1))
    ppm, pmp = check_pair((+1, -1), (-1, +1))

    assert sp.simplify(pmm - 1) == 0
    assert sp.simplify(ppp - 1) == 0
    assert sp.simplify(ppm - ((z - I) / (z + I))**2) == 0
    assert sp.simplify(pmp - ((z + I) / (z - I))**2) == 0

    print("same-helicity complementary phases:", pmm, ppp)
    print("mixed complementary phases:", ppm, pmp)
    print("PASS: complementary-helicity phase products are exactly one")
    print("PASS: their known full-conic residue Frobenius contractions are z-independent")
    print("BOUNDARY: this does not identify the unbuilt opposite physical tree with either paired residue family")
    print("NEXT: construct the opposite-tree crossing map explicitly, then test whether its sewn C^(V_m)-C^(S) inherits or breaks this z-independence before Badger projection")


if __name__ == "__main__":
    main()
