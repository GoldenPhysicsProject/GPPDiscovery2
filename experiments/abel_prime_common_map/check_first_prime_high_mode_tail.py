"""Exact rational subcertificate: first-prime high-Legendre-tail Weil coercivity.

The checks below are exact fractions. Analytic Weil/Fourier/Legendre
identities and transcendental constant bounds require separate formal proof.
"""
from fractions import Fraction as Q

L=Q(18,25)
M=Q(147,25)

def odd_double_factorial(k):
    product=1
    for j in range(1,2*k+2,2):
        product*=j
    return product

def arch_partial(r,num_terms):
    return sum(
        (Q(16*r*r,(4*k+1)*((4*k+1)**2+4*r*r)) for k in range(num_terms)),
        Q(0)
    )

for m, multiplier_floor, lower_weil in [
    (50,Q(77,10),Q(9,5)),
    (70,Q(81,10),Q(11,5)),
    (100,Q(42,5),Q(5,2))
]:
    r=Q(m)/L
    z=Q(m,2)
    first=z**(2*m)/odd_double_factorial(m)**2
    ratio=z*z/(2*m+3)**2
    assert ratio < Q(1,16)
    delta=Q(m,3)*first/(1-ratio)
    assert delta<Q(1,1000)
    amin=arch_partial(r,1000)
    assert amin>multiplier_floor
    slack=multiplier_floor*(1-Q(1,1000))-M-lower_weil
    assert slack>0
    print("PASS high mode",m,"cutoff",r,
          "a1000 >=",multiplier_floor,
          "exact low-band delta <",Q(1,1000),
          "W >=",lower_weil,"||f||²",
          "strict rational margin",slack,
          "a1000 float diagnostic",float(amin),
          "delta float diagnostic",float(delta))
print("Rational checks PASS; full mathematical formalization remains pending")
