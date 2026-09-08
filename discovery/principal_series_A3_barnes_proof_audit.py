#!/usr/bin/env python3
"""Analytic Barnes/logistic closure of the principal-series A3 moment.

Codex/GPT discovery audit only. No Claude-owned material is used.

Definitions under the normalized Barnes probability law

  p(t) = 8 t / sinh(2*pi*t),
  D(t) = Re psi(1/2+i t) - psi(1/2),
  q(t) = (pi/2) tanh(pi*t).

The paper's original moment is

  A3 = (1/4) E_p[D^3].

This audit closes the value analytically.

1. Auxiliary logistic Barnes law

   mu(t) = (pi/2) sech^2(pi*t)

   has characteristic function

   phi(x) = x/(2 sinh(x/2)).

   The digamma integral representation gives

   D'(t) = int_0^infty phi(x) sin(t x) dx.

   Therefore, by Fubini and phi(0)=1, phi(infty)=0,

   E_mu[t D'(t)]
     = - int_0^infty phi(x) phi'(x) dx
     = 1/2.

   Barnes' first lemma already gives

   E_mu[D] = 2 log 2 - 1.

   Since

   p q^2 = -t mu'(t),        p q = 4 t mu(t),

   integration by parts yields the exact mixed moments

   M := E_p[D q^2] = E_mu[D] + E_mu[t D']
                    = 2 log 2 - 1/2,

   N := E_p[q D'] = 4 E_mu[t D'] = 2.

2. Symmetric/antisymmetric Barnes deformation

   K(r,h) = (r^2-h^2)/(2 r (2r+1)).

   At r=1/2,h=0,

   K_rrr/K = 6,        K_rhh/K = 24.

   Writing R for the common third logarithmic-score term, the two exact
   Faa-di-Bruno identities are

   6  = 8 E[D^3] - 24 M + E[R],
   24 =             - 16 M + 8 N + E[R].

   Eliminating E[R] gives

   E[D^3] = M + N - 9/4 = 2 log 2 - 3/4,

   hence

   A3 = 1/2 log 2 - 3/16.

This turns the previously open/numerical A3 value into an analytic identity.
The executable checks below independently verify every numerical endpoint.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def p(t: mp.mpf) -> mp.mpf:
    return 4 / mp.pi if t == 0 else 8 * t / mp.sinh(2 * mp.pi * t)


def mu(t: mp.mpf) -> mp.mpf:
    return (mp.pi / 2) * mp.sech(mp.pi * t) ** 2


def D(t: mp.mpf) -> mp.mpf:
    z = mp.mpf("0.5") + 1j * t
    return mp.re(mp.digamma(z)) - mp.digamma(mp.mpf("0.5"))


def Dp(t: mp.mpf) -> mp.mpf:
    z = mp.mpf("0.5") + 1j * t
    return -mp.im(mp.polygamma(1, z))


def q(t: mp.mpf) -> mp.mpf:
    return (mp.pi / 2) * mp.tanh(mp.pi * t)


def even_integral(weight, f):
    return 2 * mp.quad(lambda x: weight(x) * f(x), [0, 0.5, 1, 2, 4, mp.inf])


def main() -> None:
    L = sp.log(2)

    # Exact Barnes derivative ratios.
    r, h = sp.symbols("r h", positive=True, real=True)
    K = (r**2 - h**2) / (2 * r * (2 * r + 1))
    base = {r: sp.Rational(1, 2), h: 0}
    K0 = sp.simplify(K.subs(base))
    rrr = sp.simplify(sp.diff(K, r, 3).subs(base) / K0)
    rhh = sp.simplify(sp.diff(K, r, h, 2).subs(base) / K0)
    assert K0 == sp.Rational(1, 8)
    assert rrr == 6
    assert rhh == 24

    # Exact logistic/Fourier mixed-moment reduction.
    Emu_D = 2 * L - 1
    Emu_tDp = sp.Rational(1, 2)
    M = sp.simplify(Emu_D + Emu_tDp)
    N = sp.simplify(4 * Emu_tDp)
    assert sp.simplify(M - (2 * L - sp.Rational(1, 2))) == 0
    assert N == 2

    # Eliminate the common third logarithmic-score nuisance R.
    X, R = sp.symbols("X R", real=True)
    eq_rrr = sp.Eq(8 * X - 24 * M + R, rrr)
    eq_rhh = sp.Eq(-16 * M + 8 * N + R, rhh)
    R_from_rhh = sp.solve(eq_rhh, R)[0]
    ED3 = sp.simplify(sp.solve(eq_rrr.subs(R, R_from_rhh), X)[0])
    A3 = sp.simplify(ED3 / 4)
    assert sp.simplify(ED3 - (2 * L - sp.Rational(3, 4))) == 0
    assert sp.simplify(A3 - (L / 2 - sp.Rational(3, 16))) == 0

    # Independent high-precision checks of the defining expectations.
    mp.mp.dps = 70
    Emu_D_num = even_integral(mu, D)
    Emu_tDp_num = even_integral(mu, lambda t: t * Dp(t))
    M_num = even_integral(p, lambda t: D(t) * q(t) ** 2)
    N_num = even_integral(p, lambda t: q(t) * Dp(t))
    ED3_num = even_integral(p, lambda t: D(t) ** 3)

    assert abs(Emu_D_num - (2 * mp.log(2) - 1)) < mp.mpf("1e-55")
    assert abs(Emu_tDp_num - mp.mpf("0.5")) < mp.mpf("1e-55")
    assert abs(M_num - (2 * mp.log(2) - mp.mpf("0.5"))) < mp.mpf("1e-55")
    assert abs(N_num - 2) < mp.mpf("1e-55")
    assert abs(ED3_num - (2 * mp.log(2) - mp.mpf("0.75"))) < mp.mpf("1e-55")

    print("Barnes derivative ratios:")
    print("  K_rrr/K =", rrr)
    print("  K_rhh/K =", rhh)
    print("Exact logistic mixed moments:")
    print("  E_mu[D]    =", Emu_D)
    print("  E_mu[t D'] =", Emu_tDp)
    print("  M=E_p[D q^2] =", M)
    print("  N=E_p[q D']  =", N)
    print("Third principal-series moment:")
    print("  E_p[D^3] =", ED3)
    print("  A3 =", A3)
    print("PASS: A3 = log(2)/2 - 3/16 analytically")


if __name__ == "__main__":
    main()
