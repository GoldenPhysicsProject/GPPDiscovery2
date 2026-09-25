#!/usr/bin/env python3
"""Numerical checks for the arithmetic relative-Higgs VEV.

Validation only; the mathematical proofs are in
RH_CALLIAS_HIGGS_WITTEN_2026-09-24.md.
"""

import math
import mpmath as mp
import numpy as np

mp.mp.dps = 50
V = float(-mp.zeta(mp.mpf("0.5")))
C0 = math.sqrt(2.0) - 1.0

def partial_s(N):
    return sum(1.0 / math.sqrt(n) for n in range(1, N + 1))

def c_boundary(N):
    return 2.0 * math.sqrt(N) - partial_s(N)

def cell_min(N):
    return 2.0 * N / math.sqrt(N + 1.0) - partial_s(N)

if __name__ == "__main__":
    mins = np.array([cell_min(n) for n in range(1, 1000)])
    bdy = np.array([c_boundary(n) for n in range(1, 1000)])
    print("sqrt(2)-1 =", C0)
    print("min first 999 cell minima =", mins.min())
    print("cell minima monotone =", bool(np.all(np.diff(mins) > 0)))
    print("boundary C_N monotone =", bool(np.all(np.diff(bdy) > 0)))
    print("-zeta(1/2) =", V)
    print("C_999 =", bdy[-1], "residual =", V - bdy[-1])

    r = V - bdy
    for k in range(1, 5):
        d = np.diff(r, n=k)
        print(f"(-1)^{k} Delta^{k} residual min =", (((-1) ** k) * d).min())
