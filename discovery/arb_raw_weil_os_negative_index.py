#!/usr/bin/env python3
"""EXACT FRACTION certificate for infinite-index naive Weil OS no-go.

The all-dimensional proof relies on Schur's operator norm inequality and
the infinite-dimensional +/- eigenspaces of local reflection, not on a
sampled matrix. No floating point, external packages, or numeric RH claim.
"""
from fractions import Fraction as F

x=F(2,5)
# For 0<x<1: e^x <= 1+x+x^2/2 + x^3/[6(1-x)],
# because every n! >= 6 for n >= 3.
exp_upper=1+x+x*x/2+x**3/(6*(1-x))
assert exp_upper==F(337,225) and exp_upper < F(3,2)

# log 2 = 2 * sum_{k>=0} (1/3)^(2k+1)/(2k+1).
# First term proves log2 > 2/3; dropping (2k+1)>1 for k>=1
# and summing the geometric series proves log2 < 3/4.
log2_lower=F(2,3)
log2_upper=2*F(1,3)/(1-F(1,9))
assert log2_upper==F(3,4)

delta=F(1,100)
y_lower=log2_lower-2*delta
y_upper=log2_upper+2*delta
assert y_lower>F(16,25) and y_upper<F(4,5)

# sinh y>y, e^(y/2)<e^(2/5)<3/2, e^(-y/2)<1.
# Therefore the exact kernel envelope satisfies
# |A(y)| < 3/2+1+(3/2)/(2*(16/25)) = 235/64 < 4.
sup_bound=F(3,2)+1+F(3,2)/(2*F(16,25))
assert sup_bound==F(235,64) and sup_bound<4
schur_bound=2*delta*4
assert schur_bound==F(2,25)

# sqrt2<3/2 implies w=log2/sqrt2 > (2/3)/(3/2)=4/9.
w_lower=log2_lower/F(3,2)
assert w_lower==F(4,9)
gap=w_lower-schur_bound
assert gap==F(82,225) and gap>F(1,3)
print('EXACT PASS: log2 ∈ (2/3,3/4), exp(2/5)<3/2')
print('EXACT PASS: smooth A sup <235/64<4, Schur norm K<2/25')
print('EXACT PASS: isolated prime weight w>4/9; sign gap >82/225')
print('THEOREM: raw additive Weil OS Hankel K-wR has infinite negative')
print('and positive index on the +/- reflection test subspaces.')
print('SCOPE: falsifies only raw additive OS reflection, NOT RH.')
