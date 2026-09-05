#!/usr/bin/env python3
"""Exact covariance of the massive-vector transverse residue on the full triple cut.

The full conic is a complex transverse rotation of the z=0 meridian point.  The
external gluon helicity vectors acquire only the already-certified little-group
phases.  Because the three-state massive basis closes under the same rotation, the
residue matrix in the fixed basis should transform by similarity after division by
the scalar residue.

This audit checks that statement directly against q A|_{q=0}.  It is pre-sewing
residue data, not a master-integral coefficient.
"""
from __future__ import annotations

import sympy as sp

import generic_full_chart_vector_scalar_tree_audit as full
import generic_full_chart_helicity_phase_audit as hel

r, u, v, z = full.r, full.u, full.v, full.z
I = sp.I
q = r**2 + u**2 + v**2

c = hel.c
s = hel.s
Q = sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])
conic_sub = hel.conic_sub
zero_sub = {u: I * r, v: 0}
lam = sp.symbols("lambda")


def transverse_vector_residue(h2: int, h3: int) -> sp.Matrix:
    M = full.vector_tree_matrix(h2, h3)
    return M.applyfunc(lambda x: sp.factor(sp.cancel((q * x).subs(conic_sub))))


def transverse_vector_residue_zero(h2: int, h3: int) -> sp.Matrix:
    M = full.vector_tree_matrix(h2, h3)
    return M.applyfunc(lambda x: sp.factor(sp.cancel((q * x).subs(zero_sub))))


def transverse_scalar_residue(h2: int, h3: int):
    A = full.scalar_tree(h2, h3)
    return sp.factor(sp.cancel((q * A).subs(conic_sub)))


def transverse_scalar_residue_zero(h2: int, h3: int):
    A = full.scalar_tree(h2, h3)
    return sp.factor(sp.cancel((q * A).subs(zero_sub)))


def main() -> None:
    assert sp.simplify(Q.T * Q - sp.eye(3)) == sp.zeros(3, 3)

    for h2, h3 in [(-1, -1), (+1, +1), (+1, -1), (-1, +1)]:
        phase = sp.factor(hel.phase(2, h2) * hel.phase(3, h3))
        Rz = transverse_vector_residue(h2, h3)
        R0 = transverse_vector_residue_zero(h2, h3)
        Sz = transverse_scalar_residue(h2, h3)
        S0 = transverse_scalar_residue_zero(h2, h3)

        # Scalar covariance is independently rechecked here so normalization is
        # not imported as an assumption from the helicity-phase audit.
        assert sp.simplify(Sz - phase * S0) == 0

        # Fixed-basis vector residue covariance.  Both massive external states are
        # rotated back to the meridian basis, producing Q M Q^T; Q^T=Q^-1.
        target = phase * Q * R0 * Q.T
        assert all(sp.simplify(sp.factor(Rz[i, j] - target[i, j])) == 0
                   for i in range(3) for j in range(3))

        Nz = Rz.applyfunc(lambda x: sp.factor(sp.cancel(x / Sz)))
        N0 = R0.applyfunc(lambda x: sp.factor(sp.cancel(x / S0)))
        assert all(sp.simplify(sp.factor(Nz[i, j] - (Q * N0 * Q.T)[i, j])) == 0
                   for i in range(3) for j in range(3))

        cpz = sp.factor(Nz.charpoly(lam).as_expr())
        if h2 == h3:
            expected = sp.factor((lam + 1) * (lam + r**2) * (lam * r**2 + 1) / r**2)
        else:
            expected = sp.factor((lam - 1)**2 * (lam + 1))
        assert sp.simplify(cpz - expected) == 0
        assert sp.simplify(Rz.det() + Sz**3) == 0

    print("PASS: full-conic massive-vector residue obeys exact phase-times-similarity covariance")
    print("normalized same-helicity spectrum = {-1, -r^2, -r^-2} for every z")
    print("normalized mixed-helicity spectrum = {+1, +1, -1} for every z")
    print("det(vector residue) = - scalar_residue^3 on the entire triple-cut conic")
    print("NEXT: construct the opposite-tree contraction/state sum on the full conic and perform the legitimate large-z Badger projection")


if __name__ == "__main__":
    main()
