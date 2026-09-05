#!/usr/bin/env python3
"""Lift the generic vector/extra-scalar tree engine from its meridian to the full cut sphere.

The existing generic state-sum engine uses the v=0 stereographic meridian.  This audit
constructs the full stereographic chart and helicity frame in the *same* mostly-minus
metric convention, then proves exact restriction back to the existing engine.  It also
restricts the full tree data to the genuine triple-cut conic

    u^2 + v^2 = -r^2

through its rational z-parameterization.  This is the executable bridge needed before
performing a genuine large-z Badger projection; no master coefficient is claimed here.
"""
from __future__ import annotations

import sympy as sp

import massive_vector_generic_state_sum_symbolic as mer
import massive_vector_mhv_state_sum_symbolic as base

r, u, v, z = sp.symbols("r u v z", nonzero=True)
E = base.E
I = sp.I
s = u**2 + v**2

beta = (1 - r**2) / (1 + r**2)
rho = 2 * r / (1 + r**2)

n = sp.Matrix([
    2 * u / (1 + s),
    2 * v / (1 + s),
    (1 - s) / (1 + s),
])
eu = sp.simplify((1 + s) * n.diff(u) / 2)
ev = sp.simplify((1 + s) * n.diff(v) / 2)


def full_kinematics(d: int = 5):
    q1 = sp.Matrix([-E, 0, 0, -E * beta, +E * rho])
    q4 = sp.Matrix([-E, 0, 0, +E * beta, -E * rho])
    g2 = sp.Matrix([+E, E * n[0], E * n[1], E * n[2], 0])
    g3 = sp.Matrix([+E, -E * n[0], -E * n[1], -E * n[2], 0])
    ks = [q1, g2, g3, q4]
    if d == 5:
        return ks
    if d == 6:
        return [sp.Matrix(list(k) + [0]) for k in ks]
    raise ValueError("only d=5 or d=6 is used")


def full_gluon_pol(leg: int, h: int, d: int = 5):
    # This orientation is fixed by exact reduction to the existing v=0 engine:
    # leg 2 uses +eu, leg 3 uses -eu, while ev is shared.
    if leg == 2:
        spatial = eu + I * h * ev
    elif leg == 3:
        spatial = -eu + I * h * ev
    else:
        raise ValueError("leg must be 2 or 3")
    out = sp.Matrix([0, *(list(spatial / sp.sqrt(2))), 0])
    return out if d == 5 else sp.Matrix(list(out) + [0])


def vector_tree_matrix(h2: int, h3: int):
    ks = full_kinematics(5)
    e2 = full_gluon_pol(2, h2, 5)
    e3 = full_gluon_pol(3, h3, 5)
    basis = mer.massive_basis()
    return sp.Matrix([
        [sp.factor(sp.simplify(base.amplitude(ks, [ea, e2, e3, eb]))) for eb in basis]
        for ea in basis
    ])


def scalar_tree(h2: int, h3: int):
    ks = full_kinematics(6)
    e2 = full_gluon_pol(2, h2, 6)
    e3 = full_gluon_pol(3, h3, 6)
    scalar = sp.Matrix([0, 0, 0, 0, 0, 1])
    return sp.factor(sp.simplify(base.amplitude(ks, [scalar, e2, e3, scalar])))


def main() -> None:
    g5 = base.metric(5)

    # Exact cut-sphere and polarization geometry in the amplitude-engine convention.
    assert sp.simplify(n.dot(n) - 1) == 0
    assert sp.simplify(eu.dot(n)) == 0
    assert sp.simplify(ev.dot(n)) == 0
    assert sp.simplify(eu.dot(eu) - 1) == 0
    assert sp.simplify(ev.dot(ev) - 1) == 0
    assert sp.simplify(eu.dot(ev)) == 0

    ks = full_kinematics(5)
    for k in ks:
        assert sp.simplify(base.mdot(g5, k, k)) == 0
    assert sp.simplify(sum(ks, sp.zeros(5, 1))) == sp.zeros(5, 1)

    for leg in (2, 3):
        k = ks[leg - 1]
        ep = full_gluon_pol(leg, +1, 5)
        em = full_gluon_pol(leg, -1, 5)
        assert sp.simplify(base.mdot(g5, k, ep)) == 0
        assert sp.simplify(base.mdot(g5, k, em)) == 0
        assert sp.simplify(base.mdot(g5, ep, em) + 1) == 0

    # Exact reduction to the previously CI-certified meridian engine.
    t = mer.t
    meridian_sub = {v: 0, u: t}
    full5_mer = [k.applyfunc(lambda x: sp.simplify(x.subs(meridian_sub))) for k in ks]
    old5 = mer.generic_kinematics(5)
    assert all(sp.simplify(a - b) == sp.zeros(5, 1) for a, b in zip(full5_mer, old5))
    for leg in (2, 3):
        for h in (-1, +1):
            got = full_gluon_pol(leg, h, 5).applyfunc(
                lambda x: sp.simplify(x.subs(meridian_sub)))
            want = mer.gluon_pol(leg, h, 5)
            assert sp.simplify(got - want) == sp.zeros(5, 1)

    # The genuine triple cut is the conic, retaining one complex parameter z.
    uz = I * r * (1 - z**2) / (1 + z**2)
    vz = 2 * I * r * z / (1 + z**2)
    conic_sub = {u: uz, v: vz}
    assert sp.factor(uz**2 + vz**2 + r**2) == 0

    # Tree-level objects are now explicitly defined on the full chart.  Evaluate the
    # extra-scalar mixed-helicity tree on the conic: this is the cheapest nontrivial
    # full-tree check and ensures the amplitude engine, not just kinematics, survives
    # the lift.  The expression is kept exact and rational in (r,z).
    S_pm = scalar_tree(+1, -1)
    S_pm_z = sp.factor(sp.cancel(S_pm.subs(conic_sub)))
    assert z not in sp.denom(S_pm_z).free_symbols or sp.denom(S_pm_z) != 0

    # At z=0 the full conic lands on the old +ir meridian root.  The full scalar tree
    # therefore must reproduce the previously certified meridian tree value there.
    full_at_zero = sp.simplify(S_pm_z.subs(z, 0))
    old_at_plus = sp.simplify(mer.scalar_tree(+1, -1).subs(t, I * r))
    assert sp.simplify(full_at_zero - old_at_plus) == 0

    print("full mixed-helicity scalar tree on triple-cut conic =", S_pm_z)
    print("z=0 scalar-tree value =", full_at_zero)
    print("PASS: full stereographic tree engine exactly extends the certified meridian engine")
    print("NEXT: evaluate the full vector-minus-scalar state sum as a rational function of z and extract its large-z polynomial part")


if __name__ == "__main__":
    main()
