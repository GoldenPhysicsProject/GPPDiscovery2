#!/usr/bin/env python3
"""Exact helicity-phase structure on the full nonzero-mu triple-cut conic.

The conic u^2+v^2=-r^2 is a rational complex rotation of the z=0 meridian
point.  This audit proves the exact rotation and helicity-frame phases, then checks
those phases directly against the extra-scalar transverse tree residue q A|_{q=0}.

This is pre-sewing residue data, not a master-integral coefficient.
"""
from __future__ import annotations

import sympy as sp

import generic_full_chart_vector_scalar_tree_audit as full

r, u, v, z = full.r, full.u, full.v, full.z
I = sp.I

c = (1 - z**2) / (1 + z**2)
s = 2 * z / (1 + z**2)
R = sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])
uz = I * r * c
vz = I * r * s
conic_sub = {u: uz, v: vz}
q = r**2 + u**2 + v**2


def spatial_pol(leg: int, h: int, U, V):
    pol = full.full_gluon_pol(leg, h, 5)
    return sp.Matrix([sp.simplify(pol[j].subs({u: U, v: V})) for j in (1, 2, 3)])


def phase(leg: int, h: int):
    if leg == 2:
        return -(z - I * h) / (z + I * h)
    if leg == 3:
        return -(z + I * h) / (z - I * h)
    raise ValueError("leg must be 2 or 3")


def main() -> None:
    assert sp.factor(c**2 + s**2 - 1) == 0
    assert sp.factor(uz**2 + vz**2 + r**2) == 0

    # The cut direction is exactly a complex transverse rotation of z=0.
    n0 = full.n.subs({u: I * r, v: 0})
    nz = full.n.subs(conic_sub)
    assert sp.simplify(nz - R * n0) == sp.zeros(3, 1)

    # The chart helicity frames differ from the rotated meridian frames only by
    # explicit little-group phases.
    for leg in (2, 3):
        for h in (-1, +1):
            e0 = spatial_pol(leg, h, I * r, 0)
            ez = spatial_pol(leg, h, uz, vz)
            assert sp.simplify(ez - phase(leg, h) * R * e0) == sp.zeros(3, 1)

    # The scalar transverse residue at z=0 follows from the already-certified
    # meridian coordinate residue.  Direct full-tree extraction verifies that the
    # complete z dependence is exactly the product of the two helicity phases.
    base_residue = sp.factor(2 * r**2 * (1 - r**2) / (1 + r**2))
    for h2, h3 in [(-1, -1), (+1, +1), (+1, -1), (-1, +1)]:
        A = full.scalar_tree(h2, h3)
        got = sp.factor(sp.cancel((q * A).subs(conic_sub)))
        target = sp.factor(base_residue * phase(2, h2) * phase(3, h3))
        assert sp.simplify(got - target) == 0

    # Same helicity is z-independent; mixed helicity carries a pure rational
    # little-group square.  The opposite mixed channels are reciprocal.
    assert sp.simplify(phase(2, +1) * phase(3, +1) - 1) == 0
    assert sp.simplify(phase(2, -1) * phase(3, -1) - 1) == 0
    mixed_pm = sp.factor(phase(2, +1) * phase(3, -1))
    mixed_mp = sp.factor(phase(2, -1) * phase(3, +1))
    assert sp.simplify(mixed_pm - ((z - I) / (z + I))**2) == 0
    assert sp.simplify(mixed_mp - ((z + I) / (z - I))**2) == 0
    assert sp.simplify(mixed_pm * mixed_mp - 1) == 0

    print("same-helicity transverse scalar residue =", base_residue)
    print("(+,-) helicity phase =", mixed_pm)
    print("(-,+) helicity phase =", mixed_mp)
    print("PASS: the full triple-cut z dependence is an exact rational transverse rotation/little-group phase in the scalar residue sector")
    print("NEXT: lift this covariance to the 3x3 massive-vector residue matrix; normalized vector/scalar spectra should then be z-invariant by similarity")


if __name__ == "__main__":
    main()
