#!/usr/bin/env python3
"""Exact-formula S(t) and prime-kick Lyapunov diagnostics.

Uses every prime power n<=exp(T); gamma baseline from the full digamma
series. Numerical float/MP diagnostic ONLY, NOT interval-certified and
NOT an RH proof. Private mathematical derivation: GPP-bridge
work/codex/2026-10-16_RH_strength_scalar_prime_gamma_kick_energy.md.
"""
import argparse
import math
import numpy as np
from mpmath import mp

def run(T):
    mp.dps = 45
    N = math.floor(math.exp(T)) + 1
    sieve = np.ones(N + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(N) + 1):
        if sieve[p]:
            sieve[p*p::p] = False
    lam = np.zeros(N + 1, dtype=float)
    for prime in np.flatnonzero(sieve):
        n = int(prime)
        while n <= N:
            lam[n] = math.log(int(prime))
            n *= int(prime)
    ns = np.flatnonzero(lam)
    ns = ns[(ns >= 2) & (ns <= math.exp(T))]
    t = np.log(ns.astype(float))
    w = lam[ns]/np.sqrt(ns)
    cumw = np.cumsum(w)
    cumwu = np.cumsum(w*t)
    omega0 = float(-mp.euler-mp.pi/2-3*mp.log(2)-mp.log(mp.pi))
    c = float(mp.polygamma(1,mp.mpf('0.25'))/4)
    W = 8*(np.cosh(t/2)-1) + omega0*t/2 + c
    Wprime = 4*np.sinh(t/2) + omega0/2
    for j in range(55):
        a = 2*j+0.5
        W -= np.exp(-a*t)/(a*a)
        Wprime += np.exp(-a*t)/a
    curvature = 2*np.cosh(t/2)-np.exp(-t/2)/(1-np.exp(-2*t))
    S = W - (t*cumw-cumwu)
    slope = Wprime-cumw
    E = 2*curvature*S-slope*slope
    iminS = int(np.argmin(S))
    iminE = int(np.argmin(E))
    print(f'T={T}, {len(ns)} prime-power events, last n={ns[-1]}')
    print(f'minimum S at event: {S[iminS]:.14g}, n={ns[iminS]}')
    print(f'minimum E=2Wsecond*S-slope²: {E[iminE]:.14g}, n={ns[iminE]}')
    print(f'negative E events: {np.count_nonzero(E < 0)}')
    print('FLOAT NUMERICS ONLY. The global kick-barrier remains unproved.')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--T',type=float,default=14.0)
    a=p.parse_args()
    if not (math.log(2)<a.T<=15):
        raise ValueError('Choose log(2)<T<=15 to bound memory use')
    run(a.T)
