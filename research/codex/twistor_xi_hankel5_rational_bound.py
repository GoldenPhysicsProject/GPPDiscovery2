#!/usr/bin/env python3
"""Exact finite xi H4/H5 Hankel coercivity bounds from established zero facts.

External inputs, not proved by this code:
Platt--Trudgian: all zeros below H=3e12 are on line.
First five rigorously known ordinate brackets.
Rosser: N(t)<=t^2 and N(t)<=t*log(t) for t>=H.
Exact Fraction arithmetic checks determinant/inverse and tail bounds.
This does NOT prove RH or formalize the analytic bridge in Lean.
"""
from fractions import Fraction as Q
H=3*10**12
gamma_lo=[Q(x) for x in ("14.13","21.02","25.01","30.42","32.93")]
gamma_hi=[Q(x) for x in ("14.14","21.03","25.02","30.43","32.94")]
z_lo=[Q(1)/x**2 for x in gamma_hi]
z_hi=[Q(1)/x**2 for x in gamma_lo]

def upper_inverse_frobenius(n):
    """Majorize ||V^-1||_F^2 for V_ij=z_j^(i+1) via Lagrange."""
    total=Q(0)
    for j in range(n):
        d=z_lo[j]
        for k in range(n):
            if k==j: continue
            gap=z_lo[k]-z_hi[j] if k<j else z_lo[j]-z_hi[k]
            assert gap>0
            d*=gap
        e=[Q(1)]  # elementary symmetric polynomials, upper bounds
        for k in range(n):
            if k==j: continue
            z=z_hi[k]
            out=[Q(0)]*(len(e)+1)
            for idx,v in enumerate(e):
                out[idx]+=v
                out[idx+1]+=z*v
            e=out
        total+=sum((a/d)**2 for a in e)
    return total

inv4=upper_inverse_frobenius(4)
inv5=upper_inverse_frobenius(5)
assert inv4 < 5*10**23
assert inv5 < 2*10**31

# N(t)<=t^2 -> sum_(gamma>H)gamma^-4<=2/H^2,
# so 4x4 unknown-tail matrix operator norm <=8/H^2.
tail4=Q(8,H**2)
# N(t)<=t*log t and log H<30 ->
# sum gamma^-4 <(40+4/9)/H^3<41/H^3,
# so 5x5 unknown-tail matrix norm <205/H^3.
tail5=Q(205,H**3)
bound4=Q(1,5*10**23)-tail4
bound5=Q(1,2*10**31)-tail5
assert bound4>Q(1,10**24)
assert bound5>Q(4,10**32)
print("upper inv4:",float(inv4),"upper inv5:",float(inv5))
print("H4 lower eigenvalue:",float(bound4))
print("H5 lower eigenvalue:",float(bound5))
print("PASS: H4>1e-24 I, H5>4e-32 I, subject to published inputs.")
print("NO RH/GRH claim.")
