"""Fast numerical audit of the raised-box positive-regulator DCT frontier.

Discovery support only, not a proof.  We evaluate

    J_eps(S,T) = int_{Delta_3} (S x1 x3 + T x2 x4)^(-eps) dx1 dx2 dx3

and compare with J_0 = 1/6.  We also check the certified one-channel majorant

    int_{Delta_3} [1 + (S x1 x3)^(-delta)]
      = 1/6 + S^(-delta) Gamma(1-delta)^2 / Gamma(4-2 delta).

The affine simplex is parameterized by the unit cube:
    x1 = u,
    x2 = (1-u) v,
    x3 = (1-u)(1-v) w,
    x4 = (1-u)(1-v)(1-w),
with Jacobian (1-u)^2 (1-v).

Gauss-Legendre nodes avoid the singular boundary itself and make the audit quick
and deterministic.  Increasing N gives a direct convergence check for the
integrable endpoint singularities.
"""

from __future__ import annotations

import math
import numpy as np


def nodes_weights(N: int):
    z, w = np.polynomial.legendre.leggauss(N)
    return (z + 1.0) / 2.0, w / 2.0


def simplex_moment(eps: float, S: float = 2.0, T: float = 3.0, N: int = 64) -> float:
    q, wt = nodes_weights(N)
    total = 0.0
    for i, u in enumerate(q):
        one_u = 1.0 - u
        for j, v in enumerate(q):
            one_v = 1.0 - v
            x1 = u
            x2 = one_u * v
            x3 = one_u * one_v * q
            x4 = one_u * one_v * (1.0 - q)
            jac = one_u**2 * one_v
            Q = S * x1 * x3 + T * x2 * x4
            values = np.full_like(q, jac) if eps == 0.0 else jac * Q ** (-eps)
            total += wt[i] * wt[j] * float(np.dot(wt, values))
    return total


def majorant_closed(delta: float, S: float = 2.0) -> float:
    singular = S ** (-delta) * math.gamma(1.0 - delta) ** 2 / math.gamma(4.0 - 2.0 * delta)
    return 1.0 / 6.0 + singular


def majorant_numeric(delta: float, S: float = 2.0, N: int = 96) -> float:
    q, wt = nodes_weights(N)
    total = 0.0
    for i, u in enumerate(q):
        one_u = 1.0 - u
        for j, v in enumerate(q):
            one_v = 1.0 - v
            x1 = u
            x3 = one_u * one_v * q
            jac = one_u**2 * one_v
            values = jac * (1.0 + (S * x1 * x3) ** (-delta))
            total += wt[i] * wt[j] * float(np.dot(wt, values))
    return total


def main() -> None:
    S, T = 2.0, 3.0
    target = 1.0 / 6.0
    print(f"S={S:g}, T={T:g}, target J_0={target:.16g}")
    for eps in (0.20, 0.10, 0.05, 0.02):
        val = simplex_moment(eps, S, T)
        print(f"eps={eps:0.2f}  J={val:.16g}  J-1/6={val-target:+.8e}")

    delta = 0.35
    closed = majorant_closed(delta, S)
    print(f"majorant delta={delta:g}, exact closed form={closed:.16g}")
    for N in (32, 64, 96):
        num = majorant_numeric(delta, S, N=N)
        print(f"  N={N:3d} numeric={num:.16g} abs_err={abs(num-closed):.4e}")


if __name__ == "__main__":
    main()
