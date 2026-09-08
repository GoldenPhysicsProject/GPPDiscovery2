#!/usr/bin/env python3
"""Prime/number-gas radial entropy monotonicity and Fisher fluctuation audit.

Codex/GPT discovery audit only. No Claude-owned material is used.

For the two-parameter number gas

  Z(beta, eta) = sum_{n>=2} exp[-beta X_n - eta X_n^2],
  X_n = log n,

let p_n = Z^{-1} exp[-beta X_n - eta X_n^2].  The Shannon entropy is

  S(beta,eta) = -sum p_n log p_n
              = log Z + beta E[X] + eta E[X^2].

Fix a nonzero natural-parameter vector v=(beta,eta), and scale it by tau>0:

  Z_tau = sum exp[-tau Y_n],
  Y_n = beta X_n + eta X_n^2.

Then

  d/dtau log Z_tau = -E_tau[Y],
  d/dtau E_tau[Y]  = -Var_tau(Y),

so

  S_tau = log Z_tau + tau E_tau[Y]
  dS_tau/dtau = -tau Var_tau(Y).

For beta>1 and eta>=0, Y_n is nonconstant on n>=2, hence

  dS_tau/dtau < 0  for every tau>0 for which the partition sum converges.

At tau=1 this is the exact radial identity

  beta * partial_beta S + eta * partial_eta S
    = -Var(beta X + eta X^2) < 0.

The Hessian of log Z is the Fisher covariance matrix of (X,X^2), so the same
quantity is its radial quadratic form:

  v^T g v = Var(beta X + eta X^2) > 0.

Thus the generalized radial heat-capacity/fluctuation quantity

  C_rad(tau) := tau^2 Var_tau(Y)

is strictly positive and

  dS_tau/d(log tau) = -C_rad(tau).

This gives an exact thermodynamic link among entropy, free energy/Massieu
response, and fluctuation geometry.  It is independent of the separate scalar
curvature-sign question; it does NOT imply R<=0.
"""
from __future__ import annotations

import math
import numpy as np


def stats(beta: float, eta: float, tau: float, N: int = 250_000):
    n = np.arange(2, N + 1, dtype=np.float64)
    x = np.log(n)
    y = beta * x + eta * x * x
    logw = -tau * y
    shift = float(np.max(logw))
    w = np.exp(logw - shift)
    norm = float(np.sum(w))
    p = w / norm
    Ey = float(np.sum(p * y))
    var_y = float(np.sum(p * (y - Ey) ** 2))
    logZ = math.log(norm) + shift
    S = logZ + tau * Ey

    EX = float(np.sum(p * x))
    EX2 = float(np.sum(p * x * x))
    c11 = float(np.sum(p * (x - EX) ** 2))
    c12 = float(np.sum(p * (x - EX) * (x * x - EX2)))
    c22 = float(np.sum(p * (x * x - EX2) ** 2))
    radial = beta * beta * c11 + 2 * beta * eta * c12 + eta * eta * c22
    return S, var_y, radial


def main() -> None:
    cases = [
        (2.0, 0.10, 0.8),
        (2.0, 0.10, 1.0),
        (2.0, 0.10, 1.3),
        (1.4, 0.02, 1.0),
        (3.0, 0.70, 1.0),
    ]

    for beta, eta, tau in cases:
        S, var_y, radial = stats(beta, eta, tau)
        assert var_y > 0.0
        assert abs(var_y - radial) < 2e-10 * max(1.0, var_y)

        # Finite-difference check of dS/dtau = -tau Var(Y).
        h = 2e-5
        Sp = stats(beta, eta, tau + h)[0]
        Sm = stats(beta, eta, tau - h)[0]
        dS_num = (Sp - Sm) / (2 * h)
        dS_exact = -tau * var_y
        rel = abs(dS_num - dS_exact) / max(1.0, abs(dS_exact))
        assert rel < 3e-6

        C_rad = tau * tau * var_y
        assert C_rad > 0.0
        print(
            f"beta={beta:.3f} eta={eta:.3f} tau={tau:.3f}  "
            f"S={S:.12g} Var(Y)={var_y:.12g} "
            f"dS/dtau={dS_exact:.12g} C_rad={C_rad:.12g}"
        )

    print("PASS: radial Fisher form = Var(beta X + eta X^2) > 0")
    print("PASS: dS/dtau = -tau Var(Y) < 0")
    print("PASS: dS/d(log tau) = -tau^2 Var(Y) = -C_rad")
    print("Scope guard: no scalar-curvature sign claim is made")


if __name__ == "__main__":
    main()
