"""Exact Q-arithmetic no-go: every entrant locally weak yet global H(log200)<0.

Weights are ARTIFICIAL v_n=log(n)/sqrt(n) at EVERY integer n.
Log2>69/100 is an independent elementary analytic fact; all finite arithmetic
below is exact Fraction (not floating point). This falsifies any induction
claim using ONLY the local per-entry bound g_n<1, not the actual RH criterion.
"""
from fractions import Fraction as Q
from math import isqrt

N=200
q=Q(69,100)
s=Q(0)
for k in range(2,51):
    j=k.bit_length()-1
    h=(N//k).bit_length()-1
    m=isqrt(k)
    if m*m<k: m+=1
    assert 2**j<=k and 2**h*k<=N and (m*m>=k)
    s+=q*q*Q(j*h,m)

upper=4*(Q(283,20)+Q(1,14)-2)
assert 14**2<N
assert Q(283,20)**2>N
assert s>upper
print("PASS exact rational fake-prime global counterexample")
print("Sum k=2..50 lower",s,"=",float(s))
print("Pole at log 200 upper",upper,"=",float(upper))
print("Strict rational gap",s-upper,"=",float(s-upper))
print("Thus fake H(log 200)<0, although all fake prime entries have local g_n<1.")
print("The log2>69/100 analytic fact is a separate lemma; no RH proof.")
