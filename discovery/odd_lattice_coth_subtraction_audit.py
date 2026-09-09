#!/usr/bin/env python3
"""Audit the clean full-lattice -> odd-lattice partial-fraction route.

The formal target is

    sum_{n>=0} 2 x / ((2n+1)^2 + x^2)
      = (pi/2) tanh(pi x/2).

This file does not prove the infinite partial-fraction theorem.  It isolates the exact
algebra needed once the standard full-lattice identity

    sum_{n>=1} 2 x/(n^2+x^2) = pi*coth(pi*x) - 1/x

has been obtained from the certified sinh Weierstrass product.  Subtracting its even
subsequence reduces the target to a rational hyperbolic duplication identity.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def symbolic_duplication_check() -> None:
    q = sp.symbols("q", positive=True)
    # q = exp(pi*x).  Then coth(pi*x), coth(pi*x/2), tanh(pi*x/2)
    # are rational functions of q.
    coth_full = (q**2 + 1) / (q**2 - 1)
    coth_half = (q + 1) / (q - 1)
    tanh_half = (q - 1) / (q + 1)
    defect = sp.factor(coth_full - sp.Rational(1, 2) * coth_half
                       - sp.Rational(1, 2) * tanh_half)
    assert defect == 0


def odd_partial_sum(x: mp.mpf, nmax: int) -> mp.mpf:
    return mp.fsum(2*x / ((2*n + 1)**2 + x*x) for n in range(nmax))


def main() -> None:
    symbolic_duplication_check()
    mp.mp.dps = 80
    for x in [mp.mpf("0.125"), mp.mpf("0.7"), mp.mpf("2.3"), mp.mpf("9.0")]:
        target = mp.pi/2 * mp.tanh(mp.pi*x/2)
        approx = odd_partial_sum(x, 200000)
        # elementary tail comparison: denominator >= (2n+1)^2, hence
        # tail <= 2|x| sum_{n>=N}(2n+1)^(-2).
        N = 200000
        tail_bound = abs(x)/2 * mp.polygamma(1, mp.mpf(N) + mp.mpf("0.5"))
        defect = abs(target - approx)
        assert defect <= tail_bound
        print(x, defect, tail_bound)

    print("PASS: odd-lattice target is exactly the full-lattice coth identity minus its even subsequence")
    print("LEAN BLOCKER: derive/log-differentiate the full-lattice partial fraction from SinhWeierstrassProduct with justified limit differentiation")


if __name__ == "__main__":
    main()
