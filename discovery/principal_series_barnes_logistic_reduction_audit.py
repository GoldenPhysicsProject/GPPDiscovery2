#!/usr/bin/env python3
"""Exact Barnes/logistic reduction for the principal-series A4 frontier.

Codex/GPT discovery audit only. No Claude-owned material is used.

Definitions under the normalized Barnes probability law

  p(t) = 8 t / sinh(2*pi*t),
  D(t) = Re psi(1/2+i t) - psi(1/2),
  q(t) = (pi/2) tanh(pi*t).

The current exact A4 reduction is

  E[D^4] = 2 A + 4 B - C + 25/2 - 3*pi^2/2,

where
  A = E[D^2 q^2],
  B = E[D q D'],
  C = E[(D')^2].

This file proves symbolically, from Barnes' first lemma plus integration by
parts, that B is not an independent analytic target.

Introduce the auxiliary logistic Barnes law

  mu(t) dt = (pi/2) sech^2(pi*t) dt
           = |Gamma(1/2+i t)|^4 /(2*pi) dt.

Barnes' first lemma, with two parameters varied and the other two fixed at
1/2, gives the normalized deformation

  F(a,c) = pi * Gamma(a+1/2) Gamma(c+1/2)
                 / ((a+c) Gamma(a) Gamma(c)).

At a=c=1/2,

  F_a = 2 log 2 - 1,
  F_ac = 2 - 4 log 2 + 4 log^2 2.

The corresponding parameter scores are

  U = psi(1/2+i t)-psi(1/2) = D+i q,
  V = D-i q.

Hence

  E_mu[D] = 2 log 2 - 1,
  E_mu[D^2+q^2] = 2 - 4 log 2 + 4 log^2 2.

Under mu, y=tanh(pi t) is uniform on (-1,1), so

  E_mu[q^2] = pi^2/12.

Therefore the exact unweighted sech norm is

  J0 := integral_R sech^2(pi t) D(t)^2 dt
      = (2/pi) * (2 - 4 log 2 + 4 log^2 2 - pi^2/12).

Finally p(t)q(t)=2*pi*t*sech^2(pi t) and
p(t)q(t)^2=pi^2*t*sech^2(pi t)*tanh(pi t). Integration by parts gives

  B = 2 A - pi J0.

Thus

  B = 2 A - 4 + 8 log 2 - 8 log^2 2 + pi^2/6.

In particular, inserting the current candidate

  A = 1/2 - 2 log 2 + 4 log^2 2

implies analytically

  B = -3 + 4 log 2 + pi^2/6,

exactly the high-precision PSLQ value. Therefore only A and C remain
independent analytic proof targets for A4.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def p(t: mp.mpf) -> mp.mpf:
    return 4 / mp.pi if t == 0 else 8 * t / mp.sinh(2 * mp.pi * t)


def D(t: mp.mpf) -> mp.mpf:
    z = mp.mpf("0.5") + 1j * t
    return mp.re(mp.digamma(z)) - mp.digamma(mp.mpf("0.5"))


def Dp(t: mp.mpf) -> mp.mpf:
    z = mp.mpf("0.5") + 1j * t
    return -mp.im(mp.polygamma(1, z))


def q(t: mp.mpf) -> mp.mpf:
    return (mp.pi / 2) * mp.tanh(mp.pi * t)


def even_integral(f):
    return 2 * mp.quad(f, [0, 0.5, 1, 2, 4, mp.inf])


def main() -> None:
    a, c = sp.symbols("a c", positive=True, real=True)
    half = sp.Rational(1, 2)
    L = sp.log(2)

    # Barnes-first-lemma deformation of the logistic |Gamma(1/2+it)|^4 law.
    F = sp.pi * sp.gamma(a + half) * sp.gamma(c + half) / (
        (a + c) * sp.gamma(a) * sp.gamma(c)
    )
    base = {a: half, c: half}
    assert sp.simplify(F.subs(base)) == 1

    Fa = sp.simplify(sp.diff(F, a).subs(base))
    Fac = sp.simplify(sp.diff(F, a, c).subs(base))
    assert sp.simplify(Fa - (2 * L - 1)) == 0
    assert sp.simplify(Fac - (2 - 4 * L + 4 * L**2)) == 0

    Emu_q2 = sp.pi**2 / 12
    Emu_D2 = sp.simplify(Fac - Emu_q2)
    J0 = sp.simplify((2 / sp.pi) * Emu_D2)
    J0_target = sp.simplify(
        (2 / sp.pi) * (2 - 4 * L + 4 * L**2 - sp.pi**2 / 12)
    )
    assert sp.simplify(J0 - J0_target) == 0

    A = sp.symbols("A", real=True)
    B_from_A = sp.simplify(2 * A - sp.pi * J0)
    B_relation = sp.simplify(
        2 * A - 4 + 8 * L - 8 * L**2 + sp.pi**2 / 6
    )
    assert sp.simplify(B_from_A - B_relation) == 0

    A_candidate = sp.Rational(1, 2) - 2 * L + 4 * L**2
    B_candidate = -3 + 4 * L + sp.pi**2 / 6
    assert sp.simplify(B_from_A.subs(A, A_candidate) - B_candidate) == 0

    # Independent high-precision checks against the defining integrals.
    mp.mp.dps = 80
    J0_num = even_integral(lambda t: mp.sech(mp.pi * t) ** 2 * D(t) ** 2)
    A_num = even_integral(lambda t: p(t) * D(t) ** 2 * q(t) ** 2)
    B_num = even_integral(lambda t: p(t) * D(t) * q(t) * Dp(t))

    J0_mp = (2 / mp.pi) * (
        2 - 4 * mp.log(2) + 4 * mp.log(2) ** 2 - mp.pi**2 / 12
    )
    A_mp = mp.mpf("0.5") - 2 * mp.log(2) + 4 * mp.log(2) ** 2
    B_mp = -3 + 4 * mp.log(2) + mp.pi**2 / 6

    assert abs(J0_num - J0_mp) < mp.mpf("1e-60")
    assert abs(B_num - (2 * A_num - mp.pi * J0_num)) < mp.mpf("1e-60")
    assert abs(A_num - A_mp) < mp.mpf("1e-60")
    assert abs(B_num - B_mp) < mp.mpf("1e-60")

    print("Barnes logistic deformation:")
    print("  F_a  =", Fa)
    print("  F_ac =", Fac)
    print("Exact logistic moments:")
    print("  E_mu[D]  =", sp.simplify(Fa))
    print("  E_mu[D^2] =", Emu_D2)
    print("  J0 = integral sech^2(pi t) D(t)^2 dt =", J0)
    print("Exact integration-by-parts reduction:")
    print("  B = 2 A - pi J0")
    print("    =", B_relation)
    print("Numerical checks:")
    print("  J0 =", mp.nstr(J0_num, 60))
    print("  A  =", mp.nstr(A_num, 60))
    print("  B  =", mp.nstr(B_num, 60))
    print("PASS: B is analytically dependent on A; only A and C remain independent A4 targets")


if __name__ == "__main__":
    main()
