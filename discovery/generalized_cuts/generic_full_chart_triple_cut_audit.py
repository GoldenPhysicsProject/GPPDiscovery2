#!/usr/bin/env python3
"""Exact full two-coordinate double-cut / triple-cut audit.

The earlier generic massive-vector scripts used the meridian v=0 of the cut sphere.
This file restores the full rational stereographic chart

    n(u,v) = (2u, 2v, 1-u^2-v^2)/(1+u^2+v^2),

constructs its exact orthonormal tangent frame, and derives the additional tree
propagator on the generic nonzero-mu cut.  The triple-cut constraint is then a
one-complex-parameter conic, with a rational parametrization.  This is the correct
kinematic precursor to a Badger-style root/moment projection; no master coefficient
is claimed here.

IMPORTANT: the Minkowski convention here is (+,-,-,-,-), exactly matching
``massive_vector_mhv_state_sum_symbolic.metric`` and the tree-amplitude engine.  An
earlier version accidentally used the opposite signature; that left the zero locus
unchanged but flipped propagator and polarization norms and therefore could not be
fed consistently into the amplitude code.
"""

from __future__ import annotations

import sympy as sp

u, v, z, r, E = sp.symbols("u v z r E", nonzero=True)
I = sp.I
s = u**2 + v**2

beta = (1 - r**2) / (1 + r**2)
rho = 2 * r / (1 + r**2)

n = sp.Matrix([
    2 * u / (1 + s),
    2 * v / (1 + s),
    (1 - s) / (1 + s),
])

# Stereographic coordinates are conformal.  Multiplying the coordinate tangent
# vectors by (1+s)/2 gives an exact Euclidean-orthonormal tangent frame on S^2.
eu = sp.simplify((1 + s) * n.diff(u) / 2)
ev = sp.simplify((1 + s) * n.diff(v) / 2)


def mdot5(a: sp.Matrix, b: sp.Matrix):
    """Mostly-minus 5D Minkowski product, matching the amplitude engine."""
    return sp.expand(a[0] * b[0] - sum(a[j] * b[j] for j in range(1, 5)))


def main() -> None:
    # Unit cut-sphere direction and exact tangent-frame geometry.
    assert sp.simplify(n.dot(n) - 1) == 0
    assert sp.simplify(eu.dot(n)) == 0
    assert sp.simplify(ev.dot(n)) == 0
    assert sp.simplify(eu.dot(eu) - 1) == 0
    assert sp.simplify(ev.dot(ev) - 1) == 0
    assert sp.simplify(eu.dot(ev)) == 0

    # Full generic cut kinematics.  q1 and q4 are 5D-null massive states and g2,g3
    # are opposite massless four-dimensional momenta with arbitrary cut-sphere angle.
    q1 = sp.Matrix([-E, 0, 0, -E * beta, +E * rho])
    q4 = sp.Matrix([-E, 0, 0, +E * beta, -E * rho])
    g2 = sp.Matrix([+E, E * n[0], E * n[1], E * n[2], 0])
    g3 = sp.Matrix([+E, -E * n[0], -E * n[1], -E * n[2], 0])

    for k in (q1, q4, g2, g3):
        assert sp.simplify(mdot5(k, k)) == 0
    assert sp.simplify(q1 + q4 + g2 + g3) == sp.zeros(5, 1)

    # Full-sphere helicity frame for g2.  With the mostly-minus convention used by
    # the amplitude engine, physical spacelike polarizations have norm -1.
    eps_plus = sp.Matrix([0, *(list((eu + I * ev) / sp.sqrt(2))), 0])
    eps_minus = sp.Matrix([0, *(list((eu - I * ev) / sp.sqrt(2))), 0])
    assert sp.simplify(mdot5(g2, eps_plus)) == 0
    assert sp.simplify(mdot5(g2, eps_minus)) == 0
    assert sp.simplify(mdot5(eps_plus, eps_minus) + 1) == 0

    # The extra adjacent tree propagator is exact on the full chart.  The sign is
    # fixed by the same mostly-minus metric used in the actual tree amplitude.
    D12 = sp.factor(mdot5(q1 + g2, q1 + g2))
    target = sp.factor(-4 * E**2 * (r**2 + u**2 + v**2) /
                       ((1 + r**2) * (1 + u**2 + v**2)))
    assert sp.simplify(D12 - target) == 0

    # Thus the genuine triple-cut locus is the complex conic u^2+v^2=-r^2.
    # It retains one free complex parameter, as required for subsequent moment
    # projection.  This rational parametrization covers the conic away from z=±i.
    uz = I * r * (1 - z**2) / (1 + z**2)
    vz = 2 * I * r * z / (1 + z**2)
    assert sp.factor(uz**2 + vz**2 + r**2) == 0
    assert sp.simplify(D12.subs({u: uz, v: vz})) == 0

    # The old meridian is recovered by v=0; then the conic collapses to u=± i r.
    meridian = sp.factor(D12.subs(v, 0))
    meridian_target = sp.factor(-4 * E**2 * (r**2 + u**2) /
                                ((1 + r**2) * (1 + u**2)))
    assert sp.simplify(meridian - meridian_target) == 0
    assert sp.simplify(meridian.subs(u, I * r)) == 0
    assert sp.simplify(meridian.subs(u, -I * r)) == 0

    # The conic parameter compactifies the two meridian roots as z=0 and z=infinity.
    # This is the correct relation between the earlier slice residues and a later
    # large-z Badger-style analysis.
    assert sp.simplify(uz.subs(z, 0) - I * r) == 0
    assert sp.simplify(vz.subs(z, 0)) == 0
    w = sp.symbols("w", nonzero=True)
    u_at_inf = sp.simplify(uz.subs(z, 1 / w))
    v_at_inf = sp.simplify(vz.subs(z, 1 / w))
    assert sp.simplify(sp.limit(u_at_inf, w, 0) + I * r) == 0
    assert sp.simplify(sp.limit(v_at_inf, w, 0)) == 0

    print("D12(u,v) =", D12)
    print("triple-cut conic: u^2 + v^2 + r^2 = 0")
    print("rational family: u(z)=", uz)
    print("                 v(z)=", vz)
    print("z=0 -> (+ir,0), z=infinity -> (-ir,0)")
    print("PASS: full chart uses the amplitude-engine signature and exact triple-cut family")


if __name__ == "__main__":
    main()
