#!/usr/bin/env python3
"""Exact chart-dimension audit for the generic nonzero-mu cut versus Badger subtraction.

The current generic massive-vector state-sum uses the rational meridian

    n(t) = (2t/(1+t^2), 0, (1-t^2)/(1+t^2))

of the two-particle cut sphere.  This is sufficient for the collapsed rotationally
reduced sewing and for locating the extra propagator pole on that meridian, but it
is not the full two-parameter double-cut chart required before a generic triple-cut
moment extraction.

This audit proves two exact facts.

1. The meridian used by `massive_vector_generic_state_sum_symbolic.py` is the v=0
   restriction of the full rational S^2 stereographic chart

       n(u,v) = (2u, 2v, 1-u^2-v^2)/(1+u^2+v^2),

   and the full chart has rank two away from the usual stereographic degeneracy.

2. Badger's s23 double-cut loop matrix l1(y,t) genuinely carries two independent
   parameters before the extra propagator P(y)=0 is imposed.  Its y- and t-tangent
   vectors are linearly independent identically (the (2,1) entry already separates
   them).

Therefore the previously computed roots t=+/- i r in the meridian chart are valid
pole loci on that slice, but the resulting root data cannot yet be inserted directly
into Badger's T1,T2,T3 map.  The honest next step is to lift the generic vector-minus-
scalar tree state sum to the full two-parameter cut sphere (or an equivalent spinor
chart), impose the third cut there, and only then derive the surviving one-parameter
large-coordinate moments.
"""
from __future__ import annotations

import sympy as sp

u, v, t, y, mu2 = sp.symbols("u v t y mu2", nonzero=True)

# Full rational unit-sphere chart and the meridian used in the generic state-sum.
den = 1 + u**2 + v**2
n_full = sp.Matrix([2*u/den, 2*v/den, (1-u**2-v**2)/den])
n_meridian = sp.Matrix([2*t/(1+t**2), 0, (1-t**2)/(1+t**2)])
assert all(sp.simplify(a-b) == 0 for a, b in zip(n_full.subs({u: t, v: 0}), n_meridian))
assert sp.simplify((n_full.T*n_full)[0] - 1) == 0

# A 2x2 Jacobian minor certifies rank two for the full chart generically.
Ju = sp.simplify(n_full.diff(u))
Jv = sp.simplify(n_full.diff(v))
minor_xy = sp.factor(sp.Matrix([[Ju[0], Jv[0]], [Ju[1], Jv[1]]]).det())
minor_xy_target = sp.factor(4*(1-u**2-v**2)/(1+u**2+v**2)**3)
assert sp.simplify(minor_xy - minor_xy_target) == 0
# Where that particular minor vanishes, another minor generically survives; the
# cross product gives the global rank-two witness on every finite chart point.
cross = sp.simplify(Ju.cross(Jv))
cross_sq = sp.factor((cross.T*cross)[0])
cross_sq_target = sp.factor(16/(1+u**2+v**2)**4)
assert sp.simplify(cross_sq - cross_sq_target) == 0

# Badger s23 double-cut chart from badger_s23_mhv_triangle_subtraction_one_flow.py.
l1 = sp.Matrix([
    [1-y, (y*(1-y)-mu2)/t],
    [t, y],
])
assert sp.simplify(l1.det() - mu2) == 0
ly = l1.diff(y)
lt = l1.diff(t)
# Flatten and exhibit a constant nonzero 2x2 minor: entries (0,0) and (1,0).
ly_flat = sp.Matrix([ly[0,0], ly[0,1], ly[1,0], ly[1,1]])
lt_flat = sp.Matrix([lt[0,0], lt[0,1], lt[1,0], lt[1,1]])
minor_badger = sp.Matrix([[ly_flat[0], lt_flat[0]], [ly_flat[2], lt_flat[2]]]).det()
assert sp.simplify(minor_badger + 1) == 0

print("full S2 chart n(u,v) =", n_full.T)
print("generic meridian n(t) = n(t,0): PASS")
print("full-chart tangent cross norm^2 =", cross_sq)
print("Badger double-cut tangent minor =", minor_badger)
print("PASS: both the full cut sphere and Badger pre-subtraction chart are rank two")
print("CORRECTION: t=+/- i r are meridian triple-cut roots, not yet Badger moment inputs")
print("NEXT: restore the second cut-sphere/spinor coordinate before T1,T2,T3 extraction")
