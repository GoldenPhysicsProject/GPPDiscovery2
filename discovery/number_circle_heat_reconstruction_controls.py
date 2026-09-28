#!/usr/bin/env python3
"""Numerical controls for the exact number-circle / prime-Fock heat reconstruction.

No Riemann-zero data are used.
"""

from __future__ import annotations

import json
import mpmath as mp


mp.mp.dps = 70


def theta(t):
    return mp.jtheta(3, 0, mp.e ** (-mp.pi * t))


def xi_direct(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def xi_heat(s):
    f = lambda t: (theta(t) - 1) * (t ** (s / 2) + t ** ((1 - s) / 2)) / t
    return mp.mpf("0.5") + mp.mpf("0.25") * s * (s - 1) * mp.quad(f, [1, mp.inf])


def heat_norm_sq(t):
    return (theta(t) - 1) / 2


def heat_eval_norm(t):
    return mp.sqrt(heat_norm_sq(t))


def mixed_Z(s, t):
    return mp.nsum(lambda n: n ** (-s) * mp.e ** (-mp.pi * n * n * t), [1, mp.inf])


samples = [
    mp.mpf("0.5"),
    mp.mpf("2.3"),
    mp.mpc("0.5", "5.0"),
    mp.mpc("0.7", "3.2"),
]
reconstruction = []
for s in samples:
    xd = xi_direct(s)
    xh = xi_heat(s)
    reconstruction.append(
        {
            "s": str(s),
            "xi_direct": [float(mp.re(xd)), float(mp.im(xd))],
            "xi_heat": [float(mp.re(xh)), float(mp.im(xh))],
            "abs_error": float(abs(xd - xh)),
        }
    )

theta_modular = []
for t in [mp.mpf("0.2"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("5")]:
    lhs = theta(t)
    rhs = t ** (-mp.mpf("0.5")) * theta(1 / t)
    theta_modular.append(
        {
            "t": float(t),
            "abs_error": float(abs(lhs - rhs)),
            "heat_eval_norm": float(heat_eval_norm(t)),
        }
    )

# Check partial_t Z(s,t) = -pi Z(s-2,t) by numerical differentiation.
flow = []
for s, t in [(mp.mpc("0.4", "2.0"), mp.mpf("0.3")), (mp.mpf("1.7"), mp.mpf("0.8"))]:
    lhs = mp.diff(lambda u: mixed_Z(s, u), t)
    rhs = -mp.pi * mixed_Z(s - 2, t)
    flow.append(
        {
            "s": str(s),
            "t": float(t),
            "abs_error": float(abs(lhs - rhs)),
        }
    )

print(
    json.dumps(
        {
            "uses_riemann_zero_data": False,
            "xi_reconstruction": reconstruction,
            "theta_modularity": theta_modular,
            "mixed_heat_shift_flow": flow,
        },
        indent=2,
    )
)
