#!/usr/bin/env python3
"""Exact truncation law for the odd-mode chamber Levy kernel.

For y>0 and rates lambda_n=(2n+1)pi, define the positive-half-line mode kernel

    nu_{a,n}(y) = 2 a exp(-lambda_n y) / y.

The infinite sum is a/(y sinh(pi y)).  This audit records the stronger exact
finite-N identity

    sum_{n=0}^{N-1} nu_{a,n}(y)
      = a/(y sinh(pi y)) * (1-exp(-2 pi N y)),

so the tail is exactly exp(-2 pi N y) times the full kernel.  Consequently the
relative truncation error is uniform on every y>=delta>0 with bound
exp(-2 pi N delta).

This does not remove the Levy singularity at y=0; it gives controlled convergence
away from the origin and isolates the remaining local Levy-integrability argument.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


a, y = sp.symbols("a y", positive=True)
N = sp.symbols("N", integer=True, positive=True)
q = sp.exp(-2 * sp.pi * y)

full = a / (y * sp.sinh(sp.pi * y))
finite_closed = (2 * a / y) * sp.exp(-sp.pi * y) * (1 - q**N) / (1 - q)
tail_closed = (2 * a / y) * sp.exp(-(2 * N + 1) * sp.pi * y) / (1 - q)

# Hyperbolic/geometric normalization.
assert sp.simplify(
    2 * sp.exp(-sp.pi * y) / (1 - sp.exp(-2 * sp.pi * y))
    - 1 / sp.sinh(sp.pi * y)
) == 0

# Exact finite sum and exact multiplicative tail law.
assert sp.simplify(finite_closed - full * (1 - sp.exp(-2 * sp.pi * N * y))) == 0
assert sp.simplify(tail_closed - full * sp.exp(-2 * sp.pi * N * y)) == 0
assert sp.simplify(full - finite_closed - tail_closed) == 0

# The Levy condition is locally finite after multiplication by y^2:
# y^2 nu_a(y) -> a/pi as y -> 0+.
assert sp.simplify(sp.limit(y**2 * full, y, 0, dir="+") - a / sp.pi) == 0
# At infinity the kernel decays exponentially; the rescaled limit is exact.
assert sp.simplify(sp.limit(y * sp.exp(sp.pi * y) * full, y, sp.oo) - 2 * a) == 0


def numerical_checks() -> None:
    mp.mp.dps = 80
    for aa in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2.3")]:
        for yy in [mp.mpf("0.07"), mp.mpf("0.4"), mp.mpf("1.7")]:
            exact = aa / (yy * mp.sinh(mp.pi * yy))
            for NN in [1, 2, 5, 12]:
                partial = mp.fsum(
                    2 * aa * mp.e ** (-(2 * n + 1) * mp.pi * yy) / yy
                    for n in range(NN)
                )
                tail = exact - partial
                target_tail = exact * mp.e ** (-2 * mp.pi * NN * yy)
                assert mp.almosteq(tail, target_tail, rel_eps=mp.mpf("1e-70"), abs_eps=mp.mpf("1e-70"))


if __name__ == "__main__":
    numerical_checks()
    print("PASS: exact odd-mode finite-sum/tail law and Levy endpoint asymptotics")
    print("tail/full = exp(-2*pi*N*y)")
    print("uniform on y>=delta: relative error <= exp(-2*pi*N*delta)")
    print("near zero: y^2 nu_a(y) -> a/pi; infinity: y*exp(pi*y)*nu_a(y) -> 2a")
