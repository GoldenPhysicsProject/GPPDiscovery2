#!/usr/bin/env python3
"""Exact pre-sewing Laurent-factorization audit at the generic nonzero-mu triple cut.

The collapsed two-particle sewing has a double pole at t = +/- i r because each
individual tree can carry the same extra p12 propagator.  The master-topology
information needed by generalized unitarity is therefore not just the residue of
one tree: the simple-pole coefficient of the sewn object depends on both the
factorwise residues and the factorwise finite parts.

For tree factors

    A = R_A/(t-t0) + F_A + O(t-t0),
    B = R_B/(t-t0) + F_B + O(t-t0),

we certify directly on the full generic massive-vector and extra-scalar trees that

    [AB]_{-2} = R_A R_B,
    [AB]_{-1} = R_A F_B + F_A R_B,

with matrix contraction in the vector sector.  This is the exact pre-sewing
interface required before feeding root data into the Badger subtraction/moment
machinery.  It also strengthens the earlier noninjectivity obstruction: a collapsed
Laurent coefficient does not by itself retain the split between residue and finite
part on the two tree factors.
"""
from __future__ import annotations

import sympy as sp

import massive_vector_generic_state_sum_symbolic as gen
import generic_presewing_vector_scalar_residue_audit as vra

r, t = gen.r, gen.t
I = sp.I


def exact_zero(expr) -> bool:
    return sp.factor(sp.cancel(sp.together(expr))) == 0


def finite_part(expr, res, root):
    """Finite Laurent coefficient after subtracting the certified simple pole."""
    reduced = sp.cancel(sp.together(expr - res / (t - root)))
    val = sp.factor(reduced.subs(t, root))
    if val.has(sp.zoo, sp.nan, sp.oo, -sp.oo):
        val = sp.factor(sp.limit(reduced, t, root))
    return val


def matrix_finite_part(M: sp.Matrix, R: sp.Matrix, root):
    return sp.Matrix([
        [finite_part(M[a, b], R[a, b], root) for b in range(M.cols)]
        for a in range(M.rows)
    ])


def direct_double(expr, root):
    reduced = sp.cancel(sp.together((t - root) ** 2 * expr))
    return sp.factor(reduced.subs(t, root))


def direct_simple(expr, root):
    return sp.factor(sp.residue(expr, t, root))


def audit_channel(h2: int, h3: int, root):
    # The opposite sewn factor uses the opposite external helicities, matching the
    # state-sum convention in massive_vector_generic_state_sum_symbolic.py.
    k2, k3 = -h2, -h3

    ML = gen.vector_tree_matrix(h2, h3)
    MR = gen.vector_tree_matrix(k2, k3)
    SL = gen.scalar_tree(h2, h3)
    SR = gen.scalar_tree(k2, k3)

    RML = vra.vector_residue_matrix(h2, h3, root)
    RMR = vra.vector_residue_matrix(k2, k3, root)
    RSL = vra.scalar_residue(h2, h3, root)
    RSR = vra.scalar_residue(k2, k3, root)

    FML = matrix_finite_part(ML, RML, root)
    FMR = matrix_finite_part(MR, RMR, root)
    FSL = finite_part(SL, RSL, root)
    FSR = finite_part(SR, RSR, root)

    Cv = gen.sew(ML, MR)
    Cs = sp.factor(SL * SR)

    vec_double_fact = gen.sew(RML, RMR)
    vec_simple_fact = sp.factor(gen.sew(RML, FMR) + gen.sew(FML, RMR))
    sca_double_fact = sp.factor(RSL * RSR)
    sca_simple_fact = sp.factor(RSL * FSR + FSL * RSR)

    vec_double_direct = direct_double(Cv, root)
    vec_simple_direct = direct_simple(Cv, root)
    sca_double_direct = direct_double(Cs, root)
    sca_simple_direct = direct_simple(Cs, root)

    assert exact_zero(vec_double_direct - vec_double_fact)
    assert exact_zero(vec_simple_direct - vec_simple_fact)
    assert exact_zero(sca_double_direct - sca_double_fact)
    assert exact_zero(sca_simple_direct - sca_simple_fact)

    ds4_double = sp.factor(vec_double_fact - sca_double_fact)
    ds4_simple = sp.factor(vec_simple_fact - sca_simple_fact)

    return {
        "vector_double": vec_double_fact,
        "vector_simple": vec_simple_fact,
        "scalar_double": sca_double_fact,
        "scalar_simple": sca_simple_fact,
        "ds4_double": ds4_double,
        "ds4_simple": ds4_simple,
    }


def main() -> None:
    roots = [("+", I * r), ("-", -I * r)]
    channels = [
        ("same--", -1, -1),
        ("mixed+-", +1, -1),
    ]

    results = {}
    for cname, h2, h3 in channels:
        for sname, root in roots:
            key = (cname, sname)
            results[key] = audit_channel(h2, h3, root)
            print(cname, "root", sname + "ir")
            for label, value in results[key].items():
                print(" ", label, "=", value)

    # Root-summed simple-pole data are the branch-free inputs relevant to the next
    # Badger-style moment/subtraction stage.  We record them exactly rather than
    # assigning a master topology prematurely.
    for cname, _, _ in channels:
        root_sum = sp.factor(
            results[(cname, "+")]["ds4_simple"]
            + results[(cname, "-")]["ds4_simple"]
        )
        print(cname, "Ds4 root-summed simple coefficient =", root_sum)

    print("PASS: full generic pre-sewing Laurent coefficients equal the factorwise residue/finite-part reconstruction")
    print("NEXT: apply the existing Badger root-moment/subtraction map to these branch-free pre-sewing data")


if __name__ == "__main__":
    main()
