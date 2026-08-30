"""Numerical audit of the raised-box positive-regulator DCT frontier.

This is discovery support, not a proof.  It evaluates the concrete affine-simplex
moment

    J_eps(S,T) = int_{Delta_3} (S x1 x3 + T x2 x4)^(-eps) dx1 dx2 dx3

in unit-cube coordinates and compares it with J_0 = 1/6.  It also checks the
closed integral of the one-channel majorant used by the Lean development:

    int_{Delta_3} [1 + (S x1 x3)^(-delta)]
      = 1/6 + S^(-delta) Gamma(1-delta)^2 / Gamma(4-2 delta).

The coordinate map is
    x1 = u,
    x2 = (1-u) v,
    x3 = (1-u)(1-v) w,
    x4 = (1-u)(1-v)(1-w),
with Jacobian (1-u)^2 (1-v).
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 35


def barycentric(u, v, w):
    x1 = u
    x2 = (1 - u) * v
    x3 = (1 - u) * (1 - v) * w
    x4 = (1 - u) * (1 - v) * (1 - w)
    jac = (1 - u) ** 2 * (1 - v)
    return x1, x2, x3, x4, jac


def simplex_moment(eps, S=mp.mpf(2), T=mp.mpf(3)):
    eps, S, T = map(mp.mpf, (eps, S, T))

    def fu(u):
        def fv(v):
            def fw(w):
                x1, x2, x3, x4, jac = barycentric(u, v, w)
                Q = S * x1 * x3 + T * x2 * x4
                if eps == 0:
                    return jac
                return jac * Q ** (-eps)

            return mp.quad(fw, [0, 1])

        return mp.quad(fv, [0, 1])

    return mp.quad(fu, [0, 1])


def majorant_closed(delta, S=mp.mpf(2)):
    delta, S = map(mp.mpf, (delta, S))
    singular = S ** (-delta) * mp.gamma(1 - delta) ** 2 / mp.gamma(4 - 2 * delta)
    return mp.mpf(1) / 6 + singular


def majorant_numeric(delta, S=mp.mpf(2)):
    delta, S = map(mp.mpf, (delta, S))

    def fu(u):
        def fv(v):
            def fw(w):
                x1, _, x3, _, jac = barycentric(u, v, w)
                return jac * (1 + (S * x1 * x3) ** (-delta))

            return mp.quad(fw, [0, 1])

        return mp.quad(fv, [0, 1])

    return mp.quad(fu, [0, 1])


def main():
    S, T = mp.mpf(2), mp.mpf(3)
    target = mp.mpf(1) / 6
    print(f"S={S}, T={T}, target J_0={mp.nstr(target, 18)}")
    for eps in ("0.20", "0.10", "0.05", "0.02"):
        val = simplex_moment(eps, S, T)
        print(
            "eps=", eps,
            " J=", mp.nstr(val, 18),
            " J-1/6=", mp.nstr(val - target, 10),
        )

    delta = mp.mpf("0.35")
    num = majorant_numeric(delta, S)
    closed = majorant_closed(delta, S)
    print("majorant delta=", delta)
    print(" numeric =", mp.nstr(num, 18))
    print(" closed  =", mp.nstr(closed, 18))
    print(" abs err =", mp.nstr(abs(num - closed), 8))


if __name__ == "__main__":
    main()
