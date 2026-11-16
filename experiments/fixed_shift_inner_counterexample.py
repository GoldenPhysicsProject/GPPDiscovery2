"""Exact-geometry regression control for fixed-shift inner scattering.

No external packages and no zeta-zero input. Numerical grids illustrate,
but do not prove, the analytic assertions in the companion research note.
"""
from __future__ import annotations
import argparse
import json


def quartet_poly(z: complex, gamma: float, beta: float) -> complex:
    return ((z - gamma) ** 2 + beta ** 2) * ((z + gamma) ** 2 + beta ** 2)


def shifted_ratio(z: complex, gamma: float, beta: float, a: float) -> complex:
    return quartet_poly(z - 1j * a, gamma, beta) / quartet_poly(z + 1j * a, gamma, beta)


def finite_blaschke(z: complex, gamma: float, beta: float, a: float) -> complex:
    result = 1 + 0j
    for center in (-gamma, gamma):
        for height in (a - beta, a + beta):
            upper_root = center + 1j * height
            result *= (z - upper_root) / (z - upper_root.conjugate())
    return result


def check(gamma: float = 14.0, beta: float = 0.125, a: float = 0.25) -> dict:
    assert gamma > 0 and 0 < beta < a
    real_points = [-20, -gamma - 1, -gamma, -gamma + 1, 0,
                   gamma - 1, gamma, gamma + 1, 20]
    upper_points = [
        x + 1j * y
        for x in (-gamma, -gamma + .1, -2, 0, 2, gamma - .1, gamma)
        for y in (.02, .2, 1., 4.)
    ]
    errors = [
        abs(shifted_ratio(z, gamma, beta, a) - finite_blaschke(z, gamma, beta, a))
        for z in upper_points + list(map(complex, real_points))
    ]
    boundary_deviation = max(
        abs(abs(shifted_ratio(complex(x), gamma, beta, a)) - 1)
        for x in real_points
    )
    upper_max = max(abs(shifted_ratio(z, gamma, beta, a)) for z in upper_points)
    assert max(errors) < 1.e-8, max(errors)
    assert boundary_deviation < 1.e-11, boundary_deviation
    assert upper_max < 1, upper_max

    # A smaller shift creates an actual upper-half-plane pole.
    smaller_shift = beta / 2
    upper_pole = gamma + 1j * (beta - smaller_shift)
    pole_residual = abs(quartet_poly(upper_pole + 1j * smaller_shift, gamma, beta))
    assert pole_residual < 1.e-10, pole_residual
    return dict(
        gamma=gamma, off_line_distance=beta, fixed_shift=a,
        off_line_s_zeros=[
            f"{.5 + sign * beta:+.6f} {sgn * gamma:+.6f}i"
            for sign in (-1, 1) for sgn in (-1, 1)
        ],
        upper_half_plane_test_count=len(upper_points),
        boundary_modulus_deviation=boundary_deviation,
        upper_half_plane_max_modulus=upper_max,
        finite_blaschke_formula_max_residual=max(errors),
        smaller_shift=smaller_shift,
        upper_pole=[upper_pole.real, upper_pole.imag],
        denominator_zero_residual_at_pole=pole_residual
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gamma", type=float, default=14.)
    parser.add_argument("--beta", type=float, default=.125)
    parser.add_argument("--a", type=float, default=.25)
    args = parser.parse_args()
    print(json.dumps(check(args.gamma, args.beta, args.a), indent=2))
