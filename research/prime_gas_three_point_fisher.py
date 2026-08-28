"""Exact audit of the normalized three-support Fisher determinant.

For weights p,q,r with p+q+r=1 and support x,y,z, let m_k = E[X^k].
The covariance determinant of sufficient statistics (X,X^2) should equal
p*q*r times the squared Vandermonde.
"""

import sympy as sp

p, q, r, x, y, z = sp.symbols("p q r x y z")

m1 = p*x + q*y + r*z
m2 = p*x**2 + q*y**2 + r*z**2
m3 = p*x**3 + q*y**3 + r*z**3
m4 = p*x**4 + q*y**4 + r*z**4

cov_det = sp.expand((m2 - m1**2)*(m4 - m2**2) - (m3 - m1*m2)**2)
vandermonde_det = p*q*r*(x-y)**2*(x-z)**2*(y-z)**2

# Enforce normalization exactly by eliminating r.
normalized_difference = sp.factor((cov_det - vandermonde_det).subs(r, 1-p-q))
assert normalized_difference == 0

print("normalized_difference =", normalized_difference)
print("identity: det Cov(X,X^2) = p q r (x-y)^2 (x-z)^2 (y-z)^2")
print("strict positivity follows for p,q,r>0 and pairwise distinct x,y,z")
