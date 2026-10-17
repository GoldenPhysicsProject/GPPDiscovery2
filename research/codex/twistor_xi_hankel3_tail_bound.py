#!/usr/bin/env python3
"""Exact Fraction inequalities for finite positivity of actual xi Hankel H3.

Literature inputs (NOT proved in this code):
  1. Platt--Trudgian: every zeta zero up to H=3e12 lies on Re s=1/2.
  2. First zero ordinates have rigorous coarse brackets
     (14.13,14.14), (21.02,21.03), (25.01,25.02).
  3. Classical explicit Riemann--von Mangoldt/Rosser N(T) bound:
     N(T)<=T^2 for T>=H.

Given those externally proved inputs, positivity of H3 follows with
the numerical lower bound lambda_min(H3)>1e-23.
All inequalities BELOW are exact rational arithmetic. The infinite
Hadamard representation and zero-counting bridge are mathematical
arguments in the accompanying private note, not formalized in Lean.
RH beyond H is NOT assumed or proved.
"""
from fractions import Fraction as Q

H = 3*10**12
gamma_lo=[Q(x) for x in ("14.13","21.02","25.01")]
gamma_hi=[Q(x) for x in ("14.14","21.03","25.02")]
z_lo=[Q(1)/a**2 for a in gamma_hi]
z_hi=[Q(1)/a**2 for a in gamma_lo]

assert z_lo[0]>z_hi[1] and z_lo[1]>z_hi[2]
# G=VV^T, V_ij=z_j**(i+1). Vandermonde:
det_lower=(z_lo[0]*z_lo[1]*z_lo[2])**2 * (
    (z_lo[0]-z_hi[1])*(z_lo[0]-z_hi[2])*(z_lo[1]-z_hi[2])
)**2
trace_upper=sum(z**2+z**4+z**6 for z in z_hi)
assert det_lower>Q(12,10**33)
assert trace_upper<Q(33,10**6)

# N(t)<=t^2 and Stieltjes integration give
# sum_(gamma>H) gamma^(-4)<=2/H^2.
# Each 3x3 high-zero matrix entry has absolute value <= sum.
tail_norm_upper=Q(6,H**2)
# For positive G, lambda_min(G)>=det(G)/trace(G)^2.
margin=Q(12,10**33)/Q(33,10**6)**2-tail_norm_upper
assert margin>Q(1,10**23)
print("FIRST-THREE GRAM det bound:",float(det_lower))
print("FIRST-THREE GRAM trace bound:",float(trace_upper))
print("UNVERIFIED tail operator-norm bound:",float(tail_norm_upper))
print("LOWER bound lambda_min(H3):",float(margin))
print("PASS: lambda_min(H3)>1e-23 from external published inputs.")
print("IMPORTANT: does NOT establish any unbounded hierarchy or RH.")
