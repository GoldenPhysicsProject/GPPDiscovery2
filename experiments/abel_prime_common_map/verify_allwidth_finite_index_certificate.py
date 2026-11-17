"""Exact integer receipt for a weak finite-codimension Weil certificate.

General theorem in research/actual_weil_all_width_finite_negative_index_2026_11_16.md:
For every finite L, an explicit N(L) makes W positive on tests whose first
N moments vanish. Here L=1/8,R=3000,N=1000, NOT the sharp in-tree positivity
result for this window.
"""
from fractions import Fraction as Q
R=3000
M=10**6
lower=0
for k in range(10001):
    odd=4*k+1
    lower+=(M*16*R*R)//(odd*(odd*odd+4*R*R))
assert Q(lower,M)>Q(23,2)
# Separate elementary transcendental side bounds:
# gamma<.58, log(pi)<1.15, pi/2<1.6, log2<.7,
# exp(1/16)<16/15, e<3 and pi>3.
assert Q(543,100)+Q(4,15)<Q(57,10)
assert 125*Q(9,16)**10<Q(1,2)
assert Q(23,4)-Q(57,10)==Q(1,20)
print("PASS finite-codimension Weil coefficient receipt")
print("a(3000) lower",str(Q(lower,M)))
print("B(1/8) upper",str(Q(543,100)+Q(4,15)))
print("alpha_1000 upper",str(125*Q(9,16)**10))
print("W(f) > (1/20)||f||^2 if first 1000 x-moments vanish, width=1/8.")
print("WEAKER than known in-tree all-functions L=1/8 positivity; the new value is the ALL-width proof.")
