#!/usr/bin/env python3
"""Barnes-score bridge for the celestial principal-series digamma moments.

This audit isolates a two-parameter Barnes deformation underlying the moments

    A_k = (1/(2*pi)) int_R P(lambda) D(lambda)^k d lambda,
    P(lambda) = pi*lambda/sinh(pi*lambda),
    D(lambda) = Re psi(1/2 + i lambda/2) - psi(1/2).

After lambda = 2 t and duplication,

    P(2t) = (1/pi) |Gamma(1/2+it)|^2 |Gamma(1+it)|^2.

Introduce

    K(a,c) = (1/(2*pi)) int_R
             [Gamma(a+it) Gamma(c-it)/(Gamma(a)Gamma(c))]
             Gamma(1+it) Gamma(1-it) dt.

Barnes' first lemma gives the exact closed form

    K(a,c) = a*c / ((a+c)*(a+c+1)).

At a=c=1/2, K=1/8.  Along the symmetric deformation a=c=r,
the logarithmic score of the integrand is

    S(t) = 2 [Re psi(1/2+it) - psi(1/2)] = 2 D(2t).

The normalized base probability density is

    p(t) = 8 t / sinh(2*pi*t).

The rational Barnes normalization gives E[S]=1.  Reflection gives

    dS/dr |_{r=1/2} = -pi^2 tanh^2(pi t),

whose expectation under p is exactly -4.  Combining this with
K''/K = E[S^2 + S_r] gives E[S^2]=2, hence

    A_1 = 1/8,   A_2 = 1/8.

This is intended as analytic infrastructure for the higher-moment problem,
especially the newly discovered A4 closed form.  It is not an A4 proof.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def K_closed(a, c):
    return a * c / ((a + c) * (a + c + 1))


def p(t: mp.mpf) -> mp.mpf:
    if t == 0:
        return 4 / mp.pi
    return 8 * t / mp.sinh(2 * mp.pi * t)


def score(t: mp.mpf) -> mp.mpf:
    return 2 * (
        mp.re(mp.digamma(mp.mpf("0.5") + 1j * t))
        - mp.digamma(mp.mpf("0.5"))
    )


def score_r_derivative(t: mp.mpf) -> mp.mpf:
    return -(mp.pi**2) * mp.tanh(mp.pi * t) ** 2


def even_expectation(f):
    return 2 * mp.quad(lambda x: p(x) * f(x), [0, 1, 3, mp.inf])


def main() -> None:
    mp.mp.dps = 80

    # Symbolic Barnes normalization and symmetric derivatives.
    r = sp.symbols("r", positive=True)
    Ksym = sp.simplify(K_closed(r, r))
    assert sp.simplify(Ksym - r / (2 * (2 * r + 1))) == 0

    K0 = sp.simplify(Ksym.subs(r, sp.Rational(1, 2)))
    K1_over_K = sp.simplify(sp.diff(Ksym, r).subs(r, sp.Rational(1, 2)) / K0)
    K2_over_K = sp.simplify(sp.diff(Ksym, r, 2).subs(r, sp.Rational(1, 2)) / K0)

    assert K0 == sp.Rational(1, 8)
    assert K1_over_K == 1
    assert K2_over_K == -2

    # Independent high-precision quadrature checks.
    norm = even_expectation(lambda _: mp.mpf(1))
    ES = even_expectation(score)
    ES2 = even_expectation(lambda t: score(t) ** 2)
    ESr = even_expectation(score_r_derivative)

    assert abs(norm - 1) < mp.mpf("1e-60")
    assert abs(ES - 1) < mp.mpf("1e-60")
    assert abs(ESr + 4) < mp.mpf("1e-60")
    assert abs(ES2 - 2) < mp.mpf("1e-60")

    # Score identity: K''/K = E[S^2 + S_r].
    assert abs(mp.mpf(str(K2_over_K)) - (ES2 + ESr)) < mp.mpf("1e-60")

    A1 = ES / 8  # A1 = (1/4) E[D], D=S/2.
    A2 = ES2 / 16  # A2 = (1/4) E[D^2] = E[S^2]/16.
    assert abs(A1 - mp.mpf(1) / 8) < mp.mpf("1e-60")
    assert abs(A2 - mp.mpf(1) / 8) < mp.mpf("1e-60")

    print("K(a,c) = a*c / ((a+c)*(a+c+1))")
    print("K(1/2,1/2) =", K0)
    print("K'/K at symmetric base =", K1_over_K)
    print("K''/K at symmetric base =", K2_over_K)
    print("E[S] =", mp.nstr(ES, 40))
    print("E[S_r] =", mp.nstr(ESr, 40))
    print("E[S^2] =", mp.nstr(ES2, 40))
    print("A1 =", mp.nstr(A1, 40))
    print("A2 =", mp.nstr(A2, 40))
    print("PASS: Barnes-score bridge exactly recovers A1=A2=1/8")


if __name__ == "__main__":
    main()
