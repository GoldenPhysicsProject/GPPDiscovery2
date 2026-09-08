#!/usr/bin/env python3
"""Exact antisymmetric Barnes phase law for the principal-series spectral measure.

Codex/GPT discovery audit only. This file does not inspect or depend on Claude work.

For the normalized Barnes/celestial probability density

    p(t) = 8 t / sinh(2*pi*t),        t in R,

define

    q(t) = Im[psi(1/2 + i t) - psi(1/2)]
         = (pi/2) tanh(pi t)

by digamma reflection. With x=pi*t and y=tanh(x), the positive-half
pushforward is

    p(t) dt = 4 artanh(y)/(pi^2 y) dy,       0 < y < 1,
    q = (pi/2) y.

Hence q has symmetric compact support |q|<pi/2 and density

    f_Q(q) = 4/(pi^2 |q|) artanh(2|q|/pi).

For n>=1,

    E[q^(2n)] = 2^(2-2n) pi^(2n-2) Hodd(n)/n,
    Hodd(n) = sum_{k=0}^{n-1} 1/(2k+1).

The first cases are E[q^2]=1 and E[q^4]=pi^2/6.

For the antisymmetric Barnes deformation

    K(r,h) = (r^2-h^2)/(2 r (2r+1)),

K_hhhh/K=0 at r=1/2,h=0. If R4 is the fourth symmetric logarithmic
score, Faa di Bruno gives

    0 = E[160 q^4 + 16 q q'' + R4].

The same pushforward gives E[q q'']=-2*pi^2/3, hence

    E[R4] = -16*pi^2.

This is exact phase-sector infrastructure for the A4 digamma moment problem;
it is not an A4 proof.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def p(t: mp.mpf) -> mp.mpf:
    if t == 0:
        return 4 / mp.pi
    return 8 * t / mp.sinh(2 * mp.pi * t)


def q(t: mp.mpf) -> mp.mpf:
    return (mp.pi / 2) * mp.tanh(mp.pi * t)


def qpp(t: mp.mpf) -> mp.mpf:
    x = mp.pi * t
    return -(mp.pi**3) * (1 / mp.cosh(x) ** 2) * mp.tanh(x)


def even_expectation(f):
    return 2 * mp.quad(lambda x: p(x) * f(x), [0, 0.5, 1, 2, 4, mp.inf])


def hodd(n: int):
    return sp.simplify(sum(sp.Rational(1, 2 * k + 1) for k in range(n)))


def q_even_moment_exact(n: int):
    return sp.simplify(
        sp.Rational(2) ** (2 - 2 * n)
        * sp.pi ** (2 * n - 2)
        / n
        * hodd(n)
    )


def main() -> None:
    mp.mp.dps = 80

    k = sp.symbols("k", integer=True, nonnegative=True)
    nn = sp.symbols("nn", integer=True, positive=True)
    telescoping = sp.simplify(
        1 / ((2 * k + 1) * (2 * k + 2 * nn + 1))
        - sp.Rational(1, 2) / nn
        * (1 / (2 * k + 1) - 1 / (2 * k + 2 * nn + 1))
    )
    assert telescoping == 0

    m2 = q_even_moment_exact(1)
    m4 = q_even_moment_exact(2)
    m6 = q_even_moment_exact(3)
    assert m2 == 1
    assert sp.simplify(m4 - sp.pi**2 / 6) == 0
    assert sp.simplify(m6 - 23 * sp.pi**4 / 540) == 0

    r, h = sp.symbols("r h", positive=True, real=True)
    Krh = (r**2 - h**2) / (2 * r * (2 * r + 1))
    base = {r: sp.Rational(1, 2), h: 0}
    K0 = sp.simplify(Krh.subs(base))
    h2_ratio = sp.simplify(sp.diff(Krh, h, 2).subs(base) / K0)
    h4_ratio = sp.simplify(sp.diff(Krh, h, 4).subs(base) / K0)
    assert K0 == sp.Rational(1, 8)
    assert h2_ratio == -8
    assert h4_ratio == 0

    norm = even_expectation(lambda _: mp.mpf(1))
    Eq2 = even_expectation(lambda t: q(t) ** 2)
    Eq4 = even_expectation(lambda t: q(t) ** 4)
    Eqqpp = even_expectation(lambda t: q(t) * qpp(t))

    assert abs(norm - 1) < mp.mpf("1e-60")
    assert abs(Eq2 - 1) < mp.mpf("1e-60")
    assert abs(Eq4 - mp.pi**2 / 6) < mp.mpf("1e-60")
    assert abs(Eqqpp + 2 * mp.pi**2 / 3) < mp.mpf("1e-60")

    ER4 = -160 * Eq4 - 16 * Eqqpp
    assert abs(ER4 + 16 * mp.pi**2) < mp.mpf("1e-60")

    for j in range(1, 7):
        exact = q_even_moment_exact(j)
        exact_mp = mp.mpf(str(sp.N(exact, 80)))
        numeric = even_expectation(lambda t, j=j: q(t) ** (2 * j))
        assert abs(numeric - exact_mp) < mp.mpf("1e-55")

    print("p(t) = 8 t / sinh(2*pi*t)")
    print("q(t) = (pi/2) tanh(pi*t)")
    print("pushforward y=tanh(pi*t): p(t)dt = 4 artanh(y)/(pi^2 y) dy on y>0")
    print("E[q^(2n)] = 2^(2-2n) pi^(2n-2) Hodd(n)/n")
    for j in range(1, 5):
        print(f"  n={j}: {q_even_moment_exact(j)}")
    print("K_hh/K at base =", h2_ratio)
    print("K_hhhh/K at base =", h4_ratio)
    print("E[q^2] =", mp.nstr(Eq2, 40))
    print("E[q^4] =", mp.nstr(Eq4, 40))
    print("E[q q''] =", mp.nstr(Eqqpp, 40))
    print("E[R4] =", mp.nstr(ER4, 40), "= -16*pi^2")
    print("PASS: exact Barnes antisymmetric phase law and moment hierarchy")


if __name__ == "__main__":
    main()
