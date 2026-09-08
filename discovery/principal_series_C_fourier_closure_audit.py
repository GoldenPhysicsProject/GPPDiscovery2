#!/usr/bin/env python3
"""Analytic Fourier/chamber closure of C = E_p[(D')^2].

Codex/GPT discovery audit only. No Claude-owned material is used.

Definitions:

  p(t)   = 8 t / sinh(2*pi*t),
  D(t)   = Re psi(1/2+i t) - psi(1/2),
  phi(x) = x / (2 sinh(x/2)).

The digamma integral representation gives

  D'(t) = int_0^infty phi(x) sin(t x) dx.

The normalized p-law has characteristic function

  chi(s) = E_p[e^{i s t}] = sech^2(s/4).

Therefore Fubini and sin A sin B = (cos(A-B)-cos(A+B))/2 give

  C := E_p[(D')^2]
     = 1/2 int_0^infty int_0^infty
         phi(x) phi(y)
         [chi(x-y)-chi(x+y)] dx dy.

Put x=2u, y=2v. Then

  C = 2 int int u v/(sinh u sinh v)
      [sech^2((u-v)/2)-sech^2((u+v)/2)] du dv.

Use the exact hyperbolic identity

  sech^2((u-v)/2)-sech^2((u+v)/2)
    = sinh(u)sinh(v) /
      [cosh^2((u-v)/2) cosh^2((u+v)/2)].

The sinh factors cancel. With

  a=(u+v)/2, b=(u-v)/2,  du dv = 2 da db,

and domain a>=0, |b|<=a,

  C = 4 int_0^infty sech^2(a)
        int_{-a}^a (a^2-b^2) sech^2(b) db da
    = 8 int_{0<=b<=a<infty}
        (a^2-b^2) sech^2(a) sech^2(b) db da.

Now x=tanh(a), y=tanh(b). Since sech^2(a) da=dx,
sech^2(b) db=dy and 0<=y<=x<=1,

  C = 8 int_0^1 int_0^x
        [atanh(x)^2-atanh(y)^2] dy dx
    = 8 int_0^1 (2x-1) atanh(x)^2 dx.

The two elementary endpoint integrals are

  int_0^1 atanh(x)^2 dx
    = int_0^infty t^2 sech^2(t) dt
    = pi^2/12,

and

  int_0^1 x atanh(x)^2 dx
    = int_0^infty t^2 tanh(t) sech^2(t) dt
    = int_0^infty t sech^2(t) dt
    = log 2,

where the second equality follows by integration by parts using
(tanh t sech^2 t)=-(1/2)(sech^2 t)'. Hence

  C = 8(2 log 2 - pi^2/12)
    = 16 log 2 - 2 pi^2/3.

This converts the previously numerical/PSLQ value of C into an analytic
identity and leaves A = E_p[D^2 q^2] as the only independent mixed integral
in the current A4 reduction.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def p(t: mp.mpf) -> mp.mpf:
    return 4 / mp.pi if t == 0 else 8 * t / mp.sinh(2 * mp.pi * t)


def Dp(t: mp.mpf) -> mp.mpf:
    z = mp.mpf("0.5") + 1j * t
    return -mp.im(mp.polygamma(1, z))


def even_integral(weight, f):
    return 2 * mp.quad(lambda x: weight(x) * f(x), [0, 0.5, 1, 2, 4, mp.inf])


def main() -> None:
    x = sp.symbols("x", positive=True)
    target = 16 * sp.log(2) - 2 * sp.pi**2 / 3

    # Exact one-dimensional endpoint evaluation.
    I0 = sp.pi**2 / 12
    I1 = sp.log(2)
    reduced = sp.simplify(8 * (2 * I1 - I0))
    assert sp.simplify(reduced - target) == 0

    # Independent high-precision checks.
    mp.mp.dps = 70
    target_num = 16 * mp.log(2) - 2 * mp.pi**2 / 3

    C_direct = even_integral(p, lambda t: Dp(t) ** 2)
    C_artanh = 8 * mp.quad(lambda y: (2 * y - 1) * mp.atanh(y) ** 2,
                          [0, mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99"), 1])
    I0_num = mp.quad(lambda y: mp.atanh(y) ** 2,
                     [0, mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99"), 1])
    I1_num = mp.quad(lambda y: y * mp.atanh(y) ** 2,
                     [0, mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99"), 1])

    assert abs(C_direct - target_num) < mp.mpf("1e-50")
    assert abs(C_artanh - target_num) < mp.mpf("1e-50")
    assert abs(I0_num - mp.pi**2 / 12) < mp.mpf("1e-55")
    assert abs(I1_num - mp.log(2)) < mp.mpf("1e-55")

    print("Exact Fourier/chamber closure:")
    print("  int_0^1 atanh(x)^2 dx   = pi^2/12")
    print("  int_0^1 x atanh(x)^2 dx = log(2)")
    print("  C =", reduced)
    print("Independent direct E_p[(D')^2] =", mp.nstr(C_direct, 60))
    print("Reduced artanh integral          =", mp.nstr(C_artanh, 60))
    print("PASS: C = 16 log(2) - 2 pi^2/3 analytically")


if __name__ == "__main__":
    main()
