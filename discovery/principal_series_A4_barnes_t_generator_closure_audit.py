#!/usr/bin/env python3
"""
Exact Barnes closure of the final principal-series A4 obstruction.

Definitions at the physical point r=1/2, h=0:
  a=r+h, c=r-h,
  mu(t)=(pi/2) sech^2(pi t),
  D(t)=Re psi(1/2+i t)-psi(1/2),
  q(t)=Im psi(1/2+i t)=(pi/2)tanh(pi t).

The normalized Barnes family is
  F(a,c)=pi*Gamma(a+1/2)Gamma(c+1/2)/((a+c)Gamma(a)Gamma(c)),
with F(1/2,1/2)=1.

Using i t Gamma(a+i t)=a[Gamma(a+1+i t)/Gamma(a+1)-Gamma(a+i t)/Gamma(a)]
inside the Barnes integral gives the exact t-weighted generator
  T(a,c)=-i*a*(F(a+1,c)-F(a,c)).

Write ell for the log of the Barnes integrand and use r/h derivatives:
  ell_r = 2D,
  ell_h = 2 i q,
  ell_rh = -2 i D',
  ell_rr = R2.

The h^3 and r^2 h derivatives of T give exact identities for
  Q = E_mu[t q R2] and K = E_mu[t D D'].
Together with integration by parts and the already exact phase moment
  E_mu[t q^3] = pi^2/24,
they close
  K = log 2 - 3/4 + pi^2/24.

Then
  A := E_p[D^2 q^2] = E_mu[D^2] + 2K
     = 1/2 - 2 log 2 + 4 log^2 2,
and the previously exact fourth-score reduction yields
  A4 = 3/8 - log 2 + 2 log^2 2 - pi^2/24.

This script checks the symbolic chain and independently regresses K, A, A4
against high-precision quadrature. It is an executable proof audit; a Lean
formalization would still require the Barnes integral/differentiation layer.
"""

import sympy as sp
import mpmath as mp

r, h = sp.symbols("r h", real=True)
a = r + h
c = r - h
pi = sp.pi
L = sp.log(2)


def F(A, C):
    return (
        pi
        * sp.gamma(A + sp.Rational(1, 2))
        * sp.gamma(C + sp.Rational(1, 2))
        / ((A + C) * sp.gamma(A) * sp.gamma(C))
    )


T = -sp.I * a * (F(a + 1, c) - F(a, c))
physical = {r: sp.Rational(1, 2), h: 0}

pg = {
    sp.polygamma(1, sp.Rational(3, 2)): pi**2 / 2 - 4,
    sp.polygamma(2, sp.Rational(3, 2)): 16 - 14 * sp.zeta(3),
}

H3 = sp.simplify((sp.diff(T, h, 3).subs(physical) / sp.I).xreplace(pg))
R2H = sp.simplify((sp.diff(T, r, 2, h, 1).subs(physical) / sp.I).xreplace(pg))
Frr = sp.simplify(sp.diff(F(a, c), r, 2).subs(physical).xreplace(pg))

assert sp.simplify(H3 + pi**2) == 0
assert sp.simplify(R2H - (7 - 12*L + 8*L**2 - pi**2/3)) == 0
assert sp.simplify(Frr - (8 - 16*L + 16*L**2 - 2*pi**2/3)) == 0

E_D2 = 2 - 4*L + 4*L**2 - pi**2/12
E_R2 = sp.simplify(Frr - 4 * E_D2)
assert sp.simplify(E_R2 + pi**2/3) == 0

Q3 = pi**2 / 24
Q = sp.simplify((H3 + 8*Q3 - E_R2) / 2)
assert sp.simplify(Q + pi**2/6) == 0

K = sp.simplify((2*E_D2 + E_R2 - 2*Q - R2H) / 4)
K_target = L - sp.Rational(3, 4) + pi**2/24
assert sp.simplify(K - K_target) == 0

A = sp.simplify(E_D2 + 2*K)
A_target = sp.Rational(1, 2) - 2*L + 4*L**2
assert sp.simplify(A - A_target) == 0

E_D4 = sp.simplify(10*A - sp.Rational(7, 2) + 16*L - 32*L**2 - pi**2/6)
A4 = sp.simplify(E_D4 / 4)
A4_target = sp.Rational(3, 8) - L + 2*L**2 - pi**2/24
assert sp.simplify(A4 - A4_target) == 0

print("Exact Barnes derivatives:")
print("  (1/i) T_hhh       =", H3)
print("  (1/i) T_rrh       =", R2H)
print("  F_rr               =", Frr)
print("Derived expectations:")
print("  E[R2]              =", E_R2)
print("  E[t q R2]          =", Q)
print("  K=E[t D D']        =", K)
print("  A=E_p[D^2 q^2]     =", A)
print("  A4                  =", A4)

mp.mp.dps = 60
mpi = mp.pi
psi0 = mp.digamma(mp.mpf("0.5"))


def mu(t):
    return (mpi/2) / mp.cosh(mpi*t)**2


def p(t):
    if t == 0:
        return 4/mpi
    return 8*t/mp.sinh(2*mpi*t)


def D(t):
    return mp.re(mp.digamma(mp.mpf("0.5") + 1j*t)) - psi0


def Dp(t):
    return mp.re(1j * mp.polygamma(1, mp.mpf("0.5") + 1j*t))


def q(t):
    return (mpi/2)*mp.tanh(mpi*t)


K_num = 2*mp.quad(lambda x: mu(x)*x*D(x)*Dp(x), [0, mp.inf])
A_num = 2*mp.quad(lambda x: p(x)*D(x)**2*q(x)**2, [0, mp.inf])
ED4_num = 2*mp.quad(lambda x: p(x)*D(x)**4, [0, mp.inf])
A4_num = ED4_num/4

K_mp = mp.log(2) - mp.mpf(3)/4 + mpi**2/24
A_mp = mp.mpf(1)/2 - 2*mp.log(2) + 4*mp.log(2)**2
A4_mp = mp.mpf(3)/8 - mp.log(2) + 2*mp.log(2)**2 - mpi**2/24

for name, got, target in [
    ("K", K_num, K_mp),
    ("A", A_num, A_mp),
    ("A4", A4_num, A4_mp),
]:
    err = abs(got-target)
    print(f"{name} numerical error =", mp.nstr(err, 8))
    assert err < mp.mpf("1e-45")

print("PASS: exact Barnes t-generator closes K, A, and A4; quadrature agrees.")
