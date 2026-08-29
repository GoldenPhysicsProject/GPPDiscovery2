#!/usr/bin/env python3
"""Exact conversion of generic massive-vector state-sum defects to the physical chart.

This script does not recompute the Yang--Mills trees.  It starts from the exact
rational expressions already certified in `massive_vector_generic_state_sum_symbolic.py`
and rewrites them in the physical variables

    beta = |p|/E,
    rho  = mu/E,
    c    = cos(theta),
    u    = beta^2 sin(theta)^2.

The target normal form is the one used by the celestial-cut/regulator program.
"""

import sympy as sp

r, t = sp.symbols("r t", real=True, nonzero=True)

beta = (1 - r**2) / (1 + r**2)
rho = 2*r / (1 + r**2)
c = (1 - t**2) / (1 + t**2)
s = 2*t / (1 + t**2)
u = beta**2 * s**2
den = (1 - beta*c)**2

# Exact same-helicity vector-minus-three-scalars defect from the generic tree audit.
same_defect_rt = 4*(r**2 - 1)**2*(1 + t**2)**2/(r**2 + t**2)**2
assert sp.factor(sp.together(same_defect_rt - 16*beta**2/den)) == 0

# Exact mixed-helicity scalar tree from the generic tree audit.
mixed_scalar_tree_rt = (
    -2*t**2*(r**2 - 1)**2 /
    ((r**2 + 1)*(r**2 + t**2)*(t**2 + 1))
)
mixed_scalar_cut_rt = sp.factor(mixed_scalar_tree_rt**2)
assert sp.factor(sp.together(mixed_scalar_cut_rt - u**2/den)) == 0

# The physical chart automatically satisfies beta^2 + rho^2 = 1.
assert sp.factor(sp.together(beta**2 + rho**2 - 1)) == 0

print("PASS: generic same-helicity defect = 16 beta^2/(1-beta*c)^2")
print("PASS: generic mixed-helicity scalar cut = u^2/(1-beta*c)^2")
print("PASS: beta^2 + rho^2 = 1")
