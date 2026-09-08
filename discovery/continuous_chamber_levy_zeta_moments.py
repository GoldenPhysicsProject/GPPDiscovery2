"""Audit the exact Levy-moment / even-zeta formula for continuous sech chambers.

For the symmetric Levy density
    nu_c(x) = c / (|x| sinh(pi |x|)),
its even moments are predicted to equal the chamber cumulants:

    integral_R x^(2n) nu_c(x) dx
      = 4 c Gamma(2n) (1 - 2^(-2n)) zeta(2n) / pi^(2n)
      = (-1)^(n+1) c (2^(2n)-1) B_(2n) / n.

This script verifies the algebraic equivalence through high order and checks the
integral numerically for representative n,c.  This is discovery support only;
termwise integration and the full Levy-Khintchine identity remain separate Lean
formalization targets.
"""

import mpmath as mp
import sympy as sp


mp.mp.dps = 70
n = sp.symbols("n", integer=True, positive=True)
c = sp.symbols("c", positive=True)


def zeta_moment_symbolic(k: int):
    return sp.simplify(
        4 * c * sp.factorial(2 * k - 1)
        * (1 - sp.Rational(1, 2) ** (2 * k))
        * sp.zeta(2 * k) / sp.pi ** (2 * k)
    )


def bernoulli_cumulant(k: int):
    return sp.simplify(
        (-1) ** (k + 1) * c * (2 ** (2 * k) - 1) * sp.bernoulli(2 * k) / k
    )


for k in range(1, 11):
    lhs = sp.expand_func(zeta_moment_symbolic(k))
    rhs = bernoulli_cumulant(k)
    assert sp.simplify(lhs - rhs) == 0, (k, lhs, rhs)
    print(f"n={k}: {sp.factor(rhs)}")


def levy_density(x, cc):
    if x == 0:
        return mp.inf
    return cc / (abs(x) * mp.sinh(mp.pi * abs(x)))


def numerical_even_moment(k: int, cc):
    f = lambda x: x ** (2 * k) * levy_density(x, cc)
    return 2 * mp.quad(f, [0, 1, mp.inf])


def zeta_closed(k: int, cc):
    return (
        4 * cc * mp.factorial(2 * k - 1)
        * (1 - mp.power(2, -2 * k)) * mp.zeta(2 * k)
        / mp.power(mp.pi, 2 * k)
    )


for cc in (mp.mpf("0.2"), mp.mpf("1"), mp.mpf("1.7")):
    for k in range(1, 6):
        num = numerical_even_moment(k, cc)
        exact = zeta_closed(k, cc)
        err = abs(num - exact)
        assert err < mp.mpf("1e-55"), (cc, k, num, exact, err)
        print(f"c={cc}, n={k}, moment={mp.nstr(num, 30)}, err={mp.nstr(err, 5)}")

print("all Levy/zeta moment checks passed")
