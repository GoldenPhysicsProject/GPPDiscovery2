#!/usr/bin/env python3
"""Numerically audit the Riemann-seed synthesis Gram bound.

No zeta zeros are used. This is not an RH proof.
"""

from __future__ import annotations
import argparse
import math
import numpy as np
import mpmath as mp


def phi(u):
    return (
        4*mp.pi**2*mp.e**(mp.mpf("4.5")*u)
        - 6*mp.pi*mp.e**(mp.mpf("2.5")*u)
    ) * mp.e**(-mp.pi*mp.e**(2*u))


def weighted_norm(q):
    # Exact gamma-integral form.
    p=mp.pi
    return mp.sqrt(
        8*p**4 * mp.gamma(q+mp.mpf("4.5")) / (2*p)**(q+mp.mpf("4.5"))
        -24*p**3 * mp.gamma(q+mp.mpf("3.5")) / (2*p)**(q+mp.mpf("3.5"))
        +18*p**2 * mp.gamma(q+mp.mpf("2.5")) / (2*p)**(q+mp.mpf("2.5"))
    )


def K(a):
    return mp.quad(lambda u: phi(u)*phi(u+a), [-mp.inf,0,mp.inf])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--N",type=int,default=30)
    ap.add_argument("--q",type=float,default=1.0)
    ap.add_argument("--dps",type=int,default=40)
    args=ap.parse_args()
    mp.mp.dps=args.dps
    q=mp.mpf(args.q)
    assert mp.mpf("0.5") < q < mp.mpf("2.5")

    A=weighted_norm(q)*weighted_norm(-q)
    analytic=A*(2+1/(q-mp.mpf("0.5"))+1/(q+mp.mpf("0.5")))

    G=np.empty((args.N,args.N),dtype=float)
    max_corr_ratio=mp.mpf("0")
    cache={}
    for m in range(1,args.N+1):
        for n in range(1,args.N+1):
            a=mp.log(mp.mpf(n)/m)
            key=mp.nstr(abs(a),30)
            if key not in cache:
                cache[key]=K(abs(a))
            kval=cache[key]
            G[m-1,n-1]=float(kval/mp.sqrt(m*n))
            denom=A*mp.e**(-q*abs(a))
            if denom:
                max_corr_ratio=max(max_corr_ratio,abs(kval)/denom)

    gram_norm=np.linalg.eigvalsh(G).max()
    max_rowsum=np.abs(G).sum(axis=1).max()

    print("N =",args.N,"q =",args.q)
    print("N(q)N(-q) =",mp.nstr(A,15))
    print("max |K|/(A exp(-q|a|)) =",mp.nstr(max_corr_ratio,12))
    print("finite Gram operator norm =",gram_norm)
    print("finite max row sum        =",max_rowsum)
    print("analytic row bound        =",mp.nstr(analytic,15))
    assert max_corr_ratio <= 1+mp.mpf("1e-20")
    assert gram_norm <= float(analytic)*(1+1e-10)
    print("PASS")


if __name__=="__main__":
    main()
