"""Exact moment bridge between the celestial spectral weight and the c=1 chamber law.

Codex/GPT discovery artifact only.  No RH claim is made here.

The normalized celestial spectral density is

    rho(x) = (2/pi) * [pi*x/sinh(pi*x)] = 2*x/sinh(pi*x),

with the removable value rho(0)=2/pi.  Using

    1/sinh(pi*x) = 2 * sum_{k>=0} exp(-(2k+1)pi*x),   x>0,

one obtains for n>=0

    M_{2n} = integral_R x^(2n) rho(x) dx
           = 8 Gamma(2n+2)/pi^(2n+2)
             * (1 - 2^(-(2n+2))) * zeta(2n+2).

This audit checks the exact even-zeta reduction, the first moment values, direct high-
precision quadrature, and consistency with the characteristic function

    phi(t) = sech(t/2)^2,

which is the c=1 chamber characteristic function already present elsewhere in the
Codex/GPT track.
"""

from __future__ import annotations

import sympy as sp
import mpmath as mp

mp.mp.dps = 70


def exact_even_moment(n: int) -> sp.Expr:
    n = sp.Integer(n)
    return sp.simplify(
        8 * sp.factorial(2*n + 1) / sp.pi**(2*n + 2)
        * (1 - sp.Rational(1, 2)**(2*n + 2))
        * sp.zeta(2*n + 2)
    )


def rho(x: mp.mpf) -> mp.mpf:
    if x == 0:
        return 2 / mp.pi
    return 2*x / mp.sinh(mp.pi*x)


def numerical_even_moment(n: int) -> mp.mpf:
    f = lambda x: x**(2*n) * rho(x)
    return 2 * mp.quad(f, [0, 1, mp.inf])


def characteristic_from_quadrature(t: mp.mpf) -> mp.mpf:
    f = lambda x: mp.cos(t*x) * rho(x)
    return 2 * mp.quad(f, [0, 1, mp.inf])


def characteristic_closed(t: mp.mpf) -> mp.mpf:
    return mp.sech(t/2)**2


def run() -> None:
    expected = [
        sp.Integer(1),
        sp.Rational(1, 2),
        sp.Integer(1),
        sp.Rational(17, 4),
        sp.Integer(31),
    ]

    for n, target in enumerate(expected):
        got = sp.simplify(exact_even_moment(n))
        assert sp.simplify(got - target) == 0, (n, got, target)

    for n in range(5):
        exact = mp.mpf(str(sp.N(exact_even_moment(n), 70)))
        numeric = numerical_even_moment(n)
        assert mp.almosteq(numeric, exact, rel_eps=mp.mpf("1e-55"), abs_eps=mp.mpf("1e-55")), (n, numeric, exact)

    for t in [mp.mpf("-5"), mp.mpf("-1.25"), mp.mpf("0"), mp.mpf("0.7"), mp.mpf("3")]:
        q = characteristic_from_quadrature(t)
        c = characteristic_closed(t)
        assert mp.almosteq(q, c, rel_eps=mp.mpf("1e-55"), abs_eps=mp.mpf("1e-55")), (t, q, c)

    # Moment/derivative cross-check from phi(t)=sech(t/2)^2.
    t = sp.symbols("t", real=True)
    phi = sp.sech(t/2)**2
    for n in range(5):
        from_phi = sp.simplify((-1)**n * sp.diff(phi, t, 2*n).subs(t, 0))
        assert sp.simplify(from_phi - exact_even_moment(n)) == 0, (n, from_phi, exact_even_moment(n))

    print("PASS: normalized celestial spectral density has total mass 1")
    print("PASS: exact even moments reduce to 1, 1/2, 1, 17/4, 31 through order 8")
    print("PASS: direct 70-digit quadrature agrees with the zeta/Gamma moment formula")
    print("PASS: Fourier characteristic function agrees with sech(t/2)^2")
    print("PASS: characteristic-function derivatives reproduce the exact even moments")
    print("INTERPRETATION: celestial spectral weight and the c=1 chamber law are the same normalized probability law")


if __name__ == "__main__":
    run()
