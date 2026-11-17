"""Finite test of the exact two-state prime running recurrence H_n,D_n.
For L in [log n,log(n+1)] the scalar H is convex and has a closed minimizer.
Suzuki (2025) already proved eventual H>=0 equivalent to RH; numerical scans
are NOT a proof and cannot be extrapolated to infinitely many n.
"""
import os
import math
import numpy as np
from arith_graph_common import mangoldt_sieve

N=int(os.environ.get("GPP_MAX_INTEGER","10000000"))
lam=mangoldt_sieve(N)
V=J=0.
min_H=(math.inf,0)
min_D=(math.inf,0)
min_rung=(math.inf,0)
negative_D_count=0
for n in range(2,N):
    root=math.sqrt(n)
    ll=math.log(n)
    v=lam[n]/root
    V+=v
    J+=v*ll
    H=4*(root+1/root-2)-V*ll+J
    D=2*(root-1/root)-V
    if H<min_H[0]:min_H=(H,n)
    if D<min_D[0]:min_D=(D,n)
    if D<0:negative_D_count+=1
    # H has a unique unconstrained minimizer at t*=2 asinh(V/4).
    # Only evaluate it when the slope is negative; else left endpoint wins.
    Hr=H
    if D<0:
        tstar=min(math.log(n+1),max(ll,2*math.asinh(V/4)))
        Hr=8*(math.cosh(tstar/2)-1)-V*tstar+J
    if Hr<min_rung[0]:min_rung=(Hr,n)
    if n in (2,3,10,100,1000,10000,100000,1000000):
        print("n",n,"H",H,"D",D,"V",V)
print("N",N,"min H at integer threshold",min_H,
      "min D after threshold",min_D,
      "min continuous-rung H",min_rung,
      "negative D count",negative_D_count)
print("NUMERICAL only. Finite check does not establish eventual sign / RH.")
