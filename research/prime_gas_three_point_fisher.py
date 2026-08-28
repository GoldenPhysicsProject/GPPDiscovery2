"""Exact audits of finite-support two-parameter Fisher determinants.

For sufficient statistics (X,X^2), the covariance determinant equals the 3x3
moment-Gram determinant.  Cauchy-Binet therefore predicts a sum over squared
three-row Vandermonde minors.  The three- and four-support cases below are
verified symbolically and provide executable checks of the finite-support pattern
before its general Lean formulation.
"""

import sympy as sp

# Three-point support.
p, q, r, x, y, z = sp.symbols("p q r x y z")

m1 = p*x + q*y + r*z
m2 = p*x**2 + q*y**2 + r*z**2
m3 = p*x**3 + q*y**3 + r*z**3
m4 = p*x**4 + q*y**4 + r*z**4

cov_det = sp.expand((m2 - m1**2)*(m4 - m2**2) - (m3 - m1*m2)**2)
vandermonde_det = p*q*r*(x-y)**2*(x-z)**2*(y-z)**2
three_difference = sp.factor((cov_det - vandermonde_det).subs(r, 1-p-q))
assert three_difference == 0

# Four-point support.  Cauchy-Binet gives one term for each three-point minor.
s, w = sp.symbols("s w")
m1_4 = p*x + q*y + r*z + s*w
m2_4 = p*x**2 + q*y**2 + r*z**2 + s*w**2
m3_4 = p*x**3 + q*y**3 + r*z**3 + s*w**3
m4_4 = p*x**4 + q*y**4 + r*z**4 + s*w**4
cov_det_4 = sp.expand((m2_4 - m1_4**2)*(m4_4 - m2_4**2) - (m3_4 - m1_4*m2_4)**2)

cb4 = (
    p*q*r*(x-y)**2*(x-z)**2*(y-z)**2
    + p*q*s*(x-y)**2*(x-w)**2*(y-w)**2
    + p*r*s*(x-z)**2*(x-w)**2*(z-w)**2
    + q*r*s*(y-z)**2*(y-w)**2*(z-w)**2
)
four_difference = sp.factor((cov_det_4 - cb4).subs(s, 1-p-q-r))
assert four_difference == 0

print("three_point_difference =", three_difference)
print("four_point_difference =", four_difference)
print("verified: det Cov(X,X^2) is the sum of weighted squared Vandermonde 3-minors")
print("next exact step: general finite Cauchy-Binet theorem, then countable Gibbs limit")
