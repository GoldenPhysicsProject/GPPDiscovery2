#!/usr/bin/env python3
"""Extract exact generic nonzero-mu Ds=4 Yang-Mills sewing baselines.

Uses the convention-locked generic massive-vector tree engine.  The reconstruction
identity is C^(4)=C^(V_m)-C^(S), with vector and scalar sewings evaluated at the
same generic rational kinematics.  This script prints exact factorizations and
checks the threshold r=1 regression without making any box-only claim.

The same-helicity channel admits the exact decomposition

    C^(4)_same = 2 C^(S)_same + D,

where

    D = 4 (r^2-1)^2 (1+t^2)^2 / (r^2+t^2)^2.

Thus the threshold state-count relation is the D=0 slice of a generic rational
identity, rather than a generic 3:1 vector/scalar rule.
"""
from __future__ import annotations
import sympy as sp
import massive_vector_generic_state_sum_symbolic as g


def main() -> None:
    # Exact massive-cut rational parametrization: beta=|p|/E, rho=mu/E.
    assert sp.simplify(g.beta**2 + g.rho**2 - 1) == 0

    Mmm = g.vector_tree_matrix(-1, -1)
    Mpp = g.vector_tree_matrix(+1, +1)
    Smm = g.scalar_tree(-1, -1)
    Spp = g.scalar_tree(+1, +1)
    Cv_same = g.sew(Mmm, Mpp)
    Cs_same = sp.factor(Smm * Spp)
    C4_same = sp.factor(sp.cancel(Cv_same - Cs_same))

    Mpm = g.vector_tree_matrix(+1, -1)
    Mmp = g.vector_tree_matrix(-1, +1)
    Spm = g.scalar_tree(+1, -1)
    Smp = g.scalar_tree(-1, +1)
    Cv_mixed = g.sew(Mpm, Mmp)
    Cs_mixed = sp.factor(Spm * Smp)
    C4_mixed = sp.factor(sp.cancel(Cv_mixed - Cs_mixed))

    same_defect = sp.factor(
        4 * (g.r**2 - 1)**2 * (g.t**2 + 1)**2 / (g.r**2 + g.t**2)**2
    )

    # Exact reconstruction and generic same-helicity decomposition.
    assert sp.simplify(C4_same - (Cv_same - Cs_same)) == 0
    assert sp.simplify(C4_mixed - (Cv_mixed - Cs_mixed)) == 0
    assert sp.simplify((Cv_same - 3 * Cs_same) - same_defect) == 0
    assert sp.simplify(C4_same - (2 * Cs_same + same_defect)) == 0

    # Known threshold regression.  The defect and mixed scalar vanish there.
    assert sp.simplify((Cv_same - 3 * Cs_same).subs(g.r, 1)) == 0
    assert sp.simplify(same_defect.subs(g.r, 1)) == 0
    assert sp.simplify(Cv_mixed.subs(g.r, 1) - 16) == 0
    assert sp.simplify(Cs_mixed.subs(g.r, 1)) == 0
    assert sp.simplify(C4_mixed.subs(g.r, 1) - 16) == 0
    assert sp.simplify(
        C4_same.subs(g.r, 1) - 2 * Cs_same.subs(g.r, 1)
    ) == 0

    print("beta^2+rho^2 =", sp.simplify(g.beta**2 + g.rho**2))
    print("Cv_same =", sp.factor(Cv_same))
    print("Cs_same =", sp.factor(Cs_same))
    print("same defect Cv_same-3 Cs_same =", same_defect)
    print("C4_same = Cv_same-Cs_same =", C4_same)
    print("C4_same-(2 Cs_same) =", sp.factor(C4_same - 2 * Cs_same))
    print("Cv_mixed =", sp.factor(Cv_mixed))
    print("Cs_mixed =", sp.factor(Cs_mixed))
    print("C4_mixed = Cv_mixed-Cs_mixed =", C4_mixed)
    print("threshold C4_same =", sp.factor(C4_same.subs(g.r, 1)))
    print("threshold C4_mixed =", sp.factor(C4_mixed.subs(g.r, 1)))
    print("PASS: exact generic Ds=4 massive-vector-minus-scalar extraction")


if __name__ == "__main__":
    main()
