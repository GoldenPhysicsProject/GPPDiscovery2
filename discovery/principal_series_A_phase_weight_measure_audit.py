#!/usr/bin/env python3
"""Exact probability-law reduction for the remaining A4 mixed integral.

Codex/GPT discovery audit only. No Claude-owned material is used.

Definitions
-----------
  p(t) = 8 t / sinh(2*pi*t),
  q(t) = (pi/2) tanh(pi*t),
  D(t) = Re psi(1/2+i t) - psi(1/2).

The remaining fourth-moment obstruction is

  A = E_p[D(t)^2 q(t)^2].

Put y = tanh(pi*t). On t>0,

  p(t) dt = 4 atanh(y)/(pi^2 y) dy,
  q(t)^2 = (pi^2/4) y^2.

Hence

  p(t) q(t)^2 dt = y atanh(y) dy  (t>0).

Because the original measure is even,

  nu(dt) := p(t) q(t)^2 dt

is a probability measure: under y=tanh(pi*t), its pushforward to (-1,1) is

  f_nu(y) = |y| atanh(|y|).

Indeed

  2 int_0^1 y atanh(y) dy = 1.

Therefore the only remaining A4 mixed integral is exactly

  A = 2 int_0^1 y atanh(y)
        D(atanh(y)/pi)^2 dy.

The characteristic function is also explicit.  If

  mu(t) = (pi/2) sech^2(pi*t),
  phi(s) = int exp(i s t) mu(t) dt = s/(2 sinh(s/2)),

then p q^2 = -t mu'(t), so

  chi_nu(s) = phi(s) + s phi'(s).

The y-moments close in a finite odd-harmonic sum:

  E_nu[y^(2n)]
    = 1/(n+1) * sum_{k=0}^n 1/(2k+1),  n>=0.

This is equivalent to the previously derived even-q moment hierarchy, but the
normalized phase-weight law is the useful new formulation: A is now an ordinary
L^2 expectation against a compactly supported probability density.
"""
from __future__ import annotations

import mpmath as mp


def p(t: mp.mpf) -> mp.mpf:
    if t == 0:
        return 4 / mp.pi
    return 8 * t / mp.sinh(2 * mp.pi * t)


def q(t: mp.mpf) -> mp.mpf:
    return (mp.pi / 2) * mp.tanh(mp.pi * t)


def D(t: mp.mpf) -> mp.mpf:
    return mp.re(mp.digamma(mp.mpf("0.5") + 1j * t) - mp.digamma(mp.mpf("0.5")))


def phi(s: mp.mpf) -> mp.mpf:
    if s == 0:
        return mp.mpf(1)
    return s / (2 * mp.sinh(s / 2))


def phi_prime(s: mp.mpf) -> mp.mpf:
    if s == 0:
        return mp.mpf(0)
    return (1 / (2 * mp.sinh(s / 2))
            - s * mp.cosh(s / 2) / (4 * mp.sinh(s / 2) ** 2))


def odd_harmonic(n: int) -> mp.mpf:
    return mp.fsum(mp.mpf(1) / (2 * k + 1) for k in range(n + 1))


def main() -> None:
    mp.mp.dps = 70

    # Normalization of nu = p q^2 dt.
    nu_mass_t = 2 * mp.quad(lambda t: p(t) * q(t) ** 2,
                            [0, mp.mpf("0.5"), 1, 2, 4, mp.inf])
    nu_mass_y = 2 * mp.quad(lambda y: y * mp.atanh(y),
                            [0, mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99"), 1])
    assert abs(nu_mass_t - 1) < mp.mpf("1e-55")
    assert abs(nu_mass_y - 1) < mp.mpf("1e-55")

    # Direct and compact-pushforward evaluations of A.
    A_t = 2 * mp.quad(lambda t: p(t) * q(t) ** 2 * D(t) ** 2,
                      [0, mp.mpf("0.5"), 1, 2, 4, mp.inf])
    A_y = 2 * mp.quad(
        lambda y: y * mp.atanh(y) * D(mp.atanh(y) / mp.pi) ** 2,
        [0, mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99"),
         mp.mpf("0.9999"), 1],
    )
    A_target = mp.mpf("0.5") - 2 * mp.log(2) + 4 * mp.log(2) ** 2
    assert abs(A_t - A_y) < mp.mpf("1e-50")
    assert abs(A_t - A_target) < mp.mpf("1e-50")

    # Characteristic function chi_nu = phi + s phi'.
    for s in [mp.mpf("0.3"), mp.mpf("1.1"), mp.mpf("2.7")]:
        direct = 2 * mp.quad(lambda t: p(t) * q(t) ** 2 * mp.cos(s * t),
                             [0, mp.mpf("0.5"), 1, 2, 4, mp.inf])
        closed = phi(s) + s * phi_prime(s)
        assert abs(direct - closed) < mp.mpf("1e-50")

    # Compact-support moment hierarchy.
    for n in range(7):
        numeric = 2 * mp.quad(lambda y: y ** (2 * n + 1) * mp.atanh(y),
                              [0, mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99"), 1])
        closed = odd_harmonic(n) / (n + 1)
        assert abs(numeric - closed) < mp.mpf("1e-50")

    print("PASS: nu(dt)=p(t)q(t)^2 dt is normalized")
    print("pushforward density on (-1,1): |y| atanh(|y|)")
    print("chi_nu(s)=phi(s)+s phi'(s), phi=s/(2 sinh(s/2))")
    print("E_nu[y^(2n)] = odd_harmonic(n)/(n+1)")
    print("A direct     =", mp.nstr(A_t, 55))
    print("A pushforward=", mp.nstr(A_y, 55))
    print("A candidate  =", mp.nstr(A_target, 55))
    print("NOTE: the final closed form for A remains numerical evidence here, not a proof")


if __name__ == "__main__":
    main()
