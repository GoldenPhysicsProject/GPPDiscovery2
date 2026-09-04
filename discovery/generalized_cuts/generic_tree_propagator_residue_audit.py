#!/usr/bin/env python3
"""Exact propagator interpretation of the generic nonzero-mu Ds=4 sewing pole variable.

For the color ordering (massive, gluon, gluon, massive), the complete stripped tree
contains the adjacent p12 and p23 cubic channels plus the quartic contact term.  In the
generic 5D-null kinematics used by ``massive_vector_generic_state_sum_symbolic.py`` we
prove exactly that

    p12^2 = -2 E^2 (1 - beta cos(theta)),
    p23^2 =  4 E^2.

Thus x = 1-beta*cos(theta) is not an arbitrary Laurent coordinate: it is the unique
angle-dependent adjacent tree propagator coordinate.  When two such trees are sewn,
the x^{-2}, x^{-1}, and polynomial sectors count double, single, and zero occurrences
of this propagator across the two tree factors.  This is diagram-level topology ancestry,
not yet a master-integral coefficient assignment; Badger triangle/bubble subtraction is
still required for the latter.
"""
from __future__ import annotations

import sympy as sp

import massive_vector_generic_state_sum_symbolic as gen
import massive_vector_mhv_state_sum_symbolic as base

E = base.E
r = gen.r
t = base.t
beta = gen.beta
rho = gen.rho
ct = gen.ct
x = sp.symbols("x", real=True)


def main() -> None:
    g = base.metric(5)
    q1, k2, k3, q4 = gen.generic_kinematics(5)
    p12 = sp.simplify(q1 + k2)
    p23 = sp.simplify(k2 + k3)

    p12_sq = sp.factor(base.mdot(g, p12, p12))
    p23_sq = sp.factor(base.mdot(g, p23, p23))

    x_rt = sp.factor(1 - beta * ct)
    assert sp.simplify(p12_sq + 2 * E**2 * x_rt) == 0
    assert sp.simplify(p23_sq - 4 * E**2) == 0

    # Rational parametrization cross-check: the propagator zero is exactly x=0.
    x_rational = sp.factor(x_rt)
    expected = sp.factor(2 * (r**2 + t**2) / ((1 + r**2) * (1 + t**2)))
    assert sp.simplify(x_rational - expected) == 0

    # Physical real slice: for real nonzero r,t, the rational x is positive, hence the
    # p12 pole is reached only after analytic continuation / boundary degeneration.
    numerator = sp.factor(sp.together(expected).as_numer_denom()[0])
    denominator = sp.factor(sp.together(expected).as_numer_denom()[1])
    assert numerator == 2 * (r**2 + t**2)
    assert denominator == (r**2 + 1) * (t**2 + 1)

    print("p12^2 =", p12_sq)
    print("p23^2 =", p23_sq)
    print("x = 1-beta*cos(theta) =", x_rational)
    print("x rational form =", expected)
    print("PASS: x is exactly the unique angle-dependent adjacent tree propagator coordinate")
    print("INTERPRETATION: x^-2/x^-1/x^0 are double/single/zero p12-propagator ancestry")
    print("BOUNDARY: master box/triangle/bubble assignment still requires integrand reduction")


if __name__ == "__main__":
    main()
