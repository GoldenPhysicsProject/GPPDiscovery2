#!/usr/bin/env python3
"""Lift the generic vector/extra-scalar tree engine from its meridian to the full cut sphere.

The existing generic state-sum engine uses the v=0 stereographic meridian.  This audit
constructs the full stereographic chart and helicity frame in the *same* mostly-minus
metric convention, proves exact restriction back to the existing engine, and then
restricts the *residue-level* tree data to the genuine triple-cut conic

    u^2 + v^2 = -r^2.

The raw tree has the expected third-propagator pole there, so the correct object is
q A with q := r^2+u^2+v^2, followed by q=0.  No master coefficient is claimed here.
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
    # Orientation fixed by exact reduction to the existing v=0 engine.
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
    q = r**2 + u**2 + v**2
    assert sp.factor(uz**2 + vz**2 + r**2) == 0

    # The raw tree diverges on q=0.  Extract its transverse residue first.
    S_pm = scalar_tree(+1, -1)
    transverse_scalar = sp.factor(sp.cancel(q * S_pm))
    Sres_z = sp.factor(sp.cancel(transverse_scalar.subs(conic_sub)))
    assert not Sres_z.has(sp.zoo, sp.nan, sp.oo, -sp.oo)

    # z=0 is (u,v)=(ir,0).  On the meridian q=(t-ir)(t+ir), hence
    # [q A]_{q=0,z=0} = 2 i r Res_{t=ir} A.  This checks the full residue against
    # the already-certified one-coordinate engine without evaluating the raw pole.
    old_tree = mer.scalar_tree(+1, -1)
    old_res_plus = sp.factor(sp.limit((t - I * r) * old_tree, t, I * r))
    full_at_zero = sp.factor(sp.simplify(Sres_z.subs(z, 0)))
    assert sp.simplify(full_at_zero - 2 * I * r * old_res_plus) == 0

    print("full mixed-helicity scalar transverse residue on triple-cut conic =", Sres_z)
    print("z=0 transverse residue =", full_at_zero)
    print("meridian coordinate residue at t=ir =", old_res_plus)
    print("PASS: full stereographic residue-level tree engine exactly extends the certified meridian engine")
    print("NEXT: evaluate the full vector-minus-scalar transverse residue/state sum as a rational function of z and extract its large-z polynomial part")


if __name__ == "__main__":
    main()
