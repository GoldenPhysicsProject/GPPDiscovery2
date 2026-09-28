#!/usr/bin/env python3
"""No-zero-data controls for the zeta coherent-state information geometry."""

from __future__ import annotations
import json
import mpmath as mp

mp.mp.dps = 60

def L2(x):
    f = lambda y: mp.log(mp.zeta(y))
    return mp.diff(f, x, 2)

def curvature(r):
    x = mp.mpf(1) + 2*mp.mpf(r)
    g = L2(x)
    lam = 4*g
    h = lambda y: mp.log(4*mp.diff(lambda z: mp.log(mp.zeta(z)), y, 2))
    d2r = 4*mp.diff(h, x, 2)
    K = -(1/(2*lam))*d2r
    At = -mp.diff(lambda y: mp.log(mp.zeta(y)), x, 1)
    return {
        "r": float(r),
        "g": float(g),
        "metric_lambda": float(lam),
        "gaussian_curvature": float(K),
        "berry_A_t": float(At),
        "berry_field_over_area": -0.5,
    }

def main():
    rows=[curvature(r) for r in (1,0.5,0.2,0.1,0.05,0.02,0.01)]
    print(json.dumps({
        "uses_riemann_zero_data": False,
        "metric": "ds^2 = 4 (log zeta)''(1+2r) (dr^2+dt^2)",
        "rows": rows
    }, indent=2))

if __name__=="__main__":
    main()
