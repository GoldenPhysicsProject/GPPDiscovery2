"""Numerical audit of the universal D=8-2eps massless scalar-box residue.

Euclidean chamber: S,T > 0 and
    Q = S*x1*x3 + T*x2*x4
on the barycentric simplex x_i >= 0, sum x_i = 1.
With the standard Feynman-parametric normalization,
    I4^(8-2eps) = Gamma(eps) * J_eps,
    J_eps = integral_{Delta_3} Q^(-eps) dx.
Hence eps*I4 -> 1/6 if J_eps -> Vol(Delta_3)=1/6.

This script is discovery verification only; the proof target is dominated convergence.
"""

from __future__ import annotations

import math
from scipy.integrate import nquad
from scipy.special import gamma


def parameter_integral(eps: float, S: float, T: float) -> tuple[float, float]:
    assert 0.0 <= eps < 1.0
    assert S > 0.0 and T > 0.0

    # Stick-breaking coordinates map [0,1]^3 to the barycentric 3-simplex.
    # Jacobian = (1-y1)^2 (1-y2).
    def f(y3: float, y2: float, y1: float) -> float:
        x1 = y1
        x2 = (1.0 - y1) * y2
        x3 = (1.0 - y1) * (1.0 - y2) * y3
        x4 = (1.0 - y1) * (1.0 - y2) * (1.0 - y3)
        jac = (1.0 - y1) ** 2 * (1.0 - y2)
        q = S * x1 * x3 + T * x2 * x4
        if eps == 0.0:
            return jac
        return jac * q ** (-eps)

    return nquad(
        f,
        [[0.0, 1.0], [0.0, 1.0], [0.0, 1.0]],
        opts={"epsabs": 2e-7, "epsrel": 2e-7},
    )


def audit() -> None:
    target = 1.0 / 6.0
    chambers = [(1.0, 1.0), (2.0, 3.0), (0.7, 4.2)]
    epsilons = [0.1, 0.05, 0.02]

    print("target residue =", target)
    for S, T in chambers:
        print(f"\nS={S:g}, T={T:g}")
        j0, err0 = parameter_integral(0.0, S, T)
        print(f"eps=0      J={j0:.12f}  |J-1/6|={abs(j0-target):.3e}  quaderr={err0:.2e}")
        for eps in epsilons:
            j, err = parameter_integral(eps, S, T)
            residue_est = eps * gamma(eps) * j
            print(
                f"eps={eps:<5g} J={j:.12f}  eps*Gamma(eps)*J={residue_est:.12f}  "
                f"error={abs(residue_est-target):.3e}  quaderr={err:.2e}"
            )

    # Exact domination used by the rigorous route: for 0 < eps <= a < 1,
    # Q^(-eps) <= 1 + S^(-a) x1^(-a) x3^(-a).
    # Its simplex integral is finite and known by the Dirichlet formula:
    # Gamma(1-a)^2 / Gamma(4-2a).  At a=1/2 this is pi/2.
    a = 0.5
    dirichlet_majorant_piece = gamma(1.0 - a) ** 2 / gamma(4.0 - 2.0 * a)
    assert abs(dirichlet_majorant_piece - math.pi / 2.0) < 1e-12
    print("\nDirichlet majorant integral at a=1/2 =", dirichlet_majorant_piece)


if __name__ == "__main__":
    audit()
