"""Exploratory, NOT interval-certified, tests of zeta-zero prediction rules.

Reproduces the exact theta-lattice representation of the completed xi function,
compares finite-mode zero locations with Hardy-Z zeros, and compares those to a
gamma/phase-only prediction. Requires NumPy and SciPy.

Run: python zero_meta_rule_theta_probe.py
"""

from functools import lru_cache
from math import exp, pi

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, root
from scipy.special import loggamma, lambertw


def hardy_theta(t: float) -> float:
    return float(np.imag(loggamma(0.25 + 0.5j * t)) - 0.5 * t * np.log(pi))


def zeta_by_euler_eta(s: complex, terms: int = 110) -> complex:
    """Euler-transformed alternating eta series, independent of theta integral."""
    a = np.arange(1, terms + 1, dtype=np.float64) ** (-s)
    eta = 0j
    factor = 0.5
    for _ in range(terms):
        eta += factor * a[0]
        a = a[:-1] - a[1:]
        factor *= 0.5
    return eta / (1 - 2 ** (1 - s))


def hardy_z(t: float) -> float:
    v = np.exp(1j * hardy_theta(t)) * zeta_by_euler_eta(0.5 + 1j * t)
    # Im(v) is a useful independent numerical sanity check.
    if abs(v.imag) > 2e-7:
        raise ArithmeticError(f"Hardy Z imaginary residual too large at t={t}: {v.imag}")
    return float(v.real)


@lru_cache(maxsize=25000)
def lattice_mode(n: int, t: float) -> float:
    """I_n(t) = int_0^infinity exp(u/4-pi*n^2*exp(u)) cos(t*u/2) du."""
    if n < 1:
        raise ValueError("Mode labels are positive integers")
    f = lambda u: np.exp(u / 4 - pi * n * n * np.exp(u)) * np.cos(t * u / 2)
    return quad(f, 0, 6, epsabs=3e-16, epsrel=4e-14, limit=300)[0]


def xi_truncated(t: float, modes: int) -> float:
    return 0.5 - (t * t + 0.25) * sum(lattice_mode(n, t) for n in range(1, modes + 1))


def xi_from_eta(t: complex) -> complex:
    """Independent completed xi evaluator; s=1/2+i*t may be off critical."""
    s = 0.5 + 1j * t
    return (0.5 * s * (s - 1) *
            np.exp(-0.5 * s * np.log(pi) + loggamma(s / 2)) *
            zeta_by_euler_eta(s))


def xi_at_s(s: complex) -> complex:
    return xi_from_eta(-1j * (s - 0.5))


def shifted_xi_control(s: complex, delta: float = 0.25) -> complex:
    """Even/real entire false control: xi(s-delta) * xi(s+delta)."""
    return xi_at_s(s - delta) * xi_at_s(s + delta)


def lattice_mode_complex(n: int, t: complex) -> complex:
    f = lambda u: np.exp(u / 4 - pi * n * n * np.exp(u)) * np.cos(t * u / 2)
    return quad(f, 0, 6, epsabs=2e-16, epsrel=3e-14,
                complex_func=True, limit=300)[0]


def xi_deformed_eta(t: complex, alpha: float) -> complex:
    """Multiply only the n=2 theta mode by alpha; retain entire even symmetry."""
    return (xi_from_eta(t) - (alpha - 1) * (t * t + 0.25) *
            lattice_mode_complex(2, t))


def xi_deformed_theta(t: complex, alpha: float, modes: int = 4) -> complex:
    return (0.5 - (t * t + 0.25) *
            sum((alpha if n == 2 else 1) * lattice_mode_complex(n, t)
                for n in range(1, modes + 1)))


def xi_absolute_tail_bound(t: float, modes: int) -> float:
    """Rigorous analytic bound on truncation, not quadrature or zero position."""
    k = modes + 1
    return ((t * t + 0.25) * exp(-pi * k * k)
            / (pi * k * k * (1 - exp(-pi * (2 * modes + 3)))))


def smooth_gamma_zero(n: int) -> float:
    """Heuristic count midpoint: theta(t) / pi + 1 = n - 1/2."""
    return brentq(lambda t: hardy_theta(t) - (n - 1.5) * pi, 12, 110)


def lambert_zero(n: int) -> float:
    """Stirling approximation to the same midpoint rule (Lambert-W inversion)."""
    a = n - 11 / 8
    return float((2 * pi * a / lambertw(a / np.e)).real)


