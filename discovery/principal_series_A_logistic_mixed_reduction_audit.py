#!/usr/bin/env python3
"""Audit the last principal-series A4 mixed moment reduction.

Definitions
-----------
p(t)  = 8 t / sinh(2*pi*t)
mu(t) = (pi/2) sech^2(pi*t)
D(t)  = Re psi(1/2+i t) - psi(1/2)
q(t)  = (pi/2) tanh(pi*t)
A     = E_p[D^2 q^2]

Exact density identity:
    p(t) q(t)^2 = -t mu'(t).
Hence, after integration by parts (boundary term vanishes),
    A = E_mu[D^2] + 2 E_mu[t D D'].

The first term is already exact:
    E_mu[D^2] = 2 - 4 log 2 + 4 log^2 2 - pi^2/12.

Writing
    k(x)   = 1/(2 sinh(x/2)),
    phi(x) = x k(x) = x/(2 sinh(x/2)),
we have
    D(t)  = int_0^inf k(x) (1-cos(tx)) dx,
    D'(t) = int_0^inf phi(y) sin(ty) dy,
and because mu-hat(s)=phi(s),
    E_mu[t sin(ty)] = -phi'(y).
Therefore the remaining mixed term K=E_mu[t D D'] has the deterministic
hyperbolic two-kernel representation

 K = int_0^inf int_0^inf k(x) phi(y)
       [-phi'(y) + (phi'(y+x)+phi'(y-x))/2] dx dy.

This script verifies the integration-by-parts reduction and the conjectural
closed form numerically.  IMPORTANT: the final closed form for K/A is still
DISCOVERY EVIDENCE, not an analytic proof.
"""

import mpmath as mp

mp.mp.dps = 70
pi = mp.pi
log2 = mp.log(2)


def p(t):
    if t == 0:
        return 4 / pi
    return 8 * t / mp.sinh(2 * pi * t)


def mu(t):
    return (pi / 2) / mp.cosh(pi * t) ** 2


def q(t):
    return (pi / 2) * mp.tanh(pi * t)


def D(t):
    return mp.re(mp.digamma(mp.mpf('0.5') + 1j * t)) - mp.digamma(mp.mpf('0.5'))


def Dp(t):
    return mp.re(1j * mp.polygamma(1, mp.mpf('0.5') + 1j * t))


def even_integral(f):
    # Breaks help high-precision quadrature near the origin and in the tail.
    return 2 * mp.quad(f, [0, mp.mpf('0.25'), 1, 3, 8, mp.inf])


A_num = even_integral(lambda t: p(t) * D(t) ** 2 * q(t) ** 2)
EmuD2_num = even_integral(lambda t: mu(t) * D(t) ** 2)
K_num = even_integral(lambda t: mu(t) * t * D(t) * Dp(t))

EmuD2_exact = 2 - 4 * log2 + 4 * log2**2 - pi**2 / 12
K_candidate = -mp.mpf(3) / 4 + log2 + pi**2 / 24
A_candidate = mp.mpf(1) / 2 - 2 * log2 + 4 * log2**2

print("A numerical                 =", mp.nstr(A_num, 65))
print("E_mu[D^2] numerical         =", mp.nstr(EmuD2_num, 65))
print("E_mu[D^2] exact             =", mp.nstr(EmuD2_exact, 65))
print("K=E_mu[t D D'] numerical    =", mp.nstr(K_num, 65))
print("K candidate (UNPROVED)      =", mp.nstr(K_candidate, 65))
print("A from exact reduction       =", mp.nstr(EmuD2_num + 2 * K_num, 65))
print("A candidate (UNPROVED)      =", mp.nstr(A_candidate, 65))

checks = {
    "E_mu[D^2] exact": abs(EmuD2_num - EmuD2_exact),
    "A = E_mu[D^2]+2K": abs(A_num - (EmuD2_num + 2 * K_num)),
    "K candidate numerical": abs(K_num - K_candidate),
    "A candidate numerical": abs(A_num - A_candidate),
}
for label, err in checks.items():
    print(f"{label:28s} error = {mp.nstr(err, 8)}")

# The first two checks are exact-identity audits; the latter two only certify
# high-precision agreement with the discovery candidates.
assert checks["E_mu[D^2] exact"] < mp.mpf('1e-55')
assert checks["A = E_mu[D^2]+2K"] < mp.mpf('1e-55')
assert checks["K candidate numerical"] < mp.mpf('1e-55')
assert checks["A candidate numerical"] < mp.mpf('1e-55')

print("PASS: exact A->logistic mixed reduction verified numerically; closed form remains unproved.")
