import sympy as sp


t, m = sp.symbols('t m', positive=True)
K = 2 * m * sp.log(sp.sech(t / 2))
series = sp.series(K, t, 0, 10).removeO().expand()

expected = (
    -m * t**2 / 4
    + m * t**4 / 96
    - m * t**6 / 1440
    + 17 * m * t**8 / 322560
)
assert sp.simplify(series - expected) == 0

kappa2 = sp.simplify(-2 * series.coeff(t, 2))
kappa4 = sp.simplify(sp.factorial(4) * series.coeff(t, 4))
kappa6 = sp.simplify(-sp.factorial(6) * series.coeff(t, 6))
kappa8 = sp.simplify(sp.factorial(8) * series.coeff(t, 8))
assert kappa2 == m / 2
assert kappa4 == m / 4
assert kappa6 == m / 2
assert kappa8 == 17 * m / 8

mu4 = sp.simplify(kappa4 + 3 * kappa2**2)
mu6 = sp.simplify(kappa6 + 15 * kappa4 * kappa2 + 15 * kappa2**3)
excess = sp.simplify(kappa4 / kappa2**2)

assert mu4 == m * (3 * m + 1) / 4
assert mu6 == m * (15 * m**2 + 15 * m + 4) / 8
assert excess == 1 / m

print('K(t) =', series)
print('kappa_2,4,6,8 =', kappa2, kappa4, kappa6, kappa8)
print('mu4 =', mu4)
print('mu6 =', mu6)
print('excess kurtosis =', excess)
print('standardized Gaussian limit follows from 2m log sech(t/sqrt(2m)) -> -t^2/2')