def sign_change_roots(f, lo: float, hi: float, step: float) -> list[float]:
    grid = np.arange(lo, hi + step / 2, step)
    values = [f(float(t)) for t in grid]
    result = []
    for a, b, ya, yb in zip(grid[:-1], grid[1:], values[:-1], values[1:]):
        if ya * yb < 0:
            result.append(brentq(f, float(a), float(b), xtol=3e-13))
    return result


def main():
    print("Reference Hardy-Z roots, computed independently from Euler-transformed eta:")
    truth = sign_change_roots(hardy_z, 12, 35, 0.25)
    for n, t in enumerate(truth, 1):
        phase = smooth_gamma_zero(n)
        lam = lambert_zero(n)
        print(f"{n} gamma={phase:.9f} LambertW={lam:.9f} "
              f"true={t:.12f} gamma_error={phase-t:+.6f}")

    print("\nTheta-lattice truncated roots (blind 12..35 search):")
    for modes in (1, 2, 3, 4):
        roots = sign_change_roots(lambda t: xi_truncated(t, modes), 12, 35, 0.25)
        differences = [min((abs(r - t) for r in roots), default=float('nan'))
                       for t in truth]
        print(f"modes=1..{modes} count={len(roots)} "
              f"roots={[round(x, 9) for x in roots]}")
        print(f"  nearest-root errors={[round(x, 9) for x in differences]}")

    if truth:
        first = truth[0]
        print("\nFirst-zero tail error bounds (function values only, rigorous exact form):")
        for modes in (1, 2, 3, 4):
            print(f"modes=1..{modes} |Xi-Xi_m|<={xi_absolute_tail_bound(first,modes):.4e}; "
                  f"Xi_m(gamma_1)={xi_truncated(first,modes):+.4e}")

    print("\nAdversarial arithmetic-weight experiment:")
    for alpha in (1.0, 1.00007, 1.00008, 1.0001):
        f = lambda t: (xi_truncated(t, 3) - (alpha - 1) *
                       (t * t + 0.25) * lattice_mode(2, t))
        roots = sign_change_roots(f, 12, 35, 0.025)
        print(f"alpha={alpha:.8f}: {len(roots)} real sign-changing roots in (12,35)")

    # At a double real zero both xi_alpha and its first derivative vanish.
    # Eliminate alpha via alpha(t)=1+xi(t)/((t^2+1/4)I_2(t)).
    def alpha_at_zero(t):
        return float(1 + xi_from_eta(t).real /
                     ((t * t + 0.25) * lattice_mode(2, t)))

    h = 0.0001
    def alpha_derivative(t):
        return (alpha_at_zero(t + h) - alpha_at_zero(t - h)) / (2 * h)

    collision_t = brentq(alpha_derivative, 31.1, 31.6)
    critical_alpha = alpha_at_zero(collision_t)
    print(f"two-real-zero collision: t*={collision_t:.10f}, "
          f"alpha*={critical_alpha:.12f} (numerical)")

    alpha = 1.00008
    def residual(v):
        z = xi_deformed_eta(complex(v[0], v[1]), alpha)
        return [z.real, z.imag]
    solution = root(residual, [31.19, 0.3], tol=1e-11)
    t_complex = complex(*solution.x)
    s_complex = 0.5 + 1j * t_complex
    residual_eta = abs(xi_deformed_eta(t_complex, alpha))
    residual_theta = abs(xi_deformed_theta(t_complex, alpha))
    print(f"alpha={alpha:.8f} off-line zero: t={t_complex!s}, "
          f"s={s_complex!s}; eta residual={residual_eta:.3e}; "
          f"independent theta residual={residual_theta:.3e}")
    assert solution.success and residual_eta < 1e-12 and residual_theta < 1e-12
    assert 0 < s_complex.real < 1 and abs(s_complex.real - 0.5) > 0.2

    print("\nIndependent shifted-xi entire control (delta=1/4):")
    gamma_1 = truth[0]
    center = shifted_xi_control(0.5 + 1j * gamma_1)
    off_line = shifted_xi_control(0.25 + 1j * gamma_1)
    print(f"on the line at gamma_1: {center!s} (nonnegative, nonzero)")
    print(f"off the line at 1/4+i*gamma_1: {off_line!s} (zero residual)")
    assert center.real > 0 and abs(center.imag) < 1e-14 and abs(off_line) < 1e-12


if __name__ == "__main__":
    main()
