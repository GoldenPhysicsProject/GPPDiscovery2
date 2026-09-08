#!/usr/bin/env python3
"""Exact/numerical audit for the odd-lattice -> tanh -> sech^2 bridge.

Codex/GPT discovery artifact.  This does not claim a Lean proof.

The analytic chain is

  sum_{k in Z} 1/((k*pi)^2+t^2) = coth(t)/t,

whose even-sublattice subtraction gives the odd lattice

  sum_{k odd} 1/((k*pi)^2+t^2)
    = [coth(t) - (1/2)coth(t/2)]/t
    = tanh(t/2)/(2t).

Taking half of the symmetric odd lattice therefore yields

  sum_{n>=0} 1/(((2n+1)*pi)^2+t^2) = tanh(t/2)/(4t),

and hence

  integral_0^inf sin(t x)/sinh(pi x) dx = (1/2)tanh(t/2).

Differentiating the last identity gives the spectral Fourier transform

  integral_R [pi*x/sinh(pi*x)] exp(i t x) dx
      = (pi/2) sech^2(t/2).

Thus for the normalized c=1 chamber density

  rho_1(x) = (2/pi) P(x),  P(x)=pi*x/sinh(pi*x),

its characteristic function is exactly sech^2(t/2), matching the
Gamma/chamber characteristic function at c=1.
"""

from __future__ import annotations

import mpmath as mp
import sympy as sp


mp.mp.dps = 80


def symbolic_hyperbolic_identity() -> None:
    t = sp.symbols("t", real=True, nonzero=True)
    lhs = sp.coth(t) - sp.Rational(1, 2) * sp.coth(t / 2)
    rhs = sp.Rational(1, 2) * sp.tanh(t / 2)
    # SymPy does not always simplify this directly; exponential rewriting does.
    residual = sp.factor(sp.together((lhs - rhs).rewrite(sp.exp)))
    assert residual == 0


def odd_partial_sum(t: mp.mpf, n: int) -> mp.mpf:
    return mp.fsum(
        1 / (((2 * k + 1) * mp.pi) ** 2 + t**2)
        for k in range(n)
    )


def odd_series_closed(t: mp.mpf) -> mp.mpf:
    return mp.tanh(t / 2) / (4 * t)


def sine_over_sinh(t: mp.mpf) -> mp.mpf:
    return mp.quad(lambda x: mp.sin(t * x) / mp.sinh(mp.pi * x), [0, mp.inf])


def spectral_fourier_cos(t: mp.mpf) -> mp.mpf:
    # P(x)=pi*x/sinh(pi*x) is even, so the imaginary Fourier part vanishes.
    return 2 * mp.quad(
        lambda x: mp.pi * x * mp.cos(t * x) / mp.sinh(mp.pi * x),
        [0, mp.inf],
    )


def spectral_fourier_closed(t: mp.mpf) -> mp.mpf:
    return (mp.pi / 2) / mp.cosh(t / 2) ** 2


def rho1_characteristic(t: mp.mpf) -> mp.mpf:
    return (2 / mp.pi) * spectral_fourier_cos(t)


def run() -> None:
    symbolic_hyperbolic_identity()

    tests = [
        mp.mpf("0.2"),
        mp.mpf("0.7"),
        mp.mpf("1"),
        mp.mpf("2"),
        mp.mpf("-1.3"),
    ]

    for t in tests:
        # Series identity is even in t after division by t; avoid t=0 here.
        target_series = odd_series_closed(t)
        approx = odd_partial_sum(t, 100000)
        assert abs(approx - target_series) < mp.mpf("3e-7")

        I = sine_over_sinh(t)
        I_target = mp.mpf("0.5") * mp.tanh(t / 2)
        assert mp.almosteq(I, I_target, rel_eps=mp.mpf("1e-60"), abs_eps=mp.mpf("1e-60"))

        F = spectral_fourier_cos(t)
        F_target = spectral_fourier_closed(t)
        assert mp.almosteq(F, F_target, rel_eps=mp.mpf("1e-60"), abs_eps=mp.mpf("1e-60"))

        chi = rho1_characteristic(t)
        chi_target = 1 / mp.cosh(t / 2) ** 2
        assert mp.almosteq(chi, chi_target, rel_eps=mp.mpf("1e-60"), abs_eps=mp.mpf("1e-60"))

    # t=0 normalization is the continuous limit of the Fourier identity.
    F0 = 2 * mp.quad(lambda x: mp.pi * x / mp.sinh(mp.pi * x), [0, mp.inf])
    assert mp.almosteq(F0, mp.pi / 2, rel_eps=mp.mpf("1e-60"), abs_eps=mp.mpf("1e-60"))
    assert mp.almosteq((2 / mp.pi) * F0, 1, rel_eps=mp.mpf("1e-60"), abs_eps=mp.mpf("1e-60"))

    print("PASS: odd-lattice hyperbolic identity")
    print("PASS: sine-over-sinh transform at 80-digit working precision")
    print("PASS: P(lambda) Fourier transform = (pi/2) sech^2(t/2)")
    print("PASS: rho_1 characteristic function = sech^2(t/2)")


if __name__ == "__main__":
    run()
