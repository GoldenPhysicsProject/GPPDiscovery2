#!/usr/bin/env python3
"""Exact algebraic sewing consequence of the certified full-conic residue covariance.

The generic massive-vector state sum uses the Frobenius contraction

    sew(A,B) = sum_{a,b} A[a,b] B[a,b] = tr(A^T B).

The full-conic residue audit proves fixed-basis covariance of each residue matrix in
the form

    A(z) = p_A(z) Q(z) A(0) Q(z)^T,

with complex-orthogonal Q, Q^T Q = I.  This file proves, independently of any tree
formula, the exact consequence

    sew(A(z),B(z)) = p_A(z) p_B(z) sew(A(0),B(0)).

This is a structural reduction only.  It does NOT assert that the still-unbuilt
opposite tree has the same Q/p covariance; that must be checked directly before this
identity is used for the physical D_s=4 triple-cut sewing or Badger projection.
"""
from __future__ import annotations

import sympy as sp

z = sp.symbols("z")

c = (1 - z**2) / (1 + z**2)
s = 2 * z / (1 + z**2)
Q = sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])

A = sp.Matrix(3, 3, lambda i, j: sp.symbols(f"a{i}{j}"))
B = sp.Matrix(3, 3, lambda i, j: sp.symbols(f"b{i}{j}"))
pA, pB = sp.symbols("pA pB")


def sew(X: sp.Matrix, Y: sp.Matrix):
    return sp.expand(sum(X[i, j] * Y[i, j] for i in range(3) for j in range(3)))


def main() -> None:
    assert sp.simplify(Q.T * Q - sp.eye(3)) == sp.zeros(3, 3)
    Az = pA * Q * A * Q.T
    Bz = pB * Q * B * Q.T

    # Frobenius contraction is invariant under simultaneous orthogonal congruence.
    lhs = sew(Az, Bz)
    rhs = pA * pB * sew(A, B)
    assert sp.factor(sp.cancel(lhs - rhs)) == 0

    # Equivalent trace formulation, useful for later symbolic tree contractions.
    assert sp.expand(sew(A, B) - sp.trace(A.T * B)) == 0

    print("PASS: sew(Q A Q^T, Q B Q^T) = sew(A,B) for the full-conic Q(z)")
    print("PASS: phase-times-congruence residues sew with only the product phase p_A p_B")
    print("BOUNDARY: opposite-tree covariance has not yet been proved; no physical master coefficient is claimed")
    print("NEXT: construct the opposite tree on the same conic, prove/falsify its Q/p covariance, then evaluate C^(4)=C^(V_m)-C^(S) and Badger-project it")


if __name__ == "__main__":
    main()
