#!/usr/bin/env python3
"""
Euler-local restriction of the odd semilocal Weil form.

Purpose
-------
The unrestricted LMI feasible set for the explicit-formula coefficient vector is large.
This script asks how much freedom remains after imposing the degree-one Euler law

    b(p^k) = log(p) * alpha_p^k,
    b(n)   = 0 for non-prime-powers.

It reproduces the zeta odd-sector matrix directly from the zero-free side and then:
  1. tests random signed perturbations alpha_p = 1 +/- eps*d;
  2. scans the one-parameter coherent path alpha_p = alpha for all p.

No zero list is used. Numerical only; not interval certified and not an RH proof.
"""

import math
import numpy as np
from numpy.polynomial.legendre import leggauss

GAMMA_E = 0.5772156649015328606

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def prime_power_base(n):
    for p in range(2, n+1):
        if n % p == 0:
            if not is_prime(p):
                continue
            m = n
            while m % p == 0:
                m //= p
            return p if m == 1 else None
    return None

def Gsym_matrix(N, L, u):
    if u >= 2*L:
        return np.zeros((N,N))
    a = np.arange(1, N+1) * np.pi / L
    lo, hi = -L, L-u
    aj, ak = a[:,None], a[None,:]
    def I(c,d):
        with np.errstate(divide="ignore", invalid="ignore"):
            out = (np.sin(c+d*hi)-np.sin(c+d*lo))/d
        return np.where(np.abs(d)<1e-12, np.cos(c)*(hi-lo), out)
    C = 0.5*(I(aj*u,aj-ak)-I(aj*u,aj+ak))
    return 0.5*(C+C.T)

def arch_matrix(lam,N,nq=800):
    L = math.log(lam)
    G0 = L*np.eye(N)
    t,w = leggauss(nq)
    us = L*(t+1)
    ws = L*w
    W = (-math.log(math.pi)-GAMMA_E)*G0
    for u,wt in zip(us,ws):
        Gu = Gsym_matrix(N,L,u)
        W += wt*2*(math.exp(-2*u)*G0-math.exp(-u/2)*Gu)/(-math.expm1(-2*u))
    W += -G0*math.log(-math.expm1(-4*L))
    return L,0.5*(W+W.T)

def euler_matrix(lam,N,alpha_by_prime,nq=800):
    L,W = arch_matrix(lam,N,nq)
    maxn = int(math.floor(lam**2))
    A = W.copy()
    for p,alpha in alpha_by_prime.items():
        k=1
        while p**k <= maxn and math.log(p**k) < 2*L:
            n=p**k
            b=math.log(p)*(alpha**k)
            A -= 2*b/math.sqrt(n)*Gsym_matrix(N,L,math.log(n))
            k += 1
    return L,0.5*(A+A.T)

def min_eig(lam,N,alpha_by_prime,nq=800):
    L,A=euler_matrix(lam,N,alpha_by_prime,nq)
    return np.linalg.eigvalsh(A/L)[0]

def visible_primes(lam):
    return [p for p in range(2,int(math.floor(lam**2))+1)
            if is_prime(p) and math.log(p)<2*math.log(lam)]

def random_local_test(lam,N=14,eps=1e-3,trials=100,seed=0):
    ps=visible_primes(lam)
    base={p:1.0 for p in ps}
    baseval=min_eig(lam,N,base)
    rng=np.random.default_rng(seed)
    vals=[]
    for _ in range(trials):
        d=rng.normal(size=len(ps)); d/=np.linalg.norm(d)
        vals.append((
            min_eig(lam,N,{p:1+eps*d[i] for i,p in enumerate(ps)},nq=400),
            min_eig(lam,N,{p:1-eps*d[i] for i,p in enumerate(ps)},nq=400),
        ))
    arr=np.array(vals)
    return ps,baseval,arr

if __name__ == "__main__":
    for lam in [3.0,4.0,5.0,6.0]:
        ps,base,arr=random_local_test(lam)
        print(f"lambda={lam:.1f} primes={ps}")
        print(f"  alpha_p=1 min eig: {base:.6e}")
        print(f"  eps=1e-3 random signed perturbations: "
              f"max(+d)={arr[:,0].max():.6e}, max(-d)={arr[:,1].max():.6e}, "
              f"positive counts=({np.sum(arr[:,0]>1e-9)},{np.sum(arr[:,1]>1e-9)})")
        print("  common-alpha scan")
        for alpha in [0.8,0.9,1.0,1.1,1.2]:
            v=min_eig(lam,14,{p:alpha for p in ps},nq=500)
            print(f"    alpha={alpha:.1f}: {v:.6e}")
