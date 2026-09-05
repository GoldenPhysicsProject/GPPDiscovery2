#!/usr/bin/env python3
"""Exact covariance of the massive-vector transverse residue on the full triple cut.

The full conic is a complex transverse rotation of the z=0 meridian point.  The
external gluon helicity vectors acquire only the already-certified little-group
phases.  Because the three-state massive basis closes under the same rotation, the
residue matrix in the fixed basis should transform by similarity after division by
the scalar residue.

This audit checks that statement directly against q A|_{q=0}.  It is pre-sewing
residue data, not a master-integral coefficient.

Implementation note: the previous version redundantly rebuilt the full tree matrix at
z=0 and then separately recomputed normalized covariance, characteristic polynomials,
and determinants.  That exact SymPy job was cancelled after ~19 minutes.  Here each
helicity channel constructs the tree only once; R(0) is obtained from R(z) by z=0.
Once phase-times-similarity covariance is established, normalized similarity,
characteristic-polynomial invariance, and determinant covariance are algebraic
consequences, so they are not re-expanded through the expensive tree expressions.
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


def transverse_vector_residue(h2: int, h3: int) -> sp.Matrix:
    M = full.vector_tree_matrix(h2, h3)
    return M.applyfunc(lambda x: sp.factor(sp.cancel((q * x).subs(conic_sub))))


def transverse_scalar_residue(h2: int, h3: int):
    A = full.scalar_tree(h2, h3)
    return sp.factor(sp.cancel((q * A).subs(conic_sub)))


def exact_zero(x) -> bool:
    """Cheap rational normalization first; fall back to simplify only if needed."""
    y = sp.cancel(x)
    if y == 0:
        return True
    return sp.simplify(y) == 0


def main() -> None:
    assert sp.simplify(Q.T * Q - sp.eye(3)) == sp.zeros(3, 3)

    for h2, h3 in [(-1, -1), (+1, +1), (+1, -1), (-1, +1)]:
        phase = sp.factor(hel.phase(2, h2) * hel.phase(3, h3))
        Rz = transverse_vector_residue(h2, h3)
        # Do not rebuild the amplitude at the meridian point: R0 is the z=0 member
        # of the already-computed full-conic residue family.
        R0 = Rz.applyfunc(lambda x: sp.factor(sp.cancel(x.subs(z, 0))))
        Sz = transverse_scalar_residue(h2, h3)
        S0 = sp.factor(sp.cancel(Sz.subs(z, 0)))

        # Scalar covariance is independently rechecked here so normalization is
        # not imported as an assumption from the helicity-phase audit.
        assert exact_zero(Sz - phase * S0)

        # Fixed-basis vector residue covariance.  Both massive external states are
        # rotated back to the meridian basis, producing Q M Q^T; Q^T=Q^-1.
        target = phase * Q * R0 * Q.T
        for i in range(3):
            for j in range(3):
                assert exact_zero(Rz[i, j] - target[i, j])

    print("PASS: full-conic massive-vector residue obeys exact phase-times-similarity covariance")
    print("Since scalar residue carries the same phase, R_V(z)/S(z) is similar to R_V(0)/S(0).")
    print("Therefore the already-certified meridian characteristic polynomials and determinant identity hold for every z:")
    print("  same helicity spectrum = {-1, -r^2, -r^-2}")
    print("  mixed helicity spectrum = {+1, +1, -1}")
    print("  det(vector residue) = - scalar_residue^3")
    print("NEXT: construct the opposite-tree contraction/state sum on the full conic and perform the legitimate large-z Badger projection")


if __name__ == "__main__":
    main()
