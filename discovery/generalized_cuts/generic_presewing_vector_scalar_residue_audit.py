#!/usr/bin/env python3
"""Exact vector/scalar numerator residues on the generic nonzero-mu triple cut.

For the generic color ordering (massive, gluon, gluon, massive), the only singular
piece at t = +/- i r is the p12 cubic channel.  This audit evaluates that channel's
numerator before sewing, multiplies by the already-derived propagator Jacobian, and
records exact residue matrices for the three physical massive-vector states and the
extra scalar state.

A useful invariant emerges after normalizing the vector residue matrix by the scalar
residue: mixed-helicity residues have r-independent characteristic polynomial
(lambda-1)^2(lambda+1), while same-helicity residues have spectrum
{-1,-r^2,-r^-2}.  These are pre-sewing residue invariants; they are not yet master-
integral coefficients.
"""
from __future__ import annotations

import sympy as sp

import massive_vector_generic_state_sum_symbolic as gen
import massive_vector_mhv_state_sum_symbolic as base

E, r, t = gen.E, gen.r, gen.t
I = sp.I


def p12_numerator(ks, eps):
    d = len(ks[0])
    g = base.metric(d)
    e1, e2, e3, e4 = [g * e for e in eps]
    k1, k2, k3, k4 = ks
    p12 = k1 + k2
    return sp.factor(base.contract_12_34(
        e1, e2, base.v3(g, k1, k2, -p12), g,
        base.v3(g, p12, k3, k4), e3, e4,
    ))


def vector_numerator_matrix(h2: int, h3: int):
    ks = gen.generic_kinematics(5)
    e2 = gen.gluon_pol(2, h2, 5)
    e3 = gen.gluon_pol(3, h3, 5)
    basis = gen.massive_basis()
    return sp.Matrix([
        [p12_numerator(ks, [ea, e2, e3, eb]) for eb in basis]
        for ea in basis
    ])


def scalar_numerator(h2: int, h3: int):
    ks = gen.generic_kinematics(6)
    e2 = gen.gluon_pol(2, h2, 6)
    e3 = gen.gluon_pol(3, h3, 6)
    scalar = sp.Matrix([0, 0, 0, 0, 0, 1])
    return p12_numerator(ks, [scalar, e2, e3, scalar])


root_plus = I * r
root_minus = -I * r
prop_res_plus = I * (1 - r**4) / (8 * r * E**2)
prop_res_minus = -prop_res_plus


def residue_matrix(h2: int, h3: int, root, prop_res):
    N = vector_numerator_matrix(h2, h3)
    return N.applyfunc(lambda z: sp.factor(sp.simplify(z.subs(t, root) * prop_res)))


def scalar_residue(h2: int, h3: int, root, prop_res):
    return sp.factor(sp.simplify(scalar_numerator(h2, h3).subs(t, root) * prop_res))


scalar_target_plus = I * r * (r**2 - 1) / (r**2 + 1)
scalar_target_minus = -scalar_target_plus

for hs in [(-1, -1), (+1, +1), (+1, -1), (-1, +1)]:
    Rp = residue_matrix(*hs, root_plus, prop_res_plus)
    Rm = residue_matrix(*hs, root_minus, prop_res_minus)
    Sp = scalar_residue(*hs, root_plus, prop_res_plus)
    Sm = scalar_residue(*hs, root_minus, prop_res_minus)

    assert sp.simplify(Sp - scalar_target_plus) == 0
    assert sp.simplify(Sm - scalar_target_minus) == 0
    assert sp.simplify(Sp + Sm) == 0

    # The vector determinant is universally minus the cube of the scalar residue.
    assert sp.simplify(Rp.det() + Sp**3) == 0
    assert sp.simplify(Rm.det() + Sm**3) == 0

    Np = Rp.applyfunc(lambda z: sp.factor(sp.simplify(z / Sp)))
    Nm = Rm.applyfunc(lambda z: sp.factor(sp.simplify(z / Sm)))
    lam = sp.symbols("lambda")
    cp = sp.factor(Np.charpoly(lam).as_expr())
    cm = sp.factor(Nm.charpoly(lam).as_expr())

    if hs[0] == hs[1]:
        target = sp.factor((lam + 1) * (lam + r**2) * (lam * r**2 + 1) / r**2)
    else:
        target = (lam - 1)**2 * (lam + 1)
    assert sp.simplify(cp - target) == 0
    assert sp.simplify(cm - target) == 0

print("scalar residue at +ir =", scalar_target_plus)
print("scalar residue at -ir =", scalar_target_minus)
print("same-helicity normalized vector spectrum: {-1, -r^2, -r^-2}")
print("mixed-helicity normalized vector spectrum: {+1, +1, -1}")
print("det(vector residue) = - scalar_residue^3 in every helicity channel")
print("PASS: generic pre-sewing vector/scalar triple-cut residues are exact")
print("NEXT: contract the appropriate opposite-side tree data at each root and feed the two-root result into the Badger subtraction/moment map")
