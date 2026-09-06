#!/usr/bin/env python3
"""Fix the physical propagator normalization of the full-conic transverse residue.

The full-chart tree engine extracts the finite triple-cut datum as

    R_q = [q A]_{q=0},   q = r^2 + u^2 + v^2.

This audit proves that q is exactly proportional to the remaining adjacent cubic
propagator p12^2 (equivalently p34^2 by momentum conservation), and determines the
conversion to the physical propagator residue.  On the cut the proportionality factor
is independent of the surviving conic coordinate z:

    p12^2 = -4 E^2 q / ((1+r^2)(1+u^2+v^2)),
    [p12^2 A]_{q=0} = -4 E^2/(1-r^4) [q A]_{q=0}.

This is normalization data only.  It does not perform opposite-tree sewing or assign a
master-integral coefficient.
"""
from __future__ import annotations

import sympy as sp

import generic_full_chart_vector_scalar_tree_audit as full
import massive_vector_mhv_state_sum_symbolic as base

r, u, v, z = full.r, full.u, full.v, full.z
s = full.s
E = full.E
q = r**2 + s


def main() -> None:
    g = base.metric(5)
    q1, g2, g3, q4 = full.full_kinematics(5)
    p12 = sp.simplify(q1 + g2)
    p34 = sp.simplify(g3 + q4)

    p12_sq = sp.factor(base.mdot(g, p12, p12))
    p34_sq = sp.factor(base.mdot(g, p34, p34))
    expected = sp.factor(-4 * E**2 * q / ((1 + r**2) * (1 + s)))

    assert sp.factor(sp.cancel(p12_sq - expected)) == 0
    assert sp.factor(sp.cancel(p34_sq - expected)) == 0
    assert sp.simplify(p34 + p12) == sp.zeros(5, 1)

    # Convert q-residue to the residue normalized by the actual tree propagator.
    ratio = sp.factor(sp.cancel(p12_sq / q))
    expected_ratio = sp.factor(-4 * E**2 / ((1 + r**2) * (1 + s)))
    assert sp.factor(sp.cancel(ratio - expected_ratio)) == 0

    uz = sp.I * r * (1 - z**2) / (1 + z**2)
    vz = 2 * sp.I * r * z / (1 + z**2)
    conic_sub = {u: uz, v: vz}
    ratio_cut = sp.factor(sp.cancel(ratio.subs(conic_sub)))
    expected_cut = sp.factor(-4 * E**2 / (1 - r**4))
    assert sp.factor(sp.cancel(ratio_cut - expected_cut)) == 0
    assert not ratio_cut.has(z)

    # Verify the conversion on an actual tree residue, not only on denominators.
    A = full.scalar_tree(+1, -1)
    Rq = sp.factor(sp.cancel((q * A).subs(conic_sub)))
    Rp = sp.factor(sp.cancel((p12_sq * A).subs(conic_sub)))
    assert sp.factor(sp.cancel(Rp - expected_cut * Rq)) == 0

    print("p12^2 =", p12_sq)
    print("p34^2 =", p34_sq)
    print("p12^2 / q =", ratio)
    print("cut conversion [p12^2 A] / [q A] =", ratio_cut)
    print("PASS: q-residue has a unique z-independent physical propagator normalization")
    print("BOUNDARY: opposite crossed tree and factor-preserving topology subtraction are still required before any Ds=4 master coefficient")


if __name__ == "__main__":
    main()
