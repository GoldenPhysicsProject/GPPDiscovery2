#!/usr/bin/env python3
"""
Exact audits for two Codex/GPT chamber-front identities.

1. Gamma-square convolution semigroup

    rho_a(x) = 4^a/(2*pi*Gamma(2a)) * |Gamma(a+i x)|^2,
    phi_a(t) = sech(t/2)^(2a).

Its even cumulants are

    kappa_{2n}(a) = a * (2^(2n)-1) * |B_{2n}| / n,
    kappa_{2n+1}(a) = 0.

This follows by differentiating

    log phi_a(t) = -2 a log cosh(t/2)

and the Bernoulli expansion of log cosh.

2. Odd-lattice/tanh identity

    sum_{n>=0} 2x/((2n+1)^2+x^2)
      = (pi/2) tanh(pi*x/2).

Writing a=x/2 gives

    term = (a/2) / ((n+1/2)^2+a^2).

The standard digamma series and reflection formula yield

    psi(1/2+i a)-psi(1/2-i a)
      = sum_{n>=0} 2 i a / ((n+1/2)^2+a^2)
      = i*pi*tanh(pi*a),

hence the stated identity.  The numerical audit below checks the original
series independently at high precision.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 80

t = sp.symbols("t", real=True)
a = sp.symbols("a", positive=True)
log_phi = -2 * a * sp.log(sp.cosh(t / 2))

print("Gamma-square even cumulants")
for n in range(1, 11):
    deriv = sp.simplify(sp.diff(log_phi, t, 2 * n).subs(t, 0))
    kappa = sp.simplify((-1) ** n * deriv)
    target = sp.simplify(
        a * (2 ** (2 * n) - 1) * abs(sp.bernoulli(2 * n)) / n
    )
    assert sp.simplify(kappa - target) == 0
    print(f"kappa_{2*n} = {kappa}")

# Odd cumulants vanish by evenness of log_phi.
for n in range(0, 10):
    assert sp.simplify(sp.diff(log_phi, t, 2 * n + 1).subs(t, 0)) == 0

print("\nOdd-lattice / tanh numerical audit")
def odd_lattice_sum(x):
    x = mp.mpf(x)
    return mp.nsum(lambda n: 2 * x / ((2 * n + 1) ** 2 + x ** 2), [0, mp.inf])

def tanh_target(x):
    x = mp.mpf(x)
    return mp.pi / 2 * mp.tanh(mp.pi * x / 2)

for x in [mp.mpf("0.1"), mp.mpf("0.7"), mp.mpf("1"), mp.mpf("2.3"), mp.mpf("7.5")]:
    lhs = odd_lattice_sum(x)
    rhs = tanh_target(x)
    err = abs(lhs - rhs)
    assert err < mp.mpf("1e-70")
    print(f"x={x}: error={mp.nstr(err, 8)}")

# Direct digamma-reflection check at the same points.
print("\nDigamma reflection audit")
for x in [mp.mpf("0.1"), mp.mpf("0.7"), mp.mpf("1"), mp.mpf("2.3"), mp.mpf("7.5")]:
    aa = x / 2
    lhs = mp.digamma(mp.mpf("0.5") + 1j * aa) - mp.digamma(mp.mpf("0.5") - 1j * aa)
    rhs = 1j * mp.pi * mp.tanh(mp.pi * aa)
    err = abs(lhs - rhs)
    assert err < mp.mpf("1e-70")
    print(f"x={x}: error={mp.nstr(err, 8)}")

print("\nPASS")
