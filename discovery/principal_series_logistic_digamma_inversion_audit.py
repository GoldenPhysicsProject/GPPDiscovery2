#!/usr/bin/env python3
"""Audit an exact logistic inversion representation for the principal-series score.

Let
    mu(u) = (pi/2) sech^2(pi u),
    D(t)  = Re psi(1/2+i t) - psi(1/2),
    q(t)  = Im psi(1/2+i t).

The classical logistic/digamma inversion formula

    psi(x) = integral_R mu(u) log(x-1/2+i u) du

specialized to x=1/2+i t gives the single complex logarithmic-potential identity

    psi(1/2+i t) = E_mu[log(i(t+U))].

Taking real and imaginary parts yields

    D(t) = E_mu[log|t+U| - log|U|],
    q(t) = (pi/2) E_mu[sign(t+U)]
         = (pi/2) tanh(pi t).

Thus the Barnes phase law and the real digamma score are the imaginary and real
projections of the same logistic logarithmic potential.  Differentiating the real
part (in principal-value sense) also gives

    D'(t) = PV E_mu[1/(t+U)].

This script numerically audits the complex inversion and both projections at high
precision.  The identities themselves are analytic consequences of the inversion
formula; the numerical checks are regression tests, not the proof.
"""

import mpmath as mp

mp.mp.dps = 70
pi = mp.pi
half = mp.mpf("0.5")
psi_half = mp.digamma(half)


def mu(u):
    return (pi / 2) / mp.cosh(pi * u) ** 2


def digamma_inversion(t):
    """E_mu log(i(t+U)), split at the logarithmic singularity U=-t."""
    t = mp.mpf(t)
    singular = -t
    f = lambda u: mu(u) * mp.log(1j * (t + u))
    return mp.quad(f, [-mp.inf, singular, mp.inf])


def real_potential(t):
    t = mp.mpf(t)
    singular = -t
    f = lambda u: mu(u) * (mp.log(abs(t + u)) - mp.log(abs(u)))
    # Split at U=0 and U=-t; deduplicate/sort finite breakpoints.
    points = sorted(set([mp.mpf("0"), singular]))
    intervals = [-mp.inf] + points + [mp.inf]
    return mp.quad(f, intervals)


def phase_from_cdf(t):
    t = mp.mpf(t)
    return (pi / 2) * mp.tanh(pi * t)


samples = [mp.mpf("0"), mp.mpf("0.2"), mp.mpf("0.7"), mp.mpf("1.5")]
for t in samples:
    inv = digamma_inversion(t)
    target = mp.digamma(half + 1j * t)
    D_target = mp.re(target) - psi_half
    q_target = mp.im(target)
    D_potential = real_potential(t)
    q_cdf = phase_from_cdf(t)

    errs = {
        "complex inversion": abs(inv - target),
        "real logarithmic potential": abs(D_potential - D_target),
        "phase/CDF projection": abs(q_cdf - q_target),
    }

    print(f"t={mp.nstr(t, 8)}")
    print("  psi inversion error       =", mp.nstr(errs["complex inversion"], 8))
    print("  real-potential error      =", mp.nstr(errs["real logarithmic potential"], 8))
    print("  phase/CDF error           =", mp.nstr(errs["phase/CDF projection"], 8))

    for err in errs.values():
        assert err < mp.mpf("1e-55")

print("PASS: logistic digamma inversion and its real/phase projections agree at high precision.")
