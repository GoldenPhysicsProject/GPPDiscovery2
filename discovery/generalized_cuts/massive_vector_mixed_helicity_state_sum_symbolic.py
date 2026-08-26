#!/usr/bin/env python3
"""Exact symbolic mixed-helicity massive-vector state-sum audit.

This companion imports the convention-locked tree engine from
``massive_vector_mhv_state_sum_symbolic.py`` and evaluates the two massive-vector / two
gluon tree for opposite external helicities.  The same rational angular parameter ``t``
and symbolic centre-of-mass scale ``E`` are retained, so every assertion below is an
exact symbolic identity rather than a floating-point sample.

The result is qualitatively different from the same-helicity (--|++) channel:

* the extra-dimensional adjoint-scalar tree vanishes for (-+) and (+-);
* the massive-vector tree matrix is rank one and factorizes as ``2 w w^T``;
* its polarization vector obeys ``w^T w = 0`` and ``w^† w = 2``;
* sewing the conjugate mixed-helicity matrices therefore gives the angle-independent
  constant 16.

This isolates the state-algebra content relevant to the mixed-helicity two-particle cut
that can feed the s23 bubble.  It still does not fix coupling/color/cut-orientation/loop-
measure normalization or perform the higher-topology subtraction required for the actual
bubble coefficient.
"""

from __future__ import annotations

import sympy as sp

import massive_vector_mhv_state_sum_symbolic as base


def vector_tree_matrix(h3: int, h4: int) -> sp.Matrix:
    basis = [
        sp.Matrix([0, 1, 0, 0, 0]),
        sp.Matrix([0, 0, 1, 0, 0]),
        sp.Matrix([0, 0, 0, 1, 0]),
    ]
    ks = base.kinematics(5)
    e3 = base.gluon_helicity(3, h3, 5)
    e4 = base.gluon_helicity(4, h4, 5)
    return sp.Matrix([
        [sp.factor(base.amplitude(ks, [ea, eb, e3, e4])) for eb in basis]
        for ea in basis
    ])


def scalar_tree(h3: int, h4: int):
    ks = base.kinematics(6)
    e3 = base.gluon_helicity(3, h3, 6)
    e4 = base.gluon_helicity(4, h4, 6)
    scalar = sp.Matrix([0, 0, 0, 0, 0, 1])
    return sp.factor(base.amplitude(ks, [scalar, scalar, e3, e4]))


def frobenius_sew(A: sp.Matrix, B: sp.Matrix):
    return sp.factor(sum(A[a, b] * B[a, b] for a in range(3) for b in range(3)))


def simplify_matrix(M: sp.Matrix) -> sp.Matrix:
    return M.applyfunc(lambda z: sp.factor(sp.simplify(z)))


def main() -> None:
    Mmp = vector_tree_matrix(-1, +1)
    Mpm = vector_tree_matrix(+1, -1)
    Smp = scalar_tree(-1, +1)
    Spm = scalar_tree(+1, -1)

    assert sp.simplify(Smp) == 0
    assert sp.simplify(Spm) == 0

    # The two mixed-helicity matrices are related by complex conjugation for real t.
    assert Mpm == Mmp.conjugate()

    # Exact coherent-state/rank-one factorization of the (-,+) tree matrix.
    den = 1 + base.t**2
    w = sp.Matrix([
        -2 * sp.I * base.t / den,
        -sp.I * (base.t**2 - 1) / den,
        1,
    ])
    assert simplify_matrix(Mmp - 2 * w * w.T) == sp.zeros(3)
    assert sp.simplify((w.T * w)[0]) == 0
    assert sp.simplify((w.conjugate().T * w)[0] - 2) == 0

    Cv = frobenius_sew(Mmp, Mpm)
    Cs = sp.factor(Smp * Spm)
    assert sp.simplify(Cv - 16) == 0
    assert sp.simplify(Cs) == 0

    # Transposed sewing gives the same invariant in this convention.
    CvT = sp.factor(sum(Mmp[a, b] * Mpm[b, a]
                        for a in range(3) for b in range(3)))
    assert sp.simplify(CvT - 16) == 0

    # The factorization explains the constant without expanding the matrix entries:
    # Tr[(2ww^T)(2w*w†)] = 4 (w†w)^2 = 16.
    Cv_factorized = sp.simplify(4 * (w.conjugate().T * w)[0] ** 2)
    assert Cv_factorized == 16

    print("mixed-helicity scalar trees (-+),(+-) =", Smp, Spm)
    print("rank-one factorization M_-+ = 2 w w^T: PASS")
    print("w^T w =", sp.simplify((w.T * w)[0]))
    print("w^dagger w =", sp.simplify((w.conjugate().T * w)[0]))
    print("mixed-helicity vector sewing C^(V_m) =", Cv)
    print("mixed-helicity scalar sewing C^(S)   =", Cs)
    print("mixed-helicity transposed sewing     =", CvT)
    print("PASS: exact mixed-helicity state sum is 16, scalar subtraction is zero")


if __name__ == "__main__":
    main()
