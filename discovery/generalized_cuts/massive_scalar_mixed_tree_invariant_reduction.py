#!/usr/bin/env python3
"""Exact invariant reduction of the generic mixed-helicity massive-scalar tree.

For the physical color ordering (massive, gluon, gluon, massive) used by the
s23 two-particle cut, import the generic rational kinematics from
``massive_vector_generic_state_sum_symbolic.py``.  The rational parameters r,t
are eliminated in favor of

    s = s23 = 4 E^2,
    mu^2 = E^2 rho^2,
    D  = (q1 + p2)^2,
    D' = (q1 + p3)^2.

The exact identities certified below are

    D + D' = -s,

and, for either mixed external helicity ordering,

    A_S = -2 - 2 D/s - 2 mu^2/D
        =  2 D'/s - 2 mu^2/D.

Thus the generic scalar tree splits canonically into a polynomial boundary part
and a single uncut-propagator pole.  This is the form needed before Badger's
bubble boundary extraction and higher-topology subtraction.

No coupling/color/cut-orientation/loop-measure normalization is asserted.
"""

from __future__ import annotations

import sympy as sp

import massive_vector_generic_state_sum_symbolic as gen
import massive_vector_mhv_state_sum_symbolic as base


def main() -> None:
    ks = gen.generic_kinematics(5)
    g = base.metric(5)
    q1, p2, p3, _q4 = ks

    s = sp.factor(base.mdot(g, p2 + p3, p2 + p3))
    D = sp.factor(base.mdot(g, q1 + p2, q1 + p2))
    Dp = sp.factor(base.mdot(g, q1 + p3, q1 + p3))
    mu2 = sp.factor(base.E**2 * gen.rho**2)

    AS_pm = sp.factor(gen.scalar_tree(+1, -1))
    AS_mp = sp.factor(gen.scalar_tree(-1, +1))

    assert sp.simplify(s - 4 * base.E**2) == 0
    assert sp.simplify(D + Dp + s) == 0
    assert sp.simplify(AS_pm - AS_mp) == 0

    invariant_form = sp.factor(-2 - 2 * D / s - 2 * mu2 / D)
    complementary_form = sp.factor(2 * Dp / s - 2 * mu2 / D)

    assert sp.simplify(AS_pm - invariant_form) == 0
    assert sp.simplify(invariant_form - complementary_form) == 0

    # Canonical boundary/pole split.
    boundary = sp.factor(-2 - 2 * D / s)
    pole = sp.factor(-2 * mu2 / D)
    assert sp.simplify(AS_pm - boundary - pole) == 0
    assert sp.simplify(D * pole + 2 * mu2) == 0

    print("s23 =", s)
    print("D =", D)
    print("D' =", Dp)
    print("D + D' =", sp.factor(D + Dp))
    print("mu^2 =", mu2)
    print("A_S mixed =", AS_pm)
    print("A_S invariant =", invariant_form)
    print("boundary part =", boundary)
    print("pole part =", pole)
    print("PASS: generic mixed scalar tree reduced exactly to invariant boundary + pole form")


if __name__ == "__main__":
    main()
