#!/usr/bin/env python3
"""Quantitative endpoint audit for the shifted sech-convolution primitive.

Formal target in GPPVerify2:
  D_lam(x) = log(cosh(pi*x)) - log(cosh(pi*(lam-x))).

Exact real identity used to avoid branch/asymptotic ambiguity:
  log(cosh y) = |y| - log 2 + R(y),
  R(y) = log(1 + exp(-2|y|)),
with 0 <= R(y) <= exp(-2|y|).

Hence, once x >= max(0,lam),
  D_lam(x) - pi*lam = R(pi*x) - R(pi*(lam-x)),
and
  |D_lam(x)-pi*lam|
    <= exp(-2*pi*x) + exp(-2*pi*(x-lam)).

Once x <= min(0,lam),
  D_lam(x) + pi*lam = R(pi*x) - R(pi*(lam-x)),
and
  |D_lam(x)+pi*lam|
    <= exp(2*pi*x) + exp(-2*pi*(lam-x))
(the two terms are exp(-2|pi*x|), exp(-2|pi*(lam-x)|)).

These bounds are stronger than mere convergence and are designed to be promoted
into Lean before the improper-integral theorem
  integral_R dx/[cosh(pi*x) cosh(pi*(lam-x))] = 2*lam/sinh(pi*lam).
"""

import mpmath as mp

mp.mp.dps = 80


def R(y):
    return mp.log1p(mp.e ** (-2 * abs(y)))


def logcosh_stable(y):
    return abs(y) - mp.log(2) + R(y)


def D(lam, x):
    return logcosh_stable(mp.pi*x) - logcosh_stable(mp.pi*(lam-x))


def endpoint_bound(lam, x):
    return mp.e ** (-2*abs(mp.pi*x)) + mp.e ** (-2*abs(mp.pi*(lam-x)))


def audit(lam):
    print(f"lambda={lam}")
    for x in [5, 10, 20, -5, -10, -20]:
        target = mp.pi*lam if x >= max(0, lam) else (-mp.pi*lam if x <= min(0, lam) else None)
        if target is None:
            continue
        err = abs(D(lam, x) - target)
        bnd = endpoint_bound(lam, x)
        assert err <= bnd * (1 + mp.mpf('1e-60'))
        print(f"  x={x:>3}: error={mp.nstr(err, 8)}  bound={mp.nstr(bnd, 8)}")

    # Independent quadrature check of the eventual convolution value.
    f = lambda x: 1/(mp.cosh(mp.pi*x)*mp.cosh(mp.pi*(lam-x)))
    val = mp.quad(f, [-mp.inf, 0, lam, mp.inf]) if lam > 0 else mp.quad(f, [-mp.inf, lam, 0, mp.inf])
    if lam == 0:
        expected = 2/mp.pi
    else:
        expected = 2*lam/mp.sinh(mp.pi*lam)
    print("  convolution residual =", mp.nstr(abs(val-expected), 12))
    assert mp.almosteq(val, expected)


if __name__ == "__main__":
    for lam in [mp.mpf('-2.3'), mp.mpf('-0.4'), mp.mpf('0'), mp.mpf('0.7'), mp.mpf('3.1')]:
        audit(lam)
