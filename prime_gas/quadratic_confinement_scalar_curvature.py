"""Scalar-curvature audit for the quadratically confined number gas.

Weights
    p_n(beta, eta) \propto exp(-beta L_n - eta L_n^2),  L_n = log n,
with eta > 0.

For the Hessian potential phi = log Z, the Fisher metric is

    g = Hess(phi) = Cov(L, L^2).

In two dimensions a Hessian metric has scalar curvature

    R = - det([[phi_11, phi_12, phi_22],
               [phi_111,phi_112,phi_122],
               [phi_112,phi_122,phi_222]]) / (2 det(g)^2).

Because beta and eta enter with minus signs in the Gibbs exponent, the third
potential derivatives are minus the joint third cumulants of the sufficient
statistics (L,L^2).

There is a stronger exact reduction specific to the parabola of sufficient
statistics (X,X^2).  If Z = X-E[X], m_k=E[Z^k],

    D = det g = m2*m4 - m3^2 - m2^3,

and H is the 4x4 centered Hankel moment matrix

    [[1,  0, m2, m3],
     [0, m2, m3, m4],
     [m2,m3, m4, m5],
     [m3,m4, m5, m6]],

then exact polynomial elimination gives

    det(curvature numerator matrix) = det(H) - D^2,

hence

    R = (D^2 - det(H)) / (2 D^2)
      = 1/2 * (1 - det(H)/D^2).

This identity is translation invariant: the mean of X cancels completely.
Since H is a moment Gram matrix, det(H)>=0, so every nondegenerate finite
truncation obeys the rigorous structural upper bound R<=1/2.  Negativity is the
strictly stronger condition det(H)>D^2; it is not implied by positivity alone.

This script evaluates the exact moment formula on finite truncations, checks the
Hankel reduction independently, and separately audits the curvature against a
finite-difference Levi-Civita/Ricci computation.

This is executable discovery evidence, not yet the countable differentiation
proof.  The finite-truncation algebraic identities are exact.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class CurvatureAudit:
    det_metric: float
    hankel_det: float
    scalar_curvature: float
    scalar_curvature_hankel: float
    scalar_curvature_fd: float
    hankel_relative_error: float
    fd_relative_error: float


def raw_moments(beta: float, eta: float, N: int = 200_000, max_degree: int = 6) -> np.ndarray:
    if eta <= 0:
        raise ValueError("eta must be positive")
    n = np.arange(1, N + 1, dtype=float)
    L = np.log(n)
    exponent = -beta * L - eta * L * L
    exponent -= np.max(exponent)
    w = np.exp(exponent)
    Z = np.sum(w)
    return np.array([np.sum(w * L**k) / Z for k in range(max_degree + 1)])


def central_moments_from_raw(m: np.ndarray, max_degree: int = 6) -> np.ndarray:
    mu = m[1]
    out = np.zeros(max_degree + 1)
    out[0] = 1.0
    for k in range(1, max_degree + 1):
        out[k] = sum(
            np.math.comb(k, j) * (-mu) ** (k - j) * m[j]
            for j in range(k + 1)
        )
    return out


def metric_from_raw(m: np.ndarray) -> np.ndarray:
    return np.array(
        [
            [m[2] - m[1] ** 2, m[3] - m[1] * m[2]],
            [m[3] - m[1] * m[2], m[4] - m[2] ** 2],
        ]
    )


def third_cumulant(m: np.ndarray, a: int, b: int, c: int) -> float:
    return (
        m[a + b + c]
        - m[a] * m[b + c]
        - m[b] * m[a + c]
        - m[c] * m[a + b]
        + 2.0 * m[a] * m[b] * m[c]
    )


def hankel_curvature_reduction(m: np.ndarray) -> tuple[float, float, float]:
    cm = central_moments_from_raw(m)
    m2, m3, m4, m5, m6 = cm[2], cm[3], cm[4], cm[5], cm[6]
    D = m2 * m4 - m3 * m3 - m2**3
    H = np.array(
        [
            [1.0, 0.0, m2, m3],
            [0.0, m2, m3, m4],
            [m2, m3, m4, m5],
            [m3, m4, m5, m6],
        ]
    )
    detH = float(np.linalg.det(H))
    if D <= 0.0:
        raise AssertionError("centered Fisher determinant is not positive")
    R = 0.5 * (1.0 - detH / (D * D))
    return D, detH, R


def scalar_curvature_moment_formula(beta: float, eta: float, N: int = 200_000) -> tuple[float, float, np.ndarray]:
    m = raw_moments(beta, eta, N=N)
    g = metric_from_raw(m)
    det_g = float(np.linalg.det(g))
    if det_g <= 0.0:
        raise AssertionError("finite Fisher metric is not positive definite")

    # phi_ijk = - cumulant(T_i,T_j,T_k), T_1=L, T_2=L^2.
    p111 = -third_cumulant(m, 1, 1, 1)
    p112 = -third_cumulant(m, 1, 1, 2)
    p122 = -third_cumulant(m, 1, 2, 2)
    p222 = -third_cumulant(m, 2, 2, 2)

    curvature_matrix = np.array(
        [
            [g[0, 0], g[0, 1], g[1, 1]],
            [p111, p112, p122],
            [p112, p122, p222],
        ]
    )
    det3 = float(np.linalg.det(curvature_matrix))
    R = -det3 / (2.0 * det_g * det_g)
    return det_g, R, m


def metric(beta: float, eta: float, N: int) -> np.ndarray:
    return metric_from_raw(raw_moments(beta, eta, N=N))


def christoffel(beta: float, eta: float, N: int, h: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    x = np.array([beta, eta], dtype=float)
    g = metric(*x, N)
    inv_g = np.linalg.inv(g)
    dg = []
    for k in range(2):
        xp = x.copy()
        xm = x.copy()
        xp[k] += h
        xm[k] -= h
        dg.append((metric(*xp, N) - metric(*xm, N)) / (2.0 * h))

    Gamma = np.zeros((2, 2, 2))
    for ell in range(2):
        for i in range(2):
            for j in range(2):
                Gamma[ell, i, j] = 0.5 * sum(
                    inv_g[ell, r] * (dg[i][r, j] + dg[j][r, i] - dg[r][i, j])
                    for r in range(2)
                )
    return Gamma, g, inv_g


def scalar_curvature_finite_difference(beta: float, eta: float, N: int = 200_000, h: float = 1.0e-4) -> float:
    x = np.array([beta, eta], dtype=float)
    Gamma, _g, inv_g = christoffel(beta, eta, N, h / 5.0)

    dGamma = np.zeros((2, 2, 2, 2))
    for k in range(2):
        xp = x.copy()
        xm = x.copy()
        xp[k] += h
        xm[k] -= h
        Gp, _, _ = christoffel(*xp, N, h / 5.0)
        Gm, _, _ = christoffel(*xm, N, h / 5.0)
        dGamma[k] = (Gp - Gm) / (2.0 * h)

    Ric = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            for k in range(2):
                Ric[i, j] += dGamma[k, k, i, j] - dGamma[j, k, i, k]
                for ell in range(2):
                    Ric[i, j] += (
                        Gamma[k, i, j] * Gamma[ell, k, ell]
                        - Gamma[ell, i, k] * Gamma[k, j, ell]
                    )
    return float(np.sum(inv_g * Ric.T))


def audit(beta: float, eta: float, N: int = 200_000) -> CurvatureAudit:
    det_g, R, m = scalar_curvature_moment_formula(beta, eta, N=N)
    D, detH, R_hankel = hankel_curvature_reduction(m)
    if abs(D - det_g) > 1.0e-9 * max(1.0, abs(D), abs(det_g)):
        raise AssertionError("centered determinant does not match Fisher determinant")
    R_fd = scalar_curvature_finite_difference(beta, eta, N=N)
    scale_h = max(1.0, abs(R), abs(R_hankel))
    scale_fd = max(1.0, abs(R), abs(R_fd))
    herr = abs(R - R_hankel) / scale_h
    ferr = abs(R - R_fd) / scale_fd
    return CurvatureAudit(det_g, detH, R, R_hankel, R_fd, herr, ferr)


def main() -> None:
    samples = [(2.0, 0.5), (0.0, 0.5), (-2.0, 0.5), (2.0, 1.0), (2.0, 0.2)]
    for beta, eta in samples:
        a = audit(beta, eta)
        print(
            f"beta={beta: .3f} eta={eta: .3f} detg={a.det_metric:.12g} "
            f"detH={a.hankel_det:.12g} R={a.scalar_curvature:.12g} "
            f"R_h={a.scalar_curvature_hankel:.12g} R_fd={a.scalar_curvature_fd:.12g} "
            f"herr={a.hankel_relative_error:.3e} ferr={a.fd_relative_error:.3e}"
        )
        if a.hankel_relative_error > 2.0e-10:
            raise AssertionError("Hankel reduction disagrees with curvature determinant")
        if a.fd_relative_error > 2.0e-4:
            raise AssertionError("moment curvature formula disagrees with independent Ricci audit")
        if a.scalar_curvature > 0.5 + 1.0e-10:
            raise AssertionError("moment-Gram upper bound R <= 1/2 violated")


if __name__ == "__main__":
    main()
