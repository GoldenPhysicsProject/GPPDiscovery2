"""Executable audit for the all-order continuous Gamma-chamber cumulants.

For phi_c(t)=sech(t/2)^(2c), the cumulant generating logarithm is
    log phi_c(t) = -2 c log cosh(t/2).
Using the Bernoulli expansion of log cosh gives
    kappa_{2n}(c) = (-1)^(n+1) c (2^(2n)-1) B_{2n}/n,
with odd cumulants zero.

This is discovery support: it checks the closed formula against symbolic Taylor
coefficients and the already-derived low-order moments/cumulants. It does not
replace a Lean proof of the analytic Bernoulli expansion.
"""

import sympy as sp


t, c = sp.symbols("t c")
log_phi = -2 * c * sp.log(sp.cosh(t / 2))


def bernoulli_cumulant(n: int):
    return sp.simplify(
        (-1) ** (n + 1) * c * (2 ** (2 * n) - 1) * sp.bernoulli(2 * n) / n
    )


def taylor_cumulant(n: int):
    order = 2 * n
    coeff = sp.expand(sp.series(log_phi, t, 0, order + 1).removeO()).coeff(t, order)
    # log phi(t) = sum kappa_m (i t)^m / m!
    return sp.simplify(coeff * sp.factorial(order) / ((-1) ** n))


for n in range(1, 9):
    lhs = taylor_cumulant(n)
    rhs = bernoulli_cumulant(n)
    assert sp.simplify(lhs - rhs) == 0, (n, lhs, rhs)
    print(f"kappa_{2*n}(c) = {sp.factor(rhs)}")

expected = {
    1: c / 2,
    2: c / 4,
    3: c / 2,
    4: sp.Rational(17, 8) * c,
    5: sp.Rational(31, 2) * c,
    6: sp.Rational(691, 4) * c,
}
for n, value in expected.items():
    assert sp.simplify(bernoulli_cumulant(n) - value) == 0

print("all checks passed")
