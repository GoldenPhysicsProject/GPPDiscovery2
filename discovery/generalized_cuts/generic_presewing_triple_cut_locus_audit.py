#!/usr/bin/env python3
"""Exact pre-sewing triple-cut pole-locus audit for the generic nonzero-mu tree.

This is the first constructive step after the residue non-injectivity obstruction.
For the physically relevant color ordering (massive, gluon, gluon, massive), the
angle-dependent cubic channel carries

    D12 = (q1+k2)^2
        = -4 E^2 (r^2+t^2)/((1+r^2)(1+t^2)),

where r parametrizes mu/E and t parametrizes the scattering angle.  Hence the
additional on-shell condition needed to lift the two-particle cut to a triple cut is
not a real-angle condition: in the complexified cut parameter it is exactly

    t = +/- i r.

The other cubic denominator is D23 = 4 E^2 and therefore remains regular on these
roots.  Thus, before sewing, the residue of a full tree at either triple-cut root is
carried solely by its p12 cubic channel; contact and p23-channel pieces are regular.

The script also records the exact Jacobian/residue of the bare p12 propagator.  It
does not yet claim a master-integral coefficient: numerator residues and the Badger
root-sum/subtraction map remain the next step.
"""
from __future__ import annotations

import sympy as sp

E, r, t = sp.symbols("E r t", nonzero=True)
I = sp.I

beta = (1 - r**2) / (1 + r**2)
ct = (1 - t**2) / (1 + t**2)
x = sp.factor(1 - beta * ct)

x_target = sp.factor(2 * (r**2 + t**2) / ((1 + r**2) * (1 + t**2)))
assert sp.simplify(x - x_target) == 0

D12 = sp.factor(-2 * E**2 * x)
D12_target = sp.factor(-4 * E**2 * (r**2 + t**2) / ((1 + r**2) * (1 + t**2)))
assert sp.simplify(D12 - D12_target) == 0

D23 = 4 * E**2

root_plus = I * r
root_minus = -I * r
assert sp.simplify(D12.subs(t, root_plus)) == 0
assert sp.simplify(D12.subs(t, root_minus)) == 0
assert sp.simplify(D23) != 0

# Generic roots are simple away from the threshold degeneracies r=0 and r^2=1.
dD12 = sp.factor(sp.diff(D12, t))
dD_plus = sp.factor(dD12.subs(t, root_plus))
dD_minus = sp.factor(dD12.subs(t, root_minus))

prop12 = sp.factor(1 / D12)
res_plus = sp.factor(sp.residue(prop12, t, root_plus))
res_minus = sp.factor(sp.residue(prop12, t, root_minus))
expected_plus = sp.factor(I * (1 - r**4) / (8 * r * E**2))
expected_minus = sp.factor(-I * (1 - r**4) / (8 * r * E**2))
assert sp.simplify(res_plus - expected_plus) == 0
assert sp.simplify(res_minus - expected_minus) == 0
assert sp.simplify(res_plus + res_minus) == 0

# The simple-pole Jacobian check: Res(1/D,t0)=1/D'(t0).
assert sp.simplify(res_plus - 1 / dD_plus) == 0
assert sp.simplify(res_minus - 1 / dD_minus) == 0

# A concrete rational witness keeps the audit independent of symbolic branch choices.
witness = {E: sp.Rational(3), r: sp.Rational(2, 5)}
assert sp.simplify(D12.subs(witness).subs(t, root_plus.subs(witness))) == 0
assert sp.simplify(res_plus.subs(witness)) != 0
assert sp.simplify(res_minus.subs(witness)) != 0

print("x =", x)
print("D12 =", D12)
print("triple-cut roots: t = +/- i r")
print("D23 =", D23, "(regular at both roots)")
print("Res[1/D12, t=+ir] =", res_plus)
print("Res[1/D12, t=-ir] =", res_minus)
print("PASS: the generic nonzero-mu pre-sewing triple-cut locus and propagator Jacobians are exact")
print("NEXT: evaluate the vector-minus-scalar tree numerators on t=+/- i r, then apply the existing Badger two-root sum and subtraction moments")
